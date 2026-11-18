"""F5: um comando roda tudo, na ordem: checklist (joao → referencias → csv) → extrator → autores → Notion.

    uv run python -m automacao [--dry-run] [--sem-notion] [--sem-commit] [--sem-fetch]

Nunca faz push. Commits só dos arquivos do processo.
"""
import argparse
import os
import sys

from extrator_scorm.lote import lote, varredura

from . import ambiente, caminhos, git_seguro
from .autores import casar, preencher
from .checklist import buscar, leitura
from .notion import api, modelo, sincronizar


def _extrair(saida):
    """Roda o lote do extrator só nas últimas versões; grava Cursos/registro-de-cursos.json."""
    r = lote.executar(caminhos.CURSOS, ignorar=varredura.IGNORAR_PADRAO, so_ultimas=True, pasta_registro=caminhos.REGISTRO)
    saida(f"extrator: {r['encontrados']} pacotes · extraídos {r['extraidos']} · com erro {r['com_erro']}")
    return r


def executar(dry_run=False, notion=True, commit=True, fetch=True, saida=print):
    ambiente.carregar()
    commit = commit and not dry_run
    # 1. checklist
    if dry_run:
        csv_ = buscar.csv_atual()
        if csv_ is None:
            raise SystemExit("dry-run: não há csv em automacao/referencias/. Rode sem --dry-run uma vez (ou só --sem-commit).")
        saida(f"dry-run: usando {csv_.name} já existente")
    else:
        csv_ = buscar.sincronizar(fetch=fetch, commit=commit, saida=saida)["csv"]
    linhas = leitura.ler(csv_)
    # 2. extrator
    if not caminhos.CURSOS.is_dir():
        raise SystemExit(f"{caminhos.CURSOS} não existe nesta branch (Cursos/ está na main). Use EDICAO_RAIZ ou rode na main.")
    if not dry_run:
        _extrair(saida)
    # 3. autores
    registro = casar.carregar_registro(caminhos.REGISTRO)
    r = preencher.preencher(linhas, registro, dry_run=dry_run, saida=saida)
    if r["gravados"] and not dry_run:
        _extrair(saida)
    if commit:
        h = git_seguro.commitar_somente([*r["arquivos"], caminhos.REGISTRO], "update de autores e registro dos cursos")
        saida(f"autores: commit {h}" if h else "autores: nada a commitar")
    # 4. Notion
    itens = modelo.montar(linhas)
    if not notion:
        saida("notion: pulado (--sem-notion)")
    elif dry_run and not os.environ.get("NOTION_TOKEN"):
        saida("notion (dry-run sem NOTION_TOKEN): o que seria enviado:\n" + modelo.tabela(itens))
    else:
        sincronizar.sincronizar(itens, dry_run=dry_run, saida=saida)
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="python -m automacao", description=__doc__.split("\n")[0])
    p.add_argument("--dry-run", action="store_true", help="não grava nada, não commita, não escreve no Notion")
    p.add_argument("--sem-notion", action="store_true")
    p.add_argument("--sem-commit", action="store_true")
    p.add_argument("--sem-fetch", action="store_true", help="não roda git fetch antes de ler a branch joao")
    a = p.parse_args(argv)
    try:
        return executar(a.dry_run, not a.sem_notion, not a.sem_commit, not a.sem_fetch)
    except (git_seguro.ErroGit, api.ErroNotion, ValueError) as e:
        print("Erro:", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
