"""F4: compara o modelo (csv) com o Notion e atualiza só o que mudou. Não cria linhas. `--dry-run` não escreve."""
import os
from collections import Counter

from .. import caminhos
from ..texto import chave
from . import api


def _relatorio(resultados, dry_run):
    """Grava `relatorios/notion.md` com os cursos agrupados por resultado."""
    L = ["# Notion", "", "(dry-run: nada foi escrito)" if dry_run else "", ""]
    for rotulo in ("atualizado", "sem mudança", "não achou no Notion", "duplicado no Notion", "erro"):
        itens = [r for r in resultados if r["resultado"] == rotulo]
        L.append(f"## {rotulo} ({len(itens)})")
        L.extend(f'- {r["nome"]}' + (f': {r["detalhe"]}' if r.get("detalhe") else "") for r in itens)
        L.append("")
    caminhos.RELATORIOS.mkdir(parents=True, exist_ok=True)
    (caminhos.RELATORIOS / "notion.md").write_text("\n".join(L), encoding="utf-8", newline="\n")


def sincronizar(modelo, dry_run=False, banco_id=None, saida=print, cliente=None, cancelar=None, progresso=None):
    """Devolve a lista de resultados por curso. Levanta ErroNotion se o banco ou as colunas não servirem.

    `cancelar()`: se devolver True, para entre um curso e outro (o que já foi escrito fica). `progresso(atual, total, nome)`: andamento.
    """
    cancelar = cancelar or (lambda: False)
    progresso = progresso or (lambda *_: None)
    cliente = cliente or api.Notion()
    banco = cliente.banco(banco_id or os.environ.get("NOTION_DATA_SOURCE_ID") or os.environ.get("NOTION_DATABASE_ID") or api.PAGINA_PADRAO)
    mapa = api.mapear_colunas(banco["properties"])
    nome_col = mapa["nome"][0]
    indice = {}
    for p in cliente.linhas(banco["id"]):
        indice.setdefault(chave(api.titulo_da_linha(p, nome_col)), []).append(p)
    resultados = []
    for i, item in enumerate(modelo, 1):
        if cancelar():
            saida(f"notion: interrompido antes do curso {i} de {len(modelo)}")
            break
        progresso(i, len(modelo), item["nome"])
        r = {"nome": item["nome"], "resultado": None, "detalhe": ""}
        resultados.append(r)
        achadas = indice.get(chave(item["nome"]), [])
        if not achadas:
            r["resultado"] = "não achou no Notion"
            continue
        if len(achadas) > 1:
            r["resultado"] = "duplicado no Notion"
            continue
        pagina, mudancas, props = achadas[0], [], {}
        try:
            for papel in ("status", "responsavel", "progresso"):
                valor = item["responsavel"] if papel == "responsavel" else item[papel]
                if valor is None:                                    # sem responsável no checklist: não apaga o que está no Notion
                    continue
                coluna, tipo, esquema = mapa[papel]
                comparavel, payload = api.carga(papel, tipo, esquema, valor, cliente)
                atual = api.valor_atual(pagina["properties"][coluna])
                if comparavel is None or atual != comparavel:
                    props[coluna] = payload
                    mudancas.append(f"{papel}: {atual} → {comparavel if comparavel is not None else valor}")
            if not props:
                r["resultado"] = "sem mudança"
            else:
                if not dry_run:
                    cliente.atualizar(pagina["id"], props)
                r["resultado"], r["detalhe"] = "atualizado", "; ".join(mudancas)
        except api.ErroNotion as e:
            r["resultado"], r["detalhe"] = "erro", str(e)
    _relatorio(resultados, dry_run)
    c = Counter(r["resultado"] for r in resultados)
    saida(f"notion{' (dry-run)' if dry_run else ''}: " + " · ".join(f"{k}: {v}" for k, v in c.items()))
    return resultados
