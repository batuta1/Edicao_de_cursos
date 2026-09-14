# Prompt-Mestre — Pipeline Completo de Curso
### (Roteiro → Auditoria Crítica → Reconstrução 2.0 → Trilhas Essentials/Hands-on → Versões Rise 360)

> **Como usar:** preencha o **OBJETO BASE** uma única vez — ele vale para todas as etapas. Depois, envie os blocos de prompt abaixo em sequência (Etapa 1 → 2 → 3 → 4A/4B → 5A/5B), na mesma conversa com a IA, para que cada etapa use o resultado da etapa anterior automaticamente. Se preferir rodar cada etapa isoladamente, cole o(s) arquivo(s) de saída da(s) etapa(s) anterior(es) junto com o bloco de prompt correspondente. Veja "Modo de Execução" e "Organização de Arquivos" antes de começar.

---

## Visão Geral do Pipeline

| Etapa | Produz | Entrada | Arquivo de saída |
|---|---|---|---|
| 1 — Roteiro Base | Curso "Para Leigos" completo, do zero | OBJETO BASE | `roteiro-curso-[slug].md` |
| 2 — Auditoria Crítica | Análise 360° (pedagógica, técnica, de UX) do Roteiro Base | Saída da Etapa 1 | `ANALISE_CRITICA_[SLUG].md` |
| 3 — Reconstrução 2.0 | Roteiro reconstruído, incorporando todas as correções da auditoria | Saídas das Etapas 1 e 2 | `novo-roteiro-curso-[slug].md` |
| 4A — Trilha Hands-on | Curso prático em oficinas, estilo PBL | Saída da Etapa 3 | `hands-on/[slug]-para-leigos-hands-on.md` |
| 4B — Trilha Essentials | Plano de aula formal/acadêmico | Saída da Etapa 3 | `essentials/plano-de-aula-[slug]-essentials.md` |
| 5A — Hands-on Rise 360 | Versão da Etapa 4A com cues de montagem, breadcrumbs e marcadores de lição | Saída da Etapa 3 (ou 4A) | `hands-on/[slug]-hands-on-articulate-rise360.md` |
| 5B — Essentials Rise 360 | Versão da Etapa 4B com cues de montagem, breadcrumbs, marcadores de lição e fio condutor | Saída da Etapa 3 (ou 4B) | `essentials/plano-de-aula-[slug]-essentials-articulate-rise360.md` |

Ao final das sete gerações, você terá **6 arquivos** (a Etapa 2 gera 1 arquivo de análise que não é, em si, material de curso, mas alimenta a Etapa 3) cobrindo o mesmo tema em seis formatos diferentes, todos derivados de uma única fonte auditada e corrigida.

---

## OBJETO BASE (preencher uma única vez)

```text
- Tema/ferramenta do curso: [ex.: "Claude Design", "Excel para iniciantes", "Canva para professores"]
- Público-alvo: [ex.: docentes da escola pública sem contato prévio com IA, design digital ou programação]
- Pré-requisitos: [ex.: nenhum conhecimento prévio; conta ativa na ferramenta, se aplicável]
- Recursos/requisitos técnicos: [ex.: computador com navegador e internet; plano pago X; versão Y do software]
- Material-fonte de referência: [colar ou descrever documentação, tutoriais ou notas sobre o OBJETO BASE;
  se ausente, gerar a partir de conhecimento geral — sinalizando pontos que exigem validação]
- slug (para nomes de arquivo): [versão curta, em minúsculas e com hifens, do tema — ex.: "claude-design"]
```

---

## Modo de Execução

- **Sequencial na mesma conversa (recomendado):** envie a Etapa 1; quando o resultado sair, envie a Etapa 2 (a IA já tem o Roteiro Base no contexto); envie a Etapa 3 (a IA já tem Roteiro Base + Auditoria); e assim por diante até a Etapa 5B. Cada bloco abaixo já contém uma instrução de "Entrada" indicando o que reaproveitar da conversa.
- **Etapas isoladas:** se cada etapa for enviada em uma conversa nova, cole o conteúdo do(s) arquivo(s) de saída da(s) etapa(s) anteriores logo antes do bloco de prompt, como material-fonte daquela etapa.
- Nunca pule a Etapa 2 antes da Etapa 3: a reconstrução (Etapa 3) depende integralmente da auditoria para saber o que corrigir.
- As Etapas 4A/4B e 5A/5B são independentes entre si e podem ser geradas em qualquer ordem, mas ambas dependem da Etapa 3 como fonte de conteúdo já corrigido.

---

## Organização de Arquivos e Pastas

Antes de gerar os arquivos, crie a seguinte estrutura na pasta do projeto:

```
[pasta do projeto]/
├── roteiro-curso-[slug].md              → saída da Etapa 1
├── ANALISE_CRITICA_[SLUG].md            → saída da Etapa 2
├── novo-roteiro-curso-[slug].md         → saída da Etapa 3
├── essentials/
│   ├── plano-de-aula-[slug]-essentials.md                       → saída da Etapa 4B
│   └── plano-de-aula-[slug]-essentials-articulate-rise360.md    → saída da Etapa 5B
└── hands-on/
    ├── [slug]-para-leigos-hands-on.md                → saída da Etapa 4A
    └── [slug]-hands-on-articulate-rise360.md         → saída da Etapa 5A
```

---
---

# ETAPA 1 — Roteiro Base ("Para Leigos")

Gera o curso completo do zero, em linguagem extremamente acessível, sem pressupor nenhum conhecimento prévio.

```text
# CONTEXTO
Você atuará como Designer Instrucional especializado na série "Para Leigos" (For
Dummies), com foco em ferramentas de criação assistida por Inteligência
Artificial. Sua tarefa é produzir, em português, um Relatório de Roteiro de
Curso completo, em Markdown, que ensine o OBJETO BASE de forma progressiva e
extremamente acessível a um público iniciante.

O curso NÃO forma profissionais da área (designers, programadores etc.). Parta
do princípio de que o participante não tem conhecimento técnico prévio e precisa
primeiro compreender o que está acontecendo na tela, antes de qualquer
explicação técnica.

# OBJETO BASE
Utilize o OBJETO BASE definido na seção compartilhada deste pipeline (tema,
público-alvo, pré-requisitos, recursos necessários, material-fonte).

# ESCOPO
Mantenha o curso focado no OBJETO BASE como ferramenta de criação — geração de
interfaces, páginas, materiais visuais, organização de informação, composição de
layout, refinamento iterativo — e NÃO o transforme em um curso genérico de
engenharia de prompt. Prompts só devem aparecer quando necessários para ensinar
uma atividade específica, mostrando: intenção → instrução → resultado →
refinamento, em vez de teoria extensa sobre como escrever prompts.

# PRINCÍPIO PEDAGÓGICO CENTRAL
Todo conceito novo deve responder, nesta ordem, antes de qualquer detalhe
técnico:
1. O que é isso?
2. Por que isso é útil para o público-alvo?
3. O que consigo criar com isso agora?

# ESTRUTURA OBRIGATÓRIA POR MÓDULO (nesta ordem)
1. Título do Módulo — curto, memorável, orientado ao resultado. Evite títulos
   técnicos (prefira "Primeiro desenho: pedindo à ferramenta para montar a
   tela" a "Introdução à geração de interfaces baseada em modelos generativos").
2. O "Pulo do Gato" — explicação ultrarrápida do conceito central, compreensível
   em poucos segundos, com uma analogia do cotidiano do público-alvo.
3. Desenvolvimento — contexto, conceitos necessários, para que servem, exemplos
   concretos, como a ferramenta aplica o conceito, erros comuns, como melhorar
   um primeiro resultado. Explique qualquer termo técnico indispensável no
   momento em que ele surgir. Quando houver vários elementos importantes,
   organize-os em componentes numerados simples.
4. Pílula Hands-on — Mão na Massa — exercício de aproximadamente 2 minutos,
   extremamente simples, executável por iniciantes, sem exigir conhecimento de
   programação, possível em computador e, quando a funcionalidade permitir, em
   smartphone, com passos curtos e resultado visível rápido.

# PROGRESSÃO DIDÁTICA
Organize os módulos seguindo: entender → criar → observar → modificar → refinar
→ aplicar. Evite excesso de teoria antes da primeira prática; o participante
deve experimentar alguma criação já no início do curso.

# ANALOGIAS
Utilize analogias do cotidiano real do público-alvo definido no OBJETO BASE. Se
o público for docente, por exemplo, use analogias como: hierarquia visual =
organização do quadro-negro; componentes = peças reutilizáveis de material
pedagógico; espaçamento = organização de carteiras em sala; iteração = corrigir
uma atividade; design responsivo = preparar o mesmo conteúdo para quadro, papel
impresso e tela do celular. Adapte sempre ao público-alvo real, sem se limitar a
estes exemplos.

# ABORDAGEM SOBRE CÓDIGO
Caso a ferramenta gere código (HTML, CSS, JavaScript ou outro) durante uma
atividade, não transforme a aula em aula de programação. Para iniciantes,
priorize a ideia de que a ferramenta usa código para transformar a descrição em
algo que o navegador consegue exibir. Aprofunde detalhes técnicos apenas quando
isso ajudar a compreender ou modificar o resultado.

# PENSAMENTO DE DESIGN
Ensine o participante a não aceitar automaticamente a primeira versão
produzida. Reforce perguntas como: está fácil de entender? o elemento mais
importante chama atenção primeiro? há informação demais? o texto está legível?
as cores ajudam ou atrapalham? os elementos estão organizados? uma pessoa
saberia onde clicar? o resultado combina com o público? o design ajuda o
conteúdo ou só o enfeita?

# CONTEXTO DE APLICAÇÃO
Utilize, sempre que possível, exemplos ligados ao contexto real do público-alvo
definido no OBJETO BASE — sem limitar o curso exclusivamente a eles.

# ESTILO OBRIGATÓRIO
- Linguagem formal, acolhedora, pedagógica, clara, leve, ocasionalmente
  bem-humorada, sem infantilizar o leitor.
- Frases e exemplos curtos e concretos.
- Use negrito para conceitos importantes, listas para decompor processos,
  blocos de destaque (">") para conceitos essenciais, e pequenas comparações
  "ruim vs. melhor" quando fizer sentido.
- Evite: jargão técnico em excesso, explicações abstratas, blocos longos de
  texto, linguagem publicitária, apresentar a ferramenta como infalível, e
  presumir conhecimento prévio de programação.

# ESTRUTURA DO RELATÓRIO FINAL
- Título do curso e breve apresentação (para quem é, promessa, tom).
- Nota "Antes de Começar" com pré-requisitos de acesso.
- Mapa do curso (tabela: módulo, título, fase da jornada, o que o participante
  vai conseguir fazer).
- Sequência completa de módulos, seguindo a ESTRUTURA OBRIGATÓRIA acima.
- Encerramento breve, reforçando a jornada percorrida.
- Glossário rápido dos termos técnicos introduzidos.

O curso deve levar o participante de "nunca utilizei o OBJETO BASE para isso"
até "consigo pedir, avaliar criticamente e refinar sucessivamente um resultado
até chegar a algo adequado ao meu objetivo".

# RESTRIÇÕES
- Não invente recursos, botões ou menus que a ferramenta não possua; em caso de
  incerteza, descreva a ação de forma genérica e sinalize a necessidade de
  conferir.
- Produza o documento inteiro em um único arquivo Markdown, pronto para uso.

# FORMATO DE SAÍDA
Um único documento Markdown completo, pronto para ser salvo como
`roteiro-curso-[slug].md`.
```

---
---

# ETAPA 2 — Auditoria Crítica 360°

Audita o Roteiro Base como um consultor externo — sem complacência com o próprio trabalho anterior do pipeline.

```text
# CONTEXTO
Você atuará como consultor sênior especializado em Experiência do Usuário (UX),
Design Instrucional, Design de Interfaces e ferramentas de criação assistida por
Inteligência Artificial. Sua missão é realizar uma Análise Crítica de 360 graus
sobre o Roteiro Base produzido na Etapa 1 deste pipeline, avaliando não apenas
se o material está correto, mas se ele realmente ensina o participante a
compreender, utilizar e explorar o potencial do OBJETO BASE.

# ENTRADA
Utilize como material a ser analisado o documento completo produzido na Etapa 1
(se estiver em conversa isolada, cole o conteúdo de `roteiro-curso-[slug].md`
antes de prosseguir). Utilize o OBJETO BASE definido na seção compartilhada
deste pipeline como contexto de público-alvo e limites de escopo.

# ITENS DE ANÁLISE OBRIGATÓRIOS
1. Clareza Pedagógica — ordem dos conceitos, excesso de informação antes da
   primeira prática, conhecimento prévio presumido, explicação de termos
   técnicos, qualidade dos exemplos, especificidade das instruções, conexão
   lógica entre módulos, e avaliação individual de cada Pílula Hands-on (tempo
   realista, passos implícitos, resultado esperado claro, descoberta visual
   perceptível, execução sem ajuda por um iniciante completo).
2. Rigor Técnico — precisão das explicações sobre o funcionamento do OBJETO
   BASE; identificar simplificações excessivas, explicações incorretas,
   expectativas irreais, confusão entre design e programação, capacidades
   inexistentes atribuídas à ferramenta, e fluxos que podem variar por
   versão/plataforma (sinalizando explicitamente risco de informação
   desatualizada).
3. Qualidade de UX do Próprio Tutorial — trate o roteiro como um produto
   digital: clareza de títulos, tamanho dos blocos de texto, hierarquia da
   informação, distribuição entre teoria e prática, e pontos onde um
   screenshot, GIF, vídeo, comparação antes/depois ou esquema visual
   substituiria melhor uma explicação textual — sempre especificando
   exatamente qual recurso deveria aparecer e por quê.
4. Engajamento — tom de voz adequado ao público (profissional, acolhedor,
   acessível, direto, sem infantilizar); presença de pequenas conquistas e
   momentos de "veja o que aconteceu" / "compare as duas versões" ao longo do
   curso.
5. Qualidade do Ensino de Design — verificar se aparecem, de forma não
   acadêmica, conceitos como hierarquia visual, alinhamento, contraste,
   espaçamento, tipografia, cores, consistência, agrupamento, legibilidade,
   densidade de informação, componentes, responsividade, acessibilidade,
   feedback visual e estados de interface; avaliar se o curso desenvolve a
   capacidade de reconhecer "por que esta versão parece melhor do que a
   anterior".
6. Qualidade da Interação com a Ferramenta — avaliar se o fluxo ensinado é
   descrever → gerar → observar → criticar → ajustar → comparar → refinar; se
   o curso ensina instruções como simplificar, reorganizar, melhorar
   legibilidade, alterar hierarquia, mudar público-alvo, adaptar para outro
   dispositivo; e se evita depender de "prompts perfeitos" ou se transforma em
   curso de engenharia de prompt.
7. Potencial Oculto — funcionalidades reais do OBJETO BASE ainda não
   exploradas no material, sempre explicando qual problema de design ou de
   ensino aquela funcionalidade resolveria — nunca incluir uma funcionalidade
   só por ser tecnologicamente interessante.
8. Aplicabilidade Educacional/Prática — avaliar se os exemplos fazem sentido
   para o público-alvo real definido no OBJETO BASE, e apontar onde um exemplo
   genérico poderia virar um exemplo mais significativo para esse público.

# ESTRUTURA OBRIGATÓRIA DO RELATÓRIO (nesta ordem, use estes títulos)
1. Sumário Executivo — nível geral de qualidade, maturidade pedagógica e
   técnica, qualidade do fluxo, principais forças e fragilidades, principal
   risco para o participante, principal oportunidade, e avaliação geral na
   escala Excelente / Muito Bom / Bom / Regular / Fraco.
2. Pontos Positivos — Fortalezas — o que funciona, por que funciona, qual
   princípio pedagógico/de UX está bem aplicado, e como isso beneficia um
   iniciante. Não elogie apenas por ser visualmente agradável.
3. Pontos Negativos e Gargalos — Debilidades — problemas concretos,
   classificados em Criticidade Alta (impede execução/compreensão), Média
   (prejudica a aprendizagem sem impedir) ou Baixa (clareza/acabamento).
4. Matriz de Soluções e Melhorias — tabela obrigatória com as colunas:
   Problema identificado | Criticidade | Impacto no aluno | Solução
   recomendada | Tipo de intervenção (reescrita, screenshot, vídeo, GIF,
   exemplo, exercício, reorganização, conceito adicional, correção técnica,
   melhoria visual). Soluções devem ser específicas e acionáveis, nunca
   genéricas.
5. Análise das Pílulas Hands-on — avaliação individual de cada atividade
   (objetivo, dificuldade estimada, clareza, tempo realista, conhecimento
   prévio exigido, ponto provável de dificuldade, melhoria recomendada),
   classificada como Manter / Ajustar / Substituir (com nova atividade
   proposta em caso de substituição).
6. Lacunas de Conteúdo — separadas em Essenciais, Intermediárias e Avançadas.
7. Roadmap de Expansão — três níveis (Nível 1 — Criando, Nível 2 —
   Refinando, Nível 3 — Construindo experiências), cada tópico com o que
   ensinar + por que ensinar + atividade prática sugerida.
8. Recomendações Prioritárias — as 10 melhorias mais importantes, em ordem
   de prioridade, cada uma no formato: Mudança recomendada / Problema que
   resolve / Impacto esperado / Esforço estimado (Baixo/Médio/Alto).

# CRITÉRIO CENTRAL DA AVALIAÇÃO
Utilize esta pergunta como referência ao longo de toda a análise: ao terminar
o tutorial, o participante apenas conseguiu pedir à ferramenta que criasse
algo, ou realmente começou a compreender como usá-la para tomar melhores
decisões? O segundo resultado deve ser o objetivo.

# RESTRIÇÕES
- Realize uma verdadeira auditoria, não um resumo: aponte problemas concretos
  (com referência ao trecho do Roteiro Base) e proponha soluções igualmente
  concretas.
- Quando identificar conteúdo tecnicamente duvidoso ou potencialmente
  desatualizado, sinalize a necessidade de verificação.

# FORMATO DE SAÍDA
Um único documento Markdown completo, estruturado exatamente na ordem acima,
pronto para ser salvo como `ANALISE_CRITICA_[SLUG].md` e para posterior
conversão a um documento profissional (ex.: Word).
```

---
---

# ETAPA 3 — Reconstrução 2.0

Reconstrói o curso incorporando integralmente as correções da auditoria — reestruturação completa quando necessário, não apenas ajustes pontuais.

```text
# CONTEXTO
Você atuará como Designer Instrucional e Arquiteto de Documentação Técnica. Sua
missão é reconstruir o Roteiro Base (Etapa 1) com base integral na Auditoria
Crítica (Etapa 2), transformando cada debilidade identificada em uma melhoria
concreta de clareza, progressão pedagógica, qualidade visual e aplicação
prática. Não faça apenas pequenas correções: realize uma reestruturação
pedagógica completa sempre que a auditoria indicar necessidade.

# ENTRADA
Utilize como base o Roteiro Base (Etapa 1) e a Auditoria Crítica (Etapa 2),
ambos produzidos anteriormente neste pipeline (se estiver em conversa isolada,
cole os dois documentos antes de prosseguir). Utilize o OBJETO BASE definido na
seção compartilhada deste pipeline.

# PRINCÍPIO CENTRAL
A ferramenta não deve ser apresentada apenas como algo que "gera resultados". O
participante deve aprender progressivamente o ciclo: descrever → gerar →
observar → avaliar → modificar → comparar → refinar. A aprendizagem de design
acontece DURANTE esse processo — o curso ensina não só o que pedir, mas
principalmente como reconhecer se o resultado ficou bom e como melhorá-lo.

# ESTRUTURA OBRIGATÓRIA POR AULA (nesta ordem)
1. Nome da Aula — curto, claro, orientado à ação.
2. Subseções — cada uma com "📸 Sugestão de Prints": descrição detalhada de
   qual tela deve aparecer, qual elemento deve estar destacado, quais menus
   devem estar abertos, qual botão recebe destaque, se há comparação entre
   versões, e se o print mostra o resultado antes ou depois da alteração.
   Sugira sequência numerada de screenshots, GIF ou vídeo curto quando a ação
   for difícil de explicar só com texto.
3. Objetivos da Aula — específicos e observáveis (evite objetivos vagos).
4. Habilidades Esperadas — o que o participante deverá conseguir fazer sem
   ajuda após concluir a aula.
5. Desenvolvimento da Aula — linguagem profissional, objetiva, acessível,
   pedagógica e progressiva; explique conceitos técnicos só quando necessários
   para a atividade; use analogias do cotidiano do público-alvo; se a
   ferramenta gerar código, apresente primeiro sua função prática, sem
   transformar a aula em introdução a programação.
6. Conceito de Design da Aula — cada aula introduz ou reforça pelo menos um
   princípio (hierarquia visual, contraste, alinhamento, proximidade,
   espaçamento, tipografia, cores, consistência, componentes, densidade
   visual, responsividade, acessibilidade, feedback visual, etc.), sempre
   respondendo: (1) o que é? (2) por que importa? (3) como perceber na tela?
   (4) como pedir à ferramenta para melhorar?
7. Antes e Depois — sempre que fizer sentido: uma pequena atividade de
   comparação visual (estado "antes", instrução enviada, e o que observar no
   "depois": o que mudou, por que ficou mais fácil de compreender, quais
   decisões de design foram tomadas). O objetivo é desenvolver alfabetização
   visual, não apenas ensinar comandos.
8. Pílula Hands-on — Mão na Massa — no formato fixo:
   "🧪 Pílula Hands-on / Objetivo: [...] / Faça agora: [passos numerados] /
   Observe: [elementos a comparar] / Resultado esperado: [...]". Deve durar de
   2 a 5 minutos, ser simples para iniciantes, exigir poucas etapas, produzir
   resultado visual imediato, validar o conceito aprendido, e funcionar em
   computador e, quando a funcionalidade permitir, smartphone. Nunca proponha
   um exercício de simplesmente copiar um comando sem compreender o resultado.
9. Troubleshooting — Solução de Problemas — nos pontos identificados como
   críticos na Auditoria (Etapa 2), no formato "🔧 Troubleshooting / Problema:
   [...] / Possível causa: [...] / Como resolver: [...]".

# DIRETRIZES DE CONTEÚDO
1. Comece pela experiência, não pela teoria: ver → experimentar → entender →
   melhorar.
2. Mostre progressivamente o diferencial real da ferramenta — a conversa e o
   refinamento contínuo, não apenas "digitar um pedido e ver algo aparecer".
3. Ensine design DURANTE o uso real, não em módulos teóricos isolados.
4. Prompts são ferramenta, não disciplina: quando houver uma instrução, use a
   estrutura objetivo + contexto + mudança desejada, e sempre peça que o
   participante observe o resultado depois.
5. Ensine refinamento iterativo explicitamente, repetindo o ciclo: primeira
   versão → o que está estranho? → escolha um problema → peça uma melhoria →
   compare → refine novamente — aumentando gradualmente a autonomia do
   participante ao longo do curso.
6. Utilize, sempre que possível, exemplos relevantes para o público-alvo real
   definido no OBJETO BASE, evitando exemplos exclusivamente corporativos ou
   genéricos.

# PROGRESSÃO RECOMENDADA
Organize o curso em partes progressivas cobrindo, na ordem: primeiros passos
sem exigir conhecimento prévio → organização da informação (hierarquia,
seções, agrupamento, espaçamento, alinhamento) → personalidade visual (cores,
tipografia, contraste, consistência) → componentes reutilizáveis →
refinamento crítico do próprio resultado → adaptação entre formatos/
dispositivos → acessibilidade (apresentada como parte da qualidade do design,
não como etapa burocrática) → experiências interativas simples → projetos
completos que integrem os conhecimentos anteriores → uso da ferramenta como
parceira de crítica (deixando claro que a decisão final é sempre do
participante) → uso de referências visuais → diferença entre protótipo,
interface, código e produto final, com alertas de validação, testes,
segurança, dados, manutenção e publicação quando aplicável. Adapte esta
progressão à natureza real do OBJETO BASE.

# NOTAS E ALERTAS
Utilize blocos de citação Markdown (">") para três tipos de aviso, distintos e
consistentes ao longo de todo o documento:
- "Nota:" — informação de apoio (ex.: o resultado gerado é sempre um ponto de
  partida, a decisão final é do participante).
- "Atenção:" — alerta de risco ou cuidado (ex.: não usar dados pessoais ou
  sensíveis em exemplos).
- "Nota de versão:" — aviso de que um recurso pode mudar de nome/posição
  entre versões da ferramenta, e que o roteiro deve ser revalidado antes da
  publicação.

# CRITÉRIO DE QUALIDADE
Cada aula deve responder claramente: o que o participante vai aprender? o que
ele fará na prática? o que ele deverá observar? qual princípio de design está
sendo aprendido? o que ele conseguirá fazer sozinho depois? Se uma aula não
produzir uma habilidade observável, reestruture-a.

# RESTRIÇÕES
- Utilize integralmente a Auditoria (Etapa 2) como base — cada debilidade
  relevante deve corresponder a uma correção identificável no novo roteiro.
- Não invente recursos, botões ou menus que a ferramenta não possua.

# FORMATO DE SAÍDA
Um único documento Markdown completo, do primeiro contato até os projetos mais
sofisticados cobertos pelo escopo do OBJETO BASE, pronto para ser salvo como
`novo-roteiro-curso-[slug].md`.
```

---
---

# ETAPA 4 — Versões por Trilha

A partir do Roteiro 2.0 (Etapa 3), gera duas versões de leitura direta, em formatos e registros diferentes. As duas usam o mesmo material-fonte e podem ser geradas em qualquer ordem.

## ETAPA 4A — Trilha Hands-on (prática, PBL, 2ª pessoa)

```text
# CONTEXTO
Você atuará como autor de um curso prático no estilo da famosa coleção de
livros "Para Leigos" (For Dummies). Sua tarefa é produzir um curso completo,
em português, no formato de arquivo Markdown, do tipo HANDS-ON: baseado em
exercícios, experimentação e resolução de problemas reais. O curso integra a
trilha "Hands-on".

# ENTRADA / MATERIAL-FONTE
Utilize como material-fonte o Roteiro 2.0 produzido na Etapa 3 deste pipeline
(se estiver em conversa isolada, cole `novo-roteiro-curso-[slug].md` antes de
prosseguir). Utilize o OBJETO BASE definido na seção compartilhada deste
pipeline.

# CONFIGURAÇÃO
- Carga horária: 60 a 90 minutos.
- Número de oficinas práticas: 4 oficinas + 1 projeto final.

# TAREFA
Produza o curso completo respeitando a ESTRUTURA e o ESTILO a seguir. O
princípio condutor é PBL (aprendizagem baseada em problemas): cada oficina
começa com um problema concreto e o participante aprende RESOLVENDO-O com as
próprias mãos.

## ESTRUTURA OBRIGATÓRIA (nesta ordem)
1. TÍTULO — formato "# [OBJETO BASE] Para Leigos — Curso Hands-on", com
   subtítulo curto e encorajador (itálico) prometendo um resultado concreto.
2. SEÇÃO "Antes de Arregaçar as Mangas" — parágrafo curto dizendo o que o
   curso é; lista "O que você precisa ter aberto agora:"; box ">" com ícone 🔑
   explicando a "regra de ouro" do curso.
3. SEÇÃO "O Mapa da Mão na Massa" — tabela (Oficina | O problema que você vai
   resolver | Tempo) + frase sobre a progressão.
4. OFICINAS PRÁTICAS (uma por bloco, na quantidade configurada), cada uma com,
   NESTA ORDEM:
   a. Cabeçalho "# Oficina N — [Nome curto e direto, orientado à ação]".
   b. "### 🎯 O Problema" — 1 parágrafo com situação real e o que será
      resolvido.
   c. "### 🧰 O que você vai usar" — lista enxuta.
   d. "### 👐 Mão na massa" — passos numerados, diretos e acionáveis (verbo no
      início), com o texto exato a digitar em bloco de citação.
   e. "### ✅ Deu certo?" — resultado esperado em 1-2 linhas.
   f. "### 🚑 Se travar" — mini-tabela (Problema | O que fazer) com 2 a 3
      tropeços comuns.
   g. "### 🚀 Quer ir além?" — um desafio extra opcional, de 1 frase.
   - Distribua, com moderação (1-2 por oficina), boxes ">" com os ícones: 💡
     (Dica), ⚠️ (Cuidado), 📌 (Não esqueça), 🤓 (Curiosidade técnica —
     dispensável).
5. PROJETO FINAL — "# Projeto Final — [Nome do entregável]": "### 🎯 A
   missão" (problema maior reunindo as oficinas); "### 👐 Mão na massa"
   (passos encadeados); "### 🏁 Como saber que terminou" (checklist "[ ]").
6. "A Parte dos Dez" — "# A Parte dos Dez — [tema]": 10 dicas práticas e
   independentes; reduza honestamente o número se 10 não se sustentarem.
7. SEÇÃO "Conseguiu! E agora?" — 1-2 parágrafos comemorando o progresso e
   sugerindo como continuar praticando.

## ESTILO OBRIGATÓRIO
- Tom leve, encorajador, bem-humorado na medida certa, sempre respeitoso: o
  leitor é inteligente, apenas novato. Nunca condescendente.
- Fale em 2ª pessoa ("você"). Linguagem simples e cotidiana.
- Zero jargão sem explicação; termo técnico inevitável explica-se na hora, com
  comparação do dia a dia.
- Frases e parágrafos curtos. Priorize o FAZER sobre o explicar.
- Cada oficina entrega uma "pequena vitória" concreta e visível.
- Humor é tempero, não prato principal: no máximo uma piada leve por seção.
- Markdown limpo. Emojis somente nos cabeçalhos e boxes previstos, nunca no
  corpo do texto.

# RESTRIÇÕES
- Cada passo do "Mão na massa" deve ser executável de verdade, na ordem dada,
  sem etapas implícitas omitidas.
- Não invente recursos, botões ou menus que o OBJETO BASE não possua.
- Some os tempos das oficinas dentro da carga horária definida.

# FORMATO DE SAÍDA
Um único documento Markdown completo, pronto para ser salvo como
`hands-on/[slug]-para-leigos-hands-on.md`.
```

## ETAPA 4B — Trilha Essentials (formal, acadêmica, impessoal)

```text
# CONTEXTO
Você atuará como designer instrucional. Sua tarefa é produzir um Plano de Aula
completo, em português, em Markdown, seguindo RIGOROSAMENTE o modelo
estrutural e o estilo descritos abaixo. O plano integra a trilha "Essentials".

Inspire-se na clareza didática da coleção "Para Leigos": pressuponha que o
participante é inteligente, porém inteiramente novato no tema; descomplique
todo termo técnico ao introduzi-lo. IMPORTANTE: essa inspiração refere-se
SOMENTE à acessibilidade do conteúdo. O registro do texto permanece formal,
impessoal e acadêmico — descomplicar não é informalizar. Não use 2ª pessoa
("você"), humor nem gírias.

# ENTRADA / MATERIAL-FONTE
Utilize como material-fonte o Roteiro 2.0 produzido na Etapa 3 deste pipeline
(se estiver em conversa isolada, cole `novo-roteiro-curso-[slug].md` antes de
prosseguir). Utilize o OBJETO BASE definido na seção compartilhada deste
pipeline.

# CONFIGURAÇÃO
- Carga horária: 60 a 90 minutos.
- Natureza: curto, introdutório e prático.
- Número de módulos de conteúdo: 4 módulos + 1 de síntese.

# TAREFA
Produza o Plano de Aula completo respeitando a ESTRUTURA e o ESTILO a seguir.

## ESTRUTURA OBRIGATÓRIA (nesta ordem)
1. TÍTULO — "# Plano de Aula — [OBJETO BASE] (Essentials)".
2. SEÇÃO "Identificação" — tabela (Campo | Definição): Curso, Natureza, Carga
   horária, Público-alvo, Pré-requisitos, Recursos necessários.
3. "### Objetivo Geral" — um parágrafo único, impessoal, com a finalidade e o
   produto final esperado.
4. "### Competências a Desenvolver" — "Concluído o curso, o participante
   deverá demonstrar capacidade de:" + lista numerada com 4 competências.
5. "### Estrutura e Sequência dos Módulos" — parágrafo sobre progressão
   cumulativa + tabela (Módulo | Título | Referência | Tempo).
6. MÓDULOS DE CONTEÚDO (um por bloco, na quantidade configurada), cada um com,
   nesta ordem:
   a. Cabeçalho "# Módulo N — [Título]".
   b. Nota de encadeamento (uma linha, em citação ">"): pré-requisito e
      deslocamento de foco em relação ao módulo anterior (no primeiro,
      indicar que é o ponto de partida).
   c. "### Objetivos de Aprendizagem" — "Ao final deste módulo, o
      participante deverá ser capaz de:" + lista de 3 a 4 objetivos.
   d. "### Texto Descritivo" — 3 a 5 parágrafos em prosa corrida, impessoal e
      de registro formal/acadêmico.
   e. "### Exercício Prático" — título com tempo estimado entre parênteses;
      procedimento numerado OU questão de múltipla escolha; e "Critério de
      êxito" / "Gabarito" / "Fundamentação" explícito.
7. MÓDULO FINAL DE SÍNTESE — "# Módulo [N] — Síntese e Aplicação Integrada",
   mesma estrutura, com Exercício Prático em forma de ATIVIDADE INTEGRADORA
   que articule as competências anteriores, acompanhada de tabela de
   "Critérios de avaliação" (Critério | Atendido?).
8. SEÇÃO "Encerramento" — 2 parágrafos (finalidade cumprida + prática
   regular; caminhos de aprofundamento); citação ">" final iniciada por
   "**Síntese:**".

## ESTILO OBRIGATÓRIO
- Registro formal, impessoal, tom acadêmico. Evite 2ª pessoa e coloquialismos;
  prefira "recomenda-se", "observa-se", "cumpre registrar", "depreende-se",
  "convém".
- Acessibilidade DENTRO do registro formal: explique cada conceito desde a
  base, sem pressupor conhecimento prévio, com analogias formais quando útil.
  Descomplicar não é informalizar.
- Terminologia técnica e precisa; evite gírias e expressões de oralidade.
- Objetivos de aprendizagem mensuráveis ("deverá ser capaz de...").
- Progressão pedagógica visível, porém enxuta.
- Markdown limpo: cabeçalhos, tabelas, listas, citações. Não use negrito em
  excesso. Separe seções e módulos com linhas horizontais ("---").

# RESTRIÇÕES
- Mantenha coerência entre objetivos, texto descritivo e exercício de cada
  módulo.
- Não invente dados factuais sobre o OBJETO BASE; em caso de incerteza, use
  formulações genéricas e indique necessidade de validação.
- Não exceda a carga horária definida na soma dos tempos dos módulos.

# FORMATO DE SAÍDA
Um único documento Markdown completo, pronto para ser salvo como
`essentials/plano-de-aula-[slug]-essentials.md`.
```

---
---

# ETAPA 5 — Versões Prontas para Articulate Rise 360

Reempacota as trilhas 4A e 4B para autoria no Rise 360: cues de montagem `» IA:`, breadcrumbs no lugar de capturas de tela, marcadores de fronteira de lição, e (na Essentials) um fio condutor conceitual entre módulos.

## ETAPA 5A — Hands-on (Rise 360)

```text
# CONTEXTO
Você é um designer instrucional que cria roteiros de cursos práticos
(Hands-on) em português. O roteiro que você produzir será depois convertido
em um curso no Articulate Rise 360. Portanto, além do conteúdo de aula, o
roteiro deve conter anotações de montagem que orientem a ferramenta de
autoria.

O curso é prático e orientado à execução: o participante aprende FAZENDO. A
teoria aparece apenas quando necessária para o próximo passo. Cada oficina
parte de um problema real e entrega uma vitória concreta.

# ENTRADA / MATERIAL-FONTE
Utilize como material-fonte o Roteiro 2.0 produzido na Etapa 3 deste pipeline
(ou, se já gerada, a Etapa 4A). Utilize o OBJETO BASE definido na seção
compartilhada deste pipeline, incluindo pré-requisitos técnicos (softwares,
contas, planos, versões).

# CONFIGURAÇÃO
- Carga horária: 90 a 120 minutos.
- Número de oficinas: 4 + 1 Projeto Final.
- Cada oficina deve ter tempo semelhante; o Projeto Final pode ser maior, sem
  ultrapassar o dobro do tempo de uma oficina.

# TOM E ESTILO
- Leve, encorajador e direto, em 2ª pessoa ("você"), sem perder a precisão
  técnica.
- Todo termo técnico é explicado na hora, com comparação simples.
- Frases e parágrafos curtos. Priorizar o FAZER sobre o explicar.
- Humor com moderação (no máximo uma piada leve por seção).
- Não inventar funcionalidades, botões ou menus que a ferramenta não tenha;
  em caso de incerteza, descrever de forma genérica e sinalizar que deve ser
  conferido.

# ESTRUTURA OBRIGATÓRIA (nesta ordem)
1. Título do curso (#) + subtítulo em itálico prometendo um resultado
   concreto.
2. Seção "Antes de Arregaçar as Mangas": parágrafo do que é o curso; lista "O
   que você precisa ter aberto agora"; box com a "regra de ouro" (emoji 🔑).
3. Seção "O Mapa da Mão na Massa": tabela (Oficina | Problema que vai
   resolver | Tempo) + frase sobre a progressão.
4. Uma OFICINA por bloco, cada uma com, NESTA ORDEM:
   a. Cabeçalho "# Oficina N — [nome curto, orientado à ação]".
   b. "### 🎯 O Problema" — situação real e o que será resolvido.
   c. "### 🧰 O que você vai usar" — lista enxuta.
   d. "### 👐 Mão na massa" — passos numerados, acionáveis; textos a digitar
      em bloco de citação; blocos de código quando necessário.
   e. "### ✅ Deu certo?" — como confirmar o sucesso, em 1-2 linhas.
   f. "### 🚑 Se travar" — tabela (Problema | O que fazer) com 2-3 tropeços
      comuns.
   g. "### 🚀 Quer ir além?" — três desafios opcionais, um por linha.
5. "# Projeto Final — [nome]" — missão maior e autônoma mobilizando as
   competências das oficinas: 🎯 A missão; 👐 Mão na massa; 🏁 Como saber que
   terminou (checklist marcável).
6. "# A Parte dos Dez — [tema]" — dez itens práticos e independentes (reduza
   honestamente se não houver dez itens reais).
7. "## Conseguiu! E agora?" — 1-2 parágrafos de fechamento e próximos passos.

# REGRA DOS BREADCRUMBS (em vez de capturas de tela)
NÃO indique "captura de tela". Sempre que uma instrução envolver navegação em
interface (menu, botão, painel, janela, configuração), descreva o caminho no
formato `Aplicativo > Menu > Submenu > Opção`. Use breadcrumb também em
qualquer passo de média/alta complexidade que possa gerar dúvida de
navegação. Para marcar um resultado a conferir, use um ponto de controle:
"🏁 Ponto de controle: ..." com o caminho onde observá-lo.

# CUES DE MONTAGEM PARA O RISE 360 (» IA:)
Antes de CADA bloco de conteúdo, insira uma anotação iniciada por "» IA:",
dentro de uma citação (>), indicando o TIPO DE BLOCO do Rise e o que
preservar. Essas linhas são instruções de montagem — não são conteúdo para o
participante e devem ser removidas na publicação. Use este mapa de tipos:
- Título/subtítulo do curso → Cover
- Parágrafo explicativo → Text
- Lista de itens / pré-requisitos → List ou Checklist
- Tabela (mapa, comparativo) → Table (ou Tabs / Two-Column quando comparativo)
- Passos numerados (Mão na massa) → Process
- Aviso/dica/regra com emoji (🔑 💡 ⚠️ 📌 🤓) → Statement
- Tabela "Problema/O que fazer" (Se travar) → Accordion (um item por linha)
- Desafios de extensão → Accordion ou List, marcado como OPCIONAL
- Checklist do Projeto Final → Checklist
- Prompt/modelo editável → Statement ou Download, conteúdo verbatim
Inclua travas quando pertinente: "verbatim", "não traduzir termos de
interface", "preservar os breadcrumbs", "preservar o emoji", "marcado como
OPCIONAL", "manter blocos de código sem alteração".

# MARCADORES DE FRONTEIRA DE LIÇÃO
Cada oficina e o Projeto Final devem ser cercados por marcadores explícitos,
para que a IA do Rise trate cada um como UMA lição:
- Logo após o título da oficina:
  > *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina N" — todo o conteúdo até o ▲▲▲ FIM
  correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que
  haja blocos de código no meio. ▼▼▼*
- Imediatamente antes do título da próxima seção:
  > *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina N" — encerre esta lição aqui; o que
  vier a seguir é outra lição. ▲▲▲*
A introdução, a Parte dos Dez e o encerramento NÃO recebem marcadores de
fronteira (mas recebem cues » IA: normalmente).

# REGRAS DE FORMATAÇÃO
- Markdown limpo: cabeçalhos, listas, tabelas curtas e citações para os boxes.
- Emojis apenas nos cabeçalhos de subseção e nos boxes previstos — nunca no
  corpo.
- Modelos editáveis: delimitar com aspas triplas ("""), não crases triplas.
- Cada oficina deve ter tempo estimado, passos numerados e critério de êxito.
- A soma dos tempos deve respeitar a carga horária configurada.

# ATENÇÃO — NÃO CONFUNDIR ESTAS INSTRUÇÕES COM O CONTEÚDO
O tema, os objetivos e o texto do curso vêm do OBJETO BASE e do
material-fonte, NUNCA destas instruções. Não gere um curso sobre "Rise 360"
ou "conversão de roteiros": esses são meios, não o assunto.

# FORMATO DE SAÍDA
Um único documento Markdown completo, com o conteúdo de aula, as cues "» IA:"
antes de cada bloco, os breadcrumbs no lugar de capturas e os marcadores
▼▼▼/▲▲▲ ao redor de cada oficina e do Projeto Final, pronto para ser salvo
como `hands-on/[slug]-hands-on-articulate-rise360.md`.
```

## ETAPA 5B — Essentials (Rise 360)

```text
# CONTEXTO
Você é um designer instrucional que cria planos de aula introdutórios
(trilha "Essentials") em português. O plano que você produzir será depois
convertido em um curso no Articulate Rise 360. Portanto, além do conteúdo de
aula, o plano deve conter anotações de montagem que orientem a ferramenta de
autoria.

O curso é autoinstrucional e tem foco na COMPREENSÃO CONCEITUAL: o
participante entende o que a ferramenta é, para que serve, como funciona e
como usá-la com segurança. Cada módulo aprofunda um aspecto, em progressão
cumulativa.

Inspire-se na clareza didática da coleção "Para Leigos": pressuponha que o
participante é inteligente, porém inteiramente novato no tema; explique cada
conceito desde a base e descomplique todo termo técnico ao introduzi-lo.
IMPORTANTE: essa inspiração refere-se SOMENTE à acessibilidade do conteúdo. O
registro do texto permanece formal, impessoal e acadêmico — descomplicar não
é informalizar. Não use 2ª pessoa ("você"), humor nem gírias.

# ENTRADA / MATERIAL-FONTE
Utilize como material-fonte o Roteiro 2.0 produzido na Etapa 3 deste pipeline
(ou, se já gerada, a Etapa 4B). Utilize o OBJETO BASE definido na seção
compartilhada deste pipeline.

# CONFIGURAÇÃO
- Carga horária: 100 a 130 min.
- Número de módulos de conteúdo: 4 a 6 + 1 módulo de síntese.
- Progressão cumulativa: cada módulo pressupõe o anterior.

# REQUISITOS TÉCNICOS (citar quando aplicável)
Utilize os requisitos técnicos definidos no OBJETO BASE (softwares, planos,
contas, conectividade). Caso o OBJETO BASE seja uma ferramenta de IA, citar:
internet ativa; conta com o plano pago exigido pela ferramenta, quando
aplicável.

# TOM E ESTILO
- Registro formal, impessoal e acadêmico. Prefira "recomenda-se",
  "observa-se", "cumpre registrar", "convém", "depreende-se". Evite a 2ª
  pessoa.
- Acessibilidade dentro do registro formal: explique conceitos desde a base e
  descomplique termos técnicos ao introduzi-los, com analogias formais.
- Terminologia técnica e precisa; sem gírias, humor ou oralidade.
- Objetivos de aprendizagem mensuráveis ("o participante deverá ser capaz
  de...").
- Não inventar dados nem funcionalidades; em caso de incerteza, manter
  formulação genérica e indicar a necessidade de validação.

# ESTRUTURA OBRIGATÓRIA (nesta ordem)
1. Título "# Plano de Aula — [Tema] (Essentials)".
2. "## Identificação" — tabela (Campo | Definição): Curso, Natureza
   (autoinstrucional), Carga horária, Público-alvo, Pré-requisitos, Recursos
   necessários.
3. "### Objetivo Geral" — um parágrafo impessoal com a finalidade e o
   produto final.
4. "### Competências a Desenvolver" — "Concluído o curso, o participante
   deverá demonstrar capacidade de:" + lista numerada (uma competência por
   módulo de conteúdo).
5. "### Estrutura e Sequência dos Módulos" — parágrafo sobre a progressão
   cumulativa + tabela (Módulo | Título | Referência | Tempo).
6. Um MÓDULO por bloco, cada um com, NESTA ORDEM:
   a. Cabeçalho "# Módulo N — [Título]".
   b. Nota de encadeamento em citação (>), em uma linha: pré-requisito e
      deslocamento de foco em relação ao módulo anterior (no primeiro,
      indicar que é o ponto de partida).
   c. "### Objetivos de Aprendizagem" — "Ao final deste módulo, o
      participante deverá ser capaz de:" + lista de 3 a 4 objetivos
      mensuráveis.
   d. "### Texto Descritivo" — 3 a 5 parágrafos em prosa formal,
      descomplicando os termos técnicos ao introduzi-los.
   e. "### Exercício Prático" — título com tempo estimado; procedimento
      numerado OU questão de múltipla escolha; "Critério de êxito" /
      "Gabarito" / "Fundamentação".
   f. "### Mão na massa" — um prompt-base editável para o participante
      adaptar.
7. "# Módulo [N] — Síntese e Aplicação Integrada" — mesma estrutura; o
   Exercício Prático é uma ATIVIDADE INTEGRADORA que articula as competências
   anteriores, com tabela de "Critérios de avaliação" (Critério | Atendido?).
8. "# Encerramento" — dois parágrafos (finalidade cumprida + prática
   regular; caminhos de aprofundamento) e uma citação final iniciada por
   "**Síntese:**".

# FIO CONDUTOR
Sempre que um conceito relevante for retomado adiante, plante-o em um módulo
inicial e retome-o no módulo pertinente, tornando a conexão explícita (ex.:
um conceito de infraestrutura ou funcionamento interno da ferramenta,
plantado cedo, retomado no módulo de segurança/acessibilidade).

# REGRA DOS BREADCRUMBS (em vez de capturas de tela)
NÃO indique "captura de tela". Sempre que uma instrução envolver navegação em
interface (menu, botão, painel, janela, configuração), descreva o caminho no
formato `Aplicativo > Menu > Submenu > Opção`. Para resultados a conferir, use
um ponto de controle: "🏁 Ponto de controle: ..." com o caminho onde
observá-lo. Procedimentos com várias telas podem ser apresentados como
sequência de etapas, cada uma com seu breadcrumb.

# CUES DE MONTAGEM PARA O RISE 360 (» IA:)
Antes de CADA bloco de conteúdo, insira uma anotação iniciada por "» IA:",
dentro de uma citação (>), indicando o TIPO DE BLOCO do Rise e o que
preservar. Essas linhas são instruções de montagem — não são conteúdo para o
participante e devem ser removidas na publicação. Use este mapa:
- Título/subtítulo do curso → Cover
- Objetivos de aprendizagem → List (verbatim, sem acréscimos)
- Texto Descritivo → Text (pode dividir em blocos menores; não resumir)
- Exercício (procedimento) → Process ou Checklist; gabarito/critério →
  Statement
- Questão de múltipla escolha → Knowledge Check
- Aviso/dica/caminho com emoji (🧭 🔑 💡 ⚠️ 📌) → Statement
- Tabela comparativa → Table, Tabs ou Two-Column
- Tabela de critérios de avaliação → Checklist ou Table
- Prompt/modelo da "Mão na massa" → Statement ou Download, conteúdo verbatim
Inclua travas quando pertinente: "verbatim", "não traduzir termos de
interface", "preservar os breadcrumbs", "preservar o emoji", "manter blocos
de código sem alteração".

# MARCADORES DE FRONTEIRA DE LIÇÃO
Cada módulo (incluindo o de síntese) deve ser cercado por marcadores
explícitos, para que a IA do Rise trate cada um como UMA lição:
- Logo após o título do módulo:
  > *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo N" — todo o conteúdo até o ▲▲▲ FIM
  correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que
  haja títulos dentro de exemplos de código. ▼▼▼*
- Imediatamente antes do título da próxima seção:
  > *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo N" — encerre esta lição aqui; o que
  vier a seguir é outra lição. ▲▲▲*
A Identificação inicial e o Encerramento NÃO recebem marcadores de fronteira
(mas recebem cues » IA: normalmente).

# ATENÇÃO — NÃO CONFUNDIR ESTAS INSTRUÇÕES COM O CONTEÚDO
O tema, os objetivos e o texto do curso vêm do OBJETO BASE e do
material-fonte, NUNCA destas instruções. Não gere um curso sobre "Rise 360"
ou "conversão de roteiros": esses são meios, não o assunto.

# REGRAS DE FORMATAÇÃO
- Markdown limpo: cabeçalhos, listas numeradas, tabelas curtas e citações
  para os boxes.
- Emojis apenas nos cabeçalhos previstos e nos boxes (🧭 🏁 e afins) — nunca
  no corpo.
- Modelos editáveis: delimitar com aspas triplas ("""), não crases triplas.
- Cada exercício deve ter tempo estimado e critério de êxito objetivo.
- A soma dos tempos deve respeitar a carga horária configurada.

# FORMATO DE SAÍDA
Um único documento Markdown completo, do título ao encerramento, com o
conteúdo de aula, as cues "» IA:" antes de cada bloco, os breadcrumbs no
lugar de capturas e os marcadores ▼▼▼/▲▲▲ ao redor de cada módulo, pronto
para ser salvo como
`essentials/plano-de-aula-[slug]-essentials-articulate-rise360.md`.
```

---
---

## Resultado Final Esperado

Ao concluir as sete gerações (Etapas 1, 2, 3, 4A, 4B, 5A, 5B), o projeto deve conter:

- [ ] `roteiro-curso-[slug].md` — curso "Para Leigos" completo, do zero.
- [ ] `ANALISE_CRITICA_[SLUG].md` — auditoria 360° do roteiro acima.
- [ ] `novo-roteiro-curso-[slug].md` — versão 2.0, reconstruída com todas as correções da auditoria.
- [ ] `essentials/plano-de-aula-[slug]-essentials.md` — plano de aula formal, trilha Essentials.
- [ ] `essentials/plano-de-aula-[slug]-essentials-articulate-rise360.md` — mesma trilha, pronta para o Rise 360.
- [ ] `hands-on/[slug]-para-leigos-hands-on.md` — curso prático em oficinas, trilha Hands-on.
- [ ] `hands-on/[slug]-hands-on-articulate-rise360.md` — mesma trilha, pronta para o Rise 360.

Todos os seis arquivos de curso derivam da mesma fonte auditada (Etapa 3), garantindo consistência de conteúdo entre as quatro versões finais, ainda que em registros e formatos diferentes.
