# 6 · Onde ficam as coisas

## Pastas

| Pasta | O que é |
|---|---|
| `documentacao/` | Estes guias |
| `automacao/` | O código da automação (checklist → autores → Notion) |
| `automacao/referencias/` | A planilha baixada (`.xlsx`) e o `csv`. Só a versão mais recente fica aqui |
| `automacao/relatorios/` | Relatórios em texto de cada execução (não vão para o git) |
| `automacao/notion/config.json` | Gerado por `inspecionar`: id do banco e colunas (sem token; não vai para o git) |
| `automacao/.env` | Seu token do Notion (você cria; não vai para o git) |
| `extrator_scorm/` | O extrator de dados de SCORM |
| `extrator_scorm/path/caminhos.py` | **Todos** os caminhos do extrator num lugar só |
| `Cursos/` | Os cursos (só na `main`): `Cursos/<Empresa>/<curso>/scorm/vN/` |
| `Cursos/registro-de-cursos.json` | Lista de todos os cursos (última versão de cada) |
| `Cursos/.../vN/autor.json` | Autor da versão: `{"autor": "João"}` ou `{"autor": null}` |
| `bagunca/`, `Skills/` | **Intocados** pela automação |
| `_plan/` | Planejamento (decisões e fases) |

## Arquivos gerados pelo extrator (não vão para o git)

| Arquivo | Para quê |
|---|---|
| `extrator_scorm/controle.json` | Lembra o que já foi lido, para não ler de novo |
| `extrator_scorm/resumo.json` | Resumo por curso e versão |
| `extrator_scorm/fichas/` | Uma ficha por pacote |

## Códigos principais (se um dia precisar mexer)

| Arquivo | Faz |
|---|---|
| `automacao/atualizar.py` | O comando principal e as etapas |
| `automacao/checklist/buscar.py` | Acha e baixa o `xlsx` mais novo da `joao` |
| `automacao/checklist/xlsx_para_csv.py` | Converte (`,` dentro da célula vira `;`) |
| `automacao/checklist/leitura.py` | Regras de autor, Status e Progresso |
| `automacao/autores/` | Casa curso × pasta e grava `autor.json` |
| `automacao/notion/` | `modelo.py` (o que enviar), `api.py` (conversa com o Notion), `sincronizar.py`, `inspecionar.py` |
| `automacao/git_seguro.py` | Commits só dos arquivos do processo; recusa `bagunca/` e `Skills/` |

## Glossário

| Palavra | Significa |
|---|---|
| **checklist** | A planilha `checklist-producao-de-cursos-60-dias-*.xlsx`, mantida na branch `joao` |
| **dry-run** | Ensaio: mostra o que faria sem mudar nada |
| **commit** | Registro local de mudanças no git. A automação não faz `push` |
| **SCORM** | O pacote do curso exportado pelo Rise/Articulate |
| **slug** | Nome sem acento e com hífens: `MCP - Essentials` → `mcp-essentials` |
| **token** | A "senha" da integração com o Notion ([04](04-notion-token.md)) |
