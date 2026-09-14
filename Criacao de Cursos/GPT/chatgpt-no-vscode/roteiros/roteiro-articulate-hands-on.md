# Codex no VS Code Para Leigos — Curso Hands-on

> *» IA: bloco Cover. Título e subtítulo do curso. Não traduzir "Codex" nem "VS Code".*

*No fim deste curso você vai ter organizado uma pasta de verdade e feito o computador responder perguntas sobre os seus próprios arquivos — sem escrever uma linha de código.*

## Antes de Arregaçar as Mangas

> *» IA: bloco Text.*

Este curso é mão na massa. Você vai instalar dois programas e passar as próximas duas horas mandando
um assistente mexer nos seus arquivos — renomear, organizar, procurar coisa, montar gráfico. Você não
vai programar nada. Vai só dizer o que quer, em português.

> *» IA: bloco Checklist. Verbatim, um item por linha.*

**O que você precisa ter aberto agora:**

- Um computador onde você possa instalar programas.
- Uma pasta sua com arquivos de verdade — material de aula, textos, dados.
- Uma conta do ChatGPT (o plano gratuito serve; o Codex está incluído nele).

> *» IA: bloco Statement. Preservar o emoji.*

> 🔑 **Regra de ouro:** este assistente não devolve texto na tela. Ele **mexe nos seus arquivos de
> verdade**. Um texto errado você descarta; um arquivo apagado você tem que recuperar. A Oficina 0
> faz a cópia com você, e ela não é opcional.

## O Mapa da Mão na Massa

> *» IA: bloco Table. Preservar a tabela verbatim.*

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 0 | "Antes de soltar um assistente na minha pasta: como eu seguro as rédeas?" | 7 min |
| 1 | "Como eu instalo isso?" | 20 min |
| 2 | "Tenho trinta arquivos com nomes impossíveis" | 20 min |
| 3 | "Em qual desses arquivos eu falei sobre aquilo?" | 20 min |
| 4 | "Tenho os dados numa planilha e queria um gráfico" | 20 min |
| Projeto Final | Uma disciplina inteira, organizada e que se mantém sozinha | 26 min |

> *» IA: bloco Text.*

Faça a Oficina 0 primeiro. Ela é a única do curso que protege os seus arquivos.

---

# Oficina 0 — Antes de soltar um assistente na sua pasta

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 0" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja tabelas de decisão no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: bloco Text. Preservar o emoji do cabeçalho.*

Você está prestes a autorizar um programa a ler, renomear e apagar arquivos no seu computador. Isso é
diferente de tudo que você já fez com IA até agora: no ChatGPT normal, você cola um texto e recebe
outro; aqui, ele mexe nas suas coisas. Cinco minutos para segurar as rédeas antes de soltar.

### 🧰 O que você vai usar

> *» IA: bloco List. Preservar o emoji do cabeçalho.*

- O explorador de arquivos do seu computador.
- Uma pasta sua com arquivos de verdade.
- O navegador, com a sua conta do ChatGPT.

### 👐 Mão na massa

> *» IA: bloco Process. Preservar os breadcrumbs e não traduzir termos de interface.*

1. **Entenda o que muda.** No ChatGPT que você já conhece, você cola um texto e recebe um texto. Aqui
   é um **agente**: ele lê a sua pasta inteira, cria arquivos, renomeia, apaga. Texto errado se
   descarta; arquivo apagado se recupera — se houver de onde.

2. **Faça a cópia.** Em `Explorador de Arquivos > sua pasta de trabalho`, copie a pasta que você vai
   usar no curso e renomeie a cópia acrescentando `-copia-curso` no fim do nome. **Todo o curso
   acontece na cópia.** A pasta original fica fechada.

3. **Crie a pasta de teste.** Uma pasta nova, chamada `teste-codex`, com três ou quatro arquivos de
   texto sem importância dentro — pode criar do zero, com nomes bem desorganizados de propósito. É
   nela que você vai experimentar na Oficina 1.

4. **Tire da pasta o que não pode entrar.** O agente lê a pasta **inteira** — você não escolhe arquivo
   por arquivo. Então a regra é: o que for sensível **não fica na pasta de trabalho**. Veja a lista
   logo abaixo desta sequência.

5. **Escolha o seu nível de aprovação.** São três, e você vai usar o primeiro até a Oficina 2. Veja a
   tabela de níveis abaixo.

6. **Saiba quanto custa.** O Codex está incluído nos planos do ChatGPT, inclusive o gratuito. Mas a
   cota é **compartilhada** com outros recursos da sua conta, e uma tarefa longa gasta muito mais que
   um pedido curto. Veja o seu plano em `ChatGPT > Menu de perfil > Configurações > Conta`.

7. **Responda para si**, antes de usar isso em material institucional: a sua universidade tem norma
   sobre uso de IA no tratamento de material didático e dados de pesquisa? Se usar, precisa declarar?
   O que você vai dizer aos alunos, que têm a mesma ferramenta?

> *» IA: bloco List. Verbatim, sem acréscimos.*

**Nada disto fica na pasta que o assistente vai ler:**

- Arquivo com nome de aluno ligado a nota, frequência ou ocorrência.
- Resultado de pesquisa ainda não publicado.
- Parecer sigiloso de avaliação por pares.
- Qualquer coisa coberta por acordo de confidencialidade.
- Dado pessoal de terceiro coletado em pesquisa.

> *» IA: bloco Table. Preservar a tabela verbatim. É tabela de decisão: não converter em lista.*

| Nível | O que ele pode fazer | Quando usar |
|---|---|---|
| Somente leitura | Lê e propõe; não muda nada sem você autorizar item a item | **Agora. É o seu ponto de partida.** |
| Automático | Age livre dentro da pasta aberta; pede permissão fora dela | Depois que você já viu como ele se comporta, e só em pasta de cópia |
| Acesso total | Lê qualquer lugar do computador e roda comandos com internet | Casos específicos, decidindo a cada vez |

### ✅ Deu certo?

> *» IA: bloco Statement. Preservar o emoji e o breadcrumb.*

> 🏁 **Ponto de controle:** em `Explorador de Arquivos > sua pasta` existem três coisas — a pasta
> original, a cópia com sufixo `-copia-curso`, e a pasta `teste-codex` com arquivos dentro. E você
> consegue dizer, sem consultar nada, qual nível de aprovação vai usar e por quê.

> *» IA: bloco Statement. Preservar o emoji.*

> ⚠️ **Cuidado:** o passo 2 é o único que separa "experimentei" de "perdi o material de dois
> semestres". Não pule.

### 🚑 Se travar

> *» IA: bloco Accordion, um item por linha da tabela.*

| Problema | O que fazer |
|---|---|
| A pasta é grande demais para copiar | Copie só a subpasta que você vai usar. O curso não precisa da pasta inteira. |
| Não sei o que colocar na pasta de teste | Três arquivos de texto quaisquer, com nomes desorganizados de propósito. É exatamente para isso que eles servem. |
| Não sei qual é o meu plano | Você pode ter duas contas — a institucional e a pessoal. Confira com qual e-mail está conectado. |
| Não encontro os controles de dados | Em conta administrada pela instituição, a configuração é central. Não é falha sua. |

### 🚀 Quer ir além?

> *» IA: bloco Accordion ou List, marcado como OPCIONAL.*

1. **Descubra a norma.** Procure no site da sua instituição por "inteligência artificial" e
   "integridade acadêmica". *Deu certo se:* você achou a norma, ou confirmou que ela não existe.
2. **Veja a sua cota.** Localize o painel de uso da sua conta do ChatGPT. *Deu certo se:* você sabe
   quanto tem e quando renova.
3. **Faça a lista do que não entra.** Percorra a pasta de trabalho e tire de lá dois arquivos que se
   encaixem na lista do passo 4. *Deu certo se:* você conseguiu justificar cada um em uma frase.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 0" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 1 — Instalar e experimentar sem risco

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

### 🎯 O Problema

> *» IA: bloco Text.*

Você nunca abriu um editor de código na vida e está prestes a instalar dois programas. Nesta oficina
você instala, configura a trava de segurança, e dá o primeiro comando numa pasta onde não há nada a
perder.

### 🧰 O que você vai usar

> *» IA: bloco List.*

- Um navegador.
- Permissão de instalar programas.
- A pasta `teste-codex`, criada na Oficina 0.

### 👐 Mão na massa

> *» IA: bloco Process. Preservar os breadcrumbs, o texto entre aspas triplas verbatim e não traduzir termos de interface.*

1. Baixe o Visual Studio Code no site oficial e instale. É um editor de texto gratuito da Microsoft.
   Ele foi feito para quem escreve software, mas o que você vai usar dele é simples: **ele abre uma
   pasta e mostra o que tem dentro.**

2. Abra o editor.

3. Vá em `Visual Studio Code > barra lateral > Extensões`. Extensão é um acessório que se acrescenta
   a um programa para dar a ele uma função nova.

4. Pesquise por `Codex` e instale a extensão.

5. Abra o painel do Codex e entre com a sua conta do ChatGPT.

6. **Configure o modo somente leitura**, conforme você decidiu na Oficina 0. Ele é a trava: o
   assistente propõe, mas não muda nada sem a sua autorização.

7. Abra a pasta de teste em `Visual Studio Code > Arquivo > Abrir Pasta > teste-codex`. **Não abra
   material real ainda.**

8. No painel do Codex, escreva:

   """
   Descreva o que tem nesta pasta: quantos arquivos, quais os nomes e o que cada um contém, em uma
   frase.
   """

9. Compare a resposta com o que você vê em `Visual Studio Code > barra lateral > Explorador`.

### ✅ Deu certo?

> *» IA: bloco Statement. Preservar o emoji e o breadcrumb.*

> 🏁 **Ponto de controle:** os arquivos da pasta `teste-codex` aparecem em
> `Visual Studio Code > barra lateral > Explorador`, o painel do Codex está conectado, e a descrição
> que ele deu bate com o que você vê. Nenhuma pasta de material real foi aberta.

> *» IA: bloco Statement. Preservar o emoji.*

> 💡 **Dica:** repare que você só usou a pasta de teste. Foi de propósito. Da Oficina 2 em diante você
> trabalha na cópia, nunca no original.

### 🚑 Se travar

> *» IA: bloco Accordion, um item por linha da tabela. Preservar os breadcrumbs e não traduzir o comando.*

| Problema | O que fazer |
|---|---|
| Não consigo instalar programas | Sua instituição pode bloquear instalações. Sem o editor, o curso não roda; fale com a TI. |
| Não achei a extensão | Confira a grafia e quem publicou a extensão. O nome exato pode mudar entre versões da loja. |
| Não entra na conta | Confira se está usando a conta ChatGPT certa. É comum ter uma pessoal e uma institucional. |
| O painel abre e não responde | Rode o diagnóstico. **Terminal** é uma janela onde você digita comandos em vez de clicar em botões. Abra em `Visual Studio Code > Terminal > Novo Terminal`, digite `codex doctor` e aperte Enter. Ele verifica problemas de inicialização, conexão e desempenho, e diz o que achou. |
| Não vejo os meus arquivos | O editor só mostra o conteúdo da pasta que você abriu. O que está fora dela não aparece — e o assistente também não vê. |

### 🚀 Quer ir além?

> *» IA: bloco Accordion ou List, marcado como OPCIONAL. Não traduzir o comando.*

1. **Descreva sem abrir.** Peça: "quantas palavras tem cada arquivo desta pasta?". *Deu certo se:* os
   números batem com o que você vê ao abrir os arquivos.
2. **Teste a trava.** Peça para ele apagar um dos arquivos de teste. *Deu certo se:* ele pede
   autorização em vez de apagar — e você recusa.
3. **Diagnóstico preventivo.** Rode `codex doctor` mesmo estando tudo funcionando. *Deu certo se:*
   você sabe reconhecer como é a saída de "tudo certo", para comparar quando der problema.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 2 — Arrumar uma pasta bagunçada

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

### 🎯 O Problema

> *» IA: bloco Text.*

Você tem trinta arquivos chamados `aula1.pdf`, `AULA 2 final.pdf`, `aula2-CORRIGIDA(1).pdf`, e nenhuma
vontade de renomear um por um. Nesta oficina você padroniza tudo — e aprende o hábito que evita
desfazer trinta renomeações.

### 🧰 O que você vai usar

> *» IA: bloco List.*

- A pasta `-copia-curso`, criada na Oficina 0.
- O VS Code com o Codex, em modo somente leitura.

### 👐 Mão na massa

> *» IA: bloco Process. Preservar os breadcrumbs e o texto entre aspas triplas verbatim.*

1. Confirme que você está na cópia. Olhe o nome da pasta no topo de
   `Visual Studio Code > barra lateral > Explorador`.

2. Abra a cópia em `Visual Studio Code > Arquivo > Abrir Pasta`.

3. Faça o pedido com os **três elementos** — padrão, preservação e proposta prévia:

   """
   Renomeie todos os arquivos desta pasta no padrão `aula-NN-tema.pdf`, com NN de dois dígitos e tema
   em minúsculas sem acento. Preserve o conteúdo de cada arquivo, sem alterar nada dentro deles.
   Antes de executar, mostre a lista do que vai virar o quê.
   """

4. **Não aprove ainda.** Leia a lista e faça as três verificações (ver o bloco logo abaixo).

5. Aprove, corrija ou recuse. Corrigir é dizer o que está errado: "os itens 4 e 9 estão com o tema
   trocado; refaça esses dois".

6. Confira a pasta em `Visual Studio Code > barra lateral > Explorador`: os nomes mudaram e a
   contagem de arquivos é a mesma.

> *» IA: bloco Checklist. Verbatim, um item por linha.*

**As três verificações, antes de aprovar:**

- **Está completa?** O número de itens propostos bate com o número de arquivos que você esperava.
- **Está correta?** Confira **cinco** itens escolhidos ao acaso, não só o primeiro.
- **Tem algo que não deveria estar aí?** Um arquivo que você não esperava que fosse tocado é sinal de
  que o pedido pegou mais do que devia.

### ✅ Deu certo?

> *» IA: bloco Statement. Preservar o emoji e o breadcrumb.*

> 🏁 **Ponto de controle:** em `Visual Studio Code > barra lateral > Explorador`, os arquivos aparecem
> com o padrão que você pediu, e a contagem é a mesma de antes. Nenhum arquivo sumiu. Se quiser
> certeza, abra a pasta original em `Explorador de Arquivos` e compare o número de itens.

> *» IA: bloco Statement. Preservar o emoji.*

> 💡 **Dica:** pedir a lista antes é a diferença entre corrigir uma lista e desfazer trinta
> renomeações. É o hábito mais barato deste curso.

### 🚑 Se travar

> *» IA: bloco Accordion, um item por linha da tabela.*

| Problema | O que fazer |
|---|---|
| Ele executou sem mostrar a lista | Ou o modo não está em somente leitura, ou o pedido não exigiu a proposta prévia. Corrija os dois. |
| Ele renomeou errado | Volte para a pasta original e recomece. Refaça o pedido dizendo o padrão com mais precisão. |
| A proposta pegou arquivos que não deviam | Recuse e delimite: "apenas os arquivos com extensão .pdf", ou "apenas os da subpasta X". |
| Ele pediu permissão e eu não entendi | Recuse. A regra não tem exceção: não se autoriza o que não se entendeu. |
| Um arquivo sumiu | Recupere da pasta original. É para isso que a cópia da Oficina 0 existe. |

### 🚀 Quer ir além?

> *» IA: bloco Accordion ou List, marcado como OPCIONAL.*

1. **Subpastas por unidade.** Peça para organizar os arquivos em subpastas numeradas por unidade, com
   lista prévia. *Deu certo se:* nenhum arquivo ficou de fora de alguma subpasta.
2. **Os duplicados.** Peça: "há arquivos com conteúdo duplicado ou muito parecido nesta pasta?".
   *Deu certo se:* você encontrou pelo menos um par que não sabia que existia.
3. **O relatório do que mudou.** Peça um arquivo de texto listando cada renomeação feita.
   *Deu certo se:* você consegue reconstruir os nomes antigos a partir dele.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 3 — Perguntar aos seus arquivos

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

### 🎯 O Problema

> *» IA: bloco Text.*

Você sabe que escreveu sobre determinado assunto em algum lugar — num plano de ensino antigo, numa
avaliação, num texto de apoio — mas não lembra em qual arquivo. Nesta oficina você para de procurar à
mão.

### 🧰 O que você vai usar

> *» IA: bloco List.*

- A pasta `-copia-curso`, com vários documentos de texto.
- O VS Code com o Codex.

### 👐 Mão na massa

> *» IA: bloco Process. Preservar os breadcrumbs e os textos entre aspas triplas verbatim.*

1. Abra a pasta `-copia-curso` em `Visual Studio Code > Arquivo > Abrir Pasta`.

2. Localize o assunto:

   """
   Em quais arquivos desta pasta eu menciono [assunto]? Liste o nome do arquivo e o trecho onde
   aparece. Não altere nada.
   """

3. Confira os resultados abrindo um dos arquivos apontados. Ele pode errar — vale checar.

4. Peça o panorama:

   """
   Faça um resumo de uma frase de cada arquivo desta pasta, organizados em ordem alfabética.
   """

5. Agora o entregável. Para criar arquivo, o assistente precisa de autorização — **e é aqui que você
   sai do modo somente leitura pela primeira vez**, deliberadamente:

   """
   Crie um arquivo chamado `indice.md` na raiz desta pasta, com a lista de todos os arquivos e um
   resumo de uma frase de cada um. Não altere nenhum arquivo existente.
   """

6. Autorize apenas a criação do `indice.md`. Se ele pedir para tocar em outra coisa, recuse.

7. Abra o `indice.md` e confira: cada arquivo listado existe, e cada resumo bate com o conteúdo.

### ✅ Deu certo?

> *» IA: bloco Statement. Preservar o emoji e o breadcrumb.*

> 🏁 **Ponto de controle:** o arquivo `indice.md` aparece em
> `Visual Studio Code > barra lateral > Explorador`, e ao abri-lo você vê a lista completa com os
> resumos. Nenhum outro arquivo da pasta foi alterado — confira comparando a contagem com a pasta
> original.

> *» IA: bloco Statement. Preservar o emoji.*

> 📌 **Não esqueça:** este é o primeiro momento do curso em que você autoriza uma escrita. Autorize a
> criação de **um** arquivo, e nada além disso.

### 🚑 Se travar

> *» IA: bloco Accordion, um item por linha da tabela.*

| Problema | O que fazer |
|---|---|
| Ele não leu os PDFs | Nem todo formato é lido diretamente. Converta os que importam para texto, ou trabalhe com os que ele lê. |
| O resumo está errado | Ele erra. Por isso o passo 7 existe. Corrija à mão. |
| Ele não criou o arquivo | Você está em modo somente leitura, que impede escrita. É o comportamento esperado. Autorize a criação especificamente. |
| Ele quis mexer em outros arquivos | Recuse. Reforce no pedido: "crie apenas o `indice.md` e não altere nenhum arquivo existente". |

### 🚀 Quer ir além?

> *» IA: bloco Accordion ou List, marcado como OPCIONAL.*

1. **Índice por tema.** Peça um índice organizado por assunto, e não por nome de arquivo.
   *Deu certo se:* a agrupação faz sentido para você e revelou uma categoria que você não tinha
   percebido.
2. **O que está faltando.** Pergunte: "que assuntos um curso desta área trataria e que não aparecem
   em nenhum arquivo desta pasta?". *Deu certo se:* pelo menos uma lacuna apontada era real.
3. **Linha do tempo.** Peça a lista dos arquivos ordenada por data de criação, com o resumo.
   *Deu certo se:* você consegue ver como o material evoluiu ao longo dos semestres.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 4 — Um gráfico sem programar

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja tabela de decisão no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: bloco Text.*

Você tem as médias da turma numa planilha e queria um gráfico para mostrar em aula. Não em cinco
cliques do Excel — um gráfico que você possa refazer todo semestre mudando só o arquivo de dados.
Nesta oficina você pede e recebe.

### 🧰 O que você vai usar

> *» IA: bloco List.*

- Uma planilha sua, sem nome de aluno.
- A pasta `teste-codex`, que é onde esta oficina acontece.
- O VS Code com o Codex.

### 👐 Mão na massa

> *» IA: bloco Process. Preservar os breadcrumbs, o texto entre aspas triplas verbatim e não traduzir termos de interface.*

1. **Tire os nomes.** Antes de exportar, substitua nomes de aluno por identificadores — `A01`, `A02`.
   Vale a regra da Oficina 0: o que é sensível não entra na pasta.

2. **Exporte em CSV.** CSV é um formato de planilha simplificado, em texto puro, que qualquer programa
   lê. No seu editor de planilhas:
   `planilha > Arquivo > Salvar como > CSV (separado por vírgulas)`. Salve dentro da pasta
   `teste-codex`, com o nome `notas.csv`.

3. Abra a pasta `teste-codex` em `Visual Studio Code > Arquivo > Abrir Pasta`.

4. Peça o gráfico:

   """
   A partir do arquivo `notas.csv`, faça um gráfico de barras das médias por turma e salve como
   imagem PNG nesta pasta. Antes de executar, diga o que você vai fazer e o que precisa instalar.
   """

5. **Decida sobre a rede.** Provavelmente ele vai dizer que precisa de acesso à internet para instalar
   uma biblioteca de gráficos. Por padrão o acesso à rede vem desligado, e é você quem decide. Use a
   tabela de critério abaixo.

6. Autorize (ou não) e aguarde.

7. Abra a imagem gerada, clicando nela em `Visual Studio Code > barra lateral > Explorador`.

8. **Confira os números** do gráfico contra a planilha original. Um por um.

> *» IA: bloco Table. Preservar a tabela verbatim. É tabela de decisão: não converter em lista.*

| Situação | Autorizar acesso à rede? |
|---|---|
| Pasta de teste, sem dado sensível, para instalar biblioteca de gráfico | Sim |
| Pasta com material real ou dado de pesquisa | Não. Mova os dados para a pasta de teste primeiro |
| Você não entendeu o que ele quer instalar ou por quê | Não. Peça para explicar antes |

### ✅ Deu certo?

> *» IA: bloco Statement. Preservar o emoji e o breadcrumb.*

> 🏁 **Ponto de controle:** existe um arquivo de imagem na pasta `teste-codex`, visível em
> `Visual Studio Code > barra lateral > Explorador`, ele abre no editor mostrando um gráfico de
> barras, e cada valor do gráfico bate com a planilha.

> *» IA: bloco Statement. Preservar o emoji.*

> ⚠️ **Cuidado:** esta é a única oficina do curso em que o assistente executa código e pede acesso à
> internet. Por isso ela acontece na pasta de teste, e por isso os nomes saem no passo 1.

### 🚑 Se travar

> *» IA: bloco Accordion, um item por linha da tabela.*

| Problema | O que fazer |
|---|---|
| Ele disse que precisa instalar coisas | Esperado. Aplique o critério do passo 5. |
| Os números não batem | Confira o separador decimal do CSV. Em português é comum ser vírgula, e o esperado ser ponto. Diga isso a ele: "os decimais usam vírgula". |
| O gráfico está ilegível | Peça ajustes concretos: "aumente a fonte dos rótulos", "coloque os valores em cima de cada barra", "use tons de cinza". |
| A tarefa está demorando muito | Tarefa longa consome muito mais da sua cota que um pedido curto. Interrompa e peça algo mais simples. |
| Ele não achou o arquivo | Confira se o `notas.csv` está dentro da pasta que você abriu no editor. |

### 🚀 Quer ir além?

> *» IA: bloco Accordion ou List, marcado como OPCIONAL.*

1. **Três gráficos.** Peça três formas diferentes de visualizar os mesmos dados e escolha.
   *Deu certo se:* você consegue dizer o que cada forma esconde.
2. **O gráfico que se repete.** Peça para ele deixar salvo o procedimento, de modo que no semestre que
   vem baste trocar o `notas.csv`. *Deu certo se:* você consegue refazer trocando só o arquivo.
3. **A pergunta aos dados.** Pergunte: "o que estes dados mostram que não é óbvio?". *Deu certo se:*
   você conferiu a afirmação contra a planilha — e ela se sustenta, ou você descobriu que não.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Projeto Final — Uma disciplina que se organiza sozinha no semestre que vem

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Projeto Final" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja modelo de arquivo no meio. ▼▼▼*

### 🎯 A missão

> *» IA: bloco Text. Preservar o emoji do cabeçalho.*

Não é organizar uma pasta. É deixar a pasta organizada **e escrever a regra** para que ela se organize
do mesmo jeito no semestre que vem, sem você repetir nada.

Essa última parte é a que nenhuma oficina cobriu. O Codex admite que você escreva, uma única vez, as
regras que ele deve seguir naquela pasta — em português, num arquivo de texto que fica lá dentro. A
partir daí ele as consulta sozinho, em todo pedido.

### 🧰 O que você vai usar

> *» IA: bloco List.*

- A pasta de uma disciplina sua, em cópia.
- O VS Code com o Codex.
- Tudo o que você fez nas Oficinas 2, 3 e 4.

### 👐 Mão na massa

> *» IA: bloco Process. Preservar os breadcrumbs e os textos entre aspas triplas verbatim.*

1. **Confirme a cópia.** Nome da pasta com sufixo, original fechado. E tire da pasta o que não pode
   estar lá (Oficina 0, passo 4).

2. **Peça o diagnóstico:**

   """
   Descreva o que tem nesta pasta: quantos arquivos, de que tipos, com que padrões de nome. Aponte o
   que está inconsistente. Não altere nada.
   """

3. **Padronize os nomes** (Oficina 2), com lista prévia e as três verificações antes de aprovar.

4. **Organize em subpastas**, também com lista prévia.

5. **Monte o índice** (Oficina 3), autorizando apenas a criação do `indice.md`.

6. **Escreva o arquivo de instruções.** Crie, na raiz da pasta, um arquivo de texto que responda a
   quatro perguntas, em português — veja o modelo em "Mão na massa", abaixo. A quarta pergunta é a
   mais importante e a que ninguém escreve: um arquivo que só diz o que fazer deixa o resto em
   aberto; um que diz o que **não** fazer estabelece um limite para todos os pedidos futuros.

7. **Teste a regra.** Faça um pedido que **não** repita nenhuma das regras que você escreveu — por
   exemplo:

   """
   Acrescente estes três arquivos novos à pasta, seguindo a organização existente. Antes de executar,
   mostre a lista.
   """

   Veja se ele obedece o padrão sozinho.

8. **Confira tudo** contra a pasta original: contagem de arquivos, nada perdido, nada alterado por
   dentro.

9. **Anote** as três instruções que funcionaram melhor.

### 🏁 Como saber que terminou

> *» IA: bloco Checklist. Verbatim, um item por linha.*

- [ ] Os arquivos estão com nomes padronizados, no padrão que você definiu.
- [ ] A pasta está organizada em subpastas.
- [ ] Existe um `indice.md` que lista tudo, e os resumos batem com os arquivos.
- [ ] Existe um arquivo de instruções que responde às quatro perguntas, inclusive a quarta.
- [ ] Você fez um pedido sem repetir as regras, e o agente as seguiu sozinho.
- [ ] A contagem de arquivos bate com a da pasta original. Nada sumiu.
- [ ] Nenhum arquivo das categorias vedadas na Oficina 0 estava na pasta.
- [ ] A pasta original continua intacta.
- [ ] Você respondeu, para si, se este trabalho precisa declarar o uso de IA.
- [ ] Você tem três instruções anotadas para reusar.

### Mão na massa

> *» IA: bloco Statement ou Download. Conteúdo do modelo verbatim, em aspas triplas. Não traduzir os exemplos de padrão de nome.*

Modelo do arquivo de instruções, para o passo 6. Salvar na raiz da pasta, substituindo o conteúdo
entre colchetes.

"""
# Instruções desta pasta

## O que há aqui
[Ex.: material da disciplina de ..., semestres de ... a ...]

## Como nomear os arquivos
[Ex.: aula-NN-tema.pdf, com NN de dois dígitos e tema em minúsculas, sem acento e sem espaço]

## Como organizar
[Ex.: uma subpasta por unidade, numeradas de 01- a 04-. Provas e gabaritos ficam em 99-avaliacoes]

## O que NUNCA fazer aqui
- Não alterar o conteúdo de nenhum arquivo.
- Não apagar nada. Se algo parecer sobrando, liste em vez de remover.
- Não mexer na subpasta [nome].
- [outra restrição própria]

## Antes de executar
Sempre mostre a lista do que vai fazer e aguarde aprovação.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Projeto Final" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# A Parte dos Dez — Coisas que Funcionam no Codex

> *» IA: bloco List ou Accordion. Verbatim, um item por linha. Preservar os breadcrumbs e não traduzir o comando.*

1. **Copie a pasta antes.** Sempre. É a regra que não tem exceção.
2. **Comece em somente leitura.** Você aprende o comportamento dele sem arriscar nada.
3. **Peça a lista antes de executar.** "Antes de executar, mostre o que você vai fazer."
4. **Confira cinco itens, não um.** Amostrar é revisar; ler o primeiro item é fingir que revisou.
5. **Seja específico sobre o padrão.** `aula-NN-tema.pdf` funciona; "organize isso" não.
6. **Declare o que preservar.** "Preserve o conteúdo dos arquivos e não apague nada."
7. **Não autorize o que não entendeu.** Recusar é grátis; recuperar não é.
8. **O que é sensível fica fora da pasta.** Ele lê a pasta inteira, não o que você escolhe.
9. **`codex doctor` no terminal** quando algo não funcionar
   (`Visual Studio Code > Terminal > Novo Terminal`).
10. **Escreva as regras uma vez.** O arquivo de instruções da pasta poupa você de repetir o padrão
    todo semestre.

## Conseguiu! E agora?

> *» IA: bloco Text.*

Você organizou uma pasta de verdade, fez o computador responder perguntas sobre o seu próprio
material, gerou um gráfico a partir dos seus dados, e — o mais importante — deixou escrita a regra
para que isso se repita sozinho. Nada disso exigiu uma linha de código.

O próximo passo é repetir em outra pasta. Escolha a disciplina seguinte e faça o ciclo inteiro. E
quando a cópia manual começar a incomodar, o assunto a estudar chama-se **versionamento**: é o jeito
sistemático de desfazer alterações, e é a evolução natural do que você acabou de aprender.
