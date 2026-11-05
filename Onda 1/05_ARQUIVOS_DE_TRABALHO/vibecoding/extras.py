import json,sys
d=json.load(open(sys.argv[1],encoding='utf-8'));c=d['course']
print('DESC:',c['description']); print('TITLE:',c['title'])
for li,l in enumerate(c['lessons']):
    def walk(n,p):
        if isinstance(n,dict):
            for k,v in n.items():
                if k in('matchTitle','feedbackCorrect','feedbackIncorrect','completeHint','feedbackPartial') and isinstance(v,str) and v: print(li,p+'.'+k,'=',v)
                else: walk(v,p+'.'+k if p else k)
        elif isinstance(n,list):
            for i,v in enumerate(n): walk(v,f'{p}.{i}')
    walk(l,'')
    for k in l:
        if isinstance(l[k],str) and k not in('id','type','courseId','createdAt','updatedAt','lastUpdatedBy','icon','author'): print(li,'LESSON',k,'=',l[k][:150])
