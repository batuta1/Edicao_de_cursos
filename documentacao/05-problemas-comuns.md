# 5 · Problemas comuns

| Mensagem | O que significa | O que fazer |
|---|---|---|
| `Cursos não existe nesta branch` | Você está na `structuring`; `Cursos/` está na `main` | Veja "Antes do merge" em [02](02-rodar-tudo.md), ou use `--so checklist` / `--so notion` |
| `não há csv em automacao/referencias/` | Ainda não baixou a planilha | `uv run python -m automacao --so checklist` |
| `falta Cursos/registro-de-cursos.json` | O extrator ainda não rodou | `uv run python -m automacao --so extrator` |
| `nenhum checklist-...xlsx na raiz de origin/joao` | A branch `joao` não tem o arquivo (ou o nome mudou) | Confira na branch `joao`; o nome precisa ser `checklist-producao-de-cursos-60-dias-vX-Y.xlsx` |
| `git fetch ...` falha | Sem internet ou sem acesso ao GitHub | `--sem-fetch` usa o que já está baixado |
| `NOTION_TOKEN não definido` | Falta o token | [04](04-notion-token.md) |
| `401` / `unauthorized` | Token errado ou expirado | Gere de novo e atualize o `.env` |
| `a integração vê a página, mas não os dados do banco` (ou `does not contain any data sources`) | O banco da página é uma **visão** de outro banco, que não foi compartilhado | Abra o banco original (ícone ↗ ao lado do título) → `⋯` → Conexões → adicione a integração |
| `404` / "o link não é um banco..." | O banco não foi compartilhado com a integração | Notion → banco → `⋯` → Conexões → adicionar a integração |
| `coluna "Progresso" não encontrada. Colunas do banco: ...` | O nome da coluna é diferente | Renomeie no Notion ou me avise; a lista mostra o que existe |
| `Progresso deveria ser número` | A coluna Progresso é de outro tipo | Troque para Número (formato porcentagem) |
| Status: erro de opção | A opção (`Em produção` etc.) não existe | Crie a opção no Notion com o nome exato |
| Curso aparece em "não achou no Notion" | O nome na planilha é diferente do Notion | Corrija o nome em um dos dois |
| Curso aparece em "duplicado no Notion" | Duas linhas com o mesmo nome | Apague a repetida no Notion |
| "pastas sem linha" no relatório de autores | Cursos antigos que não estão na aba "Checklist 60 dias" | Normal. Só os cursos da planilha ganham autor |
| Um curso existe mas não casou | O nome da planilha não bate com a pasta (nem com o título do Rise) | Veja `nao-casados.md`; o casamento é só por nome exato (sem acento/maiúscula) |
| `a aba "Checklist 60 dias" não existe` | A planilha mudou de estrutura | Me avise: o nome da aba está fixo em `xlsx_para_csv.py` |
| `a automação não mexe em ...` | Proteção: só escreve em `automacao/`, `extrator_scorm/`, `Cursos/` | Não é para mexer; `bagunca/` e `Skills/` são sempre recusados |

## Desfazer

Os commits da automação são locais. Para desfazer o último (mantendo os arquivos):

```bash
git reset --soft HEAD~1
```

O Notion **não** tem desfazer pela automação; por isso use `--dry-run` antes e confira `relatorios/notion.md`.

Próximo: [06-onde-ficam-as-coisas.md](06-onde-ficam-as-coisas.md)
