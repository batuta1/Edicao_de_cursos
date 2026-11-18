"""
Insere uma sequencia de blocos novos, em ordem, a partir de um unico roteiro.

Roteiro (JSON):
    {
      "licao": 2,                 position da licao (0 = primeira)
      "posicao": 4,               indice que o PRIMEIRO bloco novo vai ocupar
      "blocos": [
        {"modelo": "text-text-heading-paragraph.json", "itens": [{"heading": "...", "paragraph": "<p>...</p>"}]},
        {"modelo": "divider-continue-continue.json",   "itens": [{"title": "Continue"}]}
      ]
    }
Um bloco pode trazer "settings": {...} para ajustar o que o modelo declara em "settings_ajustaveis"
(ex.: {"hasCustomCompletion": true} no bloco HTML).
Os modelos sao procurados na pasta --modelos. Os blocos entram um apos o outro, na ordem do roteiro.
Nada e' gravado se qualquer bloco falhar.

Um campo de texto pode vir de um arquivo: "@arquivo:infografico.html" (caminho relativo ao roteiro).
Util para o srcdoc do bloco HTML, que e' um documento inteiro.

Uso:
    python inserir_sequencia.py ../trabalho/curso_E4.json --roteiro ../trabalho/roteiro_E5.json \
        --modelos ../modelos/ --saida ../trabalho/curso_E5.json
"""
import argparse
import json
import pathlib
import sys

from ids import coletar_ids
from inserir_bloco import construir_bloco, localizar_licao


def resolver_arquivos(itens, pasta_roteiro):
    """Troca valores "@arquivo:<caminho>" pelo conteudo do arquivo."""
    for it in itens or []:
        for k, v in it.items():
            if isinstance(v, str) and v.startswith('@arquivo:'):
                arq = pasta_roteiro / v[len('@arquivo:'):]
                if not arq.exists():
                    raise SystemExit(f'Arquivo {arq} nao encontrado. Nada foi gravado.')
                it[k] = arq.read_text(encoding='utf-8-sig')
    return itens


def main():
    p = argparse.ArgumentParser()
    p.add_argument('curso_json')
    p.add_argument('--roteiro', required=True)
    p.add_argument('--modelos', required=True)
    p.add_argument('--saida', required=True)
    args = p.parse_args()

    saida = pathlib.Path(args.saida)
    if saida.exists():
        raise SystemExit(f'{saida} ja existe. Nada foi gravado.')

    curso = json.loads(pathlib.Path(args.curso_json).read_text(encoding='utf-8-sig'))
    roteiro = json.loads(pathlib.Path(args.roteiro).read_text(encoding='utf-8-sig'))
    licao = localizar_licao(curso, roteiro['licao'], roteiro['posicao'])

    existentes = coletar_ids(curso)
    novos = []
    for n, spec in enumerate(roteiro['blocos']):
        arq = pathlib.Path(args.modelos) / spec['modelo']
        if not arq.exists():
            raise SystemExit(f'Bloco {n}: modelo {arq} nao encontrado. Nada foi gravado.')
        modelo = json.loads(arq.read_text(encoding='utf-8-sig'))
        itens = resolver_arquivos(spec.get('itens'), pathlib.Path(args.roteiro).parent)
        novos.append((modelo['chave'], construir_bloco(modelo, itens, existentes, spec.get('settings'))))

    pos = roteiro['posicao']
    licao['items'][pos:pos] = [b for _, b in novos]
    saida.write_text(json.dumps(curso, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f'{len(novos)} blocos inseridos na licao {roteiro["licao"]} ("{licao["title"]}"), '
          f'indices {pos}..{pos + len(novos) - 1}')
    for i, (chave, b) in enumerate(novos):
        print(f'   [{pos + i:2d}] {chave:42s} id {b["id"]}  ({len(b["items"])} item(ns))')
    print(f'Gravado: {saida}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
