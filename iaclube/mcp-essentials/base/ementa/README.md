# mcp-essentials

Curso **MCP - Essentials** (catálogo `novos-cursos-iaclube-priorizacao-v6.json`, Onda 1, ranking 2),
gerado com a skill `criar-ementa-curso` a partir do conteúdo bruto em
`Pesquisa Conteudo Onda 1/conteudo-bruto/mcp-essentials/`. Duas trilhas: Essentials (129 min) e
Hands-on (117 min).

## Produtos

| Arquivo | O que é |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada: identificação, objetivo, competências, trilhas, carga horária, avaliação, pendências |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Roteiro final Essentials (Módulos 0–6), com sugestões de print, objetivos e habilidades por aula; anexos de arquivos de teste, técnico (opcional) e rastreabilidade |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Roteiro final Hands-on (preparação, 4 oficinas, Projeto Final, Parte dos Dez) |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Versão Rise 360 do Essentials: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲, "Mão na massa" por módulo |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Versão Rise 360 do Hands-on: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲, três desafios por oficina |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | Tabela MET usada no cálculo (cópia da skill) |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | Breakdown por módulo: 18 atividades, 129 min, 34% teoria / 66% prática |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | Breakdown por oficina: 18 atividades, 117 min, 12% teoria / 88% prática |

## Processo (não é entregável)

| Arquivo | O que é |
|---|---|
| [_processo/00-contornos.md](_processo/00-contornos.md) | Objeto base, decomposição da tarefa observável, público, pré-requisitos, carga alvo, decisões de escopo, fronteiras, material-fonte |
| [_processo/01-v1-essentials.md](_processo/01-v1-essentials.md) | Versão 1.0 do Essentials (modelo base) |
| [_processo/01-v1-hands-on.md](_processo/01-v1-hands-on.md) | Versão 1.0 do Hands-on (modelo base) |
| [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md) | Auditoria 360 do Essentials v1.0 (nota 4/10) e matriz E1–E18 |
| [_processo/02-analise-hands-on.md](_processo/02-analise-hands-on.md) | Auditoria 360 do Hands-on v1.0 (nota 3/10) e matriz H1–H17 |

Cada achado das matrizes tem destino declarado na seção de rastreabilidade ao fim de cada roteiro final.

## Decisões de design

- **Claude é o caminho principal; ChatGPT é variação condicional.** A documentação pública da OpenAI
  não permite afirmar, plano a plano, quem pode adicionar servidor MCP personalizado. O curso mostra o
  fluxo `Plugins (ou Apps) > + > Add custom MCP server` e instrui "registrar indisponível e seguir no
  Claude".
- **Plano gratuito basta.** O requisito genérico "plano pago do Claude" do prompt-mestre
  `articulate-essentials.md` não se aplica: a ajuda oficial dá ao Free um conector personalizado,
  conectores Google e extensões do Desktop. O roteiro Rise cita o requisito real.
- **Tarefa observável decomposta em ordem de risco:** consultar (OpenAI Docs MCP, público e somente
  leitura) → ler arquivos (extensão Filesystem, uma pasta de teste; alternativa Google Drive) → agir
  (evento de teste no Google Calendar com Needs approval; rascunho no Gmail, nunca envio) → revogar.
- **Segurança antes da primeira conexão:** Módulo 2 (Essentials) e pílula do semáforo (Hands-on).
  Prompt injection praticada com um arquivo fictício que contém instrução maliciosa.
- **Fio condutor "tomada e crachá":** a analogia oficial do USB-C explica a padronização; o crachá
  explica permissões e revogação.
- **Público técnico (T6):** detalhes de versão, transporte e negociação ficam no Anexo B do roteiro
  Essentials, fora da carga horária e fora do roteiro Rise.
- **Dados fictícios em tudo;** nenhum exercício usa conta corporativa. Microsoft 365 só citado (exige
  conta Entra e administrador).

## O que não foi verificado (pendente de validação humana)

Nada foi testado numa conta real; os dados vêm do conteúdo bruto de 17/10/2026. Antes de gravar ou
publicar:

1. **Rótulos pt-BR marcados [conferir]** nos roteiros. Só estão confirmados em português
   `Personalizar > Conectores`, `Remover` e `Configurações da organização > Conectores`. A conferir:
   "Add custom connector", `Tool permissions` e Always allow / Needs approval / Blocked, Allow / Deny,
   `Settings > Extensions > Browse extensions` no Claude Desktop, Connect / Disconnect.
2. **ChatGPT por plano:** quem tem Plugins/Apps e `Add custom MCP server` (Free, Go, Plus, Pro);
   rótulo exibido (Plugins × Apps); botões de aprovação do plugin Gmail.
3. **OpenAI Docs MCP:** repetir a conexão no Claude e no ChatGPT na semana da gravação (em 17/10/2026
   o servidor declarava suporte até a revisão 2025-11-25).
4. **Extensão Filesystem:** tela de escolha das pastas, rótulo de desativar/desinstalar e se as
   aprovações por ferramenta valem para extensões locais como para conectores.
5. **Versão mínima do macOS** para o Claude Desktop: as duas pesquisas divergem (11 × 13); o curso
   usa 13.
6. **Caminho de revogação** de apps de terceiros na Conta Google.
7. **Google Calendar e Gmail no Claude:** confirmar que as ações pedem aprovação por padrão e que a
   tela de aprovação mostra convidados e fuso.
8. **Exemplos brasileiros** (Senior Sistemas, Econodata) são ilustrativos e exigem contratação; não
   foram testados. Casos de fornecedor não verificados (Grupo Soma, Sensedia) não foram usados.
9. **Diagrama do Google Cloud** (`diagrama-oficial-como-mcp-funciona-google-cloud.png`) sugerido no
   Módulo 1: copyright Google, manter atribuição e conferir os termos de uso antes de publicar.
10. **Cursos externos** citados no Encerramento (Anthropic Academy, Hugging Face): gratuidade,
    idioma e certificação não confirmados — o texto não as afirma.

## Próximos passos (fora desta skill)

Carregar no Articulate o `promptArticulate.md` do projeto + `roteiros/roteiro-articulate-<trilha>.md`
→ gerar o curso → verificação visual → exportar SCORM → revisar com a skill `revisar-curso-scorm`.
