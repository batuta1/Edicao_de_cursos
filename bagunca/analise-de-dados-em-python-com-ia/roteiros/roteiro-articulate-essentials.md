# Plano de Aula — Dados com Python e IA (Essentials)

> *» IA: Bloco Cover — título verbatim. Subtítulo: "Análises reprodutíveis em Python com agentes de código, para quem não programa". Não traduzir "Claude Code", "Codex", "Python", "pandas", "uv" nem nomes de comandos.*

## Identificação

> *» IA: Bloco Table — tabela verbatim.*

| Campo | Definição |
|---|---|
| Curso | Dados com Python e IA (Essentials) |
| Natureza | Autoinstrucional, introdutório e prático |
| Carga horária | 111 minutos (sem contar a espera do agente durante instalações e execuções) |
| Público-alvo | Analistas, profissionais de finanças e planejamento, pesquisadores; servidores públicos e equipes de regulação; engenheiros e técnicos |
| Pré-requisitos | *IA para Análise de Dados - Essentials* (recomendado) e Excel básico; nenhuma programação |
| Recursos necessários | Computador com macOS 13+ ou Windows 10 1809+ e 4 GB de RAM; internet; uma das rotas: Claude Code no app Claude Desktop (plano Claude Pro, R$ 110/mês, ou superior — o plano gratuito não inclui Claude Code) ou Codex no app de desktop do ChatGPT (acesso limitado no Free, sujeito a liberação gradual; Plus, R$ 99,90/mês, para uso pleno); gerenciador uv |

### Objetivo Geral

> *» IA: Bloco Text — verbatim.*

O curso tem por finalidade capacitar o participante, que não programa, a conduzir uma análise de dados reprodutível em Python com um agente de código — Claude Code ou Codex: formular o pedido em forma de brief, aprovar as ações do agente com segurança, ler o código produzido no nível de leigo, organizar o projeto para que rode novamente do zero e validar os resultados contra número oficial. Como produto final, o participante entrega o projeto `ipca-projeto`, com script, registro de versões, testes automáticos e README, reproduzindo o IPCA acumulado de 2024 e 2025 publicado pelo IBGE.

### Competências a Desenvolver

> *» IA: Bloco List — numerada, verbatim, sem acréscimos.*

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Decidir quando uma análise deve passar da conversa para um projeto em código.
2. Configurar o agente em modo restrito e decidir cada pedido de aprovação com base nos riscos documentados.
3. Redigir um brief de análise e exigir o plano antes da execução.
4. Organizar um projeto reprodutível e verificar que ele roda do zero.
5. Validar resultados com testes automáticos, contagens de controle, número oficial e revisão independente.

### Estrutura e Sequência dos Módulos

> *» IA: Bloco Text — verbatim.*

Os módulos são cumulativos: cada um pressupõe o anterior. O princípio "rodou não é o mesmo que acertou" é apresentado no Módulo 1 e retomado nos Módulos 4 e 5. O projeto `ipca-projeto`, com a série mensal do IPCA divulgada pelo Banco Central e gabarito do IBGE (4,83% em 2024; 4,26% em 2025), atravessa os Módulos 3 a 6.

> *» IA: Bloco Table — verbatim.*

| Módulo | Título | Referência | Tempo |
|---|---|---|---|
| 0 | Preparação e Verificação Inicial | Documentação do Claude Code e do Codex; página do uv | 7 min |
| 1 | Por que Código e o que é um Agente | Documentação do Claude Code; Pimentel et al. (2021) | 19 min |
| 2 | O Agente no seu Computador: Segurança e Dados | Permissões e uso de dados (Anthropic, OpenAI); USENIX Security 2025 | 15 min |
| 3 | Pedir e Planejar | Boas práticas do Claude Code; AGENTS.md | 16 min |
| 4 | Reprodutibilidade | Wilson et al. (2017); Sandve et al. (2013) | 16 min |
| 5 | Validar Resultados | DA-Code; DSBench; KramaBench; "Fail Loudly"; METR | 22 min |
| 6 | Síntese e Aplicação Integrada | — | 16 min |

---

# Módulo 0 — Preparação e Verificação Inicial

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 0" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Ponto de partida: escolhe a rota de trabalho, instala o uv e monta a pasta do projeto.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Escolher uma rota de trabalho compatível com o próprio plano e sistema operacional.
2. Instalar o uv e verificar a instalação.
3. Montar a pasta do projeto com os dados brutos.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir.*

O curso pode ser realizado por três rotas. Recomenda-se a A ou a B, nas quais o agente funciona dentro de um aplicativo de desktop, sem terminal. Cumpre registrar que não há rota inteiramente gratuita garantida: o Claude Code não está incluído no plano gratuito do Claude, e o Codex no plano gratuito do ChatGPT é oferecido de forma limitada e sujeita a liberação gradual.

> *» IA: Bloco Table — verbatim.*

| Rota | Onde | Plano necessário (17/11/2026) | Requisitos |
|---|---|---|---|
| A | App Claude Desktop, aba Code | Claude Pro (R$ 110/mês; R$ 92/mês no anual) ou superior | macOS 13+ ou Windows 10 1809+; 4 GB de RAM; Git for Windows recomendado no Windows |
| B | App de desktop do ChatGPT, modo Codex | Free limitado; Plus (R$ 99,90/mês) para uso pleno | macOS, Windows ou Linux |
| C | Terminal (Claude Code CLI ou Codex CLI) | Mesmos planos | Instalador oficial de cada ferramenta |

> *» IA: Bloco Text — verbatim; preservar os comandos sem alteração.*

O uv é o gerenciador da empresa Astral que instala o Python, as bibliotecas e registra as versões utilizadas — uma lista de compras com marca e tamanho anotados. É o único ponto do curso que exige o terminal. No Windows, o comando oficial é executado no PowerShell; no macOS, no aplicativo Terminal:

- Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- macOS: `curl -LsSf https://astral.sh/uv/install.sh | sh`

> *» IA: Accordion — título = problema, corpo = solução; verbatim.*

| Problema | Solução |
|---|---|
| Mensagem de que "irm" não é reconhecido | O comando foi colado no Prompt de Comando; abrir o PowerShell |
| `uv` não encontrado após a instalação | Fechar e reabrir o terminal |
| O aplicativo pede assinatura ao abrir Code ou Codex | A conta não possui o plano exigido; consultar a tabela de rotas |

### Exercício Prático

> *» IA: Process — passos verbatim; preservar os breadcrumbs e os endereços.*

**Verificação inicial (7 min)**

1. Abrir a rota escolhida: `Claude (app de desktop) > Code > selecionar pasta` ou `ChatGPT (app de desktop) > menu de modos > Codex`.
2. Instalar o uv e executar `uv --version`.
3. Criar a pasta `ipca-projeto/dados/brutos` e salvar nela `ipca.csv`, baixado de `api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2020&dataFinal=31/12/2025`.

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: agente aberto na rota escolhida, `uv --version` exibindo um número de versão e `ipca-projeto/dados/brutos/ipca.csv` presente.

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Estou começando a usar você para análise de dados e não sei programar. Antes de qualquer tarefa,
liste em linguagem simples o que você pode fazer nesta pasta (ler, criar, alterar, apagar,
executar), o que precisa da minha aprovação e como eu desfaço uma alteração.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 0" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 1 — Por que Código e o que é um Agente

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe o ambiente pronto no Módulo 0; desloca o foco para os conceitos de base.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Identificar as situações em que a análise deve passar para código.
2. Definir agente de código e descrever o papel do participante na interação.
3. Distinguir script, notebook, biblioteca e ambiente virtual.
4. Enunciar o princípio "rodou não é o mesmo que acertou".

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir.*

Na análise sem código, estudada em *IA para Análise de Dados*, o resultado permanece numa conversa com o assistente. Recomenda-se a passagem para código quando a análise precisa ser refeita periodicamente ou por outra pessoa, quando envolve vários arquivos ou arquivos grandes, ou quando precisa ser auditada linha a linha. O código transforma a conversa numa receita guardada em arquivo, que pode ser executada outra vez com o mesmo resultado.

Um agente de código é um programa de inteligência artificial que, segundo a documentação do Claude Code, lê o código, edita arquivos, executa comandos e se integra às ferramentas de desenvolvimento no computador do usuário. O Claude Code, da Anthropic, e o Codex, da OpenAI, recebem o pedido em português, escrevem o programa em Python, executam-no e apresentam o resultado. O participante não digita código: aprova as ações, lê o que foi produzido no nível de leigo e confere os números.

O curso adota o script como formato principal. Estudo publicado em 2021, que tentou executar 863.878 notebooks públicos do GitHub, verificou que apenas 24,11% rodaram sem erro e somente 4,03% reproduziram os resultados originais; as causas mais comuns foram dependências não declaradas, células executadas fora de ordem e caminhos de arquivo fixos. Depreende-se desse quadro o princípio que orienta o curso: rodou não é o mesmo que acertou. Um código pode executar sem nenhum erro sobre uma premissa equivocada.

> *» IA: Bloco Table — verbatim.*

| Termo | O que é | Analogia |
|---|---|---|
| Script (`.py`) | Receita completa num arquivo, executada do início ao fim | Receita impressa |
| Notebook (`.ipynb`) | Caderno com células de código, texto e gráficos | Caderno de laboratório |
| pandas | Biblioteca de tabelas | A planilha dentro do Python |
| Matplotlib | Biblioteca de gráficos | O módulo de gráficos |
| uv | Instala Python e bibliotecas e registra versões | Lista de compras com marca e tamanho |
| Ambiente virtual | Conjunto de bibliotecas exclusivo do projeto | Gaveta separada por cliente |

### Exercício Prático

> *» IA: Knowledge Check — questão de múltipla escolha; alternativas e gabarito verbatim.*

**Questão (4 min)**

Em qual situação a passagem para código mais se justifica?

(a) Uma pergunta única sobre uma planilha pequena.
(b) Um indicador mensal que precisa ser refeito todo mês, a partir de doze arquivos, por pessoas diferentes.
(c) Um gráfico rápido para uma conversa.

**Gabarito:** (b) — repetição periódica, vários arquivos e mais de um executor.

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Tenho esta análise que hoje faço [descrever: com que frequência, quantos arquivos, quem refaz].
Diga se vale transformá-la em um projeto em Python, que pastas e arquivos o projeto teria e o que
eu precisaria aprovar durante a criação.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 2 — O Agente no seu Computador: Segurança e Dados

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe a definição de agente do Módulo 1; antecede o primeiro uso real do agente.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Configurar o agente em modo restrito.
2. Explicar os limites dos mecanismos de desfazer.
3. Reconhecer os riscos documentados de agentes de código, inclusive pacotes inexistentes.
4. Aplicar as regras de dados de cada ferramenta e da LGPD.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir; não traduzir nomes de modos nem comandos.*

O agente pode ler, criar, alterar e apagar arquivos e executar comandos; as permissões definem o que ele faz sem perguntar. No Claude Code, o modo Manual (valor `default`) executa sem perguntar apenas leituras; o modo `plan` planeja sem editar; o `acceptEdits` aceita edições e comandos comuns de arquivo; e o `bypassPermissions`, que libera tudo, destina-se apenas a máquinas isoladas — nunca é utilizado neste curso. No terminal, Shift+Tab alterna os modos. No Codex, a rede permanece desligada por padrão, o agente escreve apenas na pasta de trabalho e solicita aprovação para sair dela; o comando `/permissions` alterna para somente leitura.

Para desfazer, o Claude Code oferece `/rewind` (ou `/undo`), com uma limitação documentada: um arquivo alterado apenas por comandos de terminal não é rastreado e só pode ser recuperado por controle de versão. Em julho de 2025, dois incidentes públicos ilustraram o risco: um agente da Replit apagou o banco de dados de produção de um usuário durante um período de congelamento de código, e o Gemini CLI moveu arquivos para uma pasta inexistente, perdendo-os. Outro risco é o pacote inexistente: estudo apresentado no USENIX Security 2025 encontrou 19,7% de pacotes sugeridos por modelos de código que não existiam; reavaliação com modelos de 2026 mediu entre 3,6% e 5,0% das menções. Um atacante pode registrar o nome inventado com código malicioso.

Quanto aos dados, nos planos de consumidor do Claude (Free, Pro, Max e Ultra), quando o usuário permite o uso para melhoria dos modelos, a retenção é de cinco anos; quando não permite, de 30 dias. O Claude Code guarda ainda transcrições locais, em texto simples, por 30 dias. No ChatGPT pessoal, o treino vem ativado por padrão em `Configurações > Controles de dados`, e o Codex possui uma configuração separada, "Incluir ambientes". Planos corporativos não treinam por padrão. Dados pessoais seguem o semáforo da LGPD: dado identificável não entra em conta pessoal.

> *» IA: Bloco Table — verbatim.*

| Modo do Claude Code | O que roda sem perguntar | Uso no curso |
|---|---|---|
| Manual (`default`) | Somente leituras | Início de cada sessão |
| `plan` | Leituras; planeja sem editar | Antes de executar |
| `acceptEdits` | Leituras, edições e comandos comuns de arquivo | Depois de aprovar o plano |
| `bypassPermissions` | Tudo | Nunca |

### Exercício Prático

> *» IA: Process — passos verbatim; preservar os breadcrumbs.*

**Configurar antes de usar e decidir aprovações (15 min)**

1. Abrir o agente na pasta `ipca-projeto` em modo de planejamento (Claude Code) ou somente leitura (Codex, `/permissions`).
2. Conferir a opção de treino da conta (ChatGPT: `ChatGPT > Perfil > Configurações > Controles de dados`; Claude: configurações de privacidade da conta) e decidir.
3. Classificar como "aprovar", "aprovar com cuidado" ou "recusar": (1) ler `dados/brutos/ipca.csv`; (2) instalar `pandas`; (3) instalar um pacote de nome desconhecido; (4) apagar `dados/brutos`; (5) acessar a internet para baixar um arquivo do Banco Central.

> *» IA: Statement — critério de êxito e gabarito verbatim; preservar o emoji.*

> 🏁 Ponto de controle: modo restrito ativo e decisão de privacidade registrada. Gabarito: (1) aprovar; (2) aprovar; (3) recusar até conferir em pypi.org; (4) recusar sempre; (5) aprovar com cuidado, conferindo o endereço.

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Antes de executar qualquer comando, explique em uma linha o que ele faz, que arquivos altera e se
acessa a internet. Nunca altere nem apague nada em dados/brutos. Se sugerir instalar um pacote,
informe o endereço dele em pypi.org.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 3 — Pedir e Planejar

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe o agente configurado no Módulo 2; inicia o trabalho no caso-guia.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Redigir um brief de análise com seis itens.
2. Registrar premissas permanentes em `CLAUDE.md` ou `AGENTS.md`.
3. Exigir o plano antes da execução.
4. Solicitar e ler a explicação do código por blocos.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir; não traduzir nomes de arquivos nem comandos.*

Um brief de análise reúne seis itens: objetivo (a decisão a apoiar), dados (arquivo, formato e dicionário), regras (por exemplo, não alterar `dados/brutos`), saídas (onde salvar tabelas e gráficos), verificação (o número oficial a reproduzir) e a exigência de plano antes da execução. A documentação da Anthropic recomenda anotar apenas o que o agente não descobre sozinho e oferecer a ele "algo que possa rodar e que responda passa ou falha".

As premissas permanentes ficam num arquivo de instruções que o agente lê no início de cada sessão: `CLAUDE.md`, no Claude Code — o comando `/init` gera um rascunho e `/context all` confirma o carregamento —, ou `AGENTS.md`, no Codex, que lê esses arquivos antes de qualquer trabalho. O arquivo funciona como o manual afixado na mesa de um estagiário.

A leitura do código não exige saber escrevê-lo. Convém solicitar a explicação por blocos de até cinco linhas e verificar três pontos: de onde o dado é lido, que linhas são descartadas e que fórmula gera o número final. Os dados públicos brasileiros usam ponto e vírgula, vírgula decimal e, com frequência, codificação latin-1; o brief deve declarar isso. A ferramenta de edição de notebooks do Claude Code recusa arquivos que não estejam em UTF-8 — mais uma razão para scripts que leem o arquivo bruto sem alterá-lo.

> *» IA: Accordion — título = problema, corpo = solução; verbatim.*

| Problema | Solução |
|---|---|
| O agente começa a editar sem mostrar o plano | Voltar ao modo de planejamento e repetir o pedido com "mostre o plano e espere aprovação" |
| `CLAUDE.md` não aparece em `/context all` | Conferir se o arquivo está na raiz da pasta aberta |
| Explicação técnica demais | Solicitar "em português simples, blocos de no máximo cinco linhas" |

### Exercício Prático

> *» IA: Process — passo verbatim; texto do brief verbatim.*

**Plano do caso-guia (16 min)**

1. Com o agente em modo de planejamento na pasta `ipca-projeto`, enviar o brief: "Objetivo: calcular o IPCA acumulado de cada ano de 2020 a 2025. Dados: dados/brutos/ipca.csv (ponto e vírgula, vírgula decimal). Não altere dados/brutos. Saídas em resultados/. Verificação: 2024 deve dar 4,83% e 2025, 4,26% (IBGE). Mostre o plano em até seis passos e espere minha aprovação."
2. Gerar o arquivo de instruções (`/init` no Claude Code ou `AGENTS.md` no Codex) com as premissas do brief.

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: plano exibido em até seis passos, arquivo de instruções criado e nenhum arquivo de análise gerado antes da aprovação.

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Objetivo: [decisão que a análise apoia]. Dados: [caminho], formato [separador, decimal,
codificação], dicionário [onde está]. Regras: não alterar dados/brutos. Saídas: [pasta e arquivos].
Verificação: [número oficial e fonte]. Mostre o plano em até seis passos e espere minha aprovação.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 4 — Reprodutibilidade

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe o plano aprovado no Módulo 3; retoma o princípio "rodou não é o mesmo que acertou".

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Definir reprodutibilidade.
2. Organizar as pastas de um projeto de análise.
3. Registrar as versões das bibliotecas com o uv.
4. Testar o projeto rodando do zero.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir.*

Reprodutibilidade é a condição de outra pessoa — ou o próprio autor, meses depois — obter o mesmo resultado executando o mesmo código sobre os mesmos dados. As "Good Enough Practices in Scientific Computing" (Wilson et al., 2017), escritas para iniciantes, recomendam guardar os dados brutos, registrar todos os passos, separar dados, resultados e código em pastas próprias, explicitar dependências e usar controle de versão.

As dez regras de Sandve et al. (2013) para pesquisa computacional reprodutível incluem registrar como cada resultado foi produzido, evitar passos manuais de manipulação de dados, arquivar as versões exatas dos programas, versionar os scripts, anotar as sementes aleatórias e guardar os dados brutos por trás dos gráficos. No projeto do curso, essas recomendações se traduzem em práticas concretas, e o teste final é simples: apagar os resultados e executar tudo novamente.

> *» IA: Bloco Table — verbatim.*

| Prática | No projeto |
|---|---|
| Dados brutos intocados | `dados/brutos/` |
| Versões registradas | `pyproject.toml` e `uv.lock`, gerados pelo uv |
| Passos registrados | `analise.py` e `README.md` |
| Premissas registradas | `CLAUDE.md` ou `AGENTS.md` |
| Teste de reprodução | Apagar `resultados/` e executar `uv run analise.py` |
| Histórico | Git, com um registro (commit) por etapa |

### Exercício Prático

> *» IA: Process — passos verbatim.*

**Executar e rodar do zero (6 min)**

1. Aprovar o plano do Módulo 3 (modo `acceptEdits` ou aprovação dos comandos no Codex) e acompanhar a criação de `analise.py`, a instalação de pandas e Matplotlib pelo uv e a execução.
2. Apagar `resultados/` e solicitar: "Rode tudo de novo do zero com uv run e mostre a saída."

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: os mesmos números reaparecem após a nova execução, e `uv.lock` está presente na pasta `ipca-projeto`.

> *» IA: Knowledge Check — questão de múltipla escolha; alternativas e gabarito verbatim.*

**Questão (4 min)**

Qual prática impede que a análise funcione apenas no computador de quem a fez?

(a) Salvar o gráfico em PNG.
(b) Registrar as versões das bibliotecas (`uv.lock`) e testar rodando do zero.
(c) Usar um notebook.

**Gabarito:** (b).

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Organize este projeto para que outra pessoa o rode do zero: dados brutos intocados, código em um
script, versões registradas pelo uv, resultados em pasta própria e um README com a seção "Como
rodar". Depois apague os resultados, rode tudo de novo e mostre a saída.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 5 — Validar Resultados

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 5" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe o projeto reprodutível do Módulo 4; aprofunda o princípio "rodou não é o mesmo que acertou".

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Relatar evidências independentes sobre a taxa de acerto de agentes em análise de dados.
2. Explicar o que é um erro silencioso.
3. Solicitar testes automáticos (asserts) e contagens de controle.
4. Acionar uma revisão independente do código.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir.*

Avaliações independentes mostram que agentes de análise de dados ainda erram com frequência em tarefas reais. No DA-Code (2024), o melhor sistema avaliado acertou 30,5% das tarefas; no DSBench, 34,12% das tarefas de análise; no KramaBench, apresentado na conferência ICLR 2026, o melhor sistema alcançou 55% de acerto de ponta a ponta. Mais grave que o erro visível é o erro silencioso: numa auditoria publicada em 2026, 69,8% das execuções erradas de um agente de dados entregaram resultado com aparência normal, sem relatar falha — por exemplo, juntando dois rankings sem parear as linhas.

A percepção também engana. Ensaio controlado com programadores experientes (METR, 2025) mediu que o uso de ferramentas de IA aumentou em 19% o tempo das tarefas, enquanto os próprios participantes estimavam ganho de 20%. A sensação de acerto não substitui a medição.

A defesa consiste em quatro práticas. O assert é uma linha de teste que interrompe o script quando uma condição não se verifica — por exemplo, se o IPCA de 2024 não for 4,83%. A contagem de controle imprime o número de linhas antes e depois de cada filtro ou junção. A comparação com número oficial ancora o resultado em fonte externa. A revisão independente coloca outro avaliador, que não acompanhou a conversa, para procurar falhas. A Anthropic recomenda pedir evidência — o comando executado e a saída — em vez de aceitar a afirmação de que "todos os testes passaram".

> *» IA: Bloco Table — verbatim; não traduzir nomes de comandos.*

| Defesa | Como solicitar ao agente |
|---|---|
| Assert | "Adicione asserts: linhas lidas = 72; IPCA 2024 = 4,83 ± 0,01" |
| Contagem de controle | "Imprima o número de linhas antes e depois de cada filtro" |
| Número oficial | Comparar com IBGE, CVM, CNJ ou INMET |
| Revisão independente | Claude Code: `/code-review`; Codex: nova sessão com "revise como auditor que não confia no autor" |

### Exercício Prático

> *» IA: Process — passos verbatim.*

**O assert que falha (16 min)**

1. Solicitar ao agente um assert com valor errado de propósito (IPCA 2024 = 4,99%) e executar o script.
2. Corrigir para 4,83%, executar novamente e solicitar uma revisão independente de `analise.py`.
3. Registrar no `README.md` ao menos um apontamento da revisão.

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: `AssertionError` na primeira execução; execução sem erro na segunda; apontamento da revisão registrado no `README.md`.

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Revise [script] como um auditor que não confia no autor. Liste cinco formas de o número final estar
errado (leitura, filtro, junção, escala, fórmula) e escreva um assert para cada uma. Rode e mostre o
comando executado e a saída completa.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 5" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 6 — Síntese e Aplicação Integrada

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 6" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe todos os módulos anteriores; conclui o projeto `ipca-projeto`.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Entregar um projeto de análise reprodutível e validado.
2. Documentar como rodar, como verificar e quais são as limitações.
3. Avaliar o próprio projeto por critérios objetivos.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir.*

A atividade integradora conclui o caso-guia, articulando segurança, pedido, reprodutibilidade e validação. O produto é uma pasta que outra pessoa pode receber, ler e executar com um único comando, obtendo os mesmos números e conferindo-os com o IBGE.

Diferenças de até 0,01 ponto percentual entre o acumulado calculado e o valor publicado podem ocorrer em alguns anos anteriores a 2024, porque as taxas mensais são divulgadas arredondadas em duas casas decimais. Essa diferença deve constar como limitação no README e ser tratada com tolerância no teste, e não eliminada por ajuste do número.

### Exercício Prático

> *» IA: Process — passos verbatim; preservar os breadcrumbs.*

**Atividade integradora (16 min)**

1. (Módulo 2) Confirmar o modo restrito e os controles de dados.
2. (Módulo 3) Atualizar o arquivo de instruções com as premissas do IPCA.
3. (Módulo 4) Solicitar gráfico de barras anual de 2020 a 2025 salvo em `resultados/` e rodar do zero.
4. (Módulo 5) Manter os asserts de 2024 e 2025 e registrar a revisão independente.
5. Solicitar o `README.md` com objetivo, dados, como rodar (`uv run analise.py`), verificação e limitações.

> *» IA: Checklist — tabela de critérios verbatim.*

| Critério | Atendido? |
|---|---|
| `dados/brutos/ipca.csv` intocado | |
| `uv.lock` presente e projeto roda do zero | |
| Asserts de 4,83% e 4,26% passando | |
| Gráfico em `resultados/` | |
| README com como rodar, verificação e limitações | |

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: os cinco critérios atendidos; idealmente, outra pessoa executa o projeto seguindo apenas o README.

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Escreva o README.md deste projeto com as seções: Objetivo, Dados (fonte, data de download, formato),
Como rodar (comandos exatos), Verificação (números oficiais e asserts), Resultados e Limitações.
Depois apague resultados/, rode tudo do zero e confirme que os asserts passam.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 6" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Encerramento

> *» IA: Bloco Text — verbatim.*

O curso apresentou a análise de dados com agentes de código como um método: pedir com brief, aprovar com segurança, registrar para reproduzir e validar antes de confiar. Recomenda-se praticar com bases públicas de gabarito conhecido e manter sempre os dados brutos intocados e os dados pessoais fora de contas pessoais.

Para aprofundamento, o *Hands On* deste assunto trabalha bases da CVM e do INMET; *Claude Code no VSCode* e *ChatGPT CODEX* aprofundam as ferramentas; para modelagem estatística e previsão, recomenda-se recorrer a especialista.

> *» IA: Statement — citação final verbatim.*

> **Síntese:** o agente escreve o código; o projeto só é confiável quando roda de novo e confere com a fonte.
