# Automação checklist → Notion · visão geral

Origem: [`_plan/detalhes/readme.md`](../detalhes/readme.md). Decisões: [`_plan/_duvidas/01-automacao-notion.md`](../_duvidas/01-automacao-notion.md) (D1 a D8 respondidas).

## Decisões aplicadas

| Dúvida | Decisão | Efeito nas fases |
|---|---|---|
| D1 | **API oficial do Notion** | Sem pyautogui. F4 só tem o driver de API |
| D1.2 | Link do banco recebido; colunas e tipos **faltam** | F4 descobre colunas e tipos sozinha (`inspecionar.py`), sem perguntar |
| D2 | `automacao/referencias/` | Pasta de código e dados: `automacao/` |
| D3 | `extrator_scorm` | `python -m extrator_scorm` |
| D4 | Só a aba "Checklist 60 dias" | Um `csv` por `xlsx` |
| D5 | Casamento **automático por slug**, sem mapa manual | Não existe `mapa-cursos.json`; o que não casa vai para relatório |
| D6 | "Responsável" se preenchido; senão `x` de João/Marina; sem dado → `null` | 6.1: nome curto (`João`, `Marina`). 6.2: os dois marcados → `null` |
| D7 | Progresso = etapas com `x` ÷ 5 | Regra de Status na F4 |
| D8 | `git fetch` + `git show origin/joao:<arquivo>`, commit na branch atual | Sem checkout, sem worktree |

## Veredito: viável ✅

| Item do readme | Veredito | Observação |
|---|---|---|
| Pegar o `xlsx` mais recente da `joao` | ✅ | Hoje `v0-4` |
| `xlsx` → `csv` (`,` → `;`) | ✅ | `openpyxl` já instalado; 1.261 células têm vírgula |
| Commit só dos arquivos do processo | ✅ | `git commit -- <caminhos>`; nunca `git add .` |
| Extrator na raiz, caminhos em `path/` | ✅ | Imports relativos; 2 caminhos fixos a corrigir |
| Saída em `Cursos/registro-de-cursos.json` | ✅ | `ultimas_versoes.json` → novo destino |
| Preencher `autor.json` | ⚠️ | Casamento só por slug: nomes diferentes não casam e viram relatório (ver risco) |
| Atualizar Notion | ✅ via API | Precisa de token (ação do usuário) |
| Progresso em % | ✅ | Calculado das 5 colunas de etapas |

## Achados que mudam o trabalho

- 📦 `_plan/` está no `.gitignore`: tudo em `_plan/` fica fora do git. O código novo nasce fora dele.
- `_plan/extrator` veio **sem** `extrair.py`, `pyproject.toml` e `testes/`. O ponto de entrada vira `__main__.py`.
- Caminhos fixos a corrigir: `servico.py:14` (`PASTA_SAIDA`) e `interface/tela.py:21` (`PASTA_PADRAO`). O `README.md` do extrator tem links quebrados (`../documentos`, `../_planejamento`).
- "Responsável" e "Status" estão vazios nas 104 linhas do `xlsx`; o autor sai das colunas João/Marina e o progresso das 5 etapas.
- 39 pastas de curso em `Cursos/` × 104 linhas no `xlsx`: a maioria das linhas não tem pasta (esperado).
- ⚠️ **Risco da D5 = A:** só slug. Nomes como `ChatGPT Chat - Essentials` × `openai-chatgpt-chat-essentials` podem não casar. A F3 mede a taxa de acerto no 1º relatório; se for baixa, reabrir a D5 (o mapa manual volta como D9).
- Regra de não-toque: nada em `bagunca/` e `Skills/`. Todo script valida o caminho de escrita.

## Estado da implementação (uv)

- ✅ **F6 (scripts/ + comum/):** código movido com `git mv`; `comum/` com `caminhos.py`, `autor_json.py` e `ui/` (fontes, agora carregadas também no Windows, e áreas de texto somente leitura). Os comandos não mudaram (instalação editável via `uv sync`).
- ✅ **F7 (interface da automação):** `scripts/automacao/interface/` (controlador sem widgets + janela de 2 abas), atalhos `abrir-interface.bat` nas duas partes, `--so`/cancelar no CLI, READMEs curtos e guias atualizados. Skill `interface-tkinter` corrigida.
- ✅ **F8 (deploy na main):** receita no `README.md` da raiz; ainda **não executada** (depende de o usuário abrir o PR).
- ✅ Docstrings em todo o código de `scripts/`.

- 🔧 Correção da D7: a coluna "Meta até 12 dez" = `publicado` é o **objetivo** (97 das 104 linhas), não o estado. Status e Progresso saem só das 5 etapas; 5/5 = Concluído. Bate com a coluna "Status" da própria planilha.

- ✅ F1, F2, F3, F5 implementadas e ensaiadas ponta a ponta num worktree descartável da `main` (2 commits: checklist; autores + registro). 8 testes passam.
- ✅ F4 escrita (API, `inspecionar.py`, `--dry-run`); **não testada contra o Notion real**: falta o `NOTION_TOKEN`.
- ⚠️ No ensaio, 10 das 39 pastas casaram. As 29 restantes são os cursos antigos da aba "Cadastro dos 29" (fora da D4 = A). Faltas reais: `Vibe Coding - Essentials (Lovable)` × `iaclube/vibe-coding-essentials` e `ChatGPT … Word/PowerPoint/Excel` — ver D5.
- Rodar: `uv run python -m automacao` (detalhes em `automacao/README.md`).

## Fases

| Fase | O que entrega | Depende de | Pode começar já |
|---|---|---|---|
| [F1](F1-extrator-na-raiz.md) | `extrator_scorm/` na raiz, `path/`, `Cursos/registro-de-cursos.json` | nada | ✅ |
| [F2](F2-ingestao-checklist.md) | `xlsx` da `joao` → `automacao/referencias/` + `csv` + commit | nada | ✅ |
| [F3](F3-autor-json.md) | `autor.json` preenchido do `csv` | F1, F2 | depois de F1 e F2 |
| [F4](F4-notion.md) | Notion atualizado via API | F2, F3, token | depois do token |
| [F5](F5-orquestracao.md) | Um comando roda tudo; README; ensaio ponta a ponta | F1 a F4 | depois de F4 |
| [F6](F6-reestruturar-scripts.md) | Tudo em `scripts/` (com `comum/`), comandos iguais | decisões da interface | ✅ |
| [F7](F7-interface-automacao.md) | Interface tkinter da automação + atalhos `.bat` | F6 | depois da F6 |
| [F8](F8-promover-para-main.md) | Deploy de `scripts/` na `main` (receita no `README.md` da raiz) | F6 (e F7) | depois |

F1 e F2 são independentes e podem andar juntas.

## Premissas assumidas (mude se discordar)

1. **Sem push.** Só commit local.
2. **"Mais recente"** = maior versão no nome (`v0-4` > `v0-3`); empate pela data do commit.
3. **`csv`:** separador `,`; `,` dentro da célula vira `;`; quebra de linha na célula vira espaço; UTF-8 sem BOM; fórmulas vêm do valor em cache (🧪 conferir células vazias).
4. `controle.json`, `resumo.json`, `controle.anterior.json` e `fichas/` ficam na raiz do extrator e **não são versionados**. Só `Cursos/registro-de-cursos.json` é versionado.
5. `autor.json`: só última versão; só sobrescreve `null`; autor já escrito nunca é alterado.
6. Execução **manual** por linha de comando.
7. Segredos só em variável de ambiente ou `automacao/.env` (ignorado pelo git). A automação nunca grava nem imprime o token.

## Mapa de interferência

| Quando | O que | Esforço |
|---|---|---|
| Antes da F4 | Criar a integração no Notion, compartilhar o banco "Produção de cursos" com ela e definir `NOTION_TOKEN` | 5 min, uma vez |
| F3, 1º relatório | Olhar a lista de cursos que não casaram por slug | uma leitura |
| F5 | Aprovar o merge `structuring` → `main` | decisão |

Tudo fora disso roda sem perguntar.
