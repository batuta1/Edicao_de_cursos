import json,glob,sys
d=json.load(open(glob.glob(sys.argv[1])[0],encoding='utf-8'))
for i in sys.argv[2:]:
    p=i.split('.')
    n=d['lesson']
    for k in p: n=n[int(k)] if k.isdigit() else n[k]
    print(json.dumps(n,ensure_ascii=False)[:3000]); print()
