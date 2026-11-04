# 00 — Contornos do curso Checagem de Fontes e Citações - Essentials

Documento de partida compartilhado pelas duas trilhas. Tudo o que vem depois (v1.0, auditoria,
roteiros, carga horária, ementa) se apoia nestes campos.

## Origem do pedido

| Campo | Valor |
|---|---|
| Registro no catálogo | `novos-cursos-iaclube-priorizacao-v6.json` → `"id": "checagem-de-fontes-e-citacoes-essentials"` |
| Nome no catálogo | Checagem de Fontes e Citações - Essentials |
| Onda / ranking / score | Onda 2 · ranking 10 · 87 pontos (demanda 30, ferramenta 15, base 12, lacuna 20, esforço 10) |
| Tema / linha prioritária | Pesquisa científica com IA / Pesquisa com IA |
| Ferramentas do catálogo | Scite e Perplexity |
| Competência | Verificar afirmações e citações |
| Tarefa observável | Checar se uma citação existe, o que a fonte diz e se apoia ou contesta a afirmação. |
| Base confiável | Guias da Scite e da Perplexity |
| Observação do catálogo | Combate direto a alucinações; curto. |

## Objeto base

**Checagem de fontes e citações com apoio de IA** — o método de verificar, em três camadas, uma
afirmação acompanhada de citação:

1. **Identidade** — a obra existe e os metadados batem com um registro verificável?
2. **Fidelidade** — a fonte diz, de fato, o que lhe é atribuído, no contexto certo?
3. **Estado da evidência** — o achado continua válido, ou foi contestado, corrigido ou retratado?

As ferramentas do catálogo entram como **apoio** a cada camada, não como juiz: a **Perplexity**
(Pro Search, modo Academic, Check Sources e painel Sources) para descoberta e triangulação; a
**Scite** (Smart Citations, Search, Reports, Reference Check) para o estado da evidência na
literatura acadêmica. Bases gratuitas e oficiais (DOI.org, Crossref, PubMed, SciELO, Google
Scholar, Portal CAPES, BDTD, STJ/SCON, STF, Planalto) são a autoridade final de existência e de
texto.

## Público-alvo

O curso ocupa a **posição 4 de 5** em duas trilhas (`trilhas.json`):

| Trilha | Antes | Depois | Público |
|---|---|---|---|
| T2 — Pesquisa com IA | Perplexity - Essentials, NotebookLM - Essentials, Deep Research - Hands On | Revisão Bibliográfica com IA - Hands On | Estudantes, pesquisadores, jornalistas, analistas |
| J2 — Pesquisa e fundamentação jurídica | Perplexity - Essentials, NotebookLM - Essentials, Pesquisa jurídica com IA - Hands On | Deep Research - Hands On | Advogados, assessores, estudantes e professores de Direito |

Consequência de design: todo exercício tem **uma versão científica e uma jurídica**, ou serve aos
dois públicos. A atividade integradora e o Projeto Final deixam o aluno escolher o dossiê do seu
perfil (científico ou jurídico).

## Pré-requisitos

- Uso básico de um assistente de IA (perguntar, ler a resposta, abrir um link citado).
- Recomendado, não obrigatório: *Perplexity - Essentials* (a interface da Perplexity é apresentada
  só no necessário para checar).
- Nenhum conhecimento de metodologia científica ou de técnica jurídica além do que o curso explica.

## Recursos necessários

- Computador com navegador atualizado e internet; possibilidade de abrir várias abas.
- Conta gratuita da Perplexity. No plano gratuito: buscas básicas praticamente ilimitadas, **três
  Pro Searches por dia** e uma Research query por mês (ajuda oficial, 02/09/2026). O curso foi
  desenhado para caber nessas três Pro Searches diárias.
- Scite: **opcional**. Basic US$ 12/mês e Pro US$ 40/mês (cobrança anual), teste de sete dias com
  renovação automática se não for cancelado. Não há convênio CAPES nacional conhecido. O curso tem
  rota completa sem Scite: o conceito de Smart Citation é ensinado com o relatório de exemplo
  público da Scite (`scite-reference-check-sample.pdf`) e com o artigo técnico de 2021; o uso ao
  vivo fica como caminho opcional para quem tem teste ou licença institucional.
- Bases gratuitas: DOI.org, Crossref Search, Google Scholar, SciELO, PubMed; para o público
  jurídico, STJ (SCON), STF e Planalto.
- Uma ficha de auditoria (modelo fornecido no curso, editor de texto ou planilha).

## Configuração

| Campo | Valor |
|---|---|
| Autoinstrucional | **Sim.** Nenhum passo depende de professor; todo exercício tem gabarito ou critério objetivo. |
| Trilhas | Essentials (compreensão) e Hands-on (execução), a partir deste objeto base. |
| Carga horária alvo — Essentials | 100–130 min (prompt-mestre `articulate-essentials.md`) |
| Carga horária alvo — Hands-on | 90–120 min (prompt-mestre `articulate-hands-on.md`) |
| Módulos/oficinas | Essentials: 4–6 módulos de conteúdo + síntese. Hands-on: 4 oficinas + Projeto Final. |
| Idioma | Português do Brasil. Rótulos que só existem em inglês (Supporting, Contrasting, Mentioning, Pro Search, Check Sources) ficam em inglês, com explicação. |
| Plano exigido | Gratuito (Perplexity Free + bases públicas). Scite pago/teste é sempre opcional e sinalizado. |

## Fora do escopo (outro curso cobre)

- Revisão de literatura completa (pergunta, triagem, extração) → *Revisão Bibliográfica com IA - Hands On*.
- Pesquisa profunda automatizada → *Deep Research - Hands On*.
- Montagem de peça jurídica e pesquisa de precedentes do zero → *Pesquisa jurídica com IA - Hands On*.
- Avaliação metodológica aprofundada (risco de viés, GRADE) — citada como fronteira.
- API e MCP da Scite — apêndice técnico do conteúdo bruto, não entram no curso introdutório.

## Material-fonte

Pasta `Pesquisa Conteudo Onda 2/conteudo-bruto/checagem-de-fontes-e-citacoes-essentials/`:

| Arquivo | Uso no curso |
|---|---|
| `ConteudoBruto_checagem-de-fontes-e-citacoes-essentials.txt` | Fonte principal: fatos [CONFIRMADO]/[VERIFICAR]/[SUGESTÃO], 54 referências, acesso em 04/11/2026. |
| `scite-smart-citation-index-2021.pdf` | Artigo de Nicholson et al. (DOI 10.1162/qss_a_00146): par correto e par "existe, mas não sustenta". |
| `scite-reference-check-sample.pdf` | Relatório de exemplo público da Scite (busca "tremelimumab clinical trial", 12/8/2021). Usado para ler Supporting/Contrasting/Mentioning sem conta. Observação: apesar do nome do arquivo, é um relatório de busca por citation statements, não um Reference Check de manuscrito. |
| `scite-assistant-prompt-handbook.pdf` | Boas práticas de prompt do Assistant (referência, não reproduzido). |
| `estudo-chatgpt-research-scientist-2024.pdf` | Lehr et al. (2024): taxas de alucinação por completude da referência. |
| `stj-guia-pesquisa-jurisprudencia-2025.pdf` | Guia oficial SOS Pesquisa (SCON, operadores, pesquisa avançada). |
| `capes-guia-rapido-novo-portal.pdf`, `capes-guia-acesso-cafe-2025.pdf` | Portal de Periódicos e acesso remoto institucional. |

Regra para dado factual: [CONFIRMADO] entra com data de consulta (04/11/2026); [VERIFICAR] ou NÃO
ENCONTRADO entra só como formulação genérica, marcado [conferir] nos roteiros, e vai para as
pendências do `README.md`. Todo número de estudo vem com amostra, modelo e data — nunca solto.

## Pares de exercício (fixos nas duas trilhas)

| Par | Afirmação | Citação | Gabarito |
|---|---|---|---|
| 1 — correta | A Scite classifica citation statements em apoio, contraste/disputa e menção. | Nicholson et al., 2021, DOI 10.1162/qss_a_00146 | Existe e apoia (o artigo usa "disputing"; a interface atual usa "contrasting"). |
| 2 — existe, não sustenta | "O classificador da Scite tem 99% de acurácia em todas as classes e cobre toda publicação científica." | Mesma fonte | Existe, não apoia: o artigo relata desempenho desigual entre classes e cobertura limitada. |
| 3 — contestada | Power posing altera hormônios e tolerância ao risco. | Carney, Cuddy e Yap, 2010, DOI 10.1177/0956797610383437 | Contestada em desfechos específicos por Ranehill et al., 2015 (DOI 10.1177/0956797614553946, N = 200). |
| 4 — inexistente | (referência didática inventada) | SILVA, Ana. Auditoria universal de citações por IA. Revista Brasileira de Evidência Digital, 2026. DOI 10.9999/ia-clube.2026.001 | Não localizada nas bases pesquisadas; registrar bases e data. |
| 5 — retratada | Artigo jurídico brasileiro sobre direitos fundamentais | DOI 10.5380/rinc.v9i1.83825 (SciELO) | Existe, marcado "ARTIGO RETRATADO", ligado ao aviso DOI 10.5380/rinc.v11i1.94614. |
| J — jurídico | "O STJ decidiu X no HC 1.023.732" e texto atribuído ao art. 436, §1º, CPP | STJ (SCON / notícia oficial de 18/10/2026) e Planalto | Caso real de citação inventada; conferir na base oficial. |

## Alertas herdados do conteúdo bruto

1. **Citação inline não é prova.** Link ou DOI que resolve confirma identidade, não apoio.
2. **Rótulo automático não substitui leitura.** Smart Citation classifica um trecho citante, não o
   artigo inteiro; contagem de supporting/contrasting não é placar.
3. **Fonte oficial e versão atual prevalecem** em direito, normas e dados mutáveis.
4. **Números de estudos não se misturam**: 55%/18% (Walters e Wilder, abril/2023, GPT-3.5/GPT-4),
   37% de erro da Perplexity em atribuição de notícias (Tow Center, 2025) e taxas de Lehr et al.
   (2024) medem tarefas diferentes.
5. Interfaces da Scite e da Perplexity mudaram em 2026 (Collections, Check Sources); caminhos finos
   de menu vêm em parte de tutoriais de 2021 e precisam de conferência visual.
