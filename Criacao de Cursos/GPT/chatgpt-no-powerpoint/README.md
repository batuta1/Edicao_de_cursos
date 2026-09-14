# ChatGPT no PowerPoint — pacote de curso

Curso curto, introdutório e autoinstrucional sobre o suplemento oficial ChatGPT para PowerPoint,
destinado a professores universitários. Duas trilhas, 237 minutos no total.

Gerado pela skill `criar-ementa-curso`, Fases 0 a 7.

## Índice da pasta

### Produtos

| Arquivo | O que é |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada — identificação, objetivo, competências, mapa das trilhas, carga horária e pendências. É o documento de decisão. |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Plano de aula completo da trilha Essentials, com objetivos, habilidades, sugestões de print e solução de problemas por módulo. |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Curso completo da trilha Hands-on, com as cinco oficinas, o Projeto Final e A Parte dos Dez. |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Versão da trilha Essentials pronta para o Articulate Rise 360: breadcrumbs no lugar de prints, cues `» IA:` e marcadores de lição. |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Versão da trilha Hands-on pronta para o Rise 360, com os mesmos recursos de montagem. |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | A tabela MET aplicada neste curso, com as regras de contagem adotadas. |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | Breakdown atividade a atividade da trilha Essentials: 124 min, 17 atividades, 37,9 % teoria. |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | Breakdown atividade a atividade da trilha Hands-on: 113 min, 17 atividades, 26,5 % teoria. |

### Processo (não é entregável)

| Arquivo | O que é |
|---|---|
| [_processo/00-contornos.md](_processo/00-contornos.md) | Fase 0 — objeto base, público, pré-requisitos, carga horária alvo e os três fatos centrais que o curso precisa deixar explícitos. |
| [_processo/01-v1-essentials.md](_processo/01-v1-essentials.md) | Fase 1 — primeira versão da trilha Essentials, antes da auditoria. |
| [_processo/01-v1-hands-on.md](_processo/01-v1-hands-on.md) | Fase 1 — primeira versão da trilha Hands-on, antes da auditoria. |
| [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md) | Fase 2 — auditoria crítica da Essentials, com matriz de doze soluções. |
| [_processo/02-analise-hands-on.md](_processo/02-analise-hands-on.md) | Fase 2 — auditoria crítica da Hands-on, com matriz de onze soluções. |

## Números do curso

| | Essentials | Hands-on | Total |
|---|---|---|---|
| Unidades | 6 módulos | 5 oficinas + Projeto Final | — |
| Atividades | 17 | 17 | 34 |
| Duração | 124 min | 113 min | 237 min |
| Teoria : Prática | 37,9 % : 62,1 % | 26,5 % : 73,5 % | 32,5 % : 67,5 % |

## Decisão estrutural que distingue este curso

Ambas as trilhas abrem por um módulo de decisão que **pode concluir que o curso não se aplica** ao
ambiente do participante, quando a instituição bloqueia a instalação de suplementos do Office. Nesse
caso, o roteiro encaminha explicitamente ao curso irmão [ChatGPT no Word](../chatgpt-no-word/), cujo
fluxo principal não depende de suplemento algum.

A alternativa — manter o participante em um curso que ele não conseguirá executar — foi rejeitada na
auditoria. A justificativa está em [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md),
gargalo 3.

## O que NÃO foi verificado

O material-fonte é documento único da Central de Ajuda da OpenAI, de cerca de 11 KB. É fonte primária
confiável, mas curto — **este é o curso do lote com maior risco de afirmação não sustentada.** A
lista completa, com o local de cada afirmação, está na seção "Pendências de Validação" de
[ementa.md](ementa.md). Em ordem de prioridade:

1. **Termos do Marketplace de Suplementos da Microsoft** quanto à leitura do conteúdo dos arquivos.
   É a afirmação de maior peso do curso e sustenta todo o Módulo 0 / Oficina 0. **Conferir primeiro.**
2. **Versão mínima do PowerPoint** compatível com o suplemento — não consta do material-fonte.
3. **Rótulos exatos dos menus em português**, usados em todos os breadcrumbs das versões Articulate:
   `Página Inicial > Suplementos`, `Design > Temas`,
   `Exibir > Modo de Exibição de Estrutura de Tópicos`, `Exibir > Classificação de Slides`,
   `Página Inicial > Layout`.
4. **Consumo de créditos** (10 a 50 por mensagem) e condições de uso por plano.
5. **Disponibilidade de Skills e apps** na interface do PowerPoint. Todo o Módulo 4 da Essentials
   depende deste ponto e está redigido de forma condicional.
6. **Erro de SSO** e se a correção pelo endereço de retorno no provedor de identidade permanece
   válida.
7. **Aparência da barra lateral** e nome do controle descrito na fonte apenas como "símbolo de
   adição".

## Próximo passo da esteira

1. Conferir as pendências acima, começando pela primeira.
2. Carregar no Articulate Rise 360 o `promptArticulate.md` do projeto junto com o roteiro Articulate
   da trilha desejada.
3. Gerar o curso e fazer a verificação visual.
4. Exportar o SCORM.
5. Revisar os textos com a skill `revisar-curso-scorm`.
