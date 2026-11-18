# Plano de Aula — ChatGPT (Codex) no VS Code (Essentials)

> *» IA: bloco Cover. Título e subtítulo do curso. Não traduzir "Codex" nem "VS Code".*

*Trabalho com pastas de arquivos para quem não programa*

## Identificação

> *» IA: bloco Table. Preservar a tabela verbatim.*

| Campo | Definição |
|---|---|
| Curso | ChatGPT (Codex) no VS Code (Essentials) |
| Natureza | Curto, introdutório e autoinstrucional |
| Carga horária | 125 minutos |
| Público-alvo | Professores universitários, de qualquer área, que não programam e não pretendem programar |
| Pré-requisitos | Saber criar pastas e mover arquivos; conta ativa no ChatGPT, ainda que gratuita; permissão para instalar programas; nenhum conhecimento de programação |
| Recursos necessários | Computador com Windows, macOS ou Linux, com permissão de instalação; Visual Studio Code; extensão Codex; internet ativa; conta ChatGPT; uma pasta de trabalho real |

### Objetivo Geral

> *» IA: bloco Text.*

O curso destina-se a habilitar o docente do ensino superior, ainda que sem qualquer conhecimento de
programação, a empregar o Codex no Visual Studio Code como assistente para o trabalho com pastas de
arquivos — organizar material, consultar conjuntos de documentos, converter formatos e produzir
análises simples —, compreendendo o modelo de permissões que governa o que o agente pode fazer e
mantendo controle sobre os próprios arquivos em todas as etapas.

### Competências a Desenvolver

> *» IA: bloco List. Verbatim, sem acréscimos.*

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Distinguir um sistema que responde de um agente que executa, e estabelecer os limites do agente
   antes do primeiro uso.
2. Reconhecer, na própria rotina, quais tarefas cabem no agente e quais não cabem.
3. Instalar o editor e a extensão, e configurar o nível de aprovação adequado a quem aprende.
4. Formular um pedido com padrão, restrição de preservação e exigência de proposta prévia, e revisar
   a proposta antes de aprovar.
5. Registrar em arquivo de instruções as regras permanentes de uma pasta.

### Estrutura e Sequência dos Módulos

> *» IA: bloco Text seguido de bloco Table. Preservar a tabela verbatim.*

Os módulos observam progressão cumulativa. O Módulo 0 estabelece os limites antes de qualquer
contato; o Módulo 1 responde por que isto interessa a quem não programa; o Módulo 2 dá acesso à
ferramenta; o Módulo 3 apresenta o ciclo de trabalho; o Módulo 4 trata do padrão que se repete; o
Módulo 5 integra as competências. Nenhum módulo deve ser iniciado antes da conclusão do anterior.

| Módulo | Título | Referência | Tempo |
|---|---|---|---|
| 0 | Antes de deixar um agente perto dos seus arquivos | Central de Ajuda da OpenAI — controles de dados e aprovações | 22 min |
| 1 | O que o Codex faz com uma pasta sua | Central de Ajuda da OpenAI — o que é o Codex | 18 min |
| 2 | Instalar o editor e a extensão | Central de Ajuda da OpenAI — primeiros passos | 21 min |
| 3 | Pedir, revisar, aprovar | Central de Ajuda da OpenAI; anúncio do GPT-5-Codex | 22 min |
| 4 | Ensinar ao Codex as regras da sua pasta | Central de Ajuda da OpenAI — instruções de projeto | 22 min |
| 5 | Síntese e Aplicação Integrada | — | 20 min |

---

# Módulo 0 — Antes de deixar um agente perto dos seus arquivos

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 0" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja tabelas de decisão no meio. ▼▼▼*

> Ponto de partida do curso. Nenhum módulo posterior deve ser iniciado sem que as decisões deste
> módulo estejam tomadas.

### Objetivos de Aprendizagem

> *» IA: bloco List. Verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Distinguir um sistema de conversa de um agente que executa ações sobre arquivos.
2. Descrever os três níveis de aprovação e justificar a adoção do modo somente leitura.
3. Enunciar a regra operacional de dados: o que é sensível não fica na pasta de trabalho.
4. Concluir a preparação: cópia de segurança, pasta de teste e identificação do plano.

### Texto Descritivo

> *» IA: bloco Text. Pode ser dividido em blocos menores; não resumir.*

Convém iniciar pela distinção que governa todo o curso. Um sistema de conversa responde com texto:
recebe uma pergunta e devolve palavras na tela. Um agente executa ações: lê o conteúdo de uma pasta,
cria arquivos, renomeia, apaga, e executa comandos no computador do participante. A diferença não é
de grau, mas de natureza, e a consequência prática é a seguinte: um texto equivocado se descarta; uma
alteração equivocada em arquivo precisa ser desfeita. Esta formulação será retomada nominalmente no
Módulo 3, ao tratar de revisão, e no Módulo 5, ao tratar da responsabilidade sobre o resultado.

Descomplique-se, desde já, o vocabulário que aparecerá adiante. Denomina-se extensão um acessório que
se acrescenta a um programa para lhe dar uma função nova, como um suplemento acrescenta funções ao
Word. Denomina-se pasta de trabalho, ou espaço de trabalho, a pasta que está aberta no editor: é o
território do agente, e o que estiver fora dela, ele não vê. Denomina-se terminal uma janela em que
se digitam comandos em vez de clicar em botões; o curso a utiliza uma única vez, no Módulo 2, e
explica o que fazer.

O que impede o agente de alterar o que não deve é o nível de aprovação. São três, e a escolha entre
eles é a decisão de segurança mais importante do curso. Cumpre registrar, adicionalmente, que por
padrão o Codex é executado em uma caixa fechada — um ambiente isolado do qual o programa não sai — e
com o acesso à internet desabilitado, tanto no computador do participante quanto na nuvem. A
finalidade declarada é impedir ações danosas e reduzir o risco de que instruções maliciosas
escondidas em arquivos de origem desconhecida sejam obedecidas.

Quanto aos dados, o tratamento do conteúdo processado pelo Codex segue os controles de dados do
ChatGPT. Nos planos Business, Enterprise e Edu, entradas e saídas não são usadas para melhorar os
modelos por padrão; nos planos Pro e Plus, as conversas podem ser usadas, salvo desativação pelo
participante. Distingue-se, ainda, onde o trabalho ocorre: fluxos locais são executados no
dispositivo do participante; tarefas delegadas à nuvem, em ambientes gerenciados pela OpenAI.

Cumpre observar uma diferença relevante em relação ao uso do ChatGPT em uma conversa comum. Naquele
caso, o participante escolhe o que colar. Aqui, o agente lê a pasta inteira. Decorre daí a regra
operacional do curso: o que for sensível não fica fora do alcance porque não foi selecionado — fica
fora do alcance porque não está na pasta de trabalho.

Registre-se que o Codex está incluído nos planos do ChatGPT, inclusive Free e Go, mas que a cota é
compartilhada com outros recursos da conta — entre eles o ChatGPT Work, o ChatGPT para Excel e os
agentes do espaço de trabalho. Uma tarefa de longa duração pode consumir muito mais do que uma
solicitação curta.

Antes do uso em material institucional, três perguntas requerem resposta, e elas não são respondidas
por este curso, porque a resposta é institucional e varia: o que a norma da própria instituição
estabelece sobre o uso de inteligência artificial no tratamento de material didático e de dados de
pesquisa; se o uso precisa ser declarado, observando que uma análise de dados apoiada por agente pode
ter exigência distinta da simples organização de arquivos; e que orientação será dada aos alunos, que
dispõem da mesma ferramenta.

> *» IA: bloco Table. Preservar a tabela verbatim. É tabela de decisão: não converter em lista.*

| Nível de aprovação | O que o agente pode fazer | Para quem |
|---|---|---|
| Somente leitura, com aprovações explícitas | Lê os arquivos e propõe; não altera nada sem autorização item a item | Quem está aprendendo. É o padrão adotado neste curso |
| Automático | Age livremente dentro da pasta aberta; pede aprovação para qualquer coisa fora dela | Quem já conhece o comportamento do agente e trabalha em pasta de cópia |
| Acesso total | Lê arquivos em qualquer lugar do computador e executa comandos com acesso à internet | Situações específicas, com decisão consciente a cada vez |

> *» IA: bloco Statement. Preservar o emoji.*

> ⚠️ Enquanto o participante não tiver observado o comportamento do agente em pelo menos duas tarefas
> completas, convém permanecer no modo somente leitura. Aprender qual é o resultado provável custa
> duas tarefas; recuperar uma pasta perdida custa muito mais.

> *» IA: bloco List. Verbatim, sem acréscimos.*

**Não devem constar da pasta submetida ao agente:**

- Arquivo com dado identificável de aluno — nome associado a nota, frequência, ocorrência disciplinar
  ou condição de saúde.
- Resultado de pesquisa ainda não publicado.
- Parecer sigiloso de avaliação por pares.
- Conteúdo submetido a acordo de confidencialidade.
- Dado pessoal de terceiros obtido em contexto de pesquisa.

### Exercício Prático

> *» IA: bloco Process. Preservar os breadcrumbs e não traduzir termos de interface.*

**Verificação de prontidão (7 min)**

1. Criar a cópia de segurança: localizar a pasta que será usada nos exercícios em
   `Explorador de Arquivos > pasta de trabalho`, copiá-la inteira e renomear a cópia acrescentando o
   sufixo `-copia-curso`. Todo o curso ocorre na cópia; a original permanece fechada.
2. Criar a pasta de teste: uma pasta nova, chamada `teste-codex`, contendo três ou quatro arquivos de
   texto de exemplo, sem valor, com nomes deliberadamente desorganizados.
3. Identificar o plano em uso: `ChatGPT > Menu de perfil > Configurações > Conta`.
4. Nos planos Plus e Pro, decidir sobre o uso do conteúdo:
   `ChatGPT > Configurações > Controles de dados`.

> *» IA: bloco Statement. Preservar o emoji e o breadcrumb.*

> 🏁 **Ponto de controle:** em `Explorador de Arquivos > pasta de trabalho` existem a pasta original,
> a cópia com sufixo `-copia-curso` e a pasta `teste-codex` com arquivos dentro. E o participante
> consegue afirmar qual é o seu plano.

> *» IA: bloco Statement.*

> **Critério de êxito:** os três itens do ponto de controle foram confirmados, e o participante
> consegue enunciar, sem consultar o material, qual nível de aprovação adotará e por quê.

### Mão na massa

> *» IA: bloco Statement ou Download. Conteúdo do modelo verbatim, em aspas triplas. Não traduzir.*

Modelo de decisão para preencher antes de prosseguir. Substituir o conteúdo entre colchetes e manter
à mão durante todo o curso.

"""
Pasta de trabalho deste curso: [nome da pasta com sufixo -copia-curso]
Pasta original (permanece fechada): [nome da pasta original]
Pasta de teste: teste-codex

Meu plano do ChatGPT: [Free / Go / Plus / Pro / Business / Enterprise / Edu]
Meu conteúdo é usado para treinar os modelos? [sim, salvo desativação / não, por padrão]

Nível de aprovação que vou usar: somente leitura, até a Oficina 2 / Módulo 3.

Arquivos que TIREI da pasta de trabalho por serem sensíveis:
1. [arquivo] — motivo: [qual das cinco categorias]
2. [arquivo] — motivo: [qual das cinco categorias]
"""

### Solução de Problemas — Preparação

> *» IA: bloco Accordion, um item por linha da tabela. Preservar os breadcrumbs.*

| Situação | Procedimento |
|---|---|
| A pasta é grande demais para copiar | Copiar apenas a subpasta que será usada nos exercícios. O curso não exige a pasta inteira. |
| Não sei qual é o meu plano | Podem existir duas contas — a institucional e a pessoal. Conferir com qual endereço se está conectado. |
| Os controles de dados não estão disponíveis | Ocorre em contas administradas institucionalmente, em que a configuração é central. Não é falha. |
| Não sei o que colocar na pasta de teste | Três arquivos de texto quaisquer, com nomes deliberadamente desorganizados. Servem justamente para isso. |

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 0" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 1 — O que o Codex faz com uma pasta sua

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> Pressupõe as decisões do Módulo 0 e desloca o foco do controle para o motivo: para que isto serve a
> quem não programa.

### Objetivos de Aprendizagem

> *» IA: bloco List. Verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Identificar, entre as próprias pastas, tarefas que caberiam no agente.
2. Enunciar as três condições que uma tarefa precisa satisfazer para caber no agente.
3. Reconhecer as três razões pelas quais uma tarefa não deve ser entregue ao agente.

### Texto Descritivo

> *» IA: bloco Text. Pode ser dividido em blocos menores; não resumir.*

O Codex é descrito pela OpenAI como um agente que auxilia a escrever, revisar e entregar código. Essa
descrição é correta e é incompleta para o presente público. O que ela não diz é o seguinte: o agente
opera sobre uma pasta de arquivos a partir de instruções em português. Pastas de arquivos é o que um
docente tem aos milhares, e nenhuma delas precisa conter código.

Observa-se, nos quatro casos apresentados na tabela abaixo, o que eles têm em comum: nenhum exige que
o participante escreva uma única linha de código, e todos exigem que ele descreva com precisão o que
pretende.

Convém, em seguida, delimitar. A ferramenta atua bem sobre tarefas que satisfazem três condições:
incidem sobre arquivos que estão em uma pasta; podem ser descritas em uma instrução verificável; e
produzem um resultado que o participante consegue conferir. Fora dessas condições, o retorno cai ou o
risco sobe.

Três situações ilustram o que não convém entregar ao agente. A primeira é o julgamento sobre o
conteúdo: avaliar a qualidade de um trabalho, atribuir nota, decidir se um argumento se sustenta. O
agente produz uma opinião plausível, e plausível não é o mesmo que fundamentado. A segunda é a tarefa
cujo resultado não se consegue conferir: se o participante não tem como verificar se a saída está
correta, não tem como usá-la com responsabilidade. A terceira é a tarefa sobre material que não
deveria estar na pasta — regra estabelecida no Módulo 0, anterior a qualquer consideração de
utilidade.

> *» IA: bloco Table, Tabs ou Two-Column. Preservar a tabela verbatim.*

| Situação | O que se pede | O que se obtém |
|---|---|---|
| Trinta arquivos de aula com nomes como `aula1.pdf`, `AULA 2 final.pdf`, `aula2-CORRIGIDA(1).pdf` | "Renomeie todos os arquivos no padrão `aula-NN-tema.pdf`, mostrando antes a lista do que vira o quê" | Uma lista para conferir e, aprovada, trinta arquivos padronizados |
| Uma pasta com dezenas de textos e a lembrança de ter escrito sobre um assunto em algum lugar | "Em quais arquivos desta pasta menciono [assunto]? Liste o arquivo e o trecho" | A localização exata, sem abrir arquivo por arquivo |
| Notas exportadas de uma planilha em arquivo de dados | "Faça um gráfico de barras das médias por turma a partir deste arquivo e salve como imagem" | Uma imagem de gráfico na pasta |
| Uma pasta acumulada ao longo de semestres, sem organização | "Crie um arquivo `indice.md` com a lista de todos os arquivos e um resumo de uma frase de cada um" | Um índice navegável do próprio material |

### Exercício Prático

> *» IA: bloco Process seguido de bloco Statement com o critério de êxito.*

**Identificação de tarefas próprias (4 min)**

Percorrer mentalmente as pastas do próprio computador e responder:

1. Qual das próprias pastas está mais desorganizada, e que padrão de nome conviria a ela?
2. Que pergunta ao próprio material já se quis fazer e não se fez, por dar muito trabalho procurar?
3. Que tarefa da própria rotina **não** caberia no agente, e por qual das três razões?

> *» IA: bloco Statement.*

> **Critério de êxito:** o participante nomeia uma pasta concreta com um padrão de nome desejado, uma
> pergunta concreta a fazer ao próprio material, e uma tarefa que reconhece como inadequada, com a
> razão.

### Mão na massa

> *» IA: bloco Statement ou Download. Conteúdo do modelo verbatim, em aspas triplas.*

Modelo de triagem, para decidir se uma tarefa cabe no agente antes de pedi-la.

"""
Tarefa que quero fazer: [descrever em uma frase]

Condição 1 — incide sobre arquivos que estão em uma pasta? [sim / não]
Condição 2 — consigo descrevê-la em uma instrução verificável? [sim / não]
Condição 3 — consigo conferir se o resultado está correto? [sim / não]

Se alguma resposta for "não", a tarefa não vai para o agente.
Se todas forem "sim": o padrão que quero é [descrever com precisão].
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 2 — Instalar o editor e a extensão

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> Pressupõe o Módulo 1 e desloca o foco do motivo para o acesso.

### Objetivos de Aprendizagem

> *» IA: bloco List. Verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Instalar o Visual Studio Code e a extensão Codex, conectando-a à conta.
2. Configurar o nível de aprovação em modo somente leitura.
3. Abrir uma pasta no editor e reconhecer que o agente vê apenas o que está dentro dela.
4. Executar o comando de diagnóstico quando o painel não responder.

### Texto Descritivo

> *» IA: bloco Text. Pode ser dividido em blocos menores; não resumir.*

O Visual Studio Code é um editor de texto gratuito, distribuído pela Microsoft, disponível para
Windows, macOS e Linux. Foi concebido para quem escreve software, mas sua função básica é mais
simples do que isso sugere: abre uma pasta e mostra os arquivos que ela contém. É o bastante para o
propósito deste curso, e o participante não precisará de nenhuma outra função do editor.

O Codex pode ser acessado por mais de um caminho — há uma versão para a web, uma para linha de
comando e uma dentro do aplicativo do ChatGPT para desktop. Este curso trata exclusivamente da
extensão para o Visual Studio Code, por ser a que apresenta os arquivos e as alterações propostas de
forma visual, o que é decisivo para quem está aprendendo a revisar o trabalho de um agente.

> *» IA: bloco Process. Preservar os breadcrumbs e não traduzir termos de interface.*

Procedimento de instalação:

1. Baixar o Visual Studio Code no sítio oficial e instalar.
2. Abrir o editor.
3. `Visual Studio Code > barra lateral > Extensões`.
4. Pesquisar por `Codex` e instalar a extensão correspondente.
5. Abrir o painel do Codex e entrar com a conta do ChatGPT.
6. Configurar o modo de aprovação para somente leitura, conforme decidido no Módulo 0.
7. `Visual Studio Code > Arquivo > Abrir Pasta > teste-codex`.

> *» IA: bloco Statement. Preservar o emoji.*

> ⚠️ Caso a organização gerencie as atualizações dos aplicativos, o administrador precisa implantar a
> versão aprovada antes que os recursos que a exigem possam ser utilizados. Em ambiente institucional
> com instalação bloqueada, o curso não pode ser executado.

### Exercício Prático

> *» IA: bloco Process. Preservar os breadcrumbs.*

**Instalação e primeiro reconhecimento (7 min)**

1. Executar os sete passos do procedimento acima.
2. Confirmar que a pasta `teste-codex` está aberta e que seus arquivos aparecem na barra lateral.
3. Confirmar que o painel do Codex está visível e conectado.

> *» IA: bloco Statement. Preservar o emoji e o breadcrumb.*

> 🏁 **Ponto de controle:** os arquivos de exemplo da pasta `teste-codex` aparecem em
> `Visual Studio Code > barra lateral > Explorador`, e o painel do Codex mostra a conta conectada.
> Nenhuma pasta de material real foi aberta.

> *» IA: bloco Statement.*

> **Critério de êxito:** os dois itens do ponto de controle foram confirmados, na pasta de teste e
> não em material real.

### Mão na massa

> *» IA: bloco Statement ou Download. Conteúdo do modelo verbatim, em aspas triplas.*

Prompt-base de reconhecimento, para executar na pasta de teste antes de qualquer trabalho real.

"""
Descreva o que tem nesta pasta: quantos arquivos, quais os nomes e o que cada um contém, em uma
frase. Não altere nada.
Depois, responda: que tipos de alteração você conseguiria fazer aqui, e quais não conseguiria?
"""

### Solução de Problemas — Instalação

> *» IA: bloco Accordion, um item por linha da tabela. Preservar os breadcrumbs e não traduzir o comando.*

| Situação | Procedimento |
|---|---|
| Não consigo instalar programas | A instituição pode bloquear instalações. O curso não pode ser executado sem o editor; consultar quem administra os equipamentos. |
| Não encontrei a extensão | Conferir a grafia da pesquisa e o editor responsável pela extensão. O nome exato deve ser confirmado na loja de extensões vigente. |
| A extensão instala mas não aceita a conta | Verificar se o acesso está sendo feito com a conta ChatGPT correta. É comum haver uma pessoal e uma institucional. |
| O painel abre e não responde | Executar o diagnóstico. Terminal é a janela em que se digitam comandos em vez de clicar em botões. Abrir em `Visual Studio Code > Terminal > Novo Terminal`, digitar `codex doctor` e pressionar Enter. O comando verifica problemas de inicialização, conectividade e desempenho, e informa o que encontrou. |
| Não sei onde ficam os arquivos abertos | O editor mostra, em `Visual Studio Code > barra lateral > Explorador`, apenas o conteúdo da pasta aberta. O que está fora dela não aparece — e o agente também não o vê. |

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 3 — Pedir, revisar, aprovar

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja modelos de texto no meio. ▼▼▼*

> Pressupõe a ferramenta instalada no Módulo 2 e desloca o foco do acesso para o ciclo de trabalho
> propriamente dito.

### Objetivos de Aprendizagem

> *» IA: bloco List. Verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Descrever o ciclo de três tempos: pedido, proposta e aprovação.
2. Formular um pedido contendo padrão, restrição de preservação e exigência de proposta prévia.
3. Aplicar as três verificações de revisão antes de aprovar.

### Texto Descritivo

> *» IA: bloco Text. Pode ser dividido em blocos menores; não resumir.*

O trabalho com o agente observa três tempos, sempre na mesma ordem: o participante descreve em
português o que pretende; o agente apresenta o que faria, item a item, sem alterar nada; o
participante confere a proposta e aprova, corrige ou recusa.

O segundo tempo é o que distingue um agente bem operado de um agente perigoso, e ele não acontece
sozinho: é preciso pedi-lo. A formulação que o produz é sempre da mesma família — "antes de executar,
mostre a lista do que você vai fazer". Sem ela, o agente que estiver em modo automático executa, e o
participante descobre o resultado depois.

Retoma-se aqui o conceito plantado no Módulo 0: um texto equivocado se descarta; uma alteração
equivocada em arquivo precisa ser desfeita. O segundo tempo do ciclo existe para que a alteração
equivocada não chegue a ocorrer.

Cumpre registrar o que torna um pedido eficaz. Três elementos bastam: o padrão pretendido, dito com
precisão — `aula-NN-tema.pdf` é operacional, "organize isso" não é; a restrição de preservação,
declarando o que não deve mudar, como o conteúdo dos arquivos ou os originais; e a exigência de
proposta prévia, que produz o segundo tempo.

Observa-se, por fim, que o agente aproveita o contexto do editor: quando um arquivo está aberto ou um
trecho está selecionado, o pedido pode ser mais curto, porque o sistema já sabe a que se refere.

A revisão, por sua vez, não é uma leitura rápida da proposta. Três verificações a compõem, e a
segunda é a que costuma ser omitida.

> *» IA: bloco Table ou Process. Preservar a tabela verbatim.*

| Tempo | Quem age | O que acontece |
|---|---|---|
| 1. Pedido | O participante | Descreve em português o que pretende, com o padrão desejado |
| 2. Proposta | O agente | Apresenta o que faria, item a item, sem alterar nada |
| 3. Aprovação | O participante | Confere a proposta e aprova, corrige ou recusa |

> *» IA: bloco List ou Checklist. Verbatim, um item por linha.*

**As três verificações da revisão:**

1. **A lista está completa?** O número de itens propostos corresponde ao número de arquivos que o
   participante espera ver alterados.
2. **Cada item está correto?** Amostrar: conferir cinco itens escolhidos, não apenas o primeiro.
3. **Há algo que não deveria estar ali?** Um arquivo que o participante não esperava que fosse tocado
   é sinal de que o pedido foi mais amplo do que se pretendia.

### Exercício Prático

> *» IA: bloco Process. Preservar o texto do prompt verbatim e os breadcrumbs.*

**Primeiro ciclo completo, na pasta de teste (6 min)**

1. Com a pasta `teste-codex` aberta, formular o pedido com os três elementos:
   *"Renomeie os arquivos desta pasta no padrão `documento-NN-assunto.txt`. Preserve o conteúdo de
   cada arquivo. Antes de executar, mostre a lista do que vai virar o quê."*
2. Ler a lista proposta.
3. Aplicar as três verificações de revisão.
4. Aprovar, corrigir ou recusar.
5. Conferir a pasta em `Visual Studio Code > barra lateral > Explorador`.

> *» IA: bloco Statement. Preservar o emoji e o breadcrumb.*

> 🏁 **Ponto de controle:** os arquivos da pasta `teste-codex` aparecem, em
> `Visual Studio Code > barra lateral > Explorador`, com os nomes do padrão pedido. Nenhum arquivo
> desapareceu, e a contagem é a mesma de antes.

> *» IA: bloco Statement.*

> **Critério de êxito:** o pedido continha os três elementos, a proposta foi conferida por amostragem
> antes da aprovação, e a contagem de arquivos permaneceu a mesma.

### Mão na massa

> *» IA: bloco Statement ou Download. Conteúdo do modelo verbatim, em aspas triplas.*

Modelo de pedido em três elementos. Preencher os campos entre colchetes antes de usar.

"""
[O QUE FAZER: renomeie / organize / liste / crie] os arquivos desta pasta.
Padrão: [dizer com precisão — ex.: aula-NN-tema.pdf, com NN de dois dígitos e tema em minúsculas sem
acento].
Preserve: [o que não pode mudar — ex.: o conteúdo de cada arquivo, as datas de modificação, a
subpasta "originais"].
Antes de executar, mostre a lista do que vai virar o quê. Não altere nada até eu aprovar.
"""

### Solução de Problemas — Execução

> *» IA: bloco Accordion, um item por linha da tabela.*

| Situação | Procedimento |
|---|---|
| O agente executou sem mostrar a lista | O modo de aprovação não está em somente leitura, ou o pedido não exigiu a proposta prévia. Corrigir os dois. |
| A proposta contém arquivos que não deveriam ser tocados | Recusar e refazer o pedido delimitando: "apenas os arquivos com extensão X", ou "apenas os arquivos da subpasta Y". |
| O agente pediu permissão para algo que não foi compreendido | Recusar. A regra é simples e não tem exceção: não se autoriza o que não se entendeu. |
| Um arquivo desapareceu | Recuperar a partir da cópia de segurança criada no Módulo 0. É a situação para a qual ela existe. |
| O agente não encontrou os arquivos | Conferir qual pasta está aberta. O agente vê apenas o conteúdo da pasta de trabalho. |

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 4 — Ensinar ao Codex as regras da sua pasta

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> Pressupõe o Módulo 3 e desloca o foco da tarefa isolada para o padrão que se repete a cada
> semestre.

### Objetivos de Aprendizagem

> *» IA: bloco List. Verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Explicar o que é um arquivo de instruções de projeto e o que ele economiza.
2. Aplicar o critério de repetição para decidir se compensa criá-lo.
3. Redigir um arquivo de instruções que responda às quatro perguntas, inclusive a da restrição.

### Texto Descritivo

> *» IA: bloco Text. Pode ser dividido em blocos menores; não resumir.*

O docente que organiza material de aula tem, quase sempre, um padrão próprio: nomes em determinado
formato, subpastas por unidade, um índice atualizado ao fim do semestre. Repetir esse padrão ao agente
a cada pedido é trabalho, e trabalho que se esquece de fazer.

O Codex admite que essas regras sejam escritas uma única vez, em um arquivo de instruções do projeto,
guardado na própria pasta. A partir daí, o agente as consulta em todo pedido feito naquela pasta. O
arquivo é criado por um comando de inicialização, que gera uma estrutura inicial para a pasta atual, e
o participante o edita como editaria qualquer texto — em português, sem sintaxe especial.

O critério de decisão é o mesmo de qualquer automação: se o padrão se repete a cada semestre, vale
escrevê-lo; se a tarefa é única, não vale.

Convém que o arquivo responda a quatro perguntas, em prosa simples. A quarta é a mais importante e a
menos óbvia: um arquivo de instruções que só diz o que fazer deixa o resto em aberto; um que declara o
que não fazer estabelece um limite que vale para todos os pedidos futuros.

> *» IA: bloco Table. Preservar a tabela verbatim.*

| Pergunta | Exemplo de resposta |
|---|---|
| O que há nesta pasta? | Material da disciplina de Metodologia da Pesquisa, semestres de 2024 e 2025 |
| Como os arquivos devem ser nomeados? | `aula-NN-tema.pdf`, com NN de dois dígitos e tema em minúsculas, sem acento |
| Como devem ser organizados? | Uma subpasta por unidade, numeradas de `01-` a `04-` |
| O que nunca deve ser feito aqui? | Não alterar o conteúdo dos arquivos; não apagar nada; não mexer na subpasta `originais` |

> *» IA: bloco Statement. Preservar o emoji.*

> ⚠️ O comando de inicialização é documentado para o Codex no aplicativo de desktop e na linha de
> comando. Sua disponibilidade a partir da extensão do Visual Studio Code deve ser confirmada na
> versão vigente. Não estando disponível, o mesmo efeito se obtém criando o arquivo à mão, na raiz da
> pasta, e mencionando-o no pedido.

### Exercício Prático

> *» IA: bloco Process. Preservar os breadcrumbs.*

**Criação do arquivo de instruções (6 min)**

1. Abrir a cópia de trabalho em `Visual Studio Code > Arquivo > Abrir Pasta`.
2. Criar, na raiz da pasta, um arquivo de instruções respondendo às quatro perguntas.
3. Formular um pedido que **não** repita nenhuma das regras escritas — por exemplo, "organize os
   arquivos desta pasta; antes de executar, mostre a lista".
4. Verificar, na proposta, se o padrão declarado no arquivo foi observado.

> *» IA: bloco Statement. Preservar o emoji.*

> 🏁 **Ponto de controle:** a proposta do agente segue o padrão de nome declarado no arquivo de
> instruções, embora o pedido não o tenha mencionado.

> *» IA: bloco Statement.*

> **Critério de êxito:** o arquivo de instruções existe na pasta, responde às quatro perguntas, e a
> proposta do agente reflete ao menos uma regra que não foi repetida no pedido.

### Mão na massa

> *» IA: bloco Statement ou Download. Conteúdo do modelo verbatim, em aspas triplas. Não traduzir os exemplos de padrão de nome.*

Modelo de arquivo de instruções. Salvar na raiz da pasta de trabalho, substituindo o conteúdo entre
colchetes.

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

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 5 — Síntese e Aplicação Integrada

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 5" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> Pressupõe todos os módulos anteriores e os articula em uma única atividade de produção.

### Objetivos de Aprendizagem

> *» IA: bloco List. Verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Encadear as seis etapas do fluxo de trabalho com o agente, do estabelecimento dos limites ao
   registro do padrão.
2. Situar a revisão como etapa insubstituível do fluxo.
3. Reconhecer que a decisão sobre o que aceitar permanece de quem revisa.

### Texto Descritivo

> *» IA: bloco Text. Pode ser dividido em blocos menores; não resumir.*

Cumpre articular o que foi tratado de modo disperso. O trabalho com o agente observa um fluxo de seis
etapas, e as duas primeiras acontecem antes de qualquer pedido.

Observa-se que a quarta etapa é insubstituível. Retoma-se, pela última vez, o conceito plantado no
Módulo 0: um texto equivocado se descarta; uma alteração equivocada em arquivo precisa ser desfeita. A
decisão sobre o que aceitar permanece integralmente com quem revisa, e nenhuma etapa do fluxo
transfere essa responsabilidade.

> *» IA: bloco Process ou Table. Preservar a tabela verbatim.*

| Etapa | O que se faz | Onde foi tratado |
|---|---|---|
| 1 | Estabelecer os limites: cópia de segurança, nível de aprovação, o que fica fora da pasta | Módulo 0 |
| 2 | Reconhecer se a tarefa cabe no agente | Módulo 1 |
| 3 | Formular o pedido com padrão, preservação e exigência de proposta prévia | Módulo 3 |
| 4 | Revisar a proposta pelas três verificações | Módulo 3 |
| 5 | Aprovar, corrigir ou recusar | Módulo 3 |
| 6 | Registrar o padrão no arquivo de instruções, quando se repetir | Módulo 4 |

### Exercício Prático

> *» IA: bloco Process. Preservar os breadcrumbs.*

**Atividade Integradora — uma pasta própria (6 min de execução assistida; a tarefa pode ser concluída
depois)**

1. Confirmar que se está trabalhando na cópia, e não no original.
2. Escolher uma tarefa entre as identificadas no Módulo 1.
3. Formular o pedido com os três elementos.
4. Revisar a proposta pelas três verificações.
5. Aprovar, corrigir ou recusar.
6. Conferir o resultado em `Visual Studio Code > barra lateral > Explorador` e, havendo padrão a
   repetir, registrá-lo no arquivo de instruções.

> *» IA: bloco Checklist. Preservar a tabela verbatim, um item por linha.*

**Critérios de avaliação**

| Critério | Atendido? |
|---|---|
| O trabalho ocorreu na cópia, e a pasta original permanece intacta | |
| O nível de aprovação em uso é o adequado ao nível de familiaridade do participante | |
| Nenhum arquivo das categorias vedadas no Módulo 0 estava na pasta de trabalho | |
| O pedido continha padrão, restrição de preservação e exigência de proposta prévia | |
| A proposta foi revisada pelas três verificações antes da aprovação | |
| A contagem de arquivos após a execução corresponde à esperada | |
| A decisão sobre declaração de uso, tratada no Módulo 0, foi tomada | |

### Mão na massa

> *» IA: bloco Statement ou Download. Conteúdo do modelo verbatim, em aspas triplas.*

Prompt-base de fechamento, para o participante levar como ferramenta de trabalho — a triagem que
antecede todo pedido novo.

"""
Antes de eu pedir qualquer coisa, responda sobre esta pasta, sem alterar nada:
1. Quantos arquivos há aqui, de que tipos, e quais padrões de nome você identifica?
2. O que está inconsistente?
3. Se eu pedisse para padronizar, quais arquivos seriam ambíguos e por quê?
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 5" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Encerramento

> *» IA: bloco Text.*

O curso cumpriu a finalidade de habilitar o docente, sem qualquer conhecimento de programação, a
empregar o Codex no Visual Studio Code sobre pastas de arquivos próprias, mantendo em todas as etapas
o controle sobre o que o agente pode fazer. Recomenda-se prática regular sobre material real, uma vez
que a competência aqui tratada se consolida pelo uso; sugere-se permanecer no modo somente leitura
até que o comportamento do agente seja previsível, e migrar ao modo automático apenas em pastas de
cópia.

Apontam-se, como caminhos de aprofundamento, a ampliação do arquivo de instruções para as demais
pastas de trabalho, o estudo de sistemas de versionamento — que resolvem de forma sistemática o
problema de desfazer alterações que este curso resolve por cópia manual —, e a exploração dos demais
clientes do Codex, uma vez consolidada a operação pela extensão.

> *» IA: bloco Statement. Preservar verbatim.*

> **Síntese:** o agente executa; a decisão sobre o que aceitar permanece de quem revisa.
