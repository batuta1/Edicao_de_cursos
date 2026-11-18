# Roteiro de Produção — Articulate 360
## Curso: Claude — Comece a usar o aplicativo para desktop (Essentials)

---

**Ferramenta-alvo:** Storyline 360 (principal) + Rise 360 (alternativo para versão linear)
**Público-alvo:** Docentes do ensino superior iniciantes em IA; analistas administrativos; alunos do ensino superior sem experiência prévia com ferramentas de IA
**Duração estimada:** 130 minutos (6 módulos de conteúdo + 1 módulo de síntese)
**Narração:** Locutor humano (recomendado) ou TTS
**Branching:** Não — progressão linear cumulativa
**Sistema/aplicativo referenciado:** Claude Desktop (Windows 10/11 e macOS 12+) — interfaces Chat, Code e Cowork

---

## SLIDES DE ABERTURA E NAVEGAÇÃO GERAL

---


────────────────────────────────

SLIDE 01 — ABERTURA DO CURSO
Tipo: Título
Duração estimada: 25s

────────────────────────────────

VISUAL
Fundo com textura sutil na cor institucional. Título principal em tipografia grande. Subtítulo: "Trilha Essentials — 130 minutos". Logo/ícone do Claude Desktop ao lado do título. Animação: fade-in do título (0,5s), fade-in do subtítulo (0,8s).

NARRAÇÃO
Bem-vindo ao curso Claude: Comece a usar o aplicativo para desktop — Trilha Essentials. [PAUSA]
Neste curso você vai instalar, configurar e usar o Claude Desktop de forma autônoma e segura. Você vai aprender a trabalhar com as três interfaces do aplicativo — Chat, Code e Cowork —, a formular solicitações eficazes e a adotar práticas elementares de proteção de dados. [PAUSA]
Ao final, o Claude Desktop será um recurso produtivo concreto para as suas atividades acadêmicas ou profissionais.

INTERAÇÃO
Botão "Iniciar" — avança para o Slide 02.

NAVEGAÇÃO
Restrita — botão "Próximo" da barra padrão oculto; aluno usa apenas o botão "Iniciar".


────────────────────────────────

SLIDE 02 — VISÃO GERAL DO CURSO
Tipo: Conteúdo
Duração estimada: 45s

────────────────────────────────

VISUAL
Linha do tempo horizontal com 7 etapas, cada uma com ícone distinto: monitor (M1), três abas (M2), balão de chat (M3), robô/automação (M4), pasta de arquivos (M5), lápis/revisão (M6), bandeira (M7). Abaixo da linha do tempo, seis blocos de competências a desenvolver surgindo em sequência com delay de 0,3s.

NARRAÇÃO
O curso está organizado em sete módulos em progressão cumulativa — cada módulo pressupõe os conhecimentos do anterior. [PAUSA]
No Módulo 1 você vai verificar o ambiente e instalar o Claude Desktop. No Módulo 2 você vai entender as três interfaces — Chat, Code e Cowork. No Módulo 3 vai aprofundar o uso do Chat com refinamento iterativo. No Módulo 4 vai conhecer o Cowork para delegação autônoma. No Módulo 5 vai organizar projetos e proteger dados sensíveis. No Módulo 6 vai dominar a formulação de solicitações e a revisão via diff view. E no Módulo 7 vai integrar tudo em um fluxo completo de trabalho real. [PAUSA]
Siga a ordem proposta — cada módulo é a base do seguinte.

INTERAÇÃO
Nenhuma — slide informativo.

NAVEGAÇÃO
Livre após 15 segundos (botão "Próximo" liberado com timer).

---

## MÓDULO 1 — VERIFICAÇÃO DO AMBIENTE E INSTALAÇÃO DO CLAUDE DESKTOP

---


────────────────────────────────

SLIDE 03 — ABERTURA DO MÓDULO 1
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de monitor/computador, número e título do módulo. Subtítulo: "Duração estimada: 20 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 1 — Verificação do Ambiente e Instalação do Claude Desktop. [PAUSA]
Antes de usar qualquer funcionalidade do aplicativo, é preciso confirmar que o ambiente de trabalho está em conformidade com os pré-requisitos — sistema operacional, arquitetura do processador e plano de assinatura.

INTERAÇÃO
Botão "Começar" — avança para Slide 04.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 04 — O QUE É O CLAUDE DESKTOP
Tipo: Conteúdo
Duração estimada: 35s

────────────────────────────────

VISUAL
Dois blocos contrastados lado a lado:
Esquerda — "Acesso via navegador (claude.ai)": ícone de navegador; texto: "Requer copiar e colar manualmente o conteúdo dos arquivos."
Direita — "Claude Desktop (aplicativo instalado)": ícone de aplicativo de desktop; texto: "O assistente lê e modifica diretamente arquivos armazenados no computador."; Badge "Foco deste curso".
Abaixo: nota — "Essa diferença amplia significativamente o escopo de tarefas possíveis — e exige atenção à compatibilidade e à segurança."
Animação: blocos surgem simultaneamente; note surge com delay de 0,7s.

NARRAÇÃO
O Claude Desktop é a versão em formato de aplicativo instalável do assistente Claude, desenvolvido pela Anthropic. [PAUSA]
A diferença central em relação ao acesso via navegador está na capacidade de leitura e modificação direta de arquivos armazenados no seu computador — sem necessidade de copiar e colar manualmente o conteúdo. [PAUSA]
Essa característica amplia significativamente o escopo de tarefas possíveis — e é exatamente por isso que a verificação do ambiente antes da instalação é essencial.

INTERAÇÃO
Nenhuma — slide expositivo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 05 — SISTEMAS OPERACIONAIS E ARQUITETURAS COMPATÍVEIS
Tipo: Conteúdo com instrução técnica
Duração estimada: 45s

────────────────────────────────

VISUAL
Dois blocos de sistema operacional com sub-itens:
Bloco Windows (ícone Windows): Windows 10 e 11 / Arquiteturas: x64 e ARM64 / Como verificar: Configurações > Sistema > Sobre > campo "Tipo de sistema"
Bloco macOS (ícone Apple): macOS 12 ou superior / Chips: Intel, Apple Silicon (M1, M2, M3) / Como verificar: Menu ⌘ > Sobre este Mac > campo "Chip" ou "Processador"
Caixa de alerta: "Sistemas Linux não são suportados nativamente — usuários Linux podem usar a CLI ou o acesso via navegador."
Caixa de atenção laranja: "Usar o instalador errado (ex.: x64 em processador ARM64) é a causa mais frequente de falha na inicialização do aplicativo."
Animação: blocos surgem simultaneamente; caixas de alerta em sequência após 0,8s.

[PRINT]
Nome: Tela "Configurações > Sistema > Sobre" do Windows com campo "Tipo de sistema" destacado
Caminho: Windows 10/11 > Configurações (ícone de engrenagem) > Sistema > Sobre > seção "Especificações do dispositivo" com campo "Tipo de sistema" visível
Destaque: destacar o campo "Tipo de sistema" com a arquitetura do processador (ex.: "Computador baseado em x64")
Modo: Zoom progressivo (aproximação ao campo "Tipo de sistema")

[PRINT]
Nome: Janela "Sobre este Mac" no macOS com campo "Chip" ou "Processador" destacado
Caminho: macOS > menu Apple (⌘) > Sobre este Mac > janela com campo "Chip" (Apple Silicon) ou "Processador" (Intel) visível
Destaque: destacar o campo de identificação do chip/processador
Modo: Zoom progressivo (aproximação ao campo de chip/processador)

NARRAÇÃO
O Claude Desktop é compatível com Windows 10 e 11 nas arquiteturas x64 e ARM64, e com macOS 12 ou superior tanto em processadores Intel quanto em Apple Silicon — as linhas M1, M2 e M3. [PAUSA]
Para verificar no Windows: acesse Configurações, clique em Sistema, depois em Sobre, e observe o campo "Tipo de sistema". [PAUSA]
No macOS, clique no menu Apple e em "Sobre este Mac" — o campo "Chip" ou "Processador" vai identificar a arquitetura. [PAUSA]
Atenção: usar o instalador errado é a causa mais frequente de falha na inicialização — o aplicativo simplesmente não responde ao duplo clique.

INTERAÇÃO
Nenhuma — slide de instrução técnica com prints ilustrativos.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 06 — PLANOS DE ASSINATURA: QUAL É O NECESSÁRIO?
Tipo: Conteúdo
Duração estimada: 35s

────────────────────────────────

VISUAL
Três cartões de plano lado a lado:
Cartão "Free" (fundo cinza claro): ícone ❌ — "Não inclui o Claude Desktop. A aba Code exibe mensagem 'Upgrade Required'."
Cartão "Pro / Max / Team" (fundo verde claro): ícone ✅ — "Plano mínimo necessário para o Claude Desktop." Badge "Mínimo requerido."
Cartão "Enterprise" (fundo azul claro): ícone ✅ — "Inclui Claude Desktop com recursos adicionais de segurança corporativa."
Abaixo: dica em caixa destacada — "Instituições de ensino superior podem ter acordos com a Anthropic. Consulte sua área de TI antes de adquirir um plano individual."
Como verificar: "Acesse claude.ai > faça login > localize a seção de conta ou faturamento (Billing)."
Animação: cartões surgem em sequência.

NARRAÇÃO
O acesso ao Claude Desktop requer, no mínimo, o plano Pro. O plano gratuito não inclui esse recurso — ao tentar acessar a aba Code com o plano gratuito, o aplicativo exibirá uma mensagem de atualização necessária. [PAUSA]
Para verificar o plano ativo, acesse claude.ai, faça login e localize a seção de conta ou faturamento. [PAUSA]
Uma dica importante: instituições de ensino superior podem dispor de acordos com a Anthropic que viabilizam o acesso para docentes e discentes. Consulte a área de tecnologia da informação da sua instituição antes de adquirir individualmente um plano pago.

INTERAÇÃO
Nenhuma — slide informativo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 07 — INSTALAÇÃO E PRIMEIRO LOGIN
Tipo: Conteúdo com passo a passo
Duração estimada: 45s

────────────────────────────────

VISUAL
Passo a passo numerado com 4 etapas, cada uma acompanhada de captura de tela:
1. Acessar o site oficial da Anthropic e localizar a página de download do Claude Desktop
2. Selecionar o instalador correto para a arquitetura identificada
3. Executar o instalador e aguardar a conclusão
4. Realizar o primeiro login — o aplicativo abre o navegador padrão para verificação de segurança (comportamento esperado)
Caixa de nota: "A abertura do navegador durante o login é comportamento esperado — não indica erro."
Animação: etapas surgem em sequência com delay de 0,5s.

NARRAÇÃO
Com os pré-requisitos confirmados, acesse o site oficial da Anthropic e localize a página de download do Claude Desktop. Selecione o instalador correspondente à arquitetura do processador identificada — Windows x64, Windows ARM64, macOS Intel ou macOS Apple Silicon. [PAUSA]
Execute o instalador. Após a conclusão, o aplicativo solicitará autenticação com as credenciais da sua conta Anthropic. Esse processo envolve a abertura temporária do navegador padrão para verificação adicional de segurança — trata-se de comportamento esperado e não indica nenhum erro. [PAUSA]
Concluído o login, você terá acesso às três interfaces principais do aplicativo: Chat, Code e Cowork.

INTERAÇÃO
Nenhuma — slide de instrução técnica.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 08 — VERIFICAÇÃO PÓS-INSTALAÇÃO: TRÊS INTERFACES ACESSÍVEIS
Tipo: Conteúdo
Duração estimada: 30s

────────────────────────────────

VISUAL
Print do Claude Desktop aberto e autenticado, com as três abas — Chat, Code, Cowork — visíveis na parte superior da janela. Setas indicando cada aba com rótulo curto. Caixa de critério de êxito: "As três abas estão visíveis e acessíveis. O aplicativo não exibe mensagem de erro de autenticação."

[PRINT]
Nome: Claude Desktop aberto e autenticado com as três abas Chat, Code e Cowork visíveis na parte superior da janela
Caminho: Claude Desktop > aplicativo aberto após instalação e login bem-sucedidos > janela principal com abas Chat, Code e Cowork visíveis no topo
Destaque: destacar as três abas com setas ou molduras individuais — Chat, Code e Cowork
Modo: Estática

NARRAÇÃO
Após o login, confirme a presença das três abas no topo da janela: Chat, Code e Cowork. Essa é a verificação pós-instalação mais simples e suficiente para confirmar que o aplicativo está funcionando corretamente. [PAUSA]
Se alguma das abas estiver ausente ou exibindo mensagem de erro, verifique o plano de assinatura e tente fazer logout e login novamente.

INTERAÇÃO
Nenhuma — slide de verificação com print ilustrativo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 09 — EXERCÍCIO PRÁTICO: CHECKLIST DE VERIFICAÇÃO DO AMBIENTE
Tipo: Instrução prática com checklist interativo
Duração estimada: 35s

────────────────────────────────

VISUAL
Lista de 5 itens com checkbox interativo:
☐ Sistema operacional e versão identificados
☐ Arquitetura do processador identificada (x64, ARM64, Intel ou Apple Silicon)
☐ Plano de assinatura Anthropic ativo verificado (mínimo Pro)
☐ Instalador correto baixado e instalação concluída
☐ Aplicativo aberto e autenticado — as três abas Chat, Code e Cowork estão visíveis
Barra de progresso: "Exercício 1 de 7".
Critério de êxito em destaque: "Todos os cinco itens marcados + captura de tela do aplicativo aberto com as três abas visíveis."

NARRAÇÃO
Siga os cinco itens do checklist e marque cada um conforme você o conclui. [PAUSA]
Não avance para o próximo módulo sem ter todas as cinco caixas marcadas — especialmente a última. Confirmar visualmente as três abas é a evidência de que a instalação foi bem-sucedida.

INTERAÇÃO
Checkboxes 1 a 5 — clicáveis individualmente.
Ao marcar os cinco: camada de parabéns + botão "Avançar para o Módulo 2".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os cinco checkboxes marcados.

---

## MÓDULO 2 — AS TRÊS INTERFACES DE TRABALHO: CHAT, CODE E COWORK

---


────────────────────────────────

SLIDE 10 — ABERTURA DO MÓDULO 2
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de três abas, número e título do módulo. Subtítulo: "Duração estimada: 15 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 2 — As Três Interfaces de Trabalho: Chat, Code e Cowork. [PAUSA]
Com o aplicativo instalado e autenticado, o foco desloca-se agora para a compreensão das três interfaces que organizam o Claude Desktop — determinando qual delas acionar para cada tipo de tarefa.

INTERAÇÃO
Botão "Começar" — avança para Slide 11.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 11 — AS TRÊS INTERFACES: PANORAMA
Tipo: Conteúdo interativo (três cartões clicáveis)
Duração estimada: 55s

────────────────────────────────

VISUAL
Três cartões clicáveis dispostos horizontalmente, cada um com ícone, título e síntese de uma linha:
1. Chat — ícone de balão de conversa: "Consulta e conversa — sem acesso a arquivos locais"
2. Code — ícone de código/pasta: "Trabalho colaborativo sobre arquivos reais"
3. Cowork — ícone de robô/automação: "Delegação autônoma — execução sem supervisão contínua"
Cada cartão abre layer com definição completa, exemplos de uso e uma nota sobre quando NÃO usar.
Frase síntese abaixo dos cartões: "Chat = consulta; Code = trabalho; Cowork = delegação."

NARRAÇÃO
O Claude Desktop organiza suas funções em três interfaces apresentadas como abas na parte superior da janela. Compreender a diferença entre elas é fundamental para aproveitar o potencial da ferramenta sem retrabalho. Clique nos três cartões para explorar cada uma. [PAUSA]
A aba Chat reproduz a experiência familiar do acesso via navegador — digitação e resposta em texto, sem acesso ao sistema de arquivos local. [PAUSA]
A aba Code é o diferencial central do aplicativo: com um projeto aberto, o assistente acessa todos os arquivos da pasta e propõe alterações via diff view para revisão antes de aplicar. [PAUSA]
A aba Cowork disponibiliza execução autônoma — o assistente realiza tarefas em segundo plano sem interação contínua e entrega o resultado ao final.

INTERAÇÃO
Cartão "Chat" — abre layer com:
  Definição: "Espaço de consulta e conversa. O assistente não acessa arquivos locais — toda informação deve ser digitada, colada ou anexada."
  Exemplos: "Consultas conceituais, comparações, resumos de textos colados, apoio a decisões, elaboração de textos com conteúdo fornecido na conversa."
  Quando NÃO usar: "Quando a tarefa envolve leitura ou modificação de arquivos armazenados no computador — use a aba Code."
Cartão "Code" — abre layer com:
  Definição: "Espaço de trabalho colaborativo. Com uma pasta-projeto aberta, o assistente acessa todos os arquivos de texto e propõe alterações via diff view."
  Exemplos: "Revisar e corrigir arquivos salvos localmente, criar novos arquivos, executar comandos no terminal integrado."
  Quando NÃO usar: "Quando a tarefa não envolve arquivos locais — use o Chat. Quando a tarefa é muito longa e repetitiva — considere o Cowork."
Cartão "Cowork" — abre layer com:
  Definição: "Espaço de delegação autônoma. O assistente executa tarefas em segundo plano sem solicitar aprovação a cada etapa."
  Exemplos: "Revisão de 50 documentos, geração de sumários padronizados em lote, reorganização de estrutura de arquivos."
  Quando NÃO usar: "Não recomendado para iniciantes sem base prévia no Chat e Code — a identificação de erros no resultado pressupõe compreensão do que seria o resultado correto."
Os três cartões devem ser clicados para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após clique nos três cartões.


────────────────────────────────

SLIDE 12 — CLAUDE DESKTOP VS. ACESSO VIA NAVEGADOR
Tipo: Conteúdo comparativo
Duração estimada: 35s

────────────────────────────────

VISUAL
Tabela comparativa com três linhas de capacidade e duas colunas (claude.ai via navegador vs. Claude Desktop):
1. Acesso a arquivos locais: Não (requer cópia manual) / Sim (automático, pasta-projeto)
2. Diff view para revisão de alterações: Não / Sim
3. Execução autônoma de tarefas: Não / Sim (aba Cowork)
Linha do Claude Desktop destacada. Abaixo: "Três capacidades exclusivas do aplicativo instalado."
Animação: tabela surge com fade-in; linha do Claude Desktop destaca com pulse.

NARRAÇÃO
A distinção entre o Claude Desktop e o acesso via navegador pode ser resumida em três capacidades exclusivas do aplicativo instalado. [PAUSA]
Acesso direto a arquivos locais sem cópia manual; visualização de diferenças para revisão de alterações antes de aplicá-las; e execução autônoma de tarefas pela aba Cowork. [PAUSA]
Essas três capacidades são o que torna o Claude Desktop uma ferramenta de trabalho — e não apenas de consulta.

INTERAÇÃO
Nenhuma — slide comparativo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 13 — EXERCÍCIO: MÚLTIPLA ESCOLHA — IDENTIFICAÇÃO DA INTERFACE ADEQUADA
Tipo: Questão de múltipla escolha em série (4 cenários)
Duração estimada: 55s

────────────────────────────────

VISUAL
Quatro cenários apresentados em sequência (stepper ou acordeão). Para cada cenário: enunciado + três opções (Chat / Code / Cowork) como botões de escolha. Após seleção: feedback imediato com gabarito e fundamentação. Barra de progresso: "Exercício 2 de 7".

NARRAÇÃO
Agora identifique a interface adequada para cada situação. Leia o cenário e selecione sua resposta antes de ver o gabarito.

INTERAÇÃO
Tipo: 4 questões pick-one em sequência (Storyline: série de slides de questão ou stepper com trigger)

Cenário 1: "Um docente deseja obter uma explicação sobre o conceito de inteligência artificial generativa para incluir em sua ementa."
Opções: Chat / Code / Cowork
Gabarito: Chat
Feedback: "Correto. Consulta conceitual sem arquivo local — o Chat é o espaço ideal."

Cenário 2: "Uma analista precisa que o assistente revise e corrija os termos técnicos em um relatório salvo em sua pasta de trabalho."
Opções: Chat / Code / Cowork
Gabarito: Code
Feedback: "Correto. O arquivo está armazenado localmente e precisa ser lido e modificado — tarefa para a aba Code."

Cenário 3: "Um estudante quer saber a diferença entre citação direta e indireta segundo as normas da ABNT."
Opções: Chat / Code / Cowork
Gabarito: Chat
Feedback: "Correto. Consulta conceitual sem necessidade de acesso a arquivos — Chat."

Cenário 4: "Uma coordenadora deseja que o assistente execute, de forma autônoma, a revisão de cinquenta arquivos de texto e gere um relatório consolidado ao final."
Opções: Chat / Code / Cowork
Gabarito: Cowork
Feedback: "Correto. Tarefa longa com múltiplos arquivos, adequada ao modo autônomo — Cowork. Recomendada apenas a usuários com experiência prévia no Chat e Code."

Tentativas por cenário: 2
Feedback incorreto (1ª tentativa): "Não é essa. Pense na natureza da tarefa: ela envolve arquivos locais? Exige supervisão contínua? É longa e repetitiva?"

NAVEGAÇÃO
Restrita — avanço liberado após resposta a todos os 4 cenários.


────────────────────────────────

SLIDE 14 — CHECKLIST DE CONCLUSÃO DO MÓDULO 2
Tipo: Avaliação de êxito
Duração estimada: 20s

────────────────────────────────

VISUAL
Três itens de checklist interativo:
☐ As três interfaces — Chat, Code e Cowork — compreendidas e diferenciadas
☐ Ao menos três capacidades exclusivas do Claude Desktop identificadas
☐ Exercício de identificação de interface concluído
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 3".

NARRAÇÃO
Confirme os três critérios antes de avançar. [PAUSA]
A capacidade de selecionar a interface correta reduz erros e retrabalho — e ela vai ser exercitada em todos os módulos seguintes.

INTERAÇÃO
Checkboxes 1 a 3 — clicáveis individualmente.
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 3".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os três checkboxes marcados.

---

## MÓDULO 3 — A INTERFACE CHAT: CONSULTA, ELABORAÇÃO E ITERAÇÃO

---


────────────────────────────────

SLIDE 15 — ABERTURA DO MÓDULO 3
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de balão de chat, número e título do módulo. Subtítulo: "Duração estimada: 20 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 3 — A Interface Chat: Consulta, Elaboração e Iteração. [PAUSA]
Com as três interfaces apresentadas em panorama, este módulo aprofunda o uso da aba Chat — a interface de entrada mais imediata do Claude Desktop —, explorando suas possibilidades além da pergunta simples.

INTERAÇÃO
Botão "Começar" — avança para Slide 16.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 16 — CASOS DE USO DO CHAT
Tipo: Conteúdo interativo (carrossel)
Duração estimada: 45s

────────────────────────────────

VISUAL
Carrossel com 5 cartões de casos de uso do Chat, cada um com ícone e exemplo concreto:
1. Elaboração e revisão de textos — com conteúdo fornecido na conversa
2. Síntese de documentos — texto colado ou anexado à solicitação
3. Comparação entre conceitos, abordagens ou autores
4. Apoio à tomada de decisões — análise de cenários
5. Geração de estruturas iniciais — ementas, roteiros, checklists, esboços
Setas de navegação lateral.

NARRAÇÃO
O Chat é o espaço adequado para tarefas de natureza conversacional e intelectual que não dependam de arquivos armazenados localmente. Explore os cinco casos de uso mais produtivos para o nosso público. [PAUSA]
Elaboração e revisão de textos com conteúdo fornecido na conversa; síntese de documentos cujo texto é colado ou anexado; comparação entre conceitos ou autores; apoio à tomada de decisões; e geração de estruturas iniciais que você refinará depois. [PAUSA]
Esses casos têm um denominador comum: a informação vem de você, não de arquivos locais.

INTERAÇÃO
Seta "anterior" e seta "próximo" — navegam entre os 5 cartões.
Todos os 5 devem ser visitados para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após visita aos cinco cartões.


────────────────────────────────

SLIDE 17 — A NATUREZA ITERATIVA DO CHAT
Tipo: Conteúdo com demonstração
Duração estimada: 45s

────────────────────────────────

VISUAL
Diagrama de ciclo com três setas em sequência:
1. "Solicitação inicial" → 2. "Avaliar resposta: o que faltou? (nível, tom, formato, escopo)" → 3. "Reformular com critério adicional" → (seta de retorno ao início)
Abaixo: dois exemplos de turnos de conversa em caixa de diálogo estilizada:
Turno 1 (solicitação inicial): "Elabore um parágrafo introdutório sobre avaliação formativa."
Turno 2 (refinamento): "Reescreva em registro formal e impessoal, adequado para documento acadêmico, máximo 80 palavras, sem primeira pessoa do plural."
Rótulo: "A segunda solicitação é mais precisa porque incorpora o que estava faltando na primeira."
Animação: diagrama de ciclo se constrói passo a passo; caixas de diálogo surgem em seguida.

[PRINT]
Nome: Conversa na aba Chat com ao menos dois turnos visíveis — solicitação inicial, resposta e reformulação com refinamento
Caminho: Claude Desktop > aba Chat > conversa com solicitação inicial, resposta do assistente e segunda solicitação com critério de refinamento adicionado
Destaque: destacar a diferença entre a solicitação inicial e a reformulada, evidenciando o critério adicional incorporado
Modo: Estática

NARRAÇÃO
A natureza iterativa do Chat é o aspecto mais importante — e mais negligenciado — desta interface. [PAUSA]
A primeira resposta raramente é a ideal; trata-se de um ponto de partida. O participante que avalia o que recebeu, identifica o que está faltando — nível de detalhe, tom, formato, escopo — e reformula a solicitação com essa informação adicional obtém, sistematicamente, resultados de qualidade superior. [PAUSA]
Essa capacidade de refinamento progressivo é, em essência, a competência central do uso produtivo do Chat.

INTERAÇÃO
Nenhuma — slide expositivo com demonstração visual.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 18 — LIMITAÇÕES DO CHAT: DUAS QUE IMPORTAM
Tipo: Conteúdo
Duração estimada: 35s

────────────────────────────────

VISUAL
Dois blocos de limitação com ícone de atenção:
Limitação 1 — "Sem acesso ao sistema de arquivos local": texto: "Toda informação deve ser fornecida explicitamente — digitada, colada ou anexada." Solução: "Use a aba Code quando precisar que o assistente leia ou modifique arquivos salvos."
Limitação 2 — "Sem memória entre sessões": texto: "Ao fechar e reabrir o aplicativo, o contexto da conversa anterior é perdido." Solução: "Mantenha um registro próprio das solicitações relevantes — ou transfira o trabalho em andamento para um arquivo no projeto, acessível via Code."
Animação: blocos surgem em sequência.

NARRAÇÃO
Duas limitações estruturais do Chat merecem atenção. [PAUSA]
Primeira: o assistente não acessa arquivos do computador nessa interface. Toda informação precisa ser fornecida explicitamente — digitada, colada ou anexada como arquivo. Quando a tarefa envolve arquivos locais, a aba Code é o espaço correto. [PAUSA]
Segunda: o Claude não retém memória entre sessões distintas. Ao fechar e reabrir o aplicativo, o contexto da conversa anterior é perdido. A estratégia recomendada é manter um registro próprio das solicitações mais relevantes — ou usar um arquivo no projeto, acessível via Code nas sessões seguintes.

INTERAÇÃO
Nenhuma — slide expositivo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 19 — EXERCÍCIO PRÁTICO: REFINAMENTO ITERATIVO DE SOLICITAÇÃO
Tipo: Instrução prática
Duração estimada: 40s

────────────────────────────────

VISUAL
Passo a passo de 6 etapas numeradas. Solicitação inicial em caixa de destaque. Exemplo de reformulação em caixa de destaque. Barra de progresso: "Exercício 3 de 7".

NARRAÇÃO
Este exercício simula um ciclo real de uso do Chat com duas rodadas de refinamento. [PAUSA]
Abra a aba Chat do Claude Desktop. Envie a solicitação inicial exibida na tela, substituindo o campo pelo tema da sua área. Leia a resposta e anote em uma linha o que está faltando — tom, extensão, formalidade. Envie uma segunda solicitação incorporando essa observação. Compare as duas respostas e identifique objetivamente em que aspectos a segunda é superior. [PAUSA]
O critério de êxito é demonstrar, pela comparação, que a reformulação explícita produziu resultado mensurável.

INTERAÇÃO
Botão "Ver solicitação inicial" — abre layer com o texto: "'Elabore um parágrafo introdutório sobre [tema escolhido].'"
Botão "Ver exemplo de reformulação" — abre layer com o texto: "'Reescreva o parágrafo, agora em registro formal e impessoal, adequado para um documento acadêmico, com no máximo 80 palavras. Não utilize a primeira pessoa do plural.'"
Botão "Concluí o exercício" — avança para Slide 20.

NAVEGAÇÃO
Restrita — avanço via botão "Concluí o exercício".


────────────────────────────────

SLIDE 20 — CHECKLIST DE CONCLUSÃO DO MÓDULO 3
Tipo: Avaliação de êxito
Duração estimada: 20s

────────────────────────────────

VISUAL
Três itens de checklist interativo:
☐ Casos de uso adequados ao Chat identificados
☐ Exercício de refinamento iterativo executado com ao menos dois turnos
☐ Diferença mensurável entre primeira e segunda resposta documentada
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 4".

NARRAÇÃO
Confirme os três critérios. [PAUSA]
A habilidade de refinar solicitações iterativamente vai se aplicar em todos os módulos seguintes — e é a base do uso produtivo de qualquer interface do Claude Desktop.

INTERAÇÃO
Checkboxes 1 a 3 — clicáveis individualmente.
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 4".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os três checkboxes marcados.

---

## MÓDULO 4 — A INTERFACE COWORK: DELEGAÇÃO AUTÔNOMA DE TAREFAS

---


────────────────────────────────

SLIDE 21 — ABERTURA DO MÓDULO 4
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de robô/automação, número e título do módulo. Subtítulo: "Duração estimada: 20 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 4 — A Interface Cowork: Delegação Autônoma de Tarefas. [PAUSA]
Com o Chat explorado em profundidade, este módulo apresenta a interface Cowork — o modo de operação autônoma do Claude Desktop —, enfatizando as condições necessárias para seu uso responsável.

INTERAÇÃO
Botão "Começar" — avança para Slide 22.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 22 — COMO FUNCIONA O COWORK
Tipo: Conteúdo
Duração estimada: 40s

────────────────────────────────

VISUAL
Diagrama comparativo em três linhas:

Linha 1 — Chat: "Interação contínua → aprovação explícita de cada resposta"
Linha 2 — Code: "Propõe alterações via diff view → participante revisa e aprova cada mudança"
Linha 3 — Cowork: "Executa em segundo plano → entrega resultado ao final sem aprovação intermediária"

Seta crescente de autonomia da esquerda (Chat) para a direita (Cowork). Rótulo: "Grau crescente de autonomia concedida ao assistente."
Animação: linhas surgem em sequência de baixo para cima.

NARRAÇÃO
O Cowork representa o nível mais avançado de delegação disponível no Claude Desktop. Diferentemente do Chat, onde cada resposta é aprovada pelo participante, e do Code, onde cada alteração é apresentada em diff view para revisão, o Cowork executa em segundo plano sem solicitar aprovação a cada etapa — e entrega o resultado ao final. [PAUSA]
A analogia mais precisa é a de uma instrução escrita passada a um colaborador com alto grau de autonomia: o resultado depende tanto da competência do colaborador quanto da clareza da instrução recebida.

INTERAÇÃO
Nenhuma — slide expositivo com diagrama.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 23 — TAREFAS ADEQUADAS E INADEQUADAS AO COWORK
Tipo: Conteúdo interativo (dois painéis clicáveis)
Duração estimada: 45s

────────────────────────────────

VISUAL
Dois painéis expansíveis:
Painel verde — "Adequadas ao Cowork": ícone de check. Lista: tarefas repetitivas e de longa duração; múltiplos arquivos com critério uniforme; escopo bem definido e baixo risco em caso de erro.
Exemplos: revisão padronizada de 50 documentos; geração de sumários em série; reorganização de estrutura de arquivos por critérios predefinidos.
Painel vermelho — "Inadequadas ao Cowork (use Chat ou Code)": ícone de X. Lista: tarefas que exigem julgamento caso a caso; trabalho em arquivo único com alto risco de erro; tarefas em que iniciantes não conseguiriam identificar erros no resultado.
Alerta abaixo: "Usar o Cowork sem base prévia no Chat e Code cria um risco: a identificação de erro no resultado pressupõe compreensão do que seria o resultado correto."
Ambos os painéis devem ser abertos para liberar navegação.

NARRAÇÃO
Clique nos dois painéis para identificar o que é — e o que não é — adequado ao Cowork. [PAUSA]
O Cowork é especialmente adequado para tarefas repetitivas, de longa duração ou compostas por múltiplas etapas claramente sequenciadas, com escopo bem definido e baixo risco em caso de erro. [PAUSA]
Por outro lado, tarefas que exigem julgamento caso a caso, trabalho sensível em arquivo único ou situações em que o participante ainda não se sente seguro para identificar erros no resultado devem ser feitas no Chat ou no Code — com maior supervisão.

INTERAÇÃO
Painel "Adequadas" — expande com lista completa e exemplos.
Painel "Inadequadas" — expande com lista completa e alerta sobre risco para iniciantes.
Ambos devem ser abertos para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após abertura dos dois painéis.


────────────────────────────────

SLIDE 24 — A TASK BRIEF: OS QUATRO ELEMENTOS
Tipo: Conteúdo interativo (hotspot em quatro zonas)
Duração estimada: 50s

────────────────────────────────

VISUAL
Modelo de task brief em caixa de texto com quatro zonas coloridas e clicáveis sobrepostas:
Zona 1 (azul) — Descrição da tarefa
Zona 2 (verde) — Arquivos ou fontes relevantes
Zona 3 (laranja) — Formato esperado do resultado
Zona 4 (vermelho) — Restrição explícita (o que não deve ser feito)
Cada zona abre layer com definição e exemplo preenchido.
Abaixo: critério de êxito da task brief — "Suficientemente precisa para que outra pessoa — sem conhecimento prévio do contexto — consiga executar a tarefa corretamente com base apenas nela."

NARRAÇÃO
A qualidade do resultado do Cowork é diretamente proporcional à qualidade da instrução que define a missão — a task brief. Clique em cada zona para explorar os quatro elementos que ela deve conter. [PAUSA]
Descrição da tarefa: o que deve ser feito. Arquivos ou fontes: quais recursos o assistente deve usar. Formato esperado: como o resultado deve ser entregue — extensão, estrutura, formato de arquivo. E restrição explícita: o que o assistente não deve alterar ou ultrapassar.

INTERAÇÃO
Zona 1 "Descrição" — abre layer com: Definição: "O que deve ser feito, em linguagem clara e específica." Exemplo: "Gerar um sumário padronizado de cada uma das dez atas de reunião na pasta /atas."
Zona 2 "Arquivos" — abre layer com: Definição: "Quais arquivos ou pastas o assistente deve acessar." Exemplo: "Os arquivos estão em /atas, todos com extensão .txt."
Zona 3 "Formato" — abre layer com: Definição: "Como o resultado deve ser entregue — formato, estrutura e extensão máxima." Exemplo: "Um arquivo .md por ata, com as seções: Data, Participantes, Decisões (máximo 3 itens) e Próximos Passos."
Zona 4 "Restrição" — abre layer com: Definição: "O que o assistente não deve fazer." Exemplo: "Não alterar os arquivos originais. Os sumários devem ser criados em uma nova subpasta /sumarios."
As quatro zonas devem ser clicadas para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após clique nas quatro zonas.


────────────────────────────────

SLIDE 25 — O RELATÓRIO DE EXECUÇÃO DO COWORK
Tipo: Conteúdo
Duração estimada: 35s

────────────────────────────────

VISUAL
Print ilustrativo do painel de status do Cowork com uma missão concluída, mostrando o relatório de entrega. Quatro perguntas de avaliação em lista ao lado:
1. "O que foi realizado conforme o esperado?"
2. "O que eventualmente não foi feito?"
3. "Quais ajustes são necessários para uma segunda execução?"
4. "O resultado precisaria de revisão humana adicional?"

[PRINT]
Nome: Interface do Cowork com painel de status de tarefa concluída e relatório de entrega visível
Caminho: Claude Desktop > aba Cowork > painel de status de uma missão em execução ou concluída > relatório de entrega com resumo do que foi realizado
Destaque: destacar o painel de status da tarefa e o relatório de entrega/conclusão
Modo: Estática

NARRAÇÃO
Ao final de uma execução no Cowork, o assistente entrega um relatório de execução — um resumo do que foi realizado. Sua tarefa como participante é avaliar criticamente esse relatório com quatro perguntas. [PAUSA]
O que foi realizado conforme o esperado? O que eventualmente não foi feito? Quais ajustes são necessários para uma segunda execução, se for o caso? E o resultado precisaria de revisão humana adicional? [PAUSA]
Essa avaliação crítica é o momento em que a capacidade desenvolvida nos módulos anteriores — especialmente no Chat e no Code — se mostra indispensável.

INTERAÇÃO
Nenhuma — slide expositivo com print ilustrativo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 26 — EXERCÍCIO: ELABORAÇÃO E AVALIAÇÃO DE UMA TASK BRIEF
Tipo: Instrução prática em duas partes
Duração estimada: 45s

────────────────────────────────

VISUAL
Duas partes com separador visual:
Parte 1 — "Identifique os problemas": instrução deficiente em caixa de destaque ("Revise meus documentos e me diga o que está errado.") + campo de anotação com prompt: "Liste ao menos três problemas com esta instrução."
Parte 2 — "Reescreva com os quatro elementos": cenário hipotético (pasta com dez atas em .txt, gerar sumário padronizado) + estrutura de task brief em branco com quatro campos rotulados para preenchimento. Barra de progresso: "Exercício 4 de 7".

NARRAÇÃO
Este exercício tem duas partes. [PAUSA]
Primeiro: leia a instrução deficiente exibida na tela e anote ao menos três problemas — quais documentos? qual critério de "errado"? qual formato de resposta? o que não deve ser alterado? [PAUSA]
Segundo: usando o cenário hipotético descrito, redija uma task brief completa com os quatro elementos: descrição, arquivos, formato e restrição. Ela deve ser suficientemente precisa para que outra pessoa — sem contexto — consiga executar a tarefa corretamente com base apenas nela.

INTERAÇÃO
Botão "Ver instrução deficiente" — exibe em layer: "'Revise meus documentos e me diga o que está errado.'"
Botão "Ver cenário para reescrita" — exibe em layer com o cenário das dez atas e a estrutura dos quatro campos.
Botão "Concluí o exercício" — avança para Slide 27.

NAVEGAÇÃO
Restrita — avanço via botão "Concluí o exercício".


────────────────────────────────

SLIDE 27 — CHECKLIST DE CONCLUSÃO DO MÓDULO 4
Tipo: Avaliação de êxito
Duração estimada: 20s

────────────────────────────────

VISUAL
Três itens de checklist interativo:
☐ Diferença entre Cowork, Chat e Code em grau de autonomia compreendida
☐ Categorias de tarefas adequadas e inadequadas ao Cowork identificadas
☐ Task brief com os quatro elementos elaborada para o cenário hipotético
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 5".

NARRAÇÃO
Confirme os três critérios. [PAUSA]
O uso responsável do Cowork depende diretamente da base construída no Chat e no Code — e da capacidade de avaliar criticamente o que o assistente entrega.

INTERAÇÃO
Checkboxes 1 a 3 — clicáveis individualmente.
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 5".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os três checkboxes marcados.

---

## MÓDULO 5 — ORGANIZAÇÃO DE PROJETOS E PROTEÇÃO DE DADOS

---


────────────────────────────────

SLIDE 28 — ABERTURA DO MÓDULO 5
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de pasta de arquivos, número e título do módulo. Subtítulo: "Duração estimada: 20 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 5 — Organização de Projetos e Proteção de Dados. [PAUSA]
Com as interfaces Chat e Cowork aprofundadas, este módulo desloca o foco para a configuração do ambiente de trabalho da aba Code: como estruturar uma pasta-projeto, quais arquivos o assistente pode acessar e como proteger informações sensíveis.

INTERAÇÃO
Botão "Começar" — avança para Slide 29.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 29 — A REGRA DO ESCOPO MÍNIMO
Tipo: Conteúdo
Duração estimada: 35s

────────────────────────────────

VISUAL
Diagrama de duas opções:
Opção ruim (fundo vermelho claro, ícone ❌): "Abrir a pasta do usuário completa → assistente acessa documentos pessoais, fotos e dados irrelevantes."
Opção correta (fundo verde claro, ícone ✅): "Abrir apenas a subpasta específica do projeto → assistente acessa somente o necessário."
Rótulo central: "Regra do escopo mínimo."
Animação: opções surgem simultaneamente.

NARRAÇÃO
Na aba Code do Claude Desktop, o ponto de partida é a seleção de uma pasta — denominada projeto. A partir dessa seleção, o assistente obtém acesso de leitura a todos os arquivos de texto contidos nessa pasta. [PAUSA]
A regra essencial para iniciantes é a do escopo mínimo: em vez de abrir uma pasta ampla — como a pasta de usuário do sistema operacional, que pode conter documentos pessoais e dados irrelevantes — crie e abra apenas a subpasta específica do projeto em andamento. Assim, o assistente acessa somente o que é necessário para a tarefa solicitada.

INTERAÇÃO
Nenhuma — slide expositivo com diagrama.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 30 — ESTRUTURA MÍNIMA DE UMA PASTA-PROJETO
Tipo: Conteúdo com instrução técnica
Duração estimada: 45s

────────────────────────────────

VISUAL
Representação da estrutura de arquivos em árvore:
meu-primeiro-projeto/
├── README.md       ← "Lido prioritariamente pelo assistente ao abrir o projeto"
├── .gitignore      ← "Lista arquivos a ignorar — proteção de dados sensíveis"
└── .env            ← "Credenciais — listado no .gitignore, não rastreado"
Cada arquivo com rótulo explicativo e ícone distinto. Abaixo: a função de cada arquivo em bullet points.

[PRINT]
Nome: Estrutura de pasta-projeto no explorador de arquivos mostrando README.md, .gitignore e .env
Caminho: Windows Explorer ou Finder (macOS) > pasta "meu-primeiro-projeto" aberta > arquivos README.md, .gitignore e .env visíveis na listagem
Destaque: destacar os três arquivos na estrutura de pasta com rótulos identificando cada um
Modo: Estática

NARRAÇÃO
A estrutura mínima de uma pasta-projeto compatível com o Claude Desktop inclui três arquivos. [PAUSA]
O README.md é um documento de texto simples que descreve o propósito do projeto, seu conteúdo e instruções de uso. O assistente lê esse arquivo prioritariamente ao abrir um projeto — o que permite contextualizar rapidamente o escopo do trabalho. [PAUSA]
O .gitignore especifica quais arquivos devem ser ignorados pelo sistema de controle de versão Git — e, por extensão, protegidos de compartilhamento inadvertido. [PAUSA]
E o .env isola as credenciais — senhas, chaves de API, tokens de autenticação. Ele existe no computador, mas o .gitignore garante que nunca seja rastreado nem enviado a repositórios remotos.

INTERAÇÃO
Nenhuma — slide de instrução técnica com print ilustrativo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 31 — PROTEÇÃO DE CREDENCIAIS COM .GITIGNORE
Tipo: Conteúdo de alerta
Duração estimada: 35s

────────────────────────────────

VISUAL
Dois cenários lado a lado:
Esquerda (fundo vermelho claro, ícone ❌): "Arquivo .env sem .gitignore → credenciais rastreadas → risco de exposição em repositórios remotos."
Direita (fundo verde claro, ícone ✅): "Arquivo .env listado no .gitignore → nunca rastreado → credenciais protegidas."
Conteúdo de exemplo do .gitignore em caixa monoespaçada:
  .env
  *.key
  *.pem
Definição de credencial: "Senhas de banco de dados, chaves de API, tokens de autenticação — informações que, se expostas, podem comprometer sistemas ou contas."

NARRAÇÃO
O tema das credenciais merece atenção especial. Credenciais são informações de acesso — senhas de banco de dados, chaves de API, tokens de autenticação — que, se expostas, podem comprometer sistemas inteiros. [PAUSA]
A prática recomendada é isolar as credenciais em um arquivo separado — o .env — e incluir esse arquivo na lista de exclusões do .gitignore. Assim, o arquivo existe no computador mas nunca é rastreado pelo Git nem enviado a repositórios remotos. [PAUSA]
O .gitignore mínimo recomendado inclui: .env, arquivos com extensão .key e arquivos com extensão .pem.

INTERAÇÃO
Nenhuma — slide de alerta com contraste visual.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 32 — GIT COMO REDE DE SEGURANÇA
Tipo: Conteúdo com referência técnica
Duração estimada: 45s

────────────────────────────────

VISUAL
Tabela de cinco comandos Git com descrição e uso no contexto do Claude Desktop:
git status → "Ver quais arquivos foram modificados"
git diff → "Ver exatamente o que o assistente modificou"
git add + git commit → "Aprovar e registrar mudanças no histórico"
git checkout . → "Desfazer todas as alterações desde o último commit — 'botão de desfazer' avançado"
Abaixo: nota para iniciantes: "Trate o Git inicialmente como um 'desfazer avançado': se o assistente fizer algo indesejado, git checkout . restaura todos os arquivos ao estado do último commit registrado."
Animação: linhas da tabela surgem em sequência.

NARRAÇÃO
O controle de versão com Git representa uma camada adicional de segurança no trabalho com o Claude Desktop. [PAUSA]
O Git permite que você visualize exatamente o que o assistente modificou — via git diff —, aprove as mudanças com git add e git commit, ou as descarte completamente com git checkout ponto. [PAUSA]
Para usuários sem experiência prévia em Git, o mais importante é tratar esses comandos inicialmente como uma ferramenta de "desfazer" avançada: se o assistente fizer algo indesejado, git checkout ponto restaura todos os arquivos ao estado do último commit registrado. É uma rede de segurança — e ela vale a pena configurar.

INTERAÇÃO
Nenhuma — slide de referência técnica.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 33 — EXERCÍCIO PRÁTICO: CRIAÇÃO DE ESTRUTURA MÍNIMA DE PROJETO
Tipo: Instrução prática com checklist
Duração estimada: 40s

────────────────────────────────

VISUAL
Passo a passo de 6 etapas numeradas. Conteúdo do README.md e do .gitignore em caixas de código monoespaçadas. Barra de progresso: "Exercício 5 de 7". Critério de êxito em destaque.

[PRINT]
Nome: Painel lateral da aba Code com o projeto meu-primeiro-projeto carregado — README.md e .gitignore visíveis, .env ausente da listagem de trabalho
Caminho: Claude Desktop > aba Code > projeto "meu-primeiro-projeto" aberto > painel lateral (sidebar) mostrando README.md e .gitignore mas NÃO listando o .env como arquivo de trabalho ativo
Destaque: destacar os arquivos README.md e .gitignore presentes e a ausência do .env na listagem de trabalho ativo
Modo: Estática

NARRAÇÃO
Siga os seis passos para criar a estrutura mínima de projeto. [PAUSA]
Crie a pasta meu-primeiro-projeto. Dentro dela, crie o README.md com o conteúdo exibido na tela. Crie o .gitignore com as três exclusões recomendadas. Crie o arquivo .env com a chave fictícia de exercício. Abra o Claude Desktop, acesse a aba Code, clique em Open Project e selecione a pasta. [PAUSA]
O critério de êxito: a lista de arquivos no painel lateral deve mostrar o README.md e o .gitignore — mas não o .env como arquivo de trabalho ativo.

INTERAÇÃO
Botão "Ver conteúdo do README.md" — abre layer com o texto mínimo do arquivo e botão "Copiar".
Botão "Ver conteúdo do .gitignore" — abre layer com as três linhas de exclusão e botão "Copiar".
Botão "Ver conteúdo do .env (exercício)" — abre layer com CHAVE_API=exemplo_nao_usar_em_producao e botão "Copiar".
Botão "Concluí o exercício" — avança para Slide 34.

NAVEGAÇÃO
Restrita — avanço via botão "Concluí o exercício".


────────────────────────────────

SLIDE 34 — CHECKLIST DE CONCLUSÃO DO MÓDULO 5
Tipo: Avaliação de êxito
Duração estimada: 20s

────────────────────────────────

VISUAL
Quatro itens de checklist interativo:
☐ Pasta meu-primeiro-projeto criada com README.md, .gitignore e .env
☐ Projeto aberto na aba Code — .env ausente da listagem de trabalho ativo
☐ Finalidade dos três arquivos explicada sem consulta
☐ Motivo pelo qual o .env deve estar no .gitignore compreendido
Ao marcar os quatro: camada de parabéns + botão "Avançar para o Módulo 6".

NARRAÇÃO
Confirme os quatro critérios — especialmente os dois últimos, que testam a compreensão conceitual. [PAUSA]
A organização segura do projeto é o que permite usar a aba Code com confiança e sem risco de expor dados sensíveis.

INTERAÇÃO
Checkboxes 1 a 4 — clicáveis individualmente.
Ao marcar os quatro: camada de parabéns + botão "Avançar para o Módulo 6".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os quatro checkboxes marcados.

---

## MÓDULO 6 — FORMULAÇÃO DE SOLICITAÇÕES E REVISÃO DE RESULTADOS

---


────────────────────────────────

SLIDE 35 — ABERTURA DO MÓDULO 6
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de lápis/revisão, número e título do módulo. Subtítulo: "Duração estimada: 20 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 6 — Formulação de Solicitações e Revisão de Resultados. [PAUSA]
Com o projeto estruturado e protegido, este módulo concentra-se na etapa central do uso produtivo da aba Code: como redigir solicitações que gerem resultados precisos e como revisar, aprovar ou rejeitar as alterações propostas pelo assistente.

INTERAÇÃO
Botão "Começar" — avança para Slide 36.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 36 — OS TRÊS ELEMENTOS DE UMA SOLICITAÇÃO EFICAZ
Tipo: Conteúdo interativo (hotspot em três zonas)
Duração estimada: 50s

────────────────────────────────

VISUAL
Solicitação de exemplo em caixa de código monoespaçada, com três zonas coloridas e clicáveis sobrepostas:
Zona 1 (azul) — Ação: o que deve ser feito
Zona 2 (verde) — Escopo: qual arquivo, seção ou trecho está em questão
Zona 3 (laranja) — Critérios e restrições: tom, formato, limitações a observar
Exemplo completo na caixa: "Revise o segundo parágrafo do arquivo introducao.md, corrigindo erros gramaticais e substituindo verbos no infinitivo por construções impessoais adequadas ao registro acadêmico."
Cada zona abre layer com definição e contra-exemplo.

NARRAÇÃO
Uma solicitação eficaz no Claude Desktop tende a conter três elementos. Clique em cada zona para explorar. [PAUSA]
A descrição da ação — o que deve ser feito. O escopo — qual arquivo, seção ou trecho específico está em questão. E os critérios ou restrições relevantes — tom desejado, formato de saída, limitações a observar. [PAUSA]
Não é necessário redigir solicitações longas; a precisão é mais importante que a extensão.

INTERAÇÃO
Zona 1 "Ação" — abre layer com:
  Definição: "Descreva o que o assistente deve fazer de forma clara e com verbo específico."
  Exemplo bom: "'Revise o segundo parágrafo, corrigindo erros gramaticais.'"
  Contra-exemplo: "'Melhore meu texto.' — Sem especificação da ação, o resultado será genérico."
Zona 2 "Escopo" — abre layer com:
  Definição: "Identifique qual arquivo, seção ou trecho específico está em questão."
  Exemplo bom: "'... do arquivo introducao.md...'" ou "'...a tabela da seção 3...'"
  Contra-exemplo: "'Faça um resumo.' — Sem arquivo ou trecho identificado, o assistente presume o contexto."
Zona 3 "Critérios e restrições" — abre layer com:
  Definição: "Informe o tom desejado, o formato de saída e o que não deve ser alterado."
  Exemplo bom: "'...substituindo verbos no infinitivo por construções impessoais adequadas ao registro acadêmico.'"
  Contra-exemplo: "'Verifique se há inconsistências.' — Sem critério, o assistente não sabe o que procurar."
As três zonas devem ser clicadas para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após clique nas três zonas.


────────────────────────────────

SLIDE 37 — A DIFF VIEW: REVISANDO ALTERAÇÕES ANTES DE ACEITAR
Tipo: Conteúdo com demonstração visual
Duração estimada: 50s

────────────────────────────────

VISUAL
Representação visual da diff view com dois painéis:
Painel esquerdo — conteúdo original com linhas em vermelho (sinal -): "Versão original — será removida"
Painel direito — conteúdo proposto com linhas em verde (sinal +): "Versão proposta — será inserida"
Botões "Aceitar" e "Rejeitar" visíveis.
Legenda: "Análogo ao 'controle de alterações' de processadores de texto — o arquivo original permanece intacto até você aprovar explicitamente cada mudança."

[PRINT]
Nome: Diff view do Claude Desktop com exemplo de alteração proposta — linhas removidas em vermelho e linhas adicionadas em verde
Caminho: Claude Desktop > aba Code > projeto aberto > após solicitação de alteração > diff view ativa mostrando conteúdo original (vermelho, sinal -) e conteúdo proposto (verde, sinal +) com botões de aceitar/rejeitar visíveis
Destaque: destacar as linhas vermelhas com sinal -, as linhas verdes com sinal + e os botões de aceitar e rejeitar
Modo: Estática

NARRAÇÃO
Após o assistente propor uma alteração na aba Code, o aplicativo apresenta a diff view — uma visualização que exibe, lado a lado, o conteúdo original marcado em vermelho e o conteúdo proposto marcado em verde. [PAUSA]
Trata-se de uma representação análoga ao recurso "controle de alterações" de processadores de texto — porém aplicada a qualquer tipo de arquivo de texto. [PAUSA]
O participante deve revisar essa visualização antes de aceitar qualquer modificação. Nenhuma alteração é aplicada ao arquivo enquanto você não clicar em aceitar.

INTERAÇÃO
Nenhuma — slide de demonstração com print ilustrativo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 38 — O FLUXO COMPLETO: SOLICITAR → REVISAR → REGISTRAR OU REVERTER
Tipo: Conteúdo
Duração estimada: 40s

────────────────────────────────

VISUAL
Linha do tempo com quatro passos:
1. "Solicitar" → ícone de lápis
2. "Revisar diff view" → ícone de olho
3. "Aceitar" → git add + git commit com mensagem descritiva → ícone de check verde
   "Rejeitar" → git checkout . → ícone de seta de retorno
4. "Histórico registrado no Git" → ícone de lista com commits
Caixa de dica: "Mantenha a configuração padrão do assistente ativa: ele solicita confirmação antes de aplicar alterações."
Animação: passos surgem em sequência.

NARRAÇÃO
O fluxo completo de trabalho na aba Code segue quatro passos. [PAUSA]
Você formula a solicitação. O assistente propõe alterações e você revisa na diff view. Se aceitar, registra no Git com git add e git commit com uma mensagem descritiva — criando um ponto de restauração. Se rejeitar, o comando git checkout ponto restaura todos os arquivos ao estado anterior. [PAUSA]
Uma dica: mantenha ativa a configuração padrão que faz o assistente solicitar confirmação antes de aplicar alterações. Caso o assistente inicie uma sequência de alterações que pareça inadequada, interrompa com o botão de parada disponível na interface — e reformule a solicitação com maior precisão.

INTERAÇÃO
Nenhuma — slide expositivo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 39 — EXERCÍCIO: REFINAMENTO DE SOLICITAÇÕES
Tipo: Questão de avaliação em três pares
Duração estimada: 50s

────────────────────────────────

VISUAL
Três pares de solicitações apresentados em sequência (stepper). Para cada par: as duas opções em cartões lado a lado (A e B) + botão de escolha por par + feedback com gabarito e fundamentação após a seleção. Barra de progresso: "Exercício 6 de 7".

NARRAÇÃO
Analise os três pares de solicitações e identifique, em cada par, qual é mais provável de gerar um resultado preciso.

INTERAÇÃO
Tipo: 3 questões pick-one em sequência

Par 1:
A) "Melhore meu texto."
B) "Revise o segundo parágrafo do arquivo introducao.md, corrigindo erros gramaticais e substituindo verbos no infinitivo por construções impessoais adequadas ao registro acadêmico."
Gabarito: B
Feedback: "Correto. A opção B contém ação, escopo (arquivo e parágrafo específicos) e critérios (erro gramatical, registro acadêmico)."

Par 2:
A) "Crie um resumo do documento aberto, com no máximo 150 palavras, destacando o objetivo principal e os três pontos centrais do argumento."
B) "Faça um resumo."
Gabarito: A
Feedback: "Correto. A opção A define o limite de extensão (150 palavras) e os critérios de conteúdo (objetivo principal e três pontos centrais)."

Par 3:
A) "Verifique se há inconsistências."
B) "Verifique se os dados numéricos na tabela do arquivo relatorio.md são consistentes com os valores mencionados no texto descritivo do mesmo arquivo e aponte qualquer divergência encontrada."
Gabarito: B
Feedback: "Correto. A opção B delimita o escopo (tabela vs. texto descritivo do mesmo arquivo) e descreve claramente o tipo de inconsistência a verificar."

Tentativas por par: 2
Feedback incorreto (1ª tentativa): "Reveja: qual das opções contém ação, escopo e critérios explícitos?"

NAVEGAÇÃO
Restrita — avanço liberado após resposta aos três pares.


────────────────────────────────

SLIDE 40 — CHECKLIST DE CONCLUSÃO DO MÓDULO 6
Tipo: Avaliação de êxito
Duração estimada: 20s

────────────────────────────────

VISUAL
Três itens de checklist interativo:
☐ Os três elementos de uma solicitação eficaz (ação, escopo, critérios) identificados
☐ Funcionamento da diff view compreendido — aceitar, rejeitar, registrar ou reverter
☐ Exercício de refinamento de solicitações concluído
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 7".

NARRAÇÃO
Confirme os três critérios. [PAUSA]
Você agora domina os seis elementos do fluxo de trabalho com o Claude Desktop — e está pronto para integrá-los na atividade final.

INTERAÇÃO
Checkboxes 1 a 3 — clicáveis individualmente.
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 7".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os três checkboxes marcados.

---

## MÓDULO 7 — SÍNTESE E APLICAÇÃO INTEGRADA

---


────────────────────────────────

SLIDE 41 — ABERTURA DO MÓDULO 7
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de bandeira de chegada, número e título do módulo. Subtítulo: "Duração estimada: 15 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 7 — Síntese e Aplicação Integrada. [PAUSA]
Este módulo articula, em uma atividade única, todas as competências desenvolvidas nos seis módulos anteriores. Não há conteúdo novo — o foco é a execução integrada e sequencial do fluxo completo de trabalho com o Claude Desktop.

INTERAÇÃO
Botão "Começar" — avança para Slide 42.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 42 — O FIO CONDUTOR DO CURSO
Tipo: Conteúdo — síntese conceitual
Duração estimada: 35s

────────────────────────────────

VISUAL
Diagrama de dois polos:
Polo esquerdo (PARTICIPANTE): "Compreende o que solicita → revisa o que recebe → decide o que aprova"
Polo direito (CLAUDE DESKTOP): "Amplifica a capacidade de trabalho"
Seta bidirecional com rótulo: "Colaboração crítica"
Abaixo: frase em destaque — "A produtividade genuína emerge não da delegação irrefletida, mas da colaboração crítica entre o participante e o assistente."
Animação: polos surgem com fade-in; seta aparece por último.

NARRAÇÃO
Antes de executar a atividade integradora, vale retomar o fio condutor percorrido ao longo do curso. [PAUSA]
O Claude Desktop é, em essência, uma ferramenta de amplificação: seu valor está diretamente ligado à qualidade das instruções fornecidas e à capacidade de revisar criticamente os resultados. [PAUSA]
Um assistente de inteligência artificial não substitui o julgamento profissional ou acadêmico do participante — ao contrário, potencializa a produtividade quando o participante sabe exatamente o que deseja, como solicitá-lo e como avaliar o que foi entregue.

INTERAÇÃO
Nenhuma — slide de síntese conceitual.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 43 — ATIVIDADE INTEGRADORA: SETE ETAPAS
Tipo: Instrução prática com stepper
Duração estimada: 55s

────────────────────────────────

VISUAL
Stepper vertical com 7 etapas numeradas, cada uma com referência ao módulo de origem e instrução objetiva:
Etapa 1 — Verificação do ambiente (M1): abrir o Claude Desktop, confirmar autenticação e abas; anotar versão via Help > About
Etapa 2 — Escolha da interface (M2): descrever a tarefa em um parágrafo e justificar a interface adequada para cada parte
Etapa 3 — Elaboração via Chat com refinamento (M3): solicitação inicial + ao menos um refinamento + comparação das respostas
Etapa 4 — Avaliação do Cowork (M4): task brief hipotética de duas a quatro frases para a parte adequada ao Cowork
Etapa 5 — Organização do projeto (M5): confirmar .gitignore presente; .env não aparece como ativo; git status limpo
Etapa 6 — Solicitação eficaz e revisão (M6): solicitação na aba Code + revisão da diff view + aceitar + git commit com mensagem descritiva
Etapa 7 — Verificação final: git log com ao menos um commit registrado + captura de tela
Barra de progresso: "Exercício 7 de 7".

[PRINT]
Nome: Histórico do Git (git log) ao final da atividade integradora mostrando ao menos dois commits registrados
Caminho: Terminal integrado do Claude Desktop (aba Code) ou terminal do sistema operacional > dentro da pasta meu-primeiro-projeto > comando git log executado > histórico com ao menos dois commits visíveis
Destaque: destacar os commits registrados com suas mensagens descritivas
Modo: Estática

NARRAÇÃO
Execute as sete etapas em sequência. Para cada uma, registre uma captura de tela como evidência. [PAUSA]
Etapa 1: verifique o ambiente e anote a versão do aplicativo. Etapa 2: defina a tarefa e justifique as interfaces. Etapa 3: use o Chat com ao menos um refinamento. Etapa 4: elabore uma task brief hipotética para o Cowork. Etapa 5: confirme que o projeto está organizado e o repositório limpo. Etapa 6: solicite uma edição na aba Code, revise a diff view, aceite e registre o commit. Etapa 7: execute git log e confirme o histórico. [PAUSA]
A recomendação final: ao terminar, retorne ao Chat e use o prompt de reflexão orientada para planejar o próximo projeto real com o Claude Desktop.

INTERAÇÃO
Cada etapa do stepper — expande com instrução detalhada e, quando aplicável, botão de acesso ao prompt correspondente.
Botão "Ver prompt de reflexão orientada" — abre layer com o prompt base integrador do Módulo 7 (Mão na massa) e botão "Copiar".
Botão "Concluí as sete etapas" — avança para Slide 44.

NAVEGAÇÃO
Restrita — avanço via botão "Concluí as sete etapas".


────────────────────────────────

SLIDE 44 — CHECKLIST DE AVALIAÇÃO FINAL
Tipo: Avaliação de conclusão
Duração estimada: 40s

────────────────────────────────

VISUAL
Tabela de 9 critérios com checkbox interativo:
☐ O aplicativo está autenticado e as três interfaces estão acessíveis
☐ A justificativa de escolha de interfaces (Etapa 2) está documentada
☐ A solicitação no Chat foi refinada com ao menos um critério adicional e as duas respostas foram comparadas
☐ Uma task brief hipotética para o Cowork foi elaborada com os quatro elementos recomendados
☐ O projeto aberto na aba Code possui README.md e .gitignore
☐ O arquivo .env está protegido (não aparece como arquivo de trabalho ativo)
☐ A diff view foi revisada antes da aceitação das alterações
☐ O commit com mensagem descritiva foi registrado no histórico do Git
☐ As capturas de tela documentam cada etapa realizada
Ao marcar os nove: camada de parabéns + botão "Avançar para o encerramento".

NARRAÇÃO
Confirme os nove critérios de avaliação. [PAUSA]
O atendimento a todos eles evidencia que você percorreu o fluxo completo de trabalho com o Claude Desktop — da verificação do ambiente à revisão e registro de uma alteração real em um projeto. [PAUSA]
Se algum critério não puder ser marcado, retorne ao módulo correspondente e complete a etapa.

INTERAÇÃO
Checkboxes 1 a 9 — clicáveis individualmente.
Ao marcar todos os 9: camada de parabéns + botão "Avançar para o encerramento".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os nove checkboxes marcados.

---

## SLIDE DE ENCERRAMENTO

---


────────────────────────────────

SLIDE 45 — ENCERRAMENTO DO CURSO
Tipo: Encerramento
Duração estimada: 60s

────────────────────────────────

VISUAL
Fundo com identidade visual do Slide 01. Título: "Parabéns — você concluiu a Trilha Essentials." Ícone de conquista animado. Síntese em destaque tipográfico: "O Claude Desktop é uma ferramenta de amplificação — amplifica o entendimento de quem compreende o que solicita e revisa o que recebe." Abaixo: quatro blocos de aprofundamento com ícones:
1. Arquivo .claude.md — regras e preferências persistentes por projeto
2. Cowork para automação de tarefas repetitivas
3. Integração com IDEs como VS Code e PyCharm
4. Módulos de Nível 2 — casos avançados e servidores MCP
Animação: título e síntese surgem primeiro; blocos em sequência com delay.

NARRAÇÃO
Você concluiu o curso Claude: Comece a usar o aplicativo para desktop — Trilha Essentials. [PAUSA]
Ao longo dos sete módulos, você verificou e configurou o ambiente, compreendeu as três interfaces, aprofundou o uso do Chat com refinamento iterativo, aprendeu a delegar tarefas ao Cowork de forma responsável, organizou projetos com proteção de dados e dominou o fluxo de solicitações com revisão pela diff view e registro no Git. [PAUSA]
Recomenda-se a prática regular dessas competências em projetos concretos — a familiaridade com qualquer ferramenta digital aprofunda-se com o uso continuado. Cada sessão de trabalho oferece oportunidades de refinamento das solicitações e de expansão do repertório de casos de uso. [PAUSA]
Para quem quiser avançar além dos fundamentos, quatro frentes estão indicadas na tela: o arquivo .claude.md para regras persistentes por projeto; o Cowork para automação de tarefas repetitivas; a integração com IDEs como VS Code e PyCharm; e os Módulos de Nível 2 do material-fonte, que incluem o uso de servidores MCP para expansão das capacidades do assistente. [PAUSA]
Bom trabalho.

INTERAÇÃO
Botão "Reiniciar o curso" — retorna ao Slide 01 (opcional).
Botão "Sair" — encerra o módulo e registra conclusão no LMS (trigger: Complete Course / passed).

NAVEGAÇÃO
Livre — slide final.

---

---

# TABELA GERAL DE ASSETS

| Tipo | Descrição | Slide de uso |
|------|-----------|:------------:|
| Diagrama animado | Dois blocos: acesso via navegador (cópia manual) vs. Claude Desktop (acesso direto a arquivos) | 04 |
| Diagrama animado | Dois blocos: abrir pasta ampla (❌) vs. pasta específica do projeto (✅) — regra do escopo mínimo | 29 |
| Diagrama animado | Dois blocos: .env sem .gitignore (❌) vs. .env listado no .gitignore (✅) | 31 |
| Diagrama animado | Dois polos: PARTICIPANTE ↔ CLAUDE DESKTOP — colaboração crítica | 42 |
| Diagrama animado | Linha do tempo: Solicitar → Revisar diff → Aceitar/Rejeitar → Registrar/Reverter | 38 |
| Diagrama animado | Três linhas: Chat (interação contínua) / Code (diff view) / Cowork (autônomo) com seta de autonomia crescente | 22 |
| Diagrama animado | Diagrama de ciclo: Solicitação → Avaliar → Reformular → (repetir) | 17 |
| Tabela | Comparação: claude.ai via navegador vs. Claude Desktop (3 capacidades exclusivas) | 12 |
| Tabela | Cinco comandos Git com descrição e uso no contexto do Claude Desktop | 32 |
| Árvore de arquivos | Estrutura mínima de pasta-projeto: README.md, .gitignore, .env | 30 |
| Ícone | Monitor/computador (Módulo 1) | 03 |
| Ícone | Três abas (Módulo 2) | 10 |
| Ícone | Balão de chat (Módulo 3) | 15 |
| Ícone | Robô/automação (Módulo 4) | 21 |
| Ícone | Pasta de arquivos (Módulo 5) | 28 |
| Ícone | Lápis/revisão (Módulo 6) | 35 |
| Ícone | Bandeira de chegada (Módulo 7) | 41 |
| Ícone | Conquista/medalha | 44, 45 |
| Fonte monoespaçada | Conteúdo de README.md, .gitignore, .env; comandos Git; solicitações de exemplo | 30, 31, 32, 33, 36 |
| Áudio | Narração completa (45 slides) — locutor ou TTS | Todos |

---

# TABELA DE CAPTURAS DE TELA

| Tipo | Descrição da tela | Caminho no sistema | Modo de exibição | Slide | Responsável |
|------|-------------------|--------------------|:----------------:|:-----:|-------------|
| Captura de tela | Configurações > Sistema > Sobre (Windows) com campo "Tipo de sistema" destacado | Windows 10/11 > Configurações > Sistema > Sobre > campo "Tipo de sistema" | Zoom progressivo (aproximação ao campo) | 05 | Equipe de conteúdo |
| Captura de tela | Janela "Sobre este Mac" (macOS) com campo "Chip" ou "Processador" destacado | macOS > menu Apple (⌘) > Sobre este Mac > campo de identificação do chip/processador | Zoom progressivo (aproximação ao campo) | 05 | Equipe de conteúdo |
| Captura de tela | Claude Desktop aberto e autenticado com as três abas Chat, Code e Cowork visíveis | Claude Desktop > aplicativo aberto após instalação e login > janela principal com três abas no topo | Estática | 08 | Equipe de conteúdo |
| Captura de tela | Aba Code com projeto aberto no painel lateral e área de chat ao centro | Claude Desktop > aba Code > projeto aberto no painel lateral (sidebar) esquerdo + área de interação ao centro | Estática | 11 (layer do cartão Code) | Equipe de conteúdo |
| Captura de tela | Conversa na aba Chat com dois turnos — solicitação inicial, resposta e reformulação com refinamento | Claude Desktop > aba Chat > conversa com turno inicial, resposta e segundo turno com critério adicional | Estática | 17 | Equipe de conteúdo |
| Captura de tela | Interface do Cowork com painel de status de tarefa concluída e relatório de entrega | Claude Desktop > aba Cowork > painel de status de missão concluída com relatório de entrega | Estática | 25 | Equipe de conteúdo |
| Captura de tela | Estrutura de pasta-projeto no explorador de arquivos com README.md, .gitignore e .env | Windows Explorer ou Finder (macOS) > pasta meu-primeiro-projeto com os três arquivos na listagem | Estática | 30 | Equipe de conteúdo |
| Captura de tela | Painel lateral da aba Code com projeto carregado — README.md e .gitignore visíveis, .env ausente | Claude Desktop > aba Code > projeto meu-primeiro-projeto > painel lateral sem o .env listado como ativo | Estática | 33 | Equipe de conteúdo |
| Captura de tela | Diff view com alteração proposta — linhas vermelhas (-) e linhas verdes (+) com botões aceitar/rejeitar | Claude Desktop > aba Code > diff view ativa após solicitação de alteração | Estática | 37 | Equipe de conteúdo |
| Captura de tela | Histórico do Git (git log) com ao menos dois commits registrados | Terminal integrado (aba Code) ou terminal do SO > pasta meu-primeiro-projeto > git log executado | Estática | 43, 44 | Participante (autogerado durante atividade) |
