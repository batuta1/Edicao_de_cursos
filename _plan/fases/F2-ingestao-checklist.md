# F2 · Ingestão do checklist (`joao` → `referencias` → `csv`)

Decisões: [D2](../_duvidas/01-automacao-notion.md#d2) = `automacao/referencias/`; [D4](../_duvidas/01-automacao-notion.md#d4) = só a aba "Checklist 60 dias"; [D8](../_duvidas/01-automacao-notion.md#d8) = `git show origin/joao:…` e commit na branch atual. Interferência do usuário: **nenhuma**.

## Objetivo

Um comando pega o `checklist-producao-de-cursos-60-dias-*.xlsx` mais recente da `joao`, deixa só ele em `automacao/referencias/`, gera o `csv` e faz **um** commit só desses arquivos.

## Checklist

### Buscar o arquivo
- [ ] `automacao/checklist/buscar.py`: `git fetch origin joao` (opção `--sem-fetch`)
- [ ] Listar `git ls-tree -r --name-only origin/joao` e filtrar por `^checklist-producao-de-cursos-60-dias-v(\d+)-(\d+)\.xlsx$`
- [ ] Escolher o maior `(major, minor)`; hoje deve resultar `v0-4`
- [ ] Gravar em `automacao/referencias/` via `git show origin/joao:<arquivo>` (binário; sem trocar de branch)
- [ ] Apagar de `referencias/` os `checklist-*.xlsx` e `csv` **mais antigos**
- [ ] Se o `xlsx` baixado é idêntico ao que já está lá (hash), não regravar e não commitar

### Converter
- [ ] `automacao/checklist/xlsx_para_csv.py` com `openpyxl` (`data_only=True`)
- [ ] Separador `,`; `,` dentro da célula → `;`; quebra de linha na célula → espaço; UTF-8
- [ ] Só a aba **"Checklist 60 dias"** → `referencias/checklist-producao-de-cursos-60-dias-vX-Y.csv`
- [ ] Nome da aba em constante, não por posição; se a aba sumir, erro claro
- [ ] 🧪 Fórmula sem valor em cache (célula vazia onde deveria ter número): avisar no log

### Commit só do processo
- [ ] Lista explícita de caminhos permitidos: `automacao/referencias/**`; outro caminho → erro antes de commitar
- [ ] Guarda: recusar tocar `bagunca/` e `Skills/`
- [ ] `git add -- <caminhos>` e `git commit -m "update de producao dos cursos (checklist vX-Y)" -- <caminhos>` (não leva o que já estava em stage)
- [ ] Remoção do `xlsx` antigo entra no mesmo commit
- [ ] Sem push

### Testes 🧪
- [ ] Escolha de versão (`v0-3`, `v0-4`, `v0-10` → `v0-10`)
- [ ] Conversor com célula com vírgula, quebra de linha, acento e número
- [ ] Execução real: `referencias/` com 1 `xlsx` + 1 `csv`; `git log -1 --stat` lista só esses arquivos
- [ ] Segunda execução: sem mudança, sem commit novo

## Pronto quando

`git show --stat HEAD` mostra só arquivos de `automacao/referencias/` e o `csv` tem o cabeçalho + 104 linhas de dados.
