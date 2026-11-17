# ChatGPT Chat Para Leigos — Curso Hands-on (roteiro final)

*Em menos de duas horas, você vai resolver um caso de verdade com o ChatGPT: do documento e da
planilha a um relatório de uma página, com números conferidos e lei citada na fonte.*

**Público-Alvo:** quem já fez *ChatGPT Chat - Essentials* (T1, posição 5 de 6; também serve às
trilhas de fundamentos jurídico e das demais áreas).

**Objetivo Geral:** resolver um caso completo combinando projetos, arquivos, busca na web e análise
de dados no ChatGPT, entregando um relatório de uma página verificável.

**Pré-requisitos:** conta ChatGPT gratuita; computador com navegador e internet; editor de texto
simples (Bloco de Notas no Windows, TextEdit no Mac em modo texto simples).

## Estrutura do Curso

| Parte | Conteúdo | Tempo |
|---|---|---|
| Preparação | Antes de Arregaçar as Mangas (controles de dados e materiais) | 7 min |
| Nível 1 — Montar e consultar | Oficina 1 — Projeto do caso; Oficina 2 — Pergunte ao documento | 40 min |
| Nível 2 — Confrontar e calcular | Oficina 3 — Confronte com a lei; Oficina 4 — Faça a planilha falar | 40 min |
| Integração | Projeto Final — Relatório de uma página | 26 min |
| Anexo | A Parte dos Dez | 6 min |
| **Total** | | **119 min** |

**O caso (fictício):** a Loja Aurora vende eletrodomésticos pela internet. Desde setembro de 2026,
as reclamações de "troca ou devolução" explodiram. A diretoria quer saber o tamanho do problema, se
a política de trocas tem algo errado e o que fazer.

---

## Antes de Arregaçar as Mangas

Aqui não tem palestra: você vai fazer. Cada oficina resolve um pedaço do caso, e no fim as peças
viram um relatório.

**O que você precisa ter aberto agora:**

- `chatgpt.com` com sua conta (plano Free serve).
- Um editor de texto simples.
- Uma pasta no computador chamada `caso-aurora`.

### Passo 1 — Confira seus controles de dados (2 min)

- **📸 Sugestão de Prints:** `Configurações > Controles de dados` com a chave "Melhorar o modelo
  para todos" destacada.

Abra `Perfil (canto inferior esquerdo) > Configurações > Controles de dados` e decida se mantém
"Melhorar o modelo para todos". Neste curso tudo é fictício, então qualquer escolha é segura. No
seu trabalho, a regra é o semáforo do Essentials: dado pessoal de terceiro, segredo comercial e
documento de cliente não vão para conta pessoal.

### Passo 2 — Salve os dois arquivos do caso (5 min)

1. Copie o bloco abaixo, cole no editor e salve como `reclamacoes-loja-aurora.csv` (no Bloco de
   Notas, escolha "Todos os arquivos" no tipo, para não virar `.csv.txt`):

```
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
```

2. Copie o texto abaixo e salve como `politica-de-trocas-loja-aurora.txt`:

```
POLÍTICA DE TROCAS E DEVOLUÇÕES — LOJA AURORA
(Documento fictício, criado para fins didáticos)
Versão 2 — vigente desde 01/09/2026. A versão 1, válida até 31/08/2026, previa 7 dias para desistência.

1. Desistência de compras feitas pelo site: o cliente pode desistir em até 3 (três) dias corridos, contados do recebimento do produto.
2. Produto com defeito: a troca depende de análise técnica, concluída em até 45 (quarenta e cinco) dias.
3. Produtos em promoção têm as mesmas garantias dos demais.
4. Atendimento: e-mail e chat, de segunda a sexta, das 9h às 18h.
5. Prazo de resposta a reclamações: até 5 (cinco) dias úteis.
```

> 🔑 **Regra de ouro:** o ChatGPT é seu estagiário rápido, não seu chefe. Ele faz o rascunho; você
> confere os números e a lei antes de assinar.

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1 | Tirar o caso das conversas soltas e montar um projeto | 20 min |
| 2 | Descobrir o que a política diz, sem ler tudo e sem cair em invenção | 20 min |
| 3 | Saber se a política está de acordo com a lei | 20 min |
| 4 | Transformar a planilha em números e gráfico | 20 min |
| Projeto Final | Entregar o relatório de uma página para a diretoria | 26 min |

As oficinas são em sequência: cada uma usa o que a anterior deixou pronto.

---

## Oficina 1 — Monte o projeto do caso

### 🎯 O Problema

Você abriu três conversas sobre a Loja Aurora e já não sabe qual tinha o quê. Vamos criar uma
pasta inteligente onde tudo do caso mora junto e segue as mesmas regras.

### 🧰 O que você vai usar

- Projetos do ChatGPT; o arquivo `politica-de-trocas-loja-aurora.txt`.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** (a) barra lateral com "Novo projeto" destacado; (b) janela de criação
  com o nome "Caso Loja Aurora" e o menu de memória aberto em "Apenas do projeto"; (c) página do
  projeto com instruções salvas e o arquivo listado.

1. Na barra lateral, clique em **Novo projeto**.
2. Digite o nome: `Caso Loja Aurora`.
3. Abra as configurações do projeto (ícone de engrenagem na janela de criação) e escolha a memória
   **Apenas do projeto**. Clique em **Criar projeto**.
4. Na página do projeto, abra **Instruções** e cole:

> Você apoia a análise de reclamações da Loja Aurora (caso fictício). Responda em português do
> Brasil, de forma objetiva. Ao usar um arquivo, cite o item ou a linha. Se a informação não
> estiver nos arquivos, diga "não consta nos arquivos". Ao citar lei, indique artigo e link oficial.

5. Salve. Em **Arquivos**, adicione `politica-de-trocas-loja-aurora.txt`.
6. Dentro do projeto, comece uma conversa: "Qual é o prazo de desistência para compras no site?"

### ✅ Deu certo?

Resposta: **3 dias corridos do recebimento**, citando o item 1 e a versão 2 (vigente desde
01/09/2026).

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não acho "Novo projeto" | Abra a barra lateral (ícone no canto superior esquerdo); no celular, use a web para criar |
| Já criei sem escolher a memória | Abra as configurações do projeto e confira se a opção pode ser mudada; se não, apague e recrie (projeto ainda vazio) |
| Arquivo recusado ou limite de upload | Cole o texto da política na caixa de instruções do projeto, logo abaixo das instruções |

### 🚀 Quer ir além?

1. Mova uma conversa antiga para o projeto (arrastar para o projeto na barra lateral) — valida se
   ela aparece dentro dele.
2. Pergunte fora do projeto "qual o prazo de desistência da Loja Aurora?" — valida a memória
   restrita: a resposta não deve saber.
3. Renomeie o projeto para `Caso Loja Aurora — 2026` — valida na barra lateral.

## Descrição

- **Objetivos da Aula:** criar projeto, configurar memória restrita, instruções e arquivos.
- **Habilidades Esperadas:** montar sozinho um projeto de trabalho com regras de resposta e
  documentos de referência.

---

## Oficina 2 — Pergunte ao documento

### 🎯 O Problema

A diretoria quer saber o que a política promete, em dois minutos. E você precisa ter certeza de
que o ChatGPT não está inventando regra que não existe.

### 🧰 O que você vai usar

- O projeto da Oficina 1.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** resposta em tabela com as colunas Regra, Prazo e Item, dentro do
  projeto.

1. No projeto, peça:

> Liste em tabela (Regra | Prazo | Item) todos os prazos da política de trocas.

2. Confira a tabela com o arquivo aberto no editor.
3. Agora o teste de invenção. Pergunte:

> Qual é a multa que a Loja Aurora paga ao cliente por atraso na entrega?

4. Peça o resumo para a diretoria:

> Resuma a política em 4 tópicos de uma linha cada, para quem nunca a leu.

### ✅ Deu certo?

A tabela tem **três prazos**: desistência 3 dias corridos (item 1), análise técnica 45 dias (item
2), resposta a reclamações 5 dias úteis (item 5). A pergunta da multa recebe **"não consta nos
arquivos"** — a política não fala de multa.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Ele inventou uma multa | Responda: "Mostre o trecho do arquivo que fala disso." Sem trecho, não existe |
| A tabela misturou versões | Peça "considere só a versão 2, vigente desde 01/09/2026" |
| Respondeu sem usar o arquivo | Cite o nome: "com base em politica-de-trocas-loja-aurora.txt..." |

### 🚀 Quer ir além?

1. Peça "o que mudou da versão 1 para a 2?" — valida: só o prazo de desistência (7 → 3 dias).
2. Edite sua mensagem do passo 4 para "em linguagem de cliente" — valida que a resposta muda sem
   abrir outra conversa.
3. Use "Ramificar em novo chat" na resposta do passo 1 e peça a tabela em inglês — valida que a
   conversa original fica intacta.

## Descrição

- **Objetivos da Aula:** extrair informação de documento com rastreabilidade e testar invenção.
- **Habilidades Esperadas:** interrogar um documento, exigir o trecho de origem e reconhecer
  sozinho uma resposta não sustentada pelo arquivo.

---

## Oficina 3 — Confronte com a lei

### 🎯 O Problema

Três dias para desistir de uma compra on-line parece pouco. Será que a política respeita o Código
de Defesa do Consumidor? Você vai descobrir — e conferir na fonte oficial, não na palavra do robô.

### 🧰 O que você vai usar

- Busca na web; o texto do CDC no Planalto.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** resposta com busca mostrando citações de `planalto.gov.br` e o painel
  de fontes aberto; segundo print da página do Planalto com o art. 49 visível.

1. No projeto, ative a busca: `+ > Buscar` [conferir rótulo] — ou escreva "pesquise na web".
2. Peça:

> Compare cada prazo da política com o Código de Defesa do Consumidor (Lei 8.078/1990). Para
> cada um, diga se está de acordo, cite o artigo e dê o link do texto no Planalto.

3. Abra `https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm`.
4. Use Ctrl+F (no Mac, Cmd+F) e procure "Art. 49" e depois "Art. 18".
5. Leia: o art. 49 dá **7 dias** para desistir de compra feita fora do estabelecimento; o § 1º do
   art. 18 dá **30 dias** para o fornecedor sanar o vício.

> ⚠️ **Cuidado:** link na resposta não é prova. Prova é o trecho que você leu na página oficial.

### ✅ Deu certo?

Dois conflitos confirmados no Planalto: **item 1** (3 dias × 7 dias do art. 49) e **item 2** (45
dias × 30 dias do art. 18, § 1º).

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Resposta sem fonte | Peça "pesquise na web e cite apenas fontes oficiais com link" |
| Citou artigo errado | Confira no Planalto; corrija na conversa: "o art. 49 diz...; refaça" |
| Ele disse que 45 dias está ok | O § 1º do art. 18 fixa 30 dias; peça para reler o artigo citado |

### 🚀 Quer ir além?

1. Pergunte se "produto em promoção" muda a garantia — valida com o art. 18 (não há exceção).
2. Peça uma fonte não oficial (Procon de um estado) e compare com o Planalto — valida se dizem o mesmo.
3. Pergunte o prazo para reclamar de vício em produto durável — valida no art. 26, II (90 dias).

## Descrição

- **Objetivos da Aula:** usar a busca para confrontar um documento com a norma e conferir na fonte
  oficial.
- **Habilidades Esperadas:** pedir comparação com citação, abrir a fonte oficial e confirmar ou
  derrubar sozinho cada afirmação.

---

## Oficina 4 — Faça a planilha falar

### 🎯 O Problema

São 24 linhas de números. A diretoria quer três frases e um gráfico. Bora.

### 🧰 O que você vai usar

- Análise de dados do ChatGPT; o arquivo `reclamacoes-loja-aurora.csv`.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** resposta com a tabela por categoria e o gráfico de linhas, com o
  botão de download do gráfico destacado.

1. No projeto, numa conversa nova, anexe o CSV: `+ > Adicionar fotos e arquivos`.
2. Primeiro, o teste de leitura:

> Mostre as 5 primeiras linhas e os nomes das colunas.

3. Depois:

> Calcule: total de reclamações, total resolvido e taxa de resolução. Faça uma tabela por
> categoria com reclamações, resolvidas e taxa. Diga qual mês teve mais reclamações.

4. E o gráfico:

> Faça um gráfico de linhas de "Troca ou devolucao" por mês e compare mai–ago com set–out.

5. Baixe o gráfico pelo ícone de download (no Free, o gráfico vem como imagem; tabelas e gráficos
   interativos são dos planos pagos).

> 💡 **Dica:** confira um número na mão. 46 + 58 = 104 reclamações de troca em setembro e outubro.

### ✅ Deu certo?

| Indicador | Valor certo |
|---|---|
| Total de reclamações | 609 |
| Resolvidas | 501 (82,3%) |
| Troca ou devolução (semestre) | 158 reclamações, 102 resolvidas (64,6%) |
| Troca ou devolução mai–ago × set–out | 54 × 104 |
| Pior mês | Outubro (132), seguido de setembro (122) |

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Limite de upload ou de análise no Free | Cole as 25 linhas do CSV direto na conversa e peça os mesmos cálculos |
| Números diferentes do gabarito | Peça "mostre o cálculo passo a passo"; confira se ele leu as 24 linhas |
| Arquivo virou `.csv.txt` | Renomeie a extensão; ou anexe assim mesmo e diga "é um CSV" |

### 🚀 Quer ir além?

1. Peça o prazo médio de troca por mês — valida: sobe de 4–5 dias para 15 e 18.
2. Peça um gráfico de barras empilhadas por categoria — valida que outubro é a barra mais alta.
3. Pergunte "o que estes dados NÃO permitem concluir?" — valida se ele aponta que correlação com a
   política não prova causa.

## Descrição

- **Objetivos da Aula:** analisar uma planilha com cálculo, tabela e gráfico, conferindo a leitura.
- **Habilidades Esperadas:** enviar uma planilha, validar a leitura, obter indicadores e gráfico e
  conferir sozinho pelo menos um número.

---

## Projeto Final — Relatório de uma página

### 🎯 A missão

A diretoria da Loja Aurora quer, até amanhã, uma página que responda: qual é o tamanho do
problema, o que está errado na política e o que fazer. Você tem o projeto, o documento, a lei
conferida e os números. Agora é montar — e responder por cada linha.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** relatório final aberto no Canvas (opcional) com as três seções
  visíveis.

1. No projeto, numa conversa nova, peça:

> Com base nos arquivos do projeto e nas conclusões das conversas anteriores, escreva um relatório
> de no máximo uma página para a diretoria, com 3 seções: (1) Tamanho do problema, com 3 números;
> (2) Política × CDC, com os 2 conflitos, artigos e link do Planalto; (3) Três recomendações
> práticas. Tom profissional, sem jargão.

2. Se a conversa nova não "lembrar" as anteriores, cole os resultados das Oficinas 3 e 4.
3. Confira cada número com a tabela da Oficina 4 e cada artigo com o Planalto.
4. Peça um ajuste de forma (opcional, no Canvas: "abra no canvas e deixe mais curto").
5. Copie o relatório para um documento seu e salve como `relatorio-loja-aurora`.

### 🏁 Como saber que terminou

- [ ] O relatório cabe em uma página.
- [ ] Traz 609 reclamações, 82,3% resolvidas e o salto de troca/devolução (54 → 104).
- [ ] Aponta os dois conflitos: art. 49 (7 dias) e art. 18, § 1º (30 dias), com link do Planalto.
- [ ] Tem três recomendações coerentes com os dados (ex.: voltar ao prazo legal de 7 dias).
- [ ] Você conferiu na mão pelo menos um número e um artigo.
- [ ] Nenhum dado real de pessoa ou de empresa foi usado.

## Descrição

- **Objetivos da Aula:** integrar projeto, documento, busca e análise de dados num entregável.
- **Habilidades Esperadas:** conduzir sozinho um caso completo no ChatGPT e responder por cada
  número e citação do resultado.

---

## A Parte dos Dez — Atalhos que salvam seu dia no ChatGPT

1. **Edite em vez de repetir.** O lápis na sua mensagem refaz a resposta sem poluir a conversa.
2. **Ramifique para testar.** Quer outra versão sem perder a atual? Ramifique em novo chat.
3. **Projeto por assunto.** Um caso, um projeto; memória "apenas do projeto" quando não pode misturar.
4. **Instruções do projeto são o seu contrato.** Escreva ali "diga quando não constar nos arquivos".
5. **Peça o trecho.** "De onde você tirou isso?" desmonta invenção em segundos.
6. **Primeiro as 5 linhas.** Antes de analisar planilha, confira se ele leu as colunas certas.
7. **Faça uma conta na mão.** Um número conferido vale mais que dez aceitos.
8. **Lei se confere no Planalto.** Link de resposta não é fonte; trecho lido é.
9. **Chat temporário para o que não deve ficar.** Sem histórico, sem memória, sem treino.
10. **Limite acabou?** Cole o texto em vez de anexar; o trabalho continua.

## Conseguiu! E agora?

Você acabou de fazer o que muita gente acha que só analista faz: juntou documento, lei e planilha
e entregou uma conclusão que se sustenta. O segredo não foi o ChatGPT — foi você conferir.

Para continuar: repita o roteiro com um caso público da sua área (um relatório de órgão público, uma
planilha de dados abertos do IBGE ou do `dados.gov.br`). Depois, siga para *Claude Skills -
Essentials* na trilha, ou aprofunde com *Deep Research - Hands On* e *ChatGPT Excel*.

---

## Rastreabilidade da auditoria

| Achado | Destino |
|---|---|
| H1 | Caso Loja Aurora com materiais embutidos (Preparação) |
| H2 | Gabaritos numéricos e legais em todos os "Deu certo?" |
| H3 | Passo 1 da preparação (controles de dados e semáforo) |
| H4 | Dois uploads no curso inteiro; rota "colar o texto" nas Oficinas 1 e 4; aviso de gráfico estático |
| H5 | Caminhos em todas as oficinas (breadcrumbs na versão Articulate) |
| H6 | Oficina 3 confronta política × CDC no Planalto |
| H7 | Projeto Final com três seções e checklist de seis itens |
| H8 | Se travar com tropeços reais por oficina |
| H9 | Três desafios com validação por oficina |
| H10 | Parte dos Dez específica do ChatGPT |
