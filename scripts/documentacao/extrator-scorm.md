# Extrator de SCORM

Lê os pacotes SCORM (Articulate Rise 360) da pasta `Cursos/` e gera uma **ficha** de cada curso (título, capítulos, blocos, palavras, regras de conclusão, alertas) e a lista de todos os cursos em `Cursos/registro-de-cursos.json`.

Não depende do Notion nem da planilha. Só lê `Cursos/` (que está na branch `main`).

## 🖥️ Interface (janela)

| Como abrir | O que é |
|---|---|
| Duplo clique em `scripts/extrator_scorm/abrir-interface.bat` | Atalho do Windows (precisa do `uv` instalado) |
| `uv run python -m extrator_scorm` | O mesmo, pelo terminal (sem argumentos abre a janela) |

- **Aba Pasta de cursos:** `Varrer` lista os pacotes; `Extrair tudo` roda o lote (com `Parar`). Opções: só as últimas versões, forçar.
- **Aba Individual:** escolha um `.zip`, veja o JSON e grave a ficha.
- As áreas de texto são somente leitura (dá para selecionar e copiar).

## Comandos essenciais

| Comando | O que faz |
|---|---|
| `uv run python -m extrator_scorm Cursos --so-ultimas` | **O principal.** Lê só a última versão (maior `vN`) de cada curso. Grava `Cursos/registro-de-cursos.json` |
| `uv run python -m extrator_scorm Cursos` | Lê **todas** as versões (mais lento) |
| `uv run python -m extrator_scorm Cursos --forcar` | Refaz tudo, ignorando o que já foi lido |
| `uv run python -m extrator_scorm caminho\pacote.zip` | Um pacote só (zip, ou pasta de um pacote). Grava em `scripts/extrator_scorm/fichas/_individuais/` |
| `uv run python -m extrator_scorm.lote.varredura Cursos` | Só **lista** os pacotes encontrados. Não grava nada |
| `uv run python -m extrator_scorm.lote.autores Cursos` | Mostra quantas versões estão sem `autor.json` |
| `uv run python -m extrator_scorm.lote.autores Cursos --criar` | Cria os `autor.json` que faltam, com `{"autor": null}`. Nunca sobrescreve |
| `uv run python -m extrator_scorm` | Abre a **tela** (precisa de `uv sync --extra tela`) |

**Observações rápidas**
- Rode na pasta do repositório. O caminho `Cursos` só existe na `main`; em outra branch dá `Arquivo não encontrado`.
- Rodar de novo é seguro: só lê de novo o que é novo ou mudou (controle por `sha256`).
- Um pacote com erro vira linha do relatório e **não** interrompe os outros.
- Só lê `Cursos/`. Os únicos arquivos que o extrator escreve são os JSON listados abaixo.

## Opções do lote

| Opção | Efeito |
|---|---|
| `--so-ultimas` | Extrai só a última versão de cada curso (o resumo continua completo) |
| `--forcar` | Extrai tudo de novo, ignorando o controle |
| `--ignorar CAMINHO` | Ignora um caminho relativo a `Cursos/` (repetível) |

## O que ele grava

| Arquivo | Para quê | Vai para o git? |
|---|---|---|
| `Cursos/registro-de-cursos.json` | A ficha **completa** da última versão de cada curso (+ autor) | **Sim** |
| `scripts/extrator_scorm/resumo.json` | Só números por curso e versão; marca a versão vigente e conteúdo repetido | Não |
| `scripts/extrator_scorm/controle.json` | O que já foi lido (novo, alterado, sem mudança, cópia idêntica, sumido) | Não |
| `scripts/extrator_scorm/controle.anterior.json` | O controle da execução anterior | Não |
| `scripts/extrator_scorm/fichas/<caminho>.json` | Uma ficha por pacote | Não |
| `scripts/extrator_scorm/fichas/_individuais/` | Fichas de pacotes rodados um a um | Não |

---

# Aprofundando

## Como ele funciona

```
Cursos/ → 1. varredura → 2. controle → 3. extrator (A a D) → 4. resumo
          (acha pacotes)  (o que mudou)  (lê só o novo)       (registro + resumo)
```

1. **Varredura:** acha `.zip` SCORM e pastas SCORM (com `imsmanifest.xml` na raiz). Empresa, curso e versão vêm do caminho `Cursos/<Empresa>/<curso>/scorm/vN/`.
2. **Controle:** calcula o `sha256` de cada pacote e compara com a execução anterior.
3. **Extração (A a D):** abre o zip em memória (ou a pasta no lugar), lê o manifesto, decodifica o JSON do curso (que está escondido em base64 dentro de `scormcontent/`) e monta a ficha. **Nada é extraído no disco**; o texto do conteúdo não é guardado, só a estrutura.
4. **Resumo:** agrupa por empresa e curso; a versão **vigente** é a de maior número.

## O que tem em cada ficha

| Bloco | Conteúdo |
|---|---|
| `curso` | id, título, descrição, autores do Rise, datas, se foi publicado depois da última edição |
| `capitulos` | título, tipo (conteúdo ou quiz), blocos, palavras, interativos; no quiz: nota mínima, tentativas, questões |
| `tamanho` | totais e minutos de leitura estimados (200 palavras/min) |
| `lms` | padrão exportado, como reporta e como conclui |
| `pacote` | nome, tamanho, `sha256`, versão do SCORM, `impressao_do_curso` (a mesma em pacotes diferentes = mesma versão do curso) |
| `alertas` / `avisos` | observações sobre o curso / o que aconteceu na leitura |

## Três níveis de problema

| Nível | Exemplos | O que acontece |
|---|---|---|
| **Erro** | arquivo inexistente, zip corrompido | Para e mostra a mensagem (no lote: vira linha do relatório) |
| **Aviso** | zip dentro de zip, sem manifesto | Continua e anota na ficha |
| **Alerta** | player em inglês, capítulo sem descrição, sem quiz | É uma observação sobre o curso |

## Autor de cada versão

Um nome por versão, declarado em `Cursos/<Empresa>/<curso>/scorm/vN/autor.json` (`{"autor": "Nome"}` ou `{"autor": null}`). Vale, em ordem:
1. o `autor.json`;
2. o autor do Rise, só se for uma pessoa (a conta "Iaclube Help" não conta);
3. nada (`null`).

O autor do commit no git aparece só como pista (`autor_sugerido.git`). Quem preenche o `autor.json` a partir da planilha é a [automação do Notion](automacao-notion.md).

## Conexão com a automação do Notion

O único ponto de contato é `Cursos/registro-de-cursos.json` e o formato do `autor.json`. A etapa `autores` da automação lê o registro para saber quais cursos existem e em que pasta escrever.

## Problemas comuns

| Mensagem | O que fazer |
|---|---|
| `Arquivo não encontrado: Cursos` | Você não está na `main` (a pasta `Cursos/` só existe lá) |
| Nenhum pacote encontrado | Caminho errado: o extrator avisa e **não grava nada**, para não apagar o controle anterior |
| Um pacote com `erro` | Veja a mensagem no relatório; os outros pacotes seguem normais |
| "N versões ainda sem autor.json" | `uv run python -m extrator_scorm.lote.autores Cursos --criar` |
| A tela não abre | `uv sync --extra tela`; no Linux, `sudo apt install python3-tk` |

## Onde ficam as coisas

| Caminho | O que é |
|---|---|
| `scripts/extrator_scorm/servico.py` | A lógica (a linha de comando e a tela só chamam isto) |
| `scripts/extrator_scorm/path/caminhos.py` | **Todos** os caminhos do extrator num lugar só |
| `scripts/extrator_scorm/leitura/` | Abrir zip/pasta, ler manifesto, achar e decodificar o JSON do curso |
| `scripts/extrator_scorm/estrutura/` | Montar a ficha |
| `scripts/extrator_scorm/lote/` | Varredura, controle, lote, resumo, autores |
| `scripts/extrator_scorm/interface/` | Linha de comando (`cli.py`) e tela (`tela.py`) |
| `scripts/documentacao/extrator-scorm-tecnico.md` | Documento técnico completo, com diagramas |

Glossário: **ficha** = JSON com os dados de um pacote · **versão vigente** = a de maior `vN` · **`sha256`** = impressão digital do arquivo, usada para saber se mudou.
