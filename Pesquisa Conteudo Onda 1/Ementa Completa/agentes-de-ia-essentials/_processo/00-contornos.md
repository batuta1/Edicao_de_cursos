# 00 — Contornos do curso Agentes de IA - Essentials

Documento de partida compartilhado pelas duas trilhas. Tudo o que vem depois (v1.0, auditoria,
roteiros, carga horária, ementa) se apoia nestes campos.

## Origem do pedido

| Campo | Valor |
|---|---|
| Registro no catálogo | `novos-cursos-iaclube-priorizacao-v6.json` → `"id": "agentes-de-ia-essentials"` |
| Nome no catálogo | Agentes de IA - Essentials |
| Onda / ranking / score | Onda 1 · ranking 4 · 92 pontos (demanda 30, ferramenta 20, base 15, lacuna 20, esforço 7) |
| Tema / linha prioritária | Agentes de IA |
| Ferramentas citadas no catálogo | ChatGPT (modo agente), Claude Cowork, Manus |
| Competência | Delegar tarefas de várias etapas a agentes |
| Tarefa observável | Definir uma tarefa, acompanhar a execução de um agente, revisar resultados e identificar limites e riscos. |
| Base confiável | Docs de OpenAI, Anthropic e Manus |
| Observação do catálogo | Claude Cowork cobre uma ferramenta; a competência transversal de agentes ainda não é nomeada. |

## Objeto base

**Agentes de IA** — sistemas de IA que recebem um objetivo, planejam etapas, usam ferramentas
(arquivos, navegador, busca, execução de código, aplicativos), observam o resultado de cada ação e
ajustam o caminho até concluir ou pedir intervenção humana. O curso ensina a **competência
transversal de delegar** (definir, acompanhar, revisar, reconhecer limites), e não o manual de uma
ferramenta. Três produtos servem de exemplo:

| Produto | Nome atual da experiência agente (18/10/2026) | Plano mínimo |
|---|---|---|
| ChatGPT | **Work** ("ChatGPT Trabalho" no texto da ajuda pt-BR). O antigo "modo agente"/"ChatGPT agent" foi **descontinuado**; a ajuda pt-BR diz que ele "não está mais disponível". | Plus (US$ 20/mês). Free e Go não têm Work. |
| Claude | **Cowork** (em unificação com o Chat numa experiência única chamada "Claude"; o seletor Chat/Cowork pode não aparecer) | Pro (US$ 20/mês ou US$ 200/ano). Free não tem Cowork. |
| Manus | **Agent Mode** (ao lado de Chat Mode), modelo Manus 2.0 Lite no plano gratuito | **Free** — 1.000 créditos iniciais, 300 renovados por dia, 1 tarefa concorrente. |

Consequência central: **só o Manus oferece experiência agente no plano gratuito.** O caminho
principal das atividades práticas é o Manus Free; ChatGPT Work e Claude Cowork aparecem como
caminhos opcionais para quem já assina, com a mesma tarefa.

## Público-alvo

| Trilha | Posição | Público |
|---|---|---|
| T3 — Agentes e MCP | 2 de 10 (antes: Claude Cowork - Essentials; depois: MCP - Essentials) | Profissionais de escritório que querem delegar tarefas de várias etapas; curiosos técnicos |
| J5 — Agentes e assistentes jurídicos | 1 de 7 (primeiro curso; depois: Claude Cowork - Essentials) | Escritórios de advocacia e departamentos jurídicos que atendem volume |

Consequências de design:

1. **Material de exercício comum, público e em português:** Guia de uso de IA generativa do TCU
   (7 páginas) — curto o bastante para caber nos créditos diários do Manus Free, normativo e
   concreto, útil para os dois públicos. Na atividade integradora, cada perfil escolhe o seu
   documento: Guia de Uso Responsável de IA da CGU (12 p.) para escritório; Recomendação
   001/2024/CFOAB (15 p.) para o jurídico.
2. **Pasta de treino isolada (`Treino_Agente`)** com cópias de documentos públicos e um
   arquivo-isca sintético para o exercício de injeção de prompt. Nunca Downloads, Documentos ou a
   unidade inteira.
3. **Jurídico sem dado real:** a Recomendação 001/2024/CFOAB e o caso STJ (comando oculto em recurso,
   02/09/2026) sustentam o módulo de segurança; nenhuma atividade usa processo, cliente ou dado
   pessoal real.

## Pré-requisitos

- Uso básico de um assistente de IA (ChatGPT, Claude ou Gemini).
- Nenhum conhecimento técnico.

## Recursos necessários

- Computador com navegador atualizado e internet; e-mail para criar conta.
- Conta **Manus gratuita** (caminho principal). Opcional: ChatGPT Plus (Work) ou Claude Pro (Cowork).
- Capacidade de criar uma pasta no computador e salvar PDFs nela.
- Leitor de PDF para conferir páginas.

## Configuração

| Campo | Valor |
|---|---|
| Autoinstrucional | **Sim.** Nenhum passo pode depender de instrutor (a sugestão do conteúdo bruto "o instrutor injeta uma mudança" foi convertida em instrução escrita). |
| Trilhas | Essentials (compreensão) e Hands-on (execução), ambas a partir deste objeto base. |
| Carga horária alvo — Essentials | 100–130 min (prompt-mestre `articulate-essentials.md`) |
| Carga horária alvo — Hands-on | 90–120 min (prompt-mestre `articulate-hands-on.md`) |
| Módulos/oficinas | Essentials: 4–6 módulos de conteúdo + síntese. Hands-on: 4 oficinas + Projeto Final. |
| Idioma | Português do Brasil; rótulos que a interface mantém em inglês (Work, Cowork, Agent Mode) ficam em inglês. |
| Plano exigido | Gratuito (Manus). Work e Cowork exigem plano pago e são opcionais. |

## Fora do escopo (outro curso cobre)

- Coordenar vários agentes numa mesma tarefa → *Multiagentes - Essentials*.
- Agentes de navegador em profundidade (Atlas, Claude in Chrome, Comet) → *Agentes Web - Hands On*.
- Uso detalhado do Claude Cowork → *Claude Cowork - Essentials* e *Hands On* (aqui é só exemplo).
- Construir agentes dentro de automações → *N8N: Agentes de IA - Essentials 6*.
- MCP → *MCP - Essentials*, o curso seguinte da trilha T3.
- Construção de agentes por API/SDK, benchmarks de modelos, "dots" (agentes sempre ativos da OpenAI)
  e administração empresarial.

Esses temas aparecem apenas para delimitar a fronteira (uma frase, nunca um passo a passo).

## Material-fonte

Pasta `Pesquisa Conteudo Onda 1/conteudo-bruto/agentes-de-ia-essentials/`:

| Arquivo | Uso no curso |
|---|---|
| `ConteudoBruto_agentes-de-ia-essentials.txt` (18/10/2026) | Fonte principal: definições (Anthropic, Google, NIST), chat × workflow × agente, acesso e planos, primeiros passos nas três ferramentas, glossário, modos de aprovação, segurança, troubleshooting, prompts O-F-L-C-P sugeridos, exercícios; 42 referências. |
| `ConteudoBruto_agentes-de-ia-essentials_complemento.txt` (18/10/2026) | Descontinuação do agente do ChatGPT, tabela por plano, definições OpenAI e acadêmica, system cards, casos brasileiros (CAIXA, Inter, Banlek, STJ), avaliações independentes (AI Agent Index, Princeton HAL, UW, npj), rótulos pt-BR, cinco PDFs públicos em português; 43 referências. |
| `oab-recomendacao-001-2024-ia-generativa.pdf` | Seção jurídica e atividade integradora do perfil jurídico. |
| `nist-ai-600-1-genai-profile.pdf` | Taxonomia de riscos (confabulação) — contexto, não leitura do aluno. |
| `google-secure-ai-agents-introduction.pdf` | Princípios: controlador humano definido, poderes limitados, ações observáveis. |
| `anthropic-claude-for-legal-guide-2026.pdf`, `anthropic-2026-state-of-ai-agents-report.pdf` | Casos de uso do fornecedor — citados com ressalva de patrocínio. |

PDFs de exercício **não** estão na pasta (estão como `[BAIXAR]` no complemento): Guia do TCU, Guia da
CGU. O aluno os baixa pelos links oficiais testados em 18/10/2026.

Regra para dado factual: o que no conteúdo bruto está [CONFIRMADO] entra no curso com a data de
consulta; o que está [VERIFICAR] ou NÃO ENCONTRADO entra no máximo como formulação genérica e vai
para as pendências do `README.md`. Elaborações [SUGESTÃO] (fórmula O-F-L-C-P, escada de autonomia,
fórmula de risco, prompts) podem ser usadas como proposta didática, declaradas como tal, nunca como
padrão oficial.

## Decisões sobre rótulos de interface

| Ferramenta | Rótulos usados no curso | Status |
|---|---|---|
| ChatGPT | Seletor **Chat / Work** acima da caixa de mensagem; "acompanhar o progresso"; "Permitir / Permitir uma vez / Negar"; permissões de site "Sempre perguntar / Aprovar automaticamente / Sempre permitir"; `Configurações > Navegador na nuvem > Dados do navegador` | Ajuda pt-BR; tela logada não observada → **[conferir]** |
| Claude | Seletor **Chat / Cowork** (pode não aparecer na experiência unificada); aprovação **Manual / Auto / Pular** ("Pular todas as aprovações"); `Configurações > Cowork` | Ajuda pt-BR; **[conferir]** |
| Manus | **Modo Chat / Modo Agent**; modelo **Manus 2.0 Lite**; "assumir o controle"; "Meu Computador" (desktop); `Settings > Cloud Browser` | Ajuda pt-BR mistura português e inglês; **[conferir]** toda a interface |

"Modo agente do ChatGPT" aparece no curso **somente como nome histórico** (julho de 2025 a 2026).

## Alertas herdados do conteúdo bruto

1. "Terminou" não significa "está correto": em benchmarks independentes de assistência web
   multietapas (Princeton HAL), os melhores resultados ficaram entre 35% e 42% de acerto; os números
   medem combinações de modelo e estrutura, não os produtos comerciais, e servem só como ordem de
   grandeza.
2. Injeção de prompt é risco real e brasileiro: STJ identificou comando oculto em recurso especial
   (notícia oficial de 02/09/2026).
3. Nenhum dos três produtos tem *system card* específico publicado (o do ChatGPT agent de 2025
   refere-se ao produto descontinuado).
4. Custo do Manus por tarefa não é previsível; a própria ajuda alerta que estimativas dadas pelo modelo
   podem ser alucinação.
5. Casos CAIXA, Inter e Banlek são histórias de fornecedor (Microsoft, IBM, AWS), não auditorias, e
   tratam de plataformas corporativas, não dos três produtos do curso.
6. Manus: não afirmar que "pertence à Meta" — a empresa anunciou retorno à independência (11/08/2026).
7. Planos, nomes e menus mudam em semanas; revisão humana obrigatória na semana de publicação.
