# Roteiro de Produção — Articulate 360
## Curso: Plataformas e Integrações — Use o Claude Code no VS Code (Essentials)

---

**Ferramenta-alvo:** Storyline 360 (principal) + Rise 360 (alternativo para versão linear)
**Público-alvo:** Docentes do ensino superior iniciantes em IA; analistas administrativos; alunos de graduação e pós-graduação sem experiência prévia com IA aplicada ao código
**Duração estimada:** 90 minutos (4 módulos de conteúdo + 1 módulo de síntese)
**Narração:** Locutor humano (recomendado) ou TTS
**Branching:** Não — progressão linear cumulativa
**Sistema/aplicativo referenciado:** VS Code (Visual Studio Code, versão 1.95.0+) + extensão Claude Code (Anthropic Inc.) + console.anthropic.com

---

## SLIDES DE ABERTURA E NAVEGAÇÃO GERAL

---


────────────────────────────────

SLIDE 01 — ABERTURA DO CURSO
Tipo: Título
Duração estimada: 25s

────────────────────────────────

VISUAL
Fundo com textura sutil na cor institucional. Título principal em tipografia grande. Subtítulo: "Trilha Essentials — 90 minutos". Ícone de raio ⚡ (símbolo do Claude Code) ao lado do título. Animação: fade-in do título (0,5s), fade-in do subtítulo (0,8s).

NARRAÇÃO
Bem-vindo ao curso Plataformas e Integrações: Use o Claude Code no VS Code — Trilha Essentials. [PAUSA]
Neste curso você vai instalar, configurar e usar a extensão Claude Code no editor VS Code para tarefas concretas do seu cotidiano acadêmico ou profissional: análise e explicação de código, refatoração orientada a revisão, geração de documentação e depuração. [PAUSA]
E em cada etapa, você vai aprender a fazer isso com segurança — protegendo seus dados e mantendo o controle de cada decisão.

INTERAÇÃO
Botão "Iniciar" — avança para o Slide 02.

NAVEGAÇÃO
Restrita — botão "Próximo" da barra padrão oculto; aluno usa apenas o botão "Iniciar".


────────────────────────────────

SLIDE 02 — VISÃO GERAL DO CURSO E COMPETÊNCIAS
Tipo: Conteúdo
Duração estimada: 40s

────────────────────────────────

VISUAL
Linha do tempo horizontal com 5 etapas com ícone distinto: globo/ecossistema (M1), engrenagem (M2), balão de prompt (M3), diff/comparação (M4), bandeira de chegada (M5). Abaixo, quatro blocos de competências surgindo em sequência com delay de 0,3s.

NARRAÇÃO
O curso está organizado em cinco módulos em progressão cumulativa — cada módulo apoia-se no anterior. [PAUSA]
No Módulo 1 você vai compreender o ecossistema Claude e os limites de segurança da extensão.
No Módulo 2 você vai instalar a extensão e configurar sua chave de API com segurança.
No Módulo 3 você vai aprender a formular prompts contextualizados referenciando arquivos abertos.
No Módulo 4 você vai executar o ciclo de refatoração assistida usando o diff viewer.
E no Módulo 5 você vai integrar tudo em um fluxo completo — do código problemático ao código documentado. [PAUSA]
Siga a sequência proposta: cada módulo pressupõe o anterior.

INTERAÇÃO
Nenhuma — slide informativo.

NAVEGAÇÃO
Livre após 12 segundos (botão "Próximo" liberado com timer).

---

## MÓDULO 1 — O ECOSSISTEMA CLAUDE: O QUE É, O QUE MUDA E O QUE NÃO SAI DA SUA MÁQUINA

---


────────────────────────────────

SLIDE 03 — ABERTURA DO MÓDULO 1
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de globo/ecossistema, número e título do módulo. Subtítulo: "Duração estimada: 20 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 1 — O Ecossistema Claude: o que é, o que muda e o que não sai da sua máquina. [PAUSA]
Antes de instalar qualquer ferramenta, convém compreender o que ela é, como ela se encaixa no fluxo de trabalho e quais são seus limites de segurança — o fundamento que sustenta todos os módulos seguintes.

INTERAÇÃO
Botão "Começar" — avança para Slide 04.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 04 — O QUE É O CLAUDE E COMO ACESSÁ-LO
Tipo: Conteúdo
Duração estimada: 40s

────────────────────────────────

VISUAL
Três cartões lado a lado, cada um representando um modo de acesso ao Claude:
1. Interface Web — ícone de navegador: "claude.ai — qualquer navegador"
2. Extensão VS Code — ícone de VS Code + raio ⚡: "Claude Code — painel integrado ao editor" — Badge "Foco deste curso"
3. CLI (Linha de Comando) — ícone de terminal: "claude — usos avançados e automação"
Animação: cartões surgem em sequência com delay de 0,4s; badge no cartão 2 surge com pulse.

NARRAÇÃO
O Claude é um assistente de inteligência artificial desenvolvido pela Anthropic, capaz de compreender linguagem natural e responder a perguntas, gerar texto, analisar problemas e auxiliar na escrita e revisão de código. [PAUSA]
Ele pode ser acessado de três formas: pela interface web, que funciona em qualquer navegador; pela extensão Claude Code instalada diretamente no VS Code — o foco deste curso; e pela ferramenta de linha de comando, destinada a usos mais avançados. [PAUSA]
O VS Code — Visual Studio Code — é um editor de código-fonte da Microsoft amplamente usado por programadores e analistas de dados. O Claude Code é uma extensão — um pequeno programa adicional — que integra o assistente diretamente a esse ambiente.

INTERAÇÃO
Nenhuma — slide expositivo com três cartões.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 05 — A VANTAGEM DO CONTEXTO AUTOMÁTICO
Tipo: Conteúdo com analogia
Duração estimada: 45s

────────────────────────────────

VISUAL
Dois cenários animados lado a lado:
Esquerda — "Interface Web": ícone de pessoa colando texto manualmente + balão de fala: "Preciso copiar e colar o código a cada pergunta."
Direita — "Extensão VS Code": ícone de pessoa ao lado de uma tela compartilhada + balão de fala: "O assistente já vê o arquivo aberto."
Abaixo: analogia em caixa destacada — "É como a diferença entre explicar um problema a alguém que está ao seu lado olhando para a mesma tela e explicar o mesmo problema por escrito a alguém que nunca viu o material."
Animação: cenários surgem simultaneamente; caixa de analogia com fade-in após 0,8s.

NARRAÇÃO
A principal vantagem da extensão sobre a interface web está no contexto automático. [PAUSA]
Quando você formula uma pergunta no painel do Claude Code, o assistente pode ver o conteúdo do arquivo que está aberto no editor — e até os trechos que você selecionou. Na interface web, esse contexto precisaria ser copiado e colado manualmente a cada interação, o que é mais trabalhoso e propenso a erros. [PAUSA]
A analogia mais direta: é como a diferença entre explicar um problema a alguém que está ao seu lado olhando para a mesma tela — e explicar o mesmo problema por escrito a alguém que nunca viu o material.

INTERAÇÃO
Nenhuma — slide expositivo com contraste visual.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 06 — TABELA COMPARATIVA: TRÊS MODOS DE ACESSO
Tipo: Conteúdo de referência
Duração estimada: 40s

────────────────────────────────

VISUAL
Tabela comparativa com 4 linhas de aspecto e 3 colunas de modo (Interface Web, Extensão VS Code, CLI). Cada célula com ícone de ✅ ou ❌ ou texto curto. Linha da extensão VS Code destacada com borda colorida. Abaixo: legenda resumida — quando usar cada modo.
Animação: tabela surge com fade-in; linha da extensão destaca com pulse após 0,5s.

NARRAÇÃO
Esta tabela resume as diferenças entre os três modos de acesso e orienta a escolha conforme o tipo de tarefa. [PAUSA]
A interface web é ideal para perguntas teóricas e brainstorming — não acessa arquivos locais diretamente. A extensão VS Code é ideal para trabalho em projeto ativo — acessa automaticamente os arquivos abertos. E a CLI é indicada para automação e scripts — acessa arquivos pelo caminho completo. [PAUSA]
Guarde essa distinção: ela vai aparecer no exercício deste módulo.

INTERAÇÃO
Nenhuma — slide de referência.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 07 — MODELO DE SEGURANÇA: O QUE SAI E O QUE FICA
Tipo: Conteúdo interativo (dois painéis clicáveis)
Duração estimada: 50s

────────────────────────────────

VISUAL
Diagrama central: ícone de computador do usuário ↔ seta bidirecional ↔ ícone de nuvem (servidores Anthropic).
Dois painéis clicáveis abaixo do diagrama:
Painel esquerdo — "O que é enviado aos servidores" (ícone de seta para cima, fundo neutro)
Painel direito — "O que permanece na sua máquina" (ícone de cadeado, fundo verde claro)
Seta da nuvem para o computador destacada em vermelho com rótulo: "Processamento remoto".
Animação: diagrama surge com fade-in; painéis aparecem em sequência.

NARRAÇÃO
É essencial compreender o modelo de segurança da extensão. [PAUSA]
Quando você formula uma pergunta, o texto desse prompt e o conteúdo dos arquivos referenciados são enviados aos servidores da Anthropic para processamento — da mesma forma que ocorre ao enviar um e-mail pela internet. [PAUSA]
Clique nos dois painéis para ver exatamente o que vai e o que fica.

INTERAÇÃO
Painel "O que é enviado" — abre layer com lista:
  - Texto do prompt digitado pelo usuário
  - Conteúdo do arquivo aberto no editor
  - Trechos de código selecionados
  Nota: "Trate esses dados como se fossem enviados por e-mail — revise antes de enviar."
Painel "O que permanece na máquina" — abre layer com lista:
  - Chave de API (armazenada pelo sistema operacional — gerenciador de credenciais)
  - Histórico de conversas (salvo na pasta ~/.anthropic/ localmente)
  - Arquivos fechados e não mencionados no prompt
  - Demais arquivos do projeto não abertos
  Nota: "Sua chave de API nunca trafega pela rede durante o uso normal da extensão."
Ambos os painéis devem ser clicados para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após clique nos dois painéis.


────────────────────────────────

SLIDE 08 — O QUE JAMAIS DEVE SER ENVIADO AO ASSISTENTE
Tipo: Conteúdo de alerta
Duração estimada: 35s

────────────────────────────────

VISUAL
Ícone de escudo com X vermelho. Lista em dois blocos:
Bloco "Nunca enviar" (fundo vermelho claro): senhas e tokens de autenticação, chaves de API de terceiros, números de documentos pessoais (CPF, RG), dados financeiros, informações cobertas por LGPD/GDPR.
Bloco "Requer anonimização prévia" (fundo laranja claro): logs com e-mails ou IDs de usuários reais, dados de clientes em exemplos de código.
Abaixo: regra objetiva em destaque — "Antes de enviar: removeria isso de um e-mail enviado a um desconhecido? Se sim, não envie ao assistente."
Animação: ícone de escudo com pulse ao entrar; blocos surgem em sequência.

NARRAÇÃO
Determinadas categorias de informação jamais devem ser incluídas em prompts enviados ao assistente. [PAUSA]
Senhas, tokens de autenticação, chaves de API de terceiros, números de documentos pessoais, dados financeiros e qualquer informação coberta por legislações de proteção de dados como a LGPD brasileira ou o GDPR europeu — nunca envie. [PAUSA]
Logs com e-mails ou IDs de usuários reais requerem anonimização prévia antes do envio. [PAUSA]
A regra prática é simples: antes de enviar, pergunte-se — removeria isso de um e-mail enviado a um desconhecido? Se a resposta for sim, não envie ao assistente.

INTERAÇÃO
Nenhuma — slide de alerta.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 09 — EXERCÍCIO: CLASSIFICAÇÃO DE DADOS
Tipo: Questão de classificação interativa (drag-and-drop)
Duração estimada: 60s

────────────────────────────────

VISUAL
Seis cartões arrastáveis com os itens do exercício. Três zonas de destino: "✅ Seguro", "⚠️ Atenção", "❌ Nunca enviar". Layout limpo com instruções no topo. Barra de progresso: "Exercício 1 de 5".

NARRAÇÃO
Agora classifique cada item. Arraste cada cartão para a categoria correta. [PAUSA]
Lembre-se das três categorias: Seguro — pode ser enviado ao assistente sem modificação; Atenção — requer anonimização prévia; Nunca enviar — proibido em qualquer circunstância.

INTERAÇÃO
Tipo: Drag-and-drop (Storyline: freeform drag-and-drop question)
Cartões e gabaritos:
1. "Trecho de código Python que calcula a média de uma lista de números inteiros." → ✅ Seguro
2. "Log com endereço de e-mail de cliente: KeyError: 'user@empresa.com.br'" → ⚠️ Atenção
3. "Senha de banco de dados: db_password = 'minha_senha_secreta_123'" → ❌ Nunca enviar
4. "Função JavaScript que valida o formato de um CEP." → ✅ Seguro
5. "Número de CPF em constante de teste: CPF = '123.456.789-00'" → ❌ Nunca enviar
6. "Estrutura de pastas de um projeto sem dados sensíveis." → ✅ Seguro
Tentativas: 2
Critério de êxito: acertar ao menos 5 das 6, obrigatoriamente incluindo os itens 3 e 5 como "Nunca enviar".
Feedback correto: "Excelente! Você identificou corretamente os dados que protegem sua segurança e a dos seus usuários."
Feedback parcial (1ª tentativa com erro em 3 ou 5): "Atenção: os itens 3 e 5 contêm credenciais e dados pessoais protegidos por lei — sempre classificados como 'Nunca enviar'. Tente novamente."
Feedback após 2ª tentativa: exibe gabarito completo com justificativa por item.

NAVEGAÇÃO
Restrita — avanço liberado após submissão (independente de acerto total).


────────────────────────────────

SLIDE 10 — CHECKLIST DE CONCLUSÃO DO MÓDULO 1
Tipo: Avaliação de êxito
Duração estimada: 20s

────────────────────────────────

VISUAL
Três itens de checklist interativo:
☐ Diferença entre os três modos de acesso ao Claude compreendida
☐ O que é enviado aos servidores e o que permanece na máquina identificado
☐ Exercício de classificação de dados concluído
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 2".

NARRAÇÃO
Confirme os três critérios antes de avançar. [PAUSA]
O entendimento do modelo de segurança é a base de todo o uso responsável da extensão — ele vai aparecer em todos os módulos seguintes.

INTERAÇÃO
Checkboxes 1 a 3 — clicáveis individualmente.
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 2".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os três checkboxes marcados.

---

## MÓDULO 2 — INSTALAÇÃO E CONFIGURAÇÃO DA EXTENSÃO CLAUDE CODE NO VS CODE

---


────────────────────────────────

SLIDE 11 — ABERTURA DO MÓDULO 2
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de engrenagem, número e título do módulo. Subtítulo: "Duração estimada: 20 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 2 — Instalação e Configuração da Extensão Claude Code no VS Code. [PAUSA]
Agora que você compreende o que é o Claude Code e seus limites de segurança, vamos instalar a extensão e configurar a chave de API — etapas técnicas sem as quais nenhuma interação com o assistente é possível.

INTERAÇÃO
Botão "Começar" — avança para Slide 12.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 12 — VERIFICAÇÃO DO AMBIENTE: PRÉ-REQUISITOS
Tipo: Conteúdo com instrução técnica
Duração estimada: 40s

────────────────────────────────

VISUAL
Lista de verificação em dois blocos:
Bloco 1 — "Verificar versão do VS Code": instrução com caminho Help → About (Windows/Linux) ou Code → About (macOS). Print ilustrativo da janela de informações com versão destacada.
Bloco 2 — "Máquina pessoal ou institucional?": caixa de alerta — "Em máquinas de laboratório ou corporativas pode haver restrições de instalação de extensões ou bloqueios de firewall para api.anthropic.com. Consulte a equipe de TI antes de prosseguir."
Animação: blocos surgem em sequência.

[PRINT]
Nome: Janela "About VS Code" exibindo número da versão instalada
Caminho: VS Code > menu Help > About (Windows/Linux) ou Code > About (macOS) > janela de informações com número da versão destacado
Destaque: destacar o número da versão (deve ser 1.95.0 ou superior)
Modo: Zoom progressivo (aproximação ao número da versão)

NARRAÇÃO
Antes de instalar qualquer coisa, verifique o ambiente. [PAUSA]
O VS Code deve estar na versão 1.95.0 ou superior. Para confirmar, acesse o menu Help → About no Windows ou Linux, ou Code → About no macOS, e observe o número exibido. [PAUSA]
Se a versão for inferior, atualize gratuitamente pelo site oficial antes de prosseguir. [PAUSA]
E se você estiver usando uma máquina de laboratório ou corporativa: pode haver restrições de instalação ou bloqueios de firewall. Consulte sua equipe de TI antes de avançar.

INTERAÇÃO
Nenhuma — slide de instrução técnica com print ilustrativo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 13 — INSTALAÇÃO DA EXTENSÃO NO MARKETPLACE
Tipo: Conteúdo com passo a passo
Duração estimada: 50s

────────────────────────────────

VISUAL
Passo a passo numerado com 4 etapas, cada uma acompanhada de captura de tela correspondente:
1. Abrir painel de extensões (Ctrl+Shift+X / Cmd+Shift+X)
2. Pesquisar "claude code" no campo de busca
3. Localizar a extensão publicada pela "Anthropic Inc." e clicar em Install
4. Aguardar carregamento e recarregar janela se solicitado (Developer: Reload Window via Ctrl+Shift+P)
Animação: cada passo surge com delay de 0,5s.

[PRINT]
Nome: Painel de extensões do VS Code com resultado da busca por "claude code" — extensão da Anthropic Inc. destacada com botão Install
Caminho: VS Code > ícone de extensões na barra lateral (ou Ctrl+Shift+X) > campo de busca com "claude code" digitado > resultado mostrando extensão "Claude Code" publicada por "Anthropic Inc." com botão Install
Destaque: destacar o nome do publicador "Anthropic Inc." e o botão "Install" para diferenciar da extensão oficial de versões não oficiais
Modo: Zoom progressivo (aproximação ao resultado da busca com nome do publicador)

NARRAÇÃO
A instalação é feita diretamente no painel de extensões do VS Code. [PAUSA]
Abra o painel com o atalho Ctrl+Shift+X no Windows e Linux, ou Cmd+Shift+X no macOS. No campo de pesquisa, digite "claude code". [PAUSA]
Atenção: localize a extensão publicada pela Anthropic Inc. — esse detalhe é importante para evitar a instalação de versões não oficiais. Clique em Install e aguarde entre 30 e 60 segundos. [PAUSA]
Se o editor solicitar o recarregamento da janela, use o comando Developer: Reload Window pela Paleta de Comandos com Ctrl+Shift+P.

INTERAÇÃO
Nenhuma — slide de passo a passo com prints ilustrativos.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 14 — GERAÇÃO E INSERÇÃO DA CHAVE DE API
Tipo: Conteúdo com passo a passo
Duração estimada: 55s

────────────────────────────────

VISUAL
Passo a passo de 4 etapas em dois grupos visuais:
Grupo A — "No console da Anthropic (console.anthropic.com)":
  1. Acessar a seção API Keys
  2. Clicar em Create API Key e atribuir nome descritivo (ex.: "VS Code — Máquina Pessoal")
  3. Copiar a chave imediatamente — ela é exibida apenas uma vez
Grupo B — "No VS Code":
  4. Clicar no ícone de raio ⚡ na barra lateral esquerda (ou executar Claude Code: Sign In pela Paleta de Comandos) → colar a chave no campo de diálogo
Caixa de alerta vermelho abaixo: "JAMAIS insira a chave de API em arquivos de código ou de configuração versionados pelo Git."
Animação: grupos A e B surgem em sequência; caixa de alerta surge com pulse.

[PRINT]
Nome: Caixa de diálogo de inserção da chave de API após o comando "Claude Code: Sign In"
Caminho: VS Code > ícone de raio ⚡ na barra lateral OU Paleta de Comandos (Ctrl+Shift+P) > "Claude Code: Sign In" > caixa de diálogo com campo de texto para colagem da chave de API
Destaque: destacar o campo de entrada da chave de API e o rótulo da caixa de diálogo
Modo: Estática

NARRAÇÃO
Após a instalação, é necessário vincular a extensão à sua conta Anthropic por meio de uma chave de API — uma sequência alfanumérica única que funciona como credencial de acesso ao serviço. [PAUSA]
No console da Anthropic em console.anthropic.com, acesse a seção API Keys, clique em Create API Key, atribua um nome descritivo e copie a chave imediatamente — ela é exibida apenas uma vez pela plataforma. [PAUSA]
De volta ao VS Code, clique no ícone de raio na barra lateral ou execute o comando Claude Code: Sign In pela Paleta de Comandos. Cole a chave no campo de diálogo que aparece. O sistema operacional armazenará a credencial de forma segura — sem que a chave precise ser escrita em nenhum arquivo do projeto. [PAUSA]
E o alerta mais importante: jamais insira a chave de API em arquivos de código ou de configuração versionados pelo Git. Adicione sempre o arquivo .env ao .gitignore.

INTERAÇÃO
Nenhuma — slide de instrução técnica com prints ilustrativos.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 15 — A REGRA DO .GITIGNORE
Tipo: Conteúdo de alerta
Duração estimada: 30s

────────────────────────────────

VISUAL
Dois cenários lado a lado:
Esquerda (fundo vermelho claro, ícone ❌): "Arquivo .env com a chave adicionado ao repositório Git → chave exposta publicamente → uso indevido + cobranças inesperadas."
Direita (fundo verde claro, ícone ✅): "Arquivo .env listado no .gitignore → nunca incluído em um commit → chave protegida."
Código de exemplo em caixa monoespaçada: ".gitignore contém: .env"
Animação: cenários surgem simultaneamente com fade-in.

NARRAÇÃO
Este slide merece atenção especial, mesmo que você não trabalhe com repositórios Git no momento. [PAUSA]
Um arquivo .env contendo sua chave de API, se adicionado ao repositório, expõe a credencial publicamente — o que pode resultar em uso indevido por terceiros e em cobranças inesperadas na sua conta Anthropic. [PAUSA]
A prática correta é adicionar o arquivo .env ao arquivo .gitignore do projeto, garantindo que ele nunca seja incluído em um commit.

INTERAÇÃO
Nenhuma — slide de alerta com contraste visual.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 16 — EXERCÍCIO PRÁTICO: VERIFICAÇÃO DE AMBIENTE E INSTALAÇÃO
Tipo: Instrução prática com checklist
Duração estimada: 40s

────────────────────────────────

VISUAL
Lista numerada com 7 passos do exercício, cada um com caixa de verificação clicável. Barra de progresso: "Exercício 2 de 5". Critério de êxito em destaque: "O assistente responde à pergunta do passo 7 sem exibir erro de autenticação. O ícone ⚡ aparece na barra lateral esquerda do VS Code."

[PRINT]
Nome: VS Code com painel Claude Code aberto mostrando resposta à pergunta "Hello Claude! What is 2+2?"
Caminho: VS Code > painel Claude Code aberto > campo de entrada com "Hello Claude! What is 2+2?" digitado ou resposta já recebida visível no painel
Destaque: destacar o ícone de raio ⚡ na barra lateral e a resposta do assistente no painel, confirmando autenticação bem-sucedida
Modo: Estática

NARRAÇÃO
Siga os sete passos do exercício para verificar e completar a instalação. [PAUSA]
O critério de êxito é simples: o ícone de raio deve aparecer na barra lateral esquerda do VS Code, e ao enviar a pergunta "Hello Claude! What is 2+2?" no painel, o assistente deve responder sem exibir mensagem de erro de autenticação. [PAUSA]
Marque cada passo conforme conclui.

INTERAÇÃO
Checkboxes interativos para cada um dos 7 passos.
Ao marcar todos os 7: botão "Concluí a instalação" liberado → avança para Slide 17.

NAVEGAÇÃO
Restrita — avanço via botão "Concluí a instalação", liberado após marcar os 7 passos.


────────────────────────────────

SLIDE 17 — CHECKLIST DE CONCLUSÃO DO MÓDULO 2
Tipo: Avaliação de êxito
Duração estimada: 20s

────────────────────────────────

VISUAL
Três itens de checklist interativo:
☐ VS Code na versão 1.95.0 ou superior confirmado
☐ Extensão Claude Code da Anthropic Inc. instalada
☐ Chave de API configurada e resposta de teste recebida (ícone ⚡ visível)
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 3".

NARRAÇÃO
Confirme os três critérios. [PAUSA]
Se o assistente retornou uma mensagem de erro de autenticação, verifique se a chave foi copiada corretamente e se está dentro do prazo de validade no console da Anthropic.

INTERAÇÃO
Checkboxes 1 a 3 — clicáveis individualmente.
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 3".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os três checkboxes marcados.

---

## MÓDULO 3 — PRIMEIRAS INTERAÇÕES: COMO FORMULAR PROMPTS COM CONTEXTO DE ARQUIVO

---


────────────────────────────────

SLIDE 18 — ABERTURA DO MÓDULO 3
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de balão de prompt, número e título do módulo. Subtítulo: "Duração estimada: 20 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 3 — Primeiras Interações: como formular prompts com contexto de arquivo. [PAUSA]
Com a extensão instalada e funcionando, o foco se desloca agora para o uso produtivo da ferramenta — especificamente, para a arte de formular perguntas que levem o assistente a fornecer respostas úteis e precisas.

INTERAÇÃO
Botão "Começar" — avança para Slide 19.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 19 — O QUE É UM PROMPT E POR QUE ELE IMPORTA
Tipo: Conteúdo com analogia
Duração estimada: 40s

────────────────────────────────

VISUAL
Definição em destaque tipográfico: "Prompt = o texto que você digita no campo de entrada do assistente."
Analogia médica em caixa de destaque: "Sintomas vagos → diagnóstico vago. Sintomas descritos com precisão → avaliação precisa."
Equação visual: "Prompt preciso e contextualizado → resposta útil e específica."
Animação: definição surge primeiro; analogia com fade-in; equação por último.

NARRAÇÃO
Um prompt é o texto que você digita no campo de entrada do assistente — é a pergunta ou instrução que orienta o Claude sobre o que se deseja obter. [PAUSA]
A qualidade da resposta depende diretamente da qualidade do prompt. A analogia com uma consulta médica esclarece bem: se o paciente descreve os sintomas de forma vaga, o diagnóstico será igualmente vago. Se os descreve com precisão, a avaliação pode ser muito mais precisa. [PAUSA]
A habilidade de formular bons prompts é tão relevante quanto qualquer habilidade técnica de programação — e ela é transferível para qualquer tipo de tarefa que você queira realizar com o assistente.

INTERAÇÃO
Nenhuma — slide expositivo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 20 — TRÊS ELEMENTOS DE UM BOM PROMPT NO CLAUDE CODE
Tipo: Conteúdo interativo (hotspot em três zonas)
Duração estimada: 55s

────────────────────────────────

VISUAL
Prompt de exemplo exibido em caixa de código monoespaçada, com três zonas coloridas e clicáveis sobrepostas ao texto, cada uma destacando um elemento:
Zona 1 (azul) — "Identificar o elemento" → destaca a parte que nomeia a função e o arquivo
Zona 2 (verde) — "Descrever comportamento atual e esperado" → destaca a parte que descreve o que a função faz e o cenário problemático
Zona 3 (laranja) — "Delimitar o escopo" → destaca a instrução "Não modifique o arquivo — apenas liste os problemas"
Cada zona abre layer com explicação do elemento.

NARRAÇÃO
Um bom prompt no Claude Code combina três elementos fundamentais. Clique em cada zona colorida para explorar. [PAUSA]
Primeiro: identificar o elemento de código sobre o qual se deseja operar — nome da função, nome do arquivo, linhas relevantes quando pertinente. [PAUSA]
Segundo: descrever o comportamento atual e o esperado — o que o código faz hoje e o que deveria fazer. [PAUSA]
Terceiro — e este é especialmente importante: delimitar o escopo da resposta desejada. Recomenda-se sempre solicitar primeiro uma explicação ou um plano, e apenas depois autorizar a modificação do arquivo.

INTERAÇÃO
Zona 1 "Identificar o elemento" — abre layer com:
  Definição: "Mencione o nome da função, o nome do arquivo e, quando pertinente, as linhas relevantes."
  Exemplo bom: "'Tenho a função gerar_resumo() no arquivo relatorio.py aberto no editor.'"
  Exemplo ruim: "'Melhore o código.' — O assistente não sabe a qual código se refere."
Zona 2 "Descrever comportamento" — abre layer com:
  Definição: "O que o código faz hoje e o que deveria fazer (ou qual problema você suspeita)."
  Exemplo bom: "'Ela recebe um texto longo e retorna apenas as três primeiras frases. Identifique possíveis problemas de desempenho quando o texto for muito extenso.'"
Zona 3 "Delimitar o escopo" — abre layer com:
  Definição: "Diga explicitamente se quer apenas explicação, sugestão ou modificação do arquivo."
  Exemplo bom: "'Não modifique o arquivo — apenas liste os problemas encontrados e sugira alternativas.'"
  Risco: "'Refatore tudo imediatamente.' — Sem revisão prévia, mudanças podem ser aplicadas sem compreensão."
As três zonas devem ser clicadas para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após clique nas três zonas.


────────────────────────────────

SLIDE 21 — CONTEXTO AUTOMÁTICO E REFERÊNCIA EXPLÍCITA COM @
Tipo: Conteúdo com instrução técnica
Duração estimada: 45s

────────────────────────────────

VISUAL
Dois blocos informativos:
Bloco 1 — "O que o Claude Code acessa automaticamente":
  ✅ Arquivo atualmente aberto no editor
  ✅ Linhas selecionadas pelo usuário
  ❌ Arquivos fechados
  ❌ Histórico do Git
  ❌ Variáveis de ambiente
  ❌ Dependências instaladas
Bloco 2 — "Como referenciar múltiplos arquivos explicitamente":
  Sintaxe em destaque: @nomearquivo
  Exemplo em caixa de código: "Estou trabalhando em @api.py e preciso chamar uma função de @utils.py. Como fazer o import correto?"
  Nota: "Recomendado para projetos com 2 a 5 arquivos principais abertos simultaneamente."
Animação: blocos surgem em sequência.

[PRINT]
Nome: Painel do Claude Code com arquivo Python aberto no editor e prompt com referência @ digitado no campo de entrada
Caminho: VS Code > arquivo Python visível no editor > painel Claude Code aberto à direita > campo de entrada com prompt usando sintaxe @nomearquivo digitado
Destaque: destacar o arquivo aberto no editor e a sintaxe @nomearquivo no prompt do painel Claude Code
Modo: Estática

NARRAÇÃO
Quanto ao contexto automático, é importante saber seus limites. O Claude Code acessa automaticamente o arquivo aberto no editor e as linhas que você selecionou — mas não acessa arquivos fechados, histórico do Git, variáveis de ambiente ou dependências instaladas. [PAUSA]
Para projetos com múltiplos arquivos, você pode referenciar explicitamente qualquer arquivo usando a sintaxe arroba seguida do nome do arquivo diretamente no corpo do prompt. Por exemplo: "Estou trabalhando em @api.py e preciso chamar uma função de @utils.py. Como fazer o import correto?" [PAUSA]
Essa abordagem é recomendada para projetos com dois a cinco arquivos principais abertos simultaneamente.

INTERAÇÃO
Nenhuma — slide de instrução técnica com print ilustrativo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 22 — PROMPT INADEQUADO VS. PROMPT BEM FORMULADO
Tipo: Conteúdo comparativo
Duração estimada: 35s

────────────────────────────────

VISUAL
Dois cartões lado a lado:
Cartão esquerdo (fundo vermelho claro, ícone ❌): "Prompt inadequado"
"Como melhorar essa função?" — anotação: "Sem referência ao arquivo, sem contexto, sem escopo."
Cartão direito (fundo verde claro, ícone ✅): "Prompt bem formulado"
Texto completo do prompt de exemplo (calculate_total(), instrução de não modificar o arquivo) em caixa monoespaçada. Anotação: "Contexto preciso + instrução clara + restrição de escopo explícita."
Animação: cartões surgem simultaneamente com fade-in.

NARRAÇÃO
O contraste entre um prompt inadequado e um bem formulado é marcante. [PAUSA]
"Como melhorar essa função?" — o assistente não sabe qual função, qual aspecto melhorar, nem se pode modificar o arquivo. [PAUSA]
Em contrapartida, um prompt que identifica a função pelo nome, descreve o que ela faz hoje, especifica o aspecto a melhorar e restringe explicitamente o escopo — "não faça a mudança no arquivo ainda, apenas mostre o código sugerido" — gera uma resposta útil, específica e segura. [PAUSA]
Essa diferença é o que separa uma interação produtiva de uma interação frustrante.

INTERAÇÃO
Nenhuma — slide comparativo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 23 — EXERCÍCIO: QUESTÃO DE MÚLTIPLA ESCOLHA — AVALIAÇÃO DE PROMPTS
Tipo: Questão de avaliação
Duração estimada: 50s

────────────────────────────────

VISUAL
Enunciado da questão em caixa de destaque. Cenário: "Arquivo relatorio.py aberto no editor, contendo a função gerar_resumo(texto)." Quatro alternativas em cartões clicáveis (A, B, C, D). Barra de progresso: "Exercício 3 de 5".

NARRAÇÃO
Analise os quatro prompts e identifique qual está mais bem formulado para obter uma resposta precisa e segura do Claude Code. O arquivo relatorio.py está aberto no editor e contém uma função chamada gerar_resumo().

INTERAÇÃO
Tipo: Múltipla escolha (Storyline: freeform pick-one)
Enunciado: "Qual dos prompts abaixo está mais bem formulado para obter uma resposta precisa e segura do Claude Code?"
Alternativas:
A) "Melhore o código."
B) "Analise a função gerar_resumo() no arquivo aberto. Ela recebe um texto longo e retorna apenas as três primeiras frases. Identifique possíveis problemas de desempenho quando o texto de entrada for muito extenso. Não modifique o arquivo — apenas liste os problemas encontrados e sugira alternativas."
C) "Como funciona Python?"
D) "Refatore tudo no @relatorio.py imediatamente."
Gabarito: B
Tentativas: 2
Feedback B (correto): "Correto! O prompt B atende aos três critérios: identifica o elemento (gerar_resumo()), descreve o comportamento e o cenário problemático, e delimita explicitamente o escopo (sem modificação do arquivo)."
Feedback A (incorreto): "Este prompt é excessivamente vago — o assistente não sabe qual elemento de código está sendo referenciado nem qual aspecto deve ser melhorado."
Feedback C (incorreto): "Este prompt é genérico demais e não faz uso do contexto do arquivo aberto. É mais adequado para a interface web do que para a extensão VS Code."
Feedback D (incorreto): "Este prompt não solicita revisão prévia e autoriza modificação direta sem planejamento — prática que deve ser evitada no ciclo de refatoração segura."
Feedback após 2ª tentativa errada: exibe gabarito com fundamentação completa.

Botão "Avançar para o Módulo 4" — aparece após submissão da questão.

NAVEGAÇÃO
Restrita — avanço via botão pós-submissão.


────────────────────────────────

SLIDE 24 — CHECKLIST DE CONCLUSÃO DO MÓDULO 3
Tipo: Avaliação de êxito
Duração estimada: 20s

────────────────────────────────

VISUAL
Três itens de checklist interativo:
☐ Os três elementos de um bom prompt identificados e compreendidos
☐ Diferença entre contexto automático e referência explícita com @ entendida
☐ Questão de múltipla escolha respondida
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 4".

NARRAÇÃO
Confirme os três critérios. [PAUSA]
Os princípios de formulação de prompts que você aprendeu aqui — precisão, contextualização e delimitação de escopo — se aplicam a qualquer tarefa que você venha a realizar com o assistente, muito além da programação.

INTERAÇÃO
Checkboxes 1 a 3 — clicáveis individualmente.
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 4".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os três checkboxes marcados.

---

## MÓDULO 4 — REFATORAÇÃO ASSISTIDA: O CICLO PERGUNTAR → PLANEJAR → REVISAR → ACEITAR

---


────────────────────────────────

SLIDE 25 — ABERTURA DO MÓDULO 4
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de diff/comparação (duas colunas vermelho/verde), número e título do módulo. Subtítulo: "Duração estimada: 20 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 4 — Refatoração Assistida: o ciclo Perguntar, Planejar, Revisar e Aceitar. [PAUSA]
Sabendo formular prompts contextualizados, você está em condições de dar o próximo passo: realizar modificações reais no código de forma segura, por meio do ciclo de revisão que caracteriza o uso responsável de assistentes de IA em ambientes de desenvolvimento.

INTERAÇÃO
Botão "Começar" — avança para Slide 26.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 26 — O QUE É REFATORAÇÃO?
Tipo: Conteúdo
Duração estimada: 30s

────────────────────────────────

VISUAL
Definição em destaque tipográfico: "Refatoração = reescrever ou reorganizar um trecho de código existente sem alterar o comportamento externo." Dois blocos de exemplo animados:
Antes (código com nome de variável enigmático): ícone de código "feio"
Depois (código refatorado, mais legível): ícone de código "limpo" com check verde
Abaixo: nota — "Relevante não apenas para programadores — também para scripts de análise de dados, automação de tarefas e organização de texto estruturado."
Animação: bloco "Antes" surge; seta aparece; bloco "Depois" surge com fade-in.

NARRAÇÃO
O termo refatoração designa o processo de reescrever ou reorganizar um trecho de código existente sem alterar o seu comportamento externo. O código refatorado continua fazendo a mesma coisa — porém de forma mais clara, mais eficiente ou mais fácil de manter. [PAUSA]
É uma prática rotineira no desenvolvimento de software e igualmente relevante em contextos acadêmicos onde scripts são produzidos para análise de dados ou automação de tarefas. [PAUSA]
E o mesmo ciclo que vamos aprender aqui também se aplica a depuração de erros — o que chamamos de debugging.

INTERAÇÃO
Nenhuma — slide expositivo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 27 — O CICLO DE QUATRO ETAPAS
Tipo: Conteúdo interativo (linha do tempo clicável)
Duração estimada: 55s

────────────────────────────────

VISUAL
Linha do tempo horizontal com 4 etapas clicáveis, cada uma com ícone e nome em inglês e português:
1. Perguntar (Ask) — ícone de balão de pergunta
2. Planejar (Plan) — ícone de lista de passos
3. Revisar (Diff) — ícone de colunas vermelho/verde
4. Aceitar ou Rejeitar (Accept/Reject) — ícone de check e X
Cada etapa abre layer com definição, prompt recomendado e exemplo de ação.
Animação: etapas surgem em sequência com delay de 0,4s.

NARRAÇÃO
O ciclo de refatoração segura com o Claude Code tem quatro etapas. Clique em cada uma para explorar. [PAUSA]
Perguntar: solicitar ao assistente uma análise e sugestão de melhoria, sem autorizar modificações. [PAUSA]
Planejar: pedir ao assistente que liste os passos exatos e explique os trade-offs — o que se ganha e o que se perde. [PAUSA]
Revisar: analisar o visualizador de diferenças — o diff viewer — antes de qualquer mudança ser aplicada. [PAUSA]
Aceitar ou Rejeitar: aprovar a mudança, rejeitá-la ou solicitar uma nova proposta com parâmetros diferentes.

INTERAÇÃO
Etapa 1 "Perguntar (Ask)" — abre layer com:
  Definição: "Solicite análise e sugestão SEM autorizar modificações."
  Prompt recomendado: "'Tenho a função verificar_email() no arquivo aberto. Sugira uma versão mais concisa. Não modifique o arquivo ainda — apenas mostre o código sugerido.'"
Etapa 2 "Planejar (Plan)" — abre layer com:
  Definição: "Peça a lista de passos e os trade-offs antes de prosseguir."
  Prompt recomendado: "'Antes de aplicar a mudança, explique: (a) o que mudou na lógica; (b) há casos em que a nova versão se comporta de forma diferente; (c) quais são os trade-offs?'"
Etapa 3 "Revisar (Diff)" — abre layer com:
  Definição: "Leia o diff viewer: linhas em vermelho (-) = removidas; linhas em verde (+) = adicionadas. Nenhuma mudança é aplicada sem sua aprovação."
  Analogia: "Como o 'controle de alterações' do Word — o documento original permanece intacto até você aprovar."
Etapa 4 "Aceitar ou Rejeitar (Accept/Reject)" — abre layer com:
  Definição: "Você é o árbitro final. Aceite apenas o que compreender. Rejeite e solicite nova proposta se necessário."
  Prompt recomendado: "'Entendi a explicação. Por favor, aplique a refatoração.' OU 'Prefiro uma versão mais explícita — a equipe que vai manter isso não tem experiência avançada em Python.'"
As quatro etapas devem ser clicadas para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após clique nas quatro etapas.


────────────────────────────────

SLIDE 28 — O DIFF VIEWER: LENDO AS DIFERENÇAS
Tipo: Conteúdo com demonstração visual
Duração estimada: 50s

────────────────────────────────

VISUAL
Representação visual do diff viewer com dois painéis:
Painel esquerdo — código original com linhas marcadas em vermelho (precedidas por -): "versão original que será removida"
Painel direito — código sugerido com linhas marcadas em verde (precedidas por +): "nova versão que será inserida"
Botões "Accept" e "Reject" visíveis abaixo dos painéis.
Legenda explicativa das cores e símbolos.
Animação: painéis surgem simultaneamente; legenda com fade-in.

[PRINT]
Nome: Diff viewer do VS Code exibindo código original (linhas vermelhas, símbolo -) e código sugerido (linhas verdes, símbolo +) com botões Accept e Reject visíveis
Caminho: VS Code > extensão Claude Code > após prompt de refatoração > diff viewer ativo mostrando comparação lado a lado com código original em vermelho (com -) e código sugerido em verde (com +) e botões Accept / Reject visíveis
Destaque: destacar as linhas em vermelho com símbolo -, as linhas em verde com símbolo + e os botões Accept e Reject
Modo: Estática

NARRAÇÃO
O diff viewer — visualizador de diferenças — é uma ferramenta integrada ao VS Code que exibe de forma visual e comparativa as alterações propostas pelo assistente. [PAUSA]
Linhas precedidas pelo símbolo de menos e destacadas em vermelho correspondem ao código original que será removido. Linhas precedidas por mais e destacadas em verde correspondem ao novo código que será inserido. [PAUSA]
Nenhuma modificação é aplicada ao arquivo enquanto você não clicar em Accept. Esse mecanismo é análogo à função de controle de alterações do Microsoft Word: o documento original permanece intacto até você aprovar explicitamente cada mudança. [PAUSA]
Leia sempre o diff completo antes de aceitar — inclusive para mudanças aparentemente simples.

INTERAÇÃO
Nenhuma — slide de demonstração com print ilustrativo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 29 — QUANDO REJEITAR UMA SUGESTÃO
Tipo: Conteúdo
Duração estimada: 35s

────────────────────────────────

VISUAL
Três cartões com situações de rejeição:
1. "Não entendi o que mudou" — ícone de ponto de interrogação: "Solicite explicação antes de aceitar qualquer coisa que não compreenda."
2. "Tecnicamente válido, mas inadequado ao contexto" — ícone de régua: "Ex.: código mais conciso, porém menos legível para a equipe sem experiência avançada."
3. "Comportamento diferente em casos extremos" — ícone de alerta: "Valide com casos de teste antes de aceitar."
Abaixo: princípio em destaque — "Você é sempre o árbitro final. A responsabilidade pela aprovação de qualquer alteração recai sobre você, não sobre o assistente."
Animação: cartões surgem em sequência com delay de 0,4s.

NARRAÇÃO
O assistente pode sugerir mudanças tecnicamente válidas que, no entanto, não sejam adequadas ao seu contexto específico. [PAUSA]
Rejeite — e solicite uma nova proposta — se não entendeu o que mudou, se a solução é correta mas inadequada para o nível de experiência da sua equipe, ou se suspeita que o novo código se comporta de forma diferente em casos extremos. [PAUSA]
O princípio central: você é sempre o árbitro final. A responsabilidade pela aprovação ou rejeição de qualquer alteração recai sobre você — não sobre o assistente. Nunca aceite uma sugestão sem compreender o que ela faz.

INTERAÇÃO
Nenhuma — slide expositivo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 30 — DEPURAÇÃO (DEBUGGING) COM O CLAUDE CODE
Tipo: Conteúdo
Duração estimada: 35s

────────────────────────────────

VISUAL
Três blocos de informação necessária para descrever um erro ao assistente:
1. Trecho de código onde o erro ocorreu — ícone de código com X
2. Mensagem de erro completa (stack trace) — ícone de log/terminal
3. Resultado esperado vs. resultado obtido — ícone de dois itens em comparação
Abaixo: prompt de exemplo em caixa monoespaçada mostrando os três elementos preenchidos.
Animação: blocos surgem em sequência.

NARRAÇÃO
O mesmo ciclo de quatro etapas se aplica à depuração de erros. Ao descrever um erro para o assistente, forneça sempre três informações. [PAUSA]
O trecho de código onde o erro ocorreu. A mensagem de erro completa — o que chamamos de stack trace, que é o registro sequencial das chamadas de função que levaram ao erro. E uma descrição do resultado esperado versus o resultado obtido. [PAUSA]
Quanto mais precisa for essa descrição, mais eficiente será o diagnóstico do assistente.

INTERAÇÃO
Nenhuma — slide expositivo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 31 — EXERCÍCIO PRÁTICO: CICLO DE REFATORAÇÃO GUIADA
Tipo: Instrução prática com stepper
Duração estimada: 55s

────────────────────────────────

VISUAL
Stepper vertical com 5 passos numerados, cada um com o prompt exato a enviar e instrução de ação no VS Code:
1. Criar arquivo exercicio.py com a função verificar_email()
2. Prompt 1: solicitar versão mais concisa sem modificar o arquivo
3. Prompt 2: solicitar explicação dos trade-offs antes de aplicar
4. Prompt 3: autorizar a aplicação da refatoração
5. Analisar o diff viewer e decidir: Accept ou Reject
Barra de progresso: "Exercício 4 de 5". Código da função em caixa monoespaçada.

[PRINT]
Nome: Diff viewer ativo após prompt de refatoração da função verificar_email() — versão original em vermelho e versão sugerida em verde
Caminho: VS Code > arquivo exercicio.py aberto > painel Claude Code > após prompt de refatoração da função verificar_email() > diff viewer ativo com código original e sugerido lado a lado
Destaque: destacar as linhas removidas (vermelho, -) e linhas adicionadas (verde, +) e os botões Accept e Reject
Modo: Estática

NARRAÇÃO
Agora execute o ciclo completo de refatoração guiada. [PAUSA]
Crie o arquivo exercicio.py com a função verificar_email exibida na tela. Com o arquivo aberto no editor, acesse o painel do Claude Code e siga os três prompts em sequência: primeiro peça a sugestão sem modificar o arquivo; depois peça a explicação dos trade-offs; e só então autorize a aplicação. [PAUSA]
Analise o diff viewer com atenção. Você consegue identificar o que mudou? A nova versão faz sentido para o seu contexto? Aceite ou rejeite com base nessa análise.

INTERAÇÃO
Botão "Ver código do exercício" — abre layer com o código completo da função verificar_email() e botão "Copiar código".
Botão "Ver os 3 prompts" — abre layer com os três prompts em sequência e botão "Copiar prompts".
Botão "Concluí o exercício" — avança para Slide 32.

NAVEGAÇÃO
Restrita — avanço via botão "Concluí o exercício".


────────────────────────────────

SLIDE 32 — CHECKLIST DE CONCLUSÃO DO MÓDULO 4
Tipo: Avaliação de êxito
Duração estimada: 20s

────────────────────────────────

VISUAL
Três itens de checklist interativo:
☐ As quatro etapas do ciclo executadas sem pular a revisão (diff)
☐ Diff viewer lido antes de clicar em Accept ou Reject
☐ Nenhuma mudança aceita sem compreensão do que ela faz
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 5".

NARRAÇÃO
Confirme os três critérios — especialmente os dois primeiros. [PAUSA]
A etapa de revisão pelo diff viewer é o mecanismo de segurança mais importante do ciclo. Pulá-la é o equivalente a assinar um contrato sem ler.

INTERAÇÃO
Checkboxes 1 a 3 — clicáveis individualmente.
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 5".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os três checkboxes marcados.

---

## MÓDULO 5 — SÍNTESE E APLICAÇÃO INTEGRADA

---


────────────────────────────────

SLIDE 33 — ABERTURA DO MÓDULO 5
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de bandeira de chegada, número e título do módulo. Subtítulo: "Duração estimada: 10 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 5 — Síntese e Aplicação Integrada. [PAUSA]
Este módulo não introduz conceitos novos. Seu propósito é consolidar, em uma única atividade integradora, todas as competências dos módulos anteriores: compreensão do ecossistema, instalação e configuração, formulação de prompts contextualizados e ciclo de refatoração segura.

INTERAÇÃO
Botão "Começar" — avança para Slide 34.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 34 — A ATIVIDADE INTEGRADORA: CONTEXTO
Tipo: Conteúdo — apresentação do cenário
Duração estimada: 35s

────────────────────────────────

VISUAL
Código do arquivo notas.py em caixa monoespaçada (funções c(l) e m(l) com nomes enigmáticos e sem documentação). Legenda: "Arquivo inicial — notas.py — com múltiplos problemas de legibilidade e organização." Instrução: "Reproduza este código em um arquivo chamado notas.py no VS Code antes de avançar."
Animação: código surge com fade-in; legenda aparece em seguida.

NARRAÇÃO
O arquivo que você vai trabalhar nesta atividade é o notas.py exibido na tela. Ele contém duas funções com nomes enigmáticos — c(l) e m(l) — sem documentação e sem type hints. [PAUSA]
Você vai conduzir esse arquivo, com auxílio do Claude Code, desde o estado inicial problemático até um estado final documentado, testável e legível. Esse percurso replica um cenário real de trabalho. [PAUSA]
Reproduza o código no VS Code antes de avançar. E se preferir, substitua o Python por qualquer outra linguagem — ou trabalhe com texto em linguagem natural que precise ser reorganizado. O ciclo de prompts permanece o mesmo.

INTERAÇÃO
Botão "Ver e copiar código notas.py" — abre layer com o código completo formatado e botão "Copiar código".
Botão "Reproduzi o arquivo no VS Code" — libera avanço para Slide 35.

NAVEGAÇÃO
Restrita — avanço via botão "Reproduzi o arquivo no VS Code".


────────────────────────────────

SLIDE 35 — ATIVIDADE INTEGRADORA: QUATRO ETAPAS
Tipo: Instrução prática com stepper
Duração estimada: 50s

────────────────────────────────

VISUAL
Stepper vertical com 4 etapas, cada uma com título, prompt exato e instrução de ação:
Etapa 1 — Perguntar: prompt de análise sem modificação
Etapa 2 — Planejar: prompt de sugestão de melhorias com plano listado
Etapa 3 — Revisar e aceitar: prompt de aplicação com diff
Etapa 4 — Documentar: prompt de geração de cabeçalho do arquivo
Barra de progresso: "Exercício 5 de 5".

[PRINT]
Nome: Arquivo notas.py refatorado e documentado no VS Code — versão final com nomes legíveis, type hints, docstrings e cabeçalho de módulo
Caminho: VS Code > arquivo notas.py aberto > versão final após refatoração com funções renomeadas (ex.: calcular_media, calcular_mediana), type hints, docstrings no estilo Google e comentário de cabeçalho no topo do arquivo
Destaque: destacar o cabeçalho do módulo, os nomes das funções refatoradas, os type hints e as docstrings
Modo: Estática

[PRINT]
Nome: Trecho do chat com o Claude Code utilizado em uma das etapas da atividade integradora
Caminho: VS Code > painel Claude Code > conversa com um dos quatro prompts da atividade enviado e resposta do assistente visível
Destaque: destacar o prompt enviado e a resposta do assistente com a sugestão ou explicação correspondente
Modo: Estática

NARRAÇÃO
Agora execute as quatro etapas em sequência — e não pule nenhuma delas. [PAUSA]
Etapa 1: envie o prompt de análise sem autorizar modificações — deixe o assistente explicar o que cada função faz. Etapa 2: peça um plano de melhorias com nomes mais descritivos, type hints e docstrings no estilo Google, listando as mudanças antes de aplicar. Etapa 3: autorize a aplicação e revise o diff antes de aceitar. Etapa 4: solicite a geração do comentário de cabeçalho do módulo. [PAUSA]
Registre em um arquivo de notas as decisões tomadas em cada etapa: quais sugestões você aceitou, quais rejeitou e por quê.

INTERAÇÃO
Etapa 1 — expande com: prompt "Tenho duas funções no arquivo aberto: c(l) e m(l). Analise o código e descreva o que cada função faz. Não modifique nada ainda." + botão "Copiar prompt".
Etapa 2 — expande com: prompt "Sugira melhorias para tornar o código mais legível: nomes de funções e variáveis mais descritivos, type hints e docstrings em estilo Google. Liste o plano de mudanças antes de aplicar." + botão "Copiar prompt".
Etapa 3 — expande com: prompt "Aplique as melhorias planejadas. Mostre o diff antes de confirmar." + instrução "Leia o diff viewer com atenção antes de clicar em Accept." + botão "Copiar prompt".
Etapa 4 — expande com: prompt "Gere um comentário de cabeçalho para o arquivo notas.py descrevendo o que o módulo faz, quais funções contém e um exemplo de uso de cada uma." + botão "Copiar prompt".
Botão "Concluí as quatro etapas" — avança para Slide 36.

NAVEGAÇÃO
Restrita — avanço via botão "Concluí as quatro etapas".


────────────────────────────────

SLIDE 36 — CHECKLIST DE AVALIAÇÃO FINAL
Tipo: Avaliação de conclusão
Duração estimada: 35s

────────────────────────────────

VISUAL
Tabela de 6 critérios com checkbox interativo:
☐ As quatro etapas do ciclo foram executadas sem pular a etapa de revisão (diff)
☐ Nenhum dado sensível foi incluído nos prompts
☐ A explicação do assistente foi lida e compreendida antes de aceitar a refatoração
☐ O arquivo final contém nomes de funções legíveis, type hints e docstrings
☐ O cabeçalho do módulo foi gerado e inserido no arquivo
☐ O participante consegue explicar, com suas próprias palavras, o que cada função faz
Critério de êxito em destaque: "Ao menos 5 dos 6 critérios marcados, obrigatoriamente incluindo os critérios 1 e 2."
Ao atingir o critério: camada de parabéns + botão "Avançar para o encerramento".

NARRAÇÃO
Confirme os seis critérios de avaliação. [PAUSA]
O critério de êxito é ao menos cinco dos seis marcados como Sim — obrigatoriamente incluindo o primeiro e o segundo. [PAUSA]
Os critérios 1 e 2 são inegociáveis: executar o ciclo sem pular a revisão, e não incluir dados sensíveis nos prompts. Esses dois hábitos definem o uso responsável do assistente.

INTERAÇÃO
Checkboxes 1 a 6 — clicáveis individualmente.
Trigger: ao marcar ≥5 checkboxes incluindo obrigatoriamente os checkboxes 1 e 2: camada de parabéns + botão "Avançar para o encerramento".
Trigger alternativo: se o aluno marcar 5 ou mais mas sem os checkboxes 1 e 2: exibe mensagem "Os critérios 1 e 2 são obrigatórios. Revise as etapas correspondentes antes de avançar."

NAVEGAÇÃO
Restrita — botão de avanço condicionado aos critérios acima.

---

## SLIDE DE ENCERRAMENTO

---


────────────────────────────────

SLIDE 37 — ENCERRAMENTO DO CURSO
Tipo: Encerramento
Duração estimada: 60s

────────────────────────────────

VISUAL
Fundo com identidade visual do Slide 01. Título: "Parabéns — você concluiu a Trilha Essentials." Ícone de conquista animado. Síntese em destaque tipográfico: "O uso produtivo de um assistente de IA não reside na delegação irrestrita de decisões à ferramenta, mas na construção de um diálogo preciso, informado e criticamente supervisionado — em que o profissional humano permanece responsável por cada escolha aprovada." Abaixo: três blocos de aprofundamento com ícones:
1. Geração automática de testes unitários (Aulas 6 e 7 do material-fonte)
2. Model Context Protocol (MCP) — acesso a repositórios Git e bancos de dados (Aula 11)
3. Automação de tarefas repetitivas com scripts auxiliares (Aula 9)
Link da documentação oficial em destaque: docs.anthropic.com
Animação: título e síntese surgem primeiro; blocos de aprofundamento em sequência com delay.

NARRAÇÃO
Você concluiu o curso Plataformas e Integrações: Use o Claude Code no VS Code — Trilha Essentials. [PAUSA]
Ao longo dos cinco módulos, você compreendeu o ecossistema Claude e seus limites de segurança, instalou e configurou a extensão com segurança, aprendeu a formular prompts contextualizados e executou o ciclo de refatoração assistida usando o diff viewer. [PAUSA]
Recomenda-se a prática regular dessas habilidades em projetos concretos — a fluência na interação com assistentes de IA se desenvolve de forma acumulativa. Cada sessão de uso aprimora a capacidade de formular perguntas mais precisas e de avaliar respostas com maior segurança. [PAUSA]
Para quem quiser aprofundar, três frentes estão indicadas na tela: geração automatizada de testes unitários, o Model Context Protocol para acesso a fontes externas, e automação com scripts auxiliares. A documentação oficial da Anthropic em docs.anthropic.com é a referência atualizada para todos esses tópicos. [PAUSA]
Bom trabalho.

INTERAÇÃO
Botão "Acessar documentação oficial" — abre link: https://docs.anthropic.com (nova aba).
Botão "Reiniciar o curso" — retorna ao Slide 01 (opcional).
Botão "Sair" — encerra o módulo e registra conclusão no LMS (trigger: Complete Course / passed).

NAVEGAÇÃO
Livre — slide final.

---

---

# TABELA GERAL DE ASSETS

| Tipo | Descrição | Slide de uso |
|------|-----------|:------------:|
| Diagrama animado | Três cartões: Interface Web / Extensão VS Code (badge "foco") / CLI | 04 |
| Diagrama animado | Dois cenários: colagem manual (interface web) vs. contexto automático (extensão) | 05 |
| Tabela comparativa | Três modos de acesso × quatro aspectos (acesso a arquivos, contexto, integração, ideal para) | 06 |
| Diagrama animado | Computador ↔ nuvem Anthropic com dois painéis: o que sai / o que fica | 07 |
| Diagrama animado | Dois cenários: arquivo .env no Git (perigo) vs. .env no .gitignore (seguro) | 15 |
| Diagrama animado | Linha do tempo: 4 etapas do ciclo de refatoração (Ask → Plan → Diff → Accept/Reject) | 27 |
| Diagrama animado | Diff viewer: dois painéis vermelho (-) e verde (+) com botões Accept e Reject | 28 |
| Diagrama animado | Código "feio" (antes) → seta → código refatorado "limpo" (depois) | 26 |
| Ícone | Globo/ecossistema (Módulo 1) | 03 |
| Ícone | Engrenagem (Módulo 2) | 11 |
| Ícone | Balão de prompt (Módulo 3) | 18 |
| Ícone | Diff/comparação vermelho-verde (Módulo 4) | 25 |
| Ícone | Bandeira de chegada (Módulo 5) | 33 |
| Ícone | Raio ⚡ (símbolo do Claude Code — usado em múltiplos slides) | 01, 13, 16, 17 |
| Ícone | Escudo com X (alerta de segurança) | 08 |
| Ícone | Cadeado (o que permanece na máquina) | 07 |
| Ícone | Conquista/medalha | 36, 37 |
| Fonte monoespaçada | Prompts, código Python (exercicio.py, notas.py), sintaxe @, exemplo .gitignore | 13, 14, 20, 21, 22, 31, 34, 35 |
| Áudio | Narração completa (37 slides) — locutor ou TTS | Todos |
| Link externo | Documentação oficial Anthropic | 37 |

---

# TABELA DE CAPTURAS DE TELA

| Tipo | Descrição da tela | Caminho no sistema | Modo de exibição | Slide | Responsável |
|------|-------------------|--------------------|:----------------:|:-----:|-------------|
| Captura de tela | Janela "About VS Code" exibindo número da versão instalada | VS Code > Help > About (Windows/Linux) ou Code > About (macOS) > janela com número da versão | Zoom progressivo (aproximação ao número da versão) | 12 | Equipe de conteúdo |
| Captura de tela | Painel de extensões com resultado da busca "claude code" — extensão Anthropic Inc. + botão Install | VS Code > painel de extensões (Ctrl+Shift+X) > busca por "claude code" > resultado com publicador "Anthropic Inc." e botão Install | Zoom progressivo (aproximação ao nome do publicador e botão Install) | 13 | Equipe de conteúdo |
| Captura de tela | Caixa de diálogo "Claude Code: Sign In" com campo de inserção da chave de API | VS Code > Paleta de Comandos (Ctrl+Shift+P) > "Claude Code: Sign In" > caixa de diálogo com campo de texto | Estática | 14 | Equipe de conteúdo |
| Captura de tela | VS Code com painel Claude Code aberto e resposta à pergunta "Hello Claude! What is 2+2?" | VS Code > painel Claude Code > resposta de teste recebida + ícone ⚡ visível na barra lateral | Estática | 16 | Equipe de conteúdo |
| Captura de tela | Painel Claude Code com arquivo Python aberto e prompt com sintaxe @nomearquivo digitado | VS Code > arquivo Python no editor > painel Claude Code > prompt com @nomearquivo no campo de entrada | Estática | 21 | Equipe de conteúdo |
| Captura de tela | Diff viewer com código original (vermelho, -) e código sugerido (verde, +) com botões Accept e Reject | VS Code > extensão Claude Code > diff viewer ativo após prompt de refatoração da função verificar_email() | Estática | 28, 31 | Equipe de conteúdo |
| Captura de tela | Arquivo notas.py refatorado — versão final com nomes legíveis, type hints, docstrings e cabeçalho | VS Code > arquivo notas.py > versão final após todas as etapas da atividade integradora | Estática | 35 | Participante (autogerado durante atividade) |
| Captura de tela | Trecho do chat com Claude Code em uma das etapas da atividade integradora | VS Code > painel Claude Code > um dos quatro prompts da atividade enviado + resposta do assistente | Estática | 35 | Participante (autogerado durante atividade) |
