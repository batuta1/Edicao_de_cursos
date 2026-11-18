"""MVP1.1, Fase A: percorrer a pasta de cursos e separar o que é pacote SCORM do que não é. Só lê; nunca grava.

Um pacote SCORM é um .zip (ou uma pasta) com `imsmanifest.xml` na raiz, ou, no zip, numa única pasta de topo
(documentos/identificar-scorm.md). Um pacote em pasta não é aberto por dentro: ele inteiro é um pacote só.
"""
import argparse
import io
import os
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath

from ..erros import ErroExtracao
from ..leitura import inventario

# O laboratório do João V. não se toca (nem se lê). Um nome sem barra vale em qualquer nível da pasta; com barra, é um caminho
# relativo à pasta varrida.
IGNORAR_PADRAO = ("LAB-SCORM-sem-Articulate",)
PASTAS_SEMPRE_IGNORADAS = {".git"}
# Cursos/<Empresa>/<curso>/scorm/vN[/copias]/<pacote>
CAMINHO_PADRAO = re.compile(r"^(?P<empresa>[^/]+)/(?P<curso>[^/]+)/scorm/(?P<versao>v\d+)/(?P<copias>copias/)?")


def _local_do_pacote(relativo):
    """Empresa, curso, versão e se é cópia, pelo caminho; tudo None se o caminho não segue o padrão."""
    m = CAMINHO_PADRAO.match(relativo)
    if not m:
        return {"empresa": None, "curso": None, "versao": None, "copia": None}
    return {"empresa": m["empresa"], "curso": m["curso"], "versao": m["versao"], "copia": bool(m["copias"])}


def _tem_manifesto_na_raiz(nomes_de_arquivos):
    """True se a lista de nomes tem um `imsmanifest.xml` (o que faz da pasta um pacote SCORM)."""
    return any(n.lower() == inventario.MANIFESTO for n in nomes_de_arquivos)


def _classificar_zip(caminho):
    """(eh_pacote, duplo_zip, motivo). `motivo` só quando não é pacote."""
    try:
        with inventario.abrir(caminho) as z:
            nomes = inventario.nomes_do_zip(z)
            if inventario.achar_manifesto(nomes)[0] is not None:
                return True, False, None
            fundos = [n for n in nomes if n.lower().endswith(inventario.MANIFESTO)]
            if fundos:
                return False, False, f"contêiner: {len(fundos)} manifesto(s) em subpastas, nenhum na raiz"
            internos = [n for n in nomes if n.lower().endswith(".zip")]
            if len(internos) == 1:                              # "duplo zip": o extrator lê o de dentro
                try:
                    with zipfile.ZipFile(io.BytesIO(z.read(internos[0]))) as interno:
                        if inventario.achar_manifesto(inventario.nomes_do_zip(interno))[0] is not None:
                            return True, True, None
                except zipfile.BadZipFile:
                    return False, False, f"o zip de dentro ({internos[0]}) está corrompido"
            return False, False, "sem imsmanifest.xml"
    except ErroExtracao as e:
        return False, False, str(e)
    except (zipfile.BadZipFile, OSError, RuntimeError) as e:
        return False, False, f"não consegui ler o zip: {e}"


def _tamanho_da_pasta(pasta):
    """Soma dos tamanhos dos arquivos da pasta, em bytes (ignora arquivos que não dá para ler)."""
    total = 0
    for atual, _, arquivos in os.walk(pasta):
        for a in arquivos:
            try:
                total += os.path.getsize(os.path.join(atual, a))
            except OSError:
                pass
    return total


def _a_ignorar(relativo, ignorar):
    """True se o caminho relativo está na lista de ignorados (caminho inteiro, prefixo de pasta ou só o nome)."""
    nome = relativo.rsplit("/", 1)[-1]
    return any(relativo == i or relativo.startswith(i + "/") or ("/" not in i and nome == i) for i in ignorar)


def varrer(pasta, ignorar=IGNORAR_PADRAO):
    """Percorre `pasta` e devolve {"pacotes": [...], "nao_scorm": [...], "avisos": [...]}, tudo em ordem de caminho.

    pacote:    caminho (relativo a `pasta`, com /), tipo ("zip" ou "pasta"), tamanho (bytes), empresa, curso, versao, copia,
               duplo_zip (só zip)
    nao_scorm: caminho, motivo
    """
    raiz = Path(pasta)
    if not raiz.is_dir():
        raise ErroExtracao(f"Não é uma pasta: {raiz}")
    ignorar = tuple(str(PurePosixPath(i.replace("\\", "/"))).strip("/") for i in ignorar)
    pacotes, nao_scorm, avisos = [], [], []

    def registrar(relativo, tipo, tamanho, duplo_zip=False):
        """Acrescenta um pacote à lista com empresa, curso e versão tirados do caminho (e avisa se fugir do padrão)."""
        local = _local_do_pacote(relativo)
        if local["versao"] is None:
            avisos.append({"caminho": relativo, "mensagem": "Fora do padrão <Empresa>/<curso>/scorm/vN: empresa, curso e versão ficam vazios."})
        pacotes.append({"caminho": relativo, "tipo": tipo, "tamanho": tamanho, **local, **({"duplo_zip": True} if duplo_zip else {})})

    for atual, dirs, arquivos in os.walk(raiz):
        rel_atual = Path(atual).relative_to(raiz).as_posix()
        rel_atual = "" if rel_atual == "." else rel_atual
        dirs[:] = sorted(d for d in dirs if d not in PASTAS_SEMPRE_IGNORADAS and not _a_ignorar(f"{rel_atual}/{d}".lstrip("/"), ignorar))
        if rel_atual and _tem_manifesto_na_raiz(arquivos):
            registrar(rel_atual, "pasta", _tamanho_da_pasta(atual))
            dirs[:] = []                                        # a pasta inteira é um pacote: não se desce nela
            continue
        for nome in sorted(arquivos):
            if not nome.lower().endswith(".zip"):
                continue
            relativo = f"{rel_atual}/{nome}".lstrip("/")
            eh_pacote, duplo_zip, motivo = _classificar_zip(os.path.join(atual, nome))
            if eh_pacote:
                registrar(relativo, "zip", os.path.getsize(os.path.join(atual, nome)), duplo_zip)
            else:
                nao_scorm.append({"caminho": relativo, "motivo": motivo})
    pacotes.sort(key=lambda p: p["caminho"])
    nao_scorm.sort(key=lambda p: p["caminho"])
    return {"pacotes": pacotes, "nao_scorm": nao_scorm, "avisos": avisos}


def numero_da_versao(versao):
    """'v10' -> 10; qualquer outra coisa -> -1 (nunca vence uma versão de verdade)."""
    m = re.fullmatch(r"v(\d+)", versao or "")
    return int(m.group(1)) if m else -1


def so_as_ultimas(pacotes):
    """Os caminhos que ficam quando só valem as últimas versões: todos os pacotes (zip, pasta e cópias) da maior `vN` de cada curso.

    Um pacote fora do padrão (sem curso e versão) não tem como ser comparado e fica sempre.
    """
    ultima = {}
    for p in pacotes:
        if p["versao"]:
            chave = (p["empresa"], p["curso"])
            ultima[chave] = max(ultima.get(chave, p["versao"]), p["versao"], key=numero_da_versao)
    return {p["caminho"] for p in pacotes if not p["versao"] or p["versao"] == ultima[(p["empresa"], p["curso"])]}


def texto_da_varredura(r):
    """O resultado da varredura em linhas de texto (a linha de comando e a tela mostram o mesmo)."""
    zips = sum(1 for x in r["pacotes"] if x["tipo"] == "zip")
    linhas = [f"{len(r['pacotes'])} pacotes SCORM ({zips} zips e {len(r['pacotes']) - zips} pastas), "
              f"{len({(x['empresa'], x['curso']) for x in r['pacotes'] if x['curso']})} cursos, {len(r['nao_scorm'])} zips que não são SCORM."]
    linhas += [f"  não SCORM: {x['caminho']} ({x['motivo']})" for x in r["nao_scorm"]]
    linhas += [f"  aviso: {a['caminho']}: {a['mensagem']}" for a in r["avisos"]]
    return linhas


def main(argv=None, saida=print):
    """`python -m extrator_scorm.lote.varredura PASTA`: lista os pacotes encontrados, sem gravar nada."""
    p = argparse.ArgumentParser(prog="python -m extrator_scorm.lote.varredura",
                                description="Lista os pacotes SCORM de uma pasta (só lê, nada é gravado).")
    p.add_argument("pasta", help="pasta de cursos (por exemplo Cursos)")
    p.add_argument("--ignorar", action="append", default=[], metavar="CAMINHO",
                   help="caminho relativo a ignorar, além do laboratório (pode repetir)")
    args = p.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        r = varrer(args.pasta, IGNORAR_PADRAO + tuple(args.ignorar))
    except ErroExtracao as e:
        saida(f"Erro: {e}")
        return 1
    for linha in texto_da_varredura(r):
        saida(linha)
    return 0


if __name__ == "__main__":
    sys.exit(main())
