"""Ponto de entrada: `python -m extrator_scorm` (tela), `python -m extrator_scorm Cursos` (lote) ou com um pacote."""
import sys

from .interface.cli import main

if __name__ == "__main__":
    sys.exit(main())
