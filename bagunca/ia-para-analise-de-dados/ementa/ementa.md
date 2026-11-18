# Ementa — IA para Análise de Dados

## Identificação

| Campo | Definição |
|---|---|
| Curso | IA para Análise de Dados - Essentials e IA para Análise de Dados - Hands On (registro `ia-para-analise-de-dados-essentials`, Onda 2, ranking 18) |
| Natureza | Curto, introdutório, prático e autoinstrucional |
| Trilhas | Essentials (compreensão) e Hands-on (execução) |
| Carga horária total | 232 minutos (Essentials 127 min + Hands-on 105 min), sem contar o tempo de processamento das respostas |
| Público-alvo | Analistas, finanças e planejamento, pesquisadores (T8, posição 5 de 6); escritórios de advocacia, departamentos jurídicos e compliance (J4, posição 2 de 6); finanças e negócios, servidores e regulação, gestores de saúde, engenheiros e técnicos, gestores escolares, comunicação e marketing (F2, R4, S4, TE3, E6, C2) |
| Pré-requisitos | Excel básico (ao menos *Claude Excel - Essentials*); nenhuma programação; nenhuma estatística além de média e porcentagem; para o Hands-on, o Essentials deste assunto |
| Recursos necessários | Computador com navegador e internet; conta ChatGPT (o plano Free atende, com 3 envios de arquivo por dia; o Hands-on cabe em dois dias); conta Julius AI gratuita, opcional; bases públicas do Banco Central, IBGE, CVM e CNJ, baixadas por link direto |
| Material-fonte | Pesquisa de conteúdo bruto de 17/11/2026 (duas rodadas): ajudas oficiais da OpenAI (análise de dados, envio de arquivos, controles de dados, retenção), OpenAI Academy, documentação e política de privacidade do Julius, estudos independentes (JMIR 2025; IEEE VIS 2025; VisEval), bases públicas com gabaritos conferidos por script |

## Objetivo Geral

O curso tem por finalidade capacitar o participante a analisar bases de dados sem programar, por
meio do recurso Análise de dados do ChatGPT, com o Julius AI como segunda opinião: carregar e
compreender a base, corrigir a leitura de formatos brasileiros, explorar os números com os conceitos
estatísticos mínimos, produzir gráficos honestos e interpretar os resultados com verificação contra
número oficial publicado. Como produto final, o participante entrega uma análise conferida do IPCA
de 2020 a 2025 (Essentials) e um resumo executivo da litigiosidade por habitante nos estados,
construído a partir da junção das bases do CNJ e do Censo, com gráfico, premissas e limitações
(Hands-on).

## Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Carregar uma base pública brasileira no assistente e corrigir a leitura de separador, decimal,
   codificação e cabeçalho, decidindo antes do envio se os dados podem ser enviados.
2. Explorar a base com escolhas estatísticas adequadas — média ou mediana, valor absoluto ou taxa,
   valor nominal ou real — e detectar armadilhas de escala e de linhas de total.
3. Produzir gráficos honestos e reconhecer as táticas de distorção documentadas.
4. Conferir resultados com a rotina de cinco verificações e comunicá-los em resumo executivo com
   premissas, limitações e fonte.

## Estrutura das Trilhas

O Essentials constrói o entendimento do ciclo de análise e do princípio da conferência; o Hands-on
exercita a execução completa sobre quatro bases públicas, cada uma com uma armadilha real e um
gabarito oficial. O Hands-on pressupõe o Essentials.

**Essentials (127 min)**

| Módulo | Título | Tempo |
|---|---|---|
| 0 | Preparação e Verificação Inicial | 7 min |
| 1 | Análise de Dados com IA: o que é e como funciona | 19 min |
| 2 | Dados, Privacidade e Sigilo | 15 min |
| 3 | Carregar, Entender e Limpar a Base | 16 min |
| 4 | Explorar sem Cair em Armadilhas | 16 min |
| 5 | Gráficos Honestos | 22 min |
| 6 | Verificar e Comunicar | 16 min |
| 7 | Síntese e Aplicação Integrada | 16 min |

**Hands-on (105 min)**

| Oficina | Título | Tempo |
|---|---|---|
| Preparação | Antes de Arregaçar as Mangas | 7 min |
| 1 | Calcule a inflação sem erro de soma (IPCA) | 16 min |
| 2 | Descubra quem lucrou mais, de verdade (CVM) | 22 min |
| 3 | O número que dobrou (CNJ) | 22 min |
| 4 | Três gráficos, uma verdade (Censo) | 16 min |
| Projeto Final | Onde se litiga mais por habitante (CNJ + Censo) | 22 min |

## Distribuição da Carga Horária

| Trilha | Atividades | Tempo | Teoria : Prática |
|---|---|---|---|
| Essentials | 19 | 127 min | 32% : 68% |
| Hands-on | 19 | 105 min | 11% : 89% |
| **Total** | **38** | **232 min** | — |

Cálculo pela Métrica de Estimativa de Tempo (valores fixos por tipo de atividade); detalhes em
`carga-horaria/`.

## Avaliação

- Essentials: três questões de múltipla escolha com gabarito comentado (Módulos 1, 4, 6),
  exercícios com ponto de controle numérico (IPCA 4,83% e 4,26%; 72 linhas; acentos corretos) e
  atividade integradora no Módulo 7, com tabela de cinco critérios.
- Hands-on: cada oficina termina em "Deu certo?" com o número oficial a reproduzir (IBGE, CVM, CNJ,
  Censo); o Projeto Final tem checklist de seis itens com gabarito por UF.

## Pendências de validação

1. Rótulo do comando que exibe o código no ChatGPT ("Ver análise"/"View analysis") — não consta da
   ajuda oficial.
2. Comportamento do plano Free nos exercícios: os roteiros não foram executados em conta Free real;
   tempo de processamento do arquivo de 11,6 MB do CNJ não medido.
3. Tempo de vida do ambiente Python e destino dos arquivos quando ele reinicia (conta pessoal).
4. Julius: ícone de anexar (`+` ou clipe), preço mensal × anual, comportamento do plano gratuito.
5. IPCA acumulado de 2022 publicado pelo IBGE (o desafio supõe diferença de até 0,01 p.p. em relação
   ao calculado a partir das taxas mensais).
6. Preços em reais do ChatGPT e limites do Free (vigentes em 17/11/2026) a reconferir antes da
   gravação.
