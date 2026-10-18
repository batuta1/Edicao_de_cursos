# MCP Para Leigos — Curso Hands-on

*Em pouco mais de uma hora, você vai ligar o seu assistente de IA a outros aplicativos e fazê-lo trabalhar por você.*

# Antes de Arregaçar as Mangas

Este curso é mão na massa. Nada de teoria comprida: você vai conectar o Claude e o ChatGPT a
serviços que já usa e ver o assistente buscando informação e fazendo coisas de verdade.

**O que você precisa ter aberto agora:**

- O Claude ou o ChatGPT, com sua conta.
- Sua conta do Google.
- Um café (opcional, mas recomendado).

> 🔑 **Regra de ouro:** se o assistente pedir para fazer algo, leia antes de clicar em permitir.

# O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1 | Seu assistente não sabe nada do que está fora da conversa | 15 min |
| 2 | Você perde tempo procurando arquivos no Drive | 15 min |
| 3 | Sua agenda vive bagunçada | 15 min |
| 4 | Você quer que o assistente mande e-mails por você | 15 min |
| Projeto Final | Monte seu assistente conectado | 20 min |

Dá para fazer em sequência: cada oficina entrega uma pequena vitória.

---

# Oficina 1 — Ligue seu primeiro conector

### 🎯 O Problema

Você pergunta algo ao assistente sobre um serviço que usa e ele responde de forma genérica, porque
não tem acesso a nada fora da conversa. Vamos mudar isso.

### 🧰 O que você vai usar

- Claude ou ChatGPT.

### 👐 Mão na massa

1. No Claude, vá em Customize > Connectors.
2. Clique em Add custom connector.
3. Cole a URL de um servidor MCP.
4. Clique em Add.
5. Faça uma pergunta que use o conector.

### ✅ Deu certo?

O conector aparece na lista.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não acho o menu | Procure nas configurações |
| Deu erro | Tente de novo |

### 🚀 Quer ir além?

Faça o mesmo no ChatGPT, pelo menu de Plugins.

---

# Oficina 2 — Encontre arquivos no Google Drive

### 🎯 O Problema

Você sabe que o relatório do mês passado está em algum lugar do Drive, mas não lembra onde.

### 🧰 O que você vai usar

- Claude com o conector do Google Drive.

### 👐 Mão na massa

1. Em Customize > Connectors, procure Google Drive.
2. Clique em Connect e faça login no Google.
3. Na conversa, peça:

> Encontre o relatório mais recente no meu Drive e faça um resumo.

### ✅ Deu certo?

O Claude encontra o arquivo e faz o resumo.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não encontra o arquivo | Diga o nome exato |
| Pede login de novo | Faça login |

### 🚀 Quer ir além?

Peça para ele comparar dois arquivos.

> 💡 **Dica:** quanto mais específico o pedido, melhor o resultado.

---

# Oficina 3 — Organize sua agenda

### 🎯 O Problema

Sua semana está cheia e você não sabe onde encaixar uma reunião.

### 🧰 O que você vai usar

- Claude com o conector do Google Calendar.

### 👐 Mão na massa

1. Conecte o Google Calendar como fez com o Drive.
2. Peça:

> Veja minha agenda da semana e marque uma reunião de 30 minutos no primeiro horário livre.

3. Aprove a criação do evento.

### ✅ Deu certo?

O evento aparece na sua agenda.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Criou no horário errado | Apague o evento e peça de novo |
| Não aparece | Atualize a agenda |

### 🚀 Quer ir além?

Peça para ele convidar um colega.

---

# Oficina 4 — Deixe o assistente cuidar dos e-mails

### 🎯 O Problema

Responder e-mails repetitivos toma sua manhã inteira.

### 🧰 O que você vai usar

- Claude com o conector do Gmail.

### 👐 Mão na massa

1. Conecte o Gmail.
2. Peça:

> Leia meus últimos 5 e-mails e responda os que forem simples.

3. Aprove os envios.

### ✅ Deu certo?

As respostas aparecem na pasta Enviados.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Ele não envia | Verifique se aprovou |
| Resposta ficou estranha | Peça para reescrever |

### 🚀 Quer ir além?

Peça para ele criar marcadores para organizar a caixa de entrada.

> ⚠️ **Cuidado:** confira cada e-mail antes de aprovar.

---

# Projeto Final — Seu assistente conectado

### 🎯 A missão

Conectar todos os serviços das oficinas e usar o assistente para planejar seu dia.

### 👐 Mão na massa

1. Confira se Drive, Calendar e Gmail estão conectados.
2. Peça ao assistente um resumo do seu dia com base na agenda, nos e-mails e nos arquivos.
3. Peça para ele marcar o que for necessário.

### 🏁 Como saber que terminou

- [ ] Três conectores ativos
- [ ] Resumo do dia gerado
- [ ] Pelo menos uma ação executada

# A Parte dos Dez — Conectores que Salvam seu Dia

1. Google Drive
2. Gmail
3. Google Calendar
4. Notion
5. Slack
6. GitHub
7. Canva
8. Asana
9. Dropbox
10. Microsoft 365

# Conseguiu! E agora?

Parabéns! Seu assistente agora conversa com os aplicativos que você usa. Continue testando novos
conectores e descubra quanto tempo dá para economizar.
