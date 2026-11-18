# Agentes Web Para Leigos - Curso Hands-on

**Público-alvo:** profissionais que concluíram Agentes Web - Essentials ou dominam seus conceitos.  
**Objetivo geral:** conduzir e auditar uma tarefa web em ambiente seguro, sem criar compromisso externo.  
**Pré-requisitos:** conta elegível no Comet ou ChatGPT Work, navegador atualizado e perfil de treinamento.  
**Carga horária:** 87 minutos. Formato autoinstrucional e assíncrono.

## Estrutura do Curso

- Nível 1 - Preparação e rastreabilidade: Oficinas 1 e 2.
- Nível 2 - Ação controlada: Oficinas 3 e 4.
- Integração: Projeto Final.

> Se nenhum agente estiver disponível na sua conta, faça as decisões e preencha as fichas, mas adie a execução até obter acesso autorizado.

---

## Oficina 1 - Feche as portas antes de começar

## Descrição

- **Objetivos da Aula:** ensinar a verificar elegibilidade, reduzir permissões e escrever uma ficha LIMITE.
- **Habilidades Esperadas:** preparar um ambiente de treino e executar uma leitura restrita a uma página.

### 🎯 O Problema

- **📸 Sugestão de Prints:** perfil de treino sem contas produtivas e ficha LIMITE ao lado; destacar Sites e Parada.

Você precisa usar um agente sem entregar acesso amplo demais.

### 🧰 O que você vai usar

- conta de treinamento;
- uma página pública;
- ficha com Objetivo, Sites, Dados, Permitido, Proibido, Parada e Evidência.

### 👐 Mão na massa

1. Feche contas produtivas e confirme que não há cartão ou dados reais no perfil.
2. No ChatGPT Work, revise `Settings > Cloud browser`; no Comet, revise `Settings > Privacy and security`.
3. Escolha a opção mais restritiva disponível e registre o rótulo real da sua interface.
4. Preencha a ficha LIMITE e proíba envio, compra, publicação, exclusão e alteração de conta.
5. Peça: “Resuma somente esta página em três itens e informe título e URL. Não abra outros sites.”
6. Confira se título e URL pertencem à página aberta.

### ✅ Deu certo?

Você tem uma ficha completa e uma resposta apoiada apenas no domínio autorizado.

### Verificação formativa

**Pergunta:** Qual opção é mais segura para a aula? A) Always allow; B) permissão restritiva ou pergunta por novo site; C) conta corporativa principal.  
**Gabarito:** B. **Feedback:** a aula exige menor privilégio e decisão por domínio.

### 🚑 Se travar - Solução de Problemas

| Problema | O que fazer |
|---|---|
| Menu não aparece | Confira plano, região, atualização, conta e política do workspace. |
| Rótulo é diferente | Registre o nome atual; não force tradução. |
| Abriu outro domínio | Pause, remova a permissão e reescreva o escopo. |

### 🚀 Quer ir além?

Compare o que fica local e remoto nas duas ferramentas e valide a resposta na documentação.

---

## Oficina 2 - Compare sem perder a fonte

## Descrição

- **Objetivos da Aula:** ensinar pesquisa restrita, tabela rastreável e conferência célula a célula.
- **Habilidades Esperadas:** produzir uma comparação em que cada afirmação tenha origem e status.

### 🎯 O Problema

- **📸 Sugestão de Prints:** tabela com colunas Critério, Achado, Título da fonte, URL, Data e Status; destacar Status.

Uma síntese convincente não basta: cada linha precisa voltar à página original.

### 🧰 O que você vai usar

- duas páginas públicas oficiais;
- a tabela-modelo;
- agente configurado na Oficina 1.

### 👐 Mão na massa

1. Abra duas páginas oficiais sobre o mesmo tema.
2. Autorize somente os dois domínios.
3. Peça uma tabela com Critério, Achado, Título, URL, Data e Status.
4. Exija que “não encontrado” permaneça explícito.
5. Pause se surgir terceiro domínio ou snippet sem página original.
6. Abra cada URL e confira cinco células.
7. Marque cada linha como confirmada, divergente ou não encontrada.

### ✅ Deu certo?

As URLs abrem, cinco células foram conferidas e nenhuma lacuna foi preenchida por suposição.

### Verificação formativa

**Pergunta:** A página está atrás de paywall e o agente mostra apenas um snippet. O status correto é: A) confirmado; B) acesso parcial; C) fonte integral.  
**Gabarito:** B. **Feedback:** snippet não prova leitura do conteúdo integral.

### 🚑 Se travar - Solução de Problemas

| Problema | O que fazer |
|---|---|
| Data ausente | Marque “não encontrada”. |
| Fonte contraditória | Registre a divergência e prefira a fonte primária vigente. |
| Agente inventa citação | Remova a linha e refaça com URLs fornecidas manualmente. |

### 🚀 Quer ir além?

Adicione uma coluna “decisão humana” e justifique qual evidência prevalece.

---

## Oficina 3 - Preencha, pause e não envie

## Descrição

- **Objetivos da Aula:** ensinar preenchimento controlado, pausa, takeover e desfazer.
- **Habilidades Esperadas:** preencher quatro campos fictícios sem tocar em segredo, arquivo ou Submit.

### 🎯 O Problema

- **📸 Sugestão de Prints:** Selenium Web Form com Text input, Textarea, Dropdown e Checkbox destacados; Password, File input e Submit com sinal de bloqueio.

Você quer delegar o rascunho de um formulário sem criar um envio.

### 🧰 O que você vai usar

- `https://www.selenium.dev/selenium/web/web-form.html`;
- valores fictícios;
- pausa ou takeover da ferramenta disponível.

### 👐 Mão na massa

1. Abra o Selenium Web Form e autorize apenas `selenium.dev`.
2. Instrua o agente a preencher Text input com “Treino Agente Web”.
3. Preencha Textarea com “rascunho sem dados pessoais”.
4. Escolha uma opção no Dropdown e marque uma Checkbox.
5. Proíba Password, File input e Submit.
6. Pause durante a execução e confira os quatro campos.
7. Use takeover se for necessário corrigir manualmente; nunca informe credenciais pelo chat.
8. Recarregue ou feche a página para desfazer.

### ✅ Deu certo?

Os quatro campos estão corretos, os campos proibidos estão vazios e não há página de confirmação.

### Verificação formativa

**Pergunta:** O agente pede um código MFA no chat. O que fazer? A) enviar; B) usar takeover e digitar somente no controle seguro; C) publicar o código.  
**Gabarito:** B. **Feedback:** credenciais e MFA não devem entrar na conversa.

### 🚑 Se travar - Solução de Problemas

| Problema | O que fazer |
|---|---|
| O agente tenta Submit | Pare, cancele e reescreva o ponto de parada. |
| CAPTCHA aparece | Resolva como humano ou encerre; não peça contorno. |
| Diz “concluído” sem mostrar | Confira estado visual e ausência de efeito externo. |

### 🚀 Quer ir além?

Refaça com um limite removido e identifique qual comportamento ficou ambíguo.

---

## Oficina 4 - Planeje e pare antes do compromisso

## Descrição

- **Objetivos da Aula:** aplicar reversibilidade e ponto de parada num fluxo com aparência de compra.
- **Habilidades Esperadas:** comparar opções em sandbox, chegar ao formulário e encerrar antes de qualquer confirmação.

### 🎯 O Problema

- **📸 Sugestão de Prints:** BlazeDemo com origem/destino e lista de voos; destacar preço e botão Purchase Flight como proibido.

Uma tarefa de viagem pode avançar de comparação para compromisso financeiro sem uma fronteira clara.

### 🧰 O que você vai usar

- `https://blazedemo.com/`;
- dados fictícios;
- regra “pare antes de Purchase Flight”.

### 👐 Mão na massa

1. Abra o BlazeDemo e autorize apenas `blazedemo.com`.
2. Escolha origem e destino fictícios.
3. Peça comparação por horário e preço.
4. Selecione uma opção e permita chegar ao formulário seguinte.
5. Use somente dados fictícios.
6. Proíba `Purchase Flight` e qualquer pagamento.
7. Confira rota, preço, estado da página e ausência de confirmação.
8. Feche a página e registre como o estado foi desfeito.

### ✅ Deu certo?

Há uma opção justificada e nenhuma compra, reserva, pagamento ou dado real foi criado.

### Verificação formativa

**Pergunta:** O site pede cartão para continuar. A ação correta é: A) usar cartão real; B) parar antes do campo e registrar o limite; C) pedir cartão ao agente.  
**Gabarito:** B.

### 🚑 Se travar - Solução de Problemas

| Problema | O que fazer |
|---|---|
| Site bloqueia automação | Conclua manualmente ou use outro sandbox autorizado; não contorne. |
| Preço mudou | Registre data e hora e atualize a comparação. |
| Página pede dado real | Pare e encerre. |

### 🚀 Quer ir além?

Classifique cada etapa como reversível, confirmação obrigatória ou humano executa.

---

## Projeto Final - Dossiê de delegação segura

## Descrição

- **Objetivos da Aula:** integrar escopo, execução, intervenção, verificação e registro.
- **Habilidades Esperadas:** entregar um dossiê auditável de uma tarefa de baixo risco sem compromisso externo.

### 🎯 A missão

- **📸 Sugestão de Prints:** dossiê de uma página com seções Escopo, Prompt, Plano, Log, Auditoria de cinco afirmações e Efeito final.

Escolha uma pesquisa ou comparação simples e entregue o registro completo. Para caber no tempo, use uma ficha previamente preparada e limite a auditoria a cinco afirmações.

### 👐 Mão na massa

1. Escolha um objetivo de baixo risco e até três sites públicos.
2. Escreva um prompt LIMITE completo.
3. Revise o plano antes de autorizar.
4. Observe e registre domínios, pausas e takeover.
5. Verifique cinco afirmações nas páginas originais.
6. Confirme o estado externo e registre que nenhum compromisso foi criado.

### 🏁 Como saber que terminou

- [ ] Objetivo, sites, dados, ações e parada estão explícitos.
- [ ] Nenhum dado real, senha, MFA, token ou cartão foi usado.
- [ ] Cada afirmação auditada tem URL e status.
- [ ] Intervenções e efeitos foram registrados.
- [ ] Não houve envio, compra, publicação, exclusão ou alteração de conta.

# A Parte dos Dez - Atalhos que evitam dor de cabeça

1. Comece pela parada, não pelo prompt.
2. Use conta de treino.
3. Autorize o mínimo de domínios.
4. Nunca cole senha, MFA, token ou CVV.
5. Abra a fonte original.
6. Confira o efeito no site.
7. Pare diante de instrução da página.
8. Prefira rascunho sem envio.
9. Registre data, URL e ação.
10. Limpe sessões ao final.

# Conseguiu! E agora?

Você já consegue conduzir uma tarefa web com limites e evidência. Repita o ciclo em cenários de baixo risco antes de propor uso institucional.

## Pendências de validação

- Confirmar os rótulos atuais de pausa, cancelamento e takeover.
- Testar os sandboxes e a disponibilidade das ferramentas no Brasil antes da publicação.
- Confirmar comportamento de downloads, limpeza de cookies e limites da conta usada na gravação.

