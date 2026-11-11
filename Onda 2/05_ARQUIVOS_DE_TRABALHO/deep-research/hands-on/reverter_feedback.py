"""Devolve feedbackCorrect/feedbackIncorrect da L03 ao original (validar_estrutura.py os trata como nao textuais)."""
import json, pathlib
AQUI = pathlib.Path(__file__).resolve().parent
curso = json.loads((AQUI / 'cursoDeepHandsOn.json').read_text(encoding='utf-8'))
arq = next((AQUI / 'licoes_extraidas_DeepHandsOn').glob('licao_03_*.json'))
d = json.loads(arq.read_text(encoding='utf-8'))
orig = {l['id']: l for l in curso['course']['lessons']}[d['lesson']['id']]
for k in ('feedbackCorrect', 'feedbackIncorrect'):
    d['lesson']['items'][7]['items'][0][k] = orig['items'][7]['items'][0][k]
arq.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8')
m = AQUI / 'revisao_textos' / 'L03.json'
mapa = json.loads(m.read_text(encoding='utf-8'))
for k in ('feedbackCorrect', 'feedbackIncorrect'): mapa.pop(f'items.7.items.0.{k}')
m.write_text(json.dumps(mapa, ensure_ascii=False, indent=2), encoding='utf-8')
print('revertido; L03 agora com', len(mapa), 'campos')
