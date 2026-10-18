"""Aplica as edições de edicoes.py nos licao_*.json, campo a campo.

Cada edição é (licao, bloco, caminho, texto). bloco=None aponta para a própria lição.
O caminho parte do bloco (ex.: 'items[0].paragraph', 'answers[2].feedback').
Confere que o caminho existe e já é texto antes de trocar; nunca cria chave.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))
from edicoes import EDICOES  # noqa: E402

CAMPOS_TEXTO = {'paragraph', 'description', 'heading', 'title', 'feedback'}

pasta = Path(sys.argv[1])
arquivos = {int(p.name[6:8]): p for p in pasta.glob("licao_*.json")}
dados = {n: json.loads(p.read_text(encoding="utf-8")) for n, p in arquivos.items()}

TOKEN = re.compile(r"([^.\[\]]+)|\[(\d+)\]")


def resolver(raiz, caminho):
    partes = [(m.group(1), m.group(2)) for m in TOKEN.finditer(caminho)]
    obj = raiz
    for chave, idx in partes[:-1]:
        obj = obj[chave] if chave is not None else obj[int(idx)]
    chave, idx = partes[-1]
    if chave is None or chave not in obj:
        raise KeyError(f"campo final inexistente: {caminho}")
    return obj, chave


aplicadas, iguais, vistos = 0, 0, set()
for licao, bloco, caminho, texto in EDICOES:
    chave_unica = (licao, bloco, caminho)
    if chave_unica in vistos:
        raise SystemExit(f"Edição duplicada: {chave_unica}")
    vistos.add(chave_unica)
    lesson = dados[licao]["lesson"]
    raiz = lesson if bloco is None else lesson["items"][bloco]
    obj, chave = resolver(raiz, caminho)
    if chave not in CAMPOS_TEXTO:
        raise SystemExit(f"Campo não textual: {licao}/{bloco}/{caminho}")
    if not isinstance(obj[chave], str):
        raise SystemExit(f"Valor não é texto: {licao}/{bloco}/{caminho}")
    if obj[chave] == texto:
        iguais += 1
        print(f"  (igual ao original, ignorada) {licao}/{bloco}/{caminho}")
        continue
    obj[chave] = texto
    aplicadas += 1

for n, p in arquivos.items():
    p.write_text(json.dumps(dados[n], ensure_ascii=False, indent=2), encoding="utf-8")

por_licao = {}
for licao, *_ in EDICOES:
    por_licao[licao] = por_licao.get(licao, 0) + 1
print(f"Edições aplicadas: {aplicadas} (ignoradas por serem iguais: {iguais})")
print("Por lição:", dict(sorted(por_licao.items())))
