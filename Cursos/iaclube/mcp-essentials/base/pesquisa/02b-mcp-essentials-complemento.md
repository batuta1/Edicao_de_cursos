# Pesquisa complementar — MCP - Essentials

| Campo | Valor |
|---|---|
| Curso | MCP - Essentials |
| Por que existe | A primeira pesquisa (`ConteudoBruto_mcp-essentials.txt`) ficou forte no protocolo e fraca no que o aluno não programador faz. Este prompt cobre só as lacunas. |
| Pesquisa feita por | ChatGPT Work |
| Arquivo que o ChatGPT deve entregar | `ConteudoBruto_mcp-essentials_complemento.txt` |

## Como usar

1. Abra uma conversa **nova** no ChatGPT Work e cole todo o bloco "Prompt" abaixo.
2. Salve o `.txt` entregue em `Pesquisa Conteudo Onda 1/conteudo-bruto/mcp-essentials/`, ao lado da primeira pesquisa.
3. Baixe os itens de **MATERIAIS PARA BAIXAR** e salve as páginas de **PÁGINAS PARA SALVAR** (no navegador: Imprimir > Salvar como PDF, com o nome sugerido) na mesma pasta.
4. As duas pesquisas juntas formam o conteúdo bruto do curso.

## Prompt

```text
# PAPEL
Você é um pesquisador de conteúdo a serviço de uma equipe brasileira de design
instrucional (IAClube.com). Esta é uma PESQUISA COMPLEMENTAR: uma primeira
pesquisa sobre o mesmo curso já foi feita e cobriu bem o protocolo. Agora a
equipe precisa só do que faltou. Você NÃO vai escrever o curso, a ementa nem o
plano de aula: vai coletar, organizar e referenciar a matéria-prima.

Data de hoje: 17 de outubro de 2026.

# O CURSO
- Nome: MCP - Essentials. Curso introdutório e autoinstrucional, de 100 a 130
  minutos, para quem NÃO programa: profissionais que querem delegar tarefas a
  assistentes de IA e curiosos técnicos.
- Ferramentas-âncora: Claude e ChatGPT.
- Competência: conectar assistentes a ferramentas e dados via Model Context
  Protocol.
- Tarefa observável: instalar e usar conectores MCP em Claude e ChatGPT para LER
  ARQUIVOS, CONSULTAR SERVIÇOS e EXECUTAR AÇÕES com segurança.
- Idioma e país do público: português, Brasil.

# O QUE JÁ ESTÁ COBERTO (NÃO REPITA)
A primeira pesquisa já reuniu, com fontes: origem do MCP, governança (Agentic AI
Foundation), especificação 2026-07-28 e suas mudanças, arquitetura host-client-
server, tools/resources/prompts, transportes, OAuth em nível conceitual, planos e
preços do Claude, requisitos do Claude Desktop, passo a passo para adicionar
conector remoto personalizado no Claude (ajuda em inglês), extensões do Claude
Desktop (.mcpb), fluxo "Plugins > Add custom MCP server" no ChatGPT (documentação
de desenvolvedor), registro oficial e diretórios, riscos gerais (tool poisoning,
prompt injection), comparação com API, Zapier/n8n, plugins e skills, cursos
existentes (Anthropic Academy, Hugging Face, DeepLearning.AI), e um exercício de
consulta com o servidor público OpenAI Docs MCP.

# REGRA DE PROFUNDIDADE (IMPORTANTE)
O aluno não programa. Pesquise o que ele VÊ e FAZ na tela: onde clicar, o que
aparece, o que o conector consegue ler ou fazer, que permissão é pedida e como
desfazer. NÃO pesquise construção de servidores, SDKs, detalhes do protocolo,
JSON, OAuth do lado do desenvolvedor nem solução de problemas de quem programa
um servidor: isso é de outro curso (Construindo Servidores MCP - Hands On).

# O QUE PESQUISAR
1. LER ARQUIVOS
   a. Claude Desktop: a extensão oficial de acesso a arquivos locais (Filesystem
      ou equivalente atual) — nome exato no diretório, quem publica, planos e
      sistemas compatíveis, passo a passo para instalar, como escolher as pastas
      permitidas, o que o Claude consegue fazer (listar, ler, criar, editar,
      apagar?), como a aprovação de cada ação aparece na tela, como remover.
   b. Conectores de arquivos na nuvem no Claude e no ChatGPT (Google Drive,
      OneDrive/SharePoint, Dropbox, Box): para cada um, quem publica, plano
      exigido, se só lê ou também escreve, que tipos de arquivo lê, passo a passo
      de conexão e como desconectar.
2. CONSULTAR SERVIÇOS
   Conectores oficiais de uso comum para quem não programa (Gmail, Google
   Calendar, Notion, Slack, GitHub, Canva, Asana e outros que estejam em
   destaque nos diretórios): monte uma ficha por conector com publicador, onde
   aparece (Claude, ChatGPT ou ambos), plano exigido em cada um, se é gratuito,
   o que lê, o que faz, tipo de autenticação e disponibilidade no Brasil.
3. EXECUTAR AÇÕES COM SEGURANÇA
   a. Encontre ao menos duas ações reversíveis e de baixo risco que um aluno
      possa executar com conector oficial, de preferência no plano gratuito (ex.:
      criar um evento de teste no calendário, criar uma página no Notion, criar
      um rascunho de e-mail sem enviar). Para cada uma: passo a passo, o que
      aparece na tela de aprovação, como desfazer.
   b. Como Claude e ChatGPT pedem confirmação antes de uma ação: nomes exatos dos
      botões e opções (ex.: permitir uma vez, permitir sempre, negar), onde se
      revogam permissões dadas, onde se veem as ações executadas.
4. CHATGPT: QUEM PODE USAR
   a. Quais planos (Free, Go, Plus, Pro, Business, Enterprise, Edu) podem: usar o
      diretório de plugins/apps/conectores; conectar um servidor MCP
      personalizado. Procure em páginas de ajuda para USUÁRIOS (Central de Ajuda
      / ChatGPT Learn), não só em documentação para desenvolvedores.
   b. Se a interface mostra "Plugins", "Apps" ou "Conectores", e se isso varia
      por conta, plano ou região.
5. INTERFACE EM PORTUGUÊS
   Para os fluxos dos itens 1 a 4, os nomes dos menus e botões em português do
   Brasil, no Claude e no ChatGPT. Procure páginas de ajuda em pt-BR; se só
   houver em inglês, diga isso. Indique a origem de cada nome: (interface),
   (ajuda pt-BR) ou (ajuda en).
6. CONTEXTO BRASILEIRO
   a. Artigos, cursos, vídeos e materiais em português que expliquem MCP para
      leigos, com as analogias que usam.
   b. Exemplos de uso de MCP ou de conectores de IA em empresas, órgãos públicos
      ou escolas brasileiras (se não houver, escreva NÃO ENCONTRADO).
   c. Orientações brasileiras (ANPD, LGPD, órgãos de governo) aplicáveis a dar a
      um assistente de IA acesso a arquivos, e-mail e serviços de trabalho.

# FONTES
- Prefira documentação oficial, central de ajuda e diretórios oficiais; depois
  imprensa e publicações confiáveis; comunidade sempre marcada como tal.
- Para cada fonte: título, URL, tipo, data da fonte (se visível) e data de acesso.
- Seja imparcial entre Anthropic e OpenAI.

# MATERIAIS E PÁGINAS
- Materiais que não são páginas da web (PDF, guias, vídeos, modelos): liste em
  MATERIAIS PARA BAIXAR, marcados [BAIXAR], com título, link direto, tipo,
  idioma, utilidade e nome de arquivo sugerido. Só declare BAIXADO depois de
  conferir que o arquivo é do tipo anunciado (um PDF começa com "%PDF" e não é a
  página HTML do site). Para vídeos, diga se há transcrição. Marque
  [ACESSO RESTRITO] o que exigir login ou pagamento.
- Páginas oficiais cujo texto completo a equipe precisa guardar (passo a passo,
  planos, permissões, avisos): liste em PÁGINAS PARA SALVAR, com título, URL, o
  trecho que importa, prioridade (alta, média) e nome de arquivo sugerido sem
  acento (ex.: claude-ajuda-extensao-arquivos.pdf). A equipe vai salvar essas
  páginas como PDF; você não precisa transcrevê-las por inteiro.

# REGRAS
1. Não invente nada. Se não encontrar, escreva "NÃO ENCONTRADO" e diga onde
   procurou.
2. Use só estas marcações: [CONFIRMADO] para fato sustentado por fonte oficial
   ou por duas fontes independentes; [VERIFICAR] para fonte única não oficial,
   antiga ou contraditória; [SUGESTÃO] para tudo o que for elaboração sua
   (exercícios, recomendações, comparações, cenários). Nunca marque uma
   elaboração sua como [CONFIRMADO].
3. Registre a data de cada fonte. Desconfie de informação com mais de 12 meses.
4. Atribua cada número e cada plano à página que de fato o contém.
5. Diferencie sempre o que vale para o plano gratuito e o que exige plano pago.
6. Links para o aluno usar em exercícios precisam ser públicos e levar direto ao
   conteúdo; teste cada um.
7. Não escreva ementa, plano de aula nem objetivos de aprendizagem.
8. Escreva em português do Brasil; mantenha em inglês os nomes que só existem em
   inglês.

# FORMATO DE ENTREGA
Entregue UM arquivo de texto puro (.txt), em UTF-8, chamado
ConteudoBruto_mcp-essentials_complemento.txt, para download, nesta estrutura:

================================================================
CONTEÚDO BRUTO (COMPLEMENTO) — MCP - Essentials
Pesquisa realizada em: [data]
================================================================

0. RESUMO EXECUTIVO (até 10 linhas: o que esta pesquisa acrescenta e os
   alertas principais)
1. LER ARQUIVOS (1a local; 1b nuvem)
2. CONSULTAR SERVIÇOS (uma ficha por conector)
3. EXECUTAR AÇÕES COM SEGURANÇA (3a ações de exercício; 3b telas de aprovação
   e revogação)
4. CHATGPT: QUEM PODE USAR (4a tabela por plano; 4b nomenclatura da interface)
5. INTERFACE EM PORTUGUÊS (tabela: fluxo | nome pt-BR | nome en | origem)
6. CONTEXTO BRASILEIRO
7. IDEIAS DE EXERCÍCIO
   (todas [SUGESTÃO]; ao menos uma para ler arquivo, uma para consultar serviço
   e uma para executar ação reversível, cada uma com passo a passo, plano
   exigido, resultado que comprova que deu certo e como desfazer)
8. MATERIAIS PARA BAIXAR
9. PÁGINAS PARA SALVAR
10. LACUNAS E PONTOS A VERIFICAR
11. FONTES CONSULTADAS (lista numerada)

Cite a fonte de cada informação com o número dela na seção 11 (ex.: [4]).

# ANTES DE ENTREGAR, CONFIRA
[ ] Ler arquivos, consultar serviços e executar ações têm, cada um, passo a passo
    e exercício.
[ ] Nada de construção de servidor, SDK ou detalhe de protocolo.
[ ] Nenhuma elaboração sua está marcada [CONFIRMADO].
[ ] Cada arquivo declarado BAIXADO é do tipo anunciado.
[ ] Os planos do ChatGPT vieram de páginas para usuários, com data.
[ ] Os nomes de menu indicam a origem.
```
