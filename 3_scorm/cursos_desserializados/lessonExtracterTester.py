import json
import base64
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO
# ============================================================

pasta_base = Path(__file__).parent

arquivo_curso_original = pasta_base / "cursoVSCODEtest.json"
pasta_licoes = pasta_base / "licoes_extraidas_vscode_test"

arquivo_curso_editado = pasta_base / "cursoVSCODEtest_editado.json"
arquivo_base64_editado = pasta_base / "cursoVSCODEtest_editado_base64.txt"

frase_teste = "OI EU EDITEI"


# ============================================================
# FUNÇÃO PARA PROCURAR TEXTO
# ============================================================

def procurar_texto(obj, texto):
    if isinstance(obj, dict):
        return any(procurar_texto(v, texto) for v in obj.values())

    if isinstance(obj, list):
        return any(procurar_texto(item, texto) for item in obj)

    if isinstance(obj, str):
        return texto in obj

    return False


# ============================================================
# MOSTRA OS CAMINHOS ABSOLUTOS
# ============================================================

print("Pasta base usada pelo script:")
print(pasta_base)
print()

print("Arquivo original:")
print(arquivo_curso_original)
print()

print("Pasta das lições:")
print(pasta_licoes)
print()

print("Arquivo JSON editado que será gerado:")
print(arquivo_curso_editado)
print()


# ============================================================
# CARREGA O CURSO ORIGINAL
# ============================================================

with open(arquivo_curso_original, "r", encoding="utf-8") as f:
    dados = json.load(f)


# ============================================================
# CARREGA AS LIÇÕES EDITADAS
# ============================================================

licoes_editadas = []

for arquivo_licao in sorted(pasta_licoes.glob("licao_*.json")):
    with open(arquivo_licao, "r", encoding="utf-8") as f:
        conteudo = json.load(f)

    if "lesson" not in conteudo:
        print(f"Ignorando arquivo sem chave 'lesson': {arquivo_licao.name}")
        continue

    numero = conteudo.get("numero_da_licao")
    posicao = conteudo.get("position_original")
    licao = conteudo["lesson"]

    if procurar_texto(licao, frase_teste):
        print("Frase de teste encontrada na lição carregada:")
        print(f"Arquivo: {arquivo_licao.name}")
        print(f"Número da lição: {numero}")
        print(f"Título: {licao.get('title')}")
        print()

    licoes_editadas.append({
        "numero_da_licao": numero,
        "position_original": posicao,
        "lesson": licao,
        "arquivo": arquivo_licao.name
    })


licoes_editadas = sorted(
    licoes_editadas,
    key=lambda x: x.get("numero_da_licao", 9999)
)

novas_licoes = [item["lesson"] for item in licoes_editadas]


# ============================================================
# SUBSTITUI AS LIÇÕES NO CURSO ORIGINAL
# ============================================================

print(f"Quantidade de lições no curso original: {len(dados['course']['lessons'])}")
print(f"Quantidade de lições editadas carregadas: {len(novas_licoes)}")
print()

dados["course"]["lessons"] = novas_licoes


# ============================================================
# VERIFICA ANTES DE SALVAR
# ============================================================

if procurar_texto(dados, frase_teste):
    print("OK: a frase de teste está dentro do objeto final antes de salvar.")
else:
    print("ERRO: a frase de teste NÃO está dentro do objeto final antes de salvar.")


# ============================================================
# SALVA O JSON EDITADO
# ============================================================

with open(arquivo_curso_editado, "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)


# ============================================================
# REABRE O JSON SALVO E CONFERE
# ============================================================

with open(arquivo_curso_editado, "r", encoding="utf-8") as f:
    dados_salvos = json.load(f)

if procurar_texto(dados_salvos, frase_teste):
    print("OK: a frase de teste apareceu no cursoVSCODE_editado.json salvo.")
else:
    print("ERRO: a frase de teste NÃO apareceu no cursoVSCODE_editado.json salvo.")


# ============================================================
# SERIALIZA PARA BASE64
# ============================================================

json_compacto = json.dumps(
    dados_salvos,
    ensure_ascii=False,
    separators=(",", ":")
)

base64_editado = base64.b64encode(
    json_compacto.encode("utf-8")
).decode("utf-8")

with open(arquivo_base64_editado, "w", encoding="utf-8") as f:
    f.write(base64_editado)

print()
print("Arquivos gerados:")
print(arquivo_curso_editado)
print(arquivo_base64_editado)