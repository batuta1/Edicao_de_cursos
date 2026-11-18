"""Onde fica a raiz do repositório e a pasta `Cursos/`. Único lugar com essa conta; as duas partes importam daqui.

Estrutura: <raiz>/scripts/comum/caminhos.py  →  a raiz é duas pastas acima de `scripts/`.
`EDICAO_RAIZ` (variável de ambiente) aponta para OUTRA árvore do repositório (por exemplo uma cópia da `main`, que tem `Cursos/`).
"""
import os
from pathlib import Path

PASTA_SCRIPTS = Path(__file__).resolve().parents[1]
RAIZ_REPO = Path(os.environ["EDICAO_RAIZ"]).resolve() if os.environ.get("EDICAO_RAIZ") else PASTA_SCRIPTS.parent
PASTA_CURSOS = RAIZ_REPO / "Cursos"
