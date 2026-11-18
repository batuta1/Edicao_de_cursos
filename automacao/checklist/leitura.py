"""Lê o csv do checklist e interpreta cada linha (autor, etapas, status, progresso)."""
import csv
import re
from pathlib import Path

from ..texto import chave

NOMES = ("João", "Marina")


def _marcado(v):
    return str(v).strip().lower() == "x"


def ler(caminho_csv):
    with Path(caminho_csv).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _col(linha, prefixo):
    for k in linha:
        if chave(k).startswith(chave(prefixo)):
            return k
    return None


def valor(linha, prefixo):
    k = _col(linha, prefixo)
    return (linha.get(k) or "").strip() if k else ""


def nome_curto(texto):
    """`João Vitor` → `João`; `marina moreno` → `Marina`; desconhecido → None."""
    c = chave(texto)
    for n in NOMES:
        if c.startswith(chave(n)):
            return n
    return None


def autor_da_linha(linha):
    """(autor, aviso). Responsável se preenchido; senão o `x` de João/Marina; os dois ou nenhum → None."""
    resp = valor(linha, "Responsável")
    if resp:
        n = nome_curto(resp)
        return (n, None) if n else (None, f'Responsável "{resp}" não é João nem Marina')
    marcados = [n for n in NOMES if _marcado(valor(linha, n))]
    if len(marcados) == 1:
        return marcados[0], None
    if len(marcados) == 2:
        return None, "João e Marina marcados juntos"
    return None, None


def etapas(linha):
    """(feitas, total) nas colunas E1–2, E3, E4, E5, E6."""
    colunas = [k for k in linha if re.match(r"^E\d", k.strip())]
    return sum(_marcado(linha[k]) for k in colunas), len(colunas)


def situacao(linha):
    """{"status", "progresso"} com progresso de 0 a 1, só pelas etapas E1–E6.
    A coluna "Meta até 12 dez" (`publicado`) é o objetivo, não o estado: não entra na conta."""
    feitas, total = etapas(linha)
    if total and feitas == total:
        return {"status": "Concluído", "progresso": 1.0}
    return {"status": "Em produção" if feitas else "Aguardando", "progresso": (feitas / total) if total else 0.0}
