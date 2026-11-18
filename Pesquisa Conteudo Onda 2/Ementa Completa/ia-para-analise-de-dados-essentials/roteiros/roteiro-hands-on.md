# IA para Análise de Dados Para Leigos — Curso Hands-on (roteiro final)

**Público-Alvo:** quem concluiu *IA para Análise de Dados - Essentials* — analistas, finanças,
jurídico, setor público e demais áreas que trabalham com planilhas.

**Objetivo Geral:** conduzir a análise completa de bases públicas reais no ChatGPT, do carregamento
ao resumo dos achados com gráficos, conferindo os números contra a fonte oficial.

**Pré-requisitos:** Essentials deste assunto; conta ChatGPT (o Free atende, em dois dias de estudo,
por causa do limite de 3 uploads por dia); computador com navegador; programa para descompactar
`.zip` (o do próprio Windows ou macOS serve).

## Estrutura do Curso

| Parte | Conteúdo | Tempo |
|---|---|---|
| Preparação | Antes de Arregaçar as Mangas | 7 min |
| Nível 1 — Ler direito | Oficina 1 (IPCA) · Oficina 2 (CVM) | 38 min |
| Nível 2 — Somar e mostrar direito | Oficina 3 (CNJ) · Oficina 4 (Censo) | 38 min |
| Entrega | Projeto Final (CNJ + Censo) | 22 min |
| Anexos | A Parte dos Dez · Conseguiu! E agora? | — |
| **Total** | | **105 min** |

Plano de envios para o plano Free: **dia 1** — Oficinas 1, 2 e 3 (3 envios); **dia 2** — Oficina 4
e Projeto Final (3 envios).

---

## Antes de Arregaçar as Mangas

Aqui você vai analisar dados de verdade e conferir cada número com quem publicou. Quatro bases
públicas, quatro armadilhas reais, um relatório no fim. A IA calcula; você confere.

### Passo 1 — Controles de dados (2 min)

- **📸 Sugestão de Prints:** `ChatGPT > Perfil > Configurações > Controles de dados`, com a chave
  "Melhorar o modelo para todo mundo" em destaque.

Abra `ChatGPT > Perfil (canto inferior esquerdo) > Configurações > Controles de dados` e decida
sobre "Melhorar o modelo para todo mundo". As bases do curso são públicas; em dados de trabalho,
siga o semáforo do Essentials.

### Passo 2 — Baixe as bases (5 min)

- **📸 Sugestão de Prints:** pasta `hands-on-dados` com os cinco itens: `ipca.csv`,
  `dfp_cia_aberta_DRE_con_2024.csv`, `JN_23-Jun-2026.csv`, `Variáveis - JN.csv`,
  `populacao-uf.csv`.

| Arquivo final | Link | Observação |
|---|---|---|
| `ipca.csv` | `api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2020&dataFinal=31/12/2025` | Se abrir na tela: `Arquivo > Salvar como` |
| `dfp_cia_aberta_DRE_con_2024.csv` | `dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2024.zip` | ZIP de 13 MB; extraia e guarde só este CSV (6,8 MB) |
| `JN_23-Jun-2026.csv` e `Variáveis - JN.csv` | `www.cnj.jus.br/wp-content/uploads/2026/09/17-set-2026.zip` | ZIP de 4,2 MB |
| `populacao-uf.csv` | `apisidra.ibge.gov.br/values/t/4709/n3/all/v/93/p/2022?formato=csv` | Se abrir na tela: `Arquivo > Salvar como` |

Para extrair no Windows: clique com o botão direito no `.zip > Extrair tudo`. No Mac: dois cliques
no `.zip`.

> 🔑 Regra de ouro: a IA calcula rápido; quem assina o número é você. Nenhuma oficina termina sem
> conferir com a fonte oficial.

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1 | Quanto vale hoje o salário reajustado em 2024? | 16 min |
| 2 | Quem lucrou mais na bolsa em 2024 — de verdade? | 22 min |
| 3 | Quantos processos novos o Judiciário recebeu em 2025? | 22 min |
| 4 | Como mostrar a população dos estados sem enganar ninguém? | 16 min |
| Projeto Final | Onde se litiga mais por habitante no Brasil? | 22 min |

Cada oficina usa uma base e deixa uma armadilha desarmada.

---

## Oficina 1 — Calcule a inflação sem erro de soma

### 🎯 O Problema

Seu reajuste de janeiro de 2024 vai ser comparado com a inflação. Alguém somou as taxas mensais do
IPCA e chegou a um número. Está certo?

### 🧰 O que você vai usar

- `ipca.csv` e uma conversa nova no ChatGPT.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** (a) menu `+` com "Adicionar fotos e arquivos" destacado; (b) resposta
  com a tabela anual e o controle que exibe o código (rótulo a conferir: "Ver análise").

1. Clique em `ChatGPT > Caixa de mensagem > + > Adicionar fotos e arquivos` e envie `ipca.csv`.
2. Digite: "Antes de calcular, diga linhas, colunas, tipos e período. A coluna valor usa vírgula
   decimal."
3. Digite: "Calcule o IPCA acumulado de cada ano de 2020 a 2025 compondo as taxas mensais. Mostre
   a fórmula."
4. Digite: "Agora some as taxas mensais de 2024. Por que o resultado é diferente?"
5. Abra o código da resposta e localize a multiplicação.
6. Peça: "Faça um gráfico de barras anual, eixo começando em zero, título com a conclusão e a fonte
   no rodapé."

### ✅ Deu certo?

2024 = **4,83%** e 2025 = **4,26%** (iguais ao IBGE); a soma simples de 2024 dá **4,73%** (errada).

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| "Limite de upload atingido" | Espere o horário indicado; tentativa que falha pode contar no limite |
| O número veio como texto | "Converta a coluna valor usando vírgula como decimal" |
| Não acho o código | Peça: "Mostre o código Python que você executou" |

### 🚀 Quer ir além?

1. Corrija R$ 1.000 de janeiro de 2024 até dezembro de 2025. Validação: ≈ R$ 1.092,96.
2. No Julius (opcional), envie o mesmo arquivo, abra "Generated code" e confira 4,83%. Validação:
   mesmo número nas duas ferramentas.
3. Compare 2022 calculado com o publicado pelo IBGE. Validação: diferença de até 0,01 p.p.,
   explicada pelo arredondamento das taxas mensais.

## Descrição

- **Objetivos da Aula:** compor taxas, ler o código do cálculo e conferir com o IBGE.
- **Habilidades Esperadas:** calcular sozinho um acumulado de taxas e flagrar a soma indevida.

---

## Oficina 2 — Descubra quem lucrou mais (de verdade)

### 🎯 O Problema

A diretoria pediu o ranking das companhias abertas mais lucrativas de 2024, direto da CVM. O
primeiro ranking que sai tem uma surpresa no topo. Vamos ver se ela é real.

### 🧰 O que você vai usar

- `dfp_cia_aberta_DRE_con_2024.csv` (32.776 linhas, codificação latin-1) e conversa nova.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** tabela do ranking com a coluna `ESCALA_MOEDA` visível e as linhas da
  Vivara (UNIDADE) e da Petrobras (MIL) selecionadas.

1. Envie o arquivo e digite: "O arquivo está em latin-1 e usa ponto e vírgula. Faça o Raio X."
2. Digite: "Filtre ORDEM_EXERC = ÚLTIMO e CD_CONTA = 3.11.01 (lucro atribuído aos sócios da
   controladora). Quantas linhas e quantas empresas?"
3. Digite: "Ordene pelo VL_CONTA e mostre as 5 primeiras com a coluna ESCALA_MOEDA."
4. Repare: a Vivara aparece em 1º lugar. Pergunte: "A coluna ESCALA_MOEDA tem quais valores? Quantas
   empresas em cada?"
5. Digite: "Converta tudo para reais (MIL × 1.000; UNIDADE × 1) e refaça o top 5 em bilhões."
6. Digite: "Mostre a receita (3.01) e o lucro consolidado (3.11) da Petrobras e explique a diferença
   para 3.11.01."

> 💡 **Dica:** "controladora" é a parte do lucro que pertence aos acionistas da empresa; o
> "consolidado" inclui a fatia de sócios minoritários das controladas.

### ✅ Deu certo?

Top 5: Petrobras **R$ 36,6 bi**, Vale R$ 31,6 bi, Banco do Brasil R$ 26,4 bi, Bradesco R$ 17,3 bi,
Itaúsa R$ 14,8 bi. A Vivara cai para R$ 653 milhões. Petrobras: receita R$ 490,8 bi; consolidado
R$ 37,0 bi.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Acentos quebrados ("�LTIMO") | "Releia com codificação latin-1" |
| Mais de uma linha por empresa | Duas empresas aparecem repetidas; peça "uma linha por CD_CVM" |
| "Não consegui analisar o arquivo inteiro" | Peça para informar quantas linhas leu; compare com 32.776 |

### 🚀 Quer ir além?

1. Conte quantas empresas tiveram prejuízo. Validação: 95.
2. Peça a soma do lucro das 458 empresas. Validação: ≈ R$ 303,9 bi.
3. Pergunte por que a escala existe e onde está documentada. Validação: a resposta cita o
   dicionário de dados da CVM.

## Descrição

- **Objetivos da Aula:** filtrar uma base contábil, normalizar escala e distinguir controladora de
  consolidado.
- **Habilidades Esperadas:** desconfiar de um valor atípico e encontrar sozinho a causa (escala,
  duplicidade) antes de publicar um ranking.

---

## Oficina 3 — O número que dobrou

### 🎯 O Problema

Uma notícia diz que o Judiciário recebeu 40,9 milhões de casos novos em 2025. Você baixou a base do
próprio CNJ e somou. Deu o dobro. Quem errou?

### 🧰 O que você vai usar

- `JN_23-Jun-2026.csv` (11,6 MB, 1.314 colunas, latin-1); `Variáveis - JN.csv` aberto no seu
  computador, só para consulta.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** tabela com as colunas `ano`, `justica`, `sigla` e `cn` filtrada em
  2025, com as linhas `TJ`, `TRF`, `TRT` e `TRE` selecionadas.

1. Envie o arquivo: "Está em latin-1, com ponto e vírgula. Quantas linhas, colunas e quais anos?"
2. Digite: "Some a coluna cn para o ano 2025."
3. Digite: "Liste os valores distintos da coluna sigla em 2025."
4. Repare em `TJ`, `TRF`, `TRT`, `TRE`, `TJM`, `JMU`: são **linhas de total** do ramo, não
   tribunais.
5. Digite: "Refaça a soma de 2025 excluindo as siglas TJ, TRF, TRT, TRE, TJM, JMU e nd. Mostre por
   ramo de justiça."
6. Confira no dicionário: a sigla `cn` aparece com uma descrição que não ajuda — registre isso como
   limitação.

> ⚠️ **Cuidado:** o arquivo não avisa que tem linha de total. A soma "certa" de código bem escrito
> pode estar errada pela premissa.

### ✅ Deu certo?

Soma direta: ≈ **81 milhões**. Sem as linhas de total: **40.940.966** (≈ 40,9 milhões, igual ao
relatório). Só os TJs: 28.288.316.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| A análise demora ou para | Peça só as colunas ano, justica, sigla e cn |
| A IA "corrige" sozinha e não explica | "Liste exatamente as linhas que você excluiu" |
| Resultado perto, mas não igual | Os tribunais superiores (STJ, TST, TSE, STM) entram no total |

### 🚀 Quer ir além?

1. Faça o mesmo para 2024 e compare com o Sumário Executivo 2025 (39,4 mi). Validação: base dá
   ≈ 39,57 mi; registre a diferença como revisão de dados.
2. Mostre a parcela de cada ramo em 2025. Validação: Estadual ≈ 69%.
3. Peça um gráfico de barras por ramo. Validação: eixo em zero, fonte CNJ no rodapé.

## Descrição

- **Objetivos da Aula:** detectar linhas de total escondidas e reproduzir um número oficial.
- **Habilidades Esperadas:** checar sozinho se uma base mistura detalhe e total antes de somar.

---

## Oficina 4 — Três gráficos, uma verdade

### 🎯 O Problema

Você precisa mostrar a população dos estados numa apresentação. Há jeitos honestos e jeitos
enganosos de fazer o mesmo gráfico.

### 🧰 O que você vai usar

- `populacao-uf.csv` e conversa nova.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** os três gráficos lado a lado, com o controle "Alternar para gráfico
  interativo" visível no primeiro.

1. Envie o arquivo: "A primeira linha tem códigos e a segunda os nomes das colunas. Some a
   população."
2. Digite: "Calcule a participação de cada UF no total e ordene."
3. Peça: "Barras horizontais das 10 maiores, ordenadas, eixo em zero, título com a conclusão,
   fonte IBGE Censo 2022 no rodapé." Use **Alternar para gráfico interativo** e passe o mouse.
4. Peça: "A mesma figura com eixo começando em 7 milhões."
5. Peça: "Uma pizza com as 27 UFs."
6. Escolha a versão honesta e baixe o PNG (ícone de download no canto superior direito do gráfico).

### ✅ Deu certo?

Total **203.080.756**; São Paulo ≈ 21,9%. Você explica por escrito por que a versão 4 (eixo
truncado) e a 5 (27 fatias) enganam ou confundem.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| A primeira UF virou cabeçalho | "Use a segunda linha como cabeçalho" |
| Gráfico não fica interativo | Só barras, linhas, pizza e dispersão alternam; os demais vêm como imagem |
| Cores difíceis de distinguir | "Use uma paleta segura para daltônicos" ou informe um código hexadecimal |

### 🚀 Quer ir além?

1. Peça um texto alternativo de duas frases para o gráfico. Validação: cita o maior e o menor.
2. Peça a mediana e compare com a média. Validação: mediana 3,94 mi; média 7,52 mi.
3. Mude as cores pelo código hexadecimal. Validação: o PNG baixado tem a cor escolhida.

## Descrição

- **Objetivos da Aula:** produzir um gráfico honesto e reconhecer eixo truncado e pizza inadequada.
- **Habilidades Esperadas:** escolher e ajustar sozinho o gráfico certo para uma comparação.

---

## Projeto Final — Onde se litiga mais por habitante

### 🎯 A missão

Um escritório quer saber em quais estados se ajuízam mais processos **por habitante**, não em
número absoluto. Junte a base do CNJ com a do Censo e entregue um resumo de uma página.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** tabela final com Tribunal, UF, casos novos, população e taxa por 100
  mil, ordenada, e o gráfico de barras abaixo.

1. Conversa nova; envie `JN_23-Jun-2026.csv` e `populacao-uf.csv`.
2. Peça: "Casos novos (cn) de 2025 dos Tribunais de Justiça estaduais, um por UF, excluindo a
   linha de total TJ. TJDFT corresponde ao Distrito Federal."
3. Peça: "Junte com a população do Censo 2022 por UF e calcule casos novos por 100 mil habitantes.
   Quantas UFs casaram?"
4. Peça gráfico de barras horizontais com as 27 taxas, eixo em zero, fonte nas duas bases.
5. Peça: "Resumo executivo de 5 linhas para o escritório, com premissas e limitações (população de
   2022 × processos de 2025; casos novos incluem execuções e recursos)."
6. Confira três números com a tabela de gabarito abaixo.

### 🏁 Como saber que terminou

- [ ] 27 tribunais, 27 UFs casadas, soma dos TJs = 28.288.316.
- [ ] Maiores taxas: TJRO ≈ 20.421, TJRS ≈ 19.986, TJDFT ≈ 19.691 por 100 mil.
- [ ] Menores: TJPA ≈ 6.745, TJCE ≈ 7.893, TJPE ≈ 8.037.
- [ ] O resumo diz que São Paulo lidera em número absoluto (6,8 milhões) mas não na taxa.
- [ ] Premissas e limitações escritas; nenhuma frase de causa ("porque o povo é mais litigioso").
- [ ] Gráfico com eixo em zero e fonte.

---

## A Parte dos Dez — Armadilhas que você já sabe desarmar

1. Faça o Raio X antes de qualquer conta.
2. Declare separador, decimal e codificação no pedido.
3. Taxas mensais se compõem, não se somam.
4. Valor estranho no topo do ranking? Olhe a escala.
5. Antes de somar, procure linhas de total.
6. Compare por taxa quando os tamanhos forem diferentes.
7. Barras começam no zero.
8. Abra o código do número que vai para o relatório.
9. Confira pelo menos um número com quem publicou.
10. Escreva premissas e limitações — elas protegem você.

## Conseguiu! E agora?

Você conferiu inflação com o IBGE, lucro com a CVM e processos com o CNJ, e desarmou quatro
armadilhas que pegam muita gente boa. Repita o ciclo com uma base da sua área antes de usar dados
de trabalho — e sempre dentro da política de dados da sua organização.

Próximo passo: *Dados com Python e IA* leva tudo isso para um projeto reprodutível, que roda de novo
do zero com um clique.

---

## Rastreabilidade da auditoria

| Achado | Destino |
|---|---|
| H1 Sem preparação | Antes de Arregaçar: Passos 1 e 2, plano de envios |
| H2 O1 sem caso | Oficina 1 (IPCA; 4,83%/4,26%; armadilha 4,73%) |
| H3 O2 sem caso | Oficina 2 (CVM; escala MIL/UNIDADE; R$ 36,6 bi) |
| H4 Sem armadilha de agregação | Oficina 3 (CNJ; linhas de total; 40,9 mi) |
| H5 Gráfico sem honestidade | Oficina 4 |
| H6 Passos implícitos | Breadcrumbs e prints em todas as oficinas |
| H7 Se travar genérico | Tabelas com problemas reais por oficina |
| H8 Julius ausente | Oficina 1, "Quer ir além?" 2 (opcional) |
| H9 Projeto Final fraco | Projeto Final com gabarito por UF |
| H10 Um desafio só | Três desafios com validação por oficina |
| H11 Carga horária | 105 min (ver `carga-horaria/carga-horaria-hands-on.md`) |
| H12 Parte dos Dez genérica | Dez armadilhas vistas nas oficinas |

Decisão consciente: o Julius não aparece no Projeto Final (créditos do plano gratuito e arquivos
apagados após uma hora de inatividade tornariam a entrega instável).
