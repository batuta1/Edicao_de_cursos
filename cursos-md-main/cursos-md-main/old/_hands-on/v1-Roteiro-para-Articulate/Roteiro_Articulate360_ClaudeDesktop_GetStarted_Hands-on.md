<link rel="stylesheet" href="../../.css/style.css">

# Roteiro Articulate 360 — Claude Desktop: Get Started — Curso Hands-on

*Claude: Get Started with the Desktop App — Curso Hands-on*

---

## Identificação

| Campo | Definição |
|---|---|
| **Curso** | Claude Desktop: Get Started — Curso Hands-on |
| **Natureza** | Autoinstrucional, assíncrono, orientado à execução prática |
| **Plataforma de desenvolvimento** | Articulate 360 |
| **Ferramenta sugerida** | Rise 360 (estrutura principal) com blocos Storyline 360 embutidos para interações de knowledge check e cenários de decisão |
| **Carga horária** | 90 minutos |
| **Público-alvo** | Docentes do ensino superior iniciantes em Inteligência Artificial; analistas administrativos; alunos do ensino superior sem experiência prévia com ferramentas de IA |
| **Pré-requisitos** | Capacidade de navegar em sistema operacional Windows 10/11 ou macOS 12 ou superior; conta Anthropic criada; plano Pro, Max, Team ou Enterprise ativo |
| **Recursos necessários** | Computador com Windows 10/11 ou macOS 12+; conexão à internet; editor de texto simples (Bloco de Notas ou TextEdit); navegador atualizado |
| **Produto final do participante** | Pasta-projeto estruturada (`projeto-final-claude`) com `README.md`, `.gitignore` e arquivo de conteúdo; registro documentado de pelo menos um ciclo completo de uso do Claude Desktop (prompt → diff view → aceitar/rejeitar) |

---

## Objetivo Geral

O presente curso visa desenvolver, de forma exclusivamente prática, a competência operacional necessária para instalar, configurar e utilizar o aplicativo Claude Desktop em contextos acadêmicos e profissionais. Por meio de quatro módulos de execução progressiva e um módulo de síntese aplicada, o participante realizará, em ambiente real, as operações fundamentais da ferramenta: verificação de compatibilidade e instalação, reconhecimento das interfaces de trabalho, estruturação segura de projetos e formulação de solicitações eficazes. O produto final esperado é uma sessão de trabalho completa e documentada, na qual o participante demonstra domínio operacional do fluxo central do Claude Desktop, da abertura do projeto à revisão e aceitação de alterações propostas pelo assistente.

---

## Competências Práticas a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Verificar a compatibilidade do sistema operacional, selecionar o instalador correto, executar a instalação do Claude Desktop e confirmar o acesso autenticado às três interfaces do aplicativo.
2. Distinguir as interfaces Chat, Code e Cowork, selecionar a adequada a cada tipo de tarefa e executar operações básicas em cada uma delas.
3. Criar e configurar uma pasta-projeto com estrutura mínima segura — incluindo `README.md` e `.gitignore` —, identificando e protegendo arquivos sensíveis.
4. Redigir solicitações estruturadas segundo a fórmula Contexto–Tarefa–Limite–Formato, revisar alterações propostas pelo assistente por meio da diff view e registrar ou reverter mudanças de forma consciente.

---

## Estrutura Geral do Curso

O curso está organizado em quatro módulos práticos de execução progressiva, cada um resolvendo um problema concreto e entregando um produto parcial verificável. Os módulos constroem uns sobre os outros: o aplicativo instalado no Módulo 1 é utilizado no Módulo 2; a pasta-projeto criada no Módulo 3 é o ambiente de trabalho do Módulo 4; e os produtos parciais dos quatro módulos são integrados no Módulo 5, que simula uma sessão real de trabalho do início ao fim.

| Módulo | Foco prático | Produto parcial | Interação principal | Tempo |
|---|---|---|---|---|
| 1 | Verificação, download e instalação do Claude Desktop | Aplicativo instalado, autenticado e com as três abas acessíveis | Demonstração passo a passo + checklist de validação | 20 min |
| 2 | Reconhecimento e teste das três interfaces | Arquivo `projeto-teste.txt` lido pelo Claude na aba Code | Tabs comparativas + atividade guiada | 15 min |
| 3 | Estruturação de pasta-projeto segura | Pasta `meu-projeto-claude` com `README.md`, `.gitignore` e `.env` | Process block + knowledge check | 20 min |
| 4 | Formulação de prompts eficazes e revisão de resultados | Prompt forte aplicado ao projeto; diff view revisada; alteração aceita ou rejeitada | Cenário de decisão + atividade guiada | 20 min |
| 5 (Síntese) | Sessão de trabalho integrada do zero ao entregável | Pasta `projeto-final-claude` documentada com ciclo completo registrado | Checklist integradora + avaliação por critérios | 15 min |

---

<div style="page-break-after: always;"></div>

# Módulo 1 — Verificação do Ambiente e Instalação do Claude Desktop

## Encadeamento

Este é o ponto de partida do curso. Nenhum uso do aplicativo é possível sem que o ambiente esteja verificado e a instalação concluída com sucesso.

## Finalidade prática

Neste módulo, o participante verificará a compatibilidade do computador com o Claude Desktop, confirmará o plano de assinatura Anthropic ativo, realizará o download do instalador correto e concluirá a instalação com autenticação. O produto parcial é o aplicativo aberto, autenticado e com as três interfaces acessíveis.

## Objetivos de Aprendizagem Prática

Ao final deste módulo, o participante deverá ser capaz de:

1. Acessar as configurações do sistema operacional e identificar a versão e a arquitetura do processador do computador.
2. Verificar o plano de assinatura Anthropic ativo e confirmar se ele habilita o uso do Claude Desktop.
3. Selecionar o instalador compatível com o sistema identificado, executar a instalação e realizar o primeiro login.
4. Validar a instalação por meio de checklist, confirmando que as três interfaces — Chat, Code e Cowork — estão acessíveis.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 1.1 | Abertura do módulo | Título, enunciado do problema e lista de pré-requisitos do módulo | Ícone representando instalação de aplicativo |
| 1.2 | Texto curto explicativo | O que é o Claude Desktop e por que verificar compatibilidade antes de instalar | Nenhum — bloco de texto objetivo |
| 1.3 | Tabs | Duas abas: "Windows" e "macOS" — cada uma com o caminho para identificar versão e arquitetura | Capturas de tela anotadas: tela "Sobre o seu PC" (Windows) e "Sobre este Mac" (macOS) |
| 1.4 | Texto curto explicativo | Como verificar o plano de assinatura em claude.ai | Captura de tela da seção "Billing" do perfil |
| 1.5 | Labeled graphic | Diagrama de seleção de instalador: sistema × arquitetura → instalador correto | Tabela visual com quatro combinações e o instalador correspondente |
| 1.6 | Demonstração passo a passo | Sequência de instalação no Windows e no macOS, com variação por sistema | Capturas de tela anotadas: janela do instalador, janela de segurança, tela de conclusão |
| 1.7 | Demonstração passo a passo | Processo de login: abertura do navegador para verificação extra e retorno ao app | Captura de tela: tela inicial do Claude Desktop com as três abas visíveis |
| 1.8 | Checklist | Lista de verificação pós-instalação (cinco itens) — o participante marca cada item concluído | Nenhum — componente interativo de checklist |
| 1.9 | Knowledge check | Pergunta de múltipla escolha sobre seleção de instalador | Nenhum — componente de quiz |
| 1.10 | Fechamento do módulo | Resumo do produto parcial obtido e anúncio do próximo módulo | Ícone representando missão cumprida |

## Conteúdo Instrucional Enxuto

O Claude Desktop é a versão instalável do assistente Claude, desenvolvida pela Anthropic. A diferença fundamental entre o Claude Desktop e o acesso via navegador (claude.ai) reside na capacidade da versão instalada de ler e modificar arquivos armazenados localmente no computador — o que amplia o escopo de tarefas possíveis, mas exige que o ambiente esteja corretamente configurado antes do primeiro uso.

O aplicativo é compatível com Windows 10 e 11 (arquiteturas x64 e ARM64) e com macOS 12 ou superior (processadores Intel e Apple Silicon, como as linhas M1, M2 e M3). O uso de um instalador incompatível com a arquitetura do processador é a causa mais frequente de falha de inicialização. Portanto, a verificação do sistema operacional e da arquitetura do processador é obrigatória antes do download.

O acesso ao Claude Desktop requer, no mínimo, o plano Pro da Anthropic. O plano gratuito não inclui esse recurso. Recomenda-se verificar, junto à área de tecnologia da informação da instituição, se há acordos institucionais com a Anthropic que viabilizem o acesso sem custo adicional para docentes e discentes.

## Demonstração Guiada

**Windows — Verificação do sistema e instalação:**

1. Acessar *Configurações > Sistema > Sobre* e localizar os campos "Versão do Windows" e "Tipo de sistema" (x64 ou ARM64).
2. Acessar claude.ai, fazer login e verificar o plano ativo na seção de perfil ou faturamento (*Billing*).
3. Acessar o site da Anthropic, localizar a página de download do Claude Desktop e selecionar o instalador correspondente ao sistema identificado.
4. Executar o arquivo `.exe`, seguir o assistente de instalação (Próximo → Aceitar → Instalar) e aguardar a conclusão.
5. Abrir o aplicativo, realizar o login com as credenciais da conta Anthropic (o navegador será aberto para verificação adicional — isso é esperado) e confirmar que as três abas — Chat, Code e Cowork — estão visíveis.

*Captura de tela recomendada: tela inicial do Claude Desktop com as abas Chat, Code e Cowork destacadas — evidência de instalação e autenticação bem-sucedidas.*

**macOS — Variação de instalação:**

1. Acessar o menu Apple > *Sobre este Mac* e localizar o campo "Chip" (Apple Silicon) ou "Processador" (Intel).
2. Baixar o instalador `.dmg` correspondente.
3. Abrir o arquivo `.dmg`, arrastar o ícone do Claude para a pasta Aplicativos e aguardar a cópia.
4. Abrir o aplicativo pela pasta Aplicativos e realizar o login conforme descrito acima.

*Captura de tela recomendada: janela do macOS com o ícone do Claude sendo arrastado para Aplicativos.*

## Atividade Hands-on

### Atividade prática — Checklist de Verificação e Instalação (10 minutos)

**Tarefa:** Verificar a compatibilidade do computador, selecionar e baixar o instalador correto, concluir a instalação e validar o acesso às três interfaces do Claude Desktop.

**Procedimento:**

1. Acessar as configurações do sistema operacional e registrar: (a) nome e versão do SO; (b) arquitetura do processador (x64, ARM64, Intel ou Apple Silicon).
2. Acessar claude.ai e identificar o plano de assinatura ativo.
3. Com base nos dados registrados, selecionar o instalador correto no site da Anthropic e realizar o download.
4. Executar a instalação e realizar o primeiro login no aplicativo.
5. Confirmar que as três abas — Chat, Code e Cowork — estão visíveis e responder ao checklist interativo disponível na tela 1.8.

**Produto parcial esperado:** Claude Desktop instalado, autenticado e com as três interfaces acessíveis; checklist de validação completamente marcado.

**Critério de êxito:** O participante deverá apresentar, no campo de evidência da plataforma (ou por registro próprio), a captura de tela do aplicativo aberto com as três abas visíveis, e deverá ser capaz de indicar, sem consulta, qual instalador utilizou e por quê.

## Checkpoint de Aprendizagem

**Pergunta:** Um participante utiliza um notebook com Windows 11. Ao acessar *Configurações > Sistema > Sobre*, o campo "Tipo de sistema" exibe "Sistema operacional de 64 bits, processador baseado em x64". Qual instalador do Claude Desktop deve ser selecionado?

- ( ) macOS Apple Silicon
- ( ) Windows ARM64
- (●) Windows x64
- ( ) Qualquer um, pois todos são compatíveis com Windows 11

**Gabarito:** Windows x64. O campo "processador baseado em x64" indica a arquitetura correta; selecionar ARM64 em um processador x64 resultará em falha de inicialização do aplicativo.

## Fechamento do Módulo

O Claude Desktop está instalado e autenticado. As três interfaces do aplicativo — Chat, Code e Cowork — estão acessíveis e prontas para uso. No próximo módulo, o participante aprenderá a distinguir a finalidade de cada uma dessas interfaces e realizará as primeiras operações práticas em Chat e Code.

<div style="page-break-after: always;"></div>

# Módulo 2 — Reconhecimento e Uso das Três Interfaces

## Encadeamento

Com o aplicativo instalado e autenticado (Módulo 1), o foco desloca-se para a compreensão operacional das três interfaces — Chat, Code e Cowork — e para a execução de testes práticos nas duas principais.

## Finalidade prática

Neste módulo, o participante identificará a finalidade de cada interface do Claude Desktop, testará a aba Chat com uma solicitação real, criará um arquivo de texto e utilizará a aba Code para que o assistente o leia. O produto parcial é a execução confirmada das operações básicas em Chat e Code, com compreensão objetiva de quando usar cada uma.

## Objetivos de Aprendizagem Prática

Ao final deste módulo, o participante deverá ser capaz de:

1. Descrever a finalidade de cada interface — Chat, Code e Cowork — e citar um exemplo de tarefa adequada a cada uma.
2. Formular e enviar uma solicitação na aba Chat e avaliar a resposta recebida.
3. Criar um arquivo de texto, abrir a pasta correspondente na aba Code e solicitar que o assistente leia o conteúdo do arquivo.
4. Selecionar, diante de uma tarefa descrita, a interface mais adequada e justificar a escolha.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 2.1 | Abertura do módulo | Título, enunciado do problema ("não sei para que serve cada aba") e objetivo da sessão | Ícone das três abas do aplicativo |
| 2.2 | Tabs | Três abas: "Chat", "Code" e "Cowork" — cada uma com finalidade, exemplos de uso e indicação de pré-requisito | Captura de tela de cada interface |
| 2.3 | Texto curto explicativo | Diferença prática entre Claude via navegador e Claude Desktop, destacando a leitura de arquivos locais | Diagrama simples: navegador (copiar/colar) × desktop (acesso direto) |
| 2.4 | Demonstração passo a passo | Teste da aba Chat: enviar solicitação conceitual e observar resposta | Captura de tela: caixa de texto da aba Chat com prompt digitado |
| 2.5 | Demonstração passo a passo | Criação do arquivo `projeto-teste.txt` no editor de texto do sistema operacional | Captura de tela: Bloco de Notas (Windows) ou TextEdit (macOS) com o conteúdo do arquivo |
| 2.6 | Demonstração passo a passo | Abertura da pasta na aba Code via "Open Project" e leitura do arquivo pelo assistente | Captura de tela: painel lateral da aba Code com o arquivo `projeto-teste.txt` listado |
| 2.7 | Scenario block | Cenário: quatro situações de uso — o participante seleciona a interface correta para cada uma | Ilustrações de cada situação |
| 2.8 | Knowledge check | Associação: três tarefas × três interfaces | Nenhum — componente interativo de associação |
| 2.9 | Fechamento do módulo | Resumo comparativo das três interfaces e anúncio do próximo módulo | Tabela visual: Interface × Finalidade × Acessa arquivos? |

## Conteúdo Instrucional Enxuto

O Claude Desktop organiza suas funções em três interfaces apresentadas como abas na parte superior da janela. A interface Chat reproduz a experiência de consulta já familiar para quem utiliza o claude.ai via navegador: o participante digita uma solicitação e o assistente responde em texto. Nessa interface, o Claude não acessa arquivos locais — toda informação processada é aquela explicitamente fornecida pelo participante no campo de texto.

A interface Code é o diferencial central do aplicativo em relação ao acesso via navegador. Nela, o participante seleciona uma pasta do computador — denominada "projeto" — e o assistente obtém acesso de leitura a todos os arquivos de texto contidos nessa pasta. Isso permite solicitar revisões, criação de novos arquivos e execução de comandos sem necessidade de copiar e colar conteúdo manualmente. Todas as alterações propostas são apresentadas em visualização de diferenças (*diff view*) antes de serem aplicadas.

A interface Cowork disponibiliza um modo de execução autônoma, no qual o assistente realiza uma sequência de tarefas sem supervisão contínua. Por envolver maior grau de automação, é indicada para usuários com experiência prévia nas outras duas interfaces. Recomenda-se que o participante deste curso a explore apenas após consolidar o uso de Chat e Code.

## Demonstração Guiada

**Teste da aba Chat:**

1. Clicar na aba "Chat" no topo da janela do Claude Desktop.
2. Na caixa de texto, digitar a seguinte solicitação: *"Explique em duas frases o que é inteligência artificial generativa, como se eu nunca tivesse ouvido esse termo."*
3. Pressionar Enter ou clicar no botão de enviar.
4. Ler a resposta recebida e observar que nenhum arquivo local foi necessário.
5. Resultado esperado: resposta clara e direta do assistente, sem solicitação de arquivos ou configurações adicionais.

*Captura de tela recomendada: aba Chat com o prompt digitado e a resposta visível na janela de conversa.*

**Abertura de projeto na aba Code:**

1. Abrir o Bloco de Notas (Windows) ou TextEdit (macOS), digitar o seguinte conteúdo e salvar como `projeto-teste.txt` em uma pasta de fácil acesso:
   *"Meu primeiro projeto com Claude Desktop. Objetivo: aprender a usar o aplicativo. Data: hoje."*
2. No Claude Desktop, clicar na aba "Code".
3. Clicar no botão "Open Project" (ou ícone de pasta) e selecionar a pasta onde o arquivo foi salvo — a pasta, não o arquivo em si.
4. Aguardar 2 a 3 segundos para que o painel lateral liste os arquivos da pasta.
5. Na caixa de texto, digitar: *"Leia o arquivo projeto-teste.txt e me diga o que está escrito lá."*
6. Resultado esperado: o assistente responde reproduzindo o conteúdo do arquivo, confirmando o acesso à pasta.

*Captura de tela recomendada: painel lateral da aba Code com o arquivo `projeto-teste.txt` listado e a resposta do assistente visível.*

## Atividade Hands-on

### Atividade prática — Testes nas Abas Chat e Code (10 minutos)

**Tarefa:** Executar uma solicitação na aba Chat e confirmar que o Claude responde sem necessidade de arquivos; criar um arquivo de texto e confirmar que o Claude o lê corretamente na aba Code.

**Procedimento:**

1. Na aba Chat, enviar a solicitação indicada na demonstração e registrar a resposta obtida.
2. Criar o arquivo `projeto-teste.txt` com o conteúdo indicado e salvá-lo em uma pasta de trabalho.
3. Na aba Code, clicar em "Open Project", selecionar a pasta do arquivo e aguardar o carregamento do painel lateral.
4. Enviar a solicitação de leitura do arquivo e confirmar que a resposta reproduz o conteúdo digitado.
5. Responder ao cenário interativo da tela 2.7, selecionando a interface correta para cada situação apresentada.

**Produto parcial esperado:** Registro das duas respostas obtidas (Chat e Code) e resultado do cenário interativo com 100% de acertos ou revisão fundamentada.

**Critério de êxito:** O participante deverá ser capaz de descrever, sem consulta, a diferença operacional entre as abas Chat e Code, indicando em qual delas o assistente acessa arquivos locais e por quê.

## Checkpoint de Aprendizagem

**Cenário — Selecione a interface correta para cada situação:**

| Situação | Interface correta |
|---|---|
| Um docente quer obter uma explicação sobre avaliação por competências para incluir em sua ementa | ( ) Chat  ( ) Code  ( ) Cowork |
| Uma analista precisa que o assistente revise um relatório salvo em seu computador | ( ) Chat  ( ) Code  ( ) Cowork |
| Um estudante quer gerar um resumo de um texto que copiará e colará na caixa de texto | ( ) Chat  ( ) Code  ( ) Cowork |

**Gabarito:**
- Situação 1: Chat — consulta conceitual sem arquivo local.
- Situação 2: Code — o arquivo está armazenado localmente.
- Situação 3: Chat — o texto será fornecido diretamente, sem necessidade de abrir pasta.

## Fechamento do Módulo

As interfaces Chat e Code foram testadas em operações reais. O participante já sabe quando usar cada uma e produziu os primeiros registros de interação com o assistente. No próximo módulo, a aba Code será o ambiente central: o foco passará à criação de uma pasta-projeto estruturada e segura, pronta para receber trabalho real.

<div style="page-break-after: always;"></div>

# Módulo 3 — Estruturação de Projeto e Proteção de Dados

## Encadeamento

Com as interfaces compreendidas e testadas (Módulo 2), este módulo concentra-se na configuração correta do ambiente de trabalho na aba Code: criar uma pasta-projeto com estrutura mínima e proteger arquivos sensíveis antes de qualquer interação real com o assistente.

## Finalidade prática

Neste módulo, o participante criará a pasta `meu-projeto-claude` com os três arquivos essenciais — `README.md`, `.gitignore` e `.env` —, abrirá o projeto na aba Code e verificará que a estrutura de proteção está funcionando. O produto parcial é uma pasta-projeto segura, pronta para uso nas atividades do Módulo 4.

## Objetivos de Aprendizagem Prática

Ao final deste módulo, o participante deverá ser capaz de:

1. Criar uma pasta-projeto com escopo mínimo em local adequado no sistema de arquivos.
2. Criar e preencher os arquivos `README.md` e `.gitignore` com o conteúdo mínimo recomendado.
3. Identificar categorias de arquivos sensíveis e aplicar o princípio de exclusão via `.gitignore`.
4. Abrir o projeto na aba Code, verificar que os arquivos essenciais estão listados e testar a interação com o assistente para confirmar o carregamento correto.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 3.1 | Abertura do módulo | Título, enunciado do problema e produto esperado ao final | Diagrama da estrutura de pasta-projeto |
| 3.2 | Texto curto explicativo | Princípio do escopo mínimo: por que não abrir a pasta de usuário inteira | Diagrama: pasta ampla (risco) × pasta de projeto (seguro) |
| 3.3 | Process block | Sequência de criação da estrutura: pasta → README.md → .gitignore → .env | Ícones de cada arquivo com descrição de finalidade |
| 3.4 | Demonstração passo a passo | Criação da pasta `meu-projeto-claude` no Windows e macOS | Capturas de tela anotadas: Explorador de Arquivos (Windows) e Finder (macOS) |
| 3.5 | Accordion | Três painéis expansíveis: "README.md — o que é e o que escrever", ".gitignore — o que é e o que incluir", ".env — por que isolar e como proteger" | Captura de tela de cada arquivo aberto no editor de texto |
| 3.6 | Demonstração passo a passo | Abertura do projeto na aba Code e verificação do painel lateral | Captura de tela: painel lateral com os arquivos listados |
| 3.7 | Demonstração passo a passo | Teste de interação: solicitação ao assistente para listar e descrever os arquivos do projeto | Captura de tela: resposta do assistente mencionando README.md e .gitignore |
| 3.8 | Knowledge check | Verdadeiro ou falso — cinco afirmações sobre proteção de dados e escopo de projeto | Nenhum — componente de quiz |
| 3.9 | Download de modelo | Modelos de `README.md` e `.gitignore` disponíveis para download e adaptação | Botão de download |
| 3.10 | Fechamento do módulo | Resumo da estrutura criada e preparação para o Módulo 4 | Diagrama final da pasta-projeto com os três arquivos |

## Conteúdo Instrucional Enxuto

Na aba Code do Claude Desktop, o ponto de partida é a seleção de uma pasta do computador. A partir dessa seleção, o assistente obtém acesso de leitura a todos os arquivos de texto contidos nessa pasta. Depreende-se, portanto, que a escolha da pasta é uma decisão de segurança: abrir uma pasta ampla — como a pasta de usuário do sistema operacional — expõe documentos pessoais, fotografias e outros dados que não são relevantes para a tarefa em questão. Recomenda-se adotar o princípio do escopo mínimo: criar uma pasta dedicada ao projeto específico e abrir apenas ela.

O arquivo `README.md` é um documento de texto simples que descreve o propósito, o conteúdo e as instruções de uso do projeto. O assistente lê esse arquivo prioritariamente ao carregar um projeto, o que permite contextualizar rapidamente o escopo do trabalho sem a necessidade de fornecer essas informações a cada nova sessão.

O arquivo `.gitignore` especifica quais arquivos e pastas devem ser ignorados pelo sistema de controle de versão Git — e, por extensão, protegidos de compartilhamento inadvertido. O arquivo `.env` é o repositório padrão de informações sensíveis como senhas, chaves de API e tokens de acesso; ele deve sempre figurar na lista de exclusões do `.gitignore`. Depreende-se que a criação conjunta dos três arquivos — `README.md`, `.gitignore` e `.env` — antes da abertura do projeto é a sequência operacional mínima recomendada para qualquer uso profissional da aba Code.

## Demonstração Guiada

1. Abrir o Explorador de Arquivos (Windows) ou o Finder (macOS) e navegar até a pasta Documentos.
2. Criar uma nova pasta com o nome `meu-projeto-claude`.
3. Abrir o editor de texto e criar o arquivo `README.md` com o seguinte conteúdo mínimo, salvando-o dentro da pasta criada:

```text
# Meu Projeto com Claude Desktop

## O que é isso
[Descreva brevemente para que serve este projeto]

## O que tem aqui
- README.md: este arquivo de descrição
- .gitignore: lista de arquivos que não devem ser compartilhados

## Como usar
Abrir esta pasta na aba Code do Claude Desktop.
```

4. Criar o arquivo `.gitignore` com o seguinte conteúdo e salvá-lo na mesma pasta:

```text
.env
*.key
*.pem
senhas.txt
dados-pessoais/
```

   *Atenção para Windows: no Bloco de Notas, selecionar "Todos os arquivos" no tipo de arquivo antes de salvar e digitar `.gitignore` no campo de nome — sem extensão adicional.*

5. Criar o arquivo `.env` com conteúdo fictício de exemplo (`CHAVE_API=exemplo_nao_usar_em_producao`) e salvá-lo na pasta.
6. No Claude Desktop, acessar a aba Code, clicar em "Open Project" e selecionar a pasta `meu-projeto-claude`.
7. Verificar que o painel lateral lista `README.md` e `.gitignore`.
8. Na caixa de texto, enviar: *"Você consegue ver os arquivos deste projeto? Liste o que encontrou e me explique para que serve cada arquivo."*
9. Resultado esperado: o assistente lista `README.md` e `.gitignore` com descrições coerentes.

*Captura de tela recomendada: painel lateral da aba Code com os arquivos do projeto listados, confirmando o carregamento correto da estrutura.*

## Atividade Hands-on

### Atividade prática — Criação da Pasta-Projeto Segura (12 minutos)

**Tarefa:** Criar a estrutura mínima de pasta-projeto com os três arquivos essenciais, abrir o projeto na aba Code e verificar que o assistente reconhece e descreve os arquivos corretamente.

**Procedimento:**

1. Criar a pasta `meu-projeto-claude` em Documentos (ou outro local de fácil acesso).
2. Criar o arquivo `README.md` com o conteúdo mínimo indicado, adaptando a seção "O que é isso" ao contexto de uso real do participante.
3. Criar o arquivo `.gitignore` com as exclusões indicadas.
4. Criar o arquivo `.env` com conteúdo fictício de exemplo.
5. Abrir o projeto na aba Code e enviar a solicitação de listagem de arquivos.
6. Confirmar que o assistente menciona `README.md` e `.gitignore` na resposta.
7. Responder ao knowledge check da tela 3.8.

**Produto parcial esperado:** Pasta `meu-projeto-claude` com os três arquivos criados e aberta na aba Code; registro da resposta do assistente confirmando o carregamento.

**Critério de êxito:** O participante deverá ser capaz de explicar, sem consulta, a finalidade de cada um dos três arquivos criados (`README.md`, `.gitignore`, `.env`) e justificar por que o `.env` deve estar listado no `.gitignore`.

## Checkpoint de Aprendizagem

**Verdadeiro ou Falso — marque cada afirmação:**

1. "Ao abrir uma pasta na aba Code, o Claude acessa apenas o arquivo que o participante mencionar na solicitação." → **Falso.** O assistente acessa todos os arquivos de texto contidos na pasta selecionada.
2. "O arquivo `.gitignore` protege os arquivos listados nele de serem rastreados pelo Git e de serem compartilhados inadvertidamente." → **Verdadeiro.**
3. "O arquivo `README.md` pode ser deixado em branco sem prejudicar o uso do projeto." → **Falso.** O assistente lê esse arquivo para contextualizar o projeto; um README bem escrito reduz a necessidade de fornecer contexto a cada sessão.
4. "Senhas e chaves de API devem ser armazenadas no `README.md` para facilitar o acesso pelo assistente." → **Falso.** Arquivos sensíveis devem ser isolados em `.env` e protegidos pelo `.gitignore`.
5. "O princípio do escopo mínimo indica que deve-se abrir apenas a pasta específica do projeto, não a pasta de usuário inteira." → **Verdadeiro.**

## Prompt ou Modelo Editável

O modelo abaixo deve ser adaptado ao contexto real do participante antes de ser salvo como `README.md`:

```text
# [Nome do Projeto]

## O que é isso
[Descreva em 2 a 3 frases o propósito deste projeto e o tipo de tarefa que será realizada.]

## Arquivos deste projeto
- README.md: descrição e instruções do projeto
- .gitignore: lista de exclusões de segurança
- [outros arquivos]: [descrição breve]

## Instruções de uso
Abrir esta pasta na aba Code do Claude Desktop.
[Adicione aqui qualquer instrução específica para o assistente.]

## Restrições
[Liste o que o assistente não deve alterar, remover ou criar.]
```

## Fechamento do Módulo

A pasta-projeto está criada, estruturada e aberta no Claude Desktop. O assistente reconhece os arquivos e está pronto para receber solicitações de trabalho. No próximo módulo, o participante aprenderá a redigir solicitações eficazes, a revisar as alterações propostas por meio da diff view e a aceitar ou rejeitar mudanças de forma consciente.

<div style="page-break-after: always;"></div>

# Módulo 4 — Formulação de Prompts Eficazes e Revisão de Resultados

## Encadeamento

Com o projeto estruturado e aberto na aba Code (Módulo 3), este módulo concentra-se na operação central do fluxo de trabalho: redigir solicitações que gerem resultados precisos, revisar as alterações propostas e decidir — de forma fundamentada — se devem ser aceitas ou rejeitadas.

## Finalidade prática

Neste módulo, o participante comparará um prompt fraco com um prompt forte, aprenderá e aplicará a fórmula Contexto–Tarefa–Limite–Formato, revisará uma alteração proposta pelo assistente na diff view e praticará a interrupção e o redirecionamento de uma resposta em andamento. O produto parcial é um prompt forte aplicado ao projeto do Módulo 3, com a diff view revisada e a alteração aceita ou rejeitada de forma consciente.

## Objetivos de Aprendizagem Prática

Ao final deste módulo, o participante deverá ser capaz de:

1. Identificar as diferenças entre um prompt fraco e um prompt forte, enumerando os elementos ausentes no primeiro.
2. Aplicar a fórmula Contexto–Tarefa–Limite–Formato para estruturar uma solicitação ao assistente na aba Code.
3. Interpretar a diff view, identificando linhas adicionadas e removidas, e decidir se a alteração proposta deve ser aceita ou rejeitada.
4. Acionar o botão "Stop" para interromper uma resposta em andamento e reformular a solicitação com escopo corrigido.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 4.1 | Abertura do módulo | Título, enunciado do problema e produto esperado | Ícone representando comunicação eficaz |
| 4.2 | Texto curto explicativo | Por que prompts vagos geram resultados genéricos — princípio da instrução clara | Nenhum — bloco de texto objetivo |
| 4.3 | Tabs | Duas abas: "Prompt fraco" e "Prompt forte" — com exemplo de cada e análise dos elementos presentes/ausentes | Comparação visual lado a lado |
| 4.4 | Process block | A fórmula em quatro etapas: Contexto → Tarefa → Limite → Formato | Bloco sequencial com exemplo real em cada etapa |
| 4.5 | Cenário prático | Três pares de prompts — o participante identifica qual é o mais eficaz e justifica | Nenhum — componente de escolha com feedback |
| 4.6 | Demonstração passo a passo | Aplicação do prompt forte ao projeto aberto na aba Code e revisão da diff view | Captura de tela: diff view com linhas adicionadas (verde) e removidas (vermelho) |
| 4.7 | Demonstração passo a passo | Prática de interrupção: acionar "Stop" e reformular a solicitação | Captura de tela: botão "Stop" visível durante resposta em andamento |
| 4.8 | Labeled graphic | Diagrama da diff view com rótulos explicativos: verde (+), vermelho (−), cinza (contexto) | Captura de tela anotada da diff view |
| 4.9 | Knowledge check | Múltipla escolha: três pares de prompts — identificar o mais eficaz | Nenhum — componente de quiz |
| 4.10 | Fechamento do módulo | Resumo do produto parcial e preparação para a síntese | Tabela: fórmula resumida com exemplo |

## Conteúdo Instrucional Enxuto

A qualidade dos resultados produzidos pelo assistente é diretamente proporcional à clareza da solicitação que o origina. Uma solicitação vaga — como "melhore meu texto" — não fornece ao assistente informação suficiente sobre o que mudar, como mudar nem quais restrições observar. Uma solicitação precisa, por outro lado, delimita o escopo, define a ação esperada e especifica os critérios de resultado.

A fórmula Contexto–Tarefa–Limite–Formato organiza esses elementos de forma prática. O Contexto situa o assistente no projeto: "Este é um e-mail formal para um reitor." A Tarefa define a ação: "Corrija erros gramaticais e de concordância verbal." O Limite preserva o que não deve ser alterado: "Não mude o conteúdo, os argumentos nem o tom formal." O Formato orienta a entrega: "Entregue o e-mail corrigido completo, sem comentários adicionais." Não é obrigatório utilizar todos os quatro elementos em toda solicitação, mas cada elemento adicionado reduz a ambiguidade e aumenta a precisão do resultado.

Após o assistente propor uma alteração na aba Code, a diff view exibe o conteúdo original marcado em vermelho (ou com sinal de subtração) e o conteúdo proposto marcado em verde (ou com sinal de adição). Deve-se revisar essa visualização antes de clicar em "Accept". Caso a alteração proposta esteja incorreta ou fora do escopo solicitado, clica-se em "Reject" e reformula-se a solicitação com mais precisão. Se o assistente iniciar uma resposta em direção errada, o botão "Stop" interrompe a execução imediatamente — sem necessidade de aguardar o término para redirecionar.

## Demonstração Guiada

**Aplicação da fórmula e revisão da diff view:**

1. Com o projeto `meu-projeto-claude` aberto na aba Code, digitar o seguinte prompt na caixa de texto (adaptando o conteúdo entre colchetes):

```text
CONTEXTO: Este projeto tem um arquivo README.md que descreve [seu contexto real].
TAREFA: Reescreva a seção "O que é isso" do README.md deixando o texto mais claro
e direto, em no máximo três frases.
LIMITE: Não remova nem adicione seções. Não altere o restante do arquivo.
FORMATO: Entregue apenas o texto novo da seção, sem comentários adicionais.
```

2. Enviar a solicitação e aguardar a resposta do assistente.
3. Quando a diff view for exibida, identificar as linhas marcadas em verde (adicionadas) e em vermelho (removidas).
4. Avaliar se as alterações atendem aos critérios definidos no prompt.
5. Clicar em "Accept" se a alteração estiver correta, ou em "Reject" com justificativa se não estiver.

*Captura de tela recomendada: diff view com as alterações propostas pelo assistente, com as linhas verdes e vermelhas claramente visíveis.*

**Prática de interrupção e redirecionamento:**

1. Na aba Code, digitar uma solicitação de escopo amplo: *"Reescreva todos os arquivos deste projeto melhorando o texto de cada um."*
2. Aguardar 3 a 5 segundos enquanto o assistente começa a processar.
3. Clicar no botão "Stop" (ou "Cancel") que aparece na parte inferior da janela de chat.
4. Com o assistente pausado, reformular: *"Na verdade, só quero que você melhore o texto do README.md. Apenas esse arquivo."*
5. Resultado esperado: o assistente retoma a execução com o escopo corrigido.

*Captura de tela recomendada: botão "Stop" visível durante o processamento da resposta.*

## Atividade Hands-on

### Atividade prática — Prompt Forte e Revisão de Diff View (12 minutos)

**Tarefa:** Redigir um prompt forte utilizando a fórmula Contexto–Tarefa–Limite–Formato, enviá-lo na aba Code com o projeto do Módulo 3 aberto, revisar a diff view e tomar a decisão de aceitar ou rejeitar a alteração proposta.

**Procedimento:**

1. Com o projeto `meu-projeto-claude` aberto na aba Code, identificar um arquivo que possa ser melhorado (sugestão: `README.md`).
2. Redigir um prompt forte utilizando os quatro elementos da fórmula, adaptado ao arquivo selecionado.
3. Enviar o prompt e aguardar a resposta do assistente.
4. Abrir a diff view e revisar linha por linha as alterações propostas.
5. Aceitar a alteração se estiver correta; rejeitar com justificativa se não estiver — e reformular o prompt para uma segunda tentativa.
6. Completar o cenário prático da tela 4.5, identificando o prompt mais eficaz em cada par.

**Produto parcial esperado:** Prompt forte registrado pelo participante (texto preservado em editor ou captura de tela); registro da decisão tomada na diff view (aceitar ou rejeitar) com justificativa.

**Critério de êxito:** O participante deverá ser capaz de apresentar, sem consulta, um prompt com os quatro elementos da fórmula aplicados, e explicar, observando a diff view, quais critérios utilizou para aceitar ou rejeitar a alteração proposta.

## Checkpoint de Aprendizagem

**Pergunta:** Qual dos prompts abaixo tende a gerar o resultado mais preciso na aba Code?

- ( ) "Corrija erros."
- ( ) "Revise o documento."
- (●) "CONTEXTO: Este é um relatório de gestão de 2024. TAREFA: Corrija erros gramaticais e de concordância verbal no segundo parágrafo do arquivo `relatorio.md`. LIMITE: Não altere dados numéricos, nomes próprios nem a estrutura de tópicos. FORMATO: Entregue o parágrafo corrigido completo, sem comentários."
- ( ) "Melhore o texto do relatório conforme achar melhor."

**Gabarito:** A terceira opção. Os outros prompts carecem de escopo (qual arquivo, qual trecho), tarefa definida (que tipo de correção), limitações e formato de entrega — elementos que, quando ausentes, resultam em respostas genéricas ou na execução de alterações não desejadas.

## Prompt ou Modelo Editável

O modelo abaixo pode ser copiado, preenchido e utilizado diretamente na aba Code:

```text
CONTEXTO: [Descreva o projeto e o arquivo em questão.]
TAREFA: [Descreva exatamente o que o assistente deve fazer.]
LIMITE: [Descreva o que não deve ser alterado, removido ou criado.]
FORMATO: [Especifique como a resposta deve ser entregue.]
```

## Fechamento do Módulo

O participante agora domina o ciclo central de uso da aba Code: formular um prompt estruturado, receber a proposta do assistente, revisá-la na diff view e decidir conscientemente pela aceitação ou rejeição. No módulo final, todos os produtos parciais dos módulos anteriores serão integrados em uma sessão de trabalho completa, simulando um uso real do Claude Desktop do início ao fim.

<div style="page-break-after: always;"></div>

# Módulo 5 — Síntese e Aplicação Integrada

## Finalidade da Síntese

Este módulo reúne, em uma sessão de trabalho única e contínua, as competências desenvolvidas nos quatro módulos anteriores: o aplicativo instalado e autenticado (Módulo 1), o reconhecimento e uso das interfaces (Módulo 2), a estruturação segura de um projeto (Módulo 3) e a formulação de prompts eficazes com revisão de resultados (Módulo 4). O participante criará uma nova pasta-projeto de uso real — `projeto-final-claude` —, definirá uma tarefa concreta de sua área de atuação, executará o ciclo completo de interação com o assistente e documentará o resultado obtido.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 5.1 | Abertura do módulo | Apresentação da missão integradora e do produto final esperado | Diagrama do fluxo completo: instalação → interfaces → projeto → prompt → resultado |
| 5.2 | Texto curto explicativo | Como os produtos parciais dos módulos anteriores se articulam nesta sessão | Linha do tempo visual dos módulos anteriores com ícones dos produtos parciais |
| 5.3 | Process block | Sequência da sessão integradora em seis etapas | Bloco sequencial numerado |
| 5.4 | Demonstração passo a passo | Criação da pasta `projeto-final-claude` com README.md, .gitignore e arquivo de conteúdo | Captura de tela: estrutura da pasta no Explorador ou Finder |
| 5.5 | Demonstração passo a passo | Abertura do projeto na aba Code e envio do prompt forte | Captura de tela: projeto aberto, prompt estruturado na caixa de texto |
| 5.6 | Demonstração passo a passo | Revisão da diff view, ciclo de aceitar/rejeitar e consulta final na aba Chat | Captura de tela: diff view com alterações propostas; tela da aba Chat com consulta final |
| 5.7 | Checklist integradora | Lista de sete critérios — o participante marca cada item concluído | Componente interativo de checklist |
| 5.8 | Avaliação por critérios | Tabela de critérios de avaliação com campo "Atendido?" | Nenhum — componente de autoavaliação |
| 5.9 | Encerramento do módulo | Parágrafo de encerramento e direcionamento para aprofundamento | Nenhum — bloco de texto conclusivo |

## Atividade Integradora

### Atividade integradora — Sessão de Trabalho Real com o Claude Desktop (15 minutos)

**Tarefa:** Criar uma pasta-projeto de uso real, configurá-la com estrutura mínima segura, definir uma tarefa concreta, executar o ciclo completo de interação com o assistente e documentar o resultado.

**Procedimento:**

1. Recuperar os produtos parciais dos módulos anteriores: confirmar que o Claude Desktop está aberto e autenticado (Módulo 1) e que o conhecimento das interfaces está consolidado (Módulo 2).
2. Criar a pasta `projeto-final-claude` em Documentos. Dentro dela, criar o `README.md` preenchido com nome do projeto, descrição da tarefa da sessão e critérios de qualidade esperados; criar o `.gitignore` com as exclusões mínimas; criar um arquivo de conteúdo real (documento, relatório parcial, lista ou e-mail) com nome descritivo.
3. Abrir a pasta `projeto-final-claude` na aba Code do Claude Desktop.
4. Redigir um prompt forte utilizando a fórmula Contexto–Tarefa–Limite–Formato, adaptado à tarefa definida no README, e enviá-lo ao assistente.
5. Revisar a diff view linha por linha, aceitar as alterações adequadas e rejeitar as inadequadas — com justificativa para cada rejeição e reformulação do prompt quando necessário.
6. Após pelo menos um ciclo completo (prompt → diff view → aceitar ou rejeitar), acessar a aba Chat e enviar a consulta: *"Com base nesta sessão, que outros tipos de tarefa poderiam ser realizados neste projeto?"*
7. Registrar ao menos uma sugestão recebida que será testada em sessão futura.

**Produto final esperado:** Pasta `projeto-final-claude` com `README.md`, `.gitignore` e arquivo de conteúdo; registro documentado (captura de tela ou anotação) do prompt utilizado, da decisão tomada na diff view e da consulta realizada na aba Chat.

## Critérios de Avaliação

| Critério | Descrição | Atendido? |
|---|---|---|
| Completude da estrutura | A pasta `projeto-final-claude` contém `README.md`, `.gitignore` e pelo menos um arquivo de conteúdo | ☐ Sim ☐ Não |
| Clareza do README | O `README.md` descreve o projeto, a tarefa da sessão e os critérios de qualidade esperados | ☐ Sim ☐ Não |
| Proteção de dados | O `.gitignore` está presente e contém as exclusões mínimas necessárias | ☐ Sim ☐ Não |
| Qualidade do prompt | O prompt enviado contém pelo menos dois dos quatro elementos da fórmula (Contexto, Tarefa, Limite, Formato) | ☐ Sim ☐ Não |
| Revisão da diff view | A diff view foi revisada antes da decisão de aceitar ou rejeitar a alteração | ☐ Sim ☐ Não |
| Decisão fundamentada | A aceitação ou rejeição foi tomada com justificativa explícita, não de forma aleatória | ☐ Sim ☐ Não |
| Uso integrado das interfaces | A aba Code foi utilizada para o trabalho no projeto e a aba Chat para a consulta final | ☐ Sim ☐ Não |
| Aplicabilidade | O projeto e a tarefa escolhidos correspondem a uma necessidade real do participante | ☐ Sim ☐ Não |
| Coerência | O conteúdo do README é coerente com o arquivo de trabalho criado e com o prompt enviado | ☐ Sim ☐ Não |
| Revisão final | O participante registrou ao menos um ajuste que realizaria na próxima sessão com base no que foi aprendido | ☐ Sim ☐ Não |

## Encerramento da Síntese

O participante concluiu uma sessão de trabalho completa com o Claude Desktop — da criação do projeto à revisão crítica do resultado —, demonstrando competência operacional integrada em todas as etapas do fluxo central da ferramenta. O produto final documentado constitui a evidência de aprendizagem prática do curso e o ponto de partida para o uso autônomo e continuado do aplicativo em contextos reais de trabalho.

---

<div style="page-break-after: always;"></div>

# Orientações para Produção no Articulate 360

## Organização visual

- Utilizar blocos curtos e progressivos em Rise 360, com no máximo 150 palavras por bloco de texto corrido.
- Evitar telas com excesso de texto; distribuir o conteúdo em múltiplos blocos sequenciais em vez de concentrá-lo em uma única tela longa.
- Priorizar listas, checklists, cards e process blocks para conteúdo operacional de passo a passo.
- Utilizar capturas de tela anotadas em todas as etapas que envolvam interação com interfaces, botões, menus ou resultados visuais do Claude Desktop.
- Inserir legendas descritivas em todas as capturas de tela, indicando o que está sendo destacado e por quê.
- Adotar paleta de cores e tipografia consistentes com a identidade visual da instituição produtora; reservar destaque cromático (ex.: amarelo ou laranja) para alertas e caixas de atenção.

## Interações recomendadas

As interações abaixo são adequadas ao perfil de conteúdo deste curso:

- **Process blocks** (Rise 360): para sequências de instalação, criação de arquivos e ciclo de prompt → diff view → aceitar/rejeitar.
- **Tabs** (Rise 360): para comparações entre interfaces (Chat × Code × Cowork) e entre prompts (fraco × forte).
- **Accordion** (Rise 360): para conteúdo complementar sobre arquivos de projeto (`README.md`, `.gitignore`, `.env`) que o participante pode expandir conforme necessidade.
- **Knowledge checks** (Rise 360): para múltipla escolha, verdadeiro ou falso e associação em momentos de checkpoint.
- **Checklists** (Rise 360): para validação pós-instalação e critérios de avaliação do módulo de síntese.
- **Scenario blocks** (Rise 360): para o exercício de seleção de interface correta (Módulo 2) e identificação de prompt mais eficaz (Módulo 4).
- **Labeled graphics** (Rise 360): para o diagrama de seleção de instalador (Módulo 1) e para a diff view anotada (Módulo 4).
- **Download blocks** (Rise 360): para os modelos de `README.md` e `.gitignore` disponibilizados no Módulo 3.
- **Slides Storyline 360 embutidos**: recomendados para cenários de decisão com feedback imediato e para simulações de interface quando capturas de tela estáticas forem insuficientes.

## Padrão de linguagem das telas

Cada tela deve conter:

- **Título curto** (máximo 8 palavras) que identifique o assunto ou a ação da tela.
- **Instrução objetiva** indicando o que o participante deve fazer ou observar naquela tela.
- **Uma ação principal** por tela — leitura, clique, preenchimento, resposta ou observação.
- **Feedback imediato** em telas com atividade interativa (knowledge check, cenário, checklist): confirmar acerto com explicação breve ou indicar o erro com a resposta correta e justificativa.
- **Indicação clara de avanço**: botão "Próximo", seta ou indicador de progresso visível em todas as telas.

Recomenda-se que os textos de instrução nas telas sigam o registro formal e impessoal definido neste roteiro — evitando a segunda pessoa e preferindo construções como "o participante deverá", "recomenda-se" e "observa-se" — para manter coerência com o tom do curso e com o padrão institucional esperado pelo público-alvo.

---

## Encerramento

O presente roteiro instrucional orienta a produção de um curso digital de 90 minutos no Articulate 360, estruturado em quatro módulos práticos e um módulo de síntese aplicada. O participante que percorrer os módulos na ordem proposta terá realizado, em ambiente real, o fluxo completo de uso do Claude Desktop — da instalação à revisão crítica de resultados —, tendo como evidência concreta a pasta `projeto-final-claude` documentada com prompt estruturado, decisão fundamentada na diff view e registro de consulta integradora na aba Chat. O produto final não é um exercício simulado, mas um entregável gerado a partir de uma necessidade real do participante, o que confere ao curso aplicabilidade imediata ao contexto de trabalho.

Para os participantes que desejem avançar além do escopo deste curso, recomenda-se a exploração dos seguintes temas na trilha Essentials: configuração do arquivo `.claude.md` para definição de instruções persistentes por projeto; modos de permissão avançados da aba Code (Ask, Auto-accept e Plan); uso da interface Cowork para automação de tarefas repetitivas de longa duração; e integração do Claude Desktop com ambientes de desenvolvimento integrado. O domínio operacional demonstrado ao final deste curso Hands-on constitui a base prática necessária para o aproveitamento pleno desses conteúdos avançados.

> **Síntese:** A competência com o Claude Desktop não se adquire pela leitura de conceitos, mas pela execução repetida e consciente do ciclo instalar → estruturar → solicitar → revisar → registrar — e este curso existe para que essa execução aconteça desde o primeiro acesso.
