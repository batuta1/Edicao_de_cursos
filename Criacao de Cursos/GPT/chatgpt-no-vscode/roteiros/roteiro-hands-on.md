# Roteiro Final — ChatGPT (Codex) no VS Code (Hands-on)

**Público-Alvo:** professores universitários, de qualquer área, que não programam e não pretendem
programar.

**Objetivo Geral:** levar o docente a instalar o Visual Studio Code e a extensão Codex e executar,
com as próprias mãos, quatro tarefas reais sobre pastas de arquivos — padronizar nomes, consultar o
próprio material, produzir um gráfico e montar um índice —, mantendo em todas elas o controle sobre o
que o agente pode alterar.

**Pré-requisitos:** saber criar pastas e mover arquivos; conta ativa no ChatGPT, ainda que gratuita;
permissão para instalar programas; uma pasta de trabalho real, da qual será feita cópia na Oficina 0;
**nenhum conhecimento de programação**.

**Carga horária:** 113 minutos (detalhamento em `../carga-horaria/carga-horaria-hands-on.md`).

---

## Estrutura do Curso

| Nível | Unidades | Finalidade |
|---|---|---|
| Nível 0 — Controle | Oficina 0 | Estabelecer os limites antes de o agente tocar em qualquer arquivo |
| Nível 1 — Acesso | Oficina 1 | Instalar e experimentar em pasta de teste |
| Nível 2 — Produção | Oficinas 2 a 4 | Organizar, consultar e analisar arquivos próprios |
| Nível 3 — Integração | Projeto Final | Uma disciplina inteira, com padrão que se repete sozinho |
| Apêndice | A Parte dos Dez | Repertório para consulta rápida |

**Anexos:** não há anexos. Os assuntos deslocados constam do Roadmap de Expansão em
`../_processo/02-analise-hands-on.md`.

> **Nota sobre a auditoria.** Os onze gargalos da matriz de soluções de
> `../_processo/02-analise-hands-on.md` foram endereçados. Três decisões declaradas: (a) o modo
> somente leitura passa a ser configurado explicitamente na Oficina 0 e mantido até a Oficina 2;
> (b) a Oficina 1 opera exclusivamente em uma pasta de teste criada para isso, e nenhum material real
> é aberto antes da Oficina 2; (c) `codex doctor` deixou de ser desafio opcional e foi promovido à
> tabela "Se travar" da Oficina 1, com o terminal explicado antes de mencionado.

---

# Codex no VS Code Para Leigos — Curso Hands-on

*No fim deste curso você vai ter organizado uma pasta de verdade e feito o computador responder perguntas sobre os seus próprios arquivos — sem escrever uma linha de código.*

## Antes de Arregaçar as Mangas

Este curso é mão na massa. Você vai instalar dois programas e passar as próximas duas horas mandando
um assistente mexer nos seus arquivos — renomear, organizar, procurar coisa, montar gráfico. Você não
vai programar nada. Vai só dizer o que quer, em português.

**O que você precisa ter aberto agora:**

- Um computador onde você possa instalar programas.
- Uma pasta sua com arquivos de verdade — material de aula, textos, dados.
- Uma conta do ChatGPT (o plano gratuito serve; o Codex está incluído nele).

> 🔑 **Regra de ouro:** este assistente não devolve texto na tela. Ele **mexe nos seus arquivos de
> verdade**. Um texto errado você descarta; um arquivo apagado você tem que recuperar. A Oficina 0
> faz a cópia com você, e ela não é opcional.

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 0 | "Antes de soltar um assistente na minha pasta: como eu seguro as rédeas?" | 7 min |
| 1 | "Como eu instalo isso?" | 20 min |
| 2 | "Tenho trinta arquivos com nomes impossíveis" | 20 min |
| 3 | "Em qual desses arquivos eu falei sobre aquilo?" | 20 min |
| 4 | "Tenho os dados numa planilha e queria um gráfico" | 20 min |
| Projeto Final | Uma disciplina inteira, organizada e que se mantém sozinha | 26 min |

Faça a Oficina 0 primeiro. Ela é a única do curso que protege os seus arquivos.

---

# Oficina 0 — Antes de soltar um assistente na sua pasta

## Descrição

- **Objetivos da Aula:** mostrar a diferença entre um sistema que responde e um que executa;
  apresentar os três níveis de aprovação e fixar o modo somente leitura como ponto de partida; criar
  a cópia de segurança e a pasta de teste; e nomear o que deve ficar fora da pasta de trabalho.
- **Habilidades Esperadas:** ao final, você sabe explicar o que o assistente pode fazer com os seus
  arquivos, tem a cópia e a pasta de teste criadas, e sabe qual regra usar para decidir o que não
  entra na pasta.

### 🎯 O Problema

Você está prestes a autorizar um programa a ler, renomear e apagar arquivos no seu computador. Isso é
diferente de tudo que você já fez com IA até agora: no ChatGPT normal, você cola um texto e recebe
outro; aqui, ele mexe nas suas coisas. Cinco minutos para segurar as rédeas antes de soltar.

### 🧰 O que você vai usar

- O explorador de arquivos do seu computador.
- Uma pasta sua com arquivos de verdade.
- O navegador, com a sua conta do ChatGPT.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** janela do explorador de arquivos mostrando três itens lado a lado — a
  pasta original, a pasta com sufixo `-copia-curso`, e a pasta `teste-codex` com três arquivos de
  exemplo dentro. Os três nomes precisam estar legíveis.

1. **Entenda o que muda.** No ChatGPT que você já conhece, você cola um texto e recebe um texto. Aqui
   é um **agente**: ele lê a sua pasta inteira, cria arquivos, renomeia, apaga. Texto errado se
   descarta; arquivo apagado se recupera — se houver de onde.

2. **Faça a cópia.** No explorador de arquivos, copie a pasta que você vai usar no curso e renomeie a
   cópia acrescentando `-copia-curso` no fim do nome. **Todo o curso acontece na cópia.** A pasta
   original fica fechada.

3. **Crie a pasta de teste.** Uma pasta nova, chamada `teste-codex`, com três ou quatro arquivos de
   texto sem importância dentro — pode criar do zero, com nomes bem desorganizados de propósito. É
   nela que você vai experimentar na Oficina 1.

4. **Tire da pasta o que não pode entrar.** O agente lê a pasta **inteira** — você não escolhe
   arquivo por arquivo. Então a regra é: o que for sensível **não fica na pasta de trabalho**.

   - Arquivo com nome de aluno ligado a nota, frequência ou ocorrência.
   - Resultado de pesquisa ainda não publicado.
   - Parecer sigiloso de avaliação por pares.
   - Qualquer coisa coberta por acordo de confidencialidade.
   - Dado pessoal de terceiro coletado em pesquisa.

5. **Escolha o seu nível de aprovação.** São três. Você vai usar o primeiro até a Oficina 2:

   | Nível | O que ele pode fazer | Quando usar |
   |---|---|---|
   | Somente leitura | Lê e propõe; não muda nada sem você autorizar item a item | **Agora. É o seu ponto de partida.** |
   | Automático | Age livre dentro da pasta aberta; pede permissão fora dela | Depois que você já viu como ele se comporta, e só em pasta de cópia |
   | Acesso total | Lê qualquer lugar do computador e roda comandos com internet | Casos específicos, decidindo a cada vez |

6. **Saiba quanto custa.** O Codex está incluído nos planos do ChatGPT, inclusive o gratuito. Mas a
   cota é **compartilhada** com outros recursos da sua conta, e uma tarefa longa gasta muito mais que
   um pedido curto. Veja o seu plano em `ChatGPT > Menu de perfil > Configurações > Conta`.

7. **Responda para si**, antes de usar isso em material institucional: a sua universidade tem norma
   sobre uso de IA no tratamento de material didático e dados de pesquisa? Se usar, precisa declarar?
   O que você vai dizer aos alunos, que têm a mesma ferramenta?

### ✅ Deu certo?

🏁 **Ponto de controle:** no explorador de arquivos existem três coisas — a pasta original, a cópia
com sufixo `-copia-curso`, e a pasta `teste-codex` com arquivos dentro. E você consegue dizer, sem
consultar nada, qual nível de aprovação vai usar e por quê.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| A pasta é grande demais para copiar | Copie só a subpasta que você vai usar. O curso não precisa da pasta inteira. |
| Não sei o que colocar na pasta de teste | Três arquivos de texto quaisquer, com nomes desorganizados de propósito. É exatamente para isso que eles servem. |
| Não sei qual é o meu plano | Você pode ter duas contas — a institucional e a pessoal. Confira com qual e-mail está conectado. |
| Não encontro os controles de dados | Em conta administrada pela instituição, a configuração é central. Não é falha sua. |

> ⚠️ **Cuidado:** o passo 2 é o único que separa "experimentei" de "perdi o material de dois
> semestres". Não pule.

### 🚀 Quer ir além?

1. **Descubra a norma.** Procure no site da sua instituição por "inteligência artificial" e
   "integridade acadêmica". *Deu certo se:* você achou a norma, ou confirmou que ela não existe.
2. **Veja a sua cota.** Localize o painel de uso da sua conta do ChatGPT. *Deu certo se:* você sabe
   quanto tem e quando renova.
3. **Faça a lista do que não entra.** Percorra a pasta de trabalho e tire de lá dois arquivos que se
   encaixem na lista do passo 4. *Deu certo se:* você conseguiu justificar cada um em uma frase.

---

# Oficina 1 — Instalar e experimentar sem risco

## Descrição

- **Objetivos da Aula:** conduzir a instalação do editor e da extensão; configurar o modo somente
  leitura; e fazer o primeiro pedido em ambiente sem valor.
- **Habilidades Esperadas:** ao final, você tem o editor e a extensão funcionando, sabe abrir uma
  pasta, e fez o primeiro pedido — na pasta de teste, não no seu material.

### 🎯 O Problema

Você nunca abriu um editor de código na vida e está prestes a instalar dois programas. Nesta oficina
você instala, configura a trava de segurança, e dá o primeiro comando numa pasta onde não há nada a
perder.

### 🧰 O que você vai usar

- Um navegador.
- Permissão de instalar programas.
- A pasta `teste-codex`, criada na Oficina 0.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** o Visual Studio Code com a pasta `teste-codex` aberta na barra lateral
  esquerda (mostrando os arquivos de exemplo) e o painel do Codex à direita, com a resposta ao
  primeiro pedido visível.

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

   > Descreva o que tem nesta pasta: quantos arquivos, quais os nomes e o que cada um contém, em uma
   > frase.

9. Compare a resposta com o que você vê na barra lateral esquerda.

### ✅ Deu certo?

🏁 **Ponto de controle:** os arquivos da pasta `teste-codex` aparecem na barra lateral esquerda, o
painel do Codex está conectado, e a descrição que ele deu bate com o que você vê. Nenhuma pasta de
material real foi aberta.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não consigo instalar programas | Sua instituição pode bloquear instalações. Sem o editor, o curso não roda; fale com a TI. |
| Não achei a extensão | Confira a grafia e quem publicou a extensão. O nome exato pode mudar entre versões da loja. |
| Não entra na conta | Confira se está usando a conta ChatGPT certa. É comum ter uma pessoal e uma institucional. |
| O painel abre e não responde | Rode o diagnóstico. **Terminal** é uma janela onde você digita comandos em vez de clicar em botões. Abra em `Visual Studio Code > Terminal > Novo Terminal`, digite `codex doctor` e aperte Enter. Ele verifica problemas de inicialização, conexão e desempenho, e diz o que achou. |
| Não vejo os meus arquivos | O editor só mostra o conteúdo da pasta que você abriu. O que está fora dela não aparece — e o assistente também não vê. |

> 💡 **Dica:** repare que você só usou a pasta de teste. Foi de propósito. Da Oficina 2 em diante você
> trabalha na cópia, nunca no original.

### 🚀 Quer ir além?

1. **Descreva sem abrir.** Peça: "quantas palavras tem cada arquivo desta pasta?". *Deu certo se:* os
   números batem com o que você vê ao abrir os arquivos.
2. **Teste a trava.** Peça para ele apagar um dos arquivos de teste. *Deu certo se:* ele pede
   autorização em vez de apagar — e você recusa.
3. **Diagnóstico preventivo.** Rode `codex doctor` mesmo estando tudo funcionando. *Deu certo se:*
   você sabe reconhecer como é a saída de "tudo certo", para comparar quando der problema.

---

# Oficina 2 — Arrumar uma pasta bagunçada

## Descrição

- **Objetivos da Aula:** ensinar o pedido em três elementos — padrão, preservação e proposta prévia;
  e ensinar as três verificações de revisão antes de aprovar.
- **Habilidades Esperadas:** ao final, você padroniza os nomes de uma pasta inteira sem perder
  nenhum arquivo, e sabe conferir a proposta por amostragem antes de autorizar.

### 🎯 O Problema

Você tem trinta arquivos chamados `aula1.pdf`, `AULA 2 final.pdf`, `aula2-CORRIGIDA(1).pdf`, e
nenhuma vontade de renomear um por um. Nesta oficina você padroniza tudo — e aprende o hábito que
evita desfazer trinta renomeações.

### 🧰 O que você vai usar

- A pasta `-copia-curso`, criada na Oficina 0.
- O VS Code com o Codex, em modo somente leitura.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** painel do Codex mostrando a lista de renomeações propostas — nome antigo
  e nome novo lado a lado — com a barra lateral esquerda ainda exibindo os nomes antigos. O contraste
  entre "proposto" e "ainda não feito" é o que a captura precisa mostrar.

1. Confirme que você está na cópia. Olhe o nome da pasta no topo da barra lateral.

2. Abra a cópia em `Visual Studio Code > Arquivo > Abrir Pasta`.

3. Faça o pedido com os **três elementos** — padrão, preservação e proposta prévia:

   > Renomeie todos os arquivos desta pasta no padrão `aula-NN-tema.pdf`, com NN de dois dígitos e
   > tema em minúsculas sem acento. Preserve o conteúdo de cada arquivo, sem alterar nada dentro
   > deles. Antes de executar, mostre a lista do que vai virar o quê.

4. **Não aprove ainda.** Leia a lista e faça as três verificações:

   - **Está completa?** O número de itens propostos bate com o número de arquivos que você esperava.
   - **Está correta?** Confira **cinco** itens escolhidos ao acaso, não só o primeiro.
   - **Tem algo que não deveria estar aí?** Um arquivo que você não esperava que fosse tocado é sinal
     de que o pedido pegou mais do que devia.

5. Aprove, corrija ou recuse. Corrigir é dizer o que está errado: "os itens 4 e 9 estão com o tema
   trocado; refaça esses dois".

6. Confira a pasta na barra lateral esquerda: os nomes mudaram e a contagem de arquivos é a mesma.

### ✅ Deu certo?

🏁 **Ponto de controle:** na barra lateral esquerda, os arquivos aparecem com o padrão que você pediu,
e a contagem é a mesma de antes. Nenhum arquivo sumiu. Se quiser certeza, abra a pasta original no
explorador de arquivos e compare o número de itens.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Ele executou sem mostrar a lista | Ou o modo não está em somente leitura, ou o pedido não exigiu a proposta prévia. Corrija os dois. |
| Ele renomeou errado | Volte para a pasta original e recomece. Refaça o pedido dizendo o padrão com mais precisão. |
| A proposta pegou arquivos que não deviam | Recuse e delimite: "apenas os arquivos com extensão .pdf", ou "apenas os da subpasta X". |
| Ele pediu permissão e eu não entendi | Recuse. A regra não tem exceção: não se autoriza o que não se entendeu. |
| Um arquivo sumiu | Recupere da pasta original. É para isso que a cópia da Oficina 0 existe. |

> 💡 **Dica:** pedir a lista antes é a diferença entre corrigir uma lista e desfazer trinta
> renomeações. É o hábito mais barato deste curso.

### 🚀 Quer ir além?

1. **Subpastas por unidade.** Peça para organizar os arquivos em subpastas numeradas por unidade,
   com lista prévia. *Deu certo se:* nenhum arquivo ficou de fora de alguma subpasta.
2. **Os duplicados.** Peça: "há arquivos com conteúdo duplicado ou muito parecido nesta pasta?".
   *Deu certo se:* você encontrou pelo menos um par que não sabia que existia.
3. **O relatório do que mudou.** Peça um arquivo de texto listando cada renomeação feita.
   *Deu certo se:* você consegue reconstruir os nomes antigos a partir dele.

---

# Oficina 3 — Perguntar aos seus arquivos

## Descrição

- **Objetivos da Aula:** usar o agente como mecanismo de consulta ao próprio material; e produzir um
  índice que sobrevive ao curso.
- **Habilidades Esperadas:** ao final, você localiza um assunto dentro de uma pasta sem abrir arquivo
  por arquivo, e tem um índice navegável do seu próprio material.

### 🎯 O Problema

Você sabe que escreveu sobre determinado assunto em algum lugar — num plano de ensino antigo, numa
avaliação, num texto de apoio — mas não lembra em qual arquivo. Nesta oficina você para de procurar à
mão.

### 🧰 O que você vai usar

- A pasta `-copia-curso`, com vários documentos de texto.
- O VS Code com o Codex.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** o Visual Studio Code com o arquivo `indice.md` aberto no editor,
  mostrando a lista de arquivos com os resumos, e a barra lateral esquerda exibindo o arquivo recém-
  criado na pasta.

1. Abra a pasta `-copia-curso` no editor.

2. Localize o assunto:

   > Em quais arquivos desta pasta eu menciono [assunto]? Liste o nome do arquivo e o trecho onde
   > aparece. Não altere nada.

3. Confira os resultados abrindo um dos arquivos apontados. Ele pode errar — vale checar.

4. Peça o panorama:

   > Faça um resumo de uma frase de cada arquivo desta pasta, organizados em ordem alfabética.

5. Agora o entregável. Para criar arquivo, o assistente precisa de autorização — **e é aqui que você
   sai do modo somente leitura pela primeira vez**, deliberadamente:

   > Crie um arquivo chamado `indice.md` na raiz desta pasta, com a lista de todos os arquivos e um
   > resumo de uma frase de cada um. Não altere nenhum arquivo existente.

6. Autorize apenas a criação do `indice.md`. Se ele pedir para tocar em outra coisa, recuse.

7. Abra o `indice.md` e confira: cada arquivo listado existe, e cada resumo bate com o conteúdo.

### ✅ Deu certo?

🏁 **Ponto de controle:** o arquivo `indice.md` aparece na barra lateral esquerda, e ao abri-lo você
vê a lista completa com os resumos. Nenhum outro arquivo da pasta foi alterado — confira comparando a
contagem com a pasta original.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Ele não leu os PDFs | Nem todo formato é lido diretamente. Converta os que importam para texto, ou trabalhe com os que ele lê. |
| O resumo está errado | Ele erra. Por isso o passo 7 existe. Corrija à mão. |
| Ele não criou o arquivo | Você está em modo somente leitura, que impede escrita. É o comportamento esperado. Autorize a criação especificamente. |
| Ele quis mexer em outros arquivos | Recuse. Reforce no pedido: "crie apenas o `indice.md` e não altere nenhum arquivo existente". |

> 📌 **Não esqueça:** este é o primeiro momento do curso em que você autoriza uma escrita. Autorize a
> criação de **um** arquivo, e nada além disso.

### 🚀 Quer ir além?

1. **Índice por tema.** Peça um índice organizado por assunto, e não por nome de arquivo.
   *Deu certo se:* a agrupação faz sentido para você e revelou uma categoria que você não tinha
   percebido.
2. **O que está faltando.** Pergunte: "que assuntos um curso desta área trataria e que não aparecem
   em nenhum arquivo desta pasta?". *Deu certo se:* pelo menos uma lacuna apontada era real.
3. **Linha do tempo.** Peça a lista dos arquivos ordenada por data de criação, com o resumo.
   *Deu certo se:* você consegue ver como o material evoluiu ao longo dos semestres.

---

# Oficina 4 — Um gráfico sem programar

## Descrição

- **Objetivos da Aula:** produzir uma imagem de gráfico a partir de um arquivo de dados; e apresentar
  o critério de decisão para autorizar acesso à internet.
- **Habilidades Esperadas:** ao final, você exporta dados de uma planilha, obtém um gráfico, confere
  os números, e sabe decidir quando autorizar acesso à rede e quando recusar.

### 🎯 O Problema

Você tem as médias da turma numa planilha e queria um gráfico para mostrar em aula. Não em cinco
cliques do Excel — um gráfico que você possa refazer todo semestre mudando só o arquivo de dados.
Nesta oficina você pede e recebe.

### 🧰 O que você vai usar

- Uma planilha sua, sem nome de aluno.
- A pasta `teste-codex`, que é onde esta oficina acontece.
- O VS Code com o Codex.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** o Visual Studio Code com a imagem do gráfico gerado aberta no editor, ao
  lado do arquivo de dados na barra lateral esquerda, e o painel do Codex mostrando o pedido de
  autorização de acesso à rede.

1. **Tire os nomes.** Antes de exportar, substitua nomes de aluno por identificadores — `A01`, `A02`.
   Vale a regra da Oficina 0: o que é sensível não entra na pasta.

2. **Exporte em CSV.** CSV é um formato de planilha simplificado, em texto puro, que qualquer
   programa lê. No seu editor de planilhas:
   `planilha > Arquivo > Salvar como > CSV (separado por vírgulas)`. Salve dentro da pasta
   `teste-codex`, com o nome `notas.csv`.

3. Abra a pasta `teste-codex` no editor.

4. Peça o gráfico:

   > A partir do arquivo `notas.csv`, faça um gráfico de barras das médias por turma e salve como
   > imagem PNG nesta pasta. Antes de executar, diga o que você vai fazer e o que precisa instalar.

5. **Decida sobre a rede.** Provavelmente ele vai dizer que precisa de acesso à internet para
   instalar uma biblioteca de gráficos. Por padrão o acesso à rede vem desligado, e é você quem
   decide. O critério deste curso é simples:

   | Situação | Autorizar? |
   |---|---|
   | Pasta de teste, sem dado sensível, para instalar biblioteca de gráfico | Sim |
   | Pasta com material real ou dado de pesquisa | Não. Mova os dados para a pasta de teste primeiro |
   | Você não entendeu o que ele quer instalar ou por quê | Não. Peça para explicar antes |

6. Autorize (ou não) e aguarde.

7. Abra a imagem gerada, clicando nela na barra lateral esquerda.

8. **Confira os números** do gráfico contra a planilha original. Um por um.

### ✅ Deu certo?

🏁 **Ponto de controle:** existe um arquivo de imagem na pasta `teste-codex`, ele abre no editor
mostrando um gráfico de barras, e cada valor do gráfico bate com a planilha.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Ele disse que precisa instalar coisas | Esperado. Aplique o critério do passo 5. |
| Os números não batem | Confira o separador decimal do CSV. Em português é comum ser vírgula, e o esperado ser ponto. Diga isso a ele: "os decimais usam vírgula". |
| O gráfico está ilegível | Peça ajustes concretos: "aumente a fonte dos rótulos", "coloque os valores em cima de cada barra", "use tons de cinza". |
| A tarefa está demorando muito | Tarefa longa consome muito mais da sua cota que um pedido curto. Interrompa e peça algo mais simples. |
| Ele não achou o arquivo | Confira se o `notas.csv` está dentro da pasta que você abriu no editor. |

> ⚠️ **Cuidado:** esta é a única oficina do curso em que o assistente executa código e pede acesso à
> internet. Por isso ela acontece na pasta de teste, e por isso os nomes saem no passo 1.

### 🚀 Quer ir além?

1. **Três gráficos.** Peça três formas diferentes de visualizar os mesmos dados e escolha.
   *Deu certo se:* você consegue dizer o que cada forma esconde.
2. **O gráfico que se repete.** Peça para ele deixar salvo o procedimento, de modo que no semestre
   que vem baste trocar o `notas.csv`. *Deu certo se:* você consegue refazer trocando só o arquivo.
3. **A pergunta aos dados.** Pergunte: "o que estes dados mostram que não é óbvio?". *Deu certo se:*
   você conferiu a afirmação contra a planilha — e ela se sustenta, ou você descobriu que não.

---

# Projeto Final — Uma disciplina que se organiza sozinha no semestre que vem

## Descrição

- **Objetivos da Aula:** exigir a produção de um pacote completo — pasta organizada, indexada e com
  um arquivo de instruções que faz o padrão se repetir sem ser redigitado.
- **Habilidades Esperadas:** ao final, você entrega uma pasta de disciplina padronizada e indexada, e
  um arquivo de instruções que o agente passa a seguir sozinho nos próximos semestres.

### 🎯 A missão

Não é organizar uma pasta. É deixar a pasta organizada **e escrever a regra** para que ela se
organize do mesmo jeito no semestre que vem, sem você repetir nada.

Essa última parte é a que nenhuma oficina cobriu. O Codex admite que você escreva, uma única vez, as
regras que ele deve seguir naquela pasta — em português, num arquivo de texto que fica lá dentro. A
partir daí ele as consulta sozinho, em todo pedido.

### 🧰 O que você vai usar

- A pasta de uma disciplina sua, em cópia.
- O VS Code com o Codex.
- Tudo o que você fez nas Oficinas 2, 3 e 4.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** o Visual Studio Code com a pasta final aberta — subpastas numeradas,
  arquivos com nomes padronizados, o `indice.md` e o arquivo de instruções visíveis na barra lateral
  — e o arquivo de instruções aberto no editor, mostrando texto em português.

1. **Confirme a cópia.** Nome da pasta com sufixo, original fechado. E tire da pasta o que não pode
   estar lá (Oficina 0, passo 4).

2. **Peça o diagnóstico:**

   > Descreva o que tem nesta pasta: quantos arquivos, de que tipos, com que padrões de nome. Aponte
   > o que está inconsistente. Não altere nada.

3. **Padronize os nomes** (Oficina 2), com lista prévia e as três verificações antes de aprovar.

4. **Organize em subpastas**, também com lista prévia.

5. **Monte o índice** (Oficina 3), autorizando apenas a criação do `indice.md`.

6. **Escreva o arquivo de instruções.** Crie, na raiz da pasta, um arquivo de texto que responda a
   quatro perguntas, em português:

   - O que há nesta pasta?
   - Como os arquivos devem ser nomeados?
   - Como devem ser organizados?
   - **O que nunca deve ser feito aqui?**

   A quarta é a mais importante e a que ninguém escreve. Um arquivo que só diz o que fazer deixa o
   resto em aberto; um que diz o que **não** fazer estabelece um limite para todos os pedidos
   futuros.

7. **Teste a regra.** Faça um pedido que **não** repita nenhuma das regras que você escreveu — por
   exemplo, "acrescente estes três arquivos novos à pasta, seguindo a organização existente; mostre a
   lista antes". Veja se ele obedece o padrão sozinho.

8. **Confira tudo** contra a pasta original: contagem de arquivos, nada perdido, nada alterado por
   dentro.

9. **Anote** as três instruções que funcionaram melhor.

### 🏁 Como saber que terminou

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

---

# A Parte dos Dez — Coisas que Funcionam no Codex

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

Você organizou uma pasta de verdade, fez o computador responder perguntas sobre o seu próprio
material, gerou um gráfico a partir dos seus dados, e — o mais importante — deixou escrita a regra
para que isso se repita sozinho. Nada disso exigiu uma linha de código.

O próximo passo é repetir em outra pasta. Escolha a disciplina seguinte e faça o ciclo inteiro. E
quando a cópia manual começar a incomodar, o assunto a estudar chama-se **versionamento**: é o jeito
sistemático de desfazer alterações, e é a evolução natural do que você acabou de aprender.
