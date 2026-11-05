import json,sys
a=json.load(open(sys.argv[1],encoding='utf-8'));b=json.load(open(sys.argv[2],encoding='utf-8'))
la,lb=a['labelSet'],b['labelSet']
print('A',{k:v for k,v in la.items() if k!='labels'}); print('B',{k:v for k,v in lb.items() if k!='labels'})
ka,kb=set(la['labels']),set(lb['labels'])
print('so A',len(ka-kb),sorted(ka-kb)[:20]); print('so B',len(kb-ka),sorted(kb-ka)[:20]); print('comum',len(ka&kb))
for k in ['start','continue','lessonComplete','quizSubmit','next','previous','exitMessage','salutation']:
  print(k, la['labels'].get(k),'|',lb['labels'].get(k))
print([k for k in a if k not in('course',)], a.get('labelSet',{}).get('id'))
