"""base_v2 = curso original do Articulate + rótulos de interface em PT-BR (labelSet) e idioma pt-BR.
Autorizado pelo usuário em 18/10/2026. Reaproveita a tradução do MCP Hands-on (mesma do MCP Essentials v3) (mesmo labelSet em inglês).
Confere: mesmas chaves, só labelSet mudou, '%' preservado onde existia."""
import json, pathlib, copy
AQUI = pathlib.Path(__file__).resolve().parent
base = json.loads((AQUI / 'cursoPerplexityHandsOn.json').read_text(encoding='utf-8'))
rot = json.loads((AQUI / 'revisao_rotulos/rotulos_ptbr.json').read_text(encoding='utf-8'))
novo = copy.deepcopy(base); L = novo['labelSet']['labels']
for k, v in rot.items():
    assert k in L, f'rotulo inexistente: {k}'
    assert ('%' in L[k]) == ('%' in v), f'% divergente em {k}'
    L[k] = v
novo['labelSet']['iso639Code'] = 'pt-BR'
novo['labelSet']['name'] = 'Português (Brasil)'
a = copy.deepcopy(base); a.pop('labelSet'); b = copy.deepcopy(novo); b.pop('labelSet')
assert a == b, 'algo além do labelSet mudou'
assert novo['labelSet']['labels'].keys() == base['labelSet']['labels'].keys()
saida = AQUI / 'cursoPerplexityHandsOn_base_v2.json'; assert not saida.exists()
saida.write_text(json.dumps(novo, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'base_v2: {len(rot)} rótulos traduzidos de {len(L)}; iso639Code pt-BR')
