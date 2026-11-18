"""`uv run python -m automacao.interface` abre a janela da automação."""
import sys

from .tela import abrir

sys.exit(abrir())
