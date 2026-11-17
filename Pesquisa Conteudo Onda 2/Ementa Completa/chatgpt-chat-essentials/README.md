# chatgpt-chat-essentials

Curso **ChatGPT Chat** (Essentials + Hands On), Onda 2, trilha T1 (também J1 e trilhas de
fundamentos), gerado com a skill `criar-ementa-curso` a partir de
`Pesquisa Conteudo Onda 2/conteudo-bruto/chatgpt-chat-essentials/`. Essentials 127 min; Hands-on
119 min.

## Produtos

| Arquivo | O que é |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Roteiro final Essentials (Módulos 0–6), prints, objetivos e habilidades por aula |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Roteiro final Hands-on (caso Loja Aurora: preparação, 4 oficinas, Projeto Final, Parte dos Dez) |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Versão Rise 360 do Essentials: breadcrumbs, cues `» IA:`, ▼▼▼/▲▲▲, "Mão na massa" |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Versão Rise 360 do Hands-on, com os dois arquivos de prática embutidos |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | Tabela MET (cópia da skill) |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | 18 atividades, 127 min, 32% teoria / 68% prática |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | 18 atividades, 119 min, 5% teoria / 95% prática |

## Processo (não é entregável)

| Arquivo | O que é |
|---|---|
| [_processo/00-contornos.md](_processo/00-contornos.md) | Objeto base, públicos, escopo, fontes, materiais de prática com gabarito |
| [_processo/01-v1-essentials.md](_processo/01-v1-essentials.md) | Versão 1.0 do Essentials (modelo base) |
| [_processo/01-v1-hands-on.md](_processo/01-v1-hands-on.md) | Versão 1.0 do Hands-on |
| [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md) | Auditoria (nota 4/10), matriz E1–E13 |
| [_processo/02-analise-hands-on.md](_processo/02-analise-hands-on.md) | Auditoria (nota 3,5/10), matriz H1–H10 |

## Decisões de design

- **Plano Free em tudo.** A tabela oficial de preços (17/11/2026) resolveu o conflito do bruto:
  Projetos é "Sim" no Free (limite de 5 arquivos). O Hands-on usa só dois uploads e tem rota
  "colar o texto" se a cota acabar.
- **Lógica em vez de nome de modelo.** O seletor é ensinado como "resposta rápida × raciocínio";
  nomes GPT-6/GPT-5.6 mudaram várias vezes em 2026 e ficam fora dos exercícios.
- **Privacidade antes do primeiro uso real** (Módulo 2 / passo 1 da preparação), com semáforo de
  dados, LGPD e sigilo profissional para o público jurídico.
- **Materiais de prática embutidos.** O bruto não trouxe arquivos públicos testados; o caso Loja
  Aurora (CSV de 24 linhas + política de trocas, ambos fictícios) é colado no curso, com gabarito
  calculado (609 reclamações; 82,3% resolvidas; troca/devolução 54 → 104) e dois conflitos com o
  CDC conferíveis no Planalto (art. 49: 7 dias; art. 18, § 1º: 30 dias). Serve ao público geral
  (gestão) e ao jurídico (consumidor).
- **Fio condutor:** alucinação (M1 → M4 → M6) e semáforo de dados (M2 → M3 → M5).
- Fora do escopo, com curso de destino: GPTs, pesquisa aprofundada, agentes/Atlas, plugins e MCP,
  Codex, Word/Excel a fundo, imagem e vídeo como assunto.

## O que não foi verificado

Nada foi testado em conta real. A central de ajuda da OpenAI bloqueia leitura direta (403); os
caminhos de menu vêm de resumos oficiais de busca e da página de preços. Rótulos marcados
[conferir] nos roteiros Articulate (6 no Essentials, 2 no Hands-on): "Buscar" no menu "+",
"Ramificar em novo chat", "Modo Estudo", Canvas no Free, preferências do perfil e chat incógnito do
Claude. Conferir na tela na hora da montagem; os exercícios funcionam mesmo que o rótulo mude
(sempre há alternativa por pedido em texto: "pesquise na web", "abra no canvas").

## Próximos passos (fora desta skill)

Carregar no Articulate o `promptArticulate.md` + `roteiros/roteiro-articulate-<trilha>.md` → gerar o
curso → verificação visual → exportar SCORM → `revisar-curso-scorm`.
