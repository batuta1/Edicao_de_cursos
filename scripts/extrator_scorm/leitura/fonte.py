"""MVP1.1, Fase B: uma camada de leitura comum para zip e para pasta, para o extrator não saber a diferença.

Uma fonte tem quatro operações: nomes() (arquivos, com / e relativos à raiz), ler(nome), tamanho(nome) e blocos(nome).
"""
import hashlib
import os
import posixpath
import zipfile
from pathlib import Path

from ..erros import ErroExtracao

BLOCO = 1 << 20


def _eh_lixo(nome):
    """True para entradas de zip que não são arquivos do pacote (`__MACOSX/` e pastas)."""
    return nome.startswith("__MACOSX/") or nome.endswith("/")


class FonteZip:
    """Pacote SCORM em `.zip`, lido em memória. Mesma interface de `FontePasta`: `nomes`, `ler`, `tamanho`, `blocos`."""
    def __init__(self, zip_aberto):
        self.z = zip_aberto

    def __enter__(self):
        return self

    def __exit__(self, *erro):
        self.z.close()

    def nomes(self):
        """Caminhos dos arquivos do pacote, sem as entradas de lixo."""
        return [n for n in self.z.namelist() if not _eh_lixo(n)]

    def ler(self, nome):
        """Conteúdo (bytes) de um arquivo do pacote."""
        return self.z.read(nome)

    def tamanho(self, nome):
        """Tamanho do arquivo, em bytes."""
        return self.z.getinfo(nome).file_size

    def blocos(self, nome):
        """Lê o arquivo aos poucos (blocos de `BLOCO` bytes), para arquivos grandes."""
        with self.z.open(nome) as f:
            yield from iter(lambda: f.read(BLOCO), b"")


class FontePasta:
    """Pacote SCORM em pasta, lido no lugar (sem virar zip). Mesma interface de `FonteZip`."""
    def __init__(self, pasta):
        self.raiz = Path(pasta)
        self._nomes = None

    def __enter__(self):
        return self

    def __exit__(self, *erro):
        return False

    def nomes(self):
        """Caminhos relativos (com `/`) dos arquivos da pasta, em ordem; calculado uma vez."""
        if self._nomes is None:
            achados = []
            for atual, dirs, arquivos in os.walk(self.raiz):
                dirs.sort()
                rel = Path(atual).relative_to(self.raiz).as_posix()
                achados += [posixpath.join("" if rel == "." else rel, a) for a in arquivos]
            self._nomes = sorted(n for n in achados if not _eh_lixo(n))
        return list(self._nomes)

    def ler(self, nome):
        """Conteúdo (bytes) de um arquivo da pasta; erro se não der para ler."""
        try:
            return (self.raiz / nome).read_bytes()
        except OSError as e:
            raise ErroExtracao(f"Não consegui ler {self.raiz / nome}: {e}")

    def tamanho(self, nome):
        """Tamanho do arquivo, em bytes."""
        return (self.raiz / nome).stat().st_size

    def blocos(self, nome):
        """Lê o arquivo aos poucos (blocos de `BLOCO` bytes); erro se não der para ler."""
        try:
            with open(self.raiz / nome, "rb") as f:
                yield from iter(lambda: f.read(BLOCO), b"")
        except OSError as e:
            raise ErroExtracao(f"Não consegui ler {self.raiz / nome}: {e}")


def abrir(caminho):
    """Abre um .zip ou uma pasta como fonte. Levanta ErroExtracao se não existir, não for zip válido ou não der para ler."""
    caminho = Path(caminho)
    if not caminho.exists():
        raise ErroExtracao(f"Arquivo não encontrado: {caminho}")
    if caminho.is_dir():
        return FontePasta(caminho)
    try:
        return FonteZip(zipfile.ZipFile(caminho))
    except zipfile.BadZipFile:
        raise ErroExtracao(f"Não é um zip válido (ou está corrompido): {caminho}")
    except OSError as e:
        raise ErroExtracao(f"Não consegui abrir {caminho}: {e}")


def impressao_do_conteudo(fonte, prefixo=""):
    """sha256 do conteúdo: arquivo por arquivo (nome relativo ao prefixo, tamanho e bytes), em ordem de nome.

    Uma pasta e o zip de mesmo conteúdo dão a mesma impressão; datas e a ordem dentro do zip não contam.
    """
    h = hashlib.sha256()
    for nome in sorted(n for n in fonte.nomes() if n.startswith(prefixo)):
        h.update(f"{nome[len(prefixo):]}\0{fonte.tamanho(nome)}\0".encode("utf-8", "surrogateescape"))
        for bloco in fonte.blocos(nome):
            h.update(bloco)
    return h.hexdigest()
