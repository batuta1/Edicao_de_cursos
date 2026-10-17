"""
Serializa o JSON do curso de volta para Base64 e gera um pacote SCORM novo.

O pacote original nunca e' modificado. O pacote novo e' uma copia entrada por entrada, em que
so' scormcontent/runtime-data.js muda — e, se houver --anexar, o imsmanifest.xml ganha as linhas
dos arquivos anexados.

--anexar PASTA=NOME (pode repetir) copia uma pasta local para scormcontent/assets/NOME/ e registra
cada arquivo no manifest. Usado pelo bloco HTML "cdn", que carrega assets/NOME/index.html.

Ao final o script confere, e so' entao grava o .zip:
  - ida e volta: o Base64 gravado decodifica exatamente no mesmo JSON;
  - entradas originais identicas byte a byte (exceto runtime-data.js e, com anexos, o manifest);
  - o manifest so' ganhou as linhas dos anexos — removidas, volta a ser o original;
  - todo bloco html/cdn do curso aponta para uma pasta com index.html no pacote;
  - arquivos anexados sem referencia externa (http/https), que pode nao carregar na LMS.

Uso:
    python empacotar.py ../trabalho/curso.json --pacote-original ../original/X.zip --pacote-saida ../saidas/E0.zip
    python empacotar.py ../trabalho/curso_E7c.json --pacote-original ... --pacote-saida ... \
        --anexar ../trabalho/checklist_E7c=checklist-revisao
"""
import argparse
import base64
import json
import pathlib
import re
import sys
import zipfile

from extrair import ALVO, ENVELOPE, ler_payload

MANIFEST = 'imsmanifest.xml'
PREFIXO_ASSETS = 'scormcontent/assets/'
TEXTUAIS = {'.html', '.htm', '.css', '.js', '.svg'}
EXTERNO = re.compile(r'''(?:\b(?:src|href)\s*=\s*["']?|url\(\s*["']?|@import\s+["'])(?:https?:)?//''', re.I)


def serializar(curso):
    # mesmo formato que o Rise usa: JSON compacto, UTF-8, sem escapar acentos
    compacto = json.dumps(curso, ensure_ascii=False, separators=(',', ':'))
    b64 = base64.b64encode(compacto.encode('utf-8')).decode('ascii')
    if json.loads(base64.b64decode(b64).decode('utf-8')) != curso:
        raise SystemExit('IDA E VOLTA FALHOU. Nada foi gravado.')
    return b64


def ler_anexos(specs, nomes_existentes):
    """{caminho no zip: bytes} para cada --anexar PASTA=NOME, com as checagens de seguranca."""
    anexos = {}
    for spec in specs or []:
        if '=' not in spec:
            raise SystemExit(f'--anexar {spec!r}: use PASTA=NOME. Nada foi gravado.')
        pasta, nome = spec.rsplit('=', 1)
        pasta = pathlib.Path(pasta)
        if not re.fullmatch(r'[A-Za-z0-9_-]+', nome):
            raise SystemExit(f'--anexar: nome {nome!r} invalido (letras, numeros, - e _). Nada foi gravado.')
        if not (pasta / 'index.html').is_file():
            raise SystemExit(f'--anexar: {pasta} nao tem index.html. Nada foi gravado.')
        for arq in sorted(p for p in pasta.rglob('*') if p.is_file()):
            destino = f'{PREFIXO_ASSETS}{nome}/{arq.relative_to(pasta).as_posix()}'
            if destino in nomes_existentes or destino in anexos:
                raise SystemExit(f'--anexar: {destino} ja existe no pacote. Nada foi gravado.')
            dados = arq.read_bytes()
            if arq.suffix.lower() in TEXTUAIS and EXTERNO.search(dados.decode('utf-8', 'replace')):
                raise SystemExit(f'--anexar: {arq} referencia recurso externo (http/https); '
                                 f'o conteudo precisa ser autocontido. Nada foi gravado.')
            anexos[destino] = dados
    return anexos


def manifest_com_anexos(texto, caminhos):
    """Insere um <file href> por anexo antes de </resource>, no mesmo formato do Rise."""
    marca = '    </resource>'
    if texto.count(marca) != 1:
        raise SystemExit('Manifest com formato inesperado (</resource>). Nada foi gravado.')
    linhas = ''.join(f'        <file href="{c}" />\n      \n' for c in caminhos)
    return texto.replace(marca, linhas + marca), linhas


def pastas_cdn(curso):
    """Pastas referenciadas por blocos html/cdn do curso."""
    pastas = []
    for licao in curso['course']['lessons']:
        for b in licao.get('items') or []:
            if b.get('family') == 'html' and b.get('variant') == 'cdn':
                for it in b.get('items') or []:
                    pastas.append(((it.get('media') or {}).get('sandbox') or {}).get('src'))
    return pastas


def main():
    p = argparse.ArgumentParser(description='Gera um SCORM novo a partir do JSON do curso.')
    p.add_argument('curso_json')
    p.add_argument('--pacote-original', required=True)
    p.add_argument('--pacote-saida', required=True)
    p.add_argument('--anexar', action='append', metavar='PASTA=NOME',
                   help='copia PASTA para scormcontent/assets/NOME/ e registra no manifest (pode repetir)')
    args = p.parse_args()

    saida = pathlib.Path(args.pacote_saida)
    if saida.exists():
        raise SystemExit(f'{saida} ja existe. Apague ou escolha outro nome (nada foi gravado).')
    temporario = saida.with_name(saida.name + '.parcial')

    curso = json.loads(pathlib.Path(args.curso_json).read_text(encoding='utf-8-sig'))
    b64 = serializar(curso)
    b64_original = ler_payload(args.pacote_original)

    with zipfile.ZipFile(args.pacote_original) as zin:
        nomes_originais = zin.namelist()
        anexos = ler_anexos(args.anexar, set(nomes_originais))
        manifest_original = zin.read(MANIFEST).decode('utf-8')

    # todo bloco cdn precisa apontar para uma pasta com index.html no pacote final
    nomes_finais = set(nomes_originais) | set(anexos)
    for pasta in pastas_cdn(curso):
        if f'{PREFIXO_ASSETS}{pasta}/index.html' not in nomes_finais:
            raise SystemExit(f'Bloco html/cdn aponta para assets/{pasta}/index.html, que nao estara no '
                             f'pacote. Use --anexar. Nada foi gravado.')

    linhas_novas = ''
    try:
        with zipfile.ZipFile(args.pacote_original) as zin, \
                zipfile.ZipFile(temporario, 'w', zipfile.ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                if info.filename == ALVO:
                    # troca so' o Base64, preservando o envelope original caractere por caractere
                    texto = zin.read(ALVO).decode('utf-8')
                    m = ENVELOPE.match(texto)
                    dados = (texto[:m.start(1)] + b64 + texto[m.end(1):]).encode('utf-8')
                elif info.filename == MANIFEST and anexos:
                    novo, linhas_novas = manifest_com_anexos(manifest_original, list(anexos))
                    dados = novo.encode('utf-8')
                else:
                    dados = zin.read(info.filename)
                zout.writestr(info, dados)
            for caminho, dados in anexos.items():
                zout.writestr(caminho, dados)

        with zipfile.ZipFile(args.pacote_original) as za, zipfile.ZipFile(temporario) as zb:
            if zb.namelist() != za.namelist() + list(anexos):
                raise SystemExit('!! Lista de arquivos do pacote diferente do esperado.')
            mudaveis = {ALVO} | ({MANIFEST} if anexos else set())
            difs = [n for n in za.namelist() if n not in mudaveis and za.read(n) != zb.read(n)]
            if difs:
                raise SystemExit(f'!! Arquivos alterados fora do previsto: {difs[:5]}')
            if anexos and zb.read(MANIFEST).decode('utf-8').replace(linhas_novas, '') != manifest_original:
                raise SystemExit('!! O manifest mudou alem das linhas dos anexos.')
            if any(zb.read(c) != d for c, d in anexos.items()):
                raise SystemExit('!! Algum anexo nao foi gravado byte a byte.')
            payload_original_identico = za.read(ALVO) == zb.read(ALVO)
            n = len(zb.namelist())
        temporario.replace(saida)
    finally:
        if temporario.exists():
            temporario.unlink()

    print(f'Pacote gerado          : {saida}')
    print(f'Arquivos no pacote     : {n}  ({len(nomes_originais)} originais'
          + (f' + {len(anexos)} anexados' if anexos else '') + ')')
    print(f'Originais inalterados  : todos, exceto runtime-data.js'
          + (' e imsmanifest.xml (so linhas acrescentadas)' if anexos else ''))
    for c in anexos:
        print(f'   + {c}')
    print(f'Ida e volta do Base64  : OK')
    print(f'Base64 igual ao original: {"SIM" if b64 == b64_original else "NAO"}')
    print(f'runtime-data.js identico byte a byte: {"SIM" if payload_original_identico else "NAO"}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
