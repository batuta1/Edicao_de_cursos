"""Lista folhas de texto das licoes que continuam iguais ao original (candidatas a ingles nao traduzido)."""
import json, pathlib, sys
CAMPOS = {'paragraph','description','heading','title','feedback','caption','matchTitle','feedbackCorrect','feedbackIncorrect','completeHint','label','text'}
curso, pasta = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
orig = {l['id']: l for l in json.loads(curso.read_text(encoding='utf-8'))['course']['lessons']}
def walk(a, b, cam):
    if isinstance(a, dict):
        for k in a:
            if k in CAMPOS and isinstance(a[k], str) and a[k].strip() and a[k] == b[k]: print('  ', cam + '.' + k, '=', a[k][:100])
            else: walk(a[k], b[k], cam + '.' + k)
    elif isinstance(a, list):
        for i, (x, y) in enumerate(zip(a, b)): walk(x, y, f'{cam}.{i}')
for arq in sorted(pasta.glob('licao_*.json')):
    d = json.loads(arq.read_text(encoding='utf-8'))
    print(arq.name[:40]); walk(d['lesson'], orig[d['lesson']['id']], '')
