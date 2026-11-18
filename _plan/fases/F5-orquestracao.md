# F5 · Orquestração e entrega

Depende de: F1 a F4. Interferência do usuário: **uma aprovação** (merge da `structuring` na `main`).

## Objetivo

Um comando roda tudo na ordem certa; o README diz como usar; a branch fica pronta para a `main`.

## Checklist

### Comando único
- [ ] `automacao/atualizar.py` roda: F2 (buscar + `csv` + commit) → F1 (extrator, `--so-ultimas`) → F3 (autores + commit) → F4 (Notion)
- [ ] Opções: `--dry-run`, `--sem-notion`, `--sem-commit`, `--sem-fetch`
- [ ] Para na primeira etapa que falhar e diz qual; não deixa commit pela metade
- [ ] Resumo final: arquivo usado (`v0-4`), cursos lidos, autores preenchidos, cursos não casados, Notion (ok / sem mudança / não achou / erro)
- [ ] Guarda global: toda escrita fica em `automacao/`, `extrator_scorm/`, `Cursos/` e `.gitignore`; nunca `bagunca/` ou `Skills/`

### Documentação
- [ ] `automacao/README.md`: pré-requisitos, comando, o que cada etapa faz, onde ficam os relatórios
- [ ] Como criar a integração e definir o `NOTION_TOKEN` (passo a passo, sem exemplo de token real)
- [ ] O que fazer com a lista de cursos não casados

### Ensaio final 🧪
- [ ] `--dry-run`: nada muda (`git status` limpo, Notion intacto)
- [ ] Execução real: no máximo 3 commits (`update de producao dos cursos`, `update de autores dos cursos`, e o do extrator se algo mudou)
- [ ] 2ª execução imediata: nenhum commit; Notion "sem mudança"
- [ ] `git diff main..structuring --stat` sem alteração em `bagunca/` e `Skills/`

### Entrega
- [ ] 👉 Aprovação do usuário para mover da `structuring` para a `main` (readme: "quando a implementação ficar estável")
- [ ] Sem push automático; push e merge são do usuário

## Pronto quando

O ensaio final passa e o usuário aprova o merge.
