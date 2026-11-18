"""As duas fontes da janela: uma comum (Ubuntu) para os textos e botões, e uma monoespaçada (SUSE Mono) para o texto do relatório e do JSON.

Os arquivos `.ttf` ficam em `extrator/fontes/arquivos/` (com as licenças). O Tk não carrega arquivo de fonte sozinho: no Linux
a gente avisa o fontconfig, antes de abrir a janela, de que existe mais uma pasta de fontes. Se der qualquer problema (outro
sistema, Tk sem Xft), a janela usa as fontes de sempre.
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
PASTA = Path(__file__).resolve().parents[1] / "fontes" / "arquivos"
CONF_DO_SISTEMA = Path("/etc/fonts/fonts.conf")


def preparar():
    """Chamar ANTES de criar a janela. Devolve True se a pasta de fontes foi registrada no fontconfig."""
    if not sys.platform.startswith("linux") or not PASTA.is_dir() or not CONF_DO_SISTEMA.is_file():
        return False
    try:
        pasta_conf = Path(tempfile.mkdtemp(prefix="extrator-fontes-"))
        atexit.register(shutil.rmtree, pasta_conf, True)
        conf = pasta_conf / "fonts.conf"
        conf.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n'
                        f'<fontconfig><include ignore_missing="yes">{CONF_DO_SISTEMA}</include><dir>{PASTA}</dir></fontconfig>\n',
                        encoding="utf-8")
        os.environ["FONTCONFIG_FILE"] = str(conf)
        return True
    except OSError:
        return False


def aplicar(janela, estilo):
    """Troca as fontes nomeadas do Tk (valem para todos os widgets) e a altura das linhas da tabela. Devolve {"comum": ..., "mono": ...}
    com a família que ficou valendo em cada uma (a de sempre, se a escolhida não existe nesta máquina)."""
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
