# F1 · Extrator na raiz do repositório

Decisões: [D3](../_duvidas/01-automacao-notion.md#d3) = `extrator_scorm`. Interferência do usuário: **nenhuma**.

## Objetivo

`_plan/extrator` vira o pacote `extrator_scorm/` na raiz, com os caminhos concentrados em `path/`, e o lote grava `Cursos/registro-de-cursos.json`.

## Checklist

### Mover e tornar executável
- [ ] Copiar `_plan/extrator` → `extrator_scorm/` (cópia, não `git mv`: `_plan/` é ignorado pelo git)
- [ ] Criar `extrator_scorm/__main__.py` chamando `interface.cli.main` (substitui o `extrair.py` que não veio)
- [ ] `python -m extrator_scorm` importa sem erro
- [ ] Manter `fontes/` como está

### Pasta `path/`
- [ ] Criar `extrator_scorm/path/__init__.py` e `extrator_scorm/path/caminhos.py` com todas as navegações:
  - [ ] `RAIZ_REPO` (sobe do `__file__` até a pasta que contém `Cursos/`)
  - [ ] `PASTA_CURSOS` = `RAIZ_REPO/Cursos`
  - [ ] `PASTA_EXTRATOR` = `RAIZ_REPO/extrator_scorm`
  - [ ] `REGISTRO` = `PASTA_CURSOS/registro-de-cursos.json`
  - [ ] `CONTROLE`, `CONTROLE_ANTERIOR`, `RESUMO`, `FICHAS` dentro de `PASTA_EXTRATOR`
- [ ] Trocar `servico.py:14` (`PASTA_SAIDA`) por import de `path.caminhos`
- [ ] Trocar `interface/tela.py:21` (`PASTA_PADRAO`, hoje `parents[3]/"Edicao_de_cursos"/"Cursos"`) por `PASTA_CURSOS`
- [ ] `lote/lote.py` (`NOME_ULTIMAS`, linha 16, e onde grava): gravar em `REGISTRO`, com o nome `registro-de-cursos.json`
- [ ] `lote/controle.py` e `lote/resumo.py`: gravar na raiz do extrator (mudar o valor padrão de `pasta_saida`)
- [ ] Atualizar textos de ajuda e mensagens que dizem `saida_extrator/` (`cli.py`, `lote.py`, `tela.py`)
- [ ] `grep -rn "saida_extrator\|ultimas_versoes\|Edicao_de_cursos"` em `extrator_scorm/` sem sobras

### Repositório
- [ ] `.gitignore`: `extrator_scorm/fichas/`, `extrator_scorm/controle.json`, `extrator_scorm/controle.anterior.json`, `extrator_scorm/resumo.json`, `.env`
- [ ] Corrigir `extrator_scorm/README.md`: comandos (`python -m extrator_scorm ...`) e links quebrados para `../documentos` e `../_planejamento`
- [ ] `requirements.txt` na raiz: `openpyxl` (F2), `requests` (F4), `tkinterdnd2` (só a tela)

### Verificação 🧪
- [ ] `python -m extrator_scorm Cursos --so-ultimas` termina sem erro
- [ ] `Cursos/registro-de-cursos.json` existe; `controle.json` e `resumo.json` estão em `extrator_scorm/`; nada novo em `saida_extrator/`
- [ ] Nº de cursos do registro ≥ nº em `../scorm_data_extractor/saida_extrator/ultimas_versoes.json`
- [ ] Segunda execução não reextrai nada (controle incremental)
- [ ] `git status`: só `extrator_scorm/`, `Cursos/registro-de-cursos.json`, `.gitignore`, `requirements.txt`; nada em `bagunca/` e `Skills/`

## Pronto quando

Os 5 itens de verificação passam.

## Commit

`git add extrator_scorm Cursos/registro-de-cursos.json .gitignore requirements.txt` com a mensagem `extrator: traz extrator SCORM para a raiz`. Sem push.
