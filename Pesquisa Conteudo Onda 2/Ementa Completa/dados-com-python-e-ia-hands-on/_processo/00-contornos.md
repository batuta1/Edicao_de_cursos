# 00 — Contornos do curso Dados com Python e IA

Documento de partida compartilhado pelas duas trilhas.

## Origem do pedido

| Campo | Valor |
|---|---|
| Registro no catálogo | `novos-cursos-iaclube-priorizacao-v6.json` → `"id": "dados-com-python-e-ia-hands-on"` |
| Nome no catálogo | Dados com Python e IA - Hands On (o par Essentials é produzido na mesma rodada) |
| Onda / ranking / score | Onda 3 · ranking 47 · 73 pontos (demanda 22, ferramenta 20, base 15, lacuna 12, esforço 4); trazido para a Onda 2 para fechar a T8 |
| Tema | Dados com IA |
| Ferramentas do catálogo | Claude Code e Codex |
| Competência | Analisar dados com código gerado por IA |
| Tarefa observável | Conduzir uma análise reprodutível em Python com agente de código e validar resultados. |
| Base confiável | Docs da Anthropic e OpenAI |

## Objeto base

**Análise de dados reprodutível em Python, com o código escrito por um agente de IA e conferido
pelo participante, que não programa.** O ciclo é **brief → plano → código → execução → validação →
rodar do zero → registrar**, numa pasta de projeto que outra pessoa consegue rodar de novo.

- **Agentes:** Claude Code (Anthropic) e Codex (OpenAI). Ambos leem arquivos, escrevem código e
  executam comandos no computador do participante, sob regras de permissão.
- **O participante não escreve código:** pede, aprova, lê no nível de leigo ("o que este bloco faz
  com os dados") e confere.
- **Python mínimo:** pandas (tabelas), Matplotlib (gráficos), openpyxl (Excel), uv (instala Python e
  bibliotecas, registra versões). Scripts `.py` são o formato principal; notebooks entram como
  alternativa, com as limitações documentadas.
- **Eixo do curso:** validação. Estudos independentes mostram que agentes de dados entregam
  resultados errados com aparência normal (69,8% das execuções zeradas no estudo "Fail Loudly",
  2026) e que só 24,11% de 863.878 notebooks do GitHub rodaram sem erro (Pimentel et al., 2021).

## Público-alvo

| Trilha | Posição | Antes | Depois | Público |
|---|---|---|---|---|
| T8 — IA aplicada ao trabalho: planilhas e dados | 6 de 6 (último) | IA para Análise de Dados - Essentials | — | Analistas, financeiro e planejamento, pesquisadores |
| F2 — Planilhas, finanças e indicadores | 7 de 7 (último) | Análise financeira e indicadores com IA - Hands On | — | Finanças e negócios |
| R4 — Dados, evidências e análise de impacto regulatório | 6 de 6 (último) | Claude Excel - Hands On | — | Servidores públicos e equipes de regulação |
| TE3 — Dados, scripts e cálculo técnico | 4 de 6 | IA para Análise de Dados - Essentials | IA em projetos de engenharia - Hands On | Engenheiros e técnicos |

Consequência de design: exemplos de finanças (CVM), setor público (inflação oficial, dados do
governo) e engenharia (INMET). Na R4 o aluno pode não ter feito *IA para Análise de Dados*; o
Módulo 1 retoma em um parágrafo o princípio da conferência.

## Pré-requisitos

- *IA para Análise de Dados - Essentials* (exceto R4) e Excel básico.
- Não sabe programar. O curso explica o mínimo de terminal: abrir, colar um comando, ler a resposta.
- Para o Hands-on: o Essentials deste assunto.

## Recursos necessários e rotas

| Rota | O que é | Custo (17/11/2026) | Instalação |
|---|---|---|---|
| A — Claude Code no app Claude Desktop (aba "Code") | Agente sem terminal, numa pasta local | Claude Pro R$ 110/mês (R$ 92/mês no anual); o Free não inclui Claude Code | App Claude (macOS/Windows) + uv; Git for Windows recomendado no Windows |
| B — Codex no app de desktop do ChatGPT | Modo Codex no menu do ChatGPT, pasta local | Free: GPT-6 Luna no app de desktop, "sujeito a lançamento gradual"; Plus R$ 99,90/mês para uso pleno (CLI, IDE, web) | App ChatGPT (macOS/Windows/Linux) + uv |
| C — Terminal (Claude Code CLI ou Codex CLI) | Mesmo agente, no terminal | Mesmos planos | Instalador oficial + uv |

Requisitos do Claude Code: macOS 13+, Windows 10 1809+ (ou Ubuntu 20.04+), 4 GB de RAM, internet.
Rota recomendada para iniciante: A ou B (sem terminal para o agente). O terminal aparece só para o
uv (um comando de instalação e `uv run`).

Não há rota 100% gratuita garantida: o Claude Code não está no Free; o Codex Free depende de
liberação gradual. Isso é dito ao aluno no Módulo 0.

## Natureza e carga horária

- **Autoinstrucional.**
- **Essentials:** 100–130 min, 4–6 módulos + síntese (prompt-mestre Articulate).
- **Hands-on:** 90–120 min, 4 oficinas + Projeto Final.
- Tempo de espera do agente (instalar bibliotecas, executar) fora da MET; declarado.

## Escopo — o que NÃO é deste curso

| Fica fora | Onde está |
|---|---|
| Análise sem código (ChatGPT Análise de dados, Julius) | IA para Análise de Dados (aqui: ponto de partida e "quando passar para código") |
| Uso geral do Claude Code (VS Code, comandos, CLAUDE.md para software) | Claude Code no VSCode - Essentials e Hands On |
| Uso geral do Codex (CLI, nuvem, GitHub, revisão de PR) | ChatGPT CODEX - Essentials e Hands On |
| Aprender Python como linguagem | Fora; só o mínimo para ler e conferir |
| Python no Excel | Cursos de Excel (só comparação) |
| Apps e painéis publicados | Vibe Coding, Replit Agent |
| Machine learning | Fora; "quando procurar um especialista" |
| Cursor, Copilot, Gemini Code Assist | Cursos próprios (só comparação) |

## Material-fonte

`Pesquisa Conteudo Onda 2/conteudo-bruto/dados-com-python-e-ia-hands-on/` — conteúdo bruto (duas
rodadas, 17/11/2026) + 27 PDFs e bases. Fatos usados:

| Fato | Fonte |
|---|---|
| Planos que dão acesso ao Claude Code; requisitos de sistema; comandos de instalação; Git for Windows | code.claude.com/docs (quickstart, setup, desktop-quickstart) |
| Modos de permissão (`default`/Manual, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`); Shift+Tab; deny rules | code.claude.com/docs/permission-modes |
| `/rewind` e limitação: "A file that only Bash commands changed isn't tracked" | code.claude.com/docs/checkpointing |
| NotebookEdit: uma célula por vez; limpa saídas; recusa arquivo não UTF-8; não conecta ao kernel | tools-reference, vs-code |
| `/init`, `/context all`, CLAUDE.local.md | memory |
| "Give Claude something it can run that comes back pass or fail"; pedir evidência; `/code-review` em subagente | best-practices |
| Treino e retenção (consumidor 5 anos se permitir; 30 dias se não; local `~/.claude/projects/` 30 dias) | data-usage |
| Codex: Local/Worktree/Cloud; rede desligada por padrão; preset Auto; `/permissions` read-only; AGENTS.md; planos e limites | learn.chatgpt.com/docs |
| Codex "Incluir ambientes" separado do controle de treino | Ajuda OpenAI 5722486 |
| uv: instaladores oficiais | docs.astral.sh/uv |
| Benchmarks: DA-Code 30,5%; DSBench 34,12%; KramaBench 55% / 62%; Fail Loudly 69,8%; DSDBench | PDFs na pasta |
| Pacotes inexistentes: 19,7% (USENIX 2025); 3,6–5,0% (2026) | PDFs na pasta |
| Reprodutibilidade: Pimentel 24,11% / 4,03%; Sandve 10 regras; Rule 10 regras; Wilson "Good enough" | PDFs na pasta |
| Caso Anthropic: finanças descrevendo fluxos em texto simples para o Claude Code executar | PDF "How Anthropic teams use Claude Code" |
| Incidentes Replit e Gemini CLI (jul/2025) | Imprensa / AI Incident Database |
| METR: desenvolvedores experientes 19% mais lentos com IA, achando-se 20% mais rápidos | PDF METR 2025 |

## Bases e gabaritos (conferidos por script em 17/11/2026)

| Base | Link | Formato | Gabarito |
|---|---|---|---|
| C4 IPCA mensal (BCB SGS 433) | `https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2020&dataFinal=31/12/2025` | CSV UTF-8, `;`, vírgula decimal | 2024 = 4,83%; 2025 = 4,26% (IBGE) |
| C1 CVM DFP 2024 | `https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2024.zip` (13,4 MB; 19 CSVs latin-1) | DRE consolidada: 32.776 linhas, 467 empresas | Conta 3.11.01, ÚLTIMO: 460 linhas, 458 empresas (2 linhas duplicadas idênticas); 8 em UNIDADE, 452 em MIL; top 5 em reais: Petrobras 36,606 bi, Vale 31,592, BB 26,359, Bradesco 17,253, Itaúsa 14,778; soma 303,9 bi; 95 com prejuízo; sem converter a escala, Vivara (R$ 653,4 mi) fica em 1º |
| C1b Cadastro CVM | `https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv` | 2.680 linhas, 2.569 códigos únicos, 107 códigos repetidos | Junção DRE × cadastro: 4 empresas sem cadastro; lucro por setor (preferindo registro ATIVO): Bancos R$ 60,9 bi; Petróleo e Gás 50,9; Energia Elétrica 36,5; Extração Mineral 31,4; sem converter a escala, "Comércio (Atacado e Varejo)" aparece com R$ 667 bi |
| C3 INMET 2024 | `https://portal.inmet.gov.br/uploads/dadoshistoricos/2024.zip` (102,8 MB; 565 CSVs) | 8 linhas de metadados; latin-1; `;`; vírgula decimal; hora UTC | DF: 5 estações (A001 Brasília, A042 Brazlândia, A045 Águas Emendadas, A046 Gama, A047 Paranoá); 8.784 linhas cada (2024 bissexto); vazios na temperatura de bulbo seco: 26, 235, 453, 66, 416; média anual 21,98 / 22,32 / 21,85 / 22,60 / 22,29 °C; máxima horária 36,1 / 35,2 / 37,3 / 37,5 / 37,2 °C (maior: Gama 37,5) |

## Pendências de validação herdadas

1. Codex no Free brasileiro ("subject to rollout"): disponibilidade e limites reais.
2. Suporte do Codex a notebooks: não documentado.
3. Comandos `uv init`, `uv add`, `uv run` e instalação de Python pelo uv (página não lida além da
   instalação).
4. Rótulos do app Claude Desktop (aba Code, seleção de pasta, modo Plan) e do app ChatGPT (menu
   Codex, "Work in") em português.
5. Preço do Claude Pro em dólar; Team/Enterprise.
6. Nenhum exercício executado com agente real nesta rodada.
