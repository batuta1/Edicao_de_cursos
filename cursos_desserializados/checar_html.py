"""Confere se as tags HTML dos campos de texto estao balanceadas e se nao ha '<' ou '>' soltos.
Uso: python checar_html.py pasta_licoes/"""
import json
import pathlib
import re
import sys
from html.parser import HTMLParser

VAZIAS = {'br', 'img', 'hr'}


class Checador(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pilha, self.erros = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VAZIAS:
            self.pilha.append(tag)

    def handle_endtag(self, tag):
        if tag in VAZIAS:
            return
        if not self.pilha or self.pilha[-1] != tag:
            self.erros.append(f'fechamento inesperado </{tag}> (pilha={self.pilha})')
        else:
            self.pilha.pop()


def walk(no, caminho, out):
    if isinstance(no, dict):
        for k, v in no.items():
            if isinstance(v, str) and '<' in v:
                c = Checador()
                c.feed(v)
                c.close()
                if c.pilha:
                    c.erros.append(f'tags nao fechadas: {c.pilha}')
                if c.erros:
                    out.append((f'{caminho}.{k}', c.erros))
            else:
                walk(v, f'{caminho}.{k}', out)
    elif isinstance(no, list):
        for i, v in enumerate(no):
            walk(v, f'{caminho}[{i}]', out)


total = 0
for arq in sorted(pathlib.Path(sys.argv[1]).glob('licao_*.json')):
    out = []
    walk(json.loads(arq.read_text(encoding='utf-8'))['lesson'], 'lesson', out)
    for cam, erros in out:
        print(arq.name, cam, erros)
    total += len(out)
print('campos com problema de HTML:', total)
