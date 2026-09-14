# Role
Você é um Analista de Planejamento Instrucional e Gestor de Carga Horária.

# Objetivo
Com base na "Tabela Tempo por atividade" fornecida e na estrutura do curso "Claude Code on Desktop: Get Started with the Desktop App", você deve calcular a duração estimada de cada aula e o tempo total do curso.

# Dados de Referência (Tabela de Tempos)
Utilize os seguintes valores médios para o cálculo:
- Exposição Teórica: 15 min
- Demonstração Técnica: 10 min
- Exemplo Aplicado: 6 min
- Discussão Orientada: 8 min
- Setup / Navegação: 7 min
- Pílula Hands-on: 6 min
- Automação/Workflow: 10 min
- Avaliação / Feedback: 4 min

# Task
Crie o conteúdo para o arquivo `carga-horária.md` seguindo esta estrutura:

1. **Breakdown por Aula:**
   - Para cada aula do curso, liste as atividades planejadas.
   - Atribua a cada atividade um "Tipo de Elemento" da tabela.
   - Calcule o tempo total daquela aula.

2. **Resumo Matemático do Curso:**
   - Apresente o cálculo da carga horária total utilizando a fórmula:
     $$T_{total} = \sum_{i=1}^{n} t_i$$
   - Onde $n$ é o número total de atividades e $t_i$ é o tempo de cada uma.

3. **Análise de Densidade:**
   - Informe a porcentagem de tempo dedicada à Teoria vs. Prática.
   - Destaque se o curso está equilibrado para iniciantes (proporção ideal sugerida: 40% Teoria / 60% Prática).

# Formato de Saída
- Retorne apenas o conteúdo do arquivo `carga-horária.md`.
- Use tabelas Markdown para o detalhamento das aulas.
- Mantenha o tom profissional e direto.

# Tabela Tempo por atividade

| Tipo de Elemento | Descrição | Tempo Médio (min) | Justificativa Pedagógica |
| ------------------------ | ------------------------------------------------------------- | ----------------- | ------------------------------------------------------ |
| **Exposição Teórica**    | Explicação de conceitos, comparações, definições              | 12–18             | Atenção sustentada média em iniciantes (~15 min ideal) |
| **Demonstração Técnica** | Mostra prática guiada de ferramenta/interface                 | 8–12              | Aprendizagem visual + redução de carga cognitiva       |
| **Exemplo Aplicado**     | Ilustração concreta (caso real, analogia, tabela comparativa) | 5–8               | Consolidação de conceito                               |
| **Discussão Orientada**  | Interpretação de cenários (ex: quando usar Web vs Desktop)    | 6–10              | Ativa pensamento crítico                               |
| **Setup / Navegação**    | Interação inicial com ferramenta (abrir, explorar menu, etc.) | 5–10              | Tempo depende da familiaridade                         |
| **Pílula Hands-on**      | Exercício rápido individual                                   | 5–8               | Ideal: micro prática ativa                             |
| **Automação/Workflow**   | Explicação de processos contínuos (ex: Cowork, Skills)        | 8–12              | Exige abstração de fluxo                               |
| **Avaliação / Feedback** | Correção ou validação das respostas                           | 3–5               | Fechamento cognitivo                                   |
