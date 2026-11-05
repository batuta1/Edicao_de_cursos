"""Separa o curso em licoes_extraidas_PerplexityHandsOn/licao_NN_<titulo>.json (formato da skill revisar-curso-scorm)."""
import json, pathlib, re, unicodedata
AQUI = pathlib.Path(__file__).resolve().parent
curso = json.loads((AQUI / 'cursoPerplexityHandsOn.json').read_text(encoding='utf-8'))
pasta = AQUI / 'licoes_extraidas_PerplexityHandsOn'
pasta.mkdir(exist_ok=False)
indice = []
for n, l in enumerate(sorted(curso['course']['lessons'], key=lambda x: x['position']), 1):
    t = unicodedata.normalize('NFKD', l['title']).encode('ascii', 'ignore').decode()
    t = re.sub(r'[^A-Za-z0-9]+', '_', t).strip('_')[:60]
    nome = f'licao_{n:02d}_{t}.json'
    (pasta / nome).write_text(json.dumps({'numero_da_licao': n, 'position_original': l['position'], 'title': l['title'], 'lesson': l}, ensure_ascii=False, indent=2), encoding='utf-8')
    indice.append({'numero_da_licao': n, 'arquivo': nome, 'title': l['title'], 'id': l['id'], 'blocos': len(l.get('items', []))})
(pasta / 'indice_licoes.json').write_text(json.dumps(indice, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(indice, ensure_ascii=False, indent=1))
