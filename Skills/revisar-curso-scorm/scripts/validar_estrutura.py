"""
Fase 5 do pipeline: compara cada licao editada, no' a no', contra o curso original.

A ideia e' simples: so' campos de texto pedagogico podem ter mudado. Se qualquer outra coisa
divergir — uma chave, o tamanho de um array, um id, um type, um gabarito de quiz — a edicao
quebrou a estrutura que a plataforma usa para renderizar o curso, e o pipeline precisa parar.

Sai com codigo 1 se achar divergencia estrutural, para poder ser usado como portao automatico.

Uso:
    python validar_estrutura.py curso.json licoes_extraidas_X/
    python validar_estrutura.py curso.json licoes_extraidas_X/ --detalhar
"""
import argparse
import json
import pathlib
import sys

CAMPOS_TEXTO = {'paragraph', 'description', 'heading', 'title', 'feedback',
                'caption', 'summary', 'intro', 'body', 'altText', 'placeholder',
                'instructions', 'label', 'question', 'answer', 'text'}


def comparar(a, b, caminho, estruturais, textuais):
    if isinstance(a, dict) and isinstance(b, dict):
        if a.keys() != b.keys():
            estruturais.append(f'CHAVES divergentes em {caminho}: {set(a) ^ set(b)}')
        for k in a.keys() & b.keys():
            comparar(a[k], b[k], f'{caminho}.{k}', estruturais, textuais)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            estruturais.append(f'TAMANHO de array em {caminho}: {len(a)} -> {len(b)}')
        for i in range(min(len(a), len(b))):
            comparar(a[i], b[i], f'{caminho}[{i}]', estruturais, textuais)
    elif type(a) is not type(b):
        estruturais.append(f'TIPO mudou em {caminho}')
    elif a != b:
        campo = caminho.split('.')[-1].split('[')[0]
        if campo in CAMPOS_TEXTO:
            textuais.append((campo, caminho))
        else:
            estruturais.append(f'CAMPO NAO-TEXTUAL {campo!r} mudou em {caminho}')


def main():
    p = argparse.ArgumentParser(description='Valida que so o texto pedagogico mudou nas licoes.')
    p.add_argument('curso_original', help='JSON do curso antes da edicao')
    p.add_argument('pasta_licoes', help='pasta licoes_extraidas_X/')
    p.add_argument('--detalhar', action='store_true', help='lista o caminho de cada campo alterado')
    args = p.parse_args()

    curso = json.loads(pathlib.Path(args.curso_original).read_text(encoding='utf-8'))
    por_id = {l['id']: l for l in curso['course']['lessons']}

    arquivos = sorted(pathlib.Path(args.pasta_licoes).glob('licao_*.json'))
    if not arquivos:
        print(f'Nenhum licao_*.json encontrado em {args.pasta_licoes}')
        return 1

    if len(arquivos) != len(por_id):
        print(f'!! QUANTIDADE DE LICOES DIFERE: curso tem {len(por_id)}, pasta tem {len(arquivos)}')
        return 1

    total_txt, total_estrut = 0, 0
    por_campo = {}

    for arq in arquivos:
        editada = json.loads(arq.read_text(encoding='utf-8'))['lesson']
        lid = editada.get('id')
        if lid not in por_id:
            print(f'!! {arq.name}: lesson.id {lid!r} nao existe no curso original.')
            print('   Provavel troca de curso/pasta. Pipeline interrompido.')
            return 1

        estruturais, textuais = [], []
        comparar(por_id[lid], editada, 'lesson', estruturais, textuais)
        total_txt += len(textuais)
        total_estrut += len(estruturais)
        for campo, _ in textuais:
            por_campo[campo] = por_campo.get(campo, 0) + 1

        status = 'OK' if not estruturais else f'{len(estruturais)} PROBLEMA(S)'
        print(f'{arq.name}')
        print(f'   texto alterado : {len(textuais)}')
        print(f'   ESTRUTURA      : {status}')
        if args.detalhar:
            for campo, caminho in textuais:
                print(f'      - {caminho}')
        for e in estruturais:
            print(f'      !! {e}')

    print()
    print(f'TOTAL de campos de texto alterados: {total_txt}')
    if por_campo:
        detalhe = ', '.join(f'{c}={n}' for c, n in sorted(por_campo.items()))
        print(f'   por campo: {detalhe}')

    if total_estrut:
        print(f'!! {total_estrut} DIVERGENCIA(S) ESTRUTURAL(IS). NAO prossiga para a remontagem.')
        return 1
    print('Estrutura preservada em todas as licoes.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
