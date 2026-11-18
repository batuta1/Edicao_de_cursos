# Roteiro Final — Cursor Hands-on

**Público-alvo:** pessoas com fundamentos de programação e Git, iniciantes no Cursor.  
**Objetivo geral:** concluir e revisar uma pequena mudança real com o Agent.  
**Pré-requisitos:** Cursor instalado e autenticado, Git, internet e uma implementação do Gilded Rose cujo comando de teste local já funcione.

## Estrutura do Curso

- **Nível 1 — Preparar e compreender:** Oficinas 1 e 2.
- **Nível 2 — Construir e verificar:** Oficinas 3 e 4.
- **Entrega autônoma:** Projeto Final.

> A fonte foi coletada em 03/11/2026. Se um nome de menu ou modo tiver mudado, procure o termo atual em Settings e registre a diferença para revisão editorial.

## Antes de Arregaçar as Mangas

Você vai usar o Cursor em um projeto de prática e manter o controle do começo ao fim. Escolha uma linguagem do Gilded Rose que você consiga executar localmente. Antes de chamar o Agent, rode a suíte uma vez.

> 🔑 **Regra de ouro:** o Agent pode acelerar a execução; responsabilidade, permissão e decisão continuam com você.

---

## Oficina 1 — Prepare o Terreno (23 min)

### Descrição

- **Objetivos da Aula:** preparar privacidade, permissões, dados e recuperação.
- **Habilidades Esperadas:** abrir sozinho um projeto limpo e comprovar um ponto inicial reversível.

### 🎯 O Problema

Você quer experimentar o Agent sem expor segredos, aceitar comandos perigosos ou perder o estado inicial.

- **📸 Sugestão de Prints:** Settings com Privacy Mode; `Approvals & Execution`; terminal com `git status`; Explorer sem `.env` real.

### 🧰 O que você vai usar

- Cursor Settings;
- Git;
- `.cursorignore`;
- kata Gilded Rose.

### 👐 Mão na massa

1. Abra o projeto em `File > Open Folder`.
2. Rode a suíte de testes uma vez e anote o comando.
3. Procure segredos, tokens, `.env` e dados pessoais. Retire-os do projeto didático.
4. Confira `Cursor Settings > General > Privacy Mode`.
5. Confira `Cursor Settings > Agents > Approvals & Execution`.
6. Mantenha `Auto-review` ou use `Allowlist`; não selecione `Run Everything`.
7. Rode `git status`. Se houver alterações, revise e escolha: commitar, guardar ou usar cópia limpa.
8. Identifique como voltar ao estado inicial.

> ⚠️ O `.cursorignore` não bloqueia necessariamente comandos de terminal ou ferramentas MCP. Não use o ignore como cofre.

### ✅ Deu certo?

O projeto está sem dados sigilosos, os testes executam e o Git mostra um ponto inicial conhecido.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Menu diferente | Pesquise `Privacy` ou `Approvals` em Settings |
| Testes não executam | Troque para uma implementação do kata compatível com seu ambiente |
| Repositório sujo | Não prossiga até decidir o destino de cada alteração |

### 🚀 Quer ir além?

1. Crie `.cursorignore` para artefatos locais e valide que o Agent não os sugere como contexto.
2. Use `Allowlist` vazia e confirme que cada comando pede decisão.
3. Faça um commit-base com mensagem clara e confirme que `git status` fica limpo.

---

## Oficina 2 — Converse com o Código (35 min)

### Descrição

- **Objetivos da Aula:** usar Ask, menções e pesquisa para compreender o projeto sem edição.
- **Habilidades Esperadas:** localizar regra e testes, checar afirmações do Agent e reiniciar o contexto quando necessário.

### 🎯 O Problema

Você recebeu um projeto desconhecido. Antes de mudar qualquer linha, precisa descobrir onde a regra de negócio vive e como ela é verificada.

- **📸 Sugestão de Prints:** seletor Ask; prompt no painel; resposta citando arquivos; anel de contexto aberto.

### 🧰 O que você vai usar

- Ask;
- `@` para arquivos;
- Explorer;
- requisitos e testes.

### 👐 Mão na massa

1. Abra o Agent com `Ctrl+I` ou `Cmd+I`.
2. Selecione Ask.
3. Envie:

> Explique este projeto. Aponte os pontos de entrada, a regra de atualização de qualidade e os testes. Cite os arquivos. Não altere nada.

4. Abra dois arquivos citados e confira as afirmações.
5. Anexe os requisitos em português com `@` e pergunte o que ainda não foi implementado.
6. Peça três melhorias pequenas e seguras, com trade-offs, e mande aguardar sua escolha.
7. Se a conversa ficar longa, abra outra com um resumo e somente os arquivos relevantes.

### ✅ Deu certo?

Você localiza regra e testes e o repositório permanece sem diff criado pelo Agent.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Arquivo não aparece | Confira `.cursorignore`/`.gitignore`, use `@` ou reindexe |
| Resposta inventa detalhes | Peça arquivo e trecho de suporte; confira no código |
| Contexto saturado | Inicie conversa nova com resumo mínimo |

### 🚀 Quer ir além?

1. Peça um diagrama textual e valide três relações no código.
2. Solicite que o Agent separe fatos, inferências e perguntas abertas.
3. Compare a explicação de Ask com sua leitura do README e registre divergências.

---

## Oficina 3 — Planeje Antes de Editar (24 min)

### Descrição

- **Objetivos da Aula:** construir um plano restrito, aplicar TDD e supervisionar comandos.
- **Habilidades Esperadas:** revisar um plano, recusar comandos ou arquivos inadequados e manter testes como restrição.

### 🎯 O Problema

Você precisa implementar a regra “Conjurado”, mas quer impedir que o Agent mude o problema ou enfraqueça os testes.

- **📸 Sugestão de Prints:** Plan Mode; plano com quatro etapas; comando de teste aguardando aprovação; botão Build.

### 🧰 O que você vai usar

- requisitos Gilded Rose em português;
- Plan Mode;
- Agent;
- terminal e testes.

### 👐 Mão na massa

1. Leia a regra “Conjurado”.
2. Ative Plan Mode com `Shift+Tab` no campo do Agent ou pelo seletor atual.
3. Envie:

> Planeje a implementação de “Conjurado”. Não edite ainda. Preserve testes existentes. Comece por um caso que falha, limite a mudança à regra necessária e indique o comando de validação.

4. Reduza o plano a no máximo quatro etapas, se necessário.
5. Confira arquivos, comando, diretório, efeitos e forma de reversão.
6. Autorize Build somente após a revisão.
7. Interrompa se testes existentes forem editados, se surgirem arquivos alheios ou se o comando não for compreendido.

### ✅ Deu certo?

O diff trata da regra “Conjurado”, mantém testes existentes e inclui a evidência do comando executado.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Plano amplo | Exigir um arquivo ou comportamento por etapa |
| Agent altera teste | Interromper, restaurar e reafirmar a restrição |
| Comando parece destrutivo | Não autorizar; pedir efeito, alvo e reversão |

### 🚀 Quer ir além?

1. Faça o Agent comprovar que o novo teste falha antes da implementação.
2. Peça duas soluções e compare complexidade e risco antes de escolher.
3. Defina um limite explícito de arquivos e valide o diff contra ele.

---

## Oficina 4 — Revise sem Fé Cega (20 min)

### Descrição

- **Objetivos da Aula:** revisar diff, validar em camadas e recuperar estado.
- **Habilidades Esperadas:** aceitar ou rejeitar uma mudança com justificativa e risco residual.

### 🎯 O Problema

O Agent declarou sucesso. Você precisa provar se a mudança atende ao requisito sem efeitos colaterais.

- **📸 Sugestão de Prints:** diff arquivo a arquivo; terminal com testes; Problems; Restore Checkpoint; histórico Git.

### 🧰 O que você vai usar

- diff view;
- testes;
- lint, type checker ou build, quando disponíveis;
- inspeção manual;
- checkpoint e Git.

### 👐 Mão na massa

1. Leia o diff inteiro.
2. Explique cada condição adicionada.
3. Procure arquivos fora do escopo, testes removidos e dependências novas.
4. Rode a suíte.
5. Rode uma segunda verificação disponível.
6. Inspecione manualmente um caso normal e um caso de borda.
7. Registre arquivo, efeito, evidência, decisão e risco residual.
8. Restaure checkpoint ou reverta com Git quando a mudança não merecer aceitação.

### ✅ Deu certo?

Sua decisão cita evidência de teste e de inspeção, não apenas a mensagem do Agent.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Testes passam e regra parece errada | Acrescente caso de borda derivado do requisito |
| Diff é grande | Rejeite e peça divisão em mudanças menores |
| Execução expira | Exporte logs pela Command Palette e reinicie a sessão |

### 🚀 Quer ir além?

1. Peça autorrevisão e compare com sua lista.
2. Execute mutação deliberada e confirme que um teste a detecta.
3. Produza um comentário de revisão com risco e recomendação.

---

## Projeto Final — Mudança Pequena, Evidência Grande (16 min)

### Descrição

- **Objetivos da Aula:** integrar todas as etapas em uma entrega autônoma.
- **Habilidades Esperadas:** conduzir o ciclo sem roteiro passo a passo e produzir registro auditável.

### 🎯 A missão

Escolha uma melhoria pequena no kata e entregue uma decisão completa: o que mudou, por que, como foi validado e qual risco ainda existe.

- **📸 Sugestão de Prints:** mosaico com estado Git inicial, prompt, plano, diff, testes e tabela de decisão.

### 👐 Mão na massa

1. Confira dados, permissões e estado Git.
2. Explore sem editar.
3. Defina objetivo, contexto, restrições e validação.
4. Revise o plano.
5. Autorize a implementação.
6. Leia o diff.
7. Execute testes e inspeção.
8. Registre a decisão.

### 🏁 Como saber que terminou

- [ ] O projeto não contém dados sensíveis.
- [ ] O estado inicial é recuperável.
- [ ] O pedido tem escopo e critério de êxito.
- [ ] O plano foi aprovado antes da edição.
- [ ] O diff foi lido integralmente.
- [ ] Testes e inspeção passaram.
- [ ] A decisão e o risco residual foram registrados.

## A Parte dos Dez — Hábitos que Salvam seu Repositório

1. Comece por uma tarefa pequena.
2. Peça compreensão antes de edição.
3. Defina o que não deve mudar.
4. Use contexto seletivo.
5. Leia comandos antes de autorizar.
6. Não coloque segredos no projeto didático.
7. Use Git além de checkpoints.
8. Revise cada arquivo do diff.
9. Teste casos de borda.
10. Recomece quando o contexto perder foco.

## Conseguiu! E agora?

Você concluiu o ciclo preparar → compreender → planejar → executar → verificar. Repita-o em tarefas pequenas até que evidência e revisão venham antes da aceitação.

Como próximos passos, explore Rules, `AGENTS.md`, TDD, Agent Review, Cloud Agents, Bugbot e CLI separadamente. Mantenha o mesmo padrão: escopo explícito, permissão consciente, diff lido e teste executado.

