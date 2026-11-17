# 00 — Contornos do curso Gemini Chat

Documento de partida compartilhado pelas duas trilhas (Essentials e Hands-on).

## Origem do pedido

| Campo | Valor |
|---|---|
| Registro no catálogo | `gemini-chat-essentials` (Onda 2, trilha T1) |
| Prompt de pesquisa | `Pesquisa Conteudo Onda 2/05-gemini-chat-essentials.md` |
| Tema | Fundamentos de IA Generativa |
| Ferramenta-âncora | App Gemini do Google (web `gemini.google.com`, Android, iOS, desktop Windows e macOS) |
| Competência | Uso de assistente de IA para tarefas gerais |
| Tarefa observável — Essentials | Usar o Gemini para pesquisa, redação, imagem e análise de arquivos, e integrá-lo aos apps do Google |
| Tarefa observável — Hands-on | Resolver um caso completo combinando arquivos, apps do Google (Gmail, Drive, Agenda), assistente personalizado e Canvas (sugestão da equipe, confirmada aqui com troca de Gems por **habilidades**; ver abaixo) |

## Objeto base

**Gemini Chat** — o uso do app Gemini como assistente de conversa para tarefas gerais: conduzir a
conversa, proteger dados (Histórico do Gemini, chat temporário, revisão humana), personalizar
(Personalizar, memória, informações salvas, habilidades), pesquisar e redigir (busca com fontes,
verificação, Canvas), trabalhar com arquivos, imagens e apps do Google conectados.

## Mudança relevante encontrada nesta etapa: Gems → habilidades

As notas de versão oficiais (30/09/2026) anunciam as **habilidades** (*skills*) no chat — conjuntos
reutilizáveis de instruções, acionáveis com "/" ou "@" ou automaticamente — e informam que elas
**substituirão os Gems**, com migração automática. A ajuda do Google Workspace (atualizada em
09/11/2026) e a imprensa (Canaltech, 04/10/2026) indicam a descontinuação dos Gems em contas
pessoais em novembro de 2026 (os Gems migram como rascunhos inativos em "Personalizar"); em contas
de trabalho e escola, o suporte segue até 01/03/2027 e 01/06/2027. Habilidades estão disponíveis
no plano gratuito, por ora para maiores de 18 anos.

Decisão: o curso ensina **habilidades** como o recurso de assistente personalizado; Gems aparecem
apenas como nome antigo (o aluno pode encontrá-los em material de terceiros). Onde o aluno não
tiver habilidades (menor de 18, liberação ainda não concluída), o curso oferece a rota "instruções
no início da conversa".

## Público-alvo

| Trilha | Posição | Antes | Depois | Público |
|---|---|---|---|---|
| T1 — Começando com assistentes de IA | Essentials 3 de 6 | ChatGPT Chat - Essentials | Claude Chat - Hands On | Qualquer pessoa que ainda não usa IA |
| J1 — Fundamentos de IA para o jurista | 3 de 5 | ChatGPT Chat - Essentials | Claude for Legal - Essentials | Advogados, assessores, estudantes e professores de Direito |
| R1, F1, E1, S1, C1 | logo depois de ChatGPT Chat - Essentials | — | — | Demais áreas |

O Hands-on não tem posição definida em `trilhas.json`; é produzido pela regra de que toda
pesquisa gera ementa + Essentials + Hands On. O caso do Hands-on (mutirão de orientação ao cidadão)
serve ao público geral (organização de evento, servidores) e ao jurídico (orientação jurídica
gratuita).

## Pré-requisitos

- Recomendado: *Claude Chat - Essentials* e *ChatGPT Chat - Essentials*; o curso funciona para quem
  nunca usou IA.
- Conta Google **pessoal** (a conta de trabalho/escola tem termos e recursos diferentes).
- Idade: 13 anos para o app (conta pessoal); **18 anos para habilidades** e para os planos Pro e
  Ultra.
- Hands-on: ter feito o Essentials deste assunto.

## Recursos necessários

- Computador com navegador e internet (curso desenhado para `gemini.google.com`).
- Plano **gratuito** (R$ 0). Segundo a página oficial de assinaturas (pt-BR, 17/11/2026), o gratuito
  inclui geração e edição de imagens, Deep Research, Gemini Live, Canvas e Skills, com uso
  limitado; limites baseados em computação, renovados de 5 em 5 horas até um teto semanal.
- Hands-on: Gmail, Google Drive e Google Agenda da própria conta pessoal; editor de texto simples.

| Plano | Preço (BR) | Limite relativo |
|---|---|---|
| Gratuito | R$ 0 | Base |
| Google AI Plus | R$ 24,99/mês | 2× o gratuito |
| Google AI Pro | R$ 96,99/mês | 4× o gratuito (maiores de 18) |
| Google AI Ultra | a partir de R$ 779,90/mês | 5× ou 20× o Pro (maiores de 18) |

## Configuração

| Campo | Valor |
|---|---|
| Autoinstrucional | **Sim** |
| Trilhas | Essentials e Hands-on |
| Carga horária alvo | Essentials 100–130 min (4–6 módulos + síntese); Hands-on 90–120 min (4 oficinas + Projeto Final) |
| Idioma | Português do Brasil; rótulos em pt-BR |
| Plano exigido | Gratuito |

## Fora do escopo (outro curso cobre)

| Assunto | Curso | O que entra aqui |
|---|---|---|
| Gemini no Gmail, Docs, Planilhas, Meet (painel lateral) | Gemini Workspace - Essentials | Só a conexão do app Gemini com os apps do Google |
| Deep Research | Deep Research - Hands On | Onde fica e para que serve |
| NotebookLM / Gemini Notebook | NotebookLM - Essentials | Menção |
| Programação (Antigravity, Code Assist, CLI) | Gemini Code Assist | Não entra |
| Imagem e vídeo como assunto (Veo, Flow, Omni) | Imagem com IA, Vídeo com IA | Criar e editar uma imagem na conversa |
| Recursos do ChatGPT e do Claude | Cursos próprios | Tabela de comparação |
| Gemini Spark (agente), AI Studio, API | — | Não entra |

## Material-fonte

Pasta `Pesquisa Conteudo Onda 2/conteudo-bruto/gemini-chat-essentials/`:

| Arquivo | Uso |
|---|---|
| `ConteudoBruto_gemini-chat-essentials.txt` | Pesquisa parcial; base de planos, Gems, chat temporário, novidades |
| `gemini-assinaturas.html` | Planos e preços em reais; o que o gratuito inclui; idade 18+ para Pro/Ultra |
| `gemini-release-notes.html` | Personalizar e 40+ apps (13/10/2026); habilidades (30/09/2026); app Windows (10/09/2026); importação de memória e renomeação "conversas anteriores" → "memórias" (26/03/2026) |
| `ajuda-gems.html` | Passo a passo oficial dos Gems; trecho "Sobre a transição dos Gems para habilidades" |
| `blog-chat-temporario.html` | Chat temporário e contexto pessoal (13/08/2025; prazos superados pela ajuda atual) |
| `ajuda-entrar.html` | Entrar e sair |
| `google-politica-de-privacidade.html`, `google-termos-de-servico.html` | Referência geral |
| `workspace_with_gemini_prompting_guide.pdf` | Guia oficial de prompts do Google (estrutura persona, tarefa, contexto, formato) |

Complemento feito nesta etapa (17/11/2026), na web:
- Central de privacidade dos apps do Gemini (ajuda pt-BR, answer 13594961): a configuração
  chama-se **Histórico do Gemini** (antes "Atividade nos Apps do Gemini" / "Manter atividade"),
  gerida em `myactivity.google.com/product/gemini`; exclusão automática padrão de 18 meses (opções
  3 ou 36 meses, ou nunca); com o Histórico desativado, conversas futuras ficam salvas por cerca de
  2 meses; conversas lidas por revisores humanos ficam até 3 anos mesmo após exclusão; chats
  temporários ficam cerca de 2 meses e não treinam modelos; alguns apps conectados ficam
  indisponíveis com o Histórico desativado; memória gerida em `gemini.google.com/personalization-settings`
  e informações salvas em `gemini.google.com/saved-info`; aviso oficial: não inserir informação
  confidencial que não se queira ver revisada.
- Arquivos (ajuda pt-BR, answer 14903178): até 10 arquivos por comando; 100 MB por arquivo (vídeo
  até 2 GB); vídeo até 5 min e áudio até 10 min no plano padrão.
- Transição Gems → habilidades (ajuda Workspace, 09/11/2026; Canaltech, 04/10/2026).

**Regra para dado factual:** número e nome com data de consulta; rótulo de menu não visto na tela
vai para a lista de conferência do `README.md`. O blog de 2025 (72 horas de retenção) foi
superado pela ajuda atual (cerca de 2 meses) — o curso usa a ajuda atual.

## Materiais de prática (Hands-on)

Fornecidos no próprio curso, fictícios:

1. `inscricoes-mutirao.csv` — 30 inscrições (código, tema, turno, canal, acessibilidade), sem dado
   pessoal. Gabarito: Consumidor 9, Previdência 8, Família 7, Trabalho 6; tarde 18, manhã 12;
   presencial 11, site 10, WhatsApp 9; acessibilidade 4 (I03, I06, I07, I30); maior bloco
   Previdência à tarde (7). Com atendimentos de 30 min (manhã 9h–12h = 6 horários por mesa; tarde
   13h–17h = 8 horários), uma mesa por tema em cada turno basta.
2. E-mail que o aluno envia a si mesmo ("Mutirão de Orientação Cidadã — pedido da coordenação"):
   mutirão no sábado 05/12/2026, 9h–17h; reunião de preparação na quarta 02/12/2026, 15h–16h, por
   videochamada; prazo de sexta 27/11/2026 para o comunicado e a distribuição das mesas.

## Alertas herdados

1. Nomes de modelos e recursos mudam a cada poucas semanas (Gems → habilidades; "Atividade nos Apps
   do Gemini" → "Manter atividade" → "Histórico do Gemini"; "conversas anteriores" → "memórias").
2. Conectar Gmail/Drive/Agenda exige o Histórico ativado — tensão com a recomendação de privacidade,
   tratada como decisão explícita no curso.
3. A maioria dos 40+ apps conectados funciona em inglês nos EUA; no Brasil, apenas alguns. O curso
   usa só os apps do Google.
