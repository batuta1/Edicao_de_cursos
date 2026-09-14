# Relatório de Roteiro de Curso

## Platforms and Integrations: Use Claude Code in VS Code

### Público-alvo: Docentes e discentes dos anos iniciais da graduação em Engenharia

---

## Apresentação Geral do Curso

Este curso apresenta, de forma prática e acessível, como utilizar o **Claude Code dentro do Visual Studio Code (VS Code)** para apoiar atividades de programação, revisão de código, organização de projetos, estudo de arquivos e automação de tarefas simples.

A proposta é que docentes e estudantes de Engenharia compreendam o Claude Code como um **assistente de bancada digital**: ele não substitui o raciocínio do aluno, nem o trabalho do professor, mas ajuda a organizar ideias, revisar códigos, explicar erros, sugerir melhorias e acelerar tarefas repetitivas.

> **Ideia central do curso:**
> Usar o Claude Code no VS Code é como ter um monitor de laboratório sentado ao lado: ele pode explicar, revisar, sugerir e ajudar, mas quem decide e aprende é sempre o estudante.

---

# Módulo 1 — “O Assistente que Mora Dentro do VS Code”

## O “Pulo do Gato”

O Claude Code no VS Code é uma extensão que coloca um assistente de IA diretamente dentro do ambiente de programação. Em vez de copiar código para outro site, o estudante conversa com o Claude no mesmo lugar onde escreve, testa e organiza seus arquivos.

É como trocar aquela cena clássica de “professor, olha meu código aqui rapidinho?” por uma ajuda digital sempre disponível — com a diferença de que o aluno ainda precisa pensar, revisar e decidir.

## Desenvolvimento

O VS Code é um dos ambientes mais usados por estudantes e profissionais para escrever código. A extensão do Claude Code permite que o usuário:

* converse com a IA sem sair do editor;
* peça explicações sobre trechos de código;
* solicite sugestões de melhoria;
* revise mudanças antes de aplicá-las;
* use referências diretas a arquivos e linhas;
* organize múltiplas conversas sobre tarefas diferentes.

Para estudantes dos anos iniciais da Engenharia, isso é especialmente útil porque muitos ainda estão aprendendo a lidar com:

* erros de sintaxe;
* organização de arquivos;
* lógica de programação;
* mensagens do terminal;
* leitura de códigos de exemplo;
* boas práticas de escrita técnica.

Para docentes, a ferramenta pode apoiar:

* criação de exemplos didáticos;
* revisão de atividades;
* explicação de códigos para diferentes níveis de turma;
* preparação de roteiros de laboratório;
* análise de erros recorrentes dos estudantes.

> **Atenção pedagógica:**
> O Claude Code deve ser usado como apoio ao raciocínio, não como atalho para “entregar a resposta pronta”. O estudante precisa aprender a perguntar, interpretar, testar e revisar.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

1. Abra um bloco de notas, editor de texto ou app de anotações.
2. Escreva a frase:
   **“Claude Code é um assistente integrado ao VS Code.”**
3. Agora reescreva essa frase como se fosse explicar para um colega do primeiro semestre.
4. Compare as duas versões.

**Exemplo esperado:**

> “Claude Code é uma ferramenta que fica dentro do VS Code e ajuda a entender, revisar e melhorar códigos.”

---

# Módulo 2 — “Antes de Começar: A Lista do Mercado”

## O “Pulo do Gato”

Antes de usar o Claude Code, é preciso garantir que a “cozinha” esteja montada: VS Code instalado, versão compatível e uma conta Anthropic para login.

É como tentar fazer uma aula de laboratório sem bancada, tomada e equipamentos. A ideia pode ser ótima, mas primeiro precisamos preparar o ambiente.

## Desenvolvimento

Para usar o Claude Code no VS Code, o estudante ou docente precisa verificar alguns pré-requisitos básicos:

* **VS Code versão 1.98.0 ou superior**;
* **conta Anthropic** para realizar o login;
* conexão com a internet;
* um computador com VS Code instalado;
* permissão para instalar extensões.

A extensão já inclui a interface gráfica principal e também permite acesso à CLI pelo terminal integrado do VS Code, caso o usuário avance para recursos mais técnicos.

Para turmas iniciais, recomenda-se começar pela interface gráfica, porque ela é mais visual e menos intimidadora. A CLI pode ser apresentada depois, quando os estudantes já estiverem mais familiarizados com terminal, comandos e fluxos de programação.

> **Analogia de sala de aula:**
> A extensão é como uma calculadora científica. Antes de resolver integrais, é preciso ligar, configurar e saber onde ficam as funções principais.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Faça uma pequena checklist pessoal:

```markdown
## Minha preparação para usar Claude Code

- [ ] Tenho VS Code instalado?
- [ ] Sei verificar a versão do VS Code?
- [ ] Tenho uma conta Anthropic?
- [ ] Sei abrir a aba de extensões?
- [ ] Sei abrir a paleta de comandos?
```

Depois, marque o que você já sabe fazer.

---

# Módulo 3 — “Instalando a Extensão sem Drama”

## O “Pulo do Gato”

Instalar o Claude Code é parecido com instalar um aplicativo no celular: você procura, clica em instalar e depois abre para configurar. A diferença é que, no VS Code, chamamos esses aplicativos de **extensões**.

## Desenvolvimento

A instalação pode ser feita pela área de extensões do VS Code:

1. Abrir o VS Code.
2. Clicar na aba de extensões.
3. Pesquisar por **Claude Code**.
4. Selecionar a extensão correta.
5. Clicar em **Install**.
6. Reiniciar ou recarregar a janela se a extensão não aparecer.

No Windows e Linux, o atalho comum para abrir extensões é:

```text
Ctrl + Shift + X
```

No Mac:

```text
Cmd + Shift + X
```

Caso a extensão não apareça após a instalação, o usuário pode usar a Paleta de Comandos e executar:

```text
Developer: Reload Window
```

Esse procedimento é útil em laboratório, porque muitas vezes o estudante instala corretamente, mas o VS Code ainda não atualizou a interface.

> **Dica “Para Leigos”:**
> Se instalou e não apareceu, não entre em pânico. Às vezes o VS Code só precisa de um “cafezinho”: recarregar a janela resolve boa parte dos casos.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Mesmo sem instalar nada agora, escreva em ordem os passos da instalação:

```markdown
## Como instalar Claude Code no VS Code

1. Abrir o VS Code.
2. Ir em Extensões.
3. Pesquisar "Claude Code".
4. Clicar em Instalar.
5. Recarregar a janela se necessário.
```

Agora explique esses passos em voz alta como se estivesse ajudando um colega.

---

# Módulo 4 — “Abrindo o Painel: Onde Está o Claude?”

## O “Pulo do Gato”

Depois de instalado, o Claude Code aparece como um ícone de brilho, chamado **Spark icon**. Esse ícone é a porta de entrada para conversar com o assistente.

É como encontrar o botão certo no painel de um equipamento de laboratório: depois que você sabe onde está, tudo fica mais simples.

## Desenvolvimento

O Claude Code pode ser aberto de diferentes formas dentro do VS Code:

* pelo ícone **Spark** na barra superior do editor;
* pela barra lateral de atividades;
* pela barra de status, no canto inferior direito;
* pela Paleta de Comandos;
* abrindo uma nova aba de conversa.

O ícone na barra do editor aparece quando há um arquivo aberto. Isso é importante: se o estudante só abriu uma pasta vazia, talvez não veja o ícone imediatamente.

A Paleta de Comandos também é uma alternativa muito útil. Os atalhos são:

```text
Ctrl + Shift + P
```

no Windows/Linux, ou:

```text
Cmd + Shift + P
```

no Mac.

Depois, basta digitar:

```text
Claude Code
```

e escolher uma das opções disponíveis.

> **Dica didática:**
> Ensine os alunos a usar a Paleta de Comandos desde cedo. Ela funciona como a “barra de pesquisa universal” do VS Code.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Crie um mini-mapa de acesso:

```markdown
## Formas de abrir Claude Code

- Ícone Spark no editor
- Ícone Spark na barra lateral
- Barra de status
- Paleta de Comandos
- Nova aba de conversa
```

Depois, destaque qual forma você acha mais fácil para um estudante iniciante.

---

# Módulo 5 — “Login: A Catraca da Biblioteca Digital”

## O “Pulo do Gato”

Na primeira vez que abrir o Claude Code, será necessário fazer login. Pense nisso como passar pela catraca da biblioteca: depois que você entra, pode consultar o acervo.

## Desenvolvimento

Ao abrir o painel do Claude Code pela primeira vez, aparece uma tela de autenticação. O usuário deve clicar em **Sign in** e concluir a autorização no navegador.

Se aparecer a mensagem:

```text
Not logged in · Please run /login
```

isso significa que o Claude Code não reconheceu a sessão. Nesse caso, pode ser necessário recarregar a janela do VS Code ou fazer login novamente.

Também pode acontecer de o usuário ter uma chave de API configurada no terminal, mas o VS Code não reconhecer essa variável de ambiente. Para iniciantes, o caminho mais simples geralmente é fazer login com a conta Claude diretamente pela interface.

Depois do login, pode aparecer uma checklist de aprendizagem chamada **Learn Claude Code**, com passos guiados.

> **Analogia de sala de aula:**
> O login é como assinar a lista de presença. Sem isso, o sistema não sabe quem está usando e não libera a atividade.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Responda em uma frase:

```markdown
Por que o login é necessário antes de usar Claude Code?
```

Sugestão de resposta:

> Porque o Claude Code precisa identificar minha conta para liberar o uso da ferramenta dentro do VS Code.

---

# Módulo 6 — “Primeira Conversa: Perguntar Bem é Metade da Aula”

## O “Pulo do Gato”

O Claude Code responde melhor quando o estudante faz perguntas claras. Perguntar “me ajuda?” é vago. Perguntar “explique este erro de Python para um aluno iniciante” é muito melhor.

É como perguntar ao professor: “não entendi nada” versus “não entendi por que essa variável mudou de valor no laço”.

## Desenvolvimento

Depois de abrir o painel, o usuário pode enviar prompts para o Claude Code. Alguns usos iniciais recomendados são:

* explicar um trecho de código;
* localizar um erro;
* sugerir melhorias;
* transformar um código confuso em uma versão mais legível;
* comentar uma função;
* criar exemplos didáticos;
* revisar uma atividade de programação.

Exemplos de bons prompts:

```text
Explique este código como se eu estivesse no primeiro semestre de Engenharia.
```

```text
Encontre possíveis erros neste trecho e explique sem corrigir automaticamente.
```

```text
Sugira comentários para este código, mas mantenha a lógica original.
```

```text
Crie uma explicação curta sobre este algoritmo usando uma analogia do cotidiano.
```

Para docentes, exemplos úteis são:

```text
Transforme este código em uma atividade guiada para estudantes iniciantes.
```

```text
Crie três perguntas de verificação de aprendizagem sobre este exemplo.
```

> **Regra de ouro:**
> Quanto mais claro for o pedido, melhor será a resposta. O prompt é o enunciado da atividade.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Transforme o pedido vago abaixo em um pedido melhor:

```text
Me explica esse código.
```

Exemplo de versão melhor:

```text
Explique este código passo a passo para um estudante do primeiro semestre de Engenharia, destacando variáveis, entrada, processamento e saída.
```

---

# Módulo 7 — “Selecionar Código: Apontar o Trecho Certo”

## O “Pulo do Gato”

O Claude Code consegue enxergar o texto selecionado no editor. Isso permite que o aluno mostre exatamente qual parte do código quer discutir.

É como apontar no quadro e dizer: “professor, minha dúvida está aqui”.

## Desenvolvimento

Quando o usuário seleciona um trecho no VS Code, o Claude pode usar essa seleção como contexto. Isso é muito útil porque evita perguntas genéricas.

Além disso, o usuário pode inserir uma referência com arquivo e linhas usando:

```text
Alt + K
```

no Windows/Linux, ou:

```text
Option + K
```

no Mac.

Esse comando cria uma referência do tipo:

```text
@arquivo.ts#5-10
```

Isso significa que o Claude saberá que a pergunta se refere ao arquivo indicado e às linhas selecionadas.

Esse recurso é excelente para:

* explicar um erro em uma linha específica;
* revisar uma função;
* comparar duas soluções;
* pedir comentários em um trecho;
* discutir uma parte de um algoritmo.

> **Dica para estudantes:**
> Não mande o projeto inteiro se a dúvida está em cinco linhas. Mostre o trecho certo. Isso economiza tempo e melhora a resposta.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Imagine que você tem este código:

```python
x = 10
y = 0
print(x / y)
```

Escreva um prompt específico para pedir ajuda:

```text
Explique por que o código abaixo gera erro e como eu posso entender esse problema sem apenas copiar a correção.
```

---

# Módulo 8 — “@-Mentions: Chamando Arquivos pelo Nome”

## O “Pulo do Gato”

As @-mentions permitem chamar arquivos e pastas para a conversa. É como dizer: “Claude, abra este caderno aqui e olhe esta página comigo”.

## Desenvolvimento

No Claude Code, o usuário pode digitar `@` seguido do nome de um arquivo ou pasta. O sistema faz uma busca aproximada, ou seja, não é necessário digitar o nome perfeitamente.

Exemplos:

```text
Explique a lógica em @auth
```

```text
O que existe dentro de @src/components/?
```

```text
Revise a função principal em @main.py
```

Para estudantes, esse recurso é muito útil quando o projeto começa a ter vários arquivos. Em disciplinas de programação, circuitos computacionais, modelagem ou simulação, é comum o aluno se perder entre arquivos como:

* `main.py`;
* `utils.py`;
* `dados.csv`;
* `calculos.py`;
* `app.js`;
* `README.md`.

Com as @-mentions, ele consegue direcionar a conversa para o arquivo certo.

> **Cuidado importante:**
> Quanto mais arquivos você adiciona ao contexto, mais informação o Claude precisa considerar. Para dúvidas simples, escolha poucos arquivos.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Crie três exemplos de perguntas usando `@`:

```text
Explique @main.py para um iniciante.
```

```text
Mostre o papel de @dados.csv neste projeto.
```

```text
Revise a organização de @src/
```

Agora escolha qual dessas perguntas seria mais útil para uma aula prática.

---

# Módulo 9 — “Plano Antes da Obra: O Modo Plan”

## O “Pulo do Gato”

O **Plan mode** faz o Claude explicar o que pretende fazer antes de modificar arquivos. É como pedir ao pedreiro para mostrar a planta antes de quebrar a parede.

## Desenvolvimento

No Claude Code, existem modos de permissão. Um dos mais importantes para ensino é o **Plan mode**.

Nesse modo, o Claude:

1. analisa o pedido;
2. propõe um plano;
3. espera aprovação;
4. só depois executa mudanças.

Isso é valioso pedagogicamente porque ensina o estudante a pensar antes de fazer. Em vez de aceitar alterações automaticamente, ele aprende a avaliar:

* o que será modificado;
* por que será modificado;
* se a estratégia faz sentido;
* quais riscos existem;
* se a solução respeita o objetivo da atividade.

Para docentes, o modo Plan é uma ótima forma de treinar pensamento computacional, pois transforma a IA em uma ferramenta de planejamento, não apenas de execução.

> **Mensagem-chave:**
> Antes de pedir “faça”, peça “explique o plano”. Isso reduz erros e aumenta aprendizagem.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Reescreva este pedido:

```text
Corrija meu código.
```

Como um pedido em modo planejamento:

```text
Antes de corrigir, explique qual é o problema, proponha um plano de correção em três passos e aguarde minha aprovação.
```

---

# Módulo 10 — “Diferenças Lado a Lado: Revisar Antes de Aceitar”

## O “Pulo do Gato”

Quando o Claude sugere alterações, o VS Code pode mostrar um comparativo entre o arquivo original e a versão proposta. Isso se chama **diff**.

É como corrigir uma redação vendo o “antes” e o “depois” lado a lado.

## Desenvolvimento

O recurso de revisão de mudanças é uma das partes mais importantes para uso responsável da IA.

Quando Claude propõe editar um arquivo, o usuário pode:

* aceitar a mudança;
* rejeitar a mudança;
* editar manualmente antes de aceitar;
* pedir uma nova versão;
* perguntar por que aquela alteração foi sugerida.

Para estudantes, isso evita o erro comum de aceitar tudo sem entender. Para docentes, permite criar atividades em que o aluno precisa justificar se aceitaria ou não determinada modificação.

Esse processo desenvolve competências importantes:

* leitura crítica de código;
* interpretação de diferenças;
* validação de soluções;
* autonomia técnica;
* responsabilidade acadêmica.

> **Regra de segurança:**
> Nunca aceite mudanças importantes sem revisar. A IA pode ajudar, mas a responsabilidade final é humana.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Compare mentalmente as duas versões:

**Antes:**

```python
media = soma / total
```

**Depois:**

```python
media = soma / len(notas)
```

Responda:

```markdown
1. O que mudou?
2. A mudança faz sentido?
3. Que pergunta eu faria ao Claude antes de aceitar?
```

Sugestão de pergunta:

```text
Explique por que você trocou total por len(notas) e em que casos isso pode dar erro.
```

---

# Módulo 11 — “Auto-Accept: O Piloto Automático com Cinto de Segurança”

## O “Pulo do Gato”

O modo **auto-accept** permite que Claude aplique edições automaticamente. Isso é rápido, mas exige cuidado.

É como colocar o carro no piloto automático: pode ajudar, mas não é hora de tirar as mãos da direção.

## Desenvolvimento

O Claude Code permite alternar modos de permissão. No modo normal, ele pede autorização antes de cada ação. No modo auto-accept, ele pode aplicar edições sem perguntar a cada passo.

Esse recurso pode ser útil quando:

* o projeto está em ambiente de teste;
* o usuário já revisou o plano;
* as mudanças são pequenas;
* o código está versionado com Git;
* a atividade não envolve arquivos sensíveis.

Para estudantes iniciantes, recomenda-se evitar auto-accept no começo. O ideal é usar primeiro o modo normal ou o modo Plan.

Em laboratório didático, o professor pode propor uma regra simples:

> **Para aprender:** use revisão manual.
> **Para automatizar tarefas repetitivas:** use auto-accept com cuidado.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Classifique as situações:

```markdown
## Usaria auto-accept?

1. Corrigir nome de variável em 20 arquivos.
2. Alterar cálculo principal de uma atividade avaliativa.
3. Formatar comentários de um código simples.
4. Apagar arquivos antigos de um projeto.
```

Sugestão:

* 1: talvez sim, com Git.
* 2: não.
* 3: talvez sim.
* 4: não, sem revisão cuidadosa.

---

# Módulo 12 — “Histórico de Conversas: O Caderno que Não Some”

## O “Pulo do Gato”

O Claude Code mantém histórico de conversas. Isso permite continuar uma tarefa depois, sem começar do zero.

É como guardar o caderno de laboratório com todas as anotações do experimento.

## Desenvolvimento

A extensão possui uma área de **Session history**, onde o usuário pode:

* buscar conversas anteriores;
* continuar uma conversa;
* localizar sessões por data;
* renomear sessões;
* remover sessões antigas.

Isso é muito útil em projetos acadêmicos, especialmente quando a atividade dura mais de uma aula.

Exemplos:

* uma prática de Python em duas semanas;
* um projeto de Arduino;
* uma simulação numérica;
* um relatório técnico;
* uma atividade de modelagem computacional;
* uma revisão de código em grupo.

Para docentes, uma orientação interessante é pedir que os estudantes nomeiem suas sessões de forma organizada:

```text
Aula 03 - Revisão de laços em Python
```

```text
Projeto Final - Simulação de circuito RC
```

```text
Erro no código de regressão linear
```

> **Boa prática:**
> Nomear conversas ajuda o estudante a transformar a IA em ferramenta de estudo, não em bagunça digital.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Crie três nomes bons para sessões de estudo:

```markdown
1. Aula 01 - Primeiros comandos em Python
2. Projeto Ponte - Cálculo de esforços
3. Laboratório 02 - Erro no gráfico de dados
```

Agora crie um nome ruim e explique por que ele atrapalha.

Exemplo ruim:

```text
coisa do código
```

---

# Módulo 13 — “Várias Conversas: Cada Problema no Seu Caderno”

## O “Pulo do Gato”

O Claude Code permite abrir múltiplas conversas. Isso ajuda a separar assuntos diferentes.

É como ter um caderno para Cálculo, outro para Física e outro para Programação — misturar tudo em um só vira confusão.

## Desenvolvimento

No VS Code, o usuário pode abrir Claude em nova aba ou nova janela. Cada conversa mantém seu próprio histórico e contexto.

Isso é útil quando o estudante está trabalhando em tarefas paralelas, por exemplo:

* uma conversa para explicar teoria;
* outra para revisar código;
* outra para organizar README;
* outra para depurar erros;
* outra para gerar exemplos de teste.

Para docentes, isso pode apoiar o planejamento de aulas:

* uma sessão para roteiro de aula;
* uma sessão para exemplos de código;
* uma sessão para rubrica de avaliação;
* uma sessão para adaptação de linguagem para alunos iniciantes.

> **Dica de organização:**
> Uma conversa deve ter um objetivo claro. Se mudou de assunto, talvez seja melhor abrir nova sessão.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Organize estes temas em conversas separadas:

```markdown
- Erro no código Python
- Explicação sobre matrizes
- Preparação de relatório
- Criação de exercícios
```

Sugestão:

```markdown
Sessão 1: Debug do código Python  
Sessão 2: Teoria de matrizes  
Sessão 3: Relatório técnico  
Sessão 4: Exercícios para revisão  
```

---

# Módulo 14 — “Prompt Box: A Mesa de Controle”

## O “Pulo do Gato”

A caixa de prompt é onde o usuário conversa com o Claude Code. Ela também dá acesso a comandos, arquivos, modo de permissão, contexto e opções avançadas.

É como a mesa de controle de um laboratório: parece simples, mas tem muitos botões úteis.

## Desenvolvimento

A caixa de prompt possui recursos importantes:

* escrever mensagens;
* inserir múltiplas linhas com `Shift + Enter`;
* abrir comandos digitando `/`;
* anexar arquivos;
* alternar modos de permissão;
* verificar uso de contexto;
* ativar pensamento estendido;
* usar comandos como `/compact`;
* iniciar sessões remotas;
* acessar plugins, permissões e configurações.

Para iniciantes, vale apresentar primeiro apenas quatro elementos:

1. onde digitar;
2. como enviar;
3. como escrever em múltiplas linhas;
4. como chamar comandos com `/`.

Aos poucos, podem ser introduzidos recursos mais avançados, como contexto, compactação e pensamento estendido.

> **Analogia simples:**
> O prompt box é o balcão de atendimento. Quanto mais claro for o pedido, melhor será o serviço.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Escreva um prompt em três linhas:

```text
Explique este código para um iniciante.

Depois, aponte possíveis erros.

Por fim, sugira uma melhoria simples.
```

Agora observe: um prompt em blocos ajuda a organizar melhor o pedido.

---

# Módulo 15 — “Comandos com Barra: O Cardápio Secreto”

## O “Pulo do Gato”

Ao digitar `/`, o Claude Code abre um menu de comandos. Esse menu funciona como um cardápio: você escolhe a ação que deseja.

## Desenvolvimento

O menu com `/` permite acessar recursos como:

* anexar arquivos;
* trocar modelo;
* ativar pensamento estendido;
* consultar uso com `/usage`;
* usar `/compact`;
* configurar plugins;
* acessar permissões;
* abrir opções de personalização;
* iniciar controle remoto com `/remote-control`.

Para estudantes iniciantes, o mais importante é entender que `/` não é uma pergunta comum. É um comando para abrir opções da ferramenta.

Em uma disciplina introdutória, o professor pode propor uma atividade simples:

> “Digite `/`, observe as opções e identifique três comandos que parecem úteis para estudar programação.”

Isso transforma o uso da ferramenta em aprendizagem ativa.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Imagine que você abriu o menu `/`. Complete:

```markdown
Três comandos que eu gostaria de explorar:

1. 
2. 
3. 
```

Depois, escreva por que um deles poderia ajudar em uma aula prática.

---

# Módulo 16 — “Contexto: A Mochila de Informações”

## O “Pulo do Gato”

O Claude Code trabalha melhor quando recebe contexto suficiente, mas contexto demais pode virar mochila pesada.

É como levar material para aula: se levar só uma caneta, falta coisa; se levar a biblioteca inteira, fica impossível encontrar o que importa.

## Desenvolvimento

A caixa de prompt mostra quanto da janela de contexto está sendo usada. O contexto é o conjunto de informações que Claude considera na conversa:

* mensagens anteriores;
* arquivos mencionados;
* trechos selecionados;
* anexos;
* instruções;
* histórico da sessão.

Quando o contexto fica grande, Claude pode compactar automaticamente. O usuário também pode usar:

```text
/compact
```

A compactação ajuda a resumir a conversa para continuar trabalhando sem carregar tudo literalmente.

Para estudantes, a ideia principal é:

* envie o necessário;
* evite excesso;
* seja específico;
* selecione arquivos relevantes;
* resuma o objetivo antes de continuar.

> **Dica “Para Leigos”:**
> Contexto é como dar pistas. Poucas pistas confundem. Pistas demais também.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Escolha qual prompt tem melhor contexto:

**Opção A:**

```text
Meu código não funciona.
```

**Opção B:**

```text
Estou estudando laços em Python. O programa deveria somar os números de uma lista, mas o resultado está errado. Explique o problema passo a passo.
```

Resposta esperada: **Opção B**, porque oferece contexto.

---

# Módulo 17 — “Pensamento Estendido: Quando o Problema Merece Café Forte”

## O “Pulo do Gato”

O modo de **extended thinking** permite que Claude gaste mais tempo raciocinando em problemas complexos.

É como pedir ao monitor: “não responda correndo; pense com calma porque esse problema é cabeludo”.

## Desenvolvimento

O pensamento estendido é útil quando a tarefa exige análise mais profunda, como:

* depurar erro difícil;
* planejar arquitetura de projeto;
* comparar estratégias;
* revisar vários arquivos;
* estruturar uma atividade complexa;
* explicar um algoritmo passo a passo.

Na interface, o raciocínio aparece em blocos recolhidos, que podem ser abertos pelo usuário.

Para turmas iniciais, o recurso deve ser usado com moderação. Nem toda pergunta precisa de raciocínio estendido. Para dúvidas simples, um prompt claro já resolve.

Exemplo de uso adequado:

```text
Analise este projeto com calma. Primeiro identifique a estrutura dos arquivos, depois explique o fluxo principal e só então sugira melhorias.
```

> **Resumo pedagógico:**
> Use pensamento estendido para problemas difíceis, não para perguntar “qual é o atalho para abrir o terminal”.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Classifique:

```markdown
## Precisa de pensamento estendido?

1. Explicar o que é uma variável.
2. Encontrar erro em um projeto com cinco arquivos.
3. Criar um plano de refatoração.
4. Dizer o atalho para abrir a Paleta de Comandos.
```

Sugestão:

* 1: não.
* 2: sim.
* 3: sim.
* 4: não.

---

# Módulo 18 — “Terminal ou Painel Gráfico: Duas Portas para a Mesma Sala”

## O “Pulo do Gato”

O Claude Code pode ser usado pela interface gráfica do VS Code ou pelo terminal. A interface gráfica é mais amigável; o terminal é mais poderoso para usuários avançados.

É como resolver conta na calculadora ou no quadro: os dois funcionam, mas cada um tem seu momento.

## Desenvolvimento

Por padrão, a extensão abre um painel gráfico de conversa. Essa opção é recomendada para iniciantes porque:

* mostra botões;
* facilita revisão de mudanças;
* deixa a interação mais visual;
* reduz a barreira do terminal.

Também é possível usar o modo terminal dentro do VS Code, executando:

```text
claude
```

no terminal integrado.

O terminal pode ser útil para:

* usuários avançados;
* integração com comandos;
* uso de recursos da CLI;
* retomada de conversas com `claude --resume`;
* workflows com Git;
* tarefas com worktrees.

Para uma turma de Engenharia em anos iniciais, recomenda-se a seguinte progressão:

1. começar pela interface gráfica;
2. aprender prompts e revisão de diffs;
3. conhecer o terminal integrado;
4. usar a CLI em tarefas mais avançadas.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Complete a tabela:

```markdown
| Forma de uso | Melhor para |
|---|---|
| Painel gráfico | Iniciantes, revisão visual, uso didático |
| Terminal/CLI | Usuários avançados, comandos, automação |
```

Agora escreva qual você usaria no primeiro dia de aula e por quê.

---

# Módulo 19 — “Plugins: A Caixa de Ferramentas Extra”

## O “Pulo do Gato”

Plugins adicionam novas capacidades ao Claude Code. Pense neles como acessórios de uma maleta de ferramentas: você não usa todos sempre, mas alguns resolvem problemas específicos.

## Desenvolvimento

A extensão do Claude Code permite gerenciar plugins pela interface. Digitando:

```text
/plugins
```

o usuário abre a área de gerenciamento.

Nela, é possível:

* ver plugins instalados;
* ativar ou desativar plugins;
* buscar plugins disponíveis;
* instalar novos plugins;
* escolher escopo de instalação;
* gerenciar marketplaces.

Os escopos de instalação podem ser:

* **para o usuário**;
* **para o projeto**;
* **localmente no repositório**.

Para estudantes iniciantes, o mais importante é compreender que plugins devem ser usados com propósito. Não é necessário instalar tudo. Em um curso introdutório, o professor pode apresentar plugins apenas quando houver uma necessidade concreta.

> **Dica de segurança:**
> Antes de instalar um plugin, entenda para que ele serve e se é confiável. Ferramenta demais também atrapalha.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Responda:

```markdown
Se eu pudesse instalar um plugin para me ajudar em Engenharia, ele deveria fazer o quê?
```

Exemplos:

* ajudar a revisar código Python;
* organizar documentação;
* conectar com GitHub;
* analisar erros de terminal;
* apoiar escrita de relatórios técnicos.

---

# Módulo 20 — “Claude com Chrome: Testando Aplicações Web”

## O “Pulo do Gato”

Claude Code pode se conectar ao Chrome para testar páginas, verificar erros no console e interagir com aplicações web.

É como pedir a um colega para abrir o site, clicar nos botões e dizer se algo quebrou.

## Desenvolvimento

Com a extensão adequada no Chrome, o usuário pode usar:

```text
@browser
```

no prompt para pedir tarefas relacionadas ao navegador.

Exemplo:

```text
@browser go to localhost:3000 and check the console for errors
```

Isso é útil em projetos de:

* desenvolvimento web;
* interfaces de usuário;
* dashboards;
* simulações online;
* formulários;
* páginas de laboratório;
* aplicações didáticas.

Para alunos iniciantes, o conceito principal é entender que o Claude pode observar e auxiliar em testes de uma aplicação aberta no navegador, mas sempre com autorização e configuração apropriadas.

> **Analogia simples:**
> O navegador é a bancada de teste. O Claude observa o experimento e ajuda a identificar falhas.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Imagine que você criou uma página simples com botão. Escreva um pedido para Claude testar:

```text
@browser abra minha página local, clique no botão principal e verifique se aparece alguma mensagem de erro no console.
```

Agora adapte esse pedido para uma página de formulário.

---

# Módulo 21 — “Atalhos: Pequenas Teclas, Grandes Economias”

## O “Pulo do Gato”

Atalhos são como caminhos mais curtos dentro do campus: no começo parecem difíceis, depois economizam muito tempo.

## Desenvolvimento

Alguns atalhos importantes do Claude Code no VS Code são:

```text
Ctrl + Esc
```

ou, no Mac:

```text
Cmd + Esc
```

Para alternar foco entre editor e Claude.

```text
Alt + K
```

ou, no Mac:

```text
Option + K
```

Para inserir referência com @-mention da seleção atual.

```text
Ctrl + Shift + Esc
```

ou, no Mac:

```text
Cmd + Shift + Esc
```

Para abrir nova conversa em aba.

Além disso, a Paleta de Comandos continua sendo essencial:

```text
Ctrl + Shift + P
```

ou:

```text
Cmd + Shift + P
```

Para estudantes, o objetivo não é decorar tudo no primeiro dia. O ideal é começar com dois ou três atalhos e usá-los repetidamente.

> **Dica pedagógica:**
> Atalho bom é aquele que você realmente usa. Não precisa decorar a lista inteira.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Escolha dois atalhos para memorizar:

```markdown
## Meus dois primeiros atalhos

1. Paleta de Comandos: Ctrl + Shift + P
2. Inserir @-mention: Alt + K
```

Agora escreva uma frase explicando para que serve cada um.

---

# Módulo 22 — “Configurações: Ajustando a Ferramenta ao Seu Jeito”

## O “Pulo do Gato”

As configurações permitem adaptar o Claude Code ao jeito de trabalhar do usuário. É como ajustar a altura da cadeira antes de começar uma aula longa no laboratório.

## Desenvolvimento

A extensão possui configurações próprias no VS Code. Algumas das mais importantes são:

* usar terminal ou painel gráfico;
* definir modo inicial de permissão;
* escolher local preferido do painel;
* ativar ou desativar autosave;
* usar Ctrl/Cmd + Enter para enviar;
* esconder ou mostrar onboarding;
* respeitar `.gitignore`;
* usar ambiente Python do projeto;
* configurar variáveis de ambiente.

Para iniciantes, as configurações mais relevantes são:

```markdown
- Local do painel
- Modo de permissão
- Autosave
- Envio com Enter ou Ctrl/Cmd + Enter
```

Para docentes, é interessante padronizar algumas configurações antes de uma aula prática, especialmente quando a turma usa laboratório institucional.

> **Boa prática:**
> Em ambiente de ensino, comece com permissões manuais. Assim os estudantes veem e analisam cada mudança.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Imagine que você vai configurar o Claude Code para uma turma iniciante. Complete:

```markdown
## Configuração recomendada para iniciantes

- Modo de permissão:
- Interface:
- Auto-accept:
- Revisão de mudanças:
```

Sugestão:

```markdown
- Modo de permissão: manual ou Plan mode
- Interface: painel gráfico
- Auto-accept: desligado
- Revisão de mudanças: obrigatória
```

---

# Módulo 23 — “Git com Claude: Diário de Bordo do Código”

## O “Pulo do Gato”

Git registra a história do projeto. Claude Code pode ajudar a resumir mudanças, criar commits e apoiar pull requests.

É como manter um diário de bordo do laboratório: quem fez o quê, quando e por quê.

## Desenvolvimento

O Claude Code pode ajudar em fluxos com Git, por exemplo:

```text
commit my changes with a descriptive message
```

```text
summarize the changes I've made to the auth module
```

```text
create a pr for this feature
```

Para estudantes iniciantes, o foco inicial deve ser compreender:

* o que mudou;
* por que mudou;
* como descrever a mudança;
* como evitar perder versões anteriores.

O Claude pode ajudar a escrever mensagens de commit mais claras, mas o estudante deve revisar se a mensagem realmente corresponde ao que foi feito.

Exemplo de mensagem ruim:

```text
arrumei coisas
```

Exemplo de mensagem melhor:

```text
Corrige cálculo da média e adiciona validação para lista vazia
```

> **Dica de formação profissional:**
> Saber explicar uma mudança de código é parte da competência de Engenharia.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Transforme a mensagem ruim em uma boa:

```text
mexi no código
```

Sugestão:

```text
Organiza função de cálculo e adiciona comentários explicativos para iniciantes
```

---

# Módulo 24 — “Checkpoints: O Botão de Voltar no Tempo”

## O “Pulo do Gato”

Checkpoints permitem voltar para um estado anterior do código ou da conversa. É como ter um botão “desfazer” mais organizado.

## Desenvolvimento

A extensão do Claude Code suporta checkpoints. Eles ajudam a controlar alterações feitas durante uma conversa.

O usuário pode:

* criar um novo ramo de conversa;
* voltar o código para um ponto anterior;
* bifurcar conversa e código;
* preservar histórico enquanto desfaz mudanças.

Isso é muito útil em atividades didáticas, porque o estudante pode experimentar sem tanto medo de errar.

Exemplos de uso:

* testar uma solução alternativa;
* comparar duas formas de resolver um problema;
* desfazer uma modificação ruim;
* criar uma versão experimental;
* voltar para antes de uma refatoração.

> **Analogia de sala:**
> Checkpoint é como salvar o jogo antes de enfrentar uma fase difícil.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Responda:

```markdown
Em que situação eu gostaria de ter um checkpoint?
```

Exemplo:

> Antes de aceitar uma grande alteração no código de um projeto final.

---

# Módulo 25 — “MCP: Conectando Claude a Outras Ferramentas”

## O “Pulo do Gato”

MCP é uma forma de conectar Claude Code a ferramentas externas, como APIs, bancos de dados e serviços.

É como dar ao assistente acesso a outros laboratórios do campus, desde que ele tenha autorização.

## Desenvolvimento

MCP significa **Model Context Protocol**. Ele permite que Claude Code interaja com ferramentas externas por meio de servidores configurados.

Exemplos de uso:

* consultar informações em serviços externos;
* revisar pull requests;
* acessar bancos de dados;
* integrar ferramentas de desenvolvimento;
* conectar sistemas internos de uma organização.

No VS Code, alguns aspectos do MCP podem ser gerenciados pela interface com:

```text
/mcp
```

Mas a configuração completa pode exigir terminal e comandos da CLI.

Para estudantes iniciantes, o objetivo não é configurar MCP no primeiro contato, mas entender o conceito:

> Claude pode ser conectado a ferramentas, mas isso exige cuidado, autorização e configuração.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Complete:

```markdown
Se eu pudesse conectar Claude Code a uma ferramenta externa para estudar Engenharia, eu conectaria a:
```

Exemplos:

* GitHub;
* planilha de dados;
* ambiente de simulação;
* sistema de exercícios;
* banco de questões.

---

# Módulo 26 — “Segurança e Privacidade: Não Entregue a Chave do Laboratório”

## O “Pulo do Gato”

Claude Code pode ler e sugerir alterações em arquivos. Por isso, segurança é essencial.

É como deixar alguém entrar no laboratório: pode ajudar, mas não deve ter acesso irrestrito a tudo.

## Desenvolvimento

Algumas práticas de segurança são fundamentais:

* revisar mudanças antes de aceitar;
* evitar auto-accept em projetos sensíveis;
* usar modo restrito do VS Code em códigos não confiáveis;
* não compartilhar segredos, senhas ou chaves privadas;
* respeitar políticas institucionais;
* verificar configurações antes de permitir ações automáticas;
* usar Git para recuperar versões anteriores.

A documentação também alerta que, com permissões automáticas, Claude Code pode modificar arquivos de configuração do VS Code, como `settings.json` ou `tasks.json`, que podem executar comportamentos automaticamente.

Para ensino, recomenda-se enfatizar:

> **IA não elimina responsabilidade.**
> O estudante continua responsável pelo código que entrega, executa e compartilha.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Classifique como seguro ou arriscado:

```markdown
1. Pedir explicação de um código simples.
2. Colar uma senha no prompt.
3. Revisar um diff antes de aceitar.
4. Ativar auto-accept em projeto desconhecido.
```

Sugestão:

* 1: seguro.
* 2: arriscado.
* 3: seguro.
* 4: arriscado.

---

# Módulo 27 — “Erros Comuns: Quando o Spark Some”

## O “Pulo do Gato”

Se o ícone do Claude não aparece, isso não significa que tudo deu errado. Muitas vezes falta abrir um arquivo, atualizar o VS Code ou recarregar a janela.

É como procurar o projetor ligado sem perceber que o cabo HDMI não foi conectado.

## Desenvolvimento

Problemas comuns incluem:

* extensão não aparece;
* ícone Spark não está visível;
* Claude não responde;
* login não funciona;
* VS Code está desatualizado;
* workspace está em modo restrito;
* há conflito com outra extensão;
* a janela precisa ser recarregada.

Soluções simples:

```markdown
1. Verificar versão do VS Code.
2. Abrir um arquivo.
3. Recarregar a janela.
4. Usar a Paleta de Comandos.
5. Conferir login.
6. Testar nova conversa.
7. Verificar conexão com internet.
```

Para docentes, é útil ter uma checklist de solução rápida para laboratórios, evitando que metade da aula seja consumida por problemas de instalação.

> **Dica “Para Leigos”:**
> Antes de declarar “não funciona”, faça a checklist básica. Muitas vezes o problema é só uma janela que precisa ser recarregada.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Crie sua própria checklist de emergência:

```markdown
## Se Claude Code não aparecer

- [ ] O VS Code está atualizado?
- [ ] Eu abri um arquivo?
- [ ] A extensão está instalada?
- [ ] Já recarreguei a janela?
- [ ] Estou logado?
- [ ] Tenho internet?
```

---

# Módulo 28 — “Usos Didáticos para Engenharia: Do Código ao Relatório”

## O “Pulo do Gato”

Claude Code não serve apenas para “fazer código”. Ele pode ajudar o estudante a entender, revisar, explicar e documentar soluções técnicas.

É como um monitor que ajuda tanto no cálculo quanto no relatório final.

## Desenvolvimento

Em cursos iniciais de Engenharia, o Claude Code pode ser usado em atividades como:

* introdução à programação;
* análise de algoritmos;
* simulações simples;
* leitura de arquivos de dados;
* documentação de projetos;
* interpretação de erros;
* construção de relatórios técnicos;
* organização de repositórios;
* revisão de README;
* comentários em código.

Exemplos de prompts didáticos:

```text
Explique este algoritmo usando uma analogia com uma fila de alunos.
```

```text
Crie comentários para este código sem alterar sua lógica.
```

```text
Transforme este código em um roteiro de prática de laboratório.
```

```text
Liste três erros comuns que alunos iniciantes poderiam cometer neste exercício.
```

Para docentes, a ferramenta pode apoiar a criação de:

* exercícios graduais;
* rubricas de avaliação;
* feedback formativo;
* exemplos alternativos;
* atividades mão na massa;
* desafios progressivos.

> **Importante:**
> O objetivo não é usar IA para pular etapas, mas para tornar as etapas mais visíveis e compreensíveis.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Escreva um prompt para transformar um código em atividade de aula:

```text
Transforme este código em uma atividade guiada para estudantes do primeiro semestre de Engenharia, com objetivo, passos e pergunta final de reflexão.
```

---

# Módulo 29 — “Boas Perguntas, Bons Resultados”

## O “Pulo do Gato”

Usar Claude Code bem é menos sobre “ter IA” e mais sobre saber formular boas perguntas.

É como em uma aula: o aluno que pergunta melhor geralmente aprende melhor.

## Desenvolvimento

Uma boa pergunta para Claude Code costuma ter seis componentes:

1. **Contexto:** o que estou fazendo?
2. **Objetivo:** o que quero alcançar?
3. **Trecho ou arquivo:** onde está o problema?
4. **Nível de explicação:** iniciante, intermediário ou avançado?
5. **Tipo de resposta:** explicação, plano, revisão, correção ou exemplo?
6. **Limite:** o que não deve ser feito?

Modelo de prompt:

```text
Estou estudando [tema]. Quero [objetivo]. Analise [arquivo/trecho]. Explique em nível [iniciante/intermediário]. Primeiro apresente o problema, depois sugira uma solução. Não altere o código ainda.
```

Exemplo:

```text
Estou estudando funções em Python. Quero entender por que minha função não retorna o valor esperado. Analise o trecho selecionado. Explique em nível iniciante. Primeiro apresente o problema, depois sugira uma correção. Não altere o código ainda.
```

> **Fórmula simples:**
> Contexto + objetivo + trecho + nível + formato + limite = prompt forte.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Complete o modelo:

```text
Estou estudando ________. Quero ________. Analise ________. Explique em nível ________. Primeiro ________. Não ________.
```

Exemplo preenchido:

```text
Estou estudando listas em Python. Quero entender por que meu loop não soma corretamente. Analise o trecho selecionado. Explique em nível iniciante. Primeiro mostre o erro conceitual. Não corrija automaticamente.
```

---

# Módulo 30 — “Projeto Final Relâmpago: Meu Primeiro Fluxo com Claude Code”

## O “Pulo do Gato”

O fluxo ideal com Claude Code segue uma sequência simples: preparar, perguntar, revisar, testar e refletir.

É como uma prática de laboratório bem feita: objetivo, procedimento, execução, análise e conclusão.

## Desenvolvimento

Ao final do curso, os estudantes devem ser capazes de executar um fluxo básico:

1. abrir o VS Code;
2. abrir o Claude Code;
3. selecionar um trecho de código;
4. fazer uma pergunta clara;
5. pedir plano antes de alterar;
6. revisar o diff;
7. aceitar ou rejeitar mudanças;
8. testar o código;
9. registrar o que aprenderam.

Fluxo recomendado:

```markdown
## Fluxo básico de uso responsável

1. Entenda o problema.
2. Selecione o trecho relevante.
3. Escreva um prompt claro.
4. Peça explicação antes da correção.
5. Revise as mudanças propostas.
6. Teste o resultado.
7. Registre o aprendizado.
```

Esse fluxo reforça que Claude Code é uma ferramenta de aprendizagem ativa, não uma máquina de respostas prontas.

> **Mensagem final aos estudantes:**
> Use Claude Code para pensar melhor, não para pensar menos.

## Pílula Hands-on — Mão na Massa

**Tempo estimado:** 2 minutos
**Pode ser feito no smartphone ou computador.**

Crie seu próprio mini-protocolo de uso:

```markdown
## Meu protocolo com Claude Code

Antes de pedir ajuda, eu vou:
1. 
2. 
3. 

Depois da resposta, eu vou:
1. 
2. 
3. 
```

Sugestão:

```markdown
Antes de pedir ajuda, eu vou:
1. Identificar o problema.
2. Selecionar o trecho relevante.
3. Escrever um prompt claro.

Depois da resposta, eu vou:
1. Ler a explicação.
2. Revisar as mudanças.
3. Testar o código.
```

---

# Síntese Final do Curso

O Claude Code no VS Code pode ser uma ferramenta poderosa para docentes e discentes de Engenharia, especialmente quando usado com intenção pedagógica.

Ele ajuda a:

* explicar códigos;
* revisar erros;
* planejar mudanças;
* documentar projetos;
* organizar conversas;
* integrar arquivos;
* apoiar testes;
* desenvolver autonomia técnica.

Mas seu uso responsável depende de três atitudes fundamentais:

```markdown
1. Perguntar com clareza.
2. Revisar com atenção.
3. Aprender com o processo.
```

> **Frase de encerramento:**
> Claude Code não é o colega que faz o trabalho por você. É o colega paciente que ajuda você a entender o caminho — desde que você continue caminhando.

---

# Proposta de Organização Didática

## Carga sugerida

```markdown
Duração total sugerida: 2 a 4 horas
Formato: oficina prática ou minicurso
Público: graduação em Engenharia, anos iniciais
Pré-requisito: noções básicas de computador e VS Code
```

## Sequência recomendada

```markdown
1. Conceito e instalação
2. Primeira conversa
3. Seleção de código e @-mentions
4. Modos de permissão e revisão de diffs
5. Histórico, sessões e organização
6. Segurança e boas práticas
7. Projeto final relâmpago
```

## Avaliação formativa sugerida

```markdown
O estudante deve entregar:

1. Um prompt bem formulado.
2. Uma explicação do problema analisado.
3. Um print ou descrição de uma revisão de mudança.
4. Uma reflexão curta: "O que eu entendi melhor com apoio do Claude Code?"
```

---

# Rubrica Simples de Avaliação

| Critério          | Excelente                                        | Adequado                             | Precisa melhorar             |
| ----------------- | ------------------------------------------------ | ------------------------------------ | ---------------------------- |
| Clareza do prompt | Contexto, objetivo e limite bem definidos        | Pedido compreensível, mas incompleto | Pedido vago                  |
| Uso de contexto   | Seleciona trecho ou arquivo correto              | Usa algum contexto                   | Não informa contexto         |
| Revisão crítica   | Analisa antes de aceitar                         | Revisa parcialmente                  | Aceita sem entender          |
| Segurança         | Evita dados sensíveis e usa permissões adequadas | Demonstra algum cuidado              | Usa auto-accept sem critério |
| Aprendizagem      | Explica o que aprendeu                           | Relata parcialmente                  | Apenas copia resposta        |

---

# Encerramento

Este roteiro foi desenhado para transformar uma documentação técnica em uma experiência de aprendizagem acessível, prática e segura. O foco não é apenas ensinar onde clicar, mas desenvolver uma postura de uso consciente da IA em ambientes de programação.

A competência principal não é “saber usar Claude Code”.
A competência principal é **saber dialogar com uma ferramenta inteligente para aprender melhor, programar com mais clareza e revisar com responsabilidade**.
