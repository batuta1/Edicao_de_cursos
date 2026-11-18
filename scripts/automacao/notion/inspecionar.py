"""F4: lê o banco do Notion pela API, imprime colunas e tipos e grava `notion/config.json` (sem o token).

    uv run python -m automacao.notion.inspecionar [ID_OU_LINK]
"""
import os
import re
import sys

from .. import ambiente
from . import api


def id_do_link(texto):
    """Extrai os 32 caracteres do ID de um link do Notion; se não achar, devolve o próprio texto."""
    m = re.search(r"([0-9a-f]{32})(?:[?#]|$)", texto.replace("-", ""))
    return m.group(1) if m else texto


def main(argv=None):
    """Imprime a fonte de dados e as colunas (nome, tipo, opções) e grava `config.json`. Devolve 0 (ok) ou 1 (erro)."""
    argv = sys.argv[1:] if argv is None else argv
    ambiente.carregar()
    alvo = id_do_link(argv[0]) if argv else (os.environ.get("NOTION_DATA_SOURCE_ID") or os.environ.get("NOTION_DATABASE_ID") or api.PAGINA_PADRAO)
    try:
        cliente = api.Notion()
        banco = cliente.banco(alvo)
        print("Fonte de dados:", "".join(t["plain_text"] for t in banco.get("title", [])), banco["id"])
        for nome, p in banco["properties"].items():
            extra = ""
            if p["type"] in ("status", "select", "multi_select"):
                extra = " opções: " + ", ".join(o["name"] for o in p[p["type"]]["options"])
            elif p["type"] == "number":
                extra = f" formato: {p['number']['format']}"
            print(f"  - {nome} [{p['type']}]{extra}")
        mapa = api.mapear_colunas(banco["properties"])
        api.salvar_config(banco, mapa)
        print("config.json gravado; as 4 colunas foram encontradas.")
        return 0
    except api.ErroNotion as e:
        print("Erro:", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
