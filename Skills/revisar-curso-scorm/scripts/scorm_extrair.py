"""
Fase 1+2 do pipeline: detecta o formato do pacote SCORM, extrai o payload Base64,
desserializa para JSON e CONFERE A IDENTIDADE do curso antes de gravar.

A conferencia de identidade nao e' burocracia: ja houve um caso real neste projeto em que
um arquivo de curso Hands-on foi gravado com o conteudo do curso Essentials (mesmo hash),
e o erro so' apareceu dias depois. O --titulo-esperado existe para travar isso na origem.

Uso:
    python scorm_extrair.py PACOTE.zip --saida curso.json --titulo-esperado "Curso - Trilha"
    python scorm_extrair.py PACOTE.zip --so-inspecionar
"""
import argparse
import base64
import json
import pathlib
import re
import sys
import zipfile

ALVO_DEFAULT = 'scormcontent/runtime-data.js'
ALVO_LEGACY = 'scormcontent/index.html'
PADRAO_DEFAULT = r'__jsonp\("runtime-data\.js","([A-Za-z0-9+/=]+)"\)'
PADRAO_LEGACY = r'deserialize\("([A-Za-z0-9+/=]+)"\)'


def detectar_formato(zf):
    nomes = zf.namelist()
    if ALVO_DEFAULT in nomes:
        return 'default', ALVO_DEFAULT, PADRAO_DEFAULT
    if ALVO_LEGACY in nomes:
        return 'legacy', ALVO_LEGACY, PADRAO_LEGACY
    raise SystemExit(
        'FORMATO DESCONHECIDO. Nem runtime-data.js nem index.html encontrados em scormcontent/.\n'
        f'Primeiros arquivos do pacote: {nomes[:15]}'
    )


def extrair(caminho_zip):
    zf = zipfile.ZipFile(caminho_zip)
    formato, alvo, padrao = detectar_formato(zf)
    texto = zf.read(alvo).decode('utf-8')
    m = re.search(padrao, texto)
    if not m:
        raise SystemExit(f'PAYLOAD NAO ENCONTRADO em {alvo} (formato detectado: {formato}).')
    b64 = m.group(1)
    dados = json.loads(base64.b64decode(b64 + '=' * (-len(b64) % 4)).decode('utf-8'))
    return formato, alvo, dados, len(zf.namelist())


def main():
    p = argparse.ArgumentParser(description='Extrai e desserializa o curso de um pacote SCORM.')
    p.add_argument('pacote', help='caminho do .zip SCORM')
    p.add_argument('--saida', help='arquivo .json de saida (ex.: cursoClaudeDesignEssentials.json)')
    p.add_argument('--titulo-esperado', help='trava de seguranca: aborta se o titulo divergir')
    p.add_argument('--so-inspecionar', action='store_true',
                   help='apenas mostra formato/titulo/licoes, sem gravar nada')
    args = p.parse_args()

    formato, alvo, dados, n_arquivos = extrair(args.pacote)
    curso = dados['course']
    titulo = curso.get('title')
    licoes = sorted(curso.get('lessons', []), key=lambda x: x.get('position', 0))

    print(f'Formato          : {formato}  ({alvo})')
    print(f'Arquivos no .zip : {n_arquivos}')
    print(f'Titulo           : {titulo}')
    print(f'course.id        : {curso.get("id")}')
    print(f'Licoes           : {len(licoes)}')
    for l in licoes:
        print(f'   {l.get("position")}: {l.get("title")}  [{l.get("id")}]')

    if args.titulo_esperado and titulo != args.titulo_esperado:
        print()
        print(f'!! TITULO DIVERGENTE — esperado {args.titulo_esperado!r}, obtido {titulo!r}')
        print('   Nada foi gravado. Confira se o pacote e o curso sao mesmo os que voce espera.')
        return 1

    if args.so_inspecionar or not args.saida:
        return 0

    destino = pathlib.Path(args.saida)
    if destino.exists():
        try:
            antigo = json.loads(destino.read_text(encoding='utf-8'))
            print()
            print(f'ATENCAO: {destino.name} ja existe (titulo atual: {antigo["course"].get("title")!r}).')
            print('   Sera sobrescrito.')
        except Exception:
            pass

    destino.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding='utf-8')
    print()
    print(f'Gravado: {destino}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
