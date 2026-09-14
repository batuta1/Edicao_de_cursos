<link rel="stylesheet" href="../.css/style.css">

# Prefácio

Imagine que você contratou um roteirista e designer experiente. Você descreve a ideia, o público e os objetivos. Ele estrutura tudo: sequência lógica, hierarquia visual, notas para sua fala, até sugere cores e estilos. Você revisa, ajusta e aprova. O resultado? Uma apresentação que parece ter levado semanas, mas foi criada em horas.

Este é o [Claude](#glos-claude) para [PowerPoint](#glos-powerpoint): não um gerador automático de slides, mas um **parceiro criativo** que você pode interrogar, direcionar e refinar para produzir apresentações de qualidade profissional em uma fração do tempo tradicional.

Este e-book foi concebido para **docentes, comunicadores corporativos e criadores de conteúdo** com pouco ou nenhum contato prévio com [IA Generativa](#glos-ia-generativa). Ao longo dos módulos, você vai aprender não apenas a usar ferramentas, mas a **pensar como um designer** usando a inteligência artificial como colaboradora.

---

**Como usar este livro**

Cada capítulo é independente, mas eles formam uma jornada progressiva. Se você está começando do zero, siga a ordem natural. Se já tem alguma experiência, use os *breadcrumbs* no início de cada seção para navegar diretamente ao que precisa.

Ao final de cada módulo, há uma **Pílula Hands-on** — um exercício prático de 2 a 15 minutos que você pode fazer imediatamente. Não pule essas seções: elas são onde o aprendizado real acontece.

---

# Capítulo 0 — Primeiros Passos: Acessando o Claude no PowerPoint

## O Que Você Vai Precisar

*PowerPoint > Conta Microsoft > Verificar Compatibilidade*

Antes de criar qualquer apresentação, precisamos garantir que você consiga acessar a ferramenta. Este módulo existe por uma razão simples: a maior barreira para usar novas tecnologias não é a dificuldade de uso — é a fricção de acesso. Vamos eliminá-la agora.

### Versões Compatíveis do PowerPoint

| Plataforma | Versão | Compatibilidade | Claude Disponível? |
|-----------|--------|-----------------|-------------------|
| PowerPoint Web | Qualquer | ✅ Completa | ✅ Sim (via Microsoft 365) |
| Windows Desktop | Microsoft 365 (atualizado) | ✅ Sim | ✅ Sim (versão 2405+) |
| Mac Desktop | Microsoft 365 (atualizado) | ✅ Sim | ✅ Sim (versão 16.80+) |
| PowerPoint 2019/2016 | Legacy | ❌ Não recomendado | ❌ Não suportado |
| iPad / Android | Mobile | ❌ Limitada | ❌ Não disponível |

Para usar o Claude, você precisa de uma conta [Microsoft 365](#glos-microsoft365) ativa com assinatura vigente, conexão de internet estável (Claude processa em nuvem), e um navegador moderno como Chrome, Edge ou Safari se optar pela versão Web.

---

## Guia Passo a Passo por Plataforma

*PowerPoint Web > Painel Lateral > Complemento Claude*

Dependendo de como você acessa o PowerPoint, o caminho para encontrar o Claude é um pouco diferente. Veja os três cenários mais comuns.

### Cenário A: PowerPoint Web

Acesse [office.com](https://office.com) com sua conta Microsoft e abra uma apresentação — nova ou existente. No painel direito, procure por um ícone ou botão chamado **"Claude"** ou **"Designer com IA"**. Clique nele, autorize o complemento quando a caixa de diálogo aparecer, e comece. É isso.

📸 **Sugestão de Print:** Interface do PowerPoint Web com painel lateral direito destacando o ícone Claude

### Cenário B: PowerPoint Desktop (Windows ou Mac)

Primeiro, verifique se há atualizações pendentes. No Windows: *Arquivo → Conta → Sobre → Verificar Atualizações*. No Mac: *PowerPoint → Verificar Atualizações*. Após atualizar, abra uma apresentação e procure na fita (*ribbon*) por uma aba chamada **"Designer"** ou **"Claude"** — geralmente aparece após "Inserir". Clique nela e o painel Claude surgirá à direita.

📸 **Sugestão de Print:** Fita do PowerPoint Desktop com aba "Designer" destacada em vermelho

### Cenário C: O Complemento Não Aparece

Não se preocupe — isso é mais comum do que parece. Consulte a tabela de soluções abaixo:

| Problema | Solução |
|---------|---------| 
| "Não vejo o complemento" | Verifique se Microsoft 365 está atualizado. Pode levar 24h para aparecer. |
| "Erro de autenticação" | Faça logout do Office → Limpe o cache → Faça login novamente. |
| "PowerPoint trava ao usar Claude" | Feche abas e extensões do navegador que consomem memória. |
| "Claude demora muito" | Simplifique o [prompt](#glos-prompt). Textos muito longos levam mais tempo. |

---

## Primeiro Teste: Verifique se Está Funcionando

*PowerPoint > Painel Claude > Caixa de Input*

Antes de avançar, confirme que tudo está funcionando com este exercício rápido:

1. Abra o PowerPoint (Web ou Desktop)
2. Crie um novo slide em branco
3. Clique no painel Claude
4. Escreva este comando simples:

```md
Crie um título criativo para uma apresentação sobre produtividade.
```

5. Pressione Enter ou Send

**Resultado esperado:** Claude deve responder com 3 a 5 sugestões de títulos em segundos.

Se viu o resultado → ✅ **Parabéns! Você está pronto para o curso.**

Se não viu nada → Volte à tabela de *troubleshooting* da seção anterior ou contate o suporte técnico da sua instituição.

### A Interface do Claude: Mapa Visual

O painel lateral do Claude tem uma estrutura simples que você vai usar constantemente:

```
┌─────────────────────────────────┐
│  [Histórico da Conversa]        │
│  ├─ Sua pergunta anterior       │
│  ├─ Resposta do Claude          │
│  └─ ...                         │
├─────────────────────────────────┤
│  [Caixa de Input]               │
│  Seu prompt aqui...       [↑]   │
└─────────────────────────────────┘
```

Antes de começar o próximo capítulo, confirme cada item da lista abaixo:

```md
[ ] Consigo acessar o PowerPoint (Web, Desktop ou ambos)
[ ] Vejo o painel Claude no lado direito
[ ] Consegui enviar um prompt simples
[ ] Recebi uma resposta do Claude em menos de 10 segundos
[ ] Entendo que Claude processa em servidores remotos (não localmente)
```

Se todos os itens estão marcados, você está **100% pronto**. Prossiga para o Capítulo 1.

---

# Capítulo 1 — O Claude Entrou na Sala: Entendendo Seu Novo Parceiro Criativo

## A Ilusão Antiga e a Realidade Nova

*Claude AI > Painel de Chat > Primeira Interação*

Existe uma armadilha que pega quase todo mundo na primeira vez que usa uma IA generativa para criar slides. A pessoa abre o Claude, escreve "faça uma apresentação sobre X", cola o resultado no PowerPoint e entrega. O slide fica genérico, sem personalidade, e parece exatamente o que é: feito por IA sem curadoria humana.

O problema não é a ferramenta. É o paradigma. A mentalidade correta não é "Claude gera, eu copio". É **"Claude estrutura, eu refino, juntos criamos algo único"**.

A diferença de resultado entre essas duas abordagens é enorme. No primeiro caso, você tem slides que qualquer pessoa com acesso ao mesmo prompt geraria. No segundo, você tem uma apresentação com a sua voz, os seus exemplos, o contexto dos seus alunos — apenas construída em uma fração do tempo.

---

## Os 5 Superpoderes do Claude para Apresentações

*Claude AI > Engenharia de Prompt > Casos de Uso*

Saber onde o Claude agrega valor máximo é o primeiro passo para usá-lo bem. Pense nos cinco papéis que ele pode assumir na sua criação.

### 1. Roteirista: Estrutura Lógica

Claude transforma uma descrição vaga numa sequência narrativa inteligente:

```md
ENTRADA: "Preciso falar sobre ciclo da água para crianças de 6º ano"
SAÍDA: Sequência de 6 slides com abertura, desenvolvimento gradual,
       exemplo prático, atividade interativa e fechamento
```

### 2. Curador: Simplifica Conteúdo Denso

Quando você tem um texto acadêmico longo e precisa transformá-lo em algo didático:

```md
ENTRADA: Texto acadêmico de 2000 palavras sobre mitose celular
SAÍDA: 5 bullet points claros + 2 analogias simples + 1 pergunta provocativa
```

### 3. Roteirista de Fala: Expande Títulos em Narrativas

Claude consegue tomar o título de um slide e transformá-lo em roteiro de fala:

```md
ENTRADA: Título do slide "A importância da biodiversidade"
SAÍDA: Roteiro de fala natural de 2 minutos com tons de conversa,
       exemplos locais e pausas para perguntas
```

### 4. Estrategista Visual: Sugere Estruturas e Layouts

Quando você sabe o que quer mostrar, mas não sabe como organizar visualmente:

```md
ENTRADA: "Preciso comparar 3 métodos de aprendizado"
SAÍDA: Sugestão de layout (3 colunas lado a lado, timeline ou Diagrama de Venn)
```

### 5. Gerador de Briefs Visuais: Descreve Imagens para Bancos de Dados

Claude não cria imagens, mas descreve com precisão o que você precisa buscar:

```md
ENTRADA: "Preciso uma imagem de um ecossistema saudável"
SAÍDA: Descrição detalhada para usar no Unsplash, Pexels ou DALL-E
```

---

## O Que Claude NÃO Faz

*Claude AI > Sobre o Claude > Limitações*

É igualmente importante saber onde o Claude não vai te ajudar — e por que isso está completamente bem.

Claude não cria imagens (use [DALL-E](#glos-dalle), Midjourney ou Unsplash para isso). Ele não garante precisão histórica ou científica absoluta — você valida. Ele não conhece seus alunos específicos — você personaliza. Ele não tem gosto artístico objetivo — você decide a estética. E ele não entende nuances culturais do seu contexto local — você adapta.

Reconhecer essas limitações não é uma crítica à ferramenta. É o que te torna um usuário avançado: você usa Claude exatamente onde ele brilha e assume o controle onde ele não alcança.

---

## A Mentalidade de Colaboração

*Claude AI > Painel de Chat > Ciclo de Iteração*

Pense no Claude como um ciclo contínuo de colaboração, não como uma máquina de fazer slides:

```
Você (Ideia + Objetivo) → Claude (Estrutura + Rascunho)
→ Você (Refinamento + Personalização) → Claude (Iteração)
→ Você (Aprovação + Ajustes Finais) → Resultado Profissional
```

### Pílula Hands-on — Mão na Massa

**Tempo estimado:** 3 minutos

Abra Claude (no PowerPoint ou em [claude.ai](https://claude.ai)) e envie este prompt adaptado para a sua realidade:

```md
Sou professor de [SUA DISCIPLINA] e preciso criar uma apresentação
sobre [TEMA] para alunos do [ANO/SÉRIE]. O objetivo é
[EXPLICAR / REVISAR / INTRODUZIR / OUTRO].

O que você sugere como estrutura para os slides?
```

Observe a resposta com curiosidade. Claude vai sugerir uma sequência lógica considerando o nível cognitivo do seu público. Concorda com a estrutura? O que mudaria? Essa divergência — a sua perspectiva corrigindo e enriquecendo o rascunho da IA — é exatamente onde a magia acontece.

---

# Capítulo 2 — Antes de Pedir: Preparando Seu Projeto

## O Briefing: Sua Bússola

*Claude AI > Engenharia de Prompt > Contextualização*

Um dos erros mais comuns ao usar Claude é começar a digitar sem saber exatamente o que se quer. O resultado? Uma resposta genérica que você vai precisar reformular várias vezes. A solução é simples: antes de qualquer [prompt](#glos-prompt), responda estas sete perguntas fundamentais.

```md
1. OBJETIVO: O que quero que alunos aprendam ou façam após a aula?
2. PÚBLICO: Qual é a idade, nível escolar, conhecimento prévio?
3. CONTEXTO: Onde isso se encaixa no currículo? É primeira aula ou revisão?
4. DURAÇÃO: Quantos minutos terei para apresentar?
5. FORMATO: Quantos slides? Há limitações técnicas?
6. ATIVIDADE: Que atividade ou pergunta vai engajar os alunos?
7. CONSTRAINTS: Há tópicos a evitar ou formatos específicos obrigatórios?
```

📸 **Sugestão de Print:** Template preenchido com exemplo real (ciclo da água, 6º ano, 20 minutos)

Esse documento — seu [briefing](#glos-briefing) — é o ponto de partida de tudo. Guarde-o. Você vai usá-lo nos prompts dos próximos módulos.

---

## Estruturação de Conteúdo: A Pirâmide de Informação

*Claude AI > Engenharia de Prompt > Estrutura de Conteúdo*

O Claude respeita hierarquia. Quando você organiza seu conteúdo em camadas antes de pedir, a resposta reflete essa organização. Um exemplo de como estruturar o tema "Alimentação Saudável":

```md
TÓPICO GERAL: Alimentação Saudável

├─ CONCEITO PRINCIPAL 1: Grupos de Alimentos
│  ├─ Detalhes: Proteínas, Carboidratos, Gorduras
│  └─ Exemplos: Frango (proteína), Pão (carboidrato)
│
├─ CONCEITO PRINCIPAL 2: Proporções Corretas
│  ├─ Detalhes: 50% vegetais, 25% proteína, 25% carboidrato
│  └─ Exemplos: [imagem de prato equilibrado]
│
└─ CONCEITO PRINCIPAL 3: Hábitos Diários
   ├─ Detalhes: Hidratação, intervalos entre refeições
   └─ Exemplos: Beber 2 litros de água, comer a cada 3 horas
```

Quando você passa essa estrutura para o Claude, ele a usa como esqueleto da apresentação — e o resultado é muito mais próximo do que você precisava.

---

## Persona do Aluno: Conheça Seu Público

*Claude AI > Engenharia de Prompt > Definição de Público*

A descrição do seu público é onde a maioria das pessoas é vaga demais. Compare:

❌ **Genérico:** "Para crianças de 6º ano"

✅ **Específico:** "Alunos de 6º ano (11–12 anos), escola em periferia de São Paulo, maioria nunca viu um microscópio, 60% tem acesso a smartphone em casa, nível de atenção: 20–25 minutos."

Claude **ajusta linguagem, ritmo e exemplos** baseado nessas informações. Quanto mais específico você for sobre o seu público, mais personalizada e útil será a resposta.

### Pílula Hands-on — Mão na Massa

**Tempo estimado:** 5 minutos

Preencha o template abaixo para a sua próxima aula. Você vai usá-lo no Capítulo 3.

```md
## MINHA APRESENTAÇÃO

**Objetivo:** [O que quero que alunos aprendam?]

**Público:** [Idade, série, contexto, conhecimento prévio]

**Duração:** [Quantos minutos?]

**Número de slides:** [5? 10? 15?]

**Estrutura de conteúdo:**
- Conceito 1: [Nome]
  - Detalhes: [...]
  - Exemplos: [...]
- Conceito 2: [Nome]
  - Detalhes: [...]
  - Exemplos: [...]

**Atividade de participação:** [Quiz? Debate? Brainstorm?]

**Restrições:** [Deve evitar...? Deve incluir...?]
```

---

# Capítulo 3 — O Prompt é o Bilhete: Pedindo ao Claude de Forma Estratégica

## Anatomia de um Prompt Excelente

*Claude AI > Engenharia de Prompt > Estrutura de Prompt*

Um [prompt](#glos-prompt) é muito mais do que uma pergunta. É uma instrução de trabalho. E como toda instrução, a clareza faz toda a diferença entre um entregável mediano e um resultado excelente.

A fórmula básica é simples:

```md
[CONTEXTO] + [TAREFA] + [FORMATO] + [RESTRIÇÕES] = PROMPT PODEROSO
```

Vamos dissecar cada componente.

### Componente 1: CONTEXTO

Quem é você? Qual é a situação?

```md
❌ Fraco:
"Preciso de slides sobre água"

✅ Forte:
"Sou professora de Ciências em escola pública, ensinando para crianças de 6º
ano que nunca tiveram aula prática de laboratório. Preciso introduzir o
conceito de ciclo da água."
```

### Componente 2: TAREFA

O que, exatamente, você quer que Claude faça?

```md
❌ Fraco:
"Faça uma apresentação"

✅ Forte:
"Crie uma estrutura de 6 slides que mostre as 4 etapas do ciclo da água
(evaporação, condensação, precipitação, escoamento)"
```

### Componente 3: FORMATO

Como você quer o resultado?

```md
❌ Fraco:
"Estrutura de apresentação"

✅ Forte:
"Para cada slide, forneça:
   1. Título do slide
   2. Bullet points (máximo 4, máximo 10 palavras cada)
   3. Uma atividade ou pergunta para engajar alunos
   4. Sugestão de imagem ou diagrama"
```

### Componente 4: RESTRIÇÕES

O que evitar? O que é obrigatório?

```md
❌ Fraco:
"Mantenha simples"

✅ Forte:
"Use linguagem adequada para 11-12 anos (evite jargão científico). Inclua
pelo menos um exemplo do dia a dia (ex: chuva, roupa molhada secando).
Evite gráficos muito complexos."
```

---

## Template Universal para Prompts de Apresentação

*Claude AI > Engenharia de Prompt > Templates*

Use este template como base para qualquer prompt de apresentação que você criar:

```md
# CONTEXTO
Sou [profissão] em [ambiente]. Meu público é [descrição detalhada do aluno].
Contexto: [onde isso se encaixa no currículo?].

# TAREFA
Preciso que você [ação específica]: [detalhes].

# FORMATO
Estruture o resultado assim:
[descreva exatamente como quer o output]

# RESTRIÇÕES & PREFERÊNCIAS
- Deve: [obrigações]
- Não deve: [proibições]
- Tom: [formal/casual/lúdico/etc]
- Nível de profundidade: [introdutório/intermediário/avançado]

# EXEMPLOS (opcional, mas poderoso)
[Mostrar 1-2 exemplos de saída ideal]
```

---

## Prompt Interativo e Iterativo: A Técnica dos Turnos

*Claude AI > Painel de Chat > Conversa Multi-turno*

Claude não lê mentes. Raramente um único prompt gera o resultado perfeito — e tudo bem, porque a força da [IA Generativa](#glos-ia-generativa) está exatamente na iteração rápida. Um bom fluxo de trabalho tem múltiplos turnos:

**Turno 1 — Estrutura Geral:**
```md
Estruture uma apresentação sobre fotossíntese para 8º ano com 5 slides.
Apenas os títulos e tópicos principais, sem textos completos.
```

Claude responde com uma versão rascunho.

**Turno 2 — Refinamento:**
```md
Ótimo! Agora:
1. Adicione uma pergunta provocativa no Slide 1
2. Mude o Slide 3 para incluir um experimento que alunos podem fazer em casa
3. Torne a linguagem mais simples — como se explicasse para um colega, não para um livro
```

Claude refina.

**Turno 3 — Expansão:**
```md
Agora expanda cada slide com notas de fala de 1-2 minutos.
Use tom conversacional. Inclua pausas para perguntas.
```

📸 **Sugestão de Print:** Diálogo mostrando 3 turnos de prompt/resposta no painel Claude do PowerPoint

---

## Técnicas Avançadas de Prompt

*Claude AI > Engenharia de Prompt > Técnicas Avançadas*

Três técnicas de [prompt engineering](#glos-prompt-engineering) vão elevar a qualidade das suas respostas significativamente.

### Chain-of-Thought: Pedir para Claude Pensar em Voz Alta

```md
Antes de criar os slides, pense em voz alta:
1. Qual é o conceito-chave que alunos precisam entender?
2. Qual é o equívoco mais comum que eles têm?
3. Qual é a melhor sequência para desconstruir esse equívoco?

Baseado nessa análise, crie a estrutura de 4 slides.
```

### Few-Shot: Mostrar Exemplos do Que Você Quer

```md
Aqui estão 2 exemplos de como gosto que bullets sejam escritos:

EXEMPLO 1: "Água evaporada em oceanos sobe (invisível)"
EXEMPLO 2: "Gotículas formam nuvens em altitudes frias"

Agora crie 4 bullets assim para o tema "Condensação".
```

### Role-Playing: Pedir para Claude Assumir um Papel

```md
Você é um professor de ciências extremamente criativo que consegue explicar
tópicos complexos usando apenas analogias com coisas do dia a dia dos alunos
(comida, celular, esportes, etc.).

Crie uma abertura de slide sobre "Mitose" usando 2-3 analogias simples.
```

### Pílula Hands-on — Mão na Massa

**Tempo estimado:** 5 minutos

Pegue o briefing que você preencheu no Capítulo 2, converta-o para o template de prompt desta seção, e teste no Claude. Não precisa ser perfeito na primeira vez — o objetivo é ver como um prompt bem estruturado gera um output melhor do que um pedido genérico.

---

# Capítulo 4 — Estruturando a Narrativa: Do Zero ao Deck Coerente

## As Estruturas de Narrativa Mais Eficazes para Educação

*Claude AI > Engenharia de Prompt > Narrativa e Estrutura*

Toda apresentação memorável tem uma espinha dorsal narrativa. Slides sem essa estrutura são apenas uma lista de informações. Slides com ela são uma jornada que o aluno percorre junto com você.

Existem três arquiteturas narrativas que funcionam especialmente bem em contextos educativos.

### Estrutura 1: Problema → Solução → Ação

```
ABERTURA: Contexto / Pergunta Provocativa
         ↓
DESENVOLVIMENTO: Entender o Problema (detalhes, causas)
         ↓
CLÍMAX: A Solução / A Ideia Central
         ↓
APLICAÇÃO: Como usar isso? Exemplo prático
         ↓
FECHAMENTO: Call-to-action (reflita, experimente, converse)
```

Aplicado a fotossíntese: Slide 1 pergunta "Por que as plantas precisam de luz?"; Slides 2 e 3 explicam o mecanismo; Slide 4 apresenta a fórmula central como *aha moment*; Slide 5 mostra uma estrutura real ao microscópio; Slide 6 propõe um experimento.

### Estrutura 2: O Aluno como Herói

Nesta abordagem, o protagonista da narrativa não é o conteúdo — é o próprio aluno em uma jornada de descoberta:

```
1. O Mundo Comum: "Você já viu uma nuvem?"
2. O Chamado: "Quer entender como ela se forma?"
3. Os Desafios: "Parece fácil, mas tem 3 etapas"
4. O Aprendizado: "Aqui estão as etapas"
5. O Retorno: "Agora você pode prever quando vai chover"
```

### Estrutura 3: Curiosidade → Suspense → Revelação

```
Slide 1: "Por que o céu é azul?" (Desperta curiosidade)
Slide 2: "A maioria acha que é..." (Expectativa)
Slide 3: "Mas na verdade..." (Revelação)
Slide 4: "Veja a prova:" (Validação)
Slide 5: "Agora quando olhar para o céu..." (Aplicação pessoal)
```

---

## A Throughline: O Fio Condutor da Apresentação

*Claude AI > Engenharia de Prompt > Coesão Narrativa*

Uma boa apresentação tem **UMA ideia central**. Todos os slides servem para reforçá-la. Quando um slide não contribui para esse fio condutor, ele está sobrando — ou desviando atenção.

Veja a diferença:

**Throughline fraca:**
Slide 1: "Fotossíntese" → Slide 2: "Estrutura das plantas" → Slide 3: "Ciclo da água" → Slide 4: "Energia". O aluno fica confuso — parece que são quatro aulas diferentes.

**Throughline forte:**
Tema central: *"Como as plantas transformam luz em comida"*. Cada slide é um passo dessa transformação, do início ao fim. O aluno sai com uma ideia clara, coerente e memorável.

---

## Abertura Memorável e Fechamento Impactante

*Claude AI > Engenharia de Prompt > Abertura e Fechamento de Apresentação*

A abertura decide se os alunos prestam atenção. O fechamento decide se vão lembrar do que aprenderam. Não subestime nenhum dos dois.

### Tipos de Abertura Eficazes

**Pergunta Provocativa:**
```md
"Se eu apagar a luz desta sala agora, as plantas vão parar de fabricar
comida imediatamente. Ou não? Alguém sabe a resposta?"
```

**Contradição / Surpresa:**
```md
"Vocês acham que plantas comem terra. Por isso plantamos em terra, certo?
Errado. A terra é só suporte. A comida da planta vem do AR e da LUZ."
```

**Conexão Pessoal:**
```md
"Quem aqui tem planta em casa? Já parou para pensar o que ela está fazendo
agora enquanto estamos em aula? Ela está fabricando seu próprio alimento."
```

### Prompt para Gerar Aberturas com Claude

```md
Crie 3 aberturas diferentes (pergunta provocativa, contradição, demonstração)
para uma aula sobre [TEMA] para [PÚBLICO].

Cada abertura deve:
- Levar no máximo 30 segundos para falar
- Prender atenção imediatamente
- Deixar o aluno curioso para os próximos slides

Formate assim:
ABERTURA 1 [Tipo]: [Texto de fala]
---
```

### Tipos de Fechamento Impactante

**Call-to-Action Simples:** "O desafio é: crie um experimento para testar isso em casa."

**Reflexão Pessoal:** "A próxima vez que olhar uma árvore, saiba que ela está fazendo em segundos o que levaria um químico horas para replicar em laboratório."

**Conexão com o Futuro:** "Cientistas estão tentando copiar a fotossíntese artificial para gerar energia limpa. Você poderia ser aquele que resolve este problema."

### Pílula Hands-on — Mão na Massa

**Tempo estimado:** 8 minutos

Escolha um tema que está ensinando. Escreva 3 aberturas diferentes usando os tipos descritos acima. Teste qual soaria mais natural na sua voz. Depois, escreva o fechamento que corresponderia à abertura escolhida. Esses dois elementos — gancho inicial e encerramento forte — são o que separa uma boa apresentação de uma excelente.

---

# Capítulo 5 — Notas do Orador: Expandindo Bullets em Narrativa Natural

## Por Que Notas de Orador São Críticas

*PowerPoint > Exibição > Notas*

Existe um fenômeno que todo professor conhece: você estava seguro do conteúdo, preparou os slides, chegou na frente da turma — e quando olhou para o terceiro bullet, a mente foi em branco. É a síndrome do "ah, era pra falar o quê mesmo?".

As [notas do orador](#glos-notas-orador) são a solução. Não são um script para ler em voz alta — são um roteiro de segurança que você usa para nunca perder o fio. Com elas, você fala naturalmente, parece preparado sem parecer mecânico, e a apresentação flui como uma conversa.

---

## Estrutura de Notas do Orador Eficaz

*PowerPoint > Painel de Notas > Campo de Texto*

Uma boa nota de orador para cada slide segue este padrão:

```md
[TIMING: X minutos]

[ABERTURA — gancho visual ou emocional]

[DESENVOLVIMENTO — conteúdo expandido]
- Exemplo 1: [detalhe]
- Exemplo 2: [detalhe]
- Por que isso importa: [conexão pessoal]

[PAUSA E PERGUNTA RETÓRICA]
"Vocês já pararam para pensar em...?"
[pausa de 5 segundos]

[TRANSIÇÃO PARA PRÓXIMO SLIDE]
"Agora que sabemos X, vamos ver como Y se conecta..."
```

---

## Técnica: Expandir Bullets em Narrativa

*Claude AI > Engenharia de Prompt > Expansão de Conteúdo*

Veja na prática como um bullet crú se transforma numa nota de orador completa:

❌ **Bullet crú:**
```md
• Fotossíntese = Luz + Água + CO2 → Glicose + O2
```

✅ **Nota de orador expandida:**
```md
[TIMING: 2 minutos]

Então aqui está a fórmula mágica. Não é mágica de verdade, é química —
mas parece mágica.

Peguem a fórmula do slide: Luz mais Água mais Dióxido de Carbono resulta
em Glicose mais Oxigênio.

Traduzindo em linguagem simples:
- Luz vem do sol
- Água entra pelas raízes
- CO2 entra pelos poros da folha (invisível, mas está no ar)
- A planta mistura tudo
- Sai glicose (açúcar, comida para ela crescer)
- Sai oxigênio — aquilo que VOCÊ respira

Espera... a planta está fabricando o oxigênio que você respira.

[pausa de 3 segundos]

Você está vivo porque as plantas fazem essa fórmula. Todos os dias.
Trilhões de plantas em todo o planeta fazendo isso agora.

[Aponta para o slide] Memorize esta fórmula. Ela é a razão de você existir.

[PONTE PARA PRÓXIMO SLIDE]
Agora a pergunta é: como a planta FAZ essa fórmula? Que passos ela segue?
```

---

## Prompt para Claude Gerar Notas do Orador

*Claude AI > Engenharia de Prompt > Roteiro de Fala*

```md
# Contexto
[Seu briefing + nível de alunos]

# Tarefa
Expanda cada ponto em NOTAS DO ORADOR. Não bullets adicionais —
texto narrativo que eu possa ler naturalmente.

# Formato
Para cada slide:
[TIMING: X minutos]
[Texto de abertura/gancho]
[Desenvolvimento expandido — 80-120 palavras]
[Pausa e pergunta retórica — 1 linha]
[Transição para próximo slide]

# Restrições
- Escreva como se fala, não como se escreve ensaio
- Inclua [pausas] onde alunos devem processar
- Inclua perguntas retóricas
- Máximo 2-3 minutos por slide
```

---

## Timing e Ritmo

*PowerPoint > Apresentação de Slides > Ensaiar Intervalos*

📸 **Sugestão de Print:** Timeline visual de uma apresentação de 20 minutos com alocação de tempo por slide

Uma distribuição saudável para uma aula de 20 minutos:

```md
Slide 1 (Abertura):              1 minuto  — desperta curiosidade
Slides 2–4 (Desenvolvimento):   9 minutos  — conteúdo principal (3 min cada)
Slide 5 (Atividade):             5 minutos  — engaja os alunos
Slide 6 (Fechamento):            2 minutos  — reflexão e ação
Margem para imprevistos:         3 minutos  — perguntas, ajustes
```

Inclua nas notas indicações de corte para quando o tempo apertar:

```md
[TIMING: 2 minutos — SE HOUVER TEMPO EXTRA: adicione exemplo X;
SE TEMPO CURTO: pule para a linha "Resumindo"]
```

### Pílula Hands-on — Mão na Massa

**Tempo estimado:** 10 minutos

Pegue um bullet point de uma apresentação que você já usa e expanda em nota de orador completa, seguindo a estrutura desta seção. Depois peça para Claude refinar com mais exemplos práticos do dia a dia dos seus alunos. Compare as duas versões — a sua e a refinada — e veja o que Claude adicionou que você não tinha pensado.

---

# Capítulo 6 — Automação Inteligente: Pedindo ao Claude para Escrever Código VBA

## O Que é VBA e Por Que Importa

*PowerPoint > Desenvolvedor > Visual Basic*

[VBA](#glos-vba) (Visual Basic for Applications) é a linguagem de automação do Microsoft Office. Ele permite que você instrua o PowerPoint a realizar tarefas repetitivas de forma automática — sem precisar ser programador.

O Claude pode escrever esse código para você. Você descreve o que quer em linguagem natural, ele traduz para VBA funcional.

**Caso de uso 1: Criar 20 aulas em 1 hora**

Você tem uma planilha Excel com temas, objetivos e atividades. Ao invés de criar cada apresentação manualmente — o que levaria 20 horas — você descreve a estrutura para o Claude, ele escreve a [macro](#glos-macro), a macro lê a planilha e cria automaticamente 20 apresentações. Você revisa cada uma em 2 minutos.

**Caso de uso 2: Template automático em todos os slides**

Você quer que todos os slides sigam uma estrutura consistente (título + 3 bullets + imagem + nota de rodapé). A macro aplica esse padrão a toda a apresentação em segundos.

---

## Exemplo de VBA Simples: Criar um Slide com Texto

*PowerPoint > Desenvolvedor > Visual Basic > Editor VBA*

Veja como solicitar código VBA ao Claude:

```md
Escreva uma macro VBA que:
1. Cria uma nova apresentação PowerPoint
2. Adiciona um slide com layout "Título e Conteúdo"
3. Insere título: "Fotossíntese"
4. Insere 3 bullets: Luz é absorvida / Água é processada / Oxigênio é produzido
5. Salva a apresentação

Código deve ser comentado em português para eu entender cada linha.
```

Claude responde com código como:

```vba
Sub CriarAulaFotossintese()
    ' Cria uma nova apresentação PowerPoint
    Dim pptApp As Object
    Dim pptPres As Object
    Dim pptSlide As Object
    
    ' Inicia PowerPoint
    Set pptApp = CreateObject("PowerPoint.Application")
    pptApp.Visible = True
    
    ' Cria nova apresentação
    Set pptPres = pptApp.Presentations.Add()
    
    ' Adiciona slide com layout "Título e Conteúdo" (Layout 3)
    Set pptSlide = pptPres.Slides.Add(1, 3)
    
    ' Define o título
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Fotossíntese"
    
    ' Define os bullets
    Dim textBox As Object
    Set textBox = pptSlide.Shapes(2).TextFrame
    
    textBox.TextRange.Text = "Luz é absorvida"
    textBox.TextRange.InsertAfter vbNewLine & "Água é processada"
    textBox.TextRange.InsertAfter vbNewLine & "Oxigênio é produzido"
    
    ' Salva a apresentação
    pptPres.SaveAs "C:\MinhaAula_Fotossintese.pptx"
    
    MsgBox "Aula criada com sucesso!"
End Sub
```

📸 **Sugestão de Print:** VBA Editor do PowerPoint com este código comentado e setas indicando cada seção

---

## Como Usar Código VBA no PowerPoint

*PowerPoint > Desenvolvedor > Macros > Executar*

O processo é simples mesmo para quem nunca abriu um editor de código:

**Passo 1:** Abra PowerPoint → Guia "Desenvolvedor" → "Visual Basic"

*(Se não vê "Desenvolvedor": Arquivo → Opções → Personalizar Fita → Marque "Desenvolvedor")*

📸 **Sugestão de Print:** Menu de opções mostrando onde ativar a aba "Desenvolvedor"

**Passo 2:** Cole o código que Claude gerou no editor

**Passo 3:** Clique no ícone "Play" (Run) ou pressione F5

**Passo 4:** A macro executa e cria os slides automaticamente

**Passo 5:** Você revisa e personaliza cores, fontes e conteúdo específico

---

## Prompts Avançados para Automatização

*Claude AI > Engenharia de Prompt > Geração de Código VBA*

### Prompt: Aplicar Formatação Uniforme

```md
Escreva uma macro que:
1. Acessa a apresentação PowerPoint aberta
2. Para cada slide da apresentação:
   - Define fonte como "Arial"
   - Define tamanho de título como 40pt
   - Define tamanho de bullets como 18pt
   - Alinha tudo à esquerda
   - Define cor de fundo como azul claro (RGB: 200, 220, 240)

Código em VBA comentado em português.
```

### Prompt: Ler Dados de Planilha e Criar Slides

```md
Escreva uma macro que:
1. Abre arquivo Excel "aulas.xlsx"
2. Lê as colunas:
   - A: Tema da aula
   - B: Objetivo
   - C: Atividade
3. Para cada linha, cria um novo slide PowerPoint com:
   - Título: [Tema]
   - Slide 1: Objetivo (1 bullet)
   - Slide 2: Atividade (1 bullet)
4. Salva PowerPoint como "Aulas_Criadas.pptx"

Use comentários em português.
```

### O Que o VBA Não Pode Fazer

É igualmente importante conhecer os limites. VBA não consegue baixar imagens automaticamente da internet, não gera imagens (use DALL-E separadamente), não conhece o seu conteúdo sem uma fonte de dados prévia, e não faz design criativo. Ele é uma ferramenta de **estrutura e repetição** — perfeita para isso, não para o resto.

### Pílula Hands-on — Mão na Massa

**Tempo estimado:** 15 minutos *(pode ser pulado se você não usa Excel ou não se sentir confortável com código)*

Descreva para Claude o modelo de slide que você usa no seu dia a dia e peça a criação de uma macro que gera esse template. Depois, teste no PowerPoint. Uma vez que funcionar, você tem um atalho reutilizável para o restante da sua carreira.

---

# Capítulo 7 — Direção de Arte: Imagens, Cores e Layouts Visuais

## Claude Como Diretor de Arte

*Claude AI > Engenharia de Prompt > Direção Visual*

Neste capítulo, o Claude assume um papel diferente. Ele não vai criar imagens — para isso existem DALL-E, Midjourney e Canva. Mas ele vai **dirigir visualmente** a sua apresentação: sugerir layouts, propor paletas de cores, e descrever com precisão as imagens que você precisa buscar.

Pense nisso como ter um consultor de design ao seu lado, disponível 24 horas por dia.

---

## Técnica 1: Sugestão de Layout

*PowerPoint > Design > Temas > Layout de Slide*

Quando você sabe o que quer mostrar, mas não sabe como organizar visualmente, use este prompt:

```md
Preciso que um slide mostre comparação entre 3 coisas (visual, auditivo, cinestésico).
A apresentação é para 6º ano.

Sugira 3 diferentes layouts:
1. [Nome layout 1]: [descrição visual]
2. [Nome layout 2]: [descrição visual]
3. [Nome layout 3]: [descrição visual]

Para cada layout, indique:
- Como fica visualmente
- Quando usar este layout
- Vantagens e desvantagens
```

📸 **Sugestão de Print:** Três mockups de slides lado a lado, cada um com um layout diferente

---

## Técnica 2: Paletas de Cores Comunicativas

*PowerPoint > Design > Variantes > Cores*

Cores não são acaso — elas comunicam emoções antes mesmo que o aluno leia uma palavra. Para escolher uma [paleta de cores](#glos-paleta-cores) adequada, use este prompt:

```md
Estou criando uma apresentação sobre [TEMA] para [PÚBLICO].
O objetivo é transmitir [EMOÇÃO: esperança, urgência, calma, entusiasmo].

Sugira uma paleta de cores (máximo 5 cores) que:
1. Transmita essa emoção
2. Seja acessível (altos contrastes, amigável para daltônico)
3. Funcione bem em projetor de escola (nem muito escuro, nem muito brilhante)

Para cada cor:
- Nome da cor
- Código RGB ou Hex
- Onde usar (fundo, títulos, destaque)
- Por que transmite essa emoção
```

Claude pode sugerir, por exemplo, uma paleta de "Esperança e Crescimento" com verde claro (`#4CAF50`) para elementos positivos, azul céu (`#2196F3`) para títulos, e amarelo quente (`#FFC107`) para chamadas de ação — cada escolha justificada e com indicação de uso.

---

## Técnica 3: Descrição de Imagens para Banco de Dados

*Claude AI > Engenharia de Prompt > Geração de Brief Visual*

A busca por imagens genéricas no Google resulta em imagens genéricas. Com o Claude, você descreve a imagem ideal com precisão suficiente para encontrá-la exatamente nos bancos de dados gratuitos como Unsplash, Pexels e Pixabay.

**Prompt:**
```md
Quero encontrar uma imagem para um slide sobre germinação (sementes brotando).
O público é 6º ano. Preciso de imagem que:
1. Mostre claramente o processo (semente → raiz → broto)
2. Seja visualmente simples (não muito científica)
3. Tenha cores naturais (terra, verde, luz solar)
4. Seja acolhedora ou inspiradora (não mecânica)

Descreva detalhadamente a imagem ideal para eu buscar em banco de imagens.
Sugira também: Unsplash, Pexels ou Pixabay?
```

Claude responde com uma descrição como:

```md
DESCRIÇÃO PARA BUSCAR:
"Macro photography of seed germination process showing seed sprouting with
visible root emerging, set in rich brown soil with green shoot pushing
upward, natural sunlight creating warm glow"

KEYWORDS:
- seed germination macro
- sprouting seed photography
- plant growth from seed

RECOMENDAÇÃO: Pexels ou Pixabay — grátis e boa qualidade para educação
```

Você copia essa descrição, cola no buscador, e encontra exatamente o que precisa em segundos.

### Pílula Hands-on — Mão na Massa

**Tempo estimado:** 10 minutos

Escolha um tema que está lecionando e peça para Claude sugerir apenas a paleta de cores. Depois, abra o PowerPoint, vá em *Design → Temas → Cores* e altere as cores do tema para as recomendadas. Veja como a apresentação inteira assume uma identidade visual coerente em menos de 5 minutos.

---

# Capítulo 8 — Segurança, Privacidade, Ética e Revisão Humana

## Onde Claude Processa Seus Dados

*Claude AI > Configurações > Privacidade e Dados*

Este é o capítulo mais importante do livro — e o mais ignorado por usuários iniciantes.

⚠️ **Ponto crítico:** Claude processa em **servidores remotos** da Anthropic, hospedados em nuvem. Os dados que você digita no painel do Claude **não ficam apenas no seu computador**. Eles são transmitidos para servidores externos, processados lá, e podem ser armazenados para fins de melhoria do modelo, dependendo da política de privacidade vigente.

Isso não é necessariamente um problema — mas significa que você precisa ser criterioso sobre **o que você compartilha**.

---

## O Que NUNCA Compartilhar com Claude

*Claude AI > Painel de Chat > Boas Práticas de Privacidade*

```md
❌ NUNCA:
- Nomes completos de alunos específicos
- Datas de nascimento, RG, CPF
- Endereços residenciais
- Diagnósticos médicos ou psicológicos (ex: "João tem TDAH")
- Notas ou histórico acadêmico identificado
- Fotos ou vídeos de menores
- Informações de NEE (Necessidades Educacionais Especiais)
- Senhas ou dados bancários

✅ PODE:
- Tema genérico: "Como ensinar frações para crianças com dificuldade de aprendizado"
- Contexto anônimo: "Alunos com [nível de profundidade] em [tema]"
- Contexto geral: "Escola em zona rural com internet instável"
- Feedback genérico: "Alunos têm dificuldade com metáforas"
```

A regra de ouro é simples: **se a informação identifica uma pessoa real, não compartilhe**.

---

## Validação de Informações: O Risco da Alucinação

*Claude AI > Painel de Chat > Verificação de Respostas*

Claude é uma IA generativa. Às vezes ele [alucina](#glos-alucinacao) — ou seja, gera informações que parecem corretas mas são inventadas. Isso não é uma falha de caráter; é uma característica técnica de como modelos de linguagem funcionam.

**Exemplo:** Se você perguntar "Quantas células tem uma folha de árvore?", Claude pode responder com um número específico com total confiança — e esse número pode ser completamente inventado.

A defesa é sempre a mesma: **verifique dados críticos em fontes confiáveis** antes de usar em aula. Especialmente datas, números, nomes próprios e afirmações científicas específicas.

Para auxiliar nessa validação, use este prompt:

```md
Este fato que você me passou está correto?
"[informação]"

Cite a fonte ou explique onde encontrou este dado.
Se não tem certeza, diga explicitamente "não tenho certeza".
```

---

## Transparência com Alunos: Devo Contar que Usei IA?

*Claude AI > Sobre o Claude > Uso Responsável e Ética*

A tendência do campo educacional é cada vez mais clara: **sim, contar**.

Não porque há algo errado em usar IA como ferramenta pedagógica — há muito de certo. Mas porque você modela para os seus alunos o uso responsável e transparente de tecnologia. E isso, em si, é uma lição valiosa.

Alguns exemplos de como comunicar:

**Para apresentação criada com ajuda do Claude:**
> "Esta apresentação foi organizada com ajuda de uma IA chamada Claude. Eu criei a estrutura pedagógica e revisei todo o conteúdo — Claude ajudou com organização e linguagem. Cada informação foi verificada por mim."

**Para atividade onde alunos usarão IA:**
> "Vocês vão usar uma IA para [tarefa]. Está ok usá-la para [X], mas precisam revisar e melhorar a saída. O objetivo é aprender a trabalhar com tecnologia de forma crítica."

---

## Checklist de Segurança

*Claude AI > Painel de Chat > Revisão Pré-Publicação*

Antes de usar qualquer apresentação criada com Claude em aula, percorra esta lista:

```md
[ ] Conteúdo foi verificado para precisão (datas, nomes, fatos)?
[ ] Linguagem está adequada para a idade dos alunos?
[ ] Nenhum dado sensível de aluno está na apresentação?
[ ] Imagens têm fontes atribuídas (quando necessário)?
[ ] Estrutura faz sentido no contexto da minha aula?
[ ] Testei a apresentação no projetor antes de apresentar?
[ ] Se fiz com ajuda de IA, meus alunos sabem disso?
[ ] Posso defender cada informação se aluno questionar?
[ ] Slides seguem as políticas da instituição?
```

### Pílula Hands-on — Mão na Massa

**Tempo estimado:** 5 minutos

Abra uma apresentação que você já criou com Claude. Escolha 3 fatos aleatórios e verifique-os em uma fonte externa (Google, livro didático, site oficial). Se algum estiver errado ou incompleto, corrija antes de usar em aula. Essa prática de auditoria rápida — 3 fatos, 5 minutos — pode salvar você de situações embaraçosas e, mais importante, garante que você está ensinando conteúdo correto.

---

# Capítulo Bônus — Biblioteca de Prompts Prontos para Professores

*Claude AI > Engenharia de Prompt > Biblioteca de Templates*

Este capítulo é seu guia de referência rápida. Todos os prompts abaixo foram desenvolvidos ao longo deste livro e podem ser copiados, colados e adaptados para qualquer disciplina ou série.

---

## Prompt 1: Criar Apresentação Completa

```md
# CONTEXTO
Sou professor de [DISCIPLINA] em [TIPO DE ESCOLA].
Meus alunos têm [IDADE/SÉRIE]. Eles [CONHECIMENTO PRÉVIO].

# TAREFA
Crie uma apresentação de [NÚMERO] slides sobre [TEMA].
Objetivo: [EXPLICAR / REVISAR / INTRODUZIR / OUTRO].
Duração ideal: [TEMPO] minutos.

# FORMATO
Para cada slide:
1. Título (pergunta ou afirmação memorável)
2. 3-4 bullets (máximo 8 palavras cada)
3. Uma atividade, pergunta ou exercício para esse slide
4. Sugestão de visual / imagem

# RESTRIÇÕES
- Linguagem: [SIMPLES / INTERMEDIÁRIA / AVANÇADA]
- Tom: [FORMAL / CONVERSACIONAL / LÚDICO]
- Evite: [JARGÃO / EXEMPLOS ESPECÍFICOS / OUTRO]
- Inclua: [EXEMPLOS DO DIA A DIA / ANALOGIAS / OUTRO]
```

---

## Prompt 2: Expandir em Notas do Orador

```md
Expanda cada slide em NOTAS DO ORADOR (texto conversacional que eu possa falar).

Para cada slide:
[TIMING: X minutos]
[Abertura/gancho conversacional]
[Desenvolvimento expandido — 80-120 palavras]
[Pausa e pergunta para alunos]
[Transição para próximo slide]

Escreva como eu FALO, não como livro. Use [pausas] onde eu devo parar.
```

---

## Prompt 3: Simplificar Texto Denso

```md
Tenho este parágrafo sobre [TEMA]:
[COLAR PARÁGRAFO DENSO]

Rescreva para alunos de [ANO/SÉRIE] assim:
1. Use apenas palavras que uma criança entenda
2. Quebre em 2-3 frases curtas
3. Inclua 1 comparação com algo do dia a dia
4. Mantenha a precisão científica

Resultado: 3-4 linhas máximo.
```

---

## Prompt 4: Gerar Atividade Interativa

```md
Crie uma atividade interativa para ensinar [CONCEITO] para alunos de [SÉRIE].

A atividade deve:
- Levar 10-15 minutos
- Engajar alunos de forma criativa (não apenas preencher worksheet)
- Testar compreensão de forma ativa
- Usar materiais simples (se presencial) ou online (se remoto)

Formate assim:
OBJETIVO: [uma frase]
MATERIAIS: [lista]
PASSO 1: [instruções]
PASSO 2: [instruções]
REFLEXÃO: [pergunta de síntese]
```

---

## Prompt 5: Criar Quiz de Revisão

```md
Crie um quiz para revisar [TEMA] com alunos de [SÉRIE].

Requisitos:
- Número de questões: [5 / 10 / 15]
- Tipo: [MÚLTIPLA ESCOLHA / VERDADEIRO-FALSO / ABERTA]
- Nível de dificuldade: [FÁCIL / MÉDIO / DESAFIADOR]

Para cada questão:
- Enunciado claro
- [Se múltipla escolha: 4 opções com 1 correta]
- [Se aberta: sugestão de resposta esperada]
- [Feedback: por que a resposta está correta/errada]
```

---

## Prompt 6: Descrever Imagem para Banco de Dados

```md
Preciso de uma imagem para um slide sobre [TEMA] para alunos de [SÉRIE].

Características desejadas:
- Estilo: [FOTOGRAFIA / ILUSTRAÇÃO / INFOGRÁFICO]
- Tom: [EDUCATIVO / LÚDICO / FORMAL]
- Elementos principais: [DESCREVER]
- Paleta de cores: [DESCREVER]

Gere uma descrição de 3-4 linhas para buscar em Unsplash/Pexels/Pixabay.
Sugira também qual banco de imagens tem mais chance de ter.
```

---

## Prompt 7: Gerar Paleta de Cores

```md
Estou criando uma apresentação sobre [TEMA] para [PÚBLICO].
Objetivo emocional: [ESPERANÇA / URGÊNCIA / CALMA / ENTUSIASMO / OUTRO].

Sugira paleta de cores:
- 4-5 cores com código RGB ou HEX
- Onde usar cada cor (fundo, títulos, destaques)
- Por que essa cor transmite a emoção desejada

Garanta: alto contraste (legível em projetor), acessível para daltônico,
não saturação excessiva.
```

---

## Prompt 8: Criar Roteiro de Fala

```md
Tenho estes tópicos para um slide:
- [TÓPICO 1]
- [TÓPICO 2]
- [TÓPICO 3]

Crie um roteiro de fala de 2 minutos que:
- Conecta os tópicos em sequência lógica
- Usa linguagem conversacional
- Inclui [NÚMERO] exemplo(s) do dia a dia
- Termina com pergunta para engajar alunos

Formato:
[Abertura — 20 segundos]
[Tópico 1 — com exemplo — 30 segundos]
[Tópico 2 — com exemplo — 30 segundos]
[Tópico 3 — com exemplo — 30 segundos]
[Pergunta final — 10 segundos]
```

---

## Prompt 9: Validar Informações

```md
Esta informação está correta e apropriada para ensinar a crianças de [SÉRIE]?

[COLAR INFORMAÇÃO]

Responda:
1. É factualmente correta? (Sim/Não/Parcialmente — explique)
2. É apropriada para a idade? (Sim/Não/Com contexto)
3. Há forma mais simples de explicar? (Sim — sugira)
4. Há conceitos prévios que alunos precisam saber? (Liste)
```

---

# Sequência Didática Sugerida

## Semana 1: Fundamentos

**Aula 1 (60 min)**
- Capítulo 0: Primeiros Passos (20 min)
- Capítulo 1: Entendendo o Claude (20 min)
- Capítulo 2: Preparação (20 min)

**Aula 2 (60 min)**
- Capítulo 3: Craft de Prompts (30 min)
- Atividade Prática: Criar primeiro prompt (30 min)

---

## Semana 2: Narrativa e Estrutura

**Aula 3 (60 min)**
- Capítulo 4: Estruturando Narrativa (20 min)
- Capítulo 5: Notas do Orador (20 min)
- Atividade Prática: Expandir um slide em roteiro (20 min)

**Aula 4 (60 min)**
- Atividade Integrada: Criar apresentação completa do zero ao deck final

---

## Semana 3: Técnicas Avançadas

**Aula 5 (60 min)**
- Capítulo 6: Automação com VBA (30 min, opcional)
- Capítulo 7: Direção de Arte (30 min)

**Aula 6 (60 min)**
- Capítulo 8: Segurança e Ética (20 min)
- Capítulo Bônus: Prompts Prontos (20 min)
- Revisão e Dúvidas (20 min)

---

# Avaliação Sugerida

## Critérios Formativos (Ao Longo do Curso)

```md
[ ] Participação nas Pílulas Hands-on de cada módulo
[ ] Qualidade dos prompts criados (clareza, estrutura, especificidade)
[ ] Capacidade de iterar e refinar prompts baseado no resultado
[ ] Validação de informações (verificou fatos antes de usar?)
[ ] Responsabilidade ética (considerou privacidade de alunos?)
```

## Avaliação Somativa (Final)

Cada participante apresenta:

```md
1. APRESENTAÇÃO CRIADA (10 pontos)
   - Estrutura narrativa clara?            (0-2 pontos)
   - Conteúdo verificado e apropriado?     (0-2 pontos)
   - Design visualmente coerente?          (0-2 pontos)
   - Tem atividade ou interação?           (0-2 pontos)
   - Notas do orador bem expandidas?       (0-2 pontos)

2. REFLEXÃO ESCRITA — 1 página (10 pontos)
   - Como Claude ajudou você?
   - O que você fez que a IA não poderia fazer?
   - Como você validou as informações?
   - Usaria essa técnica com seus alunos? Por quê?

TOTAL: 20 pontos
```

---

# Encerramento: A Mentalidade Futura

O Claude para PowerPoint não é mágica. É **amplificação**.

Você é o designer pedagógico. Você conhece seus alunos. Você sabe o que funciona dentro da sua sala de aula, com aqueles estudantes específicos, naquele contexto único.

Claude é seu parceiro de execução — ele ajuda a traduzir suas ideias em slides profissionais com mais rapidez. Mas a ideia é sua. A curadoria é sua. A responsabilidade é sua.

**Não use Claude para** enganar alunos fingindo que criou tudo sozinho sem esforço, para substituir o pensamento pedagógico, ou para expor dados sensíveis de estudantes.

**Use Claude para** poupar tempo em tarefas repetitivas de estruturação e escrita, aprimorar suas ideias com ângulos que você não havia considerado, manter qualidade consistente em múltiplas apresentações, e — com o tempo que você economiza — cuidar melhor do que realmente importa: o aprendizado dos seus alunos.

---

**Use o Claude para PowerPoint como seu parceiro criativo: você pensa, estrutura e valida; Claude amplifica e acelera. Juntos, criam aulas memoráveis.**

---

# Glossário

### Claude {#glos-claude}

Assistente de inteligência artificial desenvolvido pela Anthropic. No contexto deste livro, Claude está integrado ao Microsoft PowerPoint como um complemento que ajuda professores e profissionais a criar, estruturar e refinar apresentações de slides por meio de linguagem natural.

---

### PowerPoint {#glos-powerpoint}

Software de criação de apresentações de slides desenvolvido pela Microsoft, parte do pacote Microsoft 365 (antigo Office). É amplamente usado em contextos educativos e corporativos para comunicação visual.

---

### IA Generativa {#glos-ia-generativa}

Categoria de inteligência artificial capaz de gerar conteúdo original — texto, imagens, código, áudio — a partir de instruções em linguagem natural. Diferente de IAs que apenas classificam ou preveem, a IA generativa produz novos artefatos com base em padrões aprendidos durante o treinamento.

---

### Prompt {#glos-prompt}

Instrução ou solicitação enviada a um modelo de IA para gerar uma resposta. No contexto de criação de apresentações, um prompt bem elaborado especifica contexto, tarefa, formato desejado e restrições, resultando em saídas mais precisas e úteis.

---

### Prompt Engineering {#glos-prompt-engineering}

A prática de formular prompts de forma estratégica para obter melhores resultados de modelos de IA. Inclui técnicas como Chain-of-Thought (pedir raciocínio passo a passo), Few-Shot (fornecer exemplos), e Role-Playing (atribuir um papel ao modelo).

---

### Briefing {#glos-briefing}

Documento sintético que reúne as informações essenciais de um projeto antes do início da execução. No contexto deste livro, o briefing responde às sete perguntas fundamentais sobre objetivo, público, contexto, duração, formato, atividade e restrições — e serve como base para os prompts enviados ao Claude.

---

### Microsoft 365 {#glos-microsoft365}

Serviço de assinatura da Microsoft que inclui aplicativos como Word, Excel, PowerPoint, Outlook e Teams, com acesso via nuvem. A integração do Claude com o PowerPoint requer uma assinatura ativa do Microsoft 365.

---

### VBA {#glos-vba}

Visual Basic for Applications. Linguagem de programação integrada aos aplicativos do Microsoft Office que permite automatizar tarefas repetitivas. Com a ajuda do Claude, professores podem gerar código VBA em linguagem natural e usá-lo para criar, formatar ou duplicar slides em lote sem necessidade de conhecimento técnico prévio.

---

### Macro {#glos-macro}

Sequência de comandos programados (geralmente em VBA) que executa uma série de ações automaticamente no Microsoft Office. Neste livro, macros são usadas para criar estruturas de slides, aplicar formatação uniforme e processar dados de planilhas automaticamente.

---

### Notas do Orador {#glos-notas-orador}

Campo de texto associado a cada slide no PowerPoint onde o apresentador pode registrar roteiro de fala, lembretes ou contexto adicional. Não são visíveis ao público durante a apresentação. Neste livro, são tratadas como narrativas conversacionais expandidas — não bullets adicionais — que o professor pode consultar discretamente durante a aula.

---

### Throughline {#glos-throughline}

Conceito de narrativa que se refere ao fio condutor central de uma apresentação — a ideia unificadora que conecta todos os slides e dá coerência à história. Uma apresentação com throughline forte tem cada slide contribuindo para a mesma ideia central; sem ela, os slides parecem tópicos desconexos.

---

### Alucinação {#glos-alucinacao}

Fenômeno em modelos de IA generativa onde o sistema gera informações plausíveis mas factualmente incorretas ou inventadas, com aparente confiança. É uma característica técnica dos modelos de linguagem, não um defeito isolado. A defesa mais eficaz é a validação humana de dados críticos antes do uso.

---

### DALL-E {#glos-dalle}

Modelo de IA generativa desenvolvido pela OpenAI capaz de criar imagens a partir de descrições textuais. Mencionado neste livro como alternativa para geração visual, já que Claude não cria imagens diretamente — apenas descreve com precisão o que você precisa buscar ou gerar em ferramentas especializadas.

---

### Paleta de Cores {#glos-paleta-cores}

Conjunto de cores selecionadas de forma coordenada para uso em um projeto visual. Uma paleta bem escolhida transmite emoções consistentes, garante acessibilidade (especialmente para pessoas com daltonismo) e mantém coerência visual ao longo de toda a apresentação.

---

*Este e-book foi transformado a partir do Plano de Aula original "Claude: Co-Piloto Criativo", com foco em didática progressiva, acessibilidade pedagógica e produção de conteúdo educacional responsável.*

