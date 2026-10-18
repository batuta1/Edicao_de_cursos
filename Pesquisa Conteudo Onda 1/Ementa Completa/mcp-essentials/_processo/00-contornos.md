# 00 — Contornos do curso MCP - Essentials

Documento de partida compartilhado pelas duas trilhas. Tudo o que vem depois (v1.0, auditoria,
roteiros, carga horária, ementa) se apoia nestes campos.

## Origem do pedido

| Campo | Valor |
|---|---|
| Registro no catálogo | `novos-cursos-iaclube-priorizacao-v6.json` → `"id": "mcp-essentials"` |
| Nome no catálogo | MCP - Essentials |
| Onda / ranking / score | Onda 1 · ranking 2 · 97 pontos (demanda 30, ferramenta 20, base 20, lacuna 20, esforço 7) |
| Ferramentas-âncora | Claude · ChatGPT |
| Tema / linha prioritária | MCP |
| Competência | Conectar assistentes a ferramentas e dados via Model Context Protocol |
| Tarefa observável | Instalar e usar conectores MCP em Claude e ChatGPT para ler arquivos, consultar serviços e executar ações com segurança. |
| Base confiável | Documentação do protocolo; docs de Claude e OpenAI |
| Observação do catálogo | Claude Desktop ensina o app; MCP como competência nomeada não existe na oferta. |

## Objeto base

**MCP (Model Context Protocol)** — padrão aberto, anunciado pela Anthropic em 25/11/2024 e doado à
Agentic AI Foundation (Linux Foundation) em 09/12/2025, que define uma forma comum de um assistente
de IA descobrir e usar ferramentas e dados externos. Revisão estável vigente: **2026-07-28**.

O curso ensina o protocolo **pelo uso**: o aluno não programa; ele entende o que o MCP é e liga
conectores prontos em **Claude** (ferramenta principal) e **ChatGPT** (ferramenta secundária,
condicionada à conta — ver "Decisões de escopo").

## Decomposição da tarefa observável

| Ação do catálogo | Como o aluno a executa no curso | Conector |
|---|---|---|
| Instalar conector | Conector remoto personalizado no Claude (URL pública, sem login); variação no ChatGPT, se a conta exibir a opção | OpenAI Docs MCP (`https://developers.openai.com/mcp`) |
| Ler arquivos | Pasta de teste com arquivos fictícios lida pela extensão local oficial | Filesystem (Claude Desktop); alternativa web: Google Drive |
| Consultar serviços | Consulta somente leitura a documentação pública e à própria agenda | OpenAI Docs MCP; Google Calendar |
| Executar ações com segurança | Criar e apagar um evento de teste com aprovação manual; criar um rascunho de e-mail sem enviar | Google Calendar; Gmail |
| (implícito) Desfazer | Desconectar o conector e revogar o acesso no provedor | todos |

## Público-alvo

Dois públicos, vindos das trilhas em que o curso está posicionado:

| Trilha | Posição | Público |
|---|---|---|
| T3 — Agentes e MCP | 3 de 10 (antes: Agentes de IA - Essentials; depois: Claude Desktop - Essentials) | Profissionais que querem delegar tarefas de várias etapas e curiosos técnicos |
| T6 — Construindo com MCP (técnica) | 1 de 6 (primeiro curso; depois: Claude Code no VSCode - Hands On) | Desenvolvedores e equipes de TI |

Consequência de design: o curso precisa funcionar para quem **não programa**. Todo o corpo do
curso fica no nível do usuário de conectores prontos; o que interessa só a quem programa (versão
do protocolo, transporte, JSON-RPC, Inspector) vai para um **anexo técnico opcional**, fora da
carga horária.

## Pré-requisitos

- Uso básico de Claude ou ChatGPT (abrir conversa, enviar mensagem).
- Não exige saber programar.
- Uma conta Claude (o plano gratuito basta) e uma Conta Google pessoal para os exercícios de
  agenda e e-mail.

## Recursos necessários

- Computador com navegador atualizado e internet.
- **Claude Desktop** para o exercício de arquivos locais: macOS 13 ou posterior, Windows 10 ou
  posterior, Linux beta (Ubuntu 22.04+ / Debian 12+), x64 ou arm64. Há divergência entre as
  fontes sobre a versão mínima do macOS (11 × 13) — prevalece a fonte mais recente, com
  marcação [conferir]. Quem não puder instalar o aplicativo segue a alternativa web (Google Drive).
- Uma pasta de teste com dois arquivos fictícios, criada no próprio curso.
- ChatGPT: opcional. As variações em ChatGPT só são feitas se a conta exibir
  `Plugins > + > Add custom MCP server` (ou o plugin do Gmail).

## Configuração

| Campo | Valor |
|---|---|
| Autoinstrucional | **Sim.** Nenhum passo pode depender de professor. |
| Trilhas | Essentials (compreensão) e Hands-on (execução), ambas a partir deste objeto base. |
| Carga horária alvo — Essentials | 100–130 min (prompt-mestre `articulate-essentials.md`) |
| Carga horária alvo — Hands-on | 90–120 min (prompt-mestre `articulate-hands-on.md`) |
| Módulos/oficinas | Essentials: 4–6 módulos de conteúdo + síntese. Hands-on: 4 oficinas + Projeto Final. |
| Idioma | Português do Brasil; rótulos de interface que só foram confirmados em inglês aparecem em inglês, com a tradução provável entre parênteses e a marca [conferir]. |
| Plano exigido | **Claude Free basta** para todo o caminho principal (um conector personalizado no Free; conectores Google e extensões do Desktop para todos os usuários). Nenhum exercício exige pagamento. |

## Decisões de escopo

1. **Claude é o caminho principal; ChatGPT é variação condicional.** A documentação pública do
   ChatGPT não permite afirmar, plano a plano (Free, Go, Plus, Pro), quem pode adicionar um
   servidor MCP personalizado nem usar o diretório de Plugins. Ensinar o ChatGPT como caminho
   obrigatório deixaria parte dos alunos travada. O curso mostra o fluxo do ChatGPT, explica como
   reconhecer se ele está disponível e diz o que fazer se não estiver ("registrar e seguir").
2. **Requisito "plano pago" do prompt-mestre não se aplica.** O prompt `articulate-essentials.md`
   traz como requisito genérico "conta Claude com plano pago; o gratuito não habilita o recurso".
   Para conectores MCP, a ajuda oficial (17/10/2026) diz o contrário: o Free admite um conector
   personalizado, os conectores Google e as extensões do Desktop. O curso cita o requisito real.
3. **Somente leitura primeiro, escrita com aprovação manual, sempre com desfazer.** Ordem dos
   exercícios: consulta pública → leitura de arquivos fictícios → consulta à própria agenda →
   ação reversível → revogação.
4. **Dados fictícios em todos os exercícios.** Nenhum exercício usa conta corporativa, e-mail de
   trabalho, CPF, contrato ou documento real.

## Fora do escopo (outro curso cobre)

- Programar ou construir um servidor MCP → *Construindo Servidores MCP - Hands On*.
- Análise aprofundada de riscos e salvaguardas → *Segurança em MCP - Essentials* (aqui entra só o
  uso seguro básico).
- Fluxos práticos longos com conectores → *MCP com ChatGPT - Hands On* e *Claude Desktop - Hands On*.
- O conceito de agente de IA em si → *Agentes de IA - Essentials* (curso anterior na trilha T3).

Esses temas aparecem apenas para delimitar a fronteira (uma frase, nunca um passo a passo).

## Material-fonte

Pasta `Pesquisa Conteudo Onda 1/conteudo-bruto/mcp-essentials/`:

| Arquivo | Uso no curso |
|---|---|
| `ConteudoBruto_mcp-essentials.txt` | Fonte principal do protocolo: origem, governança, arquitetura, planos, fluxos Claude/ChatGPT, riscos, comparações, troubleshooting (53 referências, 17/10/2026). |
| `ConteudoBruto_mcp-essentials_complemento.txt` | Fonte do que o aluno faz: Filesystem, Google Workspace, Microsoft 365, aprovações (Always allow / Needs approval / Blocked; Allow / Deny), matriz ChatGPT por plano, rótulos pt-BR, LGPD/ANPD/Governo Digital, exemplos brasileiros (38 referências). |
| `mcp-especificacao-2026-07-28.mdx`, `mcp-changelog-2026-07-28.mdx`, `mcp-schema-2026-07-28.json` | Referência técnica para o anexo opcional; não são material para o aluno não programador. |
| `diagrama-oficial-como-mcp-funciona-google-cloud.png` | Visual de apoio para o Módulo 1 (copyright Google; manter atribuição). |
| `anpd-guia-seguranca-informacao-pequeno-porte.pdf` | Base do módulo de segurança (controle de acesso, autenticação, incidentes). |
| `anpd-radar-ia-generativa-2024.pdf` | Base da discussão de riscos de IA generativa e governança. |

Regra para dado factual: o que no conteúdo bruto está [CONFIRMADO] entra no curso com a data de
consulta; o que está [VERIFICAR], NÃO ENCONTRADO ou [SUGESTÃO] entra no máximo como formulação
genérica ou como exercício proposto, e o que for factual vai para as pendências do `README.md`.

## Alertas herdados do conteúdo bruto

1. Diretório e registro são mecanismos de descoberta, não selo de segurança. Selo "verificado"
   reduz, mas não elimina, o risco.
2. A descrição de uma ferramenta e o conteúdo que ela devolve entram no contexto do modelo e podem
   conter instruções maliciosas (*tool poisoning*, *prompt injection* indireta). O problema é
   reconhecido como aberto pelos próprios fornecedores.
3. Conector remoto do Claude é chamado a partir da nuvem da Anthropic: não alcança `localhost`,
   VPN nem rede corporativa privada.
4. Desinstalar um plugin no ChatGPT não equivale necessariamente a revogar a conexão com o serviço.
5. Nomes de menu mudaram várias vezes em 2026 (Apps → Plugins no ChatGPT; diretório unificado no
   Claude) e a ajuda nova aparece primeiro em inglês. Revisão humana obrigatória na semana da
   gravação.
