import json,sys,pathlib
pasta=pathlib.Path(sys.argv[1]); n=int(sys.argv[2]); idx=[int(x) for x in sys.argv[3].split(',')]
arq=sorted(pasta.glob(f'licao_{n:02d}_*.json'))[0]
L=json.loads(arq.read_text(encoding='utf-8'))['lesson']
for i in idx:
    print(f'=== L{n} [{i}]'); print(json.dumps(L['items'][i],ensure_ascii=False,indent=1)[:int(sys.argv[4]) if len(sys.argv)>4 else 6000])
