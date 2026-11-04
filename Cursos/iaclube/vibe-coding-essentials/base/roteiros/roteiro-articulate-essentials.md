# Plano de Aula — Vibe Coding com Lovable (Essentials)

> *» IA: Bloco Cover — título do curso verbatim; subtítulo: "Construir aplicativos web por linguagem natural: especificar, proteger, construir, testar, publicar e iterar". Não traduzir "Lovable", "vibe coding" nem os rótulos de interface.*

## Identificação

> *» IA: Bloco Table — tabela de identificação verbatim, duas colunas.*

| Campo | Definição |
|---|---|
| Curso | Vibe Coding - Essentials |
| Natureza | Curto, introdutório, autoinstrucional |
| Carga horária | 129 minutos, recomendados em três sessões em dias distintos |
| Público-alvo | Não programadores com ideias de produto, empreendedores e professores |
| Pré-requisitos | Uso básico de um assistente de IA; nenhum conhecimento de programação |
| Recursos necessários | Computador com navegador atualizado e internet ativa; conta gratuita no Lovable (`lovable.dev`), mediante e-mail, Google, GitHub ou Apple; 18 anos ou autorização de responsável. O plano gratuito oferece 5 créditos de construção por dia (teto de 30 por mês); o fabricante não garante que todo o percurso caiba no gratuito |

> *» IA: Bloco Statement — nota de vigência, verbatim; preservar o emoji.*

> 📌 Planos, créditos e rótulos de interface foram extraídos da documentação oficial do Lovable consultada em 18/10/2026, disponível em inglês. O Lovable altera nomes e limites com frequência (o modo "Agent" passou a chamar-se "Build" em 2026). Os rótulos são mantidos em inglês; itens marcados com [conferir] devem ser validados antes da publicação.

### Objetivo Geral

> *» IA: Bloco Text — parágrafo verbatim.*

O curso tem por finalidade capacitar o participante a construir aplicações web por linguagem natural — prática denominada vibe coding — com o Lovable, especificando o aplicativo antes de pedi-lo, gerando-o em etapas, acrescentando banco de dados e autenticação com controle de acesso por usuário, publicando-o, iterando-o com segurança e reconhecendo os limites do método. Ao final, o participante terá publicado o aplicativo "Minhas Tarefas", com login e banco de dados, comprovado por teste com duas contas fictícias que cada usuário vê apenas os próprios registros, e, na atividade integradora, aplicado o mesmo ciclo a um aplicativo do próprio perfil (professor ou empreendedor).

### Competências a Desenvolver

> *» IA: Bloco List (numerada) — verbatim, sem acréscimos.*

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Explicar o que é vibe coding e as partes de um aplicativo web com vocabulário correto.
2. Avaliar, antes de construir, os riscos de dados, segredos e custo de um aplicativo.
3. Especificar um aplicativo e gerar um primeiro protótipo de interface em camadas.
4. Acrescentar login e banco de dados e comprovar o controle de acesso por usuário.
5. Publicar, iterar com mudanças mínimas e reconhecer quando o método não basta.

### Estrutura e Sequência dos Módulos

> *» IA: Bloco Text para o parágrafo; Bloco Table para a tabela, verbatim.*

Os módulos obedecem a uma progressão cumulativa: verifica-se o acesso, compreende-se o método e o vocabulário, estabelecem-se os critérios de segurança antes do primeiro pedido e, então, especifica-se e constrói-se o aplicativo em camadas, testa-se o isolamento entre usuários, publica-se e itera-se, até a aplicação integrada ao perfil do participante. O aplicativo "Minhas Tarefas" acompanha os Módulos 3 a 5; a analogia da loja, plantada no Módulo 1, conduz todo o percurso.

| Módulo | Título | Referência | Tempo |
|---|---|---|---|
| 0 | Preparação e Verificação Inicial | Lovable: criar conta; preços (18/10/2026) | 7 min |
| 1 | O que é vibe coding e como funciona um aplicativo web | Karpathy (fev. 2025); Collins; documentação Lovable; casos da fabricante | 25 min |
| 2 | Segurança, Dados e Custos antes de Construir | Lovable: Security, Secrets, Data opt-out; nota de incidente (2026); LGPD; guia ANPD | 21 min |
| 3 | Especificar e gerar o primeiro protótipo | Lovable: Prompting best practices; modos Chat, Plan, Build | 16 min |
| 4 | Banco de dados, login e controle de acesso | Lovable: Cloud, Database, Authentication | 22 min |
| 5 | Publicar, iterar e reconhecer limites | Lovable: Publish, History; estudos acadêmicos de 2026 | 18 min |
| 6 | Síntese e Aplicação Integrada | Módulos 0 a 5 | 20 min |

---

# Módulo 0 — Preparação e Verificação Inicial

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 0" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> *» IA: Bloco Statement — nota de encadeamento, verbatim.*

> Ponto de partida: módulo de pré-filtro, anterior a qualquer construção.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Criar a conta gratuita no Lovable e localizar os modos de trabalho.
2. Explicar o que é um crédito e o que o plano gratuito oferece.
3. Consultar o saldo de créditos antes de cada etapa.
4. Reconhecer os rótulos da interface em inglês.

### Texto Descritivo

> *» IA: Bloco Text — dividir em blocos menores se necessário; não resumir.*

O Lovable é utilizado pelo navegador, sem instalação, no endereço `lovable.dev`. Existem aplicativos para Windows, macOS, iOS (15 ou posterior) e Android (9 ou posterior), mas a própria documentação os apresenta como complemento; as instruções deste curso referem-se à versão web. A conta gratuita é criada com e-mail e senha, Conta Google, GitHub ou Apple, e a documentação exige 18 anos ou autorização de responsável. Ao criar a conta, o usuário recebe um espaço de trabalho pessoal (personal workspace).

O plano gratuito é suficiente para as atividades, desde que se respeite a rota de baixo consumo descrita a seguir.

> *» IA: Bloco Table — planos verbatim.*

| Plano | Preço (página oficial, 18/10/2026) | O que inclui, em síntese |
|---|---|---|
| Free | US$ 0 | 5 build credits por dia (teto de 30 por mês); 20 Cloud credits/mês; 4 AI credits/mês; projetos privados; publicação em `lovable.app`; sincronização com GitHub |
| Pro | a partir de US$ 25/mês (100 créditos) | Domínio próprio, editor e download de código, mais créditos |
| Business | a partir de US$ 50/mês | Controles corporativos; dados excluídos do treinamento por padrão |

> *» IA: Bloco Text — verbatim.*

Cumpre compreender o que é um crédito: a unidade de cobrança de cada alteração feita pela IA. O custo não é fixo — a página de preços exemplifica que mudar a cor de um botão pode custar 0,50 crédito e adicionar autenticação, 1,20. Uma mensagem no modo Plan custa 1 crédito. O fabricante não garante que um aplicativo completo caiba no plano gratuito; por isso, o curso adota uma rota de baixo consumo (uma página principal, login por e-mail e senha, uma tabela, nenhuma integração externa, nenhuma imagem gerada, poucas iterações) e distribui as construções em três dias. Preços em reais não são publicados; estudantes e professores com e-mail acadêmico elegível têm desconto no Pro.

Convém, por fim, registrar que a documentação do Lovable está em inglês e não há confirmação oficial de que a interface esteja traduzida. Os rótulos são, por isso, mantidos em inglês. Os pedidos à IA, porém, podem ser escritos em português.

### Exercício Prático

> *» IA: Bloco Process — título com tempo e passos verbatim; preservar os breadcrumbs; não traduzir termos de interface.*

**Verificação de acesso (7 min)**

1. Acessar `lovable.dev > Sign up` e criar a conta gratuita (ou entrar na existente).
2. Localizar a caixa de prompt e o seletor de modo (`Chat` / `Plan` / `Build`) [conferir], sem enviar pedido.
3. Abrir `Lovable > More > Usage` [conferir] e anotar os créditos disponíveis no dia e no mês.
4. Preencher o registro de verificação da seção "Mão na massa".

> *» IA: Bloco Statement — critério e ponto de controle; preservar o emoji e o breadcrumb.*

**Critério de êxito:** conta ativa, seletor de modo localizado e saldo de créditos anotado.

> 🏁 Ponto de controle: em `Lovable > More > Usage`, o saldo de créditos do dia está visível e anotado.

> *» IA: Bloco Table — solução de problemas verbatim.*

| Situação | Procedimento |
|---|---|
| O seletor mostra "Agent" em vez de "Build" | Tratar "Agent" como o atual "Build"; registrar a divergência |
| Não aparece `More > Usage` | Procurar indicação de créditos no menu da conta ou do workspace [conferir] |
| Créditos do dia zerados ao começar | Aguardar a renovação diária antes do Módulo 3 |

### Mão na massa

> *» IA: Bloco Statement — modelo editável verbatim, entre aspas triplas.*

"""
Data da verificação: [dd/mm/aaaa]
Forma de login: [e-mail | Google | GitHub | Apple]
Plano: [Free | outro]
Idioma da interface: [inglês | português | misto]
Modos vistos no seletor: [ex.: Chat, Plan, Build]
Créditos disponíveis hoje / no mês (More > Usage): [valores]
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 0" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 1 — O que é vibe coding e como funciona um aplicativo web

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> *» IA: Bloco Statement — nota de encadeamento, verbatim.*

> Pressupõe o acesso verificado no Módulo 0; introduz o método e o vocabulário do curso.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Definir vibe coding, com sua origem, e distingui-lo de no-code e de programação assistida por IA.
2. Descrever os três modos de trabalho do Lovable.
3. Explicar front-end, back-end, banco de dados, autenticação, autorização e publicação pela analogia da loja.
4. Classificar uma prática de construção de software e justificar a classificação.

### Texto Descritivo

> *» IA: Bloco Text — dividir em blocos menores se necessário; não resumir.*

Denomina-se vibe coding a criação de software por meio da descrição, em linguagem natural, do resultado desejado, aceitando-se em grande parte o código produzido pela inteligência artificial. O termo foi popularizado por Andrej Karpathy, pesquisador de IA, em fevereiro de 2025, e escolhido palavra do ano de 2025 pelo dicionário Collins. Em sentido estrito, admite aceitar o código sem examiná-lo em detalhe — característica que o distingue da programação assistida por IA, na qual o programador continua lendo e compreendendo o código.

Convém distinguir, ainda, vibe coding de no-code e low-code. No-code designa ferramentas em que a aplicação é montada com componentes visuais, arrastando blocos; low-code mistura essa montagem com algum código. Vibe coding parte da linguagem natural. A fronteira não é absoluta — o Lovable oferece conversa, edição visual e acesso ao código —, mas, para os fins do curso, "vibe coding" descreve o método de trabalho e "no-code/low-code", o tipo de interface.

O Lovable, ferramenta deste curso, é uma plataforma lançada em 18 de novembro de 2024, em Estocolmo, que gera a partir de conversa uma aplicação web completa — interface, lógica, banco de dados, autenticação e hospedagem — e a publica num endereço terminado em `lovable.app`. Trabalha em três modos: Chat, que conversa e esclarece sem alterar o código; Plan, que propõe um plano e aguarda aprovação; e Build, que executa as alterações (chamado "Agent mode" em documentação anterior).

> *» IA: Bloco Statement — analogia do fio condutor, verbatim; preservar o emoji.*

> 🔑 Um aplicativo web assemelha-se a uma loja. O front-end é o salão: telas, botões e formulários que o cliente vê e toca no navegador. O back-end é o estoque e a administração, fora do alcance do cliente. O banco de dados é um conjunto de fichários: cada tabela é um fichário, cada linha uma ficha, cada coluna um campo. A autenticação é a catraca que confere quem entra; a autorização — no Lovable, uma regra do banco chamada RLS (Row Level Security, segurança por linha) — é o crachá que define quais gavetas cada pessoa abre. A publicação abre as portas ao público; a prévia é apenas o ensaio. Vibe coding equivale a encomendar a loja a uma equipe de obra por descrição: a velocidade aumenta, mas a inspeção continua necessária.

> *» IA: Bloco Table — glossário verbatim (alternativa: Accordion, um termo por item).*

| Termo | Definição | Na loja | No "Minhas Tarefas" |
|---|---|---|---|
| Front-end | Parte que roda no navegador | Salão e vitrine | Tela com a lista e o botão Adicionar |
| Back-end | Parte de servidor: regras, segredos, banco | Estoque e administração | Lovable Cloud |
| Banco de dados | Estrutura que guarda registros | Fichários | Tabela `tasks` |
| Autenticação | Verificar quem é o usuário | Catraca | Login por e-mail e senha |
| Autorização / RLS | Definir o que cada usuário pode ler ou alterar | Crachá que abre certas gavetas | Cada conta vê só as próprias tarefas |
| Publicação | Colocar uma versão em endereço público | Abrir as portas | Endereço `lovable.app` |
| Domínio | Nome do endereço | Endereço da loja | Subdomínio gratuito `lovable.app` |
| Segredo (secret) | Valor sensível, como chave de API | Combinação do cofre | Não usado no curso |
| Repositório | Pasta de código com histórico | Arquivo de plantas | GitHub (opcional) |

> *» IA: Bloco Text — verbatim.*

O Lovable divulga casos de não programadores: o Plinq, aplicativo brasileiro de segurança para mulheres criado por uma fundadora sem formação técnica, e o Elora, criado por um especialista em saúde em cerca de um mês. Cumpre registrar que são histórias publicadas pela própria fabricante, com números não auditados; não foi localizado caso independente e verificável de professor brasileiro.

### Exercício Prático

> *» IA: Bloco Knowledge Check — questão de múltipla escolha, alternativas e feedback verbatim.*

**Distinção entre métodos (4 min)**

Uma professora descreve em português, numa caixa de texto, um aplicativo de registro de leituras; a ferramenta gera telas, banco e login, e ela ajusta o resultado por novos pedidos, sem abrir o código. Classifica-se a prática como:

a) no-code, porque ela não escreveu código;
b) programação assistida por IA, porque uma IA escreveu o código;
c) vibe coding, porque o aplicativo foi construído a partir de descrições em linguagem natural, aceitando-se o código gerado;
d) low-code, porque houve banco de dados.

> *» IA: Bloco Statement — gabarito e fundamentação, verbatim.*

**Gabarito:** c. **Fundamentação:** não escrever código não basta para caracterizar no-code, que pressupõe montagem por componentes visuais (a); programação assistida pressupõe que a pessoa revise o código (b); a presença de banco de dados não define o método (d).

### Mão na massa

> *» IA: Bloco Statement — modelo editável verbatim, entre aspas triplas.*

Modelo para descrever uma ideia de aplicativo com o vocabulário da loja, antes de qualquer pedido:

"""
Ideia de aplicativo: [uma frase]
Salão (o que o usuário vê e faz): [telas e ação principal]
Fichários (o que precisa ser guardado): [campos]
Catraca (quem precisa entrar com login?): [sim/não; quem]
Crachás (quem pode ver o quê?): [regra de acesso]
Abrir as portas (quem vai usar o endereço público?): [público]
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 2 — Segurança, Dados e Custos antes de Construir

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> *» IA: Bloco Statement — nota de encadeamento, verbatim.*

> Pressupõe o vocabulário do Módulo 1; desloca o foco para os riscos, antes do primeiro pedido de construção.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Explicar por que o front-end é inspecionável e onde ficam os segredos.
2. Explicar o papel da RLS e o limite da varredura de segurança do Lovable.
3. Aplicar a regra de dados fictícios à luz da LGPD.
4. Configurar a recusa ao uso dos dados para treinamento.

### Texto Descritivo

> *» IA: Bloco Text — dividir em blocos menores se necessário; não resumir.*

Retomando a analogia: tudo o que está no salão da loja pode ser visto e tocado pelo cliente. Do mesmo modo, tudo o que vai para o front-end pode ser inspecionado e manipulado por qualquer usuário com as ferramentas comuns do navegador. Decorre daí a primeira regra: chaves secretas, senhas e regras sensíveis nunca ficam no front-end — nem no texto do pedido à IA. No Lovable, valores sensíveis são guardados em `More > Cloud > Secrets`, criptografados, e usados apenas pelo servidor. O curso não utiliza segredos; a regra é apresentada para que nenhum seja digitado por engano.

A segunda regra é que esconder um dado da tela não o protege. Se o banco não tiver regra de acesso por usuário (RLS), qualquer pessoa autenticada pode, em tese, ler os registros de outra, ainda que a interface não os mostre. O curso exige, no Módulo 4, um teste com duas contas para comprovar o isolamento. A ferramenta executa uma varredura rápida de segurança a cada publicação, mas a própria documentação adverte que essas ferramentas "não substituem uma revisão completa de segurança", e a opção de bloquear publicações com achados críticos pode estar desativada.

> *» IA: Bloco Statement — caso real, verbatim; preservar o emoji.*

> ⚠️ A Lovable divulgou que, entre 3 de fevereiro e 20 de abril de 2026, uma falha permitiu que usuários autenticados com o link de certos projetos públicos acessassem o histórico de conversa e o código-fonte; a empresa informou correção e que projetos privados e o Lovable Cloud não foram afetados.

> *» IA: Bloco Text — verbatim.*

Artigos acadêmicos de 2026 sintetizam as falhas recorrentes em aplicativos criados por vibe coding: autenticação e autorização inadequadas, segredos expostos e código aceito sem revisão.

Quanto aos dados, a Lei Geral de Proteção de Dados (LGPD) rege o tratamento de dados pessoais no Brasil, com princípios como finalidade, necessidade e segurança, e a ANPD orienta agentes de pequeno porte a adotar medidas técnicas e administrativas de segurança. Para um curso introdutório, a consequência é simples: somente dados fictícios. Nenhum nome real, CPF, endereço, dado de saúde, nota escolar, dado de criança ou credencial real entra no aplicativo, nem no pedido à IA. Um protótipo educacional não deve converter-se em sistema de produção sem análise de base legal, transparência, contratos, retenção e segurança.

Registra-se, ainda, que, desde 9 de setembro de 2026, os dados de clientes dos planos Free e Pro podem ser usados para treinar os modelos da Lovable, com possibilidade de recusa; os planos Business e Enterprise ficam excluídos por padrão. Segundo a documentação, os dados dos usuários finais guardados no banco do aplicativo não são usados nesse treinamento. Recomenda-se, também, manter o projeto privado durante o curso. Por fim, o custo: um pedido amplo pode consumir a cota diária e gerar um aplicativo difícil de entender; alterações pequenas são, ao mesmo tempo, mais baratas e mais fáceis de conferir.

### Exercício Prático

> *» IA: Bloco Process — título com tempo e passos verbatim; preservar os breadcrumbs.*

**Configuração e triagem de ideias (6 min)**

1. Abrir `Lovable > Account settings > Preferences > AI model training` [conferir] e decidir, de modo informado, sobre a recusa ao treinamento; registrar a escolha.
2. Classificar cada ideia de aplicativo como adequada ao curso, adequada com ajuste (indicar qual) ou inadequada:
   1. Lista pessoal de tarefas com login, dados inventados.
   2. Controle de notas da turma real, com nomes dos alunos.
   3. Catálogo de produtos fictícios com área de administração.
   4. Cadastro de clientes com CPF e telefone, para uso imediato na empresa.

> *» IA: Bloco Statement — gabarito, critério e ponto de controle; preservar o emoji e o breadcrumb.*

**Gabarito:** (1) adequada. (2) inadequada — dados pessoais de alunos, possivelmente menores; ajuste possível: turma inventada e nomes fictícios, deixando explícito que não é sistema real. (3) adequada, sem pagamentos. (4) inadequada — dados pessoais reais e uso em produção sem análise de LGPD e segurança.

**Critério de êxito:** escolha sobre treinamento registrada; quatro classificações coincidem com o gabarito.

> 🏁 Ponto de controle: em `Lovable > Account settings > Preferences > AI model training` [conferir], a opção está no estado escolhido pelo participante.

### Mão na massa

> *» IA: Bloco Statement — modelo editável verbatim, entre aspas triplas.*

"""
Ideia de aplicativo: [uma frase]
Há dados pessoais reais? [não | sim: quais — substituir por fictícios]
Há senha, chave ou segredo no pedido? [não | sim — remover]
Quem poderá acessar o endereço público? [descrever]
Regra de acesso por usuário necessária? [sim | não]
Decisão: [adequada | adequada com ajuste: qual | inadequada]
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 3 — Especificar e gerar o primeiro protótipo

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> *» IA: Bloco Statement — nota de encadeamento, verbatim.*

> Pressupõe os critérios de segurança; desloca o foco para a especificação e a primeira construção.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Preencher uma ficha de requisitos a partir das quatro perguntas oficiais.
2. Escolher entre os modos Chat, Plan e Build conforme a alteração pretendida.
3. Gerar uma interface sem back-end e conferi-la em computador e celular.

### Texto Descritivo

> *» IA: Bloco Text — verbatim.*

Retomando a analogia, ninguém encomenda uma loja sem planta. A documentação do Lovable recomenda responder, antes de construir, a quatro perguntas: o que será criado, para quem, por quê e qual é a ação principal. Recomenda, ainda, mapear a jornada do usuário, trabalhar por partes e fazer uma mudança por vez, conferindo o resultado antes da seguinte. A ficha de requisitos organiza essas respostas e acrescenta dados, regra de acesso, o que fica fora do escopo e critérios de pronto.

A escolha do modo também importa. O Chat serve para esclarecer uma dúvida sem alterar nada; o Plan pesquisa o projeto, propõe um plano e espera aprovação, ao custo de 1 crédito por mensagem; o Build executa. Recomenda-se, para mudanças grandes, planejar antes de construir. Para mudanças de texto, a barra da prévia (`Preview toolbar > Select elements`) permite editar diretamente, dentro de uma franquia diária, sem gastar créditos de construção.

A estratégia do curso é construir em camadas: primeiro só a interface, sem banco nem login; em seguida, no Módulo 4, o back-end. Essa separação reduz o custo de cada pedido, torna cada resultado conferível e evita o padrão conhecido de pedir tudo de uma vez e receber um aplicativo que ninguém consegue depurar.

> *» IA: Bloco Statement — ficha de requisitos verbatim, entre aspas triplas.*

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
Critérios de pronto: criar conta, entrar, criar tarefa, concluir, sair, entrar com outra conta e não ver os dados da primeira
"""

### Exercício Prático

> *» IA: Bloco Process — título com tempo e passos verbatim; preservar os breadcrumbs; não traduzir termos de interface.*

**Ficha de requisitos, primeiro Build e conferência (10 min)**

1. Revisar a ficha de requisitos de "Minhas Tarefas" acima.
2. Anotar o saldo em `Lovable > More > Usage` [conferir].
3. Selecionar o modo `Build`, colar o prompt-base da seção "Mão na massa" e enviar.
4. Aguardar a primeira versão na prévia, à direita do editor.
5. Alternar para `Preview toolbar > Mobile view` [conferir] e conferir a legibilidade.
6. Conferir o protótipo pela tabela de critérios.

> *» IA: Bloco Checklist — critérios verbatim.*

| Critério | Atendido? |
|---|---|
| A prévia mostra cabeçalho, campo de título e botão Adicionar | |
| Há mensagem de lista vazia | |
| Em Mobile view, os elementos continuam legíveis | |
| Não foram criados banco de dados nem login | |
| Crédito consumido anotado | |

> *» IA: Bloco Statement — critério e observação, verbatim; preservar o emoji e o breadcrumb.*

**Critério de êxito:** os cinco itens marcados. O botão pode ainda não guardar as tarefas ao recarregar a página: isso é esperado e será resolvido no Módulo 4.

> 🏁 Ponto de controle: no editor do Lovable, a prévia exibe o "Minhas Tarefas" sem tela de login; em `History` [conferir], há uma única versão nova.

> *» IA: Bloco Table — solução de problemas verbatim; preservar os breadcrumbs.*

| Situação | Procedimento |
|---|---|
| O Lovable criou login ou banco mesmo assim | `History > Revert` para a versão anterior; reenviar com "não adicione banco nem login" em linha própria |
| Texto do botão saiu diferente | Corrigir em `Preview toolbar > Select elements`, sem gastar crédito de construção |
| Créditos insuficientes | Aguardar a renovação no dia seguinte |

### Mão na massa

> *» IA: Bloco Statement — modelo editável verbatim, entre aspas triplas.*

"""
Crie um aplicativo web chamado Minhas Tarefas. Por enquanto, faça só a interface: cabeçalho, campo para o título da tarefa, botão Adicionar, lista de tarefas e uma mensagem quando a lista estiver vazia. Visual simples, alto contraste, legível no celular, em português do Brasil.
Não adicione banco de dados nem login ainda.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 4 — Banco de dados, login e controle de acesso

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> *» IA: Bloco Statement — nota de encadeamento, verbatim.*

> Pressupõe o protótipo de interface; desloca o foco para o back-end.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Explicar o que é o Lovable Cloud e por que dispensa conta própria no Supabase.
2. Acrescentar login e banco de dados pelo fluxo Plan, aprovação e Build.
3. Conferir tabelas e usuários na administração do Lovable Cloud.
4. Comprovar, com duas contas, que cada usuário vê apenas os próprios registros.

### Texto Descritivo

> *» IA: Bloco Text — dividir em blocos menores se necessário; não resumir.*

O back-end padrão do Lovable é o Lovable Cloud, construído sobre a base de código aberto do Supabase e ativado pelo próprio Lovable quando um pedido exige banco de dados ou login — às vezes solicitando aprovação. Não é preciso criar conta no Supabase: a documentação responde literalmente "Do I need Supabase? No." Conectar um projeto Supabase próprio é alternativa para quem já o possui, mas não há migração de um clique entre as duas opções, razão pela qual se recomenda decidir no início e, neste curso, permanecer no Lovable Cloud.

Retomando a analogia, este módulo instala a catraca e as gavetas com crachá. O pedido é feito em duas etapas. Primeiro, no modo Plan, pede-se a menor alteração possível para acrescentar login por e-mail e senha e uma tabela de tarefas em que cada usuário acesse apenas as próprias, com regras RLS e a descrição de como testar com duas contas; o plano é lido e aprovado. Depois, no modo Build, aplica-se o plano. Especifica-se "e-mail e senha" porque, sem essa indicação, o Lovable pode gerar outras formas de entrada, o que amplia o escopo.

Concluída a construção, confere-se o resultado na administração da loja: `More > Cloud > Database` mostra as tabelas e permite ver, adicionar, excluir e exportar linhas; `More > Cloud > Users` lista as contas e oferece Add user e Auth settings. Uma tarefa criada pela tela deve aparecer como linha na tabela.

> *» IA: Bloco Statement — aviso, verbatim; preservar o emoji.*

> ⚠️ Excluir linhas pela interface do banco é irreversível, e reverter o código (Módulo 5) não recupera dados apagados.

> *» IA: Bloco Text — verbatim.*

O teste decisivo é o de isolamento: duas contas fictícias, cada uma com uma tarefa; cada conta deve ver apenas a sua. É esse teste — e não a aparência da tela — que comprova que as gavetas estão trancadas. Para criar as contas sem depender de confirmação por e-mail, pode-se usar `More > Cloud > Users > Add user` [conferir], com endereços fictícios.

### Exercício Prático

> *» IA: Bloco Process — título com tempo e passos verbatim; preservar os breadcrumbs; não traduzir termos de interface.*

**Back-end e teste de isolamento (12 min)**

1. Anotar o saldo de créditos.
2. Selecionar `Plan`, enviar a primeira parte do prompt-base da seção "Mão na massa" e ler o plano: ele menciona e-mail e senha, a tabela e RLS?
3. Aprovar e, em `Build`, enviar a segunda parte. Se o Lovable pedir para ativar o Lovable Cloud, aprovar.
4. Abrir `Lovable > More > Cloud > Database` [conferir] e confirmar a tabela `tasks`.
5. Em `Lovable > More > Cloud > Users > Add user` [conferir], criar `teste.a@exemplo.com` e `teste.b@exemplo.com`, com senhas de teste anotadas fora do Lovable.
6. Na prévia, entrar com a conta A, criar "Tarefa da conta A" e sair; entrar com a conta B, criar "Tarefa da conta B" e verificar a lista.
7. Recarregar a página e conferir que a tarefa permanece.

> *» IA: Bloco Statement — critério e ponto de controle; preservar o emoji e o breadcrumb.*

**Critério de êxito:** a conta B vê apenas a própria tarefa; a tarefa persiste após recarregar; a tabela mostra duas linhas de donos distintos.

> 🏁 Ponto de controle: em `Lovable > More > Cloud > Database > tasks` [conferir], há duas linhas com valores diferentes na coluna `user_id`.

> *» IA: Bloco Table — solução de problemas verbatim; preservar os breadcrumbs.*

| Situação | Procedimento |
|---|---|
| A conta B vê a tarefa da conta A | Tratar como falha de segurança: não publicar; pedir em Plan "investigue por que a conta B vê tarefas da conta A e proponha a correção das políticas RLS"; repetir o teste |
| Login não funciona | Conferir `More > Cloud > Users` e `Auth settings`; copiar a mensagem exata e pedir investigação em Plan antes de corrigir |
| "Add user" não aparece | Criar as contas pela tela de cadastro do próprio app, com e-mails que o participante controle |

### Mão na massa

> *» IA: Bloco Statement — modelo editável verbatim, entre aspas triplas; manter os nomes de colunas sem alteração.*

"""
[Modo Plan]
Analise o app e proponha a menor alteração possível para adicionar autenticação por e-mail e senha e uma tabela de tarefas. Cada usuário deve acessar apenas as próprias tarefas. Inclua regras RLS e descreva como testar com duas contas. Não implemente até eu aprovar.

[Modo Build, após aprovar]
Aplique o plano aprovado. Adicione login por e-mail e senha, logout e uma tabela tasks com title, completed, user_id e created_at. Crie políticas RLS para que cada usuário só possa ler, criar, atualizar e excluir as próprias tarefas. Não altere o visual.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 5 — Publicar, iterar e reconhecer limites

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 5" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> *» IA: Bloco Statement — nota de encadeamento, verbatim.*

> Pressupõe o aplicativo com isolamento comprovado; desloca o foco para a publicação e a manutenção.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Distinguir prévia e publicação e republicar mudanças.
2. Descrever um erro de forma investigável e usar History, Bookmarks e Revert, conhecendo seu limite.
3. Publicar após a varredura e testar como visitante.
4. Identificar situações em que vibe coding não basta.

### Texto Descritivo

> *» IA: Bloco Text — dividir em blocos menores se necessário; não resumir.*

Retomando a analogia, a prévia é o ensaio; publicar é abrir as portas. No Lovable, `Publish`, no canto superior direito do editor, cria um retrato (snapshot) do projeto num endereço `[nome].lovable.app` e executa a varredura rápida de segurança. O ponto mais importante deste módulo é que a versão pública não acompanha a prévia: depois de qualquer mudança, é preciso usar `Publish > Publish changes`. Muitos "o site não atualizou" são apenas esquecimento desse passo. O teste da publicação faz-se em janela anônima do navegador, que simula um visitante sem login.

Reformar com a loja aberta exige método. A documentação recomenda uma mudança por pedido e, diante de um erro, descrevê-lo com precisão — o que acontece, onde, o que se esperava e o que se observou —, investigando a causa (no Chat ou no Plan) antes de corrigir. O History registra cada versão do código; Bookmarks marcam versões importantes; Revert volta a uma versão anterior. Revert, porém, restaura apenas o código: dados apagados do banco não voltam. Recomenda-se marcar um Bookmark antes de qualquer mudança arriscada.

Cumpre, por fim, reconhecer os limites do método. Estudos acadêmicos de 2026 associam vibe coding a prototipação rápida, mas também a código difícil de compreender, dívida técnica, falhas de segurança e manutenção custosa quando os resultados são aceitos sem revisão. O método não basta, isoladamente, quando o aplicativo envolve dinheiro, saúde, dados educacionais sensíveis, decisões de alto impacto, grandes volumes ou exigências regulatórias; nesses casos, são necessárias revisão profissional, testes e governança.

Há também dependência da plataforma: a sincronização com o GitHub, disponível no plano gratuito, guarda o código fora do Lovable, mas banco, segredos e operação ainda exigiriam planejamento para migrar — "ter o código" não equivale a "poder mudar de plataforma sem trabalho". Ferramentas como Replit Agent, Bolt e v0 seguem lógica semelhante e são estudadas em cursos próprios.

### Exercício Prático

> *» IA: Bloco Process — título com tempo e passos verbatim; preservar os breadcrumbs.*

**Publicação, teste público e prontidão (10 min)**

1. Clicar em `Lovable > Publish` [conferir] e ler o resultado da varredura antes de confirmar; havendo achado crítico sobre RLS, não publicar e voltar ao Módulo 4.
2. Revisar o endereço sugerido e confirmar.
3. Abrir o endereço em janela anônima: a tela de login deve aparecer.
4. Entrar com a conta A e confirmar que apenas a tarefa da conta A é exibida.
5. Preencher o checklist de prontidão abaixo.

> *» IA: Bloco Checklist — checklist de prontidão verbatim.*

| Item | Atendido? |
|---|---|
| Nenhum segredo (senha, chave) no pedido ou na tela | |
| Somente dados fictícios | |
| Regras RLS por usuário criadas | |
| Teste com duas contas realizado e aprovado | |
| Resultado da varredura lido; nenhum achado crítico pendente | |
| Projeto mantido privado no workspace | |
| Dados de teste que não devem ficar públicos removidos | |

> *» IA: Bloco Statement — critério e ponto de controle; preservar o emoji e o breadcrumb.*

**Critério de êxito:** endereço público abre na tela de login; a conta A vê apenas a própria tarefa; checklist integralmente marcado.

> 🏁 Ponto de controle: em janela anônima, o endereço `[nome].lovable.app` exibe a tela de login; em `Lovable > History` [conferir], a versão aparece como publicada.

> *» IA: Bloco Table — solução de problemas verbatim; preservar os breadcrumbs.*

| Situação | Procedimento |
|---|---|
| A mudança não aparece no endereço público | `Publish > Publish changes` |
| A varredura aponta problema de RLS | Não publicar; corrigir conforme o Módulo 4 e repetir o teste de isolamento |
| Um pedido grande alterou várias partes | `History > Revert` para a versão anterior e refazer em partes menores |

### Mão na massa

> *» IA: Bloco Statement — modelo editável verbatim, entre aspas triplas.*

"""
O que acontece: [descrever]
Onde: [tela ou ação]
O que eu esperava: [descrever]
O que aconteceu: [descrever; colar a mensagem de erro, se houver]
Investigue a causa primeiro e me explique. Depois, altere apenas o necessário, sem mudar visual, login ou dados.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 5" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 6 — Síntese e Aplicação Integrada

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 6" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> *» IA: Bloco Statement — nota de encadeamento, verbatim.*

> Pressupõe os Módulos 1 a 5; articula especificar, proteger, construir, testar, publicar e iterar num único ciclo.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Conduzir o ciclo completo de vibe coding num aplicativo do próprio perfil.
2. Comprovar o controle de acesso por usuário no aplicativo publicado.
3. Iterar o aplicativo publicado e levar a mudança ao endereço público.

### Texto Descritivo

> *» IA: Bloco Text — verbatim.*

Os módulos anteriores compõem um ciclo aplicável a qualquer aplicativo simples: especificar com a ficha de requisitos (Módulo 3), verificar dados e segurança antes de construir (Módulo 2), construir em camadas, com Plan antes de Build (Módulos 3 e 4), comprovar o isolamento com duas contas (Módulo 4), publicar após a varredura e iterar com mudanças mínimas, republicando (Módulo 5). Na analogia, trata-se de encomendar, inspecionar, abrir e reformar uma segunda loja — agora projetada pelo próprio participante.

A atividade integradora é diferenciada por perfil, sempre com a mesma estrutura técnica (uma tabela, login, cada usuário vê apenas os próprios registros) e dados fictícios. O professor registra as próprias leituras, nunca dados de alunos.

> *» IA: Bloco Table — perfis verbatim (alternativa: Tabs, uma aba por perfil).*

| Perfil | Aplicativo | Dados da tabela | Iteração final |
|---|---|---|---|
| Professor | Diário de Leituras | título do livro, autor, páginas lidas, status (lendo/concluído) | Filtro "Lendo / Concluídos" |
| Empreendedor | Banco de Ideias de Produto | ideia, problema, público, estágio (ideia/teste/descartada) | Filtro por estágio |

### Exercício Prático

> *» IA: Bloco Process — atividade integradora, título com tempo e passos verbatim; preservar os breadcrumbs.*

**Atividade integradora — ciclo completo em novo aplicativo (16 min)**

1. Preencher a ficha de requisitos para o aplicativo do perfil (modelo do Módulo 3).
2. Criar um novo projeto e, em `Plan`, pedir em um único plano a interface, o login por e-mail e senha, a tabela e as regras RLS; ler e aprovar.
3. Executar em `Build`.
4. Criar duas contas fictícias em `More > Cloud > Users > Add user` [conferir] e realizar o teste de isolamento.
5. Conferir a varredura e publicar em `Publish`.
6. Marcar um Bookmark da versão publicada em `History` [conferir].
7. Pedir, em `Build`, apenas o filtro indicado na tabela, sem alterar login nem dados; testar na prévia.
8. Usar `Publish > Publish changes` e conferir o filtro no endereço público, em janela anônima.

> *» IA: Bloco Checklist — critérios de avaliação verbatim.*

| Critério | Atendido? |
|---|---|
| Ficha de requisitos preenchida, com "fora do escopo" e critérios de pronto | |
| Somente dados fictícios; nenhum dado de terceiros | |
| Plano lido e aprovado antes do Build | |
| Teste com duas contas: cada uma vê apenas os próprios registros | |
| Varredura revisada antes de publicar | |
| Endereço público abre na tela de login | |
| Filtro funcionando no endereço público após Publish changes | |

> *» IA: Bloco Statement — notas, verbatim; preservar os emojis e o breadcrumb.*

> 📌 A atividade consome, em estimativa não garantida pelo fabricante, de 3 a 5 créditos (uma mensagem em Plan, uma ou duas construções e a iteração). Recomenda-se realizá-la num dia em que nenhum outro crédito tenha sido usado.

> 🏁 Ponto de controle: em janela anônima, o endereço público do novo aplicativo abre na tela de login e, após o acesso, exibe o filtro; em `Lovable > History` [conferir], a versão com o filtro aparece como publicada.

### Mão na massa

> *» IA: Bloco Statement — modelo editável verbatim, entre aspas triplas.*

"""
[Modo Plan]
Quero criar o aplicativo [nome], para [quem], cuja ação principal é [ação]. Proponha um plano único com: interface simples em português do Brasil, login por e-mail e senha, uma tabela [nome_da_tabela] com os campos [campos] e user_id, e políticas RLS para que cada usuário só possa ler, criar, atualizar e excluir os próprios registros. Fora do escopo: [itens]. Descreva como testar com duas contas. Não implemente até eu aprovar.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 6" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Encerramento

> *» IA: Bloco Text — dois parágrafos verbatim.*

Concluído o percurso, o participante dispõe de um método para construir aplicativos web por linguagem natural sem abrir mão da inspeção: especificar antes de pedir, proteger dados e segredos, construir em camadas, comprovar quem vê o quê, publicar e iterar com mudanças mínimas. Recomenda-se praticá-lo regularmente em projetos pessoais com dados fictícios, observando o consumo de créditos e mantendo o hábito de testar com duas contas antes de cada publicação.

Como caminhos de aprofundamento, indicam-se Replit Agent - Essentials, próximo curso da trilha, para um ambiente de desenvolvimento mais amplo; Lovable - Hands On, para evoluir um aplicativo com integrações; e os cursos de programação em editor (Cursor, Claude Code), para quem desejar ler e revisar o código gerado. Projetos com dados reais, pagamentos ou uso institucional devem passar por revisão profissional antes de entrar em produção.

> *» IA: Bloco Statement — citação final verbatim.*

> **Síntese:** vibe coding é encomendar a loja por descrição — mas quem abre as portas ao público responde por ela; por isso se inspeciona cada etapa, a começar por quem tem a chave de cada gaveta.
