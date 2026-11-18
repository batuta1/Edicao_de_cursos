# ChatGPT Chat Para Leigos — Curso Hands-on

> *» IA: Cover — título e subtítulo; preservar verbatim.*

*Em menos de duas horas, você vai resolver um caso de verdade com o ChatGPT: do documento e da
planilha a um relatório de uma página, com números conferidos e lei citada na fonte.*

# Antes de Arregaçar as Mangas

> *» IA: Text — parágrafo verbatim.*

Aqui não tem palestra: você vai fazer. O caso é fictício e completo: a **Loja Aurora** vende
eletrodomésticos pela internet e, desde setembro de 2026, as reclamações de troca e devolução
explodiram. A diretoria quer saber o tamanho do problema, se a política de trocas tem algo errado e
o que fazer. Cada oficina resolve um pedaço; no fim, as peças viram um relatório. Duração total:
119 minutos.

> *» IA: Checklist — itens verbatim.*

**O que você precisa ter aberto agora:**

- `chatgpt.com` com sua conta (o plano Free serve).
- Um editor de texto simples (Bloco de Notas no Windows; TextEdit no Mac, em modo texto simples).
- Uma pasta no computador chamada `caso-aurora`.

> *» IA: Process — preparação em dois passos; preservar os breadcrumbs.*

**Preparação (7 min)**

1. Abra `ChatGPT > Perfil (canto inferior esquerdo) > Configurações > Controles de dados` e decida
   se mantém "Melhorar o modelo para todos". Aqui tudo é fictício; no trabalho, vale o semáforo do
   Essentials: dado pessoal de terceiro, segredo comercial e documento de cliente não vão para
   conta pessoal.
2. Salve os dois arquivos do caso, copiando os blocos abaixo para o editor. No Bloco de Notas,
   escolha `Arquivo > Salvar como > Tipo: Todos os arquivos`, para o CSV não virar `.csv.txt`.

> *» IA: Statement — arquivo de prática 1; conteúdo verbatim, sem nenhuma alteração; oferecer também como Download "reclamacoes-loja-aurora.csv".*

Arquivo `reclamacoes-loja-aurora.csv`:

"""
mes,categoria,reclamacoes,resolvidas,prazo_medio_dias
2026-05,Atraso na entrega,42,38,6
2026-05,Produto com defeito,25,20,12
2026-05,Troca ou devolucao,12,11,4
2026-05,Cobranca indevida,9,9,3
2026-06,Atraso na entrega,38,35,5
2026-06,Produto com defeito,27,22,11
2026-06,Troca ou devolucao,14,13,4
2026-06,Cobranca indevida,8,8,3
2026-07,Atraso na entrega,45,41,6
2026-07,Produto com defeito,24,19,13
2026-07,Troca ou devolucao,13,12,5
2026-07,Cobranca indevida,10,9,4
2026-08,Atraso na entrega,40,37,5
2026-08,Produto com defeito,26,21,12
2026-08,Troca ou devolucao,15,14,4
2026-08,Cobranca indevida,7,7,3
2026-09,Atraso na entrega,39,36,6
2026-09,Produto com defeito,28,22,12
2026-09,Troca ou devolucao,46,25,15
2026-09,Cobranca indevida,9,9,3
2026-10,Atraso na entrega,41,38,5
2026-10,Produto com defeito,25,20,13
2026-10,Troca ou devolucao,58,27,18
2026-10,Cobranca indevida,8,8,3
"""

> *» IA: Statement — arquivo de prática 2; conteúdo verbatim; oferecer também como Download "politica-de-trocas-loja-aurora.txt".*

Arquivo `politica-de-trocas-loja-aurora.txt`:

"""
POLÍTICA DE TROCAS E DEVOLUÇÕES — LOJA AURORA
(Documento fictício, criado para fins didáticos)
Versão 2 — vigente desde 01/09/2026. A versão 1, válida até 31/08/2026, previa 7 dias para desistência.

1. Desistência de compras feitas pelo site: o cliente pode desistir em até 3 (três) dias corridos, contados do recebimento do produto.
2. Produto com defeito: a troca depende de análise técnica, concluída em até 45 (quarenta e cinco) dias.
3. Produtos em promoção têm as mesmas garantias dos demais.
4. Atendimento: e-mail e chat, de segunda a sexta, das 9h às 18h.
5. Prazo de resposta a reclamações: até 5 (cinco) dias úteis.
"""

> *» IA: Statement — regra de ouro; preservar o emoji.*

> 🔑 **Regra de ouro:** o ChatGPT é seu estagiário rápido, não seu chefe. Ele faz o rascunho; você
> confere os números e a lei antes de assinar.

# O Mapa da Mão na Massa

> *» IA: Table — verbatim.*

| Oficina | Problema que vai resolver | Tempo |
|---|---|---|
| 1 | Tirar o caso das conversas soltas e montar um projeto | 20 min |
| 2 | Descobrir o que a política diz, sem ler tudo e sem cair em invenção | 20 min |
| 3 | Saber se a política está de acordo com a lei | 20 min |
| 4 | Transformar a planilha em números e gráfico | 20 min |
| Projeto Final | Entregar o relatório de uma página para a diretoria | 26 min |

> *» IA: Text — frase verbatim.*

As oficinas são em sequência: cada uma usa o que a anterior deixou pronto.

---

# Oficina 1 — Monte o projeto do caso

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

Você abriu três conversas sobre a Loja Aurora e já não sabe qual tinha o quê. Vamos criar uma pasta
inteligente — um **projeto** — onde tudo do caso mora junto e segue as mesmas regras. (20 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- Projetos do ChatGPT.
- O arquivo `politica-de-trocas-loja-aurora.txt`.

### 👐 Mão na massa

> *» IA: Process — um passo por etapa; preservar os breadcrumbs; não traduzir termos de interface.*

1. Clique em `ChatGPT > Barra lateral > Novo projeto`.
2. Digite o nome `Caso Loja Aurora`.
3. Abra `Novo projeto > ícone de engrenagem > Memória` e escolha **Apenas do projeto**. Clique em
   **Criar projeto**. ("Apenas do projeto" quer dizer: o que entra aqui não vaza para outras
   conversas, e vice-versa.)
4. Abra `Caso Loja Aurora > Instruções` e cole o texto do bloco abaixo. Salve.
5. Em `Caso Loja Aurora > Arquivos > Adicionar arquivos`, envie `politica-de-trocas-loja-aurora.txt`.
6. Ainda dentro do projeto, comece uma conversa e pergunte: "Qual é o prazo de desistência para
   compras no site?"

> *» IA: Statement — instruções do projeto; verbatim, entre aspas triplas.*

"""
Você apoia a análise de reclamações da Loja Aurora (caso fictício). Responda em português do
Brasil, de forma objetiva. Ao usar um arquivo, cite o item ou a linha. Se a informação não estiver
nos arquivos, diga "não consta nos arquivos". Ao citar lei, indique artigo e link oficial.
"""

> *» IA: Statement — preservar o emoji.*

> 💡 **Dica:** projeto é como uma pasta com um bilhete colado na capa. O bilhete (as instruções)
> vale para todas as conversas que você abrir lá dentro.

### ✅ Deu certo?

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: em `ChatGPT > Barra lateral > Caso Loja Aurora`, a resposta diz **3 dias
> corridos do recebimento**, citando o item 1 e a versão 2 (vigente desde 01/09/2026).

### 🚑 Se travar

> *» IA: Accordion — um item por linha da tabela; título = Problema, corpo = O que fazer.*

| Problema | O que fazer |
|---|---|
| Não acho "Novo projeto" | Abra a barra lateral pelo ícone no canto superior esquerdo; no celular, crie pela web |
| Criei sem escolher a memória | Abra `Caso Loja Aurora > Configurações do projeto` e veja se dá para mudar; se não, apague e recrie (o projeto ainda está vazio) |
| Arquivo recusado ou limite de upload | Cole o texto da política na caixa de instruções, logo abaixo das instruções do projeto |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL; um desafio por item, com a validação.*

1. Mova uma conversa antiga para o projeto, arrastando-a na barra lateral. Validação: ela aparece
   dentro de `Caso Loja Aurora`.
2. Fora do projeto, pergunte "qual o prazo de desistência da Loja Aurora?". Validação: a resposta
   não sabe — a memória está restrita.
3. Renomeie o projeto para `Caso Loja Aurora — 2026`. Validação: o novo nome aparece na barra
   lateral.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 2 — Pergunte ao documento

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

A diretoria quer saber o que a política promete, em dois minutos. E você precisa ter certeza de que
o ChatGPT não está inventando regra que não existe. (20 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- O projeto `Caso Loja Aurora`, com a política anexada.

### 👐 Mão na massa

> *» IA: Process — passos verbatim; manter os textos a digitar entre aspas triplas.*

1. Em `ChatGPT > Barra lateral > Caso Loja Aurora`, peça:

"""
Liste em tabela (Regra | Prazo | Item) todos os prazos da política de trocas.
"""

2. Confira a tabela com o arquivo aberto no editor.
3. Agora o teste de invenção. Pergunte:

"""
Qual é a multa que a Loja Aurora paga ao cliente por atraso na entrega?
"""

4. Peça o resumo para a diretoria:

"""
Resuma a política em 4 tópicos de uma linha cada, para quem nunca a leu.
"""

> *» IA: Statement — preservar o emoji.*

> ⚠️ **Cuidado:** a pergunta da multa é uma armadilha de propósito. Assistente de IA tende a
> responder *alguma coisa*. O certo aqui é ele admitir que não sabe.

### ✅ Deu certo?

> *» IA: Statement — gabarito verbatim; preservar o emoji.*

> 🏁 Ponto de controle: a tabela tem **três prazos** — desistência 3 dias corridos (item 1), análise
> técnica 45 dias (item 2), resposta a reclamações 5 dias úteis (item 5) — e a pergunta da multa
> recebe **"não consta nos arquivos"**.

### 🚑 Se travar

> *» IA: Accordion — um item por linha.*

| Problema | O que fazer |
|---|---|
| Ele inventou uma multa | Responda: "Mostre o trecho do arquivo que fala disso." Sem trecho, a regra não existe |
| A tabela misturou versões | Peça: "considere só a versão 2, vigente desde 01/09/2026" |
| Respondeu sem usar o arquivo | Cite o nome: "com base em politica-de-trocas-loja-aurora.txt..." |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL; preservar os breadcrumbs.*

1. Pergunte "o que mudou da versão 1 para a 2?". Validação: só o prazo de desistência (7 → 3 dias).
2. Em `Conversa > sua mensagem do passo 4 > ícone de lápis`, troque para "em linguagem de cliente".
   Validação: a resposta muda sem abrir outra conversa.
3. Em `Resposta do passo 1 > Mais ações > Ramificar em novo chat` [conferir rótulo], peça a tabela em
   inglês. Validação: a conversa original fica intacta.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 3 — Confronte com a lei

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

Três dias para desistir de uma compra on-line parece pouco. Será que a política respeita o Código de
Defesa do Consumidor (CDC)? Você vai descobrir — e conferir na fonte oficial, não na palavra do
robô. (20 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- A busca na web do ChatGPT.
- O texto oficial do CDC: `https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm`.

### 👐 Mão na massa

> *» IA: Process — passos verbatim; preservar os breadcrumbs e o link.*

1. No projeto, ative a busca em `ChatGPT > Caixa de mensagem > + > Buscar` [conferir rótulo] — ou
   escreva "pesquise na web" no pedido.
2. Peça:

"""
Compare cada prazo da política com o Código de Defesa do Consumidor (Lei 8.078/1990). Para cada um,
diga se está de acordo, cite o artigo e dê o link do texto no Planalto.
"""

3. Abra `https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm`.
4. Use Ctrl+F (no Mac, Cmd+F) e procure "Art. 49" e depois "Art. 18".
5. Leia: o art. 49 dá **7 dias** para desistir de compra feita fora do estabelecimento; o § 1º do
   art. 18 dá **30 dias** para o fornecedor sanar o vício do produto.

> *» IA: Statement — preservar o emoji.*

> ⚠️ **Cuidado:** link na resposta não é prova. Prova é o trecho que você leu na página oficial.

### ✅ Deu certo?

> *» IA: Statement — gabarito verbatim; preservar o emoji.*

> 🏁 Ponto de controle: no Planalto, dois conflitos confirmados — **item 1** (3 dias × 7 dias do
> art. 49) e **item 2** (45 dias × 30 dias do art. 18, § 1º).

### 🚑 Se travar

> *» IA: Accordion — um item por linha.*

| Problema | O que fazer |
|---|---|
| Resposta sem fonte | Peça: "pesquise na web e cite apenas fontes oficiais com link" |
| Citou o artigo errado | Confira no Planalto e corrija na conversa: "o art. 49 diz...; refaça" |
| Disse que 45 dias está ok | O § 1º do art. 18 fixa 30 dias; peça para ele reler o artigo citado |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL.*

1. Pergunte se "produto em promoção" muda a garantia. Validação: o art. 18 não traz exceção para
   promoção.
2. Peça uma fonte não oficial (o site do Procon de um estado) e compare com o Planalto. Validação:
   as duas dizem a mesma coisa sobre o art. 49.
3. Pergunte o prazo para reclamar de vício aparente em produto durável. Validação: art. 26, II —
   90 dias.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 4 — Faça a planilha falar

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

São 24 linhas de números. A diretoria quer três frases e um gráfico. Bora. (20 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- A análise de dados do ChatGPT (ele faz as contas de verdade, como uma calculadora que lê planilha).
- O arquivo `reclamacoes-loja-aurora.csv`.

### 👐 Mão na massa

> *» IA: Process — passos verbatim; preservar os breadcrumbs.*

1. No projeto, abra uma conversa nova e anexe o CSV em `ChatGPT > Caixa de mensagem > + >
   Adicionar fotos e arquivos`.
2. Primeiro, o teste de leitura:

"""
Mostre as 5 primeiras linhas e os nomes das colunas.
"""

3. Depois, os números:

"""
Calcule: total de reclamações, total resolvido e taxa de resolução. Faça uma tabela por categoria
com reclamações, resolvidas e taxa. Diga qual mês teve mais reclamações.
"""

4. E o gráfico:

"""
Faça um gráfico de linhas de "Troca ou devolucao" por mês e compare maio–agosto com setembro–outubro.
"""

5. Baixe o gráfico pelo ícone de download no canto do gráfico. No Free, ele vem como imagem;
   tabelas e gráficos interativos são dos planos pagos.

> *» IA: Statement — preservar o emoji.*

> 💡 **Dica:** confira um número na mão. 46 + 58 = 104 reclamações de troca em setembro e outubro.

### ✅ Deu certo?

> *» IA: Table — gabarito verbatim.*

| Indicador | Valor certo |
|---|---|
| Total de reclamações | 609 |
| Resolvidas | 501 (82,3%) |
| Troca ou devolução no semestre | 158 reclamações, 102 resolvidas (64,6%) |
| Troca ou devolução: mai–ago × set–out | 54 × 104 |
| Pior mês | Outubro (132), seguido de setembro (122) |

> *» IA: Statement — preservar o emoji.*

> 🏁 Ponto de controle: os cinco valores da tabela batem e o gráfico está salvo na pasta
> `caso-aurora`.

### 🚑 Se travar

> *» IA: Accordion — um item por linha.*

| Problema | O que fazer |
|---|---|
| Limite de upload ou de análise no Free | Cole as 25 linhas do CSV direto na conversa e peça os mesmos cálculos |
| Números diferentes do gabarito | Peça "mostre o cálculo passo a passo" e confira se ele leu as 24 linhas de dados |
| O arquivo virou `.csv.txt` | Renomeie a extensão; ou anexe assim mesmo e avise "é um CSV" |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL.*

1. Peça o prazo médio de troca por mês. Validação: sobe de 4–5 dias para 15 (setembro) e 18
   (outubro).
2. Peça um gráfico de barras empilhadas por categoria. Validação: outubro é a barra mais alta.
3. Pergunte "o que estes dados NÃO permitem concluir?". Validação: ele aponta que coincidência no
   tempo não prova que a política causou o aumento.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Projeto Final — Relatório de uma página

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Projeto Final" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 A missão

> *» IA: Text — verbatim.*

A diretoria da Loja Aurora quer, até amanhã, uma página que responda: qual é o tamanho do problema,
o que está errado na política e o que fazer. Você tem o projeto, o documento, a lei conferida e os
números. Agora é montar — e responder por cada linha. (26 min)

### 👐 Mão na massa

> *» IA: Process — passos verbatim; preservar os breadcrumbs.*

1. Em `ChatGPT > Barra lateral > Caso Loja Aurora`, abra uma conversa nova e peça:

"""
Com base nos arquivos do projeto e nas conclusões das conversas anteriores, escreva um relatório de
no máximo uma página para a diretoria, com 3 seções: (1) Tamanho do problema, com 3 números;
(2) Política × CDC, com os 2 conflitos, artigos e link do Planalto; (3) Três recomendações
práticas. Tom profissional, sem jargão.
"""

2. Se a conversa nova não "lembrar" as anteriores, cole os resultados das Oficinas 3 e 4.
3. Confira cada número com o gabarito da Oficina 4 e cada artigo no Planalto.
4. (Opcional) Peça "abra no canvas e deixe mais curto" para lapidar o texto lado a lado.
5. Copie o relatório para um documento seu e salve como `relatorio-loja-aurora` na pasta
   `caso-aurora`.

### 🏁 Como saber que terminou

> *» IA: Checklist — itens verbatim.*

- [ ] O relatório cabe em uma página.
- [ ] Traz 609 reclamações, 82,3% resolvidas e o salto de troca/devolução (54 → 104).
- [ ] Aponta os dois conflitos: art. 49 (7 dias) e art. 18, § 1º (30 dias), com link do Planalto.
- [ ] Tem três recomendações coerentes com os dados (ex.: voltar ao prazo legal de 7 dias).
- [ ] Você conferiu na mão pelo menos um número e um artigo.
- [ ] Nenhum dado real de pessoa ou de empresa foi usado.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Projeto Final" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# A Parte dos Dez — Atalhos que salvam seu dia no ChatGPT

> *» IA: List — numerada, verbatim.*

1. **Edite em vez de repetir.** O lápis na sua mensagem refaz a resposta sem poluir a conversa.
2. **Ramifique para testar.** Quer outra versão sem perder a atual? Ramifique em novo chat.
3. **Um caso, um projeto.** Memória "apenas do projeto" quando o assunto não pode se misturar.
4. **Instruções do projeto são o seu contrato.** Escreva ali "diga quando não constar nos arquivos".
5. **Peça o trecho.** "De onde você tirou isso?" desmonta invenção em segundos.
6. **Primeiro as 5 linhas.** Antes de analisar planilha, confira se ele leu as colunas certas.
7. **Faça uma conta na mão.** Um número conferido vale mais que dez aceitos.
8. **Lei se confere no Planalto.** Link de resposta não é fonte; trecho lido é.
9. **Chat temporário para o que não deve ficar.** Sem histórico, sem memória nova, sem treino.
10. **Limite acabou?** Cole o texto em vez de anexar; o trabalho continua.

## Conseguiu! E agora?

> *» IA: Text — dois parágrafos verbatim.*

Você acabou de fazer o que muita gente acha que só analista faz: juntou documento, lei e planilha e
entregou uma conclusão que se sustenta. O segredo não foi o ChatGPT — foi você conferir.

Para continuar, repita o roteiro com um caso público da sua área: um relatório de órgão público ou
uma planilha de dados abertos do IBGE ou do `dados.gov.br`. Na trilha, o próximo passo é *Claude
Skills - Essentials*; para aprofundar, *Deep Research - Hands On* e *ChatGPT Excel*.
