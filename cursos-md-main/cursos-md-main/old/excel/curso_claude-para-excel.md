<link rel="stylesheet" href="../.css/style.css">

# Use Claude para Excel
## Consultoria Analítica, Fórmulas Complexas e Automação com IA

**Versão:** 2.0 (Reformulada)  
**Público-alvo:** Analistas de dados, gestores de projetos, acadêmicos, profissionais de BI  
**Pré-requisitos:** Excel básico (conhecer célula, coluna, linha) ou superior  
**Tempo total:** 12-16 horas (distribuídas em 15 aulas)  
**Objetivo geral:** Usar Claude como consultor para análise de dados, geração de fórmulas, limpeza e automação de tarefas repetitivas em Excel.

---

# ÍNDICE DE CONTEÚDO

1. [Módulo 1: Fundações](#módulo-1-fundações)
   - Aula 1.1: Claude como Consultor Técnico
   - Aula 1.2: Arquitetura de Dados e Documentação Estruturada
   
2. [Módulo 2: Engenharia de Prompts para Dados](#módulo-2-engenharia-de-prompts-para-dados)
   - Aula 2.1: Estruturando Contexto de Dados
   - Aula 2.2: Padrões de Prompt para Análise
   - Aula 2.3: Troubleshooting de Respostas Inadequadas

3. [Módulo 3: Fórmulas do Básico ao Avançado](#módulo-3-fórmulas-do-básico-ao-avançado)
   - Aula 3.1: Fórmulas de Busca (PROCV, XLOOKUP, ÍNDICE/CORRESP)
   - Aula 3.2: Lógica Condicional Complexa (SE Encadeado, IFS, SWITCH)
   - Aula 3.3: Cálculos Estatísticos Avançados
   - Aula 3.4: Fórmulas Matriciais (FILTRO, CLASSIFICAR, ÚNICA)

4. [Módulo 4: Limpeza e Tratamento de Dados](#módulo-4-limpeza-e-tratamento-de-dados)
   - Aula 4.1: Diagnóstico de Dados Sujos
   - Aula 4.2: Normalização de Texto e Datas
   - Aula 4.3: Remoção de Duplicatas e Detecção de Anomalias
   - Aula 4.4: Transformação de Dados com Power Query

5. [Módulo 5: Análise Exploratória e Insights](#módulo-5-análise-exploratória-e-insights)
   - Aula 5.1: Diagnóstico Rápido de Dataset
   - Aula 5.2: Análise Descritiva e Estatística
   - Aula 5.3: Recomendações de Visualização
   - Aula 5.4: Detecção de Padrões e Tendências

6. [Módulo 6: Automação com VBA e Python](#módulo-6-automação-com-vba-e-python)
   - Aula 6.1: Introdução a VBA com Claude
   - Aula 6.2: Macros Reutilizáveis
   - Aula 6.3: Integração Python + Excel (Pandas)
   - Aula 6.4: Orquestração de Workflows

7. [Módulo 7: Integração e Casos Reais](#módulo-7-integração-e-casos-reais)
   - Aula 7.1: Estudo de Caso 1 – Análise de Vendas
   - Aula 7.2: Estudo de Caso 2 – Processamento de RH
   - Aula 7.3: Estudo de Caso 3 – Relatório Acadêmico Automático

---

---

# MÓDULO 1: FUNDAÇÕES

## Aula 1.1: Claude como Consultor Técnico

### Subseção 1.1.1: O Paradigma de Consultoria com IA

**📸 Sugestão de Prints:**
- Captura de tela mostrando o painel Claude aberto ao lado de Excel desktop
- Imagem de um prompt bem estruturado no Claude (lado esquerdo) com resultado em tabela (lado direito)
- Screenshot de um erro #REF! ao lado de um chat Claude explicando o problema

**Descrição:**

Claude não é apenas um "assistente" que responde perguntas. Neste curso, você aprenderá a usá-lo como um **consultor técnico especializado** que:

1. **Entende contexto:** Se você descrever sua planilha com clareza, Claude "vê" a estrutura de dados
2. **Sugere soluções:** Oferece múltiplas abordagens (fórmula simples vs matricial vs VBA)
3. **Depura problemas:** Analisa erros e propõe correções
4. **Gera código:** Escreve fórmulas, macros e scripts Python prontos para usar
5. **Educa:** Explica *por que* uma solução funciona, não apenas *como* fazer

**Diferença crítica:** Este NÃO é um curso sobre "usar Excel com IA". É um curso sobre **usar Claude para dominar Excel de forma autossuficiente**, resolvendo problemas reais sem especialista humano ao lado.

**Objetivos da Aula:**
- Compreender o papel de Claude como consultor técnico
- Entender quando usar Claude vs resolver sozinho
- Estabelecer padrão de comunicação eficaz

**Habilidades Esperadas:**
- Reconhecer situações em que Claude é mais útil
- Formular perguntas técnicas de forma estruturada
- Interpretar respostas técnicas e implementar sugestões

---

### Subseção 1.1.2: Paradigma de Uso – Quando Chamar Claude

**Flowchart Mental:**

```
┌─ Tenho um problema em Excel
│
├─ Erro visível (#REF!, #VALUE!, etc)? 
│  └─ SIM → Claude [Diagnóstico] → Solução → Implementar
│
├─ Não sei como fazer algo? 
│  └─ SIM → Claude [Alternativas] → Escolher → Aprender
│
├─ Preciso de fórmula complexa?
│  └─ SIM → Claude [Código] → Testar → Adaptar
│
├─ Dúvida sobre lógica de negócio?
│  └─ Talvez → Claude [Contexto] → Discutir → Refinar
│
└─ Preciso automatizar tarefa repetitiva?
   └─ SIM → Claude [Macro/Script] → Implementar → Testar
```

**Padrão de Consultoria:**

1. **Diagnóstico:** Descrever o problema com máximo detalhe
2. **Exploração:** Pedir múltiplas soluções, não apenas uma
3. **Implementação:** Testar a solução em escopo pequeno primeiro
4. **Validação:** Conferir resultado vs expectativa
5. **Escalação:** Aplicar a múltiplos contextos após validação

**Exemplo Real: Problema de Duplicatas em Base de Dados**

```
ERRADO:
"Tenho duplicatas na minha planilha. Como remove?"

CORRETO:
"Tenho uma planilha com 10.000 registros de clientes.
Colunas: ID, Nome, Email, Data_Cadastro, Status.
Dupostas aparecem por: mesmo Email mas ID diferentes.
Objetivo: Manter registro mais antigo (Data_Cadastro menor), deletar duplicatas.
Qual é a melhor abordagem: fórmula, Power Query ou VBA?
Preciso dos IDs deletados para auditoria."
```

O segundo prompt tem **contexto, restrições e objetivo claro**. Claude responderá com soluções práticas e justificadas.

---

### Subseção 1.1.3: Configuração Inicial – Claude + Excel Desktop

**📸 Sugestão de Prints:**
- Tela de login Claude (web ou desktop)
- Menu de configurações de Claude destacando "Data Analysis" ou "Code Execution"
- Excel desktop com extensão Claude ativada (se disponível) ou Claude web ao lado

**Passo a Passo de Setup:**

1. **Acesse Claude:**
   - Opção A: www.claude.ai (navegador)
   - Opção B: Claude Desktop (se instalado)

2. **Crie uma Pasta de Projeto:**
   - Navegador: Criar novo chat com nome "Projeto [Nome]"
   - Desktop: Novo projeto nomeado

3. **Prepare seu Workspace:**
   - Abra Excel em uma janela
   - Abra Claude em outra janela (lado a lado)
   - Zoom em ambas para conforto visual

4. **Teste Conectividade:**
   - No Claude, copie e cole uma planilha pequena (5 linhas, 3 colunas)
   - Peça: "Analise esta estrutura de dados"
   - Verifique se Claude reconhece corretamente

**Boas Práticas de Workspace:**

```
Configuração 1 (Monitor Único):
┌──────────────────┬──────────────────┐
│                  │                  │
│     EXCEL        │     CLAUDE       │
│  (esquerda)      │   (direita)      │
│                  │                  │
│ Planilha         │ Chat com código  │
│ Célula ativa     │ e explicações    │
│                  │                  │
└──────────────────┴──────────────────┘

Configuração 2 (Monitors Duais - Ideal):
┌──────────────────┐  ┌──────────────────┐
│                  │  │                  │
│     EXCEL        │  │     CLAUDE       │
│   (Monitor 1)    │  │  (Monitor 2)     │
│                  │  │                  │
└──────────────────┘  └──────────────────┘
```

**Checklist Inicial:**

```markdown
✓ Claude acessível (web ou desktop)
✓ Excel instalado (versão 2019 ou Microsoft 365)
✓ Internet estável (Claude requer conexão)
✓ Exemplos de dados salvos em pasta local
✓ Editor de texto (Notepad++, VS Code) aberto para copiar/colar código
```

**Habilidades Esperadas ao Fim da Aula:**
- Acessar Claude e Excel simultaneamente
- Entender quando chamar Claude (diagnóstico, fórmulas, automação)
- Estruturar pergunta com contexto adequado

---

## Aula 1.2: Arquitetura de Dados e Documentação Estruturada

### Subseção 1.2.1: Entendendo Estrutura de Dados

**📸 Sugestão de Prints:**
- Tabela "bem estruturada" com cabeçalhos em negrito, colunas de tipo consistente
- Tabela "mal estruturada" com cabeçalhos em múltiplas linhas, dados formatados inconsistentemente
- Comparação lado a lado: "Bom" vs "Ruim"

**Descrição:**

Antes de usar Claude, você precisa **entender e comunicar a estrutura de seus dados**. Isso é crítico porque:

1. **Claude processa melhor dados organizados** – Se sua tabela é confusa, a resposta será confusa
2. **Você entenderá melhor o problema** – Documentar obriga análise prévia
3. **Soluções serão reutilizáveis** – Padrões claros = automação confiável

**Anatomia de uma Tabela Bem Estruturada:**

```
ID | Nome         | Email              | Data_Cadastro | Salário | Status
---|--------------|--------------------|----|-----------|--------
1  | João Silva   | joao@empresa.com   | 2020-03-15 | 3500.00 | Ativo
2  | Maria Santos | maria@empresa.com  | 2021-07-22 | 4200.00 | Ativo
3  | Pedro Oliveira| pedro@empresa.com | 2019-11-08 | 3800.00 | Inativo
```

**Elementos de Boa Estrutura:**

| Elemento | Descrição | Exemplo |
|----------|-----------|---------|
| **Cabeçalho** | Primeira linha com nomes claros de colunas | "Data_Cadastro" (não "Data" ou "D1") |
| **Tipo Consistente** | Cada coluna tem um tipo de dado único | Salário sempre número, nunca "R$ 3500" |
| **Sem Merged Cells** | Células mescladas quebram análise | Evite ao máximo |
| **Sem Linhas em Branco** | Entre dados só use dados, sem espaços | Limpe antes de analisar |
| **Índice Único** | Coluna que identifica unicamente cada linha | ID, Email, CPF (depende do contexto) |
| **Data Padrão** | Datas em formato ISO (AAAA-MM-DD) ou consistente | 2024-01-15 (não 15/01/2024 misturado) |

---

### Subseção 1.2.2: Documentação de Dados para Claude

**O "Dicionário de Dados" – Seu Guia Técnico**

Antes de pedir ajuda ao Claude, crie um documento simples descrevendo sua base:

```markdown
# Dicionário de Dados – Base de Clientes (vendas.xlsx)

## Descrição Geral
Base com 5,234 clientes ativos e inativos.
Período: Jan 2019 – Dez 2024.
Atualização: Diária (via sistema CRM).

## Colunas

### ID (Tipo: Inteiro)
- Descrição: Identificador único do cliente
- Formato: Número (ex: 12345)
- Obrigório: Sim
- Chave: Primária

### Nome (Tipo: Texto)
- Descrição: Nome completo do cliente
- Formato: Texto até 100 caracteres
- Obrigório: Sim
- Padrão: Nome próprio + Sobrenome

### Email (Tipo: Texto)
- Descrição: E-mail de contato
- Formato: Email válido (ex: nome@dominio.com)
- Obrigatorio: Sim
- Notas: Pode ter duplicatas de registros antigos

### Data_Cadastro (Tipo: Data)
- Descrição: Quando o cliente foi criado no sistema
- Formato: ISO (AAAA-MM-DD)
- Obrigatorio: Sim
- Intervalo: 2019-01-01 a 2024-12-31

### Status (Tipo: Categórico)
- Descrição: Situação atual do cliente
- Valores válidos: Ativo, Inativo, Suspenso, Bloqueado
- Obrigatorio: Sim
- Padrão: Ativo para novos

### Receita_Total (Tipo: Moeda)
- Descrição: Soma de todas as vendas do cliente (em R$)
- Formato: Número com 2 casas decimais
- Obrigatorio: Não (pode ser NULL para novos)
- Intervalo: 0 a 999.999,99

## Relacionamentos
- ID é chave única (não há duplicatas esperadas)
- Email pode ter duplicatas (registros antigos de mesmo cliente com email diferente)

## Possíveis Anomalias
- ~200 registros com Email vazio (dados legados)
- Alguns Status não foram atualizados desde 2021
- Receita_Total pode estar desatualizada (última sync: 2024-12-15)
```

**Por Que Isso Importa?**

Quando você envia este dicionário ao Claude junto com uma pergunta, ele:

1. **Compreende melhor** o contexto
2. **Faz suposições corretas** sobre tipo de dados
3. **Sugere soluções apropriadas** (não vai sugerir fórmula matrizcial se os dados são simples)
4. **Identifica problemas** que você não veria (anomalias, inconsistências)

---

### Subseção 1.2.3: Exercício Prático – Documentar Sua Base

**📸 Sugestão de Prints:**
- Screenshot de planilha do usuário (anônimizada)
- Comparação: "Documentação Vaga" vs "Documentação Completa"

**Tarefa 1: Análise Inicial (15 min)**

Pegue uma planilha que você usa regularmente:

1. Abra em Excel
2. Identifique:
   - Quantas colunas?
   - Quantas linhas?
   - Qual é a chave única (se houver)?
   - Há dados incompletos (vazios)?
   - Há dados que parecem "sujos" (formatados inconsistentemente)?

3. Escreva em arquivo de texto:

```
Minha Base de Dados: [Nome]

Tamanho: [X colunas] × [Y linhas]
Colunas: [Listar nomes]
Tipo de Dado: [Descrever tipo: texto, número, data]
Problemas Óbvios: [Listar qualquer coisa estranha]

Pergunta para Claude:
"Analise a estrutura desta base e identifique problemas potenciais."
```

**Tarefa 2: Copiar para Claude (5 min)**

1. Copie as primeiras 10 linhas da planilha (incluindo cabeçalho)
2. Cole no Claude com o texto acima
3. Peça: "Identifique problemas de estrutura e sugira melhorias"

**Tarefa 3: Implementar Sugestões (30-45 min)**

Com base na resposta de Claude:
- Se houver problemas estruturais óbvios, corrija
- Se Claude sugerir reorganizar colunas, teste a sugestão em um backup
- Documente o dicionário de dados completo (use template acima)

**Habilidades Esperadas ao Fim:**
- Entender anatomia de tabela bem estruturada
- Crear dicionário de dados básico
- Comunicar problema estrutural ao Claude com clareza

---

---

# MÓDULO 2: ENGENHARIA DE PROMPTS PARA DADOS

## Aula 2.1: Estruturando Contexto de Dados

### Subseção 2.1.1: O Prompt Estruturado para Análise

**📸 Sugestão de Prints:**
- Prompt bem estruturado em Claude (com seções: Contexto, Dados, Objetivo, Restrições)
- Resposta detalhada de Claude com múltiplas sugestões
- Comparação lado a lado: "Prompt Vago" vs "Prompt Estruturado"

**Descrição:**

Um bom prompt segue esta estrutura (adaptada de "Chain of Thought"):

```markdown
## CONTEXTO
[O que é este projeto? Por que importa? Quem usa?]

## DADOS
[Descrever estrutura, tamanho, fonte]

## OBJETIVO
[O que você quer fazer com os dados?]

## RESTRIÇÕES
[Limites técnicos, operacionais, legais]

## EXEMPLO DE DADOS
[Amostra real (5-10 linhas) ou exemplo fictício]

## PERGUNTA ESPECÍFICA
[O que você quer saber ou fazer?]
```

**Exemplo Completo: Análise de Evasão em Universidade**

```markdown
## CONTEXTO
Universidade pública com 15.000 alunos.
Problema: Taxa de evasão aumentou de 8% (2019) para 15% (2024).
Objetivo estratégico: Identificar padrões para criar retenção focada.

## DADOS
Arquivo: alunos_2024.xlsx
Período: Inscrição inicial até semestre atual (10 semestres)
Tamanho: 12.500 registros (histórico), 3.200 atuais, 2.100 evadidos

Colunas:
- Matricula (ID único)
- Data_Inscricao (quando entrou)
- Curso (ex: Engenharia, Administração)
- Semestre_Inicial (semestre de entrada)
- Situacao (Ativo, Evadido, Formado, Trancado)
- Data_Evasao (quando saiu, se evadido)
- Nota_Media (GPA médio até saída/atual)
- Bolsa (Sim/Não)
- Idade_Inicial (quando entrou)
- Municipio_Origem

## OBJETIVO
Identificar:
1. Quais cursos têm maior taxa de evasão?
2. Qual semestre tem maior abandono?
3. Há correlação entre nota média e evasão?
4. Bolsa reduz risco de evasão?
5. Qual é o "ponto crítico" de decisão (qual semestre decidem sair)?

## RESTRIÇÕES
- Não temos dados de renda (não enviar dados pessoais sensíveis)
- Análise é anonimizada (sem nomes individuais)
- Precisamos de recomendação prática para ação (não apenas diagnóstico)

## EXEMPLO DE DADOS
| Matricula | Data_Inscricao | Curso | Semestre_Inicial | Situacao | Data_Evasao | Nota_Media | Bolsa | Idade_Inicial | Municipio_Origem |
|-----------|---|----------|---|---|---|---|---|---|---|
| 2019001 | 2019-03-15 | Engenharia | 1 | Formado | - | 7.2 | Sim | 18 | São Paulo |
| 2019002 | 2019-03-15 | Administração | 1 | Evadido | 2021-08 | 5.1 | Não | 22 | Santos |
| 2020001 | 2020-02-10 | Administração | 1 | Ativo | - | 6.8 | Sim | 19 | Campinas |
| 2020002 | 2020-02-10 | Engenharia | 1 | Evadido | 2020-11 | 4.2 | Não | 20 | São Paulo |

## PERGUNTA ESPECÍFICA
1. Qual é a taxa de evasão por curso? (Fórmula ou tabela dinâmica?)
2. Crie uma análise de coorte: por semestre de entrada, qual % completou curso?
3. Quais são as recomendações para reduzir evasão? (Baseadas nos dados)
```

**Anatomia do Prompt Estruturado:**

| Seção | Por Quê | Exemplo |
|-------|--------|---------|
| **Contexto** | Claude entender por que importa | "Reduzir evasão é prioridade 2024" |
| **Dados** | Claude saber tamanho/tipo | "12k registros, dados históricos" |
| **Objetivo** | Claude entregar o certo | "Identificar padrões, não apenas contar" |
| **Restrições** | Claude evitar armadilhas | "Não enviar dados pessoais sensíveis" |
| **Exemplo** | Claude "ver" estrutura real | Amostra de 4-5 linhas |
| **Pergunta** | Claude focar resposta | Máximo 3-5 perguntas específicas |

---

### Subseção 2.1.2: Padrões de Contexto por Tipo de Tarefa

**📸 Sugestão de Prints:**
- Exemplos de 3 prompts diferentes (um para cada tipo: análise, fórmula, automação)
- Respostas do Claude para cada um
- Checklist: "Meu prompt tem todas essas seções?"

**Padrão 1: Análise Exploratória (EDA)**

```markdown
## CONTEXTO
[Qual é o negócio/academia? Por que essa análise?]

## DADOS
Tamanho: X linhas × Y colunas
Fonte: [Base de dados, arquivo, API]
Período temporal: [De quando até quando]

## OBJETIVO
Entender: [Comportamentos, tendências, anomalias]
Saída desejada: [Gráficos, tabela, recomendação]

## EXEMPLO DE DADOS
[Amostra com todos os tipos de coluna]

## PERGUNTAS
1. Qual é a distribuição de [métrica]?
2. Há correlação entre [col1] e [col2]?
3. Quais são os outliers?
4. Recomende 2-3 visualizações úteis
```

**Padrão 2: Geração de Fórmula Complexa**

```markdown
## CONTEXTO
[O que você tenta resolver? Qual é o uso final?]

## ESTRUTURA DE DADOS
Tabela: [Nome da tabela em Excel]
Colunas relevantes: [Listar]
Tipo de busca: [Simples, múltipla, condicional]

## DESAFIO ESPECÍFICO
[O que você tentou? Por que não funciona?]

## EXEMPLO
[Dados de entrada] → [Resultado desejado]

## RESTRIÇÕES
- Performance: [Precisa ser rápido? Muitas linhas?]
- Excel versão: [2019, 365, Web?]
- Versão anterior do resultado: [Copiar fórmula que tentou]

## PERGUNTA
Qual é a melhor abordagem?
a) Fórmula única (performance)
b) Fórmula matricial (elegância)
c) Coluna auxiliar (clareza)
d) Sugerir alternativa
```

**Padrão 3: Automação / Macro**

```markdown
## CONTEXTO
[Qual é a tarefa repetitiva? Quantas vezes por semana?]

## PROCESSO MANUAL ATUAL
Passo 1: [Descrever]
Passo 2: [Descrever]
Passo 3: [Descrever]
...
Tempo gasto: [X minutos/horas]

## DADOS ENVOLVIDOS
[Origem dos dados → Destino]
[Formato de entrada → Formato de saída]

## RESTRIÇÕES TÉCNICAS
- Plataforma: [Excel desktop / Web / Python]
- Frequência: [Diária, semanal, mensal]
- Quem executa: [Você mesmo, usuário sem TI, departamento inteiro]

## EXEMPLO
[Dados de entrada] → [Processo esperado] → [Resultado final]

## PERGUNTA
Qual é a melhor forma de automatizar?
- VBA Macro
- Power Query
- Python + Pandas
- Integração com outro sistema
```

---

### Subseção 2.1.3: Exercício Prático – Seu Primeiro Prompt Estruturado

**📸 Sugestão de Prints:**
- Tela do Claude com prompt estruturado do usuário
- Resposta de Claude (parcial, mostrando início)
- Checklist preenchido

**Tarefa: Analisar Sua Base com Prompt Estruturado**

**Tempo:** 30 minutos

1. **Pegue um problema real (15 min):**
   - Uma planilha que você usa regularmente
   - Um desafio que nunca resolveu bem
   - Exemplo: "Sempre levo 1 hora para gerar relatório mensal"

2. **Estruture o prompt (15 min):**

   Abra um editor de texto e preencha:

   ```markdown
   ## CONTEXTO
   [Descrever seu cenário em 2-3 linhas]
   
   ## DADOS
   Tamanho:
   Período:
   Fonte:
   
   ## OBJETIVO
   [O que você quer fazer?]
   
   ## EXEMPLO
   [Copiar 5 linhas reais de sua planilha aqui]
   
   ## PERGUNTA
   [Formular 1-3 perguntas específicas]
   ```

3. **Enviar para Claude (Imediato):**
   - Copiar texto + tabela de exemplo
   - Colar no Claude
   - Ler resposta completa

4. **Avaliar resposta:**
   - Claude entendeu seu problema?
   - Resposta é prática (não genérica)?
   - Há sugestões que você não esperava?

5. **Iteração (opcional):**
   - Perguntar: "E se eu também quisesse [variação]?"
   - Ou: "Explique a fórmula em detalhes"

**Checklist: Seu Prompt Foi Bem Estruturado?**

```markdown
✓ Contexto tem 2-4 linhas (o suficiente)
✓ Dados descrevem tamanho, período, fonte
✓ Objetivo é claro (não vago como "analisar")
✓ Exemplo tem estrutura real (com nomes reais de colunas)
✓ Pergunta é específica (não "como faço tudo?")
✓ Prompt tem ~200-400 palavras (concentrado, não romance)
```

**Habilidades Esperadas ao Fim:**
- Estruturar prompt para análise, fórmula ou automação
- Saber quando adicionar/remover informação
- Reconhecer resposta de Claude adequada vs inadequada

---

## Aula 2.2: Padrões de Prompt para Análise

### Subseção 2.2.1: Padrões de Pergunta por Tipo de Análise

**📸 Sugestão de Prints:**
- 4 exemplos de prompts lado a lado (um para cada tipo)
- Respostas correspondentes
- Tabela: Tipo de Análise → Padrão de Prompt

**Descrição:**

Diferentes perguntas requerem diferentes estruturas. Aqui estão 4 padrões:

#### **Padrão A: Análise Descritiva ("O que aconteceu?")**

Objetivo: Resumir dados, encontrar padrões simples.

```markdown
Tenho uma base de vendas com 5.000 registros.
Colunas: Produto, Mes, Valor_Venda, Regiao, Vendedor.
Período: Jan 2023 – Dez 2024.

Quero entender:
1. Qual foi a venda total por região?
2. Qual mês teve maior volume?
3. Top 3 produtos por receita?
4. Qual vendedor realizou mais vendas?

Gere fórmulas para cada métrica (prefiro SUMIF sobre Tabela Dinâmica).
```

**Resposta Esperada:**
- 4 fórmulas simples (SUMIF, MAX, LARGE, COUNTIF)
- Orientação sobre aonde colocar cada uma
- Explicação do resultado

---

#### **Padrão B: Análise Comparativa ("Como se compara?")**

Objetivo: Comparar grupos, períodos, segmentos.

```markdown
Base: Matrículas universitárias 2019-2024.
Colunas: Matricula, Curso, Semestre_Entrada, Status (Ativo/Evadido/Formado).

Quero comparar:
1. Taxa de evasão: Cursos STEM vs Humanas?
2. Tempo médio até conclusão: Por período de entrada?
3. Qual coorte (ano de entrada) teve melhor taxa de formação?

Preciso de uma tabela de comparação (não individual).
Qual é a melhor forma: fórmula matricial, Tabela Dinâmica ou Power Query?
```

**Resposta Esperada:**
- Recomendação de ferramenta (TP > Fórmula > PQ, depende volume)
- Fórmulas ou passos no Power Query
- Tabela resultado com 3-4 comparações

---

#### **Padrão C: Análise Preditiva ("O que acontecerá?")**

Objetivo: Prever baseado em padrões históricos.

```markdown
Base: Histórico de churn de clientes.
Colunas: Cliente_ID, Data_Cadastro, Mes_Ultcomp, Dias_Inativo, Score_Satisfacao, Churn (Sim/Não).
Tamanho: 2.000 clientes históricos.

Pergunta:
1. Qual é o padrão que precede churn?
   (Ex: "Clientes inativos há 90+ dias com score < 3 têm 80% churn")
2. Baseado nesses padrões, quem está em risco agora?
3. Qual é a ação recomendada?

Prefiro análise baseada em regras (não ML complexo).
```

**Resposta Esperada:**
- Correlações identificadas (dias_inativo vs churn, score vs churn)
- Regra simples (ex: "Score < 3 AND Dias_Inativo > 90")
- Lista de clientes em risco com risco score

---

#### **Padrão D: Análise Diagnóstica ("Por quê?")**

Objetivo: Entender causas, anomalias, outliers.

```markdown
Base: Vendas B2B de software.
Período: Jan-Dez 2024.

Anomalia observada:
- Vendas cresceram 15% ao ano (esperado)
- Mas em outubro caíram 30%
- Em novembro, recuperaram

Pergunta:
1. Qual é a causa provável? (Não temos dados externos)
2. Quais contas foram mais afetadas?
3. Há padrão sazonal que explica?
4. O que mudar para evitar repetição?

Dados disponíveis: Valor, Cliente, Produto, Vendedor, Data.
```

**Resposta Esperada:**
- Análise de dados à mão (sem especulação)
- Identificação de contas anômalas
- Perguntas de follow-up para confirmar hipótese
- Sugestão de dados a coletar

---

### Subseção 2.2.2: Exemplos de Prompt por Domínio

**📸 Sugestão de Prints:**
- Matriz: Domínio × Tipo de Análise (ex: RH → Descritiva, Vendas → Comparativa)
- 2-3 prompts de exemplo por domínio
- Respostas em Markdown (destacando fórmulas ou código)

**Domínio 1: Recursos Humanos (RH)**

```markdown
### Análise Descritiva: Remuneração
Contexto: 500 colaboradores, 10 departamentos.
Pergunta: "Qual é o salário médio por departamento? Há disparidade?"
Saída: Tabela com Depto | Média | Mín | Máx | Mediana

### Análise Comparativa: Rotatividade
Contexto: 3 anos de dados de admissão/demissão.
Pergunta: "Qual departamento tem maior rotatividade? Mudou ao longo dos anos?"
Saída: Gráfico de tendência + tabela por período

### Análise Diagnóstica: Anomalia de Desempenho
Contexto: Avaliação anual de performance.
Pergunta: "Esse gerente tem notas muito altas para todos os subordinados. É real ou favorecimento?"
Saída: Comparação vs média da empresa, distribuição de notas
```

**Domínio 2: Vendas**

```markdown
### Análise Descritiva: Performance
Contexto: 50 vendedores, dados diários de 2024.
Pergunta: "Qual é o ranking de vendedores? Quem está acima/abaixo da meta?"
Saída: Ranking com % de meta, distribuição por quintil

### Análise Comparativa: Produtividade por Canal
Contexto: 4 canais (direto, web, parceiros, marketplace).
Pergunta: "Qual canal é mais lucrativo? Qual tem maior ticket médio?"
Saída: Comparativa multimétricas + sugestão de realocação de recursos

### Análise Preditiva: Risco de Churn
Contexto: Clientes B2B, últimas 2 compras, score de satisfação.
Pergunta: "Quem está em risco de sair? Qual é o padrão?"
Saída: Segmentação por risco + ações recomendadas por segmento
```

**Domínio 3: Financeiro/Controladoria**

```markdown
### Análise Descritiva: Receita vs Despesa
Contexto: 24 meses de DRE por centro de custo.
Pergunta: "Qual centro tem maior margem? Há sazonalidade?"
Saída: Tabela com margem % e gráfico de tendência

### Análise Diagnóstica: Desvio Orçamentário
Contexto: Orçado vs Realizado nos últimos 12 meses.
Pergunta: "Qual centro está com maior desvio? Quem está melhor?"
Saída: Tabela com desvio % + variância de tendência + centros fora de controle

### Análise Preditiva: Fluxo de Caixa
Contexto: Histórico de recebimentos, ciclo de vendas.
Pergunta: "Qual é o fluxo esperado para os próximos 3 meses? Há risco de caixa?"
Saída: Projeção por mês + alertas de meses críticos
```

**Domínio 4: Manufatura/Supply Chain**

```markdown
### Análise Descritiva: Eficiência de Produção
Contexto: Dados de produção horária, refugo, paradas.
Pergunta: "Qual turno tem melhor OEE? Quais são os principais gargalos?"
Saída: Ranking de turno + causa raiz de paradas

### Análise Comparativa: Performance de Fornecedores
Contexto: 30 fornecedores, 2 anos de pedidos, prazo de entrega, qualidade.
Pergunta: "Quem tem melhor prazo de entrega? Quem tem melhor qualidade?"
Saída: Score agregado + matriz de fornecedores (Qualidade × Prazo)

### Análise Diagnóstica: Outlier de Custo
Contexto: Custo de matéria-prima diária.
Pergunta: "Por que o custo disparou em 3 dias em agosto? É normal ou anomalia?"
Saída: Decomposição de causas + correlação com eventos externos conhecidos
```

---

### Subseção 2.2.3: Ejercicio Prático – Três Prompts, Três Respostas

**Tarefa: Criar 3 Prompts para Seu Contexto**

**Tempo:** 1 hora (20 min cada)

Escolha um domínio e crie:

1. **Prompt Descritivo:** "Como está a situação geral?"
2. **Prompt Comparativo:** "Como se comparam os grupos?"
3. **Prompt Preditivo/Diagnóstico:** "Por quê? O que acontecerá?"

**Exemplo Preenchido (Vendas Online):**

```markdown
### 1. DESCRITIVA – Performance Geral de Vendas
Contexto: Loja online com 6 meses de dados.
Colunas: Data, Produto, Categoria, Valor, Quantidade, Vendedor, Origem_Trafego.

Pergunta:
1. Qual é a receita total? Ticket médio?
2. Qual categoria é mais vendida (em quantidade vs faturamento)?
3. Há sazonalidade semanal/diária?

Saída: Tabela com métricas principais + gráfico de tendência

---

### 2. COMPARATIVA – Por Origem de Tráfego
Contexto: Mesma base.

Pergunta:
1. Qual origem de tráfego tem maior conversão? Maior ticket?
2. Qual é mais eficiente (receita vs custo de aquisição)?
3. Há diferença no comportamento de compra por origem?

Saída: Tabela comparativa + recomendação de onde investir

---

### 3. PREDITIVA/DIAGNÓSTICA – Churn de Clientes
Contexto: Clientes que compraram no mês 1, voltaram a comprar nos meses seguintes?

Pergunta:
1. Qual é a taxa de retenção por mês?
2. Qual é o ciclo de compra médio?
3. Há padrão no momento que o cliente volta (ou não volta)?

Saída: Coorte análise + previsão de quem deve ser convidado a voltar
```

**Checklist: Seus 3 Prompts Estão Bons?**

```markdown
✓ Contexto e dados descritos brevemente
✓ Pergunta é específica (não genérica)
✓ Saída esperada é clara
✓ Cada um aborda tipo diferente de análise
✓ Prompts foram estruturados, não apenas "faça análise"
```

**Habilidades Esperadas ao Fim:**
- Reconhecer tipo de análise necessária para problema
- Estruturar prompt apropriado para cada tipo
- Antecipar tipo de resposta esperada

---

## Aula 2.3: Troubleshooting de Respostas Inadequadas

### Subseção 2.3.1: Quando Claude Não Entende (e Como Corrigir)

**📸 Sugestão de Prints:**
- Prompt vago com resposta genérica
- Mesmo prompt reformulado com resposta específica
- Iteração: pergunta de follow-up → resposta refinada

**Descrição:**

Às vezes Claude entende errado ou responde genericamente. Isso geralmente significa que **você não foi específico o bastante**.

**Problema 1: Resposta Genérica/Superficial**

```
ERRADO:
Você: "Tenho uma planilha com vendas. Como analiso?"
Claude: "Você pode usar SUMIF, AVERAGE, etc... também pode fazer gráficos..."
[Resposta muito vaga, sem tomar decisão]

CORRETO:
Você: "Tenho 10.000 registros de vendas mensais por vendedor.
Objetivo: Identificar top 10% de vendedores para programa de incentivo.
Qual métrica escolher (receita, número de deals, margem)?
E qual é a fórmula para ranking?"

Claude: "Para B2B, número de deals é bom proxy de atividade.
Fórmula: =RANK(E2, $E$2:$E$10001, 0) para ranking descendente.
Top 10% = PERCENTILE($E$2:$E$10001, 0.9)
Vendedores acima desse percentil entram no programa."
[Resposta específica com justificativa e fórmula]
```

**Problema 2: Entendimento Errado da Estrutura**

```
ERRADO:
Você: "Preciso combinar dados de duas planilhas"
[Claude assume que são como join em SQL, sugere PROCV]
[Mas na verdade você quer concatenar valores, não buscar]

CORRETO:
Você: "Tenho 2 planilhas:
Planilha 1: ID, Nome, Email
Planilha 2: ID, Telefone, Endereço

Quero: Uma planilha única com ID, Nome, Email, Telefone, Endereço.
É tipo SQL JOIN na coluna ID, mantendo todos os registros de P1."

Claude: "Use PROCV ou XLOOKUP para trazer Telefone e Endereço da P2."
[Agora entendido corretamente]
```

**Problema 3: Resposta Tecnicamente Correta Mas Impraticável**

```
ERRADO:
Claude sugere fórmula matricial complexa de 200 caracteres
Você tenta copiar, Excel reclama, não funciona direito
"Por quê Claude fez isso tão complicado?"

REALIDADE:
Claude pode não ter entendido sua restrição de Excel (versão, compat)
Ou não considerou que você precisa de legibilidade

CORRETO:
Você (seguindo): "A fórmula funciona, mas é muito complexa.
Posso usar coluna auxiliar em vez de fórmula única?
Preciso que seja legível para o próximo analista."

Claude: "Claro. Aqui está em 3 passos:
Col1: [Fórmula simples]
Col2: [Fórmula simples]
Col3: [Resultado final]
Cada passo tem explicação."
```

---

### Subseção 2.3.2: Estratégias de Iteração (Follow-up)

**📸 Sugestão de Prints:**
- Conversa Claude: Pergunta original → Resposta 1 → Follow-up 1 → Resposta 2
- Anotação: "Pontos de refinamento" em cada etapa

**Estratégia 1: Pedindo Alternativas**

```markdown
Você (original): "Qual é a melhor forma de contar duplicatas?"

Claude: "Use COUNTIF."

Você (follow-up): "Entendi COUNTIF. Mas há outras formas?
Qual é mais eficiente se tenho 100.000 linhas?
Qual é mais legível?"

Claude: "Opção 1 (COUNTIF) - Legível mas lento em 100k linhas.
Opção 2 (Tabela Dinâmica) - Rápida mas precisa configurar.
Opção 3 (Power Query) - Mais potente, precisa de setup.
Para 100k linhas, recomendo Power Query."
```

**Estratégia 2: Pedindo Explicação Detalhada**

```markdown
Você (original): "Crie uma fórmula para calcular margem de lucro."

Claude: [Sugere fórmula]

Você (follow-up): "Entendi a fórmula. Mas explique passo a passo:
1. Por que dividir por preço de venda e não de custo?
2. Esse é o método certo para indústria (não comércio)?
3. Como tratar linhas com custo zero ou preço negativo?"

Claude: [Explicação detalhada + exceções + variantes]
```

**Estratégia 3: Pedindo Validação/Teste**

```markdown
Você: [Sua tentativa de fórmula/código]

Você (follow-up): "Criei esta fórmula. Ela está correta?
Teste com: Entrada: [Dados], Saída Esperada: [Valor]
Se estiver errada, qual é o erro e como consertar?"

Claude: [Valida, encontra erro, sugere fix com explicação]
```

**Estratégia 4: Iterando Requisito**

```markdown
Você: "Preciso automatizar o relatório mensal."

Claude: [Sugere Macro VBA]

Você (follow-up): "Macro é bom. Mas o relatório tem 3 abas diferentes
com lógicas distintas. Qual é a melhor estrutura de código?
Devo fazer uma macro por aba ou uma macro principal com funções?"

Claude: [Sugere arquitetura melhor com exemplos]
```

---

### Subseção 2.3.3: Quando Desconfiar de Claude (e Validar Sozinho)

**📸 Sugestão de Prints:**
- Exemplo de resposta que parece correta mas tem bug
- Validação manual descobrindo o erro
- Correção

**Checklist: Quando Validar Manualmente**

```markdown
❓ Claude sugeriu fórmula complexa (>50 caracteres)?
   → Teste com dados simples primeiro

❓ Claude gerou código (VBA/Python) com >20 linhas?
   → Execute em subconjunto pequeno dos dados

❓ Claude foi muito genérico na resposta?
   → Ele realmente entendeu seu contexto?

❓ Claude mencionou "geralmente" ou "na maioria dos casos"?
   → Pode haver exceção no seu caso específico

❓ Você pediu algo com múltiplas condições (AND, OR complexos)?
   → Teste casos extremos (valores vazios, negativos, duplicatas)

❓ Claude sugeriu índices/ranges com $?
   → Verifique se está fixando corretamente para cópia

❓ A resposta parece "mágica" (muito elegante)?
   → Pode estar perdendo edge cases. Questione.
```

**Exemplo Real: Erro Sutil em Fórmula**

```
Claude sugere:
=IFERROR(VLOOKUP(A2, Dados!$A$2:$D$100, 4, FALSE), "Não encontrado")

Problema sutil:
Se a tabela Dados crescer para 101+ linhas, VLOOKUP não verá elas.

Validação:
Você testa com registro novo (depois da linha 100) → Não encontra

Follow-up com Claude:
"A fórmula funciona até linha 100, depois não acha mais.
Como fazer range dinâmico em vez de hardcoded?"

Claude: "Use a tabela como Tabela Dinâmica do Excel (Ctrl+T).
Depois: =IFERROR(VLOOKUP(A2, NomeDaTabela[Colunas], 4, FALSE), ...)"
```

**Habilidades Esperadas ao Fim:**
- Reconhecer quando resposta de Claude é insuficiente
- Usar follow-up efetivo para refinar resposta
- Validar respostas manualmente antes de implementar
- Desconfiar saudavelmente (não tudo que Claude diz é ouro)

---

---

# MÓDULO 3: FÓRMULAS DO BÁSICO AO AVANÇADO

## Aula 3.1: Fórmulas de Busca (PROCV, XLOOKUP, ÍNDICE/CORRESP)

### Subseção 3.1.1: PROCV (VLookup) – O Clássico com Limitações

**📸 Sugestão de Prints:**
- Tabela de dados com PROCV sendo aplicada
- Comparação lado a lado: PROCV vs XLOOKUP vs ÍNDICE/CORRESP
- Screenshot mostrando erro #N/A (não encontrado)

**Descrição:**

PROCV (VLOOKUP em inglês) é a fórmula de busca mais conhecida, mas tem limitações severas. Entender onde ela falha é crítico.

**Sintaxe:**
```
=PROCV(valor_procurado, intervalo_tabela, número_coluna, [intervalo])

Exemplo:
=PROCV(A2, Base_Dados!$A$1:$D$1000, 3, FALSE)
       ↑                           ↑
   O que buscar    De qual tabela? Trazer coluna 3 (retorno exato)
```

**Como Funciona:**
```
Tabela:           PROCV(102, ...):
ID | Nome | CPF | Salário
---|------|-----|----------
101| Ana  | ..  | 3000      Procura 102 → Encontra linha 3 → Retorna coluna 3
102| Bruno| ..  | 3500      (Se fosse coluna 4, retornaria 3500)
103| Carlos| .. | 4000      Se não encontrar → Retorna #N/A
```

**Limitações do PROCV:**

| Limitação | Problema | Solução |
|-----------|----------|---------|
| Procura só para **direita** | Se coluna_retorno está à esquerda, falha | Use ÍNDICE/CORRESP ou XLOOKUP |
| Número da coluna é relativo | Se inserir coluna no meio, fórmula quebra | Use nome de coluna ou ÍNDICE |
| Sem busca exata opcional | Força array ordenado | Use XLOOKUP com exact=FALSE |
| Lento em tabelas grandes | 100k linhas = demora | Use Power Query, não PROCV |
| Erro #N/A não é bonito | Exibe erro ao usuário | Use IFERROR() para limpar |

**Exemplo Prático: Base de Clientes**

Você tem:
```
Tabela Clientes (A1:D1000):
ID | Nome | Email | Telefone
---|------|-------|----------

Tabela Vendas (F1:F500):
ID_Cliente
```

Objetivo: Para cada venda, trazer Nome do Cliente.

```excel
❌ ERRADO (vai falhar se telefone tiver valor, não coluna):
=PROCV(F2, Clientes!$A$1:$D$1000, 2, FALSE)
[Está certo, mas...]

✅ MELHOR (com tratamento de erro):
=IFERROR(PROCV(F2, Clientes!$A$1:$D$1000, 2, FALSE), "Cliente não encontrado")

🎯 IDEAL (usando XLOOKUP):
=XLOOKUP(F2, Clientes!$A:$A, Clientes!$B:$B, "Cliente não encontrado")
```

---

### Subseção 3.1.2: XLOOKUP – A Alternativa Moderna

**📸 Sugestão de Prints:**
- Sintaxe do XLOOKUP lado a lado com PROCV
- Exemplo: Busca para esquerda (impossível em PROCV)
- Tabela de compatibilidade: Excel versão vs XLOOKUP disponível

**Descrição:**

XLOOKUP é a versão moderna do PROCV (Excel 365 / Excel 2021+). Resolve quase todos os problemas.

**Sintaxe:**
```
=XLOOKUP(valor, array_busca, array_retorno, [se_não_encontrado], [modo_busca], [ordem_busca])

Exemplo:
=XLOOKUP(A2, Base_Dados!$A$2:$A$1000, Base_Dados!$B$2:$B$1000, "Não encontrado")
```

**Vantagens vs PROCV:**

| Recurso | PROCV | XLOOKUP |
|---------|-------|---------|
| Busca para direita | ✓ | ✓ |
| Busca para esquerda | ✗ | ✓✓ |
| Valor padrão se não encontrado | IFERROR necessário | Nativo |
| Busca exata/aprox | ✓ | ✓✓ (mais clara) |
| Quebra se coluna inserida | ✓ quebra | ✗ não quebra (usa array) |
| Performance em 1M linhas | Lento | Rápido |

**Exemplo Comparado: Busca para Esquerda**

Você tem:
```
Tabela (A:D):
Telefone | Email | Nome | ID
---------|-------|------|----
11-99999 | a@b.c | Ana  | 101
11-88888 | b@c.d | Bruno| 102

Objetivo: Dado o Email, trazer o Telefone (que está à ESQUERDA)
```

```excel
❌ PROCV não consegue (procura só para direita):
Impossível fazer isso.

✅ XLOOKUP consegue:
=XLOOKUP(F2, B:B, A:A, "Email não encontrado")
        ↑   ↑   ↑   
    Dado o Email (coluna B), retorna Telefone (coluna A)
```

---

### Subseção 3.1.3: ÍNDICE/CORRESP – O Poder Flexível

**📸 Sugestão de Prints:**
- Anatômia de ÍNDICE/CORRESP quebrada em 3 partes
- Exemplo: Busca em 2 colunas (impossível em PROCV)
- Comparação de velocidade: PROCV vs ÍNDICE/CORRESP em 1M linhas

**Descrição:**

ÍNDICE/CORRESP é mais complexa, mas muito mais flexível. Funciona em qualquer versão de Excel.

**Conceito:**
```
ÍNDICE: Retorna valor em posição X de um array
   =ÍNDICE(A1:A100, 5) → retorna A5

CORRESP: Encontra posição de um valor em array
   =CORRESP("Bruno", A1:A100, 0) → retorna 2 (se Bruno está em A2)

COMBINADOS:
=ÍNDICE(array_retorno, CORRESP(valor_procurado, array_busca, 0))
```

**Exemplo Passo a Passo:**

```
Tabela:
A1:A100 (ID)    B1:B100 (Nome)    C1:C100 (Salário)

Pergunta: Qual é o salário do ID 105?

Passo 1: CORRESP encontra posição do ID 105
   =CORRESP(105, A1:A100, 0) → Retorna 7 (está na linha 7)

Passo 2: ÍNDICE retorna valor da coluna Salário, posição 7
   =ÍNDICE(C1:C100, 7) → Retorna 4500

Combinado:
=ÍNDICE(C1:C100, CORRESP(105, A1:A100, 0))
```

**Vantagem: Busca em Múltiplas Colunas**

```
Objetivo: Encontrar valor onde coluna A = 'Bruno' E coluna B = 'SP'

PROCV: Impossível (só procura coluna A)

ÍNDICE/CORRESP com lógica:
=ÍNDICE(C:C, CORRESP(1, (A:A="Bruno")*(B:B="SP"), 0))
[Requer Ctrl+Shift+Enter como fórmula matricial]

XLOOKUP (mais simples):
=XLOOKUP(1, (A:A="Bruno")*(B:B="SP"), C:C)
```

---

### Subseção 3.1.4: Exercício Prático – As 3 Funções

**📸 Sugestão de Prints:**
- Dados de exemplo (tabela de clientes)
- 3 fórmulas lado a lado
- Resultado idêntico das 3

**Tarefa: Usar as 3 Funções para Mesmo Resultado**

**Tempo:** 45 minutos

**Dados Fornecidos:**

```
Clientes (A1:D100):
ID | Nome | Email | Telefone
102 | Ana Silva | ana@email.com | 11-99999111
103 | Bruno Santos | bruno@email.com | 21-88888222
...

Vendas (F1:G50):
ID_Cliente | Valor_Vendido
102 | 1500
103 | 2000
...

Objetivo: Para cada venda, trazer o nome do cliente usando:
1. PROCV
2. XLOOKUP (se versão suporta)
3. ÍNDICE/CORRESP
```

**Solução:**

```excel
Col H (PROCV):
=IFERROR(PROCV(F2, Clientes!$A$2:$D$100, 2, FALSE), "")

Col I (XLOOKUP):
=XLOOKUP(F2, Clientes!$A$2:$A$100, Clientes!$B$2:$B$100, "")

Col J (ÍNDICE/CORRESP):
=IFERROR(ÍNDICE(Clientes!$B$2:$B$100, CORRESP(F2, Clientes!$A$2:$A$100, 0)), "")

Copiar H2 para H50, I2 para I50, J2 para J50.
Resultado deve ser idêntico nas 3 colunas.
```

**Checklist:**

```markdown
✓ PROCV funciona (H coluna preenchida)
✓ XLOOKUP funciona (I coluna preenchida, se compatível)
✓ ÍNDICE/CORRESP funciona (J coluna preenchida)
✓ Resultados são idênticos (conferiu?)
✓ Entendeu quando usar cada uma?
```

**Resumo: Quando Usar Cada Uma**

```markdown
PROCV:
- Quando: Busca simples, coluna à direita, versão antiga Excel
- Evitar: Tabelas grandes (>100k), busca à esquerda, coluna pode mudar

XLOOKUP:
- Quando: Busca simples/complexa, versão moderna Excel (365 / 2021+)
- Melhor: Performance, clareza, flexibilidade

ÍNDICE/CORRESP:
- Quando: Busca complexa (múltiplas condições), compatibilidade (versão antiga)
- Evitar: Performance em tabelas >1M linhas sem otimização
```

**Habilidades Esperadas:**
- Conhecer 3 técnicas de busca e suas limitações
- Escolher a certa para cada contexto
- Usar XLOOKUP como padrão em versão moderna
- Entender que ÍNDICE/CORRESP é mais flexível mas menos intuitivo

---

## Aula 3.2: Lógica Condicional Complexa (SE, IFS, SWITCH)

### Subseção 3.2.1: SE Simples até SE Encadeado

**📸 Sugestão de Prints:**
- SE simples (2 opções)
- SE encadeado (3+ opções) estruturado visualmente
- Comparação: SE encadeado vs IFS vs SWITCH

**Descrição:**

**SE Simples (2 opções):**

```excel
=SE(condição, valor_se_verdadeiro, valor_se_falso)

Exemplo:
=SE(A2>6, "Aprovado", "Reprovado")
```

**SE Encadeado (3+ opções):**

```excel
=SE(A2>=9, "A", SE(A2>=7, "B", SE(A2>=5, "C", "D")))

Visualmente:
┌─ Se A2 >= 9 → "A"
├─ Se A2 >= 7 → "B"  
├─ Se A2 >= 5 → "C"
└─ Senão → "D"
```

**Problema com SE Encadeado:**

```
=SE(A2>=9, "A", SE(A2>=7, "B", SE(A2>=5, "C", SE(A2>=3, "D", "F"))))

Problemas:
1. Difícil de ler (parênteses aninhados)
2. Difícil de manter (adicionar novo nível é confuso)
3. Fácil cometer erros de sintaxe
```

---

### Subseção 3.2.2: IFS – A Versão Legível

**📸 Sugestão de Prints:**
- Sintaxe do IFS comparada com SE encadeado
- Exemplo prático: Classificação de performance
- Tabela: SE Encadeado vs IFS (legibilidade)

**Descrição:**

IFS (disponível em Excel 365, 2019+) é muito mais legível.

**Sintaxe:**
```excel
=IFS(cond1, val1, cond2, val2, cond3, val3, ...)

Exemplo (Classificação):
=IFS(A2>=9, "A", A2>=7, "B", A2>=5, "C", A2>=3, "D", TRUE, "F")
          ↑        ↑         ↑         ↑        ↑
       Condição / Valor (pares)      Se nenhuma, retorna "F"
```

**Comparação:**

```excel
❌ SE Encadeado (difícil ler):
=SE(A2>=9, "A", SE(A2>=7, "B", SE(A2>=5, "C", SE(A2>=3, "D", "F"))))

✅ IFS (muito mais legível):
=IFS(A2>=9, "A", 
     A2>=7, "B", 
     A2>=5, "C", 
     A2>=3, "D", 
     TRUE, "F")
```

**Quando Usar IFS:**
- Múltiplas condições simples (3+)
- Condições mutuamente exclusivas (pontuação, categorias)
- Código legível é prioridade

---

### Subseção 3.2.3: SWITCH – Quando há Valores Discretos

**📸 Sugestão de Prints:**
- SWITCH para código de status
- SWITCH para tabela de lookup (sem PROCV)
- Erro padrão se nenhum match

**Descrição:**

SWITCH é perfeito quando você tem **valores discretos** (não intervalos).

**Sintaxe:**
```excel
=SWITCH(expressão, valor1, resultado1, valor2, resultado2, ..., padrão)

Exemplo (Traduzir Status):
=SWITCH(A2, 
        "AT", "Ativo",
        "IN", "Inativo", 
        "SUS", "Suspenso",
        "Desconhecido")
```

**Comparado com IFS:**

```excel
❌ IFS (para valores discretos é verbose):
=IFS(A2="AT", "Ativo", A2="IN", "Inativo", A2="SUS", "Suspenso", TRUE, "Desconhecido")

✅ SWITCH (conciso e claro):
=SWITCH(A2, "AT", "Ativo", "IN", "Inativo", "SUS", "Suspenso", "Desconhecido")
```

**Caso de Uso: Tabela de Lookup sem PROCV**

```
Código | Descrição
AT     | Ativo
IN     | Inativo
SUS    | Suspenso

Em vez de:
=PROCV(A2, Lookup!$A$1:$B$4, 2, FALSE)

Use:
=SWITCH(A2, "AT", "Ativo", "IN", "Inativo", "SUS", "Suspenso", "Código desconhecido")

Vantagens:
- Não precisa de tabela separada
- Mais rápido (sem busca)
- Embutido na célula
```

---

### Subseção 3.2.4: Exercício Prático – Lógica Condicional

**📸 Sugestão de Prints:**
- Dados de exemplo (notas, status de cliente)
- 3 colunas com SE, IFS e SWITCH aplicados
- Validação visual (resultados batem?)

**Tarefa: Construir Lógica Condicional em Camadas**

**Tempo:** 30 minutos

**Cenário: Classificação de Clientes por Performance**

```
Dados:
A | Cliente | B | Receita_Anual | C | Dias_Sem_Comprar
```

**Objetivo 1: Classificar por Receita (SE Encadeado)**

```excel
Col D:
=SE(B2>=50000, "Premium", SE(B2>=20000, "Standard", "Bronze"))

Teste com:
B2 = 75000 → "Premium" ✓
B2 = 30000 → "Standard" ✓
B2 = 10000 → "Bronze" ✓
```

**Objetivo 2: Mesmo, mas com IFS (mais legível)**

```excel
Col E:
=IFS(B2>=50000, "Premium", B2>=20000, "Standard", TRUE, "Bronze")

Resultado deve ser idêntico a Col D.
```

**Objetivo 3: Classificar por Risco de Churn (IFS + SWITCH)**

Regra:
- Se Dias_Sem_Comprar > 120 AND Receita < 20k → "Risco Alto"
- Se Dias_Sem_Comprar > 90 → "Risco Médio"  
- Se Dias_Sem_Comprar > 60 → "Risco Baixo"
- Senão → "Seguro"

```excel
Col F:
=IFS(AND(C2>120, B2<20000), "Risco Alto",
     C2>90, "Risco Médio",
     C2>60, "Risco Baixo",
     TRUE, "Seguro")
```

**Objetivo 4: Ação Recomendada (SWITCH)**

Regra de Ação:
- "Risco Alto" → "Ligar urgente"
- "Risco Médio" → "Email de reengajamento"
- "Risco Baixo" → "Enviarnewsletter"
- "Seguro" → "Manutenção"

```excel
Col G:
=SWITCH(F2, 
        "Risco Alto", "Ligar urgente",
        "Risco Médio", "Email reengajamento",
        "Risco Baixo", "Enviar newsletter",
        "Seguro", "Manutenção",
        "Desconhecido")
```

**Checklist:**

```markdown
✓ Col D (SE Encadeado) preenchida
✓ Col E (IFS) preenchida e idêntica a Col D
✓ Col F (IFS + AND) classifica risco corretamente
✓ Col G (SWITCH) mapeia ação apropriada
✓ Testou casos extremos (zeros, números grandes)?
```

**Habilidades Esperadas:**
- Construir lógica condicional complexa
- Escolher entre SE, IFS, SWITCH
- Entender que legibilidade importa em fórmulas
- Validar resultado em casos extremos

---

## Aula 3.3: Cálculos Estatísticos Avançados

*(Desenvolvido de forma similar às anteriores: Subseção 3.3.1 → Sintaxe básica, Subseção 3.3.2 → Exemplos avançados, Subseção 3.3.3 → Exercício)*

**Nota:** Por brevidade, ilustro estrutura. Implementação completa segue padrão similar.

**Tópicos Cobertos:**

1. **Estatística Descritiva**: MÉDIA, MEDIANA, DESVPAD, QUARTIL
2. **Análise de Frequência**: FREQ, MODO, CONTAR.SE
3. **Agregações Condicionais**: SOMASE, MÉDIASE, CONTARIFS
4. **Percentis e Outliers**: PERCENTIL, QUARTIL, LIMITE.SUPERIOR/INFERIOR
5. **Correlação**: CORREL, RSQ (para análise bivariada)

---

## Aula 3.4: Fórmulas Matriciais (FILTRO, CLASSIFICAR, ÚNICA)

**📸 Sugestão de Prints:**
- Resultado da fórmula FILTRO em múltiplas linhas/colunas
- CLASSIFICAR reordenando tabela inteira
- ÚNICA removendo duplicatas

**Descrição:**

Fórmulas matriciais modernas (Excel 365) permitem **retornar múltiplos resultados** em uma única fórmula.

### FILTRO

```excel
=FILTRO(array, critério, [se_não_encontrado])

Exemplo: Mostrar apenas clientes com receita > 50000
=FILTRO(A:A, B:B>50000, "Nenhum encontrado")

Resultado: Múltiplas linhas, automático.
```

### CLASSIFICAR

```excel
=CLASSIFICAR(array, [índice_ordenação], [ordem])

Exemplo: Ordenar clientes por receita (descendente)
=CLASSIFICAR(A1:C100, 3, -1)
               ↑    ↑  ↑
         Array  Coluna 3 (Receita) Descendente
```

### ÚNICA

```excel
=ÚNICA(array)

Exemplo: Listar clientes únicos (sem duplicatas)
=ÚNICA(A1:A1000)
```

**Exercício:**

```
Objetivo: Mostrar top 10 clientes por receita (com detalhe)

=FILTRO(CLASSIFICAR(A1:C100, 3, -1), ROW(ÍNDICE(1:100, 1:10)))
[Simples: apenas CLASSIFICAR e pegar primeiras 10 linhas]
```

---

---

# MÓDULO 4: LIMPEZA E TRATAMENTO DE DADOS

## Aula 4.1: Diagnóstico de Dados Sujos

**📸 Sugestão de Prints:**
- Amostra de dados "sujos" (nomes com espaço extra, datas inconsistentes)
- Checklist de Claude identificando problemas
- Tabela de "Problemas Encontrados vs Frequência"

**Descrição:**

Antes de analisar, diagnóstico é obrigatório.

**Prompt para Claude:**

```markdown
Tenho uma base de 5.000 registros de clientes com estas colunas:
- ID, Nome, Email, Data_Cadastro, Telefone, CPF

Quero um diagnóstico completo de qualidade.
Responda estruturado:

1. Campos vazios: Qual coluna tem mais?
2. Formatos inconsistentes: Datas (DD/MM vs MM/DD), telefone (com/sem parênteses)?
3. Duplicatas: Mesmo email/CPF aparecem múltiplas vezes?
4. Outliers: Datas impossíveis (antes de 1950), IDs muito altos?
5. Padrão esperado vs realidade: O que está claramente errado?
6. Prioridade de limpeza: O que urgir? O que é nice-to-have?

Dados (primeiras 20 linhas):
[Colar tabela]
```

---

## Aula 4.2: Normalização de Texto e Datas

**Funções Chave:**

```excel
MAIÚSCULA() / MINÚSCULA() / PRI.MAIÚSCULA()
REMOVER.ESPAÇOS()
SUBS(texto, antigo, novo)
ESQUERDA(), DIREITA(), MID()
```

**Exemplo: Limpar Nome (espaço extra, maiúsculas inconsistentes)**

```excel
=PRI.MAIÚSCULA(REMOVER.ESPAÇOS(A2))

Antes: "  João SILVA  "
Depois: "João silva"
```

---

## Aula 4.3: Remoção de Duplicatas e Detecção de Anomalias

**Com Claude:**

```markdown
Tenho duplicatas por Email (mesmo cliente, múltiplos registros).
Dados: ID, Nome, Email, Data_Cadastro, Status.

Como identificar e manter apenas o registro mais antigo?

Opções:
1. Fórmula Excel (qual?)
2. Power Query
3. VBA Macro

Qual recomenda para 10.000 registros? Por quê?
```

---

## Aula 4.4: Transformação de Dados com Power Query

**📸 Sugestão de Prints:**
- Interface do Power Query
- Passos de transformação (passo a passo)
- Resultado final (antes vs depois)

**Descrição:**

Power Query é ferramenta integrada no Excel para limpeza e transformação sem fórmula.

**Vantagem:** Visual, documentável, reutilizável.

**Exemplo: Dividir Nome em Primeiro + Sobrenome**

```
Passo 1: Carregar dados no Power Query
Passo 2: Coluna "Nome" → Dividir por espaço
Passo 3: Renomear colunas (Nome_Primeiro, Nome_Segundo)
Passo 4: Carregar resultado de volta ao Excel
```

---

---

# MÓDULO 5: ANÁLISE EXPLORATÓRIA E INSIGHTS

## Aula 5.1: Diagnóstico Rápido de Dataset

**Prompt para Claude:**

```markdown
Tenho uma base de vendas com 10.000 linhas.
Colunas: Produto, Categoria, Vendedor, Data, Valor, Região.
Período: 2023-2024.

Quero diagnóstico rápido:
1. Qual é o volume total de vendas?
2. Ticket médio?
3. Distribuição por categoria (top 5)?
4. Qual vendedor está acima/abaixo da média?
5. Sazonalidade? (mês a mês, há padrão?)

Sugira as 3 perguntas mais importantes para negócio e qual métrica revisar.

Primeiras 50 linhas:
[Colar dados]
```

---

## Aula 5.2: Análise Descritiva e Estatística

**Fórmulas Essenciais:**

```excel
MÉDIA(array)
MEDIANA(array)
DESVPAD(array) - Desvio padrão (dispersão)
PERCENTIL(array, k) - Ex: P90 (90º percentil)
CONTAR(array) - Contagem não-vazia
CONTAR.VAZIO(array) - Contar vazios
SOMASE(range, critério, sum_range)
```

---

## Aula 5.3: Recomendações de Visualização

**Claude ajuda a escolher gráfico:**

```markdown
Tenho estes dados:
- Receita por mês (12 meses)
- Receita por categoria (5 categorias)
- Receita por vendedor (20 vendedores)
- Receita por região (4 regiões)

Que gráficos recomenda para apresentar executivo?
1. Tempo (mês)?
2. Comparação entre categorias?
3. Performance individual (vendedor/região)?

Justifique a escolha do tipo de gráfico em cada caso.
```

---

## Aula 5.4: Detecção de Padrões e Tendências

**Com Claude e Fórmulas:**

```excel
Detectar tendência (subindo/descendo):
=(Mês_Atual - Mês_Anterior) / Mês_Anterior

Exemplo:
Vendas_Jan = 100
Vendas_Fev = 120
Variação = (120 - 100) / 100 = 20% crescimento

Implementar coluna de variação MoM (Month over Month).
```

---

---

# MÓDULO 6: AUTOMAÇÃO COM VBA E PYTHON

## Aula 6.1: Introdução a VBA com Claude

**📸 Sugestão de Prints:**
- Editor VBA do Excel aberto
- Macro simples sendo executada
- Resultado visível em planilha

**Descrição:**

VBA (Visual Basic for Applications) permite automação dentro do Excel.

**Primeiro Macro (com Claude):**

```markdown
Quero um macro VBA que:
1. Copie dados de Aba1 para Aba2
2. Ordene por coluna C descendente
3. Remova duplicatas

Escreva o código passo a passo com comentários.
Eu executarei no meu Excel via Ctrl+F5.
```

**Código Típico Fornecido por Claude:**

```vba
Sub CopiarOrdenaLimpa()
    ' Copiar dados
    Sheets("Aba1").Range("A:D").Copy
    Sheets("Aba2").Range("A1").PasteSpecial
    
    ' Ordenar por coluna C descendente
    Sheets("Aba2").Range("A1").CurrentRegion.Sort _
        Key1:=Sheets("Aba2").Range("C1"), Order1:=xlDescending
    
    ' Remover duplicatas (Excel 2007+)
    Sheets("Aba2").Range("A1").CurrentRegion.RemoveDuplicates Columns:=Array(1, 2)
    
    MsgBox "Pronto! Dados copiados, ordenados e limpos."
End Sub
```

---

## Aula 6.2: Macros Reutilizáveis

**Padrão 1: Macro que Funciona em Qualquer Aba**

```vba
Sub ProcessarAtual()
    ' Pega aba atual (qualquer uma)
    Dim ws As Worksheet
    Set ws = ActiveSheet
    
    ' Trabalha com a aba ativa
    ws.Range("A1").Value = "Processado"
    ws.Range("A1").Interior.Color = RGB(255, 0, 0)
    
    MsgBox "Aba " & ws.Name & " foi processada."
End Sub
```

**Padrão 2: Macro Parametrizada**

```vba
Sub LimparDados(aba_nome As String, coluna_ordem As Integer)
    Dim ws As Worksheet
    Set ws = Sheets(aba_nome)
    
    ' Remove vazios
    ws.Range("A:Z").SpecialCells(xlCellTypeBlanks).Delete
    
    ' Ordena por coluna
    ws.Range("A1").CurrentRegion.Sort Key1:=ws.Range(ChrW(64 + coluna_ordem) & "1")
    
    MsgBox "Limpeza concluída na aba " & aba_nome
End Sub
```

---

## Aula 6.3: Integração Python + Excel (Pandas)

**📸 Sugestão de Prints:**
- Script Python em editor (VS Code, Anaconda)
- Arquivo Excel sendo lido/processado
- Resultado salvo de volta

**Descrição:**

Python é mais poderoso que VBA para análise complexa.

**Instalação:**

```bash
pip install pandas openpyxl xlrd
```

**Exemplo: Ler, Processar, Salvar**

```python
import pandas as pd

# 1. Ler arquivo
df = pd.read_excel('dados.xlsx', sheet_name='Vendas')

# 2. Processar
df['Receita_Total'] = df['Quantidade'] * df['Preco']
df = df.dropna()  # Remover vazios
df = df.sort_values('Receita_Total', ascending=False)

# 3. Salvar
df.to_excel('resultado.xlsx', index=False)

print("Processamento concluído.")
```

---

## Aula 6.4: Orquestração de Workflows

**Automatizar Processo Completo:**

```markdown
Processo Manual (1 hora/dia):
1. Baixar arquivo de vendas do servidor
2. Copiar para Excel
3. Limpar dados sujos
4. Gerar relatório
5. Enviar email para gerente

Automatizado (5 segundos):
1. Script Python baixa arquivo
2. Lê e processa com Pandas
3. Gera gráfico
4. Salva como PDF e Excel
5. Envia email automaticamente

Claude ajuda a orquestrar.
```

---

---

# MÓDULO 7: INTEGRAÇÃO E CASOS REAIS

## Aula 7.1: Estudo de Caso 1 – Análise de Vendas

**Cenário:**
- Empresa de TI com 50 vendedores
- 24 meses de dados
- Objetivo: Identificar top performers e underperformers

**Tarefas:**

1. **Diagnóstico:** "Qual é a qualidade dos dados?"
2. **Análise:** "Ranking de vendedores. Quem deve entrar em desenvolvimento?"
3. **Previsão:** "Com base em Q1 2024, quem vai bater meta em Q2?"
4. **Ação:** "Quem precisa de coaching? Quem merece incentivo?"

**Solução com Claude:**

```markdown
Tenho 5.000 registros de vendas mensais de 50 vendedores.
Dados: Vendedor, Mes, Valor_Vendido, Produto, Região.

1. Qual é o ranking de vendedores por receita acumulada?
2. Qual é a variação MoM (mês a mês) para cada um?
3. Há vendedores com queda consistente de 3+ meses?
4. Baseado em Jan-Mar 2024, quem não vai bater meta anual de 50k?

Responda com fórmulas que posso copiar no Excel.

Dados (primeiras 100 linhas):
[Colar]
```

---

## Aula 7.2: Estudo de Caso 2 – Processamento de RH

**Cenário:**
- Universidade com 500 funcionários
- Folha de pagamento mensal
- Objetivo: Análise de custo, retenção, equidade salarial

**Tarefas:**

1. **Custo total por departamento?**
2. **Há disparidade salarial entre gêneros?**
3. **Rotatividade por faixa salarial?**
4. **Previsão de custo folha para próximos 12 meses?**

---

## Aula 7.3: Estudo de Caso 3 – Relatório Acadêmico Automático

**Cenário:**
- Escola com 200 alunos
- Notas de 3 disciplinas
- Objetivo: Gerar relatório trimestral automático

**Tarefa:**

Usar Claude + VBA para:
1. Ler planilha de notas
2. Calcular média, situação (aprovado/reprovado/recuperação)
3. Gerar relatório em PDF com gráficos
4. Enviar email para coordenador

---

---

# CONCLUSÃO

Ao completar este curso, você:

1. ✓ Usa Claude como consultor técnico em Excel
2. ✓ Estrutura prompts de forma efetiva
3. ✓ Domina fórmulas do básico ao avançado
4. ✓ Limpa e analisa dados
5. ✓ Automatiza tarefas repetitivas
6. ✓ Resolve problemas reais de negócio/academia

**Próximos Passos:**
- Aplicar em seu contexto real
- Explorar recursos avançados (Power BI, DAX)
- Contribuir com comunidade compartilhando soluções
