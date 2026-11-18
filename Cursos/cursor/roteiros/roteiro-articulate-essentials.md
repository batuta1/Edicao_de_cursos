> » IA: Cover; preservar título e subtítulo.

# Plano de Aula — Cursor (Essentials)

*Compreender, delegar e verificar mudanças de código com segurança.*

> » IA: Table; preservar termos de interface em inglês.

## Identificação

| Campo | Definição |
|---|---|
| Curso | Cursor — Essentials |
| Natureza | Autoinstrucional, introdutório e prático |
| Carga horária | 123 minutos |
| Público-alvo | Pessoas com fundamentos de programação e Git, iniciantes no Cursor |
| Pré-requisitos | Cursor instalado, conta ativa, internet, Git e projeto sem dados sigilosos |
| Recursos necessários | Windows 10+, macOS 12+ ou Linux compatível; repositório com testes |

> » IA: Text; manter a data da fonte.

### Objetivo Geral

Compreender e aplicar um ciclo supervisionado de desenvolvimento assistido por IA, da preparação segura do ambiente à validação por diff e testes. Material-fonte coletado em 03/11/2026; menus, atalhos, planos e modelos devem ser reconferidos antes da publicação.

> » IA: List; preservar verbatim, sem acréscimos.

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. preparar um repositório com controles de privacidade, permissão e recuperação;
2. selecionar modo e contexto adequados;
3. formular solicitações verificáveis;
4. revisar e testar mudanças antes da aceitação;
5. registrar decisões e riscos residuais.

> » IA: Table; não alterar tempos.

### Estrutura e Sequência dos Módulos

| Módulo | Título | Referência | Tempo |
|---|---|---|---:|
| 0 | Preparação, privacidade e controle | Quickstart, Privacy, Security | 26 min |
| 1 | Cursor, contexto e modos | Cursor Learn: Models, Context, Agents | 21 min |
| 2 | Pedidos verificáveis | Working with agents | 22 min |
| 3 | Do plano à mudança | Creating features | 24 min |
| 4 | Revisão, testes e recuperação | Reviewing and testing | 20 min |
| 5 | Síntese integrada | Quickstart e Gilded Rose | 10 min |

---

# Módulo 0 — Preparação, Privacidade e Controle

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 0" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> » IA: Statement; preservar breadcrumb e ponto de controle.

> Ponto de partida: preparar um ambiente reversível e sem dados sigilosos antes do primeiro pedido.

> » IA: List; preservar verbatim.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

- identificar requisitos de instalação;
- conferir Privacy Mode e execução de comandos;
- explicar o limite do `.cursorignore`;
- demonstrar um estado Git recuperável.

> » IA: Text; manter os nomes de sistemas e não inventar requisitos.

### Texto Descritivo

O Cursor requer Windows 10 ou superior, macOS 12 ou superior ou Linux compatível. No Windows, executa-se o instalador; no macOS, move-se o aplicativo para `Applications`; no Linux, os pacotes `apt` ou `dnf` são preferíveis ao AppImage. Após o login, abre-se o projeto em `Cursor > File > Open Folder`.

Recursos de IA enviam prompts e trechos de contexto a provedores. O Privacy Mode impede uso do código para treinamento, mas não implica processamento exclusivamente local. Deve-se conferir `Cursor > Cursor Settings > General > Privacy Mode`, pois o estado padrão de contas individuais não foi confirmado.

O `.cursorignore` complementa a proteção, mas comandos de terminal e MCP podem operar fora desse controle. Segredos, tokens, `.env` real e dados pessoais não devem permanecer no projeto didático.

O Agent pode editar arquivos e executar comandos. A documentação consultada diverge sobre o padrão de aprovação. Deve-se observar `Cursor > Cursor Settings > Agents > Approvals & Execution`. `Auto-review` não é fronteira de segurança; `Run Everything` não é recomendado. Git oferece recuperação durável; checkpoints são auxiliares locais.

> » IA: Process; preservar breadcrumbs e comandos.

### Exercício Prático — Checklist de prontidão (4 min)

1. Abrir o Gilded Rose em `Cursor > File > Open Folder`.
2. Confirmar ausência de segredos e dados pessoais.
3. Conferir `Cursor > Cursor Settings > General > Privacy Mode`.
4. Conferir `Cursor > Cursor Settings > Agents > Approvals & Execution`.
5. Executar `git status` no terminal.

> » IA: Statement; preservar emoji.

🏁 Ponto de controle: o projeto abre, os testes têm comando conhecido e o Git apresenta um ponto inicial recuperável.

> » IA: Statement ou Download; preservar verbatim e as aspas triplas.

### Mão na massa

"""
Antes de editar qualquer arquivo, examine este repositório e informe: (1) se há arquivos que podem conter segredos ou dados pessoais; (2) qual comando executa os testes; (3) qual é o estado atual do Git. Não altere nada. Cite os arquivos usados como evidência.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 0" — encerre esta lição aqui. ▲▲▲*

---

# Módulo 1 — Cursor, Contexto e Modos de Trabalho

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> » IA: Statement; preservar a nota de encadeamento.

> Com o ambiente protegido, o foco passa à escolha do mecanismo de assistência adequado.

> » IA: List; verbatim.

### Objetivos de Aprendizagem

- diferenciar Tab, Ask, Agent, Plan e Debug;
- explicar contexto e janela de contexto;
- reconhecer limitações probabilísticas;
- justificar a escolha de modo.

> » IA: Text; não restaurar o antigo Cmd/Ctrl+K.

### Texto Descritivo

Tab sugere código durante a digitação. Ask favorece compreensão sem alteração. Agent pesquisa, edita e executa comandos. Plan organiza mudanças maiores antes de construir. Debug parte de sintomas e evidências. O antigo fluxo de edição inline por `Cmd/Ctrl+K` foi aposentado em 26/10/2026; o curso não o ensina.

Contexto reúne prompt, arquivos, regras, ferramentas e histórico. A janela é finita; conversas longas podem ser resumidas. Deve-se anexar apenas o necessário e pedir pesquisa dirigida. Modelos são probabilísticos e podem gerar respostas plausíveis, porém incorretas.

> » IA: Table; preservar termos de modo.

| Intenção | Modo inicial | Controle |
|---|---|---|
| Compreender | Ask | Proibir edição e exigir arquivos |
| Planejar mudança ampla | Plan | Revisar etapas antes de Build |
| Investigar falha | Debug | Fornecer logs e hipótese |
| Executar tarefa delimitada | Agent | Acompanhar diff e testes |

> » IA: Knowledge Check; uma resposta por cenário, aceitar justificativas equivalentes.

### Exercício Prático — Escolha do modo (6 min)

Qual modo deve iniciar a investigação de um teste que falha de forma reproduzível?

- Ask
- Plan
- Debug
- Tab

**Gabarito:** Debug, porque há evidência de execução a ser investigada.

> » IA: Statement ou Download; verbatim.

### Mão na massa

"""
Use [Ask/Plan/Debug/Agent] para [objetivo]. Não altere arquivos até [ponto de decisão]. Baseie suas afirmações em [arquivos/logs] e valide com [comando ou comportamento].
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 1" — encerre esta lição aqui. ▲▲▲*

---

# Módulo 2 — Pedidos Verificáveis

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> » IA: Statement.

> Definidos os modos, passa-se a construir instruções com limites e evidência de conclusão.

> » IA: List; verbatim.

### Objetivos de Aprendizagem

- decompor uma demanda em resultado verificável;
- incluir contexto e restrições;
- usar menções seletivamente;
- definir validação independente.

> » IA: Text; preservar a estrutura em cinco partes.

### Texto Descritivo

Um pedido verificável contém objetivo, contexto, restrições, processo e validação. “Melhore o código” transfere decisões essenciais ao agente. “Proponha três melhorias pequenas, explique os trade-offs e aguarde minha escolha” cria um ponto de decisão.

Menções com `@` anexem arquivos, pastas ou terminais, mas não substituem a explicação do papel de cada item. Critérios de êxito podem ser testes, lint, verificação de tipos, build ou comportamento manual observável.

> » IA: Process; manter a tarefa sem fornecer uma solução pronta.

### Exercício Prático — Reescrita (6 min)

1. Partir de “corrija o projeto”.
2. Especificar a regra “Conjurado”.
3. Limitar arquivos e proibir alteração de testes existentes.
4. Exigir plano antes da edição.
5. Indicar o comando de teste.

> » IA: Statement; critério verbatim.

**Critério de êxito:** uma terceira pessoa consegue decidir objetivamente se a tarefa terminou.

> » IA: Statement ou Download; preservar aspas triplas.

### Mão na massa

"""
Objetivo: [resultado observável].
Contexto: [arquivos, erro, requisito].
Restrições: [o que não mudar].
Processo: [explique ou planeje antes de editar].
Validação: [comando e resultado esperado].
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 2" — encerre esta lição aqui. ▲▲▲*

---

# Módulo 3 — Do Plano à Mudança

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> » IA: Statement.

> Com pedidos verificáveis, aplica-se o ciclo compreender–planejar–executar–testar.

> » IA: List; verbatim.

### Objetivos de Aprendizagem

- solicitar exploração antes da alteração;
- revisar um plano;
- verificar comandos antes da autorização;
- aplicar um ciclo de TDD.

> » IA: Text; preservar breadcrumb e a restrição de testes.

### Texto Descritivo

Mudanças maiores começam pela compreensão do código. Em `Cursor > Agent > Mode > Plan`, o Agent propõe etapas; a pessoa revisa arquivos, ordem e verificações antes de Build. Durante a execução, cada comando deve ser lido com seu diretório, efeito e forma de reversão.

No TDD, confirma-se primeiro uma falha, preservam-se os testes e implementa-se apenas o necessário para fazê-los passar. Deve-se interromper quando surgem arquivos alheios, remoção de testes ou redefinição do requisito.

> » IA: Process; preservar comandos como texto literal quando presentes.

### Exercício Prático — Plano mínimo (6 min)

1. Abrir `Cursor > Agent > Mode > Plan`.
2. Solicitar um plano de no máximo quatro etapas para “Conjurado”.
3. Exigir um teste inicialmente falho.
4. Conferir arquivos e comando de validação.
5. Autorizar Build somente após a revisão.

> » IA: Statement; preservar emoji.

🏁 Ponto de controle: o plano preserva testes existentes e inclui evidência por etapa.

> » IA: Statement ou Download; verbatim.

### Mão na massa

"""
Planeje [mudança]. Não edite ainda. Preserve os testes existentes. Comece por um teste que falha, limite a alteração a [arquivos/área] e indique a validação de cada etapa. Aguarde minha aprovação.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 3" — encerre esta lição aqui. ▲▲▲*

---

# Módulo 4 — Revisão, Testes e Recuperação

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> » IA: Statement.

> Após a execução, o foco passa da geração à responsabilidade sobre o resultado.

> » IA: List; verbatim.

### Objetivos de Aprendizagem

- interpretar um diff;
- identificar mudança alheia ao pedido;
- combinar testes e inspeção;
- distinguir checkpoint de Git.

> » IA: Text; não resumir.

### Texto Descritivo

O diff deve ser lido arquivo por arquivo. A revisão verifica requisito, escopo, preservação dos testes, dependências e riscos. Testes automatizados comprovam propriedades específicas; lint, type checker, build e inspeção manual cobrem outras dimensões.

Checkpoints guardam estados locais da sessão. Git registra histórico durável. Agent Review pode apoiar a leitura, mas não substitui a decisão responsável.

> » IA: Table; manter campos editáveis.

| Arquivo/área | Efeito | Evidência | Decisão |
|---|---|---|---|
| [preencher] | [preencher] | [comando/resultado] | Aceitar/Rejeitar |

> » IA: Checklist; preservar ordem.

### Exercício Prático — Decisão com evidência (4 min)

- [ ] Ler o diff inteiro.
- [ ] Executar testes.
- [ ] Executar uma verificação adicional.
- [ ] Inspecionar um caso de borda.
- [ ] Registrar risco residual.

> » IA: Statement; critério verbatim.

**Critério de êxito:** a decisão cita efeito, evidência e risco residual.

> » IA: Statement ou Download; verbatim.

### Mão na massa

"""
Revise esta mudança sem editar. Liste: requisito atendido, arquivos fora do escopo, testes alterados, riscos e verificações ainda necessárias. Separe fatos do diff de inferências.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 4" — encerre esta lição aqui. ▲▲▲*

---

# Módulo 5 — Síntese e Aplicação Integrada

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 5" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> » IA: Statement.

> A etapa final reúne proteção, contexto, planejamento, execução e revisão.

> » IA: List; verbatim.

### Objetivos de Aprendizagem

- executar o ciclo completo;
- validar uma mudança pequena;
- registrar decisão e risco;
- recuperar o estado quando necessário.

> » IA: Text.

### Texto Descritivo

A competência central não consiste em gerar mais código, mas em controlar um processo: ambiente reversível, pedido verificável, execução observada e validação independente.

> » IA: Process; preservar a sequência.

### Exercício Prático — Mudança supervisionada (10 min)

1. Conferir dados, permissões e Git.
2. Explorar sem editar.
3. Formular pedido verificável.
4. Revisar o plano.
5. Autorizar a mudança.
6. Ler o diff e rodar testes.
7. Registrar a decisão.

> » IA: Checklist; verbatim.

| Critério de avaliação | Atendido? |
|---|---|
| Dados e permissões conferidos | [ ] |
| Pedido verificável | [ ] |
| Plano revisto | [ ] |
| Diff lido | [ ] |
| Testes e inspeção executados | [ ] |
| Decisão e risco registrados | [ ] |

> » IA: Statement ou Download; verbatim.

### Mão na massa

"""
Conduza [mudança pequena] em etapas. Primeiro explique; depois proponha um plano e aguarde. Só então implemente. Ao final, execute [validação], apresente o diff por arquivo e liste riscos residuais.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 5" — encerre esta lição aqui. ▲▲▲*

---

> » IA: Text; sem marcador de lição.

# Encerramento

O curso estabelece um método responsável: compreender antes de modificar, delimitar antes de delegar e verificar antes de aceitar. A prática regular deve preservar o ciclo mesmo em tarefas pequenas.

Como aprofundamento, recomendam-se Rules, `AGENTS.md`, TDD, Agent Review, Cloud Agents, Bugbot e CLI, um recurso por vez.

> » IA: Statement; preservar verbatim.

> **Síntese:** a velocidade do agente só produz valor quando acompanhada de contexto, limites e evidências.

