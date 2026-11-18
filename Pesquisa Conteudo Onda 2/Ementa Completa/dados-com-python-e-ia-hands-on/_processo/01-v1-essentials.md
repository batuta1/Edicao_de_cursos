# Plano de Aula — Dados com Python e IA (Essentials)

## Identificação

| Campo | Definição |
|---|---|
| Curso | Dados com Python e IA (Essentials) |
| Natureza | Curto, introdutório e prático |
| Carga horária | 90 minutos |
| Público-alvo | Analistas, profissionais de finanças, servidores e engenheiros |
| Pré-requisitos | IA para Análise de Dados - Essentials |
| Recursos necessários | Computador com Python; Claude Code ou Codex |

### Objetivo Geral

O curso tem por finalidade capacitar o participante a realizar análises de dados em Python com o
auxílio de agentes de código. Como produto final, o participante entrega um script de análise.

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Instalar o ambiente Python.
2. Utilizar agentes de código.
3. Produzir análises em pandas.
4. Validar resultados.

### Estrutura e Sequência dos Módulos

Os módulos são cumulativos.

| Módulo | Título | Referência | Tempo |
|---|---|---|---|
| 1 | Ambiente Python | python.org | 20 min |
| 2 | Agentes de código | Docs Anthropic e OpenAI | 20 min |
| 3 | Pandas e gráficos | Docs pandas | 20 min |
| 4 | Validação | — | 15 min |
| 5 | Síntese | — | 15 min |

---

# Módulo 1 — Ambiente Python

> Ponto de partida.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Instalar o Python.
2. Instalar bibliotecas.
3. Executar um script.

### Texto Descritivo

O Python é uma linguagem de programação amplamente utilizada em análise de dados. Recomenda-se
instalá-lo a partir do site oficial. As bibliotecas pandas e Matplotlib são instaladas com o
comando pip install.

Após a instalação, executa-se um script com o comando python seguido do nome do arquivo.

### Exercício Prático

**Instalação (10 min)**

1. Baixar e instalar o Python.
2. Executar pip install pandas.

Critério de êxito: pandas instalado.

---

# Módulo 2 — Agentes de código

> Pressupõe o Módulo 1.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Definir agente de código.
2. Instalar o Claude Code ou o Codex.
3. Solicitar um script.

### Texto Descritivo

Agentes de código são ferramentas de IA que escrevem e executam código. O Claude Code e o Codex
operam no terminal. Instalam-se pelo npm.

Solicita-se ao agente um script de análise descrevendo a tarefa em linguagem natural.

### Exercício Prático

**Primeiro script (10 min)**

1. Instalar o Claude Code.
2. Pedir um script que leia um CSV.

Critério de êxito: script criado.

---

# Módulo 3 — Pandas e gráficos

> Pressupõe o Módulo 2.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Ler um CSV com pandas.
2. Agrupar dados.
3. Gerar gráficos com Matplotlib.

### Texto Descritivo

O pandas organiza dados em DataFrames. A função read_csv lê arquivos CSV. A função groupby agrupa
dados. O Matplotlib gera gráficos.

### Exercício Prático

**Análise (15 min)**: pedir ao agente uma análise de uma base pública com gráfico.

Critério de êxito: gráfico gerado.

---

# Módulo 4 — Validação

> Pressupõe o Módulo 3.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de validar resultados.

### Texto Descritivo

Recomenda-se conferir os resultados. O agente pode errar.

### Exercício Prático

**Questão:** o agente pode errar? (a) Sim (b) Não. Gabarito: (a).

---

# Módulo 5 — Síntese e Aplicação Integrada

### Exercício Prático

**Atividade integradora (15 min)**: realizar uma análise completa com agente.

| Critério | Atendido? |
|---|---|
| Script | |
| Gráfico | |

---

# Encerramento

O curso apresentou a análise de dados com Python e agentes de código. Recomenda-se prática regular.

> **Síntese:** o agente escreve, o analista decide.
