"""Fase 3: separa o curso em um arquivo JSON por licao (licao_NN_Titulo.json) + indice_licoes.json.

Uso: python separar_licoes.py curso.json pasta_saida/
"""
import json
import pathlib
import re
import sys
import unicodedata


def slug(texto):
    t = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')
    t = re.sub(r'[^A-Za-z0-9]+', '_', t).strip('_')
    return t[:60]


def main():
    curso_path, saida = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    curso = json.loads(curso_path.read_text(encoding='utf-8'))
    saida.mkdir(parents=True, exist_ok=True)
    if list(saida.glob('licao_*.json')):
        raise SystemExit(f'{saida} ja tem licao_*.json. Nao sobrescrevo.')

    licoes = sorted(curso['course']['lessons'], key=lambda l: l.get('position', 0))
    indice = []
    for n, licao in enumerate(licoes, start=1):
        nome = f'licao_{n:02d}_{slug(licao.get("title", ""))}.json'
        conteudo = {
            'numero_da_licao': n,
            'position_original': licao.get('position'),
            'title': licao.get('title'),
            'lesson': licao,
        }
        (saida / nome).write_text(json.dumps(conteudo, ensure_ascii=False, indent=2), encoding='utf-8')
        indice.append({'numero_da_licao': n, 'arquivo': nome, 'id': licao['id'], 'title': licao.get('title')})
        print(f'{nome}  ({len(licao.get("items", []))} blocos)')
    (saida / 'indice_licoes.json').write_text(json.dumps(indice, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
