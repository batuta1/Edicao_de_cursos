# 1 · Instalar (uma vez)

## O que você precisa

| Programa | Como saber se tem | Onde pegar |
|---|---|---|
| Git | `git --version` | https://git-scm.com |
| uv (gerenciador do Python) | `uv --version` | https://docs.astral.sh/uv/ |

Python não precisa instalar à mão: o `uv` cuida.

## Passo a passo

1. Abra o terminal **na pasta do repositório** (`Edicao_de_cursos`).
2. Rode:

```bash
uv sync
```

Isso cria a pasta `.venv` e instala `openpyxl` (ler o `xlsx`) e `requests` (falar com o Notion). Não precisa ativar nada: sempre use `uv run ...`.

3. Teste se está tudo certo:

```bash
uv run python -m unittest discover -s automacao/testes -t .
```

Deve terminar com `OK`.

## Só para a tela do extrator (opcional)

```bash
uv sync --extra tela
uv run python -m extrator_scorm
```

Abre a janela do extrator de SCORM. Não é necessária para a automação.

Próximo: [02-rodar-tudo.md](02-rodar-tudo.md)
