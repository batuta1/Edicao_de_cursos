"""Remove dos mapas as entradas cujo texto novo e igual ao original. Uso: python limpar_mapas.py pasta_licoes revisao_textos"""
import json, pathlib, sys
pasta, mapas = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
for arq in sorted(pasta.glob('licao_*.json')):
    d = json.loads(arq.read_text(encoding='utf-8'))
    mp = mapas / f'L{d["numero_da_licao"]:02d}.json'
    if not mp.exists(): continue
    m = json.loads(mp.read_text(encoding='utf-8')); n = {}
    for c, v in m.items():
        no = d['lesson']
        for p in c.split('.'): no = no[int(p)] if p.isdigit() else no[p]
        if no != v: n[c] = v
        else: print('removido', mp.name, c)
    mp.write_text(json.dumps(n, ensure_ascii=False, indent=2), encoding='utf-8')
