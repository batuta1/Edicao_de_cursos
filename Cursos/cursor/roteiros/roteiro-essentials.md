# Roteiro Final — Cursor (Essentials)

**Público-alvo:** pessoas com fundamentos de programação e Git, iniciantes no Cursor.  
**Objetivo geral:** compreender e aplicar um ciclo supervisionado de desenvolvimento assistido por IA.  
**Pré-requisitos:** Cursor instalado, conta ativa, internet, Git e repositório de prática sem dados sigilosos.

## Estrutura do Curso

- **Nível 1 — Fundamentos e proteção:** Módulos 0 a 2.
- **Nível 2 — Execução supervisionada:** Módulos 3 e 4.
- **Síntese:** Módulo 5.
- **Aprofundamentos fora do percurso:** Rules, `AGENTS.md`, Cloud Agents, Bugbot, CLI, MCP e automações.

> **Nota de atualização:** o material-fonte foi coletado em 03/11/2026. A interface muda com frequência. Planos, modelos, atalhos e nomes de menus devem ser conferidos na semana da publicação.

---

## Módulo 0 — Preparação, Privacidade e Controle (26 min)

### Descrição

- **Objetivos da Aula:** apresentar requisitos, fluxos de dados, modos de execução e mecanismos de recuperação.
- **Habilidades Esperadas:** preparar sozinho um repositório de prática sem segredos, conferir privacidade e permissões e demonstrar um estado Git recuperável.

### 0.1 Instalação e primeiro acesso

- **📸 Sugestão de Prints:** página oficial de download com as opções macOS, Windows e Linux; em seguida, a tela inicial do Cursor com o comando `File > Open Folder` destacado.

O Cursor requer Windows 10 ou superior, macOS 12 ou superior ou Linux compatível. Em Windows, executa-se o instalador; em macOS, move-se o aplicativo para `Applications`; em Linux, os pacotes `apt` ou `dnf` são preferíveis ao AppImage. Após a abertura, realiza-se o login com uma conta Cursor.

Quem já utiliza VS Code pode importar extensões, temas, configurações e atalhos em `Cursor Settings > General > Account > VS Code Import > Import`. Nem toda extensão do Marketplace da Microsoft está no Open VSX; convém instalar apenas extensões de editores confiáveis.

**Ponto de controle:** o Cursor abre o repositório de prática e exibe seus arquivos no Explorer.

### 0.2 Dados, privacidade e arquivos ignorados

- **📸 Sugestão de Prints:** `Cursor Settings > General > Privacy Mode`, com o controle destacado; Explorer mostrando `.gitignore`, `.cursorignore` e um exemplo de `.env` fora do material didático.

Recursos de IA enviam prompts e trechos de código a provedores de modelos. Com Privacy Mode, o código não é usado para treinamento, porém isso não significa processamento exclusivamente local. O estado padrão em contas individuais não foi confirmado na fonte; por isso, o controle deve ser conferido manualmente.

O `.cursorignore` usa sintaxe semelhante à do `.gitignore`, mas não constitui barreira absoluta: comandos de terminal e ferramentas MCP operam fora dos controles de acesso a arquivos do Cursor. A proteção correta combina remoção de segredos, projeto didático, Privacy Mode, política organizacional e revisão humana.

> **Segurança:** não abrir no exercício projetos com dados pessoais, chaves, tokens, `.env` real ou código cuja política proíba envio a provedores externos.

### 0.3 Permissões e recuperação

- **📸 Sugestão de Prints:** `Cursor Settings > Agents > Approvals & Execution`, mostrando `Auto-review`, `Allowlist` e `Run Everything`; terminal com `git status` limpo.

O Agent pode modificar arquivos do workspace e executar comandos. A documentação consultada diverge entre “comandos precisam de aprovação por padrão” e “Auto-review é o padrão”. A ação segura é observar a configuração efetiva da instalação. `Auto-review` não é uma fronteira de segurança; `Allowlist` com lista vazia permite conferir cada comando. `Run Everything` não é recomendado para o percurso.

Checkpoints guardam estados locais durante a sessão. Git registra histórico durável e compartilhável. Antes do primeiro pedido, deve existir um commit conhecido ou uma cópia limpa do projeto.

### Solução de Problemas

| Situação | Ação |
|---|---|
| O caminho do menu mudou | Pesquisar `Privacy` ou `Approvals` em Settings e registrar o caminho atual |
| O repositório já contém alterações | Revisar; então commitar, guardar ou trabalhar em uma cópia limpa |
| Há segredo no histórico | Interromper o exercício e seguir o procedimento de rotação/remoção da organização |

### Pílula Hands-on — Checklist de prontidão

1. Abrir uma implementação do Gilded Rose cujo comando de teste já tenha sido identificado.
2. Confirmar ausência de segredos e dados pessoais.
3. Conferir Privacy Mode e modo de execução.
4. Rodar `git status` e identificar o ponto de retorno.

**Critério de êxito:** os quatro itens estão verificados e o participante consegue explicar como desfaria uma alteração.

---

## Módulo 1 — Cursor, Contexto e Modos de Trabalho (21 min)

### Descrição

- **Objetivos da Aula:** explicar modelos probabilísticos, contexto e diferenças entre mecanismos de assistência.
- **Habilidades Esperadas:** escolher o modo adequado para uma tarefa e justificar a escolha com base em risco e necessidade de edição.

### 1.1 O que o Cursor acrescenta ao editor

- **📸 Sugestão de Prints:** editor clássico com Explorer, área de código, terminal e painel do Agent identificados; uma segunda imagem da Agents Window, marcada como alternativa.

O Cursor integra recursos de IA ao ambiente de desenvolvimento. Tab sugere código durante a digitação. Ask favorece perguntas sem alteração. Agent pesquisa, edita e executa comandos. Plan organiza tarefas maiores antes de construir. Debug trabalha a partir de sintomas e evidências.

O antigo fluxo de edição inline por `Cmd/Ctrl+K` foi aposentado em 26/10/2026. No fluxo documentado, a seleção é enviada ao painel do Agent. O curso não ensina a funcionalidade antiga.

### 1.2 Contexto e limites do modelo

- **📸 Sugestão de Prints:** painel do Agent com o anel de contexto aberto e os agrupamentos System Prompt, Tools, Rules e Conversation; menu de `@` com arquivo e pasta.

Contexto é a memória de trabalho fornecida ao modelo: pedido, arquivos, regras, ferramentas e conversa. A janela é finita; ao se aproximar do limite, partes antigas podem ser resumidas. Acrescentar todo o projeto indiscriminadamente aumenta ruído. Deve-se fornecer apenas o necessário e pedir pesquisa dirigida.

Modelos são probabilísticos. Podem inventar uma API ou apresentar explicação convincente e incorreta. Por isso, a validação deve ser definida antes da geração.

### 1.3 Heurística de escolha

- **📸 Sugestão de Prints:** seletor de modo do Agent aberto, com Ask, Plan, Debug e Agent visíveis.

| Intenção | Modo inicial | Controle principal |
|---|---|---|
| Compreender o projeto | Ask | Proibir edição e exigir arquivos de referência |
| Planejar mudança ampla | Plan | Revisar etapas e arquivos antes de Build |
| Investigar falha reproduzível | Debug | Fornecer logs e hipótese testável |
| Executar tarefa delimitada | Agent | Acompanhar ferramentas, diff e testes |

### Solução de Problemas

| Situação | Ação |
|---|---|
| O Agent não encontra um arquivo | Conferir ignores, anexar com `@` ou reindexar |
| A conversa perdeu foco | Abrir nova conversa com resumo e contexto mínimo |
| Um modelo não está disponível | Usar um modelo permitido pelo plano; conferir disponibilidade regional |

### Pílula Hands-on — Escolha justificada

Classificar quatro cenários e escrever uma frase de justificativa para cada modo escolhido.

**Critério de êxito:** a escolha considera necessidade de edição, tamanho da tarefa e evidência disponível.

---

## Módulo 2 — Pedidos Verificáveis (22 min)

### Descrição

- **Objetivos da Aula:** apresentar uma estrutura reutilizável de delegação e critérios observáveis.
- **Habilidades Esperadas:** produzir sozinho um pedido delimitado, com contexto suficiente e validação independente.

### 2.1 Da intenção vaga à tarefa auditável

- **📸 Sugestão de Prints:** duas mensagens lado a lado no Agent: “corrija o projeto” e uma versão estruturada, com trechos objetivo, contexto, restrições e validação realçados.

“Melhore o código” é uma intenção, não uma especificação. Um pedido verificável contém: resultado esperado; contexto relevante; limites; ações proibidas; evidência de conclusão. A estrutura reduz escopo implícito sem exigir um texto longo.

**Modelo editável:**

> Objetivo: [resultado observável].  
> Contexto: [arquivos, erro, requisito].  
> Restrições: [o que não mudar; limites].  
> Processo: [explique/planeje antes de editar].  
> Validação: [comando e resultado esperado].

### 2.2 Contexto seletivo

- **📸 Sugestão de Prints:** menu `@` com um arquivo anexado e resposta citando caminhos; anel de contexto sem saturação.

Menções ajudam a anexar arquivos, pastas, terminais ou conversas. Elas não substituem a explicação do papel de cada item. Um prompt eficaz pode pedir que o Agent localize os pontos de entrada e cite os arquivos antes de propor mudança.

### Solução de Problemas

| Situação | Ação |
|---|---|
| Resposta excessivamente ampla | Reduzir o objetivo a uma mudança e listar arquivos permitidos |
| Agent pressupõe requisito inexistente | Pedir que separe fatos do repositório, inferências e perguntas |
| Validação não existe | Definir inspeção manual observável antes de implementar |

### Pílula Hands-on — Reescrita

Transformar “corrija o projeto” em pedido para localizar e implementar a regra “Conjurado”, preservando testes existentes e executando a suíte ao final.

**Critério de êxito:** uma terceira pessoa consegue decidir, pelo pedido, se a tarefa terminou.

---

## Módulo 3 — Do Plano à Mudança (24 min)

### Descrição

- **Objetivos da Aula:** ensinar o workflow compreender–planejar–executar–testar e o papel do TDD.
- **Habilidades Esperadas:** conduzir o Agent por etapas, interromper desvio de escopo e verificar comandos antes de autorizar.

### 3.1 Compreender e planejar

- **📸 Sugestão de Prints:** Plan Mode selecionado; plano curto com arquivos e testes; botão Build destacado, sem ser acionado.

Mudanças maiores começam com exploração. Recomenda-se pedir pontos de entrada, módulos envolvidos, testes relacionados e dúvidas. Em Plan Mode, o Agent propõe etapas; a pessoa revisa escopo, ordem, arquivos e verificações antes de iniciar Build.

### 3.2 Executar com supervisão

- **📸 Sugestão de Prints:** painel mostrando uma edição e um comando de teste pendente de aprovação; diretório de execução e comando visíveis.

Antes de autorizar um comando, devem ser lidos: executável, argumentos, diretório, arquivos potencialmente afetados e possibilidade de reversão. A execução precisa parar quando surgem arquivos fora do escopo, remoção de testes ou mudança de requisito.

No TDD, confirma-se uma falha, preservam-se os testes e implementa-se o mínimo para fazê-los passar. Esse fluxo impede que a meta seja redefinida para acomodar o código produzido.

### Solução de Problemas

| Situação | Ação |
|---|---|
| Plano genérico | Solicitar no máximo quatro etapas, cada uma com arquivo e verificação |
| Agent altera teste existente | Interromper, restaurar e reforçar a restrição |
| Comando é incompreensível | Não autorizar; pedir explicação de efeito e reversão |

### Pílula Hands-on — Plano mínimo

Solicitar e revisar um plano para “Conjurado” com: teste que falha, implementação mínima, suíte completa e inspeção de diff.

**Critério de êxito:** o plano não edita requisitos nem enfraquece testes e inclui uma verificação por etapa.

---

## Módulo 4 — Revisão, Testes e Recuperação (20 min)

### Descrição

- **Objetivos da Aula:** apresentar leitura de diff, validação em camadas e recuperação.
- **Habilidades Esperadas:** decidir sozinho sobre uma alteração com base em arquivos, comportamento, testes e risco residual.

### 4.1 Ler o diff como código de terceiros

- **📸 Sugestão de Prints:** diff com linhas verdes e vermelhas, navegação entre arquivos e controles de aceitar/rejeitar; uma mudança alheia destacada como exemplo.

O diff deve ser lido arquivo por arquivo. Pergunta-se: resolve o requisito? toca apenas o necessário? preserva testes? introduz dependência, segredo ou permissão? A resposta do Agent não é evidência suficiente.

### 4.2 Validar em camadas

- **📸 Sugestão de Prints:** terminal com testes aprovados; painel Problems sem novos erros; aplicação ou saída manual mostrando o comportamento esperado.

Testes automatizados cobrem propriedades declaradas. Lint, type checker ou build cobrem outras classes de falha. Inspeção manual confirma o comportamento relevante. Agent Review pode apoiar, mas não substitui a leitura humana.

### 4.3 Registrar e recuperar

- **📸 Sugestão de Prints:** opção Restore Checkpoint e histórico Git, apresentados lado a lado.

| Arquivo/área | Efeito observado | Evidência | Decisão |
|---|---|---|---|
| [preencher] | [preencher] | [comando/resultado] | Aceitar/Rejeitar |

Checkpoints ajudam durante a sessão; Git oferece recuperação durável. A escolha depende de onde o trabalho está no fluxo.

### Solução de Problemas

| Situação | Ação |
|---|---|
| Diff grande demais | Rejeitar e pedir divisão em mudanças menores |
| Testes passam, requisito falha | Criar caso de borda a partir do requisito |
| Agent Execution Timed Out | Exportar logs pela Command Palette e reiniciar a sessão |

### Pílula Hands-on — Decisão com evidência

Preencher a tabela de revisão para uma mudança do exercício.

**Critério de êxito:** a decisão cita efeito, evidência e risco residual.

---

## Módulo 5 — Síntese e Aplicação Integrada (10 min)

### Descrição

- **Objetivos da Aula:** integrar preparação, contexto, planejamento, execução e revisão.
- **Habilidades Esperadas:** completar autonomamente uma pequena mudança e documentar a decisão.

### Atividade Integradora — Mudança supervisionada

- **📸 Sugestão de Prints:** sequência de cinco quadros: `git status` inicial; prompt estruturado; plano aprovado; diff; testes aprovados.

1. Confirmar projeto sem dados sigilosos e estado Git conhecido.
2. Pedir ao Agent que localize a regra sem editar.
3. Escrever objetivo, contexto, restrições e validação.
4. Revisar o plano.
5. Autorizar uma mudança pequena.
6. Ler o diff, rodar testes e registrar a decisão.

| Critério de avaliação | Atendido? |
|---|---|
| Dados e permissões foram conferidos | [ ] |
| O pedido é verificável | [ ] |
| O plano foi revisto antes da edição | [ ] |
| O diff foi lido integralmente | [ ] |
| Testes e inspeção relevante foram executados | [ ] |
| A decisão inclui evidência e risco residual | [ ] |

**Critério de êxito:** seis itens atendidos. Se um item falhar, a mudança não está pronta para aceitação.

## Decisões Conscientes

- Planos e preços não foram incorporados à avaliação porque são voláteis; devem constar em material atualizado de apoio.
- Cloud Agents, Bugbot, CLI e MCP foram mantidos fora do percurso principal por ampliarem superfície de acesso, custo e configuração.
- A interface em português não foi pressuposta; termos oficiais permanecem em inglês.

