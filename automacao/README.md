# Automação checklist → Notion

> Guia passo a passo para iniciantes: [`documentacao/automacao-notion.md`](../documentacao/automacao-notion.md).

Um comando lê o checklist de produção (branch `joao`), atualiza `autor.json` dos cursos e o banco "Produção de cursos" do Notion.

```bash
uv sync
uv run python -m automacao --dry-run      # não grava, não commita, não escreve no Notion
uv run python -m automacao                # tudo (commits locais; nunca faz push)
uv run python -m automacao --sem-notion --sem-fetch
uv run python -m automacao --so checklist     # só uma etapa: checklist extrator autores notion
```

Roda na branch que tem `Cursos/` (hoje a `main`). Em outra pasta de trabalho: `EDICAO_RAIZ=<raiz do repo>`.

## O que cada etapa faz

| Etapa | Módulo | Resultado |
|---|---|---|
| 1. Checklist | `checklist/buscar.py`, `xlsx_para_csv.py` | `git fetch` + `git show origin/joao:<xlsx mais recente>` → `automacao/referencias/` (só o mais recente), aba "Checklist 60 dias" → `.csv`. Commit `update de producao dos cursos (checklist vX-Y)` só dessa pasta |
| 2. Extrator | `extrator_scorm/` | `Cursos/registro-de-cursos.json` (últimas versões) |
| 3. Autores | `autores/casar.py`, `preencher.py` | Casa "Curso" com a pasta por slug (ou título do Rise); grava `{"autor": "João"}` só onde está `null`. Commit `update de autores e registro dos cursos` só desses arquivos |
| 4. Notion | `notion/` | Atualiza Status, Responsável e Progresso por API; não cria linhas |

Regras: Progresso = etapas E1–E6 com `x` ÷ 5; Responsável = coluna "Responsável", senão o `x` de João/Marina; os dois ou nenhum = vazio (no Notion não apaga o que existe).

Relatórios (ignorados pelo git): `relatorios/nao-casados.md` e `relatorios/notion.md`.

## Notion: token (uma vez)

1. Notion → Configurações → Conexões → criar integração interna; copiar o token.
2. No banco "Produção de cursos": `...` → Conexões → adicionar a integração.
3. Salvar em `automacao/.env` (ignorado pelo git): `NOTION_TOKEN=...` (ou variável de ambiente).
4. `uv run python -m automacao.notion.inspecionar` mostra colunas e tipos e confere as 4 colunas.
5. Opções do Status precisam existir no Notion: `Aguardando`, `Em produção`, `Concluído`; Responsável: `João`, `Marina` (se for seleção).

## Testes

```bash
uv run python -m unittest discover -s automacao/testes -t .
```

## Segurança

Escreve só em `automacao/`, `extrator_scorm/`, `Cursos/`, `.gitignore`, `pyproject.toml`, `uv.lock`; recusa `bagunca/` e `Skills/`. Commit sempre só dos caminhos do processo.
