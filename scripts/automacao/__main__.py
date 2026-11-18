"""`uv run python -m automacao`: roda `atualizar.main` (linha de comando das etapas)."""
import sys

from .atualizar import main

sys.exit(main())
