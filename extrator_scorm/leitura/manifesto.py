"""Fase B: ler do imsmanifest.xml só o que a ficha usa (SCORM 1.2 e 2004).

O resto do manifesto (itens, recursos, metadados LOM, sequenciamento) está anotado em estrutura/disponiveis.py.
"""
import xml.etree.ElementTree as ET
from urllib.parse import unquote


def _tag(e):
    return e.tag.rsplit("}", 1)[-1]


def _attrs(e):
    return {k.rsplit("}", 1)[-1]: v for k, v in e.attrib.items()}


def _texto(e, nome):
    for f in e:
        if _tag(f) == nome and (f.text or "").strip():
            return f.text.strip()
    return None


def _caminho_declarado(href):
    return unquote(href.split("?", 1)[0].split("#", 1)[0]) if href else None


def ler(conteudo: bytes, nomes_no_zip, prefixo):
    """Devolve o que interessa do manifesto. Levanta ET.ParseError se o XML for ilegível."""
    raiz = ET.fromstring(conteudo)
    meta = next((f for f in raiz if _tag(f) == "metadata"), None)
    orgs = next((f for f in raiz if _tag(f) == "organizations"), None)
    recs = next((f for f in raiz if _tag(f) == "resources"), None)
    organizacoes = [o for o in (orgs if orgs is not None else []) if _tag(o) == "organization"]
    declarados = set()
    for r in (recs if recs is not None else []):
        if _tag(r) != "resource":
            continue
        for h in [_attrs(r).get("href")] + [_attrs(f).get("href") for f in r if _tag(f) == "file"]:
            if _caminho_declarado(h):
                declarados.add(_caminho_declarado(h))
    existentes = set(nomes_no_zip)
    return {
        "identificador": _attrs(raiz).get("identifier"),
        "esquema": _texto(meta, "schema") if meta is not None else None,
        "versao_do_esquema": _texto(meta, "schemaversion") if meta is not None else None,
        "organizacao": _attrs(organizacoes[0]).get("identifier") if organizacoes else None,
        "titulo": _texto(organizacoes[0], "title") if organizacoes else None,
        "arquivos_declarados": len(declarados),
        "declarados_ausentes_no_zip": sorted(p for p in (prefixo + d for d in declarados) if p not in existentes),
    }
