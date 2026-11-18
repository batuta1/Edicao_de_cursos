<link rel="stylesheet" href="../../css/style.css">

# Roteiro Articulate 360 — Claude para Excel — Curso Hands-on

**Claude para Excel: Consultoria Analítica, Fórmulas Complexas e Automação — Curso Hands-on**

---

## Identificação

| Campo | Definição |
|---|---|
| **Curso** | Claude para Excel: Consultoria Analítica, Fórmulas Complexas e Automação — Curso Hands-on |
| **Natureza** | Autoinstrucional, assíncrono, orientado à execução prática |
| **Plataforma de desenvolvimento** | Articulate 360 |
| **Ferramenta sugerida** | Rise 360 (estrutura principal dos módulos) com blocos Storyline 360 embutidos para interações de quiz e cenário |
| **Carga horária** | 90 minutos (aproximadamente) |
| **Público-alvo** | Docentes do ensino superior iniciantes em inteligência artificial; analistas administrativos; alunos do ensino superior |
| **Pré-requisitos** | Conhecimento básico de Excel (identificar células, colunas e linhas); acesso a uma conta em claude.ai; Microsoft Excel 2019 ou Microsoft 365 instalado |
| **Recursos necessários** | Computador com Excel instalado; navegador com acesso a claude.ai; arquivo `treino_claude.xlsx` criado durante o Módulo 1 (reutilizado nos demais módulos) |
| **Produto final do participante** | Arquivo `treino_claude.xlsx` contendo quatro abas operacionais — Clientes, Vendas, Clientes com classificação automatizada e Dashboard — com fórmulas funcionais e dados tratados, produzidos ao longo dos módulos práticos |

---

## Objetivo Geral

O presente curso tem por finalidade habilitar o participante a utilizar o modelo de inteligência artificial Claude como ferramenta de consultoria técnica aplicada ao Microsoft Excel, conduzindo-o pela execução prática de quatro processos analíticos fundamentais: diagnóstico de qualidade de dados, cruzamento de tabelas por meio de funções de busca, classificação automatizada por regras de negócio e normalização de campos de texto. A competência operacional desenvolvida ao longo do curso consolida-se na produção de um arquivo Excel funcional com múltiplas abas integradas, que constitui o produto final verificável e imediatamente aplicável ao contexto profissional ou acadêmico do participante.

---

## Competências Práticas a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Formular prompts estruturados no Claude para solicitar diagnósticos de qualidade de bases de dados no Excel, identificando campos vazios, duplicatas, formatos inconsistentes e anomalias numéricas.
2. Aplicar as funções `XLOOKUP` (ou `PROCV` com `IFERROR`) para cruzar dados entre duas abas distintas de uma planilha, tratando adequadamente registros sem correspondência.
3. Construir fórmulas de lógica condicional com `IFS` ou `SE encadeado` para classificar registros segundo regras de negócio com múltiplas condições simultâneas.
4. Utilizar as funções `PRI.MAIÚSCULA` e `TIRAR.ESPAÇOS` em combinação para normalizar campos de texto e converter resultados de fórmulas em valores fixos por meio do recurso Colar Especial.

---

## Estrutura Geral do Curso

O curso está organizado em quatro módulos práticos progressivos e um módulo de síntese aplicada. Cada módulo parte de um problema concreto, conduz o participante por uma sequência de execução passo a passo e encerra com um produto parcial verificável. Os produtos parciais de cada módulo são acumulados no mesmo arquivo Excel ao longo do curso, de modo que o módulo de síntese integra e valida os elementos produzidos anteriormente em uma entrega final unificada.

| Módulo | Foco prático | Produto parcial | Interação principal | Tempo |
|---|---|---|---|---|
| 1 | Diagnóstico de qualidade de dados com o Claude | Aba `Clientes` com lista de problemas registrada na coluna H | Demonstração guiada + atividade hands-on | 20 min |
| 2 | Cruzamento de tabelas com funções de busca | Aba `Vendas` com coluna `Nome_Cliente` preenchida por fórmula | Atividade guiada + knowledge check | 20 min |
| 3 | Classificação automatizada por regras de negócio | Aba `Clientes` com coluna `Classificação` por IFS | Cenário prático + checklist de validação | 20 min |
| 4 | Normalização de campos de texto | Aba `Clientes` com coluna `Nome_Limpo` convertida em valores fixos | Demonstração + atividade hands-on | 20 min |
| 5 | Síntese e aplicação integrada | Aba `Dashboard` com cinco indicadores e ranking de clientes | Atividade integradora + checklist final | 10 min |

---

<div style="page-break-after: always;"></div>

# Módulo 1 — Diagnóstico de Dados com o Claude

## Encadeamento

Este é o ponto de partida do curso: antes de qualquer análise, o participante aprende a avaliar a qualidade dos dados com o auxílio do Claude.

## Finalidade prática

Neste módulo, o participante construirá a planilha-base do curso (`treino_claude.xlsx`, aba `Clientes`) e utilizará o Claude para realizar um diagnóstico completo de qualidade dos dados inseridos. O produto parcial é a própria aba `Clientes` com a coluna `Problemas encontrados` (coluna H) preenchida a partir da resposta do Claude.

## Objetivos de Aprendizagem Prática

Ao final deste módulo, o participante deverá ser capaz de:

1. Criar e nomear abas no Excel e inserir dados tabulares a partir de um modelo fornecido.
2. Copiar dados do Excel e colá-los no chat do Claude como texto estruturado.
3. Formular um prompt de diagnóstico de qualidade que solicite identificação de duplicatas, campos vazios, formatos inconsistentes e anomalias numéricas.
4. Registrar os problemas apontados pelo Claude em uma coluna auxiliar da planilha.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 1.1 | Abertura do módulo | Título, objetivo prático e produto parcial esperado | Imagem ilustrativa: tela do Excel ao lado do chat do Claude |
| 1.2 | Texto curto explicativo | Contextualização: por que diagnosticar antes de analisar | Nenhum (bloco de texto simples) |
| 1.3 | Process block (Rise 360) | Sequência visual: Abrir Excel → Criar aba → Inserir dados → Copiar → Colar no Claude → Ler resposta → Registrar problemas | Ícones sequenciais ou setas entre etapas |
| 1.4 | Captura de tela anotada | Tela do Excel com os dados da aba `Clientes` inseridos (com setas apontando para os erros propositais: duplicata, nome vazio, "R$ 33.000") | Captura de tela anotada com balões ou setas coloridas |
| 1.5 | Demonstração passo a passo | Instruções de como copiar os dados e formular o prompt no Claude | Captura de tela do chat do Claude com o prompt enviado e os dados colados |
| 1.6 | Captura de tela anotada | Exemplo de resposta do Claude com os problemas listados (duplicata, nome vazio, formatos de data, valor com "R$") | Captura anotada da resposta do Claude com destaques |
| 1.7 | Atividade guiada | O participante executa os passos na própria máquina e registra os problemas na coluna H | Nenhum (atividade offline no Excel do participante) |
| 1.8 | Knowledge check | Questão de múltipla escolha: qual problema o Claude identificou na linha 6? | Bloco Storyline 360 embutido com feedback imediato |
| 1.9 | Checklist | Lista de verificação do produto parcial (aba `Clientes` criada, dados inseridos, coluna H preenchida) | Bloco de checklist interativo do Rise 360 |
| 1.10 | Fechamento do módulo | Resumo do que foi produzido e anúncio do próximo módulo | Nenhum (bloco de texto) |

## Conteúdo Instrucional Enxuto

O diagnóstico de qualidade de dados é a etapa que precede qualquer análise confiável. Quando uma base de dados contém duplicatas, campos vazios, formatos inconsistentes ou valores numéricos armazenados como texto, as fórmulas subsequentes produzem resultados incorretos ou simplesmente retornam erros — sem necessariamente avisar que algo está errado. Identificar esses problemas antes de começar a analisar poupa retrabalho e garante que as conclusões sejam baseadas em dados confiáveis.

O Claude realiza esse diagnóstico a partir de uma amostra de dados colada diretamente no chat como texto. Não é necessário enviar o arquivo Excel — basta selecionar as células relevantes, copiá-las e colá-las na conversa, acompanhadas de uma pergunta estruturada. A qualidade do diagnóstico depende diretamente da clareza da pergunta: quanto mais o participante especificar o que deseja verificar (campos obrigatórios, formato esperado de datas, regra de unicidade do identificador), mais precisa e útil será a resposta.

Neste módulo, a planilha utilizada contém seis erros propositais: uma duplicata no campo ID (valor 102 aparece duas vezes), um campo Nome vazio, dois formatos distintos de data na mesma coluna, capitalização inconsistente nos nomes e um valor de receita armazenado como texto ("R$ 33.000" em vez do número puro 33000). O participante deve ser capaz de identificar todos esses problemas na resposta do Claude ao final da atividade.

## Demonstração Guiada

1. Abrir o Excel e criar um arquivo novo chamado `treino_claude.xlsx`.
2. Clicar duas vezes na aba inferior e renomeá-la para `Clientes`.
3. Inserir os dados fornecidos no roteiro, célula a célula, a partir de A1 — incluindo os erros propositais (duplicata no ID 102, nome vazio na linha 5, "R$ 33.000" na linha 6).
4. Selecionar o intervalo A1:F7, copiar com Ctrl+C, abrir o claude.ai em nova conversa.
5. Colar os dados no campo de mensagem, adicionar o prompt de diagnóstico e enviar.
6. Ler a resposta do Claude e registrar cada problema apontado nas células H2, H3, H4 e seguintes.
7. Enviar uma segunda mensagem no mesmo chat solicitando a fórmula para corrigir o problema mais simples.

Captura de tela recomendada (tela 1.4): planilha Excel com os dados inseridos na aba `Clientes`, com anotações visuais (setas ou balões coloridos) apontando para a linha duplicada (ID 102), a célula vazia (B5), o formato de data diferente (D3: "2021-07-22") e o valor com "R$" (E6). Esta captura serve como referência visual para o participante confirmar que seus dados estão corretos antes de prosseguir.

Captura de tela recomendada (tela 1.6): janela do chat do Claude exibindo o prompt de diagnóstico enviado e a resposta com a lista de problemas identificados, com destaques (sublinhado ou caixa colorida) sobre cada problema mencionado pelo modelo.

## Atividade Hands-on

### Atividade prática — Construir a planilha e obter o diagnóstico (20 minutos)

**Tarefa:** Criar a aba `Clientes` no arquivo `treino_claude.xlsx`, inserir os dados fornecidos com os erros propositais, copiar os dados para o Claude, formular o prompt de diagnóstico e registrar os problemas identificados na coluna H da planilha.

**Procedimento:**

1. Abrir o Excel e criar o arquivo `treino_claude.xlsx`; renomear a primeira aba para `Clientes`.
2. Inserir os dados da tabela fornecida (6 linhas de dados + cabeçalho) exatamente como especificado, incluindo os erros propositais.
3. Salvar o arquivo (Ctrl+S).
4. Selecionar A1:F7, copiar (Ctrl+C), abrir o claude.ai e iniciar uma nova conversa.
5. Colar os dados no campo de mensagem, adicionar o prompt de diagnóstico indicado no roteiro e enviar.
6. Ler a resposta completa do Claude; voltar ao Excel e registrar cada problema apontado em H2, H3 e nas células seguintes (um problema por linha).
7. Retornar ao Claude no mesmo chat e solicitar a fórmula para corrigir o problema mais simples; anotar a fórmula sugerida.

**Produto parcial esperado:** Arquivo `treino_claude.xlsx` com a aba `Clientes` contendo os dados inseridos e a coluna H preenchida com pelo menos cinco problemas identificados pelo Claude.

**Critério de êxito:** A coluna H deve conter, no mínimo, os seguintes problemas: duplicata no ID 102; campo Nome vazio na linha 5; dois formatos distintos de data; capitalização inconsistente nos nomes; valor de receita armazenado como texto na linha 6. O participante deve também ter recebido e anotado ao menos uma fórmula corretiva sugerida pelo Claude.

## Checkpoint de Aprendizagem

**Tipo:** Múltipla escolha

**Enunciado:** O participante inseriu na aba `Clientes` um valor de receita escrito como "R$ 33.000" (com símbolo de moeda e ponto como separador de milhar). Ao solicitar ao Claude um diagnóstico de qualidade, o modelo apontou esse campo como problemático. Por que esse formato pode causar erros em fórmulas numéricas do Excel?

a) Porque o Excel não aceita o símbolo "R$" em nenhuma circunstância.
b) Porque valores com símbolo de moeda e separador de texto são interpretados pelo Excel como texto, não como número — e fórmulas numéricas como SOMA e MÉDIA não operam sobre texto.
c) Porque o Claude não consegue interpretar valores monetários.
d) Porque o Excel só aceita valores com vírgula como separador decimal, não com ponto.

**Gabarito:** Alternativa b.

**Fundamentação:** O Excel diferencia números de texto pela forma como os dados são armazenados internamente. Quando uma célula contém "R$ 33.000", o Excel a trata como sequência de caracteres, não como valor numérico. Fórmulas como `SOMA`, `MÉDIA` e `IFS` com comparações numéricas ignoram ou rejeitam esse tipo de entrada, produzindo resultados incorretos ou erros como `#VALOR!`.

## Prompt ou Modelo Editável

```text
Tenho uma planilha de [descrever o tipo de base: clientes, alunos, produtos, colaboradores]
com os dados abaixo. Faça um diagnóstico completo de qualidade: identifique campos
vazios, formatos inconsistentes, duplicatas e qualquer outro problema que possa
atrapalhar uma análise. Liste os problemas em ordem de prioridade e explique cada
um em uma linha.

[Colar aqui os dados copiados do Excel — cabeçalho + linhas de dados]
```

## Fechamento do Módulo

Neste módulo, o participante produziu a aba `Clientes` — a base de dados central do curso — e utilizou o Claude para realizar um diagnóstico estruturado de qualidade. Os problemas identificados (duplicata, campo vazio, formatos inconsistentes, valor numérico armazenado como texto) serão corrigidos progressivamente ao longo dos módulos seguintes. No Módulo 2, a mesma planilha será ampliada com uma segunda aba de vendas, e o participante aprenderá a cruzar as duas tabelas por meio de funções de busca.

<div style="page-break-after: always;"></div>

# Módulo 2 — Cruzamento de Tabelas com Funções de Busca

## Encadeamento

A partir da aba `Clientes` construída no Módulo 1, o participante cria uma segunda aba (`Vendas`) e aprende a cruzar as duas tabelas utilizando funções de busca adequadas à versão do Excel disponível.

## Finalidade prática

Neste módulo, o participante criará a aba `Vendas` no arquivo `treino_claude.xlsx` e utilizará o Claude para obter a fórmula correta de cruzamento de tabelas — `XLOOKUP` para o Excel 365 ou `PROCV com IFERROR` para o Excel 2019. O produto parcial é a coluna `Nome_Cliente` preenchida automaticamente na aba `Vendas`, incluindo o tratamento de um ID inexistente na aba `Clientes`.

## Objetivos de Aprendizagem Prática

Ao final deste módulo, o participante deverá ser capaz de:

1. Criar uma nova aba no Excel e inserir dados tabulares de vendas a partir de um modelo fornecido.
2. Formular um prompt ao Claude especificando a estrutura das duas tabelas, o campo de cruzamento e a versão do Excel, de modo a obter a fórmula adequada.
3. Aplicar `XLOOKUP` ou `PROCV com IFERROR` na célula E2 da aba `Vendas` e copiar a fórmula para as demais linhas utilizando o recurso de alça de preenchimento.
4. Verificar o resultado da fórmula para IDs existentes e não existentes na tabela de origem.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 2.1 | Abertura do módulo | Título, objetivo e produto parcial esperado | Imagem: duas abas do Excel com seta de cruzamento entre elas |
| 2.2 | Texto curto explicativo | Por que o cruzamento de tabelas é uma necessidade recorrente; diferença entre PROCV e XLOOKUP em uma frase cada | Nenhum |
| 2.3 | Tabs (Rise 360) | Três abas: "PROCV", "XLOOKUP", "ÍNDICE/CORRESP" — cada aba com sintaxe, caso de uso e limitação principal | Diagrama de sintaxe para cada função |
| 2.4 | Captura de tela anotada | Aba `Vendas` com os dados inseridos e a célula E1 com o cabeçalho `Nome_Cliente` em destaque | Captura anotada indicando onde a fórmula será inserida (E2) |
| 2.5 | Demonstração passo a passo | Passos para formular o prompt no Claude e aplicar a fórmula recebida | Captura de tela do Claude com o prompt enviado e a fórmula recebida em destaque |
| 2.6 | Captura de tela anotada | Aba `Vendas` com a coluna E preenchida, destacando a linha do ID 107 com "Não encontrado" | Captura anotada com balão explicativo na linha do ID inexistente |
| 2.7 | Atividade guiada | O participante executa os passos e preenche a coluna E na própria máquina | Nenhum (atividade offline) |
| 2.8 | Knowledge check | Verdadeiro ou falso: "O XLOOKUP exige que a coluna de busca seja sempre a primeira coluna da tabela" | Bloco Storyline 360 com feedback |
| 2.9 | Checklist | Verificação do produto parcial (aba `Vendas` criada, fórmula aplicada, ID 107 com "Não encontrado") | Checklist interativo do Rise 360 |
| 2.10 | Fechamento do módulo | Resumo e anúncio do próximo módulo | Nenhum |

## Conteúdo Instrucional Enxuto

O cruzamento de tabelas é uma das operações mais frequentes em planilhas de trabalho: dado um identificador em uma tabela (por exemplo, o ID de um cliente na aba `Vendas`), busca-se uma informação correspondente em outra tabela (o nome desse cliente na aba `Clientes`). Esse processo é equivalente ao que, em bancos de dados relacionais, denomina-se "junção" (join) entre tabelas.

O Excel oferece três abordagens principais para esse tipo de operação. O `PROCV` (ou `VLOOKUP` na versão em inglês) é a função mais conhecida e amplamente compatível, mas apresenta limitações: só busca valores à direita da coluna de referência e é sensível à inserção de novas colunas. O `XLOOKUP` (disponível no Excel 365 e 2021 em diante) resolve essas limitações: permite busca em qualquer direção, aceita arrays de retorno e incorpora nativamente o tratamento do caso "não encontrado". A combinação `ÍNDICE/CORRESP` é a mais flexível, mas também a mais complexa — indicada para buscas com múltiplas condições simultâneas, tema que está além do escopo deste módulo.

Neste módulo, o participante solicitará ao Claude a fórmula adequada à versão do Excel que utiliza. A prática de informar a versão ao Claude no prompt é essencial: o `XLOOKUP` não existe no Excel 2019, e uma fórmula sugerida para a versão errada simplesmente não funcionará. Esse é um exemplo de como o contexto fornecido ao Claude determina diretamente a utilidade da resposta recebida.

Um detalhe importante a observar: a tabela `Vendas` contém intencionalmente um ID (107) que não existe na aba `Clientes`. O participante deve verificar que a fórmula retorna "Não encontrado" nessa linha — confirmando que o tratamento de erro está funcionando corretamente. Esse comportamento não é uma falha da fórmula; é exatamente o que se espera de uma fórmula bem construída diante de dados incompletos.

## Demonstração Guiada

1. Abrir o arquivo `treino_claude.xlsx` e clicar no "+" para adicionar uma nova aba; renomeá-la para `Vendas`.
2. Inserir os dados de vendas fornecidos (6 linhas + cabeçalho) a partir da célula A1; digitar `Nome_Cliente` na célula E1.
3. Abrir o claude.ai e formular o prompt de cruzamento, especificando: nome das abas, colunas de cada tabela, campo de cruzamento (ID / ID_Cliente) e versão do Excel.
4. Copiar a fórmula recebida do Claude, voltar ao Excel, clicar em E2 e colar.
5. Pressionar Enter; posicionar o cursor no canto inferior direito de E2 até aparecer o cursor de preenchimento ("+") e arrastar até E7.
6. Verificar o resultado: IDs 101, 103 e 105 devem exibir os nomes correspondentes; ID 107 deve exibir "Não encontrado".
7. Retornar ao Claude e perguntar por que o ID 107 retornou "Não encontrado"; ler a explicação.

Captura de tela recomendada (tela 2.4): aba `Vendas` com todos os dados inseridos e a célula E1 contendo o cabeçalho `Nome_Cliente`, com a célula E2 vazia em destaque e uma seta indicando onde a fórmula será inserida.

Captura de tela recomendada (tela 2.6): aba `Vendas` com a coluna E completamente preenchida; a linha do ID 107 deve estar destacada (por exemplo, com borda colorida ou seta) exibindo o texto "Não encontrado", com um balão explicativo ao lado.

## Atividade Hands-on

### Atividade prática — Cruzar a aba Vendas com a aba Clientes (20 minutos)

**Tarefa:** Criar a aba `Vendas` no arquivo `treino_claude.xlsx`, formular o prompt de cruzamento no Claude, aplicar a fórmula recebida na coluna E e verificar o resultado para todos os IDs, incluindo o ID inexistente.

**Procedimento:**

1. Abrir o arquivo `treino_claude.xlsx`; criar a aba `Vendas` e inserir os seis registros de vendas fornecidos no roteiro, incluindo o cabeçalho na linha 1.
2. Digitar `Nome_Cliente` na célula E1.
3. Abrir o claude.ai (nova conversa ou a mesma do Módulo 1) e enviar o prompt de cruzamento, informando as colunas de cada aba e a versão do Excel.
4. Copiar a fórmula sugerida pelo Claude; voltar ao Excel e colá-la na célula E2; pressionar Enter.
5. Arrastar a alça de preenchimento de E2 até E7 para aplicar a fórmula em todas as linhas.
6. Verificar os resultados: confirmar que os IDs existentes exibem o nome correto e que o ID 107 exibe "Não encontrado".
7. Retornar ao Claude no mesmo chat e perguntar por que o ID 107 não foi encontrado; ler a resposta.

**Produto parcial esperado:** Aba `Vendas` com a coluna `Nome_Cliente` (E) preenchida por fórmula para todos os seis registros, com "Não encontrado" na linha do ID 107.

**Critério de êxito:** A coluna E deve exibir nomes corretos para os IDs 101, 103 e 105 (com possíveis variações de capitalização conforme digitado na aba `Clientes`) e a mensagem de tratamento de erro na linha do ID 107. A fórmula deve atualizar automaticamente se um valor na aba `Clientes` for alterado.

## Checkpoint de Aprendizagem

**Tipo:** Verdadeiro ou falso

**Enunciado 1:** O `XLOOKUP` exige que a coluna de busca seja sempre a primeira coluna do intervalo de tabela informado.

**Gabarito:** Falso. O `XLOOKUP` permite que os arrays de busca e de retorno sejam especificados de forma independente, podendo a coluna de busca estar em qualquer posição — à esquerda ou à direita da coluna de retorno. Essa é uma das principais vantagens em relação ao `PROCV`.

**Enunciado 2:** Ao usar `IFERROR` envolvendo o `PROCV`, o valor especificado no segundo argumento do `IFERROR` será exibido sempre que o `PROCV` não encontrar o valor buscado.

**Gabarito:** Verdadeiro. O `IFERROR` captura qualquer erro gerado pela fórmula interna (incluindo o `#N/D` produzido pelo `PROCV` quando não há correspondência) e substitui esse erro pelo valor definido no segundo argumento, como a mensagem "Não encontrado".

## Prompt ou Modelo Editável

```text
Tenho duas abas no Excel:

Aba "[nome da aba 1]" (colunas [especificar]): [listar nomes das colunas]

Aba "[nome da aba 2]" (colunas [especificar]): [listar nomes das colunas]

Quero trazer [nome do dado desejado] da aba "[aba de origem]" para a coluna [letra]
da aba "[aba de destino]", cruzando pelo campo [nome do campo comum às duas abas].

Meu Excel é o [versão: 2019 / Microsoft 365 / outro].

Me dê a fórmula pronta para a célula [referência], com tratamento para quando
o valor não existir na aba de origem.
```

## Fechamento do Módulo

Neste módulo, o participante criou a aba `Vendas` e estabeleceu um vínculo dinâmico entre as duas tabelas por meio de uma função de busca. A coluna `Nome_Cliente` é atualizada automaticamente sempre que os dados da aba `Clientes` forem alterados. No Módulo 3, o participante retornará à aba `Clientes` para adicionar uma coluna de classificação automática baseada em regras de negócio com múltiplas condições.

<div style="page-break-after: always;"></div>

# Módulo 3 — Classificação Automatizada por Regras de Negócio

## Encadeamento

Com a aba `Clientes` construída no Módulo 1 e a aba `Vendas` integrada no Módulo 2, o participante retorna à aba `Clientes` para adicionar uma camada de inteligência: a classificação automática de cada registro por regras de negócio definidas pelo gestor.

## Finalidade prática

Neste módulo, o participante utilizará o Claude para construir uma fórmula de lógica condicional com `IFS` (ou `SE encadeado` para Excel 2019) que classifique cada cliente em "Premium", "Padrão", "Em risco" ou "Cancelado", com base em regras que combinam o campo `Receita` e o campo `Status`. O produto parcial é a coluna `Classificação` (G) na aba `Clientes`, preenchida por fórmula com quatro categorias possíveis.

## Objetivos de Aprendizagem Prática

Ao final deste módulo, o participante deverá ser capaz de:

1. Corrigir um valor numérico armazenado como texto no Excel antes de aplicar uma fórmula condicional.
2. Formular um prompt ao Claude descrevendo regras de negócio com múltiplas condições e solicitar as versões `IFS` e `SE encadeado` para comparação.
3. Aplicar a fórmula `IFS` na coluna G da aba `Clientes` e validar os resultados com casos de teste deliberados (alteração temporária de valores).
4. Refinar a fórmula existente para incorporar uma condição adicional de prioridade, utilizando a função de acompanhamento no chat do Claude.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 3.1 | Abertura do módulo | Título, objetivo e produto parcial esperado | Imagem: coluna G da planilha com rótulos coloridos "Premium", "Padrão", "Em risco" |
| 3.2 | Texto curto explicativo | Diferença prática entre `SE encadeado`, `IFS` e `SWITCH` em um parágrafo por função | Tabela comparativa: Função / Melhor uso / Versão mínima |
| 3.3 | Accordion (Rise 360) | Três seções expansíveis: "SE encadeado", "IFS", "SWITCH" — cada uma com exemplo de sintaxe | Fragmentos de fórmula formatados em bloco de texto |
| 3.4 | Captura de tela anotada | Aba `Clientes` com a célula E6 contendo "R$ 33.000" destacada, indicando a necessidade de correção antes da fórmula | Captura com balão de aviso sobre o valor em formato texto |
| 3.5 | Process block (Rise 360) | Sequência: Corrigir E6 → Criar cabeçalho G1 → Formular prompt → Aplicar IFS em G2 → Arrastar → Testar → Refinar | Setas ou numeração sequencial |
| 3.6 | Demonstração passo a passo | Passos para corrigir o valor, formular o prompt e aplicar a fórmula | Captura de tela do Claude com o prompt de classificação enviado e a fórmula IFS recebida |
| 3.7 | Captura de tela anotada | Aba `Clientes` com a coluna G preenchida; linha da Diana (Status=Inativo) mostrando "Cancelado" | Captura anotada com seta para a linha que recebeu "Cancelado" pela condição de Status |
| 3.8 | Atividade guiada | O participante executa todos os passos e valida com teste de alteração temporária | Nenhum (atividade offline) |
| 3.9 | Knowledge check | Associação: relacionar cada função (SE, IFS, SWITCH) ao seu melhor caso de uso | Bloco Storyline 360 de associação com feedback |
| 3.10 | Checklist | Verificação do produto parcial (coluna G preenchida, "Cancelado" na linha da Diana, teste de alteração realizado) | Checklist interativo do Rise 360 |
| 3.11 | Fechamento do módulo | Resumo e anúncio do próximo módulo | Nenhum |

## Conteúdo Instrucional Enxuto

A lógica condicional é o mecanismo pelo qual o Excel toma decisões automaticamente com base no conteúdo de uma célula. A função `SE` avalia uma condição e retorna um valor se ela for verdadeira e outro se for falsa. Quando há mais de duas categorias possíveis, é necessário encadear múltiplos `SE` — o que torna a fórmula progressivamente difícil de ler e manter. A função `IFS`, disponível no Excel 365 e Excel 2019 em diante, resolve esse problema ao permitir a listagem de pares condição–resultado sem aninhamento, tornando a lógica linear e transparente.

Antes de aplicar qualquer fórmula numérica, é essencial garantir que os valores na coluna de referência sejam de fato números e não texto. Quando uma célula contém "R$ 33.000", o Excel a trata como sequência de caracteres, e comparações numéricas como `E2>=50000` retornam `FALSO` mesmo que o valor aparente seja maior que 50.000. A correção é simples: apagar o conteúdo e redigitar apenas o número puro (33000), sem símbolo de moeda, sem pontos como separadores de milhar.

Neste módulo, as regras de negócio têm dois níveis de prioridade: primeiro, verifica-se o campo `Status` — clientes com status "Inativo" recebem automaticamente a classificação "Cancelado", independentemente da receita. Em seguida, para os demais, a classificação depende do valor da receita. Esse tipo de lógica hierárquica é muito comum em contextos reais e ilustra por que a ordem das condições no `IFS` importa: a condição mais prioritária deve ser listada primeiro.

## Demonstração Guiada

1. Abrir a aba `Clientes` do arquivo `treino_claude.xlsx`; clicar em E6 e verificar que o conteúdo é "R$ 33.000" (texto).
2. Apagar o conteúdo de E6 e redigitar `33000` (número puro); pressionar Enter.
3. Clicar em G1 e digitar `Classificação`; clicar em G2.
4. Abrir o claude.ai e formular o prompt de classificação com as regras de negócio (receita e status).
5. Copiar a fórmula `IFS` recebida do Claude; colá-la em G2; pressionar Enter.
6. Arrastar a alça de preenchimento de G2 até G7 para aplicar em todas as linhas.
7. Verificar os resultados: Carlos Lima (62.000, Ativo) = "Premium"; Eduardo Rocha (33.000, Ativo) = "Padrão"; Diana (15.000, Inativo) = "Cancelado".
8. Alterar temporariamente E3 para 20.000; verificar que G3 muda para "Em risco"; desfazer com Ctrl+Z.
9. Retornar ao Claude no mesmo chat e solicitar a fórmula atualizada com a condição de prioridade para "Inativo" → "Cancelado"; aplicar em G2 e copiar para as demais linhas.

Captura de tela recomendada (tela 3.4): célula E6 da aba `Clientes` selecionada, exibindo o conteúdo "R$ 33.000" na barra de fórmulas — com um balão de aviso sobreposto explicando que esse valor será tratado como texto pelo Excel, impedindo comparações numéricas.

Captura de tela recomendada (tela 3.7): aba `Clientes` com a coluna G totalmente preenchida, exibindo "Premium", "Padrão", "Em risco" e "Cancelado" nas linhas correspondentes. A linha da Diana (ID 104) deve estar destacada com seta indicando "Cancelado" pela condição de Status = "Inativo".

## Atividade Hands-on

### Atividade prática — Criar a coluna de classificação automatizada (20 minutos)

**Tarefa:** Corrigir o valor numérico em formato texto na aba `Clientes`, formular o prompt de classificação no Claude, aplicar a fórmula `IFS` na coluna G, validar com teste de alteração e refinar a fórmula para incluir a condição de prioridade "Cancelado".

**Procedimento:**

1. Abrir a aba `Clientes`; clicar em E6, apagar o conteúdo e redigitar `33000` (número puro sem R$ nem ponto); pressionar Enter.
2. Clicar em G1 e digitar `Classificação`.
3. Abrir o claude.ai e enviar o prompt de classificação com as regras de receita (três faixas: ≥50.000, ≥25.000, <25.000), solicitando as versões IFS e SE encadeado.
4. Clicar em G2, colar a fórmula IFS recebida e pressionar Enter; arrastar a alça até G7.
5. Verificar: Carlos Lima = "Premium"; Bruno Santos e Eduardo Rocha = "Padrão"; Diana = "Em risco" (ainda sem a condição de Status).
6. Alterar temporariamente E3 (Carlos Lima) para 20.000; confirmar que G3 muda para "Em risco"; desfazer com Ctrl+Z.
7. Retornar ao Claude e solicitar a versão da fórmula com a condição adicional: Status = "Inativo" → "Cancelado" com prioridade máxima.
8. Atualizar G2 com a nova fórmula; arrastar até G7; verificar que Diana exibe "Cancelado".

**Produto parcial esperado:** Coluna G da aba `Clientes` preenchida com as classificações "Premium", "Padrão", "Em risco" e "Cancelado" para todos os registros, com a condição de Status funcionando corretamente.

**Critério de êxito:** A coluna G deve exibir "Cancelado" para todos os clientes com Status = "Inativo" (independentemente da receita), e as classificações por receita corretas para os demais. O teste de alteração temporária deve confirmar que a fórmula recalcula automaticamente ao mudar o valor de receita.

## Checkpoint de Aprendizagem

**Tipo:** Associação

Relacionar cada função à sua descrição de melhor caso de uso:

| Função | Melhor caso de uso |
|---|---|
| SE encadeado | a) Valores discretos e bem definidos, como códigos ou abreviações ("AT", "IN", "SUS") |
| IFS | b) Múltiplas condições com intervalos numéricos ou textuais; disponível a partir do Excel 2019 |
| SWITCH | c) Compatibilidade com versões antigas do Excel; até três condições sem exigir legibilidade avançada |

**Gabarito:** SE encadeado → c; IFS → b; SWITCH → a.

## Prompt ou Modelo Editável

```text
Tenho uma planilha Excel com as colunas:
- [coluna de referência numérica, ex.: E] = [nome da coluna, ex.: Receita]
- [coluna de referência textual, ex.: F] = [nome da coluna, ex.: Status]

Quero criar uma coluna [letra] chamada "[nome]" com as seguintes regras
(em ordem de prioridade):

1. Se [coluna F] for "[valor]" → "[classificação prioritária]"
2. Se [coluna E] for maior ou igual a [valor] → "[classificação A]"
3. Se [coluna E] for maior ou igual a [valor] → "[classificação B]"
4. Nos demais casos → "[classificação C]"

Me dê a fórmula usando IFS para a célula [referência].
Depois mostre a mesma lógica com SE encadeado para comparação.
```

## Fechamento do Módulo

Neste módulo, o participante adicionou à aba `Clientes` uma coluna de classificação que opera automaticamente sobre qualquer alteração nos campos de receita ou status. A coluna G será utilizada como referência nas fórmulas de contagem do Dashboard produzido no Módulo de Síntese. No Módulo 4, o participante abordará o problema da inconsistência nos nomes da mesma aba, aprendendo a padronizá-los com funções de texto combinadas.

<div style="page-break-after: always;"></div>

# Módulo 4 — Normalização de Campos de Texto

## Encadeamento

Com as colunas de busca e classificação consolidadas nos módulos anteriores, o participante retorna ao problema de qualidade identificado no Módulo 1 — a inconsistência de capitalização e espaços nos nomes — e o resolve definitivamente com funções de texto.

## Finalidade prática

Neste módulo, o participante expandirá a aba `Clientes` com três novos registros propositalmente mal formatados e utilizará o Claude para obter a fórmula combinada de `PRI.MAIÚSCULA` e `TIRAR.ESPAÇOS`. Após aplicar a fórmula na coluna H, o participante converterá os resultados em valores fixos por meio do recurso Colar Especial, eliminando a dependência das fórmulas originais. O produto parcial é a coluna `Nome_Limpo` (H) com todos os nomes padronizados e convertidos em texto estático.

## Objetivos de Aprendizagem Prática

Ao final deste módulo, o participante deverá ser capaz de:

1. Inserir novos registros com erros de formatação de texto (caixa alta, caixa baixa, espaços extras) em uma aba existente do Excel.
2. Formular um prompt ao Claude descrevendo os três tipos de problema de texto e solicitando uma fórmula única que corrija todos simultaneamente.
3. Aplicar a fórmula `PRI.MAIÚSCULA(TIRAR.ESPAÇOS(...))` na coluna H e copiar para todos os registros.
4. Converter as fórmulas da coluna H em valores fixos utilizando o recurso Colar Especial → Valores.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 4.1 | Abertura do módulo | Título, objetivo e produto parcial esperado | Imagem: coluna B com nomes bagunçados ao lado da coluna H com nomes padronizados |
| 4.2 | Texto curto explicativo | Explicação de como funções aninhadas funcionam de dentro para fora (analogia: descascar camadas) | Diagrama de seta: texto bruto → TIRAR.ESPAÇOS → PRI.MAIÚSCULA → resultado final |
| 4.3 | Labeled graphic (Rise 360) | Imagem do Excel com três células anotadas: nome em CAIXA ALTA, em minúsculas e com espaço duplo — cada uma com balão explicando o problema | Captura de tela da aba `Clientes` com balões sobrepostos |
| 4.4 | Demonstração passo a passo | Passos para inserir os novos registros, formular o prompt e aplicar a fórmula | Captura de tela da fórmula na barra de fórmulas do Excel (célula H2 selecionada) |
| 4.5 | Captura de tela anotada | Coluna B (original, com erros) e coluna H (limpa) lado a lado, com setas de comparação | Captura antes/depois com setas de correspondência entre as linhas |
| 4.6 | Process block (Rise 360) | Sequência: Selecionar H2:H9 → Copiar → Clicar com botão direito em H2 → Colar Especial → Valores → Confirmar | Ícones de passo a passo com capturas parciais de menu |
| 4.7 | Captura de tela anotada | Menu "Colar Especial" do Excel com a opção "Valores" em destaque | Captura do menu contextual com a opção destacada em amarelo ou com seta |
| 4.8 | Atividade guiada | O participante executa todos os passos, inclusive a conversão em valores | Nenhum (atividade offline) |
| 4.9 | Knowledge check | Múltipla escolha: por que converter fórmulas em valores fixos antes de apagar a coluna original? | Bloco Storyline 360 com feedback |
| 4.10 | Checklist | Verificação do produto parcial (coluna H com nomes padronizados, fórmulas convertidas em valores) | Checklist interativo do Rise 360 |
| 4.11 | Fechamento do módulo | Resumo e anúncio do módulo de síntese | Nenhum |

## Conteúdo Instrucional Enxuto

A inconsistência de capitalização em campos de texto é um dos problemas mais comuns em bases de dados exportadas de sistemas legados ou preenchidas manualmente por múltiplos usuários. Quando os mesmos nomes aparecem como "ANA SILVA", "ana silva" e "Ana Silva" na mesma coluna, filtros, tabelas dinâmicas e fórmulas de contagem tratam cada variação como um registro distinto — produzindo contagens incorretas e relatórios imprecisos.

O Excel oferece duas funções de texto diretamente úteis para esse problema. `TIRAR.ESPAÇOS` (ou `TRIM` na versão em inglês) remove todos os espaços em excesso no início, no final e entre palavras de uma célula de texto, preservando apenas um espaço simples entre palavras. `PRI.MAIÚSCULA` (ou `PROPER`) converte o texto para o padrão de capitalização de nomes próprios, com a primeira letra de cada palavra em maiúscula e as demais em minúscula. Combinadas — com `TIRAR.ESPAÇOS` como função interna e `PRI.MAIÚSCULA` como função externa —, as duas resolvem simultaneamente os três tipos de problema identificados neste módulo.

A conversão de fórmulas em valores fixos por meio do recurso Colar Especial → Valores é um passo essencial quando o objetivo é preservar os resultados sem depender das células de origem. Se a coluna B (com os nomes originais) for apagada e a coluna H ainda contiver fórmulas que referenciam B, todos os resultados da coluna H desaparecerão. Ao converter para valores fixos antes de apagar a coluna original, o participante garante que os dados limpos persistam de forma independente.

## Demonstração Guiada

1. Abrir a aba `Clientes` do arquivo `treino_claude.xlsx`; adicionar três novos registros nas linhas 8, 9 e 10 com os dados fornecidos no roteiro (Fernanda Lima em caixa alta com espaços, João Pedro Silva em minúsculas, Marcos Oliveira com espaço duplo).
2. Clicar na célula H1 e digitar `Nome_Limpo`.
3. Abrir o claude.ai e formular o prompt descrevendo os três tipos de problema de capitalização e espaço, solicitando fórmula única para a coluna H.
4. Copiar a fórmula recebida (`=PRI.MAIÚSCULA(TIRAR.ESPAÇOS(B2))` ou `=PROPER(TRIM(B2))`); clicar em H2 no Excel e colar; pressionar Enter.
5. Arrastar a alça de preenchimento de H2 até H9 (ou H10, conforme os dados inseridos); verificar os resultados linha a linha.
6. Retornar ao Claude e perguntar sobre a limitação da função quanto a abreviações como "Dra." e "Sr."; ler a resposta.
7. Selecionar H2:H9; copiar (Ctrl+C); clicar com botão direito em H2; selecionar "Colar Especial" → "Valores"; confirmar.
8. Verificar que as células H2:H9 agora contêm texto estático (a barra de fórmulas exibe o texto, não a fórmula).

Captura de tela recomendada (tela 4.5): duas colunas visíveis lado a lado — coluna B (com os nomes originais, incluindo "FERNANDA LIMA", "joão pedro silva" e "Marcos  Oliveira") e coluna H (com os nomes padronizados "Fernanda Lima", "João Pedro Silva" e "Marcos Oliveira") — com setas horizontais conectando cada par de células para evidenciar a transformação.

Captura de tela recomendada (tela 4.7): menu contextual do Excel aberto após clicar com botão direito em H2, com a opção "Colar Especial" expandida ou destacada, e o submenu ou janela de Colar Especial exibindo o botão ou opção "Valores" em destaque.

## Atividade Hands-on

### Atividade prática — Normalizar os nomes da aba Clientes (20 minutos)

**Tarefa:** Adicionar três novos registros com nomes mal formatados à aba `Clientes`, formular o prompt no Claude, aplicar a fórmula combinada na coluna H, verificar os resultados e converter as fórmulas em valores fixos com Colar Especial.

**Procedimento:**

1. Abrir a aba `Clientes` e inserir os três novos registros nas linhas 8, 9 e 10, conforme o modelo fornecido no roteiro (incluindo os espaços extras e variações de capitalização intencionais).
2. Clicar em H1 e digitar `Nome_Limpo`.
3. Abrir o claude.ai e enviar o prompt descrevendo os três tipos de problema (caixa alta, minúsculas, espaços extras), solicitando fórmula única e explicação de cada função.
4. Colar a fórmula recebida em H2; arrastar a alça até a última linha com dados.
5. Verificar cada resultado linha a linha: "Ana Silva", "Bruno Santos", "Carlos Lima", "Fernanda Lima", "João Pedro Silva", "Marcos Oliveira" (sem espaços extras).
6. Retornar ao Claude e perguntar sobre a limitação quanto a abreviações; registrar a resposta.
7. Selecionar H2 até a última linha preenchida; copiar (Ctrl+C); clicar com botão direito em H2; selecionar Colar Especial → Valores; confirmar.
8. Verificar que a barra de fórmulas de H2 exibe texto estático, não a fórmula.

**Produto parcial esperado:** Coluna `Nome_Limpo` (H) na aba `Clientes` com todos os nomes padronizados em formato "Primeira Letra Maiúscula" e sem espaços extras, convertidos em valores fixos.

**Critério de êxito:** Todas as células da coluna H devem conter texto estático (verificável pela barra de fórmulas). Os nomes "FERNANDA LIMA", "joão pedro silva" e "Marcos  Oliveira" devem ter sido transformados em "Fernanda Lima", "João Pedro Silva" e "Marcos Oliveira", respectivamente. A coluna H não deve depender da coluna B para exibir os dados — o que pode ser verificado apagando temporariamente B2 e confirmando que H2 permanece inalterada.

## Checkpoint de Aprendizagem

**Tipo:** Múltipla escolha

**Enunciado:** Após aplicar a fórmula `=PRI.MAIÚSCULA(TIRAR.ESPAÇOS(B2))` na coluna H e verificar que os resultados estão corretos, o participante decide apagar a coluna B (com os nomes originais). O que acontece com os dados da coluna H se as fórmulas ainda não tiverem sido convertidas em valores fixos?

a) Os dados da coluna H permanecem inalterados, pois a fórmula já calculou o resultado.
b) Os dados da coluna H exibem o erro `#REF!`, porque a fórmula referencia células que foram apagadas.
c) Os dados da coluna H são automaticamente convertidos em texto estático pelo Excel.
d) O Excel impede a exclusão da coluna B enquanto houver fórmulas que a referenciam.

**Gabarito:** Alternativa b.

**Fundamentação:** Fórmulas do Excel referenciam células por posição. Ao apagar a coluna B, as referências `B2`, `B3` etc. tornam-se inválidas e o Excel exibe o erro `#REF!` em todas as células que as utilizavam. A conversão em valores fixos por Colar Especial → Valores elimina essa dependência, tornando os dados da coluna H independentes da coluna de origem.

## Prompt ou Modelo Editável

```text
Tenho uma coluna de [tipo de dado: nomes, endereços, categorias] no Excel com
três tipos de problema:

1. Valores em CAIXA ALTA (ex.: "[exemplo]")
2. Valores em minúsculas (ex.: "[exemplo]")
3. Espaços extras no início, no fim ou entre palavras (ex.: "[exemplo]")

Quero uma fórmula única na coluna [letra] que corrija os três problemas de uma
vez e deixe o resultado com a primeira letra de cada palavra em maiúscula.

Me explique cada função usada e em que ordem elas são executadas.

Versão do Excel: [versão].
```

## Fechamento do Módulo

Neste módulo, o participante resolveu o problema de inconsistência de capitalização e espaços identificado no diagnóstico do Módulo 1, produzindo a coluna `Nome_Limpo` como dado padronizado e independente. O arquivo `treino_claude.xlsx` conta agora com quatro abas funcionais e colunas geradas por fórmula obtidas com o auxílio do Claude. No Módulo de Síntese, esses elementos serão integrados na construção de um Dashboard de análise de clientes.

<div style="page-break-after: always;"></div>

# Módulo 5 — Síntese e Aplicação Integrada

## Finalidade da Síntese

Este módulo reúne os produtos parciais dos quatro módulos anteriores — a aba `Clientes` com classificação e nomes padronizados, e a aba `Vendas` com o cruzamento de tabelas — em uma entrega final: a aba `Dashboard`, que consolida os principais indicadores da base em um painel de análise funcional e dinamicamente vinculado às abas de origem.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 5.1 | Abertura do módulo | Título da síntese, produto final e tempo estimado | Imagem: aba `Dashboard` com os cinco indicadores preenchidos e o ranking de clientes |
| 5.2 | Texto curto explicativo | O que é o Dashboard neste contexto e como ele se conecta às abas anteriores | Diagrama: setas de `Clientes` e `Vendas` apontando para `Dashboard` |
| 5.3 | Process block (Rise 360) | Sequência da atividade integradora: criar aba → inserir etiquetas → formular prompt → aplicar fórmulas → formatar → validar com teste | Ícones de etapa numerados |
| 5.4 | Demonstração passo a passo | Passos completos para criar a aba `Dashboard` com os cinco indicadores | Captura de tela da aba `Dashboard` com os indicadores preenchidos e formatados |
| 5.5 | Captura de tela anotada | Aba `Dashboard` completa, com setas indicando quais fórmulas referenciam a aba `Clientes` | Captura anotada com balões explicativos |
| 5.6 | Captura de tela anotada | Teste de validação: valor alterado na aba `Clientes` e Dashboard atualizado automaticamente | Captura antes/depois ou duas capturas sequenciais com destaque na célula alterada |
| 5.7 | Atividade integradora | O participante executa a construção completa do Dashboard na própria máquina | Nenhum (atividade offline) |
| 5.8 | Checklist final | Lista marcável com os oito critérios de conclusão do produto final | Bloco de checklist interativo do Rise 360 |
| 5.9 | Encerramento | Parágrafo de conclusão e indicação de próximos passos | Nenhum |

## Atividade Integradora

### Atividade integradora — Construir a aba Dashboard (10 minutos)

**Tarefa:** Criar a aba `Dashboard` no arquivo `treino_claude.xlsx` com cinco indicadores de resumo (total de clientes, receita total, receita média, contagem de Premium e contagem de Em risco) e um ranking dos três clientes com maior receita, utilizando o Claude para obter as fórmulas e validando o resultado com um teste de alteração dinâmica.

**Procedimento:**

1. Recuperar o arquivo `treino_claude.xlsx` com as abas `Clientes` e `Vendas` produzidas nos módulos anteriores; verificar se a coluna G (`Classificação`) está corretamente preenchida e se a coluna E (Receita) contém apenas valores numéricos.
2. Criar uma nova aba e renomeá-la `Dashboard`; inserir os cabeçalhos `Indicador` (A1) e `Valor` (B1); preencher A2:A6 com os rótulos dos cinco indicadores.
3. Abrir o claude.ai e enviar o prompt de solicitação de fórmulas para os cinco indicadores, descrevendo a estrutura da aba `Clientes` (colunas A a G, linhas 2 a 9) e os valores esperados de cada fórmula.
4. Aplicar cada fórmula recebida nas células B2 a B6, respectivamente; formatar B3 e B4 como moeda e B2, B5, B6 como número inteiro.
5. Adicionar o cabeçalho `Top Clientes por Receita` em D1, com `Nome` em D2 e `Receita` em E2; solicitar ao Claude a abordagem para trazer os três maiores valores da coluna E da aba `Clientes` com os nomes correspondentes; aplicar nas células D3:E5.
6. Testar a dinamicidade: alterar temporariamente um valor de receita na aba `Clientes` e verificar que os indicadores do Dashboard atualizam automaticamente; desfazer a alteração (Ctrl+Z).
7. Salvar o arquivo.

**Produto final esperado:** Arquivo `treino_claude.xlsx` com quatro abas funcionais (`Clientes`, `Vendas`, e as abas de diagnóstico e classificação consolidadas) e a aba `Dashboard` exibindo cinco indicadores calculados por fórmulas dinâmicas e um ranking dos três melhores clientes.

## Critérios de Avaliação

| Critério | Descrição | Atendido? |
|---|---|---|
| **Clareza da entrega** | A aba `Dashboard` contém cabeçalhos legíveis e valores formatados corretamente (moeda para receita, inteiro para contagens) | ☐ Sim / ☐ Não |
| **Completude** | Todos os cinco indicadores estão preenchidos e o ranking de três clientes está presente | ☐ Sim / ☐ Não |
| **Aplicabilidade** | As fórmulas referenciam corretamente as abas `Clientes` e atualizam automaticamente ao alterar os dados de origem | ☐ Sim / ☐ Não |
| **Coerência** | Os valores do Dashboard são coerentes com os dados da aba `Clientes` (ex.: receita total coincide com a soma manual dos valores) | ☐ Sim / ☐ Não |
| **Revisão final** | O participante realizou o teste de alteração dinâmica e desfez a alteração; os dados estão nos valores originais | ☐ Sim / ☐ Não |
| **Uso do Claude** | Pelo menos uma fórmula foi obtida diretamente de um prompt estruturado no Claude e o participante é capaz de explicar o que ela faz | ☐ Sim / ☐ Não |
| **Produto acumulado** | O arquivo contém as abas `Clientes` (com colunas G e H preenchidas) e `Vendas` (com coluna E preenchida por fórmula de busca) | ☐ Sim / ☐ Não |
| **Independência operacional** | O participante é capaz de adaptar pelo menos um dos prompts utilizados para uma base de dados diferente da utilizada no curso | ☐ Sim / ☐ Não |

## Encerramento da Síntese

O Módulo de Síntese concluiu a construção do produto final do curso: um arquivo Excel com quatro abas integradas, produzido inteiramente pelo participante por meio da prática orientada, com o Claude atuando como fonte de fórmulas, diagnósticos e explicações técnicas em cada etapa. A competência prática consolidada não é apenas o domínio de funções específicas — é a capacidade de estruturar um problema analítico, formular uma consulta precisa ao Claude e validar o resultado antes de aplicá-lo em escala.

---

<div style="page-break-after: always;"></div>

# Orientações para Produção no Articulate 360

## Organização visual

- Utilizar blocos curtos e progressivos no Rise 360; cada tela deve conter uma única ação ou conceito central, sem acúmulo de informações em uma mesma tela.
- Evitar telas com mais de três parágrafos de texto corrido; preferir listas, checklists, process blocks e tabs para organizar o conteúdo.
- Inserir capturas de tela anotadas em todas as etapas que envolvam interação com interfaces (Excel, claude.ai, menus, barras de fórmulas); as anotações devem ser balões, setas ou bordas coloridas — nunca texto sobreposto sem destaque visual.
- Manter consistência visual entre módulos: mesma paleta de cores para boxes de atenção, mesmo estilo de setas em capturas de tela, mesma tipografia em diagramas de processo.
- Posicionar os checklists de produto parcial ao final de cada módulo, antes do fechamento, para que o participante confirme a conclusão antes de avançar.

## Interações recomendadas

- **Process blocks:** para sequências de ação com três ou mais etapas (ex.: passos para formular o prompt e aplicar a fórmula); recomendado nos módulos 1, 3 e 5.
- **Tabs:** para apresentar versões alternativas de uma mesma fórmula (ex.: `IFS` vs. `SE encadeado` vs. `SWITCH` no Módulo 3) ou comparações entre funções (Módulo 2).
- **Accordion:** para conteúdo complementar que o participante pode consultar conforme necessário, como definições de funções ou casos de uso avançados.
- **Knowledge checks (Storyline 360 embutido):** para os checkpoints de múltipla escolha e associação; usar o recurso de feedback imediato com texto explicativo para respostas corretas e incorretas.
- **Checklists (Rise 360):** para os critérios de produto parcial ao final de cada módulo e para o checklist final do Módulo de Síntese.
- **Labeled graphics:** para a tela 4.3, com a imagem da planilha anotada indicando os três tipos de problema de capitalização.
- **Download blocks:** para disponibilizar, ao final do curso, os modelos de prompt editáveis em formato `.txt` para que o participante os utilize em seu próprio contexto profissional.
- **Scenario blocks:** opcionais no Módulo 3, para apresentar situações de decisão (ex.: "A regra mudou — qual ajuste fazer na fórmula IFS?") com ramificação de resposta.

## Padrão de linguagem das telas

Cada tela deve conter:

- **Título curto:** máximo de oito palavras; orientado à ação ou ao resultado (ex.: "Aplicar a fórmula IFS na coluna G" ou "Resultado esperado: coluna com quatro categorias").
- **Instrução objetiva:** uma frase indicando o que o participante deve fazer ou observar nesta tela; iniciar com verbo no infinitivo ou imperativo ("Observe...", "Selecione...", "Verifique...").
- **Uma ação principal:** cada tela deve conduzir o participante a executar ou verificar uma única coisa; evitar telas que combinem explicação, demonstração e atividade simultaneamente.
- **Feedback imediato:** nos knowledge checks e checklists, exibir mensagem de confirmação (acerto) ou orientação corretiva (erro) logo após a resposta do participante, sem exigir navegação adicional.
- **Indicação clara de avanço:** ao final de cada tela com atividade ou checkpoint, exibir botão "Próximo" ou indicador de progresso visível, de modo que o participante saiba quando pode avançar para a tela seguinte.

---

## Encerramento

O presente roteiro instrucional orienta a produção de um curso hands-on completo no Articulate 360, estruturado em quatro módulos práticos e um módulo de síntese, com carga horária de 90 minutos. O produto final elaborado pelo participante — o arquivo `treino_claude.xlsx` com as abas `Clientes`, `Vendas` e `Dashboard` — é uma entrega concreta, verificável e imediatamente transferível para o contexto profissional ou acadêmico, pois as mesmas estruturas de prompt, fórmulas e processos de validação aprendidos durante o curso aplicam-se a qualquer base de dados com características análogas.

O aprofundamento natural após a conclusão deste curso inclui a exploração de recursos mais avançados do Excel — como fórmulas matriciais dinâmicas (`FILTRO`, `CLASSIFICAR`, `ÚNICA`), automação com macros VBA e transformação de dados em escala com Power Query — sempre com o Claude como parceiro técnico na geração e validação de soluções. O participante que dominar o ciclo de consultoria praticado neste curso — descrever o problema com precisão, solicitar ao Claude uma solução fundamentada, implementar em escopo reduzido, validar e escalar — estará habilitado a enfrentar qualquer desafio analítico no Excel com autonomia e método.

> **Síntese:** A competência prática mais valiosa deste curso não é nenhuma fórmula específica — é a capacidade de formular a pergunta certa ao parceiro certo, no momento certo.
