# Análise Crítica 360 — ChatGPT (Codex) no VS Code (Hands-on), versão 1.0

**Objeto base:** Codex no Visual Studio Code, com recorte de uso acadêmico não-programador
**Público-alvo:** professores universitários que não programam
**Pré-requisitos declarados:** saber criar pastas e mover arquivos; conta ChatGPT; nenhum conhecimento de programação
**Trilha:** Hands-on
**Documento analisado:** `01-v1-hands-on.md`

---

## 1. Sumário Executivo

**Nota: 6,5 / 10.** Curiosamente, a trilha Hands-on entendeu o público melhor do que a Essentials: as
quatro oficinas partem de problemas docentes reais e a promessa de abertura — "sem escrever uma linha
de código" — é exatamente a certa. O documento sabe para quem está escrevendo.

O que falha é a proteção. **Este é o único curso do lote em que o participante autoriza um programa a
alterar e apagar arquivos no seu computador, e a v1.0 nunca ensina como controlar isso.**

Principais constatações:

1. **O modo somente leitura nunca é configurado.** Aparece uma única vez, na tabela "Se travar" da
   Oficina 3, como explicação de por que um arquivo não foi criado — pressupondo que o participante
   já sabe o que é e já o ativou. Ninguém lhe disse.
2. **Não há Oficina 0.** A regra de ouro pede cópia da pasta em tom de recomendação; a Oficina 1 já
   manda abrir uma pasta e comandar; e só na Oficina 2, passo 1, a cópia vira passo — para aquela
   oficina apenas.
3. **A Oficina 4 é a mais arriscada e a menos protegida.** Manda "autorize a execução quando ele
   pedir" e "autorize se você confiar na tarefa", sem que o participante tenha aprendido o que
   significa autorizar, quais são os níveis, ou o que muda quando se concede acesso à rede.
4. **`codex doctor` aparece como desafio opcional da Oficina 1**, mandando "rodar no terminal" um
   público que não sabe o que é terminal.
5. **Um desafio por oficina, sem forma de validação.** O prompt-mestre exige três com validação.
6. **Sem pontos de controle.** "Deu certo?" descreve estados em prosa, sem dizer onde olhar.
7. O Projeto Final é a soma das Oficinas 2 e 3.

---

## 2. Pontos Positivos (Fortalezas)

**A promessa de abertura.** "Você não vai programar nada. Vai só dizer o que quer, em português" é a
frase que faz o público continuar, e a v1.0 da Essentials não tem nada parecido. Mantenha literal.

**Os quatro problemas das oficinas são os certos.** Trinta arquivos com nomes impossíveis; "em qual
desses arquivos eu falei sobre aquilo"; dados numa planilha e vontade de um gráfico. São situações que
todo docente reconhece em dois segundos, e nenhuma delas exige explicar o que é programação.

**O passo 3 da Oficina 2 — pedir a lista antes de renomear.** É o procedimento mais importante do
curso inteiro, está bem escrito, e a dica que o acompanha ("é a diferença entre corrigir uma lista e
desfazer trinta renomeações") explica por quê em termos operacionais.

**A Oficina 3 termina produzindo um artefato que fica.** O `indice.md` é um entregável real, que o
participante usa depois do curso. É o melhor fecho de oficina do documento.

**O aviso da Oficina 4 sobre não colocar nome de aluno no arquivo processado** é correto e está no
lugar certo — embora chegue tarde no curso.

**A Parte dos Dez é boa e é a única parte do documento que trata de permissões de forma acionável**
(itens 2, 6 e 8). O problema é que está no fim.

---

## 3. Pontos Negativos e Gargalos (Debilidades)

### 3.1 O controle de segurança principal nunca é ensinado

Os três níveis de aprovação são o que separa "o agente propôs" de "o agente fez". O curso inteiro
passa sem configurá-los. Na Oficina 2, o participante é instruído a "aprovar ou corrigir" sem saber o
que está aprovando. Na Oficina 4, a instruir "autorize se você confiar na tarefa" — que transfere ao
iniciante uma avaliação de risco que ele não tem repertório para fazer.

### 3.2 A cópia é parcial e tardia

O cabeçalho recomenda; a Oficina 2 executa, mas apenas para aquela oficina; as Oficinas 1, 3 e 4 não
mencionam. Na Oficina 3 o agente **cria um arquivo** na pasta; na Oficina 4, **executa código e pede
acesso à rede**. As duas operam sem cópia declarada.

### 3.3 A Oficina 1 abre "uma pasta qualquer"

Passo 6: "Abra uma pasta em `Arquivo > Abrir Pasta`". Não diz qual, não diz que deve ser uma pasta de
teste, e o passo 7 já pede uma descrição do conteúdo. Se o participante abrir a pasta da tese, o
conteúdo dela foi lido antes de qualquer decisão sobre dados.

### 3.4 Terminal introduzido sem apresentação

O desafio da Oficina 1 manda "rodar `codex doctor` no terminal". Para o público declarado, isso são
três termos desconhecidos numa frase de oito palavras. E é um desafio opcional — ou seja, o comando
de diagnóstico mais útil do curso está escondido no lugar de menor visibilidade.

### 3.5 A Oficina 4 pressupõe o que não ensinou

"Exporte a planilha em CSV" — sem dizer como, e CSV não é explicado. "Autorize a execução quando ele
pedir" — sem explicar o que está sendo executado. "Ele precisa de acesso à rede. Autorize se você
confiar na tarefa" — sem critério algum de confiança.

### 3.6 Um desafio por oficina, sem validação

Quatro desafios no curso, de uma linha cada, nenhum com forma de verificação.

### 3.7 O Projeto Final é a soma das Oficinas 2 e 3

Padronizar nomes, organizar em subpastas, montar índice. Nenhuma competência nova, e a Oficina 4 nem
aparece.

### 3.8 Sem pontos de controle

"O painel do Codex respondeu descrevendo os seus arquivos" e "os arquivos estão com nomes
padronizados" descrevem o resultado, mas não dizem onde olhar na interface para confirmá-lo.

### 3.9 Limites de uso ausentes

O material-fonte declara cota compartilhada entre Codex e outros recursos, e que tarefa longa consome
muito mais que solicitação curta. A Oficina 4 é justamente uma tarefa longa. O participante pode
travar sem entender.

### 3.10 Integridade acadêmica ausente

Mesma lacuna dos cursos irmãos, com o agravante já apontado na trilha Essentials: aqui o agente lê a
pasta inteira, e não o trecho que o participante escolhe colar.

### 3.11 Não verificável

Nome exato da extensão na loja do VS Code, aparência do painel, e — sobretudo — **o comportamento do
Codex em pastas que não são repositórios de código**. Todas as quatro oficinas dependem desse
pressuposto e ele não foi testado. É pendência de primeira ordem.

---

## 4. Matriz de Soluções e Melhorias

| # | Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|---|
| 1 | Níveis de aprovação nunca ensinados | Todo o curso | Criar **Oficina 0 — Antes de deixar um agente perto dos seus arquivos**, cujo conteúdo central é: o que muda entre uma conversa e um agente; os três níveis de aprovação em linguagem do público; e a instrução explícita de operar em modo somente leitura até a Oficina 2. | Crítica |
| 2 | Cópia parcial e tardia | Cabeçalho e Oficina 2 | Virar passo numerado e verificável na Oficina 0, com ponto de controle: duas pastas visíveis. Todas as oficinas seguintes operam na cópia, e cada uma o reafirma em uma linha. | Crítica |
| 3 | Oficina 1 abre pasta real | Oficina 1 | Criar, na Oficina 0, uma **pasta de teste** com três ou quatro arquivos de exemplo. A Oficina 1 opera só nela. Nenhum material real é aberto antes da Oficina 2. | Crítica |
| 4 | Oficina 4 pressupõe o não ensinado | Oficina 4 | Explicar o que é CSV e como exportar (`planilha > Arquivo > Salvar como > CSV`); declarar o que o agente vai executar e por que precisa de rede; e dar um critério de decisão em vez de "se você confiar": autorizar rede apenas para instalar bibliotecas de gráfico, em pasta de teste, e nunca em pasta com dado sensível. | Crítica |
| 5 | Terminal sem apresentação | Oficina 1 | Explicar o que é o terminal antes de mencioná-lo, e promover `codex doctor` de desafio opcional para a tabela "Se travar" da Oficina 1, onde ele é efetivamente útil. | Alta |
| 6 | Um desafio por oficina | Todas as oficinas | Três desafios por oficina, cada um com "Deu certo se:". | Alta |
| 7 | Sem pontos de controle | Todas as oficinas | Substituir por "🏁 Ponto de controle" com o caminho de interface onde o estado é observável. | Alta |
| 8 | Projeto Final é revisão | Projeto Final | Trocar por uma missão que exige competência não coberta: **transformar a pasta bagunçada de uma disciplina em um pacote entregável** — nomes padronizados, subpastas, índice navegável **e** um arquivo de instruções de projeto que faça o agente repetir o mesmo padrão no semestre seguinte. Este último item mobiliza o módulo de instruções de projeto da trilha Essentials e não é a soma de nenhuma oficina. | Alta |
| 9 | Limites de uso ausentes | Oficina 0 | Incluir: cota compartilhada entre Codex e outros recursos; tarefa longa consome muito mais; onde consultar a situação. | Alta |
| 10 | Integridade acadêmica ausente | Oficina 0 | Três perguntas institucionais, mais a regra operacional específica: o que for sensível fica **fora da pasta de trabalho**, porque o agente lê a pasta inteira. | Alta |
| 11 | Tempos arredondados | Mapa da Mão na Massa | Recalcular na Fase 4 pela MET, com a Oficina 0 incluída. | Média |

---

## 5. Roadmap de Expansão

**Cabe neste curso** (endereçado acima): Oficina 0 com aprovações, cópia, pasta de teste e dados;
critério de decisão para acesso à rede; terminal apresentado antes de usado; três desafios por
oficina; Projeto Final com instruções de projeto.

**Fica para um curso seguinte:**

- **A interface de linha de comando.** Cliente mais poderoso e mais intimidante. Introduzi-la aqui
  desfaria o trabalho de acessibilidade que a promessa de abertura constrói.
- **Versionamento.** Desfazer alterações de forma confiável é exatamente o que um sistema de
  versionamento resolve, e é a evolução natural deste curso — mas exige um curso próprio, com
  vocabulário próprio.
- **Tarefas na nuvem e revisão automática.** Pressupõem repositório e fluxo de desenvolvimento de
  software.
- **Análise de dados.** A Oficina 4 ensina a pedir um gráfico. Estatística aplicada com apoio de
  agente é outro curso, com pré-requisitos de método.
- **Gravar e reproduzir.** Restrito a macOS, a usuários qualificados, e indisponível em parte da
  Europa. Restrições demais para um curso introdutório.
