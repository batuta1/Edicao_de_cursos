# Roteiro Final — ChatGPT no Word (Hands-on)

**Público-Alvo:** professores universitários, de qualquer área, inteiramente novatos no uso de
inteligência artificial generativa para trabalho de escrita.

**Objetivo Geral:** levar o docente a executar, com as próprias mãos, o ciclo completo de produção
de um documento do Word com apoio do ChatGPT — da estrutura em branco ao arquivo pronto para enviar
—, tendo antes verificado o que acontece com o texto que envia e o que sua instituição espera dele.

**Pré-requisitos:** uso básico do Microsoft Word; conta ativa no ChatGPT, ainda que gratuita; um
documento real de trabalho, do qual será feita cópia no início do curso.

**Carga horária:** 113 minutos (detalhamento em `../carga-horaria/carga-horaria-hands-on.md`).

---

## Estrutura do Curso

| Nível | Unidades | Finalidade |
|---|---|---|
| Nível 0 — Preparação | Oficina 0 | Verificar acesso, decidir sobre dados e autoria, criar a cópia de trabalho |
| Nível 1 — Operações | Oficinas 1 a 4 | Uma operação de escrita por oficina, cada uma entregando um resultado concreto |
| Nível 2 — Integração | Projeto Final | Uma missão que exige encadear as operações em sequência nova |
| Apêndice | A Parte dos Dez | Repertório de instruções para consulta rápida |

**Anexos:** não há anexos. Os assuntos deslocados constam do Roadmap de Expansão em
`../_processo/02-analise-hands-on.md`.

> **Nota sobre a auditoria.** Os dez gargalos da matriz de soluções de
> `../_processo/02-analise-hands-on.md` foram endereçados. Uma decisão declarada: a antiga Oficina 4
> ("revisar antes de mandar") não virou oficina própria — foi absorvida pelo Projeto Final, onde a
> revisão tem função real, em vez de ser exercício sobre um documento que ainda não existe. A
> numeração das oficinas seguintes foi ajustada.

---

# ChatGPT no Word Para Leigos — Curso Hands-on

*No fim deste curso você vai ter um documento seu, de verdade, transformado e pronto para enviar — e
um caderninho de instruções que funcionam.*

## Antes de Arregaçar as Mangas

Este curso é mão na massa. Nada de teoria longa: você vai abrir o Word, abrir o ChatGPT no
navegador, e passar as próximas duas horas resolvendo problemas de escrita que provavelmente estão
na sua mesa hoje. Cada oficina termina com alguma coisa pronta.

**O que você precisa ter aberto agora:**

- O Microsoft Word, com um documento seu de verdade.
- Um navegador aberto em `chatgpt.com`, com sua conta conectada.
- Alguma coisa para anotar as instruções que derem certo.

> 🔑 **Regra de ouro:** o ChatGPT escreve rápido e escreve errado com a mesma confiança. Você é o
> revisor, sempre. Nada sai da sua mesa sem você ter lido.

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 0 | "Antes de sair colando: o que acontece com o meu texto?" | 7 min |
| 1 | "Não sei nem como começar este documento" | 20 min |
| 2 | "Este parágrafo está horrível e eu não sei por quê" | 20 min |
| 3 | "São dezoito páginas e eu não vou colar isso parágrafo por parágrafo" | 20 min |
| 4 | "Preciso da metade do tamanho e não posso perder o conteúdo" | 20 min |
| Projeto Final | Virar um documento do avesso para outro público | 26 min |

Faça a Oficina 0 primeiro — ela não é opcional. As demais fazem mais sentido em sequência: cada uma
entrega uma pequena vitória, e o Projeto Final exige juntar todas.

---

# Oficina 0 — Cinco minutos antes de começar

## Descrição

- **Objetivos da Aula:** verificar o acesso e o plano; mostrar o que cada plano faz com o texto
  enviado; nomear o que nunca deve ser colado; conduzir a criação da cópia de trabalho; e apresentar
  as três perguntas de autoria que antecedem o uso institucional.
- **Habilidades Esperadas:** ao final, você sabe dizer qual é o seu plano e o que ele faz com o seu
  texto, tem a cópia de trabalho salva ao lado do original, e sabe quais três perguntas precisa
  responder na sua instituição.

### 🎯 O Problema

Você vai colar, nas próximas duas horas, pedaços de documentos de trabalho num serviço que roda em
servidores de outra empresa. Vale cinco minutos para saber o que acontece com esse texto — e para
garantir que, se alguma coisa der errado no meio do caminho, o documento original continua
intacto.

### 🧰 O que você vai usar

- Navegador aberto em `chatgpt.com`, conta conectada.
- Word aberto, com o documento que você vai usar no curso.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** menu de perfil do ChatGPT aberto, no canto da tela, com o nome do plano
  visível. E, ao lado, uma janela do explorador de arquivos mostrando os dois arquivos — original e
  cópia — na mesma pasta.

1. Abra o menu de perfil da sua conta no ChatGPT e veja qual é o seu plano. Anote.

2. Encontre a sua linha nesta tabela:

   | Seu plano | O que ele faz com o texto que você cola |
   |---|---|
   | Free, Go, Plus, Pro | Pode usar o conteúdo para melhorar os modelos, a menos que você desative |
   | Business, Enterprise, Edu | Não usa, por padrão |

3. Se você está em Plus ou Pro e quer desativar: vá em `Configurações > Controles de dados` e
   desligue a opção de melhoria dos modelos. Se essa opção não aparecer, sua conta é administrada
   pela instituição e a configuração é feita por lá — não é falha sua.

4. Guarde esta lista. Nada aqui entra no ChatGPT, em nenhum plano:

   - Nome de aluno associado a nota, frequência, ocorrência ou condição de saúde.
   - Resultado de pesquisa ainda não publicado.
   - Parecer sigiloso de avaliação por pares.
   - Qualquer coisa coberta por acordo de confidencialidade.
   - Dado pessoal de terceiro coletado em pesquisa.

5. Agora a cópia. No Word: `Arquivo > Salvar como`, acrescente `-copia-curso` ao nome do arquivo,
   salve na mesma pasta. No Word na web o caminho é `Arquivo > Salvar uma cópia`.

6. Feche o documento original. Você vai trabalhar só na cópia.

7. Por último, três perguntas para responder na sua instituição — não hoje, mas antes de usar isso
   em documento oficial:

   - A sua universidade tem norma sobre uso de IA em documentos acadêmicos e administrativos?
   - Se você usar, precisa declarar? Onde — nota de rodapé, seção de métodos, declaração de autoria?
   - O que você vai dizer aos seus alunos, que têm a mesma ferramenta na mão?

### ✅ Deu certo?

🏁 **Ponto de controle:** na sua pasta há dois arquivos, o original e a cópia com sufixo
`-copia-curso`. E você consegue dizer, sem consultar nada, qual é o seu plano e se ele usa o seu
texto para treinar.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não encontro qual é o meu plano | Você pode ter duas contas — a institucional e a pessoal. Confira com qual e-mail está conectado. |
| A opção de controles de dados não aparece | Conta administrada pela instituição. A configuração é central; fale com quem administra. |
| `Salvar como` não existe no meu Word | Você está no Word na web. Use `Arquivo > Salvar uma cópia`. |

> ⚠️ **Cuidado:** não pule o passo 5. Nas oficinas seguintes você vai substituir parágrafos e
> remontar seções. A cópia é o que separa "experimentei" de "estraguei".

### 🚀 Quer ir além?

1. **Descubra a norma.** Procure no site da sua instituição por "inteligência artificial" e
   "integridade acadêmica". *Deu certo se:* você achou a norma, ou confirmou que ela não existe.
2. **Teste o esquecimento.** Apague uma conversa e confira em `Configurações > Armazenamento` se o
   espaço usado diminuiu. *Deu certo se:* você sabe onde ver o próprio armazenamento.
3. **Monte a sua lista pessoal.** Acrescente à lista do passo 4 dois itens específicos da sua área.
   *Deu certo se:* você consegue justificar cada um em uma frase.

---

# Oficina 1 — Vencer a página em branco

## Descrição

- **Objetivos da Aula:** mostrar como obter uma estrutura antes do texto; produzir uma primeira
  versão de uma seção; e resolver a colagem no Word sem arrastar formatação do navegador.
- **Habilidades Esperadas:** ao final, você sai da página em branco sozinho, com uma estrutura que
  você mesmo ajustou e ao menos um parágrafo escrito dentro dela, colado limpo no Word.

### 🎯 O Problema

É segunda-feira, você precisa escrever a apresentação de uma disciplina nova, e faz quarenta minutos
que o cursor está piscando no mesmo lugar. Não é falta de assunto — é que começar custa. Nesta
oficina você vai sair da página em branco em menos de cinco minutos.

### 🧰 O que você vai usar

- Word aberto, documento novo.
- ChatGPT no navegador.
- Uma ideia do que o documento precisa dizer. Não precisa estar organizada.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** conversa do ChatGPT mostrando a resposta com a lista de seções
  numeradas, e ao lado o documento do Word já com essas seções digitadas como títulos, com o painel
  de navegação aberto.

1. No ChatGPT, descreva o documento e peça só a **estrutura**, ainda não o texto:

   > Preciso escrever a apresentação de uma disciplina de graduação sobre [tema], para alunos de
   > primeiro período. Sugira oito seções que fariam uma estrutura lógica para esse documento.
   > Só os títulos das seções, sem escrever o conteúdo.

2. Leia a lista. Corte o que não serve, reordene o que estiver fora de lugar, acrescente o que
   faltou. Ela é sua, não dele.

3. Escolha a seção mais difícil de escrever e peça a primeira versão:

   > Escreva a seção "[nome da seção]" desse documento. Público: alunos de primeiro período.
   > No máximo cento e cinquenta palavras. Tom acessível, sem jargão de área.
   > Texto puro, sem símbolos de formatação.

4. Copie o resultado.

5. No Word, cole por `Página Inicial > Colar > Colar Especial > Texto não formatado`. No Word na web,
   `Página Inicial > Colar > Manter somente texto`. Isso evita trazer fundo cinza e fonte do
   navegador.

6. Leia o que colou e corte a primeira frase. Quase sempre ela é enfeite.

7. Aplique um estilo de título às seções em `Página Inicial > Estilos > Título 1`.

### ✅ Deu certo?

🏁 **Ponto de controle:** abra `Exibir > Painel de Navegação` no Word. Você deve ver a hierarquia das
suas seções à esquerda, e ao menos uma delas com texto dentro. A página não está mais em branco.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| A estrutura veio genérica demais | Sua descrição foi genérica. Diga a área, o nível dos alunos e o que a disciplina tem de diferente das outras. |
| O texto colou com fundo cinza e fonte errada | Desfaça com `Ctrl + Z` e cole de novo com colagem especial (passo 5). |
| Veio com `##` e `**` no meio | Peça de novo com "texto puro, sem símbolos de formatação". Para limpar o que já colou, use `Ctrl + H`, procure `##`, substitua por nada. |
| O painel de navegação está vazio | Você digitou os títulos como texto comum. Aplique `Título 1` a cada um. |

> 💡 **Dica:** peça sempre a estrutura antes do texto. Corrigir um índice custa trinta segundos;
> corrigir três páginas escritas na direção errada custa a manhã.

### 🚀 Quer ir além?

1. **Dois públicos, duas estruturas.** Peça a mesma estrutura para alunos e para o colegiado.
   *Deu certo se:* você consegue apontar duas seções que aparecem em uma e não na outra.
2. **A seção que falta.** Cole a sua estrutura ajustada e pergunte: "o que está faltando aqui que um
   leitor esperaria encontrar?". *Deu certo se:* pelo menos uma sugestão fez sentido e entrou.
3. **Pergunte antes de responder.** Peça: "antes de escrever, me faça três perguntas cujas respostas
   melhorariam o texto". *Deu certo se:* você respondeu as três e a versão seguinte ficou melhor.

---

# Oficina 2 — Consertar o parágrafo que não funciona

## Descrição

- **Objetivos da Aula:** ensinar a reescrita com critério declarado e restrição de preservação; e
  ensinar a corrigir o resultado dizendo o que está errado, em vez de pedir outra versão.
- **Habilidades Esperadas:** ao final, você conduz sozinho uma reescrita em duas ou três rodadas,
  preserva a terminologia da sua área, e sabe apontar o que cada rodada corrigiu.

### 🎯 O Problema

Todo texto tem aquele parágrafo. Você reescreveu três vezes, continua pesado, e já não consegue ler
com olhos limpos. Nesta oficina você usa o ChatGPT como segundo par de olhos — e aprende a dizer o
que está errado, que é a parte que faz diferença.

### 🧰 O que você vai usar

- Um parágrafo seu que você não gosta, na cópia de trabalho.
- ChatGPT no navegador.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** conversa do ChatGPT mostrando três mensagens em sequência — a instrução
  inicial com o parágrafo, a primeira resposta, e a mensagem de correção específica do usuário
  ("você tirou o termo X e o segundo período ficou longo"). O encadeamento é o que a captura precisa
  mostrar.

1. Copie o parágrafo problemático da sua cópia de trabalho.

2. No ChatGPT, escreva a instrução **antes** de colar o texto:

   > Reescreva o parágrafo abaixo para ficar mais claro e mais curto. Mantenha os termos técnicos
   > exatamente como estão, preserve todos os números e não mude a ordem dos argumentos.
   >
   > [cole o parágrafo aqui]

3. Leia a resposta. Provavelmente não vai servir de primeira. Tudo bem — é assim mesmo.

4. Agora a parte que importa: em vez de pedir "outra versão", **diga o que está errado**:

   > Ficou bom, mas você tirou o termo "validade ecológica", que é essencial, e o segundo período
   > ficou longo demais. Refaça mantendo o termo e quebrando esse período em dois.

5. Repita o passo 4 quantas vezes precisar. Duas ou três rodadas costumam bastar.

6. Confira os números e as citações do parágrafo contra o original. Reescrever é justamente onde
   número troca de lugar.

7. Cole a versão final no Word, no lugar do parágrafo antigo, com colagem especial.

### ✅ Deu certo?

🏁 **Ponto de controle:** o parágrafo na sua cópia está mais curto que o original, mantém a
terminologia que você usa, todos os números batem, e você consegue dizer em uma frase o que a rodada
final corrigiu.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Todas as versões soam iguais e sem graça | Cole um parágrafo bem escrito seu e peça: "use este como referência de estilo". |
| Ele mudou o sentido do que você disse | Acrescente: "não acrescente nem remova nenhuma afirmação; apenas reformule". |
| Ficou "corporativo" demais | Peça: "escreva como um professor falaria, sem linguagem de relatório empresarial". |
| Um número mudou | Volte ao original e corrija à mão. Depois acrescente à instrução: "preserve todos os números exatamente". |

> ⚠️ **Cuidado:** se o parágrafo contém dado, número ou citação, confira **depois** da reescrita, não
> antes. O passo 6 não é opcional.

### 🚀 Quer ir além?

1. **Três de uma vez.** Peça três versões — uma mais formal, uma mais direta, uma mais curta — e
   escolha. *Deu certo se:* você consegue justificar a escolha em uma frase.
2. **Referência de voz.** Cole dois parágrafos seus como amostra de estilo antes de pedir a
   reescrita. *Deu certo se:* a versão nova soa mais parecida com você que a da rodada 1.
3. **O caminho inverso.** Peça: "aponte o que está errado neste parágrafo, sem reescrever".
   *Deu certo se:* você concorda com pelo menos um dos apontamentos e conserta você mesmo.

---

# Oficina 3 — Trabalhar com o documento inteiro

## Descrição

- **Objetivos da Aula:** ensinar o envio do arquivo `.docx` como alternativa ao copiar e colar;
  mostrar o que se ganha com isso — mapa, resumo por seção, extração de dados; e declarar os limites
  do envio e o que não vai junto.
- **Habilidades Esperadas:** ao final, você envia um documento e obtém dele um mapa e uma extração
  úteis, sabe quantos envios seu plano permite por dia, e sabe que comentários de margem e alterações
  controladas não são vistos pelo sistema.

### 🎯 O Problema

Copiar e colar funciona bem para um parágrafo. Para dezoito páginas, é tortura. E tem perguntas que
só fazem sentido sobre o documento inteiro: "qual é a estrutura disso?", "onde eu repito o mesmo
argumento?", "quais datas aparecem aqui?". Nesta oficina você para de fatiar e manda o arquivo.

### 🧰 O que você vai usar

- A cópia de trabalho, no formato `.docx`.
- ChatGPT no navegador.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** campo de mensagem do ChatGPT com o ícone de anexo destacado e o
  seletor de arquivos aberto, com um arquivo `.docx` selecionado. Uma segunda captura mostrando a
  conversa já com o arquivo anexado acima do campo de texto.

1. Antes de anexar, saiba o seu limite. No plano gratuito são **3 envios de arquivo por dia**. Nos
   planos pagos, até 80 arquivos a cada 3 horas. Um documento de texto do Word não chega perto dos
   limites de tamanho (512 MB por arquivo; 2 milhões de tokens por arquivo de texto).

2. No ChatGPT, clique no ícone de anexo do campo de mensagem e escolha a sua cópia de trabalho.

3. Peça o mapa do documento:

   > Descreva a estrutura deste documento: quais são as seções e o que cada uma trata, em uma frase
   > por seção. Não resuma o conteúdo.

4. Compare com o documento aberto no Word. Costuma revelar seções que você achava que estavam em
   outra ordem.

5. Peça uma extração — a operação que mais economiza tempo e que ninguém usa:

   > Liste todas as datas, todos os números e todos os nomes próprios que aparecem neste documento,
   > organizados por seção.

6. Use essa lista como sua folha de conferência. Cada item dela é uma coisa que você precisa checar
   na fonte antes de enviar o documento.

7. Peça o diagnóstico de repetição:

   > Há ideias repetidas em parágrafos diferentes deste documento? Aponte quais e onde, sem
   > reescrever nada.

8. Agora abra a sua cópia no Word e confira: se ela tem comentários de margem ou alterações
   controladas, o ChatGPT **não** os viu. Ele leu só o texto do corpo.

### ✅ Deu certo?

🏁 **Ponto de controle:** você tem, na conversa, um mapa do documento, uma lista de dados a conferir
e um diagnóstico de repetições. E confirmou que nenhum comentário de margem foi mencionado, ainda
que existam no arquivo.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| "Limite de upload atingido" e você não enviou quase nada | Confirme a conta e o plano. Envios que falharam também contam para o limite. |
| O arquivo não é aceito | Salve como `.docx` em `Arquivo > Salvar como > Documento do Word`. Formatos antigos podem falhar. |
| Ele não mencionou um trecho que existe | Esse trecho provavelmente está em imagem, caixa de texto ou tabela complexa. A leitura é do texto extraído. |
| Ele ignorou os comentários da coorientação | Esperado. Copie o texto dos comentários manualmente para a conversa, junto com o trecho a que se referem. |

> 📌 **Não esqueça:** o que ele lê é o texto, não o arquivo. Formatação, comentários, alterações
> controladas e imagens ficam de fora.

### 🚀 Quer ir além?

1. **Perguntas do leitor.** Peça: "quais são as cinco perguntas mais prováveis de quem ler este
   documento?". *Deu certo se:* o seu texto responde pelo menos três delas — e você anotou as que
   não responde.
2. **Glossário automático.** Peça a lista dos termos técnicos usados e onde cada um aparece pela
   primeira vez. *Deu certo se:* você encontrou pelo menos um termo usado antes de ser definido.
3. **Consistência terminológica.** Pergunte se algum termo está sendo usado de formas diferentes ao
   longo do texto. *Deu certo se:* você padronizou pelo menos uma ocorrência.

---

# Oficina 4 — Encolher sem perder o conteúdo

## Descrição

- **Objetivos da Aula:** ensinar a redução de texto por seção, com tamanho declarado em palavras; e
  mostrar como recuperar informação essencial que foi cortada.
- **Habilidades Esperadas:** ao final, você reduz um texto longo dentro de um limite de palavras
  definido, recupera o que foi cortado indevidamente, e confere que todo número sobreviveu.

### 🎯 O Problema

O relatório tem dezoito páginas e a coordenação pediu duas. Ou o artigo está com nove mil palavras e
o limite da revista é seis mil. Nesta oficina você encolhe texto sem perder o que importa — e sem
perder o controle sobre o que foi perdido.

### 🧰 O que você vai usar

- A cópia de trabalho, com várias seções.
- ChatGPT no navegador.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** duas janelas do Word lado a lado, a original e a reduzida, com a
  contagem de palavras visível na barra de status de cada uma (`Exibir > Contagem de Palavras` ou o
  indicador no rodapé). O contraste entre os dois números é o que a captura precisa mostrar.

1. Vá **por seção**, não pelo documento todo. Reduzir tudo de uma vez sacrifica o que você não
   escolheu.

2. Copie a primeira seção e peça a redução com número explícito em palavras:

   > Reduza o texto abaixo para entre 400 e 450 palavras, sem perder nenhuma informação essencial.
   > Preserve todos os números, datas e nomes próprios exatamente como estão. Texto puro, sem
   > símbolos de formatação.
   >
   > [cole a seção]

3. Diga o tamanho em **palavras**, nunca em proporção. "Metade" é interpretado com folga; "entre 400
   e 450" não.

4. Compare com o original e anote o que ele cortou e que você quer de volta.

5. Devolva com precisão:

   > Faltou a justificativa metodológica do segundo parágrafo. Refaça incluindo isso e cortando a
   > contextualização histórica no lugar, mantendo o mesmo limite de palavras.

6. Repita para as demais seções.

7. Para a abertura do documento reduzido, peça o resumo em formato fechado:

   > Resuma o documento inteiro em cinco itens, cada um com no máximo vinte palavras, sem símbolos
   > de formatação.

8. Monte tudo no Word, reaplique os estilos de título em `Página Inicial > Estilos`, e confira cada
   número contra a versão longa.

### ✅ Deu certo?

🏁 **Ponto de controle:** abra `Exibir > Contagem de Palavras` (ou olhe o rodapé) nos dois arquivos.
A versão reduzida está dentro do limite que você pediu, tem os títulos formatados, e cada número
dela bate com o original.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Resumiu demais e virou esqueleto | Você pediu proporção. Peça em palavras: "entre 400 e 450 palavras". |
| Sumiu informação que você precisava | Devolva com o passo 5: diga o que faltou e o que cortar no lugar. |
| A formatação sumiu ao colar | Esperado. Reaplique em `Página Inicial > Estilos`. |
| Um número mudou entre as versões | Corrija à mão e reforce na instrução: "preserve todos os números exatamente como estão". |

> 💡 **Dica:** ao encolher, os números são o primeiro item de risco, e a justificativa metodológica é
> o segundo. São as duas coisas que o sistema considera "detalhe".

### 🚀 Quer ir além?

1. **Duas reduções, dois públicos.** Reduza a mesma seção para o colegiado e para o público leigo.
   *Deu certo se:* você identifica o que cada versão sacrificou.
2. **O corte reverso.** Peça: "o que você cortaria se o limite fosse a metade disto?".
   *Deu certo se:* a lista revela o que você considera essencial e ele não.
3. **Resumo em uma frase.** Peça o documento inteiro em uma única frase de no máximo trinta
   palavras. *Deu certo se:* a frase serve como abertura do documento.

---

# Projeto Final — Virar um documento do avesso

## Descrição

- **Objetivos da Aula:** exigir o encadeamento das quatro operações em uma sequência que nenhuma
  oficina cobriu isoladamente — converter um documento existente em outro gênero, para outro público.
- **Habilidades Esperadas:** ao final, você produz sozinho um documento novo a partir de um
  existente, com estrutura própria, registro ajustado ao novo público, revisão feita e todo dado
  factual conferido.

### 🎯 A missão

Não é escrever mais um documento. É pegar um documento que já existe e **transformá-lo em outro**,
para outro leitor.

Escolha um par real da sua rotina:

- Um relatório de projeto de vinte páginas → um comunicado de duas páginas para o colegiado.
- Um artigo submetido → um texto de divulgação para o site do departamento.
- Um plano de ensino detalhado → uma orientação de uma página para os alunos.
- Um parecer técnico → um resumo executivo para a direção.

O documento de destino tem outro leitor, outro tamanho, outro tom e outra estrutura. É por isso que
as oficinas isoladas não bastam: você vai precisar de todas, em ordem, e de uma decisão sua a cada
etapa.

### 🧰 O que você vai usar

- O documento de origem (uma cópia dele).
- ChatGPT no navegador.
- Um documento novo, em branco, no Word.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** três janelas visíveis — o documento de origem no Word, a conversa do
  ChatGPT com o arquivo anexado, e o documento de destino em branco. A captura precisa mostrar a
  transformação em curso, não o resultado.

1. **Envie o documento de origem** (Oficina 3) e peça o mapa e a lista de dados factuais.

2. **Peça a estrutura do documento de destino**, declarando o novo público:

   > Com base no documento anexado, proponha a estrutura de um comunicado de duas páginas para o
   > colegiado do departamento. Só os títulos das seções. O leitor não acompanhou o projeto e
   > precisa decidir se aprova a continuidade.

3. **Ajuste a estrutura.** Corte, reordene, acrescente. Esta decisão é sua e nenhuma ferramenta a
   toma.

4. **Escreva seção por seção** (Oficina 1), sempre declarando público, extensão e registro do
   documento de **destino**, não do de origem.

5. **Reescreva as duas seções mais fracas** (Oficina 2), com critério declarado e restrição de
   preservação, corrigindo por rodadas.

6. **Reduza o que estourou** (Oficina 4), em palavras, seção por seção.

7. **Passe a revisão de diagnóstico:**

   > Leia o texto abaixo e aponte as frases confusas, longas demais ou mal estruturadas. Para cada
   > uma, sugira uma versão melhor. Não reescreva o texto inteiro.

8. **Confira todo dado factual** contra o documento de origem, usando a lista de extração do passo 1.
   Um por um.

9. **Monte no Word**, aplique os estilos, e leia o documento inteiro em voz alta. Isso pega o que
   nenhuma ferramenta pega.

10. **Anote**, no seu caderninho, as três instruções que funcionaram melhor.

### 🏁 Como saber que terminou

- [ ] O documento de destino existe, no Word, com estilos de título aplicados.
- [ ] A estrutura dele é diferente da do documento de origem — não é um resumo do original.
- [ ] Cada seção foi escrita declarando o público de destino.
- [ ] Pelo menos duas seções passaram por rodadas de reescrita com critério declarado.
- [ ] Nenhum símbolo de Markdown sobrou no texto.
- [ ] Todo número, data, nome próprio e referência foi conferido contra o documento de origem.
- [ ] Nenhum dado identificável de aluno ou informação sigilosa entrou no ChatGPT.
- [ ] Você leu o documento inteiro em voz alta.
- [ ] Você respondeu, para si, se este documento precisa declarar o uso de IA.
- [ ] Você tem três instruções anotadas para reusar.

---

# A Parte dos Dez — Instruções que Salvam seu Dia

1. **Estrutura antes de texto.** "Sugira as seções deste documento, sem escrever o conteúdo."
2. **Diga o tamanho em palavras**, não em proporção. "Entre 400 e 450 palavras" funciona; "mais
   curto" não.
3. **Declare o que não pode mudar.** "Preserve os termos técnicos, todos os números e a ordem dos
   argumentos."
4. **Peça o plano antes da edição grande.** "Antes de reescrever, diga o que pretende mudar e por
   quê."
5. **Dê uma amostra da sua voz.** Cole um parágrafo seu bem escrito: "use como referência de
   estilo".
6. **Diga o que está errado, não peça 'de novo'.** Retorno específico produz correção específica.
7. **Peça extração antes de conferência.** "Liste todas as datas e números deste documento, por
   seção." Vira a sua folha de checagem.
8. **Peça sem Markdown.** "Texto puro, sem símbolos de formatação, pronto para colar no Word."
9. **Cole especial.** `Página Inicial > Colar > Colar Especial > Texto não formatado` no desktop;
   `Colar > Manter somente texto` na web. E `Ctrl + H` limpa o que sobrou.
10. **Confira todo número.** É a única regra que não tem exceção.

## Conseguiu! E agora?

Você saiu daqui com um documento novo, feito a partir de um antigo, e com um repertório de instruções
que funcionam para o seu tipo de texto. Isso é o que realmente se leva: não a ferramenta, mas o jeito
de falar com ela — e a noção clara de onde ela para e você começa.

O próximo passo é repetir. Escolha um documento por semana durante um mês e faça o ciclo completo.
Ao fim desse mês a instrução sai pronta, sem você pensar. E você vai ter descoberto também onde a
ferramenta atrapalha mais do que ajuda, que é uma descoberta tão valiosa quanto a outra.
