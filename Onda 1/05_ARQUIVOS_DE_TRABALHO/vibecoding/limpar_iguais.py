"""Remove dos mapas as entradas cujo texto novo e' identico ao original (termos que nao se traduzem)."""
import json, pathlib, sys
curso, pasta, mapas = (pathlib.Path(a) for a in sys.argv[1:4])
c = json.loads(curso.read_text(encoding='utf-8'))
lic = sorted(c['course']['lessons'], key=lambda l: l['position'])
for i, l in enumerate(lic, 1):
    mp = mapas / f'L{i:02d}.json'
    if not mp.exists(): continue
    m = json.loads(mp.read_text(encoding='utf-8'))
    tirar = []
    for cam, novo in m.items():
        no = l
        for p in cam.split('.'):
            no = no[int(p)] if p.isdigit() else no[p]
        if no == novo: tirar.append(cam)
    for t in tirar: del m[t]
    if tirar:
        mp.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding='utf-8')
        print(mp.name, 'removidas', tirar)
