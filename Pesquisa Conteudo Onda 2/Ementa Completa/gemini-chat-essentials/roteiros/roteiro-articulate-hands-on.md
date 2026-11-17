# Gemini Chat Para Leigos — Curso Hands-on

> *» IA: Cover — título e subtítulo; preservar verbatim.*

*Em menos de duas horas, você vai organizar um evento inteiro com o Gemini: da planilha de
inscrições ao evento na sua Agenda e ao comunicado pronto no Documentos Google.*

# Antes de Arregaçar as Mangas

> *» IA: Text — parágrafo verbatim.*

Mão na massa do começo ao fim. O caso é fictício: a associação de moradores de Vila Serena vai
fazer o **Mutirão de Orientação Cidadã**, um sábado de atendimento gratuito sobre consumidor,
previdência, família e trabalho — e quem organiza é você. Cada oficina resolve uma parte; no
Projeto Final, tudo vira um pacote para a coordenação. Duração total: 119 minutos.

> *» IA: Checklist — itens verbatim.*

**O que você precisa ter aberto agora:**

- `gemini.google.com`, `mail.google.com` e `calendar.google.com`, todos com a mesma conta Google
  **pessoal** de maior de 18 anos (as habilidades exigem 18+). O plano gratuito serve.
- Um editor de texto simples e uma pasta chamada `mutirao`.

> *» IA: Process — preparação em dois passos; preservar os breadcrumbs.*

**Preparação (7 min)**

1. Abra `myactivity.google.com/product/gemini` e confira se o **Histórico do Gemini** está
   ativado. A Oficina 3 conecta o Gemini ao Gmail e à Agenda, e isso exige o Histórico ligado. Se o
   seu Gmail recebe e-mails de clientes ou dados sensíveis, faça o curso numa conta pessoal
   secundária: o que o Gemini lê pode entrar no Histórico, e conversas revisadas por pessoas ficam
   até 3 anos.
2. Salve a planilha (bloco abaixo) como `inscricoes-mutirao.csv` — no Bloco de Notas, use
   `Arquivo > Salvar como > Tipo: Todos os arquivos`. Depois, no Gmail, envie para **você mesmo** o
   e-mail de teste (segundo bloco), com o assunto exato.

> *» IA: Statement — arquivo de prática; conteúdo verbatim, sem nenhuma alteração; oferecer também como Download "inscricoes-mutirao.csv".*

Arquivo `inscricoes-mutirao.csv`:

"""
inscricao,tema,turno,canal,acessibilidade
I01,Familia,tarde,site,nao
I02,Consumidor,manha,presencial,nao
I03,Previdencia,tarde,WhatsApp,sim
I04,Trabalho,manha,presencial,nao
I05,Consumidor,manha,site,nao
I06,Trabalho,manha,WhatsApp,sim
I07,Previdencia,manha,presencial,sim
I08,Consumidor,manha,WhatsApp,nao
I09,Previdencia,tarde,WhatsApp,nao
I10,Consumidor,tarde,WhatsApp,nao
I11,Trabalho,manha,presencial,nao
I12,Familia,manha,presencial,nao
I13,Trabalho,tarde,WhatsApp,nao
I14,Previdencia,tarde,presencial,nao
I15,Familia,manha,presencial,nao
I16,Trabalho,tarde,site,nao
I17,Familia,tarde,site,nao
I18,Consumidor,manha,presencial,nao
I19,Previdencia,tarde,WhatsApp,nao
I20,Trabalho,tarde,presencial,nao
I21,Familia,manha,site,nao
I22,Previdencia,tarde,presencial,nao
I23,Consumidor,manha,presencial,nao
I24,Familia,tarde,WhatsApp,nao
I25,Consumidor,tarde,site,nao
I26,Consumidor,tarde,site,nao
I27,Familia,tarde,site,nao
I28,Previdencia,tarde,site,nao
I29,Consumidor,tarde,WhatsApp,nao
I30,Previdencia,tarde,site,sim
"""

> *» IA: Statement — e-mail de teste; assunto e corpo verbatim.*

E-mail para você mesmo — assunto: `Mutirão de Orientação Cidadã — pedido da coordenação`

"""
Olá! Confirmado: o Mutirão de Orientação Cidadã será no sábado, 05/12/2026, das 9h às 17h, no
Centro Comunitário Vila Serena. Precisamos de uma reunião de preparação com os voluntários na
quarta-feira, 02/12/2026, das 15h às 16h, por videochamada. Até sexta-feira, 27/11/2026, preciso do
comunicado aos inscritos e da distribuição das mesas por tema e turno. Cada atendimento dura 30
minutos; manhã das 9h às 12h e tarde das 13h às 17h. Obrigado! — Coordenação (caso fictício)
"""

> *» IA: Statement — regra de ouro; preservar o emoji.*

> 🔑 **Regra de ouro:** o Gemini enxerga sua conta Google — então você decide o que ele vê, e
> confere tudo o que ele escreve na sua Agenda.

# O Mapa da Mão na Massa

> *» IA: Table — verbatim.*

| Oficina | Problema que vai resolver | Tempo |
|---|---|---|
| 1 | Parar de repetir as mesmas instruções em toda conversa | 20 min |
| 2 | Entender 30 inscrições sem contar na mão | 20 min |
| 3 | Achar o pedido no e-mail e marcar a reunião sem digitar nada na Agenda | 20 min |
| 4 | Escrever o comunicado e levá-lo para o Documentos Google | 20 min |
| Projeto Final | Entregar o pacote do mutirão à coordenação | 26 min |

> *» IA: Text — frase verbatim.*

As oficinas são em sequência: a habilidade criada na Oficina 1 acompanha todas as outras.

---

# Oficina 1 — Crie a habilidade do mutirão

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

Toda conversa você explica de novo: "é um caso fictício, use só os códigos, diga de onde tirou...".
Uma **habilidade** — um pacote de instruções salvo, como uma receita guardada — faz isso por você
sempre que você digita "/". (20 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- `Personalizar > Habilidades` (as habilidades substituíram os antigos Gems em novembro de 2026).

### 👐 Mão na massa

> *» IA: Process — um passo por etapa; preservar os breadcrumbs; não traduzir termos de interface.*

1. Abra `Gemini > Menu à esquerda > Personalizar > Habilidades` [conferir] e escolha **Criar
   manualmente**.
2. Nome: `Assistente do Mutirão`. Descrição: `Organização do Mutirão de Orientação Cidadã`.
3. Cole as instruções do bloco abaixo.
4. Salve e confira se a habilidade está ativa.
5. Em `Gemini > Barra lateral > Novo chat`, digite `/Assistente do Mutirão` e pergunte: "Quais são as
   cinco tarefas principais para organizar um mutirão de atendimento de um dia?"

> *» IA: Statement — instruções da habilidade; verbatim, entre aspas triplas.*

"""
Você apoia a organização do Mutirão de Orientação Cidadã (caso fictício). Responda em português do
Brasil, em tópicos curtos. Identifique inscrições só pelo código (I01, I02...). Sempre que usar
dados de arquivo, e-mail ou agenda, diga de onde vieram. Termine toda resposta com uma linha
"Conferir:" listando o que a pessoa deve verificar.
"""

### ✅ Deu certo?

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: a resposta vem em tópicos curtos e termina com a linha **"Conferir:"**.

### 🚑 Se travar

> *» IA: Accordion — um item por linha; título = Problema, corpo = O que fazer.*

| Problema | O que fazer |
|---|---|
| Não existe "Habilidades" | Conta de menor de 18, conta de trabalho/escola ou liberação incompleta. Rota: salve as instruções num arquivo e cole-as no início de cada conversa |
| A habilidade não aparece no "/" | Confira em `Personalizar > Habilidades` se está ativa; recarregue a página |
| Tenho um Gem antigo | Ele migrou como rascunho inativo em `Personalizar`; revise e ative |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL; um desafio por item, com a validação.*

1. Crie a mesma habilidade com **Criar com o Gemini**, descrevendo a função em uma frase.
   Validação: compare as instruções geradas com as suas.
2. Combine `/Assistente do Mutirão` com `/Texto claro` (do Essentials). Validação: a resposta segue
   as duas.
3. Edite a habilidade para exigir "no máximo 8 tópicos". Validação: a próxima resposta respeita o
   limite.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 2 — Planilha de inscrições

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

São 30 inscrições. A coordenação quer saber quantas mesas montar em cada turno e quem precisa de
acessibilidade. (20 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- O envio de arquivos do Gemini.
- O arquivo `inscricoes-mutirao.csv`.

### 👐 Mão na massa

> *» IA: Process — passos verbatim; preservar os breadcrumbs.*

1. Em um chat novo, digite `/Assistente do Mutirão` e envie o CSV em `Gemini > Caixa de mensagem >
   + > Fazer upload de arquivos`.
2. Teste de leitura:

"""
Mostre as 5 primeiras linhas e os nomes das colunas.
"""

3. As contagens:

"""
Conte as inscrições por tema, por turno e por canal. Faça uma tabela tema × turno. Liste os códigos
que pediram acessibilidade.
"""

4. A decisão:

"""
Cada atendimento dura 30 minutos; a manhã tem 6 horários por mesa (9h–12h) e a tarde 8 (13h–17h).
Quantas mesas por tema em cada turno são necessárias?
"""

> *» IA: Statement — preservar o emoji.*

> 💡 **Dica:** confira uma contagem na mão. Procure "Previdencia,tarde" no arquivo (Ctrl+F): são 7.

### ✅ Deu certo?

> *» IA: Table — gabarito verbatim.*

| Indicador | Valor certo |
|---|---|
| Por tema | Consumidor 9, Previdência 8, Família 7, Trabalho 6 |
| Por turno | Tarde 18, manhã 12 |
| Por canal | Presencial 11, site 10, WhatsApp 9 |
| Acessibilidade | 4 inscrições: I03, I06, I07, I30 |
| Maior bloco | Previdência à tarde (7) |
| Mesas | Uma por tema em cada turno basta (maior uso: 7 de 8 horários) |

> *» IA: Statement — preservar o emoji.*

> 🏁 Ponto de controle: os seis indicadores batem com a tabela.

### 🚑 Se travar

> *» IA: Accordion — um item por linha.*

| Problema | O que fazer |
|---|---|
| Contagem diferente | Peça "mostre a contagem linha a linha do tema X" e confira com o arquivo |
| Arquivo recusado | Cole as 31 linhas direto na conversa |
| Apareceram nomes inventados | Lembre: "use só os códigos" — e confira se a habilidade está ativa |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL; preservar os breadcrumbs.*

1. Peça um gráfico de barras por tema e turno. Validação: a barra mais alta é Previdência/tarde.
2. Salve o CSV no Drive e use `Gemini > Caixa de mensagem > + > Adicionar do Drive`. Validação: a
   resposta é a mesma.
3. Pergunte "e se a tarde tivesse só 4 horários por mesa?". Validação: Previdência à tarde passa a
   precisar de 2 mesas.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 3 — Gmail e Agenda

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

O pedido da coordenação está no seu e-mail, com três datas diferentes. Você quer o resumo e a
reunião marcada — sem copiar nada à mão. (20 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- Os apps do Google conectados ao Gemini (Gmail e Google Agenda).
- O e-mail de teste que você mandou para si mesmo.

### 👐 Mão na massa

> *» IA: Process — passos verbatim; preservar os breadcrumbs.*

1. Abra `Gemini > Menu à esquerda > Personalizar > Apps` [conferir] e conecte **Gmail** e **Google
   Agenda**. O Gemini pede autorização; leia e aceite.
2. Em um chat novo, com `/Assistente do Mutirão`, peça:

"""
Encontre no meu Gmail o e-mail com assunto "Mutirão de Orientação Cidadã — pedido da coordenação"
e liste todas as datas, horários e prazos.
"""

3. Depois:

"""
Crie na minha Agenda o evento "Reunião de preparação — Mutirão" na quarta-feira, 02/12/2026, das
15h às 16h.
"""

4. Confirme quando o Gemini pedir e abra `calendar.google.com` no dia 02/12/2026.

> *» IA: Statement — preservar o emoji.*

> ⚠️ **Cuidado:** cite sempre o assunto exato. Pedidos como "resuma meus e-mails" fazem o Gemini
> ler mensagens que você não escolheu.

### ✅ Deu certo?

> *» IA: Statement — gabarito verbatim; preservar o emoji.*

> 🏁 Ponto de controle: três datas listadas, com o Gmail citado como origem — **mutirão em
> 05/12/2026, 9h–17h**; **reunião em 02/12/2026, 15h–16h**; **prazo em 27/11/2026** — e o evento
> visível em `Google Agenda > 02/12/2026`, das 15h às 16h.

### 🚑 Se travar

> *» IA: Accordion — um item por linha.*

| Problema | O que fazer |
|---|---|
| "Não consigo acessar seu Gmail" | Histórico desativado ou app não conectado: reveja a preparação e `Personalizar > Apps` |
| E-mail não encontrado | Confira se ele chegou na Caixa de entrada; cite o assunto entre aspas |
| Evento em horário errado | Confira o fuso da Agenda (horário de Brasília); peça a correção ou ajuste no próprio evento |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL.*

1. Peça para incluir no evento a descrição "Pauta: mesas e comunicado". Validação: abra o evento e
   confira.
2. Peça um rascunho de resposta à coordenação. Validação: o Gemini não envia nada sem você.
3. Desconecte o Gmail em `Personalizar > Apps` e repita o passo 2. Validação: o acesso acabou.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 4 — Comunicado no Canvas

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Text — verbatim.*

O comunicado aos inscritos precisa ser claro para quem nunca foi a um atendimento jurídico — e ir
para um documento que a coordenação consiga abrir. (20 min)

### 🧰 O que você vai usar

> *» IA: List — verbatim.*

- O **Canvas**: uma folha de rascunho ao lado da conversa, que você edita direto.
- A exportação para o Documentos Google.

### 👐 Mão na massa

> *» IA: Process — passos verbatim; preservar os breadcrumbs.*

1. Em um chat novo, com `/Assistente do Mutirão`, abra `Gemini > Caixa de mensagem > Ferramentas >
   Canvas`.
2. Peça:

"""
Escreva um comunicado aos inscritos do Mutirão de Orientação Cidadã: sábado, 05/12/2026, das 9h às
17h, no Centro Comunitário Vila Serena; atendimento de 30 minutos por ordem de turno; levar
documento com foto e papéis do caso. Linguagem simples, até 150 palavras.
"""

3. No Canvas, selecione a frase mais difícil e peça "mais simples".
4. Exporte em `Canvas > Compartilhar/Exportar > Exportar para o Documentos` [conferir].

### ✅ Deu certo?

> *» IA: Statement — preservar o emoji.*

> 🏁 Ponto de controle: em `Google Drive > Meu Drive`, um documento com o comunicado — data,
> horário, local, duração do atendimento e o que levar —, em até 150 palavras.

### 🚑 Se travar

> *» IA: Accordion — um item por linha.*

| Problema | O que fazer |
|---|---|
| O Canvas não abre | Peça "abra no Canvas"; confira o limite do plano gratuito |
| Data ou local errado | Corrija direto no Canvas — ele é editável |
| Não acho a exportação | Procure no menu de compartilhar do Canvas; alternativa: copiar e colar num documento novo |

### 🚀 Quer ir além?

> *» IA: Accordion — marcado como OPCIONAL.*

1. Peça uma versão de 3 linhas para WhatsApp. Validação: no máximo 3 linhas.
2. Peça "crie uma imagem simples para o cartaz do mutirão". Validação: confira data e local na
   imagem — imagens geradas costumam errar texto.
3. Peça a versão formal para um ofício à prefeitura. Validação: o tom muda e os dados continuam
   certos.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Projeto Final — Pacote do mutirão

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Projeto Final" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 A missão

> *» IA: Text — verbatim.*

A coordenação pediu, para 27/11, o comunicado e a distribuição das mesas. Monte um único documento
com tudo, conferido, e deixe a reunião de preparação na Agenda. (26 min)

### 👐 Mão na massa

> *» IA: Process — passos verbatim; preservar os breadcrumbs.*

1. Em um chat novo, com `/Assistente do Mutirão` e o Canvas aberto (`Ferramentas > Canvas`), envie o
   CSV de novo ou use `+ > Adicionar do Drive`.
2. Peça:

"""
Monte o "Pacote do Mutirão" em quatro seções: (1) Resumo do pedido da coordenação, com as datas do
e-mail no Gmail; (2) Distribuição de mesas por tema e turno, com as contagens da planilha;
(3) Atendimento com acessibilidade, só com os códigos; (4) Comunicado aos inscritos.
"""

3. Confira cada número com o gabarito da Oficina 2 e cada data com o e-mail.
4. Exporte para o Documentos Google com o título `Pacote do Mutirão`.
5. Confira em `Google Agenda > 02/12/2026` que o evento de preparação continua lá.

### 🏁 Como saber que terminou

> *» IA: Checklist — itens verbatim.*

- [ ] Documento `Pacote do Mutirão` no Drive, com as quatro seções.
- [ ] Datas certas: 05/12 (9h–17h), 02/12 (15h–16h) e prazo em 27/11.
- [ ] Contagens certas: 9/8/7/6 por tema; 12 de manhã e 18 à tarde; uma mesa por tema e turno.
- [ ] Acessibilidade só com códigos: I03, I06, I07, I30.
- [ ] Evento de preparação na Agenda.
- [ ] Nenhum dado real de pessoa; Gmail desconectado ao terminar, se você preferir.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Projeto Final" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# A Parte dos Dez — Atalhos do Gemini

> *» IA: List — numerada, verbatim.*

1. **"/" chama suas habilidades.** Instrução repetida vira habilidade.
2. **Cite o assunto exato** ao pedir algo do Gmail; nada de "resuma meus e-mails".
3. **Chat temporário** para o que não deve ir para o Histórico.
4. **O Histórico é a chave dos apps.** Sem ele, Gmail e Agenda não respondem.
5. **Primeiro as 5 linhas** de qualquer planilha.
6. **Canvas para o texto que vai sair do Gemini** — e exporte para o Documentos.
7. **Confira a Agenda** depois que o Gemini criar um evento.
8. **Verifique a resposta** com a Pesquisa Google, mas confie no trecho que você leu.
9. **Alt + Espaço** abre o Gemini no Windows sem sair do que você está fazendo.
10. **"O que você sabe sobre mim?"** mostra a memória; apague o que não deve ficar.

## Conseguiu! E agora?

> *» IA: Text — dois parágrafos verbatim.*

Você organizou um evento inteiro conversando: a planilha virou decisão, o e-mail virou compromisso
na Agenda, o rascunho virou documento. E você conferiu cada número — é isso que separa ajuda de
risco.

Para continuar, crie uma habilidade para uma tarefa que você repete toda semana. Depois, siga para
*Gemini Workspace - Essentials*, o Gemini dentro do Gmail e do Documentos, ou para *Deep Research -
Hands On*.
