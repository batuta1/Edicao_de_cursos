# Documentação

Dois documentos, um para cada parte do repositório. Cada um começa com os comandos principais.

| Quero mexer com… | Leia só este |
|---|---|
| 📋 **Planilha de produção e Notion** (autores, Status, Progresso) | **[automacao-notion.md](automacao-notion.md)** |
| 📦 **Mapear os cursos SCORM** (ler `Cursos/`, gerar o registro de cursos) | **[extrator-scorm.md](extrator-scorm.md)** |

Antes de qualquer um: [instalar.md](instalar.md) (uma vez).

As duas partes são independentes: uma funciona sem a outra.

## Começo rápido

```bash
uv sync                                                  # instala (uma vez)
uv run python -m automacao --so notion --dry-run         # ensaio do Notion
uv run python -m extrator_scorm Cursos --so-ultimas      # mapeia os SCORM (na main)
```

## Como as duas partes se ligam

Só por um arquivo: `Cursos/registro-de-cursos.json` (feito pelo extrator, lido pela etapa `autores` da automação). Uma funciona sem a outra.

| | Automação do Notion | Extrator de SCORM |
|---|---|---|
| Pasta | `automacao/` | `extrator_scorm/` |
| Pergunta | Em que pé está a produção e quem cuida de cada curso? | Quais cursos existem e como são por dentro? |
| Lê | planilha da branch `joao`, Notion | `Cursos/` |
| Produz | `csv`, `autor.json`, Notion atualizado | `Cursos/registro-de-cursos.json` |

⚠️ Hoje o código está na `structuring` e `Cursos/` só existe na `main`. Até o merge: a automação roda `--so checklist` e `--so notion`; o extrator precisa da `main` (ou da cópia temporária explicada em [automacao-notion.md](automacao-notion.md#antes-do-merge-testar-tudo-numa-cópia-da-main)).
