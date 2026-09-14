<link rel="stylesheet" href="../../.css/style.css">

# Claude para Excel: Consultoria Analítica, Fórmulas Complexas e Automação — Curso Hands-on

*Claude for Excel: Analytical Consulting, Complex Formulas and Automation — Curso Hands-on*

   > *Ao final deste curso, você terá construído, do zero, uma mini-dashboard de análise de dados usando o Claude como seu consultor particular — e vai querer mostrar para todo mundo.*

---

## Antes de Arregaçar as Mangas

Este curso não tem slides bonitos nem teoria para copiar no caderno. Tem problema real, passo a passo e você fazendo. Cada oficina começa com uma situação que qualquer pessoa que usa Excel já viveu (ou vai viver em breve), e termina com uma vitória concreta que você pode ver na tela.

Sem enrolação. Direto ao ponto. Mão na massa.

**O que você precisa ter aberto agora:**

- Microsoft Excel (versão 2019 ou Microsoft 365 — de preferência o 365, pois algumas funções são exclusivas dele)
- Um navegador aberto em [claude.ai](https://claude.ai) com uma conta ativa
- Este curso em outra janela ou aba, para consultar enquanto pratica
- Um arquivo novo e vazio no Excel — pode chamar de `treino_claude.xlsx`

> 🔑 **A regra de ouro:** Não existe resposta errada no Claude — existe prompt mal explicado. Se a resposta vier estranha, o problema quase sempre está na pergunta. Reescreva, adicione mais contexto e tente de novo. É assim que funciona, e é assim que você aprende.

---

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1 | Você tem uma planilha bagunçada e não sabe por onde começar — o Claude vai te dizer | 20 min |
| 2 | Precisa cruzar duas tabelas mas o PROCV nunca funciona direito — vamos resolver isso de vez | 20 min |
| 3 | Sua planilha precisa classificar clientes automaticamente por regras de negócio | 20 min |
| 4 | Você tem 500 linhas com nomes escritos de todo jeito — hora de limpar tudo de uma vez | 20 min |
| Projeto Final | Tudo junto: uma mini-dashboard de análise de desempenho construída por você | 20 min |

As oficinas funcionam em sequência — cada uma entrega uma pequena vitória que você vai usar na próxima. Mas se você já conhece algum tema, pode pular para o trecho que precisar.

---

<div style="page-break-after: always;"></div>

# Oficina 1 — Peça um Diagnóstico, Não uma Solução

### 🎯 O Problema

Você recebeu uma planilha de outra pessoa. Tem dados, tem colunas, mas você não sabe nem se os dados estão corretos. Antes de fazer qualquer análise, você precisa de um "raio-X" da planilha — e o Claude faz isso em segundos, se você pedir do jeito certo.

Ao final desta oficina, você vai saber pedir ao Claude que analise a estrutura de qualquer base de dados e aponte os problemas antes que eles estraguem sua análise.

### 🧰 O que você vai usar

- Excel (qualquer versão)
- Claude (claude.ai)
- A planilha de exemplo que você vai montar agora mesmo

### 👐 Mão na massa

**Parte 1: Montar a planilha de exemplo (5 minutos)**

1. Abra o Excel e vá para a planilha em branco do seu arquivo `treino_claude.xlsx`.
2. Renomeie a aba de baixo para `Clientes` (clique duas vezes no nome da aba).
3. Digite os dados abaixo, célula por célula, começando em A1:

   | ID | Nome | Email | Data_Cadastro | Receita | Status |
   |---|---|---|---|---|---|
   | 101 | ana silva | ana@empresa.com | 15/03/2021 | 45000 | Ativo |
   | 102 | BRUNO SANTOS | bruno@empresa.com | 2021-07-22 | 28000 | ativo |
   | 103 | Carlos Lima | carlos@empresa.com | 20/11/2020 | 62000 | Ativo |
   | 102 | Bruno Santos | bruno@empresa.com | 22/07/2021 | 28000 | Ativo |
   | 104 |  | diana@empresa.com | 01/04/2022 | 15000 | Inativo |
   | 105 | Eduardo Rocha | eduardo@empresa.com | 10/06/2022 | R$ 33.000 | Ativo |

   > 📌 **Não esqueça:** Digite exatamente como está acima — com os erros propositais. Eles fazem parte do exercício.

4. Salve o arquivo (Ctrl+S).

**Parte 2: Copiar os dados para o Claude (3 minutos)**

5. Selecione o intervalo A1 até F7 (cabeçalho + 6 linhas de dados).
6. Copie com Ctrl+C.
7. Vá ao Claude e abra uma nova conversa.
8. No campo de mensagem, cole os dados com Ctrl+V e adicione o seguinte texto **antes** dos dados colados:

> Tenho uma planilha de clientes com os dados abaixo. Faça um diagnóstico completo de qualidade: identifique campos vazios, formatos inconsistentes, duplicatas e qualquer outro problema que possa atrapalhar uma análise. Liste os problemas em ordem de prioridade e explique cada um em uma linha.

9. Pressione Enter para enviar.

> 📸 *Sugestão de Captura de Tela:* Tire um print da tela do Claude com o prompt enviado e os dados colados, antes de enviar — é útil para comparar com a resposta.

**Parte 3: Ler e anotar a resposta (5 minutos)**

10. Leia a resposta completa do Claude.
11. Volte ao Excel e, na célula H1, escreva `Problemas encontrados`.
12. Nas células H2, H3, H4... escreva cada problema que o Claude apontou (um por linha).

> 💡 **Dica:** O Claude provavelmente vai identificar pelo menos cinco problemas nessa planilha. Se ele encontrou menos que três, tente enviar o prompt novamente pedindo para ser mais detalhado.

**Parte 4: Perguntar como corrigir (5 minutos)**

13. No mesmo chat do Claude (não abra outro), envie esta mensagem:

> Dos problemas que você listou, qual é o mais fácil de corrigir agora mesmo com uma fórmula do Excel? Me dê a fórmula pronta.

14. Leia a resposta e anote a fórmula sugerida.

### ✅ Deu certo?

O Claude deve ter listado pelo menos: a duplicata no ID 102, o campo Nome vazio na linha 5, os formatos diferentes de data (DD/MM/AAAA e AAAA-MM-DD), a capitalização inconsistente nos nomes e o valor de receita com "R$" na linha 6. Se todos esses aparecerem na resposta, você arrasou.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O Claude respondeu de forma genérica, sem apontar problemas específicos | Verifique se os dados foram colados corretamente no chat; tente selecionar e copiar a tabela do Excel de novo |
| Os dados aparecem bagunçados no Claude (sem colunas) | Tente copiar a tabela, colar em um arquivo de texto (Notepad), e de lá copiar para o Claude |
| O Claude disse que não consegue ver a planilha | Ele não lê arquivos diretamente — precisa que você cole os dados no chat como texto |

### 🚀 Quer ir além?

- Adicione mais 10 linhas de dados fictícios à planilha e repita o diagnóstico; veja se o Claude encontra novos padrões.
- Peça ao Claude para estimar quantas linhas da planilha têm algum tipo de problema.
- Pergunte ao Claude quais colunas seriam boas candidatas a "chave única" (identificador que não se repete) nessa base.

---

<div style="page-break-after: always;"></div>

# Oficina 2 — Cruze Duas Tabelas sem Enlouquecer

### 🎯 O Problema

Você tem a lista de clientes em uma aba e o registro de vendas em outra. Precisava juntar as duas — e o PROCV que você tentou ontem retornou #N/A em metade das células. Clássico. Hoje você vai resolver isso com o Claude como assistente, e entender de verdade o que está acontecendo por baixo dos panos.

Ao final desta oficina, você terá cruzado duas tabelas e trazido o nome do cliente para a tabela de vendas — usando a função certa para o seu Excel.

### 🧰 O que você vai usar

- Excel (versão 2019 ou 365)
- Claude (claude.ai)
- O arquivo `treino_claude.xlsx` da Oficina 1

### 👐 Mão na massa

**Parte 1: Criar a segunda tabela (5 minutos)**

1. No arquivo `treino_claude.xlsx`, clique no símbolo "+" ao lado das abas de baixo para criar uma nova aba.
2. Renomeie-a para `Vendas`.
3. Digite os dados abaixo nessa nova aba, a partir da célula A1:

   | ID_Cliente | Produto | Valor_Venda | Data_Venda |
   |---|---|---|---|
   | 101 | Consultoria | 8500 | 15/01/2024 |
   | 103 | Treinamento | 4200 | 18/01/2024 |
   | 105 | Licença | 2900 | 22/01/2024 |
   | 101 | Suporte | 1500 | 05/02/2024 |
   | 103 | Consultoria | 6800 | 10/02/2024 |
   | 107 | Licença | 3300 | 14/02/2024 |

   > 📌 **Observe:** O ID 107 está na tabela de Vendas, mas não existe na aba Clientes. Isso é proposital — e você vai descobrir o que acontece com ele.

4. Na célula E1, escreva `Nome_Cliente`.

**Parte 2: Pedir a fórmula ao Claude (5 minutos)**

5. Vá ao Claude e inicie uma nova conversa (ou use a mesma da Oficina 1).
6. Envie a seguinte mensagem:

> Tenho duas abas no Excel:
>
> Aba "Clientes" (colunas A a F): ID, Nome, Email, Data_Cadastro, Receita, Status
>
> Aba "Vendas" (colunas A a D): ID_Cliente, Produto, Valor_Venda, Data_Venda
>
> Quero trazer o Nome do cliente para a coluna E da aba Vendas, cruzando pelo ID.
> Meu Excel é o Microsoft 365. Qual função usar? Me dê a fórmula pronta para colocar em E2, com tratamento para quando o ID não existir na aba Clientes.

7. Leia a resposta. O Claude provavelmente vai recomendar `XLOOKUP` para o Excel 365.

> 🤓 **Curiosidade técnica — pode pular sem prejuízo:** O XLOOKUP (ou PROCX em português no Excel 365) é o sucessor moderno do PROCV. A diferença prática mais importante: o XLOOKUP não exige que a coluna que você quer buscar seja a primeira da tabela, e você define exatamente qual coluna quer de retorno — o que elimina aquele número mágico "2" ou "3" que sempre confundia no PROCV.

**Parte 3: Aplicar a fórmula (5 minutos)**

8. Volte ao Excel, aba `Vendas`, e clique na célula E2.
9. Digite (ou copie do Claude) a fórmula sugerida. Ela deve ser parecida com esta:

```
=XLOOKUP(A2,Clientes!$A$2:$A$7,Clientes!$B$2:$B$7,"Não encontrado")
```

   Se o seu Excel não reconhecer XLOOKUP, peça ao Claude a versão com PROCV:

```
=IFERROR(PROCV(A2,Clientes!$A$2:$B$7,2,FALSO),"Não encontrado")
```

10. Pressione Enter.
11. Com a célula E2 selecionada, clique no pequeno quadrado verde no canto inferior direito da célula e arraste até E7 para copiar a fórmula para todas as linhas.

> 📸 *Sugestão de Captura de Tela:* Tire um print da aba Vendas com a coluna E preenchida — boa hora para ver o "Não encontrado" aparecer na linha do ID 107.

**Parte 4: Entender o resultado (3 minutos)**

12. Verifique a coluna E. Você deve ver os nomes corretos para os IDs 101, 103 e 105, e "Não encontrado" para o ID 107.
13. Volte ao Claude e pergunte:

> Por que o ID 107 retornou "Não encontrado"? Isso é um problema de dados ou de fórmula?

14. Leia a explicação.

### ✅ Deu certo?

A coluna E da aba Vendas deve mostrar: "ana silva" (ou como você digitou) para o 101, "Carlos Lima" para o 103, "Eduardo Rocha" para o 105, e "Não encontrado" para o 107. Se estiver assim, você acabou de dominar busca cruzada entre tabelas.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| A fórmula retorna #NOME? | Verifique se você está usando a versão em português do Excel — experimente PROCX em vez de XLOOKUP |
| Todos os resultados mostram "Não encontrado" | Confira se o nome da aba está escrito exatamente igual: `Clientes` com C maiúsculo |
| A fórmula funciona em E2 mas fica errada nas outras linhas | Certifique-se de que os intervalos da aba Clientes têm o símbolo $ (referência absoluta), como `$A$2:$A$7` |

### 🚀 Quer ir além?

- Adicione uma coluna F chamada `Receita_Cliente` e traga também a receita total de cada cliente usando a mesma lógica.
- Peça ao Claude uma fórmula que calcule o total de vendas por cliente usando SOMASE.
- Pergunte ao Claude qual é a diferença entre PROCV, XLOOKUP e ÍNDICE/CORRESP, e quando usar cada um.

---

<div style="page-break-after: always;"></div>

# Oficina 3 — Classifique Clientes com Regras de Negócio

### 🎯 O Problema

Seu gestor pediu uma coluna nova: cada cliente deve ser classificado como "Premium", "Padrão" ou "Em risco", seguindo regras que ele definiu em uma reunião. São três condições diferentes, e você não lembra como empilhar vários SE um dentro do outro sem se perder nos parênteses. O Claude vai montar a lógica por você — e você vai entender o que ele fez.

Ao final desta oficina, você terá uma coluna de classificação funcionando com lógica condicional real, e vai saber pedir ao Claude qualquer variação dessa regra.

### 🧰 O que você vai usar

- Excel (versão 2019 ou 365)
- Claude (claude.ai)
- A aba `Clientes` do arquivo `treino_claude.xlsx`

### 👐 Mão na massa

**Parte 1: Definir a regra de negócio (2 minutos)**

Antes de escrever qualquer fórmula, você precisa ter a regra clara. Use esta:

- Receita ≥ 50.000 → **Premium**
- Receita entre 25.000 e 49.999 → **Padrão**
- Receita < 25.000 → **Em risco**

**Parte 2: Pedir a fórmula ao Claude (5 minutos)**

1. Vá ao Claude e envie esta mensagem:

> Tenho uma planilha Excel com a coluna E chamada "Receita" (valores numéricos, sem texto, sem R$).
> Quero criar uma coluna G chamada "Classificação" com estas regras:
> - Receita maior ou igual a 50000 → "Premium"
> - Receita entre 25000 e 49999 → "Padrão"
> - Receita menor que 25000 → "Em risco"
>
> Me dê a fórmula para a célula G2 usando IFS (Excel 365). Depois mostre a mesma lógica usando SE encadeado, para comparar. Explique a diferença de legibilidade entre as duas.

2. Leia as duas versões que o Claude apresentar.

> 💡 **Dica:** O IFS é como uma lista de "se... então..." escrita em linha reta, sem precisar abrir parêntese dentro de parêntese. Muito mais fácil de ler — e de corrigir quando a regra muda.

**Parte 3: Aplicar na planilha (8 minutos)**

3. Volte ao Excel, aba `Clientes`.
4. Clique na célula G1 e escreva `Classificação`.
5. Clique em G2.

   Antes de digitar, um detalhe importante: a coluna E da sua planilha tem o valor da linha 6 escrito como "R$ 33.000" (com texto). Isso vai gerar erro. Primeiro, corrija esse valor:

6. Clique na célula E6 (linha do Eduardo Rocha).
7. Apague o conteúdo e digite apenas `33000` (número puro, sem R$, sem ponto).

   > ⚠️ **Cuidado:** Números com "R$" ou com ponto como separador de milhar podem ser interpretados pelo Excel como texto — e aí nenhuma fórmula numérica funciona. Quando o Claude diagnosticou isso na Oficina 1, era exatamente isso que ele estava apontando.

8. Agora clique em G2 e digite a fórmula IFS que o Claude sugeriu. Ela deve ser parecida com:

```
=IFS(E2>=50000,"Premium",E2>=25000,"Padrão",E2<25000,"Em risco")
```

9. Pressione Enter.
10. Copie a fórmula para G3 até G7 arrastando o quadradinho verde.

**Parte 4: Testar a lógica (5 minutos)**

11. Veja os resultados. Carlos Lima (62.000) deve ser "Premium"; Bruno Santos e Eduardo Rocha (28.000 e 33.000) devem ser "Padrão"; Diana (15.000) deve ser "Em risco".
12. Agora faça um teste: clique em E3 (receita do Carlos Lima) e mude temporariamente para `20000`. A célula G3 deve mudar para "Em risco" automaticamente.
13. Desfaça a mudança (Ctrl+Z) para voltar ao valor original.

> 📸 *Sugestão de Captura de Tela:* Com os dados corretos e a coluna G preenchida, tire um print para registrar seu progresso.

**Parte 5: Adicionar uma segunda regra (5 minutos)**

14. O gestor mudou de ideia (como sempre). Agora ele quer que, além da receita, o Status também conte: se o cliente estiver "Inativo", a classificação deve ser "Cancelado", independentemente da receita.

15. Volte ao Claude e envie:

> Minha fórmula atual classifica por receita. Agora preciso adicionar uma condição nova: se a coluna F (Status) for "Inativo", a classificação deve ser "Cancelado" — e isso tem prioridade sobre todas as outras regras. Como modifico o IFS?

16. Aplique a fórmula atualizada em G2 e copie para as demais linhas.

### ✅ Deu certo?

A coluna G deve mostrar "Cancelado" para Diana (Status = Inativo), e as classificações corretas por receita para os demais. Se o resultado bater, você acabou de aprender a combinar múltiplas condições numa única fórmula — e a fazer isso com a ajuda do Claude de um jeito que você entendeu cada parte.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| A fórmula retorna #NOME? no IFS | Seu Excel pode não suportar IFS — peça ao Claude a versão com SE encadeado |
| Todas as linhas mostram "Em risco" mesmo com receitas altas | Verifique se a coluna E tem números puros; selecione uma célula e olhe se aparece alinhada à direita (número) ou à esquerda (texto) |
| A condição de "Inativo" não funciona | Verifique a grafia exata na coluna Status — "Inativo" com I maiúsculo é diferente de "inativo" com i minúsculo |

### 🚀 Quer ir além?

- Adicione uma quarta categoria: clientes com receita acima de 100.000 são "VIP".
- Peça ao Claude para criar uma coluna de "Ação recomendada" usando SWITCH baseado na coluna Classificação.
- Pergunte ao Claude quando é melhor usar SWITCH em vez de IFS.

---

<div style="page-break-after: always;"></div>

# Oficina 4 — Limpe 500 Nomes de Uma Vez

### 🎯 O Problema

Alguém exportou a base de dados do sistema legado e os nomes dos clientes vieram um caos: alguns em CAIXA ALTA, outros em minúsculas, muitos com espaços sobrando no começo ou no final, e alguns com abreviações inconsistentes. Corrigir um por um levaria horas. Com o Claude e três fórmulas do Excel, você faz isso em minutos.

Ao final desta oficina, você terá uma coluna de nomes limpos e padronizados, e vai saber como empilhar funções de texto no Excel para resolver qualquer variação desse problema.

### 🧰 O que você vai usar

- Excel (qualquer versão)
- Claude (claude.ai)
- A aba `Clientes` do arquivo `treino_claude.xlsx`

### 👐 Mão na massa

**Parte 1: Ampliar a bagunça (para praticar de verdade)**

1. Na aba `Clientes`, adicione mais três linhas com dados propositalmente bagunçados (a partir da linha 8):

   | 106 |    FERNANDA LIMA    | fernanda@empresa.com | 12/01/2023 | 41000 | Ativo |
   | 107 | joão pedro silva | joao@empresa.com | 2023-05-20 | 19000 | Ativo |
   | 108 | Marcos  Oliveira | marcos@empresa.com | 30/08/2023 | 55000 | Inativo |

   > 📌 **Atenção ao digitar:** O nome da Fernanda tem espaços extras no começo e no fim (antes do F e depois do A). O do Marcos tem dois espaços entre o primeiro e o segundo nome. Isso é proposital.

2. Clique na célula H1 e escreva `Nome_Limpo`.

**Parte 2: Pedir as fórmulas ao Claude (5 minutos)**

3. Vá ao Claude e envie:

> Tenho uma coluna de nomes no Excel com três tipos de problema:
> 1. Nomes em CAIXA ALTA (ex: "FERNANDA LIMA")
> 2. Nomes em minúsculas (ex: "joão pedro silva")
> 3. Espaços extras no início, no fim ou entre palavras (ex: "  FERNANDA LIMA  " ou "Marcos  Oliveira")
>
> Quero uma fórmula única na coluna H que corrija os três problemas de uma vez e deixe o nome com a primeira letra de cada palavra em maiúscula (ex: "Fernanda Lima").
> Me explique cada função usada.

4. Leia a resposta. O Claude deve apresentar uma combinação de `PRI.MAIÚSCULA` (ou `PROPER` em inglês) e `TIRAR.ESPAÇOS` (ou `TRIM` em inglês).

> 🤓 **Curiosidade técnica — pode pular sem prejuízo:** Essas funções "empilhadas" funcionam de dentro para fora: o Excel primeiro executa a função mais interna, depois passa o resultado para a próxima. É como descascar uma cebola ao contrário — você chega ao resultado de camada em camada.

**Parte 3: Aplicar e validar (8 minutos)**

5. Clique na célula H2 no Excel.
6. Digite a fórmula sugerida pelo Claude. Ela deve ser algo parecido com:

```
=PRI.MAIÚSCULA(TIRAR.ESPAÇOS(B2))
```

   Se o seu Excel estiver em inglês:

```
=PROPER(TRIM(B2))
```

7. Pressione Enter e veja o resultado.
8. Copie a fórmula para H3 até H9 (cobrindo todas as linhas com dados).

> 📸 *Sugestão de Captura de Tela:* Com a coluna H preenchida ao lado da coluna B original, tire um print — a comparação antes/depois é satisfatória de ver.

9. Verifique linha por linha:
   - H2 deve mostrar "Ana Silva" (não "ana silva")
   - H3 deve mostrar "Bruno Santos"
   - H7 deve mostrar "Fernanda Lima" (sem os espaços extras)
   - H8 deve mostrar "João Pedro Silva"
   - H9 deve mostrar "Marcos Oliveira" (com espaço duplo corrigido)

**Parte 4: E quando a fórmula não resolve tudo? (5 minutos)**

10. Voltando ao Claude, pergunte:

> A fórmula PRI.MAIÚSCULA corrige maiúsculas e espaços. Mas e se alguns nomes tiverem abreviações como "Dra." ou "Sr." que devem ficar em maiúsculas? Existe alguma forma de tratar isso no Excel ou preciso de outra ferramenta?

11. Leia a resposta — essa é uma situação real em que o Excel tem limitações, e o Claude vai dizer honestamente o que dá e o que não dá para fazer só com fórmulas.

> 💡 **Dica:** Quando o Claude diz que a fórmula tem limitações, isso não é fracasso — é a informação mais valiosa que você pode ter antes de gastar horas tentando algo que não vai funcionar.

**Parte 5: Converter os resultados em valores fixos (2 minutos)**

12. Selecione o intervalo H2:H9.
13. Copie (Ctrl+C).
14. Clique com o botão direito em H2 e escolha "Colar Especial" → "Valores" (ícone com "123" ou apenas texto, dependendo da versão).

   Isso transforma as fórmulas em texto fixo — agora você pode apagar a coluna B original se quiser, e os nomes limpos continuam lá.

### ✅ Deu certo?

A coluna H deve conter todos os nomes padronizados com a primeira letra de cada palavra em maiúscula e sem espaços extras. Se você também conseguiu converter as fórmulas em valores fixos sem perder os dados, você dominou um processo de limpeza de dados completo.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| A fórmula retorna #NOME? | Tente a versão em inglês: `=PROPER(TRIM(B2))` |
| Os espaços extras continuam aparecendo | Verifique se usou TIRAR.ESPAÇOS por fora do PRI.MAIÚSCULA, e não por dentro |
| O "Colar Especial → Valores" não aparece | Tente via menu: Início → Colar → Colar Especial → Valores |

### 🚀 Quer ir além?

- Peça ao Claude uma fórmula que também remova caracteres especiais (como acentos) dos nomes, para uso em sistemas que não aceitam acentuação.
- Experimente a função SUBS (ou SUBSTITUTE) para trocar abreviações específicas: `=SUBS(H2,"Sr.","Senhor")`.
- Pergunte ao Claude como usar Power Query para fazer limpeza de texto em bases com mais de 10.000 linhas — ele vai explicar quando vale a pena mudar de ferramenta.

---

<div style="page-break-after: always;"></div>

# Projeto Final — Mini-Dashboard de Análise de Clientes

### 🎯 A missão

Chegou o momento de juntar tudo. Você vai construir, do zero, uma aba de resumo que transforma a base de clientes em informações de verdade: quem são os melhores clientes, qual é a receita por classificação, quem está em risco. É o tipo de coisa que aparece em reuniões de gestão — e agora você sabe fazer.

O Claude vai ser o seu par nessa missão: você descreve o que precisa, ele sugere a fórmula, você aplica e valida.

### 👐 Mão na massa

**Passo 1: Criar a aba de resumo**

1. No arquivo `treino_claude.xlsx`, crie uma nova aba e chame de `Dashboard`.
2. Na célula A1, escreva `Indicador` e em B1 escreva `Valor`.
3. Preencha as etiquetas dos indicadores nas células A2 a A6:

   - A2: `Total de clientes`
   - A3: `Receita total`
   - A4: `Receita média por cliente`
   - A5: `Clientes Premium`
   - A6: `Clientes em risco`

**Passo 2: Pedir as fórmulas ao Claude**

4. Vá ao Claude e envie esta mensagem de uma vez:

> Tenho uma aba chamada "Clientes" com estas colunas:
> A = ID, B = Nome, C = Email, D = Data_Cadastro, E = Receita, F = Status, G = Classificação (valores: "Premium", "Padrão", "Em risco", "Cancelado")
>
> Os dados vão da linha 2 até a linha 9 (8 clientes).
>
> Preciso das seguintes fórmulas para uma aba de Dashboard:
> 1. Contar quantos clientes existem (total de linhas com dados)
> 2. Somar a receita total
> 3. Calcular a receita média por cliente
> 4. Contar quantos clientes têm Classificação = "Premium"
> 5. Contar quantos clientes têm Classificação = "Em risco"
>
> Me dê cada fórmula separada, já referenciando a aba Clientes.

5. Leia as fórmulas geradas.

**Passo 3: Aplicar as fórmulas**

6. Volte ao Excel, aba `Dashboard`.
7. Clique em B2 e digite (ou cole) a fórmula de total de clientes sugerida pelo Claude. Deve ser algo como:

```
=CONT.VALORES(Clientes!A2:A9)
```

8. Clique em B3 e insira a fórmula de receita total:

```
=SOMA(Clientes!E2:E9)
```

9. Clique em B4 e insira a receita média:

```
=MÉDIA(Clientes!E2:E9)
```

10. Clique em B5 e insira o contador de clientes Premium:

```
=CONT.SE(Clientes!G2:G9,"Premium")
```

11. Clique em B6 e insira o contador de clientes em risco:

```
=CONT.SE(Clientes!G2:G9,"Em risco")
```

**Passo 4: Formatar os valores**

12. Selecione B3 e B4. Vá em Início → grupo "Número" → clique no símbolo de moeda (R$) para aplicar formatação de moeda.
13. Selecione B2, B5 e B6. Aplique formatação de número inteiro (Início → Número → sem casas decimais).

> 📸 *Sugestão de Captura de Tela:* Tire um print da aba Dashboard com todos os valores preenchidos e formatados — este é o seu entregável.

**Passo 5: Adicionar o ranking de clientes**

14. Na célula D1 da aba `Dashboard`, escreva `Top Clientes por Receita`.
15. Em D2, escreva `Nome` e em E2, escreva `Receita`.
16. Vá ao Claude e pergunte:

> Na aba "Dashboard", quero mostrar os 3 clientes com maior receita, buscando os dados da aba "Clientes" (Nome na coluna B, Receita na coluna E, linhas 2 a 9). Me dê uma forma simples de fazer isso — pode ser com fórmulas ou com os passos no Excel.

17. Aplique a solução sugerida pelo Claude nas células D3:E5.

**Passo 6: Validar tudo**

18. Volte à aba `Clientes` e mude temporariamente a receita de um cliente para um valor muito alto (por exemplo, mude E3 para `200000`).
19. Volte à aba `Dashboard` e verifique se os valores mudaram automaticamente (receita total, média e classificação Premium devem se atualizar).
20. Desfaça a mudança com Ctrl+Z.

### 🏁 Como saber que terminou

- [ ] A aba `Dashboard` existe no arquivo `treino_claude.xlsx`
- [ ] A célula B2 mostra o número correto de clientes (deve ser 8)
- [ ] A célula B3 mostra a receita total calculada corretamente
- [ ] A célula B4 mostra a receita média (valor entre a menor e a maior receita da base)
- [ ] B5 e B6 mostram a contagem correta de clientes Premium e Em risco
- [ ] Quando você muda um valor na aba Clientes, o Dashboard atualiza automaticamente
- [ ] O ranking de top 3 clientes está preenchido em D3:E5
- [ ] Pelo menos uma das fórmulas foi sugerida pelo Claude e você consegue explicar o que ela faz

---

<div style="page-break-after: always;"></div>

# A Parte dos Dez — Prompts que Salvam seu Dia

Dez situações que todo mundo enfrenta no Excel — e o texto exato para pedir ajuda ao Claude em cada uma delas. Guarde esta seção; você vai voltar aqui.

**1. Descobrir por que uma fórmula está retornando erro**

> "Minha fórmula `[cole a fórmula aqui]` está retornando `[tipo de erro]`. Os dados estão assim: `[cole 3 linhas de exemplo]`. O que está errado e como corrijo?"

**2. Pedir uma fórmula que você não sabe nem o nome**

> "Preciso de uma fórmula que faça o seguinte: dados de entrada `[exemplo]`, resultado esperado `[exemplo]`. Qual função usar e como escrever?"

**3. Entender uma fórmula complicada que você herdou**

> "Encontrei esta fórmula numa planilha que recebi: `[cole a fórmula]`. Explique o que ela faz passo a passo, como se eu nunca tivesse visto essa função antes."

**4. Limpar dados bagunçados sem saber por onde começar**

> "Minha planilha tem os seguintes problemas: `[descreva ou cole uma amostra]`. Em que ordem devo limpar isso e qual fórmula uso em cada etapa?"

**5. Cruzar duas tabelas com critérios que o PROCV não resolve**

> "Tenho duas tabelas. Tabela 1: `[descreva colunas]`. Tabela 2: `[descreva colunas]`. Quero trazer `[dado]` da Tabela 2 para a Tabela 1 quando `[condição]`. Meu Excel é `[versão]`. Qual é a melhor função?"

**6. Criar uma regra de classificação com várias condições**

> "Quero classificar cada linha com base nestas regras: `[liste as regras em ordem]`. A coluna de referência é `[nome]`. Me dê a fórmula com IFS e também com SE encadeado para comparar."

**7. Fazer um cálculo condicional (somar, contar ou calcular média só para um grupo)**

> "Quero somar a coluna `[nome]` apenas para as linhas onde a coluna `[outra coluna]` seja igual a `[valor]`. Tenho `[número]` linhas. Qual é a fórmula mais eficiente?"

**8. Detectar e sinalizar duplicatas**

> "Tenho uma coluna chamada `[nome]` e quero marcar as linhas onde o valor aparece mais de uma vez. Como faço para destacar essas linhas com uma fórmula ou formatação condicional?"

**9. Automatizar uma tarefa repetitiva que você faz todo mês**

> "Todo mês eu faço os seguintes passos manualmente: `[liste cada passo]`. Qual é a forma mais simples de automatizar isso no Excel — fórmula, Power Query ou macro? Comece pela mais fácil."

**10. Validar se o resultado de uma fórmula está correto**

> "Criei esta fórmula: `[cole a fórmula]`. Os dados de teste são: `[cole 4 a 5 linhas]`. O resultado esperado é `[descreva]`. A fórmula está correta? Se não, o que precisa mudar?"

---

## Conseguiu! E agora?

Você chegou até aqui — e isso significa que você já sabe fazer coisas que a maioria das pessoas que usa Excel todo dia ainda não dominou: pedir diagnósticos estruturados, cruzar tabelas com confiança, montar lógica condicional em camadas e limpar dados bagunçados sem enlouquecer. E fez tudo isso usando o Claude como parceiro, não como muleta.

A melhor forma de continuar evoluindo é simples: toda vez que você travar num problema de Excel no trabalho ou nas aulas, antes de tentar resolver na raça, estruture uma mensagem para o Claude seguindo o que você praticou aqui. Com o tempo, você vai perceber que a habilidade mais valiosa que este curso te deu não foi nenhuma fórmula específica — foi saber fazer a pergunta certa. A partir daqui, o próximo passo natural é explorar o mundo das macros VBA (para automatizar processos repetitivos) e do Power Query (para transformar bases de dados grandes sem fórmula nenhuma). O Claude pode te acompanhar em ambos — é só pedir.