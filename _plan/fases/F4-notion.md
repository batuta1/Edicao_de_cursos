# F4 · Atualizar o Notion (API)

Decisões: [D1](../_duvidas/01-automacao-notion.md#d1) = **API oficial**; [D7](../_duvidas/01-automacao-notion.md#d7) = Progresso = etapas com `x` ÷ 5. Banco: "Produção de cursos" (link na [D1.2](../_duvidas/01-automacao-notion.md#d1); ID `40d4a1ed76b480b18f67febbce8ade93`).
Depende de: F2 (`csv`); usa os autores da F3 quando houver.
Interferência do usuário: **uma ação**, o token.

## Objetivo

Para cada curso do `csv`, achar a linha pelo "Nome do curso" e atualizar "Status", "Responsável" e "Progresso".

## Pré-requisito 👉 (do usuário)

- [ ] Criar uma integração interna no Notion, compartilhar o banco "Produção de cursos" com ela e definir `NOTION_TOKEN` como variável de ambiente (ou em `automacao/.env`, ignorado pelo git). A automação nunca lê para exibir, grava no repositório nem imprime o token.

## Checklist

### Descobrir colunas e tipos (sem perguntar)
- [ ] `automacao/notion/inspecionar.py`: com `NOTION_TOKEN`, resolve o ID do link (página ou banco; se for página, procura o banco dentro dela) e imprime o esquema: nome e tipo de cada coluna
- [ ] Procurar as 4 colunas por nome normalizado: "Nome do curso" (título), "Status", "Responsável", "Progresso"; diferença de nome → erro listando as colunas encontradas
- [ ] Gravar `automacao/notion/config.json` com o ID do banco e o mapa coluna → tipo (sem token)
- [ ] Fixar a versão da API do Notion no cabeçalho e conferir na inspeção se o endpoint é de banco ou de fonte de dados 🧪

### Modelo (sem Notion)
- [ ] `automacao/notion/modelo.py`: do `csv` monta `[{nome, status, responsavel, progresso}]`
  - [ ] Progresso = nº de `x` em E1–2, E3, E4, E5, E6 ÷ 5
  - [ ] Status: Meta = `publicado` **ou** 5/5 → `Concluído`; 1 a 4 → `Em produção`; 0 → `Aguardando`
  - [ ] Meta `publicado` com etapas vazias: ganha `publicado` (Concluído, 100%)
  - [ ] Responsável: mesma regra da F3 (João | Marina | vazio)
- [ ] `--dry-run`: tabela "curso · antes → depois" sem escrever

### Escrita via API
- [ ] `automacao/notion/api.py` (`requests`): consulta o banco, acha a linha pelo título normalizado (sem acento nem caixa), atualiza só o que mudou
- [ ] Adapta ao tipo lido: Status (`status` ou `select`) → nome da opção; Responsável (`select`, `multi_select`, `people` ou texto) → valor; Progresso (`number`) → fração se o formato for percentual, senão 0 a 100
- [ ] Opção inexistente no Notion (ex.: `Em produção`) → erro claro (a API não cria opções de `status`)
- [ ] Linha do `csv` sem correspondência no Notion: não cria nada; vai para `automacao/relatorios/notion.md`
- [ ] Linha duplicada no Notion: não escreve; vai para o relatório
- [ ] Limite de requisições: espera e repete até 3 vezes
- [ ] Idempotente: valor igual → "sem mudança"
- [ ] Log por curso (ok / sem mudança / não achou / duplicado / erro); código de saída ≠ 0 se houver erro

### Testes 🧪
- [ ] Modelo com os 5 casos de Status (0, 1–4, 5/5, `publicado` sem etapas, `publicado` com etapas)
- [ ] `--dry-run` no banco real; conferir 3 linhas na tela
- [ ] Escrever **1 curso** real e conferir no Notion; depois o lote
- [ ] 2ª execução: "sem mudança" em tudo

## Pronto quando

`--dry-run` bate com o esperado, 1 curso real foi atualizado e conferido, e a 2ª execução não muda nada.
