# Relatório de alterações — Curso "Claude Chat — Essentials"

## Arquivos editados

- licao_01_Fundamentos_Por_Que_a_Continuidade_Não_é_Automática.json
- licao_02_Custom_Instructions_Ensinando_o_Claude_a_Reconhecer_Você.json
- licao_03_Chat_Search_Recuperando_Conversas_Anteriores.json
- licao_04_Memory_A_Memória_Automática_do_Claude.json
- licao_05_Projects_Isolando_o_Contexto_por_Frente_de_Trabalho.json
- licao_06_Síntese_e_Aplicação_Integrada_dos_Mecanismos_de_Continuidade.json

(`indice_licoes.json` foi apenas lido, não alterado.)

## Roteiro-fonte utilizado

Conforme a seção 9 do prompt de edição, o plano de aula original foi a referência principal:

- `Criacao de Cursos\Claude\Claude Chat\essentials\Plano-de-Aula-Claude-Chat-Essentials-Articulate360.md`
  — plano de aula completo, com os seis módulos, objetivos de aprendizagem, texto descritivo,
  exercício prático, ponto de controle, critério de êxito e modelo "Mão na massa" de cada um.
- `Criacao de Cursos\Claude\Claude Chat\curso_claude_chat.md` — material-fonte extenso (Módulos
  1 a 10), usado para recuperar detalhes, analogias e exemplos concretos que o plano de aula
  resume (em especial os Módulos 1 a 4 e 6, únicos referenciados pela tabela de correspondência
  do próprio plano de aula).

Mapeamento 1:1 confirmado por título — Lição 01 = Módulo 1; 02 = Módulo 2; 03 = Módulo 3;
04 = Módulo 4; 05 = Módulo 5 (que remete a "curso_claude_chat.md — Módulo 6"); 06 = Módulo 6.

**Critério aplicado:** o registro didático e claro do plano de aula foi preservado. As melhorias
se concentraram em três padrões recorrentes identificados nas seis lições: (1) parágrafos de
abertura com linguagem genérica de efeito, sem ancoragem no conteúdo específico do módulo; (2)
textos de ligação que parafraseavam a lista de objetivos, em vez de usar a fórmula padrão do
plano de aula ("Ao final deste módulo, o participante deverá ser capaz de:"); (3) fechamentos de
lição com apelo motivacional genérico, no lugar de antecipar concretamente o conteúdo seguinte.
Blocos já alinhados ao plano de aula — accordions, tabs, flashcards e exercícios guiados, em
geral de boa qualidade e com exemplos concretos — foram preservados sem alteração.

## Alterações realizadas

### Lição 01 — Fundamentos: Por Que a Continuidade Não é Automática

- Abertura substituída: o texto gerado era genérico ("é fundamental para usar a ferramenta de
  forma eficiente e segura"). Foi trocado pela formulação do plano de aula — cada chat novo é
  uma instância isolada por escolha arquitetural, não por falha — que também é a premissa da
  lição inteira.
- Lead-in dos objetivos deixou de parafrasear a lista logo abaixo e passou a usar a fórmula
  padrão do curso ("Ao final desta lição, você será capaz de:").
- Parágrafo de transição para os quatro mecanismos reescrito para incorporar a analogia do
  material-fonte — "um colega que, a cada novo encontro, lê um resumo executivo sobre você, em
  vez de alguém que viveu o histórico de trabalho ao seu lado" —, ausente da geração original.
- Bloco de destaque corrigido: o texto gerado trazia uma formulação truncada e sem sentido
  gramatical ("Não, Claude, a continuidade é sempre uma escolha ativa..."), aparentemente um
  resíduo de geração. Substituído pela síntese do plano de aula, sem o resíduo.

### Lição 02 — Custom Instructions: Ensinando o Claude a Reconhecer Você

- Abertura reescrita para nomear o diferencial concreto das Custom Instructions frente aos
  outros três mecanismos — não sofre o intervalo de atualização da Memory (Módulo 4) nem depende
  de busca ativa como o Chat Search (Módulo 3) —, com referência cruzada aos módulos
  correspondentes.
- Lead-in corrigido: o texto gerado dizia "siga as etapas abaixo", mas a lista que vem a seguir
  enumera objetivos de aprendizagem, não etapas de um processo — um descompasso entre o texto de
  ligação e o conteúdo real da lista. Substituído pela fórmula padrão do curso.
- Demais blocos (accordions, tabs com exemplo eficaz/genérico, flashcards, dicas, quiz) já
  apresentavam exemplos concretos alinhados ao plano de aula e não foram alterados.

### Lição 03 — Chat Search: Recuperando Conversas Anteriores

- Abertura substituída: o texto gerado usava linguagem genérica ("é essencial para
  profissionais", "otimizando o fluxo de trabalho"). Foi trocada pelo problema concreto que
  justifica a existência do recurso — não lembrar em qual conversa, entre dezenas, um assunto
  foi discutido — e pela característica central do Chat Search (busca por ideia, não por palavra
  exata), retomada em detalhe nos blocos seguintes.
- Lead-in dos objetivos normalizado para a fórmula padrão do curso.
- **Alternativa de quiz corrigida** (ver Pontos de atenção, item 1): a alternativa correta do
  quiz continha o texto "A e C estão corretas", mas nenhuma das quatro alternativas exibe
  rótulos A/B/C/D na interface — a referência é indecifrável para quem responde. Reescrita para
  ser autocontida ("As duas situações anteriores justificam iniciar uma nova conversa"), sem
  alterar qual alternativa é a correta, a quantidade de alternativas, a ordem ou os IDs.

### Lição 04 — Memory: A Memória Automática do Claude

- Abertura reescrita para abrir com a distinção estrutural entre Memory e Custom Instructions
  (Módulo 2) — automática e inferida versus redigida diretamente —, antecipando os dois temas
  que a lição desenvolve: a defasagem de atualização e os cuidados de privacidade.
- Lead-in corrigido: o texto gerado prometia "identificar, ativar e utilizar a Memory de forma
  seguro e eficaz", três verbos que não correspondem aos quatro itens da lista logo abaixo
  (diferenciar, ativar e auditar, selecionar informações, revisar e corrigir). Substituído pela
  fórmula padrão do curso.
- Demais blocos (accordions, tabs de boas práticas, flashcards, exercício guiado, quiz) já
  traziam o detalhe concreto do intervalo de 24 a 48 horas e as categorias de dado sensível, e
  não foram alterados.

### Lição 05 — Projects: Isolando o Contexto por Frente de Trabalho

- Abertura reescrita para partir da distinção de escopo que justifica a existência de Projects —
  Custom Instructions (Módulo 2) e Memory (Módulo 4) são globais, um Project é isolado —, com o
  exemplo concreto do plano de aula (currículo em elaboração x consultoria em andamento).
- Lead-in dos objetivos normalizado para a fórmula padrão do curso.
- Fechamento da lição reescrito: trocado o genérico "potencializando ainda mais a sua
  produtividade" pela formulação do plano de aula que abre o Módulo 6 — os quatro mecanismos são
  camadas complementares de um mesmo sistema, não alternativas concorrentes —, preparando
  corretamente a transição para a lição de síntese.

### Lição 06 — Síntese e Aplicação Integrada dos Mecanismos de Continuidade

- Abertura substituída pela formulação central do plano de aula para este módulo de encerramento
  — os quatro mecanismos são camadas complementares, cada um com uma função específica (Custom
  Instructions/identidade, Memory/reforço automático, Chat Search/recuperação ativa,
  Projects/isolamento) —, no lugar do genérico "potencializa sua produtividade profissional".
- Lead-in dos objetivos normalizado para a fórmula padrão do curso.
- O fechamento da lição (bloco de síntese final e convite à trilha prática) já reproduzia,
  quase literalmente, o texto de encerramento do plano de aula e não foi alterado.

## Campos textuais alterados

Principalmente `paragraph`, dentro de blocos `text` (variantes `heading paragraph` e
`paragraph`) e `impact`. **Uma exceção pontual e documentada**: o campo `title` de uma
alternativa de quiz na Lição 03, justificada no item 1 de "Pontos de atenção".

Contagem verificada por script (comparação campo a campo contra
`cursoClaudeChatEssentials.json`): **16 campos alterados** nas 6 lições — `paragraph` = 15,
`title` (alternativa de quiz) = 1.

**Nenhum campo `heading`, `label` ou `title` de lição/bloco/aba/item foi alterado**, com exceção
da única alternativa de quiz documentada acima — mesma linha editorial já aplicada às demais
pastas deste projeto.

A grande maioria dos blocos gerados nesta pasta (accordions, tabs, flashcards, exercícios
guiados com breadcrumbs, exemplos "eficaz vs. genérico") já estava bem alinhada ao plano de aula
e não precisou de alteração — diferente de outras pastas do projeto, aqui a revisão concentrou-se
sobretudo nos parágrafos de abertura e nos textos de ligação antes de cada lista de objetivos.

## Validação estrutural

Validação automatizada (script Python) comparando cada lição editada contra a lição
correspondente em `cursoClaudeChatEssentials.json` (mesmo `lesson.id`), percorrendo
recursivamente toda a árvore JSON e conferindo, em cada nível, o conjunto exato de chaves, o
comprimento de cada array e o valor de todo campo não pertencente à lista de campos textuais
permitidos.

Resultado: **0 divergências estruturais não documentadas nos 6 arquivos** (a única alteração
fora de `paragraph`/`description`/`feedback` — o `title` da alternativa de quiz da Lição 03 — foi
sinalizada pelo próprio script e está documentada e justificada acima).

- Nenhum `id`, `courseId`, `author`, `globalBlockId` ou `itemId` alterado.
- Nenhum `type`, `family` ou `variant` alterado.
- Nenhuma `position` alterada (0 a 5, na ordem original).
- Nenhum `settings`, `metadata`, `createdAt`, `updatedAt` ou `experiments` alterado.
- Contagem de blocos idêntica à original: L01 = 21, L02 = 16, L03 = 18, L04 = 19, L05 = 17,
  L06 = 18 itens.
- 6 quizzes (`knowledgeCheck`), um por lição, conferidos: mesma alternativa marcada como
  `correct`, na mesma ordem, em todos — inclusive na Lição 03, onde apenas o texto de uma
  alternativa (não seu status de correção) foi reescrito.
- 6 lições antes e 6 depois, com os mesmos IDs e o mesmo `courseId`.
- Todos os arquivos válidos como JSON, em UTF-8 sem BOM.
- Edições feitas por substituição pontual de string (ferramenta Edit), não por reescrita de
  arquivo — indentação e formatação originais preservadas.

## Pontos de atenção

1. **Alternativa de quiz corrigida — Lição 03, pergunta sobre quando iniciar uma nova
   conversa.** A alternativa marcada como correta trazia o texto "A e C estão corretas.", mas as
   quatro alternativas do quiz, como renderizadas no JSON (e presumivelmente na plataforma), não
   exibem nenhum rótulo A/B/C/D — são apenas quatro textos em sequência. Um participante veria
   "A e C estão corretas" sem qualquer forma de saber a que "A" e "C" se referem. Reescrita para
   "As duas situações anteriores justificam iniciar uma nova conversa", frase autocontida que
   preserva o mesmo sentido (a combinação das duas primeiras alternativas listadas). **Não foi
   alterado:** qual alternativa está marcada como `correct`, a quantidade de alternativas (4), a
   ordem ou os IDs. Os feedbacks das quatro alternativas já eram autocontidos e não precisaram de
   ajuste. **Recomenda-se conferência humana** desta reescrita, e — se a plataforma Rise 360
   rotular as alternativas com letras automaticamente na renderização final — vale confirmar que
   a nova redação continua fazendo sentido nesse contexto.

2. **Padrão sistemático nas seis lições: descompasso entre o texto de ligação e a lista de
   objetivos.** Em quatro das seis lições (01, 02, 04, 06), o parágrafo que antecede a lista de
   objetivos ou parafraseava a lista de forma imprecisa, ou prometia verbos (ex.: "identificar,
   ativar e utilizar... de forma segura e eficaz") que não correspondiam aos itens efetivamente
   listados logo abaixo. Em todos os casos, a correção seguiu a fórmula literal do plano de aula
   ("Ao final deste módulo, o participante deverá ser capaz de:"), já usada sem alteração nas
   Lições 03 e 05 desde a geração original.

3. **Nenhuma resposta correta de `knowledgeCheck` estava conceitualmente errada.** As 6 questões
   foram conferidas e a alternativa marcada como correta é coerente com o conteúdo do módulo em
   todas — inclusive a Lição 03, onde apenas a redação da alternativa (não sua correção) exigiu
   ajuste, conforme item 1 acima.

4. **Qualidade heterogênea entre lições, refletida no volume de edição.** As Lições 02 e 04
   receberam apenas 2 alterações cada, por já apresentarem exemplos concretos, comparações
   "eficaz vs. genérico" e detalhes numéricos (como o intervalo de 24 a 48 horas da Memory)
   alinhados ao material-fonte. As demais lições exigiram mais ajustes nos parágrafos de
   abertura e fechamento, mas os blocos interativos (accordions, tabs, flashcards, exercícios
   guiados) estavam consistentemente bem construídos em todas as seis lições.

## Confirmação

A estrutura técnica dos 6 arquivos JSON foi integralmente preservada, com verificação
automatizada campo a campo contra o curso original (`cursoClaudeChatEssentials.json`). Os
campos textuais pedagógicos alterados foram, em 15 dos 16 casos, exclusivamente `paragraph`; a
única exceção (`title` de uma alternativa de quiz na Lição 03) está documentada, justificada e
não altera a resposta correta, a quantidade de alternativas ou a estrutura da interação, conforme
as regras do prompt de edição.
