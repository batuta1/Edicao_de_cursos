# Plano de Aula — Claude Skills (Essentials)

---

## Identificação

| Campo | Definição |
|---|---|
| **Curso** | Claude Skills: fundamentos, criação e avaliação de procedimentos reutilizáveis para assistentes de Inteligência Artificial |
| **Natureza** | Curso curto, introdutório e prático |
| **Carga horária** | 80 minutos |
| **Público-alvo** | Docentes do ensino superior, de qualquer área do conhecimento, sem experiência prévia com desenvolvimento de software |
| **Pré-requisitos** | Nenhum conhecimento técnico prévio. Requer-se apenas familiaridade com o uso de navegador e com a criação e gravação de arquivos em computador pessoal |
| **Recursos necessários** | Computador com navegador e conexão à internet; conta ativa em claude.ai com o recurso de Skills habilitado; editor de texto simples; um documento institucional de referência do próprio participante (rubrica, formulário ou modelo de parecer) |

> **Nota de versão:** a disponibilidade do recurso de criação de Skills varia conforme o plano da conta e a configuração de execução de código. As fontes documentais consultadas divergem quanto aos planos abrangidos. Recomenda-se, portanto, que o participante verifique a existência da seção "Skills" nas configurações da própria conta antes do início do curso. Não havendo tal seção, o percurso pode ser cumprido integralmente na modalidade de elaboração dos arquivos, sem a etapa de envio.

---

### Objetivo Geral

Capacitar o docente a converter procedimentos de trabalho recorrentes em Agent Skills — pacotes de conhecimento procedural que assistentes de Inteligência Artificial carregam sob demanda —, de modo que, ao término do curso, o participante disponha de ao menos uma Skill funcional, aplicada a uma tarefa real de sua rotina acadêmica, cuja eficácia tenha sido verificada mediante comparação com uma linha de base previamente registrada.

---

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Explicar o funcionamento das Agent Skills, incluindo o mecanismo de revelação progressiva pelo qual o assistente carrega apenas a informação pertinente a cada etapa, e distinguir esse mecanismo de outras formas de instrução.
2. Elaborar e disponibilizar uma Skill própria, observando as regras de validação dos campos obrigatórios, os requisitos de gravação de arquivo e o procedimento de substituição de versão.
3. Avaliar criticamente a qualidade de uma Skill quanto à precisão do acionamento, à concisão do procedimento e à adequação da arquitetura de arquivos de apoio.
4. Verificar a eficácia de uma Skill por meio de comparação com linha de base e critérios de êxito estabelecidos previamente, bem como aplicar critérios de confiabilidade a Skills de procedência externa.

---

### Estrutura e Sequência dos Módulos

A progressão adotada é cumulativa: cada módulo pressupõe as competências desenvolvidas nos anteriores e desloca o foco de investigação. O Módulo 1 estabelece o fundamento conceitual, sem o qual as decisões de escrita dos módulos seguintes careceriam de justificativa. O Módulo 2 traduz esse fundamento em procedimento operacional de elaboração. O Módulo 3 introduz os critérios de qualidade que separam uma Skill existente de uma Skill eficaz. O Módulo 4 institui os procedimentos de verificação, tanto do próprio trabalho quanto de material de terceiros. O Módulo 5 articula as quatro competências em atividade integradora.

| Módulo | Título | Referência | Tempo |
|---|---|---|---|
| 1 | Fundamentos das Agent Skills | Arquitetura e revelação progressiva | 15 min |
| 2 | Elaboração e ciclo de vida | Estrutura do SKILL.md e operações de manutenção | 20 min |
| 3 | Critérios de qualidade | Acionamento, concisão e arquitetura da informação | 20 min |
| 4 | Verificação e confiabilidade | Avaliação por evidência e auditoria de procedência | 15 min |
| 5 | Síntese e Aplicação Integrada | Atividade integradora | 10 min |

---
---

# Módulo 1 — Fundamentos das Agent Skills

> Ponto de partida do percurso. Não pressupõe conhecimento prévio; estabelece o vocabulário e o modelo de funcionamento que sustentam todos os módulos subsequentes.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Definir Agent Skill, distinguindo-a de instrução pontual e de mecanismo de memória.
2. Descrever os três níveis de carregamento de informação e o custo associado a cada um.
3. Justificar, com base no custo de contexto, por que a concisão constitui requisito de qualidade e não mera preferência estilística.

### Texto Descritivo

Denomina-se **Agent Skill** uma pasta autocontida cujo ponto de entrada é um arquivo nomeado `SKILL.md`, contendo instruções procedimentais e, opcionalmente, documentos de referência, modelos e demais recursos. O formato foi introduzido pela Anthropic em outubro de 2025 como funcionalidade do assistente Claude e posteriormente publicado como especificação aberta, circunstância que confere às Skills bem elaboradas certo grau de portabilidade entre assistentes que adotem o mesmo padrão. Cumpre registrar que a Skill não se confunde com um comando salvo: enquanto a instrução pontual atende a uma solicitação específica, a Skill codifica um procedimento aplicável a uma categoria de tarefas, sendo carregada pelo assistente quando este reconhece a pertinência da categoria.

O mecanismo que rege esse carregamento denomina-se **revelação progressiva** (*progressive disclosure*) e opera em três níveis distintos. No primeiro nível, o assistente recebe, ao início de cada interação, apenas o nome e a descrição de cada Skill disponível — informação cujo custo a Anthropic estima em aproximadamente cem tokens por Skill, sendo o token a unidade de medida do texto processado, correspondente aproximadamente a uma palavra curta ou a um fragmento de palavra. No segundo nível, uma vez reconhecida a pertinência, o assistente procede à leitura integral do `SKILL.md`, cuja extensão a documentação recomenda manter abaixo de aproximadamente cinco mil tokens. No terceiro nível, os arquivos de apoio permanecem inacessados e sem custo algum até que a execução da tarefa os torne necessários.

Depreende-se dessa arquitetura uma consequência de ordem prática que orienta todas as decisões subsequentes de escrita. O espaço em que o assistente processa informação — designado **janela de contexto** — é finito e compartilhado entre a solicitação do usuário, o histórico da interação e os metadados de todas as Skills instaladas. A documentação da Anthropic caracteriza esse espaço como um bem público. Segue-se que a instalação de numerosas Skills não acarreta prejuízo significativo, ao passo que uma única Skill de extensão excessiva compromete o desempenho no momento em que é acionada.

Dessa mesma constatação deriva a recomendação mais reiterada da documentação oficial: não convém instruir o assistente sobre aquilo que ele já domina. Um procedimento que dedique parágrafos a explicar o conceito de rubrica avaliativa desperdiça espaço, porquanto o modelo já dispõe dessa informação. O conteúdo que justifica o custo é precisamente aquele que o modelo não poderia inferir — a rubrica específica da disciplina, a ordem estabelecida pelo colegiado, a restrição de extensão imposta pela instituição.

Convém, por fim, registrar a distinção entre dois tipos de Skill identificados pela Anthropic. As **Skills de ampliação de capacidade** ensinam ao modelo tarefas que este ainda não executa com confiabilidade suficiente, e tendem a perder relevância à medida que os modelos evoluem. As **Skills de preferência codificada** registram o processo desejado por uma pessoa ou instituição e conservam sua utilidade indefinidamente, dado que nenhum modelo, por mais capaz, inferirá as normas internas de uma instituição específica. Observa-se que, no contexto docente, a segunda categoria concentra as aplicações de maior valor.

### Exercício Prático (5 minutos)

**Questão de múltipla escolha.**

Um docente elabora uma Skill destinada à correção de trabalhos e inclui, no corpo do `SKILL.md`, três parágrafos explicando o que são rubricas avaliativas, sua função formativa e sua fundamentação na literatura pedagógica. Em seguida, apresenta os quatro critérios específicos de sua disciplina. Considerando o princípio de custo de contexto, qual avaliação se aplica a esse material?

**a)** O material está adequado, uma vez que a contextualização teórica auxilia o assistente a compreender a finalidade da tarefa.

**b)** Os três parágrafos iniciais devem ser suprimidos, porquanto veiculam conhecimento de que o modelo já dispõe; os quatro critérios específicos devem ser preservados, por constituírem informação que o modelo não poderia inferir.

**c)** Todo o material deve ser transferido para um arquivo de apoio, mantendo-se o `SKILL.md` reservado exclusivamente ao acionamento.

**d)** O material está inadequado por extensão, devendo ser reduzido pela metade de forma proporcional, preservando-se parte de cada seção.

**Gabarito:** alternativa **b**.

**Fundamentação:** a alternativa (a) contraria a orientação documental expressa de não instruir o modelo sobre aquilo que ele já domina. A alternativa (c) equivoca-se quanto à natureza dos arquivos de apoio, que se destinam a conteúdo ocasionalmente necessário, e não a conteúdo dispensável — a rubrica específica é requerida em toda execução. A alternativa (d) aplica critério quantitativo onde se impõe critério qualitativo: a redução não deve ser proporcional, mas seletiva, distinguindo o que o modelo já sabe daquilo que somente o autor sabe.

**Critério de êxito:** o participante identifica a alternativa correta e articula, em uma frase, o critério que fundamenta a distinção entre o conteúdo suprimível e o conteúdo indispensável.

---
---

# Módulo 2 — Elaboração e ciclo de vida

> Pressupõe o Módulo 1. O foco desloca-se do funcionamento conceitual para o procedimento operacional de elaboração, disponibilização e manutenção de uma Skill própria.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Identificar as duas partes constitutivas do arquivo `SKILL.md` e a função de cada uma.
2. Aplicar corretamente as regras de validação do campo `name` e os requisitos de gravação de arquivo.
3. Executar o procedimento de substituição de versão e verificar objetivamente que a substituição se efetivou.

### Texto Descritivo

O arquivo `SKILL.md` compõe-se de duas seções funcionalmente distintas, cuja separação reproduz a lógica do resumo e do corpo de um artigo científico: a primeira destina-se à decisão sobre a pertinência da leitura; a segunda, à execução propriamente dita. A seção inicial, delimitada por duas linhas contendo três hifens, denomina-se cabeçalho ou *frontmatter* e adota o formato YAML, no qual cada linha corresponde a um par de campo e valor. A seção subsequente constitui o corpo do procedimento, redigido em Markdown — sistema de formatação por marcações simples.

Dois campos revestem-se de obrigatoriedade. O campo `name` submete-se a regras rígidas de validação: extensão máxima de sessenta e quatro caracteres, restrição a letras minúsculas, algarismos e hifens, e vedação expressa das palavras reservadas *anthropic* e *claude*. O campo `description`, limitado a mil e vinte e quatro caracteres, não pode permanecer vazio e constitui o elemento determinante do acionamento, matéria tratada no módulo seguinte. Cumpre advertir que a especificação aberta admite, além desses, apenas os campos `license`, `compatibility`, `metadata` e `allowed-tools` — este último destinado à pré-autorização de ferramentas durante a execução. A inclusão de campo diverso não é ignorada: **acarreta falha explícita no envio**, circunstância que constitui causa frequente de dificuldade entre participantes que reproduzem exemplos obtidos em fontes destinadas a outro ambiente de execução.

A gravação do arquivo apresenta duas dificuldades de ordem operacional que, embora triviais em sua natureza, respondem por parcela expressiva das falhas iniciais. A primeira concerne à extensão: editores de texto simples tendem a acrescentar automaticamente o sufixo `.txt`, razão pela qual se recomenda selecionar a opção "Todos os arquivos" no campo de tipo antes de nomear o arquivo. A segunda concerne à codificação de caracteres: convém selecionar **UTF-8**, sob pena de os caracteres acentuados da língua portuguesa apresentarem-se corrompidos — sintoma cuja causa é de difícil identificação por quem desconhece sua existência. Recomenda-se, ainda, o emprego exclusivo da barra normal nos caminhos internos de arquivo, conforme orientação documental expressa, porquanto a barra invertida compromete a portabilidade entre sistemas.

O ciclo de vida da Skill compreende quatro operações: ativação, desativação, substituição por versão revista e exclusão. A substituição merece atenção particular, dado que todo aperfeiçoamento subsequente dela depende. O procedimento consiste em editar o arquivo, regravá-lo observando tipo e codificação, compactar novamente a pasta — e não o arquivo isoladamente — e proceder ao envio. Recomenda-se verificar objetivamente a efetivação da substituição mediante a inserção de uma marca reconhecível ao final do corpo, cuja recuperação por meio de solicitação direta confirma que a versão vigente é a nova. Observa-se que o comportamento do reenvio quanto à substituição ou à duplicação de entradas pode variar conforme a versão da interface, motivo pelo qual se impõe a verificação na primeira ocorrência.

Cumpre registrar, por fim, que o conteúdo de uma Skill acionada permanece na interação em que foi carregado. Segue-se que a avaliação de qualquer versão revista deve realizar-se necessariamente em interação nova, sob pena de o participante avaliar a versão anterior supondo avaliar a atual — vício metodológico que compromete toda conclusão dele derivada.

### Exercício Prático (10 minutos)

**Procedimento.**

1. Criar, no computador, uma pasta nomeada segundo as regras de validação do campo `name`.
2. Elaborar o arquivo `SKILL.md`, contendo cabeçalho com os campos `name` e `description` e corpo com procedimento de, no mínimo, quatro passos iniciados por verbo no imperativo.
3. Gravar o arquivo observando a seleção do tipo "Todos os arquivos" e da codificação UTF-8.
4. Reabrir o arquivo e verificar a integridade dos caracteres acentuados e o posicionamento das linhas delimitadoras do cabeçalho na primeira coluna.
5. Compactar a pasta e abrir o arquivo compactado, verificando que este contém uma pasta e que o `SKILL.md` encontra-se em seu interior.
6. Proceder ao envio pela seção de Skills das configurações da conta.
7. Acrescentar ao final do corpo a linha `Versão 2 — verificação de substituição`, regravar, recompactar e reenviar.
8. Em interação nova, acionar a Skill e solicitar a última linha do procedimento.

**Critério de êxito:** o assistente reproduz a marca inserida no passo 7, o que comprova objetivamente a efetivação da substituição de versão. Verifica-se, adicionalmente, que os caracteres acentuados apresentam-se íntegros e que o arquivo compactado possui a estrutura correta.

---
---

# Módulo 3 — Critérios de qualidade

> Pressupõe os Módulos 1 e 2. O foco desloca-se da existência da Skill para sua eficácia: examinam-se os atributos que distinguem uma Skill funcional de uma Skill meramente instalada.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Redigir descrição que contemple as duas dimensões requeridas — a ação executada e a circunstância de emprego.
2. Distinguir falso negativo de falso positivo de acionamento e aplicar a correção correspondente a cada um.
3. Organizar o conteúdo da Skill entre o arquivo principal e arquivos de apoio segundo o critério de frequência de uso.

### Texto Descritivo

Conforme estabelecido no Módulo 1, o assistente dispõe, no primeiro nível de carregamento, exclusivamente do nome e da descrição de cada Skill. Segue-se que a descrição constitui o único elemento sobre o qual se assenta a decisão de acionamento, circunstância que explica sua centralidade. A documentação da Anthropic distingue expressamente dois problemas independentes: o de saber se o assistente selecionou a Skill adequada e o de saber se, uma vez selecionada, executou-a corretamente. Cumpre registrar que uma Skill de procedimento irrepreensível cujo acionamento não se verifica carece inteiramente de utilidade.

Uma descrição adequada contempla duas dimensões: a ação que a Skill executa e a circunstância em que deve ser empregada. A segunda dimensão é habitualmente omitida. Recomenda-se, ademais, a redação em terceira pessoa, porquanto a descrição é incorporada às instruções internas do assistente e a inconsistência de pessoa gramatical prejudica a descoberta. Convém, sobretudo, empregar os termos que o solicitante efetivamente utilizaria, e não aqueles que o autor considera mais precisos: observa-se distância sistemática entre o vocabulário de quem redige a descrição e o de quem formula a solicitação, e é a segunda que o mecanismo de correspondência processa.

Verificam-se dois tipos de falha de acionamento, que demandam correções de sentido oposto. Denomina-se **falso negativo** a hipótese em que a Skill deveria acionar e não o fez; sua correção consiste em acrescentar vocabulário à descrição. Denomina-se **falso positivo** a hipótese em que a Skill acionou em circunstância imprópria; sua correção consiste em restringir o escopo, recomendando-se para tanto a declaração expressa daquilo que a Skill não faz. Dado que os movimentos corretivos são opostos, impõe-se a classificação prévia da falha: a correção aplicada sem diagnóstico apresenta probabilidade equivalente de agravar o problema.

Registre-se ainda uma causa de falha de acionamento pouco conhecida. Quando o número de Skills instaladas é elevado, a listagem de descrições permanentemente carregada pode exceder o orçamento de espaço a ela reservado, hipótese em que algumas descrições são abreviadas — com eventual supressão precisamente dos termos que determinariam o acionamento. A abreviação não é aleatória: incide prioritariamente sobre as Skills de menor frequência de uso. Recomenda-se, por essa razão, posicionar o caso principal no início da descrição.

Quanto à organização do conteúdo, a documentação recomenda manter o corpo do `SKILL.md` abaixo de quinhentas linhas. O critério determinante, contudo, não é a extensão, mas a frequência: o conteúdo requerido em toda execução permanece no arquivo principal; o conteúdo ocasionalmente necessário transfere-se para arquivos de apoio, os quais, conforme exposto no Módulo 1, não oneram o contexto enquanto não acessados. Impõe-se observar a **regra do nível único**: os arquivos de apoio devem ser referenciados diretamente pelo `SKILL.md`, jamais uns pelos outros, porquanto, diante de referências encadeadas, o assistente tende a realizar leituras parciais dos arquivos mais profundos, obtendo informação incompleta. Recomenda-se, adicionalmente, a inserção de sumário em arquivos que excedam cem linhas e a adoção de nomenclatura descritiva, dado que o assistente navega a estrutura de pastas pelo nome dos arquivos.

Constitui aplicação particularmente relevante ao contexto docente a incorporação de documentos institucionais à pasta da Skill — rubricas aprovadas em colegiado, formulários de plano de ensino, modelos de parecer. Nessa hipótese, convém acompanhar a referência de instruções de baixa margem interpretativa: a vedação de criar campos inexistentes no modelo e a determinação de assinalar expressamente a informação faltante, em vez de supri-la por verossimilhança.

> **Atenção:** não devem ser incorporados aos arquivos de uma Skill dados pessoais ou sensíveis de estudantes — nomes, matrículas, notas identificáveis, laudos ou situações de assistência estudantil. Cumpre registrar que, conforme a documentação da Anthropic, as Skills não se encontram abrangidas por acordos de retenção zero de dados, aplicando-se-lhes a política padrão de retenção.

### Exercício Prático (10 minutos)

**Procedimento.**

1. Redigir cinco solicitações: três que devam acionar a Skill elaborada no Módulo 2 e duas que não devam. Recomenda-se que as três primeiras adotem registros distintos — formal, coloquial e abreviado.
2. Executar cada solicitação em interação nova, registrando em tabela as colunas: acionou, deveria acionar, classificação.
3. Classificar cada divergência como falso negativo ou falso positivo.
4. Para cada falso negativo, acrescentar à descrição o termo ausente. Para cada falso positivo, acrescentar declaração expressa de não aplicabilidade.
5. Substituir a versão conforme o procedimento do Módulo 2 e repetir as cinco solicitações.

**Critério de êxito:** o número de resultados corretos na segunda execução supera o da primeira, e o participante identifica, para cada correção aplicada, o tipo de falha que a motivou. Considera-se plenamente atendido o critério quando as cinco solicitações produzem o resultado esperado.

---
---

# Módulo 4 — Verificação e confiabilidade

> Pressupõe os Módulos 1 a 3. O foco desloca-se da elaboração para a verificação: examinam-se os procedimentos que permitem afirmar, com fundamento, que uma Skill é eficaz e que uma Skill de terceiros é confiável.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Estabelecer critérios de êxito previamente à observação do resultado.
2. Aferir a eficácia de uma Skill mediante comparação com linha de base registrada anteriormente à intervenção.
3. Aplicar critérios de confiabilidade a Skills de procedência externa, reconhecendo o limite de sua própria competência técnica de auditoria.

### Texto Descritivo

A avaliação de uma Skill por seu próprio autor encontra-se sujeita a vieses de duas ordens. O primeiro decorre do conhecimento da intenção: quem redigiu o procedimento tende a ler o resultado suprindo mentalmente as lacunas existentes. O segundo decorre da contaminação de contexto: a verificação realizada na mesma interação em que a Skill foi elaborada opera sobre um assistente que dispõe de informações indisponíveis a um usuário comum. Impõe-se, em consequência, que toda verificação se realize em interação nova.

O procedimento de verificação assenta-se em dois elementos que devem ser estabelecidos **antes** da observação do resultado. O primeiro é a **linha de base**: o registro do desempenho anterior a qualquer intervenção, obtido mediante execução da tarefa sem nenhuma instrução adicional. O segundo são os **critérios de êxito**, formulados em termos verificáveis. A anterioridade de ambos não constitui formalidade: critérios estabelecidos após a observação tendem a ser ajustados ao resultado obtido, e linha de base registrada após a elaboração da Skill já reflete o conhecimento que o autor adquiriu quanto ao que deseja obter.

A documentação oficial formula recomendação que se afigura contraintuitiva e que merece registro: convém construir as avaliações antes de redigir a documentação extensa. A lógica subjacente é a seguinte — a execução das tarefas sem nenhuma Skill revela precisamente onde o assistente falha, e tais falhas constituem o escopo real do procedimento a ser elaborado. Procede-se, assim, à solução de problemas verificados, e não de problemas antecipados.

Recomenda-se aferir separadamente duas dimensões, cujas correções pertencem a módulos distintos deste curso. A dimensão do **acionamento** responde à indagação sobre em quantas solicitações a Skill foi selecionada corretamente, conforme a metodologia do Módulo 3. A dimensão da **qualidade** responde à indagação sobre a adequação do resultado nos casos em que houve acionamento, aferida contra os critérios previamente estabelecidos. Observa-se que uma Skill pode apresentar acionamento irrepreensível e resultado insatisfatório, ou a situação inversa. Convém registrar, ademais, que a eficácia de uma Skill depende do modelo subjacente, razão pela qual se recomenda a verificação em todos os modelos que se pretenda utilizar.

No que concerne a Skills de procedência externa, a documentação da Anthropic orienta o emprego exclusivo de material proveniente de fontes confiáveis, alertando para os riscos de uso indevido de ferramentas, exposição de dados e comprometimento por dependências externas. Pesquisas acadêmicas recentes — que devem ser interpretadas como levantamentos sobre ecossistemas públicos, e não como avaliação do repositório oficial — oferecem a dimensão do problema: estudo de janeiro de 2026, ao analisar trinta e um mil Skills coletadas em dois mercados, identificou padrão de vulnerabilidade em 26,1% delas, com incidência superior naquelas que incorporam scripts executáveis; publicação preliminar de agosto de 2026, ao examinar cento e trinta e oito mil arquivos `SKILL.md` públicos, identificou ao menos um defeito detectável em 91,8% deles, predominando problemas de qualidade de redação e organização sobre ameaças deliberadas.

Impõe-se, quanto à auditoria, uma delimitação honesta de competência. Ao docente sem formação técnica compete verificar a coerência entre a descrição declarada e o procedimento efetivamente descrito — critério acessível e revelador, porquanto uma Skill que executa operação não anunciada em sua descrição apresenta sinal de alerta independentemente da intenção subjacente. Compete-lhe, igualmente, verificar a ausência de menção a credenciais e a rastreabilidade da procedência. Verificando-se, contudo, a existência de pasta de scripts executáveis, de acesso a endereços externos ou de instruções que não compreenda, recomenda-se abster-se da instalação sem assessoria técnica. O reconhecimento do próprio limite constitui, nesta matéria, competência e não deficiência.

### Exercício Prático (10 minutos)

**Procedimento.**

1. Redigir quatro critérios de êxito para a Skill elaborada, em formulação verificável. Registre-se que formulações como "adequadamente redigido" não satisfazem o requisito de verificabilidade, ao passo que "extensão máxima de uma página, iniciando pelos aspectos positivos" o satisfaz.
2. Executar a tarefa em interação nova, com a Skill desativada, e registrar o resultado.
3. Avaliar esse resultado contra os quatro critérios, consignando o número de critérios atendidos.
4. Executar a mesma tarefa em interação nova, com a Skill ativa, e avaliar contra os mesmos critérios.
5. Para cada critério não atendido na segunda execução, identificar o módulo do curso que trata da correção pertinente.

**Critério de êxito:** o participante apresenta dois valores numéricos e demonstra que o segundo supera o primeiro. Considera-se o critério plenamente atendido quando, adicionalmente, cada critério não satisfeito encontra-se associado a um módulo de referência para correção.

---
---

# Módulo 5 — Síntese e Aplicação Integrada

> Pressupõe integralmente os Módulos 1 a 4. Não introduz conteúdo novo: articula as quatro competências desenvolvidas em atividade de aplicação a caso real do participante.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Articular as competências de elaboração, refinamento e verificação em um percurso completo de produção.
2. Fundamentar cada decisão de escrita mediante o princípio que a justifica.
3. Avaliar o próprio trabalho segundo critérios objetivos e identificar as correções pendentes.

### Texto Descritivo

O percurso desenvolvido nos quatro módulos anteriores estruturou-se segundo uma progressão que convém explicitar. Estabeleceu-se, primeiramente, que a informação é carregada em níveis e que o espaço de processamento é finito — do que decorre a concisão como requisito. Traduziu-se, em seguida, esse fundamento em procedimento de elaboração, no qual as regras de validação e os requisitos de gravação constituem condições de existência do artefato. Introduziram-se, posteriormente, os critérios que distinguem eficácia de mera existência: a precisão do acionamento, a economia do procedimento e a arquitetura dos arquivos de apoio. Instituíram-se, por fim, os procedimentos de verificação, sem os quais qualquer afirmação sobre a qualidade do trabalho permanece no domínio da impressão.

Observa-se que o eixo comum aos quatro módulos é a substituição do juízo impressivo pelo juízo fundamentado. A concisão não se justifica por elegância, mas por custo de contexto mensurável. A descrição não se avalia por correção gramatical, mas por taxa de acionamento verificada. A Skill não se considera boa por parecer boa, mas por atender a critérios estabelecidos previamente. Trata-se, cumpre notar, do mesmo rigor metodológico que o participante já aplica em sua área de investigação; a novidade reside na sua aplicação a um instrumento de trabalho.

A atividade integradora que se segue não introduz operação nova. Requer que o participante percorra o ciclo completo — elaborar, refinar, verificar e documentar — sobre uma tarefa efetivamente relevante de sua rotina, produzindo ao final um artefato que não constitui exercício, mas instrumento de trabalho.

### Exercício Prático — Atividade Integradora (10 minutos)

**Procedimento.**

1. Selecionar, dentre as tarefas recorrentes da própria rotina acadêmica, aquela cuja padronização produza maior benefício, aplicando os critérios de triagem: recorrência, existência de forma correta estabelecida e unidade de responsabilidade.
2. Revisar integralmente a Skill elaborada ao longo do curso, verificando: descrição contemplando as duas dimensões requeridas; corpo redigido em instruções iniciadas por verbo no imperativo, sem conteúdo que o modelo já domine; documento institucional próprio incorporado e referenciado com indicação expressa de seu conteúdo; instruções de baixa margem interpretativa nos pontos que não admitam variação.
3. Substituir a versão e verificar objetivamente a efetivação da substituição.
4. Executar a verificação de acionamento com cinco solicitações e a verificação de qualidade contra os quatro critérios estabelecidos.
5. Consignar, ao final do `SKILL.md`, a data da revisão.
6. Registrar, em uma frase, a circunstância em que um colega deveria empregar a Skill.

**Tabela de Critérios de Avaliação**

| Critério | Atendido? |
|---|---|
| A Skill possui nome em conformidade com as regras de validação do campo `name` | |
| A descrição contempla a ação executada e a circunstância de emprego | |
| A descrição declara expressamente ao menos uma hipótese de não aplicabilidade | |
| O corpo do procedimento não contém conteúdo que o modelo já domine | |
| Cada passo do procedimento inicia-se por verbo no imperativo | |
| Há ao menos um arquivo de apoio referenciado diretamente pelo `SKILL.md` | |
| Documento institucional próprio foi incorporado e é efetivamente utilizado na resposta | |
| Nenhum dado pessoal de estudante foi incorporado a qualquer arquivo | |
| O acionamento verifica-se em três formulações de registro distinto | |
| O acionamento não se verifica nas duas solicitações que não o deveriam produzir | |
| Os quatro critérios de êxito foram estabelecidos previamente à observação | |
| O número de critérios atendidos com a Skill supera o da linha de base | |
| A data da revisão consta do `SKILL.md` | |
| A circunstância de emprego é enunciável em uma frase | |

**Critério de êxito:** consideram-se satisfatoriamente cumpridos os objetivos do curso quando ao menos onze dos catorze critérios encontram-se atendidos, incluindo-se necessariamente entre eles os relativos à verificação por linha de base e à ausência de dados pessoais.

---
---

# Encerramento

Cumpriu-se a finalidade estabelecida no Objetivo Geral. O participante que percorreu integralmente os cinco módulos dispõe de ao menos uma Skill funcional, aplicada a tarefa real de sua rotina, cuja eficácia foi aferida por comparação com linha de base registrada previamente à intervenção. Mais relevante que o artefato produzido, contudo, é o método incorporado: a substituição da avaliação impressiva pela avaliação fundamentada em critérios estabelecidos de antemão. Recomenda-se, todavia, registrar que a competência aqui desenvolvida consolida-se pela prática regular. A segunda Skill demanda fração do tempo exigido pela primeira, porquanto a dificuldade inicial reside na compreensão da lógica subjacente, e não na operação da ferramenta. Convém, por essa razão, que o participante elabore ao menos mais duas Skills nas semanas subsequentes ao curso, dando preferência às tarefas submetidas a formato institucional obrigatório — aquelas que, por definição, nenhum modelo poderia inferir.

Quanto ao aprofundamento, três caminhos apresentam-se pertinentes. O primeiro consiste no exame do repositório público mantido pela Anthropic, no qual Skills reais podem ser analisadas em sua estrutura completa, constituindo material de estudo superior a qualquer descrição conceitual. O segundo consiste na exploração da Skill oficial `skill-creator`, destinada a auxiliar a elaboração, a avaliação e o refinamento de outras Skills. O terceiro, pertinente apenas a participantes cujas atividades envolvam manipulação de arquivos e execução de comandos, consiste no exame do ambiente Claude Code, no qual as Skills admitem recursos adicionais — cumprindo advertir que tais recursos não operam na superfície utilizada neste curso e que sua inclusão indevida acarreta falha de envio. Registre-se, por fim, que o ecossistema em questão encontra-se em transformação acelerada: denominações de menu, planos e limites técnicos alteram-se com frequência, razão pela qual se recomenda a revalidação periódica dos procedimentos aqui descritos. Os princípios permanecem; os rótulos deslocam-se.

> **Síntese:** uma Agent Skill constitui unidade modular e reutilizável de conhecimento procedural, destinada a ensinar a um assistente a execução consistente de uma categoria de tarefas. Sua eficácia não decorre da sofisticação técnica, mas de três atributos verificáveis — a precisão da descrição que determina o acionamento, a economia do procedimento que respeita o custo de contexto, e a existência de evidência que substitua a impressão pelo dado. No contexto docente, as Skills de maior valor duradouro são precisamente aquelas que codificam procedimentos institucionais específicos, dado que nenhum modelo, por mais capaz, inferirá as normas que somente o próprio docente conhece.
