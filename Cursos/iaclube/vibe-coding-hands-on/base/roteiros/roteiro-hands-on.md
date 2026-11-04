# Vibe Coding Para Leigos — Curso Hands-on (Roteiro Final)

*Ao final, você terá um app de verdade no ar — com login, banco de dados e a prova de que cada
pessoa só vê o que é dela —, construído conversando com a IA, sem escrever uma linha de código.*

**Público-Alvo:** quem tem uma ideia de app e nunca programou — empreendedores, professores,
curiosos.

**Objetivo Geral:** você vai construir no Lovable o app "Minhas Tarefas" em camadas: primeiro a tela,
depois o login e o banco, depois o teste com duas contas, e então publicar, mudar e republicar. No
Projeto Final, faz o ciclo inteiro sozinho com um app do seu perfil.

**Pré-requisitos:** já ter usado um assistente de IA. Nada de programação.

> Nota de vigência: nomes, planos e menus vêm da documentação oficial do Lovable (em inglês)
> consultada em 18/10/2026. O Lovable muda com frequência. Onde está **[conferir]**, confira na sua
> tela; se for diferente, vale o que a tela mostra.

## Estrutura do Curso

| Etapa | Título | Tempo |
|---|---|---|
| Preparação | Monte sua bancada | 7 min |
| Oficina 1 | Da ideia à tela | 22 min |
| Oficina 2 | Login e banco de dados | 20 min |
| Oficina 3 | Quem vê o quê | 16 min |
| Oficina 4 | Publicar, mudar, republicar | 22 min |
| Projeto Final | Seu app, do seu jeito | 28 min |
| **Total** | | **115 min** |

Tempos apurados pela MET em `carga-horaria/carga-horaria-hands-on.md`.

**Anexos:** A — Rótulos do Lovable; B — Rastreabilidade da auditoria.

---

## Antes de Arregaçar as Mangas

Aqui você não escreve código: você descreve o que quer e o Lovable constrói. Isso tem nome — *vibe
coding*. Pense numa loja: a tela que o visitante vê é o salão; o login é a catraca; o banco de dados
são os fichários dos fundos. Você vai encomendar essa loja por descrição e inspecionar cada etapa.

O que você precisa ter aberto agora:

- computador com navegador e internet;
- conta gratuita no Lovable (`lovable.dev`);
- um bloco de notas para anotar créditos e senhas de teste.

> 🔑 **Regra de ouro:** uma mudança por pedido, um teste depois de cada mudança. Pedir tudo de uma
> vez é o caminho mais curto para um app que ninguém entende.

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| Preparação | Você não sabe quanto pode gastar nem onde ficam as coisas | 7 min |
| 1 | Você tem uma ideia, mas nenhuma tela | 22 min |
| 2 | O app esquece tudo quando você recarrega a página | 20 min |
| 3 | Você não sabe se uma pessoa vê as tarefas da outra | 16 min |
| 4 | O app só existe pra você — e toda mudança some do público | 22 min |
| Projeto Final | Fazer o ciclo inteiro sozinho, com um app do seu perfil | 28 min |

Faça em sequência: cada oficina usa o app da anterior. Por causa dos créditos do plano grátis,
sugerimos três dias: Preparação + Oficinas 1–2; Oficinas 3–4; Projeto Final.

---

## Preparação — Monte sua bancada (7 min)

### 0.1 Conta, créditos e privacidade

- **📸 Sugestão de Prints:** (1) `lovable.dev` com o botão "Sign up" destacado; (2) tela inicial com
  o seletor de modo aberto mostrando Chat, Plan e Build **[conferir]**; (3) `More > Usage` com o
  saldo do dia **[conferir]**; (4) `Account settings > Preferences > AI model training` **[conferir]**.

> 📌 **Não esqueça:** o plano grátis dá **5 créditos de construção por dia** (no máximo 30 por mês).
> Cada pedido em Build gasta uma fração variável — mudar uma cor custa uns 0,50; adicionar login, uns
> 1,20 (exemplos da página de preços). Uma mensagem em Plan custa 1. Ninguém garante que o app
> inteiro caiba no grátis, por isso o curso é dividido em dias.

### 👐 Mão na massa

1. Entre em `lovable.dev` e crie sua conta (e-mail, Google, GitHub ou Apple).
2. Ache a caixa de pedido e o seletor de modo. Não envie nada ainda.
3. Abra `More > Usage` **[conferir]** e anote seus créditos de hoje.
4. Abra `Account settings > Preferences > AI model training` **[conferir]**. Desde 09/09/2026, o que
   você faz no plano grátis pode treinar a IA da Lovable. Decida se quer desligar.
5. Anote: os menus estão em inglês? (A ajuda oficial é toda em inglês; o curso usa os nomes em
   inglês.)

> 🤓 **Curiosidade técnica:** os três modos são Chat (conversa, não mexe em nada), Plan (faz um
> plano e espera seu OK) e Build (constrói). Tutorial antigo falando em "Agent mode"? É o Build com
> nome velho. Pode pular sem prejuízo.

### ✅ Deu certo?

Você tem conta, sabe quantos créditos tem hoje e já decidiu sobre o treinamento.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não acho `Usage` | Procure "credits" ou "usage" no menu da conta ou do workspace |
| O seletor mostra "Agent" | É o Build com nome antigo. Use-o |
| Já estou sem créditos hoje | Espere a renovação de amanhã para começar a Oficina 1 |

---

## Oficina 1 — Da ideia à tela

### 🎯 O Problema

Você tem uma ideia de app de tarefas. A tentação é escrever "faz um app de tarefas com login, banco,
categorias, prazos, notificações e modo escuro" e torcer. Resultado provável: créditos do dia
esgotados e um app que você não sabe por onde consertar. Nesta oficina, você faz a planta e constrói
**só a tela**.

### 🧰 O que você vai usar

- Lovable, modo Build;
- a ficha de requisitos abaixo.

### 1.1 A planta antes da obra

- **📸 Sugestão de Prints:** editor do Lovable com a conversa à esquerda e a prévia à direita, já
  mostrando o "Minhas Tarefas" com lista vazia.

A própria Lovable recomenda responder quatro perguntas antes de construir: **o quê**, **para quem**,
**por quê** e **qual a ação principal**. Some a isso o que fica de fora e como saber que está pronto,
e você tem uma ficha:

"""
Nome: Minhas Tarefas
Para quem: uma pessoa que quer organizar os próprios afazeres
Problema: anotar, concluir e remover tarefas
Ação principal: adicionar uma tarefa
Telas: login e lista de tarefas
Dados: título, concluída (sim/não), dono, data de criação
Regra de acesso: cada conta vê só as próprias tarefas
Fora do escopo: colaboração, anexos, pagamentos, notificações, dados reais
Visual: simples, alto contraste, legível no celular
Pronto quando: criar conta, entrar, criar tarefa, concluir, sair, entrar com outra conta e não ver
as tarefas da primeira
"""

### 👐 Mão na massa

1. Leia a ficha acima e ajuste o que quiser (sem acrescentar funcionalidades!).
2. Anote seus créditos em `More > Usage`.
3. Escolha o modo **Build**, cole e envie:

   """
   Crie um aplicativo web chamado Minhas Tarefas. Por enquanto, faça só a interface: cabeçalho,
   campo para o título da tarefa, botão Adicionar, lista de tarefas e uma mensagem quando a lista
   estiver vazia. Visual simples, alto contraste, legível no celular, em português do Brasil.
   Não adicione banco de dados nem login ainda.
   """

4. Espere a prévia aparecer à direita.
5. Clique no campo, digite uma tarefa e clique em Adicionar.
6. Troque para `Mobile view` **[conferir]** e veja se tudo continua legível.
7. Quer mudar um texto? Use `Preview toolbar > Select elements` **[conferir]**, clique no texto e
   edite direto — sem gastar crédito de construção.
8. Anote quanto crédito a construção gastou.

> ⚠️ **Cuidado:** recarregue a página e a tarefa some. Isso é esperado! Ainda não há banco de dados —
> é o problema da Oficina 2.

### ✅ Deu certo?

A prévia mostra o "Minhas Tarefas" com campo, botão e lista vazia, legível no celular, **sem** login.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O Lovable criou login mesmo assim | Abra `History`, clique em `Revert` na versão anterior e reenvie com "Não adicione banco nem login" numa linha sozinha |
| O visual ficou estranho | Uma mudança só: "Aumente o contraste do botão Adicionar. Não mude mais nada." |
| Acabaram os créditos | Volte amanhã: a prévia e a conversa ficam salvas |

### 🚀 Quer ir além?

1. Use o modo **Chat** para perguntar "Que melhorias de usabilidade você sugere para esta tela?" — sem
   aplicar nada. Valida se nenhuma versão nova aparecer no `History`.
2. Edite três textos pela `Preview toolbar` e confira em `Usage` que nenhum crédito de construção foi
   gasto.
3. Escreva a ficha de requisitos de outra ideia sua, sem construir. Valida se "Fora do escopo" tiver
   pelo menos três itens.

---

## Oficina 2 — Login e banco de dados

### 🎯 O Problema

Seu app esquece tudo ao recarregar a página — e qualquer pessoa que abrisse o link usaria a mesma
lista. Você precisa de uma **catraca** (login) e de **fichários** (banco de dados). No Lovable, os dois
vêm do **Lovable Cloud** — não precisa criar conta em nenhum outro serviço.

### 🧰 O que você vai usar

- modos Plan e Build;
- `More > Cloud > Database` e `More > Cloud > Users`.

### 2.1 Planejar antes de construir

- **📸 Sugestão de Prints:** (1) resposta do Plan com o plano em tópicos e o pedido de aprovação; (2)
  `More > Cloud > Database` com a tabela `tasks` aberta **[conferir]**.

Mudança grande pede plano. O modo **Plan** lê seu projeto, propõe o que vai fazer e **espera seu OK**
— por 1 crédito. Assim você descobre antes de gastar se o Lovable entendeu.

> 🤓 **Curiosidade técnica:** o Lovable Cloud é montado sobre o Supabase, um serviço de banco de dados
> de código aberto. A própria ajuda pergunta "Do I need Supabase?" e responde "No." Dá para ligar um
> Supabase seu, mas não existe botão para trocar de um para o outro depois. Neste curso, fique no
> Cloud. Pode pular sem prejuízo.

### 👐 Mão na massa

1. Anote os créditos.
2. Escolha **Plan** e envie:

   """
   Analise o app e proponha a menor alteração possível para adicionar autenticação por e-mail e
   senha e uma tabela de tarefas. Cada usuário deve acessar apenas as próprias tarefas. Inclua
   regras RLS e descreva como testar com duas contas. Não implemente até eu aprovar.
   """

3. Leia o plano. Ele fala em e-mail e senha? Em uma tabela de tarefas? Em RLS (a regra que tranca as
   gavetas — você entende na Oficina 3)? Se sim, aprove.
4. Troque para **Build** e envie:

   """
   Aplique o plano aprovado. Adicione login por e-mail e senha, logout e uma tabela tasks com
   title, completed, user_id e created_at. Crie políticas RLS para que cada usuário só possa ler,
   criar, atualizar e excluir as próprias tarefas. Não altere o visual.
   """

5. Se o Lovable pedir para ativar o Lovable Cloud, aprove.
6. Abra `More > Cloud > Database` **[conferir]**: a tabela `tasks` está lá?
7. Abra `More > Cloud > Users` **[conferir]** e ache o botão `Add user`. Ainda não crie ninguém.

> ⚠️ **Cuidado:** em `Database`, apagar linhas é para sempre. Nem o `Revert` traz dados de volta — ele
> só desfaz o código.

### ✅ Deu certo?

A prévia agora abre numa tela de login e a tabela `tasks` aparece em `More > Cloud > Database`.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O plano não fala em RLS | Responda no Plan: "Inclua políticas RLS por usuário no plano" e só depois aprove |
| O Lovable também criou login com Google | Peça em Build: "Remova as outras formas de login; mantenha só e-mail e senha" |
| Erro depois do Build | Copie a mensagem e use em Plan: "O que acontece / onde / esperado / observado. Investigue antes de corrigir." |

### 🚀 Quer ir além?

1. Em `Project settings > Knowledge` **[conferir]**, registre "Visual em português, alto contraste;
   login só por e-mail e senha". Valida se o texto ficar salvo.
2. Em `More > Cloud > Database`, abra a tabela e identifique as quatro colunas pedidas. Valida se
   estiverem todas lá.
3. Pergunte no Chat: "Explique em linguagem simples o que as políticas RLS deste projeto fazem." Valida
   se a resposta mencionar `user_id`.

---

## Oficina 3 — Quem vê o quê

### 🎯 O Problema

O login funciona. Mas será que a Ana não consegue ver as tarefas do Bruno? Esconder dados da tela não
basta: tudo o que vai para o navegador pode ser inspecionado. Quem garante que cada pessoa só abre a
própria gaveta é a regra **RLS** no banco. E só existe um jeito de saber se ela funciona: testar com
duas contas.

### 🧰 O que você vai usar

- `More > Cloud > Users > Add user`;
- a prévia do app.

### 3.1 Catraca e crachá

- **📸 Sugestão de Prints:** a prévia logada com a conta B, mostrando só "Tarefa da conta B", e
  `More > Cloud > Database` ao lado com duas linhas de `user_id` diferentes.

**Autenticação** é a catraca: confere quem entrou. **Autorização** é o crachá: diz quais gavetas
essa pessoa abre. Num app vibe-coded, o erro clássico é ter a catraca e esquecer o crachá — todo mundo
que entra abre todas as gavetas. Em 2026, pesquisas acadêmicas apontaram justamente autenticação e
autorização mal feitas como falhas recorrentes desses apps.

### 👐 Mão na massa

1. Em `More > Cloud > Users > Add user` **[conferir]**, crie `teste.a@exemplo.com` e
   `teste.b@exemplo.com` com senhas de teste (anote no seu bloco de notas, nunca no chat do Lovable).
2. Na prévia, entre como A, crie "Tarefa da conta A" e saia.
3. Entre como B, crie "Tarefa da conta B" e olhe a lista.
4. Recarregue a página: a tarefa continua?
5. Em `More > Cloud > Database`, confira as duas linhas, cada uma com um `user_id` diferente.

> 📌 **Não esqueça:** `exemplo.com` é um endereço fictício. Nada de e-mail real de colega, aluno ou
> cliente no teste.

### ✅ Deu certo?

A conta B vê **só** a tarefa B, a tarefa sobrevive ao recarregar, e a tabela mostra dois donos
diferentes.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| A conta B vê a tarefa da A | Isso é falha de segurança: **não publique**. Em Plan: "A conta B vê tarefas da conta A. Investigue as políticas RLS e proponha a correção." Depois, repita o teste |
| `Add user` não aparece ou pede confirmação por e-mail | Cadastre-se pela tela de login do próprio app com dois e-mails que você controla |
| A tarefa some ao recarregar | O app ainda não grava no banco. Descreva o erro em Plan (onde, esperado, observado) |

### 🚀 Quer ir além?

1. Com a conta B, tente marcar como concluída uma tarefa que não é dela (se aparecer alguma, é falha).
   Valida se não houver como.
2. Peça ao Lovable, no Build: "Teste o fluxo de criar conta, entrar, adicionar tarefa e sair, e
   relate cada passo; não altere o app." Valida se ele devolver um relatório passo a passo.
3. Crie uma terceira conta e repita o teste. Valida se cada conta vir só a sua tarefa.

---

## Oficina 4 — Publicar, mudar, republicar

### 🎯 O Problema

Seu app funciona — na prévia. Para o mundo, ele não existe. E tem uma pegadinha que pega todo
iniciante: depois de publicar, cada mudança que você faz fica **só na prévia** até você republicar.
Nesta oficina você abre as portas, faz uma reforma pequena e leva a reforma ao público.

### 🧰 O que você vai usar

- botões `Publish` e `Publish changes`;
- `History` e `Bookmarks`;
- uma janela anônima do navegador.

### 👐 Mão na massa

1. Clique em `Publish` (canto superior direito, perto de `Share`) **[conferir]**.
2. Leia o resultado da varredura de segurança. Achou problema de RLS? Pare e volte à Oficina 3.
3. Revise o endereço sugerido (`algo.lovable.app`) e confirme.
4. Abra o endereço numa janela anônima: deve aparecer a tela de login. Entre como A e confira que só
   a tarefa A aparece.
5. Em `History` **[conferir]**, marque a versão atual como Bookmark ("publicado v1").
6. Em **Build**, peça uma mudança só:

   """
   Adicione acima da lista um filtro com três opções: Todas, Pendentes e Concluídas. Não altere
   login, dados nem o restante do visual.
   """

7. Teste o filtro na prévia. Abra o endereço público: o filtro ainda **não** está lá, certo?
8. Clique em `Publish > Publish changes` e recarregue a janela anônima.

> 💡 **Dica:** se a mudança quebrar alguma coisa, não peça "conserte" cinco vezes. Volte ao Bookmark
> "publicado v1" com `Revert` e refaça o pedido menor.

> ⚠️ **Cuidado:** a varredura do Lovable ajuda, mas a própria documentação avisa que ela não substitui
> uma revisão de segurança completa. Ela é um alarme, não um atestado.

### ✅ Deu certo?

O endereço público abre no login, mostra só as tarefas da conta logada e exibe o filtro depois de
`Publish changes`.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Mudei e o site público não mudou | `Publish > Publish changes` |
| O filtro quebrou a lista | `History` > Bookmark "publicado v1" > `Revert`; refaça com um pedido menor |
| A janela anônima já entra logada | Feche todas as janelas anônimas e abra uma nova |

### 🚀 Quer ir além?

1. Abra o endereço público no celular. Valida se login e filtro funcionarem.
2. Peça ao Lovable: "Review my app's security. Check the authentication flow." (exemplo da biblioteca
   oficial de prompts). Valida se ele citar as políticas RLS.
3. Conecte o projeto ao GitHub (disponível no grátis) **[conferir]**. Valida se o repositório aparecer
   na sua conta do GitHub.

---

## Projeto Final — Seu app, do seu jeito

### 🎯 A missão

Agora você faz o ciclo inteiro sozinho, num app novo: ficha → plano → construção → duas contas →
varredura → publicação → uma mudança → republicação. Escolha seu perfil:

| Perfil | App | Dados da tabela | Mudança final |
|---|---|---|---|
| Professor | Diário de Leituras (suas leituras, não as dos alunos) | título, autor, páginas lidas, status (lendo/concluído) | Filtro "Lendo / Concluídos" |
| Empreendedor | Banco de Ideias de Produto | ideia, problema, público, estágio (ideia/teste/descartada) | Filtro por estágio |

### 5.1 Antes de construir: o que pode e o que não pode

Pergunte-se: tem algum dado real aí? Nome de aluno, nota, cliente, CPF, telefone? Se sim, troque por
dado inventado. Um protótipo de curso não vira sistema da escola ou da empresa sem análise de LGPD e
segurança — e, se envolver dinheiro, saúde ou dados de menores, sem revisão profissional.

> ⚠️ **Cuidado:** nada de senha, chave ou dado pessoal real no pedido ao Lovable. O que você escreve
> na conversa vai para os servidores da empresa.

> 💡 **Dica:** este projeto gasta, numa estimativa sem garantia, de 3 a 5 créditos. Faça num dia em
> que você ainda não usou nenhum.

### 👐 Mão na massa

1. Escreva a ficha de requisitos do seu app (use a da Oficina 1 como modelo).
2. Crie um projeto novo. Em **Plan**, peça num plano só: a interface, login por e-mail e senha, a
   tabela do seu perfil e regras RLS por usuário. Leia e aprove.
3. Execute em **Build**.
4. Crie duas contas fictícias e faça o teste de quem vê o quê (Oficina 3).
5. Leia a varredura e publique.
6. Marque um Bookmark, peça a mudança final do seu perfil e teste na prévia.
7. `Publish > Publish changes` e confira no endereço público, em janela anônima.

### 🏁 Como saber que terminou

- [ ] Ficha de requisitos com "fora do escopo" e "pronto quando"
- [ ] Só dados fictícios
- [ ] Plano lido e aprovado antes do Build
- [ ] Duas contas testadas: cada uma vê só o que é seu
- [ ] Varredura lida antes de publicar
- [ ] Endereço público abre no login
- [ ] Mudança final visível no endereço público depois de `Publish changes`

---

## A Parte dos Dez — Dez Hábitos de Quem Faz Vibe Coding sem Sustos

1. **Planta antes da obra.** Ficha de requisitos primeiro, pedido depois.
2. **Uma mudança por pedido.** E teste antes do próximo.
3. **Plan para mudança grande.** Um crédito para saber se a IA entendeu vale mais que três para
   desfazer.
4. **Texto se edita na prévia.** `Select elements` não gasta crédito de construção.
5. **Duas contas, sempre.** Quem não testou não sabe quem vê o quê.
6. **Prévia não é publicação.** Mudou? `Publish changes`.
7. **Bookmark antes de arriscar.** E lembre: `Revert` volta o código, não os dados.
8. **Erro se descreve.** Onde, o que esperava, o que aconteceu — e peça para investigar antes de
   corrigir.
9. **Segredo não vai na vitrine.** Senha e chave nunca no pedido nem na tela.
10. **Dado real só com análise.** Protótipo de curso é com dados inventados.

## Conseguiu! E agora?

Você construiu, protegeu, testou, publicou e reformou um app — duas vezes. Mais importante: aprendeu
a inspecionar o que a IA entrega, que é o que separa um protótipo bonito de um app em que dá para
confiar.

Para continuar, crie outros apps pequenos com dados inventados, sempre com a ficha e o teste de duas
contas. Depois, siga para *Replit Agent - Essentials*, o próximo da trilha, e, quando quiser ligar seu
app a outros serviços, para *Lovable - Hands On*.

---

## Anexo A — Rótulos do Lovable (ajuda em inglês, 18/10/2026)

| Função | Caminho |
|---|---|
| Modos | `Chat` / `Plan` / `Build` |
| Editar texto | `Preview toolbar > Select elements` **[conferir]** |
| Celular | `Mobile view` **[conferir]** |
| Créditos | `More > Usage` **[conferir]** |
| Banco | `More > Cloud > Database` **[conferir]** |
| Usuários | `More > Cloud > Users > Add user` **[conferir]** |
| Histórico | `History` / `Revert` / `Bookmarks` **[conferir]** |
| Publicar | `Publish` / `Publish > Publish changes` |
| Treinamento | `Account settings > Preferences > AI model training` **[conferir]** |
| Instruções fixas | `Project settings > Knowledge` **[conferir]** |

## Anexo B — Rastreabilidade da auditoria

| ID | Destino nesta versão |
|---|---|
| H1 | Oficina 1 (ficha + interface sem backend) |
| H2 | Oficina 2 (Plan → Build; Lovable Cloud; Database e Users) |
| H3 | Oficina 3 (duas contas fictícias) antes da publicação; Projeto Final por perfil com dados inventados |
| H4 | Oficinas 2–4 (descrever erro, investigar antes, Revert) |
| H5 | Oficina 4 (Publish → mudança → Publish changes) |
| H6 | Seção Preparação |
| H7 | Box 📌 da Preparação, créditos anotados em cada oficina, dica do Projeto Final, plano de três dias |
| H8 | Nova regra de ouro |
| H9 | Oficina 3 (RLS) e Oficina 4 (varredura não é atestado) |
| H10 | Domínio próprio removido; desafios dentro do grátis |
| H11 | "Se travar" com três linhas reais por oficina |
| H12 | Três desafios com validação por oficina |
| H13 | 115 min pela MET |
| H14 | Oficina 4 (Bookmark antes de mudar; Revert não restaura dados) |
| H15 | Projeto Final com app novo por perfil e checklist |
