"""As duas fontes das janelas: uma comum (Ubuntu) para textos e botões, e uma monoespaçada (SUSE Mono) para relatório e JSON.

Os arquivos `.ttf` ficam em `comum/ui/arquivos/` (com as licenças OFL e UFL). O Tk não carrega arquivo de fonte sozinho:
- **Windows:** registra cada `.ttf` só para este processo (`AddFontResourceExW` com `FR_PRIVATE`); nada é instalado no sistema.
- **Linux:** avisa o fontconfig, antes de a janela abrir, de que existe mais uma pasta de fontes.
Se der qualquer problema (outro sistema, Tk sem suporte), a janela usa as fontes de sempre.
"""
import atexit
import os
import shutil
import sys
import tempfile
from pathlib import Path

FONTE_COMUM = "Ubuntu"
FONTE_MONO = "SUSE Mono"
TAMANHO_COMUM = 11
TAMANHO_MONO = 10
PASTA = Path(__file__).resolve().parent / "arquivos"
CONF_DO_SISTEMA = Path("/etc/fonts/fonts.conf")
FR_PRIVATE = 0x10                       # a fonte vale só para este processo e some quando ele termina


def _preparar_windows():
    """Registra os `.ttf` no GDI, que é o que o Tk usa no Windows. Devolve quantos foram aceitos."""
    import ctypes
    adicionar = ctypes.windll.gdi32.AddFontResourceExW
    return sum(1 for ttf in sorted(PASTA.glob("*.ttf")) if adicionar(str(ttf), FR_PRIVATE, 0) > 0)


def _preparar_linux():
    """Cria um `fonts.conf` temporário que inclui o do sistema e a nossa pasta, e aponta o fontconfig para ele."""
    if not CONF_DO_SISTEMA.is_file():
        return False
    pasta_conf = Path(tempfile.mkdtemp(prefix="comum-fontes-"))
    atexit.register(shutil.rmtree, pasta_conf, True)
    conf = pasta_conf / "fonts.conf"
    conf.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n'
                    f'<fontconfig><include ignore_missing="yes">{CONF_DO_SISTEMA}</include><dir>{PASTA}</dir></fontconfig>\n',
                    encoding="utf-8")
    os.environ["FONTCONFIG_FILE"] = str(conf)
    return True


def preparar():
    """Chamar ANTES de criar a janela. Devolve True se as fontes do projeto foram registradas."""
    if not PASTA.is_dir():
        return False
    try:
        if sys.platform.startswith("win"):
            return _preparar_windows() > 0
        if sys.platform.startswith("linux"):
            return _preparar_linux()
    except (OSError, AttributeError):       # sem permissão, sem ctypes.windll, etc.
        return False
    return False


def aplicar(janela, estilo):
    """Troca as fontes nomeadas do Tk (valem para todos os widgets) e a altura das linhas da tabela.

    Devolve {"comum": ..., "mono": ...} com a família que ficou valendo em cada uma (a de sempre, se a escolhida não existe nesta máquina).
    """
    from tkinter import font
    instaladas = set(font.families(janela))
    usadas = {}
    for chave, familia, tamanho, nomes in (
            ("comum", FONTE_COMUM, TAMANHO_COMUM, ("TkDefaultFont", "TkTextFont", "TkMenuFont", "TkHeadingFont", "TkCaptionFont", "TkTooltipFont")),
            ("mono", FONTE_MONO, TAMANHO_MONO, ("TkFixedFont",))):
        if familia in instaladas:
            for nome in nomes:
                font.nametofont(nome, janela).configure(family=familia, size=tamanho)
        usadas[chave] = font.nametofont(nomes[0], janela).actual("family")
    estilo.configure("Treeview", rowheight=int(TAMANHO_COMUM * 2.2))
    return usadas
