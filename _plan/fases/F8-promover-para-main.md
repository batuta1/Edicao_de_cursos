# F8 · Promover `scripts/` para a `main`

Depende de: F6 (e da F7, se a interface já estiver pronta). Interferência do usuário: **abrir o PR e aprovar o merge**. O passo a passo está no `README.md` da raiz (seção "Deploy").

## Objetivo

Levar só `scripts/`, `pyproject.toml`, `uv.lock` e `.gitattributes` para a `main`, sem tocar em `Cursos/`, `Skills/` nem `bagunca/`. A `structuring` continua sendo o laboratório.

## Por que não é um merge

A `structuring` foi limpa (não tem `Cursos/`, `Skills/`, `bagunca/`) e a `main` andou 43 commits desde a separação. Um `git merge` pode aplicar as remoções na `main`. Por isso o deploy usa `git checkout structuring -- <caminhos>` numa cópia da `main`.

## Checklist

### Antes (na `structuring`)
- [ ] `git status` limpo; testes passam (`uv run python -m unittest discover -s scripts/automacao/testes -t scripts`)
- [ ] Ensaio completo numa cópia da `main` com `EDICAO_RAIZ` (README da raiz e `scripts/documentacao/automacao-notion.md`)
- [ ] `.env` fora do commit: `git ls-files | findstr /i "\.env"` só mostra `.env.example`

### Deploy (README da raiz, seção "🚀 Deploy")
- [ ] `git worktree add -b promove-scripts ..\Edicao_main origin/main`
- [ ] `git rm -r -q --ignore-unmatch scripts` + `git checkout structuring -- scripts pyproject.toml uv.lock .gitattributes`
- [ ] `.gitignore`: juntar à mão só as linhas novas
- [ ] `git diff origin/main --stat -- Cursos Skills bagunca` **vazio**
- [ ] Commit e `git push -u origin promove-scripts`; PR `promove-scripts` → `main`

### Depois (já na `main`)
- [ ] `uv sync` e `uv run python -m automacao --so notion --dry-run`
- [ ] `uv run python -m extrator_scorm Cursos --so-ultimas` (agora `Cursos/` existe)
- [ ] `uv run python -m automacao --dry-run` (ensaio de tudo)
- [ ] Limpar a cópia: `git worktree remove ..\Edicao_main` e `git branch -D promove-scripts`

## Regra de trabalho (daqui em diante)

Correção ou melhoria: **primeiro na `structuring`**, testa, e só então repete o deploy. Nada de editar `scripts/` direto na `main`.

## Pronto quando

A `main` tem `scripts/` funcionando, `Cursos/`, `Skills/` e `bagunca/` intactos, e o ensaio de tudo passa.
