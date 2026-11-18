# agentes-de-ia-essentials

Curso **Agentes de IA - Essentials** (catálogo `novos-cursos-iaclube-priorizacao-v6.json`, Onda 1,
ranking 4), gerado com a skill `criar-ementa-curso` a partir do conteúdo bruto em
`Pesquisa Conteudo Onda 1/conteudo-bruto/agentes-de-ia-essentials/`. Duas trilhas: Essentials
(129 min) e Hands-on (115 min).

## Produtos

| Arquivo | O que é |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada: identificação, objetivo, competências, trilhas, carga horária, avaliação, pendências |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Roteiro final Essentials (Módulos 0–6), com sugestões de print, objetivos e habilidades por aula, Anexos A–D |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Roteiro final Hands-on (preparação, 4 oficinas, Projeto Final, Parte dos Dez, anexos) |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Versão Rise 360 do Essentials: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲, "Mão na massa" por módulo |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Versão Rise 360 do Hands-on: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲ |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | Tabela MET usada no cálculo (cópia da skill) |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | Breakdown por módulo: 18 atividades, 129 min, 39% teoria / 61% prática |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | Breakdown por oficina: 19 atividades, 115 min, 23% teoria / 77% prática |

## Processo (não é entregável)

| Arquivo | O que é |
|---|---|
| [_processo/00-contornos.md](_processo/00-contornos.md) | Objeto base, público, pré-requisitos, carga alvo, fronteiras, material-fonte, rótulos, alertas |
| [_processo/01-v1-essentials.md](_processo/01-v1-essentials.md) | Versão 1.0 do Essentials (modelo base) |
| [_processo/01-v1-hands-on.md](_processo/01-v1-hands-on.md) | Versão 1.0 do Hands-on (modelo base) |
| [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md) | Auditoria 360 do Essentials v1.0 (nota 3,5/10) e matriz E1–E20 |
| [_processo/02-analise-hands-on.md](_processo/02-analise-hands-on.md) | Auditoria 360 do Hands-on v1.0 (nota 3/10) e matriz H1–H16 |

Cada achado das matrizes tem destino declarado na seção de rastreabilidade ao fim de cada roteiro final.

## Decisões de design

- **Competência, não ferramenta:** o curso ensina o ciclo de delegar (risco → ordem de serviço →
  acompanhar → conferir → limites), com ChatGPT Work, Claude Cowork e Manus como exemplos.
- **Manus gratuito como caminho principal:** é o único dos três com experiência de agente sem
  assinatura (Work exige Plus; Cowork exige Pro). Rotas alternativas para assinantes em cada atividade.
- **"Modo agente" do ChatGPT só como nome histórico:** a ajuda pt-BR diz que ele "não está mais
  disponível"; a v1.0 ensinava `/agent` e foi corrigida.
- **Fio condutor:** o agente como assistente recém-contratado que recebe uma ordem de serviço (fórmula
  O-F-L-C-P), apenas as chaves necessárias (menor privilégio) e presta contas (diário de bordo).
- **Segurança antes da primeira delegação:** Módulo 2 (Essentials) com fórmula de risco, modos de
  aprovação, injeção de prompt com o caso STJ (02/09/2026) e a Recomendação 001/2024/CFOAB.
- **Documento-âncora curto e público:** Guia de IA generativa do TCU (7 p.), para caber nos créditos
  diários; atividade final por perfil (CGU para escritório; OAB para jurídico).
- **Arquivo-isca sintético** (`nota_fornecedor.txt`, endereço fictício `exemplo.com`) para praticar a
  detecção de injeção de prompt sem risco real.
- **"Terminou ≠ correto"** sustentado por avaliações independentes (Princeton HAL; 2025 AI Agent
  Index), com a ressalva de que não medem os produtos comerciais.
- **Fora do escopo, só como fronteira:** multiagentes, agentes de navegador, Cowork detalhado, n8n,
  MCP, "dots", API/SDK.

## O que não foi verificado (pendente de validação humana)

Nada foi testado numa conta real; os rótulos vêm das centrais de ajuda consultadas em 18/10/2026.
Antes de gravar ou publicar:

1. **Tela do Manus gratuito:** nome exato do seletor de modo (Agent/Agent Mode), do seletor de modelo
   (Manus 2.0 Lite), botão de anexo, onde aparece o saldo de créditos, painel do computador do agente,
   botão de assumir o controle; idioma da interface (a ajuda pt-BR mistura português e inglês).
2. **Consumo de créditos:** quanto custam as tarefas das Oficinas 1–4 e do Projeto Final no Manus 2.0
   Lite; se cabem em 300 créditos/dia (a recomendação de dividir em dois dias parte dessa incerteza).
3. **Arquivo `.txt` no Manus:** se o anexo é aceito; o roteiro oferece PDF como alternativa [conferir].
4. **ChatGPT Work:** seletor Chat/Work numa conta Plus brasileira; rótulos de autorização ("Permitir uma
   vez") e caminho `Configurações > Navegador na nuvem`; liberação gradual.
5. **Claude Cowork:** se a conta mostra Chat/Cowork separados ou a experiência unificada; rótulos de
   aprovação em português; caminho `Configurações > Cowork`.
6. **Manus — "Meu Computador" no plano gratuito:** não esclarecido pela ajuda; o curso não depende dele.
7. **Links:** reabrir os PDFs do TCU, da CGU e da OAB e a notícia do STJ (testados em 18/10/2026).
8. **Números de avaliações independentes** (HAL Princeton 35–42%; AI Agent Index 25/30): envelhecem
   rápido; reconferir na semana de publicação.
9. **Preços e planos:** valores em dólar das páginas oficiais; nenhum preço em reais publicado.
10. **System cards:** reconferir se OpenAI, Anthropic ou Manus publicaram relatório específico do Work,
    do Cowork ou do Agent Mode depois de 18/10/2026.

## Próximos passos (fora desta skill)

Carregar no Articulate o `promptArticulate.md` do projeto + `roteiros/roteiro-articulate-<trilha>.md`
→ gerar o curso → verificação visual → exportar SCORM → revisar com a skill `revisar-curso-scorm`.
