# Contornos do curso — Agentes de IA no n8n

## Objeto base

Agentes de IA no n8n: arquitetura, configuração, uso de ferramentas, memória, RAG, controles de segurança, teste e auditoria.

## Público-alvo

Profissionais de operações, produto, atendimento, dados e áreas administrativas que desejam compreender e construir automações com agentes de IA, sem exigir experiência prévia com n8n.

## Pré-requisitos

- Familiaridade básica com navegador e serviços web.
- Para a trilha Hands-on: instância n8n Cloud ou self-hosted, acesso a um modelo compatível com tool calling e permissão para criar workflows.
- Arquivo curto, público e não sigiloso para a atividade de RAG.
- Não é necessário conhecimento de programação.

## Recursos necessários

- Computador com navegador e internet.
- n8n 2.46.6 ou interface equivalente, em inglês.
- Créditos do n8n AI Gateway ou credencial de provedor de modelo.
- Credencial de teste para uma ferramenta de ação, quando disponível.

## Configuração pedagógica

| Campo | Definição |
|---|---|
| Formato | Autoinstrucional e assíncrono |
| Trilhas | Essentials e Hands-on |
| Essentials | 5 módulos, 115 minutos |
| Hands-on | 4 oficinas + Projeto Final, 105 minutos |
| Material-fonte | Pasta `Pesquisa Conteudo Onda 1/conteudo-bruto/n8n-agentes-de-ia-essentials-6/` |
| Versão de referência | n8n 2.46.6, consultada em 05/11/2026 |

## Fronteiras

Entram no curso: workflow, Chat Trigger, AI Agent/Tools Agent, Chat Model, tools, Simple Memory, RAG, Structured Output Parser, Guardrails, human review, executions e avaliação básica.

Ficam fora do escopo: instalação e administração de ambiente self-hosted, código avançado, queue mode, arquitetura multiagente, desenvolvimento de nós, MCP em profundidade e recursos autônomos em preview.

## Decisões de design

- O Essentials ensina a decidir e avaliar, sem pedir operação externa ao Rise.
- O Hands-on constrói o workflow em camadas e usa uma ação simulada quando não houver credencial de aplicativo.
- A segurança aparece antes da publicação: menor privilégio, separação de sessão, validação, aprovação humana e revisão de execuções.
- Menus e rótulos permanecem em inglês, como na documentação oficial.
- Valores de planos e modelos não integram os exercícios porque mudam rapidamente.

## Pontos a validar antes da publicação

1. Confirmar os rótulos e caminhos na conta Cloud usada para gravação.
2. Confirmar o modelo disponível, suporte a tool calling e política de dados do provedor escolhido.
3. Verificar se a conta oferece Guardrails e human review nos mesmos pontos descritos.
4. Revalidar preços, planos, limites e recursos em preview.
5. Testar Hosted Chat, memória de sessão, vector store e execução da ferramenta em computador e celular.

