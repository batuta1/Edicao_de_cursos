# Codex Para Leigos — Curso Hands-on

*Em menos de 90 minutos, você vai sair deste curso com uma tarefa real entregue por um agente de IA — não apenas com uma explicação sobre como isso funciona.*

---

## Antes de Arregaçar as Mangas

Esquece a ideia de curso onde você passa a primeira hora só ouvindo teoria antes de encostar em qualquer coisa. Aqui a lógica é inversa: você vai abrir o Codex já na primeira oficina, e vai sair do curso com pelo menos uma tarefa de verdade — feita por um agente de IA, revisada por você — pronta para valer. Não é preciso saber programar como profissional para acompanhar; é preciso, sim, topar clicar, testar e errar um pouco pelo caminho.

**O que você precisa ter aberto agora:**

- Um navegador (Chrome, Edge ou similar) em chatgpt.com
- Uma conta no ChatGPT (o plano gratuito já é suficiente para acompanhar o curso)
- Uma conta gratuita no GitHub (vamos usá-la na Oficina 2 — se ainda não tiver uma, pode criar na hora, em poucos minutos)

> 🔑 **Regra de ouro:** o primeiro prompt quase nunca sai perfeito — e tudo bem. Ajustar o pedido faz parte do processo, não é sinal de que você fez algo errado.

---

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1. Descobrindo o Que o Codex Faz por Você | "Eu preciso de uma resposta ou preciso que alguém *faça* o trabalho?" | 15 min |
| 2. Preparando Sua Sala de Trabalho | Você tem uma conta, mas o Codex ainda não tem onde trabalhar | 20 min |
| 3. Pedindo (Direito) Sua Primeira Tarefa | Seu primeiro pedido saiu torto — e agora, o que fazer? | 20 min |
| 4. Conferindo o Trabalho do Seu Agente | O agente disse "pronto". Mas será que está, mesmo? | 15 min |
| Projeto Final | Entregar, do início ao fim, uma tarefa real pronta para revisão | 15 min |

As oficinas foram desenhadas para serem feitas em sequência: cada uma entrega uma pequena vitória concreta e deixa o terreno pronto para a próxima. Tempo total estimado do curso: cerca de 85 minutos.

---

# Oficina 1 — Descobrindo o Que o Codex Faz por Você

### 🎯 O Problema

Você abre o ChatGPT para resolver alguma coisa chata: "preciso arrumar um trecho do meu projeto" ou "preciso montar um relatório". Só que um chat comum te dá uma resposta — e quem faz o trabalho continua sendo você. Nesta oficina você vai sentir, na prática, a diferença entre *perguntar* para uma IA e *delegar* uma tarefa a ela.

### 🧰 O que você vai usar

- Navegador aberto em chatgpt.com
- Conta no ChatGPT (login feito)

### 👐 Mão na massa

1. Entre em chatgpt.com e faça login (ou crie uma conta gratuita, caso ainda não tenha).
2. Localize o Codex no menu lateral do ChatGPT.
3. Observe as opções de interação disponíveis: uma para conversar/perguntar e outra para gerar/executar código (os nomes exatos podem variar um pouco conforme a versão da interface — procure por algo como "Perguntar" e "Gerar código", ou equivalentes).
4. Escolha a opção de perguntar e digite exatamente:
   > O que é o Codex e em que tipo de tarefa eu deveria usá-lo?
5. Leia a resposta com calma.

### ✅ Deu certo?

Você recebeu uma explicação em texto — e nenhum arquivo, projeto ou tarefa foi alterado. É exatamente esse o comportamento esperado: no modo de pergunta, o Codex só conversa, nunca executa nada.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não encontro o Codex no menu | Confira se está logado e procure por "Codex" no menu principal do ChatGPT; a disponibilidade pode variar conforme o plano e a região |
| A resposta veio muito genérica | Refaça a pergunta acrescentando contexto, por exemplo: "para que tipo de tarefa de programação ou de organização de documentos eu usaria o Codex?" |

> 💡 **Dica:** sempre que tiver uma dúvida rápida e não precisar que nada seja alterado de verdade, use o modo de pergunta — é mais rápido do que abrir uma tarefa completa.

### 🚀 Quer ir além?

Pergunte ao Codex "quais são as principais diferenças entre você e um chat de IA comum?" e compare a resposta com o que você acabou de descobrir na prática.

---

# Oficina 2 — Preparando Sua Sala de Trabalho

### 🎯 O Problema

Um agente de trabalho precisa de um lugar para trabalhar. Sem um projeto conectado, o Codex simplesmente não tem onde colocar a mão. Nesta oficina você vai dar a ele essa "sala": um repositório de teste no GitHub.

### 🧰 O que você vai usar

- Conta no GitHub (gratuita)
- Conta no Codex já acessada na Oficina 1

### 👐 Mão na massa

1. Se ainda não tiver conta no GitHub, crie uma gratuitamente em github.com.
2. Dentro do GitHub, crie um repositório novo e vazio, só para praticar (sugestão de nome: `meu-teste-codex`).
3. Volte para o Codex e procure a opção para conectar ou adicionar um repositório.
4. Siga o fluxo de autorização, revisando com atenção quais permissões estão sendo concedidas ao Codex sobre sua conta do GitHub.
5. Confirme que o repositório `meu-teste-codex` aparece listado dentro do Codex.

### ✅ Deu certo?

O repositório de teste aparece disponível dentro do Codex, pronto para receber uma tarefa — era exatamente esse o objetivo desta oficina.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não aparece opção para conectar o GitHub | A sessão do ChatGPT pode ter expirado; saia e entre novamente na conta |
| O repositório não aparece na lista depois de autorizado | Verifique, nas configurações da sua conta ou organização no GitHub, se o acesso ao repositório foi realmente concedido |

> ⚠️ **Cuidado:** revise sempre quais permissões está concedendo ao autorizar o acesso ao GitHub — para praticar, prefira repositórios de teste em vez de projetos importantes.

### 🚀 Quer ir além?

Antes de seguir para a próxima oficina, explore a lista de arquivos do repositório diretamente de dentro do Codex.

---

# Oficina 3 — Pedindo (Direito) Sua Primeira Tarefa

### 🎯 O Problema

Pedir algo de forma vaga para um agente de IA é como pedir para alguém "resolver isso aí" sem dizer o quê, onde, nem como saber que terminou. Nesta oficina você vai sentir na pele a diferença entre um pedido vago e um pedido bem-feito — e vai sair com uma alteração real no seu repositório de teste.

### 🧰 O que você vai usar

- O repositório conectado na Oficina 2
- Uns 15 minutos de atenção, sem pressa

### 👐 Mão na massa

1. Abra o repositório de teste dentro do Codex e escolha a opção de gerar/executar uma tarefa (não apenas perguntar).
2. Digite um pedido propositalmente vago, só para observar o que acontece:
   > Melhora esse projeto.
3. Repare como esse tipo de pedido deixa muita coisa em aberto — o Codex pode até tentar responder, mas vai ter que "adivinhar" o que você realmente quer.
4. Agora abra uma nova tarefa e envie um pedido bem estruturado:
   > No arquivo README.md, adicione uma seção chamada "Sobre o projeto" com uma frase explicando que este é um repositório de testes para aprender a usar o Codex. Não altere mais nada além disso. Critério de sucesso: o README passa a ter essa nova seção, sem perder o conteúdo que já existia.
5. Acompanhe a execução em tempo real, observando a lista de arquivos sendo alterados e o registro (log) da tarefa.
6. Aguarde a conclusão — tarefas simples costumam terminar em poucos minutos.

### ✅ Deu certo?

O Codex mostra um comparativo (diff) com a nova seção "Sobre o projeto" adicionada ao README, sem apagar nada que já estava lá.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| A tarefa parece travada | Tarefas mais complexas podem levar até 30 minutos; aguarde e acompanhe o log — a ausência de novidade por alguns minutos é normal |
| O resultado alterou mais coisas do que o esperado | O prompt provavelmente não deixou as restrições claras; da próxima vez, diga explicitamente o que **não** deve ser alterado |

> 💡 **Dica:** um bom pedido sempre tem quatro partes: objetivo (o quê), contexto (onde), restrições (o que não mexer) e critério de sucesso (como saber que terminou).

> 📌 **Não esqueça:** pedido vago não é necessariamente "errado" — mas é imprevisível. Quanto mais claro o pedido, menos rodadas de correção você vai precisar depois.

### 🚀 Quer ir além?

Na mesma tarefa ou em uma nova, peça ao Codex para adicionar também uma seção "Como usar" ao README, seguindo a mesma estrutura de pedido.

---

# Oficina 4 — Conferindo o Trabalho do Seu Agente

### 🎯 O Problema

O Codex avisou que a tarefa terminou. Ótimo — mas "terminou" não é sinônimo de "está certo". Nesta oficina você vai aprender a conferir o trabalho do agente antes de aceitar qualquer coisa, do jeito que um profissional experiente faria.

### 🧰 O que você vai usar

- A tarefa concluída na Oficina 3

### 👐 Mão na massa

1. Abra a tarefa concluída e localize o comparativo (diff) com as linhas alteradas.
2. Leia, linha por linha, o que foi modificado — confirme que nada além do combinado foi tocado.
3. Confira o registro (log) de execução em busca de erros ou avisos.
4. Decida: aceitar o resultado, pedir um ajuste, ou pedir para o Codex testar de novo.
5. Se estiver tudo certo, aceite a alteração (ou abra uma Pull Request, caso seu repositório esteja no GitHub e essa opção esteja disponível).

### ✅ Deu certo?

Você consegue explicar, com suas próprias palavras, exatamente o que mudou no projeto e por que decidiu aceitar (ou não) o resultado.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não entendo por que uma linha específica foi alterada | Pergunte diretamente ao Codex: "explique por que você alterou esta linha" |
| O log mostra um teste que falhou | Não aceite a alteração ainda; peça uma nova execução explicando o que falhou e o que se espera como correção |

> ⚠️ **Cuidado:** nunca aceite uma alteração só para ganhar tempo, se você não entendeu completamente o que ela faz — esse é o erro mais comum de quem começa a trabalhar com agentes de IA.

> 🤓 **Curiosidade técnica:** o Codex é treinado para produzir alterações no estilo de um profissional revisando o próprio código — mas mesmo assim, a revisão humana continua sendo indispensável antes de qualquer integração.

### 🚀 Quer ir além?

Aplique esse mesmo roteiro de conferência (diff → log → decisão) a uma tarefa antiga sua, ou à tarefa de um colega, se tiver uma disponível.

---

# Projeto Final — Do Prompt à Entrega Completa

### 🎯 A missão

Chegou a hora de juntar tudo: escolher um problema real (pequeno) no seu repositório de teste, pedir a tarefa do jeito certo, acompanhar a execução, revisar com cuidado e entregar formalmente o resultado — como se fosse, de fato, seu primeiro dia trabalhando ao lado de um agente de IA.

### 👐 Mão na massa

1. Escolha uma pequena melhoria real para o seu repositório (por exemplo: corrigir um erro de digitação, atualizar o README, adicionar um comentário explicativo).
2. Escreva o pedido incluindo objetivo, contexto e critério de sucesso, do jeito praticado na Oficina 3.
3. Envie a tarefa e acompanhe a execução até o fim, como nas Oficinas 1 e 3.
4. Quando terminar, revise completamente o diff e o log, como praticado na Oficina 4.
5. Aceite a alteração ou abra uma Pull Request com o resultado.
6. Escreva, em uma frase só, o que você aprendeu fazendo esse projeto.

> 🤓 **Curiosidade técnica:** segundo dados divulgados pela própria OpenAI, mais da metade dos usuários avançados do Codex já mantém mais de uma tarefa rodando ao mesmo tempo ao longo do dia. Você acabou de treinar, em miniatura, exatamente o fluxo que esses profissionais usam todos os dias.

### 🏁 Como saber que terminou

- [ ] Escrevi um pedido com objetivo, contexto e critério de sucesso claros
- [ ] Acompanhei a execução da tarefa até o fim
- [ ] Revisei o diff e o log completos antes de decidir
- [ ] Aceitei a alteração ou abri uma Pull Request de forma consciente
- [ ] Consigo explicar, em uma frase, o que foi entregue e por quê

---

# A Parte dos Dez — Coisas Para Nunca Esquecer Sobre o Codex

1. Comece sempre pelo modo de pergunta quando tiver dúvida sobre o projeto, antes de pedir qualquer alteração.
2. Um bom pedido tem objetivo, contexto, restrições e critério de sucesso — sempre.
3. Tarefas grandes demais confundem o agente; divida-as em tarefas menores e mais claras.
4. É possível rodar mais de uma tarefa do Codex ao mesmo tempo, em projetos diferentes ou no mesmo projeto.
5. Um arquivo chamado AGENTS.md, na raiz do projeto, ajuda o Codex a seguir os padrões do seu time — e pode ser criado rapidamente com o comando `/init`.
6. Cada tarefa roda em um ambiente isolado, só dela, sem misturar com outros projetos.
7. Logs e resultados de teste são a prova do que o Codex realmente fez — vale sempre a pena dar uma olhada antes de aceitar.
8. Por padrão, o acesso à internet durante uma tarefa fica desativado; é possível ativá-lo manualmente quando necessário, mas isso pede atenção redobrada de segurança.
9. Revisão humana nunca é opcional — nem quando o resultado parece perfeito à primeira vista.
10. O Codex também serve para muito além de programação: pesquisa, planilhas, relatórios e documentos entram na lista.

---

## Conseguiu! E agora?

Se você chegou até aqui, já fez mais do que a maioria de quem só "ouve falar" sobre agentes de IA: você abriu o Codex, escreveu pedidos de verdade, acompanhou uma execução real e revisou um resultado antes de aceitá-lo. Isso não é pouca coisa — é exatamente o ciclo que profissionais experientes repetem todos os dias.

A partir daqui, o caminho é praticar com projetos reais, cada vez um pouco mais ambiciosos. Quando se sentir confortável com o básico, vale explorar recursos mais avançados, como arquivos AGENTS.md mais completos, múltiplos agentes trabalhando em paralelo e automações recorrentes. Uma tarefa de cada vez — o Codex, como qualquer boa parceria de trabalho, rende mais quando a confiança é construída aos poucos.
