"""O `autor.json` de cada versão de curso: ler e escrever. Usado pelo extrator (que só lê) e pela automação (que preenche).

Formato: `Cursos/<Empresa>/<curso>/scorm/vN/autor.json` com `{"autor": "Nome"}` ou `{"autor": null}`.
Fica em `comum/` para uma parte não precisar importar da outra.
"""
import json
from pathlib import Path

NOME_DO_ARQUIVO = "autor.json"


def pasta_da_versao(raiz, empresa, curso, versao):
    """Pasta de uma versão de curso: `<raiz>/<empresa>/<curso>/scorm/<versao>`."""
    return Path(raiz) / empresa / curso / "scorm" / versao


def ler_declaracao(pasta):
    """(autor, existe, problema) do `autor.json` de uma pasta de versão. Arquivo estragado não derruba nada: vira `problema`."""
    arquivo = Path(pasta) / NOME_DO_ARQUIVO
    if not arquivo.is_file():
        return None, False, None
    try:
        dados = json.loads(arquivo.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return None, True, f"não consegui ler: {e}"
    if not isinstance(dados, dict) or "autor" not in dados:
        return None, True, 'o arquivo precisa ser {"autor": "Nome"} (ou {"autor": null})'
    autor = dados["autor"]
    if autor is None:
        return None, True, None
    if isinstance(autor, str) and autor.strip():
        return autor.strip(), True, None
    return None, True, "«autor» precisa ser um nome (texto) ou null"


def escrever(pasta, autor):
    """Grava `{"autor": autor}` (ou `null`) em `<pasta>/autor.json`, criando a pasta se preciso. Quem chama decide se pode sobrescrever."""
    pasta = Path(pasta)
    pasta.mkdir(parents=True, exist_ok=True)
    (pasta / NOME_DO_ARQUIVO).write_text(json.dumps({"autor": autor}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
