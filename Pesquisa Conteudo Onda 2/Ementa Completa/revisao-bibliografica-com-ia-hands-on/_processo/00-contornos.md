# 00 — Contornos do curso Revisão Bibliográfica com IA - Hands On

Documento de partida compartilhado pelas duas trilhas. Tudo o que vem depois (v1.0, auditoria,
roteiros, carga horária, ementa) se apoia nestes campos.

## Origem do pedido

| Campo | Valor |
|---|---|
| Registro no catálogo | `novos-cursos-iaclube-priorizacao-v6.json` → `"id": "revisao-bibliografica-com-ia-hands-on"` |
| Nome no catálogo | Revisão Bibliográfica com IA - Hands On |
| Onda / ranking / score | Onda 2 · ranking 11 · 87 pontos (demanda 30, ferramenta 15, base 15, lacuna 20, esforço 7) |
| Tema / linha prioritária | Pesquisa científica com IA / Pesquisa com IA |
| Ferramentas do catálogo | Elicit, Consensus e Semantic Scholar |
| Competência | Conduzir revisão de literatura assistida |
| Tarefa observável | Definir pergunta, buscar, triar, extrair dados de artigos e organizar a síntese com rastreabilidade. |
| Base confiável | Guias oficiais das ferramentas |

## Objeto base

**Revisão bibliográfica assistida por IA** — o percurso de cinco etapas da tarefa observável, cada
uma com o seu registro:

1. **Pergunta** — tipo de revisão (narrativa, integrativa, escopo, sistemática), framework (PICO,
   PICo ou PCC), critérios de inclusão e exclusão definidos antes da busca.
2. **Busca** — termos e descritores (DeCS/MeSH), consultas nas ferramentas de IA e em bases
   brasileiras, com data, filtros e total registrados.
3. **Triagem** — deduplicação, decisão por título/resumo e por texto completo, motivo de exclusão.
4. **Extração** — colunas definidas e pilotadas, dado conferido no artigo, trecho de apoio.
5. **Síntese com rastreabilidade** — concordâncias, divergências e lacunas, cada frase com referência
   e trecho; fluxograma PRISMA 2020; declaração de uso de IA.

As ferramentas entram como **apoio a etapas diferentes**, nunca como fonte única nem como juiz:
**Semantic Scholar** (gratuito, sem conta para buscar) para descoberta, Library e exportação;
**Consensus** para panorama e divergências (Pro, Deep, filtros, Consensus Meter); **Elicit** para
tabela de extração com supporting quote (Research Agent, Research Report; Systematic Review só no
Pro). Bases brasileiras e gratuitas (SciELO, BVS/LILACS com DeCS, BDTD, Portal CAPES, Google
Acadêmico) completam a cobertura; Zotero (gratuito) guarda a biblioteca e ajuda a deduplicar.

## Público-alvo

O curso ocupa a **posição 5 de 5** (último) da trilha T2 (`trilhas.json`):

| Trilha | Antes | Público |
|---|---|---|
| T2 — Pesquisa com IA | Perplexity - Essentials, NotebookLM - Essentials, Deep Research - Hands On, Checagem de Fontes e Citações - Essentials | Estudantes, pesquisadores, jornalistas, analistas |

Competência de saída da trilha: "pesquisar com fontes verificáveis, conduzir deep research e
revisão de literatura com rastreabilidade". O curso fecha essa competência.

Consequência de design: o caso-guia é da saúde (é o que as três ferramentas cobrem melhor e o que
tem descritores DeCS), mas o Projeto Final e a atividade integradora deixam o aluno escolher uma das
cinco perguntas testadas (saúde, educação, comunicação, Direito, gestão pública) ou uma pergunta
própria. Público jurídico não é público formal desta trilha, mas uma das perguntas é de Direito.

## Pré-requisitos

- Uso básico de um assistente de IA.
- Recomendado: *Checagem de Fontes e Citações - Essentials* (o curso reaproveita a ideia de
  "localizada / diz isso / ainda vale" e não a reensina).
- Nenhum conhecimento prévio de metodologia de revisão: o curso explica tipos, frameworks e PRISMA
  desde a base.

## Recursos necessários

- Computador com navegador atualizado e internet. Interfaces das três ferramentas em inglês.
- **Semantic Scholar:** sem conta para buscar; conta gratuita (Google, instituição ou e-mail) para
  Library, Research Feeds e exportação.
- **Consensus:** conta gratuita. Free: Paper search ilimitado, 10 mensagens Pro/mês, 3 Deep/mês, 10
  Study Snapshots/mês (planos de 12/09/2026; uma página de ajuda ainda diz 15 mensagens Pro —
  [conferir]). Uma busca sem conta funciona; a segunda pede cadastro.
- **Elicit:** conta Basic gratuita. Research Agent e Research Reports com uso limitado; busca e
  resumos ilimitados. **Não** inclui Systematic Review (Pro, US$ 39/mês) nem exportação de tabela
  CSV/Excel (Plus, US$ 11/mês no anual). O curso usa só o Basic; o Systematic Review é apresentado
  como conceito e caminho opcional.
- **Zotero** desktop gratuito + Zotero Connector (opcional, mas recomendado para deduplicar).
- Planilha (Google Planilhas, Excel ou LibreOffice Calc) com quatro abas: Log de busca, Triagem,
  Extração, Síntese (modelo fornecido no curso).
- Materiais da pasta: `prisma-2020-fluxograma-ptbr.docx`, `prisma-2020-declaracao-ptbr.pdf`,
  `bvs-tutorial-pesquisa-2024.pdf`; artigo aberto para extração
  (`objnursing.uff.br/nursing/article/download/6885/pdf_pt`, testado em 04/11/2026).

## Configuração

| Campo | Valor |
|---|---|
| Autoinstrucional | **Sim.** Nenhum passo depende de professor; todo exercício tem gabarito ou critério objetivo. |
| Trilhas | Essentials (compreensão) e Hands-on (execução), a partir deste objeto base. |
| Carga horária alvo — Essentials | 100–130 min (prompt-mestre `articulate-essentials.md`) |
| Carga horária alvo — Hands-on | 90–120 min (prompt-mestre `articulate-hands-on.md`) |
| Módulos/oficinas | Essentials: 4–6 módulos de conteúdo + síntese. Hands-on: 4 oficinas + Projeto Final. |
| Idioma | Português do Brasil. Rótulos de interface ficam em inglês (Research Agent, Add Column, Has PDF, Save to Library, Filter, Consensus Meter), com explicação. |
| Plano exigido | Gratuito nas três ferramentas. Nenhuma atividade obrigatória depende de plano pago. |

## Fora do escopo (outro curso cobre ou é fronteira)

- Checagem de uma citação isolada (existe, diz, ainda vale) → *Checagem de Fontes e Citações - Essentials*.
- Relatório de pesquisa profunda de agente generalista → *Deep Research - Hands On*.
- Meta-análise, avaliação de risco de viés, GRADE — citados como fronteira.
- Revisão sistemática completa com protocolo registrado (PROSPERO) — o curso entrega uma
  **mini-revisão rastreável**, não uma revisão sistemática publicável.
- API do Elicit, API/MCP do Consensus e Academic Graph do Semantic Scholar — apêndice técnico.

## Material-fonte

Pasta `Pesquisa Conteudo Onda 2/conteudo-bruto/revisao-bibliografica-com-ia-hands-on/`:

| Arquivo | Uso no curso |
|---|---|
| `ConteudoBruto_revisao-bibliografica-com-ia-hands-on.txt` | Fonte principal: fatos [CONFIRMADO]/[VERIFICAR]/[SUGESTÃO], 61 referências, acesso em 04/11/2026. |
| `prisma-2020-declaracao-ptbr.pdf` | Declaração PRISMA 2020 em português (20 p.): PRISMA como diretriz de relato. |
| `prisma-2020-fluxograma-ptbr.docx` | Modelo do fluxograma em português (CC BY 4.0): entregável do Projeto Final. |
| `prisma-2020-checklist-en.pdf` | Checklist em inglês (2 p.); o checklist pt-BR retornou 404. |
| `jbi-manual-evidence-synthesis-2024.pdf` | PICo, PCC, critérios de elegibilidade (referência, não reproduzido). |
| `bvs-tutorial-pesquisa-2024.pdf` | DeCS, campos e operadores na BVS. |
| `capes-guia-novo-portal.pdf`, `capes-guia-acesso-cafe-2025.pdf` | Portal de Periódicos e acesso CAFe para texto completo. |

Regra para dado factual: [CONFIRMADO] entra com data de consulta (04/11/2026); [VERIFICAR] ou NÃO
ENCONTRADO entra só como formulação genérica, marcado [conferir] nos roteiros, e vai para as
pendências do `README.md`. Nenhum tamanho de corpus é fixado como número único.

## Caso-guia e perguntas de prática (fixos nas duas trilhas)

| Uso | Pergunta | Framework | Dado de apoio (Semantic Scholar, 04/11/2026, sem login) |
|---|---|---|---|
| Caso-guia | Telessaúde melhora o controle da hipertensão na atenção primária brasileira? | PICO | `telehealth hypertension Brazil`: cerca de 8.230 resultados; 6 dos 10 primeiros úteis |
| Projeto — educação | Quais efeitos e barreiras das metodologias ativas no ensino superior brasileiro? | PCC | `active learning higher education Brazil`: cerca de 27.200; 5 dos 10 relevantes |
| Projeto — comunicação | Quais fatores explicam crença em desinformação nas redes sociais no Brasil? | PICo | `social media misinformation Brazil`: cerca de 20.200; 5 dos 10 relevantes |
| Projeto — Direito | Quais riscos e salvaguardas são discutidos para IA em decisões judiciais brasileiras? | PCC | `artificial intelligence judicial decisions Brazil`: cerca de 1.710; 4 dos 10 relevantes |
| Projeto — gestão pública | Como o orçamento participativo afeta transparência e participação no Brasil? | PICo | `participatory budgeting transparency Brazil`: cerca de 1.520; 3 dos 10 relevantes |

Artigo de extração fixo: "Efeitos da capacitação em telessaúde..." (Online Brazilian Journal of
Nursing, PDF público). Contagens são voláteis ("About") e servem para o aluno comparar, não como
gabarito.

## Alertas herdados do conteúdo bruto

1. **Nenhuma ferramenta é fonte única de identificação.** Meliante et al. (JMIR AI, 2025), quatro
   revisões PRISMA de glaucoma: recuperação incompleta; extrações do Elicit 51,40% precisas, 13,69%
   imprecisas, 22,37% ausentes, 12,51% incorretas.
2. **Extração é falível e instável.** Estudo de viabilidade (Research Synthesis Methods, 2026), sete
   revisões ambientais e de ciências da vida: 22 divergências em 208 comparações (10,6%), acurácia
   global de 82% na versão testada; nova execução reproduziu 77% das saídas e só 10% dos supporting
   quotes coincidiram.
3. **Supporting quote é pista de auditoria, não garantia.** Sem PDF, o Elicit extrai do resumo.
4. **Tipo de estudo não é qualidade.** Classificação do Consensus é automática; Consensus Meter só
   para perguntas sim/não e não é medida de certeza.
5. **Semantic Scholar não aceita Boolean nem curingas.** Copiar estratégia do PubMed piora a busca.
6. **PRISMA é diretriz de relato**, não método de busca.
7. **Mudança recente no Elicit:** em 30/09/2026 Find Papers, Extract Data e Chat with Papers foram
   fundidos no Research Agent; vídeos antigos mostram telas que não existem mais.
8. **Declaração de IA:** o CNPq exige declarar ferramenta e finalidade em qualquer etapa; padrão
   nacional da CAPES para teses não foi encontrado.
9. **Dados:** Elicit processa nos EUA (AWS e provedores de modelo); Consensus repassa consultas e
   uploads a OpenAI, Anthropic, Google e Baseten, sem treino declarado; Semantic Scholar busca sem
   conta. Manuscrito inédito, prontuário e dado sensível não vão para nenhuma delas.
