"""Gera revisao_textos/L01.json a L03.json (texto novo por caminho do campo) para o aplicar_mapas.py.

Fonte: Pesquisa Conteudo Onda 1/Ementa Completa/perplexity-essentials/roteiros/roteiro-articulate-hands-on.md
Escrito em Python so para evitar erro de escape de aspas no JSON. Recusa sobrescrever.
"""
import json
import pathlib

AQUI = pathlib.Path(__file__).resolve().parent
SAIDA = AQUI / 'revisao_textos'


def bc(caminho):
    """Breadcrumb do roteiro em negrito, com '>' escapado como no Rise."""
    return '<strong>' + caminho.replace('>', '&gt;') + '</strong>'


def dig(texto):
    """Texto a digitar, em paragrafo proprio e em italico."""
    return f'<p><em>{texto}</em></p>'


SEP = '<p></p>'

# ---------------------------------------------------------------- Licao 1
L01 = {
    'items.0.items.0.heading': 'Antes de arregaçar as mangas',
    'items.0.items.0.paragraph': (
        '<p>Este curso é mão na massa. A Perplexity é um motor de respostas: você pergunta, ela pesquisa a web '
        'e devolve um texto com numerozinhos — as citações — mostrando de onde tirou cada ideia. Pense num resumo '
        'cheio de post-its: o post-it diz em que livro procurar, mas não garante que o livro diga aquilo. Aqui você '
        'vai aprender a abrir o livro. Basta o plano gratuito.</p>'),
    'items.1.items.0.paragraph': (
        '<p>Nesta lição você deixa a conta pronta e faz a Oficina 1, com o caso que acompanha todo o curso: '
        'um pedido de cartão negado em dez segundos por um sistema automático. Ao final desta lição, você será '
        'capaz de:</p>'),
    'items.2.items.0.paragraph': '<p>Preparar a conta e localizar os controles de privacidade da Perplexity.</p>',
    'items.2.items.1.paragraph': '<p>Decidir, pelo semáforo, o que pode e o que não pode entrar numa pergunta.</p>',
    'items.2.items.2.paragraph': ('<p>Transformar uma dúvida vaga numa pergunta pesquisável, com as cinco partes '
                                  'e as três exigências de pesquisador.</p>'),
    'items.2.items.3.paragraph': ('<p>Usar a pergunta de acompanhamento e saber quando começar uma pesquisa '
                                  'nova.</p>'),
    'items.4.items.0.heading': 'Deixe a Perplexity pronta',
    'items.4.items.0.paragraph': ('<p>Abra cada item antes da primeira pergunta. O último é o passo a passo da '
                                  'conta e da privacidade:</p>'),
    'items.5.items.0.title': 'O caminho das oficinas',
    'items.5.items.0.description': (
        '<p>As oficinas seguem um mesmo caso — um cartão negado por sistema automático — e cada uma entrega uma '
        'pequena vitória; o Projeto Final junta todas num tema seu.</p>' + SEP +
        '<ul><li><strong>Oficina 1</strong> — Da pergunta vaga à pergunta pesquisável (20 min)</li>'
        '<li><strong>Oficina 2</strong> — Mesma pergunta, dois níveis, fontes trancadas (20 min)</li>'
        '<li><strong>Oficina 3</strong> — Abra a citação e prove que existe (20 min)</li>'
        '<li><strong>Oficina 4</strong> — Escreva sua síntese citada e guarde no Projeto (20 min)</li>'
        '<li><strong>Projeto Final</strong> — O dossiê citado do seu tema (16 min)</li></ul>'),
    'items.5.items.1.title': 'O que você precisa ter aberto agora',
    'items.5.items.1.description': (
        '<ul><li>Um computador com internet (o app do celular serve, mas os caminhos do curso são da versão web).</li>'
        '<li>O navegador em perplexity.ai.</li>'
        '<li>Uma conta gratuita (e-mail ou Conta Google). Dá para pesquisar sem login, mas histórico, Projetos e '
        'privacidade só existem com conta.</li>'
        '<li>Um bloco de notas (papel ou arquivo) para as fichas.</li></ul>'),
    'items.5.items.2.title': 'Regra de ouro, cota e um alerta',
    'items.5.items.2.description': (
        '<p>🔑 <strong>Regra de ouro:</strong> a citação mostra onde conferir, não prova que está certo. Clicou, '
        'leu, comparou — só então use.</p>' + SEP +
        '<p>📌 <strong>Não esqueça:</strong> o plano gratuito dá 3 Pesquisas Pro por dia e 1 Research por mês '
        '(ajuda oficial, 02/09/2026). Este curso usa no máximo duas Pesquisas Pro e nenhuma Research.</p>' + SEP +
        '<p>📌 <strong>Não esqueça:</strong> tribunais brasileiros já multaram advogados por citar jurisprudência '
        'inventada por IA (TJPR, STJ e TSE, entre 2025 e 2026). Em todos os casos, a culpa foi de quem assinou sem '
        'conferir — não da máquina.</p>'),
    'items.5.items.3.title': 'Confira sua conta e sua privacidade',
    'items.5.items.3.description': (
        '<ol><li>Entre em perplexity.ai e faça login (ou crie a conta em '
        + bc('perplexity.ai > botão de cadastro/entrada > e-mail ou Conta Google') + ').</li>'
        '<li>Abra ' + bc('perplexity.ai > menu da conta > Configurações') + ' [conferir].</li>'
        '<li>Procure ' + bc('Configurações > Retenção de Dados de IA') + ' (AI Data Usage) [conferir] — é o '
        'controle que decide se seus dados ajudam a treinar a IA — e escolha se quer desligar.</li>'
        '<li>Ainda em Configurações, encontre "Memória". Ela guarda preferências entre conversas. Para este curso, '
        'tanto faz; só saiba onde fica.</li>'
        '<li>Volte à tela inicial e localize o botão "navegação anônima".</li></ol>' + SEP +
        '<p>🏁 <strong>Ponto de controle:</strong> você encontrou o controle de dados e a Memória nas '
        'Configurações e, na tela inicial, o botão "navegação anônima". Se algum nome estiver diferente, anote — a '
        'Perplexity muda os rótulos com frequência.</p>' + SEP +
        '<p>⚠️ <strong>Cuidado:</strong> navegação anônima não é invisibilidade. Ela não salva o histórico entre '
        'sessões, mas a pergunta continua indo para os servidores da Perplexity.</p>'),
    'items.6.items.0.heading': 'Os termos da Oficina 1',
    'items.6.items.0.paragraph': '<p>Vire cada cartão para revisar os termos que você vai usar a partir de agora:</p>',
    'items.7.items.0.front.description': '<p>Citação</p>',
    'items.7.items.0.back.description': (
        '<p>O numerozinho na resposta que leva à página de origem. Mostra onde conferir — não prova que a frase '
        'está certa.</p>'),
    'items.7.items.1.back.description': (
        '<p>Dúvida sem recorte, fonte nem formato, como "A LGPD fala de inteligência artificial?". A resposta '
        'fala de tudo um pouco e não responde à sua dúvida.</p>'),
    'items.7.items.2.front.description': '<p>Pergunta pesquisável</p>',
    'items.7.items.2.back.description': (
        '<p>Tem as cinco partes — instrução, contexto, insumo, palavras-chave e formato — e as três exigências de '
        'pesquisador: fontes aceitas, recorte e "o que não deu para confirmar".</p>'),
    'items.7.items.1.front.description': '<p>Pergunta vaga</p>',
    'items.7.items.3.front.description': '<p>Pergunta de acompanhamento</p>',
    'items.7.items.3.back.description': (
        '<p>Feita no campo logo abaixo da resposta, ela herda a conversa. Mudou de assunto? Comece uma pesquisa '
        'nova.</p>'),
    'items.7.items.4.front.description': '<p>Semáforo</p>',
    'items.7.items.4.back.description': (
        '<p>A pergunta antes de digitar: posso escrever isto aqui? Verde (lei, decisão pública, relatório oficial) '
        'entra. Amarelo (documento interno sem dado pessoal) só resumido e sem nomes. Vermelho (nome ou CPF de '
        'cliente, paciente ou aluno; peça de processo) não entra. Neste curso, tudo é verde.</p>'),
    'items.8.items.0.title': 'Oficina 1 — Da pergunta vaga à pergunta pesquisável',
    'items.8.items.0.description': (
        '<p>Você pediu um cartão pelo app do banco e, em dez segundos, veio a resposta: negado. Nenhum humano '
        'olhou. Isso pode? Você tem algum direito? A primeira pergunta que vem à cabeça é vaga — e pergunta vaga '
        'traz resposta vaga. Nesta oficina, você transforma a dúvida numa pergunta que a Perplexity consegue '
        'pesquisar direito.</p>' + SEP +
        '<p>Você vai usar perplexity.ai na busca padrão (o modo "Pesquisar") e o molde da pergunta pesquisável, '
        'que aparece logo depois desta oficina.</p>'),
    'items.8.items.1.title': 'Deu certo?',
    'items.8.items.1.description': (
        '<p><strong>Passo 7:</strong> envie a sua reescrita numa pesquisa nova e confira se a resposta trouxe a '
        'seção "o que não foi possível confirmar".</p>' + SEP +
        '<p>Deu certo se a sua pergunta reescrita tem instrução, recorte, fontes aceitas e formato, e a resposta '
        'separou o que a lei diz do que não foi possível confirmar.</p>'),
    'items.8.items.2.title': 'Passo 1: Envie a pergunta vaga',
    'items.8.items.2.description': (
        '<p>Em ' + bc('perplexity.ai > O que você quer saber?') + ', digite e envie:</p>' + SEP +
        dig('A LGPD fala de inteligência artificial?')),
    'items.8.items.3.title': 'Passo 2: Leia a resposta',
    'items.8.items.3.description': (
        '<p>Repare: ela fala de tudo um pouco e as fontes são variadas. Não está errada — só não responde à '
        '<strong>sua</strong> dúvida.</p>'),
    'items.8.items.4.title': 'Passo 3: Monte a pergunta com as cinco partes',
    'items.8.items.4.description': (
        '<p>Use as cinco partes que a própria Perplexity recomenda: <strong>instrução</strong> (o que fazer), '
        '<strong>contexto</strong> (para quem e para quê), <strong>insumo</strong> (dados que você fornece), '
        '<strong>palavras-chave</strong> e <strong>formato</strong>. E acrescente três exigências de pesquisador: '
        'fontes aceitas, recorte e "o que não deu para confirmar".</p>'),
    'items.8.items.5.title': 'Passo 4: Envie a pergunta pesquisável',
    'items.8.items.5.description': (
        '<p>Comece uma pesquisa nova (pela caixa inicial) e envie:</p>' + SEP +
        dig('Explique, para uma pessoa iniciante, o que o art. 20 da LGPD garante a quem teve um pedido negado por '
            'uma decisão tomada unicamente por sistema automatizado. Priorize planalto.gov.br e gov.br/anpd. Para '
            'cada afirmação, indique a fonte e um trecho curto. Separe: o que a lei diz, o que a ANPD orienta e o '
            'que não foi possível confirmar. Até 200 palavras, em português do Brasil.')),
    'items.8.items.6.title': 'Passo 5: Faça a pergunta de acompanhamento',
    'items.8.items.6.description': (
        '<p>Em ' + bc('perplexity.ai > resposta > campo de acompanhamento') + ', pergunte:</p>' + SEP +
        dig('Qual é exatamente o direito previsto no caput do art. 20? Transcreva no máximo uma frase da lei.')),
    'items.8.items.7.title': 'Passo 6: Agora é com você',
    'items.8.items.7.description': (
        '<p>Reescreva sozinho esta pergunta vaga, com as cinco partes e as três exigências:</p>' + SEP +
        dig('Banco pode usar meus dados para negar crédito?') + SEP +
        '<p>Use o molde que aparece logo depois desta oficina.</p>'),
    'items.9.items.0.heading': 'As cinco partes e as três exigências',
    'items.9.items.0.paragraph': ('<p>Abra cada aba para ver o papel de cada parte, com exemplos tirados da '
                                  'pergunta do art. 20. A última aba traz o molde para copiar:</p>'),
    'items.10.items.0.description': (
        '<p>É o verbo que diz o que a Perplexity deve fazer: "explique", "liste", "compare", "resuma". Cada verbo '
        'pede um tipo de resposta — "liste" traz uma enumeração; "explique" traz um texto corrido.</p>' + SEP +
        '<p>Na pergunta do art. 20: <em>"Explique…"</em>.</p>'),
    'items.10.items.1.description': (
        '<p>Diz para quem e para quê é a resposta. Sem ele, a resposta mira num leitor médio que não é você.</p>'
        + SEP + '<p>Na pergunta do art. 20: <em>"para uma pessoa iniciante"</em> e <em>"a quem teve um pedido '
        'negado"</em>.</p>'),
    'items.10.items.2.description': (
        '<p>São os dados que você fornece: a sua situação, um trecho, um número de processo, um link. Quanto mais '
        'concreto o insumo, menos a resposta precisa adivinhar.</p>' + SEP +
        '<p>Na pergunta do art. 20: <em>"um pedido negado por uma decisão tomada unicamente por sistema '
        'automatizado"</em>.</p>'),
    'items.10.items.3.description': (
        '<p>Os termos que delimitam o assunto e guiam a busca. Prefira o termo técnico ao jeito coloquial de '
        'dizer.</p>' + SEP +
        '<p>Na pergunta do art. 20: <em>"art. 20"</em>, <em>"LGPD"</em>, <em>"decisão tomada unicamente por '
        'sistema automatizado"</em>.</p>'),
    'items.10.items.4.description': (
        '<p>Diz como a resposta deve chegar: tamanho, idioma, tópicos ou tabela. Formato definido facilita '
        'conferir e comparar.</p>' + SEP +
        '<p>Na pergunta do art. 20: <em>"Até 200 palavras, em português do Brasil"</em>.</p>'),
    'items.10.items.5.description': (
        '<p>Três pedidos de quem vai conferir a resposta: <strong>fontes aceitas</strong> ("Priorize '
        'planalto.gov.br e gov.br/anpd"), <strong>recorte</strong> (país, período) e a seção <strong>"o que não foi '
        'possível confirmar"</strong>.</p>' + SEP +
        '<p>Molde da pergunta pesquisável:</p>' + SEP +
        '<p>"""<br>[Instrução] [tema] para [público]. Contexto: [para quê]. Recorte: [país, período].<br>'
        'Fontes: priorize [sites]. Para cada afirmação, fonte, data e trecho curto.<br>'
        'Separe: fatos | divergências | o que não foi possível confirmar. Formato: [tamanho].<br>"""</p>'),
    'items.11.items.0.title': ('Seu pedido de cartão foi negado em dez segundos pelo app do banco e você quer '
                               'saber que direito tem. Qual destas perguntas segue o molde da pergunta '
                               'pesquisável?'),
    'items.11.items.0.answers.0.title': 'A LGPD fala de inteligência artificial?',
    'items.11.items.0.answers.0.feedback': ('Não. É a pergunta vaga da Oficina 1: não diz para quem, não tranca '
                                            'fontes nem pede o que não deu para confirmar.'),
    'items.11.items.0.answers.1.title': ('Explique, para um iniciante, o que o art. 20 da LGPD garante a quem teve '
                                         'um pedido negado por decisão automatizada. Priorize planalto.gov.br e '
                                         'gov.br/anpd e separe o que não foi possível confirmar.'),
    'items.11.items.0.answers.1.feedback': ('Correto. Tem instrução (explique), contexto (iniciante, pedido '
                                            'negado), palavras-chave (art. 20, LGPD), fontes aceitas e a seção do '
                                            'que não foi possível confirmar.'),
    'items.11.items.0.answers.2.title': 'Banco pode negar crédito com IA? Responda rápido.',
    'items.11.items.0.answers.2.feedback': ('Não. "Responda rápido" não é formato: faltam recorte, fontes aceitas '
                                            'e a seção do que não foi possível confirmar.'),
    'items.11.items.0.answers.3.title': 'Explique tudo sobre decisão automatizada, com o máximo de detalhes.',
    'items.11.items.0.answers.3.feedback': ('Não. Tem instrução, mas sem contexto, recorte nem fontes: "tudo" e '
                                            '"o máximo" levam de volta à resposta que fala de tudo um pouco.'),
    'items.12.items.0.paragraph': (
        '<p>💡 <strong>Dica:</strong> a pergunta de acompanhamento "herda" a conversa — você não precisa repetir o '
        'assunto. Mas, se mudar de tema, comece uma pesquisa nova, senão a resposta pode misturar as duas '
        'coisas.</p>'),
    'items.13.items.0.heading': 'Se travar',
    'items.13.items.0.paragraph': '<p>Abra o problema que apareceu para você e veja o que fazer:</p>',
    'items.16.items.0.heading': 'Pergunta vaga ou pesquisável?',
    'items.16.items.0.paragraph': ('<p>Arraste cada pergunta para a pilha certa. Antes de decidir, procure '
                                   'instrução, recorte, fontes aceitas e formato:</p>'),
    'items.17.items.0.title': 'Explique o art. 20 da LGPD a iniciantes, só com planalto.gov.br, em 200 palavras',
    'items.17.items.2.title': 'Liste, em até 150 palavras, os direitos do art. 20 da LGPD, com fonte e data',
    'items.17.piles.0.title': 'Pesquisável',
    'items.18.items.0.paragraph': (
        '<p>🏁 <strong>Ponto de controle:</strong> em ' + bc('perplexity.ai > barra lateral > Recentes')
        + ', aparecem três pesquisas separadas (a vaga, a pesquisável e a sua reescrita).</p>'),
    'items.19.items.0.paragraph': (
        '<p>Na próxima lição, você tranca as fontes nos domínios oficiais, compara a busca padrão com a Pesquisa '
        'Pro e abre as citações para provar que elas existem. A pergunta do art. 20 volta na Oficina 2 — deixe '
        'as pesquisas desta oficina em Recentes.</p>'),
}

# ---------------------------------------------------------------- Licao 2
L02 = {
    'items.0.items.0.heading': 'Tranque as fontes e abra as citações',
    'items.0.items.0.paragraph': (
        '<p>A resposta da Oficina 1 trouxe fontes de blogs, escritórios e sites que você nem conhece. Você queria '
        'a lei e a ANPD. E ficou a dúvida: a busca rápida basta, ou vale gastar uma das três Pesquisas Pro do dia? '
        'Na primeira parte desta lição, você tranca as fontes e compara os dois níveis de busca lado a lado. Na '
        'segunda, abre as citações e prova que elas existem.</p>'),
    'items.1.items.0.paragraph': '<p>Esta lição reúne as Oficinas 2 e 3. Ao final dela, você será capaz de:</p>',
    'items.2.items.0.paragraph': ('<p>Trancar as fontes nos domínios oficiais escrevendo a restrição na própria '
                                  'pergunta — e conferir se ela foi obedecida.</p>'),
    'items.2.items.1.paragraph': ('<p>Comparar a busca padrão com a Pesquisa Pro e dizer qual respondeu melhor a '
                                  'uma pergunta específica.</p>'),
    'items.2.items.2.paragraph': ('<p>Auditar uma citação com a ficha de seis perguntas e decidir se ela fica, é '
                                  'trocada ou sai.</p>'),
    'items.2.items.3.paragraph': ('<p>Provar que uma decisão judicial existe, conferindo os dados no portal do '
                                  'tribunal.</p>'),
    'items.4.items.0.heading': 'Busca padrão ou Pesquisa Pro?',
    'items.4.items.0.paragraph': '<p>Compare, nas abas, os dois níveis de busca e quando vale gastar a cota:</p>',
    'items.5.items.0.description': (
        '<p>É o modo "Pesquisar", o mesmo da Oficina 1: rápido e sem cota. Sem restrição, ela traz o que achar — '
        'blogs e escritórios inclusive.</p>' + SEP +
        '<p>Para trancar as fontes, escreva a restrição na pergunta ("Use apenas fontes dos domínios '
        'planalto.gov.br e gov.br/anpd") e depois conte, na lista de fontes, quem obedeceu.</p>'),
    'items.5.items.1.description': (
        '<p>Fica no seletor junto à caixa de pergunta [conferir]. Ela mostra as buscas que está fazendo e demora '
        'mais. No plano gratuito são 3 por dia; esta oficina usa uma.</p>' + SEP +
        '<p>Não achou a Pesquisa Pro ou a cota acabou? Plano B: na busca padrão, acrescente "Antes de responder, '
        'faça pelo menos três buscas diferentes" e use o resultado na segunda coluna do quadro.</p>'),
    'items.5.items.2.description': (
        '<p>Quem decide é o quadro comparativo, não a fama do modo. Use a busca padrão para começar e para dúvidas '
        'rápidas; guarde a Pesquisa Pro para a pergunta difícil.</p>' + SEP +
        '<p>Ao fim da oficina, você deve conseguir dizer, numa frase, qual nível respondeu melhor <strong>a '
        'esta</strong> pergunta e por quê.</p>'),
    'items.6.items.0.title': 'Oficina 2 — Mesma pergunta, dois níveis, fontes trancadas',
    'items.6.items.0.description': (
        '<p>Você vai mandar a mesma pergunta duas vezes — na busca padrão e na Pesquisa Pro — com as fontes '
        'trancadas na lei e na ANPD, e contar quem obedeceu.</p>' + SEP +
        '<p>Você vai usar a busca padrão, a Pesquisa Pro (ou o plano B) e o quadro comparativo, que aparece logo '
        'depois desta oficina.</p>'),
    'items.6.items.1.title': 'Deu certo?',
    'items.6.items.1.description': (
        '<p>Deu certo se o quadro está preenchido nas duas colunas e você consegue dizer, numa frase, qual nível '
        'respondeu melhor <strong>a esta</strong> pergunta e por quê.</p>' + SEP +
        '<p>🏁 <strong>Ponto de controle:</strong> em ' + bc('perplexity.ai > resposta > lista de fontes')
        + ', nas duas pesquisas, você contou as fontes oficiais.</p>'),
    'items.6.items.2.title': 'Passo 1: Envie na busca padrão',
    'items.6.items.2.description': (
        '<p>Comece uma pesquisa nova e envie, na busca padrão:</p>' + SEP +
        dig('Explique, para uma pessoa iniciante, o que o art. 20 da LGPD (Lei nº 13.709/2018) garante ao titular '
            'diante de decisões tomadas unicamente com base em tratamento automatizado. Use apenas fontes dos '
            'domínios planalto.gov.br e gov.br/anpd; se não houver evidência nesses domínios, avise. Para cada '
            'afirmação, indique a fonte, a data e um trecho curto. Separe: o que a lei diz, o que a ANPD orienta e '
            'o que não foi possível confirmar. Até 200 palavras.')),
    'items.6.items.3.title': 'Passo 2: Conte as fontes',
    'items.6.items.3.description': (
        '<p>Abra ' + bc('perplexity.ai > resposta > lista de fontes') + '. Conte quantas são e quantas são de '
        'planalto.gov.br ou gov.br/anpd.</p>'),
    'items.6.items.4.title': 'Passo 3: Envie na Pesquisa Pro',
    'items.6.items.4.description': (
        '<p>Comece outra pesquisa nova, escolha '
        + bc('perplexity.ai > seletor junto à caixa de pergunta > Pesquisa Pro') + ' [conferir] e envie o mesmo '
        'texto.</p>'),
    'items.6.items.5.title': 'Passo 4: Observe e conte de novo',
    'items.6.items.5.description': ('<p>A Pesquisa Pro mostra as buscas que está fazendo e demora mais. Quando '
                                    'terminar, conte as fontes de novo.</p>'),
    'items.6.items.6.title': 'Passo 5: Agora é com você — preencha o quadro',
    'items.6.items.6.description': (
        '<p>Preencha o quadro comparativo (logo depois desta oficina), uma coluna para cada nível: número de '
        'fontes, número de fontes oficiais pedidas, se apareceu "não foi possível confirmar", uma frase que parece '
        'bem apoiada e uma frase que você vai conferir na Oficina 3.</p>'),
    'items.6.items.7.title': 'Passo 6: Cobre a restrição',
    'items.6.items.7.description': (
        '<p>Se alguma fonte escapou dos domínios, responda no Thread:</p>' + SEP +
        dig('Refaça usando apenas planalto.gov.br e gov.br/anpd.') + SEP + '<p>Conte de novo.</p>'),
    'items.7.items.0.paragraph': (
        '<p>🤓 <strong>Curiosidade técnica:</strong> a Perplexity não garante obedecer a operadores como '
        '<em>site:</em> ou <em>AND/OR</em>, típicos de buscadores tradicionais. O jeito documentado de trancar '
        'fontes é escrever a restrição na pergunta — e conferir, uma a uma, se ela obedeceu.</p>'),
    'items.8.items.0.heading': 'Se travar na Oficina 2',
    'items.8.items.0.paragraph': '<p>Abra o problema que apareceu para você e veja o que fazer:</p>',
    'items.10.items.0.heading': 'O quadro comparativo',
    'items.10.items.0.paragraph': (
        '<p>Copie o quadro no seu bloco de notas, com uma coluna para a busca padrão e outra para a Pesquisa Pro '
        '(ou o plano B):</p><ul>'
        '<li><strong>Nº de fontes</strong></li>'
        '<li><strong>Nº de fontes oficiais pedidas</strong> (planalto.gov.br ou gov.br/anpd)</li>'
        '<li><strong>Apareceu "não foi possível confirmar"?</strong></li>'
        '<li><strong>Uma frase que parece bem apoiada</strong></li>'
        '<li><strong>Uma frase que você vai conferir na Oficina 3</strong></li></ul>'
        '<p>Com as duas colunas cheias, responda numa frase: qual nível respondeu melhor a esta pergunta, e por '
        'quê? A última linha do quadro é o ponto de partida da próxima oficina.</p>'),
    'items.11.items.0.heading': 'Os termos para conferir fontes',
    'items.11.items.0.paragraph': '<p>Vire cada cartão para revisar os termos das duas oficinas desta lição:</p>',
    'items.12.items.0.back.description': (
        '<p>O site de quem produziu o documento: planalto.gov.br para a lei, gov.br/anpd para a ANPD, '
        'portal.tjpr.jus.br para o tribunal.</p>'),
    'items.12.items.1.back.description': (
        '<p>O documento original (a lei, o acórdão, o relatório oficial). É o que sustenta uma afirmação '
        'decisiva.</p>'),
    'items.12.items.2.back.description': (
        '<p>Notícia ou blog sobre o documento original: bom para contexto, fraco para afirmação decisiva.</p>'),
    'items.12.items.3.front.description': '<b>Fontes trancadas</b>',
    'items.12.items.3.back.description': (
        '<p>A restrição escrita na pergunta: "use apenas planalto.gov.br e gov.br/anpd". Depois, conte na lista de '
        'fontes quem obedeceu.</p>'),
    'items.12.items.4.back.description': (
        '<p>A seção em que a resposta declara o que ficou sem evidência. Lacuna declarada vale mais que lacuna '
        'escondida.</p>'),
    'items.13.items.0.title': (
        'Você mandou a pergunta do art. 20 com a restrição "use apenas planalto.gov.br e gov.br/anpd" e recebeu '
        'duas respostas. Marque uma avaliação para cada uma.\n\n'
        'Pergunta 1:\nA resposta cita apenas planalto.gov.br e traz a seção "não foi possível confirmar" para os '
        'pontos sem fonte.\n\n'
        'Pergunta 2:\nA resposta mistura fontes de blogs e sites oficiais, sem separar o que veio de cada um.'),
    'items.15.items.0.title': 'Oficina 3 — Abra a citação e prove que existe',
    'items.15.items.0.description': (
        '<p>A resposta parece ótima, cheia de numerozinhos. Mas um teste independente (Tow Center, 2025) encontrou '
        'erro de citação em 37% das respostas da Perplexity — e ela foi a <strong>melhor</strong> de oito '
        'ferramentas. Imagine levar uma dessas para uma prova, uma reportagem ou uma petição. Nesta oficina, você '
        'abre o livro indicado pelo post-it.</p>' + SEP +
        '<p>Você vai usar a resposta da Oficina 2, a ficha de auditoria e o acórdão no portal do TJPR: '
        'https://portal.tjpr.jus.br/jurisprudencia/j/4100000035121351/Ac%C3%B3rd%C3%A3o-0033052-89.2025.8.16.0001'
        '</p>'),
    'items.15.items.1.title': 'Deu certo?',
    'items.15.items.1.description': (
        '<p>Deu certo se as duas citações têm decisão (manter, trocar ou retirar) e a ficha do TJPR foi marcada '
        'olhando o <strong>portal</strong>, não a resposta.</p>'),
    'items.15.items.2.title': 'Passo 1: Siga a citação',
    'items.15.items.2.description': (
        '<p>Na resposta da Oficina 2, escolha a frase que você marcou para conferir e siga '
        + bc('resposta > número da citação > página de origem') + '.</p>'),
    'items.15.items.3.title': 'Passo 2: Procure a palavra-chave',
    'items.15.items.3.description': ('<p>Na página que abrir, aperte Ctrl+F e procure uma palavra-chave da '
                                     'frase.</p>'),
    'items.15.items.4.title': 'Passo 3: Preencha a ficha de auditoria',
    'items.15.items.4.description': (
        '<p>Responda às seis perguntas para essa citação e, depois, para uma segunda citação:</p><ul>'
        '<li>A página existe e abre?</li><li>Quem publicou? É quem a resposta diz?</li>'
        '<li>Qual a data? Serve para o tema?</li><li>O trecho que apoia a frase está lá?</li>'
        '<li>O escopo bate (país, período, público)?</li><li>É fonte primária (o documento original)?</li></ul>'),
    'items.15.items.5.title': 'Passo 4: Decida — manter, trocar ou retirar',
    'items.15.items.5.description': (
        '<p>Feche a ficha de cada citação com uma decisão: <strong>manter</strong> (a página sustenta a frase), '
        '<strong>trocar</strong> (a ideia procede, mas precisa de outra fonte) ou <strong>retirar</strong> (nada '
        'sustenta a frase).</p>'),
    'items.15.items.6.title': 'Passo 5: Peça à Perplexity que se audite',
    'items.15.items.6.description': (
        '<p>No mesmo Thread, envie:</p>' + SEP +
        dig('Releia sua resposta anterior. Para cada afirmação verificável, associe somente a fonte que contém '
            'aquela informação e transcreva o trecho curto que a sustenta. Marque como "sem apoio suficiente" o que '
            'não puder comprovar.')),
    'items.15.items.7.title': 'Passo 6: Agora é com você — prove que o acórdão existe',
    'items.15.items.7.description': (
        '<p>Comece uma pesquisa nova e envie:</p>' + SEP +
        dig('Localize o acórdão 0033052-89.2025.8.16.0001 do TJPR e informe órgão julgador, relator, data de '
            'julgamento e consequência aplicada. Use apenas portal.tjpr.jus.br. Para cada campo, mostre o link '
            'oficial. Se qualquer campo não estiver na página oficial, escreva NÃO ENCONTRADO.') + SEP +
        '<p>Anote o que a IA disse. Depois abra o link oficial do acórdão e marque, campo a campo (órgão julgador, '
        'relator, data de julgamento, consequência): a Perplexity disse / o portal mostra / confere?</p>'),
    'items.16.items.0.heading': 'Primária ou secundária?',
    'items.16.items.0.paragraph': (
        '<p>💡 Fonte primária é o documento original (a lei, o acórdão, o relatório oficial). Notícia ou blog sobre '
        'ele é fonte secundária: bom para contexto, fraco para afirmação decisiva. Arraste cada fonte para a pilha '
        'certa:</p>'),
    'items.18.items.0.paragraph': (
        '<p>🏁 <strong>Ponto de controle:</strong> no portal do TJPR, o acórdão 0033052-89.2025.8.16.0001 '
        '(consultado em 18/10/2026) mostra 7ª Câmara Cível, relator desembargador Fabian Schweitzer, julgado em '
        '01/06/2026, com ementa sobre precedentes inexistentes, multa e ofício à OAB. Ironia do destino: você '
        'acabou de conferir um caso sobre quem não conferiu.</p>'),
    'items.19.items.0.paragraph': (
        '<p>Na próxima lição, você usa a ficha de auditoria para escrever uma síntese citada, guarda o trabalho '
        'num Projeto da Perplexity e decide se compartilha. Guarde a ficha: ela volta na Oficina 4.</p>'),
}

# ---------------------------------------------------------------- Licao 3
L03 = {
    'items.0.items.0.heading': 'Escreva sua síntese citada',
    'items.0.items.0.paragraph': (
        '<p>Agora você precisa entregar: um parágrafo para o trabalho, uma nota para a pauta, um resumo para o '
        'parecer. Pedir "faz um resumo" à IA e copiar é exatamente o que este curso evita. Nesta oficina, a '
        'Perplexity faz o rascunho, você faz a auditoria — e o texto final é seu.</p>'),
    'items.1.items.0.paragraph': ('<p>Esta lição traz a Oficina 4 e fecha o curso com os hábitos para levar. Ao '
                                  'final dela, você será capaz de:</p>'),
    'items.2.items.0.paragraph': ('<p>Criar um Projeto na Perplexity com instruções que valem para as pesquisas '
                                  'feitas dentro dele.</p>'),
    'items.2.items.1.paragraph': ('<p>Pedir um rascunho citado e auditar cada parágrafo com a ficha da '
                                  'Oficina 3.</p>'),
    'items.2.items.2.paragraph': ('<p>Separar fato, inferência e lacuna e escrever a seção "Limites desta síntese" '
                                  'com suas palavras.</p>'),
    'items.2.items.3.paragraph': ('<p>Decidir se compartilha a pesquisa — e conferir o que um link público '
                                  'expõe.</p>'),
    'items.4.items.0.heading': 'Antes de escrever',
    'items.4.items.0.paragraph': ('<p>Abra cada item para ver o que muda quando a IA faz o rascunho e você faz a '
                                  'auditoria:</p>'),
    'items.5.items.0.title': 'Por que não basta pedir um resumo',
    'items.5.items.0.description': (
        '<p>Um resumo pedido à IA e copiado carrega todos os problemas que você viu na Oficina 3: citação que não '
        'sustenta a frase, fonte secundária no lugar da lei, lacuna escondida.</p>' + SEP +
        '<p>Na síntese citada, cada parágrafo termina com a fonte que sustenta exatamente a frase anterior, e você '
        'confere uma a uma. O que não tiver apoio é reescrito ou sai.</p>'),
    'items.5.items.1.title': 'Projetos: a pasta da sua pesquisa',
    'items.5.items.1.description': (
        '<p>Projetos é o nome novo dos antigos Spaces, desde agosto de 2026. Ficam em '
        + bc('perplexity.ai > barra lateral > Projetos > Criar projeto') + '.</p>' + SEP +
        '<p>Um Projeto guarda as pesquisas de um mesmo tema e tem um campo de instruções: o que você escreve ali '
        '(idioma, tipo de fonte, como marcar lacunas) acompanha as pesquisas feitas dentro dele. Se "Criar '
        'projeto" não aparecer no seu plano, faça tudo num Thread normal e cole a instrução no começo da '
        'pergunta [conferir disponibilidade no gratuito].</p>'),
    'items.5.items.2.title': 'A ficha da Oficina 3 volta',
    'items.5.items.2.description': (
        '<p>Cada parágrafo do rascunho ganha uma coluna da ficha de auditoria: a página existe, quem publicou, a '
        'data, o trecho, o escopo, se é fonte primária — e a decisão de manter, trocar ou retirar.</p>' + SEP +
        '<p>Para a frase central sobre o art. 20, vá direto à fonte primária: o texto compilado da LGPD no '
        'Planalto, com Ctrl+F em "Art. 20".</p>'),
    'items.5.items.3.title': 'Se for anexar um PDF',
    'items.5.items.3.description': (
        '<p>⚠️ <strong>Cuidado:</strong> se anexar um PDF a uma pesquisa ('
        + bc('perplexity.ai > + (Adicionar arquivos ou ferramentas) > Enviar arquivos ou imagens')
        + '), passe antes pelo semáforo. E PDF escaneado como imagem pode não ser lido — prefira o arquivo com '
        'texto selecionável.</p>'),
    'items.6.items.0.title': 'Oficina 4 — Escreva sua síntese citada e guarde no Projeto',
    'items.6.items.0.description': (
        '<p>Você vai criar um Projeto, pedir à Perplexity um rascunho sobre o art. 20 com fonte em cada parágrafo, '
        'auditar o rascunho e terminar com uma síntese que você assinaria.</p>' + SEP +
        '<p>Você vai usar ' + bc('perplexity.ai > barra lateral > Projetos > Criar projeto') + ', a ficha de '
        'auditoria da Oficina 3 e o texto compilado da LGPD: '
        'https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm</p>'),
    'items.6.items.1.title': 'Deu certo?',
    'items.6.items.1.description': (
        '<p>Deu certo se você tem uma síntese de 150 a 200 palavras, cada parágrafo com citação conferida na ficha, '
        'a seção "Limites desta síntese" escrita por você e a decisão de compartilhamento registrada.</p>'),
    'items.6.items.2.title': 'Passo 1: Crie o Projeto',
    'items.6.items.2.description': (
        '<p>Vá a ' + bc('perplexity.ai > barra lateral > Projetos > Criar projeto') + ' e dê o nome "Pesquisa '
        'citada — LGPD".</p>'),
    'items.6.items.3.title': 'Passo 2: Cole as instruções do Projeto',
    'items.6.items.3.description': (
        '<p>No campo de instruções do Projeto, cole:</p>' + SEP +
        dig('Responder em português do Brasil; separar fato, inferência e lacuna; priorizar fontes primárias e '
            'oficiais; informar a data de cada fonte; escrever NÃO ENCONTRADO quando não houver evidência.')),
    'items.6.items.4.title': 'Passo 3: Peça o rascunho citado',
    'items.6.items.4.description': (
        '<p>Dentro do Projeto, envie:</p>' + SEP +
        dig('Com base apenas em fontes oficiais (planalto.gov.br e gov.br/anpd), redija uma síntese de 150 a 200 '
            'palavras sobre o direito previsto no art. 20 da LGPD. Cada parágrafo deve terminar com a citação que '
            'sustenta exatamente a frase anterior. Não acrescente informação sem fonte. Termine com a seção '
            '"Limites desta síntese".')),
    'items.6.items.5.title': 'Passo 4: Audite parágrafo por parágrafo',
    'items.6.items.5.description': ('<p>Para cada parágrafo, abra a citação e preencha uma coluna da ficha da '
                                    'Oficina 3.</p>'),
    'items.6.items.6.title': 'Passo 5: Confirme a frase central na lei',
    'items.6.items.6.description': ('<p>Abra o texto compilado da LGPD, aperte Ctrl+F, busque "Art. 20" e confirme '
                                    'a frase central.</p>'),
    'items.6.items.7.title': 'Passo 6: Agora é com você — corte o que não tem apoio',
    'items.6.items.7.description': '<p>Reescreva ou apague toda frase que ficou sem apoio na ficha.</p>',
    'items.6.items.8.title': 'Passo 7: Escreva "Limites desta síntese"',
    'items.6.items.8.description': ('<p>Com suas palavras: o que não deu para confirmar, o período coberto e alguma '
                                    'fonte que você não conseguiu abrir.</p>'),
    'items.6.items.9.title': 'Passo 8: Decida se compartilha',
    'items.6.items.9.description': (
        '<p>Vai compartilhar? Se sim, revise a pesquisa inteira, use ' + bc('pesquisa aberta > Compartilhar')
        + ' [conferir opções] e abra o link numa janela anônima do navegador para ver o que ficou exposto. Se não, '
        'anote o motivo.</p>'),
    'items.7.items.0.heading': 'Fato, inferência, lacuna — e os limites',
    'items.7.items.0.paragraph': ('<p>Abra cada aba para ver exemplos com o art. 20 e o que conferir antes de '
                                  'compartilhar:</p>'),
    'items.8.items.0.description': (
        '<p><strong>Fato:</strong> "O art. 20 da LGPD dá ao titular o direito de pedir a revisão de decisões '
        'tomadas unicamente com base em tratamento automatizado." Está no texto da lei e leva a citação da fonte '
        'oficial.</p>' + SEP +
        '<p><strong>Inferência:</strong> "Sem regulamentação detalhada, o alcance desse direito pode ser '
        'interpretado de formas diferentes." É uma interpretação sua ou da fonte — sinalize como inferência.</p>'
        + SEP +
        '<p><strong>Lacuna:</strong> "Nesta pesquisa, não foi possível localizar orientação da ANPD específica '
        'sobre o art. 20." Diz o que você procurou e não encontrou.</p>'),
    'items.8.items.1.description': (
        '<p>Três coisas, com suas palavras: o que não deu para confirmar, o período coberto e alguma fonte que você '
        'não conseguiu abrir.</p>' + SEP +
        '<p>Exemplo: "Esta síntese usa apenas a LGPD e páginas da ANPD consultadas em outubro de 2026. Não foi '
        'possível confirmar se a ANPD publicou orientação específica sobre o art. 20. Uma página citada pela '
        'Perplexity não abriu e foi descartada."</p>'),
    'items.8.items.2.description': (
        '<p>Link público é publicação. Antes de mandar, revise a pesquisa inteira — perguntas, respostas e '
        'anexos —, use ' + bc('pesquisa aberta > Compartilhar') + ' [conferir opções] e abra o link numa janela '
        'anônima para ver o que ficou exposto.</p>' + SEP +
        '<p>Decidiu não compartilhar? Anote o motivo — por exemplo, a pesquisa ainda tem frase sem apoio ou '
        'mencionou algo que não passa no semáforo.</p>'),
    'items.9.items.0.heading': 'Cartões de revisão',
    'items.9.items.0.paragraph': ('<p>Vire cada cartão para revisar as distinções e os cuidados da Oficina '
                                  '4:</p>'),
    'items.10.items.0.back.description': (
        '<p>Primária é o documento original (a lei, o acórdão, o relatório oficial). Secundária é a notícia ou o '
        'blog sobre ele: serve para contexto, não para a afirmação decisiva.</p>'),
    'items.10.items.1.back.description': (
        '<p>No resumo automático, a IA compila e você copia. Na síntese citada, a IA faz o rascunho e você audita '
        'cada parágrafo na fonte — o texto final é seu.</p>'),
    'items.10.items.2.back.description': (
        '<p>Frase sem citação, citação que não contém o trecho e afirmação apoiada só em fonte secundária: '
        'reescreva com fonte conferida ou apague.</p>'),
    'items.10.items.3.back.description': (
        '<p>Nada que não passe no semáforo, nenhuma frase sem apoio, "Limites desta síntese" escrito — e o link '
        'testado numa janela anônima.</p>'),
    'items.11.items.0.title': (
        'Ao auditar o rascunho da sua síntese, você encontra três trechos. Como classificar cada um?\n\n'
        '1. "O art. 20 da LGPD prevê o direito de revisão de decisões automatizadas."\n'
        '2. "A falta de decisões judiciais sobre o tema indica incerteza jurídica."\n'
        '3. "Não foi possível localizar decisões judiciais sobre o art. 20 nesta pesquisa."'),
    'items.11.items.0.answers.0.feedback': (
        'Correto. O trecho 1 está no texto da lei (fato); o 2 tira uma conclusão da ausência de decisões '
        '(inferência); o 3 declara o que a pesquisa não encontrou (lacuna).'),
    'items.11.items.0.answers.1.feedback': (
        'Não. O trecho 1 está no texto da lei, então é fato, e o 2 é uma conclusão tirada da ausência de decisões, '
        'então é inferência. Só o 3 está certo como lacuna.'),
    'items.11.items.0.answers.2.feedback': (
        'Não. O trecho 2 tira uma conclusão — é inferência, não lacuna. E o 3 declara o que a pesquisa não '
        'encontrou — é lacuna, não inferência.'),
    'items.11.items.0.answers.3.feedback': (
        'Não. O trecho 1 está no texto da lei, então é fato, e o 3 declara o que a pesquisa não encontrou, então é '
        'lacuna. Só o 2 está certo como inferência.'),
    'items.12.items.0.paragraph': (
        '<p>🏁 <strong>Ponto de controle:</strong> em '
        + bc('perplexity.ai > barra lateral > Projetos > Pesquisa citada — LGPD')
        + ', a pesquisa da síntese aparece dentro do Projeto.</p>'),
    'items.14.items.0.heading': 'Quer ir além? (opcional)',
    'items.14.items.0.paragraph': ('<p>Três desafios para treinar mais a Oficina 4. Cada um diz como saber se deu '
                                   'certo:</p>'),
    'items.15.items.0.title': 'Pergunte só sobre algumas páginas de um PDF',
    'items.15.items.0.description': (
        '<p>Envie um PDF oficial (por exemplo, um guia da ANPD) e pergunte só sobre as páginas 2 a 5, pedindo '
        '"indique a página de cada conclusão".</p>' + SEP +
        '<p><strong>Validação:</strong> você confere duas páginas indicadas.</p>'),
    'items.15.items.1.title': 'Peça a síntese em tabela',
    'items.15.items.1.description': (
        '<p>Peça uma versão da síntese em tabela "afirmação | fonte | data | trecho".</p>' + SEP +
        '<p><strong>Validação:</strong> todas as linhas têm trecho que você localizou no original.</p>'),
    'items.15.items.2.title': 'Leve a pesquisa da Oficina 1 para o Projeto',
    'items.15.items.2.description': (
        '<p>Encontre a pesquisa da Oficina 1 em ' + bc('perplexity.ai > barra lateral > Recentes')
        + ' e mova-a para o Projeto [conferir se é possível].</p>' + SEP +
        '<p><strong>Validação:</strong> o Projeto passa a listar duas pesquisas.</p>'),
    'items.16.items.0.heading': 'A Parte dos Dez: hábitos de quem pesquisa com fonte verificável',
    'items.16.items.0.paragraph': '<p>Vire cada cartão para rever os dez hábitos que você leva do curso:</p>',
}
_DEZ = [
    ('Escreva a pergunta inteira.', 'Instrução, contexto, recorte, fontes aceitas e formato. Pergunta vaga, '
                                    'resposta vaga.'),
    ('Peça sempre a seção "o que não foi possível confirmar".', 'Lacuna declarada vale mais que lacuna escondida.'),
    ('Tranque as fontes na própria pergunta.', 'Escreva "use apenas…" — e conte quem obedeceu.'),
    ('Guarde a Pesquisa Pro para a pergunta difícil.', 'No gratuito são três por dia.'),
    ('Mudou de assunto? Pesquisa nova.', 'O contexto herdado contamina a resposta.'),
    ('Ctrl+F na página citada.', 'Se o termo não está lá, a citação não sustenta a frase.'),
    ('Número de processo, DOI ou lei: confirme na base oficial.', 'A IA dá a pista; o portal dá a prova.'),
    ('Prefira o documento ao que falam dele.', 'Fonte primária primeiro; notícia só para contexto.'),
    ('Antes de digitar, passe no semáforo.', 'Nome de cliente, paciente ou aluno não entra.'),
    ('Link público é publicação.', 'Revise tudo e teste numa janela anônima antes de mandar.'),
]
for i, (frente, verso) in enumerate(_DEZ):
    L03[f'items.17.items.{i}.front.description'] = f'<p><strong>{frente}</strong></p>'
    L03[f'items.17.items.{i}.back.description'] = f'<p>{verso}</p>'
L03['items.18.items.0.paragraph'] = (
    '<p>Você saiu de "a IA disse" para "eu conferi". Agora você formula perguntas que a ferramenta consegue '
    'pesquisar, escolhe quando vale a Pesquisa Pro, tranca as fontes, prova que uma referência existe e entrega uma '
    'síntese que aguenta ser questionada. Isso vale para qualquer motor de respostas — não só para a '
    'Perplexity.</p><p>Para continuar, o próximo curso da trilha é o NotebookLM - Essentials: lá você leva as fontes '
    'oficiais que encontrou aqui (a LGPD, a ANPD) para dentro de um caderno e estuda a fundo. Quer relatórios '
    'longos? Deep Research - Hands On. Quer checar citações em escala? Checagem de Fontes e Citações - '
    'Essentials.</p>')

if __name__ == '__main__':
    SAIDA.mkdir(exist_ok=True)
    for nome, mapa in (('L01', L01), ('L02', L02), ('L03', L03)):
        destino = SAIDA / f'{nome}.json'
        if destino.exists():
            raise SystemExit(f'{destino} ja existe; apague de proposito antes de regerar')
        destino.write_text(json.dumps(mapa, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'{destino.name}: {len(mapa)} entradas')
