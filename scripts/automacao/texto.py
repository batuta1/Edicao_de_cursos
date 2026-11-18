"""Normalização de texto para comparar nomes (curso do xlsx × pasta × título do Rise)."""
import re
import unicodedata


def sem_acento(texto):
    """Remove acentos (`ação` → `acao`)."""
    return "".join(c for c in unicodedata.normalize("NFKD", str(texto)) if not unicodedata.combining(c))


def slug(texto):
    """`ChatGPT Chat - Essentials` → `chatgpt-chat-essentials`."""
    return re.sub(r"[^a-z0-9]+", "-", sem_acento(texto).lower()).strip("-")


def chave(texto):
    """Comparação de nomes sem acento, caixa ou espaços extras."""
    return re.sub(r"\s+", " ", sem_acento(texto).lower()).strip()
