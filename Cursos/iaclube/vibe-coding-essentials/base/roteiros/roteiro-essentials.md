# Vibe Coding - Essentials — Roteiro Final

**Público-Alvo:** não programadores com ideias de produto, empreendedores e professores (trilha
Vibe Coding: do zero ao app, primeiro curso).

**Objetivo Geral:** capacitar o participante a construir aplicações web por linguagem natural —
prática denominada *vibe coding* — com o Lovable, especificando o aplicativo antes de pedi-lo,
gerando-o em etapas, acrescentando banco de dados e autenticação com controle de acesso por usuário,
publicando-o, iterando-o com segurança e reconhecendo os limites do método. Ao final, o participante
terá publicado o aplicativo "Minhas Tarefas", com login e banco de dados, comprovado por teste com
duas contas fictícias que cada usuário vê apenas os próprios registros, e, na atividade integradora,
aplicado o mesmo ciclo a um aplicativo do próprio perfil (professor ou empreendedor).

**Pré-requisitos:** uso básico de um assistente de IA (ChatGPT, Claude ou Gemini); **nenhum**
conhecimento de programação.

**Recursos necessários:** computador com navegador atualizado e internet; conta gratuita no Lovable
(`lovable.dev`), mediante e-mail, Google, GitHub ou Apple (18 anos ou autorização de responsável).

> Nota de vigência: planos, créditos e rótulos de interface foram extraídos da documentação oficial
> do Lovable consultada em 18/10/2026, disponível em inglês. O Lovable é um serviço de atualização
> contínua, sem número de versão, e altera nomes e limites com frequência (o modo "Agent" passou a
> chamar-se "Build" em 2026). Os rótulos de interface são mantidos em inglês; itens marcados com
> **[conferir]** dependem de validação na conta usada para a produção do curso.

## Estrutura do Curso

| Nível | Módulo | Título | Tempo |
|---|---|---|---|
| Nível 0 — Pré-filtro | 0 | Preparação e Verificação Inicial | 7 min |
| Nível 1 — Fundamentos | 1 | O que é vibe coding e como funciona um aplicativo web | 25 min |
| Nível 1 — Fundamentos | 2 | Segurança, Dados e Custos antes de Construir | 21 min |
| Nível 2 — Construção | 3 | Especificar e gerar o primeiro protótipo | 16 min |
| Nível 2 — Construção | 4 | Banco de dados, login e controle de acesso | 22 min |
| Nível 2 — Construção | 5 | Publicar, iterar e reconhecer limites | 18 min |
| Síntese | 6 | Síntese e Aplicação Integrada | 20 min |
| **Total** | | | **129 min** |

Tempos apurados pela MET em `carga-horaria/carga-horaria-essentials.md`. Por causa do limite diário
de créditos do plano gratuito, recomenda-se cursar em três dias: Módulos 0–3, Módulos 4–5 e Módulo 6.

**Anexos:** A — Rótulos e caminhos do Lovable; B — Ficha de requisitos; C — Checklist de prontidão
para publicação; D — Rastreabilidade da auditoria.

**Aplicativo-âncora:** "Minhas Tarefas" — lista pessoal de tarefas com login, construída nos Módulos
3 a 5 apenas com dados fictícios. Na atividade integradora, cada perfil constrói um aplicativo de
mesma estrutura: *Diário de Leituras* (professor) ou *Banco de Ideias de Produto* (empreendedor).

**Fio condutor:** a analogia da **loja**, plantada no Módulo 1 — o aplicativo web é uma loja com
**salão** (front-end), **estoque e administração** (back-end), **fichários** (banco de dados),
**catraca** (autenticação) e **crachás que abrem apenas certas gavetas** (autorização e RLS); a
**prévia** é o ensaio e a **publicação** é abrir as portas ao público. Vibe coding equivale a
encomendar a loja a uma equipe de obra por descrição, com inspeções frequentes. É retomada no Módulo
2 (o que fica na vitrine é visto por todos; o cofre não fica no salão), no Módulo 3 (a planta antes
da obra), no Módulo 4 (catraca e gavetas), no Módulo 5 (abrir as portas e reformar com a loja
aberta) e no Módulo 6.

**Fronteira do curso:** integrações e evolução de aplicativos existentes, Replit Agent, Bolt e v0, e
programação em editor de código (Cursor, Claude Code) são tratados, respectivamente, em *Lovable -
Hands On*, *Replit Agent - Essentials* e nos cursos próprios da trilha. Supabase próprio, domínio
próprio, Edge Functions e download de código são apenas mencionados.

---

## Módulo 0 — Preparação e Verificação Inicial

> Ponto de partida: módulo de pré-filtro, anterior a qualquer construção.

### 0.1 Conta, plano gratuito e créditos

- **📸 Sugestão de Prints:** (1) página inicial de `lovable.dev` com o botão "Sign up" destacado;
  (2) tela inicial após o login, com a caixa de prompt central e o seletor de modo ao lado, aberto,
  mostrando "Chat", "Plan" e "Build" **[conferir]**; (3) tela `More > Usage` exibindo o saldo de
  créditos do dia e do mês **[conferir]**.

O Lovable é utilizado pelo navegador, sem instalação, no endereço `lovable.dev`. Existem aplicativos
para Windows, macOS, iOS (15 ou posterior) e Android (9 ou posterior), mas a própria documentação os
apresenta como complemento; as instruções deste curso referem-se à versão web. A conta gratuita é
criada com e-mail e senha, Conta Google, GitHub ou Apple, e a documentação exige 18 anos ou
autorização de responsável. Ao criar a conta, o usuário recebe um espaço de trabalho pessoal
(*personal workspace*).

O plano gratuito é suficiente para as atividades, desde que se respeite a rota de baixo consumo
descrita a seguir. Em 18/10/2026, a página oficial de preços informava:

| Plano | Preço (página oficial) | O que inclui, em síntese |
|---|---|---|
| Free | US$ 0 | 5 *build credits* por dia (teto de 30 por mês); 20 Cloud credits/mês; 4 AI credits/mês; projetos privados; publicação em `lovable.app`; sincronização com GitHub |
| Pro | a partir de US$ 25/mês (100 créditos) | Domínio próprio, editor e download de código, mais créditos |
| Business | a partir de US$ 50/mês | Controles corporativos; dados excluídos do treinamento por padrão |

Cumpre compreender o que é um **crédito**: a unidade de cobrança de cada alteração feita pela IA. O
custo não é fixo — a página de preços exemplifica que mudar a cor de um botão pode custar 0,50
crédito e adicionar autenticação, 1,20. Uma mensagem no modo Plan custa 1 crédito. O fabricante não
garante que um aplicativo completo caiba no plano gratuito; por isso, o curso adota uma **rota de
baixo consumo** (uma página principal, login por e-mail e senha, uma tabela, nenhuma integração
externa, nenhuma imagem gerada, poucas iterações) e distribui as construções em três dias. Preços em
reais não são publicados; estudantes e professores com e-mail acadêmico elegível têm desconto no Pro.

Convém, por fim, registrar que a documentação do Lovable está em inglês e não há confirmação oficial
de que a interface esteja traduzida. Os rótulos são, por isso, mantidos em inglês (Anexo A). Os
pedidos à IA, porém, podem ser escritos em português.

### 0.2 Prompt-base (Mão na massa) — registro de verificação

"""
Data da verificação: [dd/mm/aaaa]
Forma de login: [e-mail | Google | GitHub | Apple]
Plano: [Free | outro]
Idioma da interface: [inglês | português | misto]
Modos vistos no seletor: [ex.: Chat, Plan, Build]
Créditos disponíveis hoje / no mês (More > Usage): [valores]
Divergências em relação ao Anexo A: [descrever ou "nenhuma"]
"""

### Pílula Hands-on — Verificação de acesso (7 min)

1. Acessar `lovable.dev` e criar a conta gratuita (ou entrar na existente).
2. Localizar a caixa de prompt e o seletor de modo, sem enviar pedido.
3. Abrir `More > Usage` **[conferir]** e anotar os créditos disponíveis.
4. Preencher o registro de verificação.

**Critério de êxito:** conta ativa, seletor de modo localizado e saldo de créditos anotado.

### Solução de Problemas

| Situação | Causa provável | Procedimento |
|---|---|---|
| O seletor mostra "Agent" em vez de "Build" | Material ou interface antiga | Tratar "Agent" como o atual "Build"; registrar a divergência |
| Não aparece `More > Usage` | Rótulo alterado | Procurar indicação de créditos no menu da conta ou do workspace **[conferir]** |
| Créditos do dia zerados ao começar | Uso anterior na mesma conta | Aguardar a renovação diária antes do Módulo 3 |

## Descrição

- **Objetivos da Aula:** apresentar o acesso ao Lovable, o plano gratuito, o conceito de crédito, a
  rota de baixo consumo e a convenção de rótulos em inglês.
- **Habilidades Esperadas:** criar sozinho a conta, localizar os modos de trabalho e consultar o saldo
  de créditos antes de cada etapa.

---

## Módulo 1 — O que é vibe coding e como funciona um aplicativo web

> Pressupõe o acesso verificado no Módulo 0; introduz o método e o vocabulário do curso.

### 1.1 Vibe coding: origem, definição e fronteiras

- **📸 Sugestão de Prints:** desenho de uma loja em corte, com rótulos: salão com vitrine e balcão
  ("front-end"), porta de entrada com catraca ("autenticação"), sala dos fundos com fichários
  ("banco de dados") e um cofre ("segredos"), e crachás de cores diferentes junto a gavetas
  ("autorização / RLS").

Denomina-se ***vibe coding*** a criação de software por meio da descrição, em linguagem natural, do
resultado desejado, aceitando-se em grande parte o código produzido pela inteligência artificial. O
termo foi popularizado por Andrej Karpathy, pesquisador de IA, em fevereiro de 2025, e escolhido
palavra do ano de 2025 pelo dicionário Collins. Em sentido estrito, admite aceitar o código sem
examiná-lo em detalhe — característica que o distingue da **programação assistida por IA**, na qual
o programador continua lendo e compreendendo o código.

Convém distinguir, ainda, *vibe coding* de **no-code** e **low-code**. No-code designa ferramentas
em que a aplicação é montada com componentes visuais, arrastando blocos; low-code mistura essa
montagem com algum código. *Vibe coding* parte da linguagem natural. A fronteira não é absoluta — o
Lovable oferece conversa, edição visual e acesso ao código —, mas, para os fins do curso, "*vibe
coding*" descreve o **método de trabalho** e "no-code/low-code", o **tipo de interface**.

O **Lovable**, ferramenta deste curso, é uma plataforma lançada em 18 de novembro de 2024, em
Estocolmo, que gera a partir de conversa uma aplicação web completa — interface, lógica, banco de
dados, autenticação e hospedagem — e a publica num endereço terminado em `lovable.app`. Trabalha em
três modos: **Chat**, que conversa e esclarece sem alterar o código; **Plan**, que propõe um plano e
aguarda aprovação; e **Build**, que executa as alterações (chamado "Agent mode" em documentação
anterior).

Para que a descrição em linguagem natural funcione, é indispensável compreender as partes de um
aplicativo web — e é aqui que se planta a analogia que conduzirá o curso. Um aplicativo web
assemelha-se a uma **loja**. O **front-end** é o salão: telas, botões e formulários que o cliente vê
e toca no navegador. O **back-end** é o estoque e a administração, fora do alcance do cliente, onde
se executam regras e se guardam segredos. O **banco de dados** é um conjunto de fichários: cada
tabela é um fichário, cada linha uma ficha, cada coluna um campo. A **autenticação** é a catraca que
confere quem está entrando; a **autorização** — no Lovable, implementada por uma regra do banco
chamada **RLS** (*Row Level Security*, segurança por linha) — é o crachá que define quais gavetas
cada pessoa pode abrir. A **publicação** (*deploy*) abre as portas ao público; a prévia é apenas o
ensaio. E *vibe coding*, nessa analogia, equivale a encomendar a loja a uma equipe de obra por meio
de descrições: a velocidade aumenta, mas a inspeção continua necessária.

### 1.2 Glossário aplicado e casos publicados

| Termo | Definição | Na loja | No "Minhas Tarefas" |
|---|---|---|---|
| Front-end | Parte que roda no navegador | Salão e vitrine | Tela com a lista e o botão Adicionar |
| Back-end | Parte de servidor: regras, segredos, banco | Estoque e administração | Lovable Cloud |
| Banco de dados | Estrutura que guarda registros | Fichários | Tabela `tasks` |
| Autenticação | Verificar quem é o usuário | Catraca | Login por e-mail e senha |
| Autorização / RLS | Definir o que cada usuário pode ler ou alterar | Crachá que abre certas gavetas | Cada conta vê só as próprias tarefas |
| Publicação | Colocar uma versão em endereço público | Abrir as portas | `minhas-tarefas.lovable.app` |
| Domínio | Nome do endereço | Endereço da loja | Subdomínio gratuito `lovable.app` |
| Segredo (*secret*) | Valor sensível, como chave de API | Combinação do cofre | Não usado no curso |
| Repositório | Pasta de código com histórico | Arquivo de plantas | GitHub (opcional) |

O Lovable divulga casos de não programadores: o Plinq, aplicativo brasileiro de segurança para
mulheres criado por uma fundadora sem formação técnica, e o Elora, criado por um especialista em
saúde em cerca de um mês. Cumpre registrar que são histórias publicadas pela própria fabricante, com
números não auditados; não foi localizado caso independente e verificável de professor brasileiro.

### Pílula Hands-on — Distinção entre métodos (4 min)

Questão de múltipla escolha. Uma professora descreve em português, numa caixa de texto, um aplicativo
de registro de leituras; a ferramenta gera telas, banco e login, e ela ajusta o resultado por novos
pedidos, sem abrir o código. Classifica-se a prática como:

a) no-code, porque ela não escreveu código;
b) programação assistida por IA, porque uma IA escreveu o código;
c) *vibe coding*, porque o aplicativo foi construído a partir de descrições em linguagem natural,
   aceitando-se o código gerado;
d) low-code, porque houve banco de dados.

**Gabarito:** c. **Fundamentação:** não escrever código não basta para caracterizar no-code, que
pressupõe montagem por componentes visuais (a); programação assistida pressupõe que a pessoa revise o
código (b); a presença de banco de dados não define o método (d).

## Descrição

- **Objetivos da Aula:** definir *vibe coding* com origem e fronteiras; apresentar o Lovable e seus
  três modos; introduzir o vocabulário de aplicativo web pela analogia da loja.
- **Habilidades Esperadas:** explicar sozinho, com o vocabulário correto, as partes de um aplicativo
  web e situar uma prática entre *vibe coding*, no-code e programação assistida.

---

## Módulo 2 — Segurança, Dados e Custos antes de Construir

> Pressupõe o vocabulário do Módulo 1; desloca o foco para os riscos, antes do primeiro pedido de
> construção.

### 2.1 O que fica na vitrine é visto por todos

- **📸 Sugestão de Prints:** (1) tela `Account settings > Preferences` com a opção "AI model training"
  destacada e desativada **[conferir]**; (2) tela `More > Cloud > Secrets` com a lista vazia e o botão
  de adicionar segredo **[conferir]**.

Retomando a analogia: tudo o que está no salão da loja pode ser visto e tocado pelo cliente. Do mesmo
modo, **tudo o que vai para o front-end pode ser inspecionado e manipulado por qualquer usuário** com
as ferramentas comuns do navegador. Decorre daí a primeira regra: chaves secretas, senhas e regras
sensíveis nunca ficam no front-end — nem no texto do pedido à IA. No Lovable, valores sensíveis
(chaves de API, por exemplo) são guardados em `More > Cloud > Secrets`, criptografados, e usados
apenas pelo servidor. O curso não utiliza segredos; a regra é apresentada para que nenhum seja
digitado por engano.

A segunda regra é que **esconder um dado da tela não o protege**. Se o banco não tiver regra de
acesso por usuário (RLS), qualquer pessoa autenticada pode, em tese, ler os registros de outra, ainda
que a interface não os mostre. A documentação oficial recomenda políticas RLS por usuário; o curso
exige, no Módulo 4, um teste com duas contas para comprovar o isolamento. A ferramenta executa uma
**varredura rápida de segurança** a cada publicação e oferece uma varredura mais ampla, mas a própria
documentação adverte que essas ferramentas "não substituem uma revisão completa de segurança", e a
opção de bloquear publicações com achados críticos pode estar desativada.

O risco não é teórico. A Lovable divulgou que, entre 3 de fevereiro e 20 de abril de 2026, uma falha
permitiu que usuários autenticados com o link de certos projetos públicos acessassem o histórico de
conversa e o código-fonte; a empresa informou correção e que projetos privados e o Lovable Cloud não
foram afetados. Artigos acadêmicos de 2026 sintetizam as falhas recorrentes em aplicativos criados
por *vibe coding*: autenticação e autorização inadequadas, segredos expostos e código aceito sem
revisão.

### 2.2 Dados pessoais, treinamento e custo

Quanto aos dados, a Lei Geral de Proteção de Dados (LGPD) rege o tratamento de dados pessoais no
Brasil, com princípios como finalidade, necessidade e segurança, e a ANPD orienta agentes de pequeno
porte a adotar medidas técnicas e administrativas de segurança. Para um curso introdutório, a
consequência é simples: **somente dados fictícios**. Nenhum nome real, CPF, endereço, dado de saúde,
nota escolar, dado de criança ou credencial real entra no aplicativo, nem no pedido à IA. Um protótipo
educacional não deve converter-se em sistema de produção sem análise de base legal, transparência,
contratos, retenção e segurança.

Registra-se, ainda, que, desde 9 de setembro de 2026, os dados de clientes dos planos Free e Pro
podem ser usados para treinar os modelos da Lovable, com possibilidade de recusa em `Account settings
> Preferences > AI model training` **[conferir]**; os planos Business e Enterprise ficam excluídos
por padrão. Segundo a documentação, os dados dos usuários finais guardados no banco do aplicativo
não são usados nesse treinamento. Recomenda-se, também, manter o projeto **privado** durante o curso.

Por fim, o custo: cada alteração consome créditos de forma variável, e um pedido amplo pode consumir
a cota diária e gerar um aplicativo difícil de entender. A rota de baixo consumo, apresentada no
Módulo 0, é também uma medida de segurança: alterações pequenas são mais fáceis de conferir.

### Pílula Hands-on — Configuração e triagem de ideias (6 min)

1. Abrir `Account settings > Preferences > AI model training` **[conferir]** e decidir, de modo
   informado, sobre a recusa ao treinamento; registrar a escolha.
2. Classificar cada ideia de aplicativo como **adequada ao curso**, **adequada com ajuste** (indicar
   qual) ou **inadequada**:
   1. Lista pessoal de tarefas com login, dados inventados.
   2. Controle de notas da turma real, com nomes dos alunos.
   3. Catálogo de produtos fictícios com área de administração.
   4. Cadastro de clientes com CPF e telefone, para uso imediato na empresa.

**Gabarito:** (1) adequada. (2) inadequada — dados pessoais de alunos, possivelmente menores; ajuste
possível: turma inventada e nomes fictícios, deixando explícito que não é sistema real. (3) adequada,
sem pagamentos. (4) inadequada — dados pessoais reais e uso em produção sem análise de LGPD e
segurança.

**Critério de êxito:** escolha sobre treinamento registrada; quatro classificações coincidem com o
gabarito.

### Solução de Problemas

| Situação | Causa provável | Procedimento |
|---|---|---|
| Opção de treinamento não encontrada | Rótulo ou posição alterados | Procurar "training" ou "privacy" nas configurações da conta **[conferir]** |
| Dúvida se um dado pode entrar | Ausência de classificação | Não usar; substituir por dado inventado |
| Um pedido à IA contém senha ou chave por engano | Distração | Considerar o valor exposto: revogá-lo no serviço de origem e gerar outro |

## Descrição

- **Objetivos da Aula:** apresentar o caráter inspecionável do front-end, o papel de Secrets e RLS, os
  limites da varredura, o incidente de 2026, as regras de dados fictícios à luz da LGPD, a opção de
  recusa ao treinamento e a relação entre custo e segurança.
- **Habilidades Esperadas:** decidir sozinho se uma ideia de aplicativo pode ser construída com
  segurança no curso, configurar a recusa ao treinamento e evitar dados reais e segredos nos pedidos.

---

## Módulo 3 — Especificar e gerar o primeiro protótipo

> Pressupõe os critérios de segurança; desloca o foco para a especificação e a primeira construção.

### 3.1 A planta antes da obra

- **📸 Sugestão de Prints:** (1) ficha de requisitos do Anexo B preenchida para "Minhas Tarefas";
  (2) editor do Lovable após o primeiro Build, com a conversa à esquerda e a prévia à direita
  mostrando cabeçalho, campo de título, botão "Adicionar" e mensagem de lista vazia; (3) a mesma
  prévia em `Mobile view` **[conferir]**.

Retomando a analogia, ninguém encomenda uma loja sem planta. A documentação do Lovable recomenda
responder, antes de construir, a quatro perguntas: **o que** será criado, **para quem**, **por quê**
e **qual é a ação principal**. Recomenda, ainda, mapear a jornada do usuário, trabalhar por partes e
fazer **uma mudança por vez**, conferindo o resultado antes da seguinte. A ficha de requisitos do
Anexo B organiza essas respostas e acrescenta dados, regra de acesso, o que fica fora do escopo e
critérios de pronto.

A escolha do modo também importa. O **Chat** serve para esclarecer uma dúvida sem alterar nada; o
**Plan** pesquisa o projeto, propõe um plano e espera aprovação, ao custo de 1 crédito por mensagem;
o **Build** executa. Recomenda-se, para mudanças grandes, planejar antes de construir. Para mudanças
de texto, a barra da prévia (`Preview toolbar > Select elements`) permite editar diretamente,
dentro de uma franquia diária, sem gastar créditos de construção.

A estratégia do curso é construir em camadas: primeiro **só a interface**, sem banco nem login; em
seguida, no Módulo 4, o back-end. Essa separação reduz o custo de cada pedido, torna cada resultado
conferível e evita o padrão conhecido de pedir tudo de uma vez e receber um aplicativo que ninguém
consegue depurar.

### 3.2 Prompt-base (Mão na massa) — primeira construção

"""
Crie um aplicativo web chamado Minhas Tarefas. Por enquanto, faça só a interface: cabeçalho, campo
para o título da tarefa, botão Adicionar, lista de tarefas e uma mensagem quando a lista estiver
vazia. Visual simples, alto contraste, legível no celular, em português do Brasil.
Não adicione banco de dados nem login ainda.
"""

### Pílula Hands-on — Ficha de requisitos e primeiro Build (6 min)

1. Preencher a ficha de requisitos do Anexo B para "Minhas Tarefas" (versão sugerida já preenchida).
2. Anotar o saldo de créditos em `More > Usage` **[conferir]**.
3. Na tela inicial, selecionar o modo **Build**, colar o prompt-base e enviar.
4. Aguardar a primeira versão na prévia.

### Avaliação — Conferência do protótipo (4 min)

| Critério | Atendido? |
|---|---|
| A prévia mostra cabeçalho, campo de título e botão Adicionar | |
| Há mensagem de lista vazia | |
| Em `Mobile view`, os elementos continuam legíveis | |
| Não foram criados banco de dados nem login | |
| Crédito consumido anotado | |

**Critério de êxito:** os cinco itens marcados. Observa-se que o botão pode ainda não guardar as
tarefas ao recarregar a página: isso é esperado e será resolvido no Módulo 4.

### Solução de Problemas

| Situação | Causa provável | Procedimento |
|---|---|---|
| O Lovable criou login ou banco mesmo assim | Pedido interpretado de forma ampla | Abrir `History` e usar `Revert` para a versão anterior; reenviar com "não adicione banco nem login" em linha própria |
| Texto do botão saiu diferente | Interpretação livre | Corrigir pela `Preview toolbar > Select elements`, sem gastar crédito de construção |
| Créditos insuficientes | Cota diária consumida | Aguardar a renovação no dia seguinte |

## Descrição

- **Objetivos da Aula:** apresentar as quatro perguntas oficiais, a ficha de requisitos, os modos
  Chat, Plan e Build, a edição pela barra da prévia e a construção em camadas.
- **Habilidades Esperadas:** especificar sozinho um aplicativo simples antes de pedi-lo, escolher o
  modo adequado e gerar uma primeira interface conferível, sem back-end.

---

## Módulo 4 — Banco de dados, login e controle de acesso

> Pressupõe o protótipo de interface; desloca o foco para o back-end.

### 4.1 Catraca e gavetas no Lovable Cloud

- **📸 Sugestão de Prints:** (1) resposta do modo Plan com o plano de autenticação e tabela,
  terminando no pedido de aprovação; (2) `More > Cloud > Database` com a tabela `tasks` aberta e duas
  linhas visíveis **[conferir]**; (3) `More > Cloud > Users` com duas contas de teste e o botão "Add
  user" destacado **[conferir]**.

O back-end padrão do Lovable é o **Lovable Cloud**, construído sobre a base de código aberto do
Supabase e ativado pelo próprio Lovable quando um pedido exige banco de dados ou login — às vezes
solicitando aprovação. Não é preciso criar conta no Supabase: a documentação responde literalmente
"Do I need Supabase? No." Conectar um projeto Supabase próprio é alternativa para quem já o possui,
mas não há migração de um clique entre as duas opções, razão pela qual se recomenda decidir no início
e, neste curso, permanecer no Lovable Cloud.

Retomando a analogia, este módulo instala a **catraca** e as **gavetas com crachá**. O pedido é feito
em duas etapas. Primeiro, no modo **Plan**, pede-se a menor alteração possível para acrescentar
login por e-mail e senha e uma tabela de tarefas em que cada usuário acesse apenas as próprias, com
regras RLS e a descrição de como testar com duas contas; o plano é lido e aprovado. Depois, no modo
**Build**, aplica-se o plano. Especifica-se "e-mail e senha" porque, sem essa indicação, o Lovable
pode gerar outras formas de entrada, o que amplia o escopo.

Concluída a construção, confere-se o resultado na administração da loja: `More > Cloud > Database`
mostra as tabelas e permite ver, adicionar, excluir e exportar linhas; `More > Cloud > Users` lista
as contas e oferece **Add user** e **Auth settings**. Uma tarefa criada pela tela deve aparecer como
linha na tabela. Cumpre advertir que **excluir linhas pela interface é irreversível**, e que reverter
o código (Módulo 5) não recupera dados apagados.

O teste decisivo é o de isolamento: duas contas fictícias, cada uma com uma tarefa; cada conta deve
ver apenas a sua. É esse teste — e não a aparência da tela — que comprova que as gavetas estão
trancadas. Para criar as contas sem depender de confirmação por e-mail, pode-se usar `More > Cloud >
Users > Add user` **[conferir]**, com endereços fictícios.

### 4.2 Prompt-base (Mão na massa) — plano e implementação

"""
[Modo Plan]
Analise o app e proponha a menor alteração possível para adicionar autenticação por e-mail e senha
e uma tabela de tarefas. Cada usuário deve acessar apenas as próprias tarefas. Inclua regras RLS e
descreva como testar com duas contas. Não implemente até eu aprovar.

[Modo Build, após aprovar]
Aplique o plano aprovado. Adicione login por e-mail e senha, logout e uma tabela tasks com title,
completed, user_id e created_at. Crie políticas RLS para que cada usuário só possa ler, criar,
atualizar e excluir as próprias tarefas. Não altere o visual.
"""

### Pílula Hands-on — Plano, aprovação e construção do back-end (6 min)

1. Anotar o saldo de créditos.
2. Selecionar **Plan**, enviar a primeira parte do prompt-base e ler o plano: ele menciona e-mail e
   senha, a tabela e RLS?
3. Aprovar e, em **Build**, enviar a segunda parte. Se o Lovable pedir para ativar o Lovable Cloud,
   aprovar.
4. Abrir `More > Cloud > Database` e confirmar a tabela `tasks`.

### Pílula Hands-on — Teste de isolamento com duas contas (6 min)

1. Em `More > Cloud > Users > Add user` **[conferir]**, criar `teste.a@exemplo.com` e
   `teste.b@exemplo.com`, com senhas de teste anotadas fora do Lovable.
2. Na prévia, entrar com a conta A, criar a tarefa "Tarefa da conta A" e sair.
3. Entrar com a conta B, criar "Tarefa da conta B" e verificar a lista.
4. Recarregar a página e conferir que a tarefa permanece.
5. Em `More > Cloud > Database`, verificar as duas linhas, cada uma com um `user_id` diferente.

**Critério de êxito:** a conta B vê apenas a própria tarefa; a tarefa persiste após recarregar; a
tabela mostra duas linhas de donos distintos.

### Solução de Problemas

| Situação | Causa provável | Procedimento |
|---|---|---|
| A conta B vê a tarefa da conta A | RLS ausente ou ampla | Tratar como falha de segurança: não publicar; pedir em Plan "investigue por que a conta B vê tarefas da conta A e proponha a correção das políticas RLS"; repetir o teste |
| Login não funciona | Configuração de autenticação | Conferir `More > Cloud > Users` e `Auth settings`; copiar a mensagem exata e pedir investigação em Plan antes de corrigir |
| "Add user" não aparece | Rótulo alterado | Criar as contas pela própria tela de cadastro do app, com e-mails que o participante controle |

## Descrição

- **Objetivos da Aula:** apresentar o Lovable Cloud, o fluxo Plan → aprovação → Build para o back-end,
  as telas Database e Users, a irreversibilidade da exclusão de dados e o teste de isolamento.
- **Habilidades Esperadas:** acrescentar sozinho login e banco a um protótipo, conferir o resultado na
  administração do Lovable Cloud e comprovar, com duas contas, que cada usuário vê apenas os próprios
  registros.

---

## Módulo 5 — Publicar, iterar e reconhecer limites

> Pressupõe o aplicativo com isolamento comprovado; desloca o foco para a publicação e a manutenção.

### 5.1 Abrir as portas e reformar com a loja aberta

- **📸 Sugestão de Prints:** (1) botão `Publish` no canto superior direito do editor, ao lado de
  `Share`, e a janela com o endereço `lovable.app` sugerido **[conferir]**; (2) resultado da
  varredura rápida de segurança; (3) o endereço público aberto em janela anônima, mostrando a tela de
  login; (4) painel `History` com uma versão marcada como Bookmark **[conferir]**.

Retomando a analogia, a prévia é o ensaio; **publicar** é abrir as portas. No Lovable, `Publish`, no
canto superior direito do editor, cria um retrato (*snapshot*) do projeto num endereço
`[nome].lovable.app` e executa a varredura rápida de segurança. O ponto mais importante deste módulo
é que **a versão pública não acompanha a prévia**: depois de qualquer mudança, é preciso usar
`Publish > Publish changes`. Muitos "o site não atualizou" são apenas esquecimento desse passo. O
teste da publicação faz-se em janela anônima do navegador, que simula um visitante sem login.

Reformar com a loja aberta exige método. A documentação recomenda uma mudança por pedido e, diante de
um erro, descrevê-lo com precisão — o que acontece, onde, o que se esperava e o que se observou —,
investigando a causa (no Chat ou no Plan) antes de corrigir. O **History** registra cada versão do
código; **Bookmarks** marcam versões importantes; **Revert** volta a uma versão anterior. Revert,
porém, restaura **apenas o código**: dados apagados do banco não voltam. Recomenda-se marcar um
Bookmark antes de qualquer mudança arriscada.

Cumpre, por fim, reconhecer os limites do método. Estudos acadêmicos de 2026 associam *vibe coding* a
prototipação rápida, mas também a código difícil de compreender, dívida técnica, falhas de segurança
e manutenção custosa quando os resultados são aceitos sem revisão. O método não basta, isoladamente,
quando o aplicativo envolve dinheiro, saúde, dados educacionais sensíveis, decisões de alto impacto,
grandes volumes ou exigências regulatórias; nesses casos, são necessárias revisão profissional,
testes e governança. Há também dependência da plataforma: a sincronização com o GitHub, disponível no
plano gratuito, guarda o código fora do Lovable, mas banco, segredos e operação ainda exigiriam
planejamento para migrar — "ter o código" não equivale a "poder mudar de plataforma sem trabalho".
Ferramentas como Replit Agent, Bolt e v0 seguem lógica semelhante e são estudadas em cursos próprios.

### 5.2 Prompt-base (Mão na massa) — descrição de erro

"""
O que acontece: [descrever]
Onde: [tela ou ação]
O que eu esperava: [descrever]
O que aconteceu: [descrever; colar a mensagem de erro, se houver]
Investigue a causa primeiro e me explique. Depois, altere apenas o necessário, sem mudar visual,
login ou dados.
"""

### Pílula Hands-on — Publicação e teste público (6 min)

1. Ler o resultado da varredura antes de confirmar; havendo achado crítico sobre RLS, não publicar e
   voltar ao Módulo 4.
2. Clicar em `Publish`, revisar o endereço sugerido e confirmar.
3. Abrir o endereço em janela anônima: a tela de login deve aparecer.
4. Entrar com a conta A e confirmar que apenas a tarefa da conta A é exibida.

### Avaliação — Checklist de prontidão para publicação (4 min)

Preencher o checklist do Anexo C para "Minhas Tarefas".

**Critério de êxito:** endereço público abre na tela de login; a conta A vê apenas a própria tarefa;
checklist do Anexo C integralmente marcado.

### Solução de Problemas

| Situação | Causa provável | Procedimento |
|---|---|---|
| A mudança não aparece no endereço público | Só a prévia foi atualizada | `Publish > Publish changes` |
| A varredura aponta problema de RLS | Política ausente ou ampla | Não publicar; corrigir conforme o Módulo 4 e repetir o teste de isolamento |
| Um pedido grande alterou várias partes | Mudança ampla | `History > Revert` para a versão anterior e refazer em partes menores |

## Descrição

- **Objetivos da Aula:** apresentar Publish e Publish changes, o teste em janela anônima, o método de
  descrição de erros, History/Bookmarks/Revert e seus limites, e as situações em que *vibe coding* não
  basta.
- **Habilidades Esperadas:** publicar sozinho um aplicativo após conferir a varredura, testá-lo como
  visitante, corrigir erros por mudanças mínimas e decidir quando um projeto exige revisão
  profissional.

---

## Módulo 6 — Síntese e Aplicação Integrada

> Pressupõe os Módulos 1 a 5; articula especificar, proteger, construir, testar, publicar e iterar
> num único ciclo.

### 6.1 O ciclo completo de vibe coding

- **📸 Sugestão de Prints:** esquema circular com seis etapas — Especificar → Proteger → Construir em
  camadas → Testar com duas contas → Publicar → Iterar e republicar —, cada uma com o número do
  módulo correspondente.

Os módulos anteriores compõem um ciclo aplicável a qualquer aplicativo simples: especificar com a
ficha de requisitos (Módulo 3), verificar dados e segurança antes de construir (Módulo 2), construir
em camadas, com Plan antes de Build (Módulos 3 e 4), comprovar o isolamento com duas contas (Módulo
4), publicar após a varredura e iterar com mudanças mínimas, republicando (Módulo 5). Na analogia,
trata-se de encomendar, inspecionar, abrir e reformar uma segunda loja — agora projetada pelo próprio
participante.

A atividade integradora é diferenciada por perfil, sempre com a mesma estrutura técnica (uma tabela,
login, cada usuário vê apenas os próprios registros) e dados fictícios:

| Perfil | Aplicativo | Dados da tabela | Iteração final |
|---|---|---|---|
| Professor | Diário de Leituras | título do livro, autor, páginas lidas, status (lendo/concluído) | Filtro "Lendo / Concluídos" |
| Empreendedor | Banco de Ideias de Produto | ideia, problema, público, estágio (ideia/teste/descartada) | Filtro por estágio |

O professor registra **as próprias leituras**, nunca dados de alunos.

### Atividade Integradora — Ciclo completo em novo aplicativo (10 min)

1. Preencher a ficha de requisitos (Anexo B) para o aplicativo do perfil.
2. Criar um novo projeto e, em **Plan**, pedir em um único plano a interface, o login por e-mail e
   senha, a tabela e as regras RLS; ler e aprovar.
3. Executar em **Build**.
4. Criar duas contas fictícias e realizar o teste de isolamento.
5. Conferir a varredura e publicar.

### Pílula Hands-on — Iteração e republicação (6 min)

1. Marcar um Bookmark da versão publicada em `History` **[conferir]**.
2. Pedir, em **Build**, apenas o filtro da tabela acima, sem alterar login nem dados.
3. Testar o filtro na prévia.
4. Usar `Publish > Publish changes` e conferir o filtro no endereço público, em janela anônima.

### Avaliação — Critérios de avaliação (4 min)

| Critério | Atendido? |
|---|---|
| Ficha de requisitos preenchida, com "fora do escopo" e critérios de pronto | |
| Somente dados fictícios; nenhum dado de terceiros | |
| Plano lido e aprovado antes do Build | |
| Teste com duas contas: cada uma vê apenas os próprios registros | |
| Varredura revisada antes de publicar | |
| Endereço público abre na tela de login | |
| Filtro funcionando no endereço público após `Publish changes` | |

> Nota de custo: a atividade consome, em estimativa não garantida pelo fabricante, de 3 a 5 créditos
> (uma mensagem em Plan, uma ou duas construções e a iteração). Recomenda-se realizá-la num dia em que
> nenhum outro crédito tenha sido usado.

## Descrição

- **Objetivos da Aula:** integrar especificação, segurança, construção em camadas, teste de
  isolamento, publicação e iteração num ciclo único aplicado ao perfil do participante.
- **Habilidades Esperadas:** construir, publicar e iterar sozinho um aplicativo web simples com login
  e banco de dados, comprovando o controle de acesso por usuário.

---

## Encerramento

Concluído o percurso, o participante dispõe de um método para construir aplicativos web por linguagem
natural sem abrir mão da inspeção: especificar antes de pedir, proteger dados e segredos, construir
em camadas, comprovar quem vê o quê, publicar e iterar com mudanças mínimas. Recomenda-se praticá-lo
regularmente em projetos pessoais com dados fictícios, observando o consumo de créditos e mantendo o
hábito de testar com duas contas antes de cada publicação.

Como caminhos de aprofundamento, indicam-se *Replit Agent - Essentials*, próximo curso da trilha, para
um ambiente de desenvolvimento mais amplo; *Lovable - Hands On*, para evoluir um aplicativo com
integrações; e os cursos de programação em editor (Cursor, Claude Code), para quem desejar ler e
revisar o código gerado. Projetos com dados reais, pagamentos ou uso institucional devem passar por
revisão profissional antes de entrar em produção.

> **Síntese:** *vibe coding* é encomendar a loja por descrição — mas quem abre as portas ao público
> responde por ela; por isso se inspeciona cada etapa, a começar por quem tem a chave de cada gaveta.

---

## Anexo A — Rótulos e caminhos do Lovable (ajuda em inglês, 18/10/2026)

| Função | Rótulo / caminho | Status |
|---|---|---|
| Criar conta | `lovable.dev > Sign up` | ajuda |
| Modos | `Chat` / `Plan` / `Build` (antigo "Agent mode") | ajuda |
| Editar texto na prévia | `Preview toolbar > Select elements` | ajuda; **[conferir]** |
| Visualização em celular | `Mobile view` | ajuda; **[conferir]** |
| Créditos | `More > Usage` | ajuda; **[conferir]** |
| Banco | `More > Cloud > Database` | ajuda; **[conferir]** |
| Usuários | `More > Cloud > Users > Add user` / `Auth settings` | ajuda; **[conferir]** |
| Segredos | `More > Cloud > Secrets` | ajuda; **[conferir]** |
| Histórico | `History` / `Revert` / `Bookmarks` (barra superior ou `Project > History`) | ajuda; **[conferir]** |
| Publicar | `Publish` / `Publish > Publish changes` | ajuda |
| Treinamento | `Account settings > Preferences > AI model training` | ajuda; **[conferir]** |
| Instruções persistentes | `Project settings > Knowledge` | ajuda; **[conferir]** |

## Anexo B — Ficha de requisitos

"""
Nome: Minhas Tarefas
Para quem: uma pessoa que quer organizar os próprios afazeres
Problema: anotar, concluir e remover tarefas
Ação principal: adicionar uma tarefa
Telas: login e lista de tarefas
Dados: título, concluída (sim/não), dono, data de criação
Regra de acesso: cada conta vê apenas os próprios registros
Fora do escopo: colaboração, anexos, pagamentos, notificações, dados reais
Visual: simples, alto contraste, legível no celular
Critérios de pronto: criar conta, entrar, criar tarefa, concluir, sair, entrar com outra conta e
não ver os dados da primeira
"""

## Anexo C — Checklist de prontidão para publicação

| Item | Atendido? |
|---|---|
| Nenhum segredo (senha, chave) no pedido ou na tela | |
| Somente dados fictícios | |
| Regras RLS por usuário criadas | |
| Teste com duas contas realizado e aprovado | |
| Resultado da varredura lido; nenhum achado crítico pendente | |
| Projeto mantido privado no workspace | |
| Dados de teste que não devem ficar públicos removidos | |

## Anexo D — Rastreabilidade da auditoria

| ID | Destino nesta versão |
|---|---|
| E1 | Módulo 4.1 (Lovable Cloud padrão; Supabase próprio como alternativa sem migração de um clique) |
| E2 | Módulo 1.1 e 3.1 (Chat/Plan/Build; "Agent mode" como nome antigo); Anexo A |
| E3 | Módulo 2 inteiro, antes do primeiro Build |
| E4 | Módulo 6 por perfil, com dados fictícios; Pílula do Módulo 2 classifica ideias com dados reais como inadequadas |
| E5 | Construção em camadas: interface (Módulo 3) → Plan e Build do back-end (Módulo 4) |
| E6 | Módulo 0 (créditos, `More > Usage`, rota de baixo consumo, três dias) |
| E7 | Módulo 5 (Publish, janela anônima, Publish changes) e Módulo 6 (republicação) |
| E8 | Módulo 4, Pílula de isolamento; critério de êxito obrigatório |
| E9 | Módulo 1 (analogia da loja e glossário), retomada nos Módulos 2–6 |
| E10 | Módulo 3 (quatro perguntas, ficha de requisitos, Plan) e Anexo B |
| E11 | Módulo 5 (uma mudança por vez, descrição de erro, History/Revert e limite) |
| E12 | Textos de 3 a 5 parágrafos; 129 min pela MET |
| E13 | Módulo 5.1 (limites, estudos de 2026, dependência) e Encerramento |
| E14 | Módulo 1.2 (Plinq e Elora, com ressalva; ausência de caso de professor) |
| E15 | Módulo 4 (Database e Users como pontos de controle) |
| E16 | Pílula do Módulo 1 com distratores e fundamentação |
| E17 | Módulo 5.1 e Encerramento (alternativas em uma frase) |
| E18 | Nota de vigência e Anexo A |

Decisão consciente: browser testing do Lovable, Knowledge e GitHub sync não ganharam exercício próprio
— consomem créditos ou ampliam o escopo além de 130 min; aparecem como menção (GitHub) ou ficam para
*Lovable - Hands On*.
