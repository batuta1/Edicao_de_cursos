# Relatório de alterações — Curso "Claude Chat — Hands-on"

## Arquivos editados

- licao_01_Configurando_Perfil_e_Busca_Inteligente_no_Claude_Chat.json
- licao_02_Utilizando_a_Memória_e_Separando_Projetos_no_Claude.json
- licao_03_Integrando_Perfil,_Memória,_Busca_e_Projetos_Sistema_Pessoal_de_Continuidade.json

(`indice_licoes.json` foi apenas lido, não alterado.)

## Roteiro-fonte utilizado

Existe roteiro-fonte e ele foi usado como referência principal, conforme a seção 9 do prompt
de edição:

- `Criacao de Cursos\Claude\Claude Chat\hands-on\Roteiro-Hands-on-Claude-Chat-Articulate360.md`
  — roteiro direto do curso (Oficinas 1 a 4, Projeto Final, "A Parte dos Dez" e "Conseguiu! E
  agora?").
- `Criacao de Cursos\Claude\Claude Chat\curso_claude_chat.md` — material-fonte extenso (Módulos
  1 a 10), usado para recuperar detalhes conceituais que o roteiro resume (em especial os
  Módulos 2 a 4 e 6, sobre Custom Instructions, Chat Search, Memory e Projects).

**Mapeamento — este curso condensa 6 seções do roteiro em apenas 3 lições** (diferente do
Essentials, que mapeia 1:1):

| Lição | Título | Seções do roteiro combinadas |
|---|---|---|
| 01 | Configurando Perfil e Busca Inteligente | Oficina 1 (Custom Instructions) + Oficina 2 (Chat Search) |
| 02 | Utilizando a Memória e Separando Projetos | Oficina 3 (Memory) + Oficina 4 (Projects) |
| 03 | Integrando Perfil, Memória, Busca e Projetos | Projeto Final + "A Parte dos Dez" + "Conseguiu! E agora?" |

**Critério aplicado:** todo texto marcado no roteiro como *verbatim* (prompts entre aspas
triplas, breadcrumbs `🧭`, tabelas de "Se travar", itens `[OPCIONAL]`, os dez hábitos de "A
Parte dos Dez" e os blocos de destaque `impact`) foi mantido sem alteração. As melhorias se
concentraram nas aberturas de lição, textos de ligação entre as duas oficinas de cada lição,
resumos de processo e feedbacks de quiz — conteúdo gerado pela IA e não constante do roteiro,
ou generalizado a ponto de perder informação presente na fonte.

## Alterações realizadas

### Lição 01 — Configurando Perfil e Busca Inteligente

- Abertura substituída: o texto gerado usava linguagem genérica de efeito ("verdadeiro parceiro
  de continuidade", "evitando frustrações"). Foi trocada pela imagem concreta do roteiro — todo
  chat novo é "uma folha em branco" — nomeando os dois desperdícios de tempo que a lição resolve
  (reexplicar contexto e procurar chats antigos).
- Lead-in da lista de objetivos deixou de parafrasear a lista logo abaixo e passou a usar a
  fórmula padrão do curso ("Ao final desta lição, você será capaz de:"), já empregada sem
  alterações nas Lições 02 e 03.
- Bloco de destaque "Regra de ouro" ajustado com a formulação mais concreta do roteiro-fonte —
  "não existe 'estragar o Claude para sempre'" — no lugar do genérico "Errar só significa tentar
  de novo!".
- Introdução da seção de Custom Instructions passou a explicitar a diferença com a Memory
  (tratada na Lição 02): permanente e carregada de imediato, em vez de aprendida aos poucos.
- Resumo do processo guiado (Custom Instructions) tornado verificável: descreve exatamente o que
  observar na resposta e onde confirmar que as instruções foram salvas.
- Feedbacks do quiz de Custom Instructions reescritos: o de acerto explica *por que* a resposta
  indica que o mecanismo está ativo; o de erro orienta a ação corretiva (voltar a Settings e
  confirmar o salvamento) em vez de apenas reafirmar o problema.
- Fechamento da lição reescrito para nomear concretamente o que vem a seguir — Memory e Projects
  — no lugar do genérico "personalizar ainda mais sua experiência".

### Lição 02 — Utilizando a Memória e Separando Projetos

- Abertura substituída: trocado o clichê "transformar o Claude em um assistente realmente
  inteligente" pelos dois problemas concretos do roteiro — informações que só aparecem aos
  poucos ao longo do tempo (Memory) e contextos que se misturam entre frentes de trabalho
  diferentes (Projects).
- Introdução da Memory incorporou a "pegadinha de tempo" citada no roteiro-fonte (a atualização
  leva de 24 a 48 horas), informação que antes só aparecia isolada nos passos do exercício.
- **Conteúdo restaurado** no bloco de destaque "Cuidado": a frase final do roteiro-fonte —
  "Prefira sempre descrições genéricas ('uma turma com alunos de ritmos diferentes') a
  informações que identifiquem alguém" — estava ausente na versão gerada, que continha apenas a
  lista de proibições. Restaurada por ser orientação de segurança/privacidade relevante e
  presente no material-fonte.
- Fechamento da lição reescrito para anunciar concretamente a lição final (integração dos quatro
  mecanismos, em ordem escolhida pelo participante) em vez do genérico "fluxo de trabalho ainda
  mais eficiente".

### Lição 03 — Integrando Perfil, Memória, Busca e Projetos

- Abertura substituída: retirado o apelo genérico ("Imagine nunca mais precisar...") e
  substituído por um resumo objetivo dos quatro problemas já resolvidos nas lições anteriores,
  deixando claro que esta lição não ensina mecanismo novo algum.
- Texto de ligação antes do exercício integrador reescrito para explicitar que as quatro peças
  (Custom Instructions, Memory, Project) já existem desde as lições anteriores e serão apenas
  reaproveitadas — a única novidade é a ordem escolhida pelo participante.
- Resumo do processo guiado passou a antecipar os cinco itens exatos do checklist de validação
  (que no JSON foi implementado como pergunta de múltipla resposta), no lugar do genérico "de
  forma contínua".
- Feedbacks do quiz de múltipla resposta reescritos: ambos passaram a justificar por que o sexto
  item ("atualizar o sistema operacional") é um distrator sem relação com os mecanismos de
  continuidade do curso.
- **Conteúdo restaurado** no bloco de destaque final: a versão gerada resumia o Chat Search como
  "busca eficiente", perdendo a formulação concreta do roteiro-fonte ("um jeito de achar
  qualquer conversa antiga"). Restaurada a formulação original de "Conseguiu! E agora?".
- Parágrafo de encerramento da lição substituído: trocado o fechamento motivacional genérico
  ("Parabéns por chegar até aqui!... aproveite ao máximo o potencial do Claude") pela orientação
  prática e específica do roteiro-fonte, extraída da seção "Conseguiu! E agora?" (revisar
  instruções, confiar na busca, criar Project quando uma conversa tende a se repetir).

## Campos textuais alterados

Apenas `paragraph`, `description`, `feedbackCorrect` e `feedbackIncorrect`, dentro de blocos
`text` (variantes `heading paragraph`, `paragraph` e `impact`), `interactive-fullscreen`
(`intro`/`summary`) e `knowledgeCheck`.

Contagem verificada por script (comparação campo a campo contra `cursoClaudeChatHandsOn.json`):
**20 campos alterados** nas 3 lições — `paragraph` = 14, `description` = 2, `feedbackCorrect` = 2,
`feedbackIncorrect` = 2.

**Nenhum campo `heading`, `title` ou `label` foi alterado** — apenas corpo de texto, descrições e
feedbacks, na mesma linha editorial já aplicada às demais pastas deste projeto.

Os blocos verbatim do roteiro-fonte (breadcrumbs `🧭`, modelos entre aspas triplas nos passos do
processo guiado, tabelas de "Se travar" nos accordions, itens `[OPCIONAL]` e os dez hábitos de
"A Parte dos Dez") não foram tocados.

## Validação estrutural

Validação automatizada (script Python) comparando cada lição editada contra a lição
correspondente em `cursoClaudeChatHandsOn.json` (mesmo `lesson.id`), percorrendo recursivamente
toda a árvore JSON e conferindo, em cada nível, o conjunto exato de chaves, o comprimento de
cada array e o valor de todo campo não pertencente à lista de campos textuais permitidos.

Resultado: **0 divergências estruturais nos 3 arquivos.**

- Nenhum `id`, `courseId`, `author`, `globalBlockId` ou `itemId` alterado.
- Nenhum `type`, `family` ou `variant` alterado.
- Nenhuma `position` alterada (0 a 2, na ordem original).
- Nenhum `settings`, `metadata`, `createdAt`, `updatedAt` ou `experiments` alterado.
- Contagem de blocos idêntica à original: L01 = 23, L02 = 22, L03 = 10 itens.
- 5 quizzes (`knowledgeCheck`) conferidos, mesma(s) alternativa(s) `correct` marcada(s), na
  mesma ordem e com o mesmo texto em todos:
  - Lição 01: 2 quizzes (Custom Instructions e Chat Search).
  - Lição 02: 2 quizzes (Memory e Projects).
  - Lição 03: 1 quiz de múltipla resposta (5 itens corretos de 6 alternativas).
- 3 lições antes e 3 depois, com os mesmos IDs e o mesmo `courseId`.
- Todos os arquivos válidos como JSON, em UTF-8 sem BOM.
- Edições feitas por substituição pontual de string (ferramenta Edit), não por reescrita de
  arquivo — indentação e formatação originais preservadas.

## Pontos de atenção

1. **Este curso condensa 6 seções do roteiro-fonte em 3 lições**, diferente do padrão 1:1
   observado no curso Essentials e no Cowork Hands-on. Cada lição do JSON reúne duas oficinas
   completas (introdução, exercício guiado, quiz, "se travar" e "quer ir além" — repetidos duas
   vezes), separadas por um bloco `divider`/`continue`. Isso já estava assim na geração original;
   não foi alterado, mas vale confirmar se essa condensação foi intencional na concepção do curso.

2. **Dois trechos de conteúdo verbatim do roteiro-fonte, que a geração havia generalizado a
   ponto de perder informação, foram restaurados** (Lição 02: orientação sobre generalizar dados
   de terceiros na Memory; Lição 03: menção explícita à busca de conversas antigas no fechamento).
   Em ambos os casos a mudança ficou dentro dos campos textuais permitidos (`paragraph`); nenhuma
   estrutura foi alterada.

3. **Nenhuma resposta correta de `knowledgeCheck` estava errada.** Os 5 quizzes (4 de escolha
   única/múltipla e 1 de múltipla resposta) foram conferidos e a(s) alternativa(s) marcada(s)
   como correta(s) é(são) coerente(s) com o conteúdo da respectiva lição.

4. **A checklist "Como saber que terminou" do roteiro-fonte (5 itens marcáveis) foi implementada
   no JSON como pergunta de múltipla resposta (`knowledgeCheck` / `MULTIPLE_RESPONSE`)**, com um
   sexto item de distração ("Atualizar o sistema operacional do computador") que não existe no
   roteiro. Trata-se de uma adaptação de formato já presente na geração original — não é uma
   mudança estrutural feita nesta revisão —, mas vale registrar para quem for comparar o JSON
   diretamente ao roteiro.

5. **Um pequeno detalhe de formatação pré-existente foi mantido sem alteração:** o bloco de
   destaque "Cuidado" da Lição 02 usa `<strong>` diretamente no campo `paragraph`, sem o `<p>`
   que envolve os demais blocos `impact` do curso. Apenas o texto foi ampliado (ver Lição 02
   acima); a formatação não foi tocada, por não se tratar de conteúdo pedagógico.

## Confirmação

A estrutura técnica dos 3 arquivos JSON foi integralmente preservada, com verificação
automatizada campo a campo contra o curso original (`cursoClaudeChatHandsOn.json`). Apenas
campos textuais pedagógicos permitidos (`paragraph`, `description`, `feedbackCorrect`,
`feedbackIncorrect`) foram alterados, conforme as regras do prompt de edição.
