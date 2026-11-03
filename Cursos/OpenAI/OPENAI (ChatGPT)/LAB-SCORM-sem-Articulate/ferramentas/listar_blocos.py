"""
Lista os blocos de uma licao, com indice, tipo e inicio do texto — para escolher onde inserir.

Uso:
    python listar_blocos.py ../trabalho/curso.json --licao 0
"""
import argparse
import json
import pathlib
import re
import sys


def resumo(bloco):
    textos = []
    for it in bloco.get('items') or []:
        for k in ('heading', 'paragraph', 'title', 'description'):
            if isinstance(it.get(k), str) and it[k]:
                textos.append(re.sub(r'<[^>]+>', ' ', it[k]))
                break
    return re.sub(r'\s+', ' ', ' | '.join(textos)).strip()[:90]


def main():
    p = argparse.ArgumentParser()
    p.add_argument('curso_json')
    p.add_argument('--licao', type=int, required=True, help='position da licao (0 = primeira)')
    args = p.parse_args()

    curso = json.loads(pathlib.Path(args.curso_json).read_text(encoding='utf-8-sig'))
    licao = next(l for l in curso['course']['lessons'] if l['position'] == args.licao)
    print(f'Licao {args.licao}: {licao["title"]}  ({len(licao["items"])} blocos)')
    for i, b in enumerate(licao['items']):
        tipo = f'{b.get("type")}/{b.get("variant")}'
        print(f'  [{i:2d}] {tipo:32s} {resumo(b)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
