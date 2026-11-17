"""Lista os campos de texto de cada licao com o caminho relativo a `lesson` (para montar os mapas)."""
import json, pathlib, sys
CAMPOS = {'paragraph','description','heading','title','feedback','caption','summary','intro','body','altText','placeholder','instructions','label','question','answer','text'}
def walk(no, cam, out):
    if isinstance(no, dict):
        for k, v in no.items():
            c = f'{cam}.{k}' if cam else k
            if k in CAMPOS and isinstance(v, str) and v.strip(): out.append((c, v))
            else: walk(v, c, out)
    elif isinstance(no, list):
        for i, v in enumerate(no): walk(v, f'{cam}.{i}' if cam else str(i), out)
pasta = pathlib.Path(sys.argv[1])
for arq in sorted(pasta.glob('licao_*.json')):
    d = json.loads(arq.read_text(encoding='utf-8')); L = d['lesson']
    print(f'\n######## {arq.name}  title={L["title"]!r}')
    for i, b in enumerate(L['items']):
        print(f'\n--- [{i}] {b.get("type")}/{b.get("family")}/{b.get("variant")}')
        out = []; walk(b, f'items.{i}', out)
        for c, v in out: print(f'{c} = {v}')
