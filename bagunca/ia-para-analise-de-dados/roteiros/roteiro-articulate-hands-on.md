# IA para Análise de Dados Para Leigos — Curso Hands-on

> *» IA: Cover — título e subtítulo; preservar verbatim; não traduzir "ChatGPT" nem "Julius".*

*Em menos de duas horas, você vai analisar quatro bases públicas de verdade — inflação, bolsa,
Judiciário e Censo — e conferir cada número com quem o publicou.*

# Antes de Arregaçar as Mangas

> *» IA: Text — parágrafo verbatim.*

Aqui não tem palestra: você vai analisar dados reais conversando com o ChatGPT. São quatro bases
públicas, quatro armadilhas que pegam muita gente boa e um relatório no fim. Duração total: 105
minutos, divididos em dois dias se você usa o plano Free (ele permite 3 envios de arquivo por dia).

> *» IA: Checklist — itens verbatim.*

**O que você precisa ter aberto agora:**

- `chatgpt.com` com sua conta (o Free serve).
- Uma pasta no computador chamada `hands-on-dados`.
- O programa de descompactar do seu sistema (o do Windows ou do Mac já resolve).

> *» IA: Process — preparação em dois passos; preservar os breadcrumbs e os endereços.*

**Preparação (7 min)**

1. Abra `ChatGPT > Perfil (canto inferior esquerdo) > Configurações > Controles de dados` e decida
   sobre **Melhorar o modelo para todo mundo**. As bases do curso são públicas; dados de trabalho
   seguem o semáforo do Essentials.
2. Baixe as bases da tabela abaixo para a pasta `hands-on-dados`. Para extrair um `.zip`: no
   Windows, `Botão direito no arquivo > Extrair tudo`; no Mac, dois cliques no arquivo.

> *» IA: Table — verbatim; preservar os endereços.*

| Arquivo final | Endereço | Observação |
|---|---|---|
| `ipca.csv` | `api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2020&dataFinal=31/12/2025` | Se abrir na tela: `Navegador > Arquivo > Salvar como` |
| `dfp_cia_aberta_DRE_con_2024.csv` | `dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2024.zip` | ZIP de 13 MB; guarde só este CSV (6,8 MB) |
| `JN_23-Jun-2026.csv` e `Variáveis - JN.csv` | `www.cnj.jus.br/wp-content/uploads/2026/09/17-set-2026.zip` | ZIP de 4,2 MB |
| `populacao-uf.csv` | `apisidra.ibge.gov.br/values/t/4709/n3/all/v/93/p/2022?formato=csv` | Se abrir na tela: `Navegador > Arquivo > Salvar como` |

> *» IA: Statement — preservar o emoji.*

> 🔑 **Regra de ouro:** a IA calcula rápido; quem assina o número é você. Nenhuma oficina termina
> sem conferir com a fonte oficial.

> *» IA: Statement — plano de envios; preservar o emoji.*

> 📌 **Plano de envios no Free:** dia 1 — Oficinas 1, 2 e 3 (três envios); dia 2 — Oficina 4 e
> Projeto Final (três envios).

# O Mapa da Mão na Massa

> *» IA: Table — verbatim.*

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1 | Quanto vale hoje um reajuste de 2024? | 16 min |
| 2 | Quem lucrou mais na bolsa em 2024 — de verdade? | 22 min |
| 3 | Quantos processos novos o Judiciário recebeu em 2025? | 22 min |
| 4 | Como mostrar a população dos estados sem enganar ninguém? | 16 min |
| Projeto Final | Onde se litiga mais por habitante no Brasil? | 22 min |

> *» IA: Text — frase verbatim.*

Cada oficina usa uma base e desarma uma armadilha; o Projeto Final junta duas bases sozinho.

---

# Oficina 1 — Calcule a inflação sem erro de soma

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

Seu reajuste de janeiro de 2024 vai ser comparado com a inflação. Um colega somou as taxas mensais
do IPCA e chegou a um número. Está certo? (16 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- `ipca.csv` (72 linhas, separador ponto e vírgula, vírgula decimal).
- Uma conversa nova no ChatGPT.

### 👐 Mão na massa

> *» IA: Process — um passo por etapa; preservar os breadcrumbs; textos a digitar verbatim.*

1. Clique em `ChatGPT > Caixa de mensagem > + > Adicionar fotos e arquivos` e envie `ipca.csv`.
2. Digite: "Antes de calcular, diga linhas, colunas, tipos e período. A coluna valor usa vírgula
   decimal."
3. Digite: "Calcule o IPCA acumulado de cada ano de 2020 a 2025 compondo as taxas mensais. Mostre a
   fórmula."
4. Digite: "Agora some as taxas mensais de 2024. Por que o resultado é diferente?"
5. Abra o código no fim da resposta (`Resposta > comando de exibir código` — o rótulo pode aparecer
   como "Ver análise"; se não aparecer, peça "Mostre o código Python que você executou") e ache a
   multiplicação.
6. Digite: "Faça um gráfico de barras anual, eixo começando em zero, título com a conclusão e a
   fonte no rodapé."

> *» IA: Statement — preservar o emoji.*

> 💡 **Dica:** taxa se compõe como juros: 1% em janeiro e 1% em fevereiro dá 2,01%, não 2%. Em doze
> meses, a diferença aparece.

### ✅ Deu certo?

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: na conversa, 2024 = **4,83%** e 2025 = **4,26%** (iguais ao IBGE); a soma
> simples de 2024 dá **4,73%** — e você sabe dizer por que está errada.

### 🚑 Se travar

> *» IA: Accordion — um item por linha da tabela; título = Problema, corpo = O que fazer.*

| Problema | O que fazer |
|---|---|
| "Limite de upload atingido" | Espere o horário indicado na mensagem; tentativa que falha pode contar no limite |
| O número veio como texto | Digite: "Converta a coluna valor usando vírgula como decimal" |
| Não acho o código | Peça: "Mostre o código Python que você executou" |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL; um desafio por item, com a validação.*

1. Corrija R$ 1.000 de janeiro de 2024 até dezembro de 2025. Validação: ≈ R$ 1.092,96.
2. No Julius (opcional), envie o mesmo arquivo pelo ícone `Julius > +` da barra de chat (ou arraste o arquivo para a conversa), abra **Generated code** e
   confira 4,83%. Validação: o mesmo número nas duas ferramentas.
3. Compare o acumulado de 2022 com o publicado pelo IBGE. Validação: diferença de até 0,01 ponto
   percentual, explicada pelo arredondamento das taxas mensais.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 2 — Descubra quem lucrou mais (de verdade)

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

A diretoria pediu o ranking das companhias abertas mais lucrativas de 2024, direto da CVM. O primeiro
ranking que sai tem uma surpresa no topo. Vamos descobrir se ela é real. (22 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- `dfp_cia_aberta_DRE_con_2024.csv` (32.776 linhas, codificação latin-1).
- Uma conversa nova no ChatGPT.

### 👐 Mão na massa

> *» IA: Process — um passo por etapa; preservar os breadcrumbs; textos a digitar verbatim; não traduzir nomes de colunas.*

1. Envie o arquivo por `ChatGPT > Caixa de mensagem > + > Adicionar fotos e arquivos` e digite: "O
   arquivo está em latin-1 e usa ponto e vírgula. Faça o Raio X."
2. Digite: "Filtre ORDEM_EXERC = ÚLTIMO e CD_CONTA = 3.11.01 (lucro atribuído aos sócios da
   controladora). Quantas linhas e quantas empresas?"
3. Digite: "Ordene pelo VL_CONTA e mostre as 5 primeiras, com a coluna ESCALA_MOEDA."
4. Repare: a Vivara aparece em 1º lugar. Pergunte: "Quais valores existem em ESCALA_MOEDA e quantas
   empresas há em cada um?"
5. Digite: "Converta tudo para reais (MIL vezes 1.000; UNIDADE vezes 1) e refaça o top 5 em
   bilhões."
6. Digite: "Mostre a receita (3.01) e o lucro consolidado (3.11) da Petrobras e explique a diferença
   para 3.11.01."

> *» IA: Statement — preservar o emoji.*

> 💡 **Dica:** "controladora" é a parte do lucro que pertence aos acionistas da própria empresa; o
> "consolidado" inclui também a fatia dos sócios minoritários das empresas controladas.

### ✅ Deu certo?

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: top 5 em reais — Petrobras **R$ 36,6 bi**, Vale R$ 31,6 bi, Banco do Brasil
> R$ 26,4 bi, Bradesco R$ 17,3 bi, Itaúsa R$ 14,8 bi; a Vivara cai para R$ 653 milhões. Petrobras:
> receita R$ 490,8 bi; consolidado R$ 37,0 bi.

### 🚑 Se travar

> *» IA: Accordion — um item por linha da tabela; título = Problema, corpo = O que fazer.*

| Problema | O que fazer |
|---|---|
| Acentos quebrados ("�LTIMO") | Digite: "Releia com codificação latin-1" |
| Mais de uma linha por empresa | Duas empresas vêm repetidas; peça "uma linha por CD_CVM" |
| "Não consegui analisar o arquivo inteiro" | Peça o número de linhas lidas e compare com 32.776 |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL; um desafio por item, com a validação.*

1. Conte quantas empresas tiveram prejuízo. Validação: 95.
2. Peça a soma do lucro das 458 empresas. Validação: ≈ R$ 303,9 bi.
3. Pergunte onde a escala está documentada. Validação: a resposta aponta o dicionário de dados da
   CVM (pasta META do mesmo endereço).

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 3 — O número que dobrou

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

O relatório Justiça em Números diz que o Judiciário recebeu 40,9 milhões de casos novos em 2025.
Você baixou a base do próprio CNJ e somou. Deu o dobro. Quem errou? (22 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- `JN_23-Jun-2026.csv` (11,6 MB, 1.314 colunas, latin-1).
- `Variáveis - JN.csv` aberto no seu computador, só para consulta.

### 👐 Mão na massa

> *» IA: Process — um passo por etapa; preservar os breadcrumbs; textos a digitar verbatim; não traduzir nomes de colunas nem siglas.*

1. Envie o arquivo por `ChatGPT > Caixa de mensagem > + > Adicionar fotos e arquivos` e digite: "Está
   em latin-1, com ponto e vírgula. Quantas linhas, colunas e quais anos?"
2. Digite: "Some a coluna cn para o ano 2025."
3. Digite: "Liste os valores distintos da coluna sigla em 2025."
4. Repare em `TJ`, `TRF`, `TRT`, `TRE`, `TJM` e `JMU`: são **linhas de total** do ramo, não tribunais.
5. Digite: "Refaça a soma de 2025 excluindo as siglas TJ, TRF, TRT, TRE, TJM, JMU e nd. Mostre por
   ramo de justiça."
6. Procure `cn` no dicionário: a descrição não ajuda. Anote isso como limitação.

> *» IA: Statement — preservar o emoji.*

> ⚠️ **Cuidado:** o arquivo não avisa que tem linha de total. Um código perfeito pode errar se a
> premissa estiver errada.

### ✅ Deu certo?

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: soma direta ≈ **81 milhões**; sem as linhas de total, **40.940.966**
> (≈ 40,9 milhões, igual ao relatório). Só os Tribunais de Justiça: 28.288.316.

### 🚑 Se travar

> *» IA: Accordion — um item por linha da tabela; título = Problema, corpo = O que fazer.*

| Problema | O que fazer |
|---|---|
| A análise demora ou para | Peça para usar só as colunas ano, justica, sigla e cn |
| A IA "corrige" sozinha e não explica | Digite: "Liste exatamente as linhas que você excluiu" |
| Resultado perto, mas não igual | Os tribunais superiores (STJ, TST, TSE, STM) também entram no total |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL; um desafio por item, com a validação.*

1. Faça o mesmo para 2024 e compare com o Sumário Executivo 2025 do CNJ (39,4 milhões). Validação: a
   base dá ≈ 39,57 milhões; registre a diferença como revisão de dados.
2. Calcule a parcela de cada ramo em 2025. Validação: Justiça Estadual ≈ 69%.
3. Peça um gráfico de barras por ramo. Validação: eixo em zero e fonte CNJ no rodapé.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 4 — Três gráficos, uma verdade

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

Você precisa mostrar a população dos estados numa apresentação. O mesmo dado pode virar um gráfico
honesto ou um gráfico que engana. Vamos fazer os dois e escolher. (16 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- `populacao-uf.csv` (cabeçalho em duas linhas).
- Uma conversa nova no ChatGPT.

### 👐 Mão na massa

> *» IA: Process — um passo por etapa; preservar os breadcrumbs; não traduzir termos de interface.*

1. Envie o arquivo e digite: "A primeira linha tem códigos e a segunda os nomes das colunas. Some a
   população."
2. Digite: "Calcule a participação de cada UF no total e ordene."
3. Digite: "Barras horizontais das 10 maiores, ordenadas, eixo em zero, título com a conclusão,
   fonte IBGE Censo 2022 no rodapé." Clique em `Gráfico > Alternar para gráfico interativo` e passe o
   mouse sobre as barras.
4. Digite: "A mesma figura com o eixo começando em 7 milhões."
5. Digite: "Uma pizza com as 27 UFs."
6. Escolha a versão honesta e baixe em `Gráfico > ícone de download (canto superior direito)`.

> *» IA: Statement — preservar o emoji.*

> 🤓 **Curiosidade técnica (pode pular):** só barras, linhas, pizza e dispersão ficam interativos;
> os outros tipos chegam como imagem.

### ✅ Deu certo?

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: total **203.080.756**; São Paulo ≈ 21,9%; PNG salvo em `hands-on-dados`; e
> duas frases suas explicando por que o eixo em 7 milhões engana e a pizza de 27 fatias confunde.

### 🚑 Se travar

> *» IA: Accordion — um item por linha da tabela; título = Problema, corpo = O que fazer.*

| Problema | O que fazer |
|---|---|
| A primeira UF virou cabeçalho | Digite: "Use a segunda linha como cabeçalho" |
| O gráfico não fica interativo | Só barras, linhas, pizza e dispersão alternam |
| Cores difíceis de distinguir | Peça "paleta segura para daltônicos" ou informe um código hexadecimal |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL; um desafio por item, com a validação.*

1. Peça um texto alternativo de duas frases para o gráfico. Validação: cita o maior e o menor estado.
2. Peça média e mediana. Validação: média ≈ 7,52 milhões; mediana 3,94 milhões.
3. Troque a cor pelo código hexadecimal. Validação: o PNG baixado tem a cor escolhida.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Projeto Final — Onde se litiga mais por habitante

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Projeto Final" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 A missão

> *» IA: Text — verbatim.*

Um escritório quer saber em quais estados se ajuízam mais processos **por habitante**, e não em
número absoluto. Junte a base do CNJ com a do Censo e entregue um resumo de uma página, com gráfico
e premissas. (22 min, dois envios)

### 👐 Mão na massa

> *» IA: Process — passos verbatim; preservar os breadcrumbs; não traduzir siglas.*

1. Abra uma conversa nova e envie `JN_23-Jun-2026.csv` e `populacao-uf.csv`.
2. Digite: "Casos novos (cn) de 2025 dos Tribunais de Justiça estaduais, um por UF, excluindo a linha
   de total TJ. TJDFT corresponde ao Distrito Federal."
3. Digite: "Junte com a população do Censo 2022 por UF e calcule casos novos por 100 mil habitantes.
   Quantas UFs casaram?"
4. Peça um gráfico de barras horizontais com as 27 taxas, eixo em zero e as duas fontes no rodapé.
5. Digite: "Resumo executivo de 5 linhas para o escritório, com premissas e limitações: população de
   2022 contra processos de 2025; casos novos incluem execuções e recursos."
6. Confira pelo menos três números com a checklist abaixo.

> *» IA: Statement — modelo de resumo; verbatim, entre aspas triplas.*

"""
Pergunta: em quais UFs se ajuízam mais casos novos por habitante?
Achado principal: [UF com maior taxa] ([taxa] por 100 mil) — [UF com menor taxa] ([taxa]).
Comparação: São Paulo lidera em número absoluto, mas não na taxa.
Premissas: casos novos (cn) dos TJs em 2025; população do Censo 2022; linha de total TJ excluída.
Limitações: anos diferentes nas duas bases; casos novos incluem execuções e recursos; não indica causa.
Fontes: CNJ, Justiça em Números (base de 17/09/2026); IBGE, Censo 2022 (tabela 4709).
"""

### 🏁 Como saber que terminou

> *» IA: Checklist — itens verbatim.*

- [ ] 27 tribunais, 27 UFs casadas e soma dos TJs = 28.288.316.
- [ ] Maiores taxas: TJRO ≈ 20.421, TJRS ≈ 19.986 e TJDFT ≈ 19.691 por 100 mil.
- [ ] Menores taxas: TJPA ≈ 6.745, TJCE ≈ 7.893 e TJPE ≈ 8.037.
- [ ] O resumo diz que São Paulo lidera em número absoluto (6,8 milhões), mas não na taxa.
- [ ] Premissas e limitações escritas; nenhuma frase de causa.
- [ ] Gráfico com eixo em zero e as duas fontes.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Projeto Final" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# A Parte dos Dez — Armadilhas que você já sabe desarmar

> *» IA: List — numerada, verbatim.*

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

> *» IA: Text — verbatim.*

Você conferiu inflação com o IBGE, lucro com a CVM e processos com o CNJ, e desarmou quatro
armadilhas reais. Repita o ciclo com uma base da sua área antes de usar dados de trabalho — e sempre
dentro da política de dados da sua organização.

Próximo passo: *Dados com Python e IA* leva tudo isso para um projeto reprodutível, que roda de novo
do zero com um comando.
