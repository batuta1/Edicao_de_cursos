"""F5: um comando roda tudo, na ordem: checklist (joao → referencias → csv) → extrator → autores → Notion.

    uv run python -m automacao [--so ETAPA ...] [--dry-run] [--sem-notion] [--sem-commit] [--sem-fetch]

Nunca faz push. Commits só dos arquivos do processo. A janela (`automacao.interface`) chama as mesmas funções daqui.
"""
import argparse
import os
import sys

from extrator_scorm.lote import lote, varredura

from . import ambiente, caminhos, git_seguro
from .autores import casar, preencher
from .checklist import buscar, leitura
from .notion import api, modelo, sincronizar

ETAPAS = ("checklist", "extrator", "autores", "notion")


class ErroDeEtapa(RuntimeError):
    """Falta algo para rodar a etapa (pasta, csv, registro). A mensagem diz o que fazer; a linha de comando e a janela a mostram."""


def _extrair(saida):
    """Roda o lote do extrator só nas últimas versões; grava Cursos/registro-de-cursos.json."""
    r = lote.executar(caminhos.CURSOS, ignorar=varredura.IGNORAR_PADRAO, so_ultimas=True, pasta_registro=caminhos.REGISTRO)
    saida(f"extrator: {r['encontrados']} pacotes · extraídos {r['extraidos']} · com erro {r['com_erro']}")
    return r


def executar(dry_run=False, notion=True, commit=True, fetch=True, etapas=ETAPAS, saida=print, cancelar=None):
    """Roda as `etapas` pedidas, sempre na ordem checklist → extrator → autores → notion.

    `dry_run`: ensaio, não grava nada, não commita e não escreve no Notion.
    `saida(texto)`: recebe cada mensagem de andamento. `cancelar()`: se devolver True, para entre uma etapa e outra.
    Devolve 0 se terminou e 1 se foi interrompido. Levanta `ErroDeEtapa`, `ErroGit` ou `ErroNotion` quando não dá para seguir.
    """
    cancelar = cancelar or (lambda: False)
    ambiente.carregar()
    commit = commit and not dry_run
    etapas = [e for e in ETAPAS if e in etapas and (notion or e != "notion")]
    if ("extrator" in etapas or "autores" in etapas) and not caminhos.CURSOS.is_dir():
        raise ErroDeEtapa(f"{caminhos.CURSOS} não existe nesta branch (Cursos/ está na main). Rode na main ou use EDICAO_RAIZ "
                          "(veja scripts/documentacao/automacao-notion.md).")

    # 1. checklist (csv): as etapas autores e notion precisam dele, mesmo quando o checklist não foi pedido
    csv_ = None
    if "checklist" in etapas and not dry_run:
        csv_ = buscar.sincronizar(fetch=fetch, commit=commit, saida=saida)["csv"]
    else:
        if "checklist" in etapas:                            # ensaio: só diz qual versão seria usada, sem baixar
            buscar.prever(fetch=fetch, saida=saida)
        if "autores" in etapas or "notion" in etapas:
            csv_ = buscar.csv_atual()
            if csv_ is None and dry_run and "checklist" in etapas:
                saida("ensaio: autores e notion precisam do csv, que ainda não foi baixado. Aplique a etapa checklist antes.")
                return 0
            if csv_ is None:
                raise ErroDeEtapa("não há csv em scripts/automacao/referencias/. Rode antes: uv run python -m automacao --so checklist")
            saida(f"usando {csv_.name} (já existente)")
    linhas = leitura.ler(csv_) if csv_ else []
    if cancelar():
        saida("interrompido")
        return 1

    # 2. extrator
    if "extrator" in etapas:
        if dry_run:
            saida("extrator: pulado no ensaio (ele grava registro e fichas)")
        else:
            _extrair(saida)
        if cancelar():
            saida("interrompido")
            return 1

    # 3. autores
    if "autores" in etapas:
        if not caminhos.REGISTRO.is_file():
            raise ErroDeEtapa("falta Cursos/registro-de-cursos.json. Rode antes: uv run python -m automacao --so extrator")
        r = preencher.preencher(linhas, casar.carregar_registro(caminhos.REGISTRO), dry_run=dry_run, saida=saida)
        if r["gravados"] and not dry_run:
            _extrair(saida)                                  # refaz o registro para ele trazer os autores novos
        if commit:
            h = git_seguro.commitar_somente([*r["arquivos"], caminhos.REGISTRO], "update de autores e registro dos cursos")
            saida(f"autores: commit {h}" if h else "autores: nada a commitar")
        if cancelar():
            saida("interrompido")
            return 1

    # 4. Notion
    if "notion" in etapas:
        itens = modelo.montar(linhas)
        if dry_run and not os.environ.get("NOTION_TOKEN"):
            saida("notion (ensaio sem NOTION_TOKEN): o que seria enviado:\n" + modelo.tabela(itens))
        else:
            sincronizar.sincronizar(itens, dry_run=dry_run, saida=saida, cancelar=cancelar)
    return 1 if cancelar() else 0


def main(argv=None):
    """Linha de comando. Devolve o código de saída (0 = ok)."""
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
    except (ErroDeEtapa, git_seguro.ErroGit, api.ErroNotion, ValueError) as e:
        print("Erro:", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
