# 2 · Rodar tudo

```bash
uv run python -m automacao
```

## O que acontece (nesta ordem)

| # | Etapa | O que faz | Muda o quê |
|---|---|---|---|
| 1 | `checklist` | Baixa o `xlsx` mais recente da branch `joao` (`v0-4` > `v0-3`), apaga os antigos, gera o `csv` | `automacao/referencias/` + **1 commit** |
| 2 | `extrator` | Lê os SCORM de `Cursos/` e monta a lista de todos os cursos | `Cursos/registro-de-cursos.json` |
| 3 | `autores` | Descobre o autor de cada curso na planilha e escreve no `autor.json` | `autor.json` dos cursos + **1 commit** |
| 4 | `notion` | Atualiza Status, Responsável e Progresso de cada curso | Notion |

Nunca faz `push`. Os commits ficam só no seu computador e só levam os arquivos do processo.

## Sempre faça o ensaio primeiro

```bash
uv run python -m automacao --dry-run
```

Não grava, não commita, não escreve no Notion. Mostra o que faria. Para o ensaio funcionar precisa existir um `csv` em `automacao/referencias/` (rode antes `--so checklist`, veja [03](03-rodar-por-etapas.md)).

## Opções

| Opção | Efeito |
|---|---|
| `--dry-run` | Ensaio: não muda nada |
| `--so checklist extrator autores notion` | Roda só as etapas escritas (uma ou várias) |
| `--sem-notion` | Faz tudo menos o Notion |
| `--sem-commit` | Faz tudo mas não commita |
| `--sem-fetch` | Não consulta o servidor antes de ler a branch `joao` (use sem internet) |

## Como o autor é decidido

1. Coluna **Responsável** da planilha, se estiver preenchida.
2. Senão, o `x` na coluna **João** ou **Marina**.
3. Os dois marcados, ou nenhum: fica `null` (vazio). Nada é inventado.

`autor.json` que já tem nome **nunca** é alterado. Só a **última versão** de cada curso é preenchida.

## Como Status e Progresso são calculados

Planilha: 5 etapas com `x` (E1–2, E3, E4, E5, E6).

| Situação | Status no Notion | Progresso |
|---|---|---|
| Nenhum `x` | Aguardando | 0% |
| 1 a 4 `x` | Em produção | 20% a 80% (nº de `x` ÷ 5) |
| 5 `x`, ou "Meta" = `publicado` | Concluído | 100% |

## ⚠️ Antes do merge (hoje)

A pasta `Cursos/` só existe na `main`. Se você rodar na `structuring`, as etapas `extrator` e `autores` param com a mensagem "Cursos não existe nesta branch". As etapas `checklist` e `notion` rodam em qualquer branch.

Para testar tudo sem mexer nas suas branches, use uma cópia temporária da `main`:

```powershell
git worktree add -b teste-automacao ..\Edicao_main main
$env:EDICAO_RAIZ = "$PWD\..\Edicao_main"
uv run python -m automacao --dry-run
uv run python -m automacao --sem-notion
```

Os commits dessa execução ficam na branch `teste-automacao` da cópia. Quando terminar o teste:

```powershell
Remove-Item Env:EDICAO_RAIZ
git worktree remove ..\Edicao_main
git branch -D teste-automacao
```

Depois que a `structuring` for para a `main`, basta `uv run python -m automacao` na pasta do projeto.

Próximo: [03-rodar-por-etapas.md](03-rodar-por-etapas.md)
