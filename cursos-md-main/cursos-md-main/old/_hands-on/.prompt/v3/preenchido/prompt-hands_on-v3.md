# PROMPT — Roteiro Hands-on para Articulate Rise 360

---

# CONTEXTO

Você atuará como designer instrucional especializado em cursos digitais interativos. Sua tarefa é transformar um Plano de Aula Hands-on — anexado como material-fonte — em um roteiro instrucional completo, em português, adequado para implementação no **Articulate Rise 360**.

O curso é autoinstrucional, prático e orientado à execução. Diferentemente do curso Essentials correspondente, cujo foco é a compreensão conceitual, este curso Hands-on conduz o participante por **ações concretas**, com curva de aprendizado progressiva e entregáveis verificáveis em cada etapa.

A linguagem deve ser formal, impessoal, acessível e didática. Conceitos são mencionados apenas quando necessários à execução. O foco é: **fazer, testar, validar e ir além**.

---

# OBJETO BASE (preencher antes de usar)

- **Tema/ferramenta do curso:** Claude no PowerPoint
- **Público-alvo:** docentes do ensino superior iniciantes em IA; analistas administrativos; alunos do ensino superior.
- **Material-fonte:** `curso-claude-ppt.md`
- **Nome do arquivo de saída:** `v3Roteiro_Articulate360_ClaudeParaPPT_Hands-on.md`

---

# CONFIGURAÇÃO (ajustar se necessário; manter o padrão caso contrário)

- **Carga horária total:** 90 a 150 minutos.
- **Estrutura padrão:**
  - 1 capítulo introdutório (sem atividade prática)
  - 4 atividades práticas, cada uma com 3 desafios de extensão
  - 1 trabalho de conclusão (tarefa nova e autônoma, mais complexa)
- **Plataforma de destino:** Articulate Rise 360.
- **Formato de saída:** documento único em Markdown.

---

# TAREFA

Produza o roteiro instrucional completo a partir do plano hands-on fornecido. O documento deve organizar o curso em **lições e blocos Rise 360**, com atividades práticas, desafios de extensão, trabalho de conclusão e critérios objetivos de êxito — pronto para orientar a implementação no Rise 360.

---

# ESTRUTURA OBRIGATÓRIA (nesta ordem)

## 1. Título

```
# Roteiro Rise 360 — [Nome da ferramenta ou tema] — Curso Hands-on
```

Subtítulo: `"[Título original do material-fonte] — Curso Hands-on"`

---

## 2. Identificação

Tabela de duas colunas: **Campo | Definição**.

| Campo | Definição |
|---|---|
| Curso | |
| Natureza | Hands-on — autoinstrucional |
| Plataforma de desenvolvimento | Articulate Rise 360 |
| Carga horária | |
| Público-alvo | |
| Pré-requisitos | *(ver regra abaixo)* |
| Recursos necessários | |
| Produto final do participante | |

**Regra de pré-requisitos — aplicar sempre:**

- **Ferramentas do pacote Office (Word, Excel, PowerPoint):**
  - [Desktop] Office 2021 ou superior instalado;
  - [Web] Office 365 ativo (assinatura institucional ou pessoal).
- **Claude e demais ferramentas de IA:**
  - Conexão ativa à internet;
  - Conta Claude com plano pago — Pro, Max, Team ou Enterprise.
- **Pré-requisito pedagógico obrigatório:**
  - Conclusão do curso Essentials correspondente ou conhecimento equivalente.

---

## 3. Objetivo Geral

Parágrafo único, formal e impessoal: finalidade prática do curso, ferramenta/processo utilizado, competência operacional desenvolvida e produto final esperado.

---

## 4. Competências Práticas a Desenvolver

Frase obrigatória: *"Concluído o curso, o participante deverá demonstrar capacidade de:"*

Listar **4 competências práticas**, mensuráveis e orientadas à execução.

---

## 5. Mapa do Curso

Parágrafo curto descrevendo a progressão do curso: do capítulo introdutório às quatro atividades práticas com desafios de extensão, até o trabalho de conclusão autônomo.

Tabela:

| Etapa | Título | Natureza | Tempo estimado |
|---|---|---|---|
| Capítulo 0 | [título] | Expositivo + interação leve | [X min] |
| Atividade 1 | [título] | Prática guiada + 3 desafios | [X min] |
| Atividade 2 | [título] | Prática guiada + 3 desafios | [X min] |
| Atividade 3 | [título] | Prática guiada + 3 desafios | [X min] |
| Atividade 4 | [título] | Prática guiada + 3 desafios | [X min] |
| Conclusão | [título] | Trabalho autônomo | [X min] |

> O tempo de cada atividade prática (1 a 4) deve ser semelhante entre si. O trabalho de conclusão pode ser mais longo, mas não deve ultrapassar o dobro do tempo de uma atividade individual.

---

# CAPÍTULO 0 — INTRODUÇÃO E CONEXÃO COM O ESSENTIALS

Este capítulo é **exclusivamente expositivo e informativo**. Não contém atividade prática. Seu papel é contextualizar o participante, apresentar o que o curso Essentials correspondente cobre e deixar claro o que este curso Hands-on vai adicionar.

## Roteiro de Blocos Rise 360 — Capítulo 0

| Bloco | Tipo Rise 360 | Conteúdo ou ação esperada |
|---|---|---|
| 0.1 | Cover | Título, subtítulo e imagem de abertura do curso |
| 0.2 | Text | Apresentação do Hands-on: o que é, para quem é e o que diferencia do Essentials |
| 0.3 | Statement | Pré-requisito pedagógico: conclusão do curso Essentials (ou equivalente) |
| 0.4 | Two-Column | Comparativo visual: Essentials (conceitos) × Hands-on (execução) |
| 0.5 | Text | O que o curso Essentials cobre — descrição sintética das competências desenvolvidas lá, com recomendação de acesso caso o participante ainda não o tenha feito |
| 0.6 | Text | O que este Hands-on vai além: visão geral das 4 atividades e do trabalho de conclusão |
| 0.7 | Knowledge Check | Verificação de pré-requisito pedagógico — não bloqueante (ver especificação abaixo) |
| 0.8 | Numbered List | Verificação de pré-requisitos técnicos — lista de confirmação (ver especificação abaixo) |
| 0.9 | Statement | Orientação para quem não dispõe dos recursos técnicos necessários |
| 0.10 | Button | "Iniciar a Atividade 1 →" |

### Conteúdo do Capítulo 0

Redigir de 3 a 4 parágrafos curtos cobrindo:

1. O papel do curso Essentials na trilha e o que ele desenvolve.
2. O que diferencia o Hands-on: foco na execução, não na explicação.
3. A estrutura do curso: 4 atividades práticas com desafios de extensão + trabalho de conclusão.
4. Orientação para quem ainda não fez o Essentials: recomendação explícita de fazer antes de prosseguir.

### Verificações de Prontidão do Capítulo 0

#### Verificação 0.7 — Pré-requisito pedagógico (Knowledge Check)

Criar uma pergunta única de confirmação, com resposta Sim / Não e feedback diferenciado por resposta:

- **Pergunta:** "O curso Essentials correspondente foi concluído, ou há conhecimento equivalente sobre o uso básico da ferramenta abordada neste curso?"
- **Resposta "Sim" →** retorno: "Excelente. O participante está apto a prosseguir para a Atividade 1."
- **Resposta "Não" →** retorno: "Recomenda-se concluir o curso Essentials antes de prosseguir, uma vez que este curso pressupõe os conceitos ali desenvolvidos. O avanço, contudo, permanece liberado."

> Esta verificação **não bloqueia** o avanço — é informativa e orientadora, não avaliativa.

---

#### Verificação 0.8 — Pré-requisitos técnicos (Numbered List)

Criar uma lista numerada de confirmação com título: **"Verifique se os recursos necessários estão disponíveis"**.

Adaptar os itens ao contexto da ferramenta do curso:

- **Se o curso envolve ferramentas do pacote Office:**
  1. Office 2021 ou superior instalado (Desktop) — ou Office 365 ativo (Web).
  2. Conta Claude com plano pago disponível (Pro, Max, Team ou Enterprise).
  3. Conexão ativa à internet.

- **Se o curso não envolve ferramentas Office:**
  1. Conexão ativa à internet.
  2. Conta Claude com plano pago disponível (Pro, Max, Team ou Enterprise).

O bloco Statement seguinte (0.9) deve conter a orientação:
"Caso algum recurso não esteja disponível, recomenda-se providenciá-lo antes de iniciar as atividades práticas. O avanço permanece liberado."

> Esta lista é uma autoavaliação informativa — não bloqueia o avanço e não tem interação avaliativa.

<div style="page-break-after: always;"></div>

---

# ATIVIDADES PRÁTICAS (1 a 4)

Criar um bloco por atividade, seguindo sempre a estrutura abaixo. As quatro atividades devem ter **tempo estimado semelhante** e **curva de complexidade crescente** entre si — a Atividade 1 é a mais acessível; a Atividade 4 é a mais desafiadora dentro da mesma lógica guiada.

---

## Atividade N — [Título da atividade]

### Encadeamento

> Uma linha indicando se é o ponto de partida ou como se conecta à atividade anterior.

### Finalidade Prática

Parágrafo curto: o que será executado, qual competência será exercitada e qual produto será produzido.

### Objetivos de Aprendizagem Prática

*"Ao final desta atividade, o participante deverá ser capaz de:"*

Listar 3 a 4 objetivos mensuráveis com verbos de ação: acessar, configurar, selecionar, preencher, testar, comparar, revisar, exportar, aplicar, validar.

---

### Roteiro de Blocos Rise 360 — Atividade N

| Bloco | Tipo Rise 360 | Conteúdo ou ação esperada |
|---|---|---|
| N.1 | Cover | Título e contexto da atividade |
| N.2 | Text | Contextualização mínima necessária à execução |
| N.3 | Process | Demonstração guiada — sequência de passos |
| N.4 | Checklist | Atividade prática guiada com autoavaliação |
| N.5 | Knowledge Check | Checkpoint de verificação |
| N.6 | Statement | Introdução aos desafios de extensão |
| N.7 | Accordion | Os 3 desafios de extensão (um item por desafio) |
| N.8 | Button | "Avançar para a Atividade [N+1] →" ou "Ir para o Trabalho de Conclusão →" |

> Adaptar os tipos de bloco conforme o conteúdo. Os tipos listados são o padrão recomendado — substituir por Tabs, Labeled Graphic, Scenario, Flashcards ou outros quando mais adequados.

---

### Conteúdo Instrucional Enxuto

De 2 a 3 parágrafos curtos: apenas o necessário para contextualizar e preparar a execução. Sem exposição teórica extensa.

**Regra BreadCrumb:** ao descrever navegação em interfaces, usar o formato `Menu > Submenu > Opção`.

---

### Demonstração Guiada

Sequência objetiva de execução:

1. Ação inicial.
2. Ação seguinte.
3. Configuração ou escolha.
4. Teste ou validação.
5. Resultado esperado.

**BreadCrumb obrigatório em passos de navegação:** toda ação que envolva acesso a menu, botão, painel, janela ou configuração de interface deve ser descrita no formato `Aplicativo > Menu > Submenu > Opção`, em vez de indicar captura de tela. Usar BreadCrumb também em instruções de complexidade média ou alta, mesmo fora de menus formais, sempre que a sequência de passos puder gerar dúvida de navegação.

---

### Atividade Prática Guiada

#### Atividade [N] — [Título] ([tempo estimado])

**Tarefa:** [descrever o que o participante deverá executar ou produzir.]

**Procedimento:**

1. [passo 1]
2. [passo 2]
3. [passo 3]
4. [passo 4]

**Produto esperado:** [descrever a entrega desta atividade.]

**Critério de êxito:** [definir condição objetiva e verificável de validação.]

---

### Checkpoint de Aprendizagem

Bloco Rise 360: **Knowledge Check**

Tipo (selecionar um): múltipla escolha | verdadeiro ou falso | correspondência | checklist.

Incluir gabarito ou critério de validação explícito.

---

### Desafios de Extensão

Os três desafios são **extensões diretas da atividade prática concluída** — o participante parte do que produziu e vai além. Cada desafio representa um nível adicional de complexidade ou de aplicação, sem introduzir um tema completamente novo.

Os desafios devem ser apresentados em bloco **Accordion** no Rise 360, com um item por desafio. Cada item do Accordion deve conter:

- **Título do desafio** (curto e orientado à ação);
- **O que fazer** (instrução objetiva em 2 a 4 linhas);
- **Como validar** (critério de êxito claro).

#### Estrutura dos 3 desafios:

**Desafio 1 — [Título]** *(nível: um passo além da atividade)*
O que fazer: [instrução objetiva.]
Como validar: [critério de êxito.]

**Desafio 2 — [Título]** *(nível: dois passos além da atividade)*
O que fazer: [instrução objetiva.]
Como validar: [critério de êxito.]

**Desafio 3 — [Título]** *(nível: aplicação em novo contexto ou maior escala)*
O que fazer: [instrução objetiva.]
Como validar: [critério de êxito.]

> Os desafios são **opcionais** para o avanço — o botão de progressão deve estar disponível independentemente de o participante tê-los realizado. A natureza opcional deve ser explicitada no bloco Statement que os introduz.

---

### Prompt ou Modelo Editável

Quando aplicável, fornecer modelo para o participante adaptar ao próprio contexto. Apresentar em bloco **Statement** ou bloco **Download** no Rise 360, delimitado por aspas triplas (não crases triplas):

"""
[Modelo editável — preencher os campos entre colchetes]
"""

---

### Fechamento da Atividade

Parágrafo curto: o que foi produzido, como poderá ser reaproveitado e qual será o próximo passo.

<div style="page-break-after: always;"></div>

---

# TRABALHO DE CONCLUSÃO

O trabalho de conclusão é uma **tarefa nova e autônoma**, no mesmo tema do curso, porém mais complexa e detalhada do que cada atividade individual. Ele **não** integra os produtos das atividades anteriores — é um projeto independente que mobiliza, de forma integrada, as competências desenvolvidas ao longo do curso.

O tempo estimado de execução deve ser **maior do que o de uma atividade individual**, mas **não deve ultrapassar o dobro** desse tempo.

---

## Trabalho de Conclusão — [Título]

### Finalidade

Parágrafo explicando o que torna este trabalho mais complexo do que as atividades anteriores e quais competências ele mobiliza de forma integrada.

---

### Roteiro de Blocos Rise 360 — Trabalho de Conclusão

| Bloco | Tipo Rise 360 | Conteúdo ou ação esperada |
|---|---|---|
| C.1 | Cover | Título e apresentação do trabalho de conclusão |
| C.2 | Text | Contextualização do cenário ou problema a resolver |
| C.3 | Statement | Orientações gerais e critérios de qualidade esperados |
| C.4 | Process | Sequência de execução do trabalho |
| C.5 | Checklist | Autoavaliação do resultado produzido |
| C.6 | Knowledge Check | Verificação final (opcional, mas recomendado) |
| C.7 | Button | "Concluir o curso ✓" |

---

### Conteúdo do Trabalho de Conclusão

De 2 a 4 parágrafos: apresentar o cenário ou problema proposto, situar o nível de complexidade em relação às atividades anteriores e orientar o participante sobre como abordar a execução.

---

### Tarefa de Conclusão

#### Trabalho de Conclusão — [Título] ([tempo estimado])

**Cenário:** [descrever o contexto ou problema que o participante deverá resolver.]

**Tarefa:** [descrever com precisão o que deverá ser executado ou produzido.]

**Procedimento sugerido:**

1. [passo 1]
2. [passo 2]
3. [passo 3]
4. [passo 4]
5. [passo 5]

**Produto final esperado:** [descrever a entrega concreta.]

---

### Critérios de Avaliação

| Critério | Descrição | Atendido? |
|---|---|---|
| Clareza da entrega | O produto final é compreensível e bem estruturado | |
| Completude | Todos os elementos solicitados estão presentes | |
| Aplicabilidade | O resultado é utilizável em contexto real | |
| Coerência | As escolhas feitas ao longo da execução são consistentes | |
| Revisão final | O participante revisou o produto antes de considerá-lo concluído | |

---

### Encerramento do Trabalho de Conclusão

Parágrafo curto destacando a competência prática consolidada, o valor do produto elaborado e possibilidades de uso ou aprofundamento.

---

# ORIENTAÇÕES PARA PRODUÇÃO NO RISE 360

## Organização das lições

- **Capítulo 0** → 1 lição (expositiva, com interação leve).
- **Atividades 1 a 4** → 1 lição por atividade (prática guiada + desafios).
- **Trabalho de Conclusão** → 1 lição (autônoma, mais extensa).
- Blocos devem ser curtos e progressivos — evitar blocos de texto corrido longos.
- Priorizar Process, Accordion, Checklist e Labeled Graphic em vez de parágrafos.
- BreadCrumb obrigatório para qualquer instrução de navegação em interface: `Aplicativo > Menu > Submenu > Opção`. Usar também em instruções de complexidade média ou alta sempre que a sequência de passos puder gerar dúvida de navegação.

## Navegação e conclusão

- Definir no Course Settings se a conclusão é por **progresso** (100% das lições visitadas) ou por **aprovação** no Knowledge Check do trabalho de conclusão.
- Blocos de atividade prática e checkpoints: avanço **restrito** — "Continuar" liberado após interação completa.
- Desafios de extensão e blocos informativos: avanço **livre** — participante pode prosseguir sem completá-los.
- O Knowledge Check do bloco 0.7 (pré-requisito pedagógico) é **não bloqueante** — o participante avança independentemente da resposta.
- A Numbered List do bloco 0.8 (pré-requisitos técnicos) é **informativa** — não há interação avaliativa e o avanço é livre.

## Interações recomendadas por tipo de conteúdo

| Conteúdo | Bloco Rise recomendado |
|---|---|
| Sequência de passos operacionais | Process |
| Comparação entre opções ou conceitos | Tabs ou Two-Column |
| Informações complementares ou desafios | Accordion |
| Conceitos com frente e verso | Flashcards |
| Diagrama com elementos clicáveis | Labeled Graphic |
| Alerta, princípio-chave ou instrução destacada | Statement |
| Verificação de aprendizagem | Knowledge Check |
| Tarefa com autoavaliação | Checklist |
| Arquivo ou modelo para download | Download |
| Cenário de tomada de decisão | Scenario |

## Padrão de linguagem de cada bloco

Todo bloco deve ter:

- **Título curto** (obrigatório);
- **Instrução objetiva** — o que o participante deve fazer ou observar;
- **Uma ação principal** por bloco;
- **Feedback imediato** quando houver interação;
- **Indicação clara de avanço** (botão ou instrução textual).

---

# ENCERRAMENTO

Redigir 2 parágrafos.

O primeiro reafirma a finalidade prática cumprida e destaca o produto final elaborado no trabalho de conclusão.

O segundo aponta possibilidades de aprofundamento, prática contínua ou aplicação em novos contextos — e, quando pertinente, menciona o próximo curso da trilha.

> **Síntese:** [frase que resume a filosofia hands-on do curso.]

---

# ESTILO OBRIGATÓRIO

- Registro formal, impessoal e acadêmico.
- Evitar 2ª pessoa ("você", "seu", "sua"); preferir "o participante deverá", "recomenda-se", "observa-se", "deve-se".
- Priorizar execução prática, orientação passo a passo e entregáveis verificáveis.
- Explicar conceitos apenas quando necessários à prática — sem transformar o roteiro em aula teórica.
- Linguagem acessível, sem informalidade, gírias, humor ou oralidade.
- Coerência obrigatória entre objetivos, blocos, atividades, desafios e produto final.
- **BreadCrumb obrigatório** para toda navegação em interface: `Aplicativo > Menu > Submenu > Opção`. Usar BreadCrumb também em instruções de complexidade média ou alta — sempre que a sequência de passos puder gerar dúvida de navegação, mesmo fora de menus formais. Não indicar capturas de tela como recurso de orientação.
- Cada atividade deve ter tempo estimado, procedimento numerado e critério de êxito objetivo.
- Cada desafio deve ter instrução objetiva e critério de validação claro.
- O trabalho de conclusão deve ter cenário, tarefa, procedimento sugerido, produto esperado e critérios de avaliação.
- Markdown limpo: cabeçalhos, listas, tabelas curtas, citações para boxes e separação entre atividades com `<div style="page-break-after: always;"></div>`.
- Não usar crases triplas para delimitar modelos editáveis; usar aspas triplas.
- Emojis permitidos apenas em cabeçalhos de atividade e boxes de destaque — nunca no corpo do texto.

---

# RESTRIÇÕES

- Não inventar funcionalidades da ferramenta ou da plataforma; se não estiver claro no material-fonte, indicar necessidade de validação.
- Não exceder a carga horária definida.
- Não criar atividades puramente teóricas.
- Não produzir plano de aula genérico; produzir roteiro instrucional para Rise 360.
- Não usar linguagem promocional ou conversacional.
- Não criar atividades sem critério objetivo de êxito.
- Não deixar atividades sem produto parcial e checkpoint.
- Não indicar capturas de tela como recurso de orientação — substituir sempre por BreadCrumb.
- Não fazer o trabalho de conclusão integrar os produtos das atividades anteriores — ele é uma tarefa nova e autônoma.
- Não ultrapassar o dobro do tempo de uma atividade individual no trabalho de conclusão.
- Não bloquear o avanço nos desafios de extensão — eles são sempre opcionais.
- Não transformar o Capítulo 0 em aula — ele é expositivo e informativo, sem atividade prática.

---

# FORMATO DE SAÍDA

Um único documento Markdown completo, do título ao encerramento, seguindo a estrutura obrigatória. O documento deve estar pronto para orientar a implementação no Articulate Rise 360, com lições, blocos tipados, atividades práticas, desafios de extensão, trabalho de conclusão, BreadCrumbs de navegação e critérios de validação.
