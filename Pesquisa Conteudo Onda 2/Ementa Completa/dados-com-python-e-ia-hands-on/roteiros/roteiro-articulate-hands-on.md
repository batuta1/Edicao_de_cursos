# Dados com Python e IA Para Leigos — Curso Hands-on

> *» IA: Cover — título e subtítulo; preservar verbatim; não traduzir "Claude Code", "Codex", "Python" nem nomes de comandos.*

*Em menos de duas horas, você vai pôr um agente de IA para escrever Python sobre dados reais da
inflação, da bolsa e do clima — e vai terminar com projetos que rodam de novo do zero e se recusam a
entregar número errado.*

# Antes de Arregaçar as Mangas

> *» IA: Text — parágrafo verbatim.*

Você vai mandar um agente de IA escrever Python — e vai conferir tudo o que ele fizer. São três
bases públicas, quatro armadilhas reais e um projeto que outra pessoa consegue rodar com um comando.
Duração: 105 minutos, sem contar a espera do agente instalando e executando.

> *» IA: Checklist — itens verbatim.*

**O que você precisa ter aberto agora:**

- O agente da sua rota: `Claude (app de desktop) > Code` (plano Pro ou superior) ou `ChatGPT (app de
  desktop) > menu de modos > Codex`.
- O terminal, só para conferir o uv (`uv --version`).
- Uma pasta chamada `projeto-dados`, com a subpasta `dados/brutos`.

> *» IA: Process — preparação em dois passos; preservar os breadcrumbs, os endereços e os comandos.*

**Preparação (7 min)**

1. Baixe para `projeto-dados/dados/brutos`, **sem extrair os ZIPs** (o agente lê direto deles):
   `ipca.csv`, `dfp_cia_aberta_2024.zip`, `cad_cia_aberta.csv` e `inmet-2024.zip` (endereços na
   tabela abaixo). O do INMET tem 103 MB: comece por ele.
2. Abra o agente na pasta `projeto-dados` em modo seguro: no Claude Code, modo Manual ou `plan`; no
   Codex, `Work in > This computer` e `/permissions` em somente leitura.

> *» IA: Table — verbatim; preservar os endereços.*

| Arquivo | Endereço | Tamanho |
|---|---|---|
| `ipca.csv` | `api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2020&dataFinal=31/12/2025` | 1,5 KB |
| `dfp_cia_aberta_2024.zip` | `dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2024.zip` | 13,4 MB |
| `cad_cia_aberta.csv` | `dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv` | 1,5 MB |
| `inmet-2024.zip` | `portal.inmet.gov.br/uploads/dadoshistoricos/2024.zip` | 102,8 MB |

> *» IA: Statement — preservar o emoji.*

> 🔑 **Regra de ouro:** o agente faz; você aprova, lê e confere. Dado bruto ninguém toca.

# O Mapa da Mão na Massa

> *» IA: Table — verbatim.*

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1 | Transformar o cálculo da inflação num projeto que roda de novo | 16 min |
| 2 | Fazer o ranking de lucro da bolsa sem cair na escala | 22 min |
| 3 | Descobrir qual setor lucrou mais, cruzando duas tabelas | 22 min |
| 4 | Pegar um erro silencioso com uma segunda opinião | 16 min |
| Projeto Final | Analisar o clima do Distrito Federal em 2024 a partir de cinco arquivos | 22 min |

> *» IA: Text — frase verbatim.*

As oficinas vão em sequência; cada uma deixa um script com testes que passam.

---

# Oficina 1 — Seu primeiro projeto reprodutível

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

Todo mês alguém refaz à mão o acumulado do IPCA numa planilha. Vamos deixar isso num script que
qualquer pessoa roda com um comando — e que se recusa a terminar se o número estiver errado. (16 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- `dados/brutos/ipca.csv` (ponto e vírgula, vírgula decimal).
- O agente em modo de planejamento e o uv.

### 👐 Mão na massa

> *» IA: Process — um passo por etapa; textos a digitar verbatim; não traduzir comandos nem nomes de arquivos.*

1. No Claude Code, digite `/init`; depois peça para incluir no `CLAUDE.md` (no Codex, crie
   `AGENTS.md` com o mesmo texto): "Dados em dados/brutos nunca são alterados. CSVs do Banco Central
   usam ponto e vírgula e vírgula decimal. Saídas vão para resultados/. Rodar com uv run."
2. Envie o brief do bloco abaixo.
3. Leia o plano. Para aprovar, mude para `acceptEdits` (Claude Code, `Shift+Tab` no terminal) ou
   aprove cada comando (Codex).
4. Quando o agente pedir para instalar `pandas` e `matplotlib`, aprove.
5. Apague a pasta `resultados/` e digite: "Rode do zero com uv run e mostre a saída completa."
6. Digite: "Explique analise_ipca.py em blocos de até cinco linhas."

> *» IA: Statement — brief verbatim, entre aspas triplas.*

"""
Crie analise_ipca.py que calcula o IPCA acumulado de cada ano de 2020 a 2025 por composição, salva a
tabela em resultados/ipca_anual.csv e um gráfico de barras em resultados/ipca_anual.png. Inclua
asserts: 72 linhas lidas; 2024 = 4,83 e 2025 = 4,26, com tolerância de 0,01. Use uv para as
bibliotecas. Mostre o plano e espere minha aprovação.
"""

> *» IA: Statement — preservar o emoji.*

> 💡 **Dica:** assert é um alarme. Se o número sair diferente do esperado, o script para e grita em
> vez de entregar um relatório errado com cara de certo.

### ✅ Deu certo?

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: no terminal do agente, a saída mostra **4,83** (2024) e **4,26** (2025), os
> asserts passam, e `projeto-dados` tem `uv.lock` e a pasta `resultados/`.

### 🚑 Se travar

> *» IA: Accordion — um item por linha da tabela; título = Problema, corpo = O que fazer.*

| Problema | O que fazer |
|---|---|
| O agente quer instalar um pacote de nome estranho | Recuse e procure o nome em pypi.org antes |
| `uv` não encontrado | Feche e reabra o terminal; se persistir, reinstale pelo comando oficial |
| Um assert de ano antigo falha por 0,01 | Esperado: as taxas mensais vêm arredondadas; registre como limitação e use tolerância |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL; um desafio por item, com a validação.*

1. Peça `git init` e um commit "oficina 1". Validação: `git log` mostra o commit.
2. Peça um notebook `.ipynb` equivalente. Validação: abre e reproduz 4,83%.
3. Peça que o script receba o ano como parâmetro. Validação: `uv run analise_ipca.py 2024` imprime
   4,83.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 2 — O ranking que mentia, agora em código

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

A diretoria quer o top 5 de lucro das companhias abertas de 2024, direto da CVM — e quer refazer no
ano que vem trocando um arquivo só. (22 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- `dados/brutos/dfp_cia_aberta_2024.zip` (19 arquivos CSV em latin-1).

### 👐 Mão na massa

> *» IA: Process — um passo por etapa; textos a digitar verbatim; não traduzir nomes de colunas.*

1. Digite: "Crie ranking_lucro.py que lê dfp_cia_aberta_DRE_con_2024.csv direto do ZIP (latin-1,
   ponto e vírgula), filtra ORDEM_EXERC = ÚLTIMO e CD_CONTA = 3.11.01 e imprime quantas linhas e
   quantas empresas. Mostre o plano."
2. Aprove e rode. Anote: 460 linhas, 458 empresas.
3. Digite: "Mostre as linhas duplicadas e a contagem de ESCALA_MOEDA."
4. Digite: "Remova duplicatas, converta para reais (MIL vezes 1.000; UNIDADE vezes 1), salve o top
   20 em resultados/ e adicione asserts: 458 empresas; Petrobras = 36.606.000.000; ESCALA_MOEDA só
   com MIL e UNIDADE."
5. Apague `resultados/` e rode do zero.

> *» IA: Statement — preservar o emoji.*

> 💡 **Dica:** sem converter a escala, a Vivara (R$ 653 milhões, informados em reais) vira a "maior
> lucradora do país". O código roda — a premissa é que estava errada.

### ✅ Deu certo?

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: na saída, 452 empresas em MIL e 8 em UNIDADE; top 5 — Petrobras R$ 36,6 bi,
> Vale R$ 31,6 bi, Banco do Brasil R$ 26,4 bi, Bradesco R$ 17,3 bi, Itaúsa R$ 14,8 bi; asserts
> passando.

### 🚑 Se travar

> *» IA: Accordion — um item por linha da tabela; título = Problema, corpo = O que fazer.*

| Problema | O que fazer |
|---|---|
| `UnicodeDecodeError` | Digite: "Leia com encoding latin-1" |
| O agente quer extrair o ZIP em `dados/brutos` | Peça para ler direto do ZIP ou extrair em `dados/tratados/` |
| Valores enormes no topo | Confira ESCALA_MOEDA antes de qualquer outra hipótese |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL; um desafio por item, com a validação.*

1. Conte as empresas com prejuízo. Validação: 95.
2. Some o lucro das 458. Validação: ≈ R$ 303,9 bi.
3. Exporte o top 20 para Excel com openpyxl. Validação: o `.xlsx` abre com 20 linhas.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 3 — Cruze duas tabelas sem inflar a soma

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

Agora a pergunta é por setor — e o setor está no cadastro da CVM, não na demonstração de resultado.
Juntar duas tabelas é onde mais se erra em silêncio. (22 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- O script da Oficina 2.
- `dados/brutos/cad_cia_aberta.csv` (latin-1).

### 👐 Mão na massa

> *» IA: Process — um passo por etapa; textos a digitar verbatim; não traduzir nomes de colunas.*

1. Digite: "Leia cad_cia_aberta.csv (latin-1). Quantas linhas e quantos CD_CVM únicos? Quantos
   códigos aparecem mais de uma vez?"
2. Anote: 2.680 linhas, 2.569 códigos, 107 repetidos.
3. Digite: "Antes de juntar, deixe uma linha por CD_CVM, preferindo SIT = ATIVO. Junte com o lucro da
   Oficina 2 e informe quantas empresas ficaram sem cadastro."
4. Digite: "Some o lucro por SETOR_ATIV, salve em resultados/ e adicione asserts: linhas depois da
   junção = 458; soma dos setores mais as sem cadastro = soma total da Oficina 2."
5. Rode do zero.

> *» IA: Statement — preservar o emoji.*

> ⚠️ **Cuidado:** juntar pela chave repetida duplica empresas e infla a soma sem nenhum aviso. O
> assert "linhas antes = linhas depois" é sua defesa.

### ✅ Deu certo?

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: 4 empresas sem cadastro; setores no topo — Bancos R$ 60,9 bi, Petróleo e Gás
> R$ 50,9 bi, Energia Elétrica R$ 36,5 bi, Extração Mineral R$ 31,4 bi; asserts passando.

### 🚑 Se travar

> *» IA: Accordion — um item por linha da tabela; título = Problema, corpo = O que fazer.*

| Problema | O que fazer |
|---|---|
| Soma por setor maior que a soma total | Junção com chave repetida: volte ao passo 3 |
| "Comércio" aparece com R$ 667 bi | A escala não foi convertida antes da junção |
| Setor vazio | Mostre essas empresas e decida mantê-las como "sem setor" |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL; um desafio por item, com a validação.*

1. Liste as 4 empresas sem cadastro. Validação: quatro nomes.
2. Conte empresas por setor. Validação: a soma bate com as empresas casadas.
3. Faça um gráfico de barras dos 10 setores. Validação: eixo em zero e fonte CVM no rodapé.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 4 — Peça uma segunda opinião

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

Você vai pedir uma tabela "simples" que costuma sair errada sem ninguém notar — e depois colocar um
revisor que não viu a conversa para auditar o projeto. (16 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- Os scripts das Oficinas 2 e 3.

### 👐 Mão na massa

> *» IA: Process — um passo por etapa; textos a digitar verbatim; não traduzir comandos.*

1. Digite: "Faça uma tabela com o top 5 de receita (conta 3.01) e o top 5 de lucro lado a lado."
2. Leia com atenção: as linhas pareiam a mesma empresa ou só a posição? Se a 2ª linha mostra a JBS
   (receita) ao lado do lucro da Vale, o pareamento está errado.
3. Digite: "Refaça juntando por CD_CVM, uma linha por empresa com as duas colunas, e adicione um
   assert que confira um só CD_CVM por linha."
4. Revisão independente: no Claude Code, digite `/code-review`; no Codex, abra uma sessão nova e
   envie o pedido de auditor do bloco abaixo.
5. Registre no `README.md` o que a revisão apontou e o que você fez.

> *» IA: Statement — pedido de auditor verbatim, entre aspas triplas.*

"""
Revise ranking_lucro.py e setores.py como um auditor que não confia no autor. Liste cinco formas de
o número final estar errado e escreva um teste para cada uma. Rode e mostre a saída completa.
"""

> *» IA: Statement — preservar o emoji.*

> 🤓 **Curiosidade técnica (pode pular):** o `/code-review` do Claude Code roda a revisão num
> subagente que nunca viu a conversa — por isso não herda as mesmas premissas de quem escreveu.

### ✅ Deu certo?

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: na tabela final, a Petrobras aparece numa só linha com receita R$ 490,8 bi e
> lucro R$ 36,6 bi; a revisão gerou ao menos um teste novo, registrado no `README.md`.

### 🚑 Se travar

> *» IA: Accordion — um item por linha da tabela; título = Problema, corpo = O que fazer.*

| Problema | O que fazer |
|---|---|
| `/code-review` não aparece | Use uma sessão nova com o pedido de auditor |
| O revisor só elogia | Peça "aponte obrigatoriamente cinco riscos" |
| O teste novo falha | Ótimo: investigue antes de "consertar" o teste |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL; um desafio por item, com a validação.*

1. Peça a mesma revisão à outra ferramenta (Codex ou Claude Code). Validação: compare as duas listas.
2. Faça um commit "oficina 4". Validação: `git log` com quatro commits.
3. Peça `resultados/relatorio.md` com tabelas e limitações. Validação: cita a escala e as duplicatas.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Projeto Final — O clima do Distrito Federal em 2024

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Projeto Final" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 A missão

> *» IA: Text — verbatim.*

Uma equipe técnica precisa da temperatura média e da máxima de 2024 nas estações automáticas do
Distrito Federal, num projeto que outra pessoa consiga rodar. São cinco arquivos dentro de um ZIP de
565, cada um com oito linhas de informação antes da tabela. Agora é com você. (22 min)

### 👐 Mão na massa

> *» IA: Process — passos verbatim; textos a digitar verbatim; não traduzir nomes de colunas.*

1. Atualize o arquivo de instruções: "INMET: latin-1; ponto e vírgula; vírgula decimal; 8 linhas de
   metadados antes do cabeçalho; hora em UTC; há valores vazios."
2. Envie o brief do bloco abaixo e aprove o plano.
3. Peça asserts: 5 estações; 8.784 linhas por estação (2024 é bissexto: 366 × 24).
4. Rode do zero e peça a explicação por blocos.
5. Peça o `README.md` com como rodar, verificação e limitações (vazios não entram na média; média de
   estações não é a média oficial do país).
6. Rode a revisão independente da Oficina 4.

> *» IA: Statement — brief verbatim, entre aspas triplas.*

"""
Crie clima_df.py que lê, direto de dados/brutos/inmet-2024.zip, os arquivos com _DF_ no nome. Para
cada estação: conte as linhas e os vazios da coluna de temperatura do ar (bulbo seco), calcule a
média anual dessa coluna e a máxima da coluna de temperatura máxima na hora anterior. Salve a
tabela e um gráfico de barras das médias em resultados/. Mostre o plano e espere.
"""

### 🏁 Como saber que terminou

> *» IA: Checklist — itens verbatim.*

- [ ] 5 estações: A001 Brasília, A042 Brazlândia, A045 Águas Emendadas, A046 Gama, A047 Paranoá.
- [ ] 8.784 linhas em cada uma, garantidas por assert.
- [ ] Vazios na temperatura: 26, 235, 453, 66 e 416, na mesma ordem.
- [ ] Médias anuais ≈ 21,98 / 22,32 / 21,85 / 22,60 / 22,29 °C.
- [ ] Maior máxima horária: Gama, 37,5 °C.
- [ ] `uv run clima_df.py` reproduz tudo do zero; `dados/brutos` intocado; README com limitações.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Projeto Final" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# A Parte dos Dez — Hábitos de quem analisa com agente

> *» IA: List — numerada, verbatim.*

1. Plano antes de execução, sempre.
2. Dado bruto não se edita.
3. Declare encoding, separador e decimal no arquivo de instruções.
4. Pacote desconhecido: confira no pypi.org antes de aprovar.
5. Um assert para cada número que vai para o relatório.
6. Conte linhas antes e depois de cada filtro e junção.
7. Escala e duplicata antes de qualquer ranking.
8. Rode do zero antes de entregar.
9. Segunda opinião de quem não viu a conversa.
10. README com como rodar e limitações.

## Conseguiu! E agora?

> *» IA: Text — verbatim.*

Você montou quatro scripts que se defendem sozinhos e um projeto que outra pessoa roda com um
comando. Na próxima análise do trabalho, comece pelo brief e pelos asserts — e mantenha dados
pessoais fora de conta pessoal.

Para ir além: *Claude Code no VSCode* e *ChatGPT CODEX* aprofundam as ferramentas; na trilha TE3,
*IA em projetos de engenharia* aplica o método a cálculos e memoriais.
