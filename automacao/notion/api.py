"""F4: Notion pela API oficial (requests). O token vem só de `NOTION_TOKEN` (ambiente ou automacao/.env); nunca é gravado nem impresso."""
import json
import os
import time

import requests

from .. import caminhos
from ..texto import chave

BASE = "https://api.notion.com/v1"
VERSAO_DA_API = "2022-06-28"
PAGINA_PADRAO = "40d4a1ed76b480b18f67febbce8ade93"      # "Produção de cursos" (link da D1.2)
COLUNAS = {"nome": "Nome do curso", "status": "Status", "responsavel": "Responsável", "progresso": "Progresso"}


DICA_BANCO_VINCULADO = (
    "a integração vê a página, mas não os dados do banco: ele é uma VISÃO (banco vinculado) de outro banco. "
    "No Notion, abra o banco original (na visão: ícone ↗ ao lado do título, ou ⋯ → Fonte de dados) e adicione a integração "
    "em ⋯ → Conexões NESSE banco/página. Depois rode de novo. Se o banco original tiver outro ID, use NOTION_DATABASE_ID no .env.")


class ErroNotion(RuntimeError):
    pass


class Notion:
    def __init__(self, token=None):
        token = token or os.environ.get("NOTION_TOKEN")
        if not token:
            raise ErroNotion("NOTION_TOKEN não definido (variável de ambiente ou automacao/.env).")
        self._s = requests.Session()
        self._s.headers.update({"Authorization": f"Bearer {token}", "Notion-Version": VERSAO_DA_API, "Content-Type": "application/json"})
        self._usuarios = None

    def _req(self, metodo, caminho, **kw):
        for tentativa in range(4):
            r = self._s.request(metodo, BASE + caminho, timeout=30, **kw)
            if r.status_code == 429 and tentativa < 3:
                time.sleep(float(r.headers.get("Retry-After", 1)) + 0.2)
                continue
            if r.status_code >= 400:
                try:
                    msg = r.json().get("message", r.text)
                except ValueError:
                    msg = r.text
                raise ErroNotion(f"{metodo} {caminho}: {r.status_code} {msg}")
            return r.json()

    # ---- banco ----
    def banco(self, id_):
        """O banco de dados. Se o ID for de uma página, procura o banco dentro dela."""
        try:
            return self._req("GET", f"/databases/{id_}")
        except ErroNotion as e:
            if "data sources" in str(e):
                raise ErroNotion(DICA_BANCO_VINCULADO) from e
        filhos = self._req("GET", f"/blocks/{id_}/children?page_size=100")["results"]
        bancos = [b for b in filhos if b["type"] == "child_database"]
        if not bancos:
            raise ErroNotion("o link não é um banco nem uma página com banco dentro (a integração foi compartilhada com ele?)")
        try:
            return self._req("GET", f"/databases/{bancos[0]['id']}")
        except ErroNotion as e:
            if "data sources" in str(e):
                raise ErroNotion(DICA_BANCO_VINCULADO) from e
            raise

    def linhas(self, banco_id):
        saida, cursor = [], None
        while True:
            corpo = {"page_size": 100, **({"start_cursor": cursor} if cursor else {})}
            r = self._req("POST", f"/databases/{banco_id}/query", data=json.dumps(corpo))
            saida += r["results"]
            if not r.get("has_more"):
                return saida
            cursor = r["next_cursor"]

    def atualizar(self, pagina_id, propriedades):
        return self._req("PATCH", f"/pages/{pagina_id}", data=json.dumps({"properties": propriedades}))

    def usuario(self, nome):
        if self._usuarios is None:
            self._usuarios, cursor = [], None
            while True:
                r = self._req("GET", "/users?page_size=100" + (f"&start_cursor={cursor}" if cursor else ""))
                self._usuarios += r["results"]
                if not r.get("has_more"):
                    break
                cursor = r["next_cursor"]
        achados = [u for u in self._usuarios if u.get("name") and chave(u["name"]).startswith(chave(nome))]
        if len(achados) != 1:
            raise ErroNotion(f'usuário "{nome}" do Notion: {len(achados)} correspondência(s)')
        return achados[0]["id"]


# ---- esquema, leitura e escrita por tipo ----
def mapear_colunas(propriedades):
    """{papel: (nome da coluna, tipo, propriedade)}; erro listando as colunas se alguma das 4 faltar."""
    por_chave = {chave(n): (n, p) for n, p in propriedades.items()}
    mapa = {}
    for papel, nome in COLUNAS.items():
        achado = por_chave.get(chave(nome))
        if achado is None and papel == "nome":
            achado = next(((n, p) for n, p in propriedades.items() if p["type"] == "title"), None)
        if achado is None:
            raise ErroNotion(f'coluna "{nome}" não encontrada. Colunas do banco: ' + ", ".join(f"{n} ({p['type']})" for n, p in propriedades.items()))
        mapa[papel] = (achado[0], achado[1]["type"], achado[1])
    return mapa


def _texto(rich):
    return "".join(t.get("plain_text", "") for t in rich)


def titulo_da_linha(pagina, coluna):
    return _texto(pagina["properties"][coluna].get("title", []))


def valor_atual(prop):
    t = prop["type"]
    v = prop.get(t)
    if t in ("status", "select"):
        return v["name"] if v else None
    if t == "multi_select":
        return sorted(o["name"] for o in v) or None
    if t == "people":
        return sorted(p.get("name") or p["id"] for p in v) or None
    if t in ("rich_text", "title"):
        return _texto(v) or None
    return v


def carga(papel, tipo, prop_esquema, valor, cliente=None):
    """(valor comparável com valor_atual, payload da API) para escrever `valor` na coluna. Erro se o tipo não for suportado."""
    if papel == "progresso":
        if tipo != "number":
            raise ErroNotion(f"Progresso deveria ser número, é {tipo}")
        pct = prop_esquema["number"].get("format") == "percent"
        v = round(valor, 4) if pct else round(valor * 100)
        return v, {"number": v}
    if papel == "status":
        if tipo in ("status", "select"):
            return valor, {tipo: {"name": valor}}
        raise ErroNotion(f"Status deveria ser status ou seleção, é {tipo}")
    if papel == "responsavel":
        if tipo == "select":
            return valor, {"select": {"name": valor}}
        if tipo == "multi_select":
            return [valor], {"multi_select": [{"name": valor}]}
        if tipo == "rich_text":
            return valor, {"rich_text": [{"text": {"content": valor}}]}
        if tipo == "people":
            return None, {"people": [{"id": cliente.usuario(valor)}]}
        raise ErroNotion(f"tipo de Responsável não suportado: {tipo}")
    raise ErroNotion(f"papel desconhecido: {papel}")


def salvar_config(banco, mapa):
    cfg = {"banco_id": banco["id"], "colunas": {p: {"nome": n, "tipo": t} for p, (n, t, _) in mapa.items()}}
    caminhos.NOTION_CONFIG.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return cfg
