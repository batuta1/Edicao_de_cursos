"""Gera os roteiros de insercao (fase B) de Analise de Dados em Python com IA (Essentials e Hands On).

Fonte do conteudo: roteiro-articulate-essentials.md e roteiro-articulate-hands-on.md
(Pesquisa Conteudo Onda 2/Ementa Completa/dados-com-python-e-ia-hands-on/roteiros/).
Posicoes = indices do curso REVISADO (fase A); dentro de cada licao, de baixo para cima.
"""
import json
import pathlib

AQUI = pathlib.Path(__file__).resolve().parent
HTML = '@arquivo:../../../../html/'


def tp(heading, paragraph):
    return {'modelo': 'text-text-heading-paragraph.json', 'itens': [{'heading': heading, 'paragraph': paragraph}]}


def lista(itens):
    return {'modelo': 'list-list-numbered.json', 'itens': [{'paragraph': x} for x in itens]}


def cont(tipo=''):
    item = {'title': 'Continue'}
    if tipo:
        item['type'] = tipo
    return {'modelo': 'divider-continue-continue.json', 'itens': [item]}


def html(arquivo, trava=False):
    b = {'modelo': 'html-html-inline.json', 'itens': [{'srcdoc': HTML + arquivo}], 'settings': {'width': '1'}}
    if trava:
        b['settings']['hasCustomCompletion'] = True
    return b


def kc(titulo, alternativas):
    return {'modelo': 'knowledgecheck-knowledgecheck-multiple-choice.json',
            'itens': [{'title': titulo, 'answers': [{'title': t, 'correct': c, 'feedback': f} for t, c, f in alternativas]}]}


# ====================================================================== ESSENTIALS
E = []
E.append(('e01_l6_entrega', 6, 10, [html('e6-entrega.html', trava=True), cont('completeBlock')]))
E.append(('e02_l4_pasta', 4, 7, [html('e4-pasta.html')]))
E.append(('e03_l3_brief', 3, 5, [html('e3-brief.html')]))
E.append(('e04_l2_aprovacoes', 2, 12, [html('e2-aprovacoes.html')]))
E.append(('e05_l1_conversa_codigo', 1, 4, [html('e1-conversa-ou-codigo.html')]))

# ====================================================================== HANDS ON
H = []
H.append(('h01_l2_clima', 2, 15, [html('h2-clima.html', trava=True), cont('completeBlock')]))
H.append(('h02_l1_kc_escala', 1, 15, [
    kc('Na Oficina 2, o primeiro filtro imprimiu 460 linhas e 458 empresas, e a Vivara apareceu no topo do ranking. O que o script precisa fazer antes de ordenar?', [
        ('Ordenar de novo, agora pelo nome da empresa', False, 'Não. A ordem não é o problema; o valor que entra nela é que está em escalas diferentes e com duplicatas.'),
        ('Remover as duplicatas e converter tudo para reais pela ESCALA_MOEDA', True, 'Correto. São 2 linhas a mais que empresas e 8 empresas informando em UNIDADE: sem tratar as duas coisas, o ranking mente.'),
        ('Excluir a Vivara, porque o valor dela parece estranho', False, 'Não. Excluir sem explicar é esconder a premissa. A Vivara está certa — R$ 653 milhões — só informada em reais.'),
        ('Extrair o ZIP em dados/brutos para conferir o arquivo', False, 'Não. Dado bruto não se edita; se precisar extrair, use dados/tratados/. O problema está na escala, não no ZIP.'),
    ]),
]))
H.append(('h03_l1_mapa', 1, 3, [
    tp('O mapa da mão na massa', '<p>As oficinas vão em sequência; cada uma deixa um script com testes que passam:</p>'),
    lista([
        '<p><strong>Oficina 1 (16 min):</strong> transformar o cálculo da inflação num projeto que roda de novo.</p>',
        '<p><strong>Oficina 2 (22 min):</strong> fazer o ranking de lucro da bolsa sem cair na escala.</p>',
        '<p><strong>Oficina 3 (22 min):</strong> descobrir qual setor lucrou mais, cruzando duas tabelas.</p>',
        '<p><strong>Oficina 4 (16 min):</strong> pegar um erro silencioso com uma segunda opinião (próxima lição).</p>',
        '<p><strong>Projeto Final (22 min):</strong> analisar o clima do Distrito Federal em 2024 a partir de cinco arquivos (próxima lição).</p>',
    ]),
]))
H.append(('h04_l0_preparacao', 0, 11, [html('h1-preparacao.html', trava=True), cont('completeBlock')]))


def gravar(roteiros, pasta):
    pasta.mkdir(parents=True, exist_ok=True)
    for nome, licao, posicao, blocos in roteiros:
        (pasta / f'{nome}.json').write_text(json.dumps({'licao': licao, 'posicao': posicao, 'blocos': blocos}, ensure_ascii=False, indent=1), encoding='utf-8')
        print(pasta.parent.parent.name, nome, 'licao', licao, 'pos', posicao, len(blocos), 'blocos')


if __name__ == '__main__':
    gravar(E, AQUI / 'essentials' / 'pythonia-essentials-blocos' / 'trabalho' / 'roteiros')
    gravar(H, AQUI / 'hands-on' / 'pythonia-hands-on-blocos' / 'trabalho' / 'roteiros')
