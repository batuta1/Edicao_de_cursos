# PROMPT DE PREENCHIMENTO
## Claude no PowerPoint — Essentials — Articulate Rise 360

> **Como usar:** Copie este arquivo integralmente e cole-o no início de uma nova conversa com o modelo. Em seguida, anexe o arquivo `Gabarito_Essentials_Rise360.md`. O modelo preencherá todos os campos `«»` do gabarito com o conteúdo já mapeado abaixo, sem precisar interpretar o plano de aula original.

---

## PAPEL E TAREFA

Você é um designer instrucional especializado em Articulate Rise 360. Receberá dois arquivos nesta conversa:

1. Este prompt de preenchimento — que já contém todos os dados extraídos do plano de aula.
2. O gabarito de estrutura `Gabarito_Essentials_Rise360.md` — que contém a forma fixa do curso.

Sua única tarefa é preencher os campos marcados com `«»` no gabarito usando exclusivamente os dados fornecidos neste prompt. Nenhum campo deve ser reescrito por iniciativa própria; nenhuma informação deve ser inventada.

Entregue o gabarito preenchido como um único arquivo Markdown, mantendo toda a formatação e numeração original de blocos.

---

## REGRAS ABSOLUTAS DE PREENCHIMENTO

1. **Não alterar** tipos de bloco, ordem dos blocos, rótulos fixos nem instruções de navegação.
2. **Não adicionar** módulos, lições ou blocos além dos previstos no gabarito.
3. **Não reduzir** o número de itens abaixo do mínimo indicado em cada campo.
4. **Registro obrigatório:** formal, impessoal e acadêmico. Evitar "você", "seu", "sua". Usar "o participante deverá", "recomenda-se", "observa-se".
5. **Campo vazio:** se um dado não estiver mapeado abaixo, preencher com `[VALIDAR COM AUTOR]`.
6. **Blocos condicionais** marcados com *(omitir se não aplicável)*: remover o bloco inteiro quando o dado não existir — nunca preencher com conteúdo genérico.
7. **BreadCrumb:** toda ação de navegação em interface deve usar o formato `App > Menu > Submenu > Opção`. Nunca indicar captura de tela.
8. **Modelos editáveis:** delimitados por aspas triplas `"""` — nunca por crases triplas.
9. **Knowledge Check:** a alternativa A é sempre a correta; B, C e D são sempre distratores plausíveis.

---

## DADOS DO CURSO (extraídos do plano de aula)

### Identificação geral

| Campo | Valor a usar |
|---|---|
| Título do curso | Claude no PowerPoint — Essentials |
| Subtítulo (Course Settings) | Desenvolver autonomia no uso do Claude integrado ao PowerPoint para apoio à elaboração de apresentações profissionais. |
| Subtítulo do Bloco 0.1 (Cover) | Ao final deste curso, o participante será capaz de acessar a ferramenta, formular comandos eficazes e utilizá-la com segurança. |
| Pré-requisito técnico (Bloco 0.3) | Este curso requer conta Microsoft 365 ativa, conexão estável à internet e PowerPoint atualizado (versão Web ou Desktop). |
| Linha de pré-requisito a manter | Ferramentas do pacote Office → "[Desktop] Office 2021 ou superior — [Web] Office 365 ativo." |
| Linha a remover do Bloco 0.3 | A linha sobre Claude e demais ferramentas de IA (não se aplica: o Claude aqui é acessado via PowerPoint, não via conta separada) |

---

### Competências práticas — Bloco 0.4 (Numbered List, exatamente 4 itens)

1. Acessar e verificar o funcionamento do painel Claude no PowerPoint.
2. Diferenciar as tarefas em que a ferramenta agrega valor daquelas que permanecem sob responsabilidade humana.
3. Construir um comando contemplando os elementos de contexto, tarefa e formato.
4. Aplicar princípios básicos de proteção de dados e de validação de informações ao usar a ferramenta.

---

### Estrutura dos módulos — Bloco 0.5 (Accordion, exatamente 4 itens)

- **Módulo 1 — Primeiros Passos: Acesso à Ferramenta:** verificar os requisitos técnicos, localizar o painel Claude no PowerPoint e confirmar o funcionamento por meio de teste prático.
- **Módulo 2 — A Ferramenta como Recurso de Apoio:** compreender o papel do Claude como instrumento de apoio — não de substituição — e identificar as tarefas em que ele apresenta maior utilidade e suas limitações.
- **Módulo 3 — A Construção do Comando:** identificar os três elementos constitutivos de um comando eficaz (contexto, tarefa e formato) e redigir um comando aplicável ao próprio contexto.
- **Módulo 4 — Uso Seguro e Responsável:** distinguir informações que não devem ser compartilhadas com a ferramenta e reconhecer o fenômeno da alucinação como limitação a ser gerenciada por validação.

---

## MÓDULO 1 — Primeiros Passos: Acesso à Ferramenta

### Lição 1.1 — conteúdo principal

**Bloco 1.1.1 — Cover**
- Título: Módulo 1 — Primeiros Passos: Acesso à Ferramenta
- Subtítulo: Verificar os requisitos, localizar o painel Claude no PowerPoint e confirmar o funcionamento do recurso.

**Bloco 1.1.2 — Text (2 parágrafos)**

Parágrafo 1:
O Claude é um programa de inteligência artificial capaz de compreender solicitações redigidas em linguagem comum e responder com texto. Quando integrado ao PowerPoint, apresenta-se como um painel lateral no qual o participante digita suas solicitações e recebe sugestões de títulos, estruturas de slides e roteiros de fala. Não se exige nenhum conhecimento técnico de programação para sua utilização.

Parágrafo 2:
A ferramenta opera em duas configurações. Na versão Web, o acesso ocorre pelo navegador a partir do portal office.com. Na versão Desktop, o aplicativo está instalado no computador — Windows ou macOS. Em ambas, três condições devem ser satisfeitas: conta Microsoft 365 ativa, conexão de internet estável e versão atualizada do PowerPoint. As edições de 2016 e 2019 e os aplicativos para dispositivos móveis não são compatíveis com o recurso.

**Bloco 1.1.3 — Two-Column**
- Título: Dois caminhos de acesso — Web e Desktop
- Coluna esquerda — "Versão Web":
  - Acesso pelo navegador via portal office.com
  - Requer conta Microsoft 365 ativa
  - Painel Claude localizado à direita da apresentação
  - Complemento pode requerer ativação na primeira utilização
- Coluna direita — "Versão Desktop":
  - Aplicativo instalado no computador (Windows ou macOS)
  - Verificar atualizações pendentes antes do primeiro acesso
  - Painel Claude acionado pela faixa de opções
  - Edições 2016 e 2019 e dispositivos móveis não são compatíveis

**Bloco 1.1.4 — Accordion (3 itens, navegação restrita)**
- Título: Problemas frequentes de acesso — como resolver
- Item 1 — **O painel Claude não aparece:** a ausência do complemento decorre, na maioria dos casos, de atualização pendente do Microsoft 365. A disponibilização pode requerer até 24 horas para determinados usuários. Recomenda-se aguardar e tentar novamente.
- Item 2 — **Erro de autenticação:** falhas no reconhecimento da conta resolvem-se, em regra, saindo e retornando à conta Microsoft 365. `PowerPoint > Conta > Sair > Entrar novamente`
- Item 3 — **Resposta muito lenta:** a lentidão costuma associar-se a comandos excessivamente longos. Recomenda-se encurtar a solicitação e reenviar.

**Bloco 1.1.5 — Statement**
- Ícone: informação
- Texto em destaque: O processamento ocorre em servidores remotos — não no computador do participante.
- Texto de apoio: Todo conteúdo inserido no painel é transmitido pela internet a servidores onde a resposta é gerada. Para conteúdos genéricos, isso não representa nenhuma preocupação; para informações pessoais, as implicações serão detalhadas no Módulo 4.

**Bloco 1.1.6 — BreadCrumb (INCLUIR — este módulo envolve navegação em interface)**
- Título: Como localizar o painel Claude no PowerPoint
- Conteúdo:
  - Versão Web: `office.com > Abrir apresentação > Painel lateral direito > Ícone Claude / "Designer com IA" > Ativar complemento`
  - Versão Desktop: `PowerPoint > Faixa de opções > Aba Claude ou Designer com IA > Abrir painel lateral`
  - Resultado esperado: painel Claude visível à direita da apresentação, com campo de texto ativo.

---

### Lição 1.2 — Exercício Prático e Fechamento

**Bloco 1.2.1 — Text (Mão na massa, 1 parágrafo)**
O exercício a seguir tem por objetivo confirmar, por meio de teste prático, que o recurso está acessível e operacional. O participante deverá abrir o painel Claude no PowerPoint, enviar um comando simples e verificar se a resposta é retornada em poucos segundos. O atendimento aos três critérios a seguir habilita o avanço ao módulo seguinte.

**Bloco 1.2.2 — Process (4 passos)**
- Título: Verificação de acesso ao painel Claude
1. Abrir o PowerPoint e criar um slide em branco. `office.com > Nova apresentação > Slide em branco` (Web) ou `PowerPoint > Novo > Apresentação em branco` (Desktop)
2. Localizar e acionar o painel Claude. `Painel lateral direito > Ícone Claude` (Web) ou `Faixa de opções > Aba Claude` (Desktop)
3. Inserir e enviar o comando-base exibido no Bloco 1.2.5.
4. Observar a resposta — a ferramenta deve retornar sugestões em poucos segundos.

**Bloco 1.2.3 — Checklist (exatamente 3 itens, navegação restrita)**
- Título: Critérios de êxito — verifique antes de avançar
- ☐ Acesso ao PowerPoint realizado e slide em branco criado.
- ☐ Painel Claude visível no lado direito da tela.
- ☐ Comando enviado e resposta recebida em poucos segundos.

**Bloco 1.2.4 — Knowledge Check (Multiple Choice, 2 tentativas)**
- Pergunta: Qual das condições a seguir é indispensável para o funcionamento do Claude no PowerPoint?
- A) Conta Microsoft 365 ativa, conexão de internet estável e versão atualizada do PowerPoint. *(correta)*
- B) Instalação de um software de IA separado no computador.
- C) Versão 2016 ou superior do PowerPoint instalada.
- D) Acesso exclusivo pela versão Desktop — a versão Web não é compatível.
- Feedback correto: Correto. As três condições — conta Microsoft 365 ativa, conexão estável e versão atualizada — são igualmente necessárias, independentemente de se usar a versão Web ou Desktop.
- Feedback incorreto: Revise o conteúdo da lição. Atenção às condições técnicas exigidas e às versões compatíveis antes de tentar novamente.

**Bloco 1.2.5 — Text — Prompt base (INCLUIR)**
- Título: Prompt base — adapte ao seu contexto
"""
Crie um título criativo para uma apresentação sobre [ASSUNTO DE INTERESSE].
"""

**Bloco 1.2.6 — Statement**
- Texto em destaque: O acesso ao painel Claude está confirmado — o primeiro passo do percurso foi concluído.
- Texto de apoio: No próximo módulo, o foco se desloca do acesso à compreensão da função da ferramenta: o que ela faz bem e onde a atuação humana permanece indispensável.

**Bloco 1.2.7 — Button**
- Rótulo: "Avançar para o Módulo 2 →"

---

## MÓDULO 2 — A Ferramenta como Recurso de Apoio

### Lição 2.1 — conteúdo principal

**Bloco 2.1.1 — Cover**
- Título: Módulo 2 — A Ferramenta como Recurso de Apoio
- Subtítulo: Compreender o que o Claude faz, o que não faz e onde a atuação humana é insubstituível.

**Bloco 2.1.2 — Text (2 parágrafos)**

Parágrafo 1:
Um equívoco recorrente entre usuários iniciantes consiste em atribuir à ferramenta a execução integral e autônoma da tarefa. Tal procedimento tende a produzir material genérico e impessoal, facilmente reconhecível como produto de geração automática e desprovido de adequação ao contexto específico. O Claude deve ser compreendido como recurso de apoio à criação — não como mecanismo de produção autônoma. Ao participante cabe fornecer a ideia, o objetivo e o conhecimento sobre o próprio público; à ferramenta cabe contribuir na estruturação e na agilização do processo.

Parágrafo 2:
A delimitação dos domínios de utilidade é igualmente necessária. A ferramenta auxilia na definição da sequência lógica da exposição, na conversão de textos extensos em pontos objetivos, na expansão de títulos sucintos em roteiros de fala e na descrição de imagens para busca em bancos como Unsplash e Pexels. Por outro lado, o Claude não produz imagens, não assegura a exatidão de todos os dados que apresenta e não dispõe do conhecimento do público que o profissional detém. Tais limitações não constituem deficiências — delimitam, com precisão, o espaço em que a intervenção humana é insubstituível.

**Bloco 2.1.3 — Two-Column**
- Título: O que o Claude faz e o que não faz
- Coluna esquerda — "Faz bem":
  - Organizar a sequência lógica de uma apresentação
  - Sintetizar textos extensos em tópicos objetivos
  - Expandir títulos em roteiros de fala naturais
  - Sugerir modelos de disposição de conteúdo na tela
  - Descrever imagens para busca em bancos (Unsplash, Pexels)
- Coluna direita — "Não faz":
  - Produzir fotografias ou imagens
  - Garantir a exatidão de datas, dados e citações
  - Conhecer o público específico do participante
  - Substituir o planejamento e o juízo profissional

**Bloco 2.1.4 — Tabs (3 abas, navegação restrita)**
- Título: Funções da ferramenta — explore cada uma
- Aba 1 — **Organização:** o Claude auxilia na definição da sequência lógica da apresentação — determina em que ordem os tópicos devem ser expostos para conduzir o público do problema à solução de forma coerente.
- Aba 2 — **Síntese:** textos extensos são convertidos pela ferramenta em pontos objetivos e acessíveis, adequados ao formato de slides. O participante fornece o texto; o Claude extrai os pontos essenciais.
- Aba 3 — **Expansão e formato:** a ferramenta pode expandir um título sucinto em roteiro de fala natural e sugerir formas de disposição do conteúdo na tela, tornando a apresentação mais clara e visualmente orientada.

**Bloco 2.1.5 — Statement**
- Ícone: alerta
- Texto em destaque: A responsabilidade pelo conteúdo permanece integralmente com quem o utiliza.
- Texto de apoio: A ferramenta agrega valor na estruturação e na agilização; o participante é responsável pela ideia, pelo conhecimento do público e pela validação do resultado.

**Bloco 2.1.6 — BreadCrumb (OMITIR — este módulo não envolve navegação em interface)**

---

### Lição 2.2 — Exercício Prático e Fechamento

**Bloco 2.2.1 — Text (Mão na massa, 1 parágrafo)**
O exercício a seguir propõe a classificação de tarefas entre aquelas que a ferramenta executa adequadamente e aquelas que permanecem sob responsabilidade humana. A capacidade de distinguir esses domínios constitui o fundamento para o uso produtivo do Claude — sem delegar o que não deve ser delegado, sem deixar de aproveitar o que a ferramenta oferece.

**Bloco 2.2.2 — Process (3 passos)**
- Título: Classificação de tarefas — como executar
1. Ler cada uma das seis tarefas listadas no Bloco 2.2.3.
2. Para cada tarefa, decidir: o Claude executa ou não executa adequadamente?
3. Verificar a resposta no gabarito ao final do Checklist.

**Bloco 2.2.3 — Checklist (exatamente 3 itens, navegação restrita)**
- Título: Critérios de êxito — verifique antes de avançar
- ☐ As três tarefas que o Claude executa foram identificadas corretamente: estruturar sequência, sintetizar texto e sugerir modelo de disposição.
- ☐ As três tarefas que o Claude não executa foram identificadas corretamente: produzir fotografia, garantir exatidão histórica e conhecer o público.
- ☐ A distinção entre apoio da ferramenta e responsabilidade humana foi compreendida.

**Bloco 2.2.4 — Knowledge Check (Multiple Choice, 2 tentativas)**
- Pergunta: Qual das alternativas descreve corretamente uma limitação do Claude no PowerPoint?
- A) O Claude não produz imagens e não garante a exatidão de todos os dados que apresenta. *(correta)*
- B) O Claude não consegue organizar a sequência lógica de uma apresentação.
- C) O Claude só funciona quando o participante possui formação em programação.
- D) O Claude substitui o planejamento do conteúdo pelo profissional.
- Feedback correto: Correto. A produção de imagens e a garantia de exatidão estão fora do escopo da ferramenta — ambas permanecem sob responsabilidade do participante.
- Feedback incorreto: Revise a lição. Atenção à distinção entre o que a ferramenta faz bem e o que permanece como atribuição humana.

**Bloco 2.2.5 — Text — Prompt base (INCLUIR)**
- Título: Prompt base — adapte ao seu contexto
"""
Tenho o seguinte texto sobre [ASSUNTO DE INTERESSE]:
[COLAR UM PARÁGRAFO EXTENSO]

Resuma-o em até 5 tópicos curtos e claros, adequados a um slide de apresentação.
"""

**Bloco 2.2.6 — Statement**
- Texto em destaque: O escopo da ferramenta está definido — apoio na estruturação e na agilização, não substituição do profissional.
- Texto de apoio: O próximo módulo aborda como formular solicitações eficazes: os três elementos que tornam um comando preciso o suficiente para gerar resultado ajustado já na primeira tentativa.

**Bloco 2.2.7 — Button**
- Rótulo: "Avançar para o Módulo 3 →"

---

## MÓDULO 3 — A Construção do Comando

### Lição 3.1 — conteúdo principal

**Bloco 3.1.1 — Cover**
- Título: Módulo 3 — A Construção do Comando
- Subtítulo: Aprender a formular solicitações com contexto, tarefa e formato para obter respostas ajustadas ao próprio contexto.

**Bloco 3.1.2 — Text (2 parágrafos)**

Parágrafo 1:
O termo "prompt" designa o comando inserido no campo de interação da ferramenta. A esse conceito associa-se um princípio central: a ferramenta não infere intenções que não tenham sido explicitadas. Seu funcionamento assemelha-se ao de um colaborador que dispõe exclusivamente das informações registradas na solicitação, sem acesso a qualquer contexto não declarado. Disso decorre uma relação direta: um comando impreciso conduz a uma resposta imprecisa; um comando claro conduz a um resultado ajustado às necessidades.

Parágrafo 2:
Um comando eficaz estrutura-se sobre três elementos. O **contexto** situa o autor e a circunstância — área de atuação, perfil do público e momento da apresentação. A **tarefa** especifica, com o detalhamento necessário, a ação requerida da ferramenta, restringindo interpretações genéricas. O **formato** determina como a resposta deve ser apresentada — por exemplo, a especificação de que cada slide contenha título, três tópicos e uma pergunta. A combinação dos três converte uma solicitação vaga em instrução apta a gerar resultado pertinente já na primeira tentativa.

**Bloco 3.1.3 — Two-Column**
- Título: Comando deficiente vs. comando eficaz
- Coluna esquerda — "Comando deficiente":
  - Exemplo: "Elaborar uma apresentação sobre sustentabilidade."
  - Resultado genérico — igualmente adequado e inadequado a qualquer público
  - Sem contexto: a ferramenta desconhece a área e o perfil dos destinatários
  - Sem formato: a estrutura da resposta fica a critério da ferramenta
- Coluna direita — "Comando eficaz":
  - Exemplo: inclui área de atuação, perfil do público, número de slides, objetivo e formato de cada slide
  - Resultado ajustado ao público concreto
  - Contexto claro: área, perfil e objetivo declarados
  - Formato definido: título, tópicos e pergunta por slide especificados

**Bloco 3.1.4 — Accordion (3 itens, navegação restrita)**
- Título: Os três elementos do comando — explore cada um
- Item 1 — **Contexto:** situa o autor e a circunstância. Deve incluir a área de atuação, o perfil e o nível do público e o momento em que a apresentação se insere. Exemplo: "Atuo na área de Recursos Humanos. Meu público são gestores de nível médio sem formação técnica."
- Item 2 — **Tarefa:** especifica a ação requerida com detalhamento suficiente para restringir interpretações genéricas. Deve informar o que se quer (elaborar, sintetizar, expandir), o assunto e o objetivo. Exemplo: "Elaborar uma estrutura de 6 slides sobre gestão de conflitos, com o objetivo de introduzir o tema."
- Item 3 — **Formato:** determina a forma de apresentação da resposta. Deve especificar a estrutura de cada slide, o número de itens e a linguagem desejada. Exemplo: "Para cada slide: um título em forma de pergunta, 3 tópicos de até 8 palavras e 1 pergunta de engajamento."

**Bloco 3.1.5 — Statement**
- Ícone: lâmpada
- Texto em destaque: A elaboração de comandos é uma habilidade desenvolvida de forma progressiva — não se exige acerto na primeira tentativa.
- Texto de apoio: O diálogo com a ferramenta permite o refinamento sucessivo da solicitação. O objetivo deste módulo é estabelecer a base — os três elementos — sobre a qual essa habilidade poderá desenvolver-se.

**Bloco 3.1.6 — BreadCrumb (OMITIR — este módulo não envolve navegação em interface)**

---

### Lição 3.2 — Exercício Prático e Fechamento

**Bloco 3.2.1 — Text (Mão na massa, 1 parágrafo)**
O exercício a seguir propõe a comparação entre um comando deficiente e um comando estruturado nos três elementos. O participante deverá submeter ambos à ferramenta, observar a diferença de especificidade nas respostas e identificar, no próprio comando estruturado, os três elementos constitutivos. Essa identificação constitui o critério de êxito do módulo.

**Bloco 3.2.2 — Process (4 passos)**
- Título: Comparação entre comandos — como executar
1. Abrir o painel Claude no PowerPoint. `Painel lateral direito > Campo de texto`
2. Enviar o comando deficiente: "Elaborar uma apresentação sobre [tema]." Observar o caráter genérico da resposta.
3. Enviar o comando estruturado do Bloco 3.2.5, com os campos devidamente preenchidos. Observar a resposta.
4. Comparar as duas respostas e identificar no segundo comando os elementos: contexto, tarefa e formato.

**Bloco 3.2.3 — Checklist (exatamente 3 itens, navegação restrita)**
- Título: Critérios de êxito — verifique antes de avançar
- ☐ O segundo comando produziu resposta visivelmente mais específica e ajustada ao público informado.
- ☐ Os três elementos — contexto, tarefa e formato — foram identificados no comando estruturado.
- ☐ Um comando básico aplicável ao próprio contexto foi redigido ou adaptado.

**Bloco 3.2.4 — Knowledge Check (Multiple Choice, 2 tentativas)**
- Pergunta: Um participante envia o seguinte comando: "Fazer slides sobre tecnologia." Qual é o principal problema desta solicitação?
- A) Ausência dos três elementos constitutivos: não há contexto, a tarefa é vaga e o formato não foi especificado. *(correta)*
- B) O tema "tecnologia" é muito amplo para ser abordado em uma apresentação.
- C) O comando está correto — a ferramenta inferirá o contexto automaticamente.
- D) Comandos curtos produzem respostas mais rápidas e de melhor qualidade.
- Feedback correto: Correto. Sem contexto (quem é o público e qual a área), sem tarefa definida (quantos slides, qual objetivo) e sem formato especificado, a ferramenta produzirá resultado genérico, inadequado a qualquer contexto concreto.
- Feedback incorreto: Revise os três elementos constitutivos do comando. O problema não está no tema, mas na ausência de informações que orientem a resposta da ferramenta.

**Bloco 3.2.5 — Text — Prompt base (INCLUIR)**
- Título: Prompt base — adapte ao seu contexto
"""
# CONTEXTO
Atuo na área de [ÁREA DE ATUAÇÃO].
Meu público é [PERFIL, NÍVEL E CONHECIMENTO PRÉVIO DO PÚBLICO].

# TAREFA
Elaborar uma estrutura de [NÚMERO] slides sobre [ASSUNTO DE INTERESSE].
O objetivo é [INTRODUZIR / REVISAR / EXPLICAR].

# FORMATO
Para cada slide, apresentar:
- um título (preferencialmente em forma de pergunta);
- 3 tópicos sucintos (máximo de 8 palavras cada);
- 1 atividade ou pergunta destinada ao engajamento do público.
"""

**Bloco 3.2.6 — Statement**
- Texto em destaque: O comando estruturado está formulado — a ferramenta agora tem o que precisa para gerar resultado ajustado.
- Texto de apoio: O próximo módulo aborda os limites do que pode ser enviado à ferramenta: proteção de dados de terceiros e validação das informações recebidas.

**Bloco 3.2.7 — Button**
- Rótulo: "Avançar para o Módulo 4 →"

---

## MÓDULO 4 — Uso Seguro e Responsável

### Lição 4.1 — conteúdo principal

**Bloco 4.1.1 — Cover**
- Título: Módulo 4 — Uso Seguro e Responsável
- Subtítulo: Definir o que pode — e o que não deve — ser enviado à ferramenta, e como tratar as informações recebidas.

**Bloco 4.1.2 — Text (2 parágrafos)**

Parágrafo 1:
Este módulo retoma conceito anunciado no Módulo 1: o processamento das informações ocorre em servidores remotos. Cada conteúdo inserido pelo participante é transmitido do computador local a esses servidores, onde a resposta é gerada. Para conteúdos de natureza genérica, tal circunstância é irrelevante. A situação altera-se, contudo, quando envolvidas informações pessoais de terceiros — em especial de estudantes, eventualmente menores de idade. Não se deve transmitir qualquer informação que permita a identificação de uma pessoa: nomes, documentos, datas de nascimento, endereços, diagnósticos, notas identificadas, fotografias de menores, senhas ou dados bancários.

Parágrafo 2:
Há, ademais, um segundo cuidado de particular relevância. A ferramenta pode apresentar informações incorretas com aparência de correção — fenômeno tecnicamente designado "alucinação". Não se trata de erro intencional, mas de uma limitação do modo como o sistema gera texto: pode produzir conteúdo plausível, porém falso. A medida defensiva é a confirmação dos dados relevantes em fontes confiáveis — obras de referência, publicações oficiais ou material especializado — antes de sua incorporação ao trabalho. A ferramenta agiliza a produção; a responsabilidade pelo conteúdo permanece integralmente com o participante.

**Bloco 4.1.3 — Two-Column**
- Título: O que enviar e o que não enviar à ferramenta
- Coluna esquerda — "Nunca enviar":
  - Nomes de pessoas identificáveis
  - Documentos: CPF, RG, matrícula
  - Diagnósticos e laudos médicos ou educacionais
  - Notas e históricos identificados
  - Fotografias de menores
  - Senhas e dados bancários
- Coluna direita — "Pode enviar":
  - Temas genéricos e conteúdos de domínio público
  - Descrição anônima de contexto ("turma com acesso limitado à internet")
  - Indicação de perfil ou nível sem identificação de pessoas
  - Textos não identificados para síntese ou estruturação

**Bloco 4.1.4 — Accordion (3 itens, navegação restrita)**
- Título: Dois cuidados essenciais no uso responsável
- Item 1 — **Proteção de dados de terceiros:** antes de enviar qualquer informação, aplicar o critério objetivo: caso essa informação viesse a público, alguém seria exposto? Em caso afirmativo, abster-se de transmiti-la. A anonimização é sempre preferível à abstenção: na maioria dos casos, o comando pode ser reescrito sem os elementos identificadores.
- Item 2 — **Validação contra alucinações:** confirmar os dados relevantes — datas, citações, estatísticas — em fontes confiáveis antes de incorporá-los ao trabalho. A ferramenta pode apresentar um dado incorreto com elevado grau de assertividade. O participante é sempre o responsável pelo conteúdo final.
- Item 3 — **Critério de decisão prático:** em caso de dúvida sobre o que pode ser enviado, utilizar a seguinte pergunta: "Se este texto fosse publicado com o nome da instituição, alguém seria prejudicado?" Se sim, não enviar. Se não, o uso é admissível.

**Bloco 4.1.5 — Statement**
- Ícone: alerta
- Texto em destaque: O uso responsável da ferramenta compreende dois compromissos: proteção dos dados de terceiros e validação das informações recebidas.
- Texto de apoio: Esses compromissos não decorrem de desconfiança na ferramenta — decorrem do mesmo rigor profissional já consolidado em outras práticas.

**Bloco 4.1.6 — BreadCrumb (OMITIR — este módulo não envolve navegação em interface)**

---

### Lição 4.2 — Exercício Prático e Fechamento

**Bloco 4.2.1 — Text (Mão na massa, 1 parágrafo)**
O exercício a seguir apresenta um cenário de uso com informações pessoais identificáveis e propõe a seleção da forma correta de reescrever o comando. A escolha da alternativa adequada — e a compreensão da razão que a sustenta — constitui o critério de êxito deste módulo e o Knowledge Check de conclusão do curso.

**Bloco 4.2.2 — Process (3 passos)**
- Título: Análise de adequação de comando — como executar
1. Ler o cenário: "Para preparar um material de apoio, cogita-se enviar o seguinte comando: 'Preciso de uma atividade de reforço em estatística para o aluno João Silva, matrícula 2023456, que possui diagnóstico de transtorno de atenção.'"
2. Avaliar as três alternativas do Knowledge Check com base nos critérios de proteção de dados aprendidos neste módulo.
3. Selecionar a alternativa correta e verificar a fundamentação no feedback.

**Bloco 4.2.3 — Checklist (exatamente 3 itens, navegação restrita)**
- Título: Critérios de êxito — verifique antes de avançar
- ☐ Os elementos identificadores no cenário foram reconhecidos: nome, matrícula e diagnóstico.
- ☐ A alternativa de anonimização foi identificada como correta.
- ☐ A razão pela qual a alternativa de abstenção é desnecessária foi compreendida.

**Bloco 4.2.4 — Knowledge Check — CONCLUSÃO DO CURSO (Multiple Choice, 2 tentativas)**
> Este é o Knowledge Check de conclusão do curso. O Course Settings deve registrar a conclusão com base na aprovação neste bloco.

- Pergunta: Qual é a forma mais adequada de reescrever o comando a seguir para uso na ferramenta? Comando original: "Preciso de uma atividade de reforço em estatística para o aluno João Silva, matrícula 2023456, que possui diagnóstico de transtorno de atenção."
- A) "Atividade de reforço em estatística para estudante do ensino superior, com adaptações voltadas à dificuldade de concentração." *(correta)*
- B) Enviar o comando na forma original, pois se trata de mera atividade pedagógica.
- C) Abster-se de usar a ferramenta, pois qualquer menção a estudante específico é inadmissível.
- D) Substituir o nome por iniciais — "aluno J. S." — mantendo matrícula e diagnóstico.
- Feedback correto: Correto. A alternativa A suprime os elementos identificadores (nome, matrícula e diagnóstico) e preserva as informações necessárias ao auxílio pretendido, tornando o uso ao mesmo tempo admissível e eficaz.
- Feedback incorreto: Revise os critérios de proteção de dados. Nome, matrícula e diagnóstico identificam a pessoa e não devem ser transmitidos. A anonimização completa — não parcial — é o procedimento correto.

**Bloco 4.2.5 — Text — Prompt base (INCLUIR)**
- Título: Prompt base — adapte ao seu contexto
"""
Elaborar uma atividade de [DISCIPLINA / ASSUNTO] para [PERFIL DO PÚBLICO, SEM NOMES],
com adaptações voltadas a [NECESSIDADE DESCRITA DE FORMA GENÉRICA].
"""

**Bloco 4.2.6 — Statement**
- Texto em destaque: Os quatro módulos foram concluídos — acesso, compreensão, comando e segurança.
- Texto de apoio: O módulo seguinte articula essas competências em uma atividade integradora que percorre o ciclo completo, do comando à apresentação revisada e validada.

**Bloco 4.2.7 — Button**
- Rótulo: "Avançar para a Síntese Final →"

---

## LIÇÃO 5 — SÍNTESE E ENCERRAMENTO

**Bloco 5.1 — Cover**
- Título: Síntese — Claude no PowerPoint — Essentials
- Subtítulo: Ao final deste curso, o participante é capaz de acessar a ferramenta, formular comandos eficazes e utilizá-la de forma segura e responsável.

**Bloco 5.2 — Text (1 parágrafo, prosa corrida, sem listas)**
Ao longo dos quatro módulos, o participante desenvolveu as competências que sustentam o uso produtivo do Claude no PowerPoint: a verificação dos requisitos técnicos e a abertura do painel, a compreensão do papel da ferramenta como recurso de apoio, a formulação de comandos estruturados nos elementos de contexto, tarefa e formato, e a adoção de práticas de proteção de dados e de validação das informações recebidas. A atividade a seguir articula essas competências em um percurso completo.

**Bloco 5.3 — Numbered List (exatamente 5 itens)**
- Título: Atividade integradora — percorra o ciclo completo
1. Acessar o painel Claude no PowerPoint. `Painel lateral direito > Campo de texto` (Web) ou `Faixa de opções > Aba Claude` (Desktop)
2. Inserir o comando integrador do Bloco 5.5, contemplando contexto, tarefa e formato.
3. Revisar a solicitação, confirmando a ausência de dados pessoais de terceiros.
4. Enviar o comando, analisar a estrutura proposta e validar ao menos um dado em fonte confiável.
5. Ajustar o resultado de modo a refletir a identidade e os objetivos do próprio participante.

**Bloco 5.4 — Checklist (exatamente 5 itens, navegação restrita)**
- Título: Critérios de avaliação da atividade integradora
- ☐ Acesso à ferramenta e envio do comando realizados.
- ☐ Comando contemplando contexto, tarefa e formato.
- ☐ Ausência de compartilhamento de dados sensíveis confirmada.
- ☐ Ao menos um dado validado em fonte confiável.
- ☐ Estrutura final personalizada pelo participante.

**Bloco 5.5 — Statement**
- Ícone: check ou conquista
- Texto em destaque: O Claude constitui recurso de apoio à criação. Ao participante cabe conceber, estruturar e validar; à ferramenta, ampliar e agilizar.
- Texto de apoio: Recomenda-se a elaboração de duas a três apresentações nos próximos dias para consolidar o percurso realizado.

**Bloco 5.6 — Accordion (exatamente 3 itens)**
- Título: Caminhos de aprofundamento
- Item 1 — **Construção de narrativa:** a trilha completa aborda a elaboração de apresentações com arco narrativo — introdução, desenvolvimento e chamada à ação — utilizando o Claude para estruturar o fluxo argumentativo.
- Item 2 — **Notas de orador e direção de arte:** módulos avançados tratam da geração de roteiros de fala detalhados e da especificação de elementos visuais — paletas de cores, tipografia e disposição de elementos — com apoio da ferramenta.
- Item 3 — **Curso Hands-on:** o curso Hands-on correspondente conduz o participante por projetos práticos completos — da abertura do PowerPoint à apresentação final revisada — com complexidade progressiva e critérios de entrega verificáveis.

**Bloco 5.7 — Button**
- Rótulo: "Concluir o curso ✓"
- Ação: registrar conclusão no LMS (Complete Course / passed)

---

## VERIFICAÇÃO FINAL ANTES DE ENTREGAR

Antes de submeter o gabarito preenchido, confirmar:

| Item | Verificado? |
|---|---|
| Todos os campos `«»` foram substituídos | ☐ |
| Nenhum bloco foi adicionado ou removido além dos condicionais indicados | ☐ |
| Bloco 1.1.6 (BreadCrumb) está presente com os dois caminhos (Web e Desktop) | ☐ |
| Bloco 2.1.6 foi omitido | ☐ |
| Bloco 3.1.6 foi omitido | ☐ |
| Bloco 4.1.6 foi omitido | ☐ |
| Knowledge Check do Bloco 4.2.4 está marcado como conclusão do curso | ☐ |
| Todos os prompts base estão delimitados por aspas triplas | ☐ |
| Gabarito A é sempre a alternativa correta em todos os Knowledge Checks | ☐ |
| Registro formal e impessoal em todos os campos de texto | ☐ |
