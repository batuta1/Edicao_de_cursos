# 3 · Rodar por etapas ("quero só X")

Todos os comandos começam com `uv run python -m automacao`. Acrescente `--dry-run` a qualquer um para ensaiar.

| Quero… | Comando | Precisa de |
|---|---|---|
| Tudo | `uv run python -m automacao` | `Cursos/` (main) e token do Notion |
| Ensaio de tudo | `uv run python -m automacao --dry-run` | um `csv` já gerado |
| Só baixar a planilha e gerar o `csv` | `uv run python -m automacao --so checklist` | internet (ou `--sem-fetch`) |
| Baixar a planilha **sem commitar** | `uv run python -m automacao --so checklist --sem-commit` | |
| Só atualizar a lista de cursos (`registro-de-cursos.json`) | `uv run python -m automacao --so extrator` | `Cursos/` |
| Ver quem seria o autor de cada curso, sem gravar | `uv run python -m automacao --so autores --dry-run` | `csv` + registro |
| Gravar os autores | `uv run python -m automacao --so autores` | `csv` + registro |
| Ver o que iria para o Notion, sem token | `uv run python -m automacao --so notion --dry-run` | `csv` |
| Ver o que mudaria no Notion de verdade | `uv run python -m automacao --so notion --dry-run` | `csv` + token |
| Atualizar o Notion | `uv run python -m automacao --so notion` | `csv` + token |
| Tudo menos Notion | `uv run python -m automacao --sem-notion` | `Cursos/` |
| Planilha + extrator + autores | `uv run python -m automacao --so checklist extrator autores` | `Cursos/` |

## Comandos de apoio

| Quero… | Comando |
|---|---|
| Ver colunas e tipos do Notion (e conferir o token) | `uv run python -m automacao.notion.inspecionar` |
| Rodar os testes | `uv run python -m unittest discover -s automacao/testes -t .` |
| Extrator sozinho, um curso (zip ou pasta) | `uv run python -m extrator_scorm CAMINHO\do\pacote.zip` |
| Extrator sozinho, todos os cursos | `uv run python -m extrator_scorm Cursos --so-ultimas` |
| Abrir a tela do extrator | `uv run python -m extrator_scorm` (precisa de `uv sync --extra tela`) |
| Ver todas as opções | `uv run python -m automacao --help` |

## Receita: primeira vez, com calma

```bash
uv run python -m automacao --so checklist --sem-commit   # 1. baixa e converte, sem commit
uv run python -m automacao --so notion --dry-run         # 2. vê o que iria para o Notion
uv run python -m automacao.notion.inspecionar            # 3. confere o Notion (precisa do token)
uv run python -m automacao --so notion --dry-run         # 4. vê o que mudaria de verdade
uv run python -m automacao --so notion                   # 5. atualiza o Notion
```

## Relatórios

Depois de rodar, leia (são arquivos de texto):

| Arquivo | Conta |
|---|---|
| `automacao/relatorios/nao-casados.md` | Cursos da planilha sem pasta, pastas sem linha na planilha, autores gravados |
| `automacao/relatorios/notion.md` | Por curso: atualizado, sem mudança, não achou no Notion, duplicado ou erro |

Próximo: [04-notion-token.md](04-notion-token.md)
