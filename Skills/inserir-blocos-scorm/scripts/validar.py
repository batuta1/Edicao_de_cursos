"""
Valida um curso com blocos inseridos, comparando com o curso original e com o catalogo de modelos.

Checagens:
  1. Tudo fora de course.lessons[].items continua identico ao original.
  2. Em cada licao, os blocos originais continuam todos la', identicos e na mesma ordem relativa
     (so' houve insercao).
  3. Cada bloco novo bate com um modelo: type/family/variant, chaves, settings, estrutura dos
     itens e formato dos IDs.
  4. Todos os IDs do curso sao unicos.
  5. HTML dos blocos novos so' usa <p> <strong> <em> <br> <ul> <li> <span>, sem atributos.
  5b. knowledgeCheck multiple choice novo: 1 questao, exatamente 1 alternativa correta, feedback em
      todas, texto puro (sem HTML); aviso se nao tiver 4 alternativas (padrao dos nossos cursos).
  5c. Padroes por tipo: titulos de heading paragraph e de accordion em texto puro; lista numerada
      com number "1".."n" em sequencia; item do Continue identico ao padrao (so' "type" varia entre
      "", completeBlock e completeAll). settings: so' as chaves que o modelo declara ajustaveis podem
      diferir dele, e dentro dos valores permitidos.
  5d. Bloco HTML (inline): srcdoc e' documento completo e autocontido (sem src/href para http/https,
      que pode nao carregar na LMS). As regras de tags de texto rico nao se aplicam ao srcdoc.
  5e. Bloco HTML (cdn): media.sandbox.src e' o nome simples de uma pasta em scormcontent/assets/;
      srcName preenchido. A existencia da pasta (com index.html) e' conferida pelo empacotar.py.
  6. Gabaritos (correct/corrects) apontam para alternativas existentes. Problemas que ja vinham
     do original (ex.: o knowledgeCheck multiple response do curso PowerPoint, em que o Rise
     gravou texto de pergunta em correct/corrects) aparecem como aviso, nao como erro.

Sai com codigo 1 se qualquer checagem falhar.

Uso:
    python validar.py ../trabalho/curso_E1.json --original ../trabalho/curso_E0.json --modelos ../modelos/
"""
import argparse
import collections
import json
import pathlib
import re
import sys

from ids import formato_de

TAGS_OK = {'p', 'strong', 'em', 'br', 'ul', 'li', 'span'}


def forma(o):
    """Assinatura estrutural. Em listas, todos os elementos entram (formas distintas aparecem)."""
    if isinstance(o, dict):
        return {k: forma(v) for k, v in sorted(o.items())}
    if isinstance(o, list):
        unicas = {json.dumps(forma(x), sort_keys=True) for x in o}
        return [json.loads(u) for u in sorted(unicas)]
    return type(o).__name__


# campos que, nos 5 cursos, sao sempre texto puro (sem HTML)
TEXTO_PURO = {
    'text/text/heading paragraph': ['heading'],        # 83 de 83
    'interactive/interactive/accordion': ['title'],    # 100 de 100
    'interactive/interactive/tabs': ['title'],         # 18 de 18
}


# campos em que paragrafos sao separados por um <p></p> vazio (accordion 39/39, tabs 10/10);
# sem ele, o Rise mostra os paragrafos colados
SEPARADOR_P = {
    'interactive/interactive/accordion': ['description'],
    'interactive/interactive/tabs': ['description'],
}
PARAGRAFOS_COLADOS = re.compile(r'<p>(?!</p>)(?:(?!</p>).)+</p>\s*<p>(?!</p>)', re.S)


def checar_padroes(bloco, modelo, erros, onde):
    """Padroes por tipo levantados nos 5 cursos (ver DIARIO, E3-E6)."""
    chave = modelo['chave']
    itens = bloco.get('items') or []
    for campo in TEXTO_PURO.get(chave, []):
        if any('<' in (it.get(campo) or '') for it in itens):
            erros.append(f'{onde}: "{campo}" deve ser texto puro neste tipo de bloco')
    for campo in SEPARADOR_P.get(chave, []):
        if any(PARAGRAFOS_COLADOS.search(it.get(campo) or '') for it in itens):
            erros.append(f'{onde}: paragrafos de "{campo}" precisam de <p></p> vazio entre eles')
    if chave == 'list/list/numbered':
        numeros = [it.get('number') for it in itens]
        if numeros != [str(i + 1) for i in range(len(itens))]:
            erros.append(f'{onde}: numeracao da lista fora de sequencia: {numeros}')
    if chave == 'html/html/inline':
        for it in itens:
            doc = (it.get('srcdoc') or '').lower()
            if '<html' not in doc or '<body' not in doc:
                erros.append(f'{onde}: srcdoc precisa ser um documento HTML completo (<html> e <body>)')
            if re.search(r'''(src|href)\s*=\s*["']?(https?:)?//''', doc):
                erros.append(f'{onde}: srcdoc carrega recurso externo (http/https) — deve ser autocontido')
    if chave == 'html/html/cdn':
        for it in itens:
            sb = ((it.get('media') or {}).get('sandbox') or {})
            src, nome = sb.get('src') or '', sb.get('srcName') or ''
            if not re.fullmatch(r'[A-Za-z0-9_-]+', src):
                erros.append(f'{onde}: media.sandbox.src {src!r} precisa ser so o nome de uma pasta em '
                             f'scormcontent/assets/ (letras, numeros, - e _)')
            if not nome or '{{' in nome:
                erros.append(f'{onde}: media.sandbox.srcName vazio ou com marcador do modelo')
    if chave == 'divider/continue/continue':
        # nos cursos o item e' identico nos 40 casos; so' "type" pode variar, entre os 3 valores do
        # esquema do player: "" (livre), "completeBlock" (exige o bloco acima), "completeAll" (todos)
        padrao = {k: v for k, v in modelo['item_exemplo'].items() if k not in ('id', 'type')}
        for it in itens:
            if {k: v for k, v in it.items() if k not in ('id', 'type')} != padrao:
                erros.append(f'{onde}: item do Continue difere do padrao (identico nos 40 dos cursos)')
            if it.get('type') not in ('', 'completeBlock', 'completeAll'):
                erros.append(f'{onde}: Continue com type {it.get("type")!r} (validos: "", completeBlock, completeAll)')


def checar_knowledge_check(bloco, erros, avisos, onde):
    """Regras da questao de verificacao, levantadas nos 22 knowledgeCheck multiple choice dos 5 cursos."""
    itens = bloco.get('items') or []
    if len(itens) != 1:
        erros.append(f'{onde}: knowledgeCheck deve ter 1 questao (tem {len(itens)})')
    for it in itens:
        respostas = it.get('answers') or []
        corretas = sum(1 for a in respostas if a.get('correct') is True)
        if corretas != 1:
            erros.append(f'{onde}: multiple choice precisa de exatamente 1 alternativa correta (tem {corretas})')
        if len(respostas) != 4:
            avisos.append(f'{onde}: {len(respostas)} alternativas (nossos cursos usam sempre 4)')
        campos = [it.get('title', '')] + [a.get('title', '') for a in respostas] + \
                 [a.get('feedback', '') for a in respostas]
        if any('<' in c for c in campos):
            erros.append(f'{onde}: knowledgeCheck usa texto puro (sem HTML) no enunciado, alternativas e feedback')
        if any(not a.get('feedback') for a in respostas):
            erros.append(f'{onde}: toda alternativa precisa de feedback')


def ids_com_caminho(obj, caminho, acc):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ('id', 'globalBlockId') and isinstance(v, str) and v:
                acc.append((v, f'{caminho}.{k}'))
            ids_com_caminho(v, f'{caminho}.{k}', acc)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            ids_com_caminho(v, f'{caminho}[{i}]', acc)
    return acc


def textos(obj):
    """Textos ricos (com HTML) dos blocos. 'srcdoc' fica de fora: e' um documento HTML completo,
    renderizado isolado num iframe, e tem regras proprias (ver checar_padroes)."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k != 'srcdoc':
                yield from textos(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from textos(v)
    elif isinstance(obj, str) and '<' in obj:
        yield obj


def checar_bloco_novo(bloco, modelos, erros, avisos, onde):
    chave = f'{bloco.get("type")}/{bloco.get("family")}/{bloco.get("variant")}'
    modelo = modelos.get(chave)
    if modelo is None:
        erros.append(f'{onde}: nenhum modelo para {chave}')
        return
    m = modelo['bloco']
    esperado = set(m) | {'id', 'globalBlockId', 'items'}
    if set(bloco) != esperado:
        erros.append(f'{onde}: chaves {sorted(set(bloco) ^ esperado)} divergem do modelo')
    ajustaveis = modelo.get('settings_ajustaveis', {})
    s_bloco, s_modelo = bloco.get('settings') or {}, m['settings'] or {}
    if set(s_bloco) != set(s_modelo):
        erros.append(f'{onde}: chaves de settings {sorted(set(s_bloco) ^ set(s_modelo))} divergem do modelo')
    for k in set(s_bloco) & set(s_modelo):
        if k in ajustaveis:
            regra = ajustaveis[k]
            ok = s_bloco[k] in regra if isinstance(regra, list) else (
                isinstance(s_bloco[k], bool) if regra == 'bool' else
                isinstance(s_bloco[k], (int, float)) and not isinstance(s_bloco[k], bool))
            if not ok:
                erros.append(f'{onde}: setting "{k}"={s_bloco[k]!r} fora do permitido ({regra})')
        elif s_bloco[k] != s_modelo[k]:
            erros.append(f'{onde}: setting "{k}" diferente do modelo')
    fmt = modelo['formato_id']
    if formato_de(bloco.get('id')) != fmt['bloco']:
        erros.append(f'{onde}: id {bloco.get("id")!r} nao e {fmt["bloco"]}')
    if formato_de(bloco.get('globalBlockId')) != 'uuid':
        erros.append(f'{onde}: globalBlockId nao e uuid')
    for n, it in enumerate(bloco.get('items') or []):
        if forma(it) != forma(modelo['item_exemplo']):
            erros.append(f'{onde}.items[{n}]: estrutura diferente do item do modelo')
        if formato_de(it.get('id')) != fmt.get('item'):
            erros.append(f'{onde}.items[{n}]: id {it.get("id")!r} nao e {fmt.get("item")}')
        for a in it.get('answers') or []:
            if formato_de(a.get('id')) != fmt.get('item.answers'):
                erros.append(f'{onde}.items[{n}]: id de alternativa fora do formato')
    for t in textos(bloco.get('items')):
        for tag, attrs in re.findall(r'<\s*/?\s*([a-zA-Z0-9]+)([^>]*)>', t):
            if tag.lower() not in TAGS_OK:
                erros.append(f'{onde}: tag HTML nao permitida <{tag}>')
            if attrs.strip().strip('/'):
                erros.append(f'{onde}: tag <{tag}> com atributos ({attrs.strip()})')
    checar_padroes(bloco, modelo, erros, onde)
    if bloco.get('type') == 'knowledgeCheck' and bloco.get('variant') == 'multiple choice':
        checar_knowledge_check(bloco, erros, avisos, onde)


def gabaritos_quebrados(curso):
    """(id da questao, referencia) para cada correct/corrects que nao aponta para uma alternativa.

    Identifica pela ID da questao, nao pelo caminho, para comparar original x editado mesmo com
    blocos deslocados pela insercao.
    """
    achados = set()

    def visitar(o):
        if isinstance(o, dict):
            if isinstance(o.get('answers'), list):
                ids = {a.get('id') for a in o['answers']}
                refs = ([o['correct']] if isinstance(o.get('correct'), str) else []) + \
                       [r for r in o.get('corrects') or [] if isinstance(r, str)]
                achados.update((o.get('id'), r) for r in refs if r not in ids)
            for v in o.values():
                visitar(v)
        elif isinstance(o, list):
            for v in o:
                visitar(v)
    visitar(curso)
    return achados


def main():
    p = argparse.ArgumentParser()
    p.add_argument('curso_json')
    p.add_argument('--original', required=True)
    p.add_argument('--modelos', required=True)
    args = p.parse_args()

    novo = json.loads(pathlib.Path(args.curso_json).read_text(encoding='utf-8-sig'))
    orig = json.loads(pathlib.Path(args.original).read_text(encoding='utf-8-sig'))
    modelos = {}
    for arq in pathlib.Path(args.modelos).glob('*.json'):
        m = json.loads(arq.read_text(encoding='utf-8-sig'))
        modelos[m['chave']] = m
    erros, avisos = [], []

    # 1. fora dos blocos, nada muda
    def sem_blocos(d):
        d = json.loads(json.dumps(d))
        for l in d['course']['lessons']:
            l['items'] = None
        return d
    if sem_blocos(novo) != sem_blocos(orig):
        erros.append('Algo fora de lessons[].items mudou em relacao ao original')

    # 2 e 3. blocos originais preservados; blocos novos conferidos contra modelos
    licoes_orig = {l['id']: l for l in orig['course']['lessons']}
    total_novos = 0
    for licao in novo['course']['lessons']:
        originais = licoes_orig[licao['id']]['items']
        ids_orig = {b['id'] for b in originais}
        mantidos = [b for b in licao['items'] if b['id'] in ids_orig]
        if mantidos != originais:
            erros.append(f'Licao "{licao["title"]}": blocos originais alterados, removidos ou reordenados')
        for i, b in enumerate(licao['items']):
            if b['id'] not in ids_orig:
                total_novos += 1
                print(f'   bloco novo: licao {licao["position"]}, indice {i}, '
                      f'{b.get("type")}/{b.get("variant")}, id {b.get("id")}')
                checar_bloco_novo(b, modelos, erros, avisos, f'licao {licao["position"]} bloco [{i}]')

    # 4. unicidade
    todos = ids_com_caminho(novo['course'], 'course', [])
    repetidos = [i for i, n in collections.Counter(v for v, _ in todos).items() if n > 1]
    ids_licao_quiz = {novo['course']['exportSettings'].get('quizId')}
    for r in repetidos:
        if r not in ids_licao_quiz:
            erros.append(f'ID repetido: {r} em {[c for v, c in todos if v == r]}')

    # 6. gabaritos: so' reprova o que for novo; o que ja vinha do Rise vira aviso
    antes = gabaritos_quebrados(orig['course'])
    depois = gabaritos_quebrados(novo['course'])
    for qid, ref in sorted(depois - antes):
        erros.append(f'questao {qid}: gabarito {ref!r} nao corresponde a nenhuma alternativa')
    for qid, ref in sorted(depois & antes):
        print(f'   aviso (ja existia no original): questao {qid} tem correct/corrects = {ref[:50]!r}...')
    for a in avisos:
        print(f'   aviso: {a}')

    print(f'Blocos novos encontrados: {total_novos}')
    print(f'IDs no curso: {len(todos)} ({len(set(v for v, _ in todos))} distintos)')
    if erros:
        for e in erros:
            print(f'!! {e}')
        print(f'REPROVADO: {len(erros)} problema(s).')
        return 1
    print('APROVADO: so houve insercao, e os blocos novos seguem os modelos.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
