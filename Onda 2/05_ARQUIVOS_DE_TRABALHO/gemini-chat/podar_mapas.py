"""Remove dos mapas as entradas cujo texto novo e igual ao original (nao sao edicoes)."""
import json,pathlib,sys
curso=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
L=sorted(curso['course']['lessons'],key=lambda l:l['position'])
for m in sorted(pathlib.Path(sys.argv[2]).glob('L*.json')):
    d=json.loads(m.read_text(encoding='utf-8')); lic=L[int(m.stem[1:])-1]; fora=[]
    for c,v in list(d.items()):
        no=lic; ps=c.split('.')
        for p in ps[:-1]: no=no[int(p)] if p.isdigit() else no[p]
        if no.get(ps[-1])==v: fora.append(c); del d[c]
    if fora: m.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8'); print(m.name,'removidas:',fora)
