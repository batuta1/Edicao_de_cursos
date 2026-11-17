# 02 — Análise crítica 360: ChatGPT Chat Essentials v1.0

Objeto base: ChatGPT Chat · Público: iniciantes (T1), juristas (J1) e demais áreas · Trilha: Essentials.

## 1. Sumário Executivo

**Nota: 4/10.** A v1.0 tem a estrutura do modelo e o registro formal, mas é uma lista de recursos,
não um curso. Principais constatações:

- Privacidade e dados não aparecem em nenhum módulo — e o Módulo 2 já manda o aluno pedir ao
  ChatGPT que memorize preferências e enviar arquivos.
- Não há Módulo 0: plano, conta e interface são pressupostos; o aluno do plano Free não sabe o que
  vai ou não conseguir fazer.
- Exercícios sem passos ("abra as configurações", "crie um projeto") e com critérios não
  verificáveis ("as três tarefas concluídas").
- Alucinação é citada em uma frase e nunca retomada; a verificação de respostas — tarefa central
  para o público jurídico — não tem exercício.
- Faltam a subseção "Mão na massa" e os 100–130 min exigidos pelo prompt-mestre.

## 2. Pontos Positivos

- Progressão "pedido → continuidade → recursos → comparação" é lógica e cumulativa.
- O Módulo 1 parte do contraste pedido vago × estruturado: é a alavanca de maior retorno para quem
  nunca usou IA.
- A comparação com o Claude está presente, o que respeita a posição do curso na T1 (vem depois de
  Claude Chat - Essentials).
- O registro é formal e impessoal, sem 2ª pessoa.

## 3. Pontos Negativos e Gargalos

**Clareza pedagógica**
- Módulo 2 junta três recursos (instruções, memória, projetos) em 3 frases; o aluno não sabe a
  diferença entre memória e instruções personalizadas, nem quando usar chat temporário.
- Módulo 3 empilha busca, arquivos, voz e imagem sem critério de quando usar cada um.
- Exercício do Módulo 1 usa "Fale sobre contratos" — bom para o jurista, estranho para os demais.
- Atividade integradora ("uma tarefa do próprio trabalho") é aberta demais para autoinstrucional e
  convida o aluno a colar dados reais de trabalho.

**Rigor técnico**
- Nenhum caminho de menu. Segundo a ajuda oficial (resumos, 17/11/2026): memória em
  `Configurações > Personalização > Memória`; treino em `Configurações > Controles de dados >
  Melhorar o modelo para todos`; chat temporário no botão "Temporário" de um chat novo.
- Limites do Free não aparecem: uploads, análise de dados, imagem e voz são "limitados"; Projetos
  no Free aceita 5 arquivos (25 no Go/Plus). Exercícios que pedem PDF + imagem + projeto + voz
  podem esbarrar no limite diário sem aviso.
- Seletor de modelos (resposta rápida × raciocínio) não é explicado; os nomes mudaram várias vezes
  em 2026 — ensinar a lógica, não o nome.
- Nada sobre chat temporário (retido por até 30 dias, não cria memória, não treina).

**Segurança e permissões (risco crítico)**
- Sem módulo de dados antes do primeiro uso real. Para J1: sigilo profissional e dados de
  clientes; para todos: LGPD e dados de terceiros.
- Diferença conta pessoal × Business/Enterprise/Edu (estas não treinam por padrão) ausente.

**Engajamento**
- Tom adequado, mas textos curtos demais para Essentials (1 parágrafo por módulo; o modelo pede
  3–5).

**Potencial oculto**
- Ficaram de fora: editar mensagem e regenerar, Canvas, Modo Estudo, análise de dados, memória do
  projeto, chat temporário personalizável e o mapa de "outros recursos" (pesquisa aprofundada,
  tarefas agendadas, GPTs, apps/plugins, Codex) com o curso que aprofunda cada um.

**Aderência ao público**
- Nada avançado demais; o problema é o contrário — superficialidade.

## 4. Matriz de Soluções e Melhorias

| # | Gargalo | Onde | Correção concreta | Prioridade |
|---|---|---|---|---|
| E1 | Sem pré-requisito, plano e interface | Antes do M1 | Criar **Módulo 0** com conta Free, tabela "o que o Free faz" (página de preços, 17/11/2026) e mapa da tela (barra lateral, caixa de mensagem, "+", seletor) | Alta |
| E2 | Privacidade ausente | Entre M1 e personalização | Criar **Módulo 2 — Dados, privacidade e sigilo** com "Melhorar o modelo para todos", chat temporário (30 dias), exportar/excluir, semáforo de dados e variação jurídica | Alta |
| E3 | Alucinação sem retomada | M1 → busca | Plantar alucinação no M1 e retomá-la no módulo de busca com exercício "conferir uma resposta na fonte" | Alta |
| E4 | Exercícios sem passos | Todos | Reescrever com passos numerados, caminho de menu e critério observável | Alta |
| E5 | Limites do Free | M3/M5 | Avisar o limite antes de cada exercício com upload/imagem/voz e dar rota alternativa (colar texto; voz opcional no celular) | Alta |
| E6 | Memória × instruções × projeto confusos | M3 | Tabela comparativa "o que guarda, onde fica, como apagar" + chat temporário | Média |
| E7 | Seletor de modelos | M1 | Explicar "resposta rápida × raciocínio" sem nomes de modelo; ponto de controle no seletor | Média |
| E8 | Recursos empilhados | M3 da v1 | Separar em dois módulos: **Busca e verificação** e **Arquivos, voz, imagem e Canvas** | Média |
| E9 | Mapa de outros recursos | M5 | Tabela "o que é / onde fica / curso que aprofunda" (pesquisa aprofundada, tarefas agendadas, GPTs, plugins/apps, Codex, Modo Estudo) | Média |
| E10 | Integradora aberta e com risco de dados reais | Síntese | Tarefa fixa e fictícia (dois perfis: geral e jurídico), mesma tarefa no Claude, tabela de critérios | Alta |
| E11 | Comparação sem fonte | M4 | Tabela de simetria ChatGPT × Claude com nome do recurso em cada uma; levar para a Síntese, onde a comparação acontece de fato | Média |
| E12 | Falta "Mão na massa" e carga 100–130 | Todos | Acrescentar prompt-base editável por módulo; redistribuir tempos | Alta |
| E13 | Exemplo só jurídico | M1 | Exemplo neutro + variação jurídica | Baixa |

## 5. Roadmap de Expansão

**Cabem neste curso:** editar/regenerar (M1); Modo Estudo (citação no M5); memória do projeto e
chat temporário personalizável (M3); Canvas (M5); análise de dados básica (M5).

**Ficam para outros cursos:** criação de GPTs (GPTs e Ferramentas do ChatGPT), pesquisa
aprofundada (Deep Research - Hands On), modo agente e Atlas (Agentes Web), plugins/apps e MCP
(MCP com ChatGPT), Codex (ChatGPT CODEX), Sites e tarefas agendadas (fora do Free; citados só no
mapa).

**Não verificado:** nomes exatos de menus pt-BR na tela atual (ajuda da OpenAI bloqueada para
leitura direta; dados vêm de resumos de busca); preço em reais.
