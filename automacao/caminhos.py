"""Caminhos da automação. A raiz do repositório vem do extrator (`EDICAO_RAIZ` no ambiente a substitui, útil em testes)."""
from pathlib import Path

from extrator_scorm.path import caminhos as _extrator

RAIZ = _extrator.RAIZ_REPO
PASTA_AUTOMACAO = Path(__file__).resolve().parent
REFERENCIAS = RAIZ / "automacao" / "referencias"
RELATORIOS = RAIZ / "automacao" / "relatorios"
CURSOS = _extrator.PASTA_CURSOS
REGISTRO = _extrator.REGISTRO
ENV = PASTA_AUTOMACAO / ".env"
NOTION_CONFIG = PASTA_AUTOMACAO / "notion" / "config.json"

# O que a automação pode escrever (relativo à raiz). Qualquer outro caminho é recusado.
PERMITIDOS = ("automacao/", "extrator_scorm/", "Cursos/", ".gitignore", "pyproject.toml", "uv.lock")
PROIBIDOS = ("bagunca/", "Skills/")
