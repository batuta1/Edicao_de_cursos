# 4 · Ligar o Notion (uma vez)

A automação fala com o Notion pela API oficial. Para isso precisa de um **token** (uma senha da integração). Quem cria e guarda o token é **você**.

## Passo a passo

1. No Notion: **Configurações → Conexões → Desenvolver ou gerenciar integrações → Nova integração**. Tipo: interna. Dê um nome (ex.: "Automação de cursos") e salve.
2. Copie o **Segredo da integração interna** (o token).
3. Abra a página/banco **"Produção de cursos"** → menu `⋯` → **Conexões** → adicione a integração que você criou. Sem este passo a automação não enxerga o banco.
4. Guarde o token em um destes lugares:

   **A. Arquivo `.env`** (recomendado). Crie `automacao/.env` com uma linha:

   ```
   NOTION_TOKEN=cole-o-token-aqui
   ```

   Esse arquivo é ignorado pelo git: não sobe para o repositório.

   **B. Variável de ambiente** (vale só para a janela do terminal):

   ```powershell
   $env:NOTION_TOKEN = "cole-o-token-aqui"
   ```

5. Confira:

```bash
uv run python -m automacao.notion.inspecionar
```

Deve listar as colunas do banco e terminar com `config.json gravado; as 4 colunas foram encontradas.`

## O que o banco precisa ter

| Coluna | Tipo aceito | Valores |
|---|---|---|
| Nome do curso | título | igual ao "Curso" da planilha (sem acento/maiúscula não importa) |
| Status | Status ou Seleção | `Aguardando`, `Em produção`, `Concluído` (precisam existir como opções) |
| Responsável | Seleção, Multi-seleção, Texto ou Pessoa | `João`, `Marina` |
| Progresso | Número | formato **porcentagem** → grava 0,6 (= 60%); outro formato → grava 60 |

Regras de segurança da automação:

- **Não cria** linhas: curso da planilha que não existe no Notion vai para o relatório.
- **Não apaga**: sem responsável na planilha, o Notion fica como está.
- **Só escreve o que mudou**; rodar duas vezes seguidas não altera nada na segunda.
- O token nunca é impresso nem gravado no repositório.

## Se mudar o link ou o banco

Defina `NOTION_DATABASE_ID=<id do banco>` no `.env`. O id são os 32 caracteres no fim do link do Notion.

Próximo: [05-problemas-comuns.md](05-problemas-comuns.md)
