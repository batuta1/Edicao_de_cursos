"""Troca a correta da questão da agenda (Lição 7, bloco 13): de 'Verde; somente leitura' (alt. 1) para
'Amarelo; leitura liberada e escrita em Needs approval' (alt. 4). Autorizado em 18/10/2026."""
import json, pathlib
f = next((pathlib.Path(__file__).resolve().parent / 'licoes_extraidas_MCPEssentials').glob('licao_07_*.json'))
t = f.read_text(encoding='utf-8'); d = json.loads(t)
ans = d['lesson']['items'][13]['items'][0]['answers']
assert [a['correct'] for a in ans] == [True, False, False, False], 'estado inesperado'
ans[0]['correct'] = False; ans[3]['correct'] = True
f.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8'); print('gabarito trocado:', [a['correct'] for a in ans])
