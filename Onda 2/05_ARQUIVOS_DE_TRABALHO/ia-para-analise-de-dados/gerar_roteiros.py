"""Gera os roteiros de insercao (fase B) de IA para Analise de Dados (Essentials e Hands On).

Fonte do conteudo: roteiro-articulate-essentials.md e roteiro-articulate-hands-on.md
(Pesquisa Conteudo Onda 2/Ementa Completa/ia-para-analise-de-dados-essentials/roteiros/).
Posicoes = indices do curso REVISADO (fase A). Dentro de cada licao, os roteiros vao de baixo para
cima (posicao maior primeiro), para que os indices originais continuem valendo.
"""
import json
import pathlib

AQUI = pathlib.Path(__file__).resolve().parent
HTML = '@arquivo:../../../../html/'


def tp(heading, paragraph):
    return {'modelo': 'text-text-heading-paragraph.json', 'itens': [{'heading': heading, 'paragraph': paragraph}]}


def acc(itens):
    return {'modelo': 'interactive-interactive-accordion.json', 'itens': [{'title': t, 'description': d} for t, d in itens]}


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


def alem(oficina, desafios):
    return [tp(f'Quer ir além? Desafios opcionais da Oficina {oficina}',
               '<p>Se sobrou tempo, abra cada desafio. Cada um traz o número que valida o resultado:</p>'),
            acc(desafios)]


# ====================================================================== ESSENTIALS
E = []
E.append(('e01_l7_criterios', 7, 11, [html('e7-criterios.html', trava=True), cont('completeBlock')]))
E.append(('e02_l6_armadilhas', 6, 8, [html('e6-armadilhas.html')]))
E.append(('e03_l5_eixo', 5, 9, [html('e5-eixo.html')]))
E.append(('e04_l4_kc_taxa', 4, 14, [
    kc('Você vai comparar o número de processos de São Paulo (44,4 milhões de habitantes) com o de Roraima. Que medida torna a comparação justa?', [
        ('O total de processos de cada estado', False, 'Não. O estado mais populoso sempre terá mais processos; o total mede tamanho, não incidência.'),
        ('A média de processos por tribunal', False, 'Não. A média ainda depende do tamanho de cada estado e pode ser puxada por um tribunal grande.'),
        ('Os processos por 100 mil habitantes', True, 'Correto. Dividir pela população e multiplicar por 100 mil põe estados de tamanhos diferentes na mesma régua.'),
        ('A variação percentual do total entre dois anos', False, 'Não. A variação mostra crescimento, mas não corrige a diferença de tamanho entre os estados.'),
    ]),
]))
E.append(('e05_l4_composicao', 4, 10, [html('e4-composicao.html')]))
E.append(('e06_l3_leitura', 3, 10, [html('e3-leitura.html')]))
E.append(('e07_l2_semaforo', 2, 12, [html('e2-semaforo.html')]))

# ====================================================================== HANDS ON
H = []
H.append(('h01_l2_fechamento', 2, 10, [
    cont(),
    tp('Conseguiu! E agora?', '<p>Você conferiu inflação com o IBGE, lucro com a CVM e processos com o CNJ, e desarmou quatro armadilhas reais. Repita o ciclo com uma base da sua área antes de usar dados de trabalho — e sempre dentro da política de dados da sua organização.</p><p>Próximo passo: <em>Análise de Dados em Python com IA</em> leva tudo isso para um projeto reprodutível, que roda de novo do zero com um comando.</p>'),
]))
H.append(('h02_l2_projeto', 2, 9, [html('h2-projeto-final.html', trava=True), cont('completeBlock')]))
H.append(('h03_l1_alem_o4', 1, 28, alem(4, [
    ('Texto alternativo', '<p>Peça um texto alternativo de duas frases para o gráfico.</p><p></p><p><strong>Validação:</strong> cita o maior e o menor estado.</p>'),
    ('Média e mediana', '<p>Peça a média e a mediana da população das UFs.</p><p></p><p><strong>Validação:</strong> média ≈ 7,52 milhões; mediana 3,94 milhões.</p>'),
    ('Cor por código hexadecimal', '<p>Troque a cor das barras por um código hexadecimal.</p><p></p><p><strong>Validação:</strong> o PNG baixado tem a cor escolhida.</p>'),
])))
H.append(('h04_l1_alem_o3', 1, 22, alem(3, [
    ('O mesmo para 2024', '<p>Faça a mesma soma para 2024 e compare com o Sumário Executivo 2025 do CNJ (39,4 milhões).</p><p></p><p><strong>Validação:</strong> a base dá ≈ 39,57 milhões; registre a diferença como revisão de dados.</p>'),
    ('Parcela de cada ramo', '<p>Calcule a parcela de cada ramo de justiça em 2025.</p><p></p><p><strong>Validação:</strong> Justiça Estadual ≈ 69%.</p>'),
    ('Gráfico por ramo', '<p>Peça um gráfico de barras por ramo de justiça.</p><p></p><p><strong>Validação:</strong> eixo em zero e fonte CNJ no rodapé.</p>'),
])))
H.append(('h05_l1_alem_o2', 1, 16, alem(2, [
    ('Empresas com prejuízo', '<p>Conte quantas empresas tiveram prejuízo em 2024.</p><p></p><p><strong>Validação:</strong> 95.</p>'),
    ('Lucro somado', '<p>Peça a soma do lucro das 458 empresas, já em reais.</p><p></p><p><strong>Validação:</strong> ≈ R$ 303,9 bi.</p>'),
    ('Onde a escala está documentada', '<p>Pergunte onde a coluna ESCALA_MOEDA está documentada.</p><p></p><p><strong>Validação:</strong> a resposta aponta o dicionário de dados da CVM (pasta META do mesmo endereço).</p>'),
])))
H.append(('h06_l1_alem_o1', 1, 10, alem(1, [
    ('Corrigir um valor pela inflação', '<p>Corrija R$ 1.000 de janeiro de 2024 até dezembro de 2025.</p><p></p><p><strong>Validação:</strong> ≈ R$ 1.092,96.</p>'),
    ('Segunda opinião no Julius', '<p>No Julius (opcional), envie o mesmo arquivo pelo ícone <strong>Julius &gt; +</strong> da barra de chat (ou arraste o arquivo para a conversa), abra <strong>Generated code</strong> e confira 4,83%.</p><p></p><p><strong>Validação:</strong> o mesmo número nas duas ferramentas.</p>'),
    ('Um ano anterior', '<p>Compare o acumulado de 2022 com o publicado pelo IBGE.</p><p></p><p><strong>Validação:</strong> diferença de até 0,01 ponto percentual, explicada pelo arredondamento das taxas mensais.</p>'),
])))
H.append(('h07_l0_preparacao', 0, 12, [html('h1-preparacao.html', trava=True), cont('completeBlock')]))


def gravar(roteiros, pasta):
    pasta.mkdir(parents=True, exist_ok=True)
    for nome, licao, posicao, blocos in roteiros:
        (pasta / f'{nome}.json').write_text(json.dumps({'licao': licao, 'posicao': posicao, 'blocos': blocos}, ensure_ascii=False, indent=1), encoding='utf-8')
        print(pasta.parent.parent.name, nome, 'licao', licao, 'pos', posicao, len(blocos), 'blocos')


if __name__ == '__main__':
    gravar(E, AQUI / 'essentials' / 'iadados-essentials-blocos' / 'trabalho' / 'roteiros')
    gravar(H, AQUI / 'hands-on' / 'iadados-hands-on-blocos' / 'trabalho' / 'roteiros')
