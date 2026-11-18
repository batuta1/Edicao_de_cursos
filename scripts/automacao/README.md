# Automação checklist → Notion

Pega a planilha de produção da branch `joao`, gera o `csv`, preenche o autor de cada curso e atualiza Status, Responsável e Progresso no Notion.

**Abrir a interface:** duplo clique em [`abrir-interface.bat`](abrir-interface.bat) ou

```bash
uv run python -m automacao.interface
```

Linha de comando (`uv run python -m automacao --help`), token do Notion, regras e problemas comuns: [`scripts/documentacao/automacao-notion.md`](../documentacao/automacao-notion.md).
