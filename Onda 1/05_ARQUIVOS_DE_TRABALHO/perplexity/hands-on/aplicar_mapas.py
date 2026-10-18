"""Aplica os mapas de texto (revisao_textos/L01.json ...) nas licoes extraidas.

Cada mapa e' {caminho: texto_novo}, com caminho relativo a `lesson` e indices numericos
(ex.: "items.3.items.0.paragraph"). Para cada entrada, o script exige que:
  - o ultimo campo seja textual (mesma lista do validar_estrutura.py);
  - o valor atual seja string e ainda igual ao ORIGINAL do curso (nao aplica duas vezes);
  - o texto novo nao seja vazio nem igual ao atual.
Se qualquer entrada falhar, nada e' gravado.

Uso: python aplicar_mapas.py cursoPerplexityHandsOn.json licoes_extraidas_PerplexityHandsOn/ revisao_textos/
"""
import json
import pathlib
import sys

CAMPOS_TEXTO = {'paragraph', 'description', 'heading', 'title', 'feedback', 'caption', 'summary',
                'intro', 'body', 'altText', 'placeholder', 'instructions', 'label', 'question',
                'answer', 'text'}


def navegar(raiz, caminho):
    partes = caminho.split('.')
    no = raiz
    for p in partes[:-1]:
        no = no[int(p)] if p.isdigit() else no[p]
    return no, partes[-1]


def main():
    curso_path, pasta, mapas = (pathlib.Path(a) for a in sys.argv[1:4])
    curso = json.loads(curso_path.read_text(encoding='utf-8'))
    originais = {l['id']: l for l in curso['course']['lessons']}
    pendentes = []
    total = 0
    for arq in sorted(pasta.glob('licao_*.json')):
        dados = json.loads(arq.read_text(encoding='utf-8'))
        mapa_path = mapas / f'L{dados["numero_da_licao"]:02d}.json'
        if not mapa_path.exists():
            continue
        mapa = json.loads(mapa_path.read_text(encoding='utf-8'))
        licao, original = dados['lesson'], originais[dados['lesson']['id']]
        for caminho, novo in mapa.items():
            no, campo = navegar(licao, caminho)
            no_orig, _ = navegar(original, caminho)
            if campo not in CAMPOS_TEXTO:
                raise SystemExit(f'{mapa_path.name}: campo nao textual {campo!r} em {caminho}')
            if not isinstance(no.get(campo), str):
                raise SystemExit(f'{mapa_path.name}: {caminho} nao existe ou nao e string')
            if no[campo] != no_orig[campo]:
                raise SystemExit(f'{mapa_path.name}: {caminho} ja foi alterado (valor != original)')
            if not isinstance(novo, str) or not novo.strip() or novo == no[campo]:
                raise SystemExit(f'{mapa_path.name}: texto novo vazio ou igual ao atual em {caminho}')
            no[campo] = novo
        pendentes.append((arq, dados, len(mapa)))
        total += len(mapa)
    for arq, dados, n in pendentes:
        arq.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'{arq.name}: {n} campo(s) alterado(s)')
    print(f'TOTAL: {total}')


if __name__ == '__main__':
    main()
