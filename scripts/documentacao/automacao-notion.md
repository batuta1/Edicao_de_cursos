# Automação do checklist → Notion

Pega a planilha de produção da branch `joao`, gera um `csv`, preenche o autor de cada curso e atualiza **Status, Responsável e Progresso** no Notion.

## 🖥️ Interface (janela)

| Como abrir | O que é |
|---|---|
| Duplo clique em `scripts/automacao/abrir-interface.bat` | Atalho do Windows (precisa do `uv` instalado) |
| `uv run python -m automacao.interface` | O mesmo, pelo terminal |

- **Aba Executar:** marque as etapas, faça um **Ensaio** (mostra a tabela do que mudaria) e só depois **Aplicar**. `Parar` interrompe entre um curso e outro.
- **Aba Notion:** mostra se o token existe (ele nunca é digitado na janela) e **Testar conexão** lista as colunas do banco.
- Etapa que não pode rodar fica desativada com o motivo escrito ao lado (por exemplo, sem a pasta `Cursos/`).
- A caixa "Fazer commit" vem marcada: os commits são locais, nunca há `push`.

## Comandos essenciais

Rode sempre na pasta do repositório. Primeira vez? Faça [instalar.md](instalar.md) e [Notion: token](#notion-ligar-o-token-uma-vez).

| Comando | O que faz |
|---|---|
| `uv run python -m automacao --so checklist --sem-commit` | Baixa o `xlsx` mais recente da `joao` e gera o `csv`. Faça isto antes do primeiro dry-run |
| `uv run python -m automacao.notion.inspecionar` | Confere o token e mostra as colunas do Notion. Não escreve nada |
| `uv run python -m automacao --so notion --dry-run` | **Ensaio do Notion**: mostra o que mudaria. Não escreve nada. Relatório em `scripts/automacao/relatorios/notion.md` |
| `uv run python -m automacao --so notion` | **Atualiza o Notion de verdade** |
| `uv run python -m automacao --dry-run` | Ensaio de tudo (precisa de `Cursos/`, ou seja, da `main`) |
| `uv run python -m automacao` | Tudo: planilha → registro de cursos → autores → Notion (precisa da `main`) |

O fluxo seguro, na ordem:

```bash
uv run python -m automacao --so checklist --sem-commit   # 1. planilha → csv
uv run python -m automacao --so notion --dry-run         # 2. ensaio
uv run python -m automacao --so notion                   # 3. de verdade (depois de ler o relatório)
```

**Observações rápidas**
- `--dry-run` nunca escreve no Notion, nunca commita e nunca grava autor.
- Nunca faz `push`. Os commits são locais.
- Na `structuring` só funcionam `--so checklist` e `--so notion` (as outras etapas precisam da pasta `Cursos/`, que só existe na `main`).
- Rodar duas vezes seguidas não muda nada na segunda: só escreve o que mudou.

## Opções

| Opção | Efeito |
|---|---|
| `--so ETAPA ...` | Roda só estas etapas: `checklist` `extrator` `autores` `notion` (padrão: todas) |
| `--dry-run` | Ensaio: não grava, não commita, não escreve no Notion |
| `--sem-notion` | Tudo menos o Notion |
| `--sem-commit` | Não commita |
| `--sem-fetch` | Não consulta o servidor antes de ler a branch `joao` (sem internet) |

---

# Aprofundando

## O que cada etapa faz

| # | Etapa | Faz | Muda |
|---|---|---|---|
| 1 | `checklist` | `git fetch` + `git show origin/joao:<xlsx>`: pega o de maior versão (`v0-4` > `v0-3`), apaga os antigos, converte a aba "Checklist 60 dias" em `csv` | `scripts/automacao/referencias/` + 1 commit `update de producao dos cursos (checklist vX-Y)` |
| 2 | `extrator` | Roda o [extrator de SCORM](extrator-scorm.md) | `Cursos/registro-de-cursos.json` |
| 3 | `autores` | Casa cada curso da planilha com a pasta em `Cursos/` e grava `autor.json` | `autor.json` + 1 commit `update de autores e registro dos cursos` |
| 4 | `notion` | Compara a planilha com o Notion e atualiza o que mudou | Notion |

As etapas 2 e 3 precisam de `Cursos/`. As etapas 1 e 4 não.

## Regras

**Status e Progresso** (só pelas 5 etapas da planilha: E1–2, E3, E4, E5, E6):

| `x` marcados | Status | Progresso |
|---|---|---|
| 0 | Aguardando | 0% |
| 1 a 4 | Em produção | nº de `x` ÷ 5 (20% a 80%) |
| 5 | Concluído | 100% |

⚠️ A coluna "Meta até 12 dez" (`publicado`) é a **meta**, não o estado. Ela não entra na conta.

**Autor / Responsável:**
1. Coluna **Responsável** da planilha, se preenchida (vira `João` ou `Marina`).
2. Senão, o `x` na coluna **João** ou **Marina**.
3. Os dois marcados, ou nenhum: vazio. No Notion, vazio **não apaga** o que já está lá. No `autor.json`, só preenche onde está `null` e só na última versão; nome já escrito nunca é trocado.

**Casamento curso × pasta** (para o `autor.json`): por nome exato, sem acento nem maiúscula (`MCP - Essentials` → `mcp-essentials`), ou pelo título do Rise. Não chuta: o que não casa vai para `scripts/automacao/relatorios/nao-casados.md`.

## Notion: ligar o token (uma vez)

1. No Notion: **Configurações → Conexões → Desenvolver ou gerenciar integrações → Nova integração** (interna). Copie o **segredo**.
2. Na página **"Produção de cursos"** e também no banco **original** que ela mostra (a página tem uma *visão*; ícone ↗ ao lado do título): `⋯` → **Conexões** → adicione a integração.
3. Crie `scripts/automacao/.env` com uma linha (o arquivo é ignorado pelo git):

   ```
   NOTION_TOKEN=cole-o-token-aqui
   ```

   Ou, só para a janela atual do terminal: `$env:NOTION_TOKEN = "cole-o-token-aqui"`.
4. Confira: `uv run python -m automacao.notion.inspecionar` termina com `config.json gravado; as 4 colunas foram encontradas.`

Se houver mais de uma fonte de dados visível, ponha `NOTION_DATA_SOURCE_ID=<id>` no `.env`.

## O que o banco do Notion precisa ter

| Coluna | Tipo aceito | Valores |
|---|---|---|
| Nome do curso | título | igual ao "Curso" da planilha (acento e maiúscula não importam) |
| Status | Status ou Seleção | `Aguardando`, `Em produção`, `Concluído` (devem existir como opções) |
| Responsável | Seleção, Multi-seleção, Texto ou Pessoa | `João`, `Marina` |
| Progresso | Número | formato porcentagem: grava 0,6 para 60%; outro formato: grava 60 |

Garantias: não cria linhas; não apaga valores; só escreve o que mudou; o token nunca é impresso nem gravado no repositório.

## Relatórios (texto, fora do git)

| Arquivo | Conta |
|---|---|
| `scripts/automacao/relatorios/notion.md` | Por curso: atualizado, sem mudança, não achou no Notion, duplicado, erro |
| `scripts/automacao/relatorios/nao-casados.md` | Cursos da planilha sem pasta, pastas sem linha, autores gravados |

## Antes do merge: testar tudo numa cópia da `main`

```powershell
git worktree add -b teste-automacao ..\Edicao_main main
$env:EDICAO_RAIZ = "$PWD\..\Edicao_main"
uv run python -m automacao --so checklist extrator autores --sem-notion
```

Os commits ficam na branch `teste-automacao` da cópia. Para limpar:

```powershell
Remove-Item Env:EDICAO_RAIZ
git worktree remove ..\Edicao_main
git branch -D teste-automacao
```

## Problemas comuns

| Mensagem | O que fazer |
|---|---|
| `Cursos não existe nesta branch` | Rode na `main`, use a cópia acima, ou use só `--so checklist` / `--so notion` |
| `não há csv em scripts/automacao/referencias/` | `uv run python -m automacao --so checklist --sem-commit` |
| `falta Cursos/registro-de-cursos.json` | `uv run python -m automacao --so extrator` (na `main`) |
| `nenhum checklist-...xlsx na raiz de origin/joao` | O arquivo precisa se chamar `checklist-producao-de-cursos-60-dias-vX-Y.xlsx` na raiz da `joao` |
| `git fetch` falha | Sem internet: use `--sem-fetch` |
| `NOTION_TOKEN não definido` | Veja "ligar o token" |
| `401` / `unauthorized` | Token errado ou expirado: gere outro e atualize o `.env` |
| `a integração vê a página, mas não achou a fonte de dados` | Compartilhe também o banco **original** (↗ na visão) com a integração |
| `coluna "X" não encontrada. Colunas do banco: ...` | O nome da coluna é outro; a lista mostra o que existe |
| `Progresso deveria ser número` | Troque a coluna para Número |
| Erro de opção em Status | Crie a opção com o nome exato no Notion |
| "não achou no Notion" | O nome na planilha difere do Notion (lembre: `,` do nome vira `;` no `csv`) |
| "duplicado no Notion" | Duas linhas com o mesmo nome: apague a repetida |
| `a automação não mexe em ...` | Proteção: só escreve em `scripts/` e `Cursos/`; `bagunca/` e `Skills/` são sempre recusados |

**Desfazer:** os commits são locais. `git reset --soft HEAD~1` desfaz o último mantendo os arquivos. O Notion **não** tem desfazer: use `--dry-run` antes.

## Onde ficam as coisas

| Caminho | O que é |
|---|---|
| `scripts/automacao/atualizar.py` | O comando principal |
| `scripts/automacao/checklist/` | Baixar o `xlsx`, converter, regras de autor/status |
| `scripts/automacao/autores/` | Casar curso × pasta e gravar `autor.json` |
| `scripts/automacao/notion/` | `modelo.py` (o que enviar), `api.py` (conversa com o Notion), `sincronizar.py`, `inspecionar.py` |
| `scripts/automacao/git_seguro.py` | Commits só dos arquivos do processo |
| `scripts/automacao/referencias/` | `xlsx` e `csv` (só a versão mais recente) |
| `scripts/automacao/.env` | Seu token (não vai para o git) |

Glossário: **dry-run** = ensaio sem mudar nada · **checklist** = a planilha `checklist-producao-de-cursos-60-dias-*.xlsx` · **commit** = registro local no git.
