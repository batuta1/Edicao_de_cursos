# Documentação básica

Para quem nunca rodou isso. Leia na ordem; cada arquivo é curto.

| # | Arquivo | Para quê |
|---|---|---|
| 1 | [01-instalar.md](01-instalar.md) | Deixar o computador pronto (uma vez) |
| 2 | [02-rodar-tudo.md](02-rodar-tudo.md) | O comando principal e o que ele faz |
| 3 | [03-rodar-por-etapas.md](03-rodar-por-etapas.md) | "Quero só X": um comando para cada vontade |
| 4 | [04-notion-token.md](04-notion-token.md) | Ligar o Notion (uma vez) |
| 5 | [05-problemas-comuns.md](05-problemas-comuns.md) | Mensagem de erro → o que fazer |
| 6 | [06-onde-ficam-as-coisas.md](06-onde-ficam-as-coisas.md) | Mapa de pastas e arquivos |

## Em uma frase

Você roda **um comando**. Ele pega a planilha de produção (`checklist-producao-de-cursos-60-dias-*.xlsx`) da branch `joao`, converte para `csv`, preenche quem é o autor de cada curso e atualiza Status, Responsável e Progresso no Notion.

## Começo rápido (3 linhas)

```bash
uv sync
uv run python -m automacao --dry-run
uv run python -m automacao
```

1. `uv sync`: instala as dependências (uma vez).
2. `--dry-run`: **ensaio**. Mostra o que faria, não muda nada.
3. Sem `--dry-run`: faz de verdade (commits só locais; nunca faz push).

⚠️ Hoje o código está na branch `structuring` e a pasta `Cursos/` está na `main`. Até juntar as duas, leia a seção "Antes do merge" em [02-rodar-tudo.md](02-rodar-tudo.md).
