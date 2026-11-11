"""Gera os mapas de revisao de texto (revisao_textos/LNN.json) do Deep Search Hands On.

Cada mapa e' {caminho relativo a `lesson`: texto novo}. Aplicados por aplicar_mapas.py.
Fonte: Pesquisa Conteudo Onda 2/Ementa Completa/deep-research-hands-on/roteiros/roteiro-articulate-hands-on.md
Mapeamento: L01 = preparacao + Oficina 1; L02 = Oficina 2; L03 = Oficina 3 + Projeto Final
(a Oficina 4 e A Parte dos Dez nao foram geradas pelo Articulate).
"""
import json
import pathlib

AQUI = pathlib.Path(__file__).resolve().parent
OBJ = '<p>Ao final desta lição, você será capaz de:</p>'

M = {}

# ---------------------------------------------------------------- L01 / Preparação + Oficina 1
M[1] = {
    'items.0.items.0.heading': 'Antes de clicar: um brief que o agente não entenda errado',
    'items.0.items.0.paragraph': '<p>Seu chefe (ou orientador, ou editor) pediu "uma pesquisa sobre envelhecimento no Brasil". Se você colar isso no agente, ele decide sozinho o período, o corte de idade e as fontes — e você gasta uma pesquisa para receber um relatório genérico. Nesta lição você prepara o ambiente e aprende a escrever o pedido certo, sem gastar nenhuma pesquisa.</p>',
    'items.1.items.0.paragraph': OBJ,
    'items.2.items.0.paragraph': '<p>Decidir se um pedido é caso de busca rápida ou de pesquisa profunda.</p>',
    'items.2.items.1.paragraph': '<p>Reescrever um pedido vago como brief de seis linhas.</p>',
    'items.2.items.2.paragraph': '<p>Nomear a fonte obrigatória: quem produziu o dado.</p>',
    'items.2.items.3.paragraph': '<p>Desligar o uso dos seus dados para treino em cada ferramenta.</p>',
    'items.2.items.4.paragraph': '<p>Separar o que pode, o que só pode com aprovação e o que nunca vai para a IA.</p>',
    'items.3.items.0.heading': 'Primeiro passo: é caso de pesquisa profunda?',
    'items.3.items.0.paragraph': '<p>Nem todo pedido merece uma pesquisa profunda — e, no plano gratuito, cada uma conta. Vire os cartões:</p>',
    'items.4.items.0.front.description': '<strong>Busca rápida (B)</strong>',
    'items.4.items.0.back.description': '<p>Fato pontual, como "Qual é a taxa Selic hoje?" ou "Qual o prazo para comunicar incidente na Resolução CD/ANPD 15/2024?". Até esses se conferem na fonte oficial.</p>',
    'items.4.items.1.front.description': '<strong>Pesquisa profunda (P)</strong>',
    'items.4.items.1.back.description': '<p>Síntese de várias fontes, como "Panorama de como a população de 60+ e 65+ mudou de 2010 a 2022, com dados oficiais" ou "Compare lei, regulamento e orientações da ANPD sobre comunicação de incidente".</p>',
    'items.4.items.2.back.description': '<p>Pergunte: é um dado só, ou uma síntese de várias fontes, cortes e períodos? Um dado só, busca rápida. Síntese, pesquisa profunda.</p>',
    'items.6.items.0.description': '<p>Parte guiada, sem gastar cota. Você vai pegar o pedido vago "pesquise envelhecimento no Brasil" e transformá-lo num brief que qualquer agente executa do jeito certo.</p>',
    'items.6.items.1.title': 'Deu certo?',
    'items.6.items.1.description': '<p>Classificação: B, P, B, P (e até os B se conferem na fonte oficial). Seu brief tem as seis linhas, nomeia a fonte obrigatória, pede número com fonte e data e não tem nenhum dado pessoal.</p><p>🏁 Na aba Registro, a coluna Brief tem as seis linhas e a linha extra.</p>',
    'items.6.items.2.description': '<p>Marque B (busca rápida) ou P (pesquisa profunda): "Qual é a taxa Selic hoje?"; "Panorama de como a população de 60+ e 65+ mudou de 2010 a 2022, com dados oficiais"; "Qual o prazo para comunicar incidente na Resolução CD/ANPD 15/2024?"; "Compare lei, regulamento e orientações da ANPD sobre comunicação de incidente".</p>',
    'items.6.items.3.description': '<p>Reescreva "pesquise envelhecimento no Brasil" com as seis linhas:</p><p>Pergunta: como mudou a população brasileira de 60+ e de 65+ entre 2010 e 2022?<br>Decisão apoiada: [pauta | relatório técnico | aula]<br>Recorte: Brasil, 2010–2022, com diferenças regionais quando houver.<br>Fontes obrigatórias: IBGE (Censo 2022 e IBGE Educa). Outras só para contexto.<br>Formato: resumo; tabela afirmação–número–fonte–data; evidências contrárias; lacunas.<br>Conclusão: todo número com fonte primária e data; não misturar 60+ com 65+.</p>',
    'items.6.items.4.description': '<p>Acrescente a linha que vale para qualquer brief: "Atue como assistente de pesquisa, não como autoridade final. Separe fatos, inferências e lacunas. Não preencha lacunas com suposições. Antes de começar, faça até cinco perguntas e proponha um plano editável."</p>',
    'items.6.items.5.description': '<p>Confira: tem dado pessoal ou segredo? Se tiver, tire.</p>',
    'items.6.items.6.description': '<p>Sua vez: escolha agora o dossiê do seu Projeto Final — A (Selic), B (Renda) ou C (Licitações) — e escreva o brief dele com as seis linhas. Guarde na aba Registro.</p>',
    'items.8.items.0.title': 'Qual destes pedidos está pronto para ir ao agente de pesquisa profunda sobre a população idosa no Brasil?',
    'items.8.items.0.answers.1.feedback': 'Correto. Pergunta específica, fonte obrigatória nomeada e formato definido: o agente não precisa adivinhar nada.',
    'items.9.items.0.paragraph': '<p>Três travas comuns ao escrever o brief, e como sair delas:</p>',
    'items.10.items.0.description': '<p>Pergunte: quem vai ler e o que vai fazer com isso?</p>',
    'items.10.items.1.description': '<p>Seis linhas bastam; o detalhe vai na linha de formato.</p>',
    'items.10.items.2.description': '<p>É quem produziu o dado: IBGE, Banco Central, Ipea, Planalto.</p>',
    'items.11.items.0.heading': 'Monte a planilha de auditoria',
    'items.11.items.0.paragraph': '<p>Enquanto o agente pesquisa (pode levar vários minutos), você trabalha na planilha. Crie agora as duas abas.</p><p><strong>Aba Auditoria</strong> — uma linha por afirmação:</p><ul><li>Nº</li><li>Afirmação</li><li>Fonte citada</li><li>Trecho da fonte</li><li>Suporte (integral / parcial / ausente / inacessível)</li><li>Primária ou secundária?</li><li>Data da fonte</li><li>Decisão (manter / corrigir / remover)</li></ul><p><strong>Aba Registro</strong> — uma linha por execução:</p><ul><li>Ferramenta</li><li>Modo</li><li>Data e hora</li><li>Brief</li><li>Plano e edições</li><li>Configuração de dados</li></ul>',
    'items.12.items.0.heading': 'Desligue o treino antes de começar',
    'items.12.items.0.paragraph': '<p>Por padrão, as ferramentas podem usar o que você envia para treinar modelos. Ajuste antes da primeira pesquisa:</p>',
    'items.13.items.0.description': '<p><strong>Padrão:</strong> no ChatGPT pessoal, conversas podem treinar modelos.</p><p></p><p><strong>O que fazer:</strong> <strong>Profile &gt; Settings &gt; Data Controls &gt; Improve the model for everyone</strong> — desligue.</p>',
    'items.13.items.1.description': '<p><strong>Padrão:</strong> com Keep Activity ligado, prompts e uploads podem treinar, com revisão humana; a atividade fica guardada 18 meses.</p><p></p><p><strong>O que fazer:</strong> use Temporary chat ou desligue Keep Activity. Os chats ainda ficam guardados 72 horas.</p>',
    'items.13.items.2.description': '<p><strong>Padrão:</strong> o opt-out de treino está documentado nos planos Pro, Education Pro e Max.</p><p></p><p><strong>O que fazer:</strong> no gratuito, confira em <strong>Perplexity &gt; Settings</strong> [conferir].</p>',
    'items.15.items.0.heading': 'Semáforo: o que pode ir para a IA',
    'items.15.items.0.paragraph': '<p>Arraste cada exemplo para a cor certa: verde (pode usar), amarelo (só a pasta mínima, com aprovação) ou vermelho (não envie).</p>',
    'items.18.items.0.paragraph': '<p>Brief pronto e ambiente configurado. Na próxima lição você gasta a primeira pesquisa: roda o brief, corrige o plano do agente e guarda a trilha para alguém refazer.</p>',
}

# ---------------------------------------------------------------- L02 / Oficina 2
M[2] = {
    'items.0.items.0.heading': 'Rode, dirija o plano e guarde a trilha',
    'items.0.items.0.paragraph': '<p>O agente vai propor um plano. Se você só clicar "começar", ele faz do jeito dele. Nesta lição você lê o plano, corrige o rumo, deixa o agente trabalhar e guarda tudo o que alguém precisaria para refazer a pesquisa. Vai usar <strong>1 pesquisa</strong> — de preferência no Gemini (limite diário) ou no ChatGPT — e o brief do caso-guia da lição anterior.</p>',
    'items.1.items.0.paragraph': OBJ,
    'items.2.items.0.paragraph': '<p>Rodar o brief no Deep Research da ferramenta escolhida.</p>',
    'items.2.items.1.paragraph': '<p>Ler o plano do agente e corrigir o rumo antes de começar.</p>',
    'items.2.items.2.paragraph': '<p>Registrar ferramenta, modo, data, hora, plano e edições na aba Registro.</p>',
    'items.2.items.3.paragraph': '<p>Exportar o relatório com a data no nome e pedir um refinamento sem gastar nova pesquisa.</p>',
    'items.3.items.0.heading': 'Onde fica o Deep Research em cada ferramenta',
    'items.3.items.0.paragraph': '<p>Caminhos e limites do plano gratuito. Rótulos marcados com [conferir] podem ter mudado na interface:</p>',
    'items.4.items.0.description': '<p>Caminho: <strong>caixa de mensagem &gt; + &gt; Deep research</strong>, ou digite <strong>/Deepresearch</strong>. No gratuito, o acesso é limitado e o saldo aparece no próprio produto [conferir onde].</p><p></p><p>Você responde às perguntas de esclarecimento e revisa o plano proposto antes de confirmar. Exporta em Markdown, Word e PDF.</p>',
    'items.4.items.1.description': '<p>Caminho: <strong>gemini.google.com &gt; ferramentas &gt; Deep Research</strong> [conferir rótulo]. Limite diário variável; exige 18 anos ou mais.</p><p></p><p>Mostra o plano antes de começar e deixa editá-lo em <strong>Edit plan</strong>. Exporta direto para o Docs em <strong>Open report &gt; Export &gt; Export to Docs</strong>.</p>',
    'items.4.items.2.description': '<p>Caminho: <strong>barra de pergunta &gt; + &gt; Deep research</strong>. No gratuito, <strong>1 pesquisa por mês</strong> — guarde para quando o brief estiver pronto.</p><p></p><p>Não clique em "Create files and apps": é outro modo, com outra cota. A Perplexity não tem etapa de aprovação do plano, então todo o controle fica no brief.</p>',
    'items.5.items.0.paragraph': '<p>🤓 O Gemini deixa desmarcar o Google Search (<strong>Deep Research &gt; Sources</strong>) e pesquisar só nos arquivos que você escolher. É o jeito de separar "o que meus documentos dizem" de "o que a web diz".</p>',
    'items.6.items.0.description': '<p>Parte guiada: uma pesquisa, do brief colado ao relatório exportado. Use a espera do agente para adiantar a planilha.</p>',
    'items.6.items.1.title': 'Deu certo?',
    'items.6.items.1.description': '<p>Você tem: o relatório exportado com data no nome; a aba Registro com ferramenta, modo, data, hora, plano e edição; e a tabela de afirmações com fonte. Na rota sem cota: o Registro tem o prompt e o plano tirados do relatório do MIT.</p>',
    'items.6.items.2.description': '<p>Abra o Deep Research da ferramenta escolhida e cole o brief do caso-guia da lição anterior.</p>',
    'items.6.items.3.description': '<p><strong>No Gemini:</strong> leia o plano. Se não houver um passo "separar 60+ e 65+" ou "usar o Censo 2022 do IBGE", vá a <strong>Deep Research &gt; plano &gt; Edit plan</strong> e acrescente. <strong>No ChatGPT:</strong> responda às perguntas de esclarecimento e revise o plano proposto.</p>',
    'items.6.items.4.title': 'Confirmar e registrar',
    'items.6.items.4.description': '<p>No Gemini, clique em <strong>Start research</strong>; no ChatGPT, confirme. Anote na aba Registro: ferramenta, modo (Thinking ou Pro, no Gemini), data, hora, plano e o que você editou.</p><p>🏁 No Gemini, <strong>Deep Research &gt; plano</strong> mostra o passo que você acrescentou antes de Start research.</p>',
    'items.6.items.5.description': '<p>Enquanto o agente trabalha, numere de 1 a 5 as linhas da aba Auditoria.</p>',
    'items.6.items.6.description': '<p>Com o relatório pronto, abra-o inteiro. No ChatGPT, veja <strong>relatório &gt; Sources used</strong> e o histórico de atividade (activity history).</p>',
    'items.6.items.7.description': '<p>Exporte: Gemini <strong>Open report &gt; Export &gt; Export to Docs</strong>; ChatGPT <strong>relatório &gt; Download/Export &gt; Word, PDF ou Markdown</strong> [conferir rótulo]. Guarde o arquivo com a data no nome.</p>',
    'items.6.items.8.description': '<p>Sua vez, sem gastar nova pesquisa. No mesmo chat, cole: "Transforme os achados numa tabela com quatro colunas: afirmação, número, fonte primária com link, data da fonte. Marque \'sem fonte primária\' quando for o caso." Depois, anote no Registro que houve refinamento.</p>',
    'items.8.items.0.heading': 'O que vai para a aba Registro',
    'items.8.items.0.paragraph': '<p>A aba Registro é o que permite a outra pessoa — ou a você, daqui a um mês — refazer a pesquisa. Para cada execução, anote:</p><ul><li>Ferramenta e modo (Thinking ou Pro, no Gemini)</li><li>Data e hora</li><li>Brief</li><li>Plano e as edições que você fez</li><li>Configuração de dados</li><li>Refinamentos pedidos depois do relatório</li></ul><p>O mesmo brief pode gerar números diferentes em outra data. Sem registro, não há como explicar a diferença.</p>',
    'items.10.items.0.paragraph': '<p>Três situações comuns na primeira execução:</p>',
    'items.11.items.0.description': '<p>No Gemini, o plano aparece antes do início [conferir rótulo]. No ChatGPT, edite respondendo às perguntas ou pedindo ajuste. Na Perplexity não há aprovação de plano: o controle fica todo no brief.</p>',
    'items.11.items.1.description': '<p>Normal: a pesquisa profunda pode levar vários minutos. Deixe o agente trabalhar e prepare a planilha.</p>',
    'items.11.items.2.description': '<p>Reduza o escopo, exija fonte primária e "Brasil, pt-BR" e rode em outra data.</p>',
    'items.12.items.0.paragraph': '<p>⚠️ O ChatGPT exporta em Markdown, Word e PDF; Google Docs não é formato direto (abra o Word no Drive). Só o Gemini exporta direto para o Docs.</p>',
    'items.13.items.0.heading': 'Antes de seguir: confira a trilha',
    'items.13.items.0.paragraph': '<p>Três pontos que costumam faltar no registro. Vire os cartões:</p>',
    'items.14.items.1.back.description': '<p>Que houve refinamento, o que foi pedido e quando. O refinamento muda o relatório; sem a anotação, a trilha fica incompleta.</p>',
    'items.16.items.0.paragraph': '<p>Relatório na mão e trilha guardada. Na próxima lição você confere o relatório afirmação por afirmação na fonte primária e entrega o seu dossiê auditado.</p>',
}

# ---------------------------------------------------------------- L03 / Oficina 3 + Projeto Final
M[3] = {
    'items.0.items.0.heading': 'Link não é prova: audite e entregue',
    'items.0.items.0.paragraph': '<p>O relatório está lindo, cheio de números e de links. Só que link não é prova: a fonte pode existir e não dizer aquilo. Nesta lição você pega as cinco afirmações que mais importam, confere uma por uma no IBGE e depois repete o processo no dossiê que escolheu, até entregar a versão corrigida. O relatório da IA é a matéria-prima; o produto é seu.</p>',
    'items.1.items.0.paragraph': OBJ,
    'items.2.items.0.paragraph': '<p>Escolher as cinco afirmações centrais de um relatório.</p>',
    'items.2.items.1.paragraph': '<p>Conferir cada uma na fonte primária, com o trecho copiado.</p>',
    'items.2.items.2.paragraph': '<p>Classificar o suporte como integral, parcial, ausente ou inacessível.</p>',
    'items.2.items.3.paragraph': '<p>Decidir manter, corrigir ou remover — e entregar a versão corrigida em fatos, inferências e lacunas.</p>',
    'items.3.items.0.paragraph': '<p>Três ideias que você vai usar em cada linha da aba Auditoria. Vire os cartões:</p>',
    'items.4.items.2.back.description': '<p><strong>Integral</strong> (a fonte diz isso), <strong>parcial</strong> (diz só uma parte, ou mistura cortes), <strong>ausente</strong> (não diz) ou <strong>inacessível</strong> (paywall, link quebrado).</p>',
    'items.5.items.0.description': '<p>Parte guiada, sem cota. Use o relatório da lição anterior (ou o do MIT), a página IBGE Educa "Pirâmide etária", o PDF "Censo 2022 — Pessoas de 60 anos ou mais" e a aba Auditoria.</p>',
    'items.5.items.1.title': 'Deu certo?',
    'items.5.items.1.description': '<p>Sua aba Auditoria tem cinco linhas com trecho, tipo de fonte, suporte e decisão.</p><p>🏁 Ponto de controle: nenhuma linha está sem Suporte ou sem Decisão.</p>',
    'items.5.items.2.description': '<p>Escolha as cinco afirmações centrais — de preferência as que têm número — e cole na aba Auditoria.</p>',
    'items.5.items.3.description': '<p>Clique na citação de cada uma. Anote a fonte citada.</p>',
    'items.5.items.4.description': '<p>No original, procure o número ou a frase com <strong>navegador &gt; Localizar (Ctrl+F; no Mac, Cmd+F)</strong>.</p>',
    'items.5.items.6.description': '<p>Classifique: <strong>integral</strong>, <strong>parcial</strong>, <strong>ausente</strong> ou <strong>inacessível</strong> (paywall, link quebrado).</p>',
    'items.5.items.7.description': '<p>A fonte é primária (IBGE) ou secundária (notícia, blog)? Se secundária, procure o dado em <strong>educa.ibge.gov.br &gt; Jovens &gt; Conheça o Brasil &gt; População &gt; Pirâmide etária</strong> ou no PDF do Censo.</p>',
    # (revertido: validar_estrutura trata como nao textual) 'items.7.items.0.feedbackCorrect': 'Correto. A parcela passou de 7,4% para 10,9% (e de 14 para 22,2 milhões): cresceu, mas não dobrou. A fonte não sustenta a frase.',
    # (revertido: validar_estrutura trata como nao textual) 'items.7.items.0.feedbackIncorrect': 'Não. O IBGE mostra 7,4% em 2010 e 10,9% em 2022 — aumento, mas não o dobro. A fonte existe e está acessível; só não diz o que a frase afirma: suporte ausente.',
    'items.8.items.0.paragraph': '<p>Três tropeços comuns na conferência:</p>',
    'items.9.items.1.description': '<p>Confira o corte (60+ ou 65+), o ano e se o valor é percentual ou absoluto.</p>',
    'items.9.items.2.description': '<p>Notícia é fonte secundária. Rastreie até o IBGE (o T de Trace, do SIFT) e registre a fonte primária.</p>',
    'items.11.items.0.heading': 'Projeto Final: o seu dossiê',
    'items.11.items.0.paragraph': '<p>Agora é o dossiê que você escolheu na primeira lição (A — Selic, B — Renda, C — Licitações). Rode o brief dele na ferramenta que ainda tem saldo — ou use a busca comum, anotando que não foi pesquisa profunda — e registre ferramenta, data, hora e plano. Depois, audite as cinco afirmações centrais na fonte primária: Banco Central, Ipea ou Planalto.</p>',
    'items.12.items.0.description': '<p>Do brief do seu dossiê à versão corrigida. Antes de rodar, confira o semáforo e a configuração de dados.</p>',
    'items.12.items.1.title': 'Como saber que terminou',
    'items.12.items.1.description': '<p>Cada frase da seção "Fatos verificados" remete a uma linha da aba Auditoria, e nenhuma conclusão se apoia só no relatório da IA.</p>',
    'items.13.items.0.paragraph': '<p>Treine a separação antes de escrever a sua versão. Arraste cada frase para Fatos verificados, Inferências ou Lacunas:</p>',
    'items.16.items.0.paragraph': '<p>Você pediu direito, dirigiu o plano, pegou um número misturado e entregou um relatório que aguenta a pergunta "de onde veio isso?". Próximos passos: na trilha de Pesquisa com IA, <em>Checagem de Fontes e Citações - Essentials</em> afia a conferência de citações científicas e jurídicas, e <em>Revisão Bibliográfica com IA - Hands On</em> leva o rigor para conjuntos inteiros de artigos.</p>',
}

if __name__ == '__main__':
    destino = AQUI / 'revisao_textos'
    destino.mkdir(exist_ok=True)
    for n, mapa in M.items():
        (destino / f'L{n:02d}.json').write_text(json.dumps(mapa, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'L{n:02d}: {len(mapa)} campos')
    print('TOTAL', sum(len(m) for m in M.values()))
