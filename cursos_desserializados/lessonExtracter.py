import json
import re
from pathlib import Path

# Arquivo original do curso
arquivo_entrada = Path(__file__).parent / "cursoVSCODEtest.json"

# Pasta onde serão salvas as lições separadas
pasta_saida = Path(__file__).parent / "licoes_extraidas_vscode_test"
pasta_saida.mkdir(exist_ok=True)

# Carrega o JSON completo
with open(arquivo_entrada, "r", encoding="utf-8") as f:
    dados = json.load(f)

licoes = dados["course"]["lessons"]

# Ordena as lições pela posição original
licoes_ordenadas = sorted(
    licoes,
    key=lambda x: x.get("position", 0)
)


def limpar_nome_arquivo(texto):
    """
    Remove caracteres problemáticos para nome de arquivo.
    """
    texto = texto.strip()
    texto = re.sub(r'[\\/*?:"<>|]', "", texto)
    texto = re.sub(r"\s+", "_", texto)
    return texto[:80]


indice_licoes = []

for numero, licao in enumerate(licoes_ordenadas, start=1):
    titulo = licao.get("title", f"licao_{numero}")
    posicao = licao.get("position")

    nome_limpo = limpar_nome_arquivo(titulo)

    nome_arquivo = f"licao_{numero:02d}_{nome_limpo}.json"
    caminho_saida = pasta_saida / nome_arquivo

    # Estrutura do arquivo individual da lição
    conteudo_licao = {
        "numero_da_licao": numero,
        "position_original": posicao,
        "title": titulo,
        "lesson": licao
    }

    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(
            conteudo_licao,
            f,
            ensure_ascii=False,
            indent=2
        )

    indice_licoes.append({
        "numero_da_licao": numero,
        "position_original": posicao,
        "title": titulo,
        "arquivo": nome_arquivo
    })

# Salva um índice geral das lições extraídas
arquivo_indice = pasta_saida / "indice_licoes.json"

with open(arquivo_indice, "w", encoding="utf-8") as f:
    json.dump(
        indice_licoes,
        f,
        ensure_ascii=False,
        indent=2
    )

print("Lições extraídas com sucesso.")
print(f"Pasta gerada: {pasta_saida}")
print(f"Índice gerado: {arquivo_indice}")