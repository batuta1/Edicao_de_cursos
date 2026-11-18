# n8n-agentes-de-ia-essentials

Pacote completo do curso **Agentes de IA no n8n**, gerado com a skill `criar-ementa-curso` a partir do conteúdo bruto em `Pesquisa Conteudo Onda 1/conteudo-bruto/n8n-agentes-de-ia-essentials-6/`.

## Resultado

- Essentials: 5 módulos, 115 minutos.
- Hands-on: 4 oficinas + Projeto Final, 105 minutos.
- Total: 220 minutos, com 34% de teoria e 66% de prática.
- Versões editáveis em Markdown e quatro PDFs de distribuição.

## Produtos

| Arquivo | Finalidade |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Plano conceitual final |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Curso prático final |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Roteiro operacional Essentials para Rise 360 |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Roteiro operacional Hands-on para Rise 360 |
| [roteiros/pdf/roteiro-essentials.pdf](roteiros/pdf/roteiro-essentials.pdf) | PDF do plano Essentials |
| [roteiros/pdf/roteiro-hands-on.pdf](roteiros/pdf/roteiro-hands-on.pdf) | PDF do curso Hands-on |
| [roteiros/pdf/roteiro-articulate-essentials.pdf](roteiros/pdf/roteiro-articulate-essentials.pdf) | PDF operacional Essentials para Rise 360 |
| [roteiros/pdf/roteiro-articulate-hands-on.pdf](roteiros/pdf/roteiro-articulate-hands-on.pdf) | PDF operacional Hands-on para Rise 360 |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | Tabela MET aplicada |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | Cálculo reproduzível do Essentials |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | Cálculo reproduzível do Hands-on |

## Decisões de design

- Essentials não contém pílulas Hands-on nem solicita operação externa ao Rise.
- Cada lição Essentials usa avaliação nativa e aplicação conceitual.
- Hands-on usa um único workflow cumulativo, com breadcrumbs, pontos de controle e troubleshooting.
- Statements dos roteiros Articulate contêm uma única frase curta.
- RAG, memória e ação são introduzidos separadamente para permitir diagnóstico.
- A ação sensível usa menor privilégio, confirmação, human review quando disponível e auditoria.
- Os rótulos permanecem em inglês, conforme a ajuda oficial consultada.

## Processo

Arquivos de contorno, versões iniciais e auditorias ficam em `_processo/`. Eles documentam decisões, mas não são entregáveis ao participante.

## Validação humana antes da publicação

1. Confirmar os caminhos e rótulos na conta n8n usada para gravar.
2. Testar modelo, memória, vector store, Guardrails, human review e destino de ação.
3. Revalidar planos, limites, políticas de dados e recursos em preview.
4. Montar os cursos no Rise 360, revisar em computador e celular e testar todos os gabaritos.

