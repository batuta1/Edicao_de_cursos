import json
import base64
from pathlib import Path

# ============================================================
# CAMINHOS
# ============================================================

pasta_base = Path(__file__).parent

arquivo_curso_original = pasta_base / "cursoClaudeCode.json"
pasta_licoes = pasta_base / "licoes_extraidas_ClaudeCode_test"

arquivo_curso_editado = pasta_base / "cursoClaudeCode_editado.json"
arquivo_base64_editado = pasta_base / "cursoClaudeCode_editado_base64.txt"

# Opcional: se você tiver o index.html original do curso
arquivo_html_original = pasta_base / "index.html"
arquivo_html_editado = pasta_base / "index_editado.html"


# ============================================================
# CARREGA O CURSO ORIGINAL COMO MOLDE
# ============================================================

with open(arquivo_curso_original, "r", encoding="utf-8-sig") as f:
    dados = json.load(f)


# ============================================================
# CARREGA AS LIÇÕES EDITADAS
# ============================================================

licoes_editadas = []

for arquivo_licao in sorted(pasta_licoes.glob("licao_*.json")):
    # Ignora arquivos auxiliares, se houver
    if arquivo_licao.name == "indice_licoes.json":
        continue

    with open(arquivo_licao, "r", encoding="utf-8-sig") as f:
        conteudo = json.load(f)

    # No seu caso, cada arquivo tem a estrutura:
    # {
    #   "numero_da_licao": ...,
    #   "position_original": ...,
    #   "title": ...,
    #   "lesson": {...}
    # }

    if "lesson" not in conteudo:
        raise ValueError(f"O arquivo {arquivo_licao.name} não possui a chave 'lesson'.")

    numero = conteudo.get("numero_da_licao")
    posicao = conteudo.get("position_original")
    licao = conteudo["lesson"]

    licoes_editadas.append({
        "numero_da_licao": numero,
        "position_original": posicao,
        "lesson": licao,
        "arquivo": arquivo_licao.name
    })


# Ordena pela numeração criada na extração
licoes_editadas = sorted(
    licoes_editadas,
    key=lambda x: x.get("numero_da_licao", 9999)
)

# Extrai apenas o objeto real da lição
novas_licoes = [item["lesson"] for item in licoes_editadas]


# ============================================================
# SUBSTITUI AS LIÇÕES NO CURSO ORIGINAL
# ============================================================

quantidade_original = len(dados["course"]["lessons"])
quantidade_editada = len(novas_licoes)

if quantidade_original != quantidade_editada:
    print("ATENÇÃO: a quantidade de lições mudou.")
    print(f"Lições no curso original: {quantidade_original}")
    print(f"Lições editadas encontradas: {quantidade_editada}")
    print("Verifique se isso foi intencional antes de importar na plataforma.")

dados["course"]["lessons"] = novas_licoes


# ============================================================
# SALVA O NOVO JSON DO CURSO
# ============================================================

with open(arquivo_curso_editado, "w", encoding="utf-8-sig") as f:
    json.dump(
        dados,
        f,
        ensure_ascii=False,
        indent=2
    )

print(f"Arquivo JSON editado gerado: {arquivo_curso_editado}")


# ============================================================
# SERIALIZA PARA BASE64
# ============================================================

json_compacto = json.dumps(
    dados,
    ensure_ascii=False,
    separators=(",", ":")
)

base64_editado = base64.b64encode(
    json_compacto.encode("utf-8")
).decode("utf-8")

with open(arquivo_base64_editado, "w", encoding="utf-8-sig") as f:
    f.write(base64_editado)

print(f"Arquivo Base64 gerado: {arquivo_base64_editado}")


# ============================================================
# OPCIONAL: SUBSTITUIR AUTOMATICAMENTE NO INDEX.HTML
# ============================================================

def corrigir_padding_base64(texto):
    return texto + "=" * (-len(texto) % 4)


def parece_base64_de_curso(trecho):
    try:
        trecho_corrigido = corrigir_padding_base64(trecho)
        json_texto = base64.b64decode(trecho_corrigido).decode("utf-8")
        obj = json.loads(json_texto)

        return (
            isinstance(obj, dict)
            and "course" in obj
            and isinstance(obj["course"], dict)
            and "lessons" in obj["course"]
        )
    except Exception:
        return False


if arquivo_html_original.exists():
    import re

    html = arquivo_html_original.read_text(encoding="utf-8")

    # Procura grandes blocos Base64 dentro do HTML
    candidatos = re.findall(r"[A-Za-z0-9+/=]{1000,}", html)

    base64_original_encontrado = None

    for candidato in candidatos:
        if parece_base64_de_curso(candidato):
            base64_original_encontrado = candidato
            break

    if base64_original_encontrado is None:
        print("Não encontrei automaticamente o Base64 do curso dentro do index.html.")
        print("Nesse caso, copie manualmente o conteúdo de cursoClaudeCode_editado_base64.txt para o local correto.")
    else:
        html_editado = html.replace(
            base64_original_encontrado,
            base64_editado,
            1
        )

        arquivo_html_editado.write_text(html_editado, encoding="utf-8")

        print(f"Arquivo HTML editado gerado: {arquivo_html_editado}")

else:
    print("Nenhum index.html encontrado na pasta. Apenas o JSON e o Base64 foram gerados.")