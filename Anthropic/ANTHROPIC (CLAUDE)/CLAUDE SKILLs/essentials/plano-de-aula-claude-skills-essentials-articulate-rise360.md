> *» IA: Cover — título do curso.*

# Plano de Aula — Claude Skills (Essentials)

---

> *» IA: Table — quadro de identificação. Manter as duas colunas, verbatim.*

## Identificação

| Campo | Definição |
|---|---|
| **Curso** | Claude Skills: fundamentos, criação e avaliação de procedimentos reutilizáveis para assistentes de Inteligência Artificial |
| **Natureza** | Autoinstrucional, introdutório e prático |
| **Carga horária** | 115 minutos |
| **Público-alvo** | Docentes do ensino superior, de qualquer área do conhecimento, sem experiência prévia com desenvolvimento de software |
| **Pré-requisitos** | Nenhum conhecimento técnico prévio. Requer-se apenas familiaridade com o uso de navegador e com a criação e gravação de arquivos em computador pessoal |
| **Recursos necessários** | Computador com navegador e conexão à internet ativa; conta em claude.ai com o recurso de Skills habilitado, o que pode exigir plano pago conforme a configuração vigente; editor de texto simples; um documento institucional de referência do próprio participante |

> *» IA: Statement — nota de verificação prévia. Preservar o emoji 🧭 e o breadcrumb. Não traduzir termos de interface.*

> 🧭 **Verificação preliminar.** A disponibilidade do recurso de criação de Skills varia conforme o plano da conta e a configuração de execução de código, e as fontes documentais consultadas divergem quanto aos planos abrangidos. Recomenda-se, portanto, a verificação prévia em `claude.ai > Configurações > Customize > Skills`. Não se verificando a existência da seção, o percurso pode ser cumprido integralmente na modalidade de elaboração dos arquivos, sem a etapa de envio.
>
> 🏁 **Ponto de controle:** em `claude.ai > Configurações > Customize > Skills` observa-se a existência de comando de criação ou envio de Skill.

---

> *» IA: Text — objetivo geral. Bloco único, não resumir.*

### Objetivo Geral

Capacitar o docente a converter procedimentos de trabalho recorrentes em Agent Skills — pacotes de conhecimento procedural que assistentes de Inteligência Artificial carregam sob demanda —, de modo que, ao término do curso, o participante disponha de ao menos uma Skill funcional, aplicada a uma tarefa real de sua rotina acadêmica, cuja eficácia tenha sido verificada mediante comparação com uma linha de base registrada previamente à intervenção.

> *» IA: List — competências. Verbatim, sem acréscimos.*

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Explicar o funcionamento das Agent Skills e o mecanismo de revelação progressiva que rege o carregamento de informação.
2. Elaborar um arquivo `SKILL.md` em conformidade com as regras de validação e os requisitos de gravação aplicáveis.
3. Executar as operações de ciclo de vida da Skill e verificar objetivamente a efetivação de uma substituição de versão.
4. Avaliar a qualidade de uma Skill quanto à precisão do acionamento, à economia do procedimento e à arquitetura dos arquivos de apoio.
5. Verificar a eficácia de uma Skill por comparação com linha de base e aplicar critérios de confiabilidade a material de procedência externa.

> *» IA: Text — parágrafo sobre a progressão cumulativa.*

### Estrutura e Sequência dos Módulos

A progressão adotada é cumulativa: cada módulo pressupõe as competências dos anteriores e desloca o foco de investigação. Os Módulos 1 a 3 estabelecem, respectivamente, o fundamento conceitual, o procedimento de elaboração e as operações de manutenção — sem os quais nenhum aperfeiçoamento posterior seria exequível. Os Módulos 4 e 5 introduzem os critérios que distinguem eficácia de mera existência e os procedimentos de verificação que permitem afirmá-la com fundamento. O Módulo 6 articula as cinco competências em atividade integradora.

> *» IA: Table — sequência dos módulos. Manter as quatro colunas.*

| Módulo | Título | Referência | Tempo |
|---|---|---|---|
| 1 | Fundamentos das Agent Skills | Arquitetura e revelação progressiva | 18 min |
| 2 | Elaboração do arquivo SKILL.md | Estrutura, validação e gravação | 20 min |
| 3 | Ciclo de vida e manutenção | Operações de ativação e substituição | 15 min |
| 4 | Critérios de qualidade | Acionamento, economia e arquitetura da informação | 22 min |
| 5 | Verificação e confiabilidade | Avaliação por evidência e auditoria de procedência | 20 min |
| 6 | Síntese e Aplicação Integrada | Atividade integradora | 20 min |

---
---

# Módulo 1 — Fundamentos das Agent Skills

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> *» IA: Statement — nota de encadeamento. Linha única, verbatim.*

> Ponto de partida do percurso. Não pressupõe conhecimento prévio; estabelece o vocabulário e o modelo de funcionamento que sustentam todos os módulos subsequentes.

> *» IA: List — objetivos de aprendizagem. Verbatim, sem acréscimos.*

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Definir Agent Skill, distinguindo-a de instrução pontual e de mecanismo de memória.
2. Descrever os três níveis de carregamento de informação e o custo associado a cada um.
3. Justificar, com base no custo de contexto, por que a concisão constitui requisito de qualidade e não preferência estilística.

> *» IA: Text — texto descritivo. Pode dividir em blocos menores por parágrafo; não resumir.*

### Texto Descritivo

Denomina-se **Agent Skill** uma pasta autocontida cujo ponto de entrada é um arquivo nomeado `SKILL.md`, contendo instruções procedimentais e, opcionalmente, documentos de referência, modelos e demais recursos. O formato foi introduzido pela Anthropic em outubro de 2025 como funcionalidade do assistente Claude e posteriormente publicado como especificação aberta, circunstância que confere às Skills bem elaboradas certo grau de portabilidade entre assistentes que adotem o mesmo padrão. Cumpre registrar que a Skill não se confunde com um comando salvo: enquanto a instrução pontual atende a uma solicitação específica, a Skill codifica um procedimento aplicável a uma categoria de tarefas, sendo carregada quando o assistente reconhece a pertinência da categoria. Tampouco se confunde com mecanismo de memória: a Skill registra o modo de execução, e não o histórico das interações.

O mecanismo que rege o carregamento denomina-se **revelação progressiva** e opera em três níveis. No primeiro, o assistente recebe, ao início de cada interação, apenas o nome e a descrição de cada Skill disponível — informação cujo custo a Anthropic estima em aproximadamente cem tokens por Skill, sendo o **token** a unidade de medida do texto processado, correspondente aproximadamente a uma palavra curta ou a um fragmento de palavra. No segundo nível, reconhecida a pertinência, procede-se à leitura integral do `SKILL.md`, cuja extensão a documentação recomenda manter abaixo de aproximadamente cinco mil tokens. No terceiro, os arquivos de apoio permanecem inacessados e sem custo algum até que a execução os torne necessários.

Depreende-se dessa arquitetura uma consequência de ordem prática que orientará todas as decisões subsequentes. O espaço em que o assistente processa informação — designado **janela de contexto** — é finito e compartilhado entre a solicitação, o histórico da interação e os metadados de todas as Skills instaladas. A documentação da Anthropic caracteriza esse espaço como um bem público. Segue-se que a instalação de numerosas Skills não acarreta prejuízo significativo, ao passo que uma única Skill de extensão excessiva compromete o desempenho no momento em que é acionada. Este conceito de **custo de contexto** será retomado expressamente no Módulo 4, quando se examinar a distribuição do conteúdo entre o arquivo principal e os arquivos de apoio: a arquitetura de pastas ali proposta não constitui organização estética, mas aplicação direta do princípio ora estabelecido.

Da mesma constatação deriva a recomendação mais reiterada da documentação oficial: não convém instruir o assistente sobre aquilo que ele já domina. Um procedimento que dedique parágrafos a explicar o conceito de rubrica avaliativa desperdiça espaço, porquanto o modelo já dispõe dessa informação. O conteúdo que justifica o custo é precisamente aquele que o modelo não poderia inferir — a rubrica específica da disciplina, a ordem estabelecida pelo colegiado, a restrição de extensão imposta pela instituição.

Convém, por fim, registrar duas informações que serão retomadas adiante. A primeira concerne à tipologia: a Anthropic distingue as **Skills de ampliação de capacidade**, que ensinam ao modelo tarefas que este ainda não executa com confiabilidade suficiente e tendem a perder relevância conforme os modelos evoluem, das **Skills de preferência codificada**, que registram o processo desejado por uma pessoa ou instituição e conservam utilidade indefinidamente. Observa-se que, no contexto docente, a segunda categoria concentra as aplicações de maior valor. A segunda informação concerne à retenção: conforme a documentação, as Skills **não** se encontram abrangidas por acordos de retenção zero de dados, aplicando-se-lhes a política padrão. Tal circunstância, aparentemente técnica neste momento, produzirá consequência normativa direta no Módulo 5, quando se tratar do conteúdo que não deve ser incorporado aos arquivos de uma Skill.

> *» IA: Knowledge Check — questão de múltipla escolha. Preservar as quatro alternativas.*

### Exercício Prático (6 minutos)

Um docente elabora uma Skill destinada à correção de trabalhos e inclui, no corpo do `SKILL.md`, três parágrafos explicando o que são rubricas avaliativas, sua função formativa e sua fundamentação na literatura pedagógica. Em seguida, apresenta os quatro critérios específicos de sua disciplina. Considerando o princípio de custo de contexto, qual avaliação se aplica a esse material?

**a)** O material está adequado, uma vez que a contextualização teórica auxilia o assistente a compreender a finalidade da tarefa.

**b)** Os três parágrafos iniciais devem ser suprimidos, porquanto veiculam conhecimento de que o modelo já dispõe; os quatro critérios específicos devem ser preservados, por constituírem informação que o modelo não poderia inferir.

**c)** Todo o material deve ser transferido para um arquivo de apoio, mantendo-se o `SKILL.md` reservado exclusivamente ao acionamento.

**d)** O material deve ser reduzido pela metade de forma proporcional, preservando-se parte de cada seção.

> *» IA: Statement — gabarito e fundamentação. Verbatim.*

**Gabarito:** alternativa **b**.

**Fundamentação:** a alternativa (a) contraria a orientação documental expressa de não instruir o modelo sobre aquilo que já domina. A alternativa (c) equivoca-se quanto à natureza dos arquivos de apoio, destinados a conteúdo ocasionalmente necessário e não a conteúdo dispensável — a rubrica específica é requerida em toda execução. A alternativa (d) aplica critério quantitativo onde se impõe critério qualitativo: a redução não deve ser proporcional, mas seletiva.

**Critério de êxito:** o participante identifica a alternativa correta e articula, em uma frase, o critério que distingue o conteúdo suprimível do indispensável.

> *» IA: Statement ou Download — prompt-base editável. Conteúdo verbatim; o participante adapta o trecho entre colchetes.*

### Mão na massa

Prompt-base para exame do próprio repertório de tarefas. Recomenda-se executá-lo em interação nova.

"""
Atuo como docente do ensino superior na área de [área de conhecimento].

Descrevo abaixo três tarefas recorrentes da minha rotina:
1. [tarefa]
2. [tarefa]
3. [tarefa]

Para cada uma, classifique como "ampliação de capacidade" (o modelo ainda não
executa com confiabilidade suficiente) ou "preferência codificada" (existe um
modo específico de execução determinado por mim ou pela instituição).

Justifique cada classificação em uma frase e indique qual das três apresenta
maior valor duradouro como Skill.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---
---

# Módulo 2 — Elaboração do arquivo SKILL.md

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> *» IA: Statement — nota de encadeamento. Linha única, verbatim.*

> Pressupõe o Módulo 1. O foco desloca-se do funcionamento conceitual para o procedimento operacional de elaboração e gravação do arquivo.

> *» IA: List — objetivos de aprendizagem. Verbatim, sem acréscimos.*

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Identificar as duas partes constitutivas do arquivo `SKILL.md` e a função de cada uma.
2. Aplicar corretamente as regras de validação do campo `name`.
3. Gravar o arquivo observando os requisitos de extensão e de codificação de caracteres.

> *» IA: Text — texto descritivo. Pode dividir por parágrafo; não resumir.*

### Texto Descritivo

O arquivo `SKILL.md` compõe-se de duas seções funcionalmente distintas, cuja separação reproduz a lógica do resumo e do corpo de um artigo científico: a primeira destina-se à decisão sobre a pertinência da leitura; a segunda, à execução. A seção inicial, delimitada por duas linhas contendo três hifens, denomina-se cabeçalho ou *frontmatter* e adota o formato YAML, no qual cada linha corresponde a um par de campo e valor. A seção subsequente constitui o corpo do procedimento, redigido em Markdown — sistema de formatação por marcações simples, no qual o sinal de sustenido introduz títulos, o hífen introduz itens de lista e os asteriscos duplos produzem destaque.

Dois campos revestem-se de obrigatoriedade. O campo `name` submete-se a regras rígidas: extensão máxima de sessenta e quatro caracteres, restrição a letras minúsculas, algarismos e hifens, vedação de etiquetas XML e vedação expressa das palavras reservadas *anthropic* e *claude*. Assim, `corrigir-por-rubrica` satisfaz os requisitos, ao passo que `Corrigir Por Rubrica` os viola por conter maiúsculas e espaços, e `claude-corretor` os viola por conter palavra reservada. O campo `description`, limitado a mil e vinte e quatro caracteres, não pode permanecer vazio e constitui o elemento determinante do acionamento, matéria do Módulo 4.

Cumpre advertir quanto aos demais campos. A especificação aberta admite, além dos dois obrigatórios, apenas `license`, `compatibility`, `metadata` e `allowed-tools` — este último destinado à pré-autorização de ferramentas durante a execução da Skill. Existem outros campos, dotados de funções relevantes, que operam exclusivamente no ambiente Claude Code e serão referidos no Módulo 6. Sua inclusão em Skill destinada ao claude.ai **não é ignorada: acarreta falha explícita no envio**, com mensagem do tipo *"Unexpected key(s) in SKILL.md frontmatter"*. Trata-se de causa frequente de dificuldade entre participantes que reproduzem exemplos obtidos em fontes destinadas a outro ambiente.

A gravação do arquivo apresenta duas dificuldades operacionais que, embora triviais em sua natureza, respondem por parcela expressiva das falhas iniciais. A primeira concerne à extensão: editores de texto simples acrescentam automaticamente o sufixo `.txt`, razão pela qual se impõe selecionar `Salvar como > Tipo > Todos os arquivos` antes de nomear o arquivo. A segunda concerne à codificação: convém selecionar `Salvar como > Codificação > UTF-8`, sob pena de os caracteres acentuados da língua portuguesa apresentarem-se corrompidos — sintoma cuja causa é de difícil identificação por quem desconhece sua existência. Recomenda-se, ainda, o emprego exclusivo da barra normal nos caminhos internos de arquivo, conforme orientação documental expressa, porquanto a barra invertida compromete a portabilidade entre sistemas.

Quanto ao empacotamento, o arquivo compactado deve conter **a pasta** que abriga o `SKILL.md`, e não o arquivo isoladamente. A verificação é simples e não deve ser dispensada: abrindo-se o arquivo compactado, deve-se observar uma pasta e, em seu interior, o `SKILL.md`. A inversão dessa estrutura constitui a falha mais frequente entre participantes iniciantes e não produz mensagem de erro esclarecedora.

> *» IA: Process — procedimento do exercício. Preservar os breadcrumbs e não traduzir os termos de interface.*

### Exercício Prático (10 minutos)

1. Criar uma pasta nomeada segundo as regras de validação do campo `name`.
2. Elaborar o arquivo `SKILL.md` em `Bloco de Notas > Arquivo > Novo`, contendo cabeçalho com `name` e `description` e corpo com procedimento de, no mínimo, quatro passos iniciados por verbo no imperativo.
3. Gravar em `Bloco de Notas > Arquivo > Salvar como`, selecionando `Tipo > Todos os arquivos` e `Codificação > UTF-8`.
4. Reabrir o arquivo e verificar a integridade dos caracteres acentuados e o posicionamento das linhas delimitadoras na primeira coluna.
5. Compactar em `Explorador de Arquivos > [clique direito na pasta] > Enviar para > Pasta compactada`.
6. Abrir o arquivo compactado e verificar sua estrutura interna.
7. Proceder ao envio em `claude.ai > Configurações > Customize > Skills`.

> *» IA: Statement — pontos de controle e critério de êxito. Preservar o emoji 🏁.*

🏁 **Ponto de controle 1:** o arquivo denomina-se `SKILL.md`, e não `SKILL.md.txt`; os caracteres acentuados apresentam-se íntegros; as linhas de três hifens situam-se na primeira coluna.

🏁 **Ponto de controle 2:** ao abrir o arquivo compactado observa-se uma pasta e, em seu interior, o `SKILL.md`.

**Critério de êxito:** os dois pontos de controle são satisfeitos e o envio conclui-se sem mensagem de erro.

> *» IA: Statement ou Download — prompt-base editável. Conteúdo verbatim; não traduzir os nomes de campo.*

### Mão na massa

Prompt-base para verificação do arquivo antes do envio. Recomenda-se executá-lo em interação nova, anexando o conteúdo do arquivo elaborado.

"""
Segue o conteúdo do arquivo SKILL.md que elaborei:

[colar o conteúdo integral do arquivo]

Verifique e relate:
1. O campo "name" atende às regras de validação — máximo de 64 caracteres,
   apenas letras minúsculas, números e hifens, sem as palavras reservadas
   "anthropic" e "claude"?
2. O cabeçalho contém algum campo além de name, description, license,
   compatibility, metadata e allowed-tools?
3. O campo "description" indica tanto o que a Skill faz quanto quando deve
   ser utilizada?
4. Há algum trecho do corpo que constitua conhecimento geral, dispensável
   por já ser de domínio do modelo?

Relate apenas o que estiver em desconformidade, indicando a linha.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---
---

# Módulo 3 — Ciclo de vida e manutenção

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> *» IA: Statement — nota de encadeamento. Linha única, verbatim.*

> Pressupõe os Módulos 1 e 2. O foco desloca-se da criação inicial para as operações de manutenção, das quais depende todo aperfeiçoamento subsequente.

> *» IA: List — objetivos de aprendizagem. Verbatim, sem acréscimos.*

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Executar as operações de ativação, desativação, substituição e exclusão de uma Skill.
2. Verificar objetivamente que uma substituição de versão se efetivou.
3. Justificar a exigência de que toda verificação se realize em interação nova.

> *» IA: Text — texto descritivo. Pode dividir por parágrafo; não resumir.*

### Texto Descritivo

O ciclo de vida de uma Skill compreende quatro operações: ativação, desativação, substituição por versão revista e exclusão. Este módulo antecede deliberadamente os módulos de qualidade e verificação, porquanto todos eles requerem que o participante altere a Skill e coloque a alteração em vigor. Sem o domínio da substituição, o participante encontrar-se-ia na situação de aperfeiçoar um arquivo em seu computador enquanto avalia outro em produção — vício que compromete toda conclusão dele derivada.

A desativação não implica exclusão: a Skill permanece registrada e deixa de participar das interações. Trata-se de operação útil não apenas para o procedimento de verificação do Módulo 5, mas também para o isolamento diagnóstico, quando se pretende identificar qual entre várias Skills produz determinado comportamento.

A substituição segue procedimento fixo: editar o arquivo, regravá-lo observando tipo e codificação conforme o Módulo 2, compactar novamente a pasta e proceder ao envio. Cumpre registrar que o comportamento do reenvio — se substitui a entrada homônima ou se cria entrada adicional — pode variar conforme a versão da interface, motivo pelo qual se impõe a verificação na primeira ocorrência. Verificando-se duplicação, recomenda-se a exclusão da entrada anterior, dado que a coexistência de duas versões ativas da mesma Skill produz comportamento imprevisível.

Recomenda-se verificar objetivamente a efetivação da substituição, e não presumi-la. O procedimento é simples: insere-se ao final do corpo uma marca reconhecível, procede-se ao envio e, em interação nova, solicita-se ao assistente a última linha do procedimento. A reprodução da marca constitui prova da substituição. Trata-se de técnica elementar que dispensa qualquer recurso técnico e resolve definitivamente uma incerteza que, sem ela, acompanharia o participante por todo o percurso.

Impõe-se, por fim, registrar circunstância de consequência metodológica relevante. Quando uma Skill é acionada, seu conteúdo integra a interação e nela permanece; a substituição do arquivo não reescreve o que já foi incorporado a uma interação em curso. Segue-se que **toda verificação de versão revista deve realizar-se em interação nova**. A inobservância dessa regra produz o efeito de o participante avaliar a versão anterior supondo avaliar a atual, com resultados sistematicamente enganosos. Registre-se, ainda, comportamento correlato: quando a Skill parece deixar de influenciar as respostas ao longo de uma interação extensa, o conteúdo em geral permanece presente, e o modelo é que passou a preferir outro caminho — hipótese em que a correção consiste em reforçar a assertividade das instruções, e não em reescrever o procedimento.

> *» IA: Process — procedimento do exercício. Preservar os breadcrumbs e o modelo editável.*

### Exercício Prático (8 minutos)

1. Localizar a Skill elaborada em `claude.ai > Configurações > Customize > Skills` e identificar o controle de ativação.
2. Desativar e reativar a Skill, observando a alteração na interface.
3. Acrescentar ao final do corpo do `SKILL.md` a linha de marcação de versão.

> *» IA: Statement ou Download — modelo editável de marcação de versão. Conteúdo verbatim.*

"""
Versão 2 — verificação de substituição
"""

> *» IA: Process — continuação do procedimento. Preservar os breadcrumbs.*

4. Regravar em `Bloco de Notas > Arquivo > Salvar como`, mantendo `Tipo > Todos os arquivos` e `Codificação > UTF-8`.
5. Recompactar a pasta e reenviar em `claude.ai > Configurações > Customize > Skills`.
6. Verificar a existência de entrada duplicada e, havendo-a, excluir a anterior.
7. Em interação nova, acionar a Skill e solicitar a última linha do procedimento.

> *» IA: Statement — ponto de controle e critério de êxito. Preservar o emoji 🏁.*

🏁 **Ponto de controle:** em `claude.ai > Configurações > Customize > Skills` observa-se entrada única com o nome da Skill.

**Critério de êxito:** o assistente reproduz a marca inserida no passo 3, o que comprova objetivamente a efetivação da substituição.

> *» IA: Statement ou Download — prompt-base editável. Conteúdo verbatim.*

### Mão na massa

Prompt-base para confirmação de versão. Recomenda-se executá-lo em interação nova, sem mencionar a Skill pelo nome.

"""
[formular uma solicitação que corresponda à situação descrita na descrição
da Skill, sem mencioná-la pelo nome]

Antes de executar, informe:
1. Qual procedimento está sendo seguido.
2. Qual é a última linha desse procedimento.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---
---

# Módulo 4 — Critérios de qualidade

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> *» IA: Statement — nota de encadeamento. Linha única, verbatim.*

> Pressupõe os Módulos 1 a 3. O foco desloca-se da existência da Skill para sua eficácia: examinam-se os atributos que distinguem uma Skill funcional de uma Skill meramente instalada.

> *» IA: List — objetivos de aprendizagem. Verbatim, sem acréscimos.*

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Redigir descrição que contemple a ação executada e a circunstância de emprego.
2. Distinguir falso negativo de falso positivo de acionamento e aplicar a correção correspondente.
3. Organizar o conteúdo entre o arquivo principal e os arquivos de apoio segundo o critério de frequência de uso.

> *» IA: Text — texto descritivo. Pode dividir por parágrafo; não resumir.*

### Texto Descritivo

Conforme estabelecido no Módulo 1, o assistente dispõe, no primeiro nível de carregamento, exclusivamente do nome e da descrição de cada Skill. Segue-se que a descrição constitui o único elemento sobre o qual se assenta a decisão de acionamento. A documentação da Anthropic distingue expressamente dois problemas independentes: o de saber se o assistente selecionou a Skill adequada e o de saber se, uma vez selecionada, executou-a corretamente. Cumpre registrar que uma Skill de procedimento irrepreensível cujo acionamento não se verifica carece inteiramente de utilidade.

Uma descrição adequada contempla duas dimensões — a ação executada e a circunstância de emprego —, sendo a segunda habitualmente omitida. Recomenda-se a redação em terceira pessoa, porquanto a descrição é incorporada às instruções internas do assistente e a inconsistência de pessoa gramatical prejudica a descoberta. Convém, sobretudo, empregar os termos que o solicitante efetivamente utilizaria, e não aqueles que o autor considera mais precisos: observa-se distância sistemática entre o vocabulário de quem redige e o de quem solicita, e é o segundo que o mecanismo de correspondência processa. Recomenda-se, ademais, posicionar o caso principal no início, dado que a listagem de descrições pode ser abreviada quando o número de Skills instaladas é elevado — abreviação que incide prioritariamente sobre as Skills de menor frequência de uso e que pode suprimir precisamente os termos determinantes do acionamento.

Verificam-se dois tipos de falha, que demandam correções de sentido oposto. Denomina-se **falso negativo** a hipótese em que a Skill deveria acionar e não o fez, corrigindo-se pelo acréscimo de vocabulário à descrição. Denomina-se **falso positivo** a hipótese em que a Skill acionou em circunstância imprópria, corrigindo-se pela restrição do escopo — recomendando-se, para tanto, a declaração expressa daquilo que a Skill não faz, recurso comprovadamente eficaz. Dado que os movimentos corretivos são opostos, impõe-se a classificação prévia: a correção aplicada sem diagnóstico apresenta probabilidade equivalente de agravar o problema. Registre-se, por fim, sintoma característico de natureza diversa — quando a Skill funciona ao ser invocada pelo nome mas jamais aciona espontaneamente, a causa reside habitualmente em cabeçalho malformado, hipótese em que a Skill carrega sem descrição.

Quanto à organização do conteúdo, retoma-se aqui o conceito de custo de contexto estabelecido no Módulo 1. A documentação recomenda manter o corpo do `SKILL.md` abaixo de quinhentas linhas; o critério determinante, contudo, não é a extensão, mas a frequência. O conteúdo requerido em toda execução permanece no arquivo principal; o conteúdo ocasionalmente necessário transfere-se para arquivos de apoio, os quais, conforme o terceiro nível de revelação progressiva, não oneram o contexto enquanto não acessados. A arquitetura de pastas constitui, portanto, aplicação direta do princípio do Módulo 1: não se trata de organização estética, mas de instrumento de economia mensurável.

Impõe-se observar a **regra do nível único**: os arquivos de apoio devem ser referenciados diretamente pelo `SKILL.md`, jamais uns pelos outros, porquanto, diante de referências encadeadas, o assistente tende a realizar leituras parciais dos arquivos mais profundos, obtendo informação incompleta. Recomenda-se, adicionalmente, a inserção de sumário em arquivos que excedam cem linhas, a adoção de nomenclatura descritiva — dado que o assistente navega a estrutura pelo nome dos arquivos — e a formulação da remissão de modo a indicar expressamente o conteúdo do arquivo referenciado, e não apenas seu nome. Constitui aplicação de especial relevância ao contexto docente a incorporação de documentos institucionais à pasta, hipótese em que convém acompanhar a referência de instruções de baixa margem interpretativa: a vedação de criar campos inexistentes no modelo e a determinação de assinalar expressamente a informação faltante, em vez de supri-la por verossimilhança.

> *» IA: Process — procedimento do exercício.*

### Exercício Prático (12 minutos)

1. Redigir cinco solicitações: três que devam acionar a Skill e duas que não devam. Recomenda-se que as três primeiras adotem registros distintos — formal, coloquial e abreviado.
2. Executar cada solicitação em interação nova, registrando em tabela: acionou, deveria acionar, classificação.
3. Classificar cada divergência como falso negativo ou falso positivo.
4. Para cada falso negativo, acrescentar à descrição o termo ausente. Para cada falso positivo, acrescentar declaração expressa de não aplicabilidade.
5. Transferir para arquivo de apoio todo conteúdo classificado como ocasionalmente necessário, referenciando-o no `SKILL.md` com indicação expressa de seu conteúdo.
6. Substituir a versão conforme o Módulo 3 e repetir as cinco solicitações.

> *» IA: Statement ou Download — modelo editável de declaração de não aplicabilidade. Conteúdo verbatim.*

"""
Não se aplica a [situação a excluir] nem a [segunda situação a excluir].
"""

> *» IA: Statement — ponto de controle e critério de êxito. Preservar o emoji 🏁.*

🏁 **Ponto de controle:** os nomes de critério que constam da resposta correspondem exatamente aos do arquivo de apoio incorporado, e não a formulações aproximadas.

**Critério de êxito:** o número de resultados corretos na segunda execução supera o da primeira, e o participante identifica, para cada correção aplicada, o tipo de falha que a motivou. Considera-se plenamente atendido quando as cinco solicitações produzem o resultado esperado.

> *» IA: Statement ou Download — prompt-base editável. Conteúdo verbatim.*

### Mão na massa

Prompt-base para antecipação de falsos positivos, executado antes da verificação empírica.

"""
Segue a descrição de uma Skill:

[colar a descrição integral]

Responda:
1. Que tipos de solicitação acionariam esta Skill sem que devessem acioná-la?
2. Que formulações naturais de um docente deixariam de acioná-la, ainda que
   devessem?
3. Proponha uma redação revista que corrija ambos os problemas, mantendo o
   limite de 1.024 caracteres e posicionando o caso principal no início.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---
---

# Módulo 5 — Verificação e confiabilidade

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 5" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir. ▼▼▼*

> *» IA: Statement — nota de encadeamento. Linha única, verbatim.*

> Pressupõe os Módulos 1 a 4. O foco desloca-se da elaboração para a verificação: examinam-se os procedimentos que permitem afirmar, com fundamento, que uma Skill é eficaz e que uma Skill de terceiros é confiável.

> *» IA: List — objetivos de aprendizagem. Verbatim, sem acréscimos.*

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Estabelecer critérios de êxito previamente à observação do resultado.
2. Aferir a eficácia de uma Skill mediante comparação com linha de base.
3. Aplicar critérios de confiabilidade a material de procedência externa, reconhecendo o limite da própria competência técnica de auditoria.

> *» IA: Text — texto descritivo. Pode dividir por parágrafo; não resumir.*

### Texto Descritivo

A avaliação de uma Skill por seu próprio autor encontra-se sujeita a vieses de duas ordens. O primeiro decorre do conhecimento da intenção: quem redigiu o procedimento tende a ler o resultado suprindo mentalmente as lacunas. O segundo decorre da contaminação de contexto, examinada no Módulo 3: a verificação realizada na mesma interação em que a Skill foi elaborada opera sobre um assistente que dispõe de informações indisponíveis a um usuário comum. Impõe-se, em consequência, que toda verificação se realize em interação nova.

O procedimento assenta-se em dois elementos que devem ser estabelecidos **antes** da observação do resultado. O primeiro é a **linha de base**: o registro do desempenho anterior a qualquer intervenção, obtido mediante execução da tarefa sem instrução adicional. O segundo são os **critérios de êxito**, formulados em termos verificáveis — cumprindo registrar que formulações como "adequadamente redigido" não satisfazem o requisito, ao passo que "extensão máxima de uma página, iniciando pelos aspectos positivos" o satisfaz. A anterioridade de ambos não constitui formalidade: critérios estabelecidos após a observação tendem a ser ajustados ao resultado obtido, e linha de base registrada posteriormente já reflete o conhecimento adquirido quanto ao resultado desejado.

A documentação oficial formula recomendação contraintuitiva que merece registro: convém construir as avaliações antes de redigir a documentação extensa. A execução das tarefas sem nenhuma Skill revela precisamente onde o assistente falha, e tais falhas constituem o escopo real do procedimento a elaborar. Procede-se, assim, à solução de problemas verificados, e não de problemas antecipados. Recomenda-se aferir separadamente a dimensão do **acionamento**, conforme a metodologia do Módulo 4, e a dimensão da **qualidade**, aferida contra os critérios previamente estabelecidos — porquanto uma Skill pode apresentar acionamento irrepreensível e resultado insatisfatório, ou a situação inversa, e as correções pertencem a módulos distintos. Convém registrar, ademais, que a eficácia depende do modelo subjacente, razão pela qual se recomenda a verificação em todos os modelos que se pretenda utilizar.

Retoma-se neste ponto a informação plantada ao final do Módulo 1, quanto à não abrangência das Skills por acordos de retenção zero de dados. Dela decorre consequência normativa direta: **não devem ser incorporados aos arquivos de uma Skill dados pessoais ou sensíveis de estudantes** — nomes, matrículas, notas identificáveis, laudos ou situações de assistência estudantil. Necessitando-se de exemplos realistas, impõe-se a anonimização prévia. O conteúdo de uma Skill deve ser tratado como material armazenado.

No que concerne a material de procedência externa, a documentação da Anthropic orienta o emprego exclusivo de Skills provenientes de fontes confiáveis, alertando para os riscos de uso indevido de ferramentas, exposição de dados e comprometimento por dependências externas — estas últimas de risco particular, porquanto o conteúdo obtido de endereços externos pode veicular instruções maliciosas e mesmo uma Skill originalmente confiável pode ser comprometida se aquilo de que depende se alterar. Pesquisas acadêmicas recentes, que devem ser interpretadas como levantamentos sobre ecossistemas públicos e não como avaliação do repositório oficial, oferecem a dimensão do problema: estudo de janeiro de 2026, ao analisar trinta e um mil Skills coletadas em dois mercados, identificou padrão de vulnerabilidade em 26,1% delas, com incidência superior naquelas que incorporam scripts executáveis; publicação preliminar de agosto de 2026, ao examinar cento e trinta e oito mil arquivos públicos, identificou ao menos um defeito detectável em 91,8% deles, predominando problemas de redação e organização sobre ameaças deliberadas.

Impõe-se, quanto à auditoria, delimitação honesta de competência. Ao docente sem formação técnica compete verificar a **coerência entre a descrição declarada e o procedimento efetivamente descrito** — critério acessível e revelador, porquanto uma Skill que executa operação não anunciada apresenta sinal de alerta independentemente da intenção subjacente. Compete-lhe igualmente verificar a ausência de menção a credenciais e a rastreabilidade da procedência. Verificando-se, contudo, a existência de pasta de scripts executáveis, de acesso a endereços externos ou de instruções que não compreenda, recomenda-se a abstenção de instalar sem assessoria técnica. O reconhecimento do próprio limite constitui, nesta matéria, competência e não deficiência.

> *» IA: Process — procedimento do exercício.*

### Exercício Prático (12 minutos)

1. Redigir quatro critérios de êxito em formulação verificável, antes de qualquer execução.
2. Executar a tarefa em interação nova, com a Skill desativada conforme o Módulo 3, e registrar o resultado.
3. Avaliar esse resultado contra os quatro critérios, consignando o número de critérios atendidos.
4. Executar a mesma tarefa em interação nova, com a Skill ativa, e avaliar contra os mesmos critérios.
5. Para cada critério não atendido, identificar o módulo que trata da correção pertinente.
6. Aplicar à própria Skill a verificação de coerência entre descrição e procedimento, examinando se alguma etapa executa operação não anunciada na descrição.

> *» IA: Statement — critério de êxito. Verbatim.*

**Critério de êxito:** o participante apresenta dois valores numéricos e demonstra que o segundo supera o primeiro. Considera-se plenamente atendido quando, adicionalmente, cada critério não satisfeito encontra-se associado a um módulo de referência e a verificação de coerência não identifica divergência.

> *» IA: Statement ou Download — prompt-base editável. Conteúdo verbatim.*

### Mão na massa

Prompt-base para auditoria de coerência, aplicável tanto à Skill própria quanto a material de procedência externa.

"""
Segue o conteúdo integral de uma Skill:

[colar descrição e procedimento]

Analise exclusivamente a coerência entre o que a descrição declara e o que o
procedimento executa. Relate:
1. Etapas do procedimento que executam operação não anunciada na descrição.
2. Referências a endereços externos, credenciais ou envio de dados.
3. Menções a arquivos ou scripts cujo conteúdo não esteja explicitado.

Não avalie a qualidade do procedimento nem proponha melhorias. Restrinja-se
à correspondência entre o declarado e o executado.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 5" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---
---

# Módulo 6 — Síntese e Aplicação Integrada

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 6" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja tabela de critérios no meio. ▼▼▼*

> *» IA: Statement — nota de encadeamento. Linha única, verbatim.*

> Pressupõe integralmente os Módulos 1 a 5. Não introduz conteúdo novo: articula as cinco competências desenvolvidas em atividade de aplicação a caso real do participante.

> *» IA: List — objetivos de aprendizagem. Verbatim, sem acréscimos.*

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Articular as competências de elaboração, manutenção, refinamento e verificação em percurso completo de produção.
2. Fundamentar cada decisão de escrita mediante o princípio que a justifica.
3. Avaliar o próprio trabalho segundo critérios objetivos e identificar as correções pendentes.

> *» IA: Text — texto descritivo. Pode dividir por parágrafo; não resumir.*

### Texto Descritivo

O percurso desenvolvido nos cinco módulos anteriores estruturou-se segundo progressão que convém explicitar. Estabeleceu-se, primeiramente, que a informação é carregada em níveis e que o espaço de processamento é finito — do que decorre a concisão como requisito mensurável, e não como preferência. Traduziu-se esse fundamento em procedimento de elaboração, no qual as regras de validação e os requisitos de gravação constituem condições de existência do artefato. Instituíram-se, em seguida, as operações de manutenção, sem as quais nenhum aperfeiçoamento seria exequível. Introduziram-se os critérios que distinguem eficácia de mera existência. Estabeleceram-se, por fim, os procedimentos de verificação, sem os quais qualquer afirmação sobre a qualidade permanece no domínio da impressão.

Observa-se que o eixo comum aos cinco módulos é a substituição do juízo impressivo pelo juízo fundamentado. A concisão não se justifica por elegância, mas por custo de contexto — princípio plantado no Módulo 1 e retomado no Módulo 4 como fundamento da arquitetura de arquivos. A restrição quanto a dados pessoais não constitui recomendação genérica de prudência, mas decorrência direta da política de retenção registrada no Módulo 1 e retomada no Módulo 5. A descrição não se avalia por correção gramatical, mas por taxa de acionamento verificada. A Skill não se considera boa por parecer boa, mas por atender a critérios estabelecidos previamente. Trata-se, cumpre notar, do mesmo rigor metodológico que o participante já aplica em sua área de investigação; a novidade reside em sua aplicação a um instrumento de trabalho.

Cumpre, por fim, situar o percurso no território mais amplo, a fim de que o participante interprete corretamente o material que venha a encontrar. As Skills operam em três superfícies distintas — claude.ai, Claude Code e a interface de programação —, que **não se sincronizam entre si**. O ambiente Claude Code admite campos adicionais de cabeçalho, entre os quais o controle de invocação, que restringe o acionamento a comando expresso do usuário e que a Anthropic recomenda para procedimentos dotados de efeito colateral. Tais campos, contudo, não operam na superfície utilizada neste curso, e sua inclusão acarreta falha de envio, conforme advertido no Módulo 2. Registre-se ainda a distinção entre Skill e MCP: este último fornece ao assistente acesso a sistemas externos, ao passo que a Skill codifica o conhecimento sobre o modo como determinada instituição utiliza tal sistema — sendo, portanto, mecanismos complementares e não concorrentes.

> *» IA: Process — atividade integradora, procedimento numerado. Preservar os breadcrumbs.*

### Exercício Prático — Atividade Integradora (14 minutos)

1. Selecionar, dentre as tarefas recorrentes da própria rotina, aquela cuja padronização produza maior benefício, aplicando os critérios de recorrência, existência de forma correta estabelecida e unidade de responsabilidade.
2. Revisar integralmente a Skill elaborada, verificando: descrição contemplando as duas dimensões e ao menos uma declaração de não aplicabilidade; corpo redigido em instruções iniciadas por verbo no imperativo, sem conteúdo de domínio do modelo; documento institucional incorporado e referenciado com indicação expressa de seu conteúdo; instruções de baixa margem interpretativa nos pontos que não admitam variação.
3. Substituir a versão em `claude.ai > Configurações > Customize > Skills` e verificar objetivamente a efetivação.
4. Executar a verificação de acionamento com cinco solicitações e a verificação de qualidade contra os quatro critérios estabelecidos.
5. Aplicar a verificação de coerência entre descrição e procedimento.
6. Consignar, ao final do `SKILL.md`, a data da revisão.
7. Registrar, em uma frase, a circunstância em que um colega deveria empregar a Skill.

> *» IA: Statement — ponto de controle. Preservar o emoji 🏁.*

🏁 **Ponto de controle:** em `claude.ai > Configurações > Customize > Skills` observa-se entrada única, e a execução em interação nova produz resultado conforme aos quatro critérios estabelecidos.

> *» IA: Checklist ou Table — critérios de avaliação. Um item por linha, verbatim.*

**Tabela de Critérios de Avaliação**

| Critério | Atendido? |
|---|---|
| O campo `name` atende às regras de validação | |
| O cabeçalho contém apenas campos admitidos pela especificação | |
| A descrição contempla a ação executada e a circunstância de emprego | |
| A descrição declara expressamente ao menos uma hipótese de não aplicabilidade | |
| O corpo não contém conteúdo que o modelo já domine | |
| Cada passo do procedimento inicia-se por verbo no imperativo | |
| Há ao menos um arquivo de apoio referenciado diretamente pelo `SKILL.md` | |
| A remissão ao arquivo de apoio indica expressamente seu conteúdo | |
| Documento institucional próprio foi incorporado e é efetivamente utilizado | |
| Nenhum dado pessoal de estudante foi incorporado a qualquer arquivo | |
| O acionamento verifica-se em três formulações de registro distinto | |
| O acionamento não se verifica nas duas solicitações que não o deveriam produzir | |
| Os critérios de êxito foram estabelecidos previamente à observação | |
| O número de critérios atendidos com a Skill supera o da linha de base | |
| A verificação de coerência não identificou operação não anunciada | |
| A data da revisão consta do `SKILL.md` | |

> *» IA: Statement — critério de êxito da atividade integradora. Verbatim.*

**Critério de êxito:** consideram-se satisfatoriamente cumpridos os objetivos do curso quando ao menos treze dos dezesseis critérios encontram-se atendidos, incluindo-se necessariamente entre eles os relativos à verificação por linha de base, à ausência de dados pessoais e à coerência entre descrição e procedimento.

> *» IA: Statement ou Download — prompt-base editável da atividade integradora. Conteúdo verbatim.*

### Mão na massa

Prompt-base para revisão final assistida. Recomenda-se executá-lo em interação nova, antes da última substituição de versão.

"""
Segue o conteúdo integral da minha Skill, incluindo os arquivos de apoio:

[colar SKILL.md e arquivos de apoio]

Atue como revisor e relate, sem propor reescrita integral:
1. Trechos do corpo que constituam conhecimento geral e possam ser suprimidos.
2. Instruções ambíguas — pontos em que dois leitores fariam coisas diferentes.
3. Conteúdo classificável como ocasionalmente necessário, que deveria migrar
   para arquivo de apoio.
4. Situações previsíveis que o procedimento não cobre.

Para cada item, indique a linha e proponha a correção mínima suficiente.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 6" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---
---

> *» IA: Text — encerramento, primeiro parágrafo. Sem marcadores de fronteira de lição nesta seção.*

# Encerramento

Cumpriu-se a finalidade estabelecida no Objetivo Geral. O participante que percorreu integralmente os seis módulos dispõe de ao menos uma Skill funcional, aplicada a tarefa real de sua rotina, cuja eficácia foi aferida por comparação com linha de base registrada previamente à intervenção. Mais relevante que o artefato produzido, contudo, é o método incorporado: a substituição da avaliação impressiva pela avaliação fundamentada em critérios estabelecidos de antemão. Recomenda-se, todavia, registrar que a competência aqui desenvolvida consolida-se pela prática regular. A segunda Skill demanda fração do tempo exigido pela primeira, porquanto a dificuldade inicial reside na compreensão da lógica subjacente, e não na operação da ferramenta. Convém, por essa razão, que o participante elabore ao menos mais duas Skills nas semanas subsequentes, dando preferência às tarefas submetidas a formato institucional obrigatório — aquelas que, por definição, nenhum modelo poderia inferir.

> *» IA: Text — encerramento, segundo parágrafo.*

Quanto ao aprofundamento, três caminhos apresentam-se pertinentes. O primeiro consiste no exame do repositório público mantido pela Anthropic, no qual Skills reais podem ser analisadas em sua estrutura completa, constituindo material de estudo superior a qualquer descrição conceitual. O segundo consiste na exploração da Skill oficial `skill-creator`, destinada a auxiliar a elaboração, a avaliação e o refinamento de outras Skills, e que incorpora recursos de comparação entre versões e de ajuste da descrição responsável pelo acionamento. O terceiro, pertinente apenas a participantes cujas atividades envolvam manipulação de arquivos e execução de comandos, consiste no exame do ambiente Claude Code, cujas particularidades foram referidas no Módulo 6. Registre-se, por fim, que o ecossistema encontra-se em transformação acelerada: denominações de menu, planos e limites técnicos alteram-se com frequência, razão pela qual se recomenda a revalidação periódica dos procedimentos aqui descritos, bem como o registro da data de revisão no interior de cada Skill produzida. Os princípios permanecem; os rótulos deslocam-se.

> *» IA: Statement — síntese final. Preservar o destaque inicial. Verbatim.*

> **Síntese:** uma Agent Skill constitui unidade modular e reutilizável de conhecimento procedural, destinada a ensinar a um assistente a execução consistente de uma categoria de tarefas. Sua eficácia não decorre da sofisticação técnica, mas de três atributos verificáveis — a precisão da descrição que determina o acionamento, a economia do procedimento que respeita o custo de contexto, e a existência de evidência que substitua a impressão pelo dado. No contexto docente, as Skills de maior valor duradouro são precisamente aquelas que codificam procedimentos institucionais específicos, dado que nenhum modelo, por mais capaz, inferirá as normas que somente o próprio docente conhece.
