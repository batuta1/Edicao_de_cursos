<link rel="stylesheet" href="../../.css/style.css">

# Claude: Comece a usar o aplicativo para desktop — Curso Hands-on

*Claude: Get Started with the Desktop App — Curso Hands-on*

*Ao final deste curso, você terá instalado o Claude Desktop, aberto um projeto real, feito o assistente trabalhar para você — e saberá o que fazer quando algo der errado.*

---

## Antes de Arregaçar as Mangas

Bem-vindo ao lado prático da vida. Aqui não tem slides, não tem quatro parágrafos explicando o que você vai aprender antes de aprender. Cada oficina começa com um problema real, e você resolve na hora, com as próprias mãos. Teoria aparece só quando é estritamente necessária para o próximo passo — e nada além disso.

**O que você precisa ter aberto agora:**

- O computador (Windows 10/11 ou macOS 12 ou superior) — com conexão à internet
- Uma conta na Anthropic com plano Pro, Max, Team ou Enterprise (gratuito não inclui o app desktop)
- O site [claude.ai](https://claude.ai) aberto em uma aba do navegador para conferir seu plano
- Um editor de texto simples (Bloco de Notas, TextEdit ou qualquer outro)
- Disposição para clicar, errar e tentar de novo

> 🔑 **Regra de ouro do curso:** você não vai aprender lendo — vai aprender fazendo. Se travar em algum passo, não pule: consulte a seção "Se travar" da oficina. Errar aqui é esperado e faz parte do processo.

---

## O Mapa da Mão na Massa

Cada oficina resolve um problema e entrega uma vitória concreta. Faça em sequência — cada uma constrói sobre a anterior.

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1 | "Não sei se meu computador suporta o app nem como instalar" | 20 min |
| 2 | "Instalei, mas não entendo nada dessas abas e botões" | 15 min |
| 3 | "Quero trabalhar com um arquivo real, mas não sei como organizar" | 20 min |
| 4 | "Peço coisas ao Claude e ele entende errado — como melhorar?" | 20 min |
| Projeto Final | "Quero um fluxo completo funcionando, do zero ao resultado" | 15 min |

---

<div style="page-break-after: always;"></div>

# Oficina 1 — Instale o Claude Desktop do Jeito Certo

### 🎯 O Problema

Você ouviu falar no Claude Desktop e quer experimentar. Mas antes de baixar qualquer coisa, precisa saber: o seu computador suporta? Qual versão baixar? E o que fazer se o aplicativo não abrir depois de instalar? Esta oficina resolve tudo isso — e no final você terá o app aberto e funcionando na sua máquina.

### 🧰 O que você vai usar

- Seu computador (Windows ou macOS)
- Navegador de internet
- O site oficial da Anthropic para download
- Sua conta Anthropic já criada

### 👐 Mão na massa

**Passo 1 — Descubra qual é o seu sistema operacional e processador**

No Windows:
1. Clique no botão Iniciar (o símbolo do Windows no canto inferior esquerdo).
2. Digite "Sobre" e clique em "Sobre o seu PC" (ou "Configurações > Sistema > Sobre").
3. Procure o campo "Tipo de sistema" — anote se aparece x64 ou ARM64.
4. Procure também a versão do Windows — deve ser 10 ou 11.

No macOS:
1. Clique no menu da maçã (canto superior esquerdo da tela).
2. Clique em "Sobre este Mac".
3. Procure o campo "Chip" (ex.: M1, M2, M3) ou "Processador" (ex.: Intel Core).
4. Confirme que a versão do macOS é 12 ou superior.

> 📸 **Captura de Tela sugerida:** Faça um print desta tela com as informações do seu sistema — você vai precisar delas no próximo passo para escolher o instalador certo.

> 💡 **Dica:** ARM64 e Apple Silicon (M1/M2/M3) são a mesma família de processador mais recente — só fabricantes diferentes (Microsoft/Qualcomm e Apple, respectivamente). Se você tem um Mac comprado a partir de 2020, provavelmente tem chip Apple Silicon.

**Passo 2 — Confirme seu plano Anthropic**

1. Abra [claude.ai](https://claude.ai) no navegador.
2. Faça login com seu e-mail e senha.
3. Clique no ícone do seu perfil (canto superior direito).
4. Procure a seção "Plano" ou "Billing".
5. Confirme que seu plano é Pro, Max, Team ou Enterprise.

> ⚠️ **Cuidado:** Se o seu plano for Free (gratuito), o Claude Desktop não está disponível. Ao tentar acessar a aba Code, o app vai exibir uma mensagem pedindo upgrade. Verifique com sua instituição se há acesso educacional disponível antes de assinar um plano pago.

**Passo 3 — Baixe o instalador correto**

1. Acesse o site oficial da Anthropic (anthropic.com) e localize a seção de downloads do Claude Desktop.
2. Escolha o instalador de acordo com o que você descobriu no Passo 1:

   | Meu sistema | Qual baixar |
   |---|---|
   | Windows, campo "Tipo de sistema" = x64 | Windows x64 |
   | Windows, campo "Tipo de sistema" = ARM64 | Windows ARM64 |
   | macOS, campo "Chip" = M1/M2/M3 | macOS Apple Silicon |
   | macOS, campo "Processador" = Intel | macOS Intel |

3. Aguarde o download concluir (o arquivo tem entre 150 MB e 200 MB).

**Passo 4 — Instale o aplicativo**

No Windows:
1. Localize o arquivo baixado na pasta Downloads.
2. Dê duplo clique no arquivo `.exe`.
3. Se aparecer uma janela de segurança perguntando se você quer executar, clique em "Sim".
4. Siga o assistente de instalação clicando em "Próximo" / "Aceitar" / "Instalar".
5. Marque a opção "Criar atalho na área de trabalho" se aparecer — facilita a vida depois.
6. Aguarde 2 a 3 minutos. Clique em "Concluir" quando aparecer.

No macOS:
1. Localize o arquivo `.dmg` na pasta Downloads.
2. Dê duplo clique no arquivo — uma janela abre com o ícone do Claude e uma pasta "Aplicativos".
3. Arraste o ícone do Claude para a pasta Aplicativos.
4. Aguarde 10 a 30 segundos até a cópia terminar.

**Passo 5 — Abra o app e faça login**

1. Abra o Claude Desktop (pelo atalho na área de trabalho ou pela pasta Aplicativos).
2. Na primeira abertura, o app pode demorar 20 a 30 segundos — é normal.
3. Uma tela de login vai aparecer. Digite seu e-mail e senha da conta Anthropic.
4. O app vai abrir o seu navegador para uma verificação extra de segurança — confirme lá.
5. Volte para o app. Se tudo correu bem, você verá três abas no topo: Chat, Code e Cowork.

> 📸 **Captura de Tela sugerida:** Faça um print da tela inicial do Claude Desktop com as três abas visíveis — essa é a sua primeira vitória documentada!

### ✅ Deu certo?

O Claude Desktop está aberto, você está logado e consegue ver as abas Chat, Code e Cowork no topo da janela. Se apertar na aba Chat e uma caixa de texto aparecer, está tudo funcionando.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Duplo clique no instalador e nada acontece | Clique com o botão direito no arquivo e escolha "Executar como administrador" (Windows) ou arraste novamente para Aplicativos (macOS) |
| Login funciona no navegador mas o app fica em loop | Feche o app, delete a pasta de cache (`%APPDATA%\Claude` no Windows ou `~/.cache/Claude` no macOS) e abra novamente |
| As abas aparecem mas a aba Code mostra "Upgrade Required" | Seu plano atual não inclui o desktop; verifique o plano na sua conta em claude.ai |

### 🚀 Quer ir além?

- Localize a opção "Sobre" no menu do app (Help > About) e anote qual versão foi instalada.
- Experimente digitar qualquer coisa na aba Chat e veja o Claude responder.
- Procure no menu do app a opção de configurações e explore o que pode ser ajustado.

---

<div style="page-break-after: always;"></div>

# Oficina 2 — Entenda as Três Abas em 15 Minutos

### 🎯 O Problema

O app está aberto, mas você não sabe muito bem por onde começar. Chat? Code? Cowork? O que cada um faz? Esta oficina vai deixar claro de uma vez por todas quando usar cada interface — e você vai testar as duas principais na prática, agora mesmo.

### 🧰 O que você vai usar

- Claude Desktop aberto e autenticado (resultado da Oficina 1)
- Um arquivo de texto qualquer no seu computador (pode criar um agora)

### 👐 Mão na massa

**Passo 1 — Entenda as três abas em 30 segundos**

Antes de clicar em qualquer coisa, leia o resumo abaixo. É tudo que você precisa saber agora:

| Aba | Para que serve | Acessa arquivos do seu PC? |
|---|---|---|
| Chat | Perguntas, explicações, conversas gerais | Não |
| Code | Trabalhar com arquivos e pastas reais | Sim |
| Cowork | Tarefas automáticas em segundo plano | Sim (avançado) |

> 🤓 **Curiosidade técnica — pode pular sem prejuízo:** A grande diferença entre o Claude via navegador (claude.ai) e o Claude Desktop é exatamente a aba Code. No navegador, você copia e cola. No app, o Claude lê e modifica seus arquivos diretamente — sem você precisar fazer nada manualmente.

**Passo 2 — Teste a aba Chat**

1. Clique na aba "Chat".
2. Na caixa de texto que aparece, digite exatamente o seguinte:

> Explique em duas frases o que é inteligência artificial generativa, como se eu nunca tivesse ouvido esse termo.

3. Pressione Enter ou clique no botão de enviar.
4. Leia a resposta.

Perceba que o Claude respondeu sem precisar de nenhum arquivo seu. Qualquer pergunta conceitual ou dúvida geral vai funcionar exatamente assim — direto, sem configuração.

**Passo 3 — Crie um arquivo de texto simples para usar no próximo passo**

1. Abra o Bloco de Notas (Windows) ou o TextEdit (macOS).
2. Digite o seguinte texto:

```
Meu primeiro projeto com Claude Desktop.
Objetivo: aprender a usar o aplicativo.
Data: hoje.
```

3. Salve o arquivo com o nome `projeto-teste.txt` em uma pasta fácil de encontrar, como a Área de Trabalho ou a pasta Documentos.

**Passo 4 — Teste a aba Code**

1. Clique na aba "Code".
2. Procure um botão chamado "Open Project" (ou ícone de pasta) — geralmente aparece no centro da tela ou no canto superior.
3. Clique nele. Uma janela de navegação vai abrir.
4. Navegue até a pasta onde você salvou o arquivo `projeto-teste.txt`.
5. Selecione a pasta (não o arquivo em si — a pasta inteira) e clique em "Selecionar" ou "Abrir".
6. Aguarde 2 a 3 segundos. O nome dos arquivos da pasta vai aparecer em um painel lateral.

> 📸 **Captura de Tela sugerida:** Faça um print da aba Code com o painel lateral mostrando o arquivo `projeto-teste.txt` — isso confirma que o app leu a pasta corretamente.

7. Na caixa de texto da aba Code, digite:

> Leia o arquivo projeto-teste.txt e me diga o que está escrito lá.

8. Pressione Enter e veja o Claude ler o arquivo e responder.

**Passo 5 — Explore a aba Cowork (só olhando por enquanto)**

1. Clique na aba "Cowork".
2. Observe a interface — ela tem uma aparência diferente das outras.
3. Não crie nenhuma tarefa agora. Por enquanto, basta saber onde fica.

> 📌 **Não esqueça:** A aba Cowork é poderosa, mas é para quando você já se sentir confortável com Chat e Code. Volte a ela depois que terminar este curso.

### ✅ Deu certo?

Você conseguiu que o Claude respondesse uma pergunta na aba Chat e também conseguiu que ele lesse o conteúdo do arquivo `projeto-teste.txt` na aba Code. Se ambos funcionaram, você já entende o que separa as duas abas principais.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não encontro o botão "Open Project" na aba Code | Procure um ícone de pasta no canto superior da tela ou no centro — o texto pode variar dependendo da versão do app |
| O Claude na aba Code diz que não encontrou o arquivo | Confirme que você selecionou a pasta (não o arquivo diretamente) e que o arquivo `.txt` está dentro dessa pasta |
| A aba Chat não está aparecendo ou está em branco | Feche e reabra o app; se o problema persistir, verifique sua conexão com a internet |

### 🚀 Quer ir além?

- Na aba Chat, pergunte ao Claude qual a diferença entre as três abas com suas próprias palavras e compare com o que você aprendeu aqui.
- Tente abrir uma pasta diferente na aba Code e pergunte ao Claude o que ela contém.
- Descubra o atalho de teclado para alternar entre as abas no seu sistema operacional.

---

<div style="page-break-after: always;"></div>

# Oficina 3 — Monte um Projeto Real com Proteção de Dados

### 🎯 O Problema

Você quer usar o Claude Desktop para trabalhar em algo de verdade — um relatório, um conjunto de arquivos de trabalho, um projeto de disciplina. Mas abrir a pasta errada pode expor arquivos que não deveriam sair do computador. Esta oficina ensina a montar a estrutura certa antes de qualquer coisa, protegendo o que precisa ser protegido.

### 🧰 O que você vai usar

- Claude Desktop aberto (Oficina 1)
- Bloco de Notas, TextEdit ou qualquer editor de texto simples
- Terminal ou Prompt de Comando (opcional, mas recomendado)

### 👐 Mão na massa

**Passo 1 — Crie a pasta do projeto no lugar certo**

A regra de ouro é: nunca abra uma pasta grande demais. Crie uma pasta específica para o projeto e abra só ela.

No Windows:
1. Abra o Explorador de Arquivos.
2. Navegue até Documentos (ou outra pasta de sua preferência).
3. Clique com o botão direito, escolha "Nova pasta".
4. Nomeie a pasta como `meu-projeto-claude`.

No macOS:
1. Abra o Finder.
2. Navegue até Documentos.
3. Clique com o botão direito, escolha "Nova pasta".
4. Nomeie como `meu-projeto-claude`.

**Passo 2 — Crie o arquivo README**

O README é como uma plaquinha de identificação do projeto. O Claude lê esse arquivo primeiro quando você abre a pasta — então vale a pena escrever algo útil nele.

1. Abra seu editor de texto.
2. Digite o seguinte (adaptando para o seu contexto):

```
# Meu Projeto com Claude Desktop

## O que é isso
[Descreva brevemente para que serve este projeto]

## O que tem aqui
- README.md: este arquivo de descrição
- .gitignore: lista de arquivos que não devem ser compartilhados

## Como usar
Abrir esta pasta na aba Code do Claude Desktop.
```

3. Salve o arquivo com o nome `README.md` dentro da pasta `meu-projeto-claude`.

> 💡 **Dica:** A extensão `.md` é de Markdown — um formato de texto simples com formatação básica. O Claude lê esse formato muito bem. Não se preocupe se o seu editor mostrar o texto sem formatação visual; isso é normal.

**Passo 3 — Crie o arquivo .gitignore**

O `.gitignore` é a lista de arquivos que o sistema de controle de versão (Git) deve ignorar — e que, por consequência, você não vai compartilhar por acidente. Pense nele como uma lista de exclusão.

1. No editor de texto, crie um novo arquivo.
2. Digite o seguinte:

```
.env
*.key
*.pem
senhas.txt
dados-pessoais/
```

3. Salve como `.gitignore` (com ponto na frente, sem extensão adicional) dentro da pasta `meu-projeto-claude`.

> ⚠️ **Cuidado:** Alguns sistemas operacionais reclamam de arquivos começando com ponto. No Windows, salve pelo Bloco de Notas escolhendo "Todos os arquivos" no tipo de arquivo e digitando `.gitignore` no nome. No macOS, o TextEdit aceita normalmente.

**Passo 4 — Simule um arquivo sensível (para aprender o que proteger)**

1. Crie um novo arquivo de texto.
2. Digite:

```
CHAVE_API=isso_nao_pode_vazar
SENHA_BANCO=exemplo_apenas
```

3. Salve como `.env` dentro da pasta `meu-projeto-claude`.

Agora você tem a estrutura mínima de um projeto protegido:

```
meu-projeto-claude/
├── README.md        ← O Claude lê isso primeiro
├── .gitignore       ← Lista de proteção
└── .env             ← Arquivo sensível (protegido pelo .gitignore)
```

**Passo 5 — Abra o projeto no Claude Desktop e teste**

1. No Claude Desktop, vá para a aba Code.
2. Clique em "Open Project".
3. Navegue até a pasta `meu-projeto-claude` e selecione-a.
4. Na caixa de texto, escreva:

> Você consegue ver os arquivos deste projeto? Liste o que encontrou e me explique para que serve cada arquivo.

5. Leia a resposta. O Claude deve mencionar o `README.md` e o `.gitignore`.

> 📸 **Captura de Tela sugerida:** Print do painel lateral da aba Code com os arquivos do projeto visíveis — serve como comprovação de que a estrutura foi criada corretamente.

**Passo 6 — Confira se o arquivo .env está sendo protegido**

Na caixa de texto, pergunte:

> Você vê algum arquivo chamado .env nesta pasta? Qual é o conteúdo dele?

Observe a resposta. O Claude pode ou não ter acesso ao `.env` dependendo de como o projeto está configurado — o que importa aqui é que você tomou o primeiro passo correto: saber que esse tipo de arquivo existe e precisa de cuidado.

### ✅ Deu certo?

Você criou uma pasta-projeto com três arquivos (`README.md`, `.gitignore`, `.env`), abriu a pasta na aba Code e o Claude conseguiu listar o conteúdo. A estrutura básica de um projeto seguro está no lugar.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não consigo salvar o arquivo `.gitignore` com ponto na frente | No Windows, abra o Bloco de Notas, vá em Arquivo > Salvar Como, mude o tipo para "Todos os arquivos" e digite `.gitignore` no campo do nome |
| O Claude não lista os arquivos ao abrir o projeto | Feche o projeto, clique em "Open Project" novamente e confirme que selecionou a pasta (não um arquivo dentro dela) |
| O Claude diz que não encontrou o README.md | Verifique que o arquivo está salvo com extensão `.md` e não `.md.txt` — editores como o Bloco de Notas costumam adicionar `.txt` automaticamente |

### 🚀 Quer ir além?

- Adicione ao `README.md` uma seção "Objetivos" com três metas reais para o seu uso do Claude Desktop.
- Crie uma segunda pasta dentro de `meu-projeto-claude` e adicione um arquivo de texto nela; depois abra o projeto e pergunte ao Claude se ele vê arquivos em subpastas.
- Pesquise o que é Git e por que ele é útil para quem trabalha com o Claude Desktop (dica: pergunte direto ao Claude na aba Chat).

---

<div style="page-break-after: always;"></div>

# Oficina 4 — Peça Coisas de um Jeito que o Claude Entenda

### 🎯 O Problema

Você digita uma solicitação, o Claude responde algo genérico que não serve para nada, você fica frustrado e acha que a ferramenta não presta. O problema, na maioria das vezes, não é o Claude — é a forma de pedir. Esta oficina ensina a diferença entre um prompt fraco e um prompt que gera resultados úteis de verdade, com exercícios para praticar agora.

### 🧰 O que você vai usar

- Claude Desktop com o projeto da Oficina 3 aberto na aba Code
- Aba Chat disponível para comparações

### 👐 Mão na massa

**Passo 1 — Veja a diferença entre prompt fraco e prompt forte**

1. Abra a aba Chat.
2. Digite o prompt fraco abaixo e envie:

> Melhore meu texto.

3. Observe o que o Claude responde. Provavelmente vai pedir mais informações ou dar uma resposta genérica inútil.

4. Agora envie o prompt forte abaixo (adapte o conteúdo entre colchetes para o seu contexto real):

> Reescreva o parágrafo abaixo usando linguagem formal e impessoal, adequada para um relatório acadêmico. Não altere o significado. Não ultrapasse 80 palavras. Parágrafo: "A gente precisa entender que inteligência artificial não é mágica, ela usa dados pra aprender coisas e responder perguntas."

5. Compare as duas respostas. A diferença de qualidade é o resultado de uma instrução clara.

**Passo 2 — Aprenda a fórmula**

Um prompt eficaz tem até quatro ingredientes. Você não precisa usar todos sempre — mas cada um que você adiciona melhora o resultado:

```
CONTEXTO: O que é este projeto ou texto? Para que serve?
TAREFA:   O que exatamente você quer que o Claude faça?
LIMITE:   O que ele NÃO deve alterar, omitir ou inventar?
FORMATO:  Como você quer a resposta? (lista, parágrafos, tabela, etc.)
```

**Exemplo real com a fórmula:**

Prompt fraco:
> Corrija erros.

Prompt forte usando a fórmula:
> CONTEXTO: Este é um e-mail formal para um reitor de universidade solicitando apoio institucional para uma pesquisa. TAREFA: Corrija erros gramaticais e de concordância verbal. LIMITE: Não mude o conteúdo, os argumentos nem o tom formal. FORMATO: Entregue o e-mail corrigido completo, sem comentários adicionais.

**Passo 3 — Pratique com três cenários**

Para cada prompt fraco abaixo, escreva um prompt forte usando a fórmula. Depois envie o forte ao Claude e veja o resultado.

Cenário A:
> Fraco: "Faça um resumo."
> Forte: (escreva aqui usando a fórmula)

Cenário B:
> Fraco: "Explique isso melhor."
> Forte: (escreva aqui usando a fórmula)

Cenário C:
> Fraco: "Crie uma lista."
> Forte: (escreva aqui usando a fórmula)

> 💡 **Dica:** Se o Claude ainda não entendeu depois do prompt forte, adicione um exemplo do resultado que você espera. "Quero uma resposta parecida com esta: [exemplo]" é uma das formas mais eficazes de calibrar o resultado.

**Passo 4 — Use a aba Code com um prompt contextualizado**

1. Vá para a aba Code com o projeto da Oficina 3 aberto.
2. Digite o seguinte prompt (adaptando o conteúdo entre colchetes):

> CONTEXTO: Este projeto tem um arquivo README.md que descreve [seu contexto]. TAREFA: Reescreva a seção "O que é isso" do README.md deixando o texto mais claro e direto, em no máximo três frases. LIMITE: Não remova nem adicione seções. FORMATO: Entregue apenas o texto novo da seção, sem comentários.

3. Revise o que o Claude propõe na tela de diferenças (diff view) — ela mostra em verde o que foi adicionado e em vermelho o que foi removido.
4. Se gostar, clique em "Accept" (ou equivalente). Se não gostar, clique em "Reject" e reformule o prompt com mais detalhes.

> 📸 **Captura de Tela sugerida:** Print da tela de diff view com o texto original e o proposto lado a lado — é a visualização central do fluxo de trabalho na aba Code.

**Passo 5 — Aprenda a interromper quando necessário**

Às vezes o Claude começa a fazer algo que não era o que você queria. Você não precisa esperar terminar.

1. Digite um pedido amplo na aba Code:

> Reescreva todos os arquivos deste projeto melhorando o texto de cada um.

2. Aguarde 3 a 5 segundos enquanto o Claude começa a processar.
3. Clique no botão "Stop" (ou "Cancel") que aparece durante a resposta.
4. Com o Claude pausado, reformule:

> Na verdade, só quero que você melhore o texto do README.md. Apenas esse arquivo.

5. O Claude vai retomar com o escopo correto.

### ✅ Deu certo?

Você enviou um prompt forte, recebeu uma resposta útil, viu a diff view funcionar e praticou a interrupção para redirecionar o Claude. Se você conseguiu aceitar ou rejeitar uma alteração na aba Code, completou o ciclo fundamental de uso do aplicativo.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O Claude continua dando respostas genéricas mesmo com prompt detalhado | Adicione um exemplo concreto do resultado esperado logo após a fórmula |
| Não encontro o botão "Stop" durante a resposta | Olhe na parte inferior da janela de chat — ele costuma aparecer como um quadrado ou a palavra "Stop" enquanto o Claude está respondendo |
| A diff view não aparece e o Claude simplesmente substitui o arquivo | Verifique se o modo de permissão está em "Ask" (não em "Auto-accept") — procure essa configuração próxima ao botão de enviar |

### 🚀 Quer ir além?

- Peça ao Claude na aba Chat que avalie um prompt que você criou e sugira como melhorá-lo.
- Teste o mesmo prompt com dois tamanhos de contexto (curto e longo) e compare os resultados.
- Crie um arquivo `meus-prompts.md` no projeto com os melhores prompts que você descobriu — vira um repertório pessoal reutilizável.

---

<div style="page-break-after: always;"></div>

# Projeto Final — Sessão de Trabalho Real com o Claude Desktop

### 🎯 A missão

Você praticou cada habilidade separada. Agora é hora de juntar tudo em uma sessão real de trabalho — do zero ao entregável. A missão: montar um projeto, definir uma tarefa concreta da sua área, pedir ao Claude que a execute e revisar o resultado aplicando o que aprendeu nas quatro oficinas.

### 👐 Mão na massa

1. Crie uma pasta nova chamada `projeto-final-claude` em Documentos.

2. Dentro dela, crie um arquivo `README.md` com as seguintes informações preenchidas por você:

```
# [Nome do seu projeto]

## Para que serve
[Descreva em 2-3 frases o que você quer fazer nesta sessão]

## Tarefa desta sessão
[Descreva a tarefa específica que vai pedir ao Claude]

## Critérios de qualidade
[O que o resultado precisa ter para ser considerado bom?]
```

3. Crie também um arquivo `.gitignore` com, no mínimo, a linha `.env`.

4. Crie um arquivo de conteúdo para trabalhar — pode ser um documento de texto, um relatório parcial, uma lista de itens que você quer organizar, um e-mail que precisa revisar. Salve na pasta com um nome claro.

5. Abra a pasta `projeto-final-claude` na aba Code do Claude Desktop.

6. Usando a fórmula aprendida na Oficina 4, escreva um prompt forte para a tarefa que você definiu no README. Envie.

7. Quando o Claude propuser alterações, abra a diff view e revise linha por linha.

8. Aceite o que estiver bom. Rejeite o que não estiver — e peça uma nova versão com mais detalhe sobre o que estava errado.

9. Depois de pelo menos um ciclo de aceitar ou rejeitar, vá para a aba Chat e pergunte:

> Com base no que fizemos nesta sessão, que outros tipos de tarefa você poderia me ajudar a fazer neste projeto?

10. Anote pelo menos uma ideia da resposta que você pretende testar depois.

### 🏁 Como saber que terminou

- [ ] A pasta `projeto-final-claude` existe com `README.md`, `.gitignore` e pelo menos um arquivo de conteúdo
- [ ] O projeto foi aberto na aba Code e o Claude listou os arquivos corretamente
- [ ] Um prompt forte (com pelo menos dois ingredientes da fórmula) foi enviado na aba Code
- [ ] A diff view foi usada para revisar a alteração proposta
- [ ] Pelo menos uma alteração foi aceita ou rejeitada de forma consciente (não aleatória)
- [ ] A aba Chat foi usada para uma consulta relacionada ao projeto
- [ ] Você consegue explicar em voz alta, sem consultar o material, o que cada aba faz

---

<div style="page-break-after: always;"></div>

# A Parte dos Dez — Atalhos e Macetes que Salvam seu Dia

Dez coisas rápidas que você vai querer saber assim que começar a usar o Claude Desktop com mais frequência. Nenhuma precisa de explicação longa.

1. **Escopo mínimo sempre.** Abra apenas a pasta do projeto específico, nunca a pasta inteira do seu usuário. O Claude acessa tudo dentro da pasta que você selecionar.

2. **O README.md é a primeira coisa que o Claude lê.** Quanto melhor escrito, menos você precisa explicar a cada sessão.

3. **Prompt fraco = resultado fraco.** Antes de enviar qualquer pedido na aba Code, passe 30 segundos adicionando contexto, tarefa e limite. Vale o tempo.

4. **Diff view antes de aceitar, sempre.** Não importa o quão confiante você estiver — revise o que mudou antes de clicar em "Accept". O Claude erra, e você é o responsável pelo resultado final.

5. **Stop é seu amigo.** Se perceber que o Claude está indo na direção errada, clique em Stop imediatamente e redirecione. Não espere ele terminar para reclamar.

6. **O modo "Ask Permissions" é o padrão para iniciantes.** Ele pede sua confirmação antes de alterar qualquer arquivo. Só mude para "Auto-accept" quando você confiar muito no que está pedindo — e tiver backup.

7. **Arquivo .env fora do alcance.** Qualquer arquivo com senhas, chaves de API ou credenciais deve estar no `.gitignore`. O Claude pode ler o que estiver na pasta — cuide do que fica lá.

8. **Uma sessão, uma tarefa.** O Claude não lembra de sessões anteriores. Ao abrir o app novamente, o contexto começa do zero. O README.md bem escrito resolve grande parte disso.

9. **Se a resposta foi boa, pergunte o que mais ele pode fazer.** Depois de resolver um problema, pergunte: "Que outros aspectos deste arquivo/projeto você poderia melhorar?" Costuma render boas ideias.

10. **A aba Chat não precisa de projeto aberto.** Para dúvidas rápidas, conceitos, comparações ou brainstorming, use o Chat — é mais rápido e não requer nenhuma configuração.

---

<div style="page-break-after: always;"></div>

# Conseguiu! E agora?

Parabéns — você passou da fase de "tenho medo de clicar no lugar errado" para a fase de "sei o que estou fazendo e por quê". Isso não é pouco. Você instalou o app, entendeu as três abas, montou um projeto com estrutura e proteção de dados, aprendeu a formular pedidos que geram resultados úteis e revisou alterações de forma consciente. É um fluxo de trabalho completo, e você fez tudo isso com as próprias mãos.

A partir daqui, a melhor coisa que você pode fazer é continuar usando. Pegue uma tarefa real da sua semana — um e-mail para revisar, um documento para organizar, um conjunto de anotações para transformar em relatório — e passe pelo mesmo fluxo: abre a pasta, escreve um prompt forte, revisa a diff view, aceita ou rejeita. Cada sessão vai revelar algo novo. Quando sentir que já domina o básico, explore o arquivo `.claude.md` (que permite configurar instruções permanentes para o assistente dentro de um projeto), os modos de permissão avançados e, eventualmente, a aba Cowork para tarefas mais longas. O curso Essentials da mesma trilha cobre esses tópicos com mais profundidade — e agora você tem a base prática para aproveitá-lo de verdade.
