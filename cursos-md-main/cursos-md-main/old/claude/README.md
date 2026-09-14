<link rel="stylesheet" href="../.css/style.css">

# Procedimentos Executados para construir o Curso do Claude

## O que vamos fazer?

Neste documento, registramos o processo de construção de um curso sobre a ferramenta [Claude](https://www.claude.ai), com foco na experiência Desktop e em seus três módulos principais: "ChatBox", "Coworks" e "Code".

O download do Claude Desktop está disponível neste [link](https://claude.com/download).

## Abordagem

Para estruturar o curso com progressão pedagógica, adotamos uma abordagem iterativa entre diferentes IAs. Em cada etapa, usamos um prompt de refinamento, analisamos o retorno e evoluímos para o próximo passo com base no resultado anterior.

## Passo 1 — Definir Contornos

### Gemini

Nesta etapa inicial, configuramos o Gemini no modo de **raciocínio** (plano gratuito), conforme a ilustração abaixo.

<div align="center">
  <img src="imagens/print-gemini-1.png" width="500px">
  <p style="font-size: 0.8em"> Página inicial </p>
</div>

### Prompt Gemini 1

Com esse contexto, solicitamos um prompt-base para orientar a criação do curso. O conteúdo utilizado foi:

[prompt-1.md](passos/prompt-1.md)

### Retorno Gemini 1

A partir do prompt acima, o Gemini retornou a versão que serviu como ponto de partida para a etapa seguinte:

[prompt-1.md](passos/return-1.md)

### 🚩 Marco de Desenvolvimento: Prompt-Base Validado
> **O que validar agora:**
> - [ ] Você leu `return-1.md` e conseguiu identificar claramente: papel, objetivo, estrutura e estilo de escrita.
> - [ ] Você confirma que o retorno já está pronto para copiar e reutilizar como prompt de geração de curso.
> 
> **Sinal Verde:** Se você consegue reutilizar esse prompt sem reescrever instruções centrais, pode avançar.
> **Sinal Vermelho:** Se o prompt ainda estiver ambíguo ou incompleto, revise o passo `prompt-1.md`.

## Passo 2 — Construir a Versão 1.0

Com o retorno do passo anterior em mãos, avançamos para a primeira versão do curso.

Essa execução dependia de um contexto técnico adicional: o artigo oficial da própria Claude, intitulado *"Claude Code on desktop: 'Get started with the desktop app'"*, disponível neste [link](https://code-claude-com.translate.goog/docs/en/desktop-quickstart?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc&_x_tr_hist=true), acessado em **1 de maio de 2026**.

> Para acesso local, consulte o arquivo [anexo-1.md](anexo-1.md).

### Prompt ChatGPT 1

Combinamos o [retorno do passo 1](#retorno-gemini-1) com o anexo técnico e submetemos esse conjunto ao ChatGPT (plano pago, com acesso ao modelo de raciocínio), conforme a imagem abaixo.

<div align="center">
  <img src="imagens/print-gpt-1.png" width="500px">
  <p style="font-size: 0.8em"> Página inicial </p>
</div>

### Retorno ChatGPT 1

Como resultado, foi gerado um material com 20 aulas e 5 seções auxiliares (abertura, apoio e encerramento), totalizando 1344 linhas em Markdown[^1].

O arquivo completo está disponível em [curso-v1-gpt.md](passos/curso-v1-gpt.md).

> [^1] Referência: [Markdown Guide](https://www.markdownguide.org)

### 🚩 Marco de Desenvolvimento: Versão 1.0 Consolidada
> **O que validar agora:**
> - [ ] Você gerou/obteve o arquivo [curso-v1-gpt.md](passos/curso-v1-gpt.md) e ele abre sem trechos truncados.
> - [ ] Você verificou que a estrutura inclui aulas e seções auxiliares, sem lacunas visíveis entre capítulos.
> 
> **Sinal Verde:** Se você consegue ler a versão 1.0 do início ao fim com continuidade, pode avançar para a auditoria.
> **Sinal Vermelho:** Se houver módulos faltando ou quebra de formatação, revise o passo `return-1.md`.

## Passo 3 — Gerar Instruções para Análise Crítica

Após concluir o [curso versão 1.0](#retorno-chatgpt-1), voltamos ao Gemini para criar um prompt de avaliação crítica do material.

### Prompt Gemini 2

O prompt abaixo foi usado para estruturar critérios mais claros de auditoria pedagógica e técnica:

[prompt-1.md](passos/prompt-2.md)

### Retorno Gemini 2

Como saída, recebemos o prompt que orientou a fase de análise:

[return-1.md](passos/return-2.md)

### 🚩 Marco de Desenvolvimento: Prompt de Auditoria Aprovado
> **O que validar agora:**
> - [ ] Você confirmou que `return-2.md` pede análise de clareza, rigor técnico, engajamento e potencial de uso.
> - [ ] Você conferiu que o formato de saída exige relatório estruturado (sumário, gargalos, soluções e roadmap).
> 
> **Sinal Verde:** Se você consegue executar uma auditoria completa usando apenas esse prompt, pode avançar.
> **Sinal Vermelho:** Se o prompt estiver genérico e não orientar decisão, revise o passo `prompt-2.md`.

## Passo 4 — Executar a Análise dos Resultados

Com o conjunto de instruções do passo anterior e o [curso versão 1.0](#retorno-chatgpt-1), iniciamos a avaliação crítica.

### Claude

<div align="center">
  <img src="imagens/print-claude-1.png" width="500px">
  <p style="font-size: 0.8em"> Página inicial </p>
</div>

Nesta fase, usamos o Claude (plano pago), enviamos os materiais de entrada e aguardamos a consolidação do relatório.

### Retorno Claude 1

Com base no [prompt do passo 3](#retorno-gemini-2), foi gerado o arquivo [ANALISE_CRITICA_CLAUDE_DESKTOP.md](passos/ANALISE_CRITICA_CLAUDE_DESKTOP.md).

Esse relatório contém 483 linhas, com introdução analítica e 7 capítulos cobrindo pontos fortes e pontos de melhoria do [curso versão 1.0](#retorno-chatgpt-1).

### 🚩 Marco de Desenvolvimento: Diagnóstico Crítico Concluído
> **O que validar agora:**
> - [ ] Você obteve o arquivo [ANALISE_CRITICA_CLAUDE_DESKTOP.md](passos/ANALISE_CRITICA_CLAUDE_DESKTOP.md) com pontos fortes, gargalos e correções práticas.
> - [ ] Você consegue apontar, no relatório, quais riscos são críticos para iniciantes (instalação, segurança e fluxo).
> 
> **Sinal Verde:** Se você já consegue transformar os achados em ações objetivas de melhoria, pode avançar.
> **Sinal Vermelho:** Se o relatório estiver opinativo e sem plano de ação, revise o passo `return-2.md`.

## Passo 5 — Gerar Instruções para Aprimorar a Versão 1.0

Com a análise crítica pronta, retornamos ao Gemini para criar um novo prompt de melhoria incremental do curso.

### Prompt Gemini 3

O prompt abaixo foi elaborado para transformar os achados críticos em ações de revisão objetiva:

[prompt-1.md](passos/prompt-3.md)

### Retorno Gemini 3

A versão devolvida pelo Gemini, que passou a orientar o refinamento do curso, foi:

[return-1.md](passos/return-3.md)

### 🚩 Marco de Desenvolvimento: Plano de Reformulação Definido
> **O que validar agora:**
> - [ ] Você confirmou que o prompt de reformulação exige objetivos e habilidades por aula.
> - [ ] Você verificou que o prompt inclui correções dos gargalos críticos identificados na análise.
> 
> **Sinal Verde:** Se você consegue usar esse prompt para reescrever o curso com direção clara, pode avançar.
> **Sinal Vermelho:** Se o prompt não conectar análise e correção, revise o passo `prompt-3.md`.

## Passo 6 — Aprimorar a Versão 1.0

Com o conjunto de instruções definido no [passo anterior](#retorno-gemini-3), iniciamos a etapa de reescrita.

### Claude

Retornamos ao mesmo contexto de chat no Claude (onde já havia sido gerada a análise crítica) e enviamos o [prompt-3](#retorno-gemini-3).

### Retorno Claude 2

Como resultado do [prompt-3](#retorno-gemini-3), foi produzido o arquivo [novo-roteiro-curso.md](passos/novo-roteiro-curso.md), com a proposta de curso revisada.

### 🚩 Marco de Desenvolvimento: Roteiro 2.0 Entregue
> **O que validar agora:**
> - [ ] Você gerou o arquivo [novo-roteiro-curso.md](passos/novo-roteiro-curso.md) com conteúdo completo e sem quebras.
> - [ ] Você verificou que as aulas ficaram mais acionáveis para iniciantes (objetivos, habilidades e prática).
> 
> **Sinal Verde:** Se você percebe ganho real de clareza e aplicabilidade em relação à versão 1.0, pode avançar.
> **Sinal Vermelho:** Se os problemas críticos persistirem, revise o passo `return-4-0.md`.

## Passo 7 — Gerar Instruções para Definir o Método de Carga Horária

Com o roteiro reformulado, passamos a estimar a carga horária do curso de forma estruturada. Para isso, solicitamos ao Gemini um prompt voltado à criação de uma métrica de tempo por tipo de atividade.

### Prompt Gemini 4

Diferentemente da primeira avaliação, aqui usamos duas aulas de amostragem para identificar padrões de estrutura e, com base neles, modelar uma metodologia de cálculo.

[prompt-4.md](passos/prompt-4.md)

### Retorno Gemini 4

O prompt resultante dessa etapa foi:

[return-4-0.md](passos/return-4-0.md)

### 🚩 Marco de Desenvolvimento: Método MET Estruturado
> **O que validar agora:**
> - [ ] Você confirma que o método separa atividades por tipo (teoria, prática, setup, feedback etc.).
> - [ ] Você consegue aplicar a métrica para comparar aulas diferentes sem mudar os critérios.
> 
> **Sinal Verde:** Se a MET está estável e replicável, pode avançar.
> **Sinal Vermelho:** Se os critérios ainda estiverem subjetivos, revise o passo `prompt-4.md`.

## Passo 8 — Construir o Método de Carga Horária

Na sequência, submetemos o [prompt-4](#retorno-gemini-4) em um novo chat do ChatGPT. No envio, anexamos duas aulas de referência (módulos 1 e 14), reunidas no arquivo [anexos-2-aulas-amostragem.md](passos/anexos-2-aulas-amostragem.md).

### Retorno ChatGPT 2

O ChatGPT retornou o arquivo [return-4-5.md](passos/return-4-5.md), do qual foi extraída a tabela-base apresentada a seguir:

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


### 🚩 Marco de Desenvolvimento: Tabela de Referência Validada
> **O que validar agora:**
> - [ ] Você conferiu que `tabela-tempo-atividade.md` está completa: tipo, descrição, tempo e justificativa.
> - [ ] Você consegue mapear qualquer atividade da aula para um tipo da tabela sem criar categorias novas.
> 
> **Sinal Verde:** Se a tabela funciona como base única de estimativa, pode avançar.
> **Sinal Vermelho:** Se faltarem categorias essenciais, revise o passo `return-4-5.md`.

## Passo 9 — Gerar Instruções para Avaliar a Carga Horária do Curso

Com a tabela de referência estabelecida, voltamos ao Gemini para estruturar o prompt final de avaliação temporal do curso completo.

### Prompt Gemini 5

Nesta iteração, enviamos ao Gemini apenas a tabela de tipos de elementos, suas descrições, tempos médios e justificativas pedagógicas. O prompt utilizado foi:

[prompt-5.md](passos/prompt-5.md)

### Retorno Gemini 5

A saída gerada para orientar a avaliação final foi:

[return-5.md](passos/return-5.md)

### 🚩 Marco de Desenvolvimento: Prompt Final de Carga Horária Homologado
> **O que validar agora:**
> - [ ] Você confirmou que `return-5.md` pede cálculo por aula + total do curso com método explícito.
> - [ ] Você verificou que o prompt exige análise de equilíbrio entre teoria e prática.
> 
> **Sinal Verde:** Se você consegue auditar o resultado final com esse prompt, pode avançar.
> **Sinal Vermelho:** Se os critérios de medição estiverem incompletos, revise o passo `prompt-5.md`.

## Passo 10 — Avaliar a Carga Horária do Curso

Por fim, enviamos o [prompt-5](#retorno-gemini-5) ao Claude, junto da [tabela-tempo-atividade.md](passos/tabela-tempo-atividade), no mesmo chat utilizado para consolidar este relato procedimental.

### Retorno Claude 3

Com base nesses insumos, o Claude retornou o arquivo [carga-horaria.md](passos/carga-horaria.md), contendo a análise de duração por aula e a estimativa total da carga horária do curso.

### 🚩 Marco de Desenvolvimento: Carga Horária Fechada
> **O que validar agora:**
> - [ ] Você obteve [carga-horaria.md](passos/carga-horaria.md) com tempo por aula, total e lógica de cálculo verificável.
> - [ ] Você consegue identificar, no documento, se a proporção teoria/prática está adequada para iniciantes.
> 
> **Sinal Verde:** Se os números estão rastreáveis e as recomendações finais estão claras, o processo foi replicado com sucesso.
> **Sinal Vermelho:** Se você não conseguir reproduzir os cálculos por aula, revise o passo `return-5.md`.
