# IA para Análise de Dados — Essentials (roteiro final)

**Público-Alvo:** analistas, profissionais de finanças e planejamento e pesquisadores (T8);
escritórios de advocacia, departamentos jurídicos e compliance (J4); profissionais de finanças,
servidores e equipes de regulação, gestores de saúde, engenheiros, gestores escolares e
profissionais de comunicação (trilhas de dados F2, R4, S4, TE3, E6, C2).

**Objetivo Geral:** capacitar o participante a carregar uma base de dados no ChatGPT (recurso
"Análise de dados"), explorá-la, gerar gráficos honestos e interpretar os resultados com
verificação contra número oficial publicado, conhecendo o Julius AI como segunda opinião.

**Pré-requisitos:** Excel básico (o curso funciona para quem fez apenas *Claude Excel -
Essentials*). Nenhuma programação; nenhuma estatística além de média e porcentagem. Conta ChatGPT
(o plano Free atende, com limite de 3 uploads de arquivo por dia).

## Estrutura do Curso

| Nível | Módulos | Tempo |
|---|---|---|
| Preparação | Módulo 0 — Preparação e verificação inicial | 7 min |
| Nível 1 — Fundamentos | Módulo 1 — Análise de dados com IA: o que é e como funciona; Módulo 2 — Dados, privacidade e sigilo | 34 min |
| Nível 2 — O ciclo da análise | Módulo 3 — Carregar, entender e limpar; Módulo 4 — Explorar sem cair em armadilhas; Módulo 5 — Gráficos honestos | 54 min |
| Nível 3 — Confiança | Módulo 6 — Verificar e comunicar; Módulo 7 — Síntese e aplicação integrada | 32 min |
| **Total** | | **127 min** |

Fio condutor: o princípio "o número só vale depois da conferência" é plantado no Módulo 1 e
retomado nos Módulos 3, 5 e 6. Um caso-guia (IPCA mensal do Banco Central, gabarito do IBGE)
atravessa os Módulos 1, 3, 4 e 6.

Bases do curso (todas públicas, sem login, testadas em 17/11/2026):

| Base | Conteúdo | Link | Gabarito oficial |
|---|---|---|---|
| B1 | IPCA mensal 2020–2025 (Banco Central, série 433) | `api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2020&dataFinal=31/12/2025` | 2024: 4,83%; 2025: 4,26% (IBGE) |
| B2 | População por UF, Censo 2022 (IBGE/SIDRA 4709) | `apisidra.ibge.gov.br/values/t/4709/n3/all/v/93/p/2022?formato=csv` | Brasil: 203.080.756 |
| B3 | Cadastro de companhias abertas (CVM) | `dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv` | 2.680 linhas, codificação latin-1 |

---

## Módulo 0 — Preparação e verificação inicial

### 0.1 Conta, plano e limite de envio

- **📸 Sugestão de Prints:** página `chatgpt.com/pt-BR/pricing` rolada até a tabela "Compare os
  recursos dos planos", com as linhas "Upload de arquivos", "Análise de dados" e "Tabelas e
  gráficos interativos" destacadas e a coluna Free visível.

O recurso utilizado no curso chama-se **Análise de dados** e está presente em todos os planos do
ChatGPT; no plano Free, a página oficial o classifica como "Limitado". Cumpre registrar o limite que
mais afeta o estudo: "Usuários do plano gratuito têm um limite de 3 uploads de arquivos por dia"
(ajuda OpenAI, nov/2026). Os exercícios deste curso usam no máximo um envio por módulo.

| Plano | Preço (pt-BR, nov/2026) | Análise de dados |
|---|---|---|
| Free | R$ 0 | Limitado; 3 uploads por dia |
| Go | R$ 39,99/mês | Incluída |
| Plus | R$ 99,90/mês | Incluída |

### 0.2 Pasta do curso

- **📸 Sugestão de Prints:** Explorador de Arquivos (Windows) com a pasta `analise-ia` aberta,
  mostrando os três arquivos `ipca.csv`, `populacao-uf.csv` e `cad_cia_aberta.csv`.

Recomenda-se criar uma pasta `analise-ia` e salvar nela as três bases da tabela acima: abrir cada
link no navegador, aguardar o download (ou, se o navegador exibir o texto, usar `Arquivo > Salvar
como`) e renomear para `ipca.csv`, `populacao-uf.csv` e `cad_cia_aberta.csv`.

### Solução de Problemas

| Problema | Solução |
|---|---|
| O link do IBGE ou do Banco Central exibe o texto na tela em vez de baixar | `Navegador > Arquivo > Salvar como`, tipo "Texto" ou "Todos os arquivos", extensão `.csv` |
| O Excel abre o CSV com tudo numa coluna só | Não é preciso abrir no Excel; o arquivo vai direto para o ChatGPT |
| Conta Free já usou os 3 envios do dia | Retomar no dia seguinte; o curso não exige mais de um envio por módulo |

### Pílula Hands-on — Verificação inicial (7 min)

1. Entrar em `chatgpt.com` e identificar o plano em `ChatGPT > Perfil (canto inferior esquerdo)`.
2. Localizar o botão `+` da caixa de mensagem (sem enviar nada ainda).
3. Conferir que a pasta `analise-ia` contém os três arquivos.

**Critério de êxito:** plano identificado, botão `+` localizado e três arquivos na pasta.

## Descrição

- **Objetivos da Aula:** apresentar o recurso Análise de dados, os limites do plano Free e as bases
  do curso.
- **Habilidades Esperadas:** reconhecer sozinho o próprio plano e o limite de envio, e baixar uma
  base pública por link de API.

---

## Módulo 1 — Análise de dados com IA: o que é e como funciona

### 1.1 O que acontece quando um arquivo é enviado

- **📸 Sugestão de Prints:** resposta do ChatGPT a "Calcule o IPCA acumulado de 2024" mostrando a
  tabela interativa da base e, ao final da resposta, o controle que exibe o código executado
  (rótulo a conferir: "Ver análise"/"View analysis").

Análise de dados com inteligência artificial, no sentido deste curso, consiste em enviar uma base a
um assistente e formular perguntas em linguagem natural, sem escrever fórmulas. O ChatGPT não
"adivinha" os números: segundo a documentação oficial, "para algumas tarefas de análise de dados, o
ChatGPT escreve e executa código Python em um ambiente de notebook Jupyter com estado". Em termos
simples, o assistente redige uma receita de cálculo (o código), executa-a sobre o arquivo e relata o
resultado. O termo "com estado" significa que cada passo lembra o anterior, como um caderno de
laboratório; se o ambiente for reiniciado, a memória se perde e o arquivo precisa ser enviado de
novo.

O recurso já se chamou Code Interpreter e, depois, Advanced Data Analysis. Hoje não se liga em
nenhuma configuração: é acionado ao anexar um arquivo e pedir uma análise. Aceita planilhas (`.csv`,
`.xls`, `.xlsx`, `.tsv`, `.ods`), arquivos de dados (`.json`, `.xml`), texto e PDFs; a própria
OpenAI adverte que tabelas em PDF digitalizado ou em imagem "podem não" ter os valores extraídos de
forma confiável. Outro limite relevante: o ambiente Python "não pode fazer solicitações externas na
web", de modo que a base precisa ser baixada antes e enviada como arquivo.

O Julius AI é um espaço de trabalho especializado no mesmo tipo de tarefa. Escreve Python ou R,
mostra cada etapa como "Generating code → Generated code" e oferece o Data Explorer para inspecionar
as tabelas geradas. Neste curso, funciona como segunda opinião opcional: a interface é em inglês
(as respostas podem ser em português, por instrução) e o plano gratuito dá 75 créditos iniciais e 25
diários, com arquivos apagados após uma hora de inatividade.

Decorre desse funcionamento o princípio que orienta todo o curso: **o número só vale depois da
conferência**. A OpenAI recomenda revisar "o código gerado, as saídas e as suposições antes de
confiar no resultado". A análise segue sete etapas — carregar, entender, limpar, explorar,
visualizar, interpretar e comunicar — e a verificação atravessa todas elas.

| Etapa | Pergunta que responde | Módulo |
|---|---|---|
| Carregar e entender | O que há no arquivo? | 3 |
| Limpar | O arquivo foi lido corretamente? | 3 |
| Explorar | O que os números dizem? | 4 |
| Visualizar | Como mostrar sem distorcer? | 5 |
| Interpretar e comunicar | O que se pode e o que não se pode concluir? | 6 |

### Avaliação — questão (4 min)

Um analista envia uma planilha ao ChatGPT e recebe um total. Qual procedimento é coerente com a
orientação oficial da OpenAI?

(a) Aceitar o total, pois foi calculado por código.
(b) Revisar o código, as saídas e as suposições, e conferir o total com uma fonte independente.
(c) Repetir a pergunta até obter o mesmo número duas vezes.
(d) Ativar o modo de análise avançada nas configurações.

**Gabarito:** (b). Código executado pode estar certo sobre a premissa errada; (c) não verifica nada;
(d) não existe.

## Descrição

- **Objetivos da Aula:** explicar o código por trás da resposta, os formatos aceitos, os limites e
  o papel do Julius; plantar o princípio da conferência.
- **Habilidades Esperadas:** descrever, com as próprias palavras, como o ChatGPT chega a um número e
  por que esse número precisa ser conferido.

---

## Módulo 2 — Dados, privacidade e sigilo

### 2.1 Para onde vai o arquivo

- **📸 Sugestão de Prints:** `ChatGPT > Perfil > Configurações > Controles de dados` aberto, com a
  chave "Melhorar o modelo para todo mundo" visível; no Julius, a página "Privacy and Data Security"
  com o trecho sobre "AI technology providers".

Nos espaços pessoais Free, Plus e Pro, "o compartilhamento de dados para treinamento fica ativado
por padrão" (ajuda OpenAI, 16/11/2026). A opção é desligada em `Configurações > Controles de dados >
Melhorar o modelo para todo mundo`. O chat temporário não entra no histórico e não treina modelos,
mas pode ser retido por até 30 dias por segurança. Conversas excluídas são apagadas dos sistemas em
até 30 dias; arquivos salvos na Biblioteca são excluídos à parte. Nos planos Business, Enterprise e
Edu, a OpenAI informa que não usa os dados para treinar modelos por padrão.

No Julius, a documentação declara que os Termos e a Política "permitem compartilhar o conteúdo do
usuário, incluindo prompts, arquivos enviados e saídas, com provedores de tecnologia de IA para
ajudar a avaliar, melhorar e desenvolver os modelos deles"; a recusa é feita por e-mail
(privacy@julius.ai). Os dados podem ser armazenados nos Estados Unidos.

### 2.2 O semáforo de dados

| Cor | O que é | Exemplo | Conduta |
|---|---|---|---|
| Verde | Dado público ou agregado | IPCA, população por UF | Pode ser enviado |
| Amarelo | Dado interno sem pessoa identificável | Vendas por região | Só com política da organização e conta corporativa |
| Vermelho | Dado pessoal, sensível ou sigiloso | CPF, prontuário, processo com partes, carteira de clientes | Não enviar em conta pessoal; pseudonimizar ou agregar antes |

A Lei Geral de Proteção de Dados (LGPD) protege qualquer informação que identifique uma pessoa. A
ANPD publicou apenas um estudo preliminar sobre anonimização e pseudonimização (versão de 2023,
consulta encerrada em 2024); pseudonimizar significa trocar o identificador por um código e guardar a
tabela de correspondência fora da ferramenta. Para a advocacia, a Recomendação 001/2024 do Conselho
Federal da OAB orienta supervisionar resultados, preservar o sigilo e comunicar ao cliente o uso de
IA.

### Pílula Hands-on — Configurar antes de enviar (7 min)

1. Abrir `ChatGPT > Perfil > Configurações > Controles de dados` e decidir sobre "Melhorar o modelo
   para todo mundo".
2. Abrir um chat temporário em `ChatGPT > Novo chat > Chat temporário` e fechá-lo.

**Critério de êxito:** estado da opção registrado; chat temporário localizado.

### Discussão orientada (8 min)

Classificar no semáforo: (1) IPCA mensal; (2) planilha de honorários com nome dos clientes; (3)
número de atendimentos por unidade de saúde, sem pacientes; (4) lista de alunos com notas; (5) DRE
publicada de companhia aberta.

**Gabarito:** (1) verde; (2) vermelho; (3) verde ou amarelo, conforme a política do órgão; (4)
vermelho; (5) verde.

## Descrição

- **Objetivos da Aula:** apresentar os controles de dados do ChatGPT, a política do Julius, a LGPD,
  a pseudonimização e o sigilo profissional antes do primeiro envio.
- **Habilidades Esperadas:** decidir sozinho, antes de cada envio, se uma base pode ir para o
  assistente e em que conta.

---

## Módulo 3 — Carregar, entender e limpar a base

### 3.1 Enviar e fazer o "Raio X"

- **📸 Sugestão de Prints:** caixa de mensagem com o menu `+` aberto e "Adicionar fotos e arquivos"
  destacado; em seguida, a tabela interativa de `ipca.csv` com o ícone de duas setas (expandir)
  destacado no canto superior direito.

O envio é feito em `ChatGPT > Caixa de mensagem > + > Adicionar fotos e arquivos`. Ao carregar uma
planilha, "o ChatGPT cria automaticamente uma visualização interativa da tabela"; o ícone de duas
setas expande a visualização. Antes de qualquer cálculo, recomenda-se o "Raio X": número de linhas
e colunas, tipo de cada coluna (número, texto, data), período coberto e valores vazios. O Raio X
equivale a conferir o conteúdo de uma caixa antes de assinar o recebimento.

### 3.2 Os formatos brasileiros

| Característica | Onde aparece | O que pode dar errado |
|---|---|---|
| Separador `;` | Banco Central, IBGE, CVM, CNJ | Tudo lido como uma coluna só |
| Vírgula decimal (`0,21`) | Banco Central | Número lido como texto |
| Codificação latin-1 | CVM, CNJ | "RECUPERAÇÃO" vira "RECUPERA��O" |
| Cabeçalho em duas linhas | IBGE/SIDRA (códigos na 1ª, nomes na 2ª) | Primeira linha de dados tratada como cabeçalho |
| Escala ("MIL") | CVM | Valor mil vezes menor |

Codificação é o "alfabeto" em que o arquivo foi gravado; lido com o alfabeto errado, os acentos se
corrompem. Convém declarar o formato no pedido. A ajuda oficial também recomenda dados "com nomes de
coluna claros e um registro por linha" e adverte que um arquivo pode subir e, ainda assim, não ser
analisado por inteiro.

### Solução de Problemas

| Problema | Solução |
|---|---|
| Acentos corrompidos | Pedir: "Releia o arquivo com codificação latin-1" |
| Número tratado como texto | Pedir: "Converta a coluna valor considerando vírgula decimal" |
| "Limite de upload atingido" | Aguardar o horário indicado; tentativas que falham podem contar para o limite |
| Resultado parece parcial | Pedir que informe quantas linhas leu e compará-lo com o Raio X |

### Pílula Hands-on — Raio X de duas bases (6 min)

1. Enviar `ipca.csv` com o pedido: "Antes de calcular qualquer coisa, informe número de linhas e
   colunas, tipo de cada coluna, período coberto e valores vazios."
2. Na mesma conversa, enviar `cad_cia_aberta.csv` e pedir as cinco primeiras linhas.

**Critério de êxito:** `ipca.csv` com 72 linhas, colunas `data` e `valor`, de 01/2020 a 12/2025,
`valor` reconhecido como número; cadastro exibido com acentos corretos (se não, aplicado o pedido de
latin-1). Atenção: dois envios no mesmo dia.

## Descrição

- **Objetivos da Aula:** demonstrar o envio, a tabela interativa e o Raio X; apresentar os formatos
  típicos de dados públicos brasileiros.
- **Habilidades Esperadas:** carregar uma base, descrevê-la antes de calcular e corrigir sozinho a
  leitura de separador, decimal e codificação.

---

## Módulo 4 — Explorar sem cair em armadilhas

### 4.1 Seis conceitos que evitam conclusões erradas

- **📸 Sugestão de Prints:** tabela gerada pelo ChatGPT com média e mediana da população das UFs,
  com a linha de São Paulo selecionada (Ctrl+clique).

| Conceito | Definição simples | Exemplo nas bases |
|---|---|---|
| Média × mediana | Média divide o total igualmente; mediana é o valor do meio da fila | População média das UFs ≈ 7,52 milhões, puxada por SP (44,4 milhões); a mediana é 3,94 milhões (Amazonas) |
| Valor atípico | Ponto muito fora do padrão: erro ou fato relevante | Lucro de uma empresa mil vezes maior por erro de escala |
| Taxa por 100 mil | Divide pelo tamanho da população para comparar | Processos por 100 mil habitantes, não em número absoluto |
| Nominal × real | Valor corrigido pela inflação | R$ 1.000 de jan/2024 ≈ R$ 1.092,96 em dez/2025 |
| % × ponto percentual | Diferença entre taxas se mede em p.p. | IPCA caiu 0,57 p.p. de 2024 para 2025 |
| Correlação × causa | Andar junto não prova causa | Mais processos onde há mais gente |

A OpenAI recomenda instruir o assistente a "não tratar correlações como causas" e a "apontar
quaisquer limitações nos dados". O ChatGPT calcula somas, médias, medianas, mínimos, máximos e
desvio padrão; a interpretação de qual medida usar permanece do analista.

### Pílula Hands-on — O acumulado do caso-guia (6 min)

Na conversa do IPCA, pedir: "Calcule o IPCA acumulado de 2024 e de 2025 a partir das taxas mensais
e mostre a fórmula usada."

**Critério de êxito:** 2024 = 4,83% e 2025 = 4,26%, com fórmula de composição (produto de
(1 + taxa/100), menos 1).

### Avaliação — questão (4 min)

O IPCA foi 4,83% em 2024 e 4,26% em 2025. A frase correta é:

(a) A inflação caiu 0,57%. (b) A inflação caiu 0,57 ponto percentual. (c) A inflação caiu 11,8
pontos percentuais.

**Gabarito:** (b) — é a forma usada pelo IBGE. A queda relativa seria de cerca de 11,8%, não 11,8
p.p.

## Descrição

- **Objetivos da Aula:** apresentar os conceitos estatísticos mínimos com exemplos nas bases do
  curso.
- **Habilidades Esperadas:** escolher sozinho entre média e mediana, número absoluto e taxa, valor
  nominal e real, e redigir comparações em pontos percentuais.

---

## Módulo 5 — Gráficos honestos

### 5.1 Pedir, ajustar e baixar

- **📸 Sugestão de Prints:** gráfico de barras gerado pelo ChatGPT com o controle "Alternar para
  gráfico interativo" destacado e o menu de cores aberto, mostrando o campo de código hexadecimal.

O ChatGPT gera gráficos estáticos de linhas, barras, pizza, histogramas, dispersão, box plots, mapas
de calor, área, radar, mapas de árvore, bolhas e cascata. Gráficos de barras, linhas, pizza e
dispersão podem ser exibidos como interativos, pelo controle "Alternar para gráfico interativo"; o
retorno é feito por "Alternar para gráfico estático". As cores podem ser editadas por paleta ou por
código hexadecimal, e o download padrão é em PNG. No Julius, o gráfico é descrito em linguagem
natural e salvo com o botão direito do mouse.

### 5.2 As oito táticas que enganam

Estudo apresentado no IEEE VIS 2025 reuniu oito táticas de gráfico enganoso: eixo truncado,
distorção de proporção, eixo duplo, eixo invertido, projeção distorcida (como o 3D), desproporção
entre dado e desenho, codificação contínua inadequada e codificação categórica inadequada. No
experimento, com o eixo invertido, um modelo de IA "concordou fortemente" que uma série em queda
estava em alta. Depreende-se que pedir à IA para "conferir o gráfico" não substitui a leitura humana.
Outro estudo (VisEval, 2024) classifica as falhas de gráficos gerados por IA em código que não
roda, gráfico que usa coluna ou legenda errada e gráfico ilegível.

| Pergunta de conferência | Tática que evita |
|---|---|
| O eixo das barras começa em zero? | Eixo truncado |
| O eixo cresce na direção habitual? | Eixo invertido |
| Há uma escala só? | Eixo duplo |
| O título diz a conclusão e a fonte está no rodapé? | Leitura sem contexto |
| As cores se distinguem sem depender de vermelho × verde? | Exclusão de daltônicos |

### Pílula Hands-on — O mesmo dado, duas histórias (6 min)

1. Enviar `populacao-uf.csv` e pedir um gráfico de barras horizontais das 10 UFs mais populosas,
   ordenado, com eixo começando em zero, título com a conclusão e fonte no rodapé.
2. Pedir a versão com o eixo começando em 5 milhões.

**Critério de êxito:** o participante descreve por escrito qual versão exagera as diferenças e por
quê (eixo truncado).

## Descrição

- **Objetivos da Aula:** demonstrar a criação e o ajuste de gráficos; apresentar as táticas
  enganosas documentadas e os cuidados de acessibilidade.
- **Habilidades Esperadas:** pedir e ajustar um gráfico adequado ao dado e reconhecer sozinho um
  gráfico enganoso.

---

## Módulo 6 — Verificar e comunicar

### 6.1 O que a pesquisa independente mostra

- **📸 Sugestão de Prints:** resposta do ChatGPT com o código do cálculo do IPCA aberto, destacando
  a linha da multiplicação dos fatores.

Estudo publicado no Journal of Medical Internet Research (2025) testou o ChatGPT com Python em
dados de saúde: acertou tratamento de dados e estatística descritiva em todas as tentativas, mas, na
estatística inferencial, acertou 32,5% com pedidos básicos, 81,3% com pedidos intermediários e
92,5% com pedidos detalhados. O detalhamento do pedido mudou o resultado tanto quanto a ferramenta.
Nas bases deste curso há armadilhas reais: na CVM, oito empresas informam valores em reais e as
demais em milhares — sem converter, uma empresa com lucro de R$ 653 milhões aparece acima da
Petrobras (R$ 36,6 bilhões); no CNJ, a base inclui linhas de total por ramo e a soma direta dos
casos novos de 2025 dá o dobro dos 40,9 milhões oficiais.

### 6.2 Rotina de conferência e comunicação

| Conferência | Como |
|---|---|
| 1. Contar linhas | Antes e depois de cada filtro |
| 2. Recalcular um total | Na planilha ou à mão |
| 3. Ler o cálculo | Abrir o código e localizar a fórmula principal |
| 4. Comparar com número oficial | IBGE, Banco Central, CVM, CNJ |
| 5. Listar premissas | Pedir separador, filtros, linhas excluídas, escala |

Para comunicar, a OpenAI recomenda começar pela decisão ("Estou tentando decidir ___, com base em
___"), pedir um resumo executivo e "mostrar como chegou" aos números. Um resumo honesto contém
achados, premissas, limitações e fonte com data de extração. Quando a pergunta exigir inferência
estatística ou previsão, recomenda-se procurar um especialista ou avançar para o curso *Dados com
Python e IA*.

### Pílula Hands-on — Mostre o cálculo (6 min)

Na conversa do IPCA, pedir o código do acumulado de 2024 e, em seguida: "Calcule também somando as
taxas mensais. Qual dos dois é o correto e por quê?"

**Critério de êxito:** composição = 4,83% (bate com o IBGE); soma = 4,73% (errada); o participante
aponta no código a diferença entre multiplicar e somar.

### Avaliação — questão (4 min)

Ao ordenar o lucro das companhias da CVM, uma empresa pouco conhecida aparece mil vezes acima da
segunda colocada. Qual a primeira hipótese a investigar?

(a) Fraude contábil. (b) Escala do valor (mil × unidade). (c) Erro do ChatGPT na ordenação.

**Gabarito:** (b) — na base de 2024, oito empresas informam em reais e as demais em milhares.

## Descrição

- **Objetivos da Aula:** apresentar erros documentados de IA em análise de dados, a rotina de cinco
  conferências e a estrutura de um resumo executivo com premissas.
- **Habilidades Esperadas:** aplicar sozinho as cinco conferências a qualquer resultado e redigir um
  resumo que separa achado, premissa e limitação.

---

## Módulo 7 — Síntese e aplicação integrada

### 7.1 Atividade integradora

- **📸 Sugestão de Prints:** resumo executivo final na conversa, com a tabela anual do IPCA e o
  gráfico de linhas acima dele.

A atividade integra as competências dos módulos anteriores sobre a base B1, em conversa nova (o
envio de `ipca.csv` conta um upload):

1. (Módulo 2) Confirmar o estado dos controles de dados.
2. (Módulo 3) Enviar `ipca.csv` e pedir o Raio X.
3. (Módulo 4) Pedir a tabela do IPCA acumulado de cada ano de 2020 a 2025.
4. (Módulo 5) Pedir gráfico de barras anual com eixo em zero, título com a conclusão e fonte.
5. (Módulo 6) Conferir 2024 e 2025 com o IBGE, pedir as premissas e um resumo executivo de cinco
   linhas.

| Critério | Atendido? |
|---|---|
| Raio X correto (72 linhas, 2020–2025) | |
| 2024 = 4,83% e 2025 = 4,26% | |
| Gráfico com eixo em zero, título-conclusão e fonte | |
| Premissas listadas (separador, decimal, composição) | |
| Resumo sem afirmação causal | |

### Avaliação (4 min)

Autoavaliação pela tabela acima. Diferença de até 0,01 ponto percentual entre o acumulado calculado
e o publicado em anos anteriores a 2024 decorre do arredondamento das taxas mensais e deve ser
registrada como limitação, não corrigida.

## Descrição

- **Objetivos da Aula:** integrar carregar, explorar, visualizar, verificar e comunicar numa só
  análise.
- **Habilidades Esperadas:** conduzir sozinho uma análise curta de base pública, com gráfico honesto
  e conferência contra o número oficial.

---

## Encerramento

O curso apresentou a análise de dados conversacional como um ciclo de sete etapas, sustentado pela
conferência contra fonte oficial. Recomenda-se praticar com bases públicas de gabarito conhecido
antes de levar a ferramenta a dados de trabalho, e sempre sob a política de dados da organização.

Para aprofundamento, o curso *IA para Análise de Dados - Hands On* conduz análises completas de
bases da CVM e do CNJ; *Dados com Python e IA* leva o mesmo ciclo para código próprio e
reprodutível; *Jurimetria com IA* aplica-o a dados judiciais.

> **Síntese:** a IA escreve o cálculo; a responsabilidade pelo número continua de quem o assina.

---

## Rastreabilidade da auditoria

| Achado | Destino |
|---|---|
| E1 Nome e acionamento errados | Módulo 1, 1.1 |
| E2 Sem verificação inicial | Módulo 0 |
| E3 Segurança tardia | Módulo 2, antes do primeiro envio (Módulo 3) |
| E4 Exercícios sem gabarito | Bases B1–B3 com gabarito; CVM e CNJ no Módulo 6 |
| E5 Base indefinida | Tabela de bases e Módulo 0 |
| E6 Código invisível | Módulos 1 e 6 (pílula "Mostre o cálculo") |
| E7 Formatos brasileiros | Módulo 3, 3.2 |
| E8 Estatística rasa | Módulo 4, 4.1 |
| E9 Gráficos sem crítica | Módulo 5 |
| E10 Erros da IA ausentes | Módulo 6, 6.1 |
| E11 Comunicação rasa | Módulo 6, 6.2; Módulo 7 |
| E12 Julius sem papel | Módulos 1, 2 e 5 (segunda opinião, opcional) |
| E13 Sem fio condutor | Princípio da conferência e caso IPCA (Módulos 1, 3, 4, 6, 7) |
| E14 Carga horária | 127 min (ver `carga-horaria/carga-horaria-essentials.md`) |
| E15 Quando parar | Módulo 6, 6.2 |

Decisões conscientes: conectores Google Drive/OneDrive e o plugin Data não ganharam exercício
(dependem de plano e workspace); o Julius não é obrigatório em nenhuma atividade, por causa da
política de dados e dos créditos.
