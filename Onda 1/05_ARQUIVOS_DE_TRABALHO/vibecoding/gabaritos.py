import json,sys
d=json.load(open(sys.argv[1],encoding='utf-8'))
for li,l in enumerate(d['course']['lessons']):
    for bi,b in enumerate(l['items']):
        qs = b['items'] if b.get('type')=='knowledgeCheck' else ([b] if 'answers' in b else [])
        for q in qs:
            ans=q.get('answers',[])
            print(li,bi,b.get('type'),'correct=',[i for i,a in enumerate(ans) if a.get('correct')], 'keys:',sorted(k for k in q if k not in('answers',)) if li==len(d['course']['lessons'])-1 and bi<1 else '')
