"""Lista os items/blocks de uma licao em forma resumida, para orientar a revisao."""
import json
import sys

def resumo_bloco(item, prefixo=""):
    tipo = item.get("type")
    titulo = item.get("title")
    linha = f"{prefixo}[{tipo}]"
    if titulo:
        linha += f" title={titulo!r}"
    # tentar extrair algum texto curto para paragraph/heading/statement/list
    for campo in ("text", "heading", "caption"):
        if campo in item and isinstance(item[campo], str) and item[campo].strip():
            txt = item[campo].strip().replace("\n", " ")
            linha += f" {campo}={txt[:90]!r}"
            break
    print(linha)
    # blocos aninhados comuns
    for chave_filhos in ("items", "listItems", "blocks", "tabs", "cards"):
        if chave_filhos in item and isinstance(item[chave_filhos], list):
            for sub in item[chave_filhos]:
                if isinstance(sub, dict):
                    resumo_bloco(sub, prefixo + "  ")

def main(caminho):
    with open(caminho, encoding="utf-8") as f:
        data = json.load(f)
    lesson = data["lesson"]
    print(f"=== Licao {data['numero_da_licao']}: {data['title']} ===")
    items = lesson.get("items", [])
    print(f"Total de items de topo: {len(items)}")
    for item in items:
        resumo_bloco(item)

if __name__ == "__main__":
    main(sys.argv[1])
