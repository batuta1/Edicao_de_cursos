# Vibe Coding Para Leigos — Curso Hands-on

> *» IA: Bloco Cover — título verbatim e subtítulo em itálico logo abaixo. Não traduzir "Lovable" nem "vibe coding".*

*Em menos de duas horas, você vai pôr no ar um app de verdade — com login, banco de dados e a prova de que cada pessoa só vê o que é dela —, construído conversando com a IA, sem escrever uma linha de código.*

## Antes de Arregaçar as Mangas

> *» IA: Bloco Text — parágrafo verbatim.*

Aqui você não escreve código: você descreve o que quer e o Lovable constrói. Isso tem nome — vibe coding. Pense numa loja: a tela que o visitante vê é o salão; o login é a catraca; o banco de dados são os fichários dos fundos. Você vai encomendar essa loja por descrição e inspecionar cada etapa. O plano grátis serve.

> *» IA: Bloco Checklist — itens verbatim.*

O que você precisa ter aberto agora:

- Computador com navegador e internet.
- Conta gratuita no Lovable (`lovable.dev`).
- Um bloco de notas para anotar créditos e senhas de teste.

> *» IA: Bloco Statement — regra de ouro, preservar o emoji.*

> 🔑 **Regra de ouro:** uma mudança por pedido, um teste depois de cada mudança. Pedir tudo de uma vez é o caminho mais curto para um app que ninguém entende.

> *» IA: Bloco Statement — aviso de créditos, preservar o emoji.*

> 📌 **Não esqueça:** o plano grátis dá 5 créditos de construção por dia (no máximo 30 por mês). Cada pedido em Build gasta uma fração variável — mudar uma cor custa uns 0,50; adicionar login, uns 1,20 (exemplos da página de preços). Uma mensagem em Plan custa 1. Ninguém garante que o app inteiro caiba no grátis, por isso o curso vai em três dias: Preparação + Oficinas 1–2; Oficinas 3–4; Projeto Final.

> *» IA: Bloco Process — passos de preparação verbatim; preservar os breadcrumbs; não traduzir termos de interface.*

Monte sua bancada (7 min):

1. Entre em `lovable.dev > Sign up` e crie sua conta (e-mail, Google, GitHub ou Apple).
2. Ache a caixa de pedido e o seletor de modo (`Chat` / `Plan` / `Build`) [conferir]. Não envie nada ainda.
3. Abra `Lovable > More > Usage` [conferir] e anote seus créditos de hoje.
4. Abra `Lovable > Account settings > Preferences > AI model training` [conferir]. Desde 09/09/2026, o que você faz no plano grátis pode treinar a IA da Lovable. Decida se quer desligar.
5. Repare: os menus estão em inglês. A ajuda oficial é toda em inglês, e o curso usa os nomes em inglês.

> *» IA: Bloco Statement — curiosidade técnica, preservar o emoji.*

> 🤓 **Curiosidade técnica:** os três modos são Chat (conversa, não mexe em nada), Plan (faz um plano e espera seu OK) e Build (constrói). Tutorial antigo falando em "Agent mode"? É o Build com nome velho. Pode pular sem prejuízo.

> *» IA: Bloco Statement — ponto de controle, preservar o emoji e o breadcrumb.*

> 🏁 Ponto de controle: em `Lovable > More > Usage`, você anotou os créditos de hoje; em `Account settings > Preferences`, a opção de treinamento está do jeito que você escolheu.

> *» IA: Bloco Accordion — um item por linha da tabela "Se travar".*

| Problema | O que fazer |
|---|---|
| Não acho `Usage` | Procure "credits" ou "usage" no menu da conta ou do workspace |
| O seletor mostra "Agent" | É o Build com nome antigo. Use-o |
| Já estou sem créditos hoje | Espere a renovação de amanhã para começar a Oficina 1 |

## O Mapa da Mão na Massa

> *» IA: Bloco Table — mapa verbatim.*

| Oficina | Problema que vai resolver | Tempo |
|---|---|---|
| 1 | Você tem uma ideia, mas nenhuma tela | 22 min |
| 2 | O app esquece tudo quando você recarrega a página | 20 min |
| 3 | Você não sabe se uma pessoa vê as tarefas da outra | 16 min |
| 4 | O app só existe pra você — e toda mudança some do público | 22 min |
| Projeto Final | Fazer o ciclo inteiro sozinho, com um app do seu perfil | 28 min |

> *» IA: Bloco Text — frase verbatim.*

Faça em sequência: cada oficina usa o app da anterior e entrega uma pequena vitória. Somando a preparação, são 115 minutos.

---

# Oficina 1 — Da ideia à tela

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Bloco Text — verbatim.*

Você tem uma ideia de app de tarefas. A tentação é escrever "faz um app de tarefas com login, banco, categorias, prazos, notificações e modo escuro" e torcer. Resultado provável: créditos do dia esgotados e um app que você não sabe por onde consertar. Nesta oficina, você faz a planta e constrói só a tela.

### 🧰 O que você vai usar

> *» IA: Bloco List — verbatim.*

- Lovable, modo Build.
- A ficha de requisitos abaixo.

> *» IA: Bloco Text para a frase; Bloco Statement para a ficha, verbatim, entre aspas triplas.*

A própria Lovable recomenda responder quatro perguntas antes de construir: o quê, para quem, por quê e qual a ação principal. Some a isso o que fica de fora e como saber que está pronto, e você tem uma ficha:

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
Pronto quando: criar conta, entrar, criar tarefa, concluir, sair, entrar com outra conta e não ver as tarefas da primeira
"""

### 👐 Mão na massa

> *» IA: Bloco Process — passos verbatim; preservar os breadcrumbs; prompt do passo 3 verbatim, entre aspas triplas.*

1. Leia a ficha e ajuste o que quiser (sem acrescentar funcionalidades!).
2. Anote seus créditos em `Lovable > More > Usage`.
3. Escolha o modo `Build`, cole e envie:

"""
Crie um aplicativo web chamado Minhas Tarefas. Por enquanto, faça só a interface: cabeçalho, campo para o título da tarefa, botão Adicionar, lista de tarefas e uma mensagem quando a lista estiver vazia. Visual simples, alto contraste, legível no celular, em português do Brasil.
Não adicione banco de dados nem login ainda.
"""

4. Espere a prévia aparecer à direita.
5. Clique no campo, digite uma tarefa e clique em Adicionar.
6. Troque para `Preview toolbar > Mobile view` [conferir] e veja se tudo continua legível.
7. Quer mudar um texto? Use `Preview toolbar > Select elements` [conferir], clique no texto e edite direto — sem gastar crédito de construção.
8. Anote quanto crédito a construção gastou.

> *» IA: Bloco Statement — aviso, preservar o emoji.*

> ⚠️ **Cuidado:** recarregue a página e a tarefa some. Isso é esperado! Ainda não há banco de dados — é o problema da Oficina 2.

### ✅ Deu certo?

> *» IA: Bloco Statement — ponto de controle; preservar o emoji e o breadcrumb.*

> 🏁 Ponto de controle: no editor do Lovable, a prévia mostra o "Minhas Tarefas" com campo, botão e lista vazia, legível em `Mobile view`, sem tela de login.

### 🚑 Se travar

> *» IA: Bloco Accordion — um item por linha; preservar os breadcrumbs.*

| Problema | O que fazer |
|---|---|
| O Lovable criou login mesmo assim | Abra `History`, clique em `Revert` na versão anterior e reenvie com "Não adicione banco nem login" numa linha sozinha |
| O visual ficou estranho | Uma mudança só: "Aumente o contraste do botão Adicionar. Não mude mais nada." |
| Acabaram os créditos | Volte amanhã: a prévia e a conversa ficam salvas |

### 🚀 Quer ir além?

> *» IA: Bloco Accordion — três desafios, marcado como OPCIONAL; verbatim.*

1. Use o modo `Chat` para perguntar "Que melhorias de usabilidade você sugere para esta tela?" — sem aplicar nada. Validação: nenhuma versão nova aparece no `History`.
2. Edite três textos pela `Preview toolbar` e confira em `Usage` que nenhum crédito de construção foi gasto. Validação: saldo igual antes e depois.
3. Escreva a ficha de requisitos de outra ideia sua, sem construir. Validação: "Fora do escopo" tem pelo menos três itens.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 2 — Login e banco de dados

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Bloco Text — verbatim.*

Seu app esquece tudo ao recarregar a página — e qualquer pessoa que abrisse o link usaria a mesma lista. Você precisa de uma catraca (login) e de fichários (banco de dados). No Lovable, os dois vêm do Lovable Cloud — não precisa criar conta em nenhum outro serviço.

### 🧰 O que você vai usar

> *» IA: Bloco List — verbatim; preservar os breadcrumbs.*

- Modos `Plan` e `Build`.
- `More > Cloud > Database` e `More > Cloud > Users`.

> *» IA: Bloco Text — verbatim.*

Mudança grande pede plano. O modo Plan lê seu projeto, propõe o que vai fazer e espera seu OK — por 1 crédito. Assim você descobre antes de gastar se o Lovable entendeu.

> *» IA: Bloco Statement — curiosidade técnica, preservar o emoji.*

> 🤓 **Curiosidade técnica:** o Lovable Cloud é montado sobre o Supabase, um serviço de banco de dados de código aberto. A própria ajuda pergunta "Do I need Supabase?" e responde "No." Dá para ligar um Supabase seu, mas não existe botão para trocar de um para o outro depois. Neste curso, fique no Cloud. Pode pular sem prejuízo.

### 👐 Mão na massa

> *» IA: Bloco Process — passos verbatim; preservar os breadcrumbs; prompts dos passos 2 e 4 verbatim, entre aspas triplas; manter nomes de colunas sem alteração.*

1. Anote os créditos.
2. Escolha `Plan` e envie:

"""
Analise o app e proponha a menor alteração possível para adicionar autenticação por e-mail e senha e uma tabela de tarefas. Cada usuário deve acessar apenas as próprias tarefas. Inclua regras RLS e descreva como testar com duas contas. Não implemente até eu aprovar.
"""

3. Leia o plano. Ele fala em e-mail e senha? Em uma tabela de tarefas? Em RLS (a regra que tranca as gavetas — você entende na Oficina 3)? Se sim, aprove.
4. Troque para `Build` e envie:

"""
Aplique o plano aprovado. Adicione login por e-mail e senha, logout e uma tabela tasks com title, completed, user_id e created_at. Crie políticas RLS para que cada usuário só possa ler, criar, atualizar e excluir as próprias tarefas. Não altere o visual.
"""

5. Se o Lovable pedir para ativar o Lovable Cloud, aprove.
6. Abra `Lovable > More > Cloud > Database` [conferir]: a tabela `tasks` está lá?
7. Abra `Lovable > More > Cloud > Users` [conferir] e ache o botão `Add user`. Ainda não crie ninguém.

> *» IA: Bloco Statement — aviso, preservar o emoji.*

> ⚠️ **Cuidado:** em `Database`, apagar linhas é para sempre. Nem o `Revert` traz dados de volta — ele só desfaz o código.

### ✅ Deu certo?

> *» IA: Bloco Statement — ponto de controle; preservar o emoji e o breadcrumb.*

> 🏁 Ponto de controle: a prévia abre numa tela de login e a tabela `tasks` aparece em `Lovable > More > Cloud > Database`.

### 🚑 Se travar

> *» IA: Bloco Accordion — um item por linha.*

| Problema | O que fazer |
|---|---|
| O plano não fala em RLS | Responda no Plan: "Inclua políticas RLS por usuário no plano" e só depois aprove |
| O Lovable também criou login com Google | Peça em Build: "Remova as outras formas de login; mantenha só e-mail e senha" |
| Erro depois do Build | Copie a mensagem e use em Plan: "O que acontece / onde / esperado / observado. Investigue antes de corrigir." |

### 🚀 Quer ir além?

> *» IA: Bloco Accordion — três desafios, marcado como OPCIONAL; verbatim; preservar os breadcrumbs.*

1. Em `Project settings > Knowledge` [conferir], registre "Visual em português, alto contraste; login só por e-mail e senha". Validação: o texto fica salvo.
2. Em `More > Cloud > Database`, abra a tabela e identifique as quatro colunas pedidas. Validação: todas estão lá.
3. Pergunte no `Chat`: "Explique em linguagem simples o que as políticas RLS deste projeto fazem." Validação: a resposta menciona `user_id`.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 3 — Quem vê o quê

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Bloco Text — verbatim.*

O login funciona. Mas será que a Ana não consegue ver as tarefas do Bruno? Esconder dados da tela não basta: tudo o que vai para o navegador pode ser inspecionado. Quem garante que cada pessoa só abre a própria gaveta é a regra RLS no banco. E só existe um jeito de saber se ela funciona: testar com duas contas.

### 🧰 O que você vai usar

> *» IA: Bloco List — verbatim; preservar os breadcrumbs.*

- `More > Cloud > Users > Add user`.
- A prévia do app.

> *» IA: Bloco Text — verbatim.*

Autenticação é a catraca: confere quem entrou. Autorização é o crachá: diz quais gavetas essa pessoa abre. Num app vibe-coded, o erro clássico é ter a catraca e esquecer o crachá — todo mundo que entra abre todas as gavetas. Em 2026, pesquisas acadêmicas apontaram justamente autenticação e autorização mal feitas como falhas recorrentes desses apps.

### 👐 Mão na massa

> *» IA: Bloco Process — passos verbatim; preservar os breadcrumbs.*

1. Em `Lovable > More > Cloud > Users > Add user` [conferir], crie `teste.a@exemplo.com` e `teste.b@exemplo.com` com senhas de teste (anote no seu bloco de notas, nunca no chat do Lovable).
2. Na prévia, entre como A, crie "Tarefa da conta A" e saia.
3. Entre como B, crie "Tarefa da conta B" e olhe a lista.
4. Recarregue a página: a tarefa continua?
5. Em `Lovable > More > Cloud > Database`, confira as duas linhas, cada uma com um `user_id` diferente.

> *» IA: Bloco Statement — lembrete, preservar o emoji.*

> 📌 **Não esqueça:** `exemplo.com` é um endereço fictício. Nada de e-mail real de colega, aluno ou cliente no teste.

### ✅ Deu certo?

> *» IA: Bloco Statement — ponto de controle; preservar o emoji e o breadcrumb.*

> 🏁 Ponto de controle: logada como B, a prévia mostra só "Tarefa da conta B", a tarefa sobrevive ao recarregar, e `More > Cloud > Database > tasks` mostra dois `user_id` diferentes.

### 🚑 Se travar

> *» IA: Bloco Accordion — um item por linha.*

| Problema | O que fazer |
|---|---|
| A conta B vê a tarefa da A | Isso é falha de segurança: não publique. Em Plan: "A conta B vê tarefas da conta A. Investigue as políticas RLS e proponha a correção." Depois, repita o teste |
| `Add user` não aparece ou pede confirmação por e-mail | Cadastre-se pela tela de login do próprio app com dois e-mails que você controla |
| A tarefa some ao recarregar | O app ainda não grava no banco. Descreva o erro em Plan (onde, esperado, observado) |

### 🚀 Quer ir além?

> *» IA: Bloco Accordion — três desafios, marcado como OPCIONAL; verbatim.*

1. Com a conta B, tente marcar como concluída uma tarefa que não é dela (se aparecer alguma, é falha). Validação: não há como.
2. Peça ao Lovable, em Build: "Teste o fluxo de criar conta, entrar, adicionar tarefa e sair, e relate cada passo; não altere o app." Validação: ele devolve um relatório passo a passo.
3. Crie uma terceira conta e repita o teste. Validação: cada conta vê só a sua tarefa.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 4 — Publicar, mudar, republicar

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Bloco Text — verbatim.*

Seu app funciona — na prévia. Para o mundo, ele não existe. E tem uma pegadinha que pega todo iniciante: depois de publicar, cada mudança que você faz fica só na prévia até você republicar. Nesta oficina você abre as portas, faz uma reforma pequena e leva a reforma ao público.

### 🧰 O que você vai usar

> *» IA: Bloco List — verbatim.*

- Botões `Publish` e `Publish changes`.
- `History` e `Bookmarks`.
- Uma janela anônima do navegador.

### 👐 Mão na massa

> *» IA: Bloco Process — passos verbatim; preservar os breadcrumbs; prompt do passo 6 verbatim, entre aspas triplas.*

1. Clique em `Lovable > Publish` (canto superior direito, perto de `Share`) [conferir].
2. Leia o resultado da varredura de segurança. Achou problema de RLS? Pare e volte à Oficina 3.
3. Revise o endereço sugerido (`algo.lovable.app`) e confirme.
4. Abra o endereço numa janela anônima: deve aparecer a tela de login. Entre como A e confira que só a tarefa A aparece.
5. Em `Lovable > History` [conferir], marque a versão atual como Bookmark ("publicado v1").
6. Em `Build`, peça uma mudança só:

"""
Adicione acima da lista um filtro com três opções: Todas, Pendentes e Concluídas. Não altere login, dados nem o restante do visual.
"""

7. Teste o filtro na prévia. Abra o endereço público: o filtro ainda não está lá, certo?
8. Clique em `Publish > Publish changes` e recarregue a janela anônima.

> *» IA: Bloco Statement — dica, preservar o emoji.*

> 💡 **Dica:** se a mudança quebrar alguma coisa, não peça "conserte" cinco vezes. Volte ao Bookmark "publicado v1" com `Revert` e refaça o pedido menor.

> *» IA: Bloco Statement — aviso, preservar o emoji.*

> ⚠️ **Cuidado:** a varredura do Lovable ajuda, mas a própria documentação avisa que ela não substitui uma revisão de segurança completa. Ela é um alarme, não um atestado.

### ✅ Deu certo?

> *» IA: Bloco Statement — ponto de controle; preservar o emoji e o breadcrumb.*

> 🏁 Ponto de controle: em janela anônima, o endereço `algo.lovable.app` abre no login, mostra só as tarefas da conta logada e exibe o filtro depois de `Publish > Publish changes`.

### 🚑 Se travar

> *» IA: Bloco Accordion — um item por linha; preservar os breadcrumbs.*

| Problema | O que fazer |
|---|---|
| Mudei e o site público não mudou | `Publish > Publish changes` |
| O filtro quebrou a lista | `History` > Bookmark "publicado v1" > `Revert`; refaça com um pedido menor |
| A janela anônima já entra logada | Feche todas as janelas anônimas e abra uma nova |

### 🚀 Quer ir além?

> *» IA: Bloco Accordion — três desafios, marcado como OPCIONAL; verbatim.*

1. Abra o endereço público no celular. Validação: login e filtro funcionam.
2. Peça ao Lovable: "Review my app's security. Check the authentication flow." (exemplo da biblioteca oficial de prompts). Validação: a resposta cita as políticas RLS.
3. Conecte o projeto ao GitHub (disponível no grátis) [conferir]. Validação: o repositório aparece na sua conta do GitHub.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Projeto Final — Seu app, do seu jeito

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Projeto Final" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 A missão

> *» IA: Bloco Text para o parágrafo; Bloco Table para os perfis (alternativa: Tabs), verbatim.*

Agora você faz o ciclo inteiro sozinho, num app novo: ficha → plano → construção → duas contas → varredura → publicação → uma mudança → republicação. Escolha seu perfil:

| Perfil | App | Dados da tabela | Mudança final |
|---|---|---|---|
| Professor | Diário de Leituras (suas leituras, não as dos alunos) | título, autor, páginas lidas, status (lendo/concluído) | Filtro "Lendo / Concluídos" |
| Empreendedor | Banco de Ideias de Produto | ideia, problema, público, estágio (ideia/teste/descartada) | Filtro por estágio |

> *» IA: Bloco Text — verbatim.*

Antes de construir, pergunte-se: tem algum dado real aí? Nome de aluno, nota, cliente, CPF, telefone? Se sim, troque por dado inventado. Um protótipo de curso não vira sistema da escola ou da empresa sem análise de LGPD e segurança — e, se envolver dinheiro, saúde ou dados de menores, sem revisão profissional.

> *» IA: Bloco Statement — aviso, preservar o emoji.*

> ⚠️ **Cuidado:** nada de senha, chave ou dado pessoal real no pedido ao Lovable. O que você escreve na conversa vai para os servidores da empresa.

> *» IA: Bloco Statement — dica, preservar o emoji.*

> 💡 **Dica:** este projeto gasta, numa estimativa sem garantia, de 3 a 5 créditos. Faça num dia em que você ainda não usou nenhum.

### 👐 Mão na massa

> *» IA: Bloco Process — passos verbatim; preservar os breadcrumbs.*

1. Escreva a ficha de requisitos do seu app (use a da Oficina 1 como modelo).
2. Crie um projeto novo. Em `Plan`, peça num plano só: a interface, login por e-mail e senha, a tabela do seu perfil e regras RLS por usuário. Leia e aprove.
3. Execute em `Build`.
4. Crie duas contas fictícias em `More > Cloud > Users > Add user` [conferir] e faça o teste de quem vê o quê (Oficina 3).
5. Leia a varredura e publique em `Publish`.
6. Marque um Bookmark em `History`, peça a mudança final do seu perfil e teste na prévia.
7. `Publish > Publish changes` e confira no endereço público, em janela anônima.

### 🏁 Como saber que terminou

> *» IA: Bloco Checklist — itens verbatim, marcáveis.*

- [ ] Ficha de requisitos com "fora do escopo" e "pronto quando"
- [ ] Só dados fictícios
- [ ] Plano lido e aprovado antes do Build
- [ ] Duas contas testadas: cada uma vê só o que é seu
- [ ] Varredura lida antes de publicar
- [ ] Endereço público abre no login
- [ ] Mudança final visível no endereço público depois de `Publish changes`

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Projeto Final" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# A Parte dos Dez — Dez Hábitos de Quem Faz Vibe Coding sem Sustos

> *» IA: Bloco List (numerada) — dez itens verbatim; preservar os termos de interface.*

1. **Planta antes da obra.** Ficha de requisitos primeiro, pedido depois.
2. **Uma mudança por pedido.** E teste antes do próximo.
3. **Plan para mudança grande.** Um crédito para saber se a IA entendeu vale mais que três para desfazer.
4. **Texto se edita na prévia.** `Select elements` não gasta crédito de construção.
5. **Duas contas, sempre.** Quem não testou não sabe quem vê o quê.
6. **Prévia não é publicação.** Mudou? `Publish changes`.
7. **Bookmark antes de arriscar.** E lembre: `Revert` volta o código, não os dados.
8. **Erro se descreve.** Onde, o que esperava, o que aconteceu — e peça para investigar antes de corrigir.
9. **Segredo não vai na vitrine.** Senha e chave nunca no pedido nem na tela.
10. **Dado real só com análise.** Protótipo de curso é com dados inventados.

## Conseguiu! E agora?

> *» IA: Bloco Text — dois parágrafos verbatim.*

Você construiu, protegeu, testou, publicou e reformou um app — duas vezes. Mais importante: aprendeu a inspecionar o que a IA entrega, que é o que separa um protótipo bonito de um app em que dá para confiar.

Para continuar, crie outros apps pequenos com dados inventados, sempre com a ficha e o teste de duas contas. Depois, siga para Replit Agent - Essentials, o próximo da trilha, e, quando quiser ligar seu app a outros serviços, para Lovable - Hands On.
