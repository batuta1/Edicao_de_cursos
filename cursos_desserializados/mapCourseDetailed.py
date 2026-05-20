import json
from pathlib import Path

arquivo = Path(__file__).parent / "cursoVSCODE.json"
arquivo_saida = Path(__file__).parent / "mapa_detalhado_curso.txt"

with open(arquivo, "r", encoding="utf-8") as f:
    dados = json.load(f)

licoes = dados["course"]["lessons"]
licoes_ordenadas = sorted(licoes, key=lambda x: x.get("position", 0))

linhas = []


def resumir_texto(valor, limite=120):
    if not isinstance(valor, str):
        return ""
    valor = " ".join(valor.split())
    if len(valor) > limite:
        return valor[:limite] + "..."
    return valor


def adicionar_linha(texto=""):
    linhas.append(str(texto))


def percorrer(obj, caminho, numero_licao, titulo_licao):
    if isinstance(obj, dict):
        tipo = obj.get("type", None)

        if "type" in obj:
            adicionar_linha("=" * 80)
            adicionar_linha(f"Lição {numero_licao}: {titulo_licao}")
            adicionar_linha(f"Caminho: {caminho}")
            adicionar_linha(f"Type: {repr(tipo)}")

            for campo in [
                "title",
                "heading",
                "description",
                "text",
                "question",
                "answer",
                "feedback"
            ]:
                if campo in obj:
                    adicionar_linha(
                        f"{campo}: {resumir_texto(obj.get(campo))}"
                    )

            adicionar_linha("")

        for chave, valor in obj.items():
            percorrer(
                valor,
                f"{caminho}.{chave}",
                numero_licao,
                titulo_licao
            )

    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            percorrer(
                item,
                f"{caminho}[{i}]",
                numero_licao,
                titulo_licao
            )


for i, licao in enumerate(licoes_ordenadas, start=1):
    titulo = licao.get("title", "Sem título")
    percorrer(
        licao,
        f"course.lessons[{i-1}]",
        i,
        titulo
    )

with open(arquivo_saida, "w", encoding="utf-8") as f:
    f.write("\n".join(linhas))

print(f"Arquivo gerado com sucesso: {arquivo_saida}")