# Plano de Aula — ChatGPT no PowerPoint (Essentials)

## Identificação

| Campo | Definição |
|---|---|
| Curso | ChatGPT no PowerPoint — Essentials |
| Natureza | Curto, introdutório, prático e autoinstrucional |
| Carga horária | 100 a 130 minutos |
| Público-alvo | Professores universitários, novatos em inteligência artificial generativa |
| Pré-requisitos | Uso básico do PowerPoint; conta no ChatGPT; nenhum conhecimento prévio de IA |
| Recursos necessários | Computador com PowerPoint compatível com suplementos do Office; internet; conta ChatGPT |

### Objetivo Geral

O curso destina-se a habilitar o docente do ensino superior a empregar o suplemento ChatGPT para
PowerPoint na produção e no aperfeiçoamento de apresentações, compreendendo o processo de
instalação, os critérios de formulação de instruções e as limitações declaradas da ferramenta. Ao
término, espera-se que o participante disponha de procedimentos aplicáveis à preparação de aulas,
bancas e comunicações institucionais.

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Instalar o suplemento ChatGPT para PowerPoint e reconhecer sua interface.
2. Produzir um primeiro rascunho de apresentação a partir de material de origem.
3. Solicitar alterações em apresentação existente delimitando o escopo da edição.
4. Avaliar criticamente o resultado, identificando desvios de modelo e erros factuais.

### Estrutura e Sequência dos Módulos

Os módulos observam progressão cumulativa: o primeiro apresenta a ferramenta, o segundo trata da
instalação, o terceiro e o quarto aplicam a ferramenta à criação e à edição, e o quinto integra as
competências.

| Módulo | Título | Referência (material-fonte) | Tempo |
|---|---|---|---|
| 1 | O que é o ChatGPT para PowerPoint | Central de Ajuda da OpenAI | 25 min |
| 2 | Instalação e primeiro contato | Central de Ajuda da OpenAI — instalação | 25 min |
| 3 | Criar uma apresentação a partir de material de origem | Central de Ajuda da OpenAI — como usar bem | 25 min |
| 4 | Editar uma apresentação existente | Central de Ajuda da OpenAI — prompts e limitações | 25 min |
| 5 | Síntese e Aplicação Integrada | — | 20 min |

---

# Módulo 1 — O que é o ChatGPT para PowerPoint

> Ponto de partida do curso: estabelece o que a ferramenta é e o que ela se propõe a fazer.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Definir o que é o ChatGPT para PowerPoint e onde ele opera.
2. Enumerar as quatro operações que a ferramenta se propõe a realizar.
3. Reconhecer as limitações declaradas pelo fabricante.

### Texto Descritivo

O ChatGPT para PowerPoint é uma experiência de inteligência artificial nativa do PowerPoint, que se
apresenta na forma de uma barra lateral dentro do próprio aplicativo. Diferentemente do trabalho
feito no navegador, em que o texto precisa ser transportado de um lado para o outro, aqui o sistema
opera sobre a apresentação aberta, preservando a estrutura editável dos slides.

Quatro operações são anunciadas: criar, editar, entender e refinar apresentações. Criar significa
produzir um primeiro rascunho a partir de material de origem — anotações, documentos, planilhas.
Editar significa acrescentar ou revisar slides em uma apresentação existente. Entender significa
formular perguntas sobre a narrativa e a estrutura de uma apresentação. Refinar significa ajustar a
apresentação a um público específico.

Observa-se que essas quatro operações correspondem de perto às necessidades do trabalho docente. A
transformação de um artigo em uma aula, a atualização de um conjunto de slides do semestre anterior,
a adaptação de uma apresentação de congresso para uma banca — todas são instâncias das operações
descritas.

Cumpre registrar as limitações que o próprio fabricante declara. A primeira diz respeito à aderência
a modelos: embora o produto tenha sido desenvolvido para trabalhar com modelos de apresentação
existentes, os slides gerados nem sempre correspondem perfeitamente ao estilo pretendido. A segunda
diz respeito a edições avançadas: recursos de gráficos, formas, formatação e gerenciamento de slides
podem ser limitados. A terceira, e mais importante, diz respeito à confiabilidade: os resultados
podem estar incompletos ou incorretos, e devem ser revistos antes de qualquer uso.

Registre-se, por fim, uma advertência de peso: o sistema pode editar ou excluir conteúdo da
apresentação. Recomenda-se, para trabalhos importantes, duplicar o arquivo antes de iniciar, de modo
a permitir a reversão.

### Exercício Prático

**Identificação da operação (6 min)**

Considere: o docente tem uma apresentação de quarenta slides usada em congresso e precisa de uma
versão de quinze slides para uma banca de qualificação. Qual operação descreve melhor a tarefa?

- (a) Criar
- (b) Editar
- (c) Entender
- (d) Refinar

**Gabarito:** (d).

**Fundamentação:** trata-se de ajustar uma apresentação existente a um público específico, que é a
definição de refinar. A operação envolverá edições, mas a finalidade governa a classificação.

---

# Módulo 2 — Instalação e primeiro contato

> Pressupõe o Módulo 1 e desloca o foco do que a ferramenta é para como obtê-la.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Instalar o suplemento pelo Marketplace da Microsoft.
2. Reconhecer o caminho alternativo de implantação por administrador.
3. Localizar as Skills e os apps na interface do suplemento.

### Texto Descritivo

A instalação se dá pelo Marketplace da Microsoft, a partir do próprio PowerPoint. O procedimento
compreende abrir o aplicativo, acessar a Página Inicial, acessar Suplementos, pesquisar por ChatGPT,
adicionar o suplemento e abri-lo pela faixa de opções. Em seguida, é necessário entrar com a conta
do ChatGPT que possua acesso.

Nem toda organização permite o acesso à loja da Microsoft para este suplemento. Nesses casos, um
administrador do Microsoft 365 pode implantá-lo internamente por meio do arquivo XML de manifesto,
pelo centro de administração, na seção de aplicativos integrados. O procedimento compreende
selecionar a implantação de suplemento, carregar aplicativos personalizados, carregar o arquivo de
manifesto e atribuí-lo aos usuários ou grupos apropriados. Organizações que empregam controle de
acesso baseado em funções podem exigir habilitação adicional.

Uma vez instalado, o suplemento abre uma barra lateral. Nela, o símbolo de adição dá acesso às
Skills e aos apps. Skills são descritas como playbooks reutilizáveis para o trabalho com
apresentações: codificam fluxos de trabalho, regras de estilo, expectativas de formatação e
estruturas de saída, de modo que a mesma instrução não precise ser recriada a cada vez. Apps
conectam o sistema a fontes de dados e ações aprovadas. A disponibilidade de ambos depende do plano,
do espaço de trabalho e das permissões concedidas.

### Exercício Prático

**Instalação (6 min)**

1. Abra o PowerPoint.
2. Percorra o caminho de instalação descrito acima.
3. Entre com a conta do ChatGPT.
4. Localize o símbolo de adição na barra lateral.

**Critério de êxito:** a barra lateral do ChatGPT está visível dentro do PowerPoint e o participante
localizou o acesso às Skills.

---

# Módulo 3 — Criar uma apresentação a partir de material de origem

> Pressupõe o Módulo 2 e desloca o foco da instalação para o uso mais frequente da ferramenta.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Fornecer material de origem ao sistema.
2. Especificar seções, tipos de slide e verificações esperadas.
3. Avaliar a correspondência entre o resultado e o material fornecido.

### Texto Descritivo

O uso mais produtivo da ferramenta é a produção de um primeiro rascunho a partir de material que já
existe. Para o docente, esse material costuma ser um artigo, um capítulo, um plano de ensino, um
conjunto de anotações ou uma planilha de resultados.

Recomenda-se descrever, além do conteúdo, a forma pretendida. Para uma apresentação, convém indicar
as seções esperadas, os tipos de slide e as verificações visuais que serão feitas. Uma instrução que
declare "dez slides, com um slide de abertura, três seções de conteúdo e um slide de conclusão"
produz resultado mais próximo do pretendido do que uma instrução que apenas descreva o assunto.

Convém igualmente declarar o que deve permanecer inalterado. A formulação recomendada pelo
fabricante inclui a indicação explícita do que preservar: o estilo da apresentação, a ordem dos
slides, a estrutura das tabelas.

Observa-se que o resultado é um rascunho, e não um produto. A revisão das afirmações, dos números e
das alterações é responsabilidade do participante, e deve ocorrer antes de qualquer uso.

### Exercício Prático

**Primeiro rascunho (6 min)**

1. Selecione um documento seu de origem.
2. Solicite ao ChatGPT no PowerPoint a produção de um rascunho, declarando o número de slides, as
   seções e o público.
3. Percorra os slides produzidos.
4. Verifique se algum dado numérico corresponde ao material de origem.

**Critério de êxito:** existe uma apresentação com o número de slides pedido, e o participante
conferiu ao menos um dado contra a origem.

---

# Módulo 4 — Editar uma apresentação existente

> Pressupõe o Módulo 3 e desloca o foco da criação para a intervenção em material já pronto.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Delimitar o escopo de uma edição.
2. Solicitar um plano antes de uma alteração extensa.
3. Formular perguntas sobre a narrativa da apresentação.

### Texto Descritivo

A edição de apresentação existente exige mais cuidado do que a criação, porque há trabalho anterior
a preservar. A recomendação do fabricante é ser específico sobre o que se quer alterar, o que se
quer preservar e onde a edição deve acontecer. A formulação de referência é do tipo "acrescente um
slide de riscos após a visão geral, mantenha o estilo desta apresentação e não altere os slides ao
redor".

Para edições maiores, recomenda-se solicitar um plano antes da execução: "antes de editar, descreva
quais slides você mudaria e por quê". O procedimento permite ao docente aprovar ou recusar o escopo
antes que a apresentação seja modificada.

A operação de entender merece registro à parte, por ser a menos óbvia e das mais úteis. É possível
formular perguntas sobre a apresentação: qual é a narrativa, onde estão as lacunas, que perguntas o
público provavelmente fará. Para quem prepara uma banca ou uma defesa, essa consulta antecipa a
arguição.

Cumpre reiterar que o sistema pode editar ou excluir conteúdo. A recomendação de duplicar o arquivo
antes de trabalhos importantes é do próprio fabricante e deve ser seguida.

### Exercício Prático

**Edição delimitada (6 min)**

1. Abra uma apresentação sua.
2. Solicite uma alteração pontual, declarando o local, o que preservar e o que não tocar.
3. Confira os slides vizinhos ao alterado.

**Critério de êxito:** a alteração ocorreu no local pedido e os slides vizinhos permaneceram
inalterados.

---

# Módulo 5 — Síntese e Aplicação Integrada

> Pressupõe todos os módulos anteriores e os articula em uma única atividade.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Encadear criação, edição e consulta em um fluxo único.
2. Aplicar critérios de verificação sobre a apresentação produzida.
3. Julgar quando o apoio da ferramenta é apropriado.

### Texto Descritivo

Cumpre articular o que foi tratado. As quatro operações formam um ciclo: cria-se o rascunho a partir
do material de origem, edita-se o que não corresponde ao pretendido, consulta-se a narrativa em
busca de lacunas e refina-se para o público específico.

Observa-se que a verificação atravessa todas as etapas. Cada afirmação, número e citação presente na
apresentação é de responsabilidade de quem a apresenta, e o sistema não oferece garantia sobre
nenhum deles.

Convém, por último, delimitar o que não deve ser enviado. Dados identificáveis de aluno, resultados
não publicados e informações sob confidencialidade não devem constar de apresentações submetidas ao
sistema, uma vez que o conteúdo é processado por terceiros.

### Exercício Prático

**Atividade Integradora — uma apresentação completa (10 min)**

1. Escolha um material de origem seu.
2. Produza um rascunho declarando seções, número de slides e público.
3. Solicite uma edição delimitada em um dos slides.
4. Pergunte quais lacunas a apresentação tem.
5. Confira todos os dados.

**Critérios de avaliação**

| Critério | Atendido? |
|---|---|
| O rascunho foi solicitado com seções e público declarados | |
| A edição declarou o que preservar | |
| A consulta sobre lacunas foi feita | |
| Todo dado numérico foi conferido | |
| Nenhum dado sensível foi enviado ao sistema | |

---

# Encerramento

O curso cumpriu a finalidade de estabelecer um repertório mínimo de uso do ChatGPT para PowerPoint
na preparação de apresentações acadêmicas. Recomenda-se prática regular sobre material real, uma vez
que a competência se consolida pelo uso.

Apontam-se, como caminhos de aprofundamento, o uso de Skills para fluxos repetidos, a conexão de
apps a fontes de dados aprovadas, e a comparação com as demais ferramentas disponíveis no ambiente
institucional.

> **Síntese:** o sistema monta os slides; a apresentação continua sendo de quem sobe ao palco.
