# Relatório de Edição — ChatGPT CODEX (Hands On), trilha SCORM

Revisão feita em 7 de outubro de 2026 com a skill `revisar-curso-scorm`.

## Pacote

- Original: `chatgpt-codex-hands-on-scorm12-wsKICsUG.zip` (não foi modificado)
- Revisado: `chatgpt-codex-hands-on-scorm12-wsKICsUG-REVISADO.zip`
- Formato: default (`scormcontent/runtime-data.js`)
- Título no pacote: `ChatGPT CODEX - Hands On` (bate com o título esperado, usado como trava na extração)
- `course.id`: `fN9ngsTJ7w33fLOZaVYLFwlFj8Hl9FP5`
- 3 lições. Títulos originais (em inglês) → revisados:
  - `Getting Started with Codex and ChatGPT` → **Descobrindo o Que o Codex Faz por Você**
  - `Connecting Codex to GitHub and Delegating Tasks` → **Conectando o Codex ao GitHub e Pedindo Sua Primeira Tarefa**
  - `Reviewing, Approving, and Delivering AI-Completed Tasks` → **Conferindo o Trabalho do Agente e Entregando o Projeto Final**

## O problema principal: o curso foi gerado em inglês

O roteiro-fonte é em português, os cursos irmãos (Codex Essentials, Excel, Word, PowerPoint) estão
em português, mas **todo o texto pedagógico do pacote veio em inglês**, com os prompts do roteiro
colados em português no meio ("Type exactly: O que é o Codex..."). A capa também estava em inglês.

Por isso esta revisão foi, além de melhoria de texto, uma **tradução completa para PT-BR feita a
partir do roteiro**, e não do inglês: sempre que o roteiro tinha a frase, ela foi usada.

## Material-fonte e mapeamento lição ↔ oficina

- Referência principal: `Codex-Para-Leigos-Hands-on.md` (mesmo conteúdo do `.pdf`).
- Regras de edição: `promptRevisaoPorClaude.md` (raiz do repositório).

| Lição do SCORM | Seções do roteiro |
|---|---|
| 1 — Descobrindo o Que o Codex Faz por Você | Abertura ("Antes de Arregaçar as Mangas", "O que você precisa ter aberto agora", "Regra de ouro") + Oficina 1 |
| 2 — Conectando o Codex ao GitHub e Pedindo Sua Primeira Tarefa | Oficina 2 + Oficina 3 |
| 3 — Conferindo o Trabalho do Agente e Entregando o Projeto Final | Oficina 4 + Projeto Final + "Conseguiu! E agora?" |
| — (sem bloco próprio) | "O Mapa da Mão na Massa" e "A Parte dos Dez" (ver Pontos de atenção, item 3) |

Diferente do curso de PowerPoint, aqui o **Projeto Final existe no SCORM** (process de 6 passos na
Lição 3, igual ao roteiro).

## Critério aplicado

- **Tom do roteiro "Para Leigos"**: segunda pessoa, direto, sem fórmulas de IA ("Welcome to your
  first step into practical AI automation!", "Unlocking Real Automation", "your confidence and
  skills will only grow from here!").
- **Aberturas** trocadas pelos blocos "🎯 O Problema" de cada oficina.
- **Objetivos** padronizados com "Ao final desta lição, você será capaz de:" e alinhados, na ordem,
  ao que cada oficina realmente faz.
- **Processes** seguem os passos do "👐 Mão na massa"; o resumo de cada um virou o "✅ Deu certo?"
  do roteiro, com o "🚀 Quer ir além?" quando não havia outro lugar para ele.
- **Accordions "Se travar"** reproduzem as tabelas "🚑 Se travar" do roteiro, com títulos por oficina.
- **Prompts** copiados do roteiro, em itálico e entre aspas, cada um em parágrafo próprio.
- **Fechamentos** trocados pelos próximos passos concretos (o que a próxima lição faz e o que ter à mão).
- **Nomes dos modos**: o roteiro diz que os nomes variam e sugere procurar algo como "Perguntar" e
  "Gerar código". O curso usava "Ask Mode"/"Task Mode". Ficou "modo de pergunta" (termo do roteiro)
  e "modo de tarefa", sempre ligado a "gerar/executar".
- **Não editados de propósito**: os 6 botões "Continue" dos divisores (os cursos irmãos também os
  mantêm em inglês) e as frentes de flashcard "ChatGPT", "Codex" e "Prompt" (iguais em português).

Método de edição: `aplicar_edicoes.py` + `edicoes_handson.py` (nesta pasta), com aplicação por
caminho JSON e trava sobre o valor original: o script recusa campo não textual, campo inexistente,
campo já alterado e texto igual ao original. A capa foi traduzida por `traduzir_descricao_curso.py`,
que grava um JSON-base separado (`cursoChatGPTCodexHandsOn_base_capa_pt.json`) e também tem trava
sobre o texto original.

## Alterações lição a lição

### Capa do curso (1 campo, fora das lições)

- `course.description`: o texto genérico em inglês ("Ready to see AI in action?...") virou a promessa
  do roteiro (uma tarefa real em menos de 90 minutos), o que o curso cobre (quatro oficinas e um
  Projeto Final) e o "não é preciso saber programar". O `<div data-editor-id>` foi preservado.

### Lição 1 — Descobrindo o Que o Codex Faz por Você (73 campos)

- **Abertura**: "Welcome to Hands-On AI Automation with Codex" virou o "Antes de Arregaçar as
  Mangas" do roteiro, com o formato do curso (4 oficinas + Projeto Final, cerca de 85 minutos) e o
  aviso de fazer na ordem.
- **Objetivos**: o item 4, "Prepare your workspace for automation by organizing your tools", não
  corresponde à Oficina 1 (a preparação do repositório é da Oficina 2). Foi trocado pelo que a oficina
  entrega: usar o modo de pergunta sem alterar nada.
- **Process de preparação**: a introdução virou o "O que você precisa ter aberto agora". Voltaram o
  "plano gratuito já é suficiente" e o "procure algo como 'Perguntar' e 'Gerar código'".
- **Flashcards**: as definições ficaram concretas. Codex agora é descrito pelo que faz (cria e altera
  arquivos de um projeto conectado e mostra o que mudou).
- **Accordion dos modos**: o bloco introdutório virou o "🎯 O Problema" da Oficina 1 (o chat comum
  dá uma resposta, e quem faz o trabalho continua sendo você). "Por que isso importa" ganhou o item 1
  da Parte dos Dez (na dúvida, comece perguntando).
- **Process "Mão na massa"**: o passo opcional "Try Rephrasing" repetia o accordion "Se travar". Foi
  trocado pelo "🚀 Quer ir além?" do roteiro (perguntar ao Codex as diferenças para um chat comum),
  que não existia no curso. O resumo virou o "✅ Deu certo?".
- **Se travar**: "General tips" virou a "💡 Dica" do roteiro.
- **Knowledge checks (2)**: enunciados e alternativas traduzidos; feedbacks das erradas agora dizem
  por que estão erradas. Gabaritos inalterados.
- **Fechamento**: o que a Lição 2 faz e "deixe à mão o login do GitHub".

### Lição 2 — Conectando o Codex ao GitHub e Pedindo Sua Primeira Tarefa (71 campos)

- **Abertura**: "Unlocking Real Automation" virou o "🎯 O Problema" da Oficina 2 ("um agente de
  trabalho precisa de um lugar para trabalhar"), com o material necessário e os 15 minutos da Oficina 3.
- **Objetivos**: alinhados às duas oficinas (o item "Authorize and manage access" virou "revisar as
  permissões concedidas", que é o que o roteiro pede).
- **Process da Oficina 2**: passos do roteiro; o resumo virou o "✅ Deu certo?" com o "🚀 Quer ir
  além?" (explorar a lista de arquivos de dentro do Codex). **Desvio do roteiro** no passo 2: ver
  Pontos de atenção, item 1.
- **Accordion "Se travar na Oficina 2"**: soluções do roteiro, mais "confira se o meu-teste-codex
  está entre os repositórios selecionados".
- **Bloco de destaque**: repetia o accordion "Safety First" palavra por palavra. Virou uma regra
  distinta: praticar sempre no repositório de teste até dominar o ciclo pedir/conferir/aceitar.
- **Flashcards das quatro partes**: cada verso traz a pergunta-chave do roteiro (o quê, onde, o que
  não mexer, como saber que terminou) e o exemplo tirado do próprio prompt da Oficina 3.
- **Process da Oficina 3**: os dois prompts do roteiro em parágrafo próprio. O resumo virou o "✅ Deu
  certo?" (o diff com a seção "Sobre o projeto") com o "🚀 Quer ir além?" (seção "Como usar").
- **Se travar na Oficina 3**: voltou o "até 30 minutos" do roteiro (o curso dizia só "can take
  longer").
- **Destaque final**: virou o "📌 Não esqueça" do roteiro.
- **Knowledge check**: traduzido; feedbacks explicam o motivo. Gabarito inalterado.
- **Fechamento**: "terminou não é sinônimo de está certo" e o aviso de manter à mão a tarefa do
  README, que é o ponto de partida da Oficina 4.

### Lição 3 — Conferindo o Trabalho do Agente e Entregando o Projeto Final (63 campos)

- **Abertura**: "Ensuring Quality" virou o "🎯 O Problema" da Oficina 4 e anuncia o Projeto Final.
- **Objetivos**: o lead-in "In this lesson, you will learn the essential steps involved in managing
  and completing a task" (vago, fora do padrão) foi padronizado. Os itens, que eram rótulos soltos
  ("Monitor Task Outputs"), viraram habilidades: ler o diff, conferir o log, decidir e explicar,
  entregar.
- **Process da Oficina 4**: a introdução manda abrir a tarefa do README feita na Oficina 3. O
  resumo virou o "✅ Deu certo?" com o "🚀 Quer ir além?".
- **Flashcards**: frentes traduzidas ("Diff (comparativo)", "Log (registro)", "Critério para
  aceitar"); o verso do Log ganhou o item 7 da Parte dos Dez (o log é a prova do que o Codex fez).
- **Se travar na Oficina 4**: o prompt "Explique por que você alterou esta linha" voltou; "General
  caution" virou o "⚠️ Cuidado" do roteiro (aceitar só para ganhar tempo).
- **Destaque**: une o item 9 da Parte dos Dez e a "🤓 Curiosidade técnica" da Oficina 4.
- **Process do Projeto Final**: passos do roteiro. O resumo virou o checklist "🏁 Como saber que
  terminou" (os 5 itens, em um parágrafo). O passo 3 dizia "como nas Oficinas 1 e 3"; ficou "como na
  Oficina 3", porque a Oficina 1 não tem execução de tarefa.
- **Knowledge check**: traduzido; feedbacks explicam o motivo. Gabarito inalterado.
- **Fechamento**: o "your confidence and skills will only grow from here!" virou o "Conseguiu! E
  agora?" do roteiro, com os itens 3, 4 e 5 da Parte dos Dez (dividir tarefas grandes, tarefas em
  paralelo, AGENTS.md com `/init`).

## Contagem de campos alterados

Confirmada por `validar_estrutura.py`: **207 campos de texto nas lições** (L1 = 73, L2 = 71,
L3 = 63). Por campo: title = 76, description = 70, paragraph = 34, feedback = 16, heading = 11.
A contagem do validador bate exatamente com a do script de edição. Somando a capa, **208 campos**.

## Validações

- `validar_estrutura.py`: **estrutura preservada em todas as lições**, 0 divergências estruturais.
- Conferência de HTML (parser): tags balanceadas em todos os campos de texto, 0 problemas.
- Varredura de inglês remanescente: 0 campos com palavras em inglês, fora os 6 botões "Continue".
- Gabaritos: os 4 knowledge checks têm exatamente os mesmos `correct` do original, e os 4 são
  coerentes com o roteiro (modo de tarefa; refazer com mais contexto; as quatro partes do pedido;
  pedir explicação e conferir o log).
- Comparação dos dois `.zip` decodificados: fora das lições, a única diferença é
  `course.description`; dentro delas, 207 diferenças, todas em campos de texto.
- `scorm_reempacotar.py`: round-trip do Base64 conferido. 83 arquivos no pacote, apenas
  `scormcontent/runtime-data.js` substituído e 0 arquivos alterados fora do alvo.
- **Teste em navegador** (LMS simulada com API SCORM 1.2, carregando o `scormdriver` original): o
  curso carrega; a capa mostra a descrição nova e os três títulos em português; o texto renderizado
  das três lições foi lido inteiro (liberando os botões "Continue") e corresponde às edições. Captura
  de tela conferida no topo da Lição 1 (acentos, títulos e barra lateral corretos).
- **Não verificado visualmente**: o conteúdo dos accordions abertos, o verso dos flashcards virados e
  a exibição dos feedbacks dos quizzes. Esses textos foram validados no JSON e no HTML, não na tela.

## Pontos de atenção (exigem olho humano)

1. **Desvio do roteiro: repositório com README.** O roteiro manda criar um repositório "novo e
   vazio", mas a Oficina 3 pede para adicionar uma seção ao `README.md` "sem perder o conteúdo que já
   existia", o que supõe que o README já existe. Além disso, um repositório sem nenhum commit pode
   não ser utilizável pelo Codex (não testado). O passo agora pede para marcar "Add a README file" na
   criação. **Sugestão: corrigir também o roteiro** (`Codex-Para-Leigos-Hands-on.md`, Oficina 2,
   passo 2).
2. **Rótulos da interface do Rise em inglês.** "START COURSE", "Lesson 1 of 3", "Continue",
   "SUBMIT", "TAKE AGAIN", "Click to flip" vêm do conjunto de rótulos do curso (`labelSet` "English"),
   que não é texto pedagógico e não foi tocado. Os cursos irmãos estão iguais. Para traduzir, troque
   o idioma dos rótulos nas configurações do curso no Rise.
3. **Seções do roteiro sem bloco no SCORM.** "O Mapa da Mão na Massa" (tabela de oficinas e tempos)
   foi resumido em uma frase da abertura. Da "A Parte dos Dez", os itens 1, 2, 3, 4, 5, 7 e 9 foram
   incorporados a blocos existentes; **os itens 6 (ambiente isolado por tarefa), 8 (internet
   desativada por padrão) e 10 (Codex serve também para pesquisa, planilhas e documentos) não estão no
   curso**. A estatística da "🤓 Curiosidade técnica" do Projeto Final ("mais da metade dos usuários
   avançados...") também não foi incluída, por não ter fonte citada no roteiro. Acrescentar um bloco
   para a Parte dos Dez é mudança estrutural, a fazer no Rise.
4. **Dados para conferir antes de publicar** (todos vêm do roteiro, nenhum foi verificado nesta
   revisão):
   - "o plano gratuito já é suficiente para acompanhar o curso": a disponibilidade do Codex por plano
     muda com frequência;
   - nomes dos modos na interface ("Perguntar"/"Gerar código"): o roteiro já avisa que variam;
   - "tarefas mais complexas podem levar até 30 minutos";
   - AGENTS.md criado com o comando `/init`: confirmar em qual interface do Codex o comando existe.
5. **Distrator "Apenas chat"** (quiz 1 da Lição 1): não é um modo real do Codex. Funciona como
   distrator e o feedback explica por que está errado, mas vale saber que não corresponde a nenhuma
   opção da interface.
6. **Nomes dos arquivos de lição** continuam com os títulos originais em inglês (vêm da extração e
   são referenciados em `edicoes_handson.py`). Não afetam o pacote.

## O que foi gerado

Em `Criacao de Cursos/GPT/Codex/hands-on/`:

- `cursoChatGPTCodexHandsOn.json`: payload desserializado original.
- `cursoChatGPTCodexHandsOn_base_capa_pt.json`: original com a descrição da capa traduzida (base da
  remontagem).
- `licoes_extraidas_ChatGPTCodexHandsOn/licao_01…03_*.json`: lições separadas (todas editadas) +
  `indice_licoes.json`.
- `licoes_extraidas_ChatGPTCodexHandsOn/edicoes_handson.py`, `aplicar_edicoes.py` e
  `traduzir_descricao_curso.py`: registro e aplicação de cada campo alterado.
- `cursoChatGPTCodexHandsOn_editado.json`: curso fundido com as edições.
- `cursoChatGPTCodexHandsOn_editado_base64.txt`: Base64 final (112.424 caracteres), com round-trip
  verificado.
- `chatgpt-codex-hands-on-scorm12-wsKICsUG-REVISADO.zip`: pacote reempacotado.

Entregue em `OpenAI/OPENAI (ChatGPT)/ChatGPT CODEX/hands-on/`: o `.zip` revisado, a versão extraída
`HandsOnChatGPT_CodexRevisado/`, este relatório e o roteiro-fonte (`.md` e `.pdf`).
