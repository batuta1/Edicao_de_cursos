# Plano de Aula — ChatGPT no Word (Essentials)

## Identificação

| Campo | Definição |
|---|---|
| Curso | ChatGPT no Word — Essentials |
| Natureza | Curto, introdutório, prático e autoinstrucional |
| Carga horária | 100 a 130 minutos |
| Público-alvo | Professores universitários, novatos em inteligência artificial generativa |
| Pré-requisitos | Uso básico do Word; conta no ChatGPT; nenhum conhecimento prévio de IA |
| Recursos necessários | Computador com Word instalado ou Word na web; navegador; internet; conta ChatGPT |

### Objetivo Geral

O curso destina-se a habilitar o docente do ensino superior a empregar o ChatGPT como assistente de
redação na produção de documentos do Microsoft Word, compreendendo os caminhos de integração
disponíveis, os critérios de formulação de instruções eficazes e os limites de confiabilidade da
ferramenta. Ao término, espera-se que o participante disponha de um repertório mínimo de
procedimentos aplicáveis à sua rotina de escrita acadêmica e administrativa, bem como de um
documento próprio revisado com o apoio da ferramenta.

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Distinguir os caminhos disponíveis de uso do ChatGPT com documentos do Word e selecionar o mais
   adequado a cada tarefa.
2. Formular instruções que produzam texto utilizável, especificando propósito, público, extensão e
   registro.
3. Empregar o ChatGPT nas quatro operações mais frequentes da escrita acadêmica: redigir, reescrever,
   resumir e estruturar.
4. Avaliar criticamente o resultado produzido, identificando erros factuais, generalidade de tom e
   repetição.

### Estrutura e Sequência dos Módulos

Os módulos observam progressão cumulativa: o primeiro estabelece o repertório conceitual mínimo, o
segundo trata da formulação de instruções, o terceiro e o quarto aplicam esse repertório às
operações de escrita, e o quinto integra as competências em uma atividade única.

| Módulo | Título | Referência (material-fonte) | Tempo |
|---|---|---|---|
| 1 | O que o ChatGPT faz com um documento do Word | Central de Ajuda da OpenAI; guia de uso com Word | 25 min |
| 2 | A anatomia de uma boa instrução | Guia de uso com Word (seção de prompts) | 25 min |
| 3 | Redigir e reescrever | Guia de uso com Word (casos de uso) | 25 min |
| 4 | Resumir, estruturar e revisar | Guia de uso com Word; FAQ de uploads | 25 min |
| 5 | Síntese e Aplicação Integrada | — | 20 min |

---

# Módulo 1 — O que o ChatGPT faz com um documento do Word

> Ponto de partida do curso: estabelece o repertório conceitual mínimo sobre o qual todos os módulos
> seguintes se apoiam.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Definir, em termos operacionais, o que é um modelo de linguagem e o que ele produz.
2. Distinguir os caminhos de uso do ChatGPT com documentos do Word.
3. Reconhecer que não há integração nativa da OpenAI no Microsoft Word.

### Texto Descritivo

Convém iniciar por uma definição operacional. Um modelo de linguagem é um sistema computacional
treinado para prever, a partir de um texto recebido, qual continuação é mais provável. Dessa
descrição decorre a consequência mais importante para o trabalho acadêmico: o sistema produz o texto
mais plausível, e não necessariamente o mais verdadeiro. A plausibilidade é uma propriedade da
forma; a verdade é uma propriedade do conteúdo. O ChatGPT é excelente na primeira e não oferece
garantia sobre a segunda.

Cumpre registrar, em seguida, um ponto que costuma gerar frustração. Não existe, no momento da
redação deste material, suplemento oficial da OpenAI para o Microsoft Word. Existe suplemento
oficial para o Excel e para o PowerPoint; para o Word, não. O participante que procurar uma barra
lateral do ChatGPT dentro do Word, semelhante à do Microsoft Copilot, não a encontrará.

Disso não decorre, contudo, que o ChatGPT seja inútil para quem escreve no Word. Decorre apenas que
o trabalho se dá por outros caminhos, três dos quais interessam ao presente curso. O primeiro é o
fluxo de copiar e colar: o docente redige a instrução no navegador, cola o trecho a ser trabalhado,
copia o resultado e o traz de volta ao documento. É o caminho universal, que funciona em qualquer
versão do Word e em qualquer plano do ChatGPT, inclusive o gratuito.

O segundo caminho consiste em enviar o próprio arquivo `.docx` ao ChatGPT. O sistema lê arquivos do
Word com boa fidelidade, extraindo o texto do corpo do documento. Observa-se, todavia, uma limitação
relevante: o que é enviado é o texto extraído. Comentários de margem e marcas de alterações
controladas não são preservados, de modo que a conversa de revisão que ocorre no documento
permanece invisível ao sistema.

O terceiro caminho é a solicitação de um arquivo pronto. O ChatGPT pode gerar um documento `.docx`
para download, produzido a partir de instruções ou de material de origem anexado. A disponibilidade
desse recurso varia conforme o plano contratado e as configurações do espaço de trabalho, razão pela
qual convém verificá-la na própria conta antes de planejar um trabalho em torno dele.

### Exercício Prático

**Identificação do caminho adequado (6 min)**

Considere a seguinte situação: o docente precisa reduzir pela metade a seção de metodologia de um
projeto de pesquisa, com dezoito páginas, mantendo a formatação de títulos e a numeração das
figuras. Qual caminho é o mais adequado?

- (a) Copiar e colar a seção inteira no ChatGPT e trazer o resultado de volta.
- (b) Enviar o `.docx` completo e pedir a redução, esperando receber o arquivo formatado de volta.
- (c) Trabalhar por partes, copiando e colando um subtítulo por vez, e reaplicando os estilos no
  Word.
- (d) Pedir ao ChatGPT que gere um novo `.docx` já reduzido.

**Gabarito:** (c).

**Fundamentação:** documentos longos produzem melhores resultados quando trabalhados em partes,
porque a instrução pode ser específica para cada trecho. A alternativa (b) falha porque a formatação
não sobrevive ao envio; a (d) falha porque o arquivo gerado não herda os estilos do original.

---

# Módulo 2 — A anatomia de uma boa instrução

> Pressupõe o repertório do Módulo 1 e desloca o foco do que a ferramenta é para como se fala com
> ela.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Enumerar os quatro elementos que compõem uma instrução eficaz.
2. Reescrever uma instrução vaga em uma instrução específica.
3. Reconhecer o valor de solicitar um plano antes de uma alteração extensa.

### Texto Descritivo

A qualidade do resultado depende diretamente da qualidade da instrução. Denomina-se instrução — ou,
no jargão corrente, *prompt* — o texto que o usuário fornece ao sistema descrevendo o que deseja.
Observa-se que a instrução vaga produz o texto genérico, ao passo que a instrução específica produz
o texto utilizável.

Quatro elementos costumam ser suficientes. O primeiro é a **tarefa**: o verbo que descreve a
operação pretendida — redigir, reescrever, resumir, estruturar, revisar. O segundo é o **público**:
para quem o texto se destina, uma vez que o mesmo conteúdo se escreve de modo diverso para o
colegiado, para o aluno ingressante e para a agência de fomento. O terceiro é a **extensão**: número
de palavras, de parágrafos ou de itens, conforme o caso. O quarto é o **registro**: formal ou
acessível, técnico ou divulgativo, impessoal ou direto.

Recomenda-se, ademais, informar explicitamente o que **não** deve mudar. Em uma reescrita, convém
declarar que a terminologia técnica deve ser preservada, que as citações não devem ser alteradas e
que a ordem dos argumentos deve permanecer. A ausência dessa instrução autoriza o sistema a
reorganizar o texto de maneiras que o autor não pretendia.

Para alterações extensas, recomenda-se solicitar um plano antes da execução. A formulação "antes de
reescrever, descreva o que pretende alterar e por quê" transfere ao docente a decisão sobre o
escopo, evitando que o sistema produza uma versão inteira em direção equivocada.

### Exercício Prático

**Reescrita de instrução (6 min)**

1. Considere a instrução: "melhore este parágrafo".
2. Reescreva-a acrescentando os quatro elementos apresentados, tomando como situação a introdução de
   um plano de ensino destinado a alunos de primeiro período.
3. Compare a sua formulação com o modelo abaixo.

Modelo de referência:

"""
Reescreva o parágrafo abaixo para a introdução de um plano de ensino destinado a alunos de primeiro
período. O texto deve ser acessível, sem jargão de área, com no máximo cento e vinte palavras.
Preserve os nomes das disciplinas e a ordem dos tópicos.

[colar o parágrafo]
"""

**Critério de êxito:** a instrução redigida pelo participante contém os quatro elementos (tarefa,
público, extensão, registro) e ao menos uma restrição de preservação.

---

# Módulo 3 — Redigir e reescrever

> Pressupõe o Módulo 2 e desloca o foco da formulação da instrução para a sua aplicação nas duas
> operações mais frequentes da escrita.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Empregar o ChatGPT para produzir uma primeira versão de texto a partir de descrição.
2. Solicitar reescritas orientadas por um critério declarado.
3. Ajustar o registro de um texto entre o formal e o acessível.

### Texto Descritivo

A primeira operação é a redação de uma versão inicial. A página em branco é reconhecidamente o
obstáculo mais custoso da escrita, e a função do sistema aqui é removê-lo. O texto produzido
raramente é adequado como resultado final, mas raramente precisa ser: é mais rápido corrigir uma
versão imperfeita do que produzir uma do zero. Convém, portanto, tratar o resultado como matéria
bruta, e não como produto.

A segunda operação é a reescrita. Cola-se o trecho que não funciona e solicita-se a reformulação
segundo um critério explícito: mais claro, mais curto, mais direto, mais formal. Caso a primeira
reformulação não sirva, recomenda-se declarar o que está errado nela, em vez de solicitar
genericamente outra versão. A instrução "está longo demais e perdeu o termo técnico X" produz
resultado superior à instrução "tente de novo".

Cumpre observar, quanto ao registro, que o sistema tende a um tom neutro e vagamente corporativo.
Esse tom é reconhecível e destoa da voz de um docente experiente. Recomenda-se, por isso, ajustar o
resultado antes de qualquer uso externo, ou fornecer ao sistema um parágrafo do próprio autor como
referência de voz.

### Exercício Prático

**Reescrita de um parágrafo próprio (6 min)**

1. Selecione, em um documento seu, um parágrafo que considere mal resolvido.
2. Solicite ao ChatGPT que o reescreva, declarando o critério e ao menos uma restrição de
   preservação.
3. Avalie o resultado e solicite uma segunda versão, declarando o que a primeira não resolveu.
4. Traga a versão escolhida ao Word.

**Critério de êxito:** o parágrafo final está no documento, mantém a terminologia original e o
participante consegue apontar o que a segunda instrução corrigiu em relação à primeira.

---

# Módulo 4 — Resumir, estruturar e revisar

> Pressupõe o Módulo 3 e amplia o repertório às operações que trabalham sobre o documento como um
> todo.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Solicitar resumos com formato e extensão determinados.
2. Obter uma proposta de estrutura para um documento ainda não escrito.
3. Empregar o sistema como revisor, identificando o que a revisão automática não alcança.

### Texto Descritivo

A operação de resumo consiste em reduzir a extensão preservando o conteúdo essencial. Sua utilidade
para o docente é ampla: sínteses de artigos para a preparação de aula, resumos executivos de
relatórios de projeto, ementas condensadas a partir de planos extensos. Convém sempre especificar o
formato pretendido — parágrafo corrido, número determinado de itens, tabela — porque o formato
padrão do sistema tende à lista, nem sempre adequada.

A operação de estruturação atua antes da escrita. Descreve-se o documento pretendido e solicita-se
uma proposta de seções. O resultado deve ser tomado como ponto de partida sujeito a reordenação:
serve para vencer a indecisão inicial, não para substituir o julgamento do autor sobre a arquitetura
do próprio texto.

A operação de revisão exige a cautela mais explícita. O sistema identifica com facilidade
construções obscuras, períodos excessivamente longos e inconsistências de terminologia. Não
identifica, contudo, erro factual do próprio autor, e pode introduzir erro factual novo. Toda
afirmação numérica, toda data, toda referência bibliográfica e toda menção a legislação devem ser
conferidas de forma independente. Depreende-se daí que o sistema é auxiliar de forma, não fiador de
conteúdo.

Registre-se, por fim, uma questão de formatação. O resultado costuma vir marcado com símbolos de
Markdown — cerquilhas para títulos, asteriscos para negrito, hifens para listas — que não se
convertem automaticamente ao serem colados no Word. Recomenda-se solicitar explicitamente texto sem
esses símbolos, ou empregar o recurso de localizar e substituir do Word para removê-los.

### Exercício Prático

**Resumo com formato determinado (6 min)**

1. Selecione um texto seu de ao menos duas páginas.
2. Solicite um resumo em exatamente cinco itens, cada um com no máximo vinte palavras, sem símbolos
   de Markdown.
3. Confira se o número de itens e o limite de palavras foram respeitados.
4. Verifique se algum dado numérico presente no resumo corresponde ao original.

**Critério de êxito:** o resumo tem cinco itens, respeita o limite de palavras, cola no Word sem
símbolos estranhos, e o participante conferiu ao menos um dado numérico contra o texto original.

---

# Módulo 5 — Síntese e Aplicação Integrada

> Pressupõe todos os módulos anteriores e os articula em uma única atividade de produção.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Encadear as quatro operações de escrita em um fluxo de trabalho único.
2. Aplicar critérios de verificação sobre um documento produzido com apoio da ferramenta.
3. Julgar quando o apoio da ferramenta é apropriado e quando não é.

### Texto Descritivo

Cumpre, ao final, articular o que foi tratado de modo disperso. As quatro operações — redigir,
reescrever, resumir, estruturar — não são procedimentos isolados, mas etapas de um mesmo fluxo. Um
documento típico começa por uma estrutura proposta, prossegue por versões iniciais de cada seção,
passa por reescritas orientadas e termina por um resumo executivo.

Observa-se que a etapa de verificação não é uma quinta operação a ser acrescentada ao fim, mas uma
disposição que acompanha todas as demais. Cada trecho produzido com apoio do sistema carrega o risco
de conter afirmação plausível e falsa. A responsabilidade sobre o texto assinado permanece
integralmente com o docente.

Convém, por último, delimitar o que não deve ser feito. Não se deve inserir no sistema dado
identificável de aluno, resultado de pesquisa não publicado, parecer sigiloso de avaliação por pares
ou informação submetida a compromisso de confidencialidade. Essa restrição não deriva de suspeita
sobre a ferramenta, mas do fato de que o conteúdo enviado é processado por servidores de terceiros e
pode, conforme o plano contratado, ser empregado no aperfeiçoamento dos modelos.

### Exercício Prático

**Atividade Integradora — produção de um documento completo (10 min)**

1. Escolha um documento curto de sua rotina: um comunicado ao colegiado, uma orientação de
   atividade, um resumo de projeto.
2. Solicite ao ChatGPT uma proposta de estrutura em seções.
3. Escreva ou solicite uma versão inicial da seção mais longa.
4. Solicite uma reescrita dessa seção com critério declarado.
5. Solicite um resumo do documento em três frases.
6. Monte o documento no Word e confira todo dado factual.

**Critérios de avaliação**

| Critério | Atendido? |
|---|---|
| A estrutura foi solicitada com público e finalidade declarados | |
| A instrução de reescrita continha critério e restrição de preservação | |
| O resumo respeita o formato pedido | |
| Nenhum dado identificável de aluno foi inserido no sistema | |
| Todo dado numérico ou referência foi conferido contra a fonte | |
| O documento final está no Word, sem símbolos de Markdown | |

---

# Encerramento

O curso cumpriu a finalidade de estabelecer um repertório mínimo e verificável de uso do ChatGPT na
produção de documentos do Word. Recomenda-se prática regular sobre documentos reais de trabalho, uma
vez que a competência aqui tratada se consolida pelo uso e não pela leitura. Sugere-se que o
participante mantenha, ao longo das primeiras semanas, um registro das instruções que produziram bom
resultado, formando um repertório próprio.

Apontam-se, como caminhos de aprofundamento, o uso de arquivos de referência e modelos reutilizáveis
para trabalhos recorrentes, a exploração dos recursos de leitura de arquivos para análise de
material de terceiros, e o estudo comparado com as demais ferramentas de escrita assistida
disponíveis no ambiente institucional.

> **Síntese:** a ferramenta escreve; a responsabilidade pelo que está escrito permanece de quem
> assina.
