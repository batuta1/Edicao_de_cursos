"""Único lugar com caminhos do extrator. Quem precisa de uma pasta ou arquivo importa daqui."""
import os
from pathlib import Path

PASTA_EXTRATOR = Path(__file__).resolve().parents[1]


def _achar_raiz():
    """`EDICAO_RAIZ` (ambiente) manda, se existir; senão sobe do extrator até a pasta que contém `Cursos/`; sem achar, a pasta-mãe."""
    if os.environ.get("EDICAO_RAIZ"):
        return Path(os.environ["EDICAO_RAIZ"]).resolve()
    for pasta in PASTA_EXTRATOR.parents:
        if (pasta / "Cursos").is_dir():
            return pasta
    return PASTA_EXTRATOR.parent


RAIZ_REPO = _achar_raiz()
PASTA_CURSOS = RAIZ_REPO / "Cursos"

# Versionado: a lista de todos os cursos (última versão de cada um), dentro de Cursos/.
REGISTRO = PASTA_CURSOS / "registro-de-cursos.json"

# Gerados, na raiz do extrator e fora do git.
CONTROLE = PASTA_EXTRATOR / "controle.json"
CONTROLE_ANTERIOR = PASTA_EXTRATOR / "controle.anterior.json"
RESUMO = PASTA_EXTRATOR / "resumo.json"
FICHAS = PASTA_EXTRATOR / "fichas"
INDIVIDUAIS = FICHAS / "_individuais"          # ficha de um pacote só (zip ou pasta avulsa)

PASTA_SAIDA = PASTA_EXTRATOR                   # controle.json, resumo.json e fichas/ moram aqui
FONTES = PASTA_EXTRATOR / "fontes" / "arquivos"
