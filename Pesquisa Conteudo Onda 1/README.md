# Pesquisa Conteudo Onda 1

Prompts de pesquisa para o **ChatGPT Work** levantar o conteúdo bruto dos 9 cursos da Onda 1 (ver `cursos-onda-1-por-trilha.txt`). Cada prompt gera um `.txt` que serve de material-fonte para criar a ementa do curso com a skill `criar-ementa-curso`.

| # | Prompt | Curso | Arquivo que o ChatGPT entrega |
|---|---|---|---|
| 1 | [01-notebooklm-essentials.md](01-notebooklm-essentials.md) | NotebookLM - Essentials | `ConteudoBruto_notebooklm-essentials.txt` |
| 2 | [02-mcp-essentials.md](02-mcp-essentials.md) | MCP - Essentials | `ConteudoBruto_mcp-essentials.txt` |
| 2b | [02b-mcp-essentials-complemento.md](02b-mcp-essentials-complemento.md) | MCP - Essentials (lacunas) | `ConteudoBruto_mcp-essentials_complemento.txt` |
| 3 | [03-perplexity-essentials.md](03-perplexity-essentials.md) | Perplexity - Essentials | `ConteudoBruto_perplexity-essentials.txt` |
| 3b | [03b-perplexity-essentials-complemento.md](03b-perplexity-essentials-complemento.md) | Perplexity - Essentials (lacunas) | `ConteudoBruto_perplexity-essentials_complemento.txt` |
| 4 | [04-agentes-de-ia-essentials.md](04-agentes-de-ia-essentials.md) | Agentes de IA - Essentials | `ConteudoBruto_agentes-de-ia-essentials.txt` |
| 4b | [04b-agentes-de-ia-essentials-complemento.md](04b-agentes-de-ia-essentials-complemento.md) | Agentes de IA - Essentials (lacunas) | `ConteudoBruto_agentes-de-ia-essentials_complemento.txt` |
| 5 | [05-vibe-coding-essentials.md](05-vibe-coding-essentials.md) | Vibe Coding - Essentials | `ConteudoBruto_vibe-coding-essentials.txt` |
| 6 | [06-cursor-essentials.md](06-cursor-essentials.md) | Cursor - Essentials | `ConteudoBruto_cursor-essentials.txt` |
| 7 | [07-gemini-workspace-essentials.md](07-gemini-workspace-essentials.md) | Gemini Workspace - Essentials | `ConteudoBruto_gemini-workspace-essentials.txt` |
| 8 | [08-n8n-agentes-de-ia-essentials-6.md](08-n8n-agentes-de-ia-essentials-6.md) | N8N: Agentes de IA - Essentials 6 | `ConteudoBruto_n8n-agentes-de-ia-essentials-6.txt` |
| 9 | [09-replit-agent-essentials.md](09-replit-agent-essentials.md) | Replit Agent - Essentials | `ConteudoBruto_replit-agent-essentials.txt` |

## Fluxo

1. Copie o bloco **Prompt** do arquivo do curso e cole no ChatGPT Work (um curso por conversa).
2. Salve o `.txt` entregue em `conteudo-bruto/<id-do-curso>/` (ex.: `conteudo-bruto/mcp-essentials/`).
3. Baixe para a mesma pasta tudo o que estiver na seção **MATERIAIS PARA BAIXAR** do `.txt` (itens `[BAIXAR]`). Itens `[ACESSO RESTRITO]` exigem login ou pagamento: decidir caso a caso.
4. Salve como PDF, na mesma pasta, as páginas da seção **PÁGINAS PARA SALVAR** (no navegador: Imprimir > Salvar como PDF, com o nome sugerido). O ChatGPT só resume essas páginas; o texto oficial completo fica nesses PDFs.
5. Revise a seção **LACUNAS E PONTOS A VERIFICAR** e confira os itens marcados `[VERIFICAR]`.
6. Use a pasta inteira (`.txt` + materiais baixados + páginas salvas) como material-fonte da skill `criar-ementa-curso`.

## Como os prompts foram montados

- **Parte comum**: o que a skill `criar-ementa-curso` precisa para gerar um bom curso, ou seja, glossário para leigos, nomes exatos de menus para os breadcrumbs, passo a passo executável, planos (gratuito × pago), segurança e privacidade, erros comuns e ideias de exercício com critério de êxito.
- **Parte específica**: competência, tarefa observável e ferramenta-âncora (de `novos-cursos-iaclube-priorizacao-v6.json`), público, pré-requisito e posição nas trilhas (de `trilhas.json`), o que fica de fora porque outro curso cobre, e os pontos de pesquisa próprios da ferramenta.
- **Versões:** os prompts já rodados ficam como estão, para registrar o que gerou cada pesquisa.
  - **Versão 1** — prompt 01 (NotebookLM).
  - **Versão 2** — prompt 02 (MCP). Corrige o que a avaliação do NotebookLM mostrou:
    - marcação [SUGESTÃO] para o que o ChatGPT elabora, para não inflar o [CONFIRMADO];
    - conferência de que cada arquivo baixado é o arquivo real, e não a página HTML do portal;
    - todo material não-web citado tem de aparecer na lista de downloads;
    - origem de cada nome de menu (interface ou ajuda);
    - links de exercício testados;
    - cada número atribuído à fonte certa;
    - checagem de mudança de marca;
    - checklist final antes de entregar.
  - **Versão 3** — prompt 03 (Perplexity). Acrescenta o que a avaliação do MCP mostrou:
    - **regra de profundidade:** pesquisa no nível do público; o que for técnico demais vai para um apêndice;
    - **decomposição da tarefa observável:** cada ação ganha passo a passo e exercício;
    - **seção PÁGINAS PARA SALVAR:** o ChatGPT se recusa a transcrever páginas inteiras por direitos autorais, então as páginas oficiais essenciais são salvas pela equipe.
  - **Versão 5** — prompts 05 a 09. Acrescenta o que a avaliação de Agentes de IA mostrou:
    - [CONFIRMADO] só quando a fonte diz aquilo literalmente; conclusões viram [VERIFICAR] ou [SUGESTÃO];
    - curso autoinstrucional: nada de instrutor, aula ao vivo ou divisão em blocos de tempo;
    - todos os pontos do foco e todos os materiais pedidos respondidos, ou NÃO ENCONTRADO;
    - cabeçalho, seções e checklist exatamente como pedidos;
    - um item por página na seção PÁGINAS PARA SALVAR;
    - preferência por materiais de exercício em português.
  - **04b** — prompt complementar que cobre as lacunas da pesquisa de Agentes de IA:
    - se o "modo agente" do ChatGPT ainda existe;
    - o que cada plano gratuito permite;
    - definições da OpenAI e acadêmica;
    - system cards;
    - casos brasileiros e avaliações independentes;
    - interface em pt-BR;
    - materiais em português para os exercícios.
  - **Versão 4** — prompt 04 (Agentes de IA). Acrescenta o que a avaliação da Perplexity mostrou:
    - fontes em pt-BR primeiro, depois em inglês; outros idiomas só quando forem a única fonte;
    - lojas, preços e ofertas do Brasil;
    - proibição de endereços de ambiente de teste (dev., hml., staging.);
    - casos de uso reais obrigatórios, ou NÃO ENCONTRADO, sem cenários hipotéticos no lugar;
    - checklist final respondida com SIM/NÃO, sem os rótulos de conteúdo.
  - **03b** — prompt complementar que cobre as lacunas da pesquisa da Perplexity: casos brasileiros de citação jurídica inventada, orientações do CNJ e da OAB, como conferir jurisprudência nas fontes oficiais, casos reais de uso, interface em pt-BR e a página pública da oferta da Vivo.
  - **02b** — prompt complementar que cobre as lacunas da pesquisa de MCP: ler arquivos, executar ações, planos do ChatGPT para usuários, interface em português e contexto brasileiro.
- A data de referência aparece na linha "Data de hoje" de cada prompt (17/10/2026 nos prompts 01 a 03b; 18/10/2026 a partir do 04b). Se a pesquisa for feita muito depois, atualize a linha "Data de hoje" no prompt.
