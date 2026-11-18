"""Lista o indice da alternativa correta de cada knowledgeCheck. Uso: python gabaritos.py pasta_licoes"""
import json, pathlib, sys
for arq in sorted(pathlib.Path(sys.argv[1]).glob('licao_*.json')):
    L = json.loads(arq.read_text(encoding='utf-8'))['lesson']
    for i, b in enumerate(L['items']):
        if b.get('type') == 'knowledgeCheck':
            for it in b['items']:
                c = [k for k, a in enumerate(it.get('answers', [])) if a.get('correct')]
                print(arq.name[:9], f'[{i}]', b.get('variant'), 'corretas=', c, 'n=', len(it.get('answers', [])))
