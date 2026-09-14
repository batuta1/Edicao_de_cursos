# Relatório de Roteiro de Curso

## **Código Claude no Desktop — Comece com o aplicativo de desktop**

**Público-alvo:** discentes e docentes da graduação em Engenharia, especialmente estudantes dos semestres iniciais.
**Objetivo geral:** apresentar o Claude Code Desktop como uma ferramenta de apoio à aprendizagem, programação, revisão de código, organização de projetos e experimentação prática, sem exigir domínio avançado de terminal ou infraestrutura de desenvolvimento.

---

## Visão Geral do Curso

Este curso foi pensado para quem olha para uma ferramenta de programação com IA e pensa:

> “Isso parece poderoso, mas será que eu vou quebrar tudo se clicar no botão errado?”

A resposta curta é: **não precisa entrar em pânico**.

O Claude Code Desktop funciona como um **assistente de programação com interface visual**, capaz de conversar sobre código, acessar arquivos do projeto, sugerir alterações, mostrar diferenças entre versões, abrir terminal integrado, acompanhar tarefas e ajudar em fluxos de desenvolvimento.

A ideia central do curso é mostrar que o estudante não precisa começar “dominando tudo”. Ele precisa começar entendendo **onde clicar, o que pedir e como revisar antes de aceitar mudanças**.

---

# Módulo 1 — **Claude Code Desktop: o copiloto com carteira de motorista**

## O “Pulo do Gato”

O Claude Code Desktop é como um **monitor de laboratório de programação**: ele entende o projeto, sugere mudanças e explica caminhos. Mas, no modo padrão, **você ainda dá a autorização final** antes de qualquer alteração ser aplicada.

## Desenvolvimento

O aplicativo de desktop oferece uma interface gráfica para trabalhar com código sem depender exclusivamente do terminal. Ele permite abrir projetos, conversar com Claude sobre arquivos, revisar alterações e executar tarefas de programação.

Ele é especialmente útil para estudantes de Engenharia porque ajuda em situações comuns, como:

* entender um código que o professor passou;
* localizar erros simples;
* criar testes;
* documentar um projeto;
* comparar versões de arquivos;
* organizar pequenos experimentos computacionais;
* revisar antes de entregar uma atividade.

Um ponto importante: o Claude Code Desktop possui três abas principais:

**Chat**
Funciona como uma conversa geral, parecida com o uso comum de IA. Não é o foco principal deste curso.

**Cowork**
É uma área em que um agente pode trabalhar em tarefas em segundo plano, em ambiente próprio. É mais avançada e será tratada apenas como visão geral.

**Code**
É a aba central deste curso. Nela, Claude trabalha diretamente com arquivos de um projeto, sempre com possibilidade de revisão.

> **Bloco de atenção:**
> Para estudantes iniciantes, a aba **Code** deve ser entendida como uma “bancada de laboratório”. Você testa, observa, revisa e só depois confirma.

## Pílula Hands-on — 2 minutos

No celular ou computador, escreva em uma nota:

```text
Uma tarefa que eu gostaria que uma IA me ajudasse em programação é:
```

Complete com uma frase simples, por exemplo:

```text
Explicar um código em Python que eu não entendi.
```

Depois, reescreva a frase como um comando mais claro:

```text
Explique este código em Python linha por linha, usando exemplos simples.
```

---

# Módulo 2 — **Antes de instalar: conferindo se a porta está aberta**

## O “Pulo do Gato”

Antes de usar o Claude Code Desktop, é preciso verificar três coisas: **sistema operacional, assinatura compatível e acesso à conta**.

## Desenvolvimento

O aplicativo está disponível para **macOS** e **Windows**. No caso do Windows, há instaladores específicos para processadores x64 e ARM64. O Linux, segundo o texto-base, **não é suportado** nessa versão de desktop.

Também é necessário ter uma assinatura compatível, como **Pro, Max, Team ou Enterprise**. Isso significa que nem todo acesso gratuito permitirá usar a aba Code.

Para estudantes, isso é importante porque evita uma frustração comum:

> “Instalei, abri, cliquei e apareceu uma mensagem de upgrade. Fiz algo errado?”

Provavelmente não. Pode ser apenas limitação do plano.

O processo básico de instalação envolve:

1. baixar o instalador correto;
2. executar a instalação;
3. abrir o aplicativo;
4. fazer login com a conta Anthropic;
5. acessar a aba **Code**.

Se aparecer erro de autenticação ou erro 403, o problema tende a estar relacionado ao login, permissão da conta ou necessidade de reiniciar o aplicativo após autenticação.

## Pílula Hands-on — 2 minutos

Faça uma checagem rápida no seu dispositivo:

```text
Meu sistema operacional é:
Meu computador é Windows, macOS ou outro?
Eu sei se minha conta tem plano compatível?
```

Agora transforme isso em checklist:

* [ ] Sei qual é meu sistema operacional.
* [ ] Sei se meu computador é Windows x64, Windows ARM64 ou macOS.
* [ ] Sei se minha conta tem assinatura compatível.
* [ ] Sei onde pedir ajuda se aparecer erro de login.

---

# Módulo 3 — **As três abas: cada coisa em sua gaveta**

## O “Pulo do Gato”

Pense nas três abas como espaços diferentes de uma escola: **Chat é a conversa no corredor, Cowork é o assistente trabalhando sozinho e Code é o laboratório com arquivos reais na mesa**.

## Desenvolvimento

A interface do Claude Code Desktop organiza diferentes formas de interação.

### 1. Chat: conversa geral

A aba Chat serve para perguntas amplas, explicações, ideias e planejamento. Ela não acessa diretamente seus arquivos locais do projeto.

Exemplos de uso:

* “Explique o que é uma função em Python.”
* “Qual a diferença entre algoritmo e programa?”
* “Me dê uma analogia para entender ponteiros em C.”

### 2. Cowork: agente em segundo plano

A aba Cowork permite que um agente trabalhe de forma autônoma em um ambiente próprio. Isso é mais avançado e pode ser útil para tarefas que continuam enquanto o usuário faz outra coisa.

Para iniciantes, a recomendação didática é: **entenda que existe, mas comece pela aba Code**.

### 3. Code: programação com arquivos reais

A aba Code é o foco do curso. Ela permite selecionar uma pasta de projeto, pedir alterações, revisar diferenças e aceitar ou rejeitar mudanças.

Exemplos de comandos:

```text
Encontre um comentário TODO e sugira uma correção.
```

```text
Crie um arquivo README explicando este projeto.
```

```text
Explique o que este código faz em linguagem simples.
```

> **Analogia de sala de aula:**
> O Chat é como perguntar ao professor “o que é resistência elétrica?”.
> O Code é como abrir seu relatório de laboratório e pedir: “verifique se meu cálculo de resistência está coerente com os dados da tabela”.

## Pílula Hands-on — 2 minutos

Escreva três perguntas, uma para cada aba:

**Chat:**

```text
Explique o conceito de variável como se eu estivesse no primeiro semestre.
```

**Cowork:**

```text
Liste tarefas que poderiam ser feitas em segundo plano em um projeto de programação.
```

**Code:**

```text
Analise os arquivos deste projeto e diga por onde devo começar a estudá-lo.
```

---

# Módulo 4 — **Escolhendo o projeto: comece pelo caderno pequeno**

## O “Pulo do Gato”

Não comece testando a ferramenta no projeto mais importante da sua vida. Comece com um projeto pequeno, conhecido e sem risco.

## Desenvolvimento

Ao abrir a aba Code, o usuário deve escolher um ambiente e uma pasta de projeto.

O ambiente pode ser:

**Local**
Claude trabalha com arquivos no seu próprio computador.

**Remote**
Claude executa sessões na infraestrutura em nuvem.

**SSH**
Claude se conecta a uma máquina remota, como servidor, VM ou ambiente de desenvolvimento.

Para estudantes iniciantes, o caminho mais simples é usar **Local** com uma pasta pequena, por exemplo:

* um exercício de Python;
* um projeto simples de C;
* uma atividade de Introdução à Computação;
* um arquivo HTML de teste;
* uma pasta com poucos arquivos.

No Windows, há um detalhe técnico importante: para sessões locais funcionarem, é necessário ter o **Git instalado**.

> **Bloco de atenção:**
> O projeto inicial ideal não é o mais bonito nem o mais complexo. É aquele que você entende minimamente e pode comparar se a IA está ajudando ou atrapalhando.

## Pílula Hands-on — 2 minutos

Crie mentalmente ou em uma nota uma pasta de teste:

```text
Projeto: calculadora_simples
Arquivos:
- calculadora.py
- README.md
- testes.txt
```

Agora escreva o primeiro pedido que você faria ao Claude:

```text
Leia este projeto e explique, em linguagem simples, o que cada arquivo faz.
```

---

# Módulo 5 — **Escolhendo o modelo: motor de Fusca, sedan ou Fórmula 1?**

## O “Pulo do Gato”

O modelo é o “motor” da IA. Alguns são mais rápidos, outros mais robustos. O segredo é escolher conforme a tarefa, não por vaidade tecnológica.

## Desenvolvimento

O texto-base menciona a escolha de modelos como **Opus, Sonnet e Haiku**, disponíveis em um menu próximo ao botão de envio.

Para explicar de forma simples:

**Haiku**
Pode ser entendido como uma opção mais leve e rápida. Útil para perguntas simples, revisões iniciais e tarefas menores.

**Sonnet**
Equilibra qualidade e velocidade. Costuma ser adequado para boa parte das tarefas de estudo, explicação e programação.

**Opus**
É mais indicado para tarefas complexas, análise profunda, refatorações maiores ou decisões mais sofisticadas.

Em sala de aula, a analogia seria:

* Haiku: resposta rápida no quadro.
* Sonnet: explicação completa durante a aula.
* Opus: orientação detalhada de projeto final.

Para estudantes iniciantes, a melhor prática é observar:

* a complexidade da tarefa;
* o tempo disponível;
* a necessidade de precisão;
* o risco de alterar arquivos importantes.

## Pílula Hands-on — 2 minutos

Classifique as tarefas abaixo como **simples**, **média** ou **complexa**:

1. Explicar o que é uma variável.
2. Criar testes para uma função.
3. Reorganizar um projeto inteiro de software.
4. Encontrar um erro de digitação em um arquivo.
5. Revisar uma arquitetura de sistema.

Agora escreva:

```text
Para tarefas simples, eu usaria um modelo mais rápido.
Para tarefas complexas, eu escolheria um modelo mais robusto.
```

---

# Módulo 6 — **Como pedir: prompt bom é enunciado de prova bem escrito**

## O “Pulo do Gato”

Claude entende melhor quando você dá uma tarefa clara, com contexto e resultado esperado. Prompt vago gera resposta vaga.

## Desenvolvimento

O texto-base oferece exemplos simples de comandos:

```text
Find a TODO comment and fix it
```

```text
Add tests for the main function
```

```text
Create a CLAUDE.md with instructions for this codebase
```

Em português didático, esses comandos significam:

* encontre algo pendente no código;
* crie testes;
* documente como trabalhar naquele projeto.

Para estudantes de Engenharia, uma boa estrutura de prompt pode seguir quatro partes:

1. **Contexto:** diga o que é o projeto.
2. **Tarefa:** diga o que você quer.
3. **Limite:** diga o que não deve ser alterado.
4. **Formato:** diga como quer receber a resposta.

Exemplo:

```text
Este é um projeto simples de Python para calcular média de notas.
Explique o código e sugira melhorias, mas não altere os arquivos ainda.
Organize a resposta em tópicos.
```

Outro exemplo:

```text
Analise este código em C usado em uma disciplina introdutória.
Procure erros simples de lógica.
Explique como se estivesse ensinando um aluno do primeiro semestre.
```

> **Bloco de ouro:**
> Um bom prompt é como um bom enunciado de prova: deixa claro o que deve ser feito, com quais dados e qual tipo de resposta é esperado.

## Pílula Hands-on — 2 minutos

Pegue este prompt ruim:

```text
Arrume meu código.
```

Transforme em um prompt melhor:

```text
Analise meu código em Python, encontre possíveis erros de lógica, explique cada problema em linguagem simples e sugira correções sem alterar os arquivos automaticamente.
```

Agora crie seu próprio prompt usando esta fórmula:

```text
Analise [tipo de arquivo/projeto], faça [tarefa], sem [limite], e responda em [formato].
```

---

# Módulo 7 — **Revisar antes de aceitar: o cinto de segurança do código**

## O “Pulo do Gato”

No modo padrão, Claude propõe alterações, mas você revisa antes de aceitar. É como conferir a resposta da calculadora antes de colocar no relatório.

## Desenvolvimento

A aba Code inicia, por padrão, em um modo de permissão chamado **Ask permissions**. Isso significa que Claude não sai alterando tudo livremente. Ele mostra o que pretende modificar, e o usuário decide se aceita ou rejeita.

A revisão aparece por meio de uma visualização chamada **diff view**. Nela, é possível ver:

* quais linhas foram adicionadas;
* quais linhas foram removidas;
* quais arquivos foram modificados;
* o que mudou em cada trecho.

Geralmente, mudanças aparecem com indicadores como:

```text
+12 -1
```

Isso quer dizer que houve, por exemplo, 12 linhas adicionadas e 1 linha removida.

Para estudantes, isso é excelente porque ensina uma prática profissional: **nunca aceitar mudança sem entender minimamente o que mudou**.

Se a sugestão não estiver boa, é possível rejeitar e orientar:

```text
Não altere essa função. Em vez disso, apenas adicione comentários explicativos.
```

Ou:

```text
Essa solução ficou muito avançada. Refaça usando estruturas mais simples, adequadas ao primeiro semestre.
```

## Pílula Hands-on — 2 minutos

Observe este exemplo fictício:

```diff
- media = soma / 2
+ media = soma / quantidade
```

Responda:

1. O que mudou?
2. A mudança parece fazer sentido?
3. Que pergunta você faria antes de aceitar?

Sugestão de resposta:

```text
A média deixou de ser dividida por 2 e passou a ser dividida pela quantidade de elementos. Faz sentido se a lista puder ter mais de dois valores.
```

---

# Módulo 8 — **Interromper e orientar: você pode puxar o freio de mão**

## O “Pulo do Gato”

Se Claude estiver indo para o caminho errado, você não precisa esperar terminar. Pode interromper e redirecionar.

## Desenvolvimento

Uma das funções importantes do Claude Code Desktop é permitir que o usuário interrompa a execução. Isso é essencial para manter controle sobre a tarefa.

Imagine a seguinte situação:

Você pediu:

```text
Explique este código.
```

Mas Claude começou a modificar arquivos. Você pode interromper e dizer:

```text
Pare. Eu quero apenas explicação, sem alterações nos arquivos.
```

Ou:

```text
Volte um passo. Antes de sugerir mudanças, me mostre o diagnóstico.
```

Esse tipo de interação é muito útil em contexto educacional. O estudante aprende a dialogar com a ferramenta, não apenas receber uma resposta pronta.

> **Analogia de sala:**
> É como levantar a mão no meio da explicação e dizer: “Professor, antes de continuar, pode voltar naquele passo?”

## Pílula Hands-on — 2 minutos

Escreva três frases de interrupção educada:

```text
Pare por enquanto e explique o que você está fazendo.
```

```text
Não altere os arquivos ainda. Primeiro, apresente o plano.
```

```text
Refaça usando uma solução mais simples para iniciantes.
```

Agora adapte uma delas para sua realidade de estudo.

---

# Módulo 9 — **Dando contexto: IA não lê sua mente, mas lê arquivos**

## O “Pulo do Gato”

Quanto melhor o contexto, melhor a resposta. Claude pode trabalhar melhor quando você indica arquivos, anexos ou trechos importantes.

## Desenvolvimento

O texto-base menciona várias formas de fornecer contexto:

* digitar `@filename` para mencionar um arquivo específico;
* anexar imagens e PDFs;
* arrastar e soltar arquivos;
* indicar trechos relevantes no prompt.

Isso é especialmente útil em cursos de Engenharia porque muitos problemas envolvem materiais variados:

* código;
* relatório;
* imagem de circuito;
* PDF de enunciado;
* tabela de dados;
* especificação de projeto;
* arquivo de entrada e saída.

Um pedido com pouco contexto seria:

```text
Meu código não funciona.
```

Um pedido com bom contexto seria:

```text
O arquivo main.py deveria ler uma lista de notas e calcular a média.
Use o arquivo dados.txt como entrada.
O erro acontece quando há linhas em branco.
Explique o problema e sugira correção.
```

> **Bloco de destaque:**
> Contexto é o “material da prova”. Sem ele, a IA tenta adivinhar. Com ele, a IA trabalha com mais precisão.

## Pílula Hands-on — 2 minutos

Pegue este problema:

```text
Meu programa não roda.
```

Adicione contexto:

```text
Meu programa em Python deveria calcular a área de um círculo.
O erro aparece quando digito o raio.
Quero que você explique o problema sem corrigir automaticamente.
```

Agora faça o mesmo para uma disciplina sua.

---

# Módulo 10 — **Permissões: modo aluno cauteloso, modo aluno apressado e modo planejamento**

## O “Pulo do Gato”

Os modos de permissão controlam o quanto Claude pode agir sozinho. Para iniciantes, o melhor amigo é o modo cauteloso.

## Desenvolvimento

O texto-base apresenta três modos principais:

### Ask permissions

É o modo padrão. Claude pede aprovação antes de aplicar alterações.

Ideal para:

* estudantes iniciantes;
* projetos avaliativos;
* trabalhos em grupo;
* códigos que você ainda está aprendendo;
* situações em que é importante entender cada mudança.

### Auto accept edits

Aceita automaticamente edições de arquivos. Pode acelerar o trabalho, mas exige mais confiança.

Ideal para:

* tarefas repetitivas;
* projetos de teste;
* usuários mais experientes;
* momentos em que há controle de versão bem configurado.

### Plan mode

Claude planeja antes de alterar arquivos. É útil para refatorações maiores ou decisões delicadas.

Ideal para pedir:

```text
Antes de alterar qualquer arquivo, proponha um plano de correção.
```

Ou:

```text
Monte uma estratégia para melhorar este projeto, mas não faça mudanças ainda.
```

> **Recomendação pedagógica:**
> Para os primeiros contatos, use uma mentalidade de **Plan mode + Ask permissions**. Primeiro entenda o plano, depois revise as alterações.

## Pílula Hands-on — 2 minutos

Associe cada situação ao modo mais adequado:

1. Primeiro contato com um projeto desconhecido.
2. Corrigir pequenos erros em um projeto de teste.
3. Planejar uma grande reorganização de código.
4. Revisar atividade antes de entregar.

Resposta esperada:

```text
1. Ask permissions ou Plan mode
2. Auto accept edits, se for seguro
3. Plan mode
4. Ask permissions
```

---

# Módulo 11 — **Diff View: o detector de pegadinhas**

## O “Pulo do Gato”

A diff view mostra exatamente o que mudou. Ela é o “antes e depois” do código.

## Desenvolvimento

Depois que Claude sugere ou realiza alterações, o usuário pode abrir a visualização de diferenças. Essa tela ajuda a comparar a versão anterior e a nova.

Para estudantes, a diff view ensina três habilidades essenciais:

1. **Leitura cuidadosa de código**
   O aluno aprende a perceber pequenas mudanças.

2. **Pensamento crítico**
   Nem toda sugestão da IA deve ser aceita automaticamente.

3. **Controle de versão**
   O estudante começa a entender práticas usadas em Git, GitHub e desenvolvimento profissional.

Um exemplo simples:

```diff
- if nota > 7:
+ if nota >= 7:
```

Essa pequena mudança altera o comportamento do programa. Antes, nota 7 não passava. Depois, nota 7 passa.

> **Bloco de atenção:**
> Em programação, uma única igualdade pode mudar a vida de um aluno, de um sensor ou de uma ponte. Revise.

## Pílula Hands-on — 2 minutos

Analise a mudança:

```diff
- if temperatura > 100:
+ if temperatura >= 100:
```

Responda:

```text
O que muda quando a temperatura é exatamente 100?
```

Resposta esperada:

```text
Antes, 100 não ativava a condição. Depois, 100 ativa.
```

---

# Módulo 12 — **Terminal integrado: o quadro negro dos comandos**

## O “Pulo do Gato”

O terminal integrado permite executar comandos sem sair do aplicativo. Mas, para iniciantes, ele deve ser usado com calma e propósito.

## Desenvolvimento

O Claude Code Desktop possui terminal integrado, que pode ser aberto com atalho como **Ctrl + `**. Isso permite executar comandos ao lado da sessão.

Na prática, o terminal serve para:

* rodar programas;
* instalar dependências;
* executar testes;
* iniciar servidores locais;
* verificar mensagens de erro.

Para estudantes, o terminal pode parecer assustador. Mas ele pode ser entendido como um espaço para dar ordens diretas ao computador.

Exemplos simples:

```bash
python main.py
```

```bash
npm test
```

```bash
git status
```

O papel de Claude aqui pode ser explicar o comando antes de usá-lo:

```text
Explique o que este comando faz antes de executá-lo.
```

Ou:

```text
Sugira o comando para rodar este projeto, mas não execute ainda.
```

> **Regra de bolso:**
> Se você não entende o comando, peça explicação antes. Terminal não é lugar para “clicar e rezar”.

## Pílula Hands-on — 2 minutos

Leia este comando:

```bash
python main.py
```

Escreva uma explicação simples:

```text
Esse comando pede ao computador para executar o arquivo main.py usando Python.
```

Agora escreva uma pergunta segura:

```text
Explique o que este comando faz e quais arquivos ele pode modificar, se houver.
```

---

# Módulo 13 — **Preview: olhando o experimento funcionando**

## O “Pulo do Gato”

A função Preview permite ver uma aplicação rodando. É como testar um protótipo na bancada, não apenas ler o manual.

## Desenvolvimento

O texto-base explica que o Claude Code Desktop pode rodar um servidor de desenvolvimento e visualizar a aplicação. Claude pode observar a aplicação em execução, testar endpoints, inspecionar logs e iterar com base no que vê.

Isso é muito útil em projetos como:

* páginas web;
* aplicações em JavaScript;
* APIs;
* dashboards;
* interfaces de protótipos;
* simuladores simples.

Para estudantes de Engenharia, isso se conecta bem à ideia de validação experimental:

1. você cria uma hipótese;
2. executa o sistema;
3. observa o resultado;
4. corrige;
5. testa novamente.

Exemplo de pedido:

```text
Execute a aplicação em modo de desenvolvimento, observe a tela inicial e diga se há erros visíveis.
```

Ou:

```text
Abra o preview e verifique se o botão de calcular está funcionando.
```

## Pílula Hands-on — 2 minutos

Imagine que você criou uma calculadora web. Escreva três coisas que você testaria no preview:

```text
1. Se o botão calcular responde ao clique.
2. Se o resultado aparece na tela.
3. Se entradas vazias geram erro ou aviso.
```

Agora transforme isso em prompt:

```text
Teste a calculadora no preview e verifique botão, resultado e comportamento com entrada vazia.
```

---

# Módulo 14 — **Skills e comandos: atalhos para tarefas repetidas**

## O “Pulo do Gato”

Skills são como “modelos prontos de tarefa”. Em vez de explicar tudo de novo, você chama um comando reutilizável.

## Desenvolvimento

O texto-base informa que é possível acessar comandos e skills usando `/` ou o botão `+`, em **Slash commands**.

Skills podem servir para tarefas recorrentes, como:

* revisar código;
* gerar documentação;
* conferir padrões de entrega;
* executar checklist de segurança;
* preparar deploy;
* revisar testes;
* comentar código para iniciantes.

Em contexto educacional, um professor poderia criar ou orientar o uso de skills como:

```text
/checklist-relatorio
```

```text
/revisao-codigo-iniciante
```

```text
/explicar-com-analogias
```

Mesmo sem criar skills avançadas, o estudante pode simular essa lógica guardando prompts reutilizáveis.

Exemplo:

```text
Sempre que eu enviar um código, explique:
1. o objetivo geral;
2. as variáveis principais;
3. o fluxo de execução;
4. possíveis erros;
5. uma versão comentada para iniciantes.
```

## Pílula Hands-on — 2 minutos

Crie sua “skill manual” em uma nota:

```text
Meu comando reutilizável:
Quando eu enviar um código, explique como se eu estivesse no primeiro semestre, destaque erros comuns e sugira uma melhoria simples.
```

Dê um nome para ela:

```text
/revisao-primeiro-semestre
```

---

# Módulo 15 — **Plugins: colocando ferramentas extras na mochila**

## O “Pulo do Gato”

Plugins adicionam capacidades extras ao Claude Code Desktop. Pense neles como acessórios de laboratório: úteis, mas só quando você sabe para que servem.

## Desenvolvimento

O texto-base informa que é possível instalar plugins pelo botão `+`, na opção **Plugins**. Eles podem adicionar:

* skills;
* agentes;
* servidores MCP;
* integrações;
* novas capacidades de workflow.

Para iniciantes, a principal orientação é não instalar tudo de uma vez. O ideal é perguntar:

```text
Este plugin resolve qual problema?
```

```text
Ele acessa quais dados?
```

```text
Ele modifica arquivos ou apenas consulta informações?
```

No contexto da Engenharia, plugins podem apoiar tarefas como:

* integração com repositórios;
* automação de revisão;
* consulta a ferramentas externas;
* ligação com sistemas de tarefas;
* apoio a fluxos de equipe.

> **Bloco de prudência:**
> Plugin não é figurinha de álbum. Instale por necessidade, não por curiosidade infinita.

## Pílula Hands-on — 2 minutos

Antes de instalar qualquer plugin, preencha:

```text
Nome do plugin:
Problema que ele resolve:
Dados que ele acessa:
Risco se usado incorretamente:
Eu realmente preciso dele agora?
```

Se a última resposta for “não sei”, espere.

---

# Módulo 16 — **Sessões paralelas: várias bancadas, sem misturar reagentes**

## O “Pulo do Gato”

Sessões paralelas permitem trabalhar em tarefas diferentes sem uma atrapalhar a outra.

## Desenvolvimento

Uma sessão é uma conversa com Claude sobre determinado conjunto de tarefas e arquivos. Cada sessão acompanha seu próprio contexto e suas próprias mudanças.

Isso ajuda quando há mais de uma frente de trabalho, por exemplo:

* uma sessão para corrigir bugs;
* outra para escrever documentação;
* outra para criar testes;
* outra para estudar o código.

O texto-base menciona que sessões paralelas podem trabalhar em diferentes **Git worktrees**, evitando interferência entre tarefas.

Para estudantes, a analogia é simples:

> Não misture o relatório de Física, o código de C e o trabalho de Cálculo na mesma folha de caderno.

Cada sessão deve ter um objetivo claro.

Exemplo:

```text
Sessão 1: entender o projeto.
Sessão 2: criar testes.
Sessão 3: melhorar documentação.
```

## Pílula Hands-on — 2 minutos

Organize três sessões fictícias para um projeto de disciplina:

```text
Sessão A — Explicação do código
Objetivo: entender cada arquivo.

Sessão B — Testes
Objetivo: criar casos de teste simples.

Sessão C — Documentação
Objetivo: escrever README para entrega.
```

Agora escreva o primeiro prompt da Sessão A.

---

# Módulo 17 — **Pull Requests e CI: quando o trabalho entra na fila profissional**

## O “Pulo do Gato”

Depois que um código vira Pull Request, Claude pode acompanhar resultados de verificação e ajudar a corrigir falhas.

## Desenvolvimento

O texto-base informa que Claude Code pode monitorar Pull Requests, acompanhar resultados de CI e até corrigir falhas ou realizar merge quando tudo passa.

Para estudantes iniciantes, esses termos podem parecer distantes. Vamos simplificar:

**Pull Request**
É um pedido para incorporar mudanças ao projeto principal.

**CI, ou Integração Contínua**
É um sistema automático que roda verificações, testes e validações.

**Merge**
É o ato de juntar sua contribuição ao código principal.

Em projetos acadêmicos, isso pode aparecer em:

* trabalhos em grupo no GitHub;
* projetos de iniciação científica;
* disciplinas de programação;
* extensão tecnológica;
* robótica, sistemas embarcados ou aplicações web.

O aprendizado essencial é:

> Código bom não é só o que roda no seu computador. É o que passa nos testes, pode ser revisado e faz sentido para a equipe.

## Pílula Hands-on — 2 minutos

Explique com suas palavras:

```text
Pull Request é:
CI é:
Merge é:
```

Sugestão:

```text
Pull Request é um pedido de revisão.
CI é uma bateria automática de testes.
Merge é juntar a mudança aprovada ao projeto principal.
```

---

# Módulo 18 — **Tarefas agendadas: o despertador do código**

## O “Pulo do Gato”

Tarefas agendadas permitem rodar Claude em horários definidos, como uma revisão diária ou auditoria semanal.

## Desenvolvimento

O texto-base menciona exemplos de tarefas recorrentes:

* revisão diária de código;
* auditoria semanal de dependências;
* briefing com ferramentas conectadas;
* verificações periódicas.

Para estudantes e docentes, isso pode ser adaptado a rotinas educacionais:

**Para estudantes**

```text
Toda sexta, revisar pendências do projeto.
```

```text
Antes da entrega, gerar checklist de qualidade.
```

**Para docentes**

```text
Revisar exemplos de código antes da aula.
```

```text
Gerar lista de melhorias em material didático.
```

**Para grupos de projeto**

```text
Toda semana, verificar testes quebrados e documentação desatualizada.
```

Mas é importante lembrar: automatizar não substitui compreender. A tarefa agendada ajuda, mas a revisão humana continua essencial.

## Pílula Hands-on — 2 minutos

Crie uma tarefa recorrente imaginária:

```text
Toda segunda-feira, revisar o README do projeto e listar o que está desatualizado.
```

Agora adapte para sua disciplina:

```text
Toda [dia], revisar [material/projeto] e gerar [resultado].
```

---

# Módulo 19 — **Claude Desktop e CLI: mesma cozinha, utensílios diferentes**

## O “Pulo do Gato”

A versão Desktop usa o mesmo motor do CLI, mas com interface gráfica. É como cozinhar a mesma receita usando painel digital em vez de fogão antigo.

## Desenvolvimento

O texto-base explica que o Desktop roda o mesmo mecanismo do Claude Code CLI, mas com uma interface visual.

A versão CLI é usada pelo terminal. A versão Desktop oferece uma experiência mais visual, com:

* editor de arquivos;
* diff view;
* terminal integrado;
* organização de painéis;
* sessões paralelas;
* preview;
* revisão gráfica.

Ambas podem compartilhar configurações, como:

* arquivos `CLAUDE.md`;
* servidores MCP;
* hooks;
* skills;
* settings.

Para estudantes iniciantes, a interface Desktop tende a ser mais acolhedora porque torna visível o que está acontecendo.

Por outro lado, aprender CLI continua útil, especialmente para áreas como:

* computação;
* engenharia elétrica;
* automação;
* dados;
* sistemas embarcados;
* DevOps;
* robótica.

> **Resumo “Para Leigos”:**
> Desktop é mais visual. CLI é mais direto. Os dois conversam com o mesmo “cérebro”.

## Pílula Hands-on — 2 minutos

Complete:

```text
Eu usaria Desktop quando:
Eu usaria CLI quando:
```

Exemplo:

```text
Eu usaria Desktop quando quiser revisar mudanças visualmente.
Eu usaria CLI quando precisar executar comandos rápidos no terminal.
```

---

# Módulo 20 — **Boas práticas: IA ajuda, mas o diploma ainda é seu**

## O “Pulo do Gato”

Claude Code é uma ferramenta de apoio. Ele pode acelerar, explicar e revisar, mas o estudante precisa entender o que entrega.

## Desenvolvimento

Em cursos de Engenharia, é fundamental usar IA com responsabilidade acadêmica.

Boas práticas:

### 1. Peça explicação, não apenas resposta

Em vez de:

```text
Faça meu trabalho.
```

Prefira:

```text
Explique o caminho para resolver este problema e mostre um exemplo semelhante.
```

### 2. Revise tudo antes de entregar

Código gerado por IA pode conter erros, exageros ou soluções incompatíveis com o nível da disciplina.

### 3. Declare uso quando necessário

Se a disciplina exige transparência sobre uso de IA, registre como a ferramenta foi usada.

### 4. Não aceite o que não entende

Se Claude propôs uma solução avançada demais, peça uma versão mais simples:

```text
Refaça usando apenas conceitos de programação introdutória.
```

### 5. Use para aprender melhor

A melhor pergunta não é:

```text
Qual é a resposta?
```

A melhor pergunta é:

```text
Como eu posso chegar à resposta?
```

> **Bloco final de ouro:**
> A IA pode ser uma calculadora sofisticada, um monitor paciente e um revisor incansável. Mas quem precisa aprender a pensar como engenheiro é você.

## Pílula Hands-on — 2 minutos

Reescreva este pedido inadequado:

```text
Faça meu trabalho de programação.
```

Como pedido de aprendizagem:

```text
Me ajude a entender o problema, proponha um plano de solução e explique cada etapa antes de escrever qualquer código.
```

Agora escreva seu próprio compromisso:

```text
Eu vou usar IA para aprender, revisar e melhorar, não para entregar algo que eu não compreendo.
```

---

# Sequência Didática Recomendada

## Aula 1 — Primeiros passos

* Módulo 1: visão geral;
* Módulo 2: instalação e requisitos;
* Módulo 3: abas principais;
* Módulo 4: escolha do projeto.

**Atividade:** criar uma pasta de teste e escrever o primeiro prompt de análise.

---

## Aula 2 — Pedindo bem e revisando melhor

* Módulo 5: escolha do modelo;
* Módulo 6: engenharia de prompts;
* Módulo 7: revisão antes de aceitar;
* Módulo 8: interrupção e redirecionamento.

**Atividade:** transformar prompts ruins em prompts bons.

---

## Aula 3 — Trabalhando com arquivos e contexto

* Módulo 9: fornecimento de contexto;
* Módulo 10: modos de permissão;
* Módulo 11: diff view;
* Módulo 12: terminal integrado.

**Atividade:** analisar uma mudança fictícia em diff.

---

## Aula 4 — Recursos avançados sem trauma

* Módulo 13: preview;
* Módulo 14: skills;
* Módulo 15: plugins;
* Módulo 16: sessões paralelas.

**Atividade:** montar três sessões fictícias para um projeto acadêmico.

---

## Aula 5 — Fluxo profissional e uso responsável

* Módulo 17: pull requests e CI;
* Módulo 18: tarefas agendadas;
* Módulo 19: Desktop versus CLI;
* Módulo 20: boas práticas acadêmicas.

**Atividade:** escrever uma política pessoal de uso responsável da IA.

---

# Produto Final Esperado do Aluno

Ao final do curso, o estudante deverá ser capaz de:

* diferenciar Chat, Cowork e Code;
* escolher um projeto inicial seguro;
* escrever prompts claros para tarefas de programação;
* revisar mudanças antes de aceitar;
* interpretar uma diff view simples;
* pedir explicações adequadas ao seu nível;
* usar IA como apoio à aprendizagem, não como substituta do raciocínio;
* compreender a função de modelos, permissões, terminal, preview, sessões e plugins;
* aplicar boas práticas de responsabilidade acadêmica.

---

# Checklist de Aprendizagem

Use este checklist ao final do curso:

* [ ] Sei explicar o que é o Claude Code Desktop.
* [ ] Sei a diferença entre Chat, Cowork e Code.
* [ ] Sei escolher uma pasta de projeto segura para começar.
* [ ] Sei escrever um prompt claro.
* [ ] Sei pedir para Claude não alterar arquivos sem autorização.
* [ ] Sei revisar uma mudança em diff view.
* [ ] Sei interromper e redirecionar uma tarefa.
* [ ] Sei dar contexto usando arquivos, descrições e objetivos.
* [ ] Sei diferenciar modos de permissão.
* [ ] Sei usar IA de forma ética e responsável em contexto acadêmico.

---

# Encerramento do Curso

O Claude Code Desktop deve ser apresentado aos estudantes como uma ferramenta de **aprendizagem assistida**, não como uma máquina mágica de entregar trabalhos.

A melhor forma de usá-lo é como se fosse um monitor paciente, que pode explicar, sugerir, comparar, revisar e testar. Mas o papel central continua sendo do estudante: perguntar bem, revisar com atenção e compreender antes de aceitar.

> **Mensagem final:**
> Na Engenharia, ferramenta boa não substitui raciocínio. Ela amplia a capacidade de quem sabe perguntar, testar e revisar.