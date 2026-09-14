# Relatório de alterações — Curso "Claude Cowork — Hands-on"

## Arquivos editados

- licao_01_Chat_vs._Projeto_Colocando_seu_Parceiro_de_Trabalho_em_Pé.json
- licao_02_Montando_a_Base_de_Conhecimento_Dando_Contexto_ao_Claude.json
- licao_03_Escrevendo_Instruções_Customizadas_Padronizando_a_Comunicação_da_IA.json
- licao_04_Criando_e_Ajustando_Artefatos_Pedagógicos_no_Claude.json
- licao_05_Integração_e_Finalização_Seu_Mini_Produto_Pedagógico_Completo.json
- licao_06_Boas_Práticas_e_Solução_de_Problemas_no_Uso_do_Claude.json

(`indice_licoes.json` foi apenas lido, não alterado.)

## Roteiro-fonte utilizado

Diferente de outros cursos deste projeto, aqui **existe roteiro-fonte** e ele foi usado como
referência principal, conforme a seção 9 do prompt de edição:

- `Criacao de Cursos\Claude\Claude Cowork\hands-on\Roteiro-Hands-on-Claude-Cowork-Articulate360.md`
  — roteiro direto do curso (Oficinas 1 a 4, Projeto Final, "A Parte dos Dez" e encerramento).
- `Criacao de Cursos\Claude\Claude Cowork\curso_claude-cowork.md` — material-fonte extenso
  (Módulos 1 a 7), usado para recuperar detalhes concretos que o roteiro resume.

Mapeamento confirmado: Lição 01 = Oficina 1; 02 = Oficina 2; 03 = Oficina 3; 04 = Oficina 4;
05 = Projeto Final; 06 = "A Parte dos Dez" + "Conseguiu! E agora?".

**Critério aplicado:** todo texto marcado no roteiro como *verbatim* (prompts entre aspas
triplas, breadcrumbs `🧭`, tabelas de "Se travar", itens `[OPCIONAL]`, checklist final,
os 10 hábitos e os blocos de destaque `impact`) foi mantido sem alteração. As melhorias
concentraram-se nos textos de ligação, introduções, resumos e feedbacks de quiz — que foram
gerados pela IA e não constam do roteiro.

## Alterações realizadas

### Lição 01 — Chat vs. Projeto

- Abertura reescrita: trocou a pergunta motivacional genérica ("Já pensou em ter uma IA que
  realmente entende o seu jeito de ensinar…") pelo problema concreto que o roteiro-fonte usa —
  ter que reexplicar tudo no dia seguinte porque o Chat não guarda memória.
- Lead-in da lista de tópicos deixou de repetir "principais conceitos e práticas" e passou a
  anunciar o que a lista realmente cobre.
- Introdução dos flashcards: acrescentou o ponto que faltava — a diferença entre Chat e Projeto
  não é de capacidade do modelo, é de memória disponível no momento do pedido.
- Os dois flashcards ganharam o critério de decisão (quando cada modalidade compensa), que
  antes ficava só implícito.
- Introdução do processo guiado: passou a antecipar as 3 partes, o tempo e o pré-requisito de
  plano (Pro, Max, Team ou Enterprise — o gratuito não habilita Projects), informação que estava
  no roteiro-fonte mas se perdeu na geração.
- Resumo do processo guiado: substituiu "Está pronto para avançar!" por uma ligação explícita
  entre as três seções da barra lateral e as oficinas seguintes.
- As 4 alternativas de feedback do quiz (nome de Projeto) reescritas para explicar *por que*
  cada nome funciona ou não, conectando com a dica da própria lição (nome descreve o resultado,
  não o processo).
- Fechamento: em vez de anunciar genericamente a próxima lição, nomeia o estado atual do Projeto
  (criado, porém vazio) e o que a Base de Conhecimento vai resolver.

### Lição 02 — Base de Conhecimento

- Abertura reescrita com a analogia do roteiro-fonte (colega novo na escola) e o custo concreto
  de não ter contexto: corrigir as mesmas coisas em toda conversa.
- Flashcards aprofundados: o primeiro passou a dizer o que entra na Base; o segundo descreve o
  sintoma real da falta de contexto (resposta correta mas genérica, que varia a cada pedido).
- Passo "Preparando seus documentos": recuperou detalhes do roteiro-fonte que a geração havia
  suprimido — meia página, editor de texto (Bloco de Notas/Word/Google Docs) e os formatos
  PDF/DOCX/TXT.
- Passo "Nomeando os arquivos": explica agora *para que serve* o prefixo numérico (ordem de
  leitura, do geral para o específico), em vez de só mandar numerar.
- Passo "Fazendo upload": acrescentou a ordem de grandeza do tempo de carregamento.
- Passo "Validando o upload": alerta de que arquivo em processamento ainda não é utilizável.
- Passo "Testando a compreensão": manteve o prompt verbatim e acrescentou o critério de leitura
  da resposta — se o resumo serviria para qualquer documento, o upload não terminou.
- As 4 alternativas de feedback do quiz reescritas com o motivo real de cada opção (incluindo o
  ponto de que tamanho de arquivo não é qualidade).
- Resumo do processo e fechamento reescritos para nomear o que muda a partir dali.

### Lição 03 — Instruções Customizadas

- Abertura reescrita para não repetir o bloco de destaque que aparece logo abaixo (que é verbatim
  do roteiro): agora parte do sintoma de inconsistência entre três pedidos feitos em conversas
  diferentes.
- Flashcards: o primeiro ganhou o contraste Base de Conhecimento (o que sabe) × Instruções
  (como trabalha); o segundo passou a mostrar o par vago/específico com alvo verificável.
- Introdução do processo guiado: anuncia as 6 etapas e destaca que o ajuste final é a parte de
  maior valor.
- Passo "Preencha os quatro blocos": lead-in melhorado; o modelo dentro de `<pre>` permaneceu
  intacto.
- Passo "Analise a resposta": virou uma checagem de três itens (tom, estrutura, restrições), no
  mesmo padrão do critério de avaliação usado no curso Essentials.
- Passo "Ajuste se necessário": dá a operação concreta — trocar a descrição abstrata por um
  exemplo de frase.
- Item do acordeão "O resultado ignorou uma das minhas instruções": restaurado o exemplo
  `("seja claro")` presente no roteiro-fonte e omitido na geração.
- As 4 alternativas de feedback do quiz reescritas em torno de um único critério: dá para
  verificar objetivamente se a instrução foi cumprida?

### Lição 04 — Artefatos

- Abertura reescrita com a cena concreta do roteiro-fonte (respostas empilhadas no chat até não
  se saber qual é a versão boa), substituindo o parágrafo motivacional sobre "uma das maiores
  conquistas para qualquer educador".
- Flashcards: o de Artefato passou a explicar a consequência prática (versão única, que é a
  exportada); o de feedback explica por que o feedback vago provoca reescrita total.
- Introdução do processo guiado: nomeia o ciclo pedir → revisar → apontar.
- Passo "Revisando o Conteúdo": orienta a anotar observações localizadas em vez de julgar o
  material como um todo.
- Passo "Validando a Alteração": aponta a causa mais comum de reescrita total (localização vaga)
  e remete à seção de soluções.
- Passo "Iterando": acrescentou dois critérios práticos — um problema por rodada e parar em
  "utilizável", não em "perfeito".
- As 4 alternativas de feedback do quiz reescritas nomeando os três elementos do padrão
  (local + problema + solução esperada).

### Lição 05 — Projeto Final

- Abertura reescrita a partir da "Missão" do roteiro-fonte, incluindo o ponto que a geração
  havia perdido: aqui o participante decide sozinho o que pedir.
- **Correção conceitual** no flashcard "Mini produto pedagógico completo" — ver Pontos de atenção.
- Flashcard sobre revisão reescrito em torno da supervisão ativa (a responsabilidade permanece
  do participante), em vez de afirmações genéricas sobre "evitar retrabalho".
- Bloco de destaque "Confira se seu projeto está realmente pronto" substituído pelos 5 itens
  concretos do checklist "Como saber que terminou" do roteiro-fonte, que não haviam sido
  aproveitados na geração.
- Passos "Retome seu Projeto" e "Confirme os Elementos Essenciais" ganharam o motivo da
  exigência (o pedido só funciona onde estão a Base e as Instruções).
- Passo "Revise Criticamente": trocou "olhar crítico" por perguntas concretas de quem vai
  aplicar o material.
- Passo "Exporte o Produto Final": acrescentou o caminho `Artifact > Download (ou Copy)` e a
  recomendação de abrir o arquivo fora do Claude para conferir formatação.
- Critério de qualidade "Personalização do conteúdo": o teste anterior ("seu produto poderia ser
  reconhecido como 'seu' por outro professor?") era ambíguo; virou um teste verificável —
  apontar dois trechos que só existem porque o Claude conhecia o contexto.
- As 4 alternativas de feedback do quiz reescritas, incluindo a distinção entre Projeto
  (estrutura) e Artefato (produto).

### Lição 06 — Boas Práticas e Solução de Problemas

- Abertura reescrita: nomeia o que a lição realmente entrega (hábitos + destravamento autônomo)
  em vez de repetir a promessa de "eficiência, segurança e sustentabilidade".
- Flashcard "Boas práticas no Claude" tinha definição circular ("hábitos e rotinas que tornam o
  uso mais eficiente"); passou a listar decisões concretas anteriores ao pedido.
- Os outros dois flashcards ganharam a consequência prática (custo da primeira montagem × custo
  das seguintes; uma rodada de ajuste × cinco).
- Introdução do processo de organização/reaproveitamento: acrescentou o *quando* fazer — enquanto
  o Projeto ainda está fresco.
- Passo "Registre feedbacks e melhorias" aprofundado com uma regra acionável: correção repetida
  três vezes é instrução faltando, não ajuste a repetir.
- Item "Artefato não reflete mudanças" corrigido — ver Pontos de atenção.
- Item "Por que evitar dados de alunos?" ganhou a regra prática (se o material funciona sem o
  dado, o dado não vai) e o exemplo do "Aluno A".
- As 4 alternativas de feedback do quiz reescritas.
- Fechamento reescrito a partir de "Conseguiu! E agora?" do roteiro-fonte, eliminando o
  "o futuro da educação digital está em suas mãos!".

## Campos textuais alterados

Apenas `paragraph`, `description` e `feedback`, dentro de blocos `text`, `interactive`
(flashcard, accordion, `interactive-fullscreen` dos tipos `intro`/`summary`/`step`) e
`knowledgeCheck`.

Contagem verificada por script: **107 campos alterados** de 385 campos textuais existentes
nas 6 lições — `description` = 45, `paragraph` = 38, `feedback` = 24.

**Nenhum campo `title` foi alterado** (0 de todos os títulos de lição, blocos, passos,
itens de accordion e alternativas de quiz).

## Validação estrutural

Validação automatizada comparando cada lição editada contra a lição correspondente no arquivo
original `cursoClaudeCoworkHandsOn.json` (mesmo `lesson.id`). A comparação percorreu toda a
árvore JSON e conferiu, em cada nível: o conjunto exato de chaves, o comprimento de cada array
e o valor de todos os campos protegidos.

Resultado: **0 divergências estruturais nos 6 arquivos.**

- Nenhum `id`, `courseId`, `author`, `globalBlockId` ou `itemId` alterado.
- Nenhum `type`, `family` ou `variant` alterado.
- Nenhuma `position` alterada (0 a 5, na ordem original).
- Nenhum `settings`, `metadata`, `createdAt`, `updatedAt` ou `experiments` alterado.
- Contagem de blocos idêntica à original: L01=16, L02=15, L03=16, L04=15, L05=14, L06=16.
- `globalBlockId` únicos e em igual número aos blocos em todas as lições — nenhum bloco
  adicionado, removido ou duplicado.
- Os 6 valores `correct` (um quiz por lição) conferidos: mesma alternativa marcada como `true`,
  na mesma ordem e com o mesmo texto de alternativa.
- 6 lições antes e 6 depois, com os mesmos IDs.
- Todos os arquivos válidos como JSON e em UTF-8 sem BOM.
- Edições feitas por substituição pontual de string (ferramenta Edit), não por reescrita de
  arquivo — indentação e formatação originais preservadas.

## Pontos de atenção

1. **Correção conceitual aplicada — Lição 05, flashcard "Mini produto pedagógico completo".**
   O texto original afirmava que o mini produto "reúne em um único arquivo todos os elementos
   essenciais: base de conhecimento, instruções detalhadas para aplicação e o artefato pedagógico
   propriamente dito". Isso está incorreto e contradiz o restante do curso: Base de Conhecimento
   e Instruções Customizadas são componentes do Projeto no Claude, não seções do arquivo
   exportado. O texto foi corrigido para descrever o Artefato como ele realmente é (título,
   introdução, conteúdo principal e seção final), apoiado nos outros dois componentes.
   **Recomenda-se conferência humana** desta reescrita.

2. **Correção factual aplicada — Lição 06, item "Artefato não reflete mudanças".**
   O texto original orientava "sempre salve e revise o Artefato após cada ajuste". Artefatos no
   Claude não têm ação de "salvar" pelo usuário — a edição é aplicada pelo próprio modelo. A
   orientação foi trocada por duas verificações reais: conferir se está aberta a versão mais
   recente e, se a alteração de fato não ocorreu, repetir o pedido citando uma frase exata do
   trecho. **Vale confirmar o comportamento atual do produto antes de publicar.**

3. **Nenhuma resposta correta de `knowledgeCheck` estava errada.** As 6 questões foram conferidas
   e a alternativa marcada como correta é coerente com o conteúdo da lição em todas.

4. **Conteúdo verbatim preservado deliberadamente.** Os prompts entre aspas triplas, os
   breadcrumbs com `🧭`, as tabelas de "Se travar", os itens `[OPCIONAL]`, os 10 hábitos e todos
   os blocos `impact` marcados como *Statement* no roteiro-fonte foram mantidos palavra por
   palavra. Se houver intenção de revisá-los, isso deve ser feito no roteiro-fonte primeiro,
   para não dessincronizar os dois materiais.

5. **Lição 06 não tem correspondência 1:1 no roteiro-fonte.** Ela combina "A Parte dos Dez" com
   o encerramento "Conseguiu! E agora?", além de seções sobre organização de Projetos, problemas
   comuns e privacidade que foram geradas pela IA (o roteiro-fonte não traz esses três blocos).
   Esses trechos foram melhorados com base no material-fonte extenso (`curso_claude-cowork.md`,
   Módulos 6 e 7), mas **não têm respaldo direto no roteiro do Hands-on** — vale uma decisão
   editorial sobre mantê-los ou alinhá-los ao roteiro.

## Confirmação

A estrutura técnica dos 6 arquivos JSON foi integralmente preservada, com verificação
automatizada campo a campo contra o curso original. Apenas campos textuais pedagógicos
permitidos (`paragraph`, `description`, `feedback`) foram alterados, conforme as regras do
prompt de edição.
