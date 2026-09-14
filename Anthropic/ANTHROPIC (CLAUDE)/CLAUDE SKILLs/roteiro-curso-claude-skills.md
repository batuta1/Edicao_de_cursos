# Claude Skills Para Leigos
### Ensinando a Inteligência Artificial a trabalhar do seu jeito

---

## Apresentação

**Para quem é este curso.** Para professoras e professores universitários que já usaram — ou apenas ouviram falar de — assistentes de Inteligência Artificial como o Claude, e que se veem repetindo as mesmas explicações toda vez que abrem uma conversa nova. Não é preciso saber programar. Não é preciso ter usado nenhuma ferramenta técnica antes. Se você sabe criar uma pasta no computador e escrever um documento, tem tudo o que precisa.

**A promessa.** Ao final, você será capaz de pegar um procedimento que você já domina — corrigir trabalhos segundo a sua rubrica, montar um plano de ensino no formato exigido pela sua instituição, revisar referências bibliográficas, elaborar questões de prova no seu padrão — e transformá-lo em uma **Skill**: um pacote que o Claude carrega sozinho, na hora certa, e segue como quem segue um roteiro. Você para de explicar. A ferramenta passa a saber.

**O tom.** Direto, sem jargão gratuito e sem promessas mágicas. Toda vez que aparecer um termo técnico, ele será explicado no momento em que surgir. Toda vez que a ferramenta tiver um limite, o limite será dito com todas as letras.

> **O que este curso não é.** Não é um curso de programação, nem um curso sobre "como escrever prompts perfeitos". Skills existem justamente para você **parar** de reescrever o mesmo prompt. Escreveremos instruções, sim — mas como quem escreve um procedimento para um colega novo, não como quem decora fórmulas.

---

## Antes de Começar

Você vai precisar de:

1. **Um computador com navegador e internet.** Parte das atividades funciona no celular, mas a criação de Skills envolve pastas e arquivos — no computador é bem mais confortável.
2. **Uma conta no Claude (claude.ai).** Para *criar* Skills próprias, a documentação da Anthropic indica que o recurso está disponível nos planos Pro, Max, Team e Enterprise, com a execução de código habilitada. Skills prontas da Anthropic (Word, Excel, PowerPoint, PDF) aparecem também em outros contextos.
3. **Um editor de texto simples.** O Bloco de Notas do Windows ou o TextEdit do Mac servem. Precisamos gravar arquivos com extensão `.md`, e um editor simples faz isso sem complicar.
4. **Vontade de mexer.** Cada módulo termina com uma atividade de dois minutos. Elas são curtas de propósito: o objetivo é você *ver* a coisa acontecendo, não ler sobre ela.

> **Nota de versão.** Skills são um recurso jovem e em movimento rápido. Nomes de menus, planos e limites mudam. Sempre que este roteiro descrever um caminho de tela, confira na sua conta antes de repassar a alguém — a lógica se mantém, os rótulos podem ter mudado de lugar.

---

## Mapa do Curso

| Módulo | Título | Fase da jornada | O que você vai conseguir fazer |
|---|---|---|---|
| 1 | O plano de aula do professor substituto | Entender | Explicar o que é uma Skill e reconhecer quando vale a pena criar uma |
| 2 | A ferramenta não lê tudo: como o Claude escolhe | Entender | Explicar por que uma Skill quase não "pesa", e o que isso muda na hora de escrever |
| 3 | Abrindo o pacote: a anatomia de uma Skill | Entender | Identificar as partes de um SKILL.md e dizer para que serve cada uma |
| 4 | Sua primeira Skill, em dez minutos | Criar | Criar, subir e acionar uma Skill própria do zero |
| 5 | A frase que faz a Skill existir | Observar | Escrever uma `description` que dispara nas horas certas |
| 6 | Procedimento, não palestra | Modificar | Enxugar um texto inflado até virar instrução acionável |
| 7 | Uma pasta, vários arquivos | Modificar | Dividir uma Skill grande em arquivos de apoio |
| 8 | Quando não dispara (ou dispara demais) | Refinar | Diagnosticar e corrigir problemas de acionamento |
| 9 | Como saber se ficou boa | Refinar | Comparar o Claude com e sem a Skill e decidir com evidência |
| 10 | Skills que carregam o seu jeito de trabalhar | Aplicar | Escolher quais procedimentos seus merecem virar Skill |
| 11 | Skill de terceiros é software de terceiros | Aplicar | Auditar uma Skill baixada antes de instalá-la |
| 12 | O horizonte: Claude Code, plugins e API | Aplicar | Situar o que existe além do claude.ai e decidir se vale avançar |

A jornada vai de "nunca ouvi falar disso" até "consigo pegar um procedimento meu, transformá-lo numa Skill, testar se funciona e corrigir o que não funcionou".

---
---

# Módulo 1 — O plano de aula do professor substituto

## O "Pulo do Gato"

Imagine que você vai se ausentar por duas semanas e precisa deixar um plano para quem vai assumir as suas aulas. Você não escreve "dê aula de Metodologia Científica". Você escreve: qual bibliografia usar, em que ordem, qual atividade aplicar na terça, o que aceitar como resposta válida, e aquele detalhe que só quem já deu a disciplina sabe — "não comece pela definição de epistemologia, a turma trava".

**Uma Skill é exatamente isso, só que para o Claude.** É uma pasta com um procedimento escrito, que a ferramenta abre e segue quando a situação pede.

## Desenvolvimento

### O problema que a Skill resolve

Se você já usou o Claude com alguma regularidade, provavelmente reconhece esta cena: toda conversa nova, você cola de novo o mesmo bloco de contexto. "Use a norma ABNT NBR 6023." "O plano de ensino da minha universidade tem estes seis campos, nesta ordem." "Quando eu peço feedback de trabalho, comece pelos acertos, depois os problemas, e nunca escreva mais de uma página."

Você está reensinando a mesma coisa toda vez. E o custo não é só o tempo de colar: é que, quando você esquece de colar, o resultado sai errado.

Uma Skill retira esse conhecimento da sua memória e da sua área de transferência, e coloca num lugar de onde o Claude o busca sozinho.

### O que é, formalmente

Uma Skill é uma **pasta autocontida** cujo ponto de entrada é um arquivo chamado `SKILL.md`. Dentro dela podem morar instruções em texto, documentos de referência, modelos, exemplos e — em contextos mais avançados — scripts que executam tarefas.

O nome desse formato é **Agent Skills**. Ele começou como recurso do Claude, lançado pela Anthropic em outubro de 2025, e depois foi publicado como um **padrão aberto** — o que significa que uma Skill bem escrita tende a funcionar em outros assistentes que adotem a mesma especificação, não só no Claude.

> **A ideia central:** você deixa de pedir ao modelo que invente como fazer, toda vez, e passa a lhe entregar um procedimento operacional reutilizável.

### O que uma Skill *não* é

Três confusões comuns, vale desfazê-las agora:

1. **Não é um prompt salvo.** Um prompt é uma instrução do momento: "resuma este texto". Uma Skill é um procedimento que vale para uma *categoria* de tarefas, e que o Claude carrega quando reconhece a categoria.
2. **Não é memória.** Uma Skill guarda "como fazer", não "o que aconteceu na nossa conversa de terça". Ela não sabe quem é você; ela sabe como você quer que a tarefa seja feita.
3. **Não é apenas um arquivo de texto.** A equipe da Anthropic afirma explicitamente que essa é a concepção errada mais comum. A pasta pode funcionar como um pequeno pacote: documentação, regras, modelos, dados e recursos.

### Quando vale a pena criar uma

Um critério prático e honesto: **crie uma Skill quando você notar que está colando as mesmas instruções pela terceira vez.** Antes disso, é provavelmente cedo — você ainda não sabe direito qual é o procedimento.

Dois sinais adicionais:

- Existe um **jeito certo** de fazer a tarefa na sua área ou na sua instituição, e o jeito genérico não serve.
- A tarefa tem **etapas em ordem**, e pular uma etapa estraga o resultado.

### Erro comum de quem está começando

Querer que a primeira Skill resolva tudo. A própria Anthropic, ao analisar as centenas de Skills que usa internamente, concluiu que **Skills excessivamente abrangentes funcionam pior**. As melhores resolvem uma responsabilidade coerente. Uma Skill chamada `apoio-docente` que tenta cobrir correção, plano de ensino, e-mail para alunos e revisão de artigo vai funcionar mal nas quatro coisas.

Prefira: `corrigir-por-rubrica`. Estreita, clara, boa.

## 🧪 Pílula Hands-on — Mão na Massa

**Objetivo:** identificar o seu próprio candidato a primeira Skill.

**Faça agora (2 minutos):**

1. Abra um documento em branco — ou pegue papel mesmo.
2. Responda: *qual instrução eu já colei mais de duas vezes numa conversa com uma IA?* Escreva a instrução como você a colou.
3. Abaixo dela, escreva uma frase começando por "Use quando…" descrevendo em que situação essa instrução se aplica.

**Observe:** a segunda frase, a do "Use quando", é o coração de uma Skill. Guarde esse papel — vamos usá-lo no Módulo 4.

**Resultado esperado:** um par de frases — um procedimento e um gatilho — que serão a matéria-prima da sua primeira Skill.

---
---

# Módulo 2 — A ferramenta não lê tudo: como o Claude escolhe

## O "Pulo do Gato"

Você não decora a biblioteca inteira da universidade. Você conhece as **lombadas** dos livros na estante — título e um resumo do assunto — e só tira da prateleira o volume que interessa àquela pesquisa. Depois, dentro do livro, você vai ao capítulo certo, não à página um.

O Claude faz o mesmo com as Skills. E esse mecanismo tem nome: **progressive disclosure** — revelação progressiva.

## Desenvolvimento

### Os três níveis

A informação de uma Skill entra na conversa em três momentos diferentes, e essa é provavelmente a ideia mais importante do curso todo.

**Nível 1 — Os metadados (sempre carregados).**
Logo no início de qualquer conversa, o Claude recebe apenas o **nome** e a **descrição** de cada Skill disponível. Nada mais. A Anthropic estima o custo dessa etapa em aproximadamente **100 unidades de texto (tokens) por Skill**. É a lombada do livro.

**Nível 2 — As instruções (carregadas quando aciona).**
Quando o seu pedido combina com a descrição de alguma Skill, o Claude vai até o arquivo `SKILL.md` e o lê inteiro. Só agora o procedimento entra na conversa. A recomendação oficial é manter essa parte **abaixo de cerca de 5 mil tokens**. É o livro aberto.

**Nível 3 — Os recursos (carregados só se precisar).**
Documentos de apoio, modelos, exemplos e dados ficam parados na pasta e **não custam nada** enquanto não forem abertos. Se a sua Skill tem seis arquivos de referência e a tarefa de hoje precisa de um, os outros cinco permanecem fechados. É o capítulo específico.

O caminho, em resumo:

```text
Você faz um pedido
       ↓
O Claude olha as descrições de todas as Skills
       ↓
Reconhece uma que parece encaixar
       ↓
Abre o SKILL.md e lê o procedimento
       ↓
Executa
       ↓
Se precisar: abre um arquivo de referência específico
```

### Por que isso muda tudo na prática

Duas consequências que você vai sentir imediatamente:

**Primeira: você pode ter muitas Skills sem prejuízo.** Como só a descrição fica sempre carregada, ter vinte Skills instaladas não atrapalha o Claude. Ter *uma* Skill de quarenta páginas, sim — porque, quando ela aciona, as quarenta páginas entram na conversa de uma vez.

**Segunda: o "espaço de trabalho" do Claude é limitado e compartilhado.** Esse espaço se chama **janela de contexto** (*context window*): a quantidade total de texto que a ferramenta consegue manter em mente ao mesmo tempo. A documentação da Anthropic usa uma expressão certeira — a janela de contexto é um **bem público**. Sua Skill divide esse espaço com o histórico da conversa, com as outras Skills e com o seu pedido de verdade. Cada parágrafo desnecessário que você escreve tira espaço de outra coisa.

### O erro que quase todo mundo comete

Escrever a Skill como se estivesse explicando o assunto para uma pessoa que nunca ouviu falar dele. A orientação oficial da Anthropic é direta: **não ensine ao Claude aquilo que ele já sabe.**

Compare:

> **Ruim (inflado):** "Trabalhos acadêmicos são documentos produzidos por estudantes para demonstrar aprendizagem. A correção de trabalhos é uma atividade central da docência. Existem várias abordagens para corrigir, mas a mais comum é o uso de rubricas, que são tabelas com critérios..."

> **Melhor (enxuto):** "Corrija segundo a rubrica em `rubrica.md`. Atribua nota por critério antes da nota final."

A versão enxuta pressupõe — corretamente — que o Claude já sabe o que é um trabalho acadêmico e o que é uma rubrica. O que ele **não** sabe é qual é a *sua* rubrica e que você quer a nota por critério antes da global. É isso, e só isso, que a Skill precisa carregar.

### Uma comparação que ajuda

Muita gente pergunta: por que não colocar tudo num arquivo de contexto permanente, sempre disponível?

Porque um arquivo sempre disponível ocupa espaço sempre. Uma Skill ocupa cem tokens até o momento em que é útil. Se você tem quinze procedimentos diferentes, a diferença entre as duas abordagens é a diferença entre carregar quinze manuais debaixo do braço o dia inteiro e ter quinze manuais numa estante ao alcance da mão.

## 🧪 Pílula Hands-on — Mão na Massa

**Objetivo:** sentir na prática a diferença entre lombada e livro aberto.

**Faça agora (2 minutos):**

1. Abra uma conversa nova com o Claude.
2. Pergunte: **"Quais Skills você tem disponíveis agora?"**
3. Leia a resposta com atenção.

**Observe:** a resposta traz *nomes e descrições curtas* — não o conteúdo das Skills. Isso é o Nível 1 acontecendo diante dos seus olhos: o Claude sabe o que existe sem ter aberto nada.

**Resultado esperado:** uma lista de Skills disponíveis na sua conta, e a percepção concreta de que o Claude "conhece as lombadas" sem ter lido os livros.

---
---

# Módulo 3 — Abrindo o pacote: a anatomia de uma Skill

## O "Pulo do Gato"

Todo artigo científico tem duas partes com funções muito diferentes: a **folha de rosto com o resumo e as palavras-chave**, que serve para alguém decidir se vale a pena ler; e o **corpo do texto**, que só é lido por quem decidiu que sim.

O arquivo `SKILL.md` tem exatamente essas duas partes.

## Desenvolvimento

### O arquivo mínimo

Uma Skill inteira pode caber em quinze linhas. Este é um exemplo real de estrutura mínima:

```markdown
---
name: revisao-de-documento
description: Revisa documentos segundo um procedimento definido. Use quando o
  usuário pedir para inspecionar, validar ou revisar um documento.
---

# Revisão de Documento

Siga este procedimento:

1. Identifique o tipo de documento.
2. Leia o material de referência pertinente.
3. Aplique os critérios de validação.
4. Aponte as inconsistências.
5. Produza o resultado final no formato exigido.
```

Vamos abrir as duas partes.

### Parte 1 — O cabeçalho (o *frontmatter*)

É o bloco entre as duas linhas de três hifens (`---`). Esse formato tem um nome técnico, **YAML**, mas para o que faremos aqui basta saber a regra: cada linha é `campo: valor`.

Dois campos importam agora:

**`name`** — o nome da Skill. Regras oficiais, e elas são rígidas:

| Regra | Detalhe |
|---|---|
| Tamanho | Máximo de 64 caracteres |
| Caracteres | Somente letras minúsculas, números e hifens |
| Proibido | As palavras reservadas `anthropic` e `claude` |
| Proibido | Etiquetas XML (aqueles sinais `<` e `>`) |

Ou seja: `corrigir-por-rubrica` é válido. `Corrigir Por Rubrica` não é (maiúsculas e espaços). `claude-corretor` não é (palavra reservada).

**`description`** — a descrição. Máximo de 1.024 caracteres, não pode ficar vazia. É o campo mais importante do arquivo inteiro, e o Módulo 5 é inteiramente dedicado a ele.

### Parte 2 — O corpo

Tudo o que vem depois do segundo `---`. É o procedimento em si, escrito em **Markdown** — um jeito de formatar texto com sinais simples: `#` para título, `-` para item de lista, `**palavra**` para negrito. Se você já escreveu qualquer coisa no WhatsApp com asteriscos, já usou algo parecido.

O corpo é lido pelo Claude somente quando a Skill aciona.

### A pasta em volta

À medida que a Skill cresce, ela deixa de ser um arquivo e vira uma pasta:

```text
minha-skill/
│
├── SKILL.md          ← obrigatório: o procedimento principal
├── references/
│   ├── manual.md     ← consultado quando necessário
│   └── exemplos.md
├── templates/
│   └── modelo.docx   ← um modelo institucional, por exemplo
└── assets/
    └── logo.png
```

Só o `SKILL.md` é obrigatório. Todo o resto é opcional — e, como vimos no Módulo 2, não custa nada enquanto não for aberto.

> **Atenção:** ao escrever caminhos de arquivo dentro da Skill, use sempre a barra normal (`references/manual.md`), nunca a barra invertida do Windows (`references\manual.md`). A barra invertida quebra a Skill em outros sistemas. Esta é uma recomendação explícita da documentação oficial.

### Erro comum

Esquecer as linhas de `---`, ou colocar espaços antes delas. O cabeçalho precisa começar na primeira linha do arquivo, com três hifens colados na margem. Se o cabeçalho estiver malformado, a Skill até carrega, mas sem descrição — e sem descrição ela nunca aciona sozinha.

## 🧪 Pílula Hands-on — Mão na Massa

**Objetivo:** escrever um `SKILL.md` completo, sem instalar nada.

**Faça agora (2 minutos):**

1. Abra o Bloco de Notas (ou TextEdit).
2. Copie o exemplo mínimo deste módulo.
3. Troque o `name` por um nome seu, seguindo as regras (minúsculas, hifens, sem "claude").
4. Troque os cinco passos por cinco passos de um procedimento que você conhece.
5. Salve como `SKILL.md`. **No Windows, escolha "Todos os arquivos" no tipo, senão ele grava `SKILL.md.txt`.**

**Observe:** o arquivo inteiro cabe numa tela. Não há código, não há nada para instalar.

**Resultado esperado:** um arquivo `SKILL.md` válido salvo no seu computador — o esqueleto que vamos colocar no ar no próximo módulo.

---
---

# Módulo 4 — Sua primeira Skill, em dez minutos

## O "Pulo do Gato"

Até aqui, conversamos sobre a ideia. Agora a Skill vai existir. O caminho é mais curto do que parece: uma pasta, um arquivo, um arquivo compactado (ZIP), um upload. Nada mais.

## Desenvolvimento

### O procedimento completo

**Passo 1 — Escolha o procedimento.** Pegue aquele papel do Módulo 1. Se estiver muito amplo, estreite. "Ajudar com aulas" é amplo demais; "gerar três questões dissertativas a partir de um texto, no meu formato" está no ponto.

**Passo 2 — Crie a pasta.** No seu computador, crie uma pasta com o nome da Skill, em minúsculas e com hifens: `gerar-questoes-dissertativas`.

**Passo 3 — Escreva o `SKILL.md`.** Dentro da pasta, salve o arquivo. Estrutura sugerida para uma primeira Skill:

```markdown
---
name: gerar-questoes-dissertativas
description: Gera questões dissertativas a partir de um texto-base, no formato
  padrão da disciplina, com gabarito comentado. Use quando o usuário pedir
  questões de prova, avaliação dissertativa ou exercícios a partir de uma
  leitura.
---

# Geração de questões dissertativas

## Procedimento

1. Leia o texto-base fornecido.
2. Identifique os três conceitos centrais.
3. Para cada conceito, escreva uma questão que exija análise, não recuperação
   de informação literal.
4. Escreva o gabarito comentado de cada questão, indicando o que caracteriza
   uma resposta completa, uma parcial e uma insuficiente.

## Formato de saída

Enunciado numerado, valor em pontos entre parênteses, gabarito em bloco
separado ao final.

## Regras

- Nunca formule questão cuja resposta seja uma única palavra.
- Cada enunciado deve caber em três linhas.
- Não use "disserte sobre" como abertura.
```

**Passo 4 — Compacte a pasta em ZIP.** No Windows: clique com o botão direito na pasta → *Enviar para* → *Pasta compactada*. No Mac: botão direito → *Comprimir*.

**Passo 5 — Suba no claude.ai.** Nas configurações da sua conta, procure a área de Skills — a documentação indica o caminho por `Customize > Skills`, e o Help Center também descreve o acesso via configurações de recursos. Lá existe a opção de criar uma Skill ou enviar um arquivo ZIP.

> **Nota de versão.** Este é justamente o ponto do curso mais sujeito a mudança de rótulo. Se você não encontrar exatamente "Customize > Skills", procure por "Skills" na busca das configurações. A operação — enviar um ZIP — é estável; o caminho até ela, nem tanto.

**Passo 6 — Acione.** Abra uma conversa nova e faça um pedido que combine com a sua descrição. Não cite a Skill pelo nome. O teste real é ela acionar sozinha.

### O que esperar — e o que não esperar

**Espere** que funcione em linhas gerais e erre nos detalhes. É normal e é justamente por isso que existem os Módulos 8 e 9.

**Não espere** que a Skill apareça em todos os lugares. Este ponto confunde muita gente, então vale destacar: **Skills não se sincronizam entre superfícies.** Uma Skill enviada ao claude.ai não fica automaticamente disponível na API; uma Skill criada no Claude Code é um arquivo no seu computador, separada das outras duas. Se você quer a mesma Skill em dois lugares, precisa colocá-la nos dois lugares.

E mais um detalhe de alcance: no claude.ai, Skills próprias são **individuais de cada usuário**. Não há, hoje, distribuição centralizada para uma organização inteira nessa superfície — cada colega precisa subir a sua cópia.

### Erro comum

Compactar a pasta errada. O ZIP deve conter a **pasta** com o `SKILL.md` dentro, e não o `SKILL.md` solto. Se você selecionou o arquivo e comprimiu, refaça selecionando a pasta.

## 🧪 Pílula Hands-on — Mão na Massa

**Objetivo:** colocar uma Skill sua no ar e vê-la acionar.

**Faça agora (2 minutos — mais o tempo de upload):**

1. Compacte a pasta da sua Skill em ZIP.
2. Envie pela área de Skills da sua conta.
3. Abra uma conversa nova.
4. Faça um pedido que caia na situação descrita na sua `description` — **sem** mencionar o nome da Skill.

**Observe:** o Claude sinaliza quando usa uma Skill. Compare a resposta com o que ele daria sem nenhuma instrução: o formato deve estar mais próximo do seu padrão.

**Resultado esperado:** uma Skill sua funcionando, acionada por conta própria.

---
---

# Módulo 5 — A frase que faz a Skill existir

## O "Pulo do Gato"

Você pode escrever o melhor plano de aula do departamento. Se o resumo na primeira página não disser a quem ele serve, ninguém vai tirá-lo da gaveta.

A `description` é esse resumo. E ela é, disparadamente, a parte da Skill em que mais vale investir tempo.

## Desenvolvimento

### Por que ela pesa tanto

Volte ao Módulo 2 por um instante. No Nível 1, o Claude recebe **só** nome e descrição de cada Skill. É com essa informação — e apenas com ela — que ele decide se vale a pena abrir o arquivo.

Isso significa que uma Skill pode ter um procedimento excelente e **nunca ser usada**, porque a descrição não deixou claro quando ela se aplica. A documentação da Anthropic separa os dois problemas de forma explícita:

```text
1. O Claude escolheu a Skill certa?
2. Depois de escolher, executou corretamente?
```

São falhas independentes. Uma Skill perfeita que não aciona vale zero.

### A regra das duas metades

Uma boa descrição responde a **duas** perguntas, nesta ordem: **o que a Skill faz** e **quando usá-la**. A segunda metade é a que a maioria das pessoas esquece.

> **Ruim:** `description: Ajuda a analisar arquivos`
>
> **Ruim:** `description: Processa dados`
>
> **Melhor:** `description: Analisa planilhas mensais de vendas em CSV, calcula métricas regionais de desempenho, identifica anomalias e produz a revisão padrão de vendas. Use quando o usuário pedir análise de dados mensais de vendas.`

Repare na estrutura da versão melhor: uma primeira parte descrevendo a ação, e uma segunda parte começando por "Use quando…", trazendo as palavras que a pessoa realmente digitaria.

### Três regras de escrita

**Escreva em terceira pessoa.** A descrição é inserida nas instruções internas do Claude, e misturar pontos de vista atrapalha a descoberta.

- Bom: "Processa arquivos Excel e gera relatórios."
- Evite: "Eu posso ajudar você a processar arquivos Excel."
- Evite: "Você pode usar isto para processar arquivos Excel."

**Inclua as palavras que a pessoa diria.** Se os seus colegas dizem "TCC", coloque "TCC" na descrição — não apenas "trabalho de conclusão de curso". O acionamento funciona por correspondência entre o pedido e a descrição.

**Ponha o caso principal na frente.** Há um limite de caracteres, e descrições longas podem ser cortadas quando há muitas Skills instaladas. O que estiver no começo sobrevive.

### Exemplos aplicados ao contexto docente

| Situação | Descrição fraca | Descrição forte |
|---|---|---|
| Correção por rubrica | `Ajuda a corrigir trabalhos` | `Corrige trabalhos discentes segundo a rubrica da disciplina, com nota por critério e feedback estruturado. Use quando o usuário pedir correção, avaliação ou feedback de trabalho, prova dissertativa ou TCC.` |
| Referências ABNT | `Formata referências` | `Formata referências bibliográficas na norma ABNT NBR 6023 e verifica a correspondência entre citações no texto e lista final. Use quando o usuário pedir para formatar, revisar ou conferir referências, citações ou bibliografia.` |
| Plano de ensino | `Cria planos de ensino` | `Monta o plano de ensino no formato institucional obrigatório, com ementa, objetivos, conteúdo programático, metodologia, avaliação e bibliografia. Use quando o usuário pedir plano de ensino, plano de curso ou programa de disciplina.` |

### O outro lado do problema

Existe também o excesso. Uma descrição vaga demais gera **falsos positivos**: a Skill aciona em situações onde não deveria, e passa a atrapalhar. Se a sua Skill de referências ABNT dispara toda vez que você menciona a palavra "texto", a descrição está larga demais — restrinja.

## 🧪 Pílula Hands-on — Mão na Massa

**Objetivo:** reescrever uma descrição fraca até ela ficar acionável.

**Faça agora (2 minutos):**

1. Pegue a descrição da Skill que você criou no Módulo 4.
2. Verifique se ela contém, explicitamente, uma parte "Use quando…". Se não contiver, escreva.
3. Liste três frases diferentes que uma pessoa poderia digitar para pedir aquela tarefa. Confira se pelo menos uma palavra-chave de cada frase aparece na sua descrição.

**Observe:** quase sempre falta uma das três. Aquela é a situação em que a sua Skill não vai acionar.

**Resultado esperado:** uma descrição com as duas metades — o quê e quando — cobrindo três formulações reais de pedido.

---
---

# Módulo 6 — Procedimento, não palestra

## O "Pulo do Gato"

Existe uma diferença enorme entre o **texto de apoio** que você entrega ao aluno e o **roteiro** que você entrega ao monitor. O primeiro explica o assunto. O segundo diz o que fazer, em que ordem, e onde costuma dar errado.

O corpo de uma Skill é o segundo tipo de documento.

## Desenvolvimento

### O teste de cada parágrafo

A orientação oficial propõe três perguntas para cada trecho que você escrever:

1. O Claude realmente precisa desta explicação?
2. Posso presumir que ele já sabe isto?
3. Este parágrafo justifica o espaço que ocupa?

Se a resposta for "não" para a primeira, corte.

### Ruim vs. melhor

> **Ruim (aproximadamente 150 tokens):**
> "Arquivos PDF (Portable Document Format) são um formato comum que contém texto, imagens e outros conteúdos. Para extrair texto de um PDF, você precisará de uma biblioteca. Existem muitas bibliotecas disponíveis, mas a pdfplumber é recomendada porque é fácil de usar e resolve a maioria dos casos. Primeiro, você precisa instalá-la…"

> **Melhor (aproximadamente 50 tokens):**
> "Para extrair texto de PDF, use pdfplumber."

A versão curta pressupõe que o Claude sabe o que é um PDF e o que é uma biblioteca. E ele sabe.

Transportando para o nosso terreno:

> **Ruim:** "A avaliação por rubricas é uma prática consolidada na educação superior, defendida por diversos autores, que consiste em explicitar previamente os critérios..."

> **Melhor:** "Atribua nota por critério antes da nota final. Justifique cada critério em uma frase."

### Quanta liberdade dar

Nem toda instrução deve ser igualmente rígida. A documentação propõe uma analogia útil: pense no Claude percorrendo um caminho.

**Ponte estreita com abismo dos dois lados** — há um único jeito seguro. Dê instruções exatas, sem margem.

> "Execute exatamente este procedimento, nesta ordem. Não altere a sequência."

Use quando a operação é frágil, quando a consistência é crítica, ou quando pular uma etapa estraga tudo. Exemplo docente: o preenchimento de um formulário institucional com campos obrigatórios em ordem fixa.

**Campo aberto sem obstáculos** — vários caminhos levam ao destino. Dê a direção e confie.

> "Analise a estrutura do argumento, verifique a consistência entre problema e conclusão, e sugira melhorias de clareza."

Use quando múltiplas abordagens são válidas e a decisão depende do contexto. Exemplo docente: comentar um projeto de pesquisa.

**Meio-termo** — existe um padrão preferido, mas alguma variação é aceitável. Dê um modelo e permita adaptação.

O erro de iniciante costuma ser em um dos extremos: ou se escreve tudo como campo aberto (e o resultado sai inconsistente), ou tudo como ponte estreita (e a Skill fica engessada, incapaz de lidar com o caso que você não previu).

### Ferramentas de estruturação

Três padrões que funcionam bem:

**Fluxo com etapas numeradas.** Para tarefas de várias fases, numere. Para tarefas realmente complexas, forneça uma lista de verificação que o Claude possa copiar e ir marcando:

```text
Progresso da correção:
- [ ] Etapa 1: Ler o trabalho na íntegra
- [ ] Etapa 2: Pontuar cada critério da rubrica
- [ ] Etapa 3: Verificar se a soma bate com a nota final
- [ ] Etapa 4: Redigir o feedback
- [ ] Etapa 5: Conferir o limite de uma página
```

**Ciclo de verificação.** O padrão "produzir → conferir → corrigir → repetir" melhora muito a qualidade:

```text
1. Redija o feedback seguindo o guia em criterios.md
2. Confira contra a lista: terminologia consistente? todas as seções presentes?
3. Se houver problema: anote, revise, confira de novo
4. Só entregue quando todos os requisitos estiverem atendidos
```

**Exemplos de entrada e saída.** Quando o que importa é o *estilo* do resultado, mostre. Dois ou três pares de "entrada → saída" comunicam melhor que qualquer descrição.

### Terminologia consistente

Escolha um termo e mantenha-o do começo ao fim. Se você chamou de "critério", não passe a chamar de "item", "quesito" e "aspecto" nos parágrafos seguintes. A inconsistência atrapalha a leitura do procedimento.

### Evite informação com prazo de validade

Não escreva "até dezembro de 2026, use o formato antigo". Isso envelhece mal. Se precisar registrar o histórico, separe numa seção final chamada "Padrões antigos", deixando o corpo principal limpo.

## 🧪 Pílula Hands-on — Mão na Massa

**Objetivo:** enxugar um texto inflado até virar procedimento.

**Faça agora (2 minutos):**

1. Pegue o corpo da sua Skill do Módulo 4.
2. Passe as três perguntas do teste em cada parágrafo. Corte tudo que o Claude já sabe.
3. Converta o que sobrou em passos numerados, cada passo começando com um verbo no imperativo.

**Observe:** o texto costuma encolher pela metade. Compare o antes e o depois: o que sobrou é o que só você sabia.

**Resultado esperado:** um corpo de Skill mais curto, todo em verbos de ação, sem parágrafos explicativos.

---
---

# Módulo 7 — Uma pasta, vários arquivos

## O "Pulo do Gato"

Um bom plano de ensino não traz a bibliografia inteira transcrita. Ele **remete** a ela. Quem precisa da fonte primária vai buscá-la; quem não precisa não carrega o peso.

É assim que uma Skill cresce sem ficar pesada.

## Desenvolvimento

### Quando dividir

A regra prática oficial: mantenha o corpo do `SKILL.md` **abaixo de 500 linhas**. Passou disso, é hora de separar.

Mas o critério real não é o tamanho — é a **frequência de uso**. Pergunte-se: este conteúdo é necessário em *toda* execução da Skill, ou só em alguns casos? O que é sempre necessário fica no `SKILL.md`. O que é ocasional vira arquivo à parte.

### Padrão 1 — Guia principal com remissões

O `SKILL.md` funciona como sumário: traz o essencial e aponta o resto.

```markdown
# Correção por rubrica

## Procedimento padrão

1. Leia o trabalho na íntegra antes de pontuar.
2. Pontue critério por critério usando a rubrica.
3. Redija o feedback.

## Materiais de apoio

**Rubrica completa**: ver [rubrica.md](rubrica.md)
**Modelos de feedback**: ver [modelos-feedback.md](modelos-feedback.md)
**Casos difíceis (plágio, entrega parcial)**: ver [casos-limite.md](casos-limite.md)
```

Quando você pedir uma correção comum, o Claude lê o `SKILL.md` e a `rubrica.md`. O arquivo `casos-limite.md` só será aberto se um caso limite aparecer — e, até lá, custa zero.

### Padrão 2 — Organização por domínio

Quando a Skill cobre áreas distintas, separe por área para não carregar contexto irrelevante:

```text
skill-disciplinas/
├── SKILL.md
└── references/
    ├── metodologia.md
    ├── estatistica.md
    ├── redacao-academica.md
    └── etica-em-pesquisa.md
```

Pedido sobre metodologia abre só `metodologia.md`. Os outros três permanecem fechados.

### A regra do nível único

Este é um detalhe técnico com consequência prática grande: **os arquivos de apoio devem ser referenciados diretamente pelo `SKILL.md`**, e não uns pelos outros.

> **Ruim — encadeado demais:**
> `SKILL.md` remete a `avancado.md` → que remete a `detalhes.md` → onde está a informação de verdade.
>
> **Melhor — um nível só:**
> `SKILL.md` remete diretamente a `avancado.md`, `referencia.md` e `exemplos.md`.

O motivo: quando encontra referências encadeadas, o Claude tende a fazer leituras parciais dos arquivos mais profundos — espia o começo em vez de ler tudo — e acaba com informação incompleta.

### Sumário em arquivos longos

Para qualquer arquivo de referência com mais de 100 linhas, comece com um sumário:

```markdown
# Rubrica da disciplina

## Conteúdo
- Critério 1: Domínio conceitual
- Critério 2: Estrutura argumentativa
- Critério 3: Uso de fontes
- Critério 4: Redação e norma culta
- Faixas de nota e descritores

## Critério 1: Domínio conceitual
...
```

Assim, mesmo que o Claude leia só o começo, ele enxerga o escopo completo do que está disponível.

### Nomes de arquivo importam

Use nomes que digam o conteúdo. `regras-de-validacao-do-formulario.md` é infinitamente melhor que `doc2.md`. O Claude navega a sua pasta como você navegaria: pelo nome.

## 🧪 Pílula Hands-on — Mão na Massa

**Objetivo:** dividir uma Skill em núcleo e apoio.

**Faça agora (2 minutos):**

1. Olhe o corpo da sua Skill e marque cada bloco com **S** (necessário sempre) ou **AV** (necessário às vezes).
2. Recorte todos os blocos **AV** para um arquivo novo com nome descritivo.
3. No `SKILL.md`, deixe uma linha remetendo ao arquivo: `**[assunto]**: ver [nome-do-arquivo.md](nome-do-arquivo.md)`.

**Observe:** o `SKILL.md` fica visivelmente mais curto — e, mesmo assim, nada foi perdido. Só mudou de lugar.

**Resultado esperado:** uma pasta com `SKILL.md` enxuto mais pelo menos um arquivo de apoio referenciado a um nível de distância.

---
---

# Módulo 8 — Quando não dispara (ou dispara demais)

## O "Pulo do Gato"

O problema mais comum de quem cria a primeira Skill não é a Skill estar errada. É ela **não aparecer**. E, na esmagadora maioria das vezes, a causa está numa única linha do arquivo.

## Desenvolvimento

### Diagnóstico em quatro passos

Quando o Claude não usa a sua Skill onde deveria, percorra esta sequência:

**1. A Skill está sendo vista?**
Pergunte na conversa: "Quais Skills você tem disponíveis?". Se a sua não estiver na lista, o problema é de instalação, não de escrita. Confira se o ZIP subiu, se a Skill está ativada e se você está na conta certa.

**2. A descrição tem as palavras certas?**
Compare, lado a lado, o que você digitou e o que a descrição diz. Se você pediu "revisa aí meu artigo" e a descrição fala em "documentos acadêmicos submetidos a periódicos", a distância pode ser grande demais.

**3. O cabeçalho está bem formado?**
Se o bloco YAML estiver quebrado — um `---` faltando, um espaço no lugar errado — a Skill carrega **sem descrição**. Ela continua funcionando se você a invocar pelo nome, mas o Claude não tem contra o que comparar o seu pedido. Sintoma típico: funciona quando eu chamo, nunca funciona sozinha.

**4. Você tem Skills demais?**
Este é um comportamento pouco conhecido: quando há muitas Skills instaladas, a lista de descrições que fica sempre carregada pode estourar o orçamento de espaço reservado a ela. Nesse caso, algumas descrições são **encurtadas** — e podem perder justamente as palavras-chave que fariam o acionamento acontecer. Se a sua conta tem dezenas de Skills e as menos usadas pararam de acionar, é provavelmente isto.

### O problema inverso: dispara demais

Sintoma: a Skill entra em conversas onde não tem nada a ver, e enviesa a resposta.

Duas correções, em ordem de preferência:

**Primeira — estreite a descrição.** Quase sempre resolve. Troque termos genéricos por específicos, e delimite explicitamente o escopo. Em vez de "Use quando o usuário mencionar textos", escreva "Use quando o usuário pedir formatação de referências bibliográficas".

**Segunda — desligue o acionamento automático.** Existe um campo de cabeçalho para isso:

```yaml
---
name: enviar-comunicado-turma
description: Redige e envia o comunicado padrão para a turma.
disable-model-invocation: true
---
```

Com `disable-model-invocation: true`, **só você** pode acionar a Skill; o Claude nunca a inicia por conta própria. A própria Anthropic recomenda esse padrão para qualquer procedimento com **efeito colateral** — envio de mensagem, publicação, lançamento de nota, qualquer coisa que altere o mundo fora da conversa. Você não quer que o modelo decida sozinho que é hora de enviar um comunicado a sessenta alunos.

> **Atenção:** este campo é uma extensão do Claude Code. Ao empacotar uma Skill para envio ao claude.ai ou à API, apenas os campos da especificação aberta são aceitos — `name`, `description`, `license`, `compatibility`, `metadata` e `allowed-tools`. Incluir um campo fora dessa lista faz o envio **falhar com erro**, e não ser simplesmente ignorado.

Existe também o oposto, `user-invocable: false`, para conhecimento de fundo que o Claude deve consultar mas que não faz sentido como comando manual.

### Um caso que engana

A Skill aciona, responde bem na primeira vez, e depois parece "esquecer". Isso costuma não ser esquecimento: o conteúdo geralmente continua presente, e o modelo é que está escolhendo outro caminho. A correção é reforçar as instruções — linguagem mais assertiva, regra mais destacada — e não reescrever a Skill do zero.

## 🧪 Pílula Hands-on — Mão na Massa

**Objetivo:** provocar uma falha de acionamento de propósito, para reconhecê-la depois.

**Faça agora (2 minutos):**

1. Numa conversa nova, faça um pedido usando palavras **deliberadamente distantes** da sua descrição. Se a descrição fala em "correção de trabalhos", peça "dá uma olhada nisso aqui pra mim".
2. Veja se a Skill aciona.
3. Refaça o pedido usando as palavras exatas da descrição.

**Observe:** a diferença entre as duas respostas é a distância entre a linguagem real das pessoas e a linguagem que você escreveu na descrição. Essa distância é o seu próximo ajuste.

**Resultado esperado:** uma falha de acionamento observada de perto, e ao menos uma palavra nova para acrescentar à descrição.

---
---

# Módulo 9 — Como saber se ficou boa

## O "Pulo do Gato"

"Achei que melhorou" não é avaliação. Você não aprovaria essa frase num relatório de pesquisa do seu orientando, e ela não deveria bastar aqui também.

A boa notícia é que existe um teste simples e honesto: **rode a mesma tarefa com e sem a Skill, e compare.**

## Desenvolvimento

### Por que a impressão engana

Quando você acabou de escrever uma Skill, você é a pior pessoa do mundo para julgá-la. Você sabe o que ela pretende fazer, então lê a resposta preenchendo mentalmente as lacunas. Além disso, se você testar na mesma conversa em que criou a Skill, todo o contexto daquela conversa está contaminando o resultado — o Claude sabe coisas que ele não saberia com um usuário real.

**Regra prática: teste sempre em conversa nova.** Sempre.

### O procedimento de comparação

1. **Junte de três a cinco pedidos realistas** — coisas que você ou seus colegas realmente diriam, com as palavras que realmente usariam.
2. **Rode cada pedido em conversa nova, sem a Skill ativa.** Guarde as respostas.
3. **Rode os mesmos pedidos, em conversas novas, com a Skill ativa.** Guarde as respostas.
4. **Compare par a par.**

### O que comparar

Duas coisas, separadamente — e essa separação é o ponto mais importante do módulo:

**Acionamento.** Dos cinco pedidos, em quantos a Skill entrou sozinha? E houve algum pedido em que ela entrou e não devia? O primeiro número mede falsos negativos; o segundo, falsos positivos.

**Qualidade.** Nos casos em que acionou, o resultado ficou mais próximo do que você queria? Em quê, exatamente? "Manteve o formato de quatro campos" é uma observação útil. "Ficou melhor" não é.

O resultado ideal é algo que você consiga escrever assim:

```text
Claude sem a Skill:        2 de 5 no formato correto
Claude + Skill versão 1:   4 de 5
Claude + Skill versão 2:   5 de 5
```

### Critérios de êxito escritos antes

Um truque que muda a qualidade da avaliação: **escreva o que conta como sucesso antes de rodar o teste.** Por exemplo:

- Usa os quatro critérios da rubrica, nomeados.
- Dá nota por critério antes da nota final.
- O feedback cabe em uma página.
- Não inventa critério que não está na rubrica.

Com a lista pronta antes, você avalia contra ela em vez de avaliar contra a sua impressão do momento.

### Testar em modelos diferentes

Uma Skill é um complemento ao modelo, então o resultado depende do modelo. Um procedimento que funciona perfeitamente num modelo mais potente pode precisar de mais detalhes num modelo mais rápido e econômico. Se você pretende usar a Skill em mais de um, teste nos dois.

### Escreva a avaliação antes de escrever a Skill

Esta é a recomendação mais contraintuitiva — e uma das melhores — da documentação oficial: **crie as avaliações antes de escrever a documentação extensa.**

A lógica: rode primeiro as tarefas *sem* nenhuma Skill e anote onde exatamente o Claude falha. Aquelas falhas são o escopo real da sua Skill. Escrever assim garante que você está resolvendo problemas que existem, e não antecipando problemas imaginários.

### Uma ferramenta que ajuda

Existe uma Skill oficial da Anthropic chamada **`skill-creator`**, feita para ajudar a criar e melhorar Skills. Ela não serve apenas para gerar um `SKILL.md`: também auxilia a montar avaliações, medir taxa de sucesso, comparar duas versões da Skill entre si e ajustar a descrição responsável pelo acionamento. A Anthropic relata melhora no acionamento em cinco de seis Skills públicas de criação de documentos após aplicar esse processo.

> **Nota:** parte dos recursos de avaliação automática do `skill-creator` vive no Claude Code, ambiente que trataremos apenas como horizonte no Módulo 12. A comparação manual descrita acima não depende de nada disso e já entrega a maior parte do valor.

## 🧪 Pílula Hands-on — Mão na Massa

**Objetivo:** produzir a sua primeira evidência real.

**Faça agora (2 minutos):**

1. Escreva, em três marcadores, o que contaria como sucesso para a sua Skill.
2. Abra uma conversa nova, desative a Skill e faça um pedido típico. Guarde a resposta.
3. Ative a Skill, abra outra conversa nova, faça o mesmo pedido. Compare contra os três marcadores.

**Observe:** conte quantos marcadores foram atendidos em cada versão. Um número, não uma sensação.

**Resultado esperado:** uma comparação com e sem Skill, avaliada contra critérios escritos previamente.

---
---

# Módulo 10 — Skills que carregam o seu jeito de trabalhar

## O "Pulo do Gato"

Nem toda Skill tem o mesmo destino. Algumas ensinam o Claude a fazer algo que ele ainda não faz bem — e essas tendem a envelhecer, porque os modelos melhoram. Outras codificam **o seu jeito** de fazer as coisas — e essas não envelhecem, porque o seu jeito é seu.

Saber em qual grupo a sua Skill está muda o que vale a pena investir nela.

## Desenvolvimento

### Os dois tipos

A Anthropic divide as Skills em duas famílias:

**Skills de ampliação de capacidade** (*capability uplift*). Ensinam o modelo a executar algo que ele ainda não faz de forma suficientemente confiável. São valiosas hoje e podem ficar obsoletas amanhã, conforme os modelos evoluem.

**Skills de preferência codificada** (*encoded preference*). Não tornam o modelo mais inteligente; registram o processo desejado por uma pessoa ou instituição. Uma sequência específica para avaliar um projeto de extensão. O formato exato do relatório de atividades docentes exigido pela sua pró-reitoria. A ordem em que você quer o feedback.

Essas segundas tendem a permanecer relevantes indefinidamente, porque o objetivo delas é reproduzir **uma forma específica de trabalhar** — e nenhum modelo, por melhor que fique, vai adivinhar a norma interna da sua universidade.

Para o público docente, a conclusão prática é bastante direta: **a maior parte das suas melhores Skills será do segundo tipo.**

### As famílias que aparecem na prática

Ao analisar a própria biblioteca interna de centenas de Skills, a Anthropic identificou padrões recorrentes. Traduzindo os que se aplicam ao trabalho acadêmico:

| Família | Equivalente docente |
|---|---|
| Referência de normas e procedimentos | Normas da ABNT, regimento interno, resoluções do colegiado |
| Verificação e conferência | Checagem de plano de ensino contra os requisitos obrigatórios |
| Coleta e análise de dados | Tratamento padronizado de dados de pesquisa ou de avaliação institucional |
| Modelos e estruturas iniciais | Estrutura-padrão de projeto de pesquisa, relatório, parecer |
| Qualidade e revisão | Revisão de artigo contra as normas do periódico |
| Roteiros operacionais | Passo a passo de submissão a comitê de ética |

### O que fazer com a ferramenta como parceira de crítica

Um uso que costuma render bastante: pedir ao Claude que **critique** o resultado antes de você aceitá-lo. "Aponte três pontos em que este feedback está vago." "Este plano de ensino atende a todos os campos obrigatórios? Liste o que falta."

> **Nota:** o resultado gerado é sempre um ponto de partida. A decisão final — sobre a nota, sobre o parecer, sobre o texto que leva o seu nome — é sempre sua. A ferramenta acelera o trabalho; ela não assume a responsabilidade por ele.

### Um cuidado que o contexto docente exige

> **Atenção:** não use dados pessoais ou sensíveis de estudantes em exemplos dentro de uma Skill. Nomes, matrículas, notas identificáveis, laudos, situações de saúde ou de assistência estudantil não devem entrar em arquivos que ficam armazenados e podem ser compartilhados. Se você precisa de exemplos realistas, anonimize antes.
>
> Vale ainda registrar que, segundo a documentação da Anthropic, Skills **não** estão cobertas por acordos de retenção zero de dados: definições de Skill e dados de execução seguem a política padrão de retenção. Trate o conteúdo de uma Skill como algo que fica armazenado.

### Escolhendo o que virar Skill

Um critério de triagem em três perguntas:

1. **Repete?** Se você faz isso menos de uma vez por mês, provavelmente não compensa.
2. **Tem um jeito certo?** Se qualquer resultado razoável serve, você não precisa de uma Skill — precisa de um bom pedido.
3. **Cabe numa responsabilidade só?** Se você não consegue nomear a Skill sem usar "e", ela provavelmente são duas Skills.

## 🧪 Pílula Hands-on — Mão na Massa

**Objetivo:** montar a sua fila de Skills.

**Faça agora (2 minutos):**

1. Liste cinco tarefas repetitivas da sua rotina docente.
2. Ao lado de cada uma, escreva **AC** (ampliação de capacidade) ou **PC** (preferência codificada).
3. Passe as três perguntas de triagem em cada uma e risque as que não passarem.

**Observe:** as que sobrarem marcadas com **PC** são as suas melhores candidatas — são as que ninguém mais pode escrever no seu lugar.

**Resultado esperado:** uma fila priorizada de duas a três Skills que valem o seu tempo.

---
---

# Módulo 11 — Skill de terceiros é software de terceiros

## O "Pulo do Gato"

Copiar um prompt da internet é uma coisa. Instalar uma Skill da internet é outra, e bem mais séria: uma Skill pode carregar instruções, scripts executáveis, comandos, endereços externos e permissões.

A frase para guardar é curta: **um `SKILL.md` de terceiros deve ser tratado quase como código de terceiros.**

## Desenvolvimento

### O que existe lá fora

O ecossistema cresceu muito rápido. Há repositórios comunitários anunciando mais de mil Skills compatíveis com diferentes assistentes, além de diretórios e mercados independentes. Boa parte disso é útil. Boa parte não é.

Dois levantamentos acadêmicos recentes dão a dimensão do problema — e vale lê-los como **pesquisa recente sobre ecossistemas públicos**, não como veredito definitivo, e não como avaliação do repositório oficial da Anthropic:

- Um estudo de janeiro de 2026 coletou 42.447 Skills de dois mercados e analisou 31.132: segundo os autores, **26,1% apresentavam ao menos um padrão de vulnerabilidade**. Skills contendo scripts executáveis mostraram probabilidade maior de problemas do que Skills feitas só de instruções.
- Um preprint de agosto de 2026 analisou 138.133 arquivos `SKILL.md` públicos em 20.556 repositórios e encontrou **ao menos um defeito detectável em 91,8%** deles. Os problemas mais frequentes não eram ataques sofisticados: eram descrições ruins, instruções infladas e má organização.

Ou seja: o risco mais provável que você corre ao baixar uma Skill não é ser atacado. É instalar algo de baixa qualidade que atrapalha mais do que ajuda. Mas o risco grave existe, e é por isso que se audita.

### O que a Anthropic recomenda

A orientação oficial é clara: **use Skills apenas de fontes confiáveis** — as que você mesmo criou ou as obtidas da Anthropic. Se precisar usar algo de origem desconhecida, audite minuciosamente antes.

Os riscos nomeados na documentação:

- **Auditar de verdade.** Revise todos os arquivos: `SKILL.md`, scripts, imagens e demais recursos. Procure padrões estranhos — chamadas de rede inesperadas, acessos a arquivos, operações que não combinam com o propósito declarado.
- **Fontes externas são arriscadas.** Skills que buscam dados em endereços externos representam risco particular: o conteúdo trazido de fora pode conter instruções maliciosas. E mesmo uma Skill confiável pode ser comprometida se aquilo de que ela depende mudar com o tempo.
- **Uso indevido de ferramentas.** Uma Skill maliciosa pode acionar operações de arquivo ou comandos de formas prejudiciais.
- **Exposição de dados.** Uma Skill com acesso a informação sensível pode ser desenhada para vazá-la.
- **Trate como instalar um programa.** Redobre o cuidado em contextos com dados sensíveis.

A preocupação é séria o bastante para que, em agosto de 2026, a Anthropic tenha introduzido em versão beta, no plano Enterprise, uma função de varredura de segurança para Skills e plugins de terceiros.

### Uma lista de conferência para o professor

Antes de instalar qualquer Skill que você não escreveu:

- [ ] Abri e li o `SKILL.md` inteiro, do começo ao fim.
- [ ] Verifiquei se existe uma pasta `scripts/` e, se existe, olhei o que há dentro.
- [ ] Procurei endereços de internet e me perguntei por que a Skill precisa acessá-los.
- [ ] Procurei qualquer menção a senhas, chaves, credenciais ou envio de dados.
- [ ] Conferi se o que a Skill **faz** corresponde ao que a descrição **diz** que ela faz.
- [ ] Sei quem publicou, e essa origem é rastreável.

Se você não entende o suficiente para fazer a auditoria, a resposta correta é não instalar — ou pedir a alguém do setor de TI da instituição que olhe junto.

### O outro lado da moeda

Nada disso vale para as Skills que **você** escreve. Uma Skill sua, feita de instruções em Markdown, sem scripts e sem acesso externo, é um documento de texto. O risco é essencialmente nulo. Todo este módulo trata do que vem de fora.

## 🧪 Pílula Hands-on — Mão na Massa

**Objetivo:** exercitar o olhar de auditoria.

**Faça agora (2 minutos):**

1. Pegue a sua própria Skill do Módulo 4 e finja que a recebeu de um desconhecido.
2. Passe a lista de conferência acima nela.
3. Responda: se um colega recebesse esta Skill, ele conseguiria dizer o que ela faz apenas lendo o arquivo?

**Observe:** se a sua própria Skill não passa no teste de transparência, é sinal de que falta clareza — o mesmo defeito que você procuraria numa Skill alheia.

**Resultado esperado:** a lista de conferência aplicada uma vez, e ao menos um ponto de clareza melhorado na sua Skill.

---
---

# Módulo 12 — O horizonte: Claude Code, plugins e API

## O "Pulo do Gato"

Tudo o que fizemos até aqui aconteceu num navegador. Existe mais território além dele — e a boa notícia é que **o que você aprendeu continua valendo lá**. Muda a superfície, não o conceito.

Este módulo é um mapa, não uma exigência. Ninguém precisa avançar para os territórios abaixo para tirar proveito de Skills.

## Desenvolvimento

### As três superfícies

**claude.ai** — onde estivemos. Skills próprias enviadas em ZIP, individuais por usuário, e as Skills prontas da Anthropic para documentos.

**Claude Code** — uma ferramenta que funciona no terminal do computador, voltada principalmente a quem escreve software. Ali as Skills são **arquivos no disco**, o que traz vantagens: você edita e o efeito é imediato, sem upload, e a Skill pode ser versionada junto com um projeto. É também a superfície com mais recursos avançados.

**API do Claude** — o acesso por programação, para quem constrói sistemas. Ali as Skills são enviadas por um mecanismo próprio e ficam disponíveis para todo o espaço de trabalho.

Lembre do que vimos no Módulo 4: **as três não se sincronizam.** São três lugares distintos.

### O que só existe no Claude Code

Para você reconhecer, caso encontre num tutorial:

- **Controle de invocação** — os campos `disable-model-invocation` e `user-invocable` que vimos no Módulo 8.
- **Execução em subagente** — o campo `context: fork` faz a Skill rodar num contexto separado, como um auxiliar independente que trabalha e devolve o resultado. Útil para tarefas longas de pesquisa.
- **Injeção dinâmica de contexto** — a Skill pode executar um comando e receber o resultado *antes* de o Claude ler o arquivo. É o que permite uma Skill que "já chega sabendo" o estado atual de alguma coisa.
- **Comandos personalizados** — os antigos comandos de barra foram incorporados ao sistema de Skills. Um arquivo em `.claude/commands/deploy.md` e uma Skill em `.claude/skills/deploy/SKILL.md` produzem ambos o comando `/deploy`; se houver os dois, a Skill prevalece.

> **Atenção:** vale repetir o alerta do Módulo 8, porque é uma fonte real de frustração. Esses campos extras funcionam **apenas** no Claude Code. Ao empacotar uma Skill para o claude.ai ou para a API, apenas seis campos são aceitos: `name`, `description`, `license`, `compatibility`, `metadata` e `allowed-tools`. Qualquer outro campo faz o envio falhar com erro explícito, do tipo *"Unexpected key(s) in SKILL.md frontmatter"*.

### Onde as Skills moram no Claude Code

Três lugares, com regra de precedência:

```text
~/.claude/skills/<nome>/SKILL.md      → pessoal, vale em todos os seus projetos
.claude/skills/<nome>/SKILL.md        → do projeto, vale só naquele projeto
<plugin>/skills/<nome>/SKILL.md       → distribuída por plugin
```

Havendo conflito de nomes, o nível corporativo se sobrepõe ao pessoal, e o pessoal se sobrepõe ao do projeto.

### Plugin: a embalagem maior

Um **plugin** é uma unidade de distribuição que pode empacotar várias Skills junto com outros componentes. É o mecanismo para distribuir um conjunto coerente — por exemplo, todas as Skills do seu departamento — em vez de pedir a cada pessoa que instale seis arquivos separados.

### A distinção que mais confunde: Skill e MCP

Vale a pena entender, porque os dois termos aparecem juntos com frequência.

**MCP** é um mecanismo que dá ao Claude acesso a sistemas externos. Imagine uma conexão com o sistema acadêmico da sua universidade: o MCP forneceria as operações — consultar turma, lançar nota, listar matrícula.

Mas isso não explica *como a sua instituição trabalha*. Uma Skill faria isso:

```text
Ao lançar notas:
1. Confira se o prazo do calendário acadêmico está aberto.
2. Confira se todas as avaliações previstas no plano foram lançadas.
3. Confirme a média com o critério do regimento.
4. Registre a observação padrão nos casos de reprovação por falta.
```

A síntese que a Anthropic usa é boa:

```text
MCP   = a capacidade de interagir com o sistema
Skill = o conhecimento sobre como a sua organização usa aquele sistema
```

Os dois se complementam. O MCP dá a ferramenta; a Skill ensina a usá-la dentro de um processo.

### O quadro completo

Para fechar o vocabulário:

| Mecanismo | O que é |
|---|---|
| **Prompt** | Instrução do momento: "analise este documento" |
| **Arquivo de contexto do projeto** | Contexto que deve estar sempre disponível naquele trabalho |
| **Skill** | Conhecimento ou procedimento especializado, carregado sob demanda |
| **MCP** | Acesso a sistemas e ferramentas externas |
| **Subagente** | Isolamento de contexto e execução delegada |
| **Plugin** | Unidade de distribuição que empacota vários dos anteriores |

### Vale a pena avançar?

Honestamente: **para a maioria dos docentes, não é necessário.** O claude.ai resolve os casos de correção, planejamento, revisão e formatação que compõem a rotina.

Faz sentido olhar o Claude Code se você trabalha com programação, análise de dados em código, ou se coordena um grupo que precisa compartilhar Skills versionadas junto com um repositório.

## 🧪 Pílula Hands-on — Mão na Massa

**Objetivo:** posicionar-se no mapa antes de decidir qualquer coisa.

**Faça agora (2 minutos):**

1. Responda, honestamente: as minhas tarefas repetitivas envolvem arquivos no meu computador e comandos, ou envolvem texto e documentos?
2. Se a resposta for "texto e documentos" — o claude.ai basta, e você já sabe o que precisa. Anote isso.
3. Se envolver arquivos e comandos, anote uma frase: "quero investigar o Claude Code para _____".

**Observe:** a maioria das respostas cai no primeiro caso. Reconhecer isso economiza semanas de estudo desnecessário.

**Resultado esperado:** uma decisão consciente sobre avançar ou não, com o motivo escrito.

---
---

## Encerramento

Vale a pena olhar para trás e ver o caminho percorrido.

Você começou reconhecendo um incômodo que talvez nem tivesse nome: **estar reensinando a mesma coisa toda vez**. Descobriu que o mecanismo que resolve isso se chama Skill, e que ele funciona por revelação progressiva — a ferramenta conhece as lombadas e só abre o livro necessário.

Depois você abriu o pacote: um cabeçalho com nome e descrição, um corpo com o procedimento, e uma pasta em volta para o que for opcional. E então criou a sua — de verdade, com upload e acionamento.

A partir daí, o curso deixou de ser sobre "como fazer" e passou a ser sobre **como fazer bem**: uma descrição que aciona nas horas certas, um corpo enxuto que não repete o que a ferramenta já sabe, arquivos de apoio que só custam quando são usados, diagnóstico de falhas, e — talvez o mais importante — a disciplina de comparar com e sem, contra critérios escritos antes.

Nos módulos finais, você mapeou o que vale a pena transformar em Skill, aprendeu a auditar o que vem de fora e situou-se no território maior sem precisar entrar nele.

O que você ganha com isso não é velocidade. É **consistência**: o mesmo padrão, na terça e na sexta, no primeiro trabalho e no quadragésimo, com você presente ou não. Em uma rotina docente, isso é bastante coisa.

Uma última observação, e ela é séria. Skills são um recurso em movimento rápido. Nomes de menu mudam, planos mudam, campos novos aparecem. O que você aprendeu aqui — o raciocínio sobre carregamento sob demanda, sobre acionamento, sobre concisão, sobre avaliação — esse não muda. Quando algo na tela não corresponder ao que está escrito neste roteiro, confie no raciocínio e confira o detalhe.

---

## Glossário Rápido

**Agent Skills** — o padrão aberto que define o formato de Skill. Nasceu no Claude, foi publicado como especificação, e por isso tende a funcionar em outros assistentes.

**Descrição (`description`)** — o campo do cabeçalho que diz o que a Skill faz e quando usá-la. É por ele que o Claude decide acionar. Máximo de 1.024 caracteres.

**Falso negativo / falso positivo** — quando a Skill deveria acionar e não acionou (negativo), ou acionou onde não devia (positivo). São problemas distintos, com correções distintas.

**Frontmatter (cabeçalho)** — o bloco entre `---` no topo do `SKILL.md`, com os metadados da Skill.

**Janela de contexto** — a quantidade total de texto que a ferramenta consegue manter em mente ao mesmo tempo. É limitada e compartilhada entre tudo: seu pedido, o histórico, as Skills.

**Markdown** — forma simples de formatar texto com sinais: `#` para título, `-` para lista, `**` para negrito. É o formato do `SKILL.md`.

**MCP** — mecanismo que dá ao Claude acesso a sistemas externos. Complementar à Skill: o MCP dá a ferramenta, a Skill ensina o processo.

**Plugin** — unidade maior de distribuição, capaz de empacotar várias Skills e outros componentes de uma vez.

**Progressive disclosure (revelação progressiva)** — o mecanismo de carregar informação em etapas: primeiro só a descrição, depois o procedimento, depois os arquivos de apoio, e cada etapa só se for necessária.

**SKILL.md** — o arquivo obrigatório, ponto de entrada de toda Skill.

**Skill** — pasta autocontida com um procedimento que o Claude carrega sob demanda quando reconhece a situação.

**skill-creator** — Skill oficial da Anthropic voltada a ajudar na criação, avaliação e refinamento de outras Skills.

**Subagente** — execução em contexto separado. Uma Skill pode ser configurada para rodar assim no Claude Code.

**Token** — a unidade em que se mede o texto processado pela ferramenta. Aproximadamente uma palavra curta ou um pedaço de palavra. Serve para falar de custo de espaço.

**YAML** — o formato do cabeçalho, no estilo `campo: valor`, uma linha para cada.
