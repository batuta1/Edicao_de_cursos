# Relatório de alterações — Curso "Claude Cowork — Essentials"

## Arquivos editados

- licao_01_O_Paradigma_do_Coworking_com_IA.json
- licao_02_Base_de_Conhecimento_do_Projeto.json
- licao_03_Instruções_Customizadas_para_Projetos.json
- licao_04_Artefatos_Documentos_que_Evoluem.json
- licao_05_Síntese_e_Aplicação_Integrada.json

(`indice_licoes.json` foi apenas lido, não alterado.)

## Roteiro-fonte utilizado

Conforme a seção 9 do prompt de edição, o plano de aula original foi a referência principal:

- `Criacao de Cursos\Claude\Claude Cowork\essentials\Plano-de-Aula-Claude-Cowork-Essentials-Articulate360.md`
  — plano de aula completo, com os cinco módulos, objetivos de aprendizagem, textos descritivos,
  exercícios práticos, pontos de controle, critérios de êxito e modelos "Mão na massa".
- `Criacao de Cursos\Claude\Claude Cowork\curso_claude-cowork.md` — material-fonte extenso,
  usado para recuperar detalhes concretos que o plano de aula resume.

Mapeamento 1:1 confirmado: Lição 01 = Módulo 1; 02 = Módulo 2; 03 = Módulo 3; 04 = Módulo 4;
05 = Módulo 5.

**Critério aplicado:** o registro formal e impessoal do plano de aula foi preservado — este é
um curso "curto, introdutório e autoinstrucional" para docentes, com linguagem deliberadamente
mais técnica que a do Hands-on. As melhorias eliminaram vagueza e repetição sem coloquializar o
texto. Todo conteúdo marcado como *verbatim* no plano (modelos "Mão na massa" entre aspas
triplas, breadcrumbs `🧭`, pontos de controle, critérios de êxito, objetivos de aprendizagem e
a tabela de critérios de avaliação) foi mantido sem alteração.

## Alterações realizadas

### Lição 01 — O Paradigma do Coworking com IA

- Abertura substituída: o texto gerado era um convite genérico ("Descubra como o Claude Cowork
  pode transformar…"). Foi trocado pela definição do plano de aula — o que é contexto persistente
  e por que ele torna o Projeto adequado a tarefas de múltiplas etapas.
- Lead-in dos objetivos deixou de parafrasear a lista que vem logo abaixo e passou a ser a
  fórmula do plano de aula: "Ao final deste módulo, você deverá ser capaz de:".
  *(A mesma correção foi aplicada nas cinco lições — a duplicação era sistemática.)*
- Flashcards Chat/Projeto aprofundados com o critério de uso de cada modalidade.
- Introdução do accordion Chat × Projeto: acrescentou a formulação do plano de aula — a escolha
  decorre da natureza da tarefa, não de preferência pessoal.
- Item "Quando utilizar Projeto" ganhou o teste rápido de decisão ("vou precisar revisar isto?"
  / "vou usar isto mais de uma vez?"), presente na matriz de decisão do material-fonte.
- Introdução dos princípios de comunicação reescrita para nomear os quatro princípios e sinalizar
  que a supervisão ativa é o fio condutor retomado no Módulo 5 — encadeamento explícito no plano
  de aula que se perdeu na geração.
- O segundo bloco de título ("Quatro Princípios…") repetia o parágrafo anterior; virou uma
  descrição do que cada aba traz.
- As 4 abas de princípios aprofundadas com contraste concreto: o par vago/específico de instrução,
  a ligação de "contexto" com a Base de Conhecimento (Módulo 2), a ligação de "feedback" com o
  Módulo 4 e a de "supervisão ativa" com o Módulo 5.
- As 4 alternativas de feedback do quiz reescritas (as originais tinham uma linha cada).
- Introdução e resumo do processo guiado passaram a situar o Projeto criado como o que será usado
  em todos os módulos seguintes, e a mapear as três seções da barra lateral para os módulos.

### Lição 02 — Base de Conhecimento do Projeto

- Abertura substituída pela definição do plano de aula, incluindo a analogia do colega
  recém-chegado à instituição e a expressão "memória de longo prazo".
- Flashcards aprofundados: o primeiro distingue Base de Conhecimento de arquivo anexado a uma
  conversa isolada; o segundo nomeia o sintoma da ausência de contexto (escola média, turma média,
  currículo médio).
- Introdução dos tipos de documento: acrescentou o critério de seleção do plano de aula —
  relevância direta, evitando material redundante ou de pertinência indireta.
- As 5 categorias de documento ganharam conteúdo concreto: exemplos nomeados (BNCC, currículo
  estadual), a saída para quem não tem guia de estilo formal, a observação de que exemplos de
  atividades anteriores costumam ser a categoria de maior efeito prático, e a recomendação de
  registrar necessidades de acessibilidade de forma agregada, sem identificar alunos.
- Boa prática nº 1 (nomeação) recebeu o segundo exemplo de arquivo e o critério de ordenação
  (do geral para o específico).
- Boa prática nº 3 dizia apenas "leve em consideração o limite prático de processamento de
  tokens", sem informar o limite. Agora traz o número do plano de aula: ~200 mil tokens por
  interação, cerca de 150 páginas, com a definição de "token".
- Bloco de destaque reescrito ("documentos bem escolhidos rendem mais do que documentos
  numerosos"), eliminando a exclamação motivacional.
- Introdução do processo guiado: marca que as duas últimas etapas são a verificação indispensável,
  não formalidade opcional — formulação do plano de aula.
- Passos "Submeter pergunta de síntese" e "Verificar referência": acrescentaram os critérios que
  tornam o teste válido (a pergunta precisa exigir mais de um arquivo; a resposta precisa citar
  conteúdo que só existe nos documentos).
- As 4 alternativas de feedback do quiz reescritas, cada uma nomeando qual critério falhou
  (pertinência, formato ou padronização).

### Lição 03 — Instruções Customizadas para Projetos

- Abertura substituída pela definição do plano de aula, explicitando as duas coisas que se
  deterioram sem o recurso: eficiência e consistência entre produtos.
- Flashcards: o primeiro ganhou o contraste Base de Conhecimento (o que sabe) × Instruções
  (como trabalha); o segundo explica por que a consistência deixa de depender da memória de
  quem faz o pedido.
- Introdução dos cinco elementos: acrescentou a consequência da ausência de qualquer um deles.
- Introdução das estratégias de redação passou a anunciar o que cada aba cobre.
- Aba "Especificidade": introduziu a pergunta de controle — depois de ler o resultado, dá para
  afirmar objetivamente se a instrução foi cumprida?
- Aba "Exemplos de frase": passou a explicar *por que* o exemplo funciona melhor que a descrição
  (padrão concreto a reproduzir em vez de regra abstrata a interpretar).
- Aba "Definição de limites": **acrescentou o tema das contradições**, que o título da seção
  anunciava ("instruções claras, específicas e sem contradições") mas nenhuma aba cobria. O
  conteúdo veio do plano de aula: instruções contraditórias se manifestam como hesitação ou
  ressalva na resposta da IA.
- Bloco de destaque reescrito com a informação mais útil: o ganho de tempo aparece a partir da
  segunda solicitação, não na primeira.
- Introdução e resumo do processo guiado reescritos; passo "Revisar e repetir" ganhou a operação
  concreta (substituir formulação abstrata por exemplo).
- As 4 alternativas de feedback do quiz reescritas, com a correta enumerando quais dos cinco
  elementos do módulo estão presentes na instrução.

### Lição 04 — Artefatos: Documentos que Evoluem

- Abertura substituída pela definição do plano de aula, com o problema concreto: após três ou
  quatro rodadas em Chat, não se identifica mais qual versão é a definitiva.
- Flashcards Artefato/Resposta em Chat aprofundados em contraste direto.
- Introdução dos tipos de Artefato: acrescentou que a escolha do formato precisa constar da
  própria solicitação.
- Introdução do accordion de solicitação: nomeia os três elementos exigidos (formato, conteúdo
  mínimo, público), que o plano de aula lista e a geração havia deixado implícitos.
- Bloco de destaque reescrito sem exclamação e com a relação custo/benefício explícita.
- Introdução do processo guiado: deixa claro que o ponto central do exercício é a revisão, não
  a geração.
- Resumo do processo guiado: liga o ciclo praticado aqui com a aplicação em escala maior no
  Módulo 5.
- As 4 alternativas de feedback do quiz reescritas em torno do padrão de três partes do feedback
  localizado.

### Lição 05 — Síntese e Aplicação Integrada

- Abertura substituída pelo texto descritivo do plano de aula: os quatro componentes não operam
  de forma independente, e a qualidade do Artefato decorre dos Módulos 2 e 3.
- Os 4 flashcards de componentes tinham definições curtas e intercambiáveis; foram reescritos
  para mostrar a dependência entre eles (o Projeto sustenta os outros três; a Base determina o
  teto de pertinência; as Instruções respondem pela consistência; o Artefato é o único que sai
  do Claude).
- Introdução das fases do fluxo: acrescentou que saltar uma fase se manifesta como retrabalho
  na seguinte.
- Fase "Consolidação do produto final": recuperou do plano de aula a menção ao limite de
  processamento do Módulo 2, relevante quando vários Artefatos são consolidados.
- Aba "Estruturação de solicitações complexas": passou a nomear os quatro elementos da estrutura
  de prompt (contexto, tarefa específica, detalhes/restrições, forma de entrega), conforme o
  plano de aula.
- Introdução e resumo do processo guiado reescritos, marcando que nenhum componente novo é
  introduzido e que o Projeto passa a ser reaproveitável.
- Introdução dos critérios objetivos passou a remeter diretamente à tabela de avaliação.
- As 4 alternativas de feedback do quiz reescritas — ver Pontos de atenção, item 1.
- Encerramento reescrito a partir da seção "Encerramento" e da "Síntese" do plano de aula,
  substituindo o "Parabéns por concluir esta jornada!" e o apelo genérico a "uma educação mais
  inovadora".

## Campos textuais alterados

Apenas `paragraph`, `description` e `feedback`, dentro de blocos `text`, `interactive`
(flashcard, accordion, tabs, `interactive-fullscreen` dos tipos `intro`/`summary`/`step`) e
`knowledgeCheck`.

Contagem verificada por script: **99 campos alterados** de 355 campos textuais existentes nas
5 lições — `description` = 41, `paragraph` = 38, `feedback` = 20.

**Nenhum campo `title` foi alterado** (0 de todos os títulos de lição, blocos, passos, abas,
itens de accordion e alternativas de quiz).

## Validação estrutural

Validação automatizada comparando cada lição editada contra a lição correspondente no arquivo
original `cursoClaudeCoworkEssentials.json` (mesmo `lesson.id`). A comparação percorreu toda a
árvore JSON e conferiu, em cada nível: o conjunto exato de chaves, o comprimento de cada array
e o valor de todos os campos protegidos.

Resultado: **0 divergências estruturais nos 5 arquivos.**

- Nenhum `id`, `courseId`, `author`, `globalBlockId` ou `itemId` alterado.
- Nenhum `type`, `family` ou `variant` alterado.
- Nenhuma `position` alterada (0 a 4, na ordem original).
- Nenhum `settings`, `metadata`, `createdAt`, `updatedAt` ou `experiments` alterado.
- Contagem de blocos idêntica à original: L01=19, L02=20, L03=18, L04=18, L05=20.
- `globalBlockId` únicos e em igual número aos blocos em todas as lições — nenhum bloco
  adicionado, removido ou duplicado.
- Os 5 valores `correct` (um quiz por lição) conferidos: mesma alternativa marcada como `true`,
  na mesma ordem e com o mesmo texto de alternativa.
- 5 lições antes e 5 depois, com os mesmos IDs.
- Todos os arquivos válidos como JSON e em UTF-8 sem BOM.
- Edições feitas por substituição pontual de string (ferramenta Edit), não por reescrita de
  arquivo — indentação e formatação originais preservadas.

## Pontos de atenção

1. **Lição 05 — quiz com pressupostos não enunciados (feedbacks reescritos, alternativas
   mantidas).** A pergunta é "Qual critério NÃO foi plenamente atendido ao revisar um Artefato
   que alterou mais do que o trecho indicado?". Os feedbacks originais das três alternativas
   incorretas afirmavam fatos que o enunciado não fornece — por exemplo, "O Artefato utiliza
   corretamente as informações da Base de Conhecimento, portanto este critério foi atendido".
   Como o enunciado nada diz sobre isso, a justificativa era infundada. Os feedbacks foram
   reescritos para explicar por eliminação (o critério em questão trata de outro aspecto),
   sem afirmar o que não foi dado. **A resposta correta e as alternativas não foram alteradas.**
   Se houver revisão editorial futura, vale reescrever o enunciado para explicitar que os demais
   critérios foram atendidos.

2. **Lição 02 — alternativa D do quiz é internamente contraditória (não alterada).** O texto da
   alternativa é "01_Curriculo.pdf, 02_Acessibilidade.pdf e 03_Atividades_Passadas.docx, todos em
   uma única pasta **sem nomeação padronizada**" — mas os três nomes citados *estão* padronizados
   com prefixo numérico. A alternativa contradiz a si mesma. Por ser texto de alternativa de
   quiz, foi mantida sem alteração, conforme a regra do prompt; o feedback foi redigido de modo
   a se apoiar na condição declarada ("a alternativa descarta a padronização") e não nos nomes
   de arquivo. **Recomenda-se revisão humana do texto desta alternativa.**

3. **Nenhuma resposta correta de `knowledgeCheck` estava errada.** As 5 questões foram conferidas
   e a alternativa marcada como correta é coerente com o conteúdo do módulo em todas.

4. **Registro formal preservado deliberadamente.** O plano de aula deste curso adota linguagem
   marcadamente formal ("cumpre entendê-la como", "constitui etapa indispensável"). As reescritas
   mantiveram esse registro, diferente do tom coloquial usado no curso Hands-on. Se a decisão
   editorial for aproximar os dois cursos, isso exige uma passagem específica — não foi feito aqui
   para não descaracterizar a identidade do Essentials.

5. **Repetição sistemática corrigida em todas as lições.** Nos cinco arquivos, o parágrafo que
   antecede a lista de objetivos parafraseava a própria lista ("Ao final, você será capaz de
   diferenciar, solicitar e revisar Artefatos…" seguido da lista com esses mesmos itens). Isso foi
   substituído pela fórmula do plano de aula. Vale conferir se a leitura na plataforma continua
   fluida com o parágrafo mais curto.

## Confirmação

A estrutura técnica dos 5 arquivos JSON foi integralmente preservada, com verificação
automatizada campo a campo contra o curso original. Apenas campos textuais pedagógicos
permitidos (`paragraph`, `description`, `feedback`) foram alterados, conforme as regras do
prompt de edição.
