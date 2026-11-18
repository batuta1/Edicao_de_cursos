# Plano de Aula — Deep Research (Essentials)

> *» IA: Bloco Cover — título verbatim. Subtítulo: "Pesquisa profunda com agentes de IA, do brief ao relatório auditado". Não traduzir "deep research", "ChatGPT", "Gemini" nem "Perplexity".*

## Identificação

> *» IA: Bloco Table — tabela verbatim.*

| Campo | Definição |
|---|---|
| Curso | Deep Research (Essentials) |
| Natureza | Autoinstrucional, introdutório e prático |
| Carga horária | 120 minutos (sem contar a espera do agente durante a execução) |
| Público-alvo | Estudantes, pesquisadores, jornalistas e analistas; advogados, assessores, estudantes e professores de Direito |
| Pré-requisitos | *Perplexity - Essentials* ou *NotebookLM - Essentials*; nenhum conhecimento prévio de método de pesquisa |
| Recursos necessários | Computador com navegador e internet; conta gratuita em pelo menos uma entre ChatGPT, Gemini e Perplexity com saldo de pesquisa profunda (há rota sem saldo); planilha eletrônica. Nenhuma atividade exige plano pago: no gratuito, a Perplexity oferece 1 pesquisa por mês, o ChatGPT acesso limitado e o Gemini limite diário variável. |

### Objetivo Geral

> *» IA: Bloco Text — verbatim.*

O curso tem por finalidade capacitar o participante a conduzir pesquisas profundas com agentes de inteligência artificial — ChatGPT deep research, Gemini Deep Research e Perplexity Deep Research — e a auditar o relatório resultante quanto a fontes, lacunas e erros, tratando-o como rascunho pesquisado e não como autoridade final. Como produto final, o participante entrega um dossiê com brief, plano, relatório, planilha de auditoria das afirmações centrais, versão corrigida e lista de lacunas.

### Competências a Desenvolver

> *» IA: Bloco List — numerada, verbatim, sem acréscimos.*

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Distinguir pesquisa profunda de busca rápida e de conversa com chatbot, e decidir quando utilizá-la.
2. Configurar cada ferramenta quanto a treinamento, retenção e conectores antes de enviar qualquer material.
3. Redigir brief de seis componentes e dirigir o plano e as fontes do agente.
4. Auditar as afirmações de um relatório contra a fonte primária e identificar lacunas.
5. Escolher a ferramenta conforme a tarefa e ler benchmarks considerando autoria e conflito de interesse.

### Estrutura e Sequência dos Módulos

> *» IA: Bloco Text — verbatim.*

Os módulos são cumulativos: cada um pressupõe o anterior. Um caso-guia — "Como mudou a população brasileira de 60+ e 65+ entre 2010 e 2022?", com gabarito no Censo 2022 do IBGE — é briefado no Módulo 3, auditado no Módulo 4 e consolidado no Módulo 6. Para o público jurídico, um caso paralelo sobre comunicação de incidente de segurança sob a LGPD e a Resolução CD/ANPD 15/2024 acompanha os mesmos módulos.

> *» IA: Bloco Table — verbatim.*

| Módulo | Título | Referência | Tempo |
|---|---|---|---|
| 0 | Preparação e Verificação Inicial | Ajudas e páginas de planos de OpenAI, Google e Perplexity | 7 min |
| 1 | O que é deep research | Lançamentos e ajudas oficiais; System Card | 19 min |
| 2 | Segurança, dados e sigilo | Políticas de dados das três fabricantes; LGPD | 18 min |
| 3 | Brief e plano de pesquisa | Ajudas do ChatGPT e do Gemini; vídeo da Perplexity | 22 min |
| 4 | Auditoria do relatório | Guias CMU, JHU, Illinois, Penn State; IBGE; Resolução CD/ANPD 15/2024 | 20 min |
| 5 | Escolher a ferramenta e ler benchmarks | BrowseComp; DRACO; DeepResearch Bench; Axios | 18 min |
| 6 | Síntese e Aplicação Integrada | — | 16 min |

---

# Módulo 0 — Preparação e Verificação Inicial

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 0" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Ponto de partida: verifica contas, saldo e a planilha de auditoria antes de qualquer pesquisa.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Localizar o recurso de pesquisa profunda e o respectivo saldo em ao menos uma ferramenta.
2. Escolher entre a rota com execução própria e a rota sem cota.
3. Preparar a planilha de auditoria utilizada no curso.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir.*

As três ferramentas oferecem pesquisa profunda em plano gratuito, mas com limites distintos e, em dois casos, não publicados. A Perplexity informa uma pesquisa (Research Query) por mês no plano gratuito. O ChatGPT descreve acesso "limitado" no gratuito e manda consultar o saldo no próprio produto; os números divulgados em 2025 (cinco por mês no gratuito) são históricos e não devem ser tomados como atuais. O Gemini oferece o recurso a usuários sem plano, com limites diários variáveis e possibilidade de indisponibilidade em alta demanda. Recomenda-se, por isso, verificar o saldo antes de iniciar e reservar a execução para o Módulo 3.

> *» IA: Bloco Table — verbatim; preservar os breadcrumbs; não traduzir termos de interface.*

| Ferramenta | Onde fica o recurso | Onde ver o saldo |
|---|---|---|
| ChatGPT | `ChatGPT > caixa de mensagem > + > Deep research` (ou comando `/Deepresearch`; pt-BR pode exibir "Pesquisa aprofundada") | Contador junto de Deep research ou `ChatGPT > Settings > Usage` [conferir] |
| Gemini | `gemini.google.com > caixa de texto > Add Files > Deep Research` [conferir rótulo] | `Gemini > Settings > Usage Limits` [conferir] |
| Perplexity | `Perplexity > barra de pergunta > + > Deep research` | Página de conta ou plano [conferir]; gratuito: 1 por mês |

> *» IA: Bloco Text — verbatim.*

Caso nenhuma ferramenta disponha de saldo no dia, o curso oferece uma rota sem cota: a auditoria de um relatório real de deep research publicado pelo MIT Sloan EdTech, que inclui a conversa completa e a saída produzida. O método de auditoria é idêntico nas duas rotas.

A planilha de auditoria é o instrumento central do curso. Recomenda-se criá-la com as colunas: Nº · Afirmação (copiada do relatório) · Fonte citada · Trecho da fonte · Suporte (integral, parcial, ausente, fonte inacessível) · Tipo de fonte (primária, secundária) · Data da fonte · Decisão (manter, corrigir, remover) · Observação. Uma segunda aba, "Registro", guarda o brief, o plano, a ferramenta, o modo, a data e o horário de cada execução.

> *» IA: Bloco Statement — aviso verbatim; preservar o emoji e o breadcrumb.*

> ⚠️ Na Perplexity, `+ > Create files and apps` (antigo Labs) é outro modo, com outra cota. O curso usa apenas `+ > Deep research`.

### Exercício Prático

> *» IA: Bloco Process — um passo por etapa, verbatim.*

**Verificação inicial (7 min)**

1. Entrar em ao menos uma ferramenta e localizar o recurso de pesquisa profunda, sem executá-lo.
2. Anotar o saldo exibido ou registrar "saldo não exibido".
3. Criar a planilha com as abas Auditoria e Registro.
4. Decidir a rota: execução própria ou relatório do MIT (`mit-case-study-deep-research.pdf`).

> *» IA: Bloco Statement — verbatim; preservar o emoji.*

> 🏁 Ponto de controle: o menu da ferramenta escolhida exibe a opção Deep research, e a aba Registro informa ferramenta, saldo observado, data e rota escolhida.

**Critério de êxito:** a aba Registro está preenchida com os quatro campos.

### Mão na massa

> *» IA: Bloco Statement — modelo editável verbatim; preservar as aspas triplas.*

Cabeçalho-base para a aba Registro, a ser adaptado:

"""
Pesquisa: [pergunta]
Ferramenta: [ChatGPT | Gemini | Perplexity | rota sem cota — relatório MIT]
Modo: [ex.: Thinking | Pro | padrão] · Saldo observado: [valor ou "não exibido"]
Data e hora: [ ] · Configuração de dados: [a preencher no Módulo 2]
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 0" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 1 — O que é deep research

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe o ambiente do Módulo 0; introduz os conceitos que os módulos seguintes aplicam.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Definir pesquisa profunda como tarefa de agente em várias etapas.
2. Distinguir pesquisa profunda de busca rápida e de conversa comum com chatbot.
3. Explicar os conceitos de plano, grounding, citação inline e fonte primária.
4. Decidir quando um pedido justifica pesquisa profunda.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; pode dividir por parágrafo; não resumir.*

Pesquisa profunda (deep research) é uma modalidade de pesquisa conduzida por um **agente** — sistema que planeja e executa etapas com ferramentas, em vez de produzir uma única resposta imediata. O agente recebe uma tarefa ampla, propõe ou executa um **plano** de várias etapas (uma lista de subperguntas e ações), faz buscas sucessivas, lê muitas fontes, muda de rota quando encontra nova evidência e entrega um relatório documentado. Equivale a um assistente de pesquisa que recebe um brief e volta com relatório e fichas, mas que precisa de supervisão.

A distinção em relação às outras formas de uso é prática. A busca comum devolve uma resposta curta e rápida, adequada a um fato pontual. A conversa com chatbot sem pesquisa responde principalmente a partir do próprio modelo e não produz, necessariamente, trilha verificável. A pesquisa profunda destina-se a sínteses de várias etapas, com muitas fontes, e consome mais tempo e mais cota: no lançamento, a OpenAI informava de 5 a 30 minutos por pesquisa; a ajuda atual evita prometer tempo.

Dois conceitos sustentam a auditoria ensinada adiante. **Grounding** (ancoragem) é a vinculação da resposta a fontes recuperadas; não significa que a inferência esteja correta. A **citação inline** é o marcador junto à afirmação que abre a fonte; sua presença não prova que a fonte sustente a frase. Distingue-se ainda a **fonte primária** — o documento ou dado original, como lei, decisão, base de dados ou relatório do órgão responsável — da **fonte secundária**, que interpreta a primária.

O recurso estreou no Gemini em 11/12/2024, no ChatGPT em 02/02/2025 e na Perplexity em 14/02/2025. Desde então, nomes, modelos e cotas mudaram: o ChatGPT usou inicialmente uma versão do o3 e hoje declara "latest models"; o Gemini oferece Thinking a todos e Pro a assinantes; a Perplexity alternou os nomes "Research" e "Deep Research". Cumpre, portanto, compreender o recurso pela função, não pelo modelo do momento.

> *» IA: Bloco Statement — verbatim; preservar o emoji e os breadcrumbs.*

> 🏁 Ponto de controle: em um relatório concluído, `relatório > tela cheia` exibe o sumário, as citações inline junto às afirmações e, no ChatGPT, a seção Sources used ao final.

### Exercício Prático

> *» IA: Bloco Knowledge Check — quatro itens de escolha entre "Busca rápida" e "Pesquisa profunda"; enunciados e feedback verbatim.*

**Questão de classificação (4 min)** — indicar, para cada pedido, busca rápida (B) ou pesquisa profunda (P):

1. Qual é a taxa Selic vigente hoje?
2. Panorama de como a população brasileira de 60+ e 65+ mudou entre 2010 e 2022, com dados oficiais e diferenças regionais.
3. Qual o prazo da Resolução CD/ANPD 15/2024 para comunicar incidente?
4. Comparação das obrigações de comunicação de incidente na LGPD, na Resolução 15/2024 e nas orientações da ANPD, distinguindo lei, regulamento e orientação.

> *» IA: Bloco Statement — gabarito verbatim.*

**Gabarito:** 1-B (fato pontual, verificado na fonte oficial); 2-P (síntese de várias fontes e cortes); 3-B (dispositivo único, conferido no texto da norma); 4-P (várias fontes e hierarquia normativa). Mesmo os itens B devem ser conferidos na fonte primária.

### Mão na massa

> *» IA: Bloco Statement — prompt editável verbatim; preservar as aspas triplas.*

Prompt-base para testar se um pedido justifica pesquisa profunda, a ser usado em busca comum (sem consumir cota):

"""
Vou fazer o seguinte pedido a um agente de pesquisa profunda: [pedido]. Antes, responda em três linhas: 1) isso é um fato pontual ou uma síntese de várias fontes? 2) qual seria a fonte primária? 3) que informação falta no meu pedido (período, recorte, formato)? Não faça a pesquisa.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 2 — Segurança, dados e sigilo

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe os conceitos do Módulo 1; antecede a primeira execução, para que a decisão sobre dados venha antes do uso.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Identificar como cada ferramenta trata conversas e arquivos para treinamento e retenção.
2. Localizar a configuração que limita o uso dos dados em cada ferramenta.
3. Reconhecer os riscos de conectores (Gmail, Drive) e de prompt injection.
4. Classificar materiais quanto à possibilidade de envio, à luz da LGPD e do sigilo profissional.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir; não traduzir termos de interface.*

As configurações padrão diferem entre as ferramentas e não são, em geral, as mais restritivas. No ChatGPT pessoal (Free, Plus e Pro), novas conversas podem ser usadas para melhorar os modelos por padrão. A pesquisa profunda segue as mesmas regras de retenção da conversa. Planos Business, Enterprise e Edu não usam os dados para treinamento por padrão.

No Gemini, com a atividade (Keep Activity) ligada, prompts, uploads e atividade podem ser usados para desenvolver e melhorar serviços, inclusive treinar IA, com revisão humana; a autoexclusão padrão é de 18 meses, e conteúdo revisado pode ser mantido por até três anos, desvinculado da conta. Com a atividade desligada ou em chat temporário, as conversas futuras não são usadas para treinamento, mas permanecem 72 horas para resposta e segurança — e alguns aplicativos conectados deixam de funcionar. Na Perplexity, os planos Pro, Education Pro e Max permitem desativar a coleta para treinamento; os planos Enterprise e a API declaram não usar os dados. A situação do plano gratuito não consta da documentação consultada [conferir].

Dois riscos são próprios dos agentes. O primeiro são os **conectores**: Gmail, Drive e outros aplicativos herdam as permissões do usuário e são usados apenas para leitura, mas ampliam a quantidade de dados expostos; recomenda-se criar uma pasta com o corpus mínimo, em vez de abrir a caixa de e-mail inteira. O segundo é o **prompt injection**: instrução maliciosa escondida numa página ou arquivo, que tenta desviar o agente ou extrair dados — risco descrito no System Card da OpenAI.

Para o público jurídico e para quem lida com dados de terceiros, a LGPD impõe finalidade, adequação, necessidade, segurança, prevenção, transparência e responsabilização; o envio a uma IA externa pode envolver operador, suboperador e transferência internacional, e a organização continua responsável pela base legal e pela minimização. Autos sigilosos, estratégia de cliente, credenciais e dados sensíveis não devem ir para conta pessoal; para esses casos, exige-se ambiente empresarial contratado e aprovado.

> *» IA: Bloco Table — verbatim; preservar os breadcrumbs; não traduzir termos de interface.*

| Ferramenta | Configuração | Caminho |
|---|---|---|
| ChatGPT pessoal | Desligar o uso para treinamento | `ChatGPT > Profile > Settings > Data Controls > Improve the model for everyone` |
| Gemini | Desligar a atividade ou usar chat temporário | `Gemini > Settings > Activity (Keep Activity)` ou `Gemini > Temporary chat` [conferir rótulos] |
| Gemini Deep Research | Limitar as fontes | `Deep Research > Sources > desmarcar Gmail e Drive` (ou desmarcar Google Search para usar só arquivos) |
| Perplexity | Desligar coleta para treinamento (Pro, Education Pro, Max) | `Perplexity > Settings` [conferir no plano gratuito] |

### Exercício Prático

> *» IA: Bloco Process — cinco cenários, um por etapa, verbatim.*

**Discussão orientada: cinco cenários (8 min)** — classificar em verde (pode), amarelo (só com ajuste ou autorização) ou vermelho (não), com justificativa:

1. Pesquisa sobre envelhecimento no Brasil usando apenas fontes públicas, em conta pessoal.
2. Ativar Gmail no Gemini Deep Research para "achar tudo sobre o cliente X".
3. Enviar a petição inicial de um processo sob segredo de justiça ao ChatGPT pessoal.
4. Enviar ao ChatGPT o PDF público da Resolução CD/ANPD 15/2024.
5. Usar o Drive da empresa como fonte no Gemini, sem aprovação do jurídico ou da segurança.

> *» IA: Bloco Statement — gabarito verbatim.*

**Gabarito:** 1 verde; 2 vermelho (caixa inteira, dados de terceiros; usar no máximo pasta mínima e com autorização); 3 vermelho (sigilo e dados sensíveis); 4 verde (norma pública); 5 amarelo a vermelho (depende de contrato, DPA e aprovação; sem aprovação, não).

**Exemplo aplicado (6 min):** aplicar, em cada ferramenta usada, a configuração da tabela acima e registrá-la na aba Registro.

> *» IA: Bloco Statement — verbatim; preservar o emoji e o breadcrumb.*

> 🏁 Ponto de controle: em `ChatGPT > Profile > Settings > Data Controls`, a chave "Improve the model for everyone" aparece desligada; no Gemini, o chat aberto indica modo temporário ou a atividade aparece desligada.

> *» IA: Bloco Knowledge Check — uma questão de múltipla escolha; enunciado, alternativas e feedback verbatim.*

**Avaliação (4 min):** desligar Keep Activity no Gemini significa que:
a) nenhum dado fica armazenado b) os chats futuros não treinam modelos, mas ficam 72 horas c) o Gmail continua funcionando normalmente d) os dados passam a ser apagados em 18 meses

**Gabarito:** b.

### Mão na massa

> *» IA: Bloco Statement — modelo editável verbatim; preservar as aspas triplas.*

Checklist-base antes de enviar qualquer arquivo ou conectar um aplicativo, a ser adaptado:

"""
Finalidade documentada: [ ]
O material é público? [sim | não] — se não: há base legal e autorização interna? [ ]
Mínimo necessário: [quais arquivos ou pasta, e não a caixa inteira]
Dados pessoais ou sigilosos removidos ou anonimizados de fato? [ ]
Conta: [pessoal | empresarial contratada] · Treinamento desligado? [ ]
Conectores ativos: [nenhum | quais] · Revisão de sigilo profissional feita? [ ]
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 3 — Brief e plano de pesquisa

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe as regras de dados do Módulo 2; desloca o foco para o que se decide antes e logo após clicar em pesquisar.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Redigir um brief com os seis componentes recomendados.
2. Revisar e editar o plano proposto pelo agente antes da execução.
3. Restringir ou priorizar fontes quando a ferramenta permitir.
4. Registrar brief, plano, ferramenta e horário para reprodutibilidade.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir; não traduzir termos de interface.*

As três fabricantes convergem num ponto: o pedido detalhado produz relatório melhor. A OpenAI recomenda explicitar pergunta, resultado desejado e restrições; a Perplexity afirma que "quanto mais detalhado, melhor"; o Gemini mostra um plano revisável antes da execução. O instrumento que traduz essa recomendação é o **brief**, redigido em seis linhas: pergunta; decisão que o relatório apoiará; recorte geográfico e temporal; fontes obrigatórias; fontes proibidas ou secundárias; formato de saída e critério de conclusão. Dados pessoais e segredos ficam de fora.

O pedido "pesquise envelhecimento no Brasil" ilustra o problema: não define corte etário, período, fonte nem formato, e o agente preencherá essas lacunas por conta própria. Reescrito, o brief do caso-guia passa a exigir os cortes 60+ e 65+, o período 2010–2022, o Censo do IBGE como fonte obrigatória, uma tabela com número, fonte e data para cada dado e a separação entre fatos, inferências e lacunas.

Após o envio, o ChatGPT pode fazer perguntas de esclarecimento e propõe um plano, que pode ser revisado antes do início e ajustado durante a execução, inclusive com interrupção e novo foco. O Gemini gera um plano de várias etapas, editável por Edit plan, iniciado por Start research; permite escolher Thinking (todos) ou Pro (assinantes) e marcar as fontes Google Search, Gmail e Drive — desmarcar Search restringe a pesquisa aos arquivos selecionados. A Perplexity decompõe a pergunta de forma autônoma, sem etapa pública equivalente de aprovação do plano.

O controle de fontes também varia. Apenas o ChatGPT documenta a escolha entre restringir a pesquisa a determinados sites ou priorizá-los permitindo a web aberta. Na Perplexity, existe Manage sources, mas não foi confirmada restrição exclusiva por domínio dentro do Deep Research: indicar domínios no prompt não equivale a bloquear o restante da web. Para o caso jurídico, convém restringir a planalto.gov.br e gov.br/anpd e, ainda assim, auditar hierarquia e vigência.

> *» IA: Bloco Statement — dois briefs verbatim; preservar as aspas triplas.*

"""
Brief — caso-guia (dados públicos)
Pergunta: como mudou a população brasileira de 60 anos ou mais e de 65 anos ou mais entre 2010 e 2022?
Decisão apoiada: [ex.: pauta de reportagem | seção de relatório técnico]
Recorte: Brasil, 2010–2022, com diferenças regionais quando houver.
Fontes obrigatórias: IBGE (Censo 2022 e IBGE Educa). Fontes secundárias só para contexto.
Formato: resumo; tabela afirmação–número–fonte–data; evidências contrárias; lacunas.
Conclusão: cada número com fonte primária e data; separar os cortes 60+ e 65+.
"""

"""
Brief — caso jurídico (J2)
Pesquise a obrigação de comunicar incidente de segurança sob a LGPD e a Resolução CD/ANPD 15/2024. Use apenas planalto.gov.br, gov.br/anpd e o repositório do Ministério da Justiça para a conclusão normativa. Distinga lei, regulamento e orientação; informe vigência e artigo; não dê parecer para caso concreto; transcreva no máximo o trecho necessário; liste qualquer conflito ou mudança posterior.
"""

### Exercício Prático

> *» IA: Bloco Process — um passo por etapa, verbatim; preservar os breadcrumbs; não traduzir termos de interface.*

**Exemplo aplicado (6 min):** ler os dois briefs acima e copiá-los para a aba Registro.

**Demonstração (10 min)**

1. Abrir o recurso na ferramenta com saldo e colar o brief do caso-guia.
2. No ChatGPT: responder às perguntas de esclarecimento e revisar o plano proposto antes de confirmar. Para o caso jurídico: `ChatGPT > caixa do prompt > Sites > Manage sites`, inserir os domínios e escolher restringir.
3. No Gemini: `Deep Research > plano > Edit plan`, incluir "separar 60+ e 65+" se o plano não o fizer; depois `Start research`.
4. Registrar brief, plano, modo e horário; enquanto o agente trabalha, preparar as linhas da aba Auditoria.
5. Rota sem cota: ler no relatório do MIT o prompt e o plano usados e registrá-los.

> *» IA: Bloco Statement — verbatim; preservar o emoji e os breadcrumbs.*

> 🏁 Ponto de controle: no Gemini, `Deep Research > plano` exibe a etapa acrescentada antes de Start research; no ChatGPT, o plano confirmado aparece no início da atividade da pesquisa.

**Pílula Hands-on (6 min):** reescrever o brief "Quais os juros no Brasil?" com os seis componentes, para as decisões do Copom de janeiro de 2025 a setembro de 2026.

**Critério de êxito:** o brief contém as seis linhas, nomeia o Banco Central como fonte obrigatória e pede data e percentual de cada decisão.

### Mão na massa

> *» IA: Bloco Statement — prompt editável verbatim; preservar as aspas triplas.*

Prompt-base para qualquer pesquisa profunda, a ser adaptado:

"""
Atue como assistente de pesquisa, não como autoridade final. Produza um relatório para [público/decisão] sobre [pergunta]. Recorte: Brasil, [datas]. Priorize [fontes primárias/domínios] e separe fatos, inferências e lacunas. Para cada número, cite a fonte exata e a data. Inclua: resumo; método e consultas; achados; evidências contrárias; limitações; tabela afirmação–fonte–trecho; e lista de pontos que exigem verificação humana. Não preencha lacunas com suposições. Antes de começar, faça até cinco perguntas e proponha um plano editável.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 4 — Auditoria do relatório

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe o relatório obtido no Módulo 3; desloca o foco da produção para a verificação.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Extrair e numerar as afirmações verificáveis de um relatório.
2. Classificar o suporte de cada citação como integral, parcial, ausente ou fonte inacessível.
3. Aplicar SIFT e leitura lateral para avaliar autoria, data e independência das fontes.
4. Identificar lacunas e famílias de evidência repetidas.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir.*

A auditoria parte de uma constatação documentada: citação visível não garante suporte. Os erros mais comuns em relatórios de pesquisa assistida são fonte inexistente ou mal atribuída, fonte verdadeira que não sustenta a frase, fonte de baixa autoridade, duplicação, desatualização, paywall (o agente vê apenas trecho ou resumo), omissão, inferência excessiva e confiança indevida. A própria OpenAI reconhece, no lançamento e no System Card, alucinações, dificuldade de distinguir fonte autoritativa de rumor e confiança mal calibrada.

O procedimento mínimo tem dez passos: salvar prompt, plano, relatório e horário; numerar as afirmações verificáveis; abrir cada citação; procurar no original a frase ou o número; registrar "suporta", "suporta parcialmente", "não suporta" ou "fonte inacessível"; conferir autor, data, atualização e conflito de interesse; procurar a fonte primária; listar lacunas e perspectivas ausentes; corrigir o texto; guardar a trilha de evidências. Para uso de alto risco, prioriza-se a conferência de 100% das conclusões centrais e de uma amostra das demais.

Dois métodos de bibliotecas universitárias apoiam o passo de avaliação. O **SIFT** — Stop; Investigate the source; Find trusted coverage; Trace claims to original context — e a **leitura lateral**, que consiste em sair da página e investigar autor, organização, financiamento e cobertura independente em outras abas. Ambos ajudam a detectar **famílias de evidência**: várias fontes que apenas repetem a mesma matéria contam como uma, não como várias.

A auditoria termina na **lacuna**: comparar o brief com o que foi respondido e procurar grupos, períodos, fontes e contrapontos ausentes. No caso jurídico, acrescenta-se a vigência: legislação revogada exige abrir o texto consolidado, conferir atos alteradores e o repositório oficial. Um alerta final: o relatório nunca serve de evidência de si mesmo.

### Exercício Prático

> *» IA: Bloco Process — um passo por etapa, verbatim; preservar os breadcrumbs.*

**Demonstração (10 min)**

1. No relatório do Módulo 3 (ou do MIT), numerar cinco afirmações verificáveis.
2. Abrir a citação de cada uma em nova aba e localizar o trecho com `navegador > Localizar (Ctrl+F; no Mac, Cmd+F)`.
3. Preencher a aba Auditoria com trecho, suporte, tipo de fonte e decisão.
4. Para o caso-guia, comparar os números com `educa.ibge.gov.br > Jovens > Conheça o Brasil > População > Pirâmide etária` e com o PDF "Censo 2022 — Pessoas de 60 anos ou mais".

> *» IA: Bloco Statement — verbatim; preservar o emoji.*

> 🏁 Ponto de controle: na aba Auditoria, as cinco linhas têm a coluna Suporte preenchida e, quando a fonte é secundária, a fonte primária correspondente anotada.

**Pílula Hands-on (6 min):** conferir, no IBGE, os dados de 65+ em 2010 e 2022.

> *» IA: Bloco Statement — gabarito verbatim; preservar os números.*

**Gabarito:** 65+ = 7,4% e 14 milhões em 2010; 10,9% e 22,2 milhões em 2022. Para 60+: 15,8% em 2022, crescimento de 46,6% sobre 2010. Para o caso jurídico: comunicação à ANPD e aos titulares em três dias úteis (art. 6º da Resolução 15/2024); registro do incidente por pelo menos cinco anos (art. 10). **Critério de êxito:** valores, URL e data da consulta registrados, sem misturar os cortes 60+ e 65+.

> *» IA: Bloco Knowledge Check — três itens com as opções "Integral", "Parcial" e "Não suporta"; enunciados e feedback verbatim.*

**Avaliação (4 min)** — com base no gabarito do IBGE, classificar o suporte de cada frase:

1. "Em 2022, pessoas com 65 anos ou mais eram 10,9% da população, cerca de 22,2 milhões."
2. "A população idosa cresceu 46,6% entre 2010 e 2022 e chegou a 10,9% do total."
3. "A parcela de pessoas com 65 anos ou mais dobrou entre 2010 e 2022."

**Gabarito:** 1 integral; 2 parcial — mistura cortes (46,6% refere-se a 60+; 10,9% a 65+); 3 não suporta — passou de 7,4% para 10,9% (e de 14 para 22,2 milhões), o que não é dobrar.

### Mão na massa

> *» IA: Bloco Statement — prompt editável verbatim; preservar as aspas triplas.*

Prompt-base de auditoria, para usar em uma IA diferente da que produziu o relatório (as respostas também devem ser conferidas à mão):

"""
Audite o relatório anexado. Extraia todas as afirmações verificáveis. Para cada uma, abra a fonte citada, copie o trecho que sustenta a afirmação, classifique suporte integral/parcial/ausente e registre data, autoria e tipo de fonte. Depois liste fontes inexistentes, links quebrados, dados antigos, conclusões sem evidência, grupos ausentes e perguntas não respondidas. Não use o próprio relatório como evidência.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 5 — Escolher a ferramenta e ler benchmarks

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 5" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe a experiência de produção e auditoria; desloca o foco para a escolha entre ferramentas e a leitura crítica de comparações.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Comparar as três ferramentas por planejamento, controle de fontes, saída e acesso gratuito.
2. Identificar autoria, métrica e conflito de interesse em um benchmark.
3. Escolher a ferramenta conforme a tarefa, e não por "vencedor" declarado.

### Texto Descritivo

> *» IA: Bloco Text — verbatim.*

As três ferramentas diferem em pontos verificáveis.

> *» IA: Bloco Table — comparativo verbatim (alternativa: Tabs, uma aba por ferramenta); não traduzir termos de interface.*

| Aspecto | ChatGPT deep research | Gemini Deep Research | Perplexity Deep Research |
|---|---|---|---|
| Plano | Perguntas de esclarecimento; plano editável antes e durante | Plano editável (Edit plan) antes do início | Decomposição autônoma, sem aprovação pública do plano |
| Controle de fontes | Restringir ou priorizar sites; arquivos; apps elegíveis | Google Search, Gmail, Drive; Search pode ser desligado | Manage sources; restrição exclusiva por domínio não confirmada |
| Saída | Markdown, Word, PDF | Export to Docs, Copy, Share, Audio Overview, visuais | Citações inline; formatos de exportação a testar [conferir] |
| Gratuito | Acesso limitado, saldo no produto | Limite diário variável | 1 pesquisa por mês |

> *» IA: Bloco Text — verbatim; preservar os números; não resumir.*

Benchmark é um conjunto padronizado de tarefas e métricas; não reproduz todo uso real, e seus resultados dependem de versão, prompt, acesso à web, avaliador e data. Três estudos circulam com frequência. O **BrowseComp**, criado pela OpenAI, tem 1.266 problemas de localização de fatos difíceis; o deep research da empresa obteve 51,5%, mas a própria OpenAI informa treinamento em dados específicos para essas tarefas, e o resultado agrega até 64 tentativas. O **DRACO** (2026) avaliou 100 tarefas em 10 domínios com um modelo como juiz; a Perplexity liderou com 67,15%, mas os autores incluem pesquisadores da Perplexity e as tarefas vieram de consultas da própria Perplexity. O **DeepResearch Bench** (2025), acadêmico e aberto, separa qualidade do relatório de precisão de citação: o Gemini produziu mais citações efetivas (111,21 em média), e a Perplexity teve maior precisão de citação — ambos com versões de 2025, já superadas.

Depreende-se que nenhum desses números ranqueia as ferramentas de forma neutra, e que não há benchmark atual e independente em português do Brasil. Um teste de imprensa (Axios, 2025) encontrou o ChatGPT mais detalhado e ambos melhores em resumir consenso do que em trazer novidade — amostra pequena, sem auditoria estatística. Recomenda-se escolher por tarefa: ChatGPT quando restrição de sites e exportação editável importam; Gemini quando o corpus está no Gmail ou no Drive, ou quando Docs e áudio são o destino; Perplexity quando o fluxo centrado em citação e a rapidez são prioritários — e validar na própria pergunta.

### Exercício Prático

> *» IA: Bloco Process — três cenários, um por etapa, verbatim.*

**Exemplo aplicado (6 min):** ler a tabela comparativa e registrar, na aba Registro, a ferramenta usada no Módulo 3 e a justificativa da escolha.

**Discussão orientada (8 min):** indicar a ferramenta mais adequada e a justificativa:

1. Relatório jurídico que só pode usar planalto.gov.br e gov.br/anpd.
2. Pesquisa que deve cruzar cinco documentos internos de uma pasta do Drive, já autorizada.
3. Primeira aproximação rápida, com citações inline, para pauta do dia.

> *» IA: Bloco Statement — gabarito verbatim.*

**Gabarito:** 1 ChatGPT, por documentar restrição de sites (e ainda assim auditar); 2 Gemini, com Drive marcado e Search desligado para separar "o que os arquivos dizem"; 3 Perplexity, se houver saldo. Aceitam-se outras escolhas com justificativa por recurso documentado.

> *» IA: Bloco Knowledge Check — uma questão de múltipla escolha; enunciado, alternativas e feedback verbatim.*

**Avaliação (4 min):** o resultado de 67,15% da Perplexity no DRACO:
a) prova que a Perplexity é a melhor ferramenta b) deve ser lido considerando que os autores têm vínculo com a Perplexity c) vale para português do Brasil d) mede a mesma coisa que o BrowseComp

**Gabarito:** b.

### Mão na massa

> *» IA: Bloco Statement — modelo editável verbatim; preservar as aspas triplas.*

Ficha-base para ler qualquer benchmark ou comparação de ferramentas, a ser preenchida:

"""
Benchmark: [nome, data] · Quem fez: [autores e vínculos]
O que mede: [ex.: achar fatos difíceis | qualidade do relatório | precisão de citação]
Tarefas: [quantas, de que tipo, em que idioma] · Quem avaliou: [humano | modelo-juiz]
Versões testadas: [ ] · Ainda são as atuais? [sim | não]
Conflito de interesse: [ ] · Vale para a minha tarefa? [por quê]
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 5" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 6 — Síntese e Aplicação Integrada

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 6" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe todos os módulos anteriores; integra produção, auditoria e correção no dossiê do caso-guia.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Auditar integralmente as conclusões centrais de um relatório.
2. Produzir versão corrigida que separe fatos, inferências e lacunas.
3. Registrar o método de modo que a pesquisa possa ser repetida.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir.*

O produto de uma pesquisa profunda responsável não é o relatório da IA, mas o relatório auditado. A versão corrigida mantém o que foi confirmado na fonte primária, reduz a alegação quando o suporte é parcial e remove o que não se sustenta. Separa explicitamente fatos verificados, inferências (com indicação de que são inferências) e lacunas — inclusive as do próprio brief. Toda correção remete à linha correspondente da planilha.

O registro do método completa o dossiê: ferramenta e modo, data e horário, brief, plano (com as edições feitas), configuração de dados adotada e limitações. Esse registro é o que permite repetir a pesquisa em outra data e explicar diferenças: o mesmo brief pode produzir relatórios distintos em versões ou dias diferentes.

### Exercício Prático

> *» IA: Bloco Process — atividade integradora, um passo por etapa, verbatim.*

**Atividade integradora: dossiê do caso-guia (16 min)**

1. **Auditoria (6 min):** completar a aba Auditoria com as cinco afirmações centrais do relatório do caso-guia (ou do caso jurídico), cada uma com trecho da fonte primária.
2. **Correção e lacunas (6 min):** redigir a versão corrigida em três seções (fatos verificados, inferências, lacunas) e o registro do método.
3. **Autoavaliação (4 min):** aplicar a tabela de critérios.

> *» IA: Bloco Statement — verbatim; preservar o emoji.*

> 🏁 Ponto de controle: cada frase da seção "Fatos verificados" remete a uma linha da aba Auditoria marcada como "integral" ou corrigida a partir de "parcial".

> *» IA: Bloco Checklist — critérios verbatim, um item por linha.*

| Critério | Atendido? |
|---|---|
| Brief com seis componentes e sem dados pessoais | |
| Execução registrada (ferramenta, modo, data, plano e edições) ou rota sem cota declarada | |
| Cinco afirmações centrais com suporte classificado e trecho da fonte | |
| Números conferidos na fonte primária, sem misturar cortes ou períodos | |
| Versão corrigida separando fatos, inferências e lacunas | |
| Configuração de dados registrada e nenhum material sigiloso enviado | |

**Critério de êxito:** seis critérios atendidos.

### Mão na massa

> *» IA: Bloco Statement — modelo editável verbatim; preservar as aspas triplas.*

Modelo-base da versão corrigida, a ser preenchido:

"""
RELATÓRIO AUDITADO — [pergunta] · [data]
Fatos verificados: [afirmação] — [fonte primária, data] (Auditoria nº __)
Inferências: [o que se deduz, marcado como inferência, e a partir de quê]
Lacunas: [o que o brief pedia e não foi encontrado; grupos, períodos ou fontes ausentes]
Método: [ferramenta, modo, data e hora, brief, plano e edições, configuração de dados]
Limitações: [paywall, fontes repetidas, versões, idioma]
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 6" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Encerramento

> *» IA: Bloco Text — dois parágrafos verbatim.*

O curso apresentou a pesquisa profunda como trabalho de um agente que planeja, busca e sintetiza — e que, por isso mesmo, exige um brief claro antes e uma auditoria rigorosa depois. Recomenda-se aplicar o ciclo brief, plano, execução, auditoria e correção a cada uso, conferindo sempre as conclusões centrais na fonte primária e registrando a configuração de dados adotada.

Para aprofundamento, indicam-se *Checagem de Fontes e Citações - Essentials* (verificação detalhada de citações científicas e jurídicas) e *Revisão Bibliográfica com IA - Hands On* (revisão de literatura com triagem e PRISMA), além do System Card da OpenAI e dos guias de avaliação de fontes das bibliotecas universitárias.

> *» IA: Bloco Statement — citação final verbatim.*

> **Síntese:** o agente pesquisa; a responsabilidade pelo que o relatório afirma continua de quem o assina.
