# 00 — Contornos do curso Deep Research - Hands On

Documento de partida compartilhado pelas duas trilhas. Tudo o que vem depois (v1.0, auditoria,
roteiros, carga horária, ementa) se apoia nestes campos.

## Origem do pedido

| Campo | Valor |
|---|---|
| Registro no catálogo | `novos-cursos-iaclube-priorizacao-v6.json` → `"id": "deep-research-hands-on"` |
| Nome no catálogo | Deep Research - Hands On |
| Onda / ranking / score | Onda 2 · ranking 17 · 84 pontos (demanda 30, ferramenta 20, base 15, lacuna 12, esforço 7) |
| Tema / linha prioritária | Pesquisa com IA / Pesquisa com IA |
| Ferramentas do catálogo | ChatGPT, Gemini e Perplexity (modos de pesquisa profunda) |
| Competência | Conduzir pesquisas profundas e avaliá-las |
| Tarefa observável | Produzir um relatório com deep research e auditar fontes, lacunas e erros. |
| Base confiável | Docs dos três fornecedores |
| Observação do catálogo | Pré-requisito: Perplexity - Essentials ou NotebookLM - Essentials. |

## Objeto base

**Pesquisa profunda (deep research) com agentes de IA, com auditoria do relatório** — o ciclo
**brief → plano → execução → auditoria → correção**:

1. **Brief** — pergunta, decisão que o relatório apoia, recorte, fontes obrigatórias e excluídas,
   formato e critério de conclusão; sem dados pessoais.
2. **Plano** — revisar e editar o plano proposto pelo agente (ChatGPT e Gemini documentam essa
   etapa); escolher fontes e restrição de sites quando houver.
3. **Execução** — acompanhar, exportar e guardar prompt, plano, relatório e horário.
4. **Auditoria** — numerar afirmações verificáveis, abrir cada citação, classificar suporte
   (integral, parcial, ausente, fonte inacessível), conferir autoria, data, vigência e fonte
   primária, listar lacunas.
5. **Correção** — reescrever o que não se sustenta, separar fato, inferência e lacuna, registrar
   a trilha de evidências.

As três ferramentas são tratadas como **variações do mesmo tipo de agente**, escolhidas por tarefa,
não como "vencedora": ChatGPT deep research (plano editável, restrição/priorização de sites,
exportação Markdown/Word/PDF), Gemini Deep Research (plano editável, Search/Gmail/Drive, Export to
Docs, Audio Overview) e Perplexity Deep Research (menu +, citação inline, 1 pesquisa/mês no
gratuito). O relatório da IA é **rascunho pesquisado, não autoridade final**.

## Público-alvo

O curso aparece em duas trilhas (`trilhas.json`):

| Trilha | Posição | Antes | Depois | Público |
|---|---|---|---|---|
| T2 — Pesquisa com IA | 3 de 5 | Perplexity - Essentials, NotebookLM - Essentials | Checagem de Fontes e Citações - Essentials, Revisão Bibliográfica com IA - Hands On | Estudantes, pesquisadores, jornalistas, analistas |
| J2 — Pesquisa e fundamentação jurídica | 5 de 5 (último) | Perplexity - Essentials, NotebookLM - Essentials, Pesquisa jurídica com IA - Hands On, Checagem de Fontes e Citações - Essentials | — | Advogados, assessores, estudantes e professores de Direito |

Consequência de design: na T2 o aluno ainda **não** fez o curso de Checagem, então a auditoria de
citações precisa ser ensinada aqui no mínimo necessário (existe, sustenta, é atual). Na J2 o aluno
já fez Checagem e Pesquisa jurídica; o curso oferece um caso jurídico-regulatório (LGPD/ANPD) e um
de licitações (Lei 14.133) para ele. Todo exercício tem versão de dados públicos (IBGE, Banco
Central, Ipea) e versão jurídica.

## Pré-requisitos

- *Perplexity - Essentials* ou *NotebookLM - Essentials* (observação do catálogo): saber fazer uma
  pergunta, ler uma resposta com citações e abrir as fontes.
- Nenhum conhecimento de método de pesquisa além do que o curso explica.

## Recursos necessários

- Computador com navegador e internet; abrir várias abas; ler PDF.
- Contas gratuitas nas três ferramentas (o curso funciona com **pelo menos uma** delas com saldo):
  - **ChatGPT Free:** deep research com acesso limitado; o saldo aparece só no produto (contador
    junto do Deep research ou `Settings > Usage` [conferir]); franquias fixas reiniciam 30 dias
    após o primeiro uso. Os números de 2025 (5/25/250 por mês) são históricos e não devem ser
    ensinados como atuais.
  - **Gemini (sem plano):** Deep Research com modelo Thinking; limites diários variáveis, sem número
    público; exige 18+ e Conta Google; pode faltar capacidade em alta demanda.
  - **Perplexity Free:** **1 Research Query por mês** (ajuda de 02/09/2026); Pro/Max com "limites
    médios", sem número fixo.
- Planilha de auditoria (modelo no curso).
- Materiais públicos de gabarito: página IBGE Educa "Pirâmide etária" e PDF IBGE "Censo 2022 —
  Pessoas de 60 anos ou mais"; histórico da Selic no Banco Central; nota Ipea "Retrato dos
  rendimentos do trabalho" (2º tri/2025); Resolução CD/ANPD 15/2024 e página da ANPD sobre
  comunicação de incidente; Lei 14.133/2021 consolidada no Planalto.
- **Rota sem cota:** se nenhuma ferramenta tiver saldo no dia, o aluno audita o relatório real de
  deep research publicado pelo MIT Sloan EdTech (`mit-case-study-deep-research.pdf`), que contém a
  conversa e a saída completas.

## Configuração

| Campo | Valor |
|---|---|
| Autoinstrucional | **Sim.** Nenhum passo depende de professor; todo exercício tem gabarito ou critério objetivo. |
| Trilhas | Essentials (compreensão) e Hands-on (execução), a partir deste objeto base. |
| Carga horária alvo — Essentials | 100–130 min (prompt-mestre `articulate-essentials.md`) |
| Carga horária alvo — Hands-on | 90–120 min (prompt-mestre `articulate-hands-on.md`) |
| Módulos/oficinas | Essentials: 4–6 módulos de conteúdo + síntese. Hands-on: 4 oficinas + Projeto Final. |
| Idioma | Português do Brasil. Rótulos em inglês (Deep research, Manage sites, Edit plan, Start research, Export to Docs, Keep Activity, Data Controls) mantidos e explicados; a tradução pt-BR pode exibir "Pesquisa aprofundada" no ChatGPT. |
| Plano exigido | Gratuito. Nenhuma atividade exige plano pago; a comparação das três ferramentas é desafio opcional, porque depende de saldo nas três. |
| Tempo de execução do agente | Não entra na MET (é espera, não atividade). O roteiro orienta a preencher a planilha enquanto o agente trabalha. Referência histórica: 5 a 30 min (lançamento do ChatGPT, 2025). |

## Fora do escopo

- Checagem detalhada de citação científica (DOI, retratação, Smart Citations) → *Checagem de
  Fontes e Citações - Essentials*.
- Revisão de literatura com triagem e PRISMA → *Revisão Bibliográfica com IA - Hands On*.
- Pesquisa de jurisprudência e montagem de peça → *Pesquisa jurídica com IA - Hands On*.
- APIs (Gemini Deep Research Max, Perplexity API), MCP e conectores corporativos — apêndice técnico.
- "Create files and apps" (antigo Labs) e Deep Research dentro de Computer na Perplexity — citados
  só para não confundir com o modo Deep Research.
- Parecer jurídico para caso concreto.

## Material-fonte

Pasta `Pesquisa Conteudo Onda 2/conteudo-bruto/deep-research-hands-on/`:

| Arquivo | Uso no curso |
|---|---|
| `ConteudoBruto_deep-research-hands-on.txt` | Fonte principal: fatos [CONFIRMADO]/[VERIFICAR]/[SUGESTÃO], 63 referências, acesso em 04/11/2026. |
| `openai-deep-research-system-card.pdf` | Riscos (alucinação, calibração, prompt injection). |
| `openai-browsecomp-paper.pdf`, `draco-benchmark-2026.pdf`, `deepresearch-bench-2025.pdf` | Leitura crítica de benchmarks e conflito de interesse. |
| `mit-case-study-deep-research.pdf` | Relatório real de deep research com conversa completa: rota sem cota. |
| `ibge-censo-2022-pessoas-idosas.pdf` | Gabarito do caso-guia (envelhecimento). |
| `ipea-rendimentos-trabalho-2025.pdf` | Gabarito do dossiê de rendimentos. |
| `anpd-resolucao-15-2024.pdf` | Gabarito do caso jurídico (o PDF traz a edição do DOU com outros atos antes; buscar pelo título). |
| `trt3-deep-research-pesquisa-juridica.pdf`, `new-york-law-journal-ai-research-panel.pdf`, `poynter-ai-ethics-journalism-report.pdf` | Casos de uso (jurídico brasileiro, escritórios, redações). |

Regra para dado factual: [CONFIRMADO] entra com data de consulta (04/11/2026); [VERIFICAR] ou NÃO
ENCONTRADO entra só como formulação genérica, marcado [conferir] nos roteiros, e vai para as
pendências do `README.md`. Nenhum modelo (o3, Opus 4.6, Gemini 3 Pro) é ensinado como estado atual
do recurso; nenhuma cota numérica é ensinada para ChatGPT e Gemini.

## Casos e gabaritos (fixos nas duas trilhas)

| Caso | Pergunta | Fonte primária | Gabarito |
|---|---|---|---|
| Guia — envelhecimento | Como mudou a população brasileira de 60+ e 65+ entre 2010 e 2022? | IBGE Educa; PDF IBGE Censo 2022 | 60+ = 15,8% em 2022, +46,6% sobre 2010; 65+ = 10,9% / 22,2 milhões em 2022 contra 7,4% / 14 milhões em 2010. Acerto: não misturar os dois cortes. |
| Jurídico — LGPD/ANPD | Quando e como o controlador deve comunicar incidente com risco relevante? | Resolução CD/ANPD 15/2024; página da ANPD | ANPD e titulares; três dias úteis; conteúdo nos arts. 6º e 9º; registro por pelo menos cinco anos (art. 10). Acerto: cita artigo e não vira parecer. |
| Projeto A — Selic | Decisões do Copom de jan/2025 a set/2026: pico e reversão | Banco Central, histórico de taxas | 13,25% em 29/01/2025; 15,00% de 18/06/2025 a 28/01/2026; cortes até 13,75% em 16/09/2026 [reconferir no dia]. |
| Projeto B — renda | Crescimento da renda por gênero no 2º tri/2025 | Nota Ipea (PNAD Contínua) | 3,4% homens e 3,3% mulheres, interanual; é taxa de crescimento, não igualdade de nível. |
| Projeto C — licitações (J2) | Valores de dispensa da Lei 14.133 vigentes em 2026 e o ato que os atualizou | Lei 14.133 consolidada (Planalto) | Montado no dia: identificar o decreto vigente e rejeitar ato revogado; valores mudam em 1º de janeiro. |

## Alertas herdados do conteúdo bruto

1. **Citação visível não é suporte.** Grounding vincula a fontes, não garante a inferência.
2. **Benchmarks com conflito de interesse:** BrowseComp (OpenAI; 1.266 problemas; 51,5% com
   treinamento específico; até 64 tentativas agregadas) e DRACO (autores ligados à Perplexity;
   Perplexity 67,15%) não são comparações neutras. DeepResearch Bench (acadêmico, 2025): Gemini com
   mais citações efetivas (111,21 em média), Perplexity com maior precisão de citação. Não há
   benchmark pt-BR dos três.
3. **Cotas, modelos e preços mudam;** conferir no produto. Preços públicos em dólar: ChatGPT Go
   US$ 8, Plus US$ 20; Google AI Pro US$ 19,99; Perplexity Pro US$ 20 — sem preço em reais estável.
4. **Dados:** ChatGPT pessoal treina por padrão (opt-out em Data Controls); Gemini com Keep Activity
   pode usar prompts e uploads para treino, com revisão humana, e retém por 18 meses por padrão;
   Temporary chat não treina mas fica 72 h; Perplexity permite opt-out em Pro/Education Pro/Max (o
   plano gratuito não aparece na lista [conferir]).
5. **Restrição de domínio:** só o ChatGPT documenta restringir a sites; na Perplexity, pedir domínio
   no prompt não bloqueia a web.
6. **Não rotular casos de chatbot comum como falha de deep research:** não foi encontrado caso
   judicial causado especificamente por esses modos.
7. **Não confundir** Perplexity Deep Research com Create files and apps, nem o Gemini do app com
   Deep Research Max da API.
