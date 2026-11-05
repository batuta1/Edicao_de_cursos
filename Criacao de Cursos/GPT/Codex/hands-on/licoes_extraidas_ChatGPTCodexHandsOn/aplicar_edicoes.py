"""Aplica edicoes pontuais de texto nas licoes, por caminho JSON.

Cada edicao e' (caminho, texto_novo). O script:
  - so' aceita caminhos cujo ultimo campo seja textual (lista CAMPOS_TEXTO);
  - exige que o valor atual seja string (nunca troca tipo, nunca cria chave);
  - exige que o valor atual ainda seja o ORIGINAL do curso (evita aplicar duas vezes
    ou sobrescrever por engano uma edicao anterior);
  - regrava o arquivo com a mesma formatacao em que foi gerado (indent=2, UTF-8).

Uso: python aplicar_edicoes.py modulo_de_edicoes   (ex.: edicoes_essentials)
"""
import importlib
import json
import pathlib
import re
import sys

CAMPOS_TEXTO = {'paragraph', 'description', 'heading', 'title', 'feedback', 'caption', 'summary',
                'intro', 'body', 'altText', 'placeholder', 'instructions', 'label', 'question',
                'answer', 'text'}
TOKEN = re.compile(r'([A-Za-z_]+)(?:\[(\d+)\])?')


def navegar(raiz, caminho):
    partes = caminho.split('.')
    no = raiz
    for p in partes[:-1]:
        m = TOKEN.fullmatch(p)
        if not m:
            raise SystemExit(f'caminho invalido: {caminho}')
        no = no[m.group(1)]
        if m.group(2) is not None:
            no = no[int(m.group(2))]
    return no, partes[-1]


def main():
    mod = importlib.import_module(sys.argv[1])
    pasta = pathlib.Path(mod.PASTA)
    curso = json.loads(pathlib.Path(mod.CURSO_ORIGINAL).read_text(encoding='utf-8'))
    originais = {l['id']: l for l in curso['course']['lessons']}

    total = 0
    for nome_arq, edicoes in mod.EDICOES.items():
        arq = pasta / nome_arq
        dados = json.loads(arq.read_text(encoding='utf-8'))
        licao = dados['lesson']
        original = originais[licao['id']]
        vistos = set()
        for caminho, novo in edicoes:
            if caminho in vistos:
                raise SystemExit(f'{nome_arq}: caminho repetido {caminho}')
            vistos.add(caminho)
            no, campo = navegar(licao, caminho)
            no_orig, _ = navegar(original, caminho)
            if campo not in CAMPOS_TEXTO:
                raise SystemExit(f'{nome_arq}: campo nao textual {campo!r} em {caminho}')
            if campo not in no or not isinstance(no[campo], str):
                raise SystemExit(f'{nome_arq}: {caminho} nao existe ou nao e string')
            if no[campo] != no_orig[campo]:
                raise SystemExit(f'{nome_arq}: {caminho} ja foi alterado antes (valor != original)')
            if not isinstance(novo, str) or not novo.strip():
                raise SystemExit(f'{nome_arq}: texto novo vazio em {caminho}')
            if novo == no[campo]:
                raise SystemExit(f'{nome_arq}: texto novo igual ao original em {caminho}')
            no[campo] = novo
            total += 1
        arq.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'{nome_arq}: {len(edicoes)} campo(s) alterado(s)')
    print(f'TOTAL: {total}')


if __name__ == '__main__':
    main()
