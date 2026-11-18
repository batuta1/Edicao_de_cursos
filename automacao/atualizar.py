"""F5: um comando roda tudo, na ordem: checklist (joao → referencias → csv) → extrator → autores → Notion.

    uv run python -m automacao [--so ETAPA ...] [--dry-run] [--sem-notion] [--sem-commit] [--sem-fetch]

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


ETAPAS = ("checklist", "extrator", "autores", "notion")


def executar(dry_run=False, notion=True, commit=True, fetch=True, etapas=ETAPAS, saida=print):
    """Roda as `etapas` pedidas, sempre na ordem checklist → extrator → autores → notion."""
    ambiente.carregar()
    commit = commit and not dry_run
    etapas = [e for e in ETAPAS if e in etapas and (notion or e != "notion")]
    if ("extrator" in etapas or "autores" in etapas) and not caminhos.CURSOS.is_dir():
        raise SystemExit(f"{caminhos.CURSOS} não existe nesta branch (Cursos/ está na main). Rode na main ou use EDICAO_RAIZ (veja documentacao/automacao-notion.md).")
    # 1. checklist (csv): as etapas autores e notion precisam dele, mesmo quando o checklist não foi pedido
    csv_ = None
    if "checklist" in etapas and not dry_run:
        csv_ = buscar.sincronizar(fetch=fetch, commit=commit, saida=saida)["csv"]
    elif "autores" in etapas or "notion" in etapas:
        csv_ = buscar.csv_atual()
        if csv_ is None:
            raise SystemExit("não há csv em automacao/referencias/. Rode antes: uv run python -m automacao --so checklist")
        saida(f"usando {csv_.name} (já existente)")
    linhas = leitura.ler(csv_) if csv_ else []
    # 2. extrator
    if "extrator" in etapas:
        if dry_run:
            saida("extrator: pulado no --dry-run (ele grava registro e fichas)")
        else:
            _extrair(saida)
    # 3. autores
    if "autores" in etapas:
        if not caminhos.REGISTRO.is_file():
            raise SystemExit("falta Cursos/registro-de-cursos.json. Rode antes: uv run python -m automacao --so extrator")
        r = preencher.preencher(linhas, casar.carregar_registro(caminhos.REGISTRO), dry_run=dry_run, saida=saida)
        if r["gravados"] and not dry_run:
            _extrair(saida)
        if commit:
            h = git_seguro.commitar_somente([*r["arquivos"], caminhos.REGISTRO], "update de autores e registro dos cursos")
            saida(f"autores: commit {h}" if h else "autores: nada a commitar")
    # 4. Notion
    if "notion" in etapas:
        itens = modelo.montar(linhas)
        if dry_run and not os.environ.get("NOTION_TOKEN"):
            saida("notion (dry-run sem NOTION_TOKEN): o que seria enviado:\n" + modelo.tabela(itens))
        else:
            sincronizar.sincronizar(itens, dry_run=dry_run, saida=saida)
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="python -m automacao", description=__doc__.split("\n")[0])
    p.add_argument("--so", nargs="+", choices=ETAPAS, metavar="ETAPA", default=list(ETAPAS),
                   help="roda só estas etapas: checklist extrator autores notion (padrão: todas)")
    p.add_argument("--dry-run", action="store_true", help="não grava nada, não commita, não escreve no Notion")
    p.add_argument("--sem-notion", action="store_true")
    p.add_argument("--sem-commit", action="store_true")
    p.add_argument("--sem-fetch", action="store_true", help="não roda git fetch antes de ler a branch joao")
    a = p.parse_args(argv)
    try:
        return executar(a.dry_run, not a.sem_notion, not a.sem_commit, not a.sem_fetch, a.so)
    except (git_seguro.ErroGit, api.ErroNotion, ValueError) as e:
        print("Erro:", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
