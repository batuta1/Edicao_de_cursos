# 00 — Contornos do curso ChatGPT Chat

Documento de partida compartilhado pelas duas trilhas (Essentials e Hands-on).

## Origem do pedido

| Campo | Valor |
|---|---|
| Registro no catálogo | `chatgpt-chat-essentials` (Onda 2, trilha T1) |
| Prompt de pesquisa | `Pesquisa Conteudo Onda 2/04-chatgpt-chat-essentials.md` |
| Tema | Fundamentos de IA Generativa |
| Ferramenta-âncora | ChatGPT (OpenAI), web `chatgpt.com`, apps de desktop e celular |
| Competência | Uso de assistente de IA para tarefas gerais (Essentials); fluxos de trabalho com assistente (Hands-on) |
| Tarefa observável — Essentials | Conduzir conversas produtivas no ChatGPT, usando instruções personalizadas, memória, projetos, busca, voz e imagem, e comparar com o Claude Chat |
| Tarefa observável — Hands-on | Resolver um caso completo combinando projetos, arquivos, busca e análise de dados |

## Objeto base

**ChatGPT Chat** — o uso do ChatGPT como assistente de conversa para tarefas gerais: conduzir a
conversa, personalizar e dar continuidade (instruções personalizadas, memória, chat temporário,
projetos), buscar na web com fontes, trabalhar com arquivos e planilhas, usar voz, imagem e Canvas,
proteger dados e verificar respostas.

## Público-alvo

| Trilha | Posição | Antes | Depois | Público |
|---|---|---|---|---|
| T1 — Começando com assistentes de IA | Essentials 2 de 6; Hands-on 5 de 6 | Claude Chat - Essentials / Claude Chat - Hands On | Gemini Chat - Essentials / Claude Skills - Essentials | Qualquer pessoa que ainda não usa IA no dia a dia |
| J1 — Fundamentos de IA para o jurista | 2 de 5 | Claude Chat - Essentials | Gemini Chat - Essentials | Advogados, assessores, estudantes e professores de Direito |
| R1, F1, E1, S1, C1, TE1 | logo depois de Claude Chat - Essentials | — | — | Servidores, negócios, educação, saúde, comunicação, tecnologia |

Consequência de design: exemplos neutros (vida profissional comum) com uma variação jurídica em
cada módulo quando faz diferença real (sigilo de cliente, conferência de norma na fonte oficial).
O caso do Hands-on (reclamações de consumidores de uma loja fictícia) serve aos dois públicos:
é problema de gestão e é problema de Código de Defesa do Consumidor.

## Pré-requisitos

- Ter feito *Claude Chat - Essentials* (recomendado), mas o curso funciona para quem nunca usou IA.
- Nenhum conhecimento técnico.
- Hands-on: ter feito o Essentials deste assunto.

## Recursos necessários

- Computador com navegador atualizado e internet (o curso é desenhado para a web, `chatgpt.com`;
  app de celular é opcional para o recurso de voz).
- Conta ChatGPT **gratuita (Free)**. Segundo a página oficial de preços (pt-BR, acesso 17/11/2026),
  o Free tem conversas de texto ilimitadas sujeitas a proteções contra abuso, Buscar, Projetos e
  Modo Estudo; uploads, análise de dados, visão, voz, memória e criação de imagens são
  "limitados"; tarefas agendadas, Sites e tabelas/gráficos interativos não estão no Free.
- Hands-on: editor de texto simples (Bloco de Notas, TextEdit) para salvar os dois arquivos de
  prática que o próprio curso fornece.

## Configuração

| Campo | Valor |
|---|---|
| Autoinstrucional | **Sim.** Nenhum passo depende de professor; todo exercício tem critério de êxito. |
| Trilhas | Essentials (compreensão) e Hands-on (execução) |
| Carga horária alvo — Essentials | 100–130 min, 4–6 módulos + síntese (`articulate-essentials.md`) |
| Carga horária alvo — Hands-on | 90–120 min, 4 oficinas + Projeto Final (`articulate-hands-on.md`) |
| Idioma | Português do Brasil; rótulos de interface em pt-BR, com o inglês entre parênteses quando ajuda |
| Plano exigido | Free. Onde o Free limita (uploads, análise de dados, imagem), o curso dá rota alternativa |

## Fora do escopo (outro curso cobre)

| Assunto | Curso | O que entra aqui |
|---|---|---|
| Recursos do Claude | Claude Chat - Essentials/Hands On | Só a tabela de comparação |
| Criar GPTs, loja de GPTs | GPTs e Ferramentas do ChatGPT | O que é um GPT e onde abrir um pronto |
| Pesquisa aprofundada | Deep Research - Hands On | Onde fica e para que serve |
| Modo agente, Atlas | Agentes Web, ChatGPT Atlas | Não entra |
| Apps/plugins/conectores, MCP | MCP com ChatGPT | O que são e onde ficam |
| Codex | ChatGPT CODEX | Só a menção na lista de recursos |
| Word e Excel a fundo | ChatGPT Word, ChatGPT Excel | Análise de dados básica (planilha → resumo, tabela, gráfico) |
| Imagem e vídeo como assunto | Imagem com IA, Vídeo com IA | Criar e editar uma imagem na conversa |

## Material-fonte

Pasta `Pesquisa Conteudo Onda 2/conteudo-bruto/chatgpt-chat-essentials/`:

| Arquivo | Uso |
|---|---|
| `ConteudoBruto_chatgpt-chat-essentials.txt` | Pesquisa **parcial** (ajuda da OpenAI devolveu 403); fatos [CONFIRMADO]/[VERIFICAR]/NÃO ENCONTRADO |
| `ChatGPT-precos.html` | Tabela oficial de planos e recursos (pt-BR). **Fonte principal de "o que cada plano libera".** Resolve o conflito do bruto: Projetos aparece como "Sim" no Free |
| `docs-pricing.html` | Preços em US$ (documentação; parece ser de Codex — usado só com ressalva) |
| `system-card-gpt-6-astra.pdf`, `system-card-gpt-5-6.pdf`, `preparedness-framework-v2.pdf` | Contexto de segurança dos modelos; não entram no curso de iniciante (citados só na ementa) |

Complemento feito nesta etapa (17/11/2026), por busca na web, porque a ajuda da OpenAI bloqueia
leitura direta: resumos das páginas de ajuda pt-BR sobre memória (`Configurações > Personalização >
Memória`), controles de dados (`Configurações > Controles de dados > Melhorar o modelo para todos`),
chat temporário (botão "Temporário" no canto superior direito de um chat novo; cópia mantida por
até 30 dias; não cria memória; não treina), uploads (512 MB por arquivo; projetos com 5 arquivos no
Free, 25 no Go/Plus, 40 no Pro/Business/Enterprise/Edu) e seletor de modelos (níveis com nomes que
mudam: o curso ensina a lógica "resposta rápida × raciocínio", não os nomes).

**Regra para dado factual:** número e nome de plano entram com a data de consulta; nome de menu
que não foi visto na tela entra com o caminho mais provável e vai para a lista de conferência do
`README.md`. O curso evita amarrar exercícios a nomes de modelos (GPT-6 Sol, Luna, Astra…), que
mudaram três vezes em 2026.

## Materiais de prática (Hands-on)

O bruto não trouxe arquivos públicos testados. Decisão: **o próprio curso fornece os materiais**,
como texto para o aluno copiar e salvar, o que elimina link quebrado e login:

1. `reclamacoes-loja-aurora.csv` — 24 linhas (6 meses × 4 categorias) de uma loja fictícia.
   Gabarito calculado: 609 reclamações, 501 resolvidas (82,3%); "Troca ou devolucao" salta de 54
   (mai–ago) para 104 (set–out), com taxa de resolução de 64,6% no semestre; setembro (122) e
   outubro (132) são os piores meses.
2. `politica-de-trocas-loja-aurora.txt` — política fictícia vigente desde 01/09/2026 com dois
   conflitos plantados com o Código de Defesa do Consumidor: prazo de 3 dias para desistir de
   compra pela internet (o art. 49 do CDC garante 7 dias) e "análise técnica em até 45 dias" para
   produto com defeito (o art. 18, § 1º, fixa 30 dias para sanar o vício).
3. Fonte pública para conferência: CDC no Planalto,
   `https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm`.

## Alertas herdados do conteúdo bruto

1. Planos, preços e modelos mudam a cada poucas semanas; o curso cita a página de preços como
   fonte e ensina o aluno a consultá-la.
2. Preços em reais: a página oficial não mostrou valores; imprensa de 2025 (Go R$ 39,99, Plus
   R$ 99,90) é antiga. O curso não cita preço em reais.
3. Nomes de menu em pt-BR não foram vistos na tela: conferir na gravação.
