# Claude Design 2.0 — Da Ideia à Interface

### Roteiro completo do curso reformulado, para docentes da escola pública

*Este roteiro reconstrói o curso Claude Design a partir da auditoria crítica realizada sobre a versão anterior. Cada debilidade identificada — falta de recursos visuais, lacunas de navegação, mecânica de comparação não explicada, ausência de acessibilidade e alinhamento, entre outras — foi convertida em uma correção estrutural específica dentro deste novo roteiro.*

Público-alvo: docentes da escola pública com pouco ou nenhum contato prévio com inteligência artificial, ferramentas profissionais de design, desenvolvimento web, HTML, CSS ou JavaScript.

O curso não forma designers nem programadores. Ele leva o aluno de:

> "Não sei como transformar uma ideia em algo visual."

para:

> "Consigo criar uma interface com o Claude, avaliar criticamente o resultado e refiná-lo até que fique adequado ao meu objetivo e ao meu público."

---

## O Ciclo Central do Curso

Todo o roteiro gira em torno de um único ciclo, repetido e aprofundado a cada aula:

**descrever → gerar → observar → avaliar → modificar → comparar → refinar**

O Claude não é apresentado como uma máquina que "gera telas". Ele é apresentado como um parceiro de conversa que constrói um rascunho visual e continua ajustando esse rascunho junto com você. A aprendizagem de design acontece dentro desse ciclo — não em blocos de teoria isolados.

---

## Antes de Começar

> **Nota:** você vai precisar de uma conta gratuita em `claude.ai`. O Claude Design é acessado em `claude.ai/design` e faz parte dos planos pagos do Claude (Pro, Max, Team ou Enterprise) — não está disponível no plano gratuito. Verifique com a coordenação da sua escola ou secretaria de educação se já existe uma licença paga disponível.

> **Nota de versão:** o Claude Design está em fase beta e muda com frequência. Nomes de botões, telas de configuração e a posição exata de alguns recursos citados neste roteiro podem mudar entre uma atualização e outra. Valide as capturas de tela e os passos de navegação deste curso antes de cada nova turma.

> **Atenção:** a geração da primeira página ou de um sistema de estilo completo pode levar entre 5 e 10 minutos. **Não feche nem atualize a aba enquanto o Claude estiver gerando** — isso descarta o trabalho e obriga a recomeçar do zero. Abra uma segunda aba se precisar fazer outra coisa nesse meio-tempo.

> **Nota:** o Claude Design usa a mesma cota de uso do seu plano Claude. Projetos com muitas rodadas de ajuste consomem mais dessa cota. Se você atingir o limite do seu plano, a ferramenta ficará indisponível até o próximo ciclo — isso não é um erro, é um limite de uso normal.

> **Atenção:** não utilize dados pessoais, sensíveis ou informações reais de alunos (nomes completos, notas individuais, fotos) em nenhum exercício deste curso. Use exemplos fictícios ou anonimizados, e observe as políticas de privacidade e segurança da sua instituição.

> **Nota de versão:** hoje o Claude Design funciona em navegador de computador. Sua disponibilidade e comportamento em navegador de celular não são garantidos nem documentados de forma estável — trate o celular como forma de *acompanhar* o trabalho, não de criá-lo do zero, até que isso seja confirmado na versão que você estiver usando.

---

## Mapa do Curso

| Parte | Tema | Aulas |
|---|---|---|
| 1 | Primeiros Passos | 1.1 O Que É o Claude Design? · 1.2 Criando Sua Primeira Página · 1.3 Entendendo o Que Apareceu na Tela · 1.4 Fazendo Sua Primeira Alteração Visual |
| 2 | Organizando a Informação | 2.1 Hierarquia Visual · 2.2 Agrupando com Seções e Cards · 2.3 Espaçamento e Alinhamento |
| 3 | Dando Personalidade ao Design | 3.1 Cores que Ajudam · 3.2 Tipografia · 3.3 Consistência |
| 4 | Trabalhando com Componentes | 4.1 As Peças Reutilizáveis da Interface · 4.2 Montando uma Página com Vários Componentes |
| 5 | Refinando Interfaces | 5.1 Virando Crítico do Próprio Design · 5.2 O Ciclo do Refinamento na Prática |
| 6 | Desktop e Mobile | 6.1 Uma Página, Duas Telas |
| 7 | Acessibilidade | 7.1 Design para Todo Mundo |
| 8 | Experiências Interativas | 8.1 Cliques que Revelam Coisas · 8.2 Estados e Feedback |
| 9 | Projetos Educacionais | 9.1 Página de Disciplina · 9.2 Quiz Interativo · 9.3 Página de Revisão · 9.4 Painel de Acompanhamento |
| 10 | Refinamento Avançado | 10.1 O Claude Como Parceiro de Crítica |
| 11 | Referências Visuais | 11.1 Mostrar em Vez de Descrever |
| 12 | Do Protótipo ao Resultado Final | 12.1 Protótipo, Interface e Produto: Sabendo a Diferença |

---
---

# Parte 1 — Primeiros Passos

Nesta parte você não precisa de nenhum conhecimento prévio. O objetivo é sair com uma pequena conquista real: uma página criada por você, com sua primeira alteração já aplicada.

## Aula 1.1 — O Que É o Claude Design?

### Objetivos da Aula

- Entender o que é o Claude Design e em que ele difere de um editor tradicional.
- Reconhecer a lógica de conversa + tela (chat + canvas).
- Conhecer o ciclo completo que vai guiar todo o curso.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- explicar com suas próprias palavras o que é o Claude Design;
- localizar a área de chat e a área de canvas na interface;
- descrever, em ordem, as sete etapas do ciclo descrever → gerar → observar → avaliar → modificar → comparar → refinar.

### Desenvolvimento da Aula

Pense no Claude como alguém para quem você descreve a sala de aula que gostaria de organizar. Você não precisa dizer onde vai cada parafuso da carteira — primeiro explica o que precisa existir e como gostaria que tudo fosse organizado. A pessoa monta uma primeira versão, você olha, e diz o que quer mudar. O Claude Design funciona assim, só que o "ambiente" é uma tela.

**A tela tem duas metades.** De um lado, o **chat**: o espaço onde você escreve o que quer. Do outro, o **canvas**: a área de trabalho onde o resultado visual aparece e se atualiza conforme a conversa avança.

**O verdadeiro diferencial não é gerar uma página — é conversar sobre ela.** Qualquer ferramenta gera algo a partir de um texto. O que faz o Claude Design valer a pena é o que acontece depois do primeiro rascunho: você aponta o que não gostou, ele ajusta, você compara, ajusta de novo. O curso inteiro é construído em cima dessa conversa contínua, não do primeiro clique.

**O ciclo que vai se repetir em toda aula:**

1. **Descrever** — contar o que você quer, para quem, e com que clima.
2. **Gerar** — o Claude produz um primeiro rascunho.
3. **Observar** — você olha com atenção antes de reagir.
4. **Avaliar** — você decide o que funciona e o que não funciona.
5. **Modificar** — você pede um ajuste específico.
6. **Comparar** — você olha a versão nova ao lado da anterior.
7. **Refinar** — você repete o processo até o resultado servir ao seu objetivo.

> 📸 **Sugestão de Prints:** captura de tela cheia da interface do Claude Design, com uma seta e legenda "Chat" apontando para a coluna esquerda e outra seta e legenda "Canvas" apontando para a área direita. Por quê: é a primeira vez que o aluno vê a ferramenta — orientar espacialmente antes de qualquer texto evita que ele precise imaginar a tela.

### Conceito de Design da Aula: Refinamento Iterativo

1. **O que é?** A ideia de que a primeira versão de qualquer coisa — um texto, uma prova, um design — raramente é a versão final.
2. **Por que importa?** Se você espera acertar de primeira, qualquer resultado imperfeito parece um fracasso. Se você espera refinar, o mesmo resultado é só o ponto de partida esperado.
3. **Como perceber na tela?** Toda vez que você olhar para um rascunho gerado pelo Claude e pensar "quase, mas falta algo" — isso não é um problema, é a etapa normal do processo.
4. **Como pedir ao Claude para melhorar?** Você não "pede para melhorar" nesta aula ainda — você só reconhece que vai pedir, repetidamente, ao longo de todo o curso.

### 🧪 Pílula Hands-on

**Objetivo:** reconhecer o terreno antes de criar qualquer coisa.

**Faça agora:**
1. Acesse `claude.ai/design` pelo navegador do computador.
2. Observe a tela inicial por 2 minutos, sem clicar em nada que pareça iniciar um projeto.
3. Localize: o campo onde se escreve um pedido, as opções de tipo de projeto e a opção de começar em branco.

**Observe:**
- onde fica o campo de texto principal;
- se existe alguma indicação de "modelo" ou "sistema de design" na tela;
- quantas opções diferentes de ponto de partida você consegue identificar.

**Resultado esperado:** você reconhece os elementos da tela inicial e chega à Aula 1.2 já sabendo onde vai clicar.

### 🔧 Troubleshooting

**Problema:** não encontro a opção "Design" ou a ferramenta parece bloqueada.
**Possível causa:** o Claude Design não está incluído no plano gratuito, e pode estar desativado por padrão em contas Enterprise.
**Como resolver:** confirme com quem administra a conta da sua escola se o plano é Pro, Max, Team ou Enterprise, e se o recurso foi ativado.

**Problema:** abri pelo celular e a tela parece quebrada ou incompleta.
**Possível causa:** o Claude Design hoje é otimizado para navegador de computador; o comportamento em navegador mobile não é garantido.
**Como resolver:** prefira um computador para as atividades de criação. Use o celular apenas para revisar um trabalho já pronto, se necessário.

---

## Aula 1.2 — Criando Sua Primeira Página

### Objetivos da Aula

- Criar uma primeira página com o Claude Design a partir de uma descrição simples.
- Responder às perguntas de esclarecimento que o Claude pode fazer antes de gerar.
- Compreender por que a primeira geração demora alguns minutos.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- iniciar um novo projeto e escolher entre um modelo pronto ou começar em branco;
- escrever um pedido descrevendo conteúdo, público e clima;
- responder com segurança se o Claude fizer perguntas antes de gerar;
- aguardar a geração sem interromper o processo.

### Desenvolvimento da Aula

**Passo a passo da tela inicial.** Ao clicar em iniciar um novo projeto, você verá um campo de texto para descrever o que quer, e um conjunto de pontos de partida — algo como uma página interativa, uma apresentação de slides, um documento, um esboço simples ou uma animação. Se você não souber qual escolher, use a opção de começar em branco: ela é a mais segura para o primeiro contato.

> 📸 **Sugestão de Prints:** sequência numerada de 3 capturas de tela: (1) a tela inicial com o campo de prompt e as opções de tipo de projeto, com um círculo destacando "começar em branco"; (2) o campo de texto já preenchido com um exemplo de pedido; (3) o botão de enviar/gerar em destaque. Por quê: substitui três parágrafos de instrução textual por um percurso visual direto, eliminando a principal fonte de travamento identificada na versão anterior do curso.

**O pedido não precisa ser perfeito — precisa ser claro.** Um bom primeiro pedido conta três coisas: o **conteúdo** (sobre o que é), o **público** (quem vai ver) e o **clima** (que sensação deve passar). Você não precisa de vocabulário técnico para isso — é a mesma informação que você já usa ao planejar uma aula.

| Pedido vago | Pedido claro |
|---|---|
| "Faça uma página bonita sobre minha disciplina." | "Crie uma página de apresentação da disciplina de Ciências para o 6º ano, com um clima acolhedor e curioso, mostrando os temas do bimestre." |

**O Claude pode fazer perguntas antes de gerar — isso é esperado, não um erro.** Ele pode perguntar sobre tom, formato ou o que priorizar. Responda com frases curtas; não existe resposta errada nesta etapa.

> 📸 **Sugestão de Prints:** captura de tela de um exemplo real de tela de perguntas de esclarecimento do Claude (tom, público, formato), com uma legenda explicando "isso é normal — responda em uma frase cada". Por quê: sem essa imagem, um iniciante que nunca viu essa tela pode interpretar as perguntas como um erro e desistir.

**A geração leva tempo — e isso é normal.** A primeira geração de uma página costuma levar de alguns minutos até dez minutos, dependendo da complexidade do pedido. Use esse tempo para reler o que você escreveu, não para fechar a aba.

### Conceito de Design da Aula: Densidade Visual

1. **O que é?** A quantidade de informação e elementos visuais presentes em uma mesma área da tela.
2. **Por que importa?** Uma página muito densa cansa antes mesmo de ser lida; uma página muito vazia parece incompleta. O equilíbrio certo depende do público.
3. **Como perceber na tela?** Olhe seu primeiro rascunho e pergunte: "dá para respirar entre os blocos, ou tudo parece amontoado?"
4. **Como pedir ao Claude para melhorar?** "Esta página está com informação demais para uma primeira leitura — reduza para o essencial" ou "esta página está muito vazia — adicione um elemento de apoio nesta seção."

### Antes e Depois

**Antes**
Você ainda não tem uma página — só uma ideia na cabeça.

**Peça ao Claude:**
> "Crie uma página simples de apresentação da minha disciplina de [nome da disciplina], para alunos de [idade/série], com um clima [acolhedor / animado / sério e direto]."

**Depois, observe:**
- o que o Claude priorizou visualmente sem você pedir;
- se o clima que você descreveu realmente aparece no resultado;
- se a densidade de informação parece adequada para o público que você descreveu.

### 🧪 Pílula Hands-on

**Objetivo:** produzir sua primeira página real com o Claude Design.

**Faça agora:**
1. Inicie um novo projeto e escolha "começar em branco".
2. Escreva o pedido do quadro "Antes e Depois" acima, preenchendo os colchetes com sua disciplina real.
3. Envie e aguarde a geração — sem fechar a aba.
4. Se o Claude fizer perguntas, responda cada uma em uma frase curta.

**Observe:**
- o título gerado;
- as seções em que o conteúdo foi dividido;
- se algo te surpreendeu, para melhor ou para pior.

**Resultado esperado:** uma página completa aparece no canvas, refletindo o conteúdo, o público e o clima que você descreveu.

### 🔧 Troubleshooting

**Problema:** a geração está demorando muito e parece travada.
**Possível causa:** gerações completas costumam levar minutos, especialmente em horários de pico de uso.
**Como resolver:** aguarde até 10 minutos sem fechar ou atualizar a aba. Se não concluir depois disso, tente recarregar em uma aba nova, mantendo a original aberta até confirmar que precisa recomeçar.

**Problema:** o resultado não tem nada a ver com o que eu pedi.
**Possível causa:** o pedido pode ter sido interpretado de forma genérica por faltar contexto (público ou clima).
**Como resolver:** não regenere do zero. Use o chat para pedir um ajuste específico, contando o que faltou — você vai praticar exatamente isso na Aula 1.4.

---

## Aula 1.3 — Entendendo o Que Apareceu na Tela

### Objetivos da Aula

- Reconhecer os principais elementos visuais de uma página gerada pelo Claude.
- Diferenciar título, conteúdo, componentes e ações principais.
- Perceber, de forma inicial, o que guia o olhar em uma página.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- apontar, na sua própria página, onde está o título, o conteúdo principal, os componentes e a ação principal;
- explicar por que alguns elementos chamam mais atenção do que outros;
- descrever sua página para outra pessoa usando esse vocabulário básico.

### Desenvolvimento da Aula

Você acabou de criar sua primeira página. Antes de mudar qualquer coisa nela, vale aprender a "ler" o que está na tela — do mesmo jeito que você ensinaria um aluno a identificar as partes de um texto antes de reescrevê-lo.

**Quatro elementos aparecem em praticamente qualquer página:**

1. **Título** — o que identifica do que se trata a página.
2. **Conteúdo** — o texto, as informações, a substância que você pediu.
3. **Componentes** — as peças visuais que organizam o conteúdo (caixas, cartões, listas, menus). Vamos aprofundar isso na Parte 4.
4. **Ação principal** — o que a página espera que a pessoa faça (um botão, um link, um convite claro).

**Nem tudo tem o mesmo peso — e isso não é acidente.** Repare que, mesmo sem ninguém explicar, seus olhos provavelmente foram primeiro para o título, depois para os blocos maiores de texto, e só depois para os detalhes menores. Isso tem nome — **hierarquia visual** — e é o assunto central da Parte 2. Por enquanto, o objetivo é só notar que essa ordem existe.

> 📸 **Sugestão de Prints:** a página criada na Aula 1.2, com quatro etiquetas numeradas sobrepostas apontando para título, conteúdo, um componente (ex.: card ou lista) e a ação principal (ex.: botão). Por quê: nomear os elementos sobre a própria captura de tela do aluno é mais eficaz do que uma ilustração genérica — ele reconhece exatamente o que já criou.

### Conceito de Design da Aula: Hierarquia Visual (introdução)

1. **O que é?** A ordem em que os olhos percorrem uma página, definida por tamanho, posição, cor e peso dos elementos.
2. **Por que importa?** Se tudo tiver a mesma força visual, ninguém sabe por onde começar a olhar.
3. **Como perceber na tela?** Pergunte: "o que meus olhos veem primeiro, sem eu precisar procurar?"
4. **Como pedir ao Claude para melhorar?** Você ainda não vai pedir ajustes de hierarquia nesta aula — isso é o foco da Aula 2.1. Por enquanto, só observe e anote.

### 🧪 Pílula Hands-on

**Objetivo:** nomear os elementos da própria página.

**Faça agora:**
1. Abra a página criada na Aula 1.2.
2. Aponte (com o dedo na tela ou em voz alta) onde está o título, o conteúdo, um componente e a ação principal.
3. Escreva uma frase: "a primeira coisa que meus olhos veem nesta página é ___."

**Observe:**
- se a "primeira coisa que seus olhos veem" é o que você gostaria que fosse;
- se algum dos quatro elementos está difícil de identificar.

**Resultado esperado:** você consegue apontar os quatro elementos na sua própria página sem hesitar, e identificou o que atrai o olhar primeiro.

---

## Aula 1.4 — Fazendo Sua Primeira Alteração Visual

### Objetivos da Aula

- Pedir uma alteração visual específica ao Claude.
- Aprender a preservar a versão anterior antes de pedir uma mudança.
- Comparar duas versões da mesma página.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- pedir uma mudança pontual usando a estrutura objetivo + contexto + mudança desejada;
- guardar a versão "antes" de um jeito confiável;
- comparar duas versões e nomear o que mudou.

### Desenvolvimento da Aula

Este é o momento em que o curso deixa de ser "peça e receba" e começa a ser "converse e refine" — o verdadeiro diferencial do Claude Design.

**A estrutura de um bom pedido de mudança:** objetivo + contexto + mudança desejada.

> "Esta página será usada por alunos do ensino fundamental *(contexto)*. Quero que fique mais fácil de ler *(objetivo)*. Aumente o tamanho do texto principal e deixe só um botão em destaque *(mudança desejada)*."

Repare que isso não é "engenharia de prompt" — é a mesma clareza que você já usa ao dar uma instrução para uma turma.

**Antes de pedir a mudança, garanta uma forma de comparar depois.** Existem duas maneiras simples, e vale usar as duas até você se sentir confortável:

1. **Peça ao Claude para guardar a versão atual:** diga algo como "salve esta versão antes de eu pedir a próxima mudança." Isso permite voltar e comparar mais tarde na conversa.
2. **Tire um print da tela agora.** É a forma mais simples e nunca falha, independente de qualquer recurso da ferramenta: uma captura de tela sua, do jeito que a página está *antes* da mudança.

> 📸 **Sugestão de Prints:** comparação lado a lado — a versão da página **antes** da alteração à esquerda, e a versão **depois** à direita, com uma seta vermelha apontando para o elemento que mudou. Por quê: este é o primeiro de muitos momentos de comparação do curso; estabelecer aqui o padrão visual "antes à esquerda, depois à direita" cria uma convenção que se repete em todas as aulas seguintes.

### Conceito de Design da Aula: Refinamento Iterativo (na prática)

1. **O que é?** O ato concreto de pedir uma mudança, ver o resultado, e decidir se repete o processo.
2. **Por que importa?** É a diferença entre "gerar uma vez e aceitar" e "usar o Claude Design de verdade".
3. **Como perceber na tela?** Compare o antes e o depois: se pelo menos uma coisa específica mudou como você pediu, o ciclo funcionou.
4. **Como pedir ao Claude para melhorar?** Use sempre objetivo + contexto + mudança desejada, e peça uma coisa de cada vez — mudanças pontuais são mais fáceis de avaliar do que mudanças em bloco.

### Antes e Depois

**Antes**
A página criada na Aula 1.2, sem nenhum ajuste.

**Peça ao Claude:**
> "Salve esta versão. Depois, quero que o título desta página fique claramente mais destacado do que o resto do texto."

**Depois, observe:**
- o que especificamente mudou de tamanho, cor ou posição;
- se ficou mais fácil identificar do que se trata a página em menos de dois segundos;
- se alguma outra coisa mudou que você não pediu.

### 🧪 Pílula Hands-on

**Objetivo:** completar seu primeiro ciclo real de pedido → geração → comparação.

**Faça agora:**
1. Tire um print da sua página atual (ou peça ao Claude para salvar a versão).
2. Envie o pedido de mudança do quadro "Antes e Depois" acima.
3. Compare o print antigo com o resultado novo.

**Observe:**
- o elemento que mudou;
- se a mudança resolveu o que você pediu;
- se você conseguiria explicar essa mudança para um colega em uma frase.

**Resultado esperado:** você tem duas versões da mesma página e consegue nomear exatamente o que é diferente entre elas.

### 🔧 Troubleshooting

**Problema:** não sei mais como era a página antes da mudança.
**Possível causa:** a alteração foi aplicada diretamente sobre o rascunho anterior, sem que uma cópia tivesse sido guardada antes.
**Como resolver:** peça ao Claude "volte para a versão anterior" — a conversa geralmente preserva o histórico. Para não depender disso, adote o hábito de tirar um print antes de cada mudança grande, a partir de agora.

---
---

# Parte 2 — Organizando a Informação

Com uma página no ar e o primeiro ciclo de ajuste praticado, esta parte ensina a organizar o conteúdo para que ele seja compreendido rapidamente — o núcleo de qualquer bom design.

## Aula 2.1 — Hierarquia Visual: o Que Vem Primeiro

### Objetivos da Aula

- Aprofundar o conceito de hierarquia visual introduzido na Aula 1.3.
- Usar tamanho, peso e posição para destacar o elemento mais importante de uma página.
- Corrigir uma página onde nada se destaca.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- identificar uma página sem hierarquia clara;
- pedir ao Claude para destacar um elemento específico;
- explicar por que uma versão com hierarquia é mais fácil de escanear do que uma sem.

### Desenvolvimento da Aula

A hierarquia visual funciona como a organização de uma aula no quadro. O título precisa chamar atenção primeiro, os tópicos vêm depois, e os exemplos aparecem como informação de apoio. Ninguém precisa explicar essa ordem — o próprio tamanho da letra no quadro já avisa o que é mais importante.

**Quando a hierarquia falha, tudo grita ao mesmo tempo.** Título, texto e detalhes do mesmo tamanho criam o que chamamos de "gritaria visual": nada se destaca porque tudo está competindo pela mesma atenção.

| Sem hierarquia | Com hierarquia |
|---|---|
| Título, texto e detalhes todos do mesmo tamanho | Título grande e em destaque, subtítulo médio, texto de apoio menor |

**Como pedir:** nomeie o que precisa se destacar e o que pode ficar em segundo plano. "Quero que [elemento] seja a primeira coisa vista nesta página. Aumente-o e deixe o restante mais discreto" é uma instrução que o Claude executa com precisão.

> 📸 **Sugestão de Prints:** comparação antes/depois da mesma página, antes com todos os textos do mesmo tamanho (esquerda) e depois com hierarquia clara aplicada (direita). Destacar com um círculo o título ampliado e com uma seta a redução do texto de apoio. Por quê: hierarquia é um conceito que se entende em um olhar e demora parágrafos para descrever — a imagem substitui a explicação.

### Conceito de Design da Aula: Hierarquia Visual (aprofundamento)

1. **O que é?** O uso deliberado de tamanho, peso, cor e posição para indicar o que deve ser visto primeiro, segundo e terceiro.
2. **Por que importa?** Alunos, pais e colegas escaneiam uma página antes de ler palavra por palavra. Sem hierarquia, a leitura vira esforço extra.
3. **Como perceber na tela?** Cubra a página com a mão e revele aos poucos: o que aparece primeiro deveria ser, de fato, o mais importante.
4. **Como pedir ao Claude para melhorar?** "Aumente o contraste de tamanho entre o título e o corpo do texto" ou "quero que [elemento] seja visto antes de qualquer outra coisa nesta página."

### Antes e Depois

**Antes**
Página com título pouco destacado, texto corrido do mesmo tamanho em toda a página, sem prioridade clara.

**Peça ao Claude:**
> "Reorganize esta página para deixar o título claramente prioritário. O restante do conteúdo deve ficar visivelmente menor e mais discreto."

**Depois, observe:**
- o que mudou de tamanho e peso;
- se o olho vai direto para o título agora;
- que decisão de design o Claude tomou para criar esse destaque (tamanho? cor? posição? as três?).

### 🧪 Pílula Hands-on

**Objetivo:** aplicar hierarquia visual deliberada em um elemento real.

**Faça agora:**
1. Na sua página, escolha um elemento que deveria ser a primeira coisa vista (título, data, nome de uma atividade).
2. Peça: "Quero que [elemento] seja a primeira coisa que as pessoas veem nesta página. Deixe-o maior e mais destacado, e o restante mais discreto."
3. Compare com a versão anterior.

**Observe:**
- se o elemento escolhido realmente chama atenção primeiro agora;
- o que ficou mais discreto para abrir espaço para esse destaque;
- se a mudança usou tamanho, cor, posição, ou uma combinação.

**Resultado esperado:** o elemento escolhido se torna, de forma perceptível, o primeiro ponto de atenção da página.

---

## Aula 2.2 — Agrupando com Seções e Cards

### Objetivos da Aula

- Compreender o princípio de proximidade: itens próximos parecem relacionados.
- Organizar conteúdo solto em seções e cards.
- Aplicar esse agrupamento a uma lista real de conteúdos escolares.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- identificar conteúdo "solto" que deveria estar agrupado;
- pedir ao Claude para organizar uma lista em cards ou seções;
- explicar por que a proximidade comunica relação, mesmo sem nenhuma linha ou caixa desenhada.

### Desenvolvimento da Aula

Pense em como você organiza materiais de uma atividade: tudo que pertence à "parte 1" fica junto, fisicamente separado do que pertence à "parte 2". Na tela, isso se chama **proximidade**: elementos próximos parecem pertencer ao mesmo grupo; elementos afastados parecem tratar de assuntos diferentes — mesmo sem nenhuma linha os separando.

**Cards são a forma mais simples de aplicar proximidade.** Um card é uma "caixinha" que resume uma informação isolada — uma atividade, um tópico, um projeto de aluno. Cada card mantém seu conteúdo unido e visivelmente separado dos outros cards.

**Seções fazem o mesmo em uma escala maior:** um bloco temático (como "Objetivos", "Atividades", "Avaliação") separa partes diferentes de uma página inteira.

> 📸 **Sugestão de Prints:** duas versões da mesma lista de tópicos — à esquerda, os tópicos soltos, um embaixo do outro sem agrupamento; à direita, os mesmos tópicos organizados em cards. Destacar com uma chave (colchete) cada card, mostrando visualmente onde cada grupo começa e termina. Por quê: proximidade é um efeito perceptivo — só é realmente entendido quando visto, não descrito.

### Conceito de Design da Aula: Proximidade

1. **O que é?** O princípio de que elementos colocados próximos uns dos outros são percebidos como relacionados.
2. **Por que importa?** Permite organizar informação sem precisar de linhas, molduras ou cores para separar grupos — só a distância já comunica.
3. **Como perceber na tela?** Pergunte: "dá para saber quais itens pertencem ao mesmo grupo só de olhar, sem ler o texto?"
4. **Como pedir ao Claude para melhorar?** "Organize estes tópicos em cards, um para cada um" ou "agrupe visualmente os itens que tratam do mesmo assunto."

### Antes e Depois

**Antes**
Uma lista de 4 a 5 tópicos da disciplina, todos em texto corrido, sem separação visual.

**Peça ao Claude:**
> "Organize estes tópicos em cards, um card para cada um: [liste seus tópicos]."

**Depois, observe:**
- se cada tópico agora tem um espaço visual próprio;
- se fica mais fácil contar rapidamente quantos tópicos existem;
- se algum card parece "sobrando" ou redundante.

### 🧪 Pílula Hands-on

**Objetivo:** transformar uma lista solta em grupos visuais organizados.

**Faça agora:**
1. Pense em 3 a 5 tópicos ou atividades da sua disciplina.
2. Peça ao Claude: "Organize estes tópicos em cards, um para cada um: [liste os tópicos]."
3. Observe o resultado no canvas.

**Observe:**
- se cada card segue o mesmo formato visual;
- a distância entre um card e outro comparada à distância entre os elementos dentro do mesmo card;
- se ficou mais fácil "escanear" a lista rapidamente.

**Resultado esperado:** os tópicos aparecem organizados em blocos visuais distintos, com espaço claro entre um card e outro.

---

## Aula 2.3 — Espaçamento e Alinhamento: Dando Ordem à Página

### Objetivos da Aula

- Compreender a função do espaço em branco em uma página.
- Reconhecer elementos desalinhados e corrigi-los.
- Aplicar espaçamento e alinhamento a uma seção sobrecarregada.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- identificar uma seção "apertada" e pedir mais espaço entre os elementos;
- identificar elementos desalinhados e pedir correção;
- explicar a diferença entre espaçamento (distância) e alinhamento (organização em linha).

### Desenvolvimento da Aula

**Espaçamento é como organizar carteiras em uma sala.** Mesmo que todos os elementos necessários estejam presentes — quadro, mesa, carteiras, materiais — se estiverem apertados demais, fica difícil circular e trabalhar. Numa tela, o problema raramente é falta de conteúdo. É falta de espaço entre os conteúdos.

**Alinhamento é diferente de espaçamento, mas trabalha junto com ele.** Alinhamento é garantir que elementos relacionados comecem e terminem na mesma linha invisível — como carteiras enfileiradas, mesmo bem espaçadas, parecem desorganizadas se estiverem tortas. Uma página pode ter espaço de sobra e, ainda assim, parecer bagunçada se os títulos, textos e botões não estiverem alinhados entre si.

| Problema comum | Versão melhor |
|---|---|
| Texto colado, títulos grudados no parágrafo seguinte, elementos começando em pontos diferentes da página | Espaço claro entre seções, e todos os elementos começando na mesma margem |

> 📸 **Sugestão de Prints:** print anotado de uma seção "antes", com setas vermelhas horizontais indicando o pouco espaço entre blocos de texto, e linhas verticais tracejadas mostrando que os elementos começam em pontos diferentes da margem. Ao lado, a versão "depois" com espaçamento ampliado e uma única linha vertical alinhando todos os elementos. Por quê: alinhamento é um dos erros mais difíceis de notar sem ajuda visual — uma régua ou linha guia desenhada sobre o print torna o problema óbvio.

### Conceito de Design da Aula: Espaçamento e Alinhamento

1. **O que é?** Espaçamento é a distância entre elementos; alinhamento é a organização desses elementos em relação a uma linha comum.
2. **Por que importa?** Espaçamento evita a sensação de aperto; alinhamento evita a sensação de bagunça, mesmo quando há espaço de sobra.
3. **Como perceber na tela?** Para espaçamento: "dá para respirar entre os blocos?" Para alinhamento: imagine uma linha vertical na margem esquerda — os elementos relacionados começam todos nela?
4. **Como pedir ao Claude para melhorar?** "Esta seção está muito apertada, dê mais espaço entre os itens" e "alinhe estes elementos pela mesma margem esquerda."

### Antes e Depois

**Antes**
Uma seção com textos colados, pouco espaço entre blocos, e elementos que começam em posições diferentes da página.

**Peça ao Claude:**
> "Esta seção está muito apertada e desorganizada. Aumente o espaço entre os itens e alinhe todos pela mesma margem."

**Depois, observe:**
- se a seção ficou mais fácil de escanear rapidamente;
- se os elementos agora parecem seguir uma linha comum;
- se algum item continua fora do padrão.

### 🧪 Pílula Hands-on

**Objetivo:** aplicar espaçamento e alinhamento juntos em uma seção real.

**Faça agora:**
1. Identifique uma seção da sua página que parece "cheia" ou "torta".
2. Peça: "Esta seção está muito apertada, dê mais respiro entre os elementos e alinhe todos pela mesma margem."
3. Compare com a versão anterior.

**Observe:**
- a distância entre os elementos antes e depois;
- se os elementos agora começam no mesmo ponto da página;
- se a seção parece mais "organizada" mesmo sem nenhum conteúdo ter sido removido.

**Resultado esperado:** a seção escolhida ganha respiro visível entre os elementos e uma linha de alinhamento consistente.

### 🔧 Troubleshooting

**Problema:** depois do ajuste, alguns elementos ficaram desalinhados de um jeito diferente.
**Possível causa:** pedidos muito amplos ("organize tudo") podem gerar reorganizações inesperadas em partes da página que você não queria mudar.
**Como resolver:** peça ajustes pontuais, nomeando a seção exata. Se o problema persistir, peça: "mantenha o restante da página como está, ajuste apenas [seção específica]."

---
---

# Parte 3 — Dando Personalidade ao Design

Com a informação organizada, esta parte ensina a "vestir" essa organização — cor, tipografia e consistência — sem perder de vista que bonito não é o mesmo que fácil de usar.

## Aula 3.1 — Cores que Ajudam (Não Só Decoram)

### Objetivos da Aula

- Entender cor como ferramenta funcional, não apenas decorativa.
- Aplicar contraste para melhorar legibilidade.
- Ajustar uma paleta de cores para um público específico.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- identificar quando uma combinação de cores prejudica a leitura;
- pedir ajuste de contraste ao Claude;
- explicar a diferença entre cor como clima e cor como função.

### Desenvolvimento da Aula

A mesma informação pode "vestir" um terno sério ou uma camiseta colorida, dependendo das cores escolhidas. A roupa muda a primeira impressão — mas, assim como uma roupa desconfortável atrapalha o dia inteiro, cores mal escolhidas atrapalham a leitura inteira.

**Cor cumpre dois papéis, e só um deles é estético:**

- **Contraste** — o que permite a leitura. Texto escuro em fundo claro (ou o inverso) é confortável; texto claro sobre fundo vibrante cansa a vista rapidamente.
- **Clima** — o que comunica uma sensação antes de qualquer palavra ser lida. Cores vibrantes tendem a passar energia; tons suaves tendem a passar calma.

Uma regra segura para começar: **poucas cores bem escolhidas** funcionam melhor do que muitas cores competindo entre si.

| Problema comum | Versão melhor |
|---|---|
| Fundo colorido vibrante atrás de texto pequeno | Fundo neutro, com a cor forte reservada para um único destaque |

> 📸 **Sugestão de Prints:** comparação antes/depois lado a lado da mesma seção de texto — antes com baixo contraste (texto cinza claro sobre fundo colorido), depois com alto contraste (texto escuro sobre fundo neutro, cor reservada para um botão). Ampliar em destaque apenas o bloco de texto para deixar a diferença de legibilidade evidente. Por quê: contraste insuficiente é algo que se sente ao tentar ler, mas raramente se percebe ao simplesmente olhar rápido — a ampliação força a comparação de legibilidade real.

### Conceito de Design da Aula: Cores e Contraste

1. **O que é?** Cor é a escolha de tons de uma página; contraste é a diferença de claridade entre o texto e o fundo em que ele aparece.
2. **Por que importa?** Sem contraste suficiente, mesmo uma cor bonita torna o texto difícil ou impossível de ler.
3. **Como perceber na tela?** Afaste-se da tela ou entorne os olhos: o texto ainda se distingue claramente do fundo?
4. **Como pedir ao Claude para melhorar?** "Aumente o contraste entre o texto e o fundo para melhorar a leitura" ou "use poucas cores, reservando a cor mais forte só para o botão principal."

> **Nota:** o Claude pode escolher combinações visualmente agradáveis, mas pouco legíveis. Sempre confira você mesmo antes de considerar a página pronta — isso será aprofundado como hábito na Parte 7 (Acessibilidade).

### Antes e Depois

**Antes**
Página com fundo colorido vibrante atrás do texto principal, cansativa de ler.

**Peça ao Claude:**
> "Esta página será usada por alunos do ensino fundamental. Aumente o contraste entre o texto e o fundo para facilitar a leitura, e reserve a cor mais forte apenas para o botão principal."

**Depois, observe:**
- se o texto ficou visivelmente mais fácil de ler;
- onde a cor forte foi aplicada;
- se o clima geral da página mudou.

### 🧪 Pílula Hands-on

**Objetivo:** melhorar a legibilidade de uma página através do contraste.

**Faça agora:**
1. Escolha uma seção da sua página com texto sobre fundo colorido.
2. Peça: "Aumente o contraste entre o texto e o fundo desta seção para melhorar a leitura."
3. Compare a versão nova com a anterior.

**Observe:**
- a diferença de esforço para ler o texto antes e depois;
- se a cor de destaque ficou reservada a menos elementos;
- se o clima da página mudou ou se manteve.

**Resultado esperado:** o texto se torna visivelmente mais legível, sem perder a identidade visual da página.

---

## Aula 3.2 — Tipografia: Escolhendo as Letras Certas

### Objetivos da Aula

- Compreender a diferença entre tipografia decorativa e tipografia legível.
- Ajustar tamanho e estilo de fonte para um público específico.
- Reconhecer quando uma fonte decorativa está sendo usada em excesso.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- identificar um texto difícil de ler por causa da fonte escolhida;
- pedir ajuste de tipografia com base no público-alvo;
- explicar quando vale usar uma fonte decorativa e quando não vale.

### Desenvolvimento da Aula

Fontes decorativas podem parecer atraentes em um título, mas cansam — ou até impedem — a leitura em blocos de texto mais longos. Para textos que crianças pequenas vão ler, letras maiores e mais simples fazem diferença real na compreensão.

**Regra prática:** fonte decorativa está liberada em títulos curtos; texto corrido pede uma fonte simples e neutra.

| Problema comum | Versão melhor |
|---|---|
| Fonte decorativa em parágrafos inteiros — difícil de ler | Fonte decorativa só no título; texto corrido em fonte simples e legível |

**Um pedido que resolve a maioria dos casos escolares:**

> "Deixe esta página mais fácil de ler para alunos do ensino fundamental."

Repare que esse pedido não cita nenhum nome técnico de fonte — descreve o efeito desejado, e o Claude traduz isso em decisões de tipografia.

> 📸 **Sugestão de Prints:** print anotado mostrando um parágrafo inteiro em fonte decorativa (antes), com uma legenda circulando trechos difíceis de decifrar; ao lado, o mesmo parágrafo em fonte simples (depois), com a legenda "mesmo conteúdo, leitura sem esforço". Por quê: a dificuldade de leitura de uma fonte decorativa em bloco só é percebida ao tentar ler o texto inteiro — o print precisa mostrar um parágrafo completo, não apenas uma palavra isolada.

### Conceito de Design da Aula: Tipografia

1. **O que é?** O estilo, tamanho e formato das letras usadas em uma página.
2. **Por que importa?** Afeta diretamente a legibilidade e comunica um tom — sério, divertido, formal — antes mesmo do conteúdo ser lido.
3. **Como perceber na tela?** Leia um parágrafo inteiro em voz alta: você tropeçou nas letras ou leu de forma fluida?
4. **Como pedir ao Claude para melhorar?** "Deixe esta página mais fácil de ler para [idade/série]" ou "use uma fonte decorativa só no título, e uma fonte simples no restante do texto."

### Antes e Depois

**Antes**
Texto corrido inteiro em uma fonte decorativa, difícil de ler rapidamente.

**Peça ao Claude:**
> "Deixe esta página mais fácil de ler para alunos de [idade/série]. Use uma fonte decorativa apenas no título."

**Depois, observe:**
- a diferença de tamanho de letra entre título e corpo do texto;
- se o texto corrido ficou visivelmente mais simples de ler;
- se a identidade visual da página se perdeu ou se manteve.

### 🧪 Pílula Hands-on

**Objetivo:** ajustar a tipografia de uma página para o público real dela.

**Faça agora:**
1. Escolha a faixa etária real do seu público (uma turma específica).
2. Peça: "Deixe esta página mais fácil de ler para alunos de [idade/série]."
3. Observe o que muda no tamanho e no estilo das letras.

**Observe:**
- se o tamanho do texto aumentou;
- se a fonte do corpo do texto ficou mais simples;
- se o título manteve alguma personalidade visual.

**Resultado esperado:** o texto corrido fica visivelmente mais fácil de ler, mantendo o título com identidade própria.

---

## Aula 3.3 — Consistência: Criando um Estilo Próprio

### Objetivos da Aula

- Compreender por que repetir escolhas visuais fortalece a comunicação.
- Verificar se uma página mantém o mesmo estilo em todas as seções.
- Aplicar o mesmo padrão visual a duas páginas diferentes.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- identificar uma inconsistência visual dentro da mesma página;
- pedir ao Claude para manter um estilo entre páginas diferentes;
- explicar por que consistência gera confiança e familiaridade.

### Desenvolvimento da Aula

Pense em como você usa sempre a mesma cor de caneta para marcar "atenção" no quadro. Depois de ver esse padrão uma vez, a turma reconhece o significado sem precisar de explicação nova. Consistência visual funciona da mesma forma: repetir as mesmas cores, fontes e formatos de caixa cria um "idioma visual" que a pessoa aprende a reconhecer rapidamente.

**Onde a inconsistência aparece:** títulos de tamanhos diferentes em seções parecidas; cards com formatos diferentes para o mesmo tipo de conteúdo; botões com cores diferentes para a mesma ação em páginas diferentes.

**Consistência entre páginas diferentes.** Se você for criar mais de uma peça para o mesmo projeto — por exemplo, uma página de disciplina e depois um cronograma — vale pedir explicitamente que o Claude mantenha o mesmo estilo:

> "Crie esta nova página mantendo o mesmo estilo visual (cores, fontes e formato de cards) da página que fizemos antes."

> 📸 **Sugestão de Prints:** duas páginas diferentes do mesmo projeto lado a lado — uma com estilos inconsistentes entre si (fontes e cores diferentes) e outra com o mesmo padrão visual aplicado às duas. Circular os elementos que se repetem (cor do botão, formato do card, fonte do título) na versão consistente. Por quê: consistência só é perceptível quando duas peças são vistas juntas — uma página isolada não revela o problema.

### Conceito de Design da Aula: Consistência

1. **O que é?** O uso repetido das mesmas escolhas visuais (cores, fontes, formatos) ao longo de uma página ou de um conjunto de páginas.
2. **Por que importa?** Cria familiaridade: depois de aprender o padrão uma vez, a pessoa reconhece o significado sem esforço nas vezes seguintes.
3. **Como perceber na tela?** Compare duas seções (ou duas páginas) parecidas: os títulos, cores e formatos se repetem, ou cada uma parece "de um projeto diferente"?
4. **Como pedir ao Claude para melhorar?** "Mantenha o mesmo estilo visual desta página em [nova página]" ou "deixe todos os cards desta página com o mesmo formato."

### Antes e Depois

**Antes**
Duas seções (ou duas páginas) do mesmo projeto com fontes, cores ou formatos de card diferentes entre si.

**Peça ao Claude:**
> "Deixe o estilo visual (cores, fontes e formato de cards) consistente entre estas duas seções/páginas."

**Depois, observe:**
- quais elementos passaram a se repetir;
- se as duas partes agora parecem pertencer ao mesmo projeto;
- se alguma diferença proposital (por exemplo, uma cor de destaque para "urgente") foi mantida de propósito.

### 🧪 Pílula Hands-on

**Objetivo:** verificar e corrigir a consistência visual de um material com mais de uma parte.

**Faça agora:**
1. Se você já tem duas páginas ou seções do mesmo projeto, compare-as lado a lado. Se não tem, peça ao Claude para criar uma segunda peça simples (ex.: um aviso curto) a partir da sua página existente.
2. Peça: "Mantenha o mesmo estilo visual da página anterior nesta nova peça."
3. Compare as duas.

**Observe:**
- se cores e fontes se repetem entre as duas peças;
- se o formato dos componentes (cards, botões) é o mesmo;
- se alguém reconheceria as duas peças como parte do mesmo projeto.

**Resultado esperado:** as duas peças compartilham um padrão visual reconhecível, mesmo tendo conteúdos diferentes.

---
---

# Parte 4 — Trabalhando com Componentes

Até aqui você organizou e estilizou conteúdo já existente. Nesta parte, você aprende a pensar em uma interface como um conjunto de peças reutilizáveis — a base de qualquer criação mais ambiciosa daqui em diante.

## Aula 4.1 — As Peças Reutilizáveis da Interface

### Objetivos da Aula

- Reconhecer os componentes mais comuns de uma interface: botões, cards, menus, cabeçalhos, campos e listas.
- Entender o conceito de affordance — um elemento parecer aquilo que ele faz.
- Nomear componentes na própria página.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- apontar botões, cards, menus, cabeçalhos e listas na sua página;
- explicar por que um botão precisa "parecer clicável";
- pedir ao Claude a criação de um componente específico.

### Desenvolvimento da Aula

Componentes são como peças reutilizáveis de um material pedagógico. Você pode usar o mesmo modelo de caixa de "Atenção" em diferentes partes de uma aula — o aluno aprende rápido a reconhecer aquele formato e já sabe o que esperar dele. Um botão, um card ou um menu funcionam exatamente assim: um molde visual repetido que cria familiaridade.

**Os componentes mais comuns, no contexto escolar:**

| Componente | O que é | Uso escolar comum |
|---|---|---|
| **Card** | Uma "caixinha" com uma informação isolada | Uma atividade, um tópico, um projeto de aluno |
| **Botão** | Uma ação clara e clicável | "Ver atividade", "Baixar material" |
| **Menu** | Uma lista de opções, geralmente no topo | Seções de um cronograma ou projeto |
| **Cabeçalho** | O topo que identifica a página | Nome da disciplina, turma ou projeto |
| **Campo** | Um espaço para inserir informação | Um campo de busca ou de resposta |
| **Lista** | Itens organizados em sequência | Passos de uma atividade, regras de uma tarefa |

**Um botão precisa parecer um botão.** Esse princípio tem nome: **affordance** — a ideia de que a aparência de um elemento já sugere o que ele faz, sem precisar de instrução extra. Um botão com contraste de cor, bordas visíveis e um verbo de ação ("Ver mais", "Enviar") comunica sozinho que pode ser clicado. Um texto sem destaque nenhum, mesmo que também seja clicável, não passa essa mensagem.

> 📸 **Sugestão de Prints:** captura da página do aluno com etiquetas numeradas apontando cada componente identificado (card, botão, menu, cabeçalho), e um zoom ampliado especificamente no botão principal, com uma seta destacando o contraste de cor que indica "isto pode ser clicado". Por quê: affordance é um conceito perceptivo — o aluno precisa *ver* a diferença entre um botão com bom contraste e um elemento de texto qualquer para internalizar o princípio.

### Conceito de Design da Aula: Componentes e Affordance

1. **O que é?** Componentes são peças visuais reutilizáveis; affordance é a aparência de um componente comunicar sua função sem explicação.
2. **Por que importa?** Componentes dão consistência; affordance evita que a pessoa precise "adivinhar" onde clicar.
3. **Como perceber na tela?** Pergunte: "um aluno saberia, só de olhar, onde deve clicar?"
4. **Como pedir ao Claude para melhorar?** "Deixe este botão com mais contraste, para ficar claro que pode ser clicado" ou "crie um menu no topo com as seções deste projeto."

### Antes e Depois

**Antes**
Um botão sem contraste, parecido com texto comum, sem indicação clara de que é clicável.

**Peça ao Claude:**
> "Este botão não parece clicável. Aumente o contraste e deixe claro visualmente que é uma ação."

**Depois, observe:**
- o que mudou na aparência do botão (cor, borda, sombra, texto);
- se agora fica óbvio que se trata de uma ação;
- se o restante da página continua com o mesmo estilo.

### 🧪 Pílula Hands-on

**Objetivo:** identificar e reforçar a affordance de um componente de ação.

**Faça agora:**
1. Localize o botão ou ação principal da sua página.
2. Peça: "Este botão precisa parecer mais claramente clicável. Aumente o contraste e o destaque dele."
3. Compare o antes e o depois.

**Observe:**
- a diferença de contraste do botão;
- se a mudança tornou a ação mais óbvia;
- se o botão continua alinhado ao restante do estilo da página.

**Resultado esperado:** o botão principal se torna visivelmente reconhecível como uma ação clicável.

---

## Aula 4.2 — Montando uma Página com Vários Componentes

### Objetivos da Aula

- Combinar múltiplos componentes em uma única página coerente.
- Evitar excesso de componentes competindo entre si.
- Praticar a escolha do componente certo para cada tipo de conteúdo.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- montar uma página combinando cabeçalho, cards e um botão de ação;
- identificar quando há componentes demais em uma mesma página;
- justificar a escolha de um componente para um conteúdo específico.

### Desenvolvimento da Aula

Depois de reconhecer os componentes isoladamente (Aula 4.1), o próximo passo é combiná-los. Uma página educacional típica reúne um cabeçalho (identifica do que se trata), uma ou mais seções organizadas em cards (o conteúdo principal) e uma ação clara (o que fazer a seguir).

**O erro mais comum nesta etapa é excesso, não falta.** Usar componentes demais em uma página só cria bagunça visual — mesmo com hierarquia e espaçamento corretos (Parte 2). Cada tipo de componente deve ter uma função clara: se dois cards fazem a mesma coisa, um deles provavelmente é desnecessário.

**Uma pergunta simples resolve a maioria das dúvidas de excesso:** para cada componente da página, pergunte "o que aconteceria se eu removesse isso?" Se a resposta for "nada", ele provavelmente pode sair.

> 📸 **Sugestão de Prints:** duas versões da mesma página — uma versão "antes" com componentes redundantes (dois cards parecidos, três botões diferentes para ações parecidas) e uma versão "depois" simplificada, com um X vermelho sobre os componentes removidos na primeira imagem. Por quê: excesso de componentes é mais fácil de perceber comparando um "cheio" contra um "enxuto" lado a lado do que descrevendo em texto o que remover.

### Conceito de Design da Aula: Componentes (aplicação) e Densidade Visual

1. **O que é?** A combinação deliberada de poucos componentes bem escolhidos, evitando repetição desnecessária.
2. **Por que importa?** Cada componente extra aumenta a carga de decisão de quem vê a página — "onde eu olho, onde eu clico?"
3. **Como perceber na tela?** Conte os componentes da sua página. Para cada um, pergunte se ele tem uma função que nenhum outro já cumpre.
4. **Como pedir ao Claude para melhorar?** "Esta página tem componentes repetidos — simplifique, mantendo só o essencial" ou "combine estes dois cards parecidos em um só."

### Antes e Depois

**Antes**
Uma página com componentes redundantes: por exemplo, dois cards com informação parecida ou mais de um botão de ação para o mesmo objetivo.

**Peça ao Claude:**
> "Esta página tem componentes repetidos ou parecidos demais. Simplifique, mantendo apenas um componente para cada função."

**Depois, observe:**
- quais componentes foram removidos ou combinados;
- se a página ficou mais fácil de entender rapidamente;
- se nenhuma informação importante se perdeu no processo.

### 🧪 Pílula Hands-on

**Objetivo:** montar (ou simplificar) uma página combinando cabeçalho, cards e uma ação principal.

**Faça agora:**
1. Peça ao Claude: "Organize esta página com um cabeçalho claro, o conteúdo dividido em cards, e apenas uma ação principal em destaque."
2. Conte quantos componentes diferentes aparecem no resultado.
3. Para cada um, decida se ele tem uma função própria.

**Observe:**
- se algum componente parece redundante;
- se a ação principal está clara e única;
- se a página como um todo parece "enxuta" ou "carregada".

**Resultado esperado:** uma página com cabeçalho, cards organizados e uma única ação principal, sem componentes competindo entre si.

### 🔧 Troubleshooting

**Problema:** pedi um ajuste em um componente específico usando o comentário direto no elemento, e nada mudou.
**Possível causa:** a função de comentário direto no elemento tem uma falha intermitente conhecida na versão beta — o comentário às vezes não é registrado.
**Como resolver:** copie o texto do seu comentário e cole diretamente no campo de chat. Isso funciona como alternativa confiável sempre que o comentário direto não parecer surtir efeito.

**Problema:** depois de adicionar vários componentes, alguns ficaram com formatos diferentes entre si.
**Possível causa:** pedidos feitos em momentos diferentes da conversa podem gerar pequenas variações de estilo.
**Como resolver:** peça explicitamente: "deixe todos os cards desta página com o mesmo formato e tamanho" — reforçando o conceito de consistência da Aula 3.3.

---
---

# Parte 5 — Refinando Interfaces

Você já sabe criar, organizar, estilizar e montar com componentes. Esta parte formaliza a habilidade mais importante do curso: avaliar criticamente o próprio resultado antes — e depois — de qualquer ajuste.

## Aula 5.1 — Virando Crítico do Próprio Design

### Objetivos da Aula

- Aplicar um checklist de avaliação crítica a qualquer página gerada.
- Diferenciar avaliação estética de avaliação funcional.
- Produzir uma lista de problemas específicos e priorizados.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- responder ao checklist de avaliação crítica sobre qualquer página;
- diferenciar "está feio" de "está confuso";
- transformar uma impressão vaga em um problema específico e acionável.

### Desenvolvimento da Aula

É como corrigir a primeira versão da redação de um aluno: você não risca tudo de uma vez, mas também não aprova de cara só porque "ficou bonitinho". Você lê com atenção, identifica o que funciona e o que não funciona, e só depois devolve com comentários específicos. Com o Claude é igual — só que quem escreveu o rascunho foi a IA, e quem corrige agora é você.

**O checklist de observação**, dividido em três grupos:

**Dá para entender rápido?**
- Está fácil de entender?
- O elemento mais importante chama atenção primeiro?
- Há informação demais?

**Dá para usar?**
- O texto está legível?
- As cores ajudam ou atrapalham?
- Os elementos estão organizados?
- Um aluno saberia onde clicar?

**Faz sentido para o meu contexto?**
- O resultado combina com o público?
- O design ajuda o conteúdo ou apenas o enfeita?

**Avaliar pela estética é a armadilha mais comum.** Um design pode ser visualmente agradável e, ainda assim, confuso, ilegível ou fora do tom para os alunos. "Ficou bonito" não é uma resposta válida a nenhuma das perguntas acima.

> 📸 **Sugestão de Prints:** captura de uma página com três etiquetas coloridas sobrepostas, uma para cada grupo de perguntas do checklist ("entender rápido", "usar", "contexto"), cada etiqueta apontando para a parte da página mais relacionada àquele grupo. Por quê: transforma um checklist abstrato em um exercício de apontar sobre uma imagem real, tornando a avaliação mais concreta para quem está aprendendo a fazer isso pela primeira vez.

### Conceito de Design da Aula: Densidade Visual e Hierarquia (revisão crítica)

1. **O que é?** A aplicação conjunta dos conceitos já aprendidos como ferramenta de diagnóstico, não apenas de criação.
2. **Por que importa?** Saber nomear qual conceito está causando um problema transforma uma sensação vaga ("não gostei") em um pedido específico e executável.
3. **Como perceber na tela?** Para cada resposta negativa do checklist, pergunte: isso é um problema de hierarquia, densidade, espaçamento, cor, tipografia ou componente?
4. **Como pedir ao Claude para melhorar?** Você vai praticar isso na Aula 5.2 — por enquanto, o objetivo é só produzir a lista de problemas nomeados.

### Antes e Depois

**Antes**
Sua própria página, sem nenhuma avaliação crítica ainda aplicada.

**Não peça nada ao Claude ainda.** Esta é uma aula de observação.

**Depois, observe:**
- quantas perguntas do checklist tiveram resposta "não" ou "mais ou menos";
- se você consegue nomear, para cada resposta negativa, qual conceito das Partes 2, 3 ou 4 está envolvido;
- qual desses problemas parece mais urgente de resolver primeiro.

### 🧪 Pílula Hands-on

**Objetivo:** produzir uma lista de problemas específicos e priorizados.

**Faça agora:**
1. Abra sua página mais recente.
2. Responda, por escrito, as 9 perguntas do checklist acima.
3. Escolha a resposta mais negativa e nomeie o conceito de design relacionado a ela (hierarquia? espaçamento? cor? componente redundante?).

**Observe:**
- quantos problemas você identificou no total;
- se algum problema aparece em mais de uma pergunta ao mesmo tempo;
- qual problema, se resolvido, teria o maior impacto na clareza da página.

**Resultado esperado:** uma lista escrita de um a três problemas específicos, cada um nomeado com o conceito de design correspondente — pronta para virar pedido de ajuste na próxima aula.

---

## Aula 5.2 — O Ciclo do Refinamento na Prática

### Objetivos da Aula

- Transformar a lista de problemas da Aula 5.1 em pedidos de ajuste específicos.
- Praticar o ciclo completo: primeira versão → o que está estranho? → escolha um problema → peça uma melhoria → compare → refine novamente.
- Usar as diferentes formas de dar feedback ao Claude (chat, comentário no elemento, ajustes rápidos).

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- transformar "não gostei" em um pedido específico;
- escolher a forma de feedback adequada (chat, comentário no elemento ou ajuste rápido) para cada tipo de mudança;
- repetir o ciclo de refinamento de forma autônoma, sem depender de um roteiro passo a passo.

### Desenvolvimento da Aula

**O ciclo completo de refinamento:**

Primeira versão → O que está estranho? → Escolha um problema → Peça uma melhoria → Compare → Refine novamente

Você já praticou pedaços desse ciclo em quase toda aula anterior. Agora ele se torna explícito e repetível, sem precisar de um exemplo pronto para seguir.

**Três formas de pedir ajustes**, cada uma melhor para um tipo de mudança:

1. **Chat** — ideal para mudanças grandes e estruturais: "deixe a página inteira com um tom mais formal."
2. **Comentário direto no elemento** — clique na parte exata da tela que quer mudar e escreva o ajuste ali. Mais rápido do que descrever a localização em palavras.
3. **Ajustes rápidos** (no Claude Design, chamados de *Tweaks*) — pequenos controles, como controles deslizantes, para afinar detalhes sem escrever um novo pedido.

> 📸 **Sugestão de Prints:** captura da interface do Claude Design com três círculos numerados: (1) o campo de chat, (2) um clique de comentário sobre um elemento específico, (3) o painel de ajustes rápidos/Tweaks. Por quê: os três métodos têm localizações físicas diferentes na tela — sem a imagem, o aluno só tem os nomes, não sabe onde procurar cada um.

**A regra de ouro do feedback específico:** "não gostei" não ajuda ninguém a melhorar — nem um aluno, nem uma IA. "O título está pequeno, aumente e centralize" ajuda muito. Você já pratica essa habilidade toda vez que corrige uma atividade.

| Feedback vago | Feedback específico |
|---|---|
| "Não ficou legal." | "O título está pequeno e a cor de fundo dificulta a leitura." |
| "Deixa mais bonito." | "Aumente o espaço entre as seções e use uma cor de destaque só no botão principal." |

**Peça variações quando não tiver certeza.** "Mostre-me três versões diferentes do cabeçalho desta página" é sempre mais rápido do que tentar acertar em uma única tentativa.

### Conceito de Design da Aula: Refinamento Iterativo (autonomia)

1. **O que é?** A repetição consciente do ciclo completo, sem depender de um exemplo externo dizendo o que pedir.
2. **Por que importa?** É a habilidade que sustenta todo o resto do curso — sem ela, cada aula futura exigiria um roteiro novo.
3. **Como perceber na tela?** Você consegue, sozinho, olhar para qualquer página e produzir pelo menos um pedido de ajuste específico?
4. **Como pedir ao Claude para melhorar?** Escolha o problema mais urgente da sua lista da Aula 5.1, use objetivo + contexto + mudança desejada, e escolha entre chat, comentário ou ajuste rápido conforme o tipo de mudança.

### Antes e Depois

**Antes**
A lista de problemas específicos produzida na Aula 5.1.

**Peça ao Claude** (usando o problema mais urgente da sua lista):
> "[Descreva o contexto]. [Nomeie o problema específico]. [Diga a mudança desejada.]"

**Depois, observe:**
- se o pedido específico resolveu o problema em uma única rodada;
- se algo mais mudou além do que foi pedido;
- se ainda restam problemas da sua lista original.

### 🧪 Pílula Hands-on

**Objetivo:** completar um ciclo inteiro de refinamento de forma autônoma.

**Faça agora:**
1. Pegue o problema mais urgente da lista da Aula 5.1.
2. Transforme-o em um pedido específico e envie pelo método mais adequado (chat, comentário ou ajuste rápido).
3. Compare o resultado com a versão anterior.
4. Repita o ciclo com o segundo problema da sua lista, se houver tempo.

**Observe:**
- se cada pedido específico resolveu exatamente o que foi pedido;
- qual método de feedback (chat, comentário, ajuste rápido) pareceu mais rápido para cada tipo de mudança;
- quantas rodadas foram necessárias até você ficar satisfeito.

**Resultado esperado:** pelo menos um problema da sua lista original resolvido, com a comparação antes/depois documentada.

### 🔧 Troubleshooting

**Problema:** pedi para "salvar o que temos e tentar uma abordagem diferente", mas não sei como voltar à versão salva.
**Possível causa:** a versão anterior fica referenciável dentro da própria conversa, não em um menu separado.
**Como resolver:** peça diretamente "volte para a versão que salvamos antes" — a referência acontece pela conversa, não por navegação em menu.

**Problema:** depois de várias rodadas de ajuste, a página piorou em vez de melhorar.
**Possível causa:** mudanças acumuladas sem comparação constante podem se afastar do objetivo original.
**Como resolver:** peça para "recriar a página do zero, mas mantendo [liste as 2-3 melhores decisões já tomadas]" — isso é mais eficaz do que tentar consertar um resultado que já se perdeu.

---
---

# Parte 6 — Desktop e Mobile

## Aula 6.1 — Uma Página, Duas Telas

### Objetivos da Aula

- Compreender o conceito de responsividade.
- Reconhecer diferenças entre uma página pensada para computador e uma pensada para celular.
- Adaptar uma página existente para leitura em tela pequena.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- explicar o que significa "design responsivo" sem jargão técnico;
- identificar elementos que funcionam mal em uma tela pequena;
- pedir ao Claude uma adaptação para celular.

### Desenvolvimento da Aula

É como preparar o mesmo conteúdo para aparecer no quadro, em uma folha impressa ou na tela do celular: a informação continua sendo a mesma, mas precisa se reorganizar para caber bem em cada formato. Esse princípio técnico tem um nome — **design responsivo** — que significa apenas isso: o mesmo conteúdo se reorganizando para caber bem em telas diferentes, sem perder informação.

**Por que isso importa na prática:** boa parte de quem vai ver o material que você cria — alunos, famílias — provavelmente vai abri-lo primeiro no celular, não no computador.

**O que costuma quebrar em telas pequenas:**
- menus horizontais que não cabem na largura da tela;
- textos com fonte pequena demais para ler sem dar zoom;
- botões pequenos demais para tocar com o dedo;
- colunas lado a lado que deveriam empilhar uma sobre a outra.

> 📸 **Sugestão de Prints:** comparação lado a lado — a mesma página em formato desktop (larga, várias colunas) à esquerda, e a versão adaptada para celular (estreita, elementos empilhados, botões maiores) à direita. Usar molduras de dispositivo (formato de tela de computador e formato de tela de celular) para deixar clara a diferença de contexto. Por quê: responsividade é, por definição, uma comparação entre dois formatos — não existe forma de ensinar isso sem mostrar as duas versões lado a lado.

### Conceito de Design da Aula: Responsividade

1. **O que é?** A capacidade de uma mesma página se reorganizar para funcionar bem em telas de tamanhos diferentes.
2. **Por que importa?** A maioria das pessoas que vai ver seu material provavelmente vai abri-lo no celular.
3. **Como perceber na tela?** Peça para o Claude mostrar como a página fica em formato de celular, e observe se algo fica cortado, pequeno demais ou difícil de tocar.
4. **Como pedir ao Claude para melhorar?** "Crie uma versão desta página pensada para ser lida no celular" ou "aumente o tamanho dos botões para facilitar o toque em telas pequenas."

> **Nota de versão:** o comportamento do Claude Design em navegadores de celular não é garantido de forma estável nesta fase beta. As orientações desta aula tratam de como *pedir* uma versão adaptada para tela pequena — não de usar a ferramenta em si a partir de um celular.

### Antes e Depois

**Antes**
A página em formato desktop, com colunas lado a lado ou menu horizontal.

**Peça ao Claude:**
> "Crie uma versão desta página pensada para ser lida no celular. Empilhe os elementos que hoje estão lado a lado, e aumente o tamanho dos botões para facilitar o toque."

**Depois, observe:**
- se os elementos que eram colunas agora aparecem empilhados;
- se o texto continua legível sem precisar de zoom;
- se os botões parecem grandes o suficiente para tocar com o dedo.

### 🧪 Pílula Hands-on

**Objetivo:** adaptar uma página para leitura confortável em tela pequena.

**Faça agora:**
1. Escolha uma página já criada.
2. Peça: "Crie uma versão desta página pensada para ser lida no celular."
3. Compare a versão desktop com a versão celular lado a lado.

**Observe:**
- o que mudou de posição;
- o que aumentou de tamanho;
- se algum conteúdo foi resumido ou reorganizado.

**Resultado esperado:** duas versões da mesma página, cada uma adequada ao seu formato de tela, com o mesmo conteúdo essencial preservado.

### 🔧 Troubleshooting

**Problema:** a versão para celular ficou com texto cortado ou elementos sobrepostos.
**Possível causa:** conteúdo pensado originalmente para uma tela larga pode não caber diretamente em uma tela estreita sem reorganização mais profunda.
**Como resolver:** peça explicitamente "reduza a quantidade de texto visível de uma vez" ou "empilhe estes elementos em vez de colocá-los lado a lado" — adaptação para mobile às vezes exige simplificar, não só reorganizar.

---
---

# Parte 7 — Acessibilidade

## Aula 7.1 — Design para Todo Mundo

### Objetivos da Aula

- Compreender acessibilidade como parte da qualidade do design, não como etapa burocrática extra.
- Verificar contraste, tamanho de texto e clareza de linguagem em uma página.
- Pedir diretamente ao Claude uma avaliação de acessibilidade.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- explicar por que acessibilidade beneficia todos os alunos, não só alunos com alguma necessidade específica;
- verificar contraste mínimo e tamanho de texto em uma página;
- pedir ao Claude para avaliar e corrigir problemas de acessibilidade.

### Desenvolvimento da Aula

Uma sala de aula bem planejada pensa em todo mundo: quem está longe do quadro, quem tem dificuldade de leitura, quem precisa de mais tempo. Acessibilidade em design digital é essa mesma lógica aplicada à tela — e, exatamente como na sala de aula, quase sempre beneficia todo mundo, não apenas quem tem uma necessidade específica.

**O que verificar, em termos simples:**

- **Contraste:** o texto se distingue claramente do fundo, mesmo para quem tem dificuldade de enxergar cores próximas?
- **Tamanho do texto:** dá para ler sem precisar aproximar o rosto da tela ou aplicar zoom?
- **Clareza da linguagem:** as frases são diretas, sem jargão desnecessário?
- **Estrutura:** títulos e seções seguem uma ordem lógica, que faria sentido mesmo se lida em voz alta, de cima para baixo?
- **Elementos interativos:** botões e links são grandes e claros o suficiente para quem tem dificuldade motora tocar com precisão?

**O recurso mais direto desta aula:** você pode simplesmente pedir ao Claude para fazer essa checagem por você.

> "Avalie esta página em termos de acessibilidade e contraste, e liste o que poderia melhorar."

Isso não substitui o seu julgamento — mas dá um segundo olhar rápido, especialmente útil para quem ainda não tem o hábito de checar esses pontos manualmente.

> 📸 **Sugestão de Prints:** captura de uma página com quatro elementos circulados e numerados: (1) um trecho de texto com contraste insuficiente, (2) um texto pequeno demais, (3) um botão pequeno demais para tocar, (4) um trecho de linguagem excessivamente técnica. Ao lado, a versão corrigida com os quatro pontos resolvidos. Por quê: acessibilidade reúne vários critérios diferentes ao mesmo tempo — uma imagem com os quatro problemas nomeados simultaneamente ajuda o aluno a lembrar de checar todos, não só um.

### Conceito de Design da Aula: Acessibilidade

1. **O que é?** O conjunto de decisões de design que garantem que a página possa ser usada pelo maior número possível de pessoas, incluindo quem tem baixa visão, dificuldade de leitura ou limitações motoras.
2. **Por que importa?** Turmas de escola pública são heterogêneas. Acessibilidade não é um extra — é parte do que torna um material verdadeiramente utilizável por toda a turma.
3. **Como perceber na tela?** Peça a avaliação diretamente ao Claude, e complemente checando você mesmo o contraste, o tamanho do texto e a clareza da linguagem.
4. **Como pedir ao Claude para melhorar?** "Avalie esta página em termos de acessibilidade e contraste, e liste o que poderia melhorar" e, depois, peça a correção de cada ponto específico apontado.

### Antes e Depois

**Antes**
Uma página com pelo menos um problema de acessibilidade não verificado (contraste, tamanho de texto, linguagem ou tamanho de botão).

**Peça ao Claude:**
> "Avalie esta página em termos de acessibilidade e contraste, e corrija os pontos mais importantes que encontrar."

**Depois, observe:**
- quais problemas o Claude identificou que você não tinha notado;
- o que mudou especificamente para resolver cada um;
- se a página perdeu alguma característica visual importante no processo.

### 🧪 Pílula Hands-on

**Objetivo:** realizar uma auditoria de acessibilidade guiada pelo próprio Claude.

**Faça agora:**
1. Abra uma página já criada em uma aula anterior.
2. Peça: "Avalie esta página em termos de acessibilidade e contraste, e liste o que poderia melhorar."
3. Escolha um dos pontos levantados e peça a correção específica.

**Observe:**
- quantos pontos de melhoria o Claude listou;
- se algum deles já tinha sido notado por você em aulas anteriores (ex.: contraste, na Aula 3.1);
- se a correção resolveu o ponto sem prejudicar outras partes da página.

**Resultado esperado:** uma lista de pontos de acessibilidade avaliados pelo Claude, com pelo menos um deles corrigido e comparado.

> **Nota:** o resultado gerado pelo Claude é um ponto de partida. Você continua responsável por avaliar se a página realmente atende às necessidades reais da sua turma — a IA pode não conhecer particularidades específicas dos seus alunos.

---
---

# Parte 8 — Experiências Interativas

## Aula 8.1 — Cliques que Revelam Coisas

### Objetivos da Aula

- Compreender o que torna uma página interativa, em vez de apenas visual.
- Criar um elemento que reage a um clique.
- Reconhecer quando a interatividade tem função pedagógica e quando é desnecessária.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- explicar a diferença entre uma página estática e uma interativa;
- pedir ao Claude um elemento clicável simples (esconder/revelar);
- testar o elemento interativo diretamente no canvas.

### Desenvolvimento da Aula

É a diferença entre uma folha de atividade impressa, que o aluno preenche com caneta, e a mesma atividade na tela, em que clicar em "ver resposta" revela a solução na hora. O conteúdo pode ser o mesmo — o que muda é que a versão interativa **responde** a quem está usando.

**Recursos simples de interatividade, com uso escolar direto:**
- um botão que revela uma resposta;
- uma seção que expande ao ser clicada;
- um cronograma em que cada etapa mostra mais detalhes ao ser tocada.

**Sobre o código, rapidamente:** por trás dos panos, o Claude usa código — a mesma linguagem que faz os sites da internet funcionarem — para transformar sua ideia em algo que o navegador consegue mostrar e com que dá para interagir. Você não precisa entender esse código para usar a ferramenta, da mesma forma que não precisa entender de motor para dirigir um carro.

**Interatividade precisa servir a um objetivo — não é obrigatória.** Se não há motivo pedagógico claro, uma página estática e bem organizada continua sendo a escolha certa.

> 📸 **Sugestão de Prints:** sequência de 2 capturas (formato "antes do clique" / "depois do clique") mostrando o mesmo elemento fechado e depois aberto, com uma seta circular indicando a ação de clique entre as duas imagens. Se possível, um GIF curto mostrando o clique acontecendo em tempo real. Por quê: interatividade é, por natureza, movimento — uma única imagem estática nunca comunica “isto reage a um clique” com a mesma clareza que ver o clique acontecer.

### Conceito de Design da Aula: Feedback Visual

1. **O que é?** A resposta visível que a interface dá quando alguém interage com ela — por exemplo, uma resposta aparecendo depois de um clique.
2. **Por que importa?** Sem feedback visual, a pessoa não sabe se sua ação teve efeito.
3. **Como perceber na tela?** Clique no elemento interativo: algo muda de forma clara e imediata?
4. **Como pedir ao Claude para melhorar?** "Transforme esta pergunta em algo interativo: a resposta só deve aparecer quando a pessoa clicar em um botão."

### Antes e Depois

**Antes**
Uma pergunta ou informação estática, sempre visível na página.

**Peça ao Claude:**
> "Transforme esta pergunta em algo interativo: esconda a resposta até a pessoa clicar em um botão para revelar."

**Depois, observe:**
- se o clique realmente esconde e revela o conteúdo;
- se existe algum indício visual (ícone, texto do botão) de que ali existe algo para clicar;
- se essa interatividade tem uma função clara (estimular a pensar antes de ver a resposta).

### 🧪 Pílula Hands-on

**Objetivo:** criar e testar um primeiro elemento interativo.

**Faça agora:**
1. Escolha um elemento da sua página que poderia "reagir" a um clique — uma pergunta, uma curiosidade, um detalhe extra.
2. Peça: "Torne [elemento] interativo: esconda [a resposta/o detalhe] até a pessoa clicar em um botão para revelar."
3. Clique você mesmo no botão gerado, diretamente no canvas, e veja o efeito acontecer.

**Observe:**
- se o clique funcionou como esperado;
- o que visualmente indicava que aquele elemento era clicável antes mesmo de você clicar;
- se essa interatividade melhora ou só decora a experiência.

**Resultado esperado:** um elemento da página que esconde e revela conteúdo ao ser clicado, testado com sucesso por você mesmo.

### 🔧 Troubleshooting

**Problema:** cliquei no elemento e nada aconteceu.
**Possível causa:** o teste pode estar sendo feito em um modo de edição em vez de um modo de visualização/apresentação da página.
**Como resolver:** procure uma opção de "apresentar" ou "visualizar" a página, separada do modo de edição, e teste o clique nesse modo. Se ainda assim não funcionar, descreva o comportamento esperado novamente ao Claude, pedindo confirmação de que o elemento foi criado como interativo.

---

## Aula 8.2 — Estados e Feedback

### Objetivos da Aula

- Compreender o conceito de "estado" de um componente (normal, selecionado, correto, incorreto).
- Aplicar feedback visual de certo/errado a uma pergunta simples.
- Avaliar se a interatividade criada está clara para quem vai usá-la.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- explicar o que é um "estado" de um componente, com um exemplo próprio;
- pedir ao Claude para adicionar feedback visual de certo/errado a uma pergunta;
- verificar se o feedback visual é claro o suficiente sem texto explicativo adicional.

### Desenvolvimento da Aula

Um componente pode aparecer de formas diferentes dependendo do que está acontecendo com ele — isso se chama **estado**. Um botão comum tem um estado "normal" e pode ter um estado "selecionado". Uma resposta de quiz pode ter um estado "não respondido", um estado "correto" e um estado "incorreto" — cada um comunicado por uma cor ou ícone diferente.

**Por que isso importa em uma atividade escolar:** um quiz sem feedback visual de estado obriga o aluno a olhar em outro lugar para saber se acertou. Um quiz com feedback visual (verde para certo, vermelho para errado, por exemplo) comunica isso instantaneamente, sem depender de mais texto.

> 📸 **Sugestão de Prints:** três capturas lado a lado do mesmo botão de resposta de quiz em três estados diferentes: "não respondido" (neutro), "correto" (verde, com um ícone de check) e "incorreto" (vermelho, com um ícone de X). Por quê: estados de interface só fazem sentido quando comparados entre si — ver os três juntos é a única forma de entender o que muda em cada um.

### Conceito de Design da Aula: Feedback Visual (estados)

1. **O que é?** As diferentes aparências que um mesmo componente assume dependendo da situação (normal, selecionado, correto, incorreto).
2. **Por que importa?** Permite que a pessoa entenda o resultado de uma ação sem precisar de texto explicativo adicional.
3. **Como perceber na tela?** Interaja com o componente (clique, selecione uma resposta): a aparência muda de forma clara para indicar o que aconteceu?
4. **Como pedir ao Claude para melhorar?** "Quando a resposta estiver correta, mostre um destaque verde; quando estiver incorreta, mostre um destaque vermelho, sem precisar de texto adicional."

### Antes e Depois

**Antes**
Uma pergunta de múltipla escolha sem nenhuma indicação visual de certo ou errado.

**Peça ao Claude:**
> "Nesta pergunta, quando a pessoa escolher a resposta correta, mostre um destaque visual verde. Quando escolher uma resposta incorreta, mostre um destaque vermelho."

**Depois, observe:**
- se a diferença entre certo e errado é reconhecível sem ler nenhum texto extra;
- se as cores escolhidas mantêm bom contraste (revisando o conceito da Aula 3.1);
- se o restante da pergunta continua claro durante a interação.

### 🧪 Pílula Hands-on

**Objetivo:** adicionar feedback visual de certo/errado a uma pergunta interativa.

**Faça agora:**
1. Crie ou reaproveite uma pergunta simples de múltipla escolha.
2. Peça: "Quando a resposta estiver correta, mostre um destaque verde; quando estiver incorreta, mostre um destaque vermelho."
3. Teste clicando em uma resposta certa e depois em uma errada.

**Observe:**
- se os dois estados (certo/errado) são claramente diferentes um do outro;
- se dá para entender o resultado sem ler nenhuma palavra;
- se o feedback aparece de forma imediata ao clique.

**Resultado esperado:** uma pergunta interativa com dois estados visuais distintos e claros — um para resposta certa, outro para resposta errada.

---
---

# Parte 9 — Projetos Educacionais

Esta parte integra tudo que foi aprendido em projetos completos. Cada projeto combina conceitos de partes anteriores — use-os como referência sempre que precisar relembrar um conceito específico.

> **Atenção:** ao trabalhar nestes projetos, use sempre conteúdo fictício ou anonimizado. Não insira nomes reais, notas individuais ou fotos de alunos.

## Aula 9.1 — Projeto 1: Página de Apresentação de Disciplina

### Objetivos da Aula

- Aplicar hierarquia, espaçamento, cor, tipografia e componentes em um projeto único e completo.
- Praticar o ciclo de refinamento de forma autônoma, do início ao fim.
- Produzir um material pronto para uso real em sala.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- planejar e descrever um projeto completo antes de gerar;
- aplicar pelo menos três conceitos de design diferentes ao mesmo projeto;
- avaliar e refinar o resultado até considerá-lo pronto para uso.

### Desenvolvimento da Aula

Este projeto reúne o ciclo inteiro do curso em um único material real: uma página de apresentação de disciplina, pensada para ser usada nas primeiras semanas de aula.

**Conceitos que este projeto revisita:** conteúdo e clima (Aula 1.2), hierarquia (Aula 2.1), cards (Aula 2.2), cor e tipografia (Partes 3), componentes (Parte 4) e o checklist crítico (Aula 5.1).

**Estrutura sugerida para o pedido inicial:** conte a disciplina, a série, os temas do período e o clima desejado — exatamente como praticado na Aula 1.2, mas agora com mais detalhe, já que você tem mais vocabulário de design disponível.

> 📸 **Sugestão de Prints:** a página final do projeto, com etiquetas numeradas apontando cada decisão de design aplicada (hierarquia no título, cards para os temas, cor de destaque no botão, espaçamento entre seções). Por quê: funciona como um "mapa de decisões", mostrando ao aluno que o resultado final é a soma de escolhas conscientes, não um acidente.

### Conceito de Design da Aula: Síntese (Hierarquia + Componentes)

1. **O que é?** A aplicação combinada de hierarquia e componentes para organizar um conteúdo real e completo.
2. **Por que importa?** Projetos reais raramente usam um conceito de design isolado — a qualidade vem da combinação.
3. **Como perceber na tela?** O título se destaca, o conteúdo está organizado em blocos reconhecíveis, e existe uma ação clara — os três ao mesmo tempo.
4. **Como pedir ao Claude para melhorar?** Use o checklist da Aula 5.1 para identificar o que falta, e peça ajustes específicos um de cada vez.

### Antes e Depois

**Antes**
Uma ideia de disciplina, série e temas do período — ainda sem página.

**Peça ao Claude:**
> "Crie uma página de apresentação da disciplina de [nome], para a turma de [série], destacando os temas do período: [liste 3 a 5 temas]. Clima: [escolha]."

**Depois, observe:**
- se os temas do período aparecem organizados de forma reconhecível (cards, lista, seções);
- se o clima pedido realmente aparece no resultado;
- o que, no checklist da Aula 5.1, ainda precisa de ajuste.

### 🧪 Pílula Hands-on

**Objetivo:** criar e refinar uma página de apresentação de disciplina pronta para uso.

**Faça agora:**
1. Descreva o projeto usando a estrutura do quadro "Antes e Depois".
2. Aplique o checklist da Aula 5.1 ao resultado.
3. Escolha ao menos dois pontos de ajuste e peça as correções.

**Observe:**
- quantas rodadas de ajuste foram necessárias;
- quais conceitos de design você aplicou conscientemente;
- se o resultado final está pronto para ser usado com uma turma real.

**Resultado esperado:** uma página de apresentação de disciplina completa, revisada pelo checklist crítico e refinada em pelo menos duas rodadas.

---

## Aula 9.2 — Projeto 2: Quiz Educacional Interativo

### Objetivos da Aula

- Combinar componentes, interatividade e feedback visual em um quiz funcional.
- Aplicar estados de certo/errado a múltiplas perguntas.
- Avaliar a clareza da experiência do ponto de vista de quem responde.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- planejar um quiz com pelo menos três perguntas;
- pedir ao Claude a criação de perguntas com feedback visual de certo/errado;
- testar o quiz como se fosse um aluno respondendo.

### Desenvolvimento da Aula

Este projeto retoma diretamente a Parte 8: interatividade (Aula 8.1) e estados de feedback (Aula 8.2), agora aplicados a um material com múltiplas perguntas — um quiz de revisão simples.

**Planeje antes de pedir.** Separe de três a cinco perguntas de múltipla escolha sobre um conteúdo já ensinado, com as alternativas e a resposta correta de cada uma.

**O pedido reúne tudo:** conteúdo (as perguntas), interatividade (Aula 8.1) e feedback visual (Aula 8.2), em um único pedido bem estruturado.

> 📸 **Sugestão de Prints:** sequência de 3 capturas mostrando o mesmo quiz em três momentos: pergunta ainda não respondida, o clique acontecendo, e o feedback visual de certo/errado aparecendo. Se possível, um GIF mostrando a sequência completa de interação. Por quê: um quiz só se comunica de verdade em movimento — a sequência de imagens (ou o GIF) é o único jeito de mostrar a experiência completa de responder.

### Conceito de Design da Aula: Síntese (Interatividade + Feedback Visual)

1. **O que é?** A combinação de elementos clicáveis com respostas visuais imediatas, aplicada a um conjunto de perguntas.
2. **Por que importa?** Um quiz sem feedback claro perde a função pedagógica de revisão imediata.
3. **Como perceber na tela?** Responda ao quiz você mesmo: o feedback de cada pergunta é imediato e claro?
4. **Como pedir ao Claude para melhorar?** "Adicione feedback visual de certo/errado a todas as perguntas, de forma consistente" (revisando o conceito de consistência da Aula 3.3).

### Antes e Depois

**Antes**
Uma lista de perguntas de múltipla escolha, ainda em texto simples, sem interatividade.

**Peça ao Claude:**
> "Transforme estas perguntas em um quiz interativo. Cada pergunta deve ter alternativas clicáveis, com destaque verde para a resposta correta e vermelho para a incorreta: [cole suas perguntas e respostas]."

**Depois, observe:**
- se todas as perguntas têm o mesmo padrão de feedback (consistência);
- se o quiz é fácil de responder sem instrução adicional;
- se a experiência de responder parece clara e imediata.

### 🧪 Pílula Hands-on

**Objetivo:** criar e testar um quiz interativo completo.

**Faça agora:**
1. Escreva de três a cinco perguntas de múltipla escolha com respostas certas definidas.
2. Peça ao Claude o quiz interativo com feedback de certo/errado, usando o modelo do quadro "Antes e Depois".
3. Responda ao quiz você mesmo, como se fosse um aluno.

**Observe:**
- se todas as perguntas respondem de forma consistente ao clique;
- se o feedback visual é claro sem precisar de texto extra;
- se alguma pergunta ficou confusa ou diferente das demais.

**Resultado esperado:** um quiz funcional com pelo menos três perguntas, feedback visual consistente, testado por você mesmo do início ao fim.

### 🔧 Troubleshooting

**Problema:** só a primeira pergunta do quiz tem o feedback visual funcionando corretamente.
**Possível causa:** o padrão pedido pode não ter sido aplicado a todas as perguntas de forma automática.
**Como resolver:** peça explicitamente: "aplique o mesmo padrão de feedback visual da primeira pergunta a todas as outras" — reforçando consistência (Aula 3.3) como correção.

---

## Aula 9.3 — Projeto 3: Página de Revisão para Prova

### Objetivos da Aula

- Organizar uma grande quantidade de conteúdo sem gerar excesso de informação.
- Aplicar hierarquia e agrupamento a um material denso por natureza.
- Praticar adaptação para diferentes públicos em um mesmo material.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- organizar um conteúdo naturalmente extenso em blocos hierarquizados;
- identificar e reduzir excesso de informação em uma página densa;
- adaptar a mesma página de revisão para dois públicos diferentes.

### Desenvolvimento da Aula

Páginas de revisão tendem a acumular conteúdo — é da natureza da tarefa. O desafio de design aqui não é criatividade, é **domar densidade visual** (Aula 1.2) sem cortar conteúdo importante.

**A estratégia:** hierarquize por prioridade de estudo, não por ordem cronológica do conteúdo. O que cai mais na prova, ou o que a turma tem mais dificuldade, deveria se destacar mais — não necessariamente o que veio primeiro no calendário.

**Este projeto também é uma boa oportunidade de praticar adaptação de público** (retomando o espírito da responsividade da Parte 6, agora aplicado à linguagem e não só à tela): a mesma revisão pode precisar de uma versão mais densa para o próprio professor organizar o pensamento, e uma versão mais enxuta para entregar à turma.

> 📸 **Sugestão de Prints:** duas versões da mesma página de revisão lado a lado — a versão inicial "densa" (muito texto, hierarquia fraca) e a versão final "hierarquizada por prioridade" (tópicos mais importantes em destaque visual maior). Por quê: densidade excessiva é um problema que só se percebe claramente quando comparado a uma versão resolvida ao lado.

### Conceito de Design da Aula: Síntese (Densidade + Hierarquia)

1. **O que é?** A aplicação de hierarquia como ferramenta de priorização de conteúdo, não apenas de estilo.
2. **Por que importa?** Em materiais de revisão, a pergunta certa não é "o que cabe", é "o que precisa se destacar".
3. **Como perceber na tela?** Os tópicos mais importantes para a prova são, visualmente, os que mais chamam atenção?
4. **Como pedir ao Claude para melhorar?** "Reorganize esta página priorizando visualmente os tópicos [liste os mais importantes], deixando os demais mais discretos, sem removê-los."

### Antes e Depois

**Antes**
Uma lista longa de tópicos de revisão, todos com o mesmo peso visual.

**Peça ao Claude:**
> "Esta é uma página de revisão para prova. Reorganize priorizando visualmente os tópicos [liste os 2-3 mais importantes], mantendo os demais visíveis, porém mais discretos."

**Depois, observe:**
- se os tópicos prioritários realmente se destacam mais que os demais;
- se nenhum conteúdo foi perdido no processo, apenas reorganizado;
- se a página, mesmo densa por natureza, ficou mais fácil de navegar.

### 🧪 Pílula Hands-on

**Objetivo:** organizar um conteúdo extenso por prioridade visual, sem perder informação.

**Faça agora:**
1. Liste os tópicos de revisão de uma prova real (ou fictícia) e marque os 2-3 mais importantes.
2. Peça ao Claude a página de revisão, priorizando visualmente esses tópicos.
3. Compare com uma versão sem priorização (se quiser, peça as duas para comparar).

**Observe:**
- se os tópicos prioritários se destacam claramente dos demais;
- se a página continua completa, sem cortes de conteúdo;
- se ficaria fácil para um aluno saber por onde começar a estudar.

**Resultado esperado:** uma página de revisão completa, com prioridades visuais claras, sem perda de conteúdo.

---

## Aula 9.4 — Projeto 4: Painel de Acompanhamento de Projeto Escolar

### Objetivos da Aula

- Organizar informações de acompanhamento (etapas, prazos, status) em um painel visual.
- Aplicar componentes e estados a um contexto de gestão, não só de conteúdo.
- Produzir um material que se atualiza ao longo do tempo.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- estruturar um painel com etapas, prazos e status visual;
- usar cor e estado para comunicar progresso (não iniciado, em andamento, concluído);
- planejar como esse painel será atualizado ao longo de um projeto real.

### Desenvolvimento da Aula

Diferente dos projetos anteriores, um painel de acompanhamento não é estático — ele existe para ser revisitado e atualizado conforme um projeto avança (uma feira de ciências, um projeto interdisciplinar, um cronograma de entregas).

**A estrutura típica de um painel:** etapas do projeto, prazo de cada uma, e um status visual (não iniciado, em andamento, concluído) — retomando diretamente o conceito de estados da Aula 8.2, agora aplicado a progresso em vez de certo/errado.

**Componentes reutilizáveis fazem toda a diferença aqui** (Parte 4): cada etapa deveria usar exatamente o mesmo formato de card, mudando apenas a cor de status — assim, a turma aprende a "ler" o painel de relance, sem precisar reler o texto toda vez.

> 📸 **Sugestão de Prints:** o painel completo, com três cards de etapas em cores de status diferentes (cinza para "não iniciado", amarelo para "em andamento", verde para "concluído"), com uma legenda de cores destacada ao lado. Por quê: painéis de status dependem inteiramente de leitura rápida por cor — a imagem precisa comprovar que os três estados são visualmente distinguíveis à primeira vista.

### Conceito de Design da Aula: Síntese (Componentes + Estados)

1. **O que é?** O uso de um mesmo componente reutilizável, variando apenas seu estado, para comunicar progresso.
2. **Por que importa?** Permite que qualquer pessoa entenda o andamento do projeto sem precisar ler cada etapa em detalhe.
3. **Como perceber na tela?** Os diferentes status (não iniciado, em andamento, concluído) são reconhecíveis só pela cor, à distância?
4. **Como pedir ao Claude para melhorar?** "Use o mesmo formato de card para todas as etapas, mudando apenas a cor conforme o status: cinza para não iniciado, amarelo para em andamento, verde para concluído."

### Antes e Depois

**Antes**
Uma lista de etapas de um projeto escolar, em texto simples, sem indicação visual de status.

**Peça ao Claude:**
> "Crie um painel com estas etapas do projeto: [liste as etapas e prazos]. Use um card para cada uma, com cor cinza para não iniciado, amarelo para em andamento e verde para concluído."

**Depois, observe:**
- se os três status são visualmente distintos entre si;
- se todos os cards seguem exatamente o mesmo formato (revisando consistência, Aula 3.3);
- se seria fácil atualizar esse painel na semana seguinte, só mudando a cor de status de uma etapa.

### 🧪 Pílula Hands-on

**Objetivo:** criar um painel de acompanhamento reutilizável.

**Faça agora:**
1. Liste de três a cinco etapas de um projeto escolar (real ou fictício), com prazos.
2. Peça ao Claude o painel com cards de status coloridos, conforme o modelo do quadro "Antes e Depois".
3. Escolha uma etapa e peça para mudar seu status (por exemplo, de "não iniciado" para "em andamento").

**Observe:**
- se a mudança de status foi aplicada só naquela etapa, sem afetar as demais;
- se os cards mantiveram o mesmo formato antes e depois da atualização;
- se o painel comunicaria o progresso do projeto para alguém que não participou de nenhuma etapa.

**Resultado esperado:** um painel de acompanhamento com etapas, prazos e status visual, atualizado com sucesso em pelo menos uma etapa.

---
---

# Parte 10 — Refinamento Avançado

## Aula 10.1 — O Claude Como Parceiro de Crítica

### Objetivos da Aula

- Usar o Claude para obter uma avaliação especializada do próprio design.
- Comparar a avaliação do Claude com a avaliação própria feita na Parte 5.
- Decidir, de forma autônoma, quais sugestões aceitar e quais recusar.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- pedir ao Claude uma avaliação crítica especializada de um design;
- comparar essa avaliação com o próprio julgamento;
- justificar a decisão de aceitar ou recusar uma sugestão da IA.

### Desenvolvimento da Aula

Até aqui, você foi quem avaliou cada resultado usando o checklist da Aula 5.1. Nesta aula, você aprende a pedir uma segunda opinião — vinda do próprio Claude — sem abrir mão da decisão final.

**Perguntas que convidam a uma crítica mais profunda:**

> "Avalie esta interface como especialista em UX e indique os três principais problemas."

> "Identifique elementos que prejudicam a hierarquia visual desta página."

> "Analise esta página pensando em alunos de 12 anos."

> "Verifique se esta página possui problemas de acessibilidade."

**A decisão final é sempre sua.** O Claude pode apontar problemas reais e também pode sugerir mudanças que não fazem sentido para o seu contexto específico — porque ele não conhece sua turma, sua escola ou sua intenção pedagógica da forma que você conhece. Trate cada sugestão como um ponto de vista a considerar, não como uma ordem a cumprir.

> 📸 **Sugestão de Prints:** captura de uma resposta real do Claude a um pedido de crítica especializada, com três problemas numerados listados por ele. Ao lado, uma anotação manual do professor marcando cada sugestão com "aceito" ou "não se aplica", com uma frase curta justificando cada decisão. Por quê: essa imagem demonstra concretamente que a palavra final pertence a quem ensina, não à ferramenta — um princípio central desta aula que texto sozinho pode não deixar claro.

### Conceito de Design da Aula: Pensamento Crítico de Design (síntese)

1. **O que é?** A capacidade de avaliar uma sugestão de design — vinda de qualquer fonte, incluindo uma IA — com critério próprio.
2. **Por que importa?** Sem isso, o aluno troca a dependência de "não saber o que pedir" pela dependência de "aceitar tudo que a IA sugere" — nenhuma das duas é autonomia real.
3. **Como perceber na tela?** Compare a lista de problemas que o Claude apontou com a lista que você mesmo produziu na Aula 5.1: elas coincidem? Onde divergem?
4. **Como pedir ao Claude para melhorar?** Peça a crítica, avalie cada ponto, e só then decida quais pedidos de ajuste enviar — nem todo ponto levantado precisa virar uma mudança.

### Antes e Depois

**Antes**
Uma página já refinada em aulas anteriores, que você considera praticamente pronta.

**Peça ao Claude:**
> "Avalie esta interface como especialista em UX e indique os três principais problemas, pensando em alunos de [idade/série]."

**Depois, observe:**
- se os três problemas apontados fazem sentido para o seu contexto real;
- se algum deles já havia sido identificado por você mesmo antes;
- quais você decide aceitar, e por quê — e quais decide não aplicar, e por quê.

### 🧪 Pílula Hands-on

**Objetivo:** obter e avaliar criticamente uma crítica especializada do Claude.

**Faça agora:**
1. Escolha uma página que você considera quase pronta.
2. Peça: "Avalie esta interface como especialista em UX e indique os três principais problemas."
3. Para cada problema apontado, escreva "aceito" ou "não se aplica", com uma frase justificando.

**Observe:**
- se você concordou com todos os pontos ou só com alguns;
- se algum ponto revelou algo que você realmente não tinha notado;
- como foi a experiência de discordar de uma sugestão da IA com base no seu próprio critério.

**Resultado esperado:** uma lista de três problemas apontados pelo Claude, cada um avaliado e decidido por você, com justificativa.

---
---

# Parte 11 — Trabalhando com Referências Visuais

## Aula 11.1 — Mostrar em Vez de Descrever

### Objetivos da Aula

- Usar uma imagem de referência para comunicar intenção visual.
- Diferenciar "usar como inspiração" de "copiar um design".
- Anexar uma referência real e pedir uma adaptação a partir dela.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- anexar uma imagem de referência a um pedido;
- pedir uma adaptação inspirada na referência, sem copiar diretamente;
- explicar quando vale mais mostrar uma imagem do que descrever em palavras.

### Desenvolvimento da Aula

Descrever um estilo visual em palavras é difícil mesmo para quem já tem vocabulário de design — "quero algo moderno, mas não frio" significa coisas diferentes para pessoas diferentes. Uma imagem resolve isso instantaneamente: uma foto de um mural que você gosta, um print de um site, ou até uma foto de um material impresso já usado em sala comunicam uma intenção visual que nenhuma frase substitui sozinha.

**Isso não é copiar — é comunicar intenção.** Anexar uma referência e pedir "algo no mesmo espírito visual disso, mas para [seu novo conteúdo]" usa a imagem como ponto de partida de estilo, não como modelo a ser reproduzido igual.

**Onde encontrar boas referências no seu cotidiano:** um mural físico da escola que você gosta, a identidade visual de um material que a coordenação já aprovou, ou até uma página de outra disciplina que funcionou bem com a turma.

> 📸 **Sugestão de Prints:** três imagens lado a lado: a foto de referência original (por exemplo, um mural físico), o resultado gerado pelo Claude a partir dela, e uma legenda explicando qual elemento da referência foi absorvido (paleta de cores, formato dos títulos) e qual foi adaptado ao novo contexto. Por quê: o conceito de "inspiração sem cópia" é abstrato até ser visto — mostrar exatamente o que foi herdado e o que foi mudado deixa esse limite claro.

### Conceito de Design da Aula: Comunicação Visual de Intenção

1. **O que é?** O uso de uma imagem, em vez de apenas texto, para transmitir um estilo, clima ou padrão visual desejado.
2. **Por que importa?** Reduz a dependência de vocabulário técnico de design — mostrar substitui descrever.
3. **Como perceber na tela?** O resultado gerado carrega o "espírito" da referência (cores, tom, formato), mesmo sendo sobre um conteúdo diferente?
4. **Como pedir ao Claude para melhorar?** "Use esta imagem como referência de estilo — não copie exatamente, mas aplique a mesma sensação visual ao conteúdo novo."

### Antes e Depois

**Antes**
Um projeto novo, sem nenhuma direção visual definida, e uma foto ou print de algo que você já gosta visualmente.

**Peça ao Claude** (anexando a imagem de referência):
> "Use esta imagem como referência de estilo visual. Crie [descreva seu novo conteúdo] no mesmo espírito visual dela, sem copiar exatamente."

**Depois, observe:**
- quais elementos da referência (cor, formato, tom) aparecem no resultado;
- o que foi adaptado para servir ao novo conteúdo;
- se o resultado parece genuinamente inspirado, ou uma cópia exata.

### 🧪 Pílula Hands-on

**Objetivo:** usar uma referência visual real para guiar um novo projeto.

**Faça agora:**
1. Tire uma foto ou separe um print de algo visualmente que você já gosta (um mural, um material aprovado pela escola, uma página que funcionou bem).
2. Anexe essa imagem ao Claude Design e peça: "Use esta imagem como referência de estilo. Crie [novo conteúdo] no mesmo espírito visual dela."
3. Compare a referência original com o resultado gerado.

**Observe:**
- o que foi absorvido da referência;
- o que foi adaptado para o novo conteúdo;
- se você conseguiria explicar, em uma frase, o que a referência "emprestou" ao novo material.

**Resultado esperado:** um novo material visualmente inspirado em uma referência real, sem ser uma cópia dela.

### 🔧 Troubleshooting

**Problema:** o resultado ignorou completamente a imagem de referência.
**Possível causa:** o pedido pode não ter deixado claro que a imagem deveria influenciar o estilo, e não apenas ter sido anexada sem instrução.
**Como resolver:** seja explícito: "use as cores e o formato de título desta imagem como referência direta" — nomeie especificamente o que deve ser absorvido da referência.

---
---

# Parte 12 — Do Protótipo ao Resultado Final

## Aula 12.1 — Protótipo, Interface e Produto: Sabendo a Diferença

### Objetivos da Aula

- Diferenciar conceito, protótipo, interface, código, preview e produto final.
- Reconhecer os limites do que foi criado no curso até aqui.
- Saber quando um material está pronto para uso direto e quando precisa de apoio técnico adicional.

### Habilidades Esperadas

Ao final desta aula, você será capaz de:

- explicar a diferença entre um protótipo funcional e um sistema pronto para produção;
- identificar se um material criado no curso pode ser usado diretamente ou precisa de revisão adicional;
- saber para quem pedir ajuda quando um projeto crescer além do que o curso cobre.

### Desenvolvimento da Aula

Ao longo do curso, você criou páginas, quizzes e painéis totalmente funcionais — cliques reagem, respostas aparecem, o painel se atualiza. É natural achar que isso significa "pronto para qualquer uso", mas vale entender as diferenças:

- **Conceito** — a ideia, ainda em palavras.
- **Protótipo** — uma versão navegável que demonstra a ideia, como tudo que você fez neste curso.
- **Interface** — a camada visual com que a pessoa interage.
- **Código** — o que existe por trás da interface, permitindo que o navegador a exiba e a torne interativa.
- **Preview (visualização)** — o modo em que você testa o resultado antes de compartilhar.
- **Produto final** — um sistema testado, validado, hospedado de forma estável e mantido ao longo do tempo.

**O que você fez no curso vive, principalmente, entre "protótipo" e "interface".** Isso é mais do que suficiente para a grande maioria dos usos educacionais deste roteiro: apresentações, materiais de revisão, painéis de acompanhamento, quizzes de uma turma. Não é, no entanto, o mesmo que um sistema de produção — algo que vai receber dados reais de muitas pessoas, precisa de manutenção contínua, ou lidar com informações sensíveis em escala.

**Alertas importantes antes de usar um material em contextos maiores:**

- **Validação:** teste o material com uma pessoa que não participou da criação antes de usar com a turma inteira.
- **Testes:** confira o material em mais de um navegador ou dispositivo, se possível.
- **Segurança:** nunca insira dados pessoais reais de alunos ou famílias nos materiais criados.
- **Dados:** se o material for coletar respostas de verdade (por exemplo, um formulário), verifique com a coordenação da escola onde essas informações serão armazenadas.
- **Manutenção:** um painel ou página publicada não se atualiza sozinha — alguém precisa voltar e atualizá-la.
- **Publicação:** se o material for publicado em um site da escola ou compartilhado amplamente, converse com quem cuida da infraestrutura de TI antes.

> 📸 **Sugestão de Prints:** esquema visual simples, em linha do tempo horizontal, mostrando as seis etapas (conceito → protótipo → interface → código → preview → produto final), com um marcador destacado indicando "você está aqui" posicionado entre protótipo e interface. Por quê: um esquema visual comunica em segundos uma progressão que, em texto, exige memorizar uma lista de seis termos.

### Conceito de Design da Aula: Consistência (revisão final)

1. **O que é?** A garantia de que um material continua funcionando e coerente mesmo depois de sair do ambiente onde foi criado.
2. **Por que importa?** Um protótipo bonito na tela de criação pode se comportar de forma diferente quando compartilhado, impresso ou aberto em outro dispositivo.
3. **Como perceber na tela?** Teste o material exportado ou compartilhado exatamente como uma outra pessoa vai vê-lo, não apenas dentro do ambiente de edição.
4. **Como pedir ao Claude para melhorar?** "Revise esta página pensando em como ela vai aparecer para alguém que a abre pela primeira vez, fora do ambiente de edição."

### Antes e Depois

**Antes**
Um material do curso, considerado "pronto" dentro do ambiente de edição do Claude Design.

**Peça ao Claude:**
> "Revise esta página pensando em alguém que vai abri-la pela primeira vez, sem contexto sobre como ela foi criada. Aponte qualquer coisa que dependa de explicação extra para funcionar."

**Depois, observe:**
- se algo no material só faz sentido para quem participou da criação;
- se o material se sustenta sozinho, sem sua presença para explicar;
- o que precisaria ser testado antes de um uso mais amplo (outra turma, outra escola).

### 🧪 Pílula Hands-on

**Objetivo:** avaliar a maturidade real de um material criado no curso.

**Faça agora:**
1. Escolha o material que você mais gostou de criar ao longo do curso.
2. Responda: ele está pronto para (a) uso pessoal, (b) uso com uma turma, ou (c) publicação mais ampla (site da escola, compartilhamento com outras escolas)?
3. Para o nível que você escolheu, marque na lista de alertas ("Validação", "Testes", "Segurança", "Dados", "Manutenção", "Publicação") quais ainda precisam de atenção.

**Observe:**
- se o nível de prontidão do material corresponde ao uso que você pretende dar a ele;
- quais alertas da lista já estão resolvidos e quais ainda não;
- se algum desses pontos exige apoio de outra pessoa (coordenação, TI) antes de seguir.

**Resultado esperado:** uma avaliação honesta e específica de quão pronto está o seu material, com os próximos passos identificados antes de um uso mais amplo.

> **Nota:** o resultado gerado pelo Claude é sempre um ponto de partida. Você continua responsável por avaliar se o conteúdo, a experiência e o design atendem ao público pretendido — do primeiro rascunho da Aula 1.2 até o material mais sofisticado desta última aula.
