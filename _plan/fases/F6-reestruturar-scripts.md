# F6 · Reestruturar em `scripts/` (com `comum/`)

Decisões: [D1](../_duvidas/02-interface-automacao.md#d1) e "Estrutura nova" (P10 a P15). Interferência do usuário: **nenhuma** (o `.env` é movido sem ler o conteúdo).
Vem **antes** da F7 (interface). Não toca `Cursos/`, `Skills/` nem `bagunca/`.

## Objetivo

Tudo que é código fica em `scripts/`; o que as duas partes usam fica em `scripts/comum/`; os comandos continuam iguais.

## Checklist

### Mover (com `git mv`, para manter o histórico)
- [ ] `automacao/` → `scripts/automacao/`
- [ ] `extrator_scorm/` → `scripts/extrator_scorm/`
- [ ] `documentacao/` → `scripts/documentacao/`
- [ ] `automacao/.env.example` (já commitado) e `automacao/.env` (ignorado pelo git) → `scripts/automacao/.env`: mover o arquivo sem abrir; confirmar só que existe
- [ ] Arquivos gerados e ignorados (`fichas/`, `controle.json`, `resumo.json`, `referencias/*.xlsx|csv`) acompanham a pasta ou são regenerados; nenhum entra no git

### Criar `scripts/comum/`
- [ ] `comum/caminhos.py`: `RAIZ_REPO`, `PASTA_CURSOS`, `EDICAO_RAIZ` (hoje em `extrator_scorm/path/caminhos.py`); a raiz passa a ser achada pela pasta que contém `scripts/` ou `Cursos/`
- [ ] `comum/autor_json.py`: `NOME_DO_ARQUIVO`, `pasta_da_versao`, `ler_declaracao`, `escrever` (hoje em `extrator_scorm/lote/autores.py` e `automacao/autores/preencher.py`)
- [ ] `comum/ui/fontes.py` + `comum/ui/arquivos/` (`.ttf`, `OFL.txt`, `UFL.txt`), movidos de `extrator_scorm/interface/fontes.py` e `extrator_scorm/fontes/`
- [ ] `extrator_scorm/path/caminhos.py` fica só com o que é do extrator (fichas, controle, resumo) e importa a raiz de `comum`
- [ ] `automacao/caminhos.py` importa a raiz de `comum` **e não mais** de `extrator_scorm`
- [ ] `automacao/autores/preencher.py` passa a usar `comum.autor_json` (some o import de `extrator_scorm.lote.autores`)
- [ ] Verificar: `grep -rn "from extrator_scorm\|import extrator_scorm" scripts/automacao` só acha o `atualizar.py` (a etapa `extrator`)
- [ ] Verificar: `grep -rn "automacao" scripts/extrator_scorm scripts/comum` sem resultado

### `pyproject.toml` (raiz)
- [ ] Trocar `package = false` por projeto instalável (backend `hatchling`), `packages = ["scripts/automacao", "scripts/extrator_scorm", "scripts/comum"]`
- [ ] `uv sync` e conferir: `uv run python -m automacao --help`, `uv run python -m extrator_scorm --help`, `uv run python -c "import comum"`
- [ ] `uv.lock` atualizado

### READMEs curtos por pasta (D2)
- [ ] `scripts/extrator_scorm/README.md`: resumir para ≤ 15 linhas (o que é, o comando/atalho que abre a interface, link para a documentação)
- [ ] O conteúdo técnico longo do README atual (diagramas, fases A a D) vai para `scripts/documentacao/extrator-scorm-tecnico.md`, sem perder nada
- [ ] `scripts/automacao/README.md`: o mesmo formato curto
- [ ] Os atalhos `abrir-interface.bat` são criados na F7 (a tela da automação ainda não existe); o do extrator já pode ser criado aqui

### Ajustes de texto e proteção
- [ ] `PERMITIDOS` em `caminhos.py`: `scripts/`, `Cursos/`, `.gitignore`, `pyproject.toml`, `uv.lock`; `PROIBIDOS` continua `bagunca/`, `Skills/`
- [ ] `.gitignore`: caminhos novos (`scripts/extrator_scorm/fichas/`, `scripts/extrator_scorm/controle*.json`, `scripts/extrator_scorm/resumo.json`, `scripts/automacao/relatorios/*.md`, `scripts/automacao/notion/config.json`, `.env`)
- [ ] Documentação: trocar caminhos (`automacao/...` → `scripts/automacao/...`); os comandos `uv run ...` continuam iguais
- [ ] README de `automacao/` e do extrator com os caminhos novos
- [ ] `--so checklist` grava em `scripts/automacao/referencias/`

- [ ] `README.md` da raiz: ajustar a seção "O que tem aqui" (a nota sobre a F6 sai quando ela terminar)

### Verificação 🧪
- [ ] `uv run python -m unittest discover -s scripts/automacao/testes -t scripts` passa (8/8)
- [ ] `uv run python -m automacao --so checklist --sem-commit --sem-fetch` e `--so notion --dry-run` funcionam com o token movido
- [ ] Ensaio completo numa cópia da `main` (worktree) com `EDICAO_RAIZ`: 2 commits, só com arquivos permitidos
- [ ] `git status` mostra só movimentações e edições dentro de `scripts/`, `.gitignore`, `pyproject.toml`, `uv.lock`

## Pronto quando

Os comandos documentados funcionam sem alteração, nenhuma das duas partes importa da outra (só de `comum`) e os testes passam.

## Commit

Um commit de movimentação (`git mv`, sem mudar conteúdo) e outro com os ajustes de imports e `pyproject.toml`, para o histórico seguir os arquivos.
