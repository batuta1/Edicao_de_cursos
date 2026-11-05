# Roteiro Final — ChatGPT (Codex) no VS Code (Essentials)

**Público-Alvo:** professores universitários, de qualquer área, que não programam e não pretendem
programar.

**Objetivo Geral:** habilitar o docente do ensino superior, ainda que sem qualquer conhecimento de
programação, a empregar o Codex no Visual Studio Code como assistente para o trabalho com pastas de
arquivos — organizar material, consultar conjuntos de documentos, converter formatos e produzir
análises simples —, compreendendo o modelo de permissões que governa o que o agente pode fazer e
mantendo controle sobre os próprios arquivos em todas as etapas.

**Pré-requisitos:** saber criar pastas, mover arquivos e localizar uma pasta no próprio computador;
conta ativa no ChatGPT, ainda que gratuita; permissão para instalar programas; **nenhum conhecimento
de programação**.

**Carga horária:** 125 minutos (detalhamento em `../carga-horaria/carga-horaria-essentials.md`).

---

## Estrutura do Curso

| Nível | Módulos | Finalidade |
|---|---|---|
| Nível 0 — Controle | Módulo 0 | Entender o que um agente pode fazer e estabelecer os limites antes de qualquer uso |
| Nível 1 — Motivo | Módulo 1 | Reconhecer, em casos concretos, para que isto serve a um docente |
| Nível 2 — Acesso | Módulo 2 | Instalar o editor e a extensão |
| Nível 3 — Uso | Módulo 3 | Pedir, revisar e aprovar uma tarefa |
| Nível 4 — Escala | Módulo 4 | Ensinar ao agente as regras que se repetem |
| Nível 5 — Integração | Módulo 5 | Articular as competências em atividade única |

**Anexos:** não há anexos. Os assuntos deslocados constam do Roadmap de Expansão em
`../_processo/02-analise-essentials.md`.

> **Fio condutor do curso.** O conceito plantado no Módulo 0 — *um texto equivocado se descarta; uma
> alteração equivocada em arquivo precisa ser desfeita* — é retomado nominalmente no Módulo 3, ao
> tratar de revisão e aprovação, e no Módulo 5, ao tratar da responsabilidade sobre o resultado.

> **Nota sobre a auditoria.** Os doze gargalos da matriz de soluções de
> `../_processo/02-analise-essentials.md` foram endereçados. Três decisões declaradas:
> (a) o Módulo 4 original, sobre permissões, deixou de existir — seu conteúdo subiu integralmente
> para o Módulo 0, porque a auditoria demonstrou que ele chegava tarde demais;
> (b) o parágrafo sobre distribuições do subsistema Windows para Linux foi removido, por ser
> irrelevante ao público e por sugerir um pré-requisito inexistente;
> (c) a menção aos quatro clientes do Codex foi reduzida a uma frase, no Módulo 2.

---

# Módulo 0 — Antes de deixar um agente perto dos seus arquivos

> Ponto de partida do curso. Nenhum módulo posterior deve ser iniciado sem que as decisões deste
> módulo estejam tomadas.

## Descrição

- **Objetivos da Aula:** distinguir um sistema de conversa de um agente que executa ações; apresentar
  os três níveis de aprovação e a caixa fechada em que o agente opera; expor o tratamento dado aos
  dados e os limites de uso; e conduzir a criação da cópia de segurança e da pasta de teste.
- **Habilidades Esperadas:** ao final, o participante sabe explicar o que um agente pode fazer com
  seus arquivos, sabe qual nível de aprovação adotar enquanto aprende, tem a cópia de segurança e a
  pasta de teste criadas, e sabe o que deve ficar fora da pasta de trabalho.

### O que muda quando o sistema executa em vez de responder

- **📸 Sugestão de Prints:** duas janelas lado a lado — à esquerda, uma conversa comum do ChatGPT no
  navegador; à direita, o Visual Studio Code com uma pasta aberta e o painel do Codex visível. O
  contraste entre "texto na tela" e "arquivos na pasta" é o que a captura precisa mostrar.

Convém iniciar pela distinção que governa todo o curso. Um sistema de conversa responde com texto:
recebe uma pergunta e devolve palavras na tela. Um **agente** executa ações: lê o conteúdo de uma
pasta, cria arquivos, renomeia, apaga, e executa comandos no computador do participante.

A diferença não é de grau, mas de natureza, e a consequência prática é a seguinte: **um texto
equivocado se descarta; uma alteração equivocada em arquivo precisa ser desfeita.** Esta formulação
será retomada nominalmente no Módulo 3, ao tratar de revisão, e no Módulo 5, ao tratar da
responsabilidade sobre o resultado.

Descomplique-se, desde já, o vocabulário que aparecerá adiante. Denomina-se **extensão** um acessório
que se acrescenta a um programa para lhe dar uma função nova — como um suplemento acrescenta funções
ao Word. Denomina-se **pasta de trabalho**, ou espaço de trabalho, a pasta que está aberta no editor:
é o território do agente, e o que estiver fora dela, ele não vê. Denomina-se **terminal** uma janela
em que se digitam comandos em vez de clicar em botões; o curso a utiliza uma única vez, no Módulo 2,
e explica o que fazer.

### Os três níveis de aprovação

- **📸 Sugestão de Prints:** painel de configurações do Codex mostrando a opção de modo de aprovação,
  com o modo somente leitura selecionado e os demais visíveis.

O que impede o agente de alterar o que não deve é o **nível de aprovação**. São três, e a escolha
entre eles é a decisão de segurança mais importante do curso.

| Nível | O que o agente pode fazer | Para quem |
|---|---|---|
| **Somente leitura, com aprovações explícitas** | Lê os arquivos e propõe; não altera nada sem autorização item a item | **Quem está aprendendo. É o padrão adotado neste curso.** |
| **Automático** | Age livremente dentro da pasta aberta; pede aprovação para qualquer coisa fora dela | Quem já conhece o comportamento do agente e trabalha em pasta de cópia |
| **Acesso total** | Lê arquivos em qualquer lugar do computador e executa comandos com acesso à internet | Situações específicas, com decisão consciente a cada vez |

Cumpre registrar, adicionalmente, que por padrão o Codex é executado em uma **caixa fechada** — um
ambiente isolado do qual o programa não sai — e **com o acesso à internet desabilitado**, tanto no
computador do participante quanto na nuvem. A finalidade declarada é impedir ações danosas e reduzir o
risco de que instruções maliciosas escondidas em arquivos de origem desconhecida sejam obedecidas.

> ⚠️ **Recomendação do curso.** Enquanto o participante não tiver observado o comportamento do agente
> em pelo menos duas tarefas completas, convém permanecer no modo somente leitura. Aprender qual é o
> resultado provável custa duas tarefas; recuperar uma pasta perdida custa muito mais.

### O que acontece com os seus dados

O tratamento do conteúdo processado pelo Codex segue os controles de dados do ChatGPT. Nos planos
Business, Enterprise e Edu, entradas e saídas não são usadas para melhorar os modelos por padrão. Nos
planos Pro e Plus, as conversas podem ser usadas, salvo desativação pelo participante nos controles
de dados da conta.

Distingue-se, ainda, onde o trabalho ocorre: fluxos locais são executados no dispositivo do
participante; tarefas delegadas à nuvem são executadas em ambientes gerenciados pela OpenAI.

Cumpre observar uma diferença relevante em relação ao uso do ChatGPT em uma conversa comum. Naquele
caso, o participante escolhe o que colar. Aqui, **o agente lê a pasta inteira**. Decorre daí a regra
operacional do curso: o que for sensível não fica fora do alcance porque não foi selecionado — fica
fora do alcance porque **não está na pasta de trabalho**. Não devem constar da pasta submetida ao
agente: arquivo com dado identificável de aluno; resultado de pesquisa ainda não publicado; parecer
sigiloso; conteúdo sob acordo de confidencialidade; e dado pessoal de terceiros obtido em pesquisa.

Quanto ao consumo, registre-se que o Codex está incluído nos planos do ChatGPT, inclusive Free e Go,
mas que a cota é **compartilhada** com outros recursos da conta — entre eles o ChatGPT Work, o
ChatGPT para Excel e os agentes do espaço de trabalho. Uma tarefa de longa duração pode consumir
muito mais do que uma solicitação curta. Recomenda-se verificar a situação de uso na própria conta
antes de iniciar um trabalho extenso.

### Autoria e uso declarado

Antes do uso em material institucional, três perguntas requerem resposta, e elas não são respondidas
por este curso, porque a resposta é institucional e varia:

1. O que a norma da própria instituição estabelece sobre o uso de sistemas de inteligência artificial
   no tratamento de material didático e de dados de pesquisa?
2. O uso precisa ser declarado? Uma análise de dados apoiada por agente pode ter exigência distinta
   da organização de arquivos.
3. Que orientação será dada aos alunos, que dispõem da mesma ferramenta?

### Preparação

- **📸 Sugestão de Prints:** janela do explorador de arquivos mostrando três itens lado a lado — a
  pasta original, a pasta com sufixo `-copia-curso`, e a pasta `teste-codex` com três arquivos de
  exemplo dentro.

Três passos antecedem o Módulo 1.

1. **Criar a cópia de segurança.** Localizar a pasta que será usada nos exercícios, copiá-la inteira
   e renomear a cópia acrescentando o sufixo `-copia-curso`. Todo o curso ocorre na cópia. A pasta
   original permanece fechada.
2. **Criar a pasta de teste.** Uma pasta nova, chamada `teste-codex`, contendo três ou quatro
   arquivos de texto de exemplo, sem valor. O primeiro contato com o agente, no Módulo 2, será feito
   nela.
3. **Identificar o plano e os controles de dados.** Localizar o plano em uso no menu de perfil da
   conta do ChatGPT e, nos planos Plus e Pro, decidir sobre o uso do conteúdo para aperfeiçoamento
   dos modelos.

### Exercício Prático

**Verificação de prontidão (7 min)**

Executar os três passos acima e conferir o resultado.

> 🏁 **Ponto de controle:** no explorador de arquivos, existem a pasta original, a cópia com sufixo
> `-copia-curso` e a pasta `teste-codex` com arquivos dentro. E o participante consegue afirmar qual
> é o seu plano.

**Critério de êxito:** os três itens do ponto de controle foram confirmados, e o participante
consegue enunciar, sem consultar o material, qual nível de aprovação adotará e por quê.

### Solução de Problemas — Preparação

| Situação | Procedimento |
|---|---|
| A pasta é grande demais para copiar | Copiar apenas a subpasta que será usada nos exercícios. O curso não exige a pasta inteira. |
| Não sei qual é o meu plano | Podem existir duas contas — a institucional e a pessoal. Conferir com qual endereço se está conectado. |
| Os controles de dados não estão disponíveis | Ocorre em contas administradas institucionalmente, em que a configuração é central. Não é falha. |
| Não sei o que colocar na pasta de teste | Três arquivos de texto quaisquer, com nomes deliberadamente desorganizados. Servem justamente para isso. |

---

# Módulo 1 — O que o Codex faz com uma pasta sua

> Pressupõe as decisões do Módulo 0 e desloca o foco do controle para o motivo: para que isto serve a
> quem não programa.

## Descrição

- **Objetivos da Aula:** apresentar, em casos concretos do trabalho docente, o que o agente faz sobre
  uma pasta de arquivos; e delimitar os tipos de tarefa em que a ferramenta ajuda e aqueles em que
  não ajuda.
- **Habilidades Esperadas:** ao final, o participante identifica em sua própria rotina ao menos duas
  tarefas que caberiam no agente, e reconhece pelo menos uma que não cabe.

### Quatro coisas que um docente pede a um agente

- **📸 Sugestão de Prints:** Visual Studio Code com uma pasta de material de aula aberta na barra
  lateral esquerda, exibindo uma lista de arquivos com nomes desorganizados, e o painel do Codex à
  direita com um pedido em português digitado.

O Codex é descrito pela OpenAI como um agente que auxilia a escrever, revisar e entregar código. Essa
descrição é correta e é incompleta para o presente público. O que ela não diz é o seguinte: **o
agente opera sobre uma pasta de arquivos a partir de instruções em português.** Pastas de arquivos é
o que um docente tem aos milhares, e nenhuma delas precisa conter código.

Quatro casos ilustram o alcance:

| Situação | O que se pede | O que se obtém |
|---|---|---|
| Trinta arquivos de aula com nomes como `aula1.pdf`, `AULA 2 final.pdf`, `aula2-CORRIGIDA(1).pdf` | "Renomeie todos os arquivos no padrão `aula-NN-tema.pdf`, mostrando antes a lista do que vira o quê" | Uma lista para conferir e, aprovada, trinta arquivos padronizados |
| Uma pasta com dezenas de textos e a lembrança de ter escrito sobre um assunto em algum lugar | "Em quais arquivos desta pasta menciono [assunto]? Liste o arquivo e o trecho" | A localização exata, sem abrir arquivo por arquivo |
| Notas exportadas de uma planilha em arquivo de dados | "Faça um gráfico de barras das médias por turma a partir deste arquivo e salve como imagem" | Uma imagem de gráfico na pasta |
| Uma pasta acumulada ao longo de semestres, sem organização | "Crie um arquivo `indice.md` com a lista de todos os arquivos e um resumo de uma frase de cada um" | Um índice navegável do próprio material |

Observa-se o que os quatro casos têm em comum: nenhum exige que o participante escreva uma única
linha de código, e todos exigem que ele descreva com precisão o que pretende.

### Discussão Orientada — quando serve e quando não serve

Convém delimitar. A ferramenta atua bem sobre tarefas que satisfazem três condições: incidem sobre
arquivos que estão em uma pasta; podem ser descritas em uma instrução verificável; e produzem um
resultado que o participante consegue conferir.

Fora dessas condições, o retorno cai ou o risco sobe. Três exemplos de tarefa em que não convém
empregar o agente:

1. **Julgamento sobre o conteúdo.** Avaliar a qualidade de um trabalho, atribuir nota, decidir se um
   argumento se sustenta. O agente produz uma opinião plausível, e plausível não é o mesmo que
   fundamentado.
2. **Tarefa cujo resultado não se consegue conferir.** Se o participante não tem como verificar se a
   saída está correta, não tem como usá-la com responsabilidade.
3. **Tarefa sobre material que não deveria estar na pasta.** A regra do Módulo 0 é anterior a
   qualquer consideração de utilidade.

### Exercício Prático

**Identificação de tarefas próprias (4 min)**

Percorrer mentalmente as pastas do próprio computador e responder:

1. Qual das próprias pastas está mais desorganizada, e que padrão de nome conviria a ela?
2. Que pergunta ao próprio material já se quis fazer e não se fez, por dar muito trabalho procurar?
3. Que tarefa da própria rotina **não** caberia no agente, e por qual das três razões acima?

**Critério de êxito:** o participante nomeia uma pasta concreta com um padrão de nome desejado, uma
pergunta concreta a fazer ao próprio material, e uma tarefa que reconhece como inadequada, com a
razão.

---

# Módulo 2 — Instalar o editor e a extensão

> Pressupõe o Módulo 1 e desloca o foco do motivo para o acesso.

## Descrição

- **Objetivos da Aula:** conduzir a instalação do Visual Studio Code e da extensão Codex; e
  apresentar o editor pelo que ele é para este público — uma janela que abre uma pasta e mostra o que
  há dentro.
- **Habilidades Esperadas:** ao final, o participante tem o editor e a extensão instalados e
  conectados à conta, abre uma pasta sozinho, e sabe diagnosticar uma falha de inicialização.

### O editor, sem intimidação

- **📸 Sugestão de Prints:** Visual Studio Code recém-instalado, com a pasta `teste-codex` aberta na
  barra lateral esquerda, mostrando os arquivos de exemplo. A captura deve mostrar a interface limpa,
  antes de qualquer configuração.

O Visual Studio Code é um editor de texto gratuito, distribuído pela Microsoft, disponível para
Windows, macOS e Linux. Foi concebido para quem escreve software, mas sua função básica é mais
simples do que isso sugere: **abre uma pasta e mostra os arquivos que ela contém.** É o bastante para
o propósito deste curso, e o participante não precisará de nenhuma outra função do editor.

O Codex pode ser acessado por mais de um caminho — há uma versão para a web, uma para linha de
comando e uma dentro do aplicativo do ChatGPT para desktop. Este curso trata exclusivamente da
extensão para o Visual Studio Code, por ser a que apresenta os arquivos e as alterações propostas de
forma visual, o que é decisivo para quem está aprendendo a revisar o trabalho de um agente.

### Procedimento de instalação

1. Baixar o Visual Studio Code no sítio oficial e instalar.
2. Abrir o editor.
3. Abrir o painel de extensões, na barra lateral esquerda:
   `Visual Studio Code > barra lateral > Extensões`.
4. Pesquisar por `Codex` e instalar a extensão correspondente.
5. Abrir o painel do Codex e entrar com a conta do ChatGPT.
6. Configurar o modo de aprovação para somente leitura, conforme decidido no Módulo 0.
7. Abrir a pasta de teste: `Visual Studio Code > Arquivo > Abrir Pasta > teste-codex`.

> ⚠️ **Observação.** Caso a organização gerencie as atualizações dos aplicativos, o administrador
> precisa implantar a versão aprovada antes que os recursos que a exigem possam ser utilizados. Em
> ambiente institucional com instalação bloqueada, o curso não pode ser executado.

### Exercício Prático

**Instalação e primeiro reconhecimento (7 min)**

1. Executar os sete passos do procedimento acima.
2. Confirmar que a pasta `teste-codex` está aberta e que seus arquivos aparecem na barra lateral.
3. Confirmar que o painel do Codex está visível e conectado.

> 🏁 **Ponto de controle:** os arquivos de exemplo da pasta `teste-codex` aparecem na barra lateral
> esquerda, e o painel do Codex mostra a conta conectada. **Nenhuma pasta de material real foi
> aberta.**

**Critério de êxito:** os dois itens do ponto de controle foram confirmados, na pasta de teste e não
em material real.

### Solução de Problemas — Instalação

| Situação | Procedimento |
|---|---|
| Não consigo instalar programas | A instituição pode bloquear instalações. O curso não pode ser executado sem o editor; consultar quem administra os equipamentos. |
| Não encontrei a extensão | Conferir a grafia da pesquisa e o editor responsável pela extensão. O nome exato deve ser confirmado na loja de extensões vigente. |
| A extensão instala mas não aceita a conta | Verificar se o acesso está sendo feito com a conta ChatGPT correta. É comum haver uma pessoal e uma institucional. |
| O painel abre e não responde | Executar o diagnóstico. Abrir o terminal — a janela em que se digitam comandos em vez de clicar em botões — em `Visual Studio Code > Terminal > Novo Terminal`, digitar `codex doctor` e pressionar Enter. O comando verifica problemas de inicialização, conectividade e desempenho, e informa o que encontrou. |
| Não sei onde ficam os arquivos abertos | O editor mostra, na barra lateral esquerda, apenas o conteúdo da pasta aberta. O que está fora dela não aparece — e o agente também não o vê. |

---

# Módulo 3 — Pedir, revisar, aprovar

> Pressupõe a ferramenta instalada no Módulo 2 e desloca o foco do acesso para o ciclo de trabalho
> propriamente dito.

## Descrição

- **Objetivos da Aula:** apresentar o ciclo de três tempos — pedido, proposta, aprovação; demonstrar
  a formulação de pedido que produz uma proposta conferível; e situar a revisão como etapa
  insubstituível.
- **Habilidades Esperadas:** ao final, o participante formula sozinho um pedido que resulta em uma
  lista de alterações propostas, confere essa lista antes de aprovar, e sabe recusar.

### O ciclo de três tempos

- **📸 Sugestão de Prints:** painel do Codex exibindo uma lista de alterações propostas — nomes de
  arquivo antigos e novos lado a lado — com os controles de aceitar e recusar visíveis, e a pasta
  ainda inalterada na barra lateral esquerda.

O trabalho com o agente observa três tempos, sempre na mesma ordem.

| Tempo | Quem age | O que acontece |
|---|---|---|
| 1. Pedido | O participante | Descreve em português o que pretende, com o padrão desejado |
| 2. Proposta | O agente | Apresenta o que faria, item a item, sem alterar nada |
| 3. Aprovação | O participante | Confere a proposta e aprova, corrige ou recusa |

O segundo tempo é o que distingue um agente bem operado de um agente perigoso, e ele não acontece
sozinho: **é preciso pedi-lo**. A formulação que o produz é sempre da mesma família — "antes de
executar, mostre a lista do que você vai fazer". Sem ela, o agente que estiver em modo automático
executa, e o participante descobre o resultado depois.

Retoma-se aqui o conceito plantado no Módulo 0: um texto equivocado se descarta; uma alteração
equivocada em arquivo precisa ser desfeita. O segundo tempo do ciclo existe para que a alteração
equivocada não chegue a ocorrer.

Cumpre registrar o que torna um pedido eficaz. Três elementos bastam: o **padrão** pretendido, dito
com precisão (`aula-NN-tema.pdf` é operacional; "organize isso" não é); a **restrição de
preservação**, declarando o que não deve mudar (o conteúdo dos arquivos, a data de modificação, os
originais); e a **exigência de proposta prévia**, que produz o segundo tempo.

Observa-se, por fim, que o agente aproveita o contexto do editor: quando um arquivo está aberto ou um
trecho está selecionado, o pedido pode ser mais curto, porque o sistema já sabe a que se refere.

### O que a revisão precisa alcançar

A revisão não é uma leitura rápida da proposta. Três verificações a compõem:

1. **A lista está completa?** O número de itens propostos corresponde ao número de arquivos que o
   participante espera ver alterados.
2. **Cada item está correto?** Amostrar. Conferir cinco itens escolhidos, não apenas o primeiro.
3. **Há algo que não deveria estar ali?** Um arquivo que o participante não esperava que fosse
   tocado é sinal de que o pedido foi mais amplo do que se pretendia.

### Exercício Prático — Pílula Hands-on

**Primeiro ciclo completo, na pasta de teste (6 min)**

1. Com a pasta `teste-codex` aberta, formular o pedido com os três elementos:
   *"Renomeie os arquivos desta pasta no padrão `documento-NN-assunto.txt`. Preserve o conteúdo de
   cada arquivo. Antes de executar, mostre a lista do que vai virar o quê."*
2. Ler a lista proposta.
3. Aplicar as três verificações de revisão.
4. Aprovar, corrigir ou recusar.
5. Conferir a pasta na barra lateral.

> 🏁 **Ponto de controle:** os arquivos da pasta `teste-codex` aparecem, na barra lateral esquerda,
> com os nomes do padrão pedido. Nenhum arquivo desapareceu, e a contagem é a mesma de antes.

**Critério de êxito:** o pedido continha os três elementos, a proposta foi conferida por amostragem
antes da aprovação, e a contagem de arquivos permaneceu a mesma.

### Solução de Problemas — Execução

| Situação | Procedimento |
|---|---|
| O agente executou sem mostrar a lista | O modo de aprovação não está em somente leitura, ou o pedido não exigiu a proposta prévia. Corrigir os dois. |
| A proposta contém arquivos que não deveriam ser tocados | Recusar e refazer o pedido delimitando: "apenas os arquivos com extensão X", ou "apenas os arquivos da subpasta Y". |
| O agente pediu permissão para algo que não foi compreendido | Recusar. A regra é simples e não tem exceção: não se autoriza o que não se entendeu. |
| Um arquivo desapareceu | Recuperar a partir da cópia de segurança criada no Módulo 0. É a situação para a qual ela existe. |
| O agente não encontrou os arquivos | Conferir qual pasta está aberta. O agente vê apenas o conteúdo da pasta de trabalho. |

---

# Módulo 4 — Ensinar ao Codex as regras da sua pasta

> Pressupõe o Módulo 3 e desloca o foco da tarefa isolada para o padrão que se repete a cada
> semestre.

## Descrição

- **Objetivos da Aula:** apresentar o arquivo de instruções de projeto como forma de registrar, uma
  única vez, as regras que o agente deve seguir naquela pasta; e apresentar o critério de quando vale
  criá-lo.
- **Habilidades Esperadas:** ao final, o participante cria um arquivo de instruções em português para
  uma pasta sua e verifica que o agente passa a seguir a regra sem que ela seja repetida.

### O problema da instrução repetida

- **📸 Sugestão de Prints:** o Visual Studio Code com o arquivo de instruções aberto no editor,
  mostrando texto em português, e a árvore de arquivos da pasta na barra lateral esquerda.

O docente que organiza material de aula tem, quase sempre, um padrão próprio: nomes em determinado
formato, subpastas por unidade, um índice atualizado ao fim do semestre. Repetir esse padrão ao agente
a cada pedido é trabalho, e trabalho que se esquece de fazer.

O Codex admite que essas regras sejam escritas uma única vez, em um **arquivo de instruções do
projeto**, guardado na própria pasta. A partir daí, o agente as consulta em todo pedido feito naquela
pasta. O arquivo é criado por um comando de inicialização, que gera uma estrutura inicial para a
pasta atual, e o participante o edita como editaria qualquer texto — em português, sem sintaxe
especial.

O critério de decisão é o mesmo de qualquer automação: **se o padrão se repete a cada semestre, vale
escrevê-lo; se a tarefa é única, não vale.**

> ⚠️ **Condicionante.** O comando de inicialização é documentado para o Codex no aplicativo de
> desktop e na linha de comando. Sua disponibilidade a partir da extensão do Visual Studio Code deve
> ser confirmada na versão vigente. Não estando disponível, o mesmo efeito se obtém criando o arquivo
> à mão, na raiz da pasta, e mencionando-o no pedido.

### O que escrever nesse arquivo

Convém que o arquivo responda a quatro perguntas, em prosa simples:

| Pergunta | Exemplo de resposta |
|---|---|
| O que há nesta pasta? | Material da disciplina de Metodologia da Pesquisa, semestres de 2024 e 2025 |
| Como os arquivos devem ser nomeados? | `aula-NN-tema.pdf`, com NN de dois dígitos e tema em minúsculas, sem acento |
| Como devem ser organizados? | Uma subpasta por unidade, numeradas de `01-` a `04-` |
| O que nunca deve ser feito aqui? | Não alterar o conteúdo dos arquivos; não apagar nada; não mexer na subpasta `originais` |

A quarta pergunta é a mais importante e a menos óbvia. Um arquivo de instruções que só diz o que
fazer deixa o resto em aberto; um que declara o que não fazer estabelece um limite que vale para
todos os pedidos futuros.

### Exercício Prático — Pílula Hands-on

**Criação do arquivo de instruções (6 min)**

1. Abrir a cópia de trabalho no editor.
2. Criar, na raiz da pasta, um arquivo de instruções respondendo às quatro perguntas acima.
3. Formular um pedido que **não** repita nenhuma das regras escritas — por exemplo, "organize os
   arquivos desta pasta; antes de executar, mostre a lista".
4. Verificar, na proposta, se o padrão declarado no arquivo foi observado.

> 🏁 **Ponto de controle:** a proposta do agente segue o padrão de nome declarado no arquivo de
> instruções, embora o pedido não o tenha mencionado.

**Critério de êxito:** o arquivo de instruções existe na pasta, responde às quatro perguntas, e a
proposta do agente reflete ao menos uma regra que não foi repetida no pedido.

---

# Módulo 5 — Síntese e Aplicação Integrada

> Pressupõe todos os módulos anteriores e os articula em uma única atividade de produção.

## Descrição

- **Objetivos da Aula:** apresentar o fluxo completo de trabalho com o agente, do controle à
  automação; e situar a responsabilidade sobre o resultado.
- **Habilidades Esperadas:** ao final, o participante conduz sozinho uma tarefa completa sobre pasta
  própria, do estabelecimento dos limites à conferência do resultado.

### O fluxo completo

- **📸 Sugestão de Prints:** Visual Studio Code com uma pasta reorganizada — subpastas numeradas,
  arquivos com nomes padronizados, um arquivo de índice e o arquivo de instruções visíveis na barra
  lateral esquerda.

Cumpre articular o que foi tratado de modo disperso. O trabalho com o agente observa um fluxo de seis
etapas, e as duas primeiras acontecem antes de qualquer pedido:

| Etapa | O que se faz | Onde foi tratado |
|---|---|---|
| 1 | Estabelecer os limites: cópia de segurança, nível de aprovação, o que fica fora da pasta | Módulo 0 |
| 2 | Reconhecer se a tarefa cabe no agente | Módulo 1 |
| 3 | Formular o pedido com padrão, preservação e exigência de proposta prévia | Módulo 3 |
| 4 | Revisar a proposta pelas três verificações | Módulo 3 |
| 5 | Aprovar, corrigir ou recusar | Módulo 3 |
| 6 | Registrar o padrão no arquivo de instruções, quando se repetir | Módulo 4 |

Observa-se que a etapa 4 é insubstituível. Retoma-se, pela última vez, o conceito do Módulo 0: um
texto equivocado se descarta; uma alteração equivocada em arquivo precisa ser desfeita. **A decisão
sobre o que aceitar permanece integralmente com quem revisa**, e nenhuma etapa do fluxo transfere
essa responsabilidade.

### Exercício Prático — Atividade Integradora

**Uma pasta própria, do controle ao resultado (6 min de execução assistida; a tarefa pode ser
concluída depois)**

1. Confirmar que se está trabalhando na cópia, e não no original.
2. Escolher uma tarefa entre as identificadas no Módulo 1.
3. Formular o pedido com os três elementos.
4. Revisar a proposta pelas três verificações.
5. Aprovar, corrigir ou recusar.
6. Conferir o resultado na barra lateral e, havendo padrão a repetir, registrá-lo no arquivo de
   instruções.

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

---

# Encerramento

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

> **Síntese:** o agente executa; a decisão sobre o que aceitar permanece de quem revisa.
