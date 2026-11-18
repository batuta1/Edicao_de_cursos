"""Fase A: abrir o zip em memória e achar o manifesto (D01-6). Não lista nem guarda os arquivos de dentro."""
import hashlib
import posixpath
import zipfile
from pathlib import Path

from ..erros import ErroExtracao

MANIFESTO = "imsmanifest.xml"
BLOCO = 1 << 20


def abrir(caminho) -> zipfile.ZipFile:
    caminho = Path(caminho)
    if not caminho.exists():
        raise ErroExtracao(f"Arquivo não encontrado: {caminho}")
    if not caminho.is_file():
        raise ErroExtracao(f"Não é um arquivo: {caminho}")
    try:
        return zipfile.ZipFile(caminho)
    except zipfile.BadZipFile:
        raise ErroExtracao(f"Não é um zip válido (ou está corrompido): {caminho}")
    except OSError as e:
        raise ErroExtracao(f"Não consegui abrir {caminho}: {e}")


def sha256_arquivo(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(BLOCO), b""):
            h.update(bloco)
    return h.hexdigest()


def nomes_do_zip(z):
    return [n for n in z.namelist() if not n.startswith("__MACOSX/") and not n.endswith("/")]


def achar_manifesto(nomes):
    """Devolve (caminho_do_manifesto, prefixo) com o manifesto na raiz ou em uma pasta de topo; ou (None, '')."""
    candidatos = [n for n in nomes if posixpath.basename(n).lower() == MANIFESTO and n.count("/") <= 1]
    if len(candidatos) != 1:
        return None, ""
    m = candidatos[0]
    return m, posixpath.dirname(m) + "/" if "/" in m else ""


def dados_do_zip(caminho_zip):
    caminho_zip = Path(caminho_zip)
    return {"nome": caminho_zip.name, "tamanho": caminho_zip.stat().st_size, "sha256": sha256_arquivo(caminho_zip)}


def dados_de_bytes(nome, conteudo: bytes):
    return {"nome": nome, "tamanho": len(conteudo), "sha256": hashlib.sha256(conteudo).hexdigest()}
