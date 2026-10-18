# 00 — Contornos do curso Perplexity - Essentials

Documento de partida compartilhado pelas duas trilhas. Tudo o que vem depois (v1.0, auditoria,
roteiros, carga horária, ementa) se apoia nestes campos.

## Origem do pedido

| Campo | Valor |
|---|---|
| Registro no catálogo | `novos-cursos-iaclube-priorizacao-v6.json` → `"id": "perplexity-essentials"` |
| Nome no catálogo | Perplexity - Essentials |
| Onda / ranking / score | Onda 1 · ranking 3 · 95 pontos (demanda 30, ferramenta 20, base 15, lacuna 20, esforço 10) |
| Tema / linha prioritária | Pesquisa com IA |
| Competência | Pesquisar com fontes verificáveis |
| Tarefa observável | Formular perguntas, usar modos de busca, comparar fontes e produzir uma síntese citada. |
| Base confiável | Centro de ajuda e guias da Perplexity |
| Observação do catálogo | Porta de entrada da linha de pesquisa. |

## Objeto base

**Perplexity** — o motor de respostas com IA da Perplexity AI (produto-âncora: Perplexity Search),
que pesquisa a web, sintetiza a resposta com um modelo de linguagem e associa as afirmações a
citações clicáveis. O curso trata do **Search** (pesquisa com resposta citada). Os produtos vizinhos
— Computer, Create files and apps (antigo Labs), o navegador Comet e a API — aparecem só como
fronteira.

## Público-alvo

Dois públicos, vindos das trilhas em que o curso é a porta de entrada:

| Trilha | Posição | Público |
|---|---|---|
| T2 — Pesquisa com IA | 1 de 5 (primeiro curso; depois: NotebookLM - Essentials) | Estudantes, pesquisadores, jornalistas e analistas |
| J2 — Pesquisa e fundamentação jurídica | 1 de 5 (primeiro curso; depois: NotebookLM - Essentials) | Advogados, assessores jurídicos, estudantes e professores de Direito |

Consequências de design:

1. **Tema-âncora comum:** LGPD e decisões automatizadas (art. 20 da Lei nº 13.709/2018), com fontes
   oficiais públicas (Planalto e ANPD). Serve aos dois públicos, é situação cotidiana (crédito negado
   por sistema automático) e dá continuidade ao curso seguinte da trilha, *NotebookLM - Essentials*,
   que usa um corpus LGPD: o aluno localiza fontes aqui e as estuda lá.
2. **Verificação com gabarito conhecido:** acórdão do TJPR nº 0033052-89.2025.8.16.0001 (link oficial
   testado em 18/10/2026, valores de controle conhecidos). Serve ao jurídico (repositório oficial) e
   ao jornalismo/pesquisa (prova de existência de uma referência).
3. **Atividade integradora por perfil:** o aluno escolhe o recorte do seu público.

## Pré-requisitos

- Uso básico de um assistente de IA (ChatGPT, Claude ou Gemini).
- Nenhum conhecimento técnico.

## Recursos necessários

- Computador com navegador atualizado e internet. O fluxo principal é o **web** (`perplexity.ai`);
  aplicativos para Windows, macOS, iPhone/iPad (iOS/iPadOS 18.0 ou posterior, App Store Brasil em
  18/10/2026) e Android existem, mas ficam como complemento.
- Conta gratuita na Perplexity (e-mail ou Conta Google). A busca básica funciona sem login, mas
  histórico, Projetos e configurações de privacidade dependem de conta.
- Plano **gratuito** basta para todo o curso. Cotas do gratuito (ajuda oficial, 02/09/2026): busca
  básica "praticamente ilimitada", **3 Pesquisas Pro por dia**, **1 Research por mês**, uploads
  limitados. Nenhum exercício depende de Research; o exercício com Pesquisa Pro tem rota alternativa
  para quem já esgotou a cota.

## Configuração

| Campo | Valor |
|---|---|
| Autoinstrucional | **Sim.** Nenhum passo pode depender de professor. |
| Trilhas | Essentials (compreensão) e Hands-on (execução), ambas a partir deste objeto base. |
| Carga horária alvo — Essentials | 100–130 min (prompt-mestre `articulate-essentials.md`) |
| Carga horária alvo — Hands-on | 90–120 min (prompt-mestre `articulate-hands-on.md`) |
| Módulos/oficinas | Essentials: 4–6 módulos de conteúdo + síntese. Hands-on: 4 oficinas + Projeto Final. |
| Idioma | Português do Brasil; nomes de recurso que só existem em inglês ficam em inglês. |
| Plano exigido | Gratuito. Pro, Max, Education Pro e Enterprise são citados, não exigidos. |

## Fora do escopo (outro curso cobre)

- Relatórios longos de deep research auditados, comparando ChatGPT, Gemini e Perplexity →
  *Deep Research - Hands On*.
- Verificação de citações com ferramentas como Scite → *Checagem de Fontes e Citações - Essentials*.
- O navegador Comet → *Perplexity Comet - Essentials*.
- Estudo aprofundado de um conjunto fechado de fontes próprias → *NotebookLM - Essentials* (curso
  seguinte da trilha).
- Computer, Create files and apps, API, conectores e administração Enterprise.

Esses temas aparecem apenas para delimitar a fronteira (uma frase, nunca um passo a passo).

## Material-fonte

Pasta `Pesquisa Conteudo Onda 1/conteudo-bruto/perplexity-essentials/`:

| Arquivo | Uso no curso |
|---|---|
| `ConteudoBruto_perplexity-essentials.txt` (17/10/2026) | Fonte principal: identidade, planos, modos, citações, Projetos, privacidade, estrutura oficial de prompt, estudos independentes, exercícios; 31 referências. |
| `ConteudoBruto_perplexity-essentials_complemento.txt` (18/10/2026) | Casos brasileiros de jurisprudência inventada (TJPR, STJ, TSE), prompt injection (STF), CNJ e OAB, pesquisa em repositórios oficiais, **rótulos da interface pt-BR observados em 18/10/2026**, lojas Brasil; 31 referências. |
| `guia-oficial-perplexity-at-work.pdf` | Guia oficial (44 p., inglês): referência de terminologia e fluxos; licença não informada, não reproduzido. |
| `relatorio-oficial-draco-deep-research.pdf` | Benchmark de Deep Research de autoria da Perplexity: só contexto; não é avaliação independente e o tema pertence a outro curso. |
| `oab-recomendacao-001-2024-ia-generativa.pdf` | Itens 2.1–2.5 (sigilo) e 3.1–3.8 (veracidade, revisão integral) — base do módulo de segurança. |
| `cnj-resolucao-615-2025-compilada-674-2026.pdf` | Supervisão humana (arts. 2º, 3º, 32–34) — citada como parâmetro, com o escopo correto (Poder Judiciário). |

Regra para dado factual: o que no conteúdo bruto está [CONFIRMADO] entra no curso com a data de
consulta; o que está [VERIFICAR] ou NÃO ENCONTRADO entra no máximo como formulação genérica e vai
para as pendências do `README.md`. Elaborações [SUGESTÃO] do pesquisador (prompts, exercícios) podem
ser usadas como proposta didática, nunca como fato.

## Decisões sobre rótulos de interface

A interface muda rápido e a ajuda pt-BR é parcialmente tradução automática. Em 18/10/2026, a tela
pública pt-BR mostrava: caixa "O que você quer saber?", modos "Pesquisar" e "Computer", menu "+"
"Adicionar arquivos ou ferramentas" (com "Enviar arquivos ou imagens" e "Conectores"), seletor
"Modelo", menu de fontes "Aplicativos e mais" (Finanças, Saúde, Acadêmico, Patentes), "Projetos" /
"Criar projeto", barra lateral "Recentes" (rota `/library`), "Compartilhar", "navegação anônima".
"Best", "Pesquisa Pro" e "Research" **não** apareceram sem login.

Portanto: o curso ensina **três níveis de profundidade** (busca padrão, Pesquisa Pro, Research) como
conceitos, com tabela de equivalência pt-BR/inglês datada, e marca **[conferir]** todo rótulo não
observado diretamente. Pages (recurso legado sem confirmação atual) não é ensinado.

## Alertas herdados do conteúdo bruto

1. Citação presente não significa afirmação comprovada: em teste independente (Tow Center, resumido
   pelo El País em 25/04/2025), a Perplexity teve a menor taxa de erro de citação entre oito
   ferramentas — e ainda assim 37%.
2. Referência jurídica gerada por IA nunca vai para uma peça sem conferência do inteiro teor no
   repositório oficial; há sanções reais no Brasil (TJPR, STJ, TSE) e no exterior (Mata v. Avianca).
3. Planos, cotas, modelos, nomes e menus mudam em semanas (Spaces → Projetos em 04/08/2026; Labs →
   Create files and apps em 05/02/2026); revisão humana obrigatória na semana de publicação.
4. A oferta B2C da Vivo descrita na primeira pesquisa veio de ambiente de teste e **não** deve ser
   apresentada como vigente.
