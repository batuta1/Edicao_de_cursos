# Claude Cowork Para Leigos — Curso Hands-on

*Ao final deste curso, você vai ter um Projeto de verdade no Claude — com Base de Conhecimento, Instruções Customizadas e um Artefato pronto, tudo criado com as próprias mãos.*

---

## Antes de Arregaçar as Mangas

Esse curso não é para só ler. É para você abrir o Claude, criar um Projeto de verdade e ver ele ganhar vida na tela. Nada de decorar termo técnico — você vai aprender fazendo, oficina por oficina, cada uma te deixando um passo mais perto de ter um parceiro de trabalho que realmente conhece o seu contexto.

**O que você precisa ter aberto agora:**
- Claude Desktop (aplicativo) ou o Claude no navegador
- Uma conta ativa no Claude, com acesso à função Projects
- Internet
- Se tiver à mão, um documento seu (currículo, exemplo de atividade, material de referência) — mas não é obrigatório para começar

> 🔑 **Regra de ouro deste curso:** errar faz parte. Se o Projeto sair torto na primeira tentativa, você não quebrou nada — é só ajustar a instrução e pedir de novo. Ninguém vira parceiro de ninguém na primeira reunião.

---

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1 | Decidir entre Chat e Projeto, e criar seu primeiro Projeto no Claude | 15 min |
| 2 | Montar uma Base de Conhecimento para o Claude "conhecer" o seu contexto | 20 min |
| 3 | Escrever Instruções Customizadas para o Claude manter o padrão sozinho | 20 min |
| 4 | Criar um Artefato e ajustá-lo até ficar do jeito que você quer | 20 min |
| **Projeto Final** | Juntar tudo num mini produto pedagógico pronto para usar | 15 min |

As oficinas foram pensadas para serem feitas em sequência — cada uma te entrega uma pequena vitória que vira ferramenta pronta para a próxima. Bora?

---

# Oficina 1 — Chat ou Projeto? Coloque Seu Parceiro de Trabalho em Pé

### 🎯 O Problema

Você já pediu para uma IA fazer alguma coisa, gostou do resultado, e no dia seguinte teve que explicar tudo de novo do zero? Isso acontece porque um Chat comum não guarda memória entre conversas. Nesta oficina você vai sentir na prática a diferença entre um Chat rápido e um Projeto — e vai criar o seu primeiro Projeto, que lembra de tudo enquanto você trabalha nele.

### 🧰 O que você vai usar

- Claude Desktop ou Claude no navegador
- Sua conta ativa no Claude

### 👐 Mão na massa

**Parte 1 — Teste um Chat rápido**

1. Abra o Claude.
2. Fique na tela inicial de Chat comum (sem abrir nenhum Projeto).
3. Digite:
   ```
   Sugira 3 ideias de atividade de 30 minutos para ensinar frações a alunos do 6º ano.
   ```
4. Leia a resposta. Repare: é útil, mas é uma resposta isolada — se você fechar e voltar amanhã, o Claude não vai lembrar dela.

**Parte 2 — Crie seu primeiro Projeto**

5. Procure o botão **"+ Novo Projeto"** (ou **"New Project"**) — normalmente fica na aba **Projects**.
6. Clique nele.
7. No campo **Nome**, digite um título curto para algo que você realmente queira criar (por exemplo: "Apostila de Frações 6º Ano" ou "Plano de Aula de Ciências").
8. No campo **Descrição**, escreva uma frase dizendo o que esse Projeto vai produzir e para quem.
9. Clique em **Criar** (ou **Create**).

**Parte 3 — Explore a tela**

10. Repare na barra lateral: você vai ver seções como **Instructions**, **Knowledge Base** e **Artifacts**.
11. Essas três seções são o "esqueleto" do seu Projeto — vamos preencher cada uma delas nas próximas oficinas.

### ✅ Deu certo?

Se você tem um Projeto criado, com nome e descrição preenchidos, e consegue ver as seções Instructions, Knowledge Base e Artifacts na tela, deu certo.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não encontro o botão "Novo Projeto" | Procure a aba "Projects" no menu principal — em algumas versões fica no menu lateral esquerdo |
| Criei o Projeto, mas não vejo as seções da barra lateral | Clique em uma área vazia do Projeto para abrir a tela completa; a barra pode estar recolhida |
| Minha conta não mostra a opção "Projects" | Confirme se o seu plano do Claude inclui essa função; se não, verifique com o suporte ou com quem administra a conta |

### 🚀 Quer ir além?

Crie um segundo Projeto (vazio mesmo) só para comparar nomes e descrições — isso ajuda a pegar o jeito de definir objetivos claros antes de começar.

> 💡 Dica: dê nomes de Projeto que descrevam o resultado final, não o processo. "Apostila de Frações 6º Ano" é melhor que "Testando o Claude".

---

# Oficina 2 — Dê Contexto: Monte a Base de Conhecimento

### 🎯 O Problema

Imagine que o Claude é um colega novo na sua escola: ele não sabe qual currículo você segue, nem o tom que suas atividades costumam ter. A Base de Conhecimento (Knowledge Base) é o jeito de apresentar esse contexto de uma vez só — para não ter que repetir tudo em toda conversa.

### 🧰 O que você vai usar

- O Projeto criado na Oficina 1
- Ao menos 1 ou 2 arquivos seus (currículo, exemplo de atividade, planilha) — ou um documento simples que você escreva na hora

### 👐 Mão na massa

1. Se ainda não tiver um arquivo à mão, abra um editor de texto (Bloco de Notas, Word ou Google Docs) e escreva um documento curto (meia página) descrevendo o tom que você usa com seus alunos e o tipo de atividade que costuma aplicar. Salve como PDF, DOCX ou TXT.
2. Nomeie o arquivo com um número na frente, por exemplo: `01_Estilo_Pedagogico.docx`.
3. Dentro do seu Projeto, abra a seção **Knowledge Base** na barra lateral.
4. Clique em **"+ Adicionar Arquivo"** (ou **"Add File"**).
5. Arraste o arquivo para a janela, ou clique para selecioná-lo no computador.
6. Espere a confirmação de que o arquivo foi carregado.
7. Se tiver um segundo arquivo (por exemplo, um currículo ou exemplos de atividades anteriores), repita os passos 3 a 6 nomeando como `02_...`.
8. Teste se o Claude está "lendo" o conteúdo: no campo de conversa do Projeto, escreva:
   ```
   Resuma em 3 pontos o que você entendeu do(s) documento(s) que acabei de adicionar.
   ```
9. Leia a resposta e confira se ela realmente menciona o conteúdo do seu arquivo.

### ✅ Deu certo?

Se o Claude resumiu corretamente o conteúdo do arquivo que você subiu — mencionando detalhes que só estariam ali dentro — deu certo. Isso confirma que ele está lendo sua Base de Conhecimento.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O arquivo não termina de carregar | Verifique o tamanho do arquivo (arquivos muito grandes demoram mais) e sua conexão com a internet |
| O Claude responde de forma genérica, sem citar o documento | Confirme que o upload foi concluído (deve aparecer um ícone de "carregado") antes de perguntar |
| Não tenho nenhum documento pronto | Use o passo 1 para criar um documento simples de meia página — vale como teste |

### 🚀 Quer ir além?

Adicione um terceiro arquivo e peça ao Claude para combinar informações dos três documentos em uma única resposta, citando de qual arquivo veio cada parte.

> ⚠️ Cuidado: evite subir documentos com dados sensíveis de alunos (nomes completos, notas individuais) sem necessidade — prefira versões resumidas ou fictícias para praticar.

> 📌 Não esqueça: nomear os arquivos com números na frente (01, 02, 03...) ajuda o Claude — e você — a organizar a ordem de leitura.

---

# Oficina 3 — Dê Personalidade: Escreva Instruções Customizadas

### 🎯 O Problema

Sem instruções fixas, você acaba repetindo "use um tom mais simples" ou "sempre inclua um exemplo prático" em toda conversa nova. As Instruções Customizadas (Custom Instructions) resolvem isso: você escreve uma vez, e o Claude aplica sempre que trabalhar nesse Projeto.

### 🧰 O que você vai usar

- O Projeto das oficinas anteriores, já com ao menos um arquivo na Knowledge Base

### 👐 Mão na massa

1. Dentro do Projeto, procure a seção **Custom Instructions** (ou **Instructions**) na barra lateral.
2. Escreva as instruções preenchendo estes 4 blocos (copie e adapte):
   ```
   OBJETIVO DO PROJETO:
   [uma frase dizendo o que este projeto produz e para quem]

   TOM E LINGUAGEM:
   [como você quer que o Claude fale — formal? descontraído? Dê um exemplo de frase]

   O QUE FAZER:
   - [uma instrução-chave, ex: "sempre incluir contexto prático"]
   - [outra instrução-chave]

   O QUE NÃO FAZER:
   - NÃO [algo que você quer evitar]
   - NÃO [outra coisa a evitar]
   ```
3. Clique em **Salvar** (ou **Save**).
4. No campo de conversa do Projeto, peça um pequeno teste:
   ```
   Crie um exemplo curto (um parágrafo ou um exercício) seguindo as instruções
   customizadas que acabei de salvar. Depois, me diga qual instrução você
   seguiu em cada parte.
   ```
5. Leia a resposta e confira: o tom bate com o que você pediu? Alguma restrição foi ignorada?
6. Se algo não bateu, volte à instrução correspondente e deixe-a mais específica (troque "seja claro" por um exemplo concreto de frase clara).

### ✅ Deu certo?

Se o exemplo criado pelo Claude respeitou o tom e não violou nenhuma das restrições que você escreveu — e ele conseguiu explicar qual instrução seguiu em cada parte — deu certo.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não encontro a seção "Custom Instructions" | Procure por "Instructions" ou pelo ícone de engrenagem nas configurações do Projeto |
| O resultado ignorou uma das minhas instruções | Reescreva essa instrução com um exemplo concreto — instruções vagas ("seja claro") funcionam pior do que instruções com exemplo |
| Minhas instruções parecem se contradizer | Releia em voz alta: se duas frases pedem coisas opostas (ex: "fácil" e "rápido"), escolha uma prioridade clara |

### 🚀 Quer ir além?

Peça ao próprio Claude para apontar se encontrou alguma contradição ou ambiguidade nas suas instruções — às vezes ele identifica o problema antes de você.

> 🤓 Curiosidade técnica: instruções com exemplo ("Exemplo bom: ...", "Exemplo ruim: ...") funcionam melhor do que só descrições, porque dão ao Claude um padrão concreto para copiar — não só uma regra abstrata para interpretar.

---

# Oficina 4 — Crie e Ajuste um Artefato de Verdade

### 🎯 O Problema

Pedir uma coisa, receber uma resposta longa no meio do chat, pedir um ajuste e receber outra resposta longa embaixo da primeira — isso vira bagunça rápido. Os Artefatos (Artifacts) resolvem isso: é um documento único que evolui, com o conteúdo de um lado e a visualização do outro. Nesta oficina você cria e refina o seu primeiro.

### 🧰 O que você vai usar

- O Projeto das oficinas anteriores, já com Knowledge Base e Custom Instructions prontos

### 👐 Mão na massa

1. No campo de conversa do Projeto, peça um Artefato de forma clara:
   ```
   Crie um ARTIFACT com um pequeno exercício (ou um parágrafo de material didático,
   ou um mini roteiro de 10 minutos de aula — escolha o que fizer mais sentido
   para o seu Projeto).

   Siga as instruções customizadas do projeto.
   Formato: Markdown, com título claro.
   ```
2. Espere o Claude criar o Artefato — você vai ver o conteúdo de um lado (editor) e a visualização do outro lado (preview).
3. Leia o resultado com calma, como se estivesse revisando o trabalho de um colega.
4. Escreva um feedback específico, apontando exatamente onde está o problema e o que você espera no lugar. Use este padrão:
   ```
   [Onde está o problema]: [o que está errado]. [O que você quer no lugar].
   ```
   Exemplo: "No segundo parágrafo: a frase está muito longa. Quero uma frase de no máximo 15 palavras ali."
5. Envie o feedback e observe: o Claude deve editar só a parte indicada, sem reescrever o Artefato inteiro.
6. Repita os passos 4 e 5 quantas vezes achar necessário, até o resultado ficar do jeito que você quer.

### ✅ Deu certo?

Se você consegue apontar uma parte específica do Artefato, pedir uma mudança, e ver só aquela parte mudar (sem perder o resto do que já estava bom), deu certo.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O Claude reescreveu o Artefato inteiro em vez de só o trecho pedido | Repita o pedido deixando ainda mais claro: "mantenha tudo igual, mude só [trecho]" |
| Não sei como localizar o "trecho" no feedback | Cite uma palavra ou frase exata do texto gerado como referência do lugar |
| O Artefato não apareceu, só veio uma resposta de texto comum | Reforce no pedido a palavra "ARTIFACT" ou "crie um documento", deixando claro que não é para responder só no chat |

### 🚀 Quer ir além?

Peça ao Claude para exportar o Artefato (botão "Download" ou "Copy") e abra o arquivo fora do Claude — veja como ficaria pronto para imprimir ou compartilhar.

> 📌 Não esqueça: feedback vago ("não ficou bom") obriga o Claude a adivinhar. Feedback com local + problema + solução esperada é sempre mais rápido de resolver.

---

# Projeto Final — Seu Primeiro Mini Produto Pedagógico Completo

### 🎯 A missão

Juntar tudo que você praticou — Projeto, Base de Conhecimento, Instruções Customizadas e Artefato — em um único mini produto pronto para usar de verdade: por exemplo, um exercício completo com gabarito, ou um mini roteiro de aula com abertura, desenvolvimento e encerramento.

### 👐 Mão na massa

1. Volte ao Projeto que você construiu ao longo do curso.
2. Confira rapidamente: ele já tem pelo menos 1 arquivo na Knowledge Base e as Custom Instructions salvas? Se faltar algo, complete antes de seguir.
3. Peça ao Claude, em um único pedido, um Artefato "final":
   ```
   Crie um ARTIFACT chamado "[nome do seu produto]" que reúna:
   - Um título e uma breve introdução
   - O conteúdo principal (exercício, atividade ou mini roteiro)
   - Uma seção final (gabarito, ou "próximos passos", conforme o caso)

   Use a Base de Conhecimento e siga as Custom Instructions do projeto.
   Formato: Markdown, pronto para revisão.
   ```
4. Revise o resultado com o mesmo olhar crítico da Oficina 4: o que está bom? O que precisa de ajuste?
5. Aplique pelo menos uma rodada de feedback específico.
6. Quando estiver satisfeito, clique em **Download** (ou **Copy**) e salve o arquivo no seu computador.

### 🏁 Como saber que terminou

- [ ] O Projeto tem ao menos 1 documento na Knowledge Base
- [ ] O Projeto tem Custom Instructions salvas
- [ ] Existe um Artefato final, revisado e ajustado por pelo menos um ciclo de feedback
- [ ] O arquivo final foi exportado (baixado ou copiado) para uso fora do Claude
- [ ] Você olhou o resultado com olhos de quem vai realmente usar — e aprovou

---

# A Parte dos Dez — Hábitos que Fazem Você Trabalhar Melhor com o Claude

1. Prefira Projeto a Chat sempre que for usar o resultado mais de uma vez.
2. Escreva a instrução pensando em alguém que nunca viu o seu contexto — quanto mais específico, melhor.
3. Dê exemplo de "bom" e de "ruim" nas suas instruções — isso vale mais do que uma descrição longa.
4. Nomeie os arquivos da Knowledge Base com número na frente (01, 02, 03...).
5. Peça a "versão 1" rápido, em vez de tentar escrever o pedido perfeito por meia hora.
6. Dê feedback apontando local + problema + solução esperada — nunca só "não gostei".
7. Revise sempre antes de usar. Você é responsável pelo resultado final, não o Claude.
8. Quando o resultado ficar bom, guarde o Projeto — ele pode ser reaproveitado no próximo semestre ou ano letivo.
9. Evite subir documentos com dados sensíveis de alunos sem necessidade.
10. Se travar em algo, pergunte ao próprio Claude "o que eu poderia deixar mais claro nesse pedido?" — às vezes a resposta está ali.

---

## Conseguiu! E agora?

Você acabou de sair de "só usar o Claude" para "trabalhar junto com o Claude" — e isso muda o jogo. Um Projeto bem montado, com contexto certo e instruções claras, economiza um tempo enorme na próxima vez que você precisar de algo parecido.

A partir daqui, o caminho é prática: reaproveite o Projeto que você criou, duplique-o para uma nova turma ou disciplina, e vá refinando as instruções conforme aprende o que funciona melhor com o seu estilo. Cada rodada fica mais rápida que a anterior.
