"""
Extrai o curso de dentro de um pacote SCORM do Rise 360.

Le scormcontent/runtime-data.js de dentro do .zip (sem descompactar o pacote), decodifica o
Base64 e grava o JSON do curso formatado, para leitura e edicao.

Uso:
    python extrair.py PACOTE.zip --saida ../trabalho/curso.json
"""
import argparse
import base64
import json
import pathlib
import re
import sys
import zipfile

ALVO = 'scormcontent/runtime-data.js'
ENVELOPE = re.compile(r'^__jsonp\("runtime-data\.js","([A-Za-z0-9+/=]+)"\);?\s*$', re.S)


def ler_payload(pacote):
    with zipfile.ZipFile(pacote) as z:
        if ALVO not in z.namelist():
            raise SystemExit(f'{ALVO} nao encontrado no pacote. Formato nao suportado.')
        texto = z.read(ALVO).decode('utf-8')
    m = ENVELOPE.match(texto)
    if not m:
        raise SystemExit(f'Envelope __jsonp nao reconhecido em {ALVO}.')
    return m.group(1)


def main():
    p = argparse.ArgumentParser(description='Extrai o JSON do curso de um SCORM do Rise.')
    p.add_argument('pacote')
    p.add_argument('--saida', required=True, help='arquivo .json a gravar')
    args = p.parse_args()

    b64 = ler_payload(args.pacote)
    curso = json.loads(base64.b64decode(b64).decode('utf-8'))
    c = curso['course']

    saida = pathlib.Path(args.saida)
    if saida.exists():
        raise SystemExit(f'{saida} ja existe. Apague ou escolha outro nome (nada foi gravado).')
    saida.write_text(json.dumps(curso, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f'Curso   : {c["title"]}')
    print(f'course.id: {c["id"]}')
    for L in sorted(c['lessons'], key=lambda l: l['position']):
        print(f'   [{L["position"]}] {L["type"]:6s} {len(L["items"]):3d} blocos  {L["title"]}')
    print(f'Gravado : {saida}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
