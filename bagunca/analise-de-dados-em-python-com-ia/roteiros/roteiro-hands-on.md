# Dados com Python e IA Para Leigos — Curso Hands-on (roteiro final)

**Público-Alvo:** quem concluiu *Dados com Python e IA - Essentials* — analistas, finanças, setor
público e regulação, engenharia.

**Objetivo Geral:** conduzir, com um agente de código, análises reprodutíveis em Python sobre bases
públicas reais (Banco Central, CVM, INMET), validando cada resultado com asserts, contagens, revisão
independente e número oficial.

**Pré-requisitos:** Essentials deste assunto; rota A (Claude Code no app Claude Desktop, plano Pro ou
superior) ou rota B (Codex no app de desktop do ChatGPT; Plus para uso pleno); uv instalado;
cerca de 120 MB livres para as bases.

## Estrutura do Curso

| Parte | Conteúdo | Tempo |
|---|---|---|
| Preparação | Antes de Arregaçar as Mangas | 7 min |
| Nível 1 — Projeto e leitura | Oficina 1 (IPCA) · Oficina 2 (CVM) | 38 min |
| Nível 2 — Cruzar e revisar | Oficina 3 (CVM × cadastro) · Oficina 4 (revisão e erro silencioso) | 38 min |
| Entrega | Projeto Final (INMET) | 22 min |
| Anexos | A Parte dos Dez · Conseguiu! E agora? | — |
| **Total** | | **105 min** (sem contar a espera do agente) |

---

## Antes de Arregaçar as Mangas

Você vai mandar um agente de IA escrever Python — e vai conferir tudo o que ele fizer. Três bases
públicas, quatro armadilhas, um projeto que roda de novo do zero.

> 🔑 Regra de ouro: o agente faz; você aprova, lê e confere. Dado bruto ninguém toca.

### Passo 1 — Pasta e bases (5 min)

- **📸 Sugestão de Prints:** pasta `projeto-dados/dados/brutos` com `ipca.csv`,
  `dfp_cia_aberta_2024.zip`, `cad_cia_aberta.csv` e `inmet-2024.zip`.

Crie `projeto-dados/dados/brutos` e baixe para lá (sem extrair os ZIPs — o agente lê direto deles):

| Arquivo | Endereço | Tamanho |
|---|---|---|
| `ipca.csv` | `api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2020&dataFinal=31/12/2025` | 1,5 KB |
| `dfp_cia_aberta_2024.zip` | `dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2024.zip` | 13,4 MB |
| `cad_cia_aberta.csv` | `dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv` | 1,5 MB |
| `inmet-2024.zip` | `portal.inmet.gov.br/uploads/dadoshistoricos/2024.zip` | 102,8 MB (comece o download agora) |

### Passo 2 — Agente em modo seguro (2 min)

- **📸 Sugestão de Prints:** Claude Desktop, aba Code, com a pasta `projeto-dados` selecionada e o
  modo de permissão "Manual" (ou "Plan") visível; ou ChatGPT desktop em modo Codex com "Work in >
  This computer".

Abra o agente na pasta `projeto-dados`, em modo de planejamento ou somente leitura. Confira `uv
--version` no terminal.

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1 | Transformar o cálculo da inflação num projeto que roda de novo | 16 min |
| 2 | Fazer o ranking de lucro da bolsa sem cair na escala | 22 min |
| 3 | Descobrir qual setor lucrou mais, cruzando duas tabelas | 22 min |
| 4 | Pegar um erro silencioso com uma segunda opinião | 16 min |
| Projeto Final | Analisar o clima do Distrito Federal em 2024 a partir de cinco arquivos | 22 min |

Cada oficina deixa um script com asserts que passam.

---

## Oficina 1 — Seu primeiro projeto reprodutível

### 🎯 O Problema

Todo mês alguém refaz à mão o acumulado do IPCA numa planilha. Vamos deixar isso num script que
qualquer pessoa roda com um comando — e que se recusa a terminar se o número estiver errado.

### 🧰 O que você vai usar

- `dados/brutos/ipca.csv`; agente em modo de planejamento; uv.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** (a) plano do agente em seis passos aguardando aprovação; (b) terminal
  com a saída de `uv run analise_ipca.py` mostrando 4,83 e 4,26.

1. No Claude Code, digite `/init` e depois peça para incluir no `CLAUDE.md` (no Codex, crie
   `AGENTS.md`): "Dados em dados/brutos nunca são alterados. CSVs do Banco Central usam ponto e
   vírgula e vírgula decimal. Saídas vão para resultados/. Rodar com uv run."
2. Envie o brief: "Crie analise_ipca.py que calcula o IPCA acumulado de cada ano de 2020 a 2025 por
   composição, salva a tabela em resultados/ipca_anual.csv e um gráfico de barras em
   resultados/ipca_anual.png. Inclua asserts: 72 linhas lidas; 2024 = 4,83 e 2025 = 4,26 com
   tolerância de 0,01. Use uv para as bibliotecas. Mostre o plano e espere."
3. Leia o plano. Aprove (mude para `acceptEdits` no Claude Code, ou aprove os comandos no Codex).
4. Quando o agente pedir para instalar `pandas` e `matplotlib`, aprove.
5. Apague `resultados/` e peça: "Rode do zero com uv run e mostre a saída completa."
6. Peça: "Explique analise_ipca.py em blocos de até cinco linhas."

### ✅ Deu certo?

A saída mostra 4,83 (2024) e 4,26 (2025), os asserts passam, e `uv.lock` e `resultados/` existem.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O agente quer instalar um pacote com nome estranho | Recuse; procure o nome em pypi.org antes |
| `uv` não encontrado | Feche e reabra o terminal; se persistir, reinstale pelo comando oficial |
| Assert de 2022 falha por 0,01 | Esperado em alguns anos: as taxas mensais vêm arredondadas; registre como limitação |

### 🚀 Quer ir além?

1. Faça um `git init` e um commit "oficina 1". Validação: `git log` mostra o commit.
2. Peça um notebook `.ipynb` equivalente. Validação: abre e reproduz 4,83%.
3. Peça que o script aceite o ano como parâmetro. Validação: `uv run analise_ipca.py 2024` imprime
   4,83.

## Descrição

- **Objetivos da Aula:** criar arquivo de instruções, brief, plano, script com asserts e rodar do zero.
- **Habilidades Esperadas:** transformar sozinho um cálculo repetitivo num script reprodutível e
  autoverificável.

---

## Oficina 2 — O ranking que mentia, agora em código

### 🎯 O Problema

A diretoria quer o top 5 de lucro das companhias abertas de 2024, direto da CVM, e quer poder
refazer no ano que vem trocando um arquivo.

### 🧰 O que você vai usar

- `dados/brutos/dfp_cia_aberta_2024.zip` (19 CSVs, latin-1).

### 👐 Mão na massa

- **📸 Sugestão de Prints:** saída do script com a contagem de ESCALA_MOEDA (452 MIL, 8 UNIDADE) e o
  top 5 em bilhões.

1. Brief: "Crie ranking_lucro.py que lê dfp_cia_aberta_DRE_con_2024.csv direto do ZIP (latin-1, ponto
   e vírgula), filtra ORDEM_EXERC = ÚLTIMO e CD_CONTA = 3.11.01 e imprime quantas linhas e empresas.
   Mostre o plano."
2. Aprove e rode. Anote: 460 linhas, 458 empresas.
3. Peça: "Mostre as linhas duplicadas e a contagem de ESCALA_MOEDA."
4. Peça: "Remova duplicatas, converta para reais (MIL × 1.000; UNIDADE × 1), salve o top 20 em
   resultados/ e adicione asserts: 458 empresas; Petrobras = 36.606.000.000; nenhum valor de
   ESCALA_MOEDA além de MIL e UNIDADE."
5. Rode do zero.

> 💡 **Dica:** sem converter a escala, a Vivara (R$ 653 milhões, informada em reais) vira a "maior
> lucradora do país". O código roda — a premissa é que estava errada.

### ✅ Deu certo?

Top 5: Petrobras R$ 36,6 bi, Vale R$ 31,6 bi, Banco do Brasil R$ 26,4 bi, Bradesco R$ 17,3 bi,
Itaúsa R$ 14,8 bi; asserts passando.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| `UnicodeDecodeError` | "Leia com encoding latin-1" |
| O agente quer extrair o ZIP em `dados/brutos` | Peça para ler direto do ZIP ou extrair para `dados/tratados/` |
| Valores enormes no topo | Confira ESCALA_MOEDA antes de qualquer outra hipótese |

### 🚀 Quer ir além?

1. Conte empresas com prejuízo. Validação: 95.
2. Some o lucro das 458. Validação: ≈ R$ 303,9 bi.
3. Exporte o top 20 para Excel com openpyxl. Validação: o `.xlsx` abre com 20 linhas.

## Descrição

- **Objetivos da Aula:** ler direto de ZIP em latin-1, filtrar, deduplicar e normalizar escala com
  asserts.
- **Habilidades Esperadas:** detectar sozinho escala e duplicidade numa base contábil e travá-las
  com testes.

---

## Oficina 3 — Cruze duas tabelas sem inflar a soma

### 🎯 O Problema

Agora a pergunta é por setor. O setor está no cadastro da CVM, não na DRE. Juntar duas tabelas é
onde mais se erra em silêncio.

### 🧰 O que você vai usar

- O resultado da Oficina 2 e `dados/brutos/cad_cia_aberta.csv` (latin-1).

### 👐 Mão na massa

- **📸 Sugestão de Prints:** saída com "códigos repetidos no cadastro: 107" e "empresas sem
  cadastro: 4", seguida do top 5 de setores.

1. Peça: "Leia cad_cia_aberta.csv (latin-1). Quantas linhas e quantos CD_CVM únicos? Quantos códigos
   aparecem mais de uma vez?"
2. Anote: 2.680 linhas, 2.569 códigos, 107 repetidos.
3. Peça: "Antes de juntar, deixe uma linha por CD_CVM, preferindo SIT = ATIVO. Junte com o lucro da
   Oficina 2 e informe quantas empresas ficaram sem cadastro."
4. Peça: "Some o lucro por SETOR_ATIV, salve em resultados/ e adicione asserts: número de linhas
   depois da junção = 458; soma dos setores + sem cadastro = soma total da Oficina 2."
5. Rode do zero.

> ⚠️ **Cuidado:** juntar com a chave repetida duplica empresas e infla a soma sem nenhum aviso. O
> assert "linhas antes = linhas depois" é sua defesa.

### ✅ Deu certo?

4 empresas sem cadastro; top setores: Bancos R$ 60,9 bi, Petróleo e Gás R$ 50,9 bi, Energia Elétrica
R$ 36,5 bi, Extração Mineral R$ 31,4 bi; asserts passando.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Soma por setor maior que a soma total | Junção com chave repetida; volte ao passo 3 |
| "Comércio" com R$ 667 bi | A escala não foi convertida antes da junção |
| Setor vazio | Mostre essas empresas e decida (manter como "sem setor") |

### 🚀 Quer ir além?

1. Liste as 4 empresas sem cadastro. Validação: 4 nomes.
2. Conte empresas ativas por setor. Validação: soma = empresas casadas.
3. Gráfico de barras dos 10 setores. Validação: eixo em zero e fonte CVM.

## Descrição

- **Objetivos da Aula:** deduplicar chave, juntar tabelas e provar com asserts que nada foi inflado.
- **Habilidades Esperadas:** cruzar sozinho duas bases públicas e conferir a junção por contagem e
  soma de controle.

---

## Oficina 4 — Peça uma segunda opinião

### 🎯 O Problema

Você vai pedir uma tabela "simples" que costuma sair errada sem ninguém notar — e depois pôr um
revisor que não viu a conversa para auditar o projeto.

### 🧰 O que você vai usar

- Os scripts das Oficinas 2 e 3.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** tabela "lado a lado" com a coluna de empresa, mostrando que a JBS não
  está na linha da Vale.

1. Peça: "Faça uma tabela com o top 5 de receita (conta 3.01) e o top 5 de lucro lado a lado."
2. Leia: as linhas pareiam a mesma empresa ou só a posição? Se a 2ª linha mostra JBS (receita) ao lado
   do lucro da Vale, o pareamento está errado.
3. Peça: "Refaça juntando por CD_CVM, com uma linha por empresa e as duas colunas, e adicione um
   assert que confira que cada linha tem um só CD_CVM."
4. Revisão independente: no Claude Code, rode `/code-review`; no Codex, abra uma sessão nova e peça
   "Revise ranking_lucro.py e setores.py como um auditor que não confia no autor: liste 5 jeitos de o
   número final estar errado e escreva um teste para cada."
5. Registre no `README.md` o que a revisão apontou e o que você fez.

### ✅ Deu certo?

A tabela final tem Petrobras com receita R$ 490,8 bi e lucro R$ 36,6 bi na mesma linha; a revisão
gerou pelo menos um teste novo.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| `/code-review` não aparece | Use uma sessão nova com o pedido de auditor |
| O revisor só elogia | Peça "aponte obrigatoriamente cinco riscos" |
| Teste novo falha | Ótimo: investigue antes de "consertar" o teste |

### 🚀 Quer ir além?

1. Peça a outro modelo/ferramenta a mesma revisão. Validação: compare as listas.
2. Faça commit "oficina 4". Validação: `git log` com quatro commits.
3. Peça um relatório `resultados/relatorio.md` com tabelas e limitações. Validação: cita a escala e
   as duplicatas.

## Descrição

- **Objetivos da Aula:** reconhecer erro silencioso de pareamento e usar revisão independente.
- **Habilidades Esperadas:** desconfiar sozinho de tabelas "lado a lado" e acionar um revisor antes
  de entregar.

---

## Projeto Final — O clima do Distrito Federal em 2024

### 🎯 A missão

Uma equipe técnica precisa da temperatura média e da máxima de 2024 nas estações automáticas do
Distrito Federal, com um projeto que outra pessoa consiga rodar. São cinco arquivos dentro de um ZIP
de 565, cada um com oito linhas de cabeçalho antes da tabela.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** saída final com uma linha por estação (código, nome, linhas, vazios,
  média, máxima) e o gráfico de barras das médias.

1. Atualize o arquivo de instruções: "INMET: latin-1; ponto e vírgula; vírgula decimal; 8 linhas de
   metadados antes do cabeçalho; hora em UTC; valores vazios existem."
2. Brief: "Crie clima_df.py que lê, direto de dados/brutos/inmet-2024.zip, os arquivos com _DF_ no
   nome; para cada estação, conta linhas e vazios da coluna de temperatura do ar (bulbo seco) e
   calcula a média anual e a máxima da coluna de temperatura máxima na hora anterior. Salve tabela e
   gráfico em resultados/. Mostre o plano."
3. Aprove; peça asserts: 5 estações; 8.784 linhas por estação (2024 é bissexto: 366 × 24).
4. Rode do zero e peça a explicação por blocos.
5. Peça `README.md` com como rodar, verificação e limitações (vazios não entram na média; média de
   estações não é a média oficial do país).
6. Rode a revisão independente da Oficina 4.

### 🏁 Como saber que terminou

- [ ] 5 estações: A001 Brasília, A042 Brazlândia, A045 Águas Emendadas, A046 Gama, A047 Paranoá.
- [ ] 8.784 linhas em cada uma, garantidas por assert.
- [ ] Vazios na temperatura: 26, 235, 453, 66 e 416.
- [ ] Médias anuais ≈ 21,98 / 22,32 / 21,85 / 22,60 / 22,29 °C.
- [ ] Maior máxima horária: Gama, 37,5 °C.
- [ ] `uv run clima_df.py` reproduz tudo do zero; `dados/brutos` intocado; README com limitações.

## Descrição

- **Objetivos da Aula:** ler vários arquivos de dentro de um ZIP, tratar metadados e vazios, e
  entregar um projeto reprodutível com asserts e README.
- **Habilidades Esperadas:** conduzir sozinho, com o agente, uma análise de vários arquivos públicos
  que outra pessoa roda do zero e confere.

---

## A Parte dos Dez — Hábitos de quem analisa com agente

1. Plano antes de execução, sempre.
2. Dado bruto não se edita.
3. Declare encoding, separador e decimal no arquivo de instruções.
4. Pacote desconhecido: confira no pypi.org antes de aprovar.
5. Um assert por número que vai para o relatório.
6. Conte linhas antes e depois de cada filtro e junção.
7. Escala e duplicata antes de ranking.
8. Rode do zero antes de entregar.
9. Segunda opinião de quem não viu a conversa.
10. README com como rodar e limitações.

## Conseguiu! E agora?

Você montou quatro scripts que se defendem sozinhos e um projeto que outra pessoa roda com um
comando. Na próxima análise do trabalho, comece pelo brief e pelos asserts — e mantenha os dados
pessoais fora de conta pessoal.

Para ir além: *Claude Code no VSCode* e *ChatGPT CODEX* aprofundam as ferramentas; na trilha TE3, *IA
em projetos de engenharia* aplica o método a cálculos e memoriais.

---

## Rastreabilidade da auditoria

| Achado | Destino |
|---|---|
| H1 Regra de ouro | Antes de Arregaçar |
| H2 Instalação | Passos 1 e 2 (rotas do Essentials; uv) |
| H3 Sem permissões | Passo 2; Oficina 1, passos 3–4 |
| H4 O1 sem caso | Oficina 1 (IPCA com asserts) |
| H5 O2 sem caso | Oficina 2 (CVM; escala; duplicatas) |
| H6 Sem cruzamento | Oficina 3 (cadastro; chave repetida) |
| H7 Sem revisão | Oficina 4 (pareamento; `/code-review`) |
| H8 Projeto Final fraco | Projeto Final INMET com gabarito por estação |
| H9 Se travar genérico | Tabelas com problemas reais |
| H10 Um desafio só | Três desafios por oficina |
| H11 Carga horária | 105 min (ver `carga-horaria/carga-horaria-hands-on.md`) |

Decisão consciente: o Portal da Transparência (Viagens 2024, quatro tabelas, 148 MB) ficou fora
por não ter gabarito oficial localizado; pode virar desafio para o público de setor público.
