"""F2: pega o `checklist-producao-de-cursos-60-dias-vX-Y.xlsx` mais recente da branch `joao` sem trocar de branch."""
import re
from pathlib import Path

from .. import caminhos, git_seguro
from . import xlsx_para_csv

REF_PADRAO = "origin/joao"
PADRAO = re.compile(r"^checklist-producao-de-cursos-60-dias-v(\d+)-(\d+)\.xlsx$")
MENSAGEM = "update de producao dos cursos (checklist {versao})"


def escolher_mais_recente(nomes):
    """O nome com maior (major, minor) na versão, ou None."""
    candidatos = [(tuple(int(x) for x in m.groups()), n) for n in nomes if (m := PADRAO.match(n))]
    return max(candidatos)[1] if candidatos else None


def versao_do_nome(nome):
    m = PADRAO.match(nome)
    return f"v{m.group(1)}-{m.group(2)}"


def listar(ref):
    return [n for n in git_seguro.git("ls-tree", "-r", "--name-only", ref).splitlines() if "/" not in n]


def sincronizar(ref=REF_PADRAO, fetch=True, commit=True, saida=print):
    """Devolve {"xlsx", "csv", "versao", "commit"}. Deixa só o checklist mais recente em referencias/."""
    if fetch:
        remoto, _, ramo = ref.partition("/")
        git_seguro.git("fetch", remoto, ramo)
    nome = escolher_mais_recente(listar(ref))
    if nome is None:
        raise git_seguro.ErroGit(f"nenhum checklist-producao-de-cursos-60-dias-vX-Y.xlsx na raiz de {ref}")
    pasta = caminhos.REFERENCIAS
    pasta.mkdir(parents=True, exist_ok=True)
    destino = pasta / nome
    dados = git_seguro.git("show", f"{ref}:{nome}", binario=True)
    if not destino.exists() or destino.read_bytes() != dados:
        destino.write_bytes(dados)
        saida(f"checklist: {nome} gravado em {git_seguro.relativo(pasta)}/")
    else:
        saida(f"checklist: {nome} já estava em {git_seguro.relativo(pasta)}/ (sem mudança)")
    for velho in list(pasta.glob("checklist-producao-de-cursos-60-dias-v*")):
        if velho.stem != destino.stem:
            velho.unlink()
            saida(f"checklist: removido {velho.name}")
    arquivo_csv = xlsx_para_csv.converter(destino, saida=saida)
    hash_commit = None
    if commit:
        hash_commit = git_seguro.commitar_somente([pasta], MENSAGEM.format(versao=versao_do_nome(nome)))
        saida(f"checklist: commit {hash_commit}" if hash_commit else "checklist: nada a commitar")
    return {"xlsx": destino, "csv": arquivo_csv, "versao": versao_do_nome(nome), "commit": hash_commit}


def csv_atual():
    """O `csv` do checklist em referencias/ (o de maior versão), ou None."""
    achados = [p for p in caminhos.REFERENCIAS.glob("checklist-producao-de-cursos-60-dias-v*.csv")]
    return max(achados, key=lambda p: [int(x) for x in re.findall(r"\d+", p.stem)[-2:]]) if achados else None
