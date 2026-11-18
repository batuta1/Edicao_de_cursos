# Registro de atividade ou projeto

> Escrito em 2026-11-18, seguindo a skill `registro-de-atividade-ou-projeto`. Cobre o que aconteceu na branch `structuring` até o commit `355b100`. Os números abaixo foram conferidos no histórico do git, nos testes e nas execuções feitas nesta sessão.

## Identificação

- **Nome da atividade:** Automação da planilha de produção para o Notion, extrator de SCORM e janelas de uso (branch `structuring`).
- **Responsável:** Cadu-Tower (autor dos commits da branch).
- **Status:** Em andamento.
- **Data de início:** 2026-11-18 (primeiro commit da branch: "Limpa arquivos da branch structuring").
- **Previsão de conclusão:** Não informado.
- **Data de conclusão efetiva:** Não se aplica ainda.
- **Tarefas relacionadas:** Fases F1 a F8 em `_plan/fases/`; dúvidas em `_plan/_duvidas/01-automacao-notion.md` e `02-interface-automacao.md`.

## Planejamento inicial

Fonte: `_plan/detalhes/readme.md`.

- **Ponto de partida:**
  - A planilha de produção dos cursos (`checklist-producao-de-cursos-60-dias-*.xlsx`) existe só na branch `joao`.
  - O Notion tem uma tabela de cursos (nome, status, responsável, progresso) que era atualizada à mão.
  - O extrator de dados dos pacotes SCORM estava em outro repositório.
  - Os arquivos `autor.json` dos cursos estavam sem autor.
- **Entrega pretendida:**
  - Pegar o `xlsx` mais recente da `joao`, guardar só o último e fazer um commit simples.
  - Converter o `xlsx` em `csv`.
  - Preencher o `autor.json` e atualizar o Notion a partir do `csv`.
  - Trazer o extrator para este repositório, gerando a lista de cursos em `Cursos/`.
- **Limites da atividade:**
  - Incluído: scripts de automação e extrator.
  - Fora: as pastas `bagunca/` e `Skills/` da `main`, que não podem ser alteradas.
  - O trabalho acontece na `structuring`; o que ficar estável vai para a `main`.
- **Critério de conclusão:** Não informado no início. As fases F1 a F8 definiram "pronto quando" para cada parte (reconstrução posterior, feita durante o trabalho).
- **Caminho previsto:** O readme previa atualizar o Notion com `pyautogui` (cliques na tela). A ordem das etapas (planilha, `csv`, extrator, autores, Notion) foi organizada nas fases F1 a F5.

## Acompanhamento

Todo o trabalho ocorreu em 2026-11-18. As entradas seguem a ordem dos acontecimentos.

### 2026-11-18 · 1. Análise e decisões

- **Avanços e entregas:**
  - Análise do readme: o plano é viável.
  - Arquivo de dúvidas com 8 decisões, todas respondidas pelo usuário (`01-automacao-notion.md`).
  - Cinco fases de implementação com listas de conferência (`F1` a `F5`).
- **Dificuldades e ajustes:**
  - O usuário escolheu a API do Notion em vez de `pyautogui`, que dependeria de cliques na tela.
  - Os cursos antigos não estão na aba usada ("Checklist 60 dias"), então só parte deles tem linha na planilha.
- **Próximo passo:** Implementar as fases.

### 2026-11-18 · 2. Primeira implementação

- **Avanços e entregas:**
  - Extrator copiado para a raiz como `extrator_scorm`, com a pasta `path/` concentrando os caminhos.
  - Projeto com `uv` (`pyproject.toml`, `uv.lock`).
  - Módulo `automacao`: baixa o `xlsx` da `joao`, converte para `csv`, casa curso e pasta, preenche `autor.json`, atualiza o Notion e commita só os arquivos do processo.
  - 8 testes automatizados passando.
  - Ensaio numa cópia da `main`: 163 pacotes lidos, 10 de 39 pastas casadas com a planilha, 10 `autor.json` gravados, 2 commits só com arquivos permitidos.
- **Dificuldades e ajustes:**
  - A pasta `Cursos/` só existe na `main`. Para testar, foi usada uma cópia temporária da `main`, com a variável `EDICAO_RAIZ`.
  - Só 10 de 39 pastas casaram. As outras 29 são cursos antigos (fora da aba usada). Alguns cursos novos também não casaram, como `Vibe Coding - Essentials (Lovable)`.
- **Próximo passo:** Escrever a documentação e conectar ao Notion real.

### 2026-11-18 · 3. Documentação e execução por etapas

- **Avanços e entregas:**
  - Opção `--so` para rodar uma etapa de cada vez (`checklist`, `extrator`, `autores`, `notion`).
  - Documentação reorganizada em dois guias: um só da automação do Notion e outro só do extrator de SCORM, cada um começando pelos comandos principais.
- **Dificuldades e ajustes:**
  - O usuário pediu a separação dos guias; os guias numerados anteriores foram substituídos.
  - O usuário moveu a documentação duas vezes de lugar (commits "mov documentacao..." e "+"), até ela voltar para a raiz.
- **Próximo passo:** Ligar o Notion.

### 2026-11-18 · 4. Ligação com o Notion

- **Avanços e entregas:**
  - Token criado pelo usuário e guardado em `.env`, que o git ignora.
  - Cliente do Notion atualizado para a API de 2025 (fonte de dados).
  - Ensaio no Notion real: 53 cursos sem mudança, 43 a atualizar, 7 linhas não encontradas. Nada foi escrito no Notion.
- **Dificuldades e ajustes:**
  - Erro 404: a página não estava compartilhada com a integração.
  - Erro de "fonte de dados": a página mostrava uma visão de outro banco, que também precisou ser compartilhado.
  - A coluna "Meta até 12 dez" (`publicado`) é a meta de 97 das 104 linhas, não o estado. Ela foi retirada do cálculo de Status e Progresso. Antes disso, quase todos os cursos apareciam como Concluído.
  - Dos 7 itens não encontrados, 6 são linhas de resumo da planilha e 1 é um curso cujo nome tem vírgula, que o `csv` troca por `;`.
- **Próximo passo:** Definir a interface de uso.

### 2026-11-18 · 5. Reorganização e janela da automação

- **Avanços e entregas:**
  - Revisão da skill `interface-tkinter` contra a tela do extrator: 5 problemas apontados, 4 corrigidos na skill.
  - Duas decisões do usuário: base compartilhada em `scripts/comum/` e um atalho de duplo clique (`abrir-interface.bat`) em cada parte.
  - Código movido para `scripts/` (`automacao`, `extrator_scorm`, `comum`, `documentacao`) com `git mv`. As duas partes importam só de `comum`. Os comandos não mudaram.
  - Janela da automação com duas abas (Executar e Notion): Ensaio, depois Aplicar com confirmação, botão Parar, etapas indisponíveis com o motivo escrito.
  - As fontes Ubuntu e SUSE Mono passaram a carregar também no Windows. As áreas de texto do extrator ficaram somente leitura.
  - Documentação curta em cada pasta, receita de deploy no `README.md` da raiz e 140 docstrings adicionadas.
  - 15 testes passando. Os dois atalhos abriram a janela. Ensaio completo numa cópia da `main`: 2 commits só com arquivos permitidos, nada em `bagunca/` ou `Skills/`.
  - Commit `355b100`.
- **Dificuldades e ajustes:**
  - A `structuring` não tem `Cursos/`, `Skills/` nem `bagunca/`. Um `git merge` na `main` poderia apagá-los. Por isso o deploy foi definido como cópia só dos caminhos do código (fase F8).
  - O `.exe` de verdade (PyInstaller) ficou em espera por decisão do usuário.
- **Próximo passo:** Executar a fase F8 (deploy na `main`).

### 2026-11-18 · 6. Skill de registro

- **Avanços e entregas:** Skill `registro-de-atividade-ou-projeto` adicionada em `.claude/skill/` e este registro criado com ela.
- **Dificuldades e ajustes:** A pasta `.claude/skill/` está no `.gitignore` por decisão do usuário; a skill não foi versionada.
- **Próximo passo:** Decidir se a skill entra no repositório (só ela, com `git add -f`).

## Pendências em aberto (confirmadas em 2026-11-18)

- **Aplicar de verdade no Notion:** não foi testado. O usuário pediu para esperar.
- **Deploy na `main` (F8):** a receita existe, mas não foi executada.
- **Casamento curso × pasta:** 10 de 39 pastas casaram, e alguns cursos novos não casam por diferença de nome. Se a taxa continuar baixa, reabrir a decisão D5 (mapa manual).
- **Nome com vírgula:** o curso "IA no Direito: ética, sigilo e responsabilidade - Essentials" não casa com o Notion. Falta tratar a diferença entre `,` e `;`.
- **Linhas de resumo da planilha:** 6 itens do cabeçalho são lidos como cursos e aparecem como "não achou no Notion". Falta ignorá-los.
- **`.exe` com PyInstaller:** em espera (decisão D2.1).

## Encerramento

Não preenchido: a atividade está em andamento. Preencher depois do deploy na `main` e do primeiro Aplicar real no Notion.

- **Resultado entregue:**
- **Comparação com o planejamento:**
- **Tempo dedicado:**
- **Aprendizados:**
- **Continuidade:**
