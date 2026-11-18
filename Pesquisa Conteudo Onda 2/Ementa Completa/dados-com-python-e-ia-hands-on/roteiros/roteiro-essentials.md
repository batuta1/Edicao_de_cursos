# Dados com Python e IA — Essentials (roteiro final)

**Público-Alvo:** analistas, financeiro e planejamento, pesquisadores (T8); finanças e negócios
(F2); servidores públicos e equipes de regulação (R4); engenheiros e técnicos (TE3).

**Objetivo Geral:** capacitar o participante, que não programa, a conduzir uma análise de dados
reprodutível em Python com um agente de código (Claude Code ou Codex): pedir com um brief, aprovar
com segurança, ler o código no nível de leigo, organizar o projeto para rodar de novo do zero e
validar os resultados contra número oficial.

**Pré-requisitos:** *IA para Análise de Dados - Essentials* (recomendado; na trilha R4, o Módulo 1
retoma o essencial) e Excel básico. Nenhuma programação. Plano pago de uma das ferramentas (Claude
Pro ou ChatGPT Plus) ou acesso ao Codex no plano Free do ChatGPT, se liberado na conta.

## Estrutura do Curso

| Nível | Módulos | Tempo |
|---|---|---|
| Preparação | Módulo 0 — Preparação e verificação inicial | 7 min |
| Nível 1 — Fundamentos | Módulo 1 — Por que código e o que é um agente; Módulo 2 — O agente no seu computador: segurança e dados | 34 min |
| Nível 2 — Método | Módulo 3 — Pedir e planejar; Módulo 4 — Reprodutibilidade | 32 min |
| Nível 3 — Confiança | Módulo 5 — Validar resultados; Módulo 6 — Síntese e aplicação integrada | 38 min |
| **Total** | | **111 min** |

Fio condutor: "rodou não é o mesmo que acertou" é plantado no Módulo 1 e retomado nos Módulos 4 e 5.
Caso-guia: o projeto `ipca-projeto`, com a série mensal do IPCA (Banco Central), atravessa os Módulos
3 a 6; gabarito do IBGE: 4,83% em 2024 e 4,26% em 2025.

---

## Módulo 0 — Preparação e verificação inicial

### 0.1 Escolher a rota

- **📸 Sugestão de Prints:** (a) app Claude Desktop com a aba "Code" destacada no topo da barra
  lateral e o seletor de pasta aberto; (b) app de desktop do ChatGPT com o menu de modos aberto e a
  opção "Codex" destacada.

| Rota | Onde | Plano necessário (17/11/2026) | Requisitos |
|---|---|---|---|
| A | App Claude Desktop, aba Code | Claude Pro (R$ 110/mês; R$ 92/mês no anual) ou superior; o Free não inclui Claude Code | macOS 13+ ou Windows 10 1809+; 4 GB de RAM; Git for Windows recomendado |
| B | App de desktop do ChatGPT, modo Codex | Free com acesso limitado ("sujeito a lançamento gradual"); Plus (R$ 99,90/mês) para uso pleno | macOS, Windows ou Linux |
| C | Terminal (Claude Code CLI ou Codex CLI) | Mesmos planos | Instalador oficial de cada ferramenta |

Recomenda-se a rota A ou B: o agente funciona sem terminal. O terminal aparece apenas para o uv.

### 0.2 O uv e a pasta do projeto

- **📸 Sugestão de Prints:** janela do PowerShell com o comando de instalação do uv e, abaixo, a
  resposta de `uv --version` exibindo um número de versão.

O uv é o gerenciador oficial da Astral que instala o Python, as bibliotecas e registra as versões
usadas. Instalação (página oficial do uv):

- Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- macOS: `curl -LsSf https://astral.sh/uv/install.sh | sh`

Fechar e reabrir o terminal; `uv --version` deve exibir um número. Criar a pasta `ipca-projeto` com a
subpasta `dados/brutos` e salvar nela `ipca.csv`, baixado de
`https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2020&dataFinal=31/12/2025`.

### Solução de Problemas

| Problema | Solução |
|---|---|
| "irm não é reconhecido" | O comando foi colado no Prompt de Comando (CMD); abrir o PowerShell |
| `uv` não encontrado após instalar | Fechar e reabrir o terminal |
| App pede para assinar plano ao abrir Code/Codex | A conta não tem o plano exigido; ver a tabela de rotas |

### Pílula Hands-on — Verificação inicial (7 min)

1. Abrir a rota escolhida e localizar onde se seleciona a pasta do projeto.
2. Rodar `uv --version`.
3. Conferir `ipca-projeto/dados/brutos/ipca.csv`.

**Critério de êxito:** agente aberto, uv respondendo e arquivo na pasta.

## Descrição

- **Objetivos da Aula:** apresentar as rotas, custos e requisitos; instalar o uv; montar a pasta.
- **Habilidades Esperadas:** escolher a própria rota e verificar sozinho que o ambiente está pronto.

---

## Módulo 1 — Por que código e o que é um agente de código

### 1.1 Quando passar do sem código para o código

- **📸 Sugestão de Prints:** pasta `ipca-projeto` no Explorador de Arquivos, com `dados/brutos`,
  `analise.py`, `resultados/` e `README.md` visíveis.

Na análise sem código (*IA para Análise de Dados*), o resultado vive numa conversa. Recomenda-se
passar para código quando a análise precisa ser refeita (todo mês, por outra pessoa), envolve vários
arquivos ou arquivos grandes, ou precisa ser auditada linha a linha. O código transforma a conversa
numa receita guardada em arquivo.

Um agente de código é um programa de IA que "lê o código, edita arquivos, executa comandos" no
computador do usuário (documentação do Claude Code). O Claude Code (Anthropic) e o Codex (OpenAI)
recebem o pedido em português, escrevem o script em Python, executam-no e mostram o resultado. O
participante não digita código: aprova, lê no nível de leigo e confere.

### 1.2 Vocabulário mínimo

| Termo | O que é | Analogia |
|---|---|---|
| Script (`.py`) | Receita completa num arquivo, executada do começo ao fim | Receita impressa |
| Notebook (`.ipynb`) | Caderno com células de código, texto e gráficos | Caderno de laboratório |
| pandas | Biblioteca de tabelas | A planilha dentro do Python |
| Matplotlib | Biblioteca de gráficos | O módulo de gráficos |
| uv | Instala Python e bibliotecas e registra versões | A lista de compras com marca e tamanho |
| Ambiente virtual | Caixa de bibliotecas só daquele projeto | Gaveta separada por cliente |

O curso usa scripts como formato principal: estudo de 2021 com 863.878 execuções de notebooks
públicos verificou que apenas 24,11% rodaram sem erro e 4,03% reproduziram os resultados.

Princípio do curso: **rodou não é o mesmo que acertou.** Um código pode executar sem erro sobre uma
premissa errada.

### Avaliação — questão (4 min)

Em qual situação a passagem para código mais se justifica?

(a) Uma pergunta única sobre uma planilha pequena.
(b) Um indicador mensal que precisa ser refeito todo mês, a partir de doze arquivos, por pessoas
diferentes.
(c) Um gráfico rápido para uma conversa.

**Gabarito:** (b) — repetição, vários arquivos e mais de um executor.

## Descrição

- **Objetivos da Aula:** distinguir análise sem código e com código; apresentar agente, script,
  notebook e bibliotecas; plantar o princípio "rodou ≠ acertou".
- **Habilidades Esperadas:** decidir sozinho quando uma análise deve virar projeto em código.

---

## Módulo 2 — O agente no seu computador: segurança e dados

### 2.1 Permissões e desfazer

- **📸 Sugestão de Prints:** terminal do Claude Code com a barra de status mostrando "plan mode on"
  após Shift+Tab; no Codex, o resultado do comando `/permissions` com a opção somente leitura.

O agente pode ler, criar, alterar e apagar arquivos e executar comandos. As permissões controlam o
que ele faz sem perguntar:

| Claude Code (modo) | O que roda sem perguntar | Uso |
|---|---|---|
| Manual (`default`) | Só leituras | Trabalho sensível; início |
| `plan` | Leituras (planeja sem editar) | Antes de executar |
| `acceptEdits` | Leituras, edições e comandos de arquivo comuns | Quando o plano foi aprovado |
| `bypassPermissions` | Tudo | Só em máquinas isoladas — nunca neste curso |

No CLI, Shift+Tab alterna os modos. No Codex, a rede fica desligada por padrão, o agente escreve só
na pasta de trabalho e pede aprovação para sair dela; `/permissions` alterna para somente leitura.
Para desfazer, o Claude Code oferece `/rewind` (ou `/undo`), com uma limitação documentada: "um
arquivo alterado apenas por comandos Bash não é rastreado". Por isso, trabalha-se sempre em cópia
dos dados e com versionamento (Módulo 4).

### 2.2 Riscos documentados e dados

Em julho de 2025, dois incidentes públicos envolveram agentes: um agente da Replit apagou o banco de
dados de produção de um usuário durante um "congelamento" de código, e o Gemini CLI moveu arquivos
para uma pasta inexistente, perdendo-os. Outro risco é o pacote inexistente: estudo apresentado no
USENIX Security 2025 encontrou 19,7% de pacotes sugeridos por modelos de código que não existiam;
reavaliação com modelos de 2026 mediu de 3,6% a 5,0%. Um atacante pode registrar o nome inventado.

Quanto aos dados: no Claude em planos de consumidor (Free, Pro, Max, Ultra), se o usuário permitir o
uso para melhoria dos modelos, a retenção é de 5 anos; se não permitir, 30 dias; o Claude Code guarda
transcrições locais em texto simples por 30 dias. No ChatGPT pessoal, o treino vem ativado por padrão
(`Configurações > Controles de dados`), e o Codex tem uma configuração separada, "Incluir ambientes".
Planos corporativos não treinam por padrão. Dados pessoais seguem o semáforo da LGPD.

### Pílula Hands-on — Configurar antes de usar (7 min)

1. Abrir o agente na pasta `ipca-projeto` e colocá-lo em modo de planejamento ou somente leitura.
2. Conferir a opção de treino da conta (Claude: configurações de privacidade da conta — caminho a
   conferir na interface; ChatGPT: `Configurações > Controles de dados`) e decidir.

**Critério de êxito:** modo restrito ativo e decisão de privacidade registrada.

### Discussão orientada (8 min)

Classificar como "aprovar", "aprovar com cuidado" ou "recusar": (1) ler `dados/brutos/ipca.csv`;
(2) instalar `pandas`; (3) instalar um pacote de nome desconhecido; (4) apagar `dados/brutos`;
(5) acessar a internet para baixar um arquivo do Banco Central.

**Gabarito:** (1) aprovar; (2) aprovar; (3) recusar até conferir em pypi.org; (4) recusar sempre;
(5) aprovar com cuidado, conferindo o endereço.

## Descrição

- **Objetivos da Aula:** apresentar permissões, sandbox, desfazer e seus limites, riscos
  documentados e regras de dados de cada agente.
- **Habilidades Esperadas:** configurar o agente em modo restrito e decidir sozinho cada pedido de
  aprovação.

---

## Módulo 3 — Pedir e planejar

### 3.1 O brief e o arquivo de instruções

- **📸 Sugestão de Prints:** arquivo `CLAUDE.md` (ou `AGENTS.md`) aberto no editor com as seções
  "Dados", "Premissas" e "Verificação".

Um brief de análise tem seis itens: objetivo (decisão a apoiar), dados (arquivo, formato, dicionário),
regras (não alterar `dados/brutos`), saídas (onde salvar tabelas e gráficos), verificação (número
oficial) e plano antes de executar. As premissas permanentes ficam num arquivo de instruções que o
agente lê no início de cada sessão: `CLAUDE.md` (Claude Code; `/init` gera um rascunho e `/context
all` confirma que foi carregado) ou `AGENTS.md` (Codex, que "lê os arquivos AGENTS.md antes de
qualquer trabalho"). A Anthropic recomenda anotar só o que o agente não descobre sozinho e dar a ele
"algo que ele possa rodar e que responda passa ou falha".

### 3.2 Ler o código como leigo e os dados brasileiros

- **📸 Sugestão de Prints:** resposta do agente explicando `analise.py` em blocos numerados de até
  cinco linhas.

Não se exige saber escrever código, e sim pedir a explicação por blocos e conferir três pontos: de
onde o dado é lido, que linhas são descartadas e que fórmula gera o número final. Dados públicos
brasileiros usam ponto e vírgula, vírgula decimal e, muitas vezes, codificação latin-1; o brief deve
declarar isso. A ferramenta de edição de notebooks do Claude Code recusa arquivos que não estejam em
UTF-8, mais um motivo para usar scripts que leem o arquivo bruto sem alterá-lo.

### Solução de Problemas

| Problema | Solução |
|---|---|
| O agente começa a editar sem mostrar o plano | Voltar ao modo de planejamento e repetir o pedido com "mostre o plano e espere aprovação" |
| `CLAUDE.md` não aparece em `/context all` | Conferir se está na raiz da pasta aberta |
| Explicação técnica demais | Pedir "em português simples, blocos de no máximo cinco linhas" |

### Pílula Hands-on — Plano do caso-guia (6 min)

Com o agente em modo de planejamento na pasta `ipca-projeto`, enviar o brief:

"Objetivo: calcular o IPCA acumulado de cada ano de 2020 a 2025. Dados: `dados/brutos/ipca.csv`
(ponto e vírgula, vírgula decimal). Não altere `dados/brutos`. Saídas em `resultados/`. Verificação:
2024 deve dar 4,83% e 2025, 4,26% (IBGE). Mostre o plano em até seis passos e espere minha aprovação."

**Critério de êxito:** plano exibido, nenhum arquivo criado ainda.

## Descrição

- **Objetivos da Aula:** demonstrar o brief, o arquivo de instruções, o plano antes da execução e a
  leitura de código por blocos.
- **Habilidades Esperadas:** redigir sozinho um brief de seis itens e exigir o plano antes da execução.

---

## Módulo 4 — Reprodutibilidade

### 4.1 O que é e como se organiza

- **📸 Sugestão de Prints:** árvore da pasta `ipca-projeto` com `dados/brutos`, `resultados`,
  `analise.py`, `pyproject.toml`, `uv.lock`, `README.md` e `CLAUDE.md`.

Reprodutibilidade é a condição de outra pessoa — ou o próprio autor, meses depois — obter o mesmo
resultado rodando o mesmo código sobre os mesmos dados. As "Good Enough Practices in Scientific
Computing" (Wilson et al., 2017) recomendam: guardar os dados brutos, registrar todos os passos,
colocar dados em `data`, resultados em `results` e código em `src`, explicitar dependências e usar
controle de versão. As dez regras de Sandve et al. (2013) incluem "evitar passos manuais de
manipulação de dados", "arquivar as versões exatas dos programas", "anotar as sementes aleatórias"
e "guardar os dados brutos por trás dos gráficos".

| Prática | No projeto |
|---|---|
| Dados brutos intocados | `dados/brutos/` |
| Versões registradas | `pyproject.toml` e `uv.lock` (gerados pelo uv) |
| Passos registrados | `analise.py` + `README.md` |
| Premissas registradas | `CLAUDE.md` ou `AGENTS.md` |
| Teste de reprodução | Apagar `resultados/` e rodar `uv run analise.py` |
| Histórico | Git (um "commit" por etapa) |

### Pílula Hands-on — Executar e rodar do zero (6 min)

1. Aprovar o plano do Módulo 3 (modo `acceptEdits` ou equivalente) e acompanhar a criação de
   `analise.py`, a instalação de pandas e Matplotlib pelo uv e a execução.
2. Apagar `resultados/` e pedir: "Rode tudo de novo do zero com uv run e mostre a saída."

**Critério de êxito:** os mesmos números reaparecem; `uv.lock` existe na pasta.

### Avaliação — questão (4 min)

Qual prática impede que a análise "funcione só no computador de quem fez"?

(a) Salvar o gráfico em PNG. (b) Registrar as versões das bibliotecas (`uv.lock`) e testar rodando do
zero. (c) Usar um notebook.

**Gabarito:** (b).

## Descrição

- **Objetivos da Aula:** apresentar reprodutibilidade, organização de pastas, registro de versões e o
  teste de rodar do zero.
- **Habilidades Esperadas:** montar sozinho a pasta de um projeto reprodutível e verificar que ele
  roda do zero.

---

## Módulo 5 — Validar resultados

### 5.1 O que os estudos mostram

- **📸 Sugestão de Prints:** saída do terminal com `AssertionError` após um assert com valor errado
  de propósito, e em seguida a execução correta.

Agentes de análise de dados ainda erram com frequência em tarefas reais: o melhor sistema avaliado no
DA-Code (2024) acertou 30,5%; no DSBench, 34,12% das tarefas de análise; no KramaBench (ICLR 2026), o
melhor sistema chegou a 55% de acerto de ponta a ponta. Mais grave é o erro silencioso: numa auditoria
publicada em 2026, 69,8% das execuções erradas de um agente de dados entregaram resultado com
aparência normal, sem relatar falha — por exemplo, juntando dois rankings sem parear as linhas. Um
ensaio controlado com programadores experientes (METR, 2025) mediu que o uso de IA aumentou o tempo
das tarefas em 19%, enquanto os participantes estimavam ganho de 20%: a sensação de acerto não
substitui a medição.

### 5.2 As quatro defesas

| Defesa | Como pedir ao agente |
|---|---|
| Assert (teste que para o script se falhar) | "Adicione asserts: linhas lidas = 72; IPCA 2024 = 4,83% ± 0,01" |
| Soma e contagem de controle | "Imprima linhas antes e depois de cada filtro" |
| Número oficial | Comparar com IBGE, CVM, CNJ, INMET |
| Revisão independente | Claude Code: `/code-review` (revisor que não viu a conversa); Codex: nova sessão "revise como auditor que não confia no autor" |

A Anthropic recomenda pedir evidência — "o comando que rodou e a saída" — em vez de aceitar "todos os
testes passaram".

### Pílula Hands-on — O assert que falha (6 min)

1. Pedir ao agente um assert com valor errado de propósito (IPCA 2024 = 4,99%) e rodar.
2. Corrigir para 4,83% e rodar de novo; pedir uma revisão independente do `analise.py`.

**Critério de êxito:** `AssertionError` na primeira execução; execução limpa na segunda; ao menos um
apontamento da revisão registrado no `README.md`.

## Descrição

- **Objetivos da Aula:** apresentar evidências independentes sobre erros de agentes, o erro
  silencioso e as quatro defesas.
- **Habilidades Esperadas:** exigir sozinho asserts, contagens, comparação com fonte oficial e
  revisão independente antes de confiar no número.

---

## Módulo 6 — Síntese e aplicação integrada

### 6.1 Atividade integradora

- **📸 Sugestão de Prints:** `README.md` final do `ipca-projeto` com as seções Objetivo, Dados,
  Como rodar, Resultados, Verificação e Limitações.

A atividade fecha o caso-guia, integrando os módulos:

1. (Módulo 2) Confirmar modo restrito e controles de dados.
2. (Módulo 3) Atualizar o `CLAUDE.md`/`AGENTS.md` com as premissas do IPCA.
3. (Módulo 4) Pedir gráfico de barras anual 2020–2025 salvo em `resultados/` e rodar do zero.
4. (Módulo 5) Manter os asserts de 2024 e 2025 e registrar a revisão independente.
5. Pedir o `README.md` com "Como rodar" (`uv run analise.py`) e limitações (diferenças de até 0,01
   p.p. em anos anteriores, por arredondamento das taxas mensais).

| Critério | Atendido? |
|---|---|
| `dados/brutos/ipca.csv` intocado | |
| `uv.lock` presente e projeto roda do zero | |
| Asserts de 4,83% e 4,26% passando | |
| Gráfico em `resultados/` | |
| README com como rodar, verificação e limitações | |

### Avaliação (4 min)

Autoavaliação pela tabela acima; idealmente, outra pessoa roda o projeto seguindo só o README.

## Descrição

- **Objetivos da Aula:** integrar pedido, segurança, reprodutibilidade e validação num projeto.
- **Habilidades Esperadas:** entregar sozinho um projeto pequeno que outra pessoa consegue rodar e
  conferir.

---

## Encerramento

O curso apresentou a análise de dados com agentes de código como um método: pedir com brief,
aprovar com segurança, registrar para reproduzir e validar antes de confiar. Recomenda-se praticar
com bases públicas de gabarito conhecido e manter sempre os dados brutos intocados.

Para aprofundamento, o *Hands On* deste assunto trabalha bases da CVM e do INMET; *Claude Code no
VSCode* e *ChatGPT CODEX* aprofundam as ferramentas; para modelagem estatística, recomenda-se
recorrer a especialista.

> **Síntese:** o agente escreve o código; o projeto só é confiável quando roda de novo e confere com
> a fonte.

---

## Rastreabilidade da auditoria

| Achado | Destino |
|---|---|
| E1 Requisitos ocultos | Módulo 0, 0.1 |
| E2 Instalação frágil | Módulo 0, 0.2 (uv; apps de desktop) |
| E3 Segurança ausente | Módulo 2 (antes do primeiro uso no Módulo 3) |
| E4 Privacidade ausente | Módulo 2, 2.2 |
| E5 Pedido e plano | Módulo 3 |
| E6 Reprodutibilidade | Módulo 4 |
| E7 Validação rasa | Módulo 5 |
| E8 Dados BR | Módulo 3, 3.2 |
| E9 Quando passar para código | Módulo 1, 1.1 |
| E10 Aula de pandas | Removida; Módulo 1, 1.2 (vocabulário) e 3.2 (ler como leigo) |
| E11 Sem gabarito | Caso-guia IPCA (Módulos 3–6) |
| E12 Carga horária | 111 min (ver `carga-horaria/carga-horaria-essentials.md`) |

Decisão consciente: notebooks não são o formato principal (limitações de edição e dado de
reprodutibilidade de Pimentel et al.); aparecem como alternativa no Hands-on.
