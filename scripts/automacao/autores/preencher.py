"""F3: grava o autor (nome curto) no `autor.json` da última versão de cada curso casado.

Só troca `null`; nunca sobrescreve autor já escrito. O formato do arquivo vem de `comum.autor_json`.
"""
from comum import autor_json

from .. import caminhos
from ..checklist import leitura
from . import casar


def preencher(linhas, registro, dry_run=False, raiz_cursos=None, saida=print):
    """Preenche os `autor.json` e devolve um dict com o que mudou e o que ficou de fora; grava `relatorios/nao-casados.md`.

    `linhas`: linhas do csv do checklist. `registro`: o `registro-de-cursos.json` já lido. `dry_run`: só calcula, não grava.
    """
    raiz_cursos = raiz_cursos or caminhos.CURSOS
    cursos = casar.indice(registro)
    nomes = [leitura.valor(l, "Curso") for l in linhas if leitura.valor(l, "Curso")]
    casados, ambiguos, sem_pasta, sobras = casar.casar(nomes, cursos)
    por_nome = {leitura.valor(l, "Curso"): l for l in linhas}
    gravados, iguais, divergentes, avisos, problemas = [], [], [], [], []
    for nome, curso in casados.items():
        autor, aviso = leitura.autor_da_linha(por_nome[nome])
        if aviso:
            avisos.append((nome, aviso))
        if autor is None:                                    # sem informação na planilha: não mexe no autor.json
            continue
        pasta = autor_json.pasta_da_versao(raiz_cursos, curso["empresa"], curso["curso"], curso["versao"])
        atual, existe, problema = autor_json.ler_declaracao(pasta)
        rotulo = f'{curso["empresa"]}/{curso["curso"]}/{curso["versao"]}'
        if problema:                                         # arquivo estragado: não sobrescreve, só avisa
            problemas.append((rotulo, problema))
        elif atual is None:                                  # vazio (`null`) ou inexistente: pode preencher
            if not dry_run:
                autor_json.escrever(pasta, autor)
            gravados.append((rotulo, autor, pasta / autor_json.NOME_DO_ARQUIVO))
        elif atual == autor:
            iguais.append(rotulo)
        else:                                                # já tem outro nome escrito: nunca troca
            divergentes.append((rotulo, atual, autor))
    r = {"casados": len(casados), "ambiguos": ambiguos, "sem_pasta": sem_pasta, "pastas_sem_linha": sobras, "gravados": gravados,
         "iguais": iguais, "divergentes": divergentes, "avisos": avisos, "problemas": problemas, "dry_run": dry_run,
         "pastas": len(cursos), "arquivos": [g[2] for g in gravados]}
    _relatorio(r)
    saida(f"autores: {len(casados)} de {len(cursos)} pastas casadas com o checklist; "
          f"{'a gravar' if dry_run else 'gravados'}: {len(gravados)}; já iguais: {len(iguais)}; divergentes: {len(divergentes)}; "
          f"sem pasta: {len(sem_pasta)}; ambíguos: {len(ambiguos)}; pastas sem linha: {len(sobras)}")
    return r


def _relatorio(r):
    """Escreve `relatorios/nao-casados.md` com as listas do resultado de `preencher`."""
    L = ["# Casamento checklist × Cursos/ e autores", "",
         f"Casados: {r['casados']} de {r['pastas']} pastas. {'(dry-run: nada foi gravado)' if r['dry_run'] else ''}", ""]

    def bloco(titulo, itens, fmt=str):
        """Acrescenta uma seção `## título (n)` com uma linha por item; `fmt` transforma cada item em texto."""
        L.append(f"## {titulo} ({len(itens)})")
        L.extend(f"- {fmt(i)}" for i in itens)
        L.append("")
    bloco("Pastas em Cursos/ sem linha no checklist (confira o nome)", r["pastas_sem_linha"], lambda c: f'{c["empresa"]}/{c["curso"]}')
    bloco("Ambíguos (mais de uma pasta)", list(r["ambiguos"].items()), lambda i: f'{i[0]}: ' + ", ".join(f'{c["empresa"]}/{c["curso"]}' for c in i[1]))
    bloco("Linhas do checklist sem pasta (esperado: curso ainda não produzido)", r["sem_pasta"])
    bloco("Autor gravado", r["gravados"], lambda g: f"{g[0]}: {g[1]}")
    bloco("Autor divergente (já escrito, não alterado)", r["divergentes"], lambda d: f"{d[0]}: autor.json={d[1]}, checklist={d[2]}")
    bloco("Avisos do checklist", r["avisos"], lambda a: f"{a[0]}: {a[1]}")
    bloco("Problemas em autor.json", r["problemas"], lambda p: f"{p[0]}: {p[1]}")
    caminhos.RELATORIOS.mkdir(parents=True, exist_ok=True)
    (caminhos.RELATORIOS / "nao-casados.md").write_text("\n".join(L), encoding="utf-8", newline="\n")
