"""Gera os roteiros de insercao (fase B) dos dois cursos de Revisao Bibliografica com IA.

Fonte do conteudo: roteiro-articulate-hands-on.md e roteiro-articulate-essentials.md
(Pesquisa Conteudo Onda 2/Ementa Completa/revisao-bibliografica-com-ia-hands-on/roteiros/).
As posicoes sao indices do curso REVISADO (fase A). Dentro de cada licao, os roteiros sao aplicados
de baixo para cima (posicao maior primeiro), para que os indices originais continuem valendo.
"""
import json
import pathlib

AQUI = pathlib.Path(__file__).resolve().parent
HTML = '@arquivo:../../../../html/'


def tp(heading, paragraph):
    return {'modelo': 'text-text-heading-paragraph.json', 'itens': [{'heading': heading, 'paragraph': paragraph}]}


def par(p):
    return {'modelo': 'text-text-paragraph.json', 'itens': [{'paragraph': p}]}


def imp(p):
    return {'modelo': 'text-impact-b.json', 'itens': [{'paragraph': p}]}


def lista(itens):
    return {'modelo': 'list-list-numbered.json', 'itens': [{'paragraph': x} for x in itens]}


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


def desafio(o_que, valida):
    return f'<p>{o_que}</p><p></p><p><strong>Valida se:</strong> {valida}</p>'


IR_ALEM = '<p>Três desafios opcionais, para quem quiser ir além. Abra cada um — o desafio diz como saber se deu certo:</p>'

# ====================================================================== HANDS-ON
H = []

# --- L03 (licao 2): Oficina 4 + Projeto Final ---------------------------------
H.append(('h01_l2_pf_checklist_dez_conseguiu', 2, 16, [
    html('h4-checklist-final.html', trava=True),
    cont('completeBlock'),
    tp('A Parte dos Dez', '<p>Dez hábitos de quem revisa com IA:</p>'),
    lista([
        '<p><strong>Pergunta antes de buscador.</strong> Tema não é pergunta.</p>',
        '<p><strong>Critério antes de resultado.</strong> Critério escrito depois da busca vira desculpa.</p>',
        '<p><strong>Nenhuma ferramenta sozinha.</strong> Pelo menos uma de IA e uma base brasileira.</p>',
        '<p><strong>Semantic Scholar não fala booleano.</strong> Consulta curta, uma por sinônimo.</p>',
        '<p><strong>Anote a busca na hora.</strong> Data, consulta exata, filtros, total. Amanhã o total muda.</p>',
        '<p><strong>Total recuperado não é total relevante.</strong> Quem diz o que serve é a triagem.</p>',
        '<p><strong>TLDR e Meter são pistas.</strong> Resumo e estudo são a prova.</p>',
        '<p><strong>Supporting quote se abre.</strong> E o dado se confere no artigo.</p>',
        '<p><strong>"Só resumo" se anota.</strong> Extração sem texto completo vale menos — e o leitor precisa saber.</p>',
        '<p><strong>Declare a IA.</strong> Ferramenta, finalidade e data, como pede o CNPq.</p>',
    ]),
    tp('Conseguiu! E agora?', '<p>Você fez o que muita revisão por aí não faz: deixou cada passo anotado. Pergunta estruturada, busca em três lugares, triagem com motivo, dado conferido no artigo, síntese citada e PRISMA. Isso é o que separa "a IA me deu uns artigos" de "eu revisei a literatura".</p><p>Para continuar: use a planilha na próxima revisão de verdade, com mais registros. Se a sua instituição tiver Elicit Pro, experimente o Systematic Review — agora você sabe conferir o que ele entrega. E, para ir além da mini-revisão, os próximos degraus são o manual do JBI, o Cochrane Handbook e a avaliação de risco de viés.</p>'),
]))
H.append(('h02_l2_o4_ir_alem', 2, 12, [
    tp('Quer ir além? (opcional)', IR_ALEM),
    acc([
        ('Desafio 1: rode de novo', desafio('Rode a mesma pergunta de novo no Research Agent e compare duas células com a primeira execução.', 'você anotou se o resultado mudou (no estudo de 2026, só 77% se repetiram).')),
        ('Desafio 2: Research Report', desafio('Gere um Research Report (<strong>elicit.com &gt; Research Report</strong>) com a mesma pergunta e abra três citações.', 'cada uma tem o supporting quote conferido.')),
        ('Desafio 3: instrução mais precisa', desafio('Escreva uma coluna com instrução mais precisa ("Sample size: number of participants analyzed, not recruited") e compare.', 'a coluna nova errou menos.')),
    ]),
    cont(),
]))
H.append(('h03_l2_o4_sua_vez_uff', 2, 7, [
    imp('<p>🤓 <strong>Mudou em 30/09/2026:</strong> Find Papers, Extract Data e Chat with Papers viraram parte do Research Agent. Se um vídeo mostrar esses botões, ele é anterior à mudança.</p>'),
    tp('Sua vez: você contra o Elicit', '<p>Agora com um artigo aberto, do começo ao fim: "Efeitos da capacitação em telessaúde..." (objnursing.uff.br/nursing/article/download/6885/pdf_pt). Você extrai à mão, o Elicit extrai, e vocês comparam:</p>'),
    lista([
        '<p>Baixe o PDF do artigo da UFF (acesso aberto, sinal verde).</p>',
        '<p>Preencha à mão, na aba Extração: país, desenho, população e resultado, cada um com página e trecho.</p>',
        '<p>Envie o mesmo PDF ao Research Agent (opção de upload de PDF) e peça as mesmas quatro colunas.</p>',
        '<p>Compare célula por célula e anote as divergências.</p>',
    ]),
    imp('<p>✅ <strong>Deu certo?</strong> Cada célula tem página e trecho, a coluna "texto completo ou só resumo" está preenchida e as divergências entre você e o Elicit estão anotadas. Detalhe: esse artigo mede encaminhamentos presenciais à cardiologia, não a pressão arterial — pelos critérios do caso-guia, ele seria excluído ("sem desfecho de pressão"). Notou? É a triagem conversando com a extração.</p>'),
]))

# --- L02 (licao 1): Oficinas 2 e 3 --------------------------------------------
H.append(('h04_l1_o3_ir_alem', 1, 18, [
    tp('Quer ir além? (opcional)', IR_ALEM),
    acc([
        ('Desafio 1: triagem em dupla', desafio('Peça a um colega para triar os mesmos 10 registros com os seus critérios e compare.', 'você anotou quantas decisões divergiram.')),
        ('Desafio 2: triagem da BVS', desafio('Aplique a mesma triagem aos resultados da BVS.', 'as duplicatas foram marcadas.')),
        ('Desafio 3: tipo de estudo não é qualidade', desafio('No Consensus, aplique o filtro de desenho do estudo (Study design, no botão Filter) e veja quantos dos seus incluídos são ensaios.', 'você não trocou "tipo de estudo" por "qualidade" na anotação.')),
    ]),
]))
H.append(('h05_l1_o3_triagem_html', 1, 14, [
    html('h3-triagem.html'),
]))
H.append(('h06_l1_o2_ir_alem', 1, 11, [
    tp('Quer ir além? (opcional)', IR_ALEM),
    acc([
        ('Desafio 1: a mesma busca em português', desafio('Repita a busca do Semantic Scholar em português, entre aspas, e compare o total.', 'o Log tem as duas linhas.')),
        ('Desafio 2: Library e Research Feed', desafio('No Semantic Scholar, crie conta, salve 5 artigos com Save to Library e crie um Research Feed (marque 5 relevantes e 3 "less like this").', 'o feed sugeriu artigos novos.')),
        ('Desafio 3: do Semantic Scholar ao Zotero', desafio('Exporte a Library em BibTeX (<strong>semanticscholar.org &gt; Account &gt; Research &gt; Library &gt; Export</strong>) e importe no Zotero (<strong>Zotero &gt; File &gt; Import… &gt; A file</strong>).', 'as referências aparecem no Zotero.')),
    ]),
    cont(),
]))

# --- L01 (licao 0): preparacao + Oficina 1 ------------------------------------
H.append(('h07_l0_o1_ir_alem', 0, 12, [
    tp('Quer ir além? (opcional)', IR_ALEM),
    acc([
        ('Desafio 1: expressão para a BVS', desafio('Monte a expressão para a BVS: (termos de I unidos por OR) AND (termos de P unidos por OR).', 'cada conceito está entre parênteses.')),
        ('Desafio 2: recorte de tempo', desafio('Reescreva a sua pergunta com recorte de tempo (ex.: 2015–2026).', 'o critério de inclusão ganhou o período.')),
        ('Desafio 3: DeCS × MeSH', desafio('Procure os seus termos no MeSH (meshb.nlm.nih.gov) e compare com o DeCS.', 'você anotou uma diferença.')),
    ]),
]))
H.append(('h08_l0_preparacao', 0, 3, [
    tp('Antes de arregaçar as mangas', '<p>Este curso é mão na massa: você vai fazer uma revisão de literatura de verdade, pequena e completa, com três ferramentas de IA gratuitas e uma base brasileira. Revisão é trabalho de abas e de anotação — e a anotação é o que transforma "uns artigos que a IA me deu" em revisão. A preparação leva 7 minutos.</p><p>Toda revisão passa por cinco etapas: <strong>pergunta → busca → triagem → extração → síntese</strong>. Cada uma deixa uma pegada na planilha. Se a pegada não está lá, para quem lê a revisão a etapa não aconteceu.</p>'),
    tp('Monte a planilha', '<p>Revisão bem anotada é como receita bem escrita: outra pessoa segue e chega ao mesmo bolo. Crie uma planilha com quatro abas — abra cada uma para ver as colunas:</p>'),
    acc([
        ('Log', '<p><strong>Colunas:</strong> Data · Onde buscou · Consulta exata · Filtros · Total exibido.</p><p></p><p><strong>Para quê:</strong> refazer cada busca — e explicar por que o total mudou.</p>'),
        ('Triagem', '<p><strong>Colunas:</strong> ID · Título · Onde achou · Decisão (incluir / excluir / incerto) · Motivo.</p><p></p><p><strong>Para quê:</strong> mostrar por que cada registro entrou ou saiu.</p>'),
        ('Extração', '<p><strong>Colunas:</strong> ID · País · Desenho · Amostra · Resultado · Página e trecho · Texto completo ou só resumo? · Conferido?</p><p></p><p><strong>Para quê:</strong> guardar cada dado com a sua origem.</p>'),
        ('Síntese', '<p><strong>Colunas:</strong> Frase · Tipo · Referência · Trecho.</p><p></p><p><strong>Para quê:</strong> ligar cada frase da conclusão ao trecho que a sustenta.</p>'),
    ]),
    tp('O que pode ir para a IA', '<p>O Elicit pode processar dados nos Estados Unidos com provedores de modelo; o Consensus repassa consultas e uploads a OpenAI, Anthropic, Google e Baseten (sem usar para treino, segundo a política). O Semantic Scholar busca sem conta. Antes de colar qualquer coisa, passe pelo semáforo:</p>'),
    html('h1-semaforo.html'),
    imp('<p>⚠️ <strong>Não precisa pagar:</strong> Systematic Review do Elicit e exportação de tabela em CSV são pagos. Você não precisa deles — a planilha faz esse papel.</p>'),
    html('h2-preparacao.html', trava=True),
    cont('completeBlock'),
]))

# ====================================================================== ESSENTIALS
E = []
E.append(('e01_l1_prisma_kc', 1, 14, [
    kc('Um colega diz que vai "usar o PRISMA" para buscar os artigos da revisão dele. O que o PRISMA 2020 é, de fato?', [
        ('Um método de busca em bases', False, 'Não. O PRISMA não busca nada: ele orienta o que a revisão deve relatar.'),
        ('Uma diretriz de relato de revisões', True, 'Correto. O PRISMA orienta o que relatar; não busca, não tria e não avalia qualidade.'),
        ('Um software de triagem', False, 'Não. A triagem é feita por quem revisa, com critérios. O PRISMA só pede que ela seja relatada.'),
        ('Uma escala de qualidade de estudos', False, 'Não. Avaliar qualidade é a etapa de avaliação crítica, com instrumentos próprios. O PRISMA é diretriz de relato.'),
    ]),
]))
E.append(('e02_l1_modalidade_html', 1, 7, [
    html('e1-modalidade.html'),
]))
E.append(('e03_l2_declaracao_html', 2, 12, [
    html('e2-declaracao.html'),
]))
E.append(('e04_l3_pilula_pcc', 3, 15, [
    tp('Pílula Hands-on (6 min): agora em PCC', '<p>Converta a pergunta "Quais efeitos e barreiras das metodologias ativas no ensino superior brasileiro?" em PCC e redija dois critérios de inclusão e um de exclusão. Faça antes de abrir o gabarito:</p>'),
    acc([
        ('Gabarito: os componentes', '<p><strong>P</strong> — estudantes e docentes do ensino superior.</p><p></p><p><strong>C</strong> — metodologias ativas, seus efeitos e barreiras. <strong>C</strong> — instituições de ensino superior brasileiras.</p>'),
        ('Gabarito: critérios aceitáveis', '<p>Incluir estudos realizados no Brasil; incluir estudos que relatem efeitos ou barreiras; excluir relatos de opinião sem dados.</p>'),
        ('Critério de êxito', '<p>Os três componentes nomeados e cada critério derivado de um componente.</p>'),
    ]),
]))
E.append(('e05_l4_onde_buscar_html', 4, 8, [
    html('e3-onde-buscar.html'),
]))
E.append(('e06_l5_confira_celula_html', 5, 14, [
    html('e4-confira-celula.html'),
]))
E.append(('e07_l6_prisma_html', 6, 11, [
    html('e5-prisma.html'),
]))


def gravar(lista_roteiros, pasta):
    pasta.mkdir(parents=True, exist_ok=True)
    for nome, licao, posicao, blocos in lista_roteiros:
        (pasta / f'{nome}.json').write_text(json.dumps({'licao': licao, 'posicao': posicao, 'blocos': blocos}, ensure_ascii=False, indent=1), encoding='utf-8')
        print(pasta.parent.parent.name, nome, 'licao', licao, 'pos', posicao, len(blocos), 'blocos')


if __name__ == '__main__':
    gravar(H, AQUI / 'hands-on' / 'revbib-hands-on-blocos' / 'trabalho' / 'roteiros')
    gravar(E, AQUI / 'essentials' / 'revbib-essentials-blocos' / 'trabalho' / 'roteiros')
