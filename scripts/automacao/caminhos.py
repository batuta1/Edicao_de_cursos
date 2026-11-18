"""Caminhos da automação. A raiz do repositório vem de `comum.caminhos` (`EDICAO_RAIZ` no ambiente a substitui, útil em testes)."""
from pathlib import Path

from comum.caminhos import PASTA_CURSOS, RAIZ_REPO

RAIZ = RAIZ_REPO
PASTA_AUTOMACAO = Path(__file__).resolve().parent
CURSOS = PASTA_CURSOS
REGISTRO = CURSOS / "registro-de-cursos.json"

# Dados gerados ficam junto do código, mas relativos à raiz escolhida (assim uma cópia da `main` recebe os commits dela).
REFERENCIAS = RAIZ / "scripts" / "automacao" / "referencias"
RELATORIOS = RAIZ / "scripts" / "automacao" / "relatorios"

# Pessoais e gerados: sempre na pasta do código.
ENV = PASTA_AUTOMACAO / ".env"
NOTION_CONFIG = PASTA_AUTOMACAO / "notion" / "config.json"

# O que a automação pode escrever (relativo à raiz). Qualquer outro caminho é recusado.
PERMITIDOS = ("scripts/", "Cursos/", ".gitignore", "pyproject.toml", "uv.lock")
PROIBIDOS = ("bagunca/", "Skills/")
