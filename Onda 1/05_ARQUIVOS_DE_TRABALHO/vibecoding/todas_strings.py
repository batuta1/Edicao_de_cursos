"""Lista toda folha string do curso (fora das chaves claramente tecnicas), agrupando por nome de chave."""
import json, sys, collections, re
TEC = {'id','type','family','variant','key','crushedKey','src','url','courseId','lessonId','createdAt','updatedAt','originalId','duplicatedFromId','author','selectedAuthorId','icon','color','globalBlockId','shareId','media','mimeType','format','fontFamily','backgroundColor','textColor','accentColor','theme','navigationMode','transferredAt','exportSettings','originalUrl','filename','extension','touchedAt','status','fileName','mediaType','x','y'}
d = json.load(open(sys.argv[1], encoding='utf-8'))
cont = collections.defaultdict(list)
def walk(n, p):
    if isinstance(n, dict):
        for k, v in n.items(): walk(v, p + [k])
    elif isinstance(n, list):
        for i, v in enumerate(n): walk(v, p + [str(i)])
    elif isinstance(n, str):
        k = p[-1] if not p[-1].isdigit() else p[-2]
        if k in TEC or not re.search('[A-Za-z]{3}', n) or re.fullmatch(r'[\w-]{20,}', n): return
        cont[k].append(('.'.join(p), n))
walk(d, [])
for k, vs in sorted(cont.items(), key=lambda x: -len(x[1])):
    print(f'== {k} ({len(vs)})')
    for c, v in vs[:int(sys.argv[2]) if len(sys.argv)>2 else 3]: print('   ', c[:110], '=', v[:120].replace('\n',' '))
