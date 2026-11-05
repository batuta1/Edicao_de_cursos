"""Edições de texto em campos (curso Vibe Coding) que validar_estrutura.py e validar.py não cobrem:
course.description (capa) e completeHint de todos os Continues (aviso em inglês -> português).

Uso: python -I pos_edicoes.py essentials|hands-on ENTRADA.json SAIDA.json
Depois de editar, compara ENTRADA x SAIDA folha a folha e falha se mudou qualquer coisa fora desses campos.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
qual, ent, sai = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
if sai.exists():
    raise SystemExit(f"{sai} já existe; escolha outro nome.")

CAPAS = {
    "essentials": ("Ever imagined creating",
        "Como construir um aplicativo web descrevendo-o em português — e saber se ele é seguro antes de abri-lo ao "
        "público? Pensado para não programadores, empreendedores e professores, este curso ensina vibe coding com o "
        "Lovable, no plano gratuito: especificar o aplicativo numa ficha de requisitos, avaliar dados, segredos e "
        "custos antes de construir, gerar a interface em camadas, acrescentar login e banco de dados com regras de "
        "acesso por usuário, comprovar com duas contas que cada pessoa vê só o que é seu, publicar e iterar. Ao final, "
        "você terá publicado o aplicativo “Minhas Tarefas” e aplicado o mesmo ciclo a um aplicativo do seu perfil."),
    "hands-on": ("Ever wanted to create",
        "Em menos de duas horas, você vai pôr no ar um app de verdade — com login, banco de dados e a prova de que "
        "cada pessoa só vê o que é dela —, construído conversando com a IA, sem escrever uma linha de código. São "
        "quatro oficinas e um projeto final no Lovable, no plano gratuito, para quem tem ideias de app mas não "
        "programa: da planta à tela, do login ao teste com duas contas, da publicação à primeira reforma."),
}
HINT_ANTIGO = "Complete the content above before moving on."
HINT_NOVO = "Conclua o conteúdo acima para continuar."

antes = json.loads(ent.read_text(encoding="utf-8"))
dados = json.loads(ent.read_text(encoding="utf-8"))
curso = dados["course"]
contagem = {"description": 0, "completeHint": 0}

inicio, capa = CAPAS[qual]
assert curso["description"].startswith(inicio), "capa inesperada"
curso["description"] = capa
contagem["description"] += 1

for licao in curso["lessons"]:
    for bloco in licao.get("items", []):
        if bloco.get("type") == "divider" and bloco.get("family") == "continue":
            for it in bloco["items"]:
                if it.get("completeHint") == HINT_ANTIGO:
                    it["completeHint"] = HINT_NOVO
                    contagem["completeHint"] += 1

PERMITIDOS = set(contagem)
mudancas, proibidas = [], []


def comparar(a, b, caminho):
    if isinstance(a, dict):
        if not isinstance(b, dict) or a.keys() != b.keys():
            proibidas.append(f"CHAVES/TIPO em {caminho}")
            return
        for k in a:
            comparar(a[k], b[k], f"{caminho}.{k}")
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b):
            proibidas.append(f"ARRAY em {caminho}")
            return
        for i, (x, y) in enumerate(zip(a, b)):
            comparar(x, y, f"{caminho}[{i}]")
    elif a != b:
        campo = caminho.rsplit(".", 1)[-1]
        (mudancas if campo in PERMITIDOS else proibidas).append(caminho)


comparar(antes, dados, "")
if proibidas:
    print("\n".join(proibidas))
    raise SystemExit("REPROVADO: mudou algo fora dos campos permitidos. Nada gravado.")
if contagem["description"] != 1 or contagem["completeHint"] < 1:
    raise SystemExit(f"REPROVADO: contagem inesperada {contagem}. Nada gravado.")
if len(mudancas) != sum(contagem.values()):
    raise SystemExit("REPROVADO: número de folhas alteradas não bate com as edições. Nada gravado.")

sai.write_text(json.dumps(dados, ensure_ascii=False), encoding="utf-8")
print("Edições:", contagem, "| folhas alteradas:", len(mudancas))
print("APROVADO: só mudaram description (capa) e completeHint.")
