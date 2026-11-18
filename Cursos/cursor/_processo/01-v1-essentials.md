# Plano de Aula — Cursor (Essentials)

## Identificação

| Campo | Definição |
|---|---|
| Curso | Cursor — Essentials |
| Natureza | Introdutório, autoinstrucional e prático |
| Carga horária | 123 minutos |
| Público-alvo | Pessoas com fundamentos de programação e Git, iniciantes no Cursor |
| Pré-requisitos | Cursor instalado, conta ativa, internet e projeto de prática versionado |
| Recursos necessários | Computador compatível, Git e repositório sem dados sigilosos |

### Objetivo Geral

Compreender o funcionamento do Cursor e aplicar um ciclo supervisionado de desenvolvimento assistido por IA, da preparação segura do ambiente à validação das alterações por diff e testes.

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. preparar um projeto local para uso seguro no Cursor;
2. distinguir Tab, Ask, Agent, Plan e Debug e selecionar o modo adequado;
3. formular solicitações com objetivo, contexto, restrições e critério de êxito;
4. revisar alterações propostas e validá-las com testes antes da aceitação.

### Estrutura e Sequência dos Módulos

O percurso parte da preparação do ambiente, explica a arquitetura de interação, desenvolve a competência de delegação e termina em revisão integrada.

| Módulo | Título | Referência | Tempo |
|---|---|---|---:|
| 0 | Preparação, privacidade e controle | Pesquisa, seções 2, 3 e 8 | 26 min |
| 1 | Cursor, contexto e modos de trabalho | Cursor Learn e pesquisa, seções 4 e 5 | 21 min |
| 2 | Pedidos verificáveis | Learn: Working with agents e Context | 22 min |
| 3 | Do plano à mudança | Learn: Creating features | 24 min |
| 4 | Revisão, testes e recuperação | Learn: Reviewing and testing | 20 min |
| 5 | Síntese e aplicação integrada | Quickstart e Gilded Rose | 10 min |

---

# Módulo 0 — Preparação, Privacidade e Controle

> Ponto de partida: prepara-se um ambiente reversível e sem dados sigilosos antes do primeiro pedido ao Agent.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

- identificar requisitos de instalação e conta;
- ativar ou conferir o Privacy Mode;
- explicar por que `.cursorignore` não substitui uma política de dados;
- confirmar um estado inicial recuperável com Git.

### Texto Descritivo

O Cursor reúne editor, terminal, controle de versão e recursos de IA. Os recursos de IA enviam prompts e trechos de contexto a provedores de modelos. Por isso, a preparação não se limita à instalação: inclui a seleção de um repositório de prática sem dados pessoais, credenciais ou segredos.

O Privacy Mode impede que o código seja utilizado para treinamento, mas não torna todo fluxo local. A documentação informa que prompts e contexto podem ser enviados a provedores. Arquivos ignorados também podem ser alcançados por comandos de terminal ou ferramentas externas. Convém manter `.env`, chaves e bases reais fora do projeto didático.

O Agent pode editar arquivos do workspace e executar comandos. O Git constitui a camada de recuperação durável; checkpoints do Cursor são auxiliares locais e não substituem commits. Recomenda-se iniciar com `Auto-review` ou `Allowlist`, nunca com `Run Everything` em repositório desconhecido.

### Exercício Prático — Checklist de prontidão (4 min)

1. Abrir um repositório de prática no Cursor.
2. Confirmar que não há segredos nem dados pessoais.
3. Conferir o Privacy Mode e as configurações de aprovação.
4. Confirmar que `git status` apresenta um estado conhecido.

**Critério de êxito:** os quatro itens são verificados e o participante sabe explicar como reverter uma mudança.

---

# Módulo 1 — Cursor, Contexto e Modos de Trabalho

> Com o ambiente protegido, o foco passa para a escolha do mecanismo de assistência adequado.

### Objetivos de Aprendizagem

- diferenciar autocomplete, conversa, planejamento e execução;
- explicar contexto e janela de contexto;
- escolher entre Ask, Agent, Plan e Debug;
- reconhecer que o modelo é probabilístico.

### Texto Descritivo

O Cursor oferece Tab para sugestões durante a digitação e um Agent capaz de pesquisar o projeto, editar arquivos e executar comandos. Ask favorece compreensão sem edição; Plan organiza mudanças maiores; Debug parte de evidências de execução; Agent realiza a tarefa. A escolha do modo reduz ações desnecessárias.

Contexto é a informação disponível ao modelo: prompt, arquivos, regras, ferramentas e histórico. A janela de contexto é limitada; conversas extensas podem ser resumidas. Incluir apenas arquivos relevantes costuma ser mais eficaz do que despejar todo o repositório.

Modelos geram saídas probabilísticas, não provas. Uma resposta plausível pode estar errada ou citar uma API inexistente. A verificação deve ser planejada antes da geração.

### Exercício Prático — Escolha do modo (6 min)

Classificar quatro situações: compreender arquitetura; planejar refatoração; corrigir falha reproduzível; alterar um texto simples.

**Gabarito:** Ask; Plan; Debug; Agent, respectivamente, admitindo variações justificadas.

---

# Módulo 2 — Pedidos Verificáveis

> Definidos os modos, passa-se a construir instruções que reduzam ambiguidade e escopo excessivo.

### Objetivos de Aprendizagem

- decompor uma demanda em resultado verificável;
- incluir contexto e restrições relevantes;
- usar menções a arquivos sem inflar o contexto;
- exigir validação explícita.

### Texto Descritivo

Um bom pedido contém objetivo, contexto, restrições e critério de conclusão. “Melhore o código” transfere ao agente decisões que pertencem à pessoa responsável. “Explique três melhorias pequenas, não altere arquivos e aguarde minha escolha” delimita a tarefa e cria um ponto de decisão.

Menções com `@` ajudam a anexar arquivos, pastas, terminais ou conversas. O recurso deve ser usado de forma seletiva. O agente também pesquisa o repositório, mas precisa de direção para distinguir a parte relevante do ruído.

Critérios verificáveis incluem testes, lint, type checker, build ou comportamento observável. Quando não existe teste automatizado, deve-se descrever como a pessoa confirmará o resultado.

### Exercício Prático — Reescrita de prompt (6 min)

Reescrever “corrija o projeto” com: arquivo ou área, falha observada, restrição de escopo, proibição de editar testes e comando de validação.

**Critério de êxito:** o pedido permite decidir objetivamente se a tarefa terminou.

---

# Módulo 3 — Do Plano à Mudança

> Com pedidos verificáveis, aplica-se um fluxo de entendimento, planejamento, execução e teste.

### Objetivos de Aprendizagem

- solicitar exploração antes de alteração;
- avaliar um plano antes de autorizar sua execução;
- acompanhar ferramentas e comandos usados pelo Agent;
- manter o escopo durante a implementação.

### Texto Descritivo

Mudanças maiores devem começar pela compreensão do código. Recomenda-se pedir os pontos de entrada, módulos envolvidos e testes relacionados. Em seguida, o Plan Mode transforma o objetivo em etapas revisáveis. Somente após a aprovação do plano se inicia a implementação.

Durante a execução, o Agent pode pesquisar, editar e chamar o terminal. O fato de uma ferramenta ter sido acionada não confirma a correção do resultado. Convém acompanhar arquivos tocados, comandos e mensagens de erro, interrompendo desvios de escopo.

Em desenvolvimento orientado a testes, cria-se ou confirma-se primeiro uma falha, preservam-se os testes e implementa-se apenas o suficiente para fazê-los passar. Esse ciclo reduz a possibilidade de o agente redefinir o problema para parecer bem-sucedido.

### Exercício Prático — Fluxo em quatro etapas (6 min)

Ordenar e executar, em um projeto de prática: compreender; planejar; implementar; testar.

**Critério de êxito:** existe um plano aprovado, a mudança permanece no escopo e uma verificação foi executada.

---

# Módulo 4 — Revisão, Testes e Recuperação

> Após a execução, o foco desloca-se da geração para a responsabilidade sobre o resultado.

### Objetivos de Aprendizagem

- interpretar um diff;
- identificar mudança não solicitada;
- combinar testes automatizados e inspeção humana;
- distinguir checkpoint de commit Git.

### Texto Descritivo

O diff representa linhas adicionadas, removidas ou modificadas. Sua revisão deve responder: a alteração resolve o pedido, toca apenas os arquivos necessários, preserva testes e introduz risco de segurança? Aceitar o diff sem leitura equivale a incorporar código de autoria desconhecida.

Testes comprovam propriedades específicas, não a ausência total de defeitos. Convém executar testes, lint, verificação de tipos ou build e, quando aplicável, realizar uma inspeção manual. O Agent Review pode apoiar a leitura, mas não substitui o julgamento responsável.

Checkpoints registram estados locais da sessão; commits integram o histórico do projeto. Se o Agent desviar, restaura-se um checkpoint ou reverte-se pelo Git, conforme o estágio e a durabilidade necessária.

### Exercício Prático — Aceitar ou rejeitar (4 min)

Revisar um diff e registrar uma decisão em três linhas: efeito pretendido, risco encontrado e evidência de validação.

**Critério de êxito:** a aceitação ou rejeição é sustentada por evidência, não pela aparência da resposta.

---

# Módulo 5 — Síntese e Aplicação Integrada

> A etapa final reúne preparação, delegação, execução e revisão em um único ciclo supervisionado.

### Objetivos de Aprendizagem

- executar o ciclo completo com autonomia;
- manter dados e permissões sob controle;
- validar uma pequena alteração no Gilded Rose;
- registrar a decisão final.

### Texto Descritivo

A competência central não consiste em obter mais código, mas em controlar um processo: ambiente reversível, pedido verificável, execução observada e validação independente. O exercício integrado utiliza uma alteração pequena para que a atenção permaneça no método.

### Exercício Prático — Mudança supervisionada (10 min)

1. Confirmar a segurança e o estado Git do projeto.
2. Pedir ao Agent que localize a regra relevante sem editar.
3. Solicitar um plano curto e aprová-lo.
4. Autorizar a alteração e executar os testes.
5. Revisar o diff e aceitar ou rejeitar.

| Critério de avaliação | Atendido? |
|---|---|
| O repositório não contém dados sigilosos | [ ] |
| O pedido inclui restrição e critério de êxito | [ ] |
| O plano foi revisto antes da implementação | [ ] |
| O diff foi lido | [ ] |
| Testes ou verificação equivalente foram executados | [ ] |

# Encerramento

O curso estabelece uma base para o uso responsável do Cursor: compreender antes de modificar, delimitar antes de delegar e verificar antes de aceitar. A prática regular deve preservar esse ciclo mesmo em tarefas pequenas.

Como aprofundamento, recomendam-se Rules, `AGENTS.md`, TDD, Agent Review, Cloud Agents, Bugbot e CLI, sempre após a consolidação do fluxo local supervisionado.

> **Síntese:** a velocidade do agente só produz valor quando acompanhada de contexto, limites e evidências.

