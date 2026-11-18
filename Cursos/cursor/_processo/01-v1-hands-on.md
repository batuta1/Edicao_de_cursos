# Cursor Para Leigos — Curso Hands-on

*Ao final, você terá concluído e revisado uma pequena mudança real com o Agent.*

## Antes de Arregaçar as Mangas

Este curso é mão na massa: você vai preparar um repositório seguro, conversar com o código, delegar uma mudança e decidir se ela merece ser aceita.

O que você precisa ter aberto agora:

- Cursor instalado e autenticado;
- Git disponível;
- kata Gilded Rose aberto como pasta;
- terminal e suíte de testes funcionando.

> 🔑 **Regra de ouro:** o Agent propõe; você continua responsável por entender, testar e aprovar.

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---:|
| 1 | Preparar um projeto reversível e sem segredos | 23 min |
| 2 | Fazer o Agent explicar o projeto sem mudar nada | 35 min |
| 3 | Planejar e implementar uma mudança pequena | 24 min |
| 4 | Revisar o diff e diagnosticar falhas | 20 min |
| Projeto Final | Entregar uma mudança validada | 16 min |

As oficinas formam um único ciclo, e cada uma entrega uma vitória visível.

---

# Oficina 1 — Prepare o Terreno

### 🎯 O Problema

Você quer experimentar o Agent, mas não quer expor credenciais nem perder o estado inicial do projeto.

### 🧰 O que você vai usar

- Cursor Settings;
- Git;
- `.cursorignore`;
- kata Gilded Rose.

### 👐 Mão na massa

1. Abra o kata em `File > Open Folder`.
2. Procure por `.env`, chaves e dados reais; remova-os do exercício.
3. Confira o Privacy Mode em `Cursor Settings > General > Privacy Mode`.
4. Confira o modo de execução em `Cursor Settings > Agents > Approvals & Execution`.
5. Mantenha `Auto-review` ou use `Allowlist`; não escolha `Run Everything`.
6. Rode `git status` e crie um commit inicial, se necessário.

### ✅ Deu certo?

O projeto abre, não contém segredos e o Git mostra um ponto inicial conhecido.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O menu mudou | Procure por `Privacy` ou `Approvals` em Settings e registre o caminho atual |
| O projeto não tem Git | Execute `git init`, adicione os arquivos e faça um commit inicial |
| Há arquivo sensível | Retire-o do projeto; não confie apenas no `.cursorignore` |

### 🚀 Quer ir além?

Crie um `.cursorignore` e confirme que ele complementa, mas não substitui, a remoção de dados sensíveis.

---

# Oficina 2 — Converse com o Código

### 🎯 O Problema

Você recebeu um projeto desconhecido e precisa localizar os pontos de entrada sem permitir alterações prematuras.

### 🧰 O que você vai usar

- Ask;
- Agent;
- menções com `@`;
- contexto do projeto.

### 👐 Mão na massa

1. Abra o painel do Agent com `Ctrl+I` ou `Cmd+I`.
2. Selecione Ask.
3. Envie: “Explique este projeto. Aponte os pontos de entrada, a regra de atualização de qualidade e os testes. Não altere arquivos.”
4. Peça que cada afirmação cite o arquivo correspondente.
5. Abra os arquivos citados e confira duas afirmações.
6. Pergunte quais três mudanças pequenas seriam seguras e peça que aguarde sua escolha.

### ✅ Deu certo?

Você consegue apontar onde está a regra de negócio e onde estão os testes, sem diff pendente.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O Agent não encontra arquivo | Confira `.cursorignore`/`.gitignore`, anexe o arquivo com `@` ou reindexe |
| A resposta é genérica | Cite a pasta relevante e peça referências de arquivo e linha |
| O contexto ficou cheio | Abra uma nova conversa com um resumo curto e apenas os arquivos necessários |

### 🚀 Quer ir além?

Peça um diagrama textual dos módulos e valide cada relação no código.

---

# Oficina 3 — Planeje Antes de Editar

### 🎯 O Problema

Você precisa adicionar suporte ao item “Conjurado”, mas quer impedir que o Agent altere testes para mascarar o resultado.

### 🧰 O que você vai usar

- requisitos em português;
- Plan Mode;
- Agent;
- testes do projeto.

### 👐 Mão na massa

1. Leia `gilded-rose-requisitos-pt-br.md`.
2. Abra o Agent e ative Plan Mode com `Shift+Tab` no campo de entrada.
3. Peça um plano para implementar “Conjurado”, sem editar arquivos.
4. Exija que o plano preserve os testes existentes e proponha casos novos antes do código.
5. Revise arquivos, riscos e comando de teste indicados.
6. Clique em Build somente quando o plano estiver coerente.
7. Acompanhe cada arquivo e comando usado.

### ✅ Deu certo?

O diff trata apenas da regra “Conjurado”, e o comando de teste foi executado.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O plano é amplo demais | Peça uma versão com no máximo quatro etapas e arquivos explícitos |
| O Agent quer mudar testes existentes | Interrompa e reforce que testes existentes são restrição |
| Um comando pede permissão | Leia o comando e seu diretório antes de autorizar |

### 🚀 Quer ir além?

Faça o Agent começar por um teste que falha e só depois implementar a regra.

---

# Oficina 4 — Revise sem Fé Cega

### 🎯 O Problema

O Agent declara que terminou. Agora você precisa descobrir se isso é verdade.

### 🧰 O que você vai usar

- diff view;
- testes;
- lint ou build, se disponíveis;
- checkpoint e Git.

### 👐 Mão na massa

1. Leia o diff arquivo por arquivo.
2. Explique com suas palavras cada condição adicionada.
3. Procure mudanças fora do pedido e testes removidos ou enfraquecidos.
4. Rode testes e uma verificação adicional disponível.
5. Se houver falha, envie a saída ao Debug Mode e peça diagnóstico antes da correção.
6. Aceite apenas o que você consegue justificar; restaure checkpoint ou reverta pelo Git se necessário.

### ✅ Deu certo?

Você registrou a decisão, a evidência e o risco residual da mudança.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Testes passam, mas a regra parece errada | Acrescente casos de borda derivados dos requisitos |
| O diff é grande | Rejeite e peça uma mudança menor e focada |
| Agent Execution Timed Out | Exporte logs pela Command Palette e reinicie a sessão |

### 🚀 Quer ir além?

Peça uma autorrevisão ao Agent e compare as observações com sua própria leitura.

---

# Projeto Final — Mudança Pequena, Evidência Grande

### 🎯 A missão

Escolha uma melhoria pequena no kata, conduza o ciclo completo e entregue uma decisão auditável.

### 👐 Mão na massa

1. Confirme privacidade, permissões e estado Git.
2. Peça uma explicação sem edição.
3. Defina objetivo, escopo, restrições e critério de êxito.
4. Revise um plano curto.
5. Autorize a implementação.
6. Leia o diff, rode testes e registre a decisão.

### 🏁 Como saber que terminou

- [ ] Nenhum dado sensível entrou no contexto.
- [ ] O pedido tem critério verificável.
- [ ] O plano foi aprovado antes da edição.
- [ ] O diff não contém mudanças alheias.
- [ ] Os testes passaram.
- [ ] A decisão final está registrada.

# A Parte dos Dez — Hábitos que Salvam seu Repositório

1. Comece pequeno.
2. Peça explicação antes de edição.
3. Dê critérios de êxito.
4. Anexe apenas o contexto necessário.
5. Leia cada comando antes de autorizar.
6. Nunca coloque segredos no prompt.
7. Use Git, não apenas checkpoints.
8. Revise o diff inteiro.
9. Teste casos de borda.
10. Recomece a conversa quando o contexto perder foco.

# Conseguiu! E agora?

Você já tem um método repetível: preparar, entender, planejar, executar e verificar. Pratique com tarefas pequenas até que a revisão se torne automática.

Depois, explore Rules, `AGENTS.md`, TDD, Agent Review, Cloud Agents, Bugbot e CLI — um recurso por vez, sempre mantendo o mesmo padrão de evidência.

