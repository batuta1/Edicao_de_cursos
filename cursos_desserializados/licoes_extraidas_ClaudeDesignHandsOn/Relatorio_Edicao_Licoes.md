# Relatório de alterações — Curso "Claude Design — Hands-on"

## Arquivos editados

- licao_01_Primeiros_Passos_Preparação_e_Criação_da_Página_Visual.json
- licao_03_Interatividade,_Avaliação_e_Compartilhamento_do_Material_Final.json

## Arquivo lido, sem alterações

- licao_02_Ajustando_Hierarquia,_Cores_e_Legibilidade.json — conferido de ponta a ponta contra o
  roteiro-fonte (abertura, lead-in, accordions, quizzes, boxes de dica/curiosidade, fechamento).
  Já reproduzia o roteiro de forma próxima ao verbatim em todos os pontos relevantes; nenhuma
  alteração foi necessária.
- `indice_licoes.json` foi apenas lido, não alterado.

## Roteiro-fonte utilizado

Existe roteiro-fonte e ele foi usado como referência principal, conforme a seção 9 do prompt de
edição:

- `Criacao de Cursos\Claude\Claude Design\hands-on\claude-design-hands-on-articulate-rise360.md`
  — roteiro direto do curso (Oficinas 1 a 4 + Projeto Final + "A Parte dos Dez" + "Conseguiu! E
  agora?"), com prompts entre aspas triplas, breadcrumbs, tabelas de "Se travar" e desafios
  opcionais "Quer ir além".
- `Criacao de Cursos\Claude\Claude Design\roteiro-curso-claude-design.md` — roteiro completo do
  curso "para leigos" (11 módulos), usado como referência complementar para o mesmo conteúdo em
  formato mais extenso.

**Mapeamento — este curso condensa 4 oficinas + projeto final do roteiro em 3 lições**:

| Lição | Título | Seções do roteiro combinadas |
|---|---|---|
| 01 | Primeiros Passos | Oficina 1 (Tirando Sua Disciplina do Papel) |
| 02 | Ajustando Hierarquia, Cores e Legibilidade | Oficina 2 (Fazendo o Olho Ir Direto ao Ponto) + Oficina 3 (Domando Cores e Letras Rebeldes) |
| 03 | Interatividade, Avaliação e Compartilhamento | Oficina 4 (Dando Vida à Tela) + Projeto Final + "A Parte dos Dez" (parcial) + "Conseguiu! E agora?" |

Mapeamento confirmado por título e correspondência de conteúdo (prompts, breadcrumbs e blocos de
destaque reproduzidos quase verbatim do roteiro em todas as três lições).

**Critério aplicado:** o mesmo já usado nas demais pastas deste projeto — todo texto verbatim do
roteiro-fonte (prompts entre aspas triplas, breadcrumbs, tabelas de "Se travar", desafios
opcionais, boxes de destaque com emoji) foi conferido e, na esmagadora maioria dos casos, já
estava reproduzido fielmente na geração original. As duas alterações feitas corrigem uma perda
concreta de informação em relação ao roteiro-fonte — não reescrevem tom ou estilo, que já estava
adequado ao restante do curso.

## Alterações realizadas

### Lição 01 — Primeiros Passos: Preparação e Criação da Página Visual

- **Checklist de pré-requisitos corrigida.** A versão gerada trazia itens vagos: "Tenha uma conta
  ativa no serviço necessário" (não nomeia qual serviço) e "Confirme que tem acesso ao que
  precisa" (não diz a quê). O roteiro-fonte é específico nesse ponto — conta em Claude.ai com o
  Claude Design habilitado, hoje restrito aos planos pagos (Pro, Max, Team ou Enterprise) — e essa
  especificidade é prática: sem ela, um professor no plano gratuito não entenderia por que não
  consegue acessar a ferramenta. Os quatro itens da checklist foram reescritos para restaurar esse
  nível de detalhe, mantendo os quatro itens originais (nenhum item adicionado ou removido).
- Abertura, lead-in da lista de objetivos, accordion de acesso, exercício guiado, quiz, blocos de
  destaque e desafios opcionais conferidos contra o roteiro-fonte (Oficina 1): já reproduziam o
  conteúdo de forma fiel — não alterados.

### Lição 02 — Ajustando Hierarquia, Cores e Legibilidade

Nenhuma alteração. Abertura, lead-in, os dois exercícios guiados (hierarquia; cores e contraste),
os dois quizzes, os boxes de dica e curiosidade técnica, e os desafios opcionais já reproduziam o
roteiro-fonte (Oficinas 2 e 3) de forma próxima ao verbatim, incluindo os prompts entre aspas
triplas e as tabelas de "Se travar".

### Lição 03 — Interatividade, Avaliação e Compartilhamento do Material Final

- **Fechamento da lição enriquecido.** A primeira metade do parágrafo final já reproduzia de perto
  a seção "Conseguiu! E agora?" do roteiro-fonte ("Você saiu de 'nunca usei IA' para 'tenho um
  material pronto para usar'...") e foi mantida. A segunda metade generalizava o fechamento do
  roteiro ("pegue o próximo material que você precisa criar — um cronograma, um aviso, uma
  atividade — e aplique o mesmo caminho") para uma frase sem exemplos ("Use o ciclo... para cada
  novo material... Bons projetos!"). Reescrita para restaurar os exemplos concretos do
  roteiro-fonte.
- Abertura, lead-in, exercício guiado de interatividade, exercício guiado de avaliação final,
  checklist de qualidade, quiz, boxes de destaque, desafios opcionais e flashcards de dicas
  conferidos contra o roteiro-fonte (Oficina 4 + Projeto Final + "A Parte dos Dez"): já
  reproduziam o conteúdo de forma fiel — não alterados, com uma ressalva registrada abaixo.

## Campos textuais alterados

Exclusivamente o campo `paragraph`, dentro de blocos `text` (variantes `heading paragraph` e
`paragraph`). **Nenhum campo `heading`, `title` ou `label` foi alterado.**

**2 campos `paragraph` alterados** no total — 1 na Lição 01 (checklist de pré-requisitos), 1 na
Lição 03 (parágrafo de fechamento). A Lição 02 não recebeu nenhuma alteração.

## Validação estrutural

`cursoClaudeDesignHandsOn.json` foi regenerado durante esta revisão (ver "Pontos de atenção",
item 1) e passou a servir como linha de base confiável para validação automatizada campo a campo,
no mesmo padrão usado nas demais pastas deste projeto.

Validação automatizada (script PowerShell) comparando cada lição editada, nó a nó recursivamente,
contra a lição correspondente em `cursoClaudeDesignHandsOn.json` (mesmo `lesson.id`), conferindo
em cada nível o conjunto exato de chaves, o comprimento de cada array, e o valor de todo campo que
não seja `paragraph`.

Resultado: **0 divergências estruturais nos 3 arquivos**, e a contagem de campos `paragraph`
alterados por lição confere exatamente com as edições pontuais descritas acima — Lição 01 = 1,
Lição 02 = 0, Lição 03 = 1.

- Nenhum `id`, `courseId`, `author`, `globalBlockId` ou `itemId` alterado.
- Nenhum `type`, `family`, `variant` ou `position` alterado.
- Nenhum `heading`, `title` ou `label` alterado — confirmado nó a nó, não só por inspeção.
- Contagem de blocos e de itens dentro de cada bloco idêntica à original em todas as lições
  (nenhuma divergência de comprimento de array em nenhum nível, incluindo os 4 itens `<li>` da
  checklist de pré-requisitos da Lição 01).
- 5 quizzes (`knowledgeCheck`) conferidos: mesma alternativa marcada como `correct`, na mesma
  ordem e com o mesmo texto em todos — nenhum foi tocado.
- Todos os arquivos válidos como JSON, em UTF-8 sem BOM.
- Edições feitas por substituição pontual de string (ferramenta Edit), não por reescrita de
  arquivo — indentação e formatação originais preservadas.

## Pontos de atenção

1. **`cursoClaudeDesignHandsOn.json` estava com o título e o conteúdo do curso Essentials —
   corrigido durante esta revisão.** Investigação a pedido do usuário: o arquivo era uma cópia
   idêntica (mesmo hash SHA-256) de `cursoClaudeDesignEssentials.json`, com `course.title` "Claude
   Design - Essentials" e as seis lições do curso Essentials, em vez das três lições do Hands-on.
   Pela data de criação/modificação dos arquivos (11/08), o arquivo correto havia sido gerado às
   13:24:22 — a extração de `licao_02` e do `indice_licoes.json`, feita logo em seguida, usou essa
   versão correta — mas foi sobrescrito às 13:35:16, 18 segundos antes de
   `cursoClaudeDesignEssentials.json` ser criado com o mesmo conteúdo. As lições `licao_01` e
   `licao_03`, concluídas mais tarde (13:49:55 e 13:50:19), já não vieram mais desse arquivo — por
   isso as três lições em `licoes_extraidas_ClaudeDesignHandsOn/` permaneceram corretas e não
   precisaram de correção quanto a esse ponto. O arquivo foi regenerado decodificando
   `HandsOnClaudeDesign-Default.zip` (`scormcontent/runtime-data.js`, payload em Base64 dentro de
   uma chamada `__jsonp(...)`, exatamente o formato descrito na seção 1 do prompt de edição).
   Verificado após a regeneração: `course.title` = "Claude Design - Hands-On", `course.id` =
   `I1RdLMucyKlVsh-B5lbGdFvQy9TZc8Ue`, e os três `lesson.id` batendo exatamente com os três
   arquivos já extraídos.
2. **Flashcards de dicas da Lição 03 cobrem 8 dos 10 itens de "A Parte dos Dez" do roteiro-fonte.**
   Faltam os itens sobre anexar uma imagem de referência visual ao pedido e sobre o Claude Design
   não gerar fotos realistas nem logos. Isso já estava assim na geração original — trata-se de uma
   escolha de escopo (quais 8 de 10 dicas entraram no material), não de uma perda por edição, e
   corrigir exigiria adicionar itens ao array de flashcards, o que está fora do escopo desta
   revisão (que não pode adicionar itens a listas/arrays). Registrado para eventual decisão
   humana sobre incluir os dois itens restantes.
3. **Nenhuma resposta correta de `knowledgeCheck` estava errada.** As 5 questões (Lições 01, 02 —
   duas — e 03) foram conferidas e a alternativa marcada como correta é coerente com o conteúdo da
   respectiva lição e com o roteiro-fonte em todas.
4. **Qualidade já alta na geração original.** Diferente do curso Essentials, as três lições deste
   Hands-on já reproduziam o roteiro-fonte de forma muito próxima ao verbatim — prompts,
   breadcrumbs, tabelas de "Se travar" e boxes de destaque praticamente idênticos ao roteiro. Por
   isso o volume de edição foi baixo (2 campos em 2 das 3 lições): a revisão restaurou
   especificidade perdida em pontos pontuais, mas não havia o padrão de abertura genérica
   observado no curso Essentials.

## Confirmação

Apenas o campo textual pedagógico `paragraph` foi alterado, em 2 lições das 3 (Lições 01 e 03),
conforme as regras do prompt de edição. A estrutura técnica dos 3 arquivos JSON foi integralmente
preservada, com verificação automatizada, nó a nó, contra `cursoClaudeDesignHandsOn.json`
(regenerado corretamente durante esta revisão — ver "Pontos de atenção", item 1).

## Remontagem, serialização e teste (seção 15 do prompt de edição)

O curso foi remontado e reserializado, concluindo o ciclo completo pedido pelo prompt de edição.

**Como o payload é armazenado neste export:** `HandsOnClaudeDesign-Default.zip` guarda o curso em
`scormcontent/runtime-data.js`, num arquivo à parte de `index.html`, dentro de uma chamada
`__jsonp("runtime-data.js","BASE64")` — o mesmo esquema de Base64 simples (sem LZW) usado no
export Essentials, só que embrulhado de outro jeito. Foi o mesmo arquivo já decodificado para
corrigir `cursoClaudeDesignHandsOn.json` (ver "Pontos de atenção", item 1).

**Processo:**

1. Teste de sanidade primeiro: o payload original (sem edição) foi decodificado, re-serializado
   pelo mesmo processo e comparado com o original — o arquivo resultante ficou com o **mesmo
   tamanho exato** (102830 caracteres) e **0 divergências estruturais** em relação ao original.
   Só depois desse teste passar as lições editadas foram aplicadas de verdade.
2. As 3 lições foram lidas e substituídas, por `lesson.id`, dentro do array `course.lessons` do
   objeto completo do curso (2 delas com o texto editado; a Lição 02, sem alterações, entrou
   idêntica à original).
3. O objeto foi serializado para JSON minificado, codificado em Base64 e embrulhado de volta em
   `__jsonp("runtime-data.js","...")`, substituindo o arquivo `runtime-data.js` por completo (é um
   arquivo dedicado só a isso, diferente do Essentials onde o payload fica embutido em meio a
   outro código).
4. Um novo pacote SCORM foi gerado — `HandsOnClaudeDesign-Default-REVISADO.zip`, na pasta
   `Edicao_de_cursos` — copiando o zip original e substituindo apenas
   `scormcontent/runtime-data.js`. Os outros 73 arquivos do pacote permaneceram inalterados;
   verificado por comparação de tamanho de cada entrada do zip.

**Validação:**

- Comparação automatizada, nó a nó, entre o curso remontado e `cursoClaudeDesignHandsOn.json`:
  exatamente os 2 campos `paragraph` documentados acima aparecem como diferentes (1 na Lição 01,
  1 na Lição 03), e nenhuma outra divergência estrutural foi encontrada.
- Cada uma das 3 lições dentro do curso remontado foi comparada com o respectivo arquivo
  `licao_0X_*.json` extraído: **0 diferenças** em todas.
- **Testado de fato no HTML:** o pacote `HandsOnClaudeDesign-Default-REVISADO.zip` foi extraído e
  aberto em navegador local (via um mock mínimo da API de LMS, já que o pacote recusa-se a
  renderizar fora de uma LMS real — mesmo comportamento do zip original). O curso carregou e
  navegou normalmente; a Lição 1 exibiu exatamente a checklist de pré-requisitos reescrita nesta
  revisão, com os quatro itens corrigidos.

O pacote pronto para teste na plataforma está em:
`Edicao_de_cursos\HandsOnClaudeDesign-Default-REVISADO.zip`. O zip original não foi alterado. O
pacote `HandsOnClaudeDesign-Legacy.zip` (variante alternativa de export) não foi usado para a
remontagem — apenas o `Default`, escolhido pelo usuário para a correção do item 1.
