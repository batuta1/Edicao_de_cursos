"""
Monta o catalogo de modelos: um arquivo por tipo de bloco, a partir de blocos reais do curso.

Cada modelo guarda:
  - o bloco com type/family/variant/settings exatamente como o Rise gerou;
  - metadata minima {"createdVia": "ai"} (forma comprovada em 110 blocos dos nossos cursos);
  - o formato de ID de cada nivel (bloco, item, alternativa), lido do bloco real;
  - um item de exemplo, com os textos originais, so' como referencia de estrutura.

Uso:
    python catalogar_modelos.py ../trabalho/curso.json --saida ../modelos/
"""
import argparse
import copy
import json
import pathlib
import re
import sys

from ids import formato_de

CAMPOS_TEXTO = {'heading', 'paragraph', 'title', 'description', 'feedback',
                'feedbackCorrect', 'feedbackIncorrect'}


def nome_arquivo(bloco):
    partes = [bloco.get('type'), bloco.get('family'), bloco.get('variant')]
    return re.sub(r'[^a-z0-9]+', '-', '__'.join(str(p) for p in partes).lower()).strip('-') + '.json'


def formatos_internos(obj, caminho, acc):
    """Registra o formato de ID por caminho estrutural (ex.: 'item', 'item.answers')."""
    if isinstance(obj, dict):
        if 'id' in obj:
            acc.setdefault(caminho, formato_de(obj['id']))
        for k, v in obj.items():
            if isinstance(v, (list, dict)):
                formatos_internos(v, f'{caminho}.{k}', acc)
    elif isinstance(obj, list):
        for v in obj:
            formatos_internos(v, caminho, acc)
    return acc


def main():
    p = argparse.ArgumentParser()
    p.add_argument('curso_json')
    p.add_argument('--saida', required=True)
    p.add_argument('--somente', nargs='+', metavar='VARIANT',
                   help='so cataloga estes variants (ex.: tabs). Util para trazer modelos de outro curso.')
    args = p.parse_args()

    curso = json.loads(pathlib.Path(args.curso_json).read_text(encoding='utf-8-sig'))
    pasta = pathlib.Path(args.saida)
    pasta.mkdir(exist_ok=True)

    vistos = set()
    for licao in curso['course']['lessons']:
        if licao['type'] != 'blocks':      # quiz final fica fora do escopo
            continue
        for bloco in licao['items']:
            if args.somente and bloco.get('variant') not in args.somente:
                continue
            arq = nome_arquivo(bloco)
            if arq in vistos:
                continue
            vistos.add(arq)
            if (pasta / arq).exists():
                print(f'   {arq:55s} ja existe, mantido (nao sobrescreve)')
                continue
            item = copy.deepcopy((bloco.get('items') or [{}])[0])
            modelo = {
                'chave': f'{bloco.get("type")}/{bloco.get("family")}/{bloco.get("variant")}',
                'origem': {'curso': curso['course']['title'], 'licao': licao['title'],
                           'bloco_id': bloco['id']},
                'formato_id': {'bloco': formato_de(bloco['id']), 'globalBlockId': 'uuid',
                               **formatos_internos(bloco.get('items') or [], 'item', {})},
                'campos_texto_item': sorted(k for k in item if k in CAMPOS_TEXTO),
                'bloco': {
                    'type': bloco.get('type'), 'family': bloco.get('family'),
                    'variant': bloco.get('variant'), 'settings': bloco.get('settings'),
                    'metadata': {'createdVia': 'ai'},
                },
                'item_exemplo': item,
            }
            (pasta / arq).write_text(json.dumps(modelo, ensure_ascii=False, indent=2), encoding='utf-8')
            print(f'   {arq:55s} ids={modelo["formato_id"]}')
    print(f'{len(vistos)} modelos em {pasta}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
