# Claude Skills Para Leigos — Curso Hands-on

*Em pouco mais de uma hora você sai daqui com uma Skill sua, funcionando, que corrige, monta ou revisa do seu jeito — sem escrever uma linha de código.*

---

## Antes de Arregaçar as Mangas

Este não é um curso sobre Skills. É um curso em que você **faz** Skills. Cada oficina começa com um problema chato e real da vida docente, e termina com aquele problema resolvido por um arquivo que você mesmo escreveu. Nada de teoria antes da hora: a explicação vem quando ela é necessária para o próximo passo, e não antes.

### O que você precisa ter aberto agora

- O navegador, com o claude.ai aberto e você logado.
- O Bloco de Notas (Windows) ou o TextEdit (Mac).
- Uma pasta qualquer no seu computador onde você consiga salvar arquivos e achá-los depois.
- Um documento seu de verdade: uma rubrica de correção, um formulário de plano de ensino, um modelo de parecer. Qualquer coisa que você já use e que tenha um formato fixo.
- Vinte minutos de silêncio, se possível. As oficinas são curtas, mas a Oficina 2 não gosta de interrupção.

> 🔑 **A regra de ouro deste curso:** você não vai perguntar "está bom?". Você vai perguntar "atende a quantos critérios?". Toda vez que mexer na sua Skill, teste em **conversa nova** e conte. Impressão engana; contagem não.

> ⚠️ **Confira isto antes de começar, leva um minuto.** Entre nas configurações da sua conta e procure por "Skills". Existe a opção de criar ou enviar uma Skill? Se sim, você está pronto para tudo. Se não, o recurso não está habilitado no seu plano — e você ainda consegue fazer o curso inteiro escrevendo os arquivos, guardando-os prontos para o dia em que tiver acesso. Só a etapa de envio ficará pendente.

---

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| **1** | "Toda vez eu copio o texto da tela e colo no Word" | 15 min |
| **2** | "Toda conversa nova eu colo as mesmas instruções" | 20 min |
| **3** | "Criei a Skill e o Claude simplesmente ignora ela" | 15 min |
| **4** | "A Skill corrige, mas não usa a MINHA rubrica" | 15 min |
| **Projeto Final** | "Quero uma Skill que sirva de verdade no meu semestre" | 20 min |

Repare na progressão: você começa **usando** o que já existe, passa a **criar**, depois aprende a fazer **funcionar sozinho**, e termina conectando a Skill ao seu material real. Cada oficina depende da anterior — faça na ordem.

---
---

# Oficina 1 — Ponha uma Skill para trabalhar

### 🎯 O Problema

Você pede um resumo ao Claude, ele escreve um texto bonito na tela, e aí começa o trabalho chato: selecionar, copiar, abrir o Word, colar, arrumar a formatação que veio torta, ajustar os títulos. Cinco minutos de tarefa braçal toda vez. E você faz isso desde sempre, sem saber que não precisava.

Nesta oficina você vai eliminar essa etapa e, de quebra, ver uma Skill funcionando antes mesmo de saber direito o que é uma.

### 🧰 O que você vai usar

- O claude.ai, numa conversa nova.
- Um assunto que você domina — o tema da sua próxima aula serve.
- Um arquivo de texto vazio no computador, para guardar uma coisa importante.

### 👐 Mão na massa

1. Abra uma **conversa nova** no claude.ai.

2. Digite exatamente isto, trocando o assunto pelo seu:

> Crie um documento Word de uma página com um resumo sobre [seu assunto].

3. Envie e **observe a resposta enquanto ela aparece**. Em algum momento o Claude sinaliza que está usando uma Skill. Ache esse ponto.

4. Baixe o arquivo e abra. É um `.docx` de verdade, formatado, pronto.

5. Agora repita o pedido numa conversa nova, mas peça **"um resumo"** em vez de **"um documento Word"**. Compare os dois resultados.

6. **Este passo é o mais importante da oficina, e você só vai entender por quê no Projeto Final.** Abra outra conversa nova e peça ao Claude que execute uma tarefa repetitiva sua — corrigir um trabalho, montar um plano de ensino, formatar referências —, **sem dar nenhuma instrução de formato**. Deixe-o fazer do jeito dele.

7. Copie a resposta inteira e salve num arquivo chamado `linha-de-base.txt`. Guarde numa pasta que você vá achar depois.

> 💡 **Dica:** faça o passo 6 com a tarefa que mais te consome tempo no semestre. É essa que vai virar a sua Skill.

### ✅ Deu certo?

Você tem um arquivo `.docx` baixado que nasceu pronto, sem copiar e colar. E tem um arquivo `linha-de-base.txt` guardado com a resposta "crua" do Claude a uma tarefa sua.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O Claude respondeu com texto na tela, sem gerar arquivo | Peça explicitamente: "gere o arquivo .docx para download". Se ainda assim não vier, veja nas configurações se a criação de arquivos está ativa |
| Não achei onde ele avisa que usou uma Skill | Deixa quieto. Se o arquivo foi gerado, uma Skill trabalhou. O rótulo muda de lugar conforme a versão |
| Não sei que tarefa usar no passo 6 | Aquela que você adiaria se pudesse. É essa |

### 🚀 Quer ir além?

Peça uma planilha do Excel e uma apresentação do PowerPoint — são outras duas Skills prontas, e cada uma se comporta de um jeito diferente.

---
---

# Oficina 2 — Escreva e suba a sua primeira Skill

### 🎯 O Problema

Toda conversa nova, lá vai você colar o mesmo bloco: "use a norma ABNT", "o plano tem estes seis campos, nesta ordem", "comece o feedback pelos acertos e nunca passe de uma página". Você está reensinando a mesma coisa desde o semestre passado. E, quando esquece de colar, o resultado sai errado — o que é pior do que colar.

Nesta oficina esse bloco sai da sua área de transferência e vira um arquivo que o Claude busca sozinho.

### 🧰 O que você vai usar

- O Bloco de Notas ou o TextEdit.
- Uma pasta no computador.
- O procedimento que você mais repete.

### 👐 Mão na massa

**Bloco A — Escrever (7 min)**

1. Crie uma pasta com o nome da sua Skill, **em minúsculas e com hifens**. Exemplo: `corrigir-por-rubrica`. Nada de espaços, nada de maiúsculas, e **não use a palavra "claude" no nome** — ela é proibida.

2. Abra o Bloco de Notas e escreva o arquivo, adaptando este modelo ao seu caso:

> ```
> ---
> name: corrigir-por-rubrica
> description: Corrige trabalhos discentes segundo a rubrica da disciplina, com
>   nota por critério e feedback estruturado. Use quando o usuário pedir correção,
>   avaliação, nota ou feedback de trabalho, prova dissertativa, artigo ou TCC.
> ---
>
> # Correção por rubrica
>
> 1. Leia o trabalho na íntegra antes de pontuar.
> 2. Pontue cada critério separadamente.
> 3. Confira se a soma corresponde à nota final.
> 4. Escreva o feedback: acertos primeiro, depois os problemas.
> 5. Limite o feedback a uma página.
> ```

3. Na hora de salvar, **preste atenção nestes dois campos da janela, porque eles derrubam quase todo mundo**:
   - **Tipo:** mude para "Todos os arquivos". Se não mudar, você vai salvar `SKILL.md.txt` e nada vai funcionar.
   - **Codificação:** escolha **UTF-8**. Se não escolher, "correção" pode virar "correÃ§Ã£o".

4. Salve com o nome `SKILL.md`, dentro da pasta que você criou.

5. Feche e reabra o arquivo. Os acentos estão certos? O nome é mesmo `SKILL.md`? Então segue.

**Bloco B — Empacotar (3 min)**

6. Clique com o botão direito **na pasta** (não no arquivo!) → *Enviar para* → *Pasta compactada*. No Mac: botão direito na pasta → *Comprimir*.

7. **Agora abra o ZIP com dois cliques e olhe dentro.** Você tem que ver **uma pasta**. Entrando nela, o `SKILL.md`.

   Se você vir o `SKILL.md` solto assim que abrir o ZIP, você compactou o arquivo em vez da pasta. Refaça.

**Bloco C — Subir e testar (10 min)**

8. Nas configurações da sua conta, ache a área de Skills. O caminho documentado é `Customize > Skills`; se o nome estiver diferente, use a busca das configurações e procure "Skills".

9. Envie o ZIP.

10. Abra uma **conversa nova** e faça um pedido que caia na situação que você descreveu — **sem citar o nome da Skill**. O teste é ela aparecer sozinha.

> 📌 **Não esqueça:** o `---` tem que estar colado na margem esquerda, sem nenhum espaço antes. Um espacinho ali e a Skill sobe sem descrição: funciona quando você a chama pelo nome, nunca funciona sozinha. É o defeito mais comum e o mais difícil de perceber.

> 🤓 **Curiosidade técnica (pode pular):** aquele bloco entre os `---` chama-se *frontmatter* e é escrito em YAML. Só o que fica ali dentro é lido o tempo todo pelo Claude — o resto do arquivo só é aberto quando a Skill aciona. É por isso que dá para ter vinte Skills instaladas sem pesar nada.

### ✅ Deu certo?

Você fez um pedido em linguagem normal, sem citar o nome de nada, e o Claude usou a sua Skill sozinho — devolvendo a resposta no formato que você especificou.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O envio foi recusado falando em "chave inesperada" no cabeçalho | Você copiou um campo de algum tutorial que só vale no Claude Code. Deixe só `name` e `description` e reenvie |
| O envio foi recusado sem explicação | Confira, nesta ordem: o ZIP tem uma pasta dentro? o `name` só tem minúsculas, números e hifens? o `name` não tem "claude" nem "anthropic"? |
| Subiu, mas não aciona | Chame pelo nome. Se funcionar assim e nunca sozinha, o problema está na descrição ou no cabeçalho — é exatamente a Oficina 3 |

### 🚀 Quer ir além?

Escreva uma segunda Skill, bem pequena, para outra tarefa sua — e repare em como a segunda leva um terço do tempo da primeira.

---
---

# Oficina 3 — Faça a Skill acionar sozinha

### 🎯 O Problema

Você criou a Skill, ela está lá, você sabe que ela funciona — e o Claude simplesmente a ignora. Você pede "dá uma nota nisso aqui" e ele responde qualquer coisa genérica, como se a Skill não existisse. Frustrante ao ponto de fazer desistir.

A culpa quase nunca é do procedimento. É de uma frase só.

### 🧰 O que você vai usar

- A sua Skill da Oficina 2.
- O Bloco de Notas.
- Cinco pedidos escritos por você.

### 👐 Mão na massa

1. Escreva **cinco pedidos**: três que **devem** acionar a sua Skill e dois que **não devem**. Escreva do jeito que você falaria de verdade, não do jeito bonito. Exemplo:

   - Deve acionar: "corrige este trabalho pela rubrica" / "dá uma nota nisso aqui" / "preciso avaliar os TCCs"
   - Não deve: "revisa a redação deste parágrafo" / "me ajuda a escrever a ementa"

2. Rode os cinco, **cada um numa conversa nova**, e anote numa tabela: acionou? deveria? Batendo as duas colunas, você tem a classificação:
   - Deveria e não acionou → **falso negativo**
   - Não deveria e acionou → **falso positivo**

3. Abra o `SKILL.md`. Para cada **falso negativo**, encontre a palavra-chave que faltava no pedido e **acrescente** à descrição. ("nota" faltava? bota "nota".)

4. Para cada **falso positivo**, **restrinja**: acrescente ao final da descrição uma frase dizendo o que a Skill **não** faz. Assim:

> Não se aplica a revisão de texto em elaboração nem a produção de material didático.

5. Salve (Tipo = Todos os arquivos, Codificação = UTF-8), recompacte a pasta e reenvie.

6. Se aparecerem duas Skills com o mesmo nome na lista, **exclua a antiga**. Duas versões ativas dão comportamento imprevisível.

7. Rode os cinco pedidos de novo, em conversas novas. Conte os acertos.

> 💡 **Dica que vale a oficina inteira:** falso negativo e falso positivo se corrigem em direções **opostas** — um pede acrescentar, o outro pede restringir. Por isso você classifica antes de mexer. Quem corrige sem classificar fica meses oscilando entre os dois extremos.

> ⚠️ **Cuidado com a tentação de alargar.** Acrescentar palavras genéricas como "texto", "documento" ou "ajuda" faz a Skill acionar em tudo. Prefira sempre o termo do seu domínio: "rubrica" em vez de "critério", "TCC" em vez de "trabalho".

### ✅ Deu certo?

Você tem dois números: quantos dos cinco acertavam antes e quantos acertam agora. E o segundo é maior.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Corrigi o falso negativo e apareceram falsos positivos novos | O termo que você acrescentou era genérico demais. Troque por um termo do seu domínio e acrescente a frase do "não se aplica" |
| Os cinco acionaram, inclusive os dois que não deviam | Comece pela frase do "não se aplica". Se insistir, o problema é o **nome** da Skill: nomes genéricos como `revisar` acionam por conta própria |
| A Skill aciona certo, mas o resultado sai errado | Isso não é problema de acionamento, é de procedimento. O corpo da Skill está vago demais — deixe cada passo começando com um verbo no imperativo |

### 🚀 Quer ir além?

Peça a um colega que descreva, com as palavras dele, como pediria a mesma tarefa. Quase sempre ele usa uma palavra que não passou pela sua cabeça — e que faltava na sua descrição.

---
---

# Oficina 4 — Anexe a sua rubrica de verdade

### 🎯 O Problema

A Skill corrige. Só que ela corrige com critérios genéricos — "conteúdo", "argumentação", "escrita" — e não com os quatro critérios exatos da rubrica que o seu colegiado aprovou. Numa correção de rotina passa; num pedido de revisão de nota, não passa.

Você tem a rubrica num arquivo. Está na hora de a Skill usar aquele arquivo, e não uma versão aproximada que ela imaginou.

### 🧰 O que você vai usar

- A sua Skill das oficinas anteriores.
- Um documento seu de verdade: rubrica, formulário de plano de ensino, modelo de parecer.

### 👐 Mão na massa

1. Abra o seu documento real e passe o conteúdo dele para um arquivo de texto na **mesma pasta** da Skill. Nomeie de forma clara: `rubrica.md`, `formulario-plano.md`, `modelo-parecer.md`. Nada de `doc2.md`.

2. Se o arquivo passar de umas 100 linhas, comece com um sumário — uma lista do que tem dentro:

> ```
> # Rubrica da disciplina
>
> ## Conteúdo
> - Critério 1: Domínio conceitual
> - Critério 2: Estrutura argumentativa
> - Critério 3: Uso de fontes
> - Critério 4: Redação e norma culta
> - Faixas de nota e descritores
> ```

3. Abra o `SKILL.md` e acrescente ao final uma seção que **remeta** ao arquivo, dizendo o que tem lá dentro:

> ```
> ## Materiais de apoio
>
> **Rubrica completa, com os quatro critérios e as faixas de nota**:
> ver [rubrica.md](rubrica.md)
> ```

4. Ainda no `SKILL.md`, acrescente ao procedimento **três instruções sem margem para interpretação**:

> ```
> - Use os nomes de critério exatamente como estão em rubrica.md.
> - Não crie critério que não exista na rubrica.
> - Se faltar informação, escreva "A DEFINIR" e liste ao final o que falta.
> ```

5. Aproveite e **enxugue** o resto do corpo. Passe cada parágrafo por esta pergunta: *o Claude já sabe isto?* Explicação sobre o que é uma rubrica, ele já sabe — corte. A **sua** rubrica, ele não sabe — fica.

6. Recompacte a pasta inteira (agora com dois arquivos dentro) e reenvie.

7. Teste em conversa nova. Confira se os critérios que apareceram na resposta são **os seus**, com os nomes que estão na rubrica.

> 📌 **Não esqueça:** os arquivos de apoio só custam alguma coisa quando são abertos. Você pode ter cinco arquivos na pasta que, numa correção comum, o Claude vai abrir só o que precisa. É por isso que dividir não é desperdício — é economia.

> ⚠️ **Cuidado sério:** não coloque dados de estudantes nos arquivos da Skill. Nada de nomes, matrículas, notas identificáveis ou situações pessoais. Se quiser exemplo realista, anonimize antes. O conteúdo de uma Skill fica armazenado.

### ✅ Deu certo?

A resposta do Claude usa os nomes exatos dos seus critérios, tirados do arquivo que você anexou — e não uma aproximação inventada por ele.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O Claude ignorou o arquivo anexado | Sua remissão está vaga. Não escreva "ver rubrica.md". Escreva "**Rubrica completa com os quatro critérios e as faixas de nota**: ver [rubrica.md](rubrica.md)". É essa frase que faz ele decidir abrir |
| Ele leu só um pedaço do arquivo | Se o arquivo é longo, acrescente o sumário no topo. E garanta que ele é chamado direto pelo `SKILL.md`, não por outro arquivo de apoio |
| Meu modelo é um `.docx`, não dá para colar | Descreva a estrutura em texto: quais campos, em que ordem, o que vai em cada um. Funciona melhor do que anexar o Word |

### 🚀 Quer ir além?

Separe também os casos raros — plágio, entrega fora do prazo, pedido de recurso — num arquivo `casos-limite.md`. Eles só vão ser abertos quando aparecer um caso desses.

---
---

# Projeto Final — A Skill do seu semestre

### 🎯 A missão

Até agora você construiu por partes. Agora vai fechar o ciclo inteiro numa coisa só: pegar a tarefa que mais consome o seu tempo no semestre e entregar uma Skill que a resolva **e que você consiga provar que resolve**.

Provar é a palavra-chave. Você tem guardado, desde a Oficina 1, um arquivo `linha-de-base.txt` com a resposta crua do Claude a essa mesma tarefa — de quando ele não sabia nada do seu jeito de trabalhar. É contra aquilo que você vai medir.

### 👐 Mão na massa

1. **Escreva quatro critérios de êxito. Agora, antes de qualquer teste.** O que precisa acontecer para você considerar a Skill boa? Escreva de forma verificável — "bem escrito" não vale, "no máximo uma página, começando pelos acertos" vale.

2. Abra o `linha-de-base.txt` da Oficina 1. Avalie contra os quatro critérios e **anote o número**. Provavelmente vai ser 0 ou 1.

3. Faça uma revisão completa da sua Skill, aplicando tudo que você aprendeu:
   - Descrição com as duas metades: o que faz **e** quando usar. (Oficina 3)
   - Corpo enxuto, cada passo começando com verbo no imperativo. (Oficina 4)
   - Seu documento real anexado e referenciado com clareza. (Oficina 4)
   - Instruções sem margem nos pontos que não admitem variação.

4. Recompacte, reenvie, exclua a versão antiga se ela ficar duplicada.

5. Em **conversa nova**, rode a mesma tarefa da linha de base. Avalie contra os quatro critérios e anote o número.

6. Para cada critério que ainda falhou, identifique a causa e volte à oficina correspondente. Corrija **uma coisa de cada vez**, testando entre uma e outra.

7. Quando chegar a 4 de 4, faça a última coisa: acrescente ao final do `SKILL.md` uma linha com a data de hoje, assim — `Última revisão: [data]`. Daqui a seis meses você vai agradecer.

8. Envie o ZIP a um colega da sua área, com uma frase explicando quando ele deve usar. Se você não conseguir escrever essa frase em uma linha, a sua descrição também não consegue — e é a mesma frase.

### 🏁 Como saber que terminou

- [ ] Escrevi os quatro critérios **antes** de testar qualquer coisa.
- [ ] Tenho o número da linha de base anotado.
- [ ] Tenho o número da versão final anotado, e ele é maior.
- [ ] A Skill aciona sozinha em pelo menos três formulações diferentes do pedido.
- [ ] A Skill **não** aciona nos dois pedidos que não deviam acioná-la.
- [ ] O meu documento real está na pasta e é efetivamente usado na resposta.
- [ ] Nenhum dado de estudante entrou em nenhum arquivo da Skill.
- [ ] O `SKILL.md` tem a data da última revisão.
- [ ] Um colega recebeu o ZIP e sabe quando usar.

---
---

# A Parte dos Dez — Coisas que ninguém conta antes de você tropeçar nelas

1. **Teste sempre em conversa nova.** Quando uma Skill aciona, o conteúdo dela entra na conversa e fica. Testar a versão nova na mesma conversa que carregou a versão velha é receita para conclusão errada.

2. **"Funciona quando eu chamo, nunca sozinha" tem uma causa só, em 90% dos casos:** espaço antes dos `---` no topo do arquivo. O cabeçalho quebra, a Skill sobe sem descrição, e sem descrição não há acionamento.

3. **Compacte a pasta, não o arquivo.** E confira abrindo o ZIP. Este é o erro número um de quem está subindo a primeira Skill, e ele não dá mensagem de erro clara.

4. **UTF-8 na hora de salvar.** Sem isso, "avaliação" vira "avaliaÃ§Ã£o" e você vai passar meia hora achando que o problema é outra coisa.

5. **Skill não sincroniza entre lugares.** O que você subiu no claude.ai não aparece no Claude Code nem na API. São três lugares diferentes, e nenhum conversa com os outros.

6. **Se um exemplo da internet tem campos estranhos no cabeçalho, ele provavelmente é do Claude Code.** Coisas como `context: fork` ou `disable-model-invocation` não só não funcionam no claude.ai como **fazem o envio falhar**. Deixe só `name` e `description`.

7. **Não ensine ao Claude o que ele já sabe.** Ele sabe o que é uma rubrica, o que é ABNT, o que é um plano de ensino. Ele não sabe qual é a **sua** rubrica. Escreva só a segunda parte.

8. **Uma Skill que precisa de "e" para ser descrita são duas Skills.** Skills abrangentes funcionam pior — quem descobriu isso foi a própria Anthropic, olhando as centenas que usa internamente.

9. **Guarde as versões anteriores numeradas** no computador: `SKILL-v1.md`, `SKILL-v2.md`. Custa nada e é o que permite você voltar quando uma "melhoria" piorar tudo.

10. **Skill de estranho é software de estranho.** Se veio de fora e tem pasta `scripts/` ou acessa endereços na internet, não instale sem alguém do TI olhar junto. E, mesmo nas simples, faça a única verificação que qualquer um consegue fazer: **o que ela faz é o que ela diz que faz?**

---

## Conseguiu! E agora?

Olha o que aconteceu em pouco mais de uma hora. Você entrou aqui copiando texto da tela para o Word e saiu com um arquivo seu, escrito por você, que faz o Claude corrigir, montar ou revisar seguindo o **seu** procedimento — com a sua rubrica, no seu formato, na sua ordem. E, mais importante que isso: você sai sabendo **provar** que ele faz, porque tem dois números anotados em vez de uma impressão.

O que você ganhou não foi velocidade, foi consistência. O mesmo padrão na terça e na sexta, no primeiro trabalho e no quadragésimo, esteja você descansado ou no fim do semestre.

E agora? Faça a segunda. Sério — a segunda Skill leva um terço do tempo da primeira, porque a parte difícil não era a ferramenta, era entender a lógica. Olhe a sua lista de tarefas repetitivas e escolha a próxima, dando preferência àquelas que têm um formato obrigatório da sua instituição: são as que ninguém pode escrever no seu lugar, e as que continuam valendo por anos.

Uma última coisa: este ecossistema muda rápido. Menus mudam de nome, campos novos aparecem. O raciocínio que você aprendeu aqui — carregar só o necessário, escrever a descrição para o vocabulário dos outros, medir em vez de achar — esse não muda. Quando a tela não corresponder ao que está escrito aqui, confie no raciocínio e confira o detalhe.

Boa correção. E que a sua próxima pilha de trabalhos ache você preparado.
