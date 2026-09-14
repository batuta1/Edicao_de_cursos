<link rel="stylesheet" href="../../.css/style.css">

# (Plano de Aula) Claude para Excel: Consultoria Analítica, Fórmulas Complexas e Automação — Curso Essentials

*Claude for Excel: Analytical Consulting, Complex Formulas and Automation — Curso Essentials*

---

## Identificação

| Campo | Definição |
|---|---|
| **Curso** | Claude para Excel: Consultoria Analítica, Fórmulas Complexas e Automação — Curso Essentials |
| **Natureza** | Autoinstrucional, assíncrono |
| **Carga horária** | 90 minutos (aproximadamente) |
| **Público-alvo** | Docentes do ensino superior iniciantes em inteligência artificial; analistas administrativos; alunos do ensino superior |
| **Pré-requisitos** | Conhecimento básico de Excel (identificar células, colunas e linhas); acesso a uma conta Claude (claude.ai) e ao Microsoft Excel (versão 2019 ou Microsoft 365) |
| **Recursos necessários** | Computador com Excel instalado (versão 2019 ou Microsoft 365); acesso à internet; navegador para acessar claude.ai; editor de texto para rascunho de prompts (opcional: Notepad, VS Code ou equivalente) |

---

### Objetivo Geral

O presente curso tem por finalidade capacitar o participante a utilizar o modelo de inteligência artificial Claude como consultor técnico especializado no contexto do Microsoft Excel, habilitando-o a estruturar perguntas analíticas com precisão, a solicitar e interpretar fórmulas de busca e lógica condicional complexas, a diagnosticar e tratar bases de dados com qualidade insatisfatória e, por fim, a identificar possibilidades de automação de tarefas repetitivas. Ao concluir o curso, espera-se que o participante seja capaz de aplicar de forma autônoma o fluxo de consultoria com IA — do diagnóstico à validação — em situações reais de sua área profissional ou acadêmica.

---

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Estruturar prompts analíticos para o Claude, discriminando contexto, objetivo, dados de exemplo e restrições, de modo a obter respostas técnicas adequadas e acionáveis.
2. Selecionar e aplicar as funções de busca (`PROCV`, `XLOOKUP`, `ÍNDICE/CORRESP`) e de lógica condicional (`SE`, `IFS`, `SWITCH`) mais adequadas a cada situação analítica no Excel.
3. Diagnosticar e tratar problemas de qualidade em bases de dados (campos vazios, formatos inconsistentes, duplicatas e anomalias) empregando Claude como orientador metodológico.
4. Avaliar criticamente as respostas geradas pelo Claude, identificando imprecisões, solicitando refinamentos por meio de perguntas de acompanhamento e validando resultados antes de implementá-los em escopo produtivo.

---

### Estrutura e Sequência dos Módulos

Os módulos estão organizados em progressão cumulativa: cada unidade pressupõe os conceitos introduzidos na anterior e os amplia, de modo que o participante transite gradualmente do entendimento do papel do Claude como ferramenta de consultoria para a aplicação prática de fórmulas e, em seguida, para o tratamento de dados. O Módulo de Síntese final articula todas as competências em uma atividade integradora.

| Módulo | Título | Referência (material-fonte) | Tempo estimado |
|---|---|---|---|
| 1 | Claude como Consultor Técnico: Fundamentos da Parceria Analítica | Módulo 1 — Aulas 1.1 e 1.2 | 20 min |
| 2 | Engenharia de Prompts: Como Estruturar Perguntas Analíticas | Módulo 2 — Aulas 2.1, 2.2 e 2.3 | 25 min |
| 3 | Fórmulas de Busca e Lógica Condicional no Excel | Módulo 3 — Aulas 3.1 e 3.2 | 25 min |
| 4 | Diagnóstico e Tratamento de Bases de Dados | Módulo 4 — Aulas 4.1, 4.2 e 4.3 | 10 min |
| 5 | Síntese e Aplicação Integrada | Todos os módulos anteriores | 10 min |

---

<div style="page-break-after: always;"></div>

# Módulo 1 — Claude como Consultor Técnico: Fundamentos da Parceria Analítica

> **Ponto de partida do curso.** Este módulo introduz o paradigma central que sustenta toda a trilha: o uso do Claude não como um buscador de respostas prontas, mas como consultor técnico que exige do interlocutor clareza de contexto e precisão de objetivos.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Descrever o papel do Claude como consultor técnico especializado no contexto do Excel, diferenciando-o do uso casual de assistentes de linguagem.
2. Identificar as situações em que acionar o Claude é mais produtivo do que tentar resolver o problema de forma independente (diagnóstico de erros, geração de fórmulas, automação).
3. Configurar o ambiente de trabalho básico — Excel e Claude abertos simultaneamente — e testar a comunicação inicial entre as duas ferramentas.
4. Aplicar o padrão de cinco etapas de consultoria (diagnóstico, exploração, implementação, validação, escalação) a um problema simples de planilha.

---

### Texto Descritivo

O Microsoft Excel é uma das ferramentas de análise de dados mais amplamente utilizadas em ambientes acadêmicos e administrativos. Contudo, um número expressivo de usuários permanece restrito a operações elementares — soma, filtro, cópia de fórmulas — por não dispor de suporte técnico especializado imediato. É precisamente nesse intervalo entre o problema e o especialista humano que modelos de linguagem de grande porte, como o Claude, podem atuar de forma relevante.

Convém esclarecer, desde o início, o que se entende por "consultor técnico" neste contexto. Um consultor técnico não apenas responde a perguntas; ele solicita informações adicionais quando o problema está mal definido, apresenta múltiplas abordagens possíveis com suas respectivas vantagens e limitações, e explica o raciocínio por trás de cada sugestão. O Claude opera de maneira análoga: quanto mais detalhado e estruturado for o pedido do usuário, mais precisa e útil será a resposta gerada. Essa dinâmica é fundamentalmente diferente de uma busca em mecanismo de pesquisa, em que a qualidade do resultado depende pouco da qualidade da pergunta.

Para ilustrar essa diferença por meio de analogia formal: consultar o Claude com uma pergunta vaga ("como analiso minha planilha?") equivale a procurar um médico e dizer apenas "não estou bem" — o profissional poderá oferecer orientações genéricas, mas não um diagnóstico preciso. Já uma pergunta detalhada ("tenho 10.000 registros de clientes com duplicatas por e-mail, quero manter apenas o registro mais antigo e gerar uma lista dos IDs removidos para auditoria") permite que o Claude apresente soluções concretas, justificadas e adaptadas ao cenário descrito.

O ambiente de trabalho recomendado consiste em manter o Excel e o Claude abertos lado a lado na mesma tela ou em monitores distintos. Essa disposição facilita o ciclo de consultoria: formular a dúvida no Claude, copiar a solução gerada, aplicá-la no Excel e retornar ao Claude para validação ou refinamento. O fluxo não é linear, mas iterativo — e a familiaridade com essa iteração constitui, em si, uma competência a ser desenvolvida ao longo deste curso.

Cumpre registrar que o Claude não é infalível. Erros ocorrem, especialmente quando o contexto fornecido é insuficiente ou quando a tarefa envolve lógicas muito específicas do ambiente do usuário (como versões antigas do Excel ou configurações regionais que alteram nomes de funções). Por essa razão, o ciclo de consultoria inclui, obrigatoriamente, uma etapa de validação: antes de aplicar qualquer solução em dados reais, recomenda-se testá-la em um subconjunto pequeno e controlado. Esse hábito de validação crítica será retomado e aprofundado no Módulo 2.

---

### Exercício Prático

**Atividade: Configurar o Ambiente e Realizar a Primeira Consulta** *(20 minutos)*

**Procedimento:**

1. Abra o Excel e crie uma planilha nova com os seguintes dados nas células A1 a C6 (incluindo cabeçalho):

   | ID | Nome | Receita |
   |---|---|---|
   | 101 | Ana Silva | 45000 |
   | 102 | Bruno Santos | 28000 |
   | 103 | Carlos Lima | 62000 |
   | 104 | Diana Costa | 15000 |
   | 105 | Eduardo Rocha | 33000 |

2. Acesse o Claude em claude.ai e abra uma nova conversa.

3. Copie a tabela acima (células A1 a C6) e cole-a no chat do Claude, acompanhada do seguinte texto:

   > "Tenho uma planilha com 5 clientes. Colunas: ID, Nome, Receita. Quero identificar quem está acima da receita média e classificar cada um como 'Acima da Média' ou 'Abaixo da Média'. Qual fórmula devo usar na coluna D?"

4. Leia a resposta do Claude atentamente. Observe se ele: (a) entendeu a estrutura dos dados; (b) sugeriu uma fórmula específica; (c) explicou o raciocínio da fórmula.

5. Implemente a fórmula sugerida na célula D2 e arraste-a até D6.

6. Verifique se os resultados são coerentes com os dados.

> 📸 *Sugestão de Captura de Tela:* Registre a janela do Claude com a resposta recebida ao lado da planilha do Excel com a fórmula aplicada na coluna D, para referência futura.

**Critério de êxito:** A coluna D deve exibir "Acima da Média" para Ana Silva (45.000), Carlos Lima (62.000) e Eduardo Rocha (33.000 — verificar se está acima ou abaixo da média calculada de 36.600) e "Abaixo da Média" para os demais. O participante deve ser capaz de explicar, com suas próprias palavras, o que a fórmula faz.

---

### Mão na massa

Utilize o modelo de prompt abaixo, substituindo os campos entre colchetes por informações do seu próprio contexto profissional ou acadêmico:

```
Tenho uma planilha chamada [nome da planilha] com [número aproximado] registros.
As colunas são: [listar os nomes das colunas].
O meu objetivo é: [descrever o que precisa fazer, por exemplo: calcular, classificar, comparar].
Qual é a fórmula ou abordagem mais adequada para esta tarefa no Excel?
```

---

<div style="page-break-after: always;"></div>

# Módulo 2 — Engenharia de Prompts: Como Estruturar Perguntas Analíticas

> **Pré-requisito: Módulo 1 concluído.** O foco desloca-se da compreensão do papel do Claude para a habilidade central que determina a qualidade de toda interação: a construção de um prompt bem estruturado.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Redigir um prompt estruturado contendo as seções Contexto, Dados, Objetivo, Restrições, Exemplo e Pergunta, adaptando-o ao tipo de análise requerido (descritiva, comparativa, diagnóstica ou preditiva).
2. Distinguir os quatro tipos de análise (descritiva, comparativa, preditiva e diagnóstica) e associar cada um ao padrão de prompt mais adequado.
3. Reconhecer respostas insuficientes, genéricas ou tecnicamente impraticáveis do Claude e utilizar perguntas de acompanhamento para refiná-las.
4. Aplicar um procedimento básico de validação manual antes de implementar em produção qualquer solução sugerida pelo Claude.

---

### Texto Descritivo

A qualidade de uma resposta gerada por um modelo de inteligência artificial é diretamente proporcional à qualidade do pedido que a originou. Esse princípio — amplamente documentado na literatura sobre interação humano-computador e sobre o design de sistemas de linguagem — pode ser sintetizado da seguinte forma: um modelo de linguagem não "lê nas entrelinhas"; ele interpreta literalmente o que lhe é fornecido. Quando o contexto está ausente, o modelo preenche as lacunas com suposições genéricas, o que resulta em respostas superficiais.

Para tornar essa lógica operacional, o material-fonte deste curso propõe uma estrutura de seis seções para qualquer prompt analítico: Contexto (o que é o projeto e por que importa), Dados (tamanho, fonte e período da base), Objetivo (o que se pretende obter), Restrições (limitações técnicas, operacionais ou legais), Exemplo (amostra real de dados com 5 a 10 linhas) e Pergunta (máximo de três a cinco questões específicas). Essa estrutura não é uma formalidade burocrática; é o equivalente de um briefing que um profissional entregaria a um consultor externo antes de uma reunião técnica.

Diferentes tipos de problemas analíticos exigem ênfases distintas dentro dessa estrutura. A análise descritiva — que responde à pergunta "o que aconteceu?" — beneficia-se de uma descrição detalhada das métricas desejadas (receita total, ticket médio, ranking). A análise comparativa — "como se comparam os grupos?" — requer que os grupos de comparação estejam claramente delimitados no prompt. A análise diagnóstica — "por quê isso ocorreu?" — demanda a descrição precisa da anomalia observada. E a análise preditiva ou de risco — "o que acontecerá?" ou "quem está em risco?" — pressupõe que o participante especifique as variáveis que suspeita serem relevantes, poupando ao Claude a necessidade de realizar suposições arbitrárias sobre o domínio do problema.

Cumpre também discutir o que fazer quando a resposta do Claude é insatisfatória. Três situações são recorrentes. A primeira é a resposta genérica, que ocorre quando o prompt carece de especificidade: a solução é reformular, acrescentando o dado que estava implícito. A segunda é o entendimento equivocado da estrutura dos dados: o Claude pode supor que se trata de uma operação de junção (join) de tabelas quando, na verdade, o participante deseja uma concatenação — nesse caso, uma descrição explícita da estrutura resolve o problema. A terceira situação é a resposta tecnicamente correta, porém impraticável: o Claude pode sugerir uma fórmula matricial de grande complexidade quando uma solução com colunas auxiliares seria mais legível e sustentável. Nesse caso, convém informar ao Claude a restrição de legibilidade e solicitar uma alternativa mais simples.

Depreende-se, portanto, que a interação com o Claude é um diálogo iterativo, não uma consulta de resposta única. O participante que internalizar essa dinâmica — e que desenvolver o hábito de validar manualmente qualquer solução antes de aplicá-la em produção — estará habilitado a extrair o máximo de valor da parceria com a inteligência artificial, independentemente do domínio analítico em que atua.

---

### Exercício Prático

**Atividade: Comparar Prompt Vago com Prompt Estruturado** *(25 minutos)*

Esta atividade consiste em uma questão de múltipla escolha precedida de um experimento prático.

**Parte 1 — Experimento (15 minutos):**

1. No Claude, envie o seguinte prompt vago: `"Tenho duplicatas na minha planilha. Como removo?"`
2. Leia a resposta e anote se ela é genérica ou específica.
3. Em seguida, envie o prompt estruturado abaixo no mesmo chat (ou em uma nova conversa):

```
## CONTEXTO
Base de dados de clientes de uma universidade. O objetivo é manter apenas
um registro por e-mail para evitar envio duplicado de comunicações.

## DADOS
Planilha: clientes.xlsx
Colunas: ID (inteiro), Nome (texto), Email (texto), Data_Cadastro (data), Status (texto)
Tamanho: aproximadamente 3.000 registros
Anomalia: mesmo e-mail pode aparecer com IDs diferentes (registros duplicados por migração de sistema)

## OBJETIVO
Manter apenas o registro com a Data_Cadastro mais antiga para cada e-mail.
Registros removidos devem ser listados (com seus IDs) para fins de auditoria.

## RESTRIÇÕES
- Excel versão 2019 (sem XLOOKUP disponível)
- Não posso alterar a planilha original; trabalhar em uma cópia

## EXEMPLO DE DADOS
| ID  | Nome        | Email          | Data_Cadastro | Status |
|-----|-------------|----------------|---------------|--------|
| 101 | Ana Silva   | ana@univ.edu   | 2021-03-10    | Ativo  |
| 102 | Ana Silva   | ana@univ.edu   | 2023-07-15    | Ativo  |
| 103 | Bruno Costa | bruno@univ.edu | 2020-11-02    | Ativo  |

## PERGUNTA
Qual é a melhor abordagem para identificar e remover as duplicatas descritas?
Prefiro uma solução que possa ser replicada mensalmente sem retrabalho.
```

4. Compare as duas respostas recebidas.

**Parte 2 — Questão de Múltipla Escolha:**

Com base no experimento realizado, qual afirmação descreve melhor a diferença entre as duas respostas do Claude?

a) As respostas foram equivalentes, pois o Claude sempre entende o contexto implícito.  
b) O prompt estruturado gerou uma resposta mais específica e acionável porque forneceu ao Claude informações de contexto, estrutura de dados, restrições e um exemplo concreto.  
c) O prompt vago foi mais eficiente por ser mais curto e direto.  
d) A qualidade da resposta dependeu exclusivamente da versão do Claude utilizada, não do prompt.

> 📸 *Sugestão de Captura de Tela:* Capture as duas respostas do Claude lado a lado para registro comparativo.

**Gabarito:** Alternativa **b**.

**Fundamentação:** A resposta ao prompt vago tende a ser genérica (lista de opções sem orientação contextual). O prompt estruturado fornece ao modelo as informações necessárias para propor uma solução específica para o problema descrito — identificar duplicatas por e-mail, manter o registro mais antigo e gerar lista de auditoria — respeitando as restrições de versão do Excel informadas.

---

### Mão na massa

Utilize o modelo abaixo para estruturar uma consulta analítica sobre um conjunto de dados do seu próprio contexto. Preencha cada seção com informações reais:

```
## CONTEXTO
[Descreva em 2 a 3 frases: qual é o projeto, quem usa e por que importa]

## DADOS
Arquivo: [nome do arquivo]
Colunas: [listar colunas e tipo de dado de cada uma]
Tamanho aproximado: [número de linhas × número de colunas]
Período: [intervalo de tempo coberto, se aplicável]

## OBJETIVO
[Descreva o que precisa obter: classificar, comparar, detectar anomalias, gerar relatório, etc.]

## RESTRIÇÕES
[Versão do Excel, limitações de tempo, dados sensíveis que não devem ser enviados, etc.]

## EXEMPLO DE DADOS
[Insira 5 a 10 linhas reais ou fictícias representativas]

## PERGUNTA
[Formule de 1 a 3 perguntas específicas e mensuráveis]
```

---

<div style="page-break-after: always;"></div>

# Módulo 3 — Fórmulas de Busca e Lógica Condicional no Excel

> **Pré-requisito: Módulo 2 concluído.** Com domínio da estruturação de prompts, o participante está preparado para aprofundar-se nas fórmulas mais demandadas em análise de dados: as funções de busca e as de lógica condicional.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Distinguir as funções `PROCV`, `XLOOKUP` e `ÍNDICE/CORRESP` quanto a sintaxe, limitações e casos de uso recomendados, selecionando a mais adequada para cada cenário.
2. Construir fórmulas de lógica condicional com `SE`, `IFS` e `SWITCH`, escolhendo a função mais legível e sustentável para o contexto.
3. Solicitar ao Claude, por meio de prompts estruturados, a geração e a explicação de fórmulas complexas, incluindo tratamento de erros com `IFERROR`.
4. Validar manualmente uma fórmula recebida do Claude por meio de testes com dados extremos (valores vazios, negativos ou fora do intervalo esperado).

---

### Texto Descritivo

As fórmulas de busca constituem um dos recursos mais utilizados — e mais mal compreendidos — do Excel. Sua função essencial é a seguinte: dado um valor em uma célula, localizar esse mesmo valor em outra tabela e retornar uma informação associada a ele. Trata-se, em termos simples, de um mecanismo de cruzamento de tabelas, análogo ao que em bancos de dados relacionais denomina-se "junção" (join).

A função `PROCV` (denominada `VLOOKUP` na versão em inglês do Excel) é a mais conhecida entre os usuários. Sua lógica é a seguinte: dado um valor de referência, ela percorre a primeira coluna de um intervalo de tabela e, ao encontrar uma correspondência, retorna o valor da coluna especificada pelo usuário. A limitação mais crítica do `PROCV` é estrutural: ele só consegue retornar valores localizados à direita da coluna de busca. Se a informação desejada estiver em uma coluna à esquerda, a função falha. Além disso, o `PROCV` é sensível à inserção de novas colunas na tabela de referência, pois o número da coluna de retorno é indicado de forma relativa (1, 2, 3...) e não pelo nome da coluna.

A função `XLOOKUP`, disponível no Excel 365 e no Excel 2021 em diante, resolve as principais limitações do `PROCV`. Ela aceita busca em qualquer direção (esquerda ou direita), permite definir diretamente os intervalos de busca e de retorno pelo nome ou referência de coluna, e incorpora nativamente o tratamento do caso "não encontrado", eliminando a necessidade de encapsular a fórmula em `IFERROR`. Recomenda-se que usuários de versões modernas do Excel adotem o `XLOOKUP` como padrão para operações de busca simples.

Para situações que envolvem múltiplas condições simultâneas de busca — por exemplo, localizar um registro em que a coluna A contenha determinado nome *e* a coluna B contenha determinada categoria — a combinação `ÍNDICE/CORRESP` é a solução mais indicada. O `CORRESP` localiza a posição (linha ou coluna) em que um valor se encontra dentro de um intervalo; o `ÍNDICE` utiliza essa posição para retornar o valor correspondente em outro intervalo. A combinação das duas funções confere grande flexibilidade, ao custo de uma sintaxe mais complexa que exige prática para ser dominada.

No que se refere à lógica condicional, a função `SE` — equivalente ao `IF` em inglês — avalia uma condição e retorna um valor caso ela seja verdadeira e outro caso seja falsa. Quando há mais de duas categorias possíveis, é necessário encadear múltiplos `SE`, o que torna a fórmula progressivamente difícil de ler e manter. A função `IFS`, disponível nas versões mais recentes do Excel, resolve esse problema ao permitir a listagem de pares condição–resultado sem aninhamento, resultando em fórmulas mais legíveis. Por sua vez, a função `SWITCH` é recomendada quando as condições envolvem valores discretos e bem definidos (códigos, categorias, abreviações), pois sua sintaxe é mais concisa do que a do `IFS` nesses casos.

Observa-se que o Claude é particularmente útil para a geração dessas fórmulas quando o participante fornece exemplos concretos de dados de entrada e do resultado esperado. A prática de solicitar ao Claude não apenas a fórmula, mas também a explicação de cada argumento, acelera o processo de aprendizagem e reduz a dependência futura da ferramenta para situações similares. Convém reiterar que toda fórmula recebida deve ser validada em um subconjunto controlado antes de ser aplicada à base completa.

---

### Exercício Prático

**Atividade: Selecionar a Função de Busca Correta para Cada Cenário** *(25 minutos)*

**Cenário:** Uma planilha de controle acadêmico possui duas tabelas:

- **Tabela Alunos** (colunas A a D): `Matrícula | Nome | Curso | Turma`
- **Tabela Notas** (colunas F a H): `Matrícula | Nota_Final | Situação`

**Procedimento:**

1. Monte as duas tabelas em abas distintas de uma planilha Excel (pode utilizar dados fictícios).

2. Na aba "Tabela Notas", adicione uma coluna I chamada "Nome_Aluno".

3. Solicite ao Claude a fórmula adequada com o seguinte prompt:

```
Tenho duas tabelas no Excel:
Tabela Alunos (Aba1, colunas A:D): Matrícula, Nome, Curso, Turma
Tabela Notas (Aba2, colunas F:H): Matrícula, Nota_Final, Situação

Quero trazer o Nome do aluno para a coluna I da Aba2, cruzando pela Matrícula.
Tenho Excel 2019 (sem XLOOKUP).
Qual função devo usar e por quê? Mostre a fórmula com tratamento de erro.
```

4. Implemente a fórmula sugerida. Teste com pelo menos uma matrícula inexistente para verificar se o tratamento de erro funciona corretamente.

5. Na coluna J, adicione uma fórmula `IFS` que classifique cada aluno segundo a seguinte regra:
   - Nota ≥ 7,0 → "Aprovado"
   - Nota ≥ 5,0 → "Recuperação"
   - Nota < 5,0 → "Reprovado"

6. Solicite ao Claude que valide a lógica da fórmula `IFS` e que sugira como tratar o caso de célula de nota vazia.

> 📸 *Sugestão de Captura de Tela:* Registre a planilha com as colunas I e J preenchidas e o trecho do chat com o Claude que gerou as fórmulas, para documentação do processo.

**Critério de êxito:** A coluna I deve exibir o nome correto para todas as matrículas existentes e uma mensagem de erro tratada ("Não encontrado" ou equivalente) para matrículas inexistentes. A coluna J deve classificar corretamente os alunos de acordo com as três faixas de nota. O participante deve ser capaz de identificar qual função foi utilizada para a busca e justificar a escolha em função da versão do Excel disponível.

---

### Mão na massa

Utilize o prompt abaixo para solicitar ao Claude uma fórmula de busca ou lógica condicional aplicável a uma planilha do seu próprio contexto:

```
Tenho as seguintes tabelas no Excel:
Tabela 1 ([nome da aba], colunas [especificar]): [listar colunas]
Tabela 2 ([nome da aba], colunas [especificar]): [listar colunas]

Objetivo: [descrever o cruzamento ou classificação desejada]

Versão do Excel: [informar: 2019, 365, web, etc.]

Dados de exemplo:
[inserir 4 a 5 linhas ilustrativas]

Resultado esperado:
[descrever o que deve aparecer na célula de destino]

Por favor, forneça a fórmula com tratamento de erro e explique cada argumento.
```

---

<div style="page-break-after: always;"></div>

# Módulo 4 — Diagnóstico e Tratamento de Bases de Dados

> **Pré-requisito: Módulo 3 concluído.** O deslocamento de foco, neste módulo, vai das fórmulas de cálculo para a etapa que as precede logicamente: garantir que os dados sobre os quais se aplicam as fórmulas sejam confiáveis, consistentes e livres de anomalias.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Elaborar um prompt de diagnóstico de qualidade de dados que solicite ao Claude a identificação de campos vazios, formatos inconsistentes, duplicatas e outliers em uma base descrita.
2. Aplicar as funções `REMOVER.ESPAÇOS`, `PRI.MAIÚSCULA`, `SUBS` e suas variantes para normalizar campos de texto em uma planilha Excel.
3. Descrever, em termos gerais, as diferenças entre as abordagens disponíveis para remoção de duplicatas no Excel (fórmula, Power Query, VBA), reconhecendo a mais indicada para bases de até 10.000 registros.
4. Utilizar o Claude para interpretar e corrigir problemas de qualidade identificados, solicitando soluções passo a passo e validando os resultados.

---

### Texto Descritivo

Antes de qualquer análise, é necessário assegurar a qualidade dos dados. Essa premissa, consagrada na literatura de ciência de dados pela expressão "garbage in, garbage out" (lixo entra, lixo sai), significa que fórmulas sofisticadas e visualizações elaboradas perdem completamente sua utilidade quando aplicadas sobre dados imprecisos, incompletos ou inconsistentes. O diagnóstico prévio da base é, portanto, uma etapa incontornável do trabalho analítico.

Os problemas mais comuns em bases de dados de uso cotidiano — em ambientes acadêmicos e administrativos — podem ser agrupados em quatro categorias. A primeira é a presença de campos vazios: colunas obrigatórias que, por falhas de entrada de dados ou migrações de sistema, não foram preenchidas. A segunda é a inconsistência de formatos: datas registradas em padrões distintos (DD/MM/AAAA e MM/DD/AAAA na mesma coluna, por exemplo), números armazenados como texto ou telefones com e sem parênteses e hífens. A terceira categoria é a duplicação de registros: o mesmo cliente, aluno ou produto aparece mais de uma vez com identificadores distintos, geralmente como consequência de processos de importação ou integração entre sistemas. A quarta é a presença de anomalias ou outliers: valores numericamente possíveis, mas improvável no contexto (uma data de nascimento no século XVIII em um cadastro de funcionários ativos, por exemplo).

O Claude pode atuar como orientador metodológico nessa etapa, desde que o participante forneça uma amostra representativa dos dados — idealmente as primeiras 20 linhas, incluindo o cabeçalho — e descreva o padrão esperado para cada coluna. Com essas informações, o Claude é capaz de identificar inconsistências, sugerir fórmulas de normalização e recomendar uma sequência lógica de limpeza.

No que se refere à normalização de texto, o Excel dispõe de funções específicas para as situações mais frequentes. `REMOVER.ESPAÇOS` elimina espaços em excesso no início, no fim e entre palavras de uma célula de texto — problema muito comum em dados copiados de sistemas legados. `PRI.MAIÚSCULA` converte o texto para o padrão de capitalização de nomes próprios (primeira letra de cada palavra em maiúscula). `SUBS` (ou `SUBSTITUIR`) permite trocar um padrão de caracteres por outro, sendo útil, por exemplo, para padronizar separadores em números de telefone.

Para o tratamento de duplicatas, a escolha da abordagem depende do volume de dados e das regras de negócio envolvidas. Para bases de até 10.000 registros, o Power Query — ferramenta integrada ao Excel que permite transformações visuais e auditáveis — é a solução recomendada pelo material-fonte. Fórmulas podem ser utilizadas para identificar duplicatas, mas não as removem diretamente; e macros VBA, embora potentes, exigem um nível de familiaridade com programação que vai além do escopo deste curso introdutório. O Módulo 6 do material-fonte aprofunda o uso de VBA e Python para automação, mas esses tópicos estão fora do escopo desta trilha Essentials.

---

### Exercício Prático

**Atividade: Diagnosticar e Normalizar uma Base com Problemas de Qualidade** *(10 minutos)*

**Dados fornecidos para o exercício:** Considere a seguinte amostra de dados com problemas intencionais.

| ID | Nome | Email | Data_Cadastro | Telefone |
|---|---|---|---|---|
| 201 | ana silva | ana@univ.edu | 15/03/2021 | (11)99999-1111 |
| 202 | BRUNO SANTOS | bruno@univ.edu | 2021-07-22 | 11 88888 2222 |
| 203 | Carlos Lima | carlos@univ.edu | 03/11/2020 | 21-77777-3333 |
| 202 | Bruno Santos | bruno@univ.edu | 22/07/2021 | (21)88888-2222 |
| 204 |  | diana@univ.edu | 01/04/2022 |  |

**Procedimento:**

1. Reproduza a tabela acima em uma planilha Excel (aba "Dados_Brutos").

2. Envie ao Claude o seguinte prompt:

```
Tenho uma base de dados com os seguintes problemas identificados visualmente:
- Coluna Nome: capitalização inconsistente (minúsculas, maiúsculas, misturadas)
- Coluna Data_Cadastro: dois formatos diferentes (DD/MM/AAAA e AAAA-MM-DD)
- Coluna Telefone: formatos variados para o mesmo dado
- ID 202: duplicado com variação de capitalização no nome e formato diferente no telefone
- Linha 5: campo Nome vazio

Para cada problema, indique:
a) A fórmula Excel mais adequada para corrigir ou sinalizar o problema
b) Se a fórmula deve ser aplicada em coluna auxiliar ou no dado original
c) Qual é a ordem de prioridade de limpeza

Versão do Excel disponível: 2019.
```

3. Leia a resposta do Claude e implemente pelo menos uma das normalizações sugeridas (recomenda-se a normalização do campo Nome com `PRI.MAIÚSCULA` e `REMOVER.ESPAÇOS`).

4. Na coluna F, crie uma fórmula que sinalize os IDs duplicados com o texto "DUPLICADO" e os demais com "OK".

> 📸 *Sugestão de Captura de Tela:* Registre a planilha com a coluna de normalização de nomes e a coluna de sinalização de duplicatas aplicadas, bem como o prompt enviado ao Claude e a respectiva resposta.

**Critério de êxito:** A coluna de nomes normalizados deve exibir "Ana Silva", "Bruno Santos" e "Carlos Lima" com capitalização consistente. A coluna de sinalização deve marcar as linhas com ID 202 como "DUPLICADO" e as demais como "OK". O participante deve ser capaz de descrever o problema de qualidade que cada fórmula resolve.

---

### Mão na massa

Use o prompt abaixo para solicitar ao Claude um diagnóstico de qualidade de uma base de dados do seu próprio contexto:

```
Tenho uma base de dados com as seguintes colunas: [listar colunas e tipo de dado esperado].
O tamanho aproximado é: [número de linhas].
Suspeito dos seguintes problemas: [descrever o que foi observado visualmente].

Com base na amostra abaixo, identifique:
1. Problemas de formato inconsistente
2. Campos vazios ou com valores impossíveis
3. Possíveis duplicatas
4. Ordem de prioridade de limpeza

Amostra (10 a 20 linhas):
[inserir a amostra]
```

---

<div style="page-break-after: always;"></div>

# Módulo 5 — Síntese e Aplicação Integrada

> **Pré-requisito: Módulos 1 a 4 concluídos.** Este módulo não introduz conteúdo novo; sua função é consolidar, por meio de uma atividade integradora, todas as competências desenvolvidas ao longo do curso.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Executar um fluxo completo de consultoria com o Claude — do diagnóstico inicial à validação do resultado — aplicado a uma base de dados de domínio próprio ou fornecida para o exercício.
2. Selecionar, de forma autônoma e justificada, as ferramentas e funções estudadas (estrutura de prompt, fórmulas de busca, lógica condicional, normalização de texto) adequadas a cada etapa do fluxo.
3. Produzir um registro documentado da interação com o Claude (prints ou anotações) que permita a replicação futura do procedimento adotado.
4. Avaliar criticamente o resultado obtido em relação aos critérios de êxito definidos previamente, identificando limitações e possíveis aprimoramentos.

---

### Texto Descritivo

O aprendizado de uma ferramenta técnica consolida-se, em larga medida, pela aplicação integrada dos conceitos em um problema que exige a articulação de múltiplas competências. Ao longo dos módulos anteriores, o participante foi apresentado ao paradigma de consultoria com inteligência artificial, ao método de estruturação de prompts, às principais fórmulas de busca e lógica condicional do Excel e às técnicas básicas de diagnóstico e tratamento de dados. Neste módulo, essas competências são articuladas em um fluxo de trabalho contínuo.

O fluxo proposto na atividade integradora segue as cinco etapas do padrão de consultoria apresentado no Módulo 1: diagnóstico (identificar o problema e a qualidade dos dados), exploração (solicitar ao Claude múltiplas abordagens possíveis), implementação (aplicar a solução em um subconjunto controlado), validação (conferir o resultado com dados de teste) e escalação (aplicar a solução aprovada à base completa). A execução completa desse ciclo, ainda que em escala reduzida, é o indicador mais confiável de que o participante internalizou não apenas as técnicas individuais, mas a lógica de uso da inteligência artificial como parceira analítica.

Observa-se que o registro documentado do processo — capturas de tela dos prompts enviados, das respostas recebidas e dos resultados implementados — é uma prática altamente recomendável. Esse registro cumpre duas funções: permite a replicação futura do procedimento em contextos similares e possibilita a revisão crítica do fluxo, identificando etapas que poderiam ter sido mais eficientes. No ambiente acadêmico e administrativo, em que processos analíticos tendem a ser repetidos periodicamente (relatórios mensais, análises trimestrais, consolidações anuais), a documentação das decisões metodológicas tem valor permanente.

Por fim, convém reiterar que a parceria com o Claude não substitui o julgamento analítico do profissional. O Claude pode gerar fórmulas incorretas, interpretar equivocadamente a estrutura de dados ou sugerir abordagens inapropriadas para o contexto. A competência que este curso busca desenvolver não é a de delegar o raciocínio analítico à inteligência artificial, mas a de utilizá-la como amplificador das capacidades do profissional — reduzindo o tempo despendido em tarefas mecânicas e liberando atenção para o que realmente importa: a interpretação dos resultados e a tomada de decisão.

---

### Exercício Prático

**Atividade Integradora: Fluxo Completo de Consultoria Analítica com Claude** *(10 minutos de planejamento + execução adicional conforme disponibilidade)*

**Cenário:** Uma coordenação acadêmica possui uma planilha de desempenho de alunos com os seguintes dados (reproduza em uma planilha Excel):

| Matrícula | Nome | Curso | Nota_Final | Frequência | Data_Matrícula |
|---|---|---|---|---|---|
| 2021001 | ana lima | Administração | 7,5 | 85 | 15/03/2021 |
| 2021002 | CARLOS SOUZA | Engenharia | 4,8 | 72 | 2021-03-15 |
| 2021003 | Maria Costa | Administração | 8,2 | 91 | 20/04/2021 |
| 2021002 | Carlos Souza | Engenharia | 4,8 | 72 | 15/03/2021 |
| 2021004 | Pedro Alves | Direito |  | 65 | 05/05/2021 |
| 2021005 | Lucia Ferreira | Administração | 5,5 | 78 | 10/06/2021 |

**A atividade integradora exige a execução das seguintes etapas:**

**Etapa 1 — Diagnóstico (Módulo 4):** Envie ao Claude um prompt de diagnóstico de qualidade desta base, identificando pelo menos três problemas distintos.

**Etapa 2 — Normalização (Módulo 4):** Aplique fórmulas para normalizar o campo Nome e sinalizar a duplicata identificada na Matrícula 2021002.

**Etapa 3 — Classificação por Lógica Condicional (Módulo 3):** Crie uma coluna "Situação" utilizando `IFS` com as seguintes regras:
- Nota ≥ 7,0 E Frequência ≥ 75 → "Aprovado"
- Nota ≥ 5,0 E Frequência ≥ 75 → "Recuperação"
- Frequência < 75 → "Reprovado por Falta"
- Nota < 5,0 → "Reprovado por Nota"
- Nota vazia → "Sem Registro"

**Etapa 4 — Busca Cruzada (Módulo 3):** Crie uma segunda aba com uma tabela de referência:

| Curso | Coordenador |
|---|---|
| Administração | Prof. Dr. João Mendes |
| Engenharia | Prof. Dra. Sandra Ramos |
| Direito | Prof. Dr. Ricardo Fonseca |

Na planilha principal, adicione uma coluna "Coordenador" que busque o nome do coordenador correspondente ao curso de cada aluno, utilizando `ÍNDICE/CORRESP` ou `PROCV`.

**Etapa 5 — Validação:** Teste a coluna "Situação" com o aluno de Nota vazia (Pedro Alves) e o aluno duplicado (Carlos Souza). Registre se o resultado corresponde ao esperado.

> 📸 *Sugestão de Captura de Tela:* Registre a planilha final com todas as colunas preenchidas e pelo menos um trecho do chat com o Claude utilizado em alguma das etapas.

**Tabela de Critérios de Avaliação:**

| Critério | Atendido? |
|---|---|
| Diagnóstico identificou pelo menos 3 problemas de qualidade distintos | ☐ Sim / ☐ Não |
| Campo Nome normalizado com capitalização consistente | ☐ Sim / ☐ Não |
| Duplicata da Matrícula 2021002 sinalizada corretamente | ☐ Sim / ☐ Não |
| Coluna "Situação" classifica corretamente os 6 registros, incluindo nota vazia | ☐ Sim / ☐ Não |
| Coluna "Coordenador" traz o nome correto para os 3 cursos distintos | ☐ Sim / ☐ Não |
| Pelo menos um prompt estruturado (com Contexto, Dados, Objetivo, Exemplo e Pergunta) foi utilizado | ☐ Sim / ☐ Não |
| Resultado foi validado com ao menos um caso de teste extremo antes da aplicação completa | ☐ Sim / ☐ Não |

---

### Mão na massa

Utilize o modelo abaixo para documentar o fluxo de consultoria realizado nesta atividade, criando um registro que poderá ser reutilizado em contextos similares no futuro:

```
## Registro de Consultoria com Claude
Data: [data]
Base de dados: [nome do arquivo ou planilha]
Problema original: [descrever em 2 a 3 frases]

## Etapas Realizadas
1. Diagnóstico: [resumo do que foi identificado]
2. Normalização: [funções utilizadas e resultado]
3. Classificação: [lógica condicional aplicada]
4. Busca cruzada: [função utilizada e tabela de referência]
5. Validação: [casos testados e resultados]

## Prompts Mais Eficazes
[Copiar aqui os prompts que geraram as respostas mais úteis]

## Limitações Identificadas
[O que o Claude não conseguiu resolver adequadamente? O que exigiu validação manual?]

## Próximos Passos
[O que poderia ser automatizado ou aprofundado em uma próxima sessão?]
```

---

## Encerramento

O presente curso percorreu, em quatro módulos de conteúdo progressivo e um módulo de síntese, os fundamentos necessários para o uso do Claude como parceiro analítico no Microsoft Excel. Partiu-se do entendimento do papel da inteligência artificial como consultor técnico, passou-se pela construção de prompts estruturados, aprofundou-se nas principais funções de busca e lógica condicional e encerrou-se com as práticas essenciais de diagnóstico e tratamento de dados. Recomenda-se que o participante mantenha o hábito de aplicar o fluxo de consultoria — diagnóstico, exploração, implementação, validação e escalação — em situações reais de sua prática profissional ou acadêmica, pois é pela repetição contextualizada que as competências aqui introduzidas se consolidam em autonomia analítica duradoura.

Para o aprofundamento das competências desenvolvidas neste curso, o participante pode explorar os módulos avançados do material-fonte, que cobrem temas como fórmulas matriciais modernas (`FILTRO`, `CLASSIFICAR`, `ÚNICA`), automação com VBA e integração do Excel com Python por meio da biblioteca Pandas. Adicionalmente, recomenda-se a exploração de ferramentas complementares de análise de dados, como o Power BI para visualizações interativas e o Power Query para transformações de dados em escala, ambos integrados ao ecossistema Microsoft. O domínio progressivo dessas ferramentas, aliado à competência de consultoria com inteligência artificial desenvolvida neste curso, posiciona o profissional para enfrentar desafios analíticos de crescente complexidade com autonomia e precisão metodológica.

> **Síntese:** A inteligência artificial não substitui o julgamento analítico do profissional — ela o amplifica; e a competência de formular perguntas precisas é, nesse contexto, tão importante quanto a de interpretar respostas.
