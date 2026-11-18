# Claude Chat Para Leigos — Curso Hands-on

*Ao final deste curso, o Claude vai lembrar quem você é, achar suas conversas antigas sozinho e parar de tratar todo dia como se fosse a primeira vez que vocês se falam.*

---

## Antes de Arregaçar as Mangas

Esse curso não é para só ler. É para você abrir o Claude, mexer nas configurações de verdade e sair com um "Claude" que já sabe quem você é antes mesmo de terminar de digitar a primeira pergunta do dia. Nada de decorar termo técnico — você vai aprender fazendo, oficina por oficina, cada uma resolvendo um pedaço bem real daquele problema de "toda vez eu tenho que explicar tudo de novo".

**O que você precisa ter aberto agora:**
- Claude (claude.ai no navegador, ou o aplicativo Desktop)
- Uma conta ativa no Claude
- Internet
- Se puder, um histórico com pelo menos algumas conversas antigas — deixa os exercícios de busca bem mais reais (mas se não tiver, sem problema, você constrói histórico ao longo do curso)

> 🔑 **Regra de ouro deste curso:** você não vai quebrar nada. Toda configuração que vamos mexer pode ser reescrita, desativada ou apagada depois. Errar uma instrução só significa reescrevê-la — não existe "estragar o Claude para sempre".

---

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1 | Parar de se reapresentar a cada conversa nova | 15 min |
| 2 | Achar uma conversa antiga sem rolar a tela por 20 minutos | 20 min |
| 3 | Fazer o Claude "aprender" coisas sobre você sozinho | 20 min |
| 4 | Separar projetos diferentes para não misturar contexto | 20 min |
| **Projeto Final** | Montar seu sistema pessoal de continuidade, tudo junto | 15 min |

As oficinas foram pensadas para serem feitas em sequência — cada uma resolve um pedaço do mesmo problema geral: parar de recomeçar do zero. Bora?

---

# Oficina 1 — Pare de se Reapresentar Toda Vez (Custom Instructions)

### 🎯 O Problema

Você já perdeu os primeiros minutos de uma conversa nova explicando de novo quem você é, o que você faz e como gosta que as respostas venham? Pois é — isso acontece porque, por padrão, todo chat novo é uma folha em branco. Nesta oficina você resolve isso de vez, configurando um "perfil" que o Claude carrega automaticamente em toda conversa.

### 🧰 O que você vai usar

- Claude (claude.ai ou Desktop)
- Sua conta ativa

### 👐 Mão na massa

1. Clique no seu ícone de perfil, no canto superior direito da tela.
2. Vá em **Settings**.
3. Procure por **Custom Instructions** (pode aparecer também como **Preferences**).
4. No primeiro campo — "O que você gostaria que o Claude soubesse sobre você?" — escreva algo assim:
   ```
   Sou [sua profissão/função]. Trabalho com [seu público-alvo].
   Meus objetivos principais são [1 a 3 objetivos]. Minhas
   restrições de trabalho são [tempo, orçamento, regras da
   instituição — o que for relevante].
   ```
5. No segundo campo — "Como você gostaria que o Claude respondesse?" — escreva algo assim:
   ```
   Use um tom [formal / casual / técnico — escolha o seu]. Prefiro
   respostas em [listas / parágrafos / tabelas]. Quando houver mais
   de um jeito de responder, priorize [o que for mais importante
   para você: rapidez, profundidade, exemplos práticos...].
   ```
6. Salve.
7. Abra uma conversa nova e faça uma pergunta qualquer da sua área — sem explicar quem você é.

### ✅ Deu certo?

Se a resposta já veio no tom certo, ou já considerou o seu público, sem você precisar dizer nada disso na pergunta, deu certo.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não encontro "Custom Instructions" | Procure por "Preferences" — o nome muda um pouco entre versões |
| A resposta veio genérica, do jeito de sempre | Confirme se você clicou em salvar antes de abrir a conversa nova |
| Não sei o que escrever sobre mim | Comece simples: profissão + público + 1 objetivo. Você refina depois |

### 🚀 Quer ir além?

Pergunte ao próprio Claude: "com base no que você sabe sobre mim agora, o que ficou pouco claro nas minhas instruções?" — às vezes ele aponta uma lacuna que você nem tinha percebido.

> 💡 Dica: instruções específicas funcionam muito mais do que instruções genéricas. "Sou professora do 6º ano em escola pública, com turmas grandes e pouco recurso" ensina muito mais do que "sou professora".

---

# Oficina 2 — Nunca Mais Perca uma Conversa (Chat Search)

### 🎯 O Problema

Você sabe que discutiu aquele assunto com o Claude semanas atrás. Só não lembra em qual das dezenas de conversas. Rolar a lista inteira toma tempo — e o Chat Search resolve isso, com um detalhe importante: ele não busca palavra por palavra, ele busca por ideia.

### 🧰 O que você vai usar

- Sua conta no Claude, com algum histórico de conversas (mesmo que pequeno)

### 👐 Mão na massa

1. Vá em **Settings > Features** (ou **Experimental Features**).
2. Procure **Search chats** (ou **Chat search**) e ative, se ainda não estiver ativo.
3. Volte para a tela principal e clique no ícone de busca (lupa), geralmente no topo da barra lateral.
4. Digite uma busca ampla sobre um tema que você já discutiu — por exemplo, "planejamento de aula" ou "relatório mensal".
5. Veja quantos resultados aparecem. Se forem muitos, refine: acrescente um detalhe mais específico (um tipo de documento, uma decisão que vocês tomaram, uma época aproximada).
6. Repita o refinamento até sobrar só uma ou duas conversas que parecem ser exatamente o que você procurava.
7. Abra a conversa. Decida: você vai continuar escrevendo ali mesmo, ou vai copiar o essencial e abrir uma conversa nova?

### ✅ Deu certo?

Se você saiu de uma busca ampla, com muitos resultados, para uma busca específica, com 1 ou 2 resultados relevantes, em até três tentativas, deu certo.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não acho a opção de busca | Confirme que ativou em Settings > Features; em algumas contas o ícone só aparece depois disso |
| A busca não retorna nada | Tente um sinônimo, ou acrescente uma referência de tempo ("mês passado", "no início do ano") |
| Muitos resultados parecidos | Adicione um detalhe concreto: um nome de produto, uma decisão, um formato de documento |

### 🚀 Quer ir além?

Teste a diferença entre buscar por uma palavra exata (ex.: "Excel") e por uma descrição (ex.: "planilha para controlar gastos") — repare como a segunda costuma trazer resultados que a primeira não traria.

> 🤓 Curiosidade técnica: essa busca é "semântica" — ela entende ideias, não só palavras. Por isso uma busca por "alimentação saudável" pode encontrar uma conversa sobre "hábitos alimentares de adolescentes", mesmo sem nenhuma palavra em comum entre as duas.

---

# Oficina 3 — Faça o Claude Aprender Sozinho (Memory)

### 🎯 O Problema

Custom Instructions você escreve uma vez, na mão. Mas e as coisas que vão surgindo aos poucos, ao longo do tempo? É para isso que serve a Memory: o Claude vai "prestando atenção" no que você conta, e passa a lembrar sozinho — com uma pegadinha de tempo que você vai descobrir nesta oficina.

### 🧰 O que você vai usar

- Sua conta no Claude

### 👐 Mão na massa

1. Vá em **Settings > Privacy** (ou **Data & Privacy**).
2. Procure **Memory** (ou "Claude aprende sobre você") e ative, se ainda não estiver ativo.
3. Em uma conversa, escreva um "lembre que eu..." com 2 ou 3 informações genéricas e seguras sobre seu trabalho. Por exemplo:
   ```
   Lembre que eu sou coordenador pedagógico, atendo professores do
   ensino fundamental e prefiro sugestões práticas em vez de teoria
   longa.
   ```
4. Em seguida (na mesma conversa ou em uma nova), pergunte: "o que você sabe sobre mim até agora?"
5. Leia a resposta. Ela já reflete o que você disse no passo 3?
6. Anote: se alguma informação ainda não apareceu, tudo bem — a atualização completa da Memory pode levar de 24 a 48 horas.

### ✅ Deu certo?

Se a resposta do passo 4 já menciona pelo menos uma das informações que você forneceu, deu certo — mesmo que o restante ainda leve um tempinho para "assentar".

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não encontro "Memory" nas configurações | Procure por "Privacy" ou "Data & Privacy" — às vezes fica dentro de um submenu |
| A resposta veio vazia ou genérica | Normal logo após ativar; espere um pouco e repita o teste em uma conversa nova, no dia seguinte |
| Fiquei em dúvida se algo é "seguro" para contar | Regra prática: se envolve outra pessoa identificável (nome, diagnóstico, dado pessoal dela), generalize antes de contar ao Claude |

### 🚀 Quer ir além?

Peça uma "auditoria de memória" completa: "faça uma auditoria da minha memória — resuma o que você sabe sobre meu cargo, público, objetivos e preferências, e diga se algo parece desatualizado."

> ⚠️ Cuidado: nunca conte à Memory nomes completos de alunos ou clientes, diagnósticos de saúde, dados financeiros ou senhas. Prefira sempre descrições genéricas ("uma turma com alunos de ritmos diferentes") a informações que identifiquem alguém.

---

# Oficina 4 — Um Espaço Só Seu Para Cada Projeto (Projects)

### 🎯 O Problema

Se você usa o Claude para coisas bem diferentes — um projeto educacional de manhã, uma consultoria à tarde — misturar tudo no mesmo lugar é receita para o Claude confundir tom, público ou decisões já tomadas. Um Project resolve isso: é um espaço isolado, com histórico e instruções próprios.

### 🧰 O que você vai usar

- Sua conta no Claude, com acesso à função Projects

### 👐 Mão na massa

1. Na barra lateral, clique no ícone **[+]** e escolha **New Project** (em vez de "New Chat").
2. No campo **Nome**, escreva um título que descreva o resultado, não o processo — por exemplo, "Currículo de Ciências 2026" em vez de "Testando o Claude".
3. No campo **Descrição**, escreva uma frase dizendo o que esse Project vai produzir e para quem.
4. Abra as **Project Instructions** e escreva, especificamente para essa frente de trabalho:
   ```
   Neste projeto, meu papel é [seu papel aqui]. O público é
   [quem vai usar o resultado]. Os objetivos deste projeto são
   [2 a 3 objetivos]. Aqui, diferente das minhas instruções gerais,
   evite [algo que só vale para este contexto].
   ```
5. Salve e comece uma conversa dentro do Project, com uma pergunta relacionada à finalidade dele.
6. Compare: essa resposta parece diferente do que você receberia numa conversa comum, fora do Project?

### ✅ Deu certo?

Se você consegue apontar pelo menos uma diferença clara entre a resposta de dentro do Project e o que o Claude responderia numa conversa comum, deu certo.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não vejo a opção "New Project" | Procure "Projects" no menu lateral; confirme se seu plano inclui essa função |
| A resposta veio igual a uma conversa comum | Confira se as Project Instructions foram salvas antes de perguntar |
| Não sei separar o que vai em Custom Instructions e o que vai em Project Instructions | Regra prática: o que vale para VOCÊ em qualquer contexto vai nas Custom Instructions; o que vale só PARA ESSE projeto vai nas Project Instructions |

### 🚀 Quer ir além?

Crie um segundo Project, para outra frente de trabalho bem diferente da primeira, e compare as duas Instructions lado a lado.

> 📌 Não esqueça: dê ao Project um nome que descreva o resultado final. Isso ajuda você a encontrá-lo depois — e ajuda o próprio Claude a entender o objetivo só de ler o nome.

---

# Projeto Final — Seu Sistema Pessoal de Continuidade

### 🎯 A missão

Juntar as quatro oficinas em um único fluxo: Custom Instructions prontas, pelo menos um fato salvo na Memory, um Project com instruções específicas, e uma busca no Chat Search retomando algo antigo. No final, você vai ter, de verdade, um "Claude" que se lembra de você.

### 👐 Mão na massa

1. Confirme que suas Custom Instructions (Oficina 1) estão salvas e atualizadas.
2. Confirme que você já disse à Memory (Oficina 3) pelo menos uma informação sobre você.
3. Abra o Project criado na Oficina 4 (ou crie um novo, se preferir usar outra frente de trabalho).
4. Use o Chat Search (Oficina 2) para localizar uma conversa antiga relacionada a essa frente de trabalho.
5. Dentro do Project, escreva uma mensagem de continuidade real, por exemplo:
   ```
   Encontrei nossa conversa anterior sobre [tema]. Quero continuar
   a partir dali, agora fazendo [nova tarefa]. Mantenha o tom e as
   decisões que já tínhamos combinado.
   ```
6. Leia a resposta com espírito crítico: ela realmente parece "lembrar" do que veio antes?

### 🏁 Como saber que terminou

- [ ] Custom Instructions preenchidas e salvas
- [ ] Pelo menos uma informação registrada explicitamente na Memory
- [ ] Um Project criado, com Project Instructions específicas
- [ ] Uma busca no Chat Search feita com sucesso, encontrando uma conversa relevante
- [ ] Uma resposta final que reúne contexto recuperado, perfil e instruções do Project

---

# A Parte dos Dez — Hábitos que Fazem Você Nunca Mais Recomeçar do Zero

1. Escreva suas Custom Instructions pensando em alguém que nunca te conheceu — quanto mais específico, melhor.
2. Revise suas Custom Instructions a cada 2 a 4 semanas; seu trabalho muda, elas também devem mudar.
3. Prefira buscas por ideia ("relatório de acompanhamento mensal") a buscas por palavra exata.
4. Refine a busca aos poucos: comece amplo, adicione um detalhe, repita.
5. Diga explicitamente ao Claude o que lembrar ("lembre que eu...") em vez de esperar que ele adivinhe.
6. Nunca conte à Memory nomes completos, diagnósticos ou dados financeiros de terceiros.
7. Faça uma auditoria de memória de vez em quando: pergunte "o que você sabe sobre mim?"
8. Crie um Project sempre que uma tarefa for durar mais de uma conversa ou gerar um documento reaproveitável.
9. Não misture frentes de trabalho diferentes no mesmo Project.
10. Revise sempre o que o Claude produz antes de usar — a responsabilidade pelo resultado final é sua, não da ferramenta.

---

## Conseguiu! E agora?

Você acabou de sair de "recomeçar do zero em toda conversa" para ter um sistema de verdade: um perfil permanente, uma memória que aprende sozinha, um jeito de achar qualquer conversa antiga e espaços isolados para cada projeto importante.

Daqui para frente, é prática: revise suas instruções de tempos em tempos, confie na busca em vez de rolar a tela, e crie um Project sempre que perceber que uma conversa vai se repetir. Cada vez fica mais rápido — porque, dessa vez, o Claude já sabe por onde vocês pararam.
