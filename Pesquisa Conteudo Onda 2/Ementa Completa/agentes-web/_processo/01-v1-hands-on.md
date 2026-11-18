# Agentes Web Para Leigos - Curso Hands-on

*Ao final, voce tera conduzido e auditado uma tarefa web sem criar compromisso externo.*

## Antes de Arregacar as Mangas

Este curso e pratica guiada: voce vai limitar, observar, interromper e verificar um agente web em ambiente seguro.

O que voce precisa ter aberto agora:

- conta de treinamento no Comet ou ChatGPT Work;
- editor de texto;
- Selenium Web Form, Wikipedia, gov.br e BlazeDemo;
- nenhum dado pessoal, cartao ou conta produtiva.

> 🔑 Regra de ouro: o agente prepara; voce decide, confirma e assume qualquer compromisso.

## O Mapa da Mao na Massa

| Oficina | Problema | Tempo |
|---|---|---:|
| 1 | Preparar um ambiente restrito | 17 min |
| 2 | Comparar fontes com rastreabilidade | 20 min |
| 3 | Preencher sem enviar e intervir | 20 min |
| 4 | Planejar em sandbox e parar a tempo | 20 min |
| Projeto Final | Produzir um dossie auditavel | 10 min |

As oficinas formam uma sequencia de pequenas vitorias e podem usar qualquer uma das ferramentas elegiveis.

---

# Oficina 1 - Feche as portas antes de comecar

### 🎯 O Problema

Voce precisa usar um agente sem entregar acesso amplo demais.

### 🧰 O que voce vai usar

- conta de treino;
- pagina publica;
- ficha LIMITE.

### 👐 Mao na massa

1. Confirme que nao ha cartao, dados reais ou sistema produtivo aberto.
2. No ChatGPT Work, revise `Settings > Cloud browser`; no Comet, revise `Settings > Privacy and security`.
3. Escolha a opcao mais restritiva disponivel e anote o rotulo exato.
4. Escreva objetivo, sites, dados, acoes permitidas, proibidas, parada e evidencia.
5. Peca apenas o resumo da pagina publica e confira titulo e URL.

### ✅ Deu certo?

Ha uma ficha completa e a resposta cita somente a pagina autorizada.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Menu nao aparece | Confira plano, regiao, conta e politica do workspace. |
| O agente abre outro site | Pause e restrinja explicitamente o dominio. |

### 🚀 Quer ir alem?

Repita com a segunda ferramenta e compare o isolamento local/remoto.

---

# Oficina 2 - Compare sem perder a fonte

### 🎯 O Problema

Uma sintese convincente nao basta: cada linha precisa voltar a uma fonte publica.

### 🧰 O que voce vai usar

- duas paginas publicas oficiais;
- tabela com titulo, URL, data e evidencia.

### 👐 Mao na massa

1. Abra duas paginas autorizadas sobre o mesmo tema.
2. Instrua o agente a usar somente essas paginas.
3. Peca uma tabela com criterio, valor, URL e trecho de apoio parafraseado.
4. Pause se surgir terceiro dominio.
5. Abra cada URL e confira ao menos cinco celulas.
6. Marque cada linha como confirmada, divergente ou nao encontrada.

### ✅ Deu certo?

Todas as linhas possuem URL aberta e apoio verificavel.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O agente usa snippet | Exija pagina original e marque acesso parcial. |
| A data nao aparece | Registre "nao encontrada"; nao invente. |
| Paywall bloqueia | Procure fonte primaria aberta ou exclua a linha. |

### 🚀 Quer ir alem?

Adicione uma coluna de divergencias e explique qual fonte prevalece.

---

# Oficina 3 - Preencha, pause e nao envie

### 🎯 O Problema

Voce quer delegar preenchimento sem permitir envio ou uso de dados sensiveis.

### 🧰 O que voce vai usar

- Selenium Web Form;
- valores ficticios;
- controle de pausa ou takeover.

### 👐 Mao na massa

1. Abra `https://www.selenium.dev/selenium/web/web-form.html`.
2. Autorize somente esse dominio.
3. Instrua o agente a preencher Text input, Textarea, Dropdown e Checkbox.
4. Proiba Password, File input e Submit.
5. Pause durante a execucao e confira a tela.
6. Assuma o controle se a ferramenta oferecer takeover; nao envie.
7. Recarregue ou feche a pagina para desfazer.

### ✅ Deu certo?

Os quatro campos estao corretos, os campos proibidos permanecem vazios e Submit nao foi acionado.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| CAPTCHA ou login | Assuma o controle; nunca cole senha ou MFA no chat. |
| O agente tenta enviar | Pare, cancele e revise o prompt. |
| Sucesso sem evidencia | Confira o estado visual e o historico. |

### 🚀 Quer ir alem?

Refaca com uma instrucao mal definida e registre qual limite fez falta.

---

# Oficina 4 - Planeje e pare antes do compromisso

### 🎯 O Problema

Uma tarefa de viagem parece inocente, mas pode chegar a compra e dados pessoais.

### 🧰 O que voce vai usar

- BlazeDemo;
- dados ficticios;
- regra de parada.

### 👐 Mao na massa

1. Abra `https://blazedemo.com/`.
2. Escolha origem e destino ficticios.
3. Peca ao agente para comparar opcoes por horario e preco.
4. Permita chegar ao formulario seguinte com dados ficticios.
5. Proiba `Purchase Flight` e qualquer pagamento.
6. Confira preco, rota, estado da pagina e ausencia de confirmacao.
7. Feche a pagina e registre o que foi desfeito.

### ✅ Deu certo?

Ha uma opcao justificada e nenhuma compra, reserva ou dado real foi criado.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Site bloqueia automacao | Conclua manualmente ou use outro sandbox autorizado. |
| Preco muda | Registre data e hora; nao esconda a divergencia. |
| Pagina pede dado real | Pare e use dado ficticio ou encerre. |

### 🚀 Quer ir alem?

Inclua uma matriz reversivel, confirmacao obrigatoria e humano executa.

---

# Projeto Final - Dossie de delegacao segura

### 🎯 A missao

Produza um dossie de pesquisa ou compra sem compra, com escopo, prompt, plano, log e auditoria.

### 👐 Mao na massa

1. Escolha um objetivo de baixo risco e tres sites publicos.
2. Escreva o prompt LIMITE completo.
3. Revise o plano antes da execucao.
4. Observe e registre dominios e intervencoes.
5. Verifique cinco afirmacoes nas fontes.
6. Confirme que nenhum compromisso foi criado.

### 🏁 Como saber que terminou

- [ ] Escopo e parada estao explicitos.
- [ ] Nenhum dado real foi usado.
- [ ] Cada afirmacao tem URL e status.
- [ ] Intervencoes e efeitos foram registrados.
- [ ] Nao houve envio, compra, publicacao ou alteracao de conta.

# A Parte dos Dez - Atalhos que evitam dor de cabeca

1. Comece pela parada, nao pelo prompt.
2. Use conta de treino.
3. Autorize o minimo de dominios.
4. Nunca cole senha, MFA, token ou CVV.
5. Abra a fonte original.
6. Confira o efeito no site.
7. Pare diante de instrucao da pagina.
8. Prefira rascunho sem envio.
9. Registre data, URL e acao.
10. Limpe sessoes ao final.

# Conseguiu! E agora?

Voce ja consegue conduzir uma tarefa web com limites e evidencia. Repita o ciclo em cenarios de baixo risco antes de propor uso institucional.

