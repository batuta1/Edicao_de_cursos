# Ementa — MCP (Model Context Protocol)

## Identificação

| Campo | Definição |
|---|---|
| Curso | MCP - Essentials (registro `mcp-essentials`, Onda 1, ranking 2) |
| Natureza | Curto, introdutório, prático e autoinstrucional |
| Trilhas | Essentials (compreensão) e Hands-on (execução) |
| Carga horária total | 246 minutos (Essentials 129 min + Hands-on 117 min) |
| Público-alvo | Profissionais que desejam delegar tarefas de várias etapas a assistentes de IA e curiosos técnicos (T3 — Agentes e MCP); desenvolvedores e equipes de TI (T6 — Construindo com MCP, primeiro curso da trilha). Desenhado para quem não programa |
| Pré-requisitos | Uso básico de Claude ou ChatGPT; nenhum conhecimento de programação; conta Claude (plano gratuito suficiente); Conta Google pessoal |
| Recursos necessários | Computador com navegador atualizado e internet; Claude Desktop (macOS 13+, Windows 10+ ou Linux beta) para a leitura de arquivos locais, com alternativa pelo navegador; ChatGPT opcional, condicionado à disponibilidade de Plugins/MCP personalizado na conta |
| Ferramentas-âncora | Claude (caminho principal) e ChatGPT (variação condicional) |
| Material-fonte | Pesquisa de conteúdo bruto de 17/10/2026 (especificação MCP 2026-07-28 e changelog; ajuda oficial da Anthropic e documentação da OpenAI; 91 referências em duas pesquisas), Lei nº 13.709/2018, guia de segurança da informação e Radar de IA generativa da ANPD, Guia de IA Generativa do Governo Digital |

## Objetivo Geral

O curso tem por finalidade capacitar o participante a compreender o Model Context Protocol — padrão
aberto que conecta assistentes de inteligência artificial a ferramentas e dados externos — e a
instalar e utilizar conectores MCP no Claude e, quando a conta o permitir, no ChatGPT, para consultar
serviços, ler arquivos e executar ações com aprovação humana, com possibilidade de desfazer e de
revogar o acesso concedido. Como produto final, o participante terá conectado um servidor remoto
público, autorizado a leitura de uma pasta de arquivos fictícios, realizado uma ação reversível na
própria agenda e elaborado, para um caso do seu perfil profissional, um plano de conexão segura que
define conector, permissões, classificação de risco e forma de revogação.

## Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Explicar o que o MCP padroniza e o que não garante, distinguindo-o de API, conector, plugin, skill
   e orquestradores de automação, e reconhecendo servidores locais e remotos.
2. Decidir, antes de instalar, se um conector pode ser ligado, com qual conta e com quais permissões,
   a partir da ficha do conector, do semáforo de risco e das referências da LGPD.
3. Instalar e utilizar conectores para consultar um serviço e ler arquivos com acesso restrito,
   conferindo a origem das respostas pela chamada de ferramenta e recusando instruções embutidas em
   conteúdo externo.
4. Executar ações com aprovação manual, conferir o resultado no serviço de origem, desfazê-las e
   desconectar e revogar os acessos concedidos.

## Estrutura das Trilhas

A trilha Essentials constrói o entendimento — o que o protocolo é, que riscos envolve e como decidir
cada conexão —, em registro formal. A trilha Hands-on exercita a execução, em oficinas de risco
crescente (consultar, ler, agir), com os mesmos conectores e os mesmos arquivos de teste. As duas
podem ser cursadas isoladamente; para o público que não programa, recomenda-se a sequência
Essentials → Hands-on. Detalhes técnicos do protocolo (versão, transporte, negociação de versão)
constam de anexo opcional do Essentials, voltado à trilha técnica e fora da carga horária.

**Essentials**

| Módulo | Título | Tempo |
|---|---|---|
| 0 | Preparação e Verificação Inicial | 7 min |
| 1 | O que é o MCP: um padrão comum entre assistentes e serviços | 25 min |
| 2 | Segurança, Permissões e Uso Responsável | 19 min |
| 3 | Primeira conexão: consultar um serviço | 20 min |
| 4 | Ler arquivos: pasta local e nuvem | 20 min |
| 5 | Executar ações com aprovação e desfazer | 20 min |
| 6 | Síntese e Aplicação Integrada | 18 min |

**Hands-on**

| Oficina | Título | Tempo |
|---|---|---|
| — | Antes de Arregaçar as Mangas (contas, pasta de teste e semáforo) | 13 min |
| 1 | Ligue seu primeiro conector | 20 min |
| 2 | Deixe o Claude ler uma pasta — só uma | 20 min |
| 3 | Consulte sua agenda sem mexer em nada | 20 min |
| 4 | Crie, confira e apague | 20 min |
| — | Projeto Final — Seu plano de conexão segura | 18 min |
| — | A Parte dos Dez | 6 min |

## Distribuição da Carga Horária

| Trilha | Atividades | Tempo | Teoria : Prática |
|---|---|---|---|
| Essentials | 18 | 129 min | 34% : 66% |
| Hands-on | 18 | 117 min | 12% : 88% |
| **Total geral** | **36** | **246 min** | **24% : 76%** |

Tempos calculados pela MET (Métrica de Estimativa de Tempo), com valores fixos por tipo de atividade,
conforme `carga-horaria/`. Ambas as trilhas estão dentro das faixas-alvo (Essentials 100–130 min;
Hands-on 90–120 min). A trilha Hands-on fica abaixo da proporção de referência de 40% de teoria, por
desenho; daí a recomendação de cursar o Essentials antes.

## Avaliação

A aprendizagem é verificada por evidência de execução, conferida no serviço de origem, e por questões
objetivas:

- **Essentials:** questões de múltipla escolha com gabarito fundamentado (Módulo 1) e análise de
  cenários pelo semáforo (Módulo 2); critérios de êxito objetivos nos Módulos 0, 3, 4 e 5 (registro
  de verificação; chamada de ferramenta e URL oficial; leitura restrita à pasta de teste, com a
  instrução maliciosa não executada; evento de teste criado, conferido e removido); atividade
  integradora do Módulo 6, avaliada por tabela de seis critérios, incluindo a revogação dos acessos.
- **Hands-on:** seção "Deu certo?" com resultado observável em cada oficina; Projeto Final em caso
  próprio, avaliado por checklist de seis itens (finalidade, ficha lida, destino das ferramentas de
  escrita, semáforo justificado, teste com dado fictício, nenhuma conexão remanescente sem motivo).

## Pendências de validação

O material-fonte é datado de 17/10/2026, e os produtos tiveram nomes e menus alterados diversas vezes
em 2026. Nada foi testado em conta real. Antes da publicação, devem ser conferidos:

1. Rótulos pt-BR da interface marcados com [conferir] nos roteiros (somente `Personalizar >
   Conectores`, `Remover` e `Configurações da organização > Conectores` estão confirmados em
   português): conector personalizado, Tool permissions e suas três opções, Allow/Deny,
   `Settings > Extensions` no Claude Desktop.
2. Elegibilidade do ChatGPT, por plano, para o diretório de Plugins e para `Add custom MCP server`, e
   se a conta exibe "Plugins" ou "Apps".
3. Funcionamento do OpenAI Docs MCP no Claude e no ChatGPT na semana da gravação (em 17/10/2026, o
   servidor declarava suporte até a revisão 2025-11-25).
4. Tela de escolha de pastas e rótulo de desinstalação da extensão Filesystem.
5. Versão mínima do macOS para o Claude Desktop (fontes indicam 11 e 13).
6. Caminho de revogação de apps de terceiros na Conta Google.
7. Comportamento das aprovações do Google Calendar e do Gmail no Claude (aprovação explícita por
   padrão) e rótulos de confirmação dos plugins correspondentes no ChatGPT.
