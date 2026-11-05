> *» IA: Cover — título e subtítulo do curso. Preservar o subtítulo em itálico.*

# Claude Skills Para Leigos — Curso Hands-on

*Em duas horas você sai daqui com uma Skill sua, funcionando, que corrige, monta ou revisa do seu jeito — e com dois números que provam que ela funciona.*

---

> *» IA: Text — parágrafo de abertura. Não resumir.*

## Antes de Arregaçar as Mangas

Este não é um curso sobre Skills. É um curso em que você **faz** Skills. Cada oficina começa com um problema chato e real da vida docente e termina com esse problema resolvido por um arquivo que você mesmo escreveu. A teoria entra quando é necessária para o próximo passo, e não antes.

> *» IA: Checklist — pré-requisitos. Um item por linha, verbatim.*

### O que você precisa ter aberto agora

- O navegador, com o claude.ai aberto e você logado.
- O Bloco de Notas (Windows) ou o TextEdit (Mac).
- Uma pasta no seu computador onde você consiga salvar arquivos e achá-los depois.
- Um documento seu de verdade: uma rubrica de correção, um formulário de plano de ensino, um modelo de parecer. Qualquer coisa que você já use e tenha formato fixo.

> *» IA: Statement — regra de ouro do curso. Preservar o emoji 🔑. Verbatim.*

> 🔑 **A regra de ouro deste curso:** você não vai perguntar "está bom?". Vai perguntar "atende a quantos critérios?". Toda vez que mexer na sua Skill, teste em **conversa nova** e conte. Impressão engana; contagem não.

> *» IA: Statement — verificação prévia de acesso. Preservar o emoji ⚠️ e o breadcrumb. Não traduzir termos de interface.*

> ⚠️ **Confira isto antes de começar, leva um minuto.** Vá em `claude.ai > Configurações > Customize > Skills` e veja se existe a opção de criar ou enviar uma Skill. Se existir, você está pronto para tudo. Se não existir, o recurso não está habilitado no seu plano — e você ainda faz o curso inteiro escrevendo os arquivos e guardando-os prontos. Só a etapa de envio ficará pendente.
>
> 🏁 **Ponto de controle:** em `claude.ai > Configurações > Customize > Skills` você consegue ver um botão de envio ou criação de Skill.

---

> *» IA: Text — parágrafo introdutório do mapa.*

## O Mapa da Mão na Massa

> *» IA: Table — mapa das oficinas. Manter as três colunas.*

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| **1** | "Toda vez eu copio o texto da tela e colo no Word" | 20 min |
| **2** | "Toda conversa nova eu colo as mesmas instruções" | 20 min |
| **3** | "Criei a Skill e o Claude simplesmente ignora ela" | 20 min |
| **4** | "A Skill corrige, mas não usa a MINHA rubrica" | 20 min |
| **Projeto Final** | "Quero uma Skill que sirva de verdade no meu semestre" | 35 min |

> *» IA: Text — frase de progressão. Não resumir.*

Repare na progressão: você começa **usando** o que já existe, passa a **criar**, depois faz **funcionar sozinho**, e termina conectando a Skill ao seu material real. Cada oficina depende da anterior — faça na ordem.

---
---

# Oficina 1 — Ponha uma Skill para trabalhar

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

> *» IA: Text — problema da oficina. Preservar o emoji no cabeçalho.*

### 🎯 O Problema

Você pede um resumo ao Claude, ele escreve um texto bonito na tela, e aí começa o trabalho braçal: selecionar, copiar, abrir o Word, colar, arrumar a formatação torta, ajustar os títulos. Cinco minutos de tarefa chata toda vez. E você faz isso desde sempre, sem saber que não precisava.

Nesta oficina você elimina essa etapa e, de quebra, vê uma Skill funcionando antes de saber direito o que é uma.

> *» IA: List — materiais. Enxuta, verbatim.*

### 🧰 O que você vai usar

- O claude.ai, numa conversa nova.
- Um assunto que você domina — o tema da sua próxima aula serve.
- Um arquivo de texto vazio no computador, para guardar uma coisa importante.

> *» IA: Process — passos numerados da oficina. Preservar os breadcrumbs e o texto a digitar. Não fundir passos.*

### 👐 Mão na massa

1. Abra uma conversa nova em `claude.ai > Nova conversa`.

2. Digite exatamente isto, trocando o assunto pelo seu:

   > Crie um documento Word de uma página com um resumo sobre [seu assunto].

3. Envie e observe a resposta **enquanto ela aparece**. Em algum momento o Claude sinaliza que está usando uma Skill. Ache esse ponto.

4. Baixe o arquivo e abra. É um `.docx` de verdade, formatado, pronto.

5. Numa conversa nova, repita o pedido pedindo **"um resumo"** em vez de **"um documento Word"**. Compare os dois resultados.

6. Abra outra conversa nova e peça ao Claude que execute uma tarefa repetitiva sua — corrigir um trabalho, montar um plano de ensino, formatar referências —, **sem dar nenhuma instrução de formato**. Deixe-o fazer do jeito dele.

7. Copie a resposta inteira e salve num arquivo chamado `linha-de-base.txt`, numa pasta que você vá achar depois.

   🏁 **Ponto de controle:** o arquivo `linha-de-base.txt` existe na sua pasta e contém a resposta crua do Claude.

> *» IA: Statement — dica. Preservar o emoji 💡.*

> 💡 **Dica:** faça o passo 6 com a tarefa que mais consome o seu tempo no semestre. É essa que vai virar a sua Skill — e é contra esse arquivo que você vai medir tudo no Projeto Final.

> *» IA: Statement — critério de êxito da oficina. Preservar o emoji ✅.*

### ✅ Deu certo?

Você tem um `.docx` baixado que nasceu pronto, sem copiar e colar, e um `linha-de-base.txt` guardado com a resposta crua do Claude a uma tarefa sua.

> *» IA: Accordion — solução de problemas, um item por linha da tabela.*

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O Claude respondeu com texto na tela, sem gerar arquivo | Peça explicitamente: "gere o arquivo .docx para download". Persistindo, confira em `claude.ai > Configurações > Recursos` se a criação de arquivos está ativa |
| Não achei onde ele avisa que usou uma Skill | Deixe quieto. Se o arquivo foi gerado, uma Skill trabalhou. O rótulo muda de lugar conforme a versão |
| Não sei que tarefa usar no passo 6 | Aquela que você adiaria se pudesse. É essa |

> *» IA: Accordion — desafios de extensão, um por linha. Marcado como OPCIONAL.*

### 🚀 Quer ir além?

- Peça uma planilha do Excel e observe que a Skill acionada é outra, com comportamento diferente.
- Peça uma apresentação do PowerPoint e compare quanto o resultado se aproxima do que você faria à mão.
- Peça o **mesmo** conteúdo em `.docx` e em `.pdf` e repare em quais decisões de formatação mudam entre os dois.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---
---

# Oficina 2 — Escreva e suba a sua primeira Skill

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja modelos editáveis no meio. ▼▼▼*

> *» IA: Text — problema da oficina.*

### 🎯 O Problema

Toda conversa nova, lá vai você colar o mesmo bloco: "use a norma ABNT", "o plano tem estes seis campos, nesta ordem", "comece o feedback pelos acertos e nunca passe de uma página". Você está reensinando a mesma coisa desde o semestre passado. E, quando esquece de colar, o resultado sai errado — o que é pior do que colar.

Nesta oficina esse bloco sai da sua área de transferência e vira um arquivo que o Claude busca sozinho.

> *» IA: List — materiais.*

### 🧰 O que você vai usar

- O Bloco de Notas ou o TextEdit.
- Uma pasta no computador.
- O procedimento que você mais repete.

> *» IA: Process — Bloco A. Preservar os breadcrumbs e não traduzir os termos de interface "Todos os arquivos" e "UTF-8".*

### 👐 Mão na massa

**Bloco A — Escrever (8 min)**

1. Crie uma pasta com o nome da sua Skill, **em minúsculas e com hifens**: `corrigir-por-rubrica`, por exemplo. Sem espaços, sem maiúsculas, e **sem a palavra "claude"** — ela é proibida.

2. Abra o editor em `Bloco de Notas > Arquivo > Novo` e escreva o arquivo adaptando o modelo abaixo.

> *» IA: Statement ou Download — modelo editável. Conteúdo verbatim, delimitadores preservados. Este bloco o participante copia e adapta.*

"""
---
name: corrigir-por-rubrica
description: Corrige trabalhos discentes segundo a rubrica da disciplina, com
  nota por critério e feedback estruturado. Use quando o usuário pedir correção,
  avaliação, nota ou feedback de trabalho, prova dissertativa, artigo ou TCC.
---

# Correção por rubrica

1. Leia o trabalho na íntegra antes de pontuar.
2. Pontue cada critério separadamente.
3. Confira se a soma corresponde à nota final.
4. Escreva o feedback: acertos primeiro, depois os problemas.
5. Limite o feedback a uma página.
"""

> *» IA: Process — continuação do Bloco A. Preservar os breadcrumbs exatamente como escritos.*

3. Salve em `Bloco de Notas > Arquivo > Salvar como`. Dois campos dessa janela derrubam quase todo mundo:

   - `Salvar como > Tipo > Todos os arquivos` — sem isso você salva `SKILL.md.txt` e nada funciona.
   - `Salvar como > Codificação > UTF-8` — sem isso "correção" vira "correÃ§Ã£o".

4. Nomeie o arquivo `SKILL.md` e salve dentro da pasta que você criou.

5. Feche e reabra o arquivo.

   🏁 **Ponto de controle:** o arquivo se chama `SKILL.md` (e não `SKILL.md.txt`), os acentos estão corretos, e as linhas de três hifens estão coladas na margem esquerda.

**Bloco B — Empacotar (4 min)**

6. Empacote em `Explorador de Arquivos > [clique direito na pasta] > Enviar para > Pasta compactada`. No Mac: `Finder > [clique direito na pasta] > Comprimir`.

   Atenção ao alvo do clique: **na pasta**, não no arquivo.

7. Abra o ZIP com dois cliques e olhe dentro.

   🏁 **Ponto de controle:** ao abrir o ZIP você vê **uma pasta**; entrando nela, encontra o `SKILL.md`. Se o `SKILL.md` aparecer solto na raiz do ZIP, você compactou o arquivo em vez da pasta — refaça.

**Bloco C — Subir e testar (8 min)**

8. Vá em `claude.ai > Configurações > Customize > Skills` e envie o ZIP.

9. Abra uma conversa nova e faça um pedido que caia na situação que você descreveu — **sem citar o nome da Skill**. O teste é ela aparecer sozinha.

   🏁 **Ponto de controle:** o Claude usou a sua Skill sem que você a chamasse pelo nome, e a resposta veio no formato que você especificou.

> *» IA: Statement — alerta sobre o cabeçalho. Preservar o emoji 📌.*

> 📌 **Não esqueça:** o `---` tem que estar colado na margem esquerda, sem nenhum espaço antes. Um espacinho ali e a Skill sobe sem descrição: funciona quando você a chama pelo nome, nunca funciona sozinha. É o defeito mais comum e o mais difícil de perceber.

> *» IA: Statement — curiosidade técnica, marcado como dispensável. Preservar o emoji 🤓.*

> 🤓 **Curiosidade técnica (pode pular):** o bloco entre os `---` chama-se *frontmatter* e usa o formato YAML. Só o que está ali dentro fica carregado o tempo todo; o resto do arquivo só é aberto quando a Skill aciona. É por isso que dá para ter vinte Skills instaladas sem pesar nada.

> *» IA: Statement — critério de êxito.*

### ✅ Deu certo?

Você fez um pedido em linguagem normal, sem citar nome de nada, e o Claude usou a sua Skill sozinho — devolvendo a resposta no formato que você especificou.

> *» IA: Accordion — solução de problemas, um item por linha.*

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Envio recusado com aviso de "chave inesperada" no cabeçalho | Você copiou um campo de tutorial do Claude Code. Deixe só `name` e `description` e reenvie |
| Envio recusado sem explicação | Confira nesta ordem: o ZIP tem uma pasta dentro? o `name` só tem minúsculas, números e hifens? o `name` não contém "claude" nem "anthropic"? |
| Subiu, mas não aciona | Chame pelo nome. Se funcionar assim e nunca sozinha, o problema está na descrição ou no cabeçalho — é exatamente a Oficina 3 |

> *» IA: Accordion — desafios de extensão, um por linha. Marcado como OPCIONAL.*

### 🚀 Quer ir além?

- Escreva uma segunda Skill bem pequena para outra tarefa sua, e cronometre: leva cerca de um terço do tempo da primeira.
- Peça ao Claude, numa conversa nova, que aponte três instruções ambíguas no seu `SKILL.md` — pontos em que dois leitores fariam coisas diferentes.
- Acrescente ao final do corpo a linha `Última revisão: [data de hoje]` e crie o hábito de mantê-la atualizada.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---
---

# Oficina 3 — Faça a Skill acionar sozinha

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> *» IA: Text — problema da oficina.*

### 🎯 O Problema

Você criou a Skill, ela está lá, você sabe que funciona — e o Claude simplesmente a ignora. Você pede "dá uma nota nisso aqui" e ele responde qualquer coisa genérica, como se a Skill não existisse. Frustrante ao ponto de fazer desistir.

A culpa quase nunca é do procedimento. É de uma frase só: a descrição.

> *» IA: List — materiais.*

### 🧰 O que você vai usar

- A sua Skill da Oficina 2.
- O Bloco de Notas.
- Cinco pedidos escritos por você.

> *» IA: Process — passos numerados. Preservar os breadcrumbs e o modelo editável do passo 4.*

### 👐 Mão na massa

1. Escreva **cinco pedidos**: três que **devem** acionar a sua Skill e dois que **não devem**. Escreva do jeito que você falaria, não do jeito bonito.

   - Devem acionar: "corrige este trabalho pela rubrica" / "dá uma nota nisso aqui" / "preciso avaliar os TCCs"
   - Não devem: "revisa a redação deste parágrafo" / "me ajuda a escrever a ementa"

2. Rode os cinco, **cada um numa conversa nova**, e monte a tabela: acionou? deveria? A combinação das duas colunas dá a classificação:

   - Deveria e não acionou → **falso negativo**
   - Não deveria e acionou → **falso positivo**

3. Abra o `SKILL.md`. Para cada **falso negativo**, ache a palavra-chave que faltava no pedido e **acrescente** à descrição. Faltou "nota"? Bota "nota".

4. Para cada **falso positivo**, **restrinja**: acrescente ao final da descrição uma frase dizendo o que a Skill não faz.

> *» IA: Statement ou Download — modelo editável de delimitação negativa. Conteúdo verbatim.*

"""
Não se aplica a revisão de texto em elaboração nem a produção de material didático.
"""

> *» IA: Process — continuação dos passos. Preservar os breadcrumbs.*

5. Salve em `Bloco de Notas > Arquivo > Salvar como`, mantendo `Tipo > Todos os arquivos` e `Codificação > UTF-8`.

6. Recompacte a pasta e reenvie em `claude.ai > Configurações > Customize > Skills`.

7. Se aparecerem duas Skills com o mesmo nome na lista, **exclua a antiga**. Duas versões ativas dão comportamento imprevisível.

   🏁 **Ponto de controle:** em `claude.ai > Configurações > Customize > Skills` existe apenas uma entrada com o nome da sua Skill.

8. Rode os cinco pedidos de novo, em conversas novas. Conte os acertos.

> *» IA: Statement — dica central da oficina. Preservar o emoji 💡.*

> 💡 **Dica que vale a oficina inteira:** falso negativo e falso positivo se corrigem em direções **opostas** — um pede acrescentar, o outro pede restringir. Por isso você classifica antes de mexer. Quem corrige sem classificar fica meses oscilando entre os dois extremos.

> *» IA: Statement — alerta. Preservar o emoji ⚠️.*

> ⚠️ **Cuidado com a tentação de alargar.** Palavras genéricas como "texto", "documento" ou "ajuda" fazem a Skill acionar em tudo. Prefira sempre o termo do seu domínio: "rubrica" em vez de "critério", "TCC" em vez de "trabalho".

> *» IA: Statement — critério de êxito.*

### ✅ Deu certo?

Você tem dois números: quantos dos cinco acertavam antes e quantos acertam agora. E o segundo é maior.

> *» IA: Accordion — solução de problemas, um item por linha.*

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Corrigi o falso negativo e surgiram falsos positivos novos | O termo acrescentado era genérico demais. Troque por um termo do seu domínio e acrescente a frase do "não se aplica" |
| Os cinco acionaram, inclusive os dois que não deviam | Comece pela frase do "não se aplica". Se insistir, o problema é o **nome**: nomes genéricos como `revisar` acionam por conta própria |
| A Skill aciona certo, mas o resultado sai errado | Não é problema de acionamento, é de procedimento. Deixe cada passo do corpo começando com verbo no imperativo |

> *» IA: Accordion — desafios de extensão, um por linha. Marcado como OPCIONAL.*

### 🚀 Quer ir além?

- Peça a um colega que descreva, com as palavras dele, como pediria a mesma tarefa — quase sempre ele usa uma palavra que não passou pela sua cabeça.
- Amplie o teste para dez pedidos e monte a tabela completa; a proporção de acertos fica muito mais confiável.
- Pergunte ao Claude, numa conversa nova: "esta descrição vai acionar em que tipos de pedido que não deveriam acioná-la?" — ele antecipa falsos positivos que você ainda não viu.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---
---

# Oficina 4 — Anexe a sua rubrica de verdade

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja modelos editáveis no meio. ▼▼▼*

> *» IA: Text — problema da oficina.*

### 🎯 O Problema

A Skill corrige. Só que corrige com critérios genéricos — "conteúdo", "argumentação", "escrita" — e não com os quatro critérios exatos da rubrica que o seu colegiado aprovou. Numa correção de rotina passa; num pedido de revisão de nota, não passa.

Você tem a rubrica num arquivo. Está na hora de a Skill usar aquele arquivo, e não uma versão aproximada que ela imaginou.

> *» IA: List — materiais.*

### 🧰 O que você vai usar

- A sua Skill das oficinas anteriores.
- Um documento seu de verdade: rubrica, formulário de plano de ensino, modelo de parecer.

> *» IA: Process — passos numerados. Preservar os modelos editáveis e os breadcrumbs.*

### 👐 Mão na massa

1. Passe o conteúdo do seu documento real para um arquivo de texto na **mesma pasta** da Skill. Nomeie com clareza: `rubrica.md`, `formulario-plano.md`, `modelo-parecer.md`. Nada de `doc2.md` — o Claude navega a pasta pelo nome dos arquivos.

2. Se o arquivo passar de umas cem linhas, comece com um sumário do que tem dentro.

> *» IA: Statement ou Download — modelo editável de sumário. Conteúdo verbatim.*

"""
# Rubrica da disciplina

## Conteúdo
- Critério 1: Domínio conceitual
- Critério 2: Estrutura argumentativa
- Critério 3: Uso de fontes
- Critério 4: Redação e norma culta
- Faixas de nota e descritores
"""

> *» IA: Process — continuação. Preservar os modelos editáveis.*

3. Abra o `SKILL.md` e acrescente uma seção que **remeta** ao arquivo, dizendo o que tem lá dentro. A frase da remissão é o que faz o Claude decidir abrir — "ver rubrica.md" é vago demais.

> *» IA: Statement ou Download — modelo editável de remissão. Conteúdo verbatim.*

"""
## Materiais de apoio

**Rubrica completa, com os quatro critérios e as faixas de nota**:
ver [rubrica.md](rubrica.md)
"""

> *» IA: Process — continuação dos passos.*

4. Ainda no `SKILL.md`, acrescente ao procedimento três instruções sem margem para interpretação.

> *» IA: Statement ou Download — modelo editável de instruções de baixa margem. Conteúdo verbatim.*

"""
- Use os nomes de critério exatamente como estão em rubrica.md.
- Não crie critério que não exista na rubrica.
- Se faltar informação, escreva "A DEFINIR" e liste ao final o que falta.
"""

> *» IA: Process — passos finais. Preservar os breadcrumbs.*

5. Aproveite e **enxugue** o resto do corpo. Passe cada parágrafo por esta pergunta: *o Claude já sabe isto?* Explicação sobre o que é uma rubrica, ele já sabe — corte. A **sua** rubrica, ele não sabe — fica.

6. Recompacte a pasta inteira, agora com dois arquivos dentro, e reenvie em `claude.ai > Configurações > Customize > Skills`.

7. Teste em conversa nova.

   🏁 **Ponto de controle:** os nomes de critério que aparecem na resposta são **os seus**, escritos exatamente como estão no arquivo `rubrica.md` — e não uma aproximação inventada.

> *» IA: Statement — nota sobre custo de arquivos de apoio. Preservar o emoji 📌.*

> 📌 **Não esqueça:** arquivos de apoio só custam alguma coisa quando são abertos. Você pode ter cinco arquivos na pasta e, numa correção comum, o Claude abre só o que precisa. Dividir não é desperdício — é economia.

> *» IA: Statement — alerta sobre dados pessoais. Preservar o emoji ⚠️. Verbatim.*

> ⚠️ **Cuidado sério:** não coloque dados de estudantes nos arquivos da Skill. Nada de nomes, matrículas, notas identificáveis ou situações pessoais. Se quiser exemplo realista, anonimize antes. O conteúdo de uma Skill fica armazenado, e não está coberto por acordos de retenção zero de dados.

> *» IA: Statement — critério de êxito.*

### ✅ Deu certo?

A resposta do Claude usa os nomes exatos dos seus critérios, tirados do arquivo que você anexou — e não uma aproximação inventada por ele.

> *» IA: Accordion — solução de problemas, um item por linha.*

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O Claude ignorou o arquivo anexado | A remissão está vaga. Troque "ver rubrica.md" por "**Rubrica completa com os quatro critérios e as faixas de nota**: ver [rubrica.md](rubrica.md)" |
| Ele leu só um pedaço do arquivo | Acrescente o sumário no topo, e garanta que o arquivo é chamado direto pelo `SKILL.md` e não por outro arquivo de apoio |
| Meu modelo é um `.docx` e não dá para colar | Descreva a estrutura em texto: quais campos, em que ordem, o que vai em cada um. Funciona melhor do que anexar o Word |

> *» IA: Accordion — desafios de extensão, um por linha. Marcado como OPCIONAL.*

### 🚀 Quer ir além?

- Separe os casos raros — plágio, entrega fora do prazo, pedido de recurso — num arquivo `casos-limite.md`, que só será aberto quando um caso desses aparecer.
- Anexe um segundo documento institucional e verifique se o Claude escolhe o certo conforme o pedido.
- Peça ao Claude que aponte que situação previsível o seu procedimento ainda não cobre.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---
---

# Projeto Final — A Skill do seu semestre

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Projeto Final" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja checklist e modelos no meio. ▼▼▼*

> *» IA: Text — enunciado da missão. Preservar o emoji no cabeçalho. Não resumir.*

### 🎯 A missão

Até agora você construiu por partes. Agora fecha o ciclo inteiro numa coisa só: pegar a tarefa que mais consome o seu tempo no semestre e entregar uma Skill que a resolva **e que você consiga provar que resolve**.

Provar é a palavra-chave. Você tem guardado, desde a Oficina 1, um arquivo `linha-de-base.txt` com a resposta crua do Claude a essa mesma tarefa — de quando ele não sabia nada do seu jeito de trabalhar. É contra aquilo que você vai medir. E não adiantaria registrar agora: você já sabe o que quer, e formularia o pedido de outro jeito.

> *» IA: Process — passos do projeto final. Preservar os breadcrumbs e o modelo editável.*

### 👐 Mão na massa

1. **Escreva quatro critérios de êxito. Agora, antes de qualquer teste.** Formule de modo verificável: "bem escrito" não vale; "no máximo uma página, começando pelos acertos" vale.

2. Abra o `linha-de-base.txt` da Oficina 1, avalie contra os quatro critérios e **anote o número**. Provavelmente vai ser 0 ou 1.

3. Faça uma revisão completa da sua Skill aplicando tudo que você aprendeu:

   - Descrição com as duas metades: o que faz **e** quando usar (Oficina 3).
   - Pelo menos uma frase declarando o que a Skill **não** faz (Oficina 3).
   - Corpo enxuto, cada passo começando com verbo no imperativo (Oficina 4).
   - Seu documento real anexado e referenciado com clareza (Oficina 4).
   - Instruções sem margem nos pontos que não admitem variação (Oficina 4).

4. Recompacte e reenvie em `claude.ai > Configurações > Customize > Skills`. Exclua a versão antiga se ela ficar duplicada.

5. Em conversa nova, rode a mesma tarefa da linha de base. Avalie contra os quatro critérios e anote o número.

6. Para cada critério que ainda falhou, identifique a causa e volte à oficina correspondente. Corrija **uma coisa de cada vez**, testando entre uma correção e outra.

7. Chegando a 4 de 4, acrescente ao final do `SKILL.md` a linha de data de revisão.

> *» IA: Statement ou Download — modelo editável da linha de revisão. Conteúdo verbatim.*

"""
Última revisão: [dia/mês/ano]
"""

> *» IA: Process — passo final de compartilhamento.*

8. Envie o ZIP a um colega da sua área, com uma frase explicando quando ele deve usar a Skill. Se você não conseguir escrever essa frase em uma linha, a sua descrição também não consegue — e é a mesma frase.

   🏁 **Ponto de controle:** o colega recebeu o arquivo, conseguiu enviá-lo em `claude.ai > Configurações > Customize > Skills`, e sabe dizer quando usar.

> *» IA: Checklist — lista de conclusão do projeto. Manter marcável, um item por linha, verbatim.*

### 🏁 Como saber que terminou

- [ ] Escrevi os quatro critérios **antes** de testar qualquer coisa.
- [ ] Tenho o número da linha de base anotado.
- [ ] Tenho o número da versão final anotado, e ele é maior.
- [ ] A Skill aciona sozinha em pelo menos três formulações diferentes do pedido.
- [ ] A Skill **não** aciona nos dois pedidos que não deviam acioná-la.
- [ ] A descrição declara expressamente ao menos uma coisa que a Skill não faz.
- [ ] O meu documento real está na pasta e é efetivamente usado na resposta.
- [ ] Cada passo do procedimento começa com um verbo no imperativo.
- [ ] Nenhum dado de estudante entrou em nenhum arquivo da Skill.
- [ ] O `SKILL.md` tem a data da última revisão.
- [ ] Existe uma única entrada da Skill na lista da conta.
- [ ] Um colega recebeu o ZIP e sabe quando usar.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Projeto Final" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---
---

> *» IA: Text — abertura da seção de dicas. Sem marcadores de fronteira de lição nesta seção.*

# A Parte dos Dez — Coisas que ninguém conta antes de você tropeçar nelas

> *» IA: Accordion ou List — dez itens independentes. Um item por linha. Preservar os breadcrumbs.*

1. **Teste sempre em conversa nova.** Quando uma Skill aciona, o conteúdo dela entra na conversa e fica. Testar a versão nova na mesma conversa que carregou a versão velha é receita para conclusão errada.

2. **"Funciona quando eu chamo, nunca sozinha" tem uma causa só em quase todos os casos:** espaço antes dos `---` no topo do arquivo. O cabeçalho quebra, a Skill sobe sem descrição, e sem descrição não há acionamento.

3. **Compacte a pasta, não o arquivo.** E confira abrindo o ZIP. É o erro número um de quem sobe a primeira Skill, e ele não dá mensagem de erro clara.

4. **`Salvar como > Codificação > UTF-8`.** Sem isso, "avaliação" vira "avaliaÃ§Ã£o" e você passa meia hora achando que o problema é outro.

5. **Skill não sincroniza entre lugares.** O que você subiu no claude.ai não aparece no Claude Code nem na API. São três lugares diferentes, e nenhum conversa com os outros.

6. **Se um exemplo da internet tem campos estranhos no cabeçalho, ele provavelmente é do Claude Code.** Coisas como `context: fork` ou `disable-model-invocation` não só não funcionam no claude.ai como **fazem o envio falhar**. Deixe só `name` e `description`.

7. **Não ensine ao Claude o que ele já sabe.** Ele sabe o que é uma rubrica, o que é ABNT, o que é um plano de ensino. Não sabe qual é a **sua** rubrica. Escreva só a segunda parte.

8. **Uma Skill que precisa de "e" para ser descrita são duas Skills.** Skills abrangentes funcionam pior — quem constatou isso foi a própria Anthropic, olhando as centenas que usa internamente.

9. **Guarde as versões anteriores numeradas** no computador: `SKILL-v1.md`, `SKILL-v2.md`. Custa nada e é o que permite voltar quando uma "melhoria" piorar tudo.

10. **Skill de estranho é software de estranho.** Se veio de fora e tem pasta `scripts/` ou acessa endereços na internet, não instale sem alguém do TI olhar junto. E, mesmo nas simples, faça a verificação que qualquer um consegue fazer: **o que ela faz é o que ela diz que faz?**

---

> *» IA: Text — fechamento do curso. Sem marcadores de fronteira de lição. Não resumir.*

## Conseguiu! E agora?

Olha o que aconteceu em pouco menos de duas horas. Você entrou aqui copiando texto da tela para o Word e sai com um arquivo seu, escrito por você, que faz o Claude corrigir, montar ou revisar seguindo o **seu** procedimento — com a sua rubrica, no seu formato, na sua ordem. E, mais importante: você sai sabendo **provar** que ele faz, porque tem dois números anotados em vez de uma impressão.

O que você ganhou não foi velocidade, foi consistência. O mesmo padrão na terça e na sexta, no primeiro trabalho e no quadragésimo, esteja você descansado ou no fim do semestre.

E agora? Faça a segunda. Sério — a segunda Skill leva um terço do tempo da primeira, porque a parte difícil não era a ferramenta, era a lógica. Olhe a sua lista de tarefas repetitivas e escolha a próxima, dando preferência às que têm formato obrigatório da sua instituição: são as que ninguém pode escrever no seu lugar, e as que continuam valendo por anos.

Uma última coisa: este ecossistema muda rápido. Menus mudam de nome, campos novos aparecem. O raciocínio que você aprendeu — carregar só o necessário, escrever a descrição para o vocabulário dos outros, medir em vez de achar — esse não muda. Quando a tela não corresponder ao que está escrito aqui, confie no raciocínio e confira o detalhe.

Boa correção. E que a sua próxima pilha de trabalhos ache você preparado.
