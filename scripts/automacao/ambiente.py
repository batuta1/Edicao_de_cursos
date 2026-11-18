"""Lê `automacao/.env` (CHAVE=valor) para o ambiente, sem sobrescrever o que já existe. O arquivo é ignorado pelo git."""
import os

from . import caminhos


def carregar():
    """Copia as linhas CHAVE=valor de `automacao/.env` para o ambiente (sem sobrescrever o que já existe). Sem o arquivo, não faz nada."""
    if not caminhos.ENV.is_file():
        return
    for linha in caminhos.ENV.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#") or "=" not in linha:
            continue
        k, v = linha.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
