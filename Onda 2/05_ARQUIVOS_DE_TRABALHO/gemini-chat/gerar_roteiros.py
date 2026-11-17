"""Gera os roteiros de insercao (fase B) dos dois cursos Gemini Chat (Essentials e Hands On).

Fonte do conteudo: roteiro-articulate-essentials.md e roteiro-articulate-hands-on.md
(Pesquisa Conteudo Onda 2/Ementa Completa/gemini-chat-essentials/roteiros/).
As posicoes sao indices do curso REVISADO (fase A). Dentro de cada licao, os roteiros sao aplicados
de baixo para cima (posicao maior primeiro), para que os indices originais continuem valendo.
"""
import json
import pathlib

AQUI = pathlib.Path(__file__).resolve().parent
HTML = '@arquivo:../../../../html/'


def tp(heading, paragraph):
    return {'modelo': 'text-text-heading-paragraph.json', 'itens': [{'heading': heading, 'paragraph': paragraph}]}


def imp(p):
    return {'modelo': 'text-impact-b.json', 'itens': [{'paragraph': p}]}


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

# --- licao 2: Oficinas 3 e 4 + Projeto Final (de baixo para cima) -------------
H.append(('h01_l2_pf_checklist_dez', 2, 21, [
    html('h4-pacote-final.html', trava=True),
    cont('completeBlock'),
    tp('A Parte dos Dez — atalhos do Gemini', '<p>Dez hábitos para levar do mutirão para o seu dia a dia:</p>'),
    lista([
        '<p><strong>“/” chama suas habilidades.</strong> Instrução repetida vira habilidade.</p>',
        '<p><strong>Cite o assunto exato</strong> ao pedir algo do Gmail; nada de “resuma meus e-mails”.</p>',
        '<p><strong>Chat temporário</strong> para o que não deve ir para o Histórico.</p>',
        '<p><strong>O Histórico é a chave dos apps.</strong> Sem ele, Gmail e Agenda não respondem.</p>',
        '<p><strong>Primeiro as 5 linhas</strong> de qualquer planilha.</p>',
        '<p><strong>Canvas para o texto que vai sair do Gemini</strong> — e exporte para o Documentos.</p>',
        '<p><strong>Confira a Agenda</strong> depois que o Gemini criar um evento.</p>',
        '<p><strong>Verifique a resposta</strong> com a Pesquisa Google, mas confie no trecho que você leu.</p>',
        '<p><strong>Alt + Espaço</strong> abre o Gemini no Windows sem sair do que você está fazendo.</p>',
        '<p><strong>“O que você sabe sobre mim?”</strong> mostra a memória; apague o que não deve ficar.</p>',
    ]),
]))
H.append(('h02_l2_pf_separador', 2, 18, [cont()]))
H.append(('h03_l2_o4_separador', 2, 12, [cont()]))
H.append(('h04_l2_o3_pedido_gmail', 2, 7, [html('h3-pedido-gmail.html')]))

# --- licao 1: Oficina 2 ---------------------------------------------------------
H.append(('h05_l1_o2_mesas', 1, 12, [html('h2-mesas.html')]))

# --- licao 0: preparacao antes da Oficina 1 ------------------------------------
H.append(('h06_l0_preparacao', 0, 0, [
    tp('Antes de arregaçar as mangas', '<p>Mão na massa do começo ao fim. O caso é fictício: a associação de moradores de Vila Serena vai fazer o <strong>Mutirão de Orientação Cidadã</strong>, um sábado de atendimento gratuito sobre consumidor, previdência, família e trabalho — e quem organiza é você. Cada oficina resolve uma parte; no Projeto Final, tudo vira um pacote para a coordenação. Duração total: 119 minutos.</p>'),
    tp('O mapa da mão na massa', '<p>As oficinas são em sequência: a habilidade criada na Oficina 1 acompanha todas as outras.</p>'),
    lista([
        '<p><strong>Oficina 1 (20 min):</strong> parar de repetir as mesmas instruções em toda conversa.</p>',
        '<p><strong>Oficina 2 (20 min):</strong> entender 30 inscrições sem contar na mão.</p>',
        '<p><strong>Oficina 3 (20 min):</strong> achar o pedido no e-mail e marcar a reunião sem digitar nada na Agenda.</p>',
        '<p><strong>Oficina 4 (20 min):</strong> escrever o comunicado e levá-lo para o Documentos Google.</p>',
        '<p><strong>Projeto Final (26 min):</strong> entregar o pacote do mutirão à coordenação.</p>',
    ]),
    imp('<p>🔑 <strong>Regra de ouro:</strong> o Gemini enxerga sua conta Google — então você decide o que ele vê, e confere tudo o que ele escreve na sua Agenda.</p>'),
    html('h1-preparacao.html', trava=True),
    cont('completeBlock'),
]))

# ====================================================================== ESSENTIALS
E = []
E.append(('e01_l0_kc_idade', 0, 11, [
    kc('Uma estagiária de 16 anos entrou no Gemini com a conta Google pessoal dela, no plano gratuito, mas não encontra a opção Habilidades em Personalizar. O que explica?', [
        ('Conta pessoal não dá acesso ao Gemini antes dos 18 anos', False, 'Não. A conta pessoal permite usar o Gemini a partir de 13 anos.'),
        ('As habilidades estão disponíveis, por ora, só para maiores de 18 anos', True, 'Correto. A partir de 13 anos o Gemini funciona, mas habilidades (e os planos Pro e Ultra) são, por ora, para maiores de 18. A rota é colar as instruções no início da conversa.'),
        ('Habilidades exigem o plano Google AI Pro', False, 'Não. As habilidades estão no plano gratuito, com uso limitado.'),
        ('Ela atingiu o limite de uso das últimas 5 horas', False, 'Não. Quando o limite chega, a interface avisa quando o recurso volta; a opção não desaparece do menu.'),
    ]),
]))
E.append(('e02_l1_monte_pedido', 1, 18, [html('e1-monte-pedido.html')]))
E.append(('e03_l2_historico', 2, 7, [html('e2-historico.html')]))
E.append(('e04_l3_camadas', 3, 7, [html('e3-camadas.html')]))
E.append(('e05_l4_ja_conferi', 4, 7, [html('e4-ja-conferi.html')]))
E.append(('e06_l5_kc_arquivo', 5, 10, [
    kc('Você quer que o Gemini calcule a média diária de atendimentos de uma planilha que traz nome e telefone de cada cliente. Você usa conta pessoal. Qual é a conduta adequada?', [
        ('Enviar a planilha inteira, porque o arquivo só será usado para o cálculo', False, 'Não. Arquivo enviado é dado tratado: nomes e telefones de clientes são sinal vermelho.'),
        ('Enviar e excluir a conversa logo depois', False, 'Não. Conversas lidas por revisores humanos ficam até 3 anos, mesmo depois de excluídas.'),
        ('Enviar só as colunas de dia e de atendimentos, sem nomes nem telefones', True, 'Correto. Sem dado que identifique pessoa, o arquivo passa a sinal verde — e o cálculo continua possível.'),
        ('Usar o chat temporário para enviar a planilha inteira', False, 'Não. O chat temporário fica salvo por cerca de 2 meses e não muda a cor do conteúdo: dados de clientes continuam em sinal vermelho.'),
    ]),
]))
E.append(('e07_l6_comparacao', 6, 12, [html('e5-comparacao.html')]))


def gravar(roteiros, pasta):
    pasta.mkdir(parents=True, exist_ok=True)
    for nome, licao, posicao, blocos in roteiros:
        (pasta / f'{nome}.json').write_text(json.dumps({'licao': licao, 'posicao': posicao, 'blocos': blocos}, ensure_ascii=False, indent=1), encoding='utf-8')
        print(pasta.parent.parent.name, nome, 'licao', licao, 'pos', posicao, len(blocos), 'blocos')


if __name__ == '__main__':
    gravar(H, AQUI / 'hands-on' / 'gemini-hands-on-blocos' / 'trabalho' / 'roteiros')
    gravar(E, AQUI / 'essentials' / 'gemini-essentials-blocos' / 'trabalho' / 'roteiros')
