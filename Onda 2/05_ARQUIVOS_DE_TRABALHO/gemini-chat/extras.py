import json,sys,pathlib
pasta=pathlib.Path(sys.argv[1])
for arq in sorted(pasta.glob('licao_*.json')):
    L=json.loads(arq.read_text(encoding='utf-8'))['lesson']
    for i,b in enumerate(L['items']):
        subs = b.get('items',[]) if b.get('type')=='knowledgeCheck' else ([b] if b.get('answers') is not None else [])
        for s in subs:
            print(arq.name[:8],i,s.get('type'),'| correct:',[k for k,a in enumerate(s.get('answers',[])) if a.get('correct')])
            for k in ('feedbackCorrect','feedbackIncorrect','feedback'):
                if s.get(k): print('   ',k,'=',s[k])
            for a in s.get('answers',[]):
                if 'matchTitle' in a: print('    match:',a['title'],'->',a['matchTitle'])
        if b.get('variant')=='sorting':
            piles={p['id']:p['title'] for p in b['piles']}
            print(arq.name[:8],i,'SORTING',[(x['title'],piles.get(x.get('pileId'))) for x in b['items']])
