"""
Verifica a consistencia de um pacote SCORM 1.2 exportado pelo Articulate Rise 360.

Serve para qualquer pacote do Rise (original, revisado ou com blocos inseridos). Responde a pergunta
"este .zip esta inteiro e coerente?" antes de ele ir para a LMS. Cada checagem imprime OK, AVISO ou
ERRO. Sai com codigo 1 se houver qualquer ERRO.

  1. Pacote     : o .zip abre, nenhum arquivo corrompido (CRC), arquivos essenciais presentes.
  2. Manifest   : XML valido; todo <file href> existe no pacote; arquivos de conteudo fora do manifest.
  3. Versao     : coursePackageVersion igual no manifest, no index.html e no indexAPI.html.
  4. Curso      : runtime-data.js decodifica (Base64 -> JSON) e tem curso e licoes.
  5. Estrutura  : licoes com position 0..n-1; courseId coerente; quizId aponta para a licao de quiz;
                  todos os IDs unicos; todo bloco com id, type e items.
  6. Tipos      : todo tipo de bloco (family/variant) existe no player deste pacote.
  7. Regras     : knowledgeCheck multiple choice com 1 correta; Continue com type valido;
                  gabaritos apontando para alternativas (aviso: o proprio Rise as vezes grava errado).
  8. Arquivos   : blocos HTML "cdn" com assets/<pasta>/index.html no pacote; HTML "inline" com srcdoc;
                  midias citadas pelo curso presentes em scormcontent/assets/.
  9. Comparacao : (com --original) nada removido; nada alterado fora de runtime-data.js e manifest;
                  arquivos novos so em scormcontent/assets/.

Uso:
    python verificar_scorm.py PACOTE.zip
    python verificar_scorm.py PACOTE-NOVO.zip --original PACOTE-ORIGINAL.zip
"""
import argparse
import base64
import collections
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

ALVO = 'scormcontent/runtime-data.js'
MANIFEST = 'imsmanifest.xml'
INDEX = 'scormcontent/index.html'
DRIVER = 'scormdriver/indexAPI.html'
ESSENCIAIS = [MANIFEST, INDEX, ALVO, DRIVER, 'scormdriver/scormdriver.js']
ENVELOPE = re.compile(r'^__jsonp\("runtime-data\.js","([A-Za-z0-9+/=]+)"\);?\s*$', re.S)
EXT_MIDIA = ('.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.mp4', '.mp3', '.m4a', '.wav',
             '.webm', '.pdf', '.vtt')
TIPOS_CONTINUE = ('', 'completeBlock', 'completeAll')


class Relatorio:
    def __init__(self):
        self.erros = self.avisos = 0

    def secao(self, titulo):
        print(f'\n== {titulo}')

    def ok(self, msg):
        print(f'   OK     {msg}')

    def aviso(self, msg):
        self.avisos += 1
        print(f'   AVISO  {msg}')

    def erro(self, msg):
        self.erros += 1
        print(f'   ERRO   {msg}')


def percorrer(obj, fn, caminho='$'):
    """Chama fn(chave, valor, caminho) para todo par chave/valor do JSON."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            fn(k, v, f'{caminho}.{k}')
            percorrer(v, fn, f'{caminho}.{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            percorrer(v, fn, f'{caminho}[{i}]')


def checar_pacote(z, r):
    r.secao('1. Pacote')
    corrompido = z.testzip()
    if corrompido:
        r.erro(f'arquivo corrompido no .zip: {corrompido}')
    else:
        r.ok(f'.zip integro ({len(z.namelist())} arquivos, CRC conferido)')
    faltando = [e for e in ESSENCIAIS if e not in z.namelist()]
    if faltando:
        r.erro(f'arquivos essenciais ausentes: {faltando}')
    else:
        r.ok('arquivos essenciais presentes (manifest, index.html, runtime-data.js, driver SCORM)')
    return not faltando and not corrompido


def checar_manifest(z, r):
    r.secao('2. Manifest')
    texto = z.read(MANIFEST).decode('utf-8')
    try:
        raiz = ET.fromstring(texto)
    except ET.ParseError as e:
        r.erro(f'imsmanifest.xml nao e XML valido: {e}')
        return texto
    r.ok('imsmanifest.xml e XML valido')
    nomes = set(z.namelist())
    ns = {'c': 'http://www.imsproject.org/xsd/imscp_rootv1p1p2'}
    recursos = raiz.findall('.//c:resource', ns)
    for rec in recursos:
        href = rec.get('href')
        if href and href not in nomes:
            r.erro(f'resource aponta para {href}, que nao existe no pacote')
    listados = [f.get('href') for f in raiz.findall('.//c:file', ns)]
    ausentes = [h for h in listados if h not in nomes]
    if ausentes:
        r.erro(f'{len(ausentes)} arquivo(s) listados no manifest nao existem no pacote: {ausentes[:5]}')
    else:
        r.ok(f'os {len(listados)} arquivos listados no manifest existem no pacote')
    repetidos = [h for h, n in collections.Counter(listados).items() if n > 1]
    if repetidos:
        r.aviso(f'arquivos listados mais de uma vez no manifest: {repetidos[:5]}')
    fora = sorted(n for n in nomes if n.startswith(('scormcontent/', 'scormdriver/'))
                  and not n.endswith('/') and n not in set(listados))
    if fora:
        r.aviso(f'{len(fora)} arquivo(s) de conteudo fora do manifest (algumas LMS nao os entregam): {fora[:5]}')
    else:
        r.ok('todo arquivo de conteudo esta listado no manifest')
    return texto


def checar_versao(z, manifest, r):
    r.secao('3. Versao do pacote')
    driver = z.read(DRIVER).decode('utf-8', 'replace')
    index = z.read(INDEX).decode('utf-8', 'replace')
    m_drv = re.search(r'"coursePackageVersion"\s*:\s*"([^"]+)"', driver)
    m_idx = re.search(r'course package version:\s*(\S+)', index)
    m_man = re.search(r'<manifest[^>]*\bidentifier="([^"]+)"', manifest)
    if not m_drv:
        r.erro('coursePackageVersion nao encontrado em scormdriver/indexAPI.html')
        return
    versao = m_drv.group(1)
    if m_idx and m_idx.group(1) != versao:
        r.erro(f'versao no index.html ({m_idx.group(1)}) difere do indexAPI.html ({versao})')
    if m_man and not m_man.group(1).endswith(versao):
        r.erro(f'identifier do manifest ({m_man.group(1)}) nao termina com a versao {versao}')
    if (not m_idx or m_idx.group(1) == versao) and (not m_man or m_man.group(1).endswith(versao)):
        r.ok(f'versao {versao} coerente no manifest, index.html e indexAPI.html')


def checar_curso(z, r):
    r.secao('4. Curso (runtime-data.js)')
    texto = z.read(ALVO).decode('utf-8')
    m = ENVELOPE.match(texto)
    if not m:
        r.erro('runtime-data.js fora do formato __jsonp("runtime-data.js","BASE64")')
        return None
    try:
        dados = json.loads(base64.b64decode(m.group(1)).decode('utf-8'))
    except Exception as e:  # noqa: BLE001 — qualquer falha aqui significa curso ilegivel
        r.erro(f'payload nao decodifica para JSON: {e}')
        return None
    curso = dados.get('course') or {}
    licoes = curso.get('lessons') or []
    if not licoes:
        r.erro('curso sem licoes')
        return None
    blocos = sum(len(l.get('items') or []) for l in licoes)
    r.ok(f'"{curso.get("title")}" — {len(licoes)} licoes, {blocos} blocos')
    return dados


def checar_estrutura(dados, r):
    r.secao('5. Estrutura')
    curso = dados['course']
    licoes = curso['lessons']
    posicoes = sorted(l.get('position') for l in licoes)
    if posicoes != list(range(len(licoes))):
        r.erro(f'positions das licoes nao sao 0..{len(licoes) - 1}: {posicoes}')
    else:
        r.ok('positions das licoes em sequencia')
    errados = [l.get('title') for l in licoes if l.get('courseId') != curso.get('id')]
    if errados:
        r.erro(f'licoes com courseId diferente do curso: {errados[:3]}')
    agg = (dados.get('exportAggregate') or {}).get('courseId')
    if agg and agg != curso.get('id'):
        r.erro('exportAggregate.courseId diferente de course.id')
    if not errados and (not agg or agg == curso.get('id')):
        r.ok('courseId coerente em todas as licoes')
    quiz_id = (curso.get('exportSettings') or {}).get('quizId')
    if quiz_id:
        alvo = [l for l in licoes if l.get('id') == quiz_id]
        if not alvo or alvo[0].get('type') != 'quiz':
            r.erro(f'exportSettings.quizId ({quiz_id}) nao aponta para uma licao de quiz')
        else:
            r.ok('quizId aponta para a licao de quiz')

    ids = []
    percorrer(curso, lambda k, v, c: ids.append((v, c)) if k in ('id', 'globalBlockId') and isinstance(v, str) and v else None)
    contagem = collections.Counter(v for v, _ in ids)
    repetidos = [v for v, n in contagem.items() if n > 1]
    if repetidos:
        for v in repetidos[:5]:
            r.erro(f'ID repetido {v} em {[c for x, c in ids if x == v][:3]}')
    else:
        r.ok(f'{len(ids)} IDs, todos unicos')

    incompletos = []
    for l in licoes:
        for i, b in enumerate(l.get('items') or []):
            if not b.get('id') or not b.get('type') or not isinstance(b.get('items', []), list):
                incompletos.append(f'licao {l.get("position")} bloco {i}')
    if incompletos:
        r.erro(f'blocos sem id/type/items: {incompletos[:5]}')
    else:
        r.ok('todos os blocos tem id, type e items')


def checar_tipos(z, dados, r):
    r.secao('6. Tipos de bloco x player do pacote')
    player = ''.join(z.read(n).decode('utf-8', 'replace') for n in z.namelist()
                     if n.startswith('scormcontent/lib/rise/') and n.endswith('.js'))
    if '"text/paragraph"' not in player:
        r.aviso('nao achei a tabela de tipos no player (versao diferente do Rise?) — checagem pulada')
        return
    tipos = collections.Counter()
    for l in dados['course']['lessons']:
        if l.get('type') != 'blocks':
            continue
        for b in l.get('items') or []:
            tipos[f'{b.get("family")}/{b.get("variant")}'] += 1
    desconhecidos = [t for t in tipos if f'"{t}"' not in player]
    for t in desconhecidos:
        r.erro(f'tipo "{t}" ({tipos[t]} bloco(s)) nao existe no player deste pacote — nao sera exibido')
    if not desconhecidos:
        r.ok(f'{len(tipos)} tipos de bloco, todos conhecidos pelo player')


def checar_regras(dados, r):
    r.secao('7. Regras de questoes e Continue')
    problemas = 0
    for l in dados['course']['lessons']:
        for i, b in enumerate(l.get('items') or []):
            onde = f'licao {l.get("position")} bloco {i}'
            if b.get('type') == 'knowledgeCheck' and b.get('variant') == 'multiple choice':
                for it in b.get('items') or []:
                    corretas = sum(1 for a in it.get('answers') or [] if a.get('correct') is True)
                    if corretas != 1:
                        problemas += 1
                        r.erro(f'{onde}: multiple choice com {corretas} alternativas corretas')
            if b.get('family') == 'continue':
                for it in b.get('items') or []:
                    if it.get('type', '') not in TIPOS_CONTINUE:
                        problemas += 1
                        r.erro(f'{onde}: Continue com type {it.get("type")!r}')
    if not problemas:
        r.ok('questoes multiple choice com 1 correta; Continues com type valido')

    quebrados = []

    def gabarito(o):
        # questoes ficam dentro de listas (items[]), por isso a busca e' propria, nao via percorrer()
        if isinstance(o, dict):
            if isinstance(o.get('answers'), list):
                validos = {a.get('id') for a in o['answers']}
                refs = ([o['correct']] if isinstance(o.get('correct'), str) else []) + \
                       [x for x in o.get('corrects') or [] if isinstance(x, str)]
                quebrados.extend((o.get('id'), x) for x in refs if x not in validos)
            for v in o.values():
                gabarito(v)
        elif isinstance(o, list):
            for v in o:
                gabarito(v)
    gabarito(dados['course'])
    for qid, ref in sorted(set(quebrados)):
        r.aviso(f'questao {qid}: correct/corrects = {ref[:45]!r} nao e id de alternativa '
                f'(o Rise as vezes grava assim; a correcao usa answers[].correct)')
    if not quebrados:
        r.ok('gabaritos (correct/corrects) apontam para alternativas existentes')


def checar_arquivos(z, dados, r):
    r.secao('8. Arquivos usados pelo curso')
    nomes = set(z.namelist())
    problemas = 0
    for l in dados['course']['lessons']:
        for i, b in enumerate(l.get('items') or []):
            onde = f'licao {l.get("position")} bloco {i}'
            if b.get('family') == 'html' and b.get('variant') == 'cdn':
                for it in b.get('items') or []:
                    src = (((it.get('media') or {}).get('sandbox')) or {}).get('src')
                    if f'scormcontent/assets/{src}/index.html' not in nomes:
                        problemas += 1
                        r.erro(f'{onde}: bloco HTML aponta para assets/{src}/index.html, ausente no pacote')
            if b.get('family') == 'html' and b.get('variant') == 'inline':
                if not all((it.get('srcdoc') or '').strip() for it in b.get('items') or []):
                    problemas += 1
                    r.erro(f'{onde}: bloco HTML inline sem srcdoc')
            if b.get('family') == 'html' and 'scormcontent/lib/sandbox/sandbox.html' not in nomes:
                problemas += 1
                r.erro(f'{onde}: bloco HTML, mas o pacote nao tem lib/sandbox/sandbox.html')
    if not problemas:
        r.ok('blocos HTML com conteudo e pastas presentes (se houver)')

    # midias exportadas sao citadas pelo nome do arquivo (ex.: "stock-image.jpg"); caminhos como
    # "rise/courses/..." ou "rise/brands/..." sao chaves internas da plataforma de edicao, nao arquivos
    citados = set()
    percorrer(dados, lambda k, v, c: citados.add(v) if isinstance(v, str) and '/' not in v
              and '<' not in v and v.lower().endswith(EXT_MIDIA) else None)
    faltando = sorted(m for m in citados if f'scormcontent/assets/{m}' not in nomes)
    for m in faltando:
        r.aviso(f'midia citada no curso nao esta em scormcontent/assets/: {m}')
    if not faltando:
        r.ok(f'{len(citados)} midia(s) citada(s) pelo curso, todas presentes em assets/')


def comparar(z, original, r):
    r.secao('9. Comparacao com o pacote original')
    with zipfile.ZipFile(original) as zo:
        antes, depois = set(zo.namelist()), set(z.namelist())
        removidos = sorted(antes - depois)
        novos = sorted(depois - antes)
        alterados = sorted(n for n in antes & depois if zo.read(n) != z.read(n))
    if removidos:
        r.erro(f'{len(removidos)} arquivo(s) do original foram removidos: {removidos[:5]}')
    inesperados = [n for n in alterados if n not in (ALVO, MANIFEST)]
    if inesperados:
        r.erro(f'arquivos alterados alem de runtime-data.js/manifest: {inesperados[:5]}')
    fora_assets = [n for n in novos if not n.startswith('scormcontent/assets/')]
    if fora_assets:
        r.aviso(f'arquivos novos fora de scormcontent/assets/: {fora_assets[:5]}')
    if not removidos and not inesperados:
        r.ok(f'alterados: {alterados or "nenhum"}; novos: {len(novos)}'
             + (f' ({", ".join(novos[:4])}{"..." if len(novos) > 4 else ""})' if novos else ''))


def main():
    p = argparse.ArgumentParser(description='Verifica a consistencia de um SCORM do Rise 360.')
    p.add_argument('pacote')
    p.add_argument('--original', help='pacote original, para conferir o que mudou')
    args = p.parse_args()

    r = Relatorio()
    print(f'Verificando {args.pacote}')
    try:
        z = zipfile.ZipFile(args.pacote)
    except (zipfile.BadZipFile, FileNotFoundError) as e:
        print(f'   ERRO   nao foi possivel abrir o pacote: {e}')
        return 1
    with z:
        if checar_pacote(z, r):
            manifest = checar_manifest(z, r)
            checar_versao(z, manifest, r)
            dados = checar_curso(z, r)
            if dados:
                checar_estrutura(dados, r)
                checar_tipos(z, dados, r)
                checar_regras(dados, r)
                checar_arquivos(z, dados, r)
            if args.original:
                comparar(z, args.original, r)

    print(f'\nResultado: {r.erros} erro(s), {r.avisos} aviso(s).')
    print('REPROVADO — nao envie este pacote para a LMS.' if r.erros else
          'APROVADO — pacote consistente.' + (' Leia os avisos.' if r.avisos else ''))
    return 1 if r.erros else 0


if __name__ == '__main__':
    sys.exit(main())
