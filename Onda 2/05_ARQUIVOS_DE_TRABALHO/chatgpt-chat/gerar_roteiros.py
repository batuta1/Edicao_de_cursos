"""Gera os roteiros de insercao (fase B) dos dois cursos ChatGPT Chat (Essentials e Hands On).

Fonte do conteudo: roteiro-articulate-essentials.md e roteiro-articulate-hands-on.md
(Pesquisa Conteudo Onda 2/Ementa Completa/chatgpt-chat-essentials/roteiros/).
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


# ====================================================================== HANDS-ON
H = []
# --- licao 4: Projeto Final -----------------------------------------------------
H.append(('h01_l4_parte_dos_dez', 4, 12, [
    tp('A Parte dos Dez — atalhos que salvam seu dia no ChatGPT', '<p>Dez hábitos para levar do caso Aurora para o seu trabalho:</p>'),
    lista([
        '<p><strong>Edite em vez de repetir.</strong> O lápis na sua mensagem refaz a resposta sem poluir a conversa.</p>',
        '<p><strong>Ramifique para testar.</strong> Quer outra versão sem perder a atual? Ramifique em novo chat.</p>',
        '<p><strong>Um caso, um projeto.</strong> Memória “apenas do projeto” quando o assunto não pode se misturar.</p>',
        '<p><strong>Instruções do projeto são o seu contrato.</strong> Escreva ali “diga quando não constar nos arquivos”.</p>',
        '<p><strong>Peça o trecho.</strong> “De onde você tirou isso?” desmonta invenção em segundos.</p>',
        '<p><strong>Primeiro as 5 linhas.</strong> Antes de analisar planilha, confira se ele leu as colunas certas.</p>',
        '<p><strong>Faça uma conta na mão.</strong> Um número conferido vale mais que dez aceitos.</p>',
        '<p><strong>Lei se confere no Planalto.</strong> Link de resposta não é fonte; trecho lido é.</p>',
        '<p><strong>Chat temporário para o que não deve ficar.</strong> Sem histórico, sem memória nova, sem treino.</p>',
        '<p><strong>Limite acabou?</strong> Cole o texto em vez de anexar; o trabalho continua.</p>',
    ]),
]))
# --- licao 3: Oficina 4 ---------------------------------------------------------
H.append(('h02_l3_confira_numeros', 3, 9, [
    html('h3-confira-numeros.html', trava=True),
    cont('completeBlock'),
    tp('✅ Deu certo? O gabarito', '<p><strong>Total de reclamações:</strong> 609<br><strong>Resolvidas:</strong> 501 (82,3%)<br><strong>Troca ou devolução no semestre:</strong> 158 reclamações, 102 resolvidas (64,6%)<br><strong>Troca ou devolução, mai–ago × set–out:</strong> 54 × 104<br><strong>Pior mês:</strong> outubro (132), seguido de setembro (122)</p>'),
]))
# --- licao 2: Oficina 3 ---------------------------------------------------------
H.append(('h03_l2_quer_ir_alem', 2, 10, [
    tp('🚀 Quer ir além? (opcional)', '<p>Três desafios curtos, cada um com a sua validação:</p>'),
]))
H.append(('h04_l2_politica_cdc', 2, 9, [html('h2-politica-cdc.html')]))
# --- licao 0: preparacao e mapa -------------------------------------------------
H.append(('h05_l0_mapa', 0, 8, [
    tp('O mapa da mão na massa', '<p>Cada etapa resolve um problema da diretoria:</p>'),
    lista([
        '<p><strong>Oficina 1 (20 min):</strong> tirar o caso das conversas soltas e montar um projeto.</p>',
        '<p><strong>Oficina 2 (20 min):</strong> descobrir o que a política diz, sem ler tudo e sem cair em invenção.</p>',
        '<p><strong>Oficina 3 (20 min):</strong> saber se a política está de acordo com a lei.</p>',
        '<p><strong>Oficina 4 (20 min):</strong> transformar a planilha em números e gráfico.</p>',
        '<p><strong>Projeto Final (26 min):</strong> entregar o relatório de uma página para a diretoria.</p>',
    ]),
    par('<p>As oficinas são em sequência: cada uma usa o que a anterior deixou pronto.</p>'),
    cont(),
]))
H.append(('h06_l0_kit', 0, 7, [html('h1-kit-aurora.html', trava=True), cont('completeBlock')]))

# ====================================================================== ESSENTIALS
E = []
E.append(('e01_l0_planos', 0, 9, [html('e1-planos.html')]))
E.append(('e02_l1_monte_pedido', 1, 12, [html('e2-monte-pedido.html')]))
E.append(('e03_l2_semaforo', 2, 11, [html('e3-semaforo.html')]))
E.append(('e04_l3_continuidade', 3, 9, [html('e4-continuidade.html')]))
E.append(('e05_l4_fonte_sustenta', 4, 13, [html('e5-fonte-sustenta.html')]))
E.append(('e06_l5_kc_arquivo', 5, 13, [
    kc('Você quer que o ChatGPT calcule a média mensal de atendimentos de uma planilha que traz nome e CPF de cada cliente. Você usa conta pessoal, no Free. Qual é a conduta adequada?', [
        ('Enviar a planilha inteira, porque o arquivo só será usado para o cálculo', False, 'Não. Arquivo enviado é dado tratado: nome e CPF de clientes são sinal vermelho.'),
        ('Enviar no chat temporário, que não fica no histórico', False, 'Não. O chat temporário pode ficar guardado por até 30 dias e não muda a cor do conteúdo: continua sinal vermelho.'),
        ('Enviar só as colunas de mês e de atendimentos, sem nomes nem CPFs', True, 'Correto. Sem dado que identifique pessoa, o arquivo vira sinal verde — e o cálculo continua possível.'),
        ('Desativar “Melhorar o modelo para todos” e enviar a planilha inteira', False, 'Não. O controle reduz o uso dos dados, mas não elimina o tratamento pela empresa.'),
    ]),
]))
E.append(('e07_l6_comparacao', 6, 10, [html('e6-comparacao.html')]))


def gravar(roteiros, pasta):
    pasta.mkdir(parents=True, exist_ok=True)
    for nome, licao, posicao, blocos in roteiros:
        (pasta / f'{nome}.json').write_text(json.dumps({'licao': licao, 'posicao': posicao, 'blocos': blocos}, ensure_ascii=False, indent=1), encoding='utf-8')
        print(pasta.parent.parent.name, nome, 'licao', licao, 'pos', posicao, len(blocos), 'blocos')


if __name__ == '__main__':
    gravar(H, AQUI / 'hands-on' / 'chatgpt-hands-on-blocos' / 'trabalho' / 'roteiros')
    gravar(E, AQUI / 'essentials' / 'chatgpt-essentials-blocos' / 'trabalho' / 'roteiros')
