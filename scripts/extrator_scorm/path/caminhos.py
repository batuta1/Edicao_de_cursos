"""Único lugar com os caminhos do extrator. Quem precisa de uma pasta ou arquivo importa daqui.

A raiz do repositório e `Cursos/` vêm de `comum.caminhos` (a mesma conta da automação).
"""
from pathlib import Path

from comum.caminhos import PASTA_CURSOS, RAIZ_REPO  # noqa: F401 (reexportados para o resto do extrator)

PASTA_EXTRATOR = Path(__file__).resolve().parents[1]

# Versionado: a lista de todos os cursos (última versão de cada um), dentro de Cursos/.
REGISTRO = PASTA_CURSOS / "registro-de-cursos.json"

# Gerados, na pasta do extrator e fora do git.
CONTROLE = PASTA_EXTRATOR / "controle.json"
CONTROLE_ANTERIOR = PASTA_EXTRATOR / "controle.anterior.json"
RESUMO = PASTA_EXTRATOR / "resumo.json"
FICHAS = PASTA_EXTRATOR / "fichas"
INDIVIDUAIS = FICHAS / "_individuais"          # ficha de um pacote só (zip ou pasta avulsa)

PASTA_SAIDA = PASTA_EXTRATOR                   # controle.json, resumo.json e fichas/ moram aqui
