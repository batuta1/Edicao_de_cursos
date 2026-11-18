"""
Insere um bloco novo numa licao, a partir de um modelo do catalogo.

O bloco nasce do modelo (type/family/variant/settings/metadata do Rise), recebe os textos do
arquivo de conteudo e ganha IDs novos em todos os niveis, no formato que o modelo indica.
Nenhum bloco existente e' tocado: o novo entra na posicao pedida e os demais so' deslocam.

Arquivo de conteudo (JSON):
    {"itens": [ {"paragraph": "<p>Texto...</p>"} ]}
Cada item precisa trazer todos os campos de texto do modelo (campos_texto_item) e pode trazer
qualquer outro campo que exista no item de exemplo; o resto e' herdado do exemplo.

Uso:
    python inserir_bloco.py ../trabalho/curso_E0.json --modelo ../modelos/text__text__paragraph.json \
        --conteudo ../trabalho/conteudo_E1.json --licao 0 --posicao 1 --saida ../trabalho/curso_E1.json
"""
import argparse
import copy
import json
import pathlib
import sys

from ids import coletar_ids, novo_id


def regenerar_ids(obj, caminho, formatos, existentes):
    """Da' ID novo a todo objeto num nivel que, no modelo, tem ID (ex.: 'item', 'item.answers').

    O ID e' criado mesmo que a chave nao exista: alternativas vindas do arquivo de conteudo, por
    exemplo, chegam sem 'id'. O id fica como primeira chave, como o Rise grava.
    """
    if isinstance(obj, dict):
        if caminho in formatos:
            resto = {k: v for k, v in obj.items() if k != 'id'}
            obj.clear()
            obj['id'] = novo_id(formatos[caminho], existentes)
            obj.update(resto)
        elif 'id' in obj:
            raise SystemExit(f'Modelo nao informa formato de ID para "{caminho}".')
        for k, v in obj.items():
            if isinstance(v, (list, dict)):
                regenerar_ids(v, f'{caminho}.{k}', formatos, existentes)
    elif isinstance(obj, list):
        for v in obj:
            regenerar_ids(v, caminho, formatos, existentes)


def montar_item(modelo, conteudo_item, n):
    exemplo = modelo['item_exemplo']
    extras = set(conteudo_item) - set(exemplo)
    if extras:
        raise SystemExit(f'Item {n}: campos que o modelo nao tem: {sorted(extras)}')
    # listas e objetos (ex.: answers, front/back do flashcard, media) tambem sao obrigatorios:
    # herdar os do exemplo traria o conteudo de outro bloco para dentro do bloco novo
    compostos = [k for k, v in exemplo.items() if isinstance(v, (list, dict))]
    listas = [k for k in compostos if isinstance(exemplo[k], list)]
    obrigatorios = modelo['campos_texto_item'] + compostos + modelo.get('campos_obrigatorios', [])
    faltando = [c for c in dict.fromkeys(obrigatorios) if c not in conteudo_item]
    if faltando:
        raise SystemExit(f'Item {n}: faltam campos obrigatorios: {faltando}')
    for k in listas:
        chaves_modelo = set(exemplo[k][0]) - {'id'} if exemplo[k] else set()
        for m, el in enumerate(conteudo_item[k]):
            if set(el) != chaves_modelo:
                raise SystemExit(f'Item {n}, {k}[{m}]: campos {sorted(set(el))} '
                                 f'diferem do modelo {sorted(chaves_modelo)} (sem o id)')
    item = copy.deepcopy(exemplo)
    item.update(copy.deepcopy(conteudo_item))
    # lista numerada: sem numeracao explicita, numera na ordem (senao todos herdariam o "1" do exemplo)
    if 'number' in exemplo and 'number' not in conteudo_item:
        item['number'] = str(n + 1)
    return item


def tipo_ok(valor, regra):
    if isinstance(regra, list):
        return valor in regra
    return {'bool': lambda v: isinstance(v, bool),
            'number': lambda v: isinstance(v, (int, float)) and not isinstance(v, bool)}[regra](valor)


def construir_bloco(modelo, itens, existentes, settings=None):
    """Monta um bloco completo a partir do modelo e dos itens de conteudo, com IDs ineditos.

    `settings` (opcional) ajusta chaves que o modelo declara em "settings_ajustaveis"; qualquer
    outra chave e' recusada, para nao inventar configuracao que o Rise nao conhece.
    """
    if not itens:
        raise SystemExit(f'Bloco {modelo["chave"]}: conteudo sem "itens".')
    formatos = modelo['formato_id']
    bloco = copy.deepcopy(modelo['bloco'])
    ajustaveis = modelo.get('settings_ajustaveis', {})
    for k, v in (settings or {}).items():
        if k not in ajustaveis:
            raise SystemExit(f'Bloco {modelo["chave"]}: setting "{k}" nao e ajustavel neste modelo '
                             f'(ajustaveis: {sorted(ajustaveis) or "nenhum"}).')
        if not tipo_ok(v, ajustaveis[k]):
            raise SystemExit(f'Bloco {modelo["chave"]}: setting "{k}"={v!r} fora do permitido ({ajustaveis[k]}).')
        bloco['settings'][k] = v
    bloco['id'] = novo_id(formatos['bloco'], existentes)
    bloco['globalBlockId'] = novo_id(formatos['globalBlockId'], existentes)
    bloco['items'] = [montar_item(modelo, it, n) for n, it in enumerate(itens)]
    regenerar_ids(bloco['items'], 'item', formatos, existentes)
    return bloco


def localizar_licao(curso, posicao_licao, indice):
    licao = next((l for l in curso['course']['lessons'] if l['position'] == posicao_licao), None)
    if licao is None or licao['type'] != 'blocks':
        raise SystemExit(f'Licao {posicao_licao} nao existe ou nao e do tipo "blocks".')
    if not 0 <= indice <= len(licao['items']):
        raise SystemExit(f'Posicao {indice} fora da licao (0..{len(licao["items"])}).')
    return licao


def main():
    p = argparse.ArgumentParser()
    p.add_argument('curso_json')
    p.add_argument('--modelo', required=True)
    p.add_argument('--conteudo', required=True)
    p.add_argument('--licao', type=int, required=True, help='position da licao (0 = primeira)')
    p.add_argument('--posicao', type=int, required=True, help='indice que o bloco novo vai ocupar')
    p.add_argument('--saida', required=True)
    args = p.parse_args()

    saida = pathlib.Path(args.saida)
    if saida.exists():
        raise SystemExit(f'{saida} ja existe. Nada foi gravado.')

    curso = json.loads(pathlib.Path(args.curso_json).read_text(encoding='utf-8-sig'))
    modelo = json.loads(pathlib.Path(args.modelo).read_text(encoding='utf-8-sig'))
    conteudo = json.loads(pathlib.Path(args.conteudo).read_text(encoding='utf-8-sig'))

    licao = localizar_licao(curso, args.licao, args.posicao)
    bloco = construir_bloco(modelo, conteudo.get('itens'), coletar_ids(curso))
    licao['items'].insert(args.posicao, bloco)
    saida.write_text(json.dumps(curso, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f'Bloco {modelo["chave"]} inserido na licao {args.licao} ("{licao["title"]}"), indice {args.posicao}')
    print(f'   id            : {bloco["id"]}')
    print(f'   globalBlockId : {bloco["globalBlockId"]}')
    for it in bloco['items']:
        print(f'   item id       : {it["id"]}')
    print(f'Gravado: {saida}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
