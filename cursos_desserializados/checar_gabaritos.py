"""Lista cada questao (knowledge check e quiz) com o gabarito, e confere se os campos
`correct`/`corrects` apontam para ids de alternativas existentes e se batem com os booleanos
`answers[].correct`.

Uso: python checar_gabaritos.py pasta_licoes/
"""
import json
import pathlib
import sys

TIPOS = ('MULTIPLE_CHOICE', 'MULTIPLE_RESPONSE', 'TRUE_FALSE', 'FILL_IN_THE_BLANK', 'MATCHING')


def walk(obj, caminho, licao):
    if isinstance(obj, dict):
        if obj.get('type') in TIPOS and 'answers' in obj:
            ids = [a.get('id') for a in obj['answers']]
            bools = [i for i, a in enumerate(obj['answers']) if a.get('correct') is True]
            print(f'\n=== [{licao}] {caminho}  type={obj["type"]}')
            print(f'    pergunta: {obj.get("title")}')
            if 'correct' in obj:
                c = obj['correct']
                alvo = ids.index(c) if c in ids else None
                print(f'    correct  = {c!r}  -> indice {alvo}')
            if 'corrects' in obj:
                cs = obj['corrects']
                print(f'    corrects = {cs!r}  -> indices {[ids.index(c) if c in ids else None for c in cs]}')
            print(f'    booleanos correct=True nos indices: {bools}')
            for i, a in enumerate(obj['answers']):
                marca = 'CORRETA' if a.get('correct') else '       '
                print(f'    [{i}] [{marca}] {a.get("title")}')
                if a.get('feedback'):
                    print(f'                 -> {a["feedback"]}')
            for k in ('feedbackCorrect', 'feedbackIncorrect', 'feedback'):
                if obj.get(k):
                    print(f'    {k}: {obj[k]}')
        for k, v in obj.items():
            if isinstance(v, (list, dict)):
                walk(v, f'{caminho}.{k}', licao)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk(v, f'{caminho}[{i}]', licao)


for arq in sorted(pathlib.Path(sys.argv[1]).glob('licao_*.json')):
    c = json.loads(arq.read_text(encoding='utf-8'))
    walk(c['lesson'], 'lesson', arq.name[:8])
