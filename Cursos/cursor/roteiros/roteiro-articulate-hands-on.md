> » IA: Cover; preservar título e subtítulo.

# Cursor Para Leigos — Curso Hands-on

*Conclua e revise uma pequena mudança real com o Agent.*

> » IA: Text; não alterar a data.

## Antes de Arregaçar as Mangas

Você vai usar o Cursor em um projeto de prática e manter o controle do começo ao fim. A fonte foi coletada em 03/11/2026; nomes de menus, atalhos, planos e modelos devem ser conferidos antes da publicação.

> » IA: Checklist; preservar termos de interface.

O que você precisa ter aberto agora:

- [ ] Cursor instalado e autenticado;
- [ ] Git disponível;
- [ ] uma implementação do Gilded Rose cujo teste local já funciona;
- [ ] requisitos `gilded-rose-requisitos-pt-br.md`;
- [ ] terminal no diretório correto.

> » IA: Statement; preservar emoji e texto verbatim.

> 🔑 **Regra de ouro:** o Agent pode acelerar a execução; responsabilidade, permissão e decisão continuam com você.

> » IA: Table; não alterar tempos.

## O Mapa da Mão na Massa

| Oficina | Problema que vai resolver | Tempo |
|---|---|---:|
| 1 | Preparar projeto reversível e sem segredos | 23 min |
| 2 | Compreender o código sem editar | 35 min |
| 3 | Planejar e implementar mudança pequena | 24 min |
| 4 | Revisar diff e diagnosticar falhas | 20 min |
| Projeto Final | Entregar mudança validada | 16 min |

> » IA: Text.

As oficinas formam um único ciclo: preparar, compreender, planejar, executar e verificar.

---

# Oficina 1 — Prepare o Terreno

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> » IA: Text.

### 🎯 O Problema

Você quer experimentar o Agent sem expor segredos, aceitar comandos perigosos ou perder o estado inicial.

> » IA: List.

### 🧰 O que você vai usar

- Cursor Settings;
- Git;
- `.cursorignore`;
- kata Gilded Rose.

> » IA: Process; preservar breadcrumbs e comandos.

### 👐 Mão na massa

1. Abra o projeto em `Cursor > File > Open Folder`.
2. Rode a suíte de testes e anote o comando.
3. Retire segredos, tokens, `.env` e dados pessoais.
4. Confira `Cursor > Cursor Settings > General > Privacy Mode`.
5. Confira `Cursor > Cursor Settings > Agents > Approvals & Execution`.
6. Mantenha `Auto-review` ou use `Allowlist`; não selecione `Run Everything`.
7. Rode `git status`. Se houver alterações, revise e escolha: commitar, guardar ou usar cópia limpa.
8. Identifique como voltar ao estado inicial.

> » IA: Statement; preservar emoji.

> ⚠️ O `.cursorignore` não bloqueia necessariamente terminal ou MCP. Não use o ignore como cofre.

> » IA: Statement; preservar emoji e breadcrumb.

### ✅ Deu certo?

🏁 Ponto de controle: o projeto está sem dados sigilosos, os testes executam e o Git mostra um ponto inicial conhecido.

> » IA: Accordion; um item por linha.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Menu diferente | Pesquise `Privacy` ou `Approvals` em Settings |
| Testes não executam | Escolha outra implementação do kata |
| Repositório sujo | Não prossiga sem decidir o destino de cada alteração |

> » IA: Accordion; marcado como OPCIONAL; cada item deve manter instrução e validação.

### 🚀 Quer ir além?

1. Crie `.cursorignore` e valide que o arquivo não é sugerido como contexto.
2. Use `Allowlist` vazia e confirme que cada comando pede decisão.
3. Faça um commit-base e confirme `git status` limpo.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 1" — encerre esta lição aqui. ▲▲▲*

---

# Oficina 2 — Converse com o Código

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> » IA: Text.

### 🎯 O Problema

Você recebeu um projeto desconhecido e precisa localizar a regra de negócio e os testes sem permitir alteração prematura.

> » IA: List.

### 🧰 O que você vai usar

- Ask;
- menções com `@`;
- Explorer;
- requisitos e testes.

> » IA: Process; preservar o prompt verbatim.

### 👐 Mão na massa

1. Abra `Cursor > Agent` com `Ctrl+I` ou `Cmd+I`.
2. Selecione `Cursor > Agent > Mode > Ask`.
3. Envie:

> Explique este projeto. Aponte os pontos de entrada, a regra de atualização de qualidade e os testes. Cite os arquivos. Não altere nada.

4. Abra dois arquivos citados e confira as afirmações.
5. Anexe os requisitos com `@` e pergunte o que ainda não foi implementado.
6. Peça três melhorias pequenas, com trade-offs, e mande aguardar.
7. Se a conversa ficar longa, abra outra com resumo e arquivos mínimos.

> » IA: Statement; preservar emoji.

### ✅ Deu certo?

🏁 Ponto de controle: você localiza regra e testes, e não existe diff criado pelo Agent.

> » IA: Accordion; um item por linha.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Arquivo não aparece | Confira ignores, use `@` ou reindexe |
| Resposta inventa detalhes | Exija arquivo e trecho de suporte |
| Contexto saturado | Inicie conversa nova com resumo mínimo |

> » IA: Accordion; marcado como OPCIONAL.

### 🚀 Quer ir além?

1. Peça um diagrama textual e valide três relações.
2. Separe fatos, inferências e perguntas abertas.
3. Compare a resposta com o README e registre divergências.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 2" — encerre esta lição aqui. ▲▲▲*

---

# Oficina 3 — Planeje Antes de Editar

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> » IA: Text.

### 🎯 O Problema

Você precisa implementar “Conjurado”, mas quer impedir que o Agent mude o problema ou enfraqueça testes.

> » IA: List.

### 🧰 O que você vai usar

- requisitos em português;
- Plan Mode;
- Agent;
- terminal e testes.

> » IA: Process; preservar prompt e breadcrumb.

### 👐 Mão na massa

1. Leia a regra “Conjurado”.
2. Abra `Cursor > Agent > Mode > Plan` ou use `Shift+Tab` no campo.
3. Envie:

> Planeje a implementação de “Conjurado”. Não edite ainda. Preserve testes existentes. Comece por um caso que falha, limite a mudança à regra necessária e indique o comando de validação.

4. Reduza o plano a no máximo quatro etapas.
5. Confira arquivos, comando, diretório, efeitos e reversão.
6. Autorize Build somente após a revisão.
7. Interrompa se testes forem editados, surgirem arquivos alheios ou o comando não for compreendido.

> » IA: Statement; preservar emoji.

### ✅ Deu certo?

🏁 Ponto de controle: o diff trata de “Conjurado”, mantém testes existentes e inclui evidência de execução.

> » IA: Accordion; um item por linha.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Plano amplo | Exija arquivo e verificação por etapa |
| Agent altera teste | Interrompa, restaure e reafirme a restrição |
| Comando parece destrutivo | Não autorize; peça efeito, alvo e reversão |

> » IA: Accordion; marcado como OPCIONAL.

### 🚀 Quer ir além?

1. Comprove que o novo teste falha antes da implementação.
2. Compare duas soluções por complexidade e risco.
3. Defina limite de arquivos e valide o diff contra ele.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 3" — encerre esta lição aqui. ▲▲▲*

---

# Oficina 4 — Revise sem Fé Cega

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> » IA: Text.

### 🎯 O Problema

O Agent declarou sucesso. Você precisa provar se a mudança atende ao requisito sem efeitos colaterais.

> » IA: List.

### 🧰 O que você vai usar

- diff view;
- testes;
- lint, type checker ou build;
- inspeção manual;
- checkpoint e Git.

> » IA: Process; preservar a sequência.

### 👐 Mão na massa

1. Leia o diff inteiro.
2. Explique cada condição adicionada.
3. Procure arquivos fora do escopo, testes removidos e dependências novas.
4. Rode a suíte.
5. Rode uma segunda verificação disponível.
6. Inspecione um caso normal e um caso de borda.
7. Registre efeito, evidência, decisão e risco residual.
8. Use `Cursor > Agent > Restore Checkpoint` ou Git quando necessário.

> » IA: Statement; preservar emoji.

### ✅ Deu certo?

🏁 Ponto de controle: sua decisão cita evidência de teste e de inspeção, não apenas a mensagem do Agent.

> » IA: Accordion; um item por linha.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Testes passam e regra parece errada | Acrescente caso de borda |
| Diff é grande | Rejeite e peça divisão |
| Execução expira | Use `Cursor > Command Palette > Developer: Export Logs...` |

> » IA: Accordion; marcado como OPCIONAL.

### 🚀 Quer ir além?

1. Compare sua revisão com uma autorrevisão do Agent.
2. Faça uma mutação deliberada e confirme que o teste detecta.
3. Escreva comentário de revisão com risco e recomendação.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 4" — encerre esta lição aqui. ▲▲▲*

---

# Projeto Final — Mudança Pequena, Evidência Grande

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Projeto Final" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> » IA: Text.

### 🎯 A missão

Escolha uma melhoria pequena no kata e entregue uma decisão completa: o que mudou, por que, como foi validado e qual risco ainda existe.

> » IA: Process.

### 👐 Mão na massa

1. Confira dados, permissões e Git.
2. Explore sem editar.
3. Defina objetivo, contexto, restrições e validação.
4. Revise o plano.
5. Autorize a implementação.
6. Leia o diff.
7. Execute testes e inspeção.
8. Registre a decisão.

> » IA: Checklist; preservar verbatim.

### 🏁 Como saber que terminou

- [ ] O projeto não contém dados sensíveis.
- [ ] O estado inicial é recuperável.
- [ ] O pedido tem escopo e critério de êxito.
- [ ] O plano foi aprovado antes da edição.
- [ ] O diff foi lido integralmente.
- [ ] Testes e inspeção passaram.
- [ ] A decisão e o risco residual foram registrados.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Projeto Final" — encerre esta lição aqui. ▲▲▲*

---

> » IA: List; sem marcador de lição.

# A Parte dos Dez — Hábitos que Salvam seu Repositório

1. Comece por uma tarefa pequena.
2. Peça compreensão antes de edição.
3. Defina o que não deve mudar.
4. Use contexto seletivo.
5. Leia comandos antes de autorizar.
6. Não coloque segredos no projeto.
7. Use Git além de checkpoints.
8. Revise cada arquivo do diff.
9. Teste casos de borda.
10. Recomece quando o contexto perder foco.

> » IA: Text; sem marcador de lição.

## Conseguiu! E agora?

Você concluiu o ciclo preparar → compreender → planejar → executar → verificar. Repita-o em tarefas pequenas até que evidência e revisão venham antes da aceitação.

Depois, explore Rules, `AGENTS.md`, TDD, Agent Review, Cloud Agents, Bugbot e CLI separadamente, mantendo o mesmo padrão de controle.

