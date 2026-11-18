# F3 · Preencher `autor.json`

Decisões: [D5](../_duvidas/01-automacao-notion.md#d5) = casamento automático por slug (sem mapa manual); [D6](../_duvidas/01-automacao-notion.md#d6) = "Responsável" se preenchido, senão o `x` de João/Marina, sem dado → `null`; 6.1 = nome curto; 6.2 = os dois marcados → `null`.
Depende de: F1 (registro e pastas) e F2 (`csv`). Interferência do usuário: **uma leitura** do 1º relatório.

## Objetivo

Para cada linha do `csv` que casa com uma pasta de `Cursos/`, gravar o autor em `Cursos/<Empresa>/<curso>/scorm/vN/autor.json` da última versão.

## Checklist

### Casar curso ↔ pasta (só slug)
- [ ] `automacao/autores/casar.py`: normalizar (minúsculo, sem acento, sem pontuação, espaços → `-`) o campo "Curso" do `csv` e comparar com o slug de cada curso do `Cursos/registro-de-cursos.json`
- [ ] Ordem de tentativa: slug igual → slug da pasta sem prefixo de empresa (`openai-`, `google-`…) igual → vários candidatos = **ambíguo, não casa**
- [ ] Nunca chuta: sem casamento exato não grava nada
- [ ] Relatório `automacao/relatorios/nao-casados.md` com 3 listas separadas: **sem pasta (esperado)**, **ambíguos** e **pastas sem linha no `csv`**
- [ ] Mostrar no resumo a taxa: linhas casadas ÷ pastas existentes. ⚠️ Se várias pastas não casarem, reabrir a D5 (mapa manual como D9)

### Preencher
- [ ] `automacao/autores/preencher.py` lê o `csv` (colunas `Curso`, `João`, `Marina`, `Responsável`)
- [ ] Regra:
  - [ ] "Responsável" preenchido → usa; normaliza para o nome curto (`João Vitor` → `João`, `Marina Moreno` → `Marina`)
  - [ ] senão só `João` com `x` → `João`; só `Marina` com `x` → `Marina`
  - [ ] os dois com `x` (6.2) ou nenhum → `null`, com aviso no relatório quando forem os dois
- [ ] Reusar as funções de `extrator_scorm/lote/autores.py` (ler/escrever `autor.json`); não duplicar o formato
- [ ] Grava só se o `autor` atual é `null`; autor já preenchido é preservado e, se divergir do `csv`, entra no relatório
- [ ] Só a pasta da **última versão** (maior `vN`)
- [ ] `--dry-run` mostra o que mudaria sem gravar

### Fechar
- [ ] Rodar o extrator (F1) para o `registro-de-cursos.json` refletir os autores novos
- [ ] Commit só de `Cursos/**/autor.json` alterados + `Cursos/registro-de-cursos.json`: `update de autores dos cursos`
- [ ] Guarda de caminhos (nada em `bagunca/`, `Skills/`)

### Testes 🧪
- [ ] Casamento com nomes difíceis (`ChatGPT Chat - Essentials`, `Perplexity Comet - Essentials`, `MCP - Essentials`)
- [ ] Regra do autor: Responsável, só João, só Marina, ambos, nenhum
- [ ] `--dry-run` primeiro; relatório conferido; depois gravação

## Pronto quando

Todo curso casado com autor definido no `csv` tem `autor.json` preenchido; a 2ª execução não altera nada; o relatório lista o que não casou.
