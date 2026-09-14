# Plano de Aula — Claude Chat (Essentials)

---

## Identificação

| Campo | Definição |
|---|---|
| Curso | Claude Chat — Essentials |
| Natureza | Curto, introdutório e prático |
| Carga horária | 100 minutos (aproximadamente 1h40) |
| Público-alvo | Profissionais que utilizam o Claude em seu trabalho cotidiano — docentes, gestores de projeto, especialistas em conteúdo e designers instrucionais —, sem experiência prévia com os recursos de continuidade da ferramenta |
| Pré-requisitos | Conta ativa no Claude (claude.ai ou aplicativo Desktop). Alguns dos recursos abordados, em especial Memory e Projects, podem estar sujeitos ao plano contratado; recomenda-se confirmar a disponibilidade de cada recurso nas configurações da própria conta antes do curso. Nenhum conhecimento prévio em inteligência artificial é exigido |
| Recursos necessários | Computador ou dispositivo com acesso à internet e ao Claude; recomenda-se dispor de um histórico com ao menos algumas conversas anteriores na conta, de modo a tornar os exercícios de busca mais realistas |

---

### Objetivo Geral

O presente curso tem por finalidade capacitar o participante a compreender e a aplicar, de forma autônoma, os quatro mecanismos de continuidade disponíveis no Claude — Custom Instructions, Chat Search, Memory e Projects —, transformando um uso fragmentado da ferramenta, marcado pela repetição constante de contexto, em um uso sistemático, no qual cada nova conversa se apoia no trabalho já realizado. Ao término do curso, espera-se que o participante seja capaz de redigir um perfil permanente de si mesmo, localizar conversas anteriores por meio de busca eficaz, avaliar criticamente o que deve alimentar a memória automática da ferramenta e isolar frentes de trabalho distintas em Projects próprios.

---

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Diferenciar os quatro mecanismos de continuidade do Claude — Custom Instructions, Chat Search, Memory e Projects — reconhecendo o papel específico e as limitações de cada um.
2. Redigir Custom Instructions específicas e estáveis, capazes de reduzir a repetição de contexto ao longo de conversas distintas.
3. Localizar conversas anteriores por meio de buscas semânticas eficazes, aplicando padrões de refinamento progressivo.
4. Avaliar o que deve ou não ser fornecido à Memory automática do Claude, resguardando dados sensíveis de terceiros.
5. Estruturar um Project com instruções específicas, isolando o contexto de diferentes frentes de trabalho.

---

### Estrutura e Sequência dos Módulos

Os módulos foram organizados em progressão cumulativa: o módulo inicial estabelece o vocabulário comum aos demais, os quatro módulos seguintes aprofundam, cada um, um mecanismo de continuidade, e o módulo final articula os quatro em um único fluxo de trabalho.

| Módulo | Título | Referência (material-fonte) | Tempo |
|---|---|---|---|
| 1 | Fundamentos: Por Que a Continuidade Não é Automática | curso_claude_chat.md — Módulo 1 | 10 min |
| 2 | Custom Instructions: Ensinando o Claude a Reconhecer Você | curso_claude_chat.md — Módulo 2 | 18 min |
| 3 | Chat Search: Recuperando Conversas Anteriores | curso_claude_chat.md — Módulo 3 | 18 min |
| 4 | Memory: A Memória Automática do Claude | curso_claude_chat.md — Módulo 4 | 18 min |
| 5 | Projects: Isolando o Contexto por Frente de Trabalho | curso_claude_chat.md — Módulo 6 | 18 min |
| 6 | Síntese e Aplicação Integrada | curso_claude_chat.md — Módulos 1 a 6 | 18 min |

---

# Módulo 1 — Fundamentos: Por Que a Continuidade Não é Automática

> Módulo de abertura: nenhum conhecimento prévio é pressuposto; estabelece o vocabulário e o mapa dos quatro mecanismos retomados nos módulos subsequentes.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Explicar por que o Claude não retém, por padrão, informações de uma conversa para a seguinte.
2. Enumerar os quatro mecanismos disponíveis para criar continuidade — Custom Instructions, Chat Search, Memory e Projects — e a natureza de cada um (permanente, manual, automática ou isolada).
3. Diferenciar a memória humana da "memória" artificial do Claude, evitando expectativas equivocadas quanto ao seu funcionamento.
4. Localizar, nas configurações da própria conta, onde cada um dos quatro mecanismos é gerenciado.

### Texto Descritivo

Um modelo de linguagem como o Claude não possui, por padrão, memória intrínseca entre conversas distintas: cada novo chat constitui uma instância isolada, sem acesso automático a interações anteriores. Esse comportamento decorre da própria arquitetura da ferramenta, e não de uma limitação acidental — cumpre, portanto, compreendê-lo como ponto de partida, e não como uma falha a ser contornada.

Não obstante essa ausência de memória intrínseca, quatro mecanismos permitem, cada um a seu modo, a criação de continuidade entre conversas. As Custom Instructions constituem um perfil permanente, redigido uma única vez e carregado em todas as conversas subsequentes. O Chat Search permite localizar, mediante busca ativa do participante, conversas anteriores específicas. A Memory opera de forma automática: o Claude infere padrões a partir das conversas realizadas e os disponibiliza em interações futuras, com uma defasagem de atualização da ordem de vinte e quatro a quarenta e oito horas. Os Projects, por fim, isolam o contexto de uma frente de trabalho específica, com histórico e instruções próprios, sem que haja mistura com outras frentes.

Convém não confundir a memória humana com a memória do Claude. A memória humana é contínua, automática e baseada em experiência vivida; a do Claude, por sua vez, resulta inteiramente de dados textuais fornecidos pelo próprio participante ou registrados em conversas salvas, e sua atualização segue ritmo próprio, não instantâneo. Uma analogia pertinente é a de um colega que, a cada novo encontro, lê um resumo executivo a respeito do interlocutor, em vez de alguém que tenha vivenciado o histórico de trabalho em conjunto. Essa distinção orienta a forma como as instruções e o contexto devem ser redigidos ao longo de todo o curso: de modo explícito, específico e não dependente de experiência tácita.

Decorre do exposto que a continuidade, no trabalho com o Claude, constitui uma escolha ativa do usuário, e não um comportamento padrão da ferramenta. Os módulos subsequentes aprofundam, cada um, um dos quatro mecanismos apresentados, na ordem: Custom Instructions, Chat Search, Memory e Projects, culminando em um módulo de síntese que articula os quatro em um único sistema de trabalho.

### Exercício Prático

**Reconhecimento dos Quatro Mecanismos (10 min)**

1. Acessar as configurações da conta Claude (ícone de perfil, no canto superior direito da tela).
2. Localizar a seção em que as Custom Instructions são redigidas e registrar, em uma frase, se já existe algum conteúdo preenchido.
3. Localizar a opção de ativação da Memory e registrar se está ativa ou inativa.
4. Localizar a opção de ativação do Chat Search e registrar se está ativa ou inativa.
5. Localizar a área de Projects e registrar quantos Projects, se algum, já existem na conta.
6. Para cada um dos quatro mecanismos localizados, classificar, com base no texto descritivo, se sua natureza é permanente, manual, automática ou isolada.

**Critério de êxito:** o participante localiza corretamente os quatro mecanismos nas configurações da própria conta e classifica cada um deles quanto à sua natureza (permanente, manual, automática ou isolada), sem inversões.

---

# Módulo 2 — Custom Instructions: Ensinando o Claude a Reconhecer Você

> Módulo subsequente ao reconhecimento dos quatro mecanismos (Módulo 1); aprofunda o primeiro deles — o único de natureza inteiramente permanente e estática.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Localizar e acessar as Custom Instructions nas configurações do Claude.
2. Distinguir os dois campos que compõem as Custom Instructions e a função específica de cada um.
3. Redigir um perfil próprio no campo relativo ao participante, com contexto específico e verificável, em vez de formulações genéricas.
4. Redigir preferências de resposta no segundo campo, estabelecendo critérios objetivos para casos de ambiguidade.

### Texto Descritivo

As Custom Instructions constituem o mecanismo de continuidade mais estável entre os quatro estudados neste curso: uma vez redigidas, permanecem carregadas em todas as conversas subsequentes, sem sofrer o intervalo de atualização próprio da Memory nem depender de uma busca ativa, como ocorre no Chat Search. Compõem-se de dois campos distintos, disponíveis nas configurações da conta: um destinado a informações sobre o próprio participante — cargo, público atendido, objetivos e restrições de trabalho —, e outro destinado às preferências quanto à forma da resposta — tom, extensão, estrutura e critérios a adotar diante de ambiguidade.

O primeiro campo funciona como um contexto operacional, e não como um currículo: cumpre registrar, de forma sucinta, a profissão ou função exercida, o público afetado pelo trabalho realizado, os objetivos principais — recomenda-se um número reduzido, da ordem de três — e eventuais restrições relevantes, como limitações de tempo, orçamento ou exigências de conformidade institucional. Formulações genéricas, tais como "sou um profissional que trabalha com IA", pouco contribuem para a qualidade das respostas subsequentes; formulações específicas, que mencionem o público exato e o tipo de produto habitualmente elaborado, produzem resultados sensivelmente mais adequados.

O segundo campo define o formato e o tom esperados das respostas, sendo particularmente útil para resolver ambiguidades que, de outro modo, exigiriam esclarecimento a cada nova conversa: se a resposta deve ser breve ou detalhada, estruturada em listas ou em prosa, e qual o registro de linguagem — técnico, pedagógico ou institucional — mais adequado ao contexto de trabalho do participante. A ausência desse campo tende a gerar respostas de tom genérico, que exigem ajuste manual repetido.

Cumpre registrar, por fim, que as Custom Instructions não constituem um documento estático e definitivo: a experiência de uso ao longo de semanas revela lacunas — informações que o Claude interpretou de forma inadequada, ou estilos que se mostraram mais eficazes do que outros —, e a revisão periódica, com intervalo da ordem de duas a quatro semanas, constitui prática recomendada para manter o perfil atualizado.

### Exercício Prático

**Redação das Custom Instructions Próprias (18 min)**

1. Acessar as configurações da conta e localizar o campo destinado a informações sobre o participante.
2. Redigir, nesse campo, cargo ou função, público atendido, até três objetivos principais e eventuais restrições de trabalho.
3. Acessar o campo destinado às preferências de resposta.
4. Redigir, nesse campo, o tom de linguagem desejado, o formato preferido (listas, prosa ou tabelas) e ao menos um critério explícito para casos de ambiguidade.
5. Salvar as instruções registradas.
6. Abrir uma nova conversa e formular uma pergunta simples, relacionada à própria área de atuação, sem fornecer contexto adicional.
7. Avaliar se a resposta obtida já reflete o perfil e as preferências registrados, sem necessidade de repeti-los.

**Critério de êxito:** a resposta obtida no passo 7 reflete, de forma identificável, ao menos duas das informações registradas nas Custom Instructions — por exemplo, o público mencionado ou o formato solicitado —, sem que o participante as tenha repetido na pergunta.

---

# Módulo 3 — Chat Search: Recuperando Conversas Anteriores

> Módulo subsequente às Custom Instructions (Módulo 2); desloca o foco do perfil permanente para a recuperação ativa de conversas específicas já realizadas.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Ativar o Chat Search nas configurações da conta.
2. Diferenciar busca semântica de busca literal, reconhecendo as implicações dessa diferença para a formulação de consultas.
3. Aplicar padrões de busca eficazes, refinando consultas amplas até resultados específicos.
4. Selecionar, diante de uma conversa localizada, entre continuar nela diretamente ou transferir o contexto relevante para uma nova conversa.

### Texto Descritivo

O Chat Search constitui o mecanismo destinado à localização de conversas anteriores sem que seja necessário percorrer manualmente o histórico da conta. Trata-se, em muitas contas, de um recurso não ativado por padrão, cuja habilitação ocorre nas configurações, na seção usualmente identificada como "Features" ou "Recursos Experimentais".

Cumpre observar que o Chat Search realiza busca semântica, e não busca literal: ao contrário de uma busca por correspondência exata de palavras, o mecanismo localiza conversas relacionadas ao tema ou à intenção descrita na consulta, ainda que os termos exatos não constem no texto original. Uma consulta como "linguagem de programação para análise de dados", por exemplo, tende a recuperar conversas sobre Python, R ou bibliotecas de ciência de dados, mesmo que nenhuma delas mencione literalmente a expressão utilizada na busca.

A eficácia de uma busca depende, em grande medida, de sua formulação. Consultas amplas — referentes, por exemplo, a um tema genérico — tendem a retornar um número elevado de resultados, de utilidade limitada; recomenda-se, nesse caso, o refinamento progressivo da consulta, incorporando elementos mais específicos, como o tipo de produto elaborado, uma decisão tomada durante a conversa ou uma referência temporal aproximada, até que o número de resultados se reduza a poucas conversas efetivamente pertinentes.

Uma vez localizada a conversa desejada, cabe ao participante decidir entre dois caminhos: prosseguir diretamente na conversa antiga, o que preserva a totalidade do contexto já acumulado, ainda que estenda uma conversa já longa; ou extrair os pontos relevantes e iniciar uma nova conversa, o que favorece a organização, ao custo de exigir transcrição manual do contexto pertinente. Quando a busca não retorna resultados satisfatórios — o que tende a ocorrer com conversas muito antigas ou com consultas vagas —, recomenda-se experimentar sinônimos, incluir uma referência temporal ou, alternativamente, solicitar diretamente ao Claude que reconstrua o contexto a partir de uma descrição fornecida pelo próprio participante.

### Exercício Prático

**Busca Refinada de uma Conversa Anterior (18 min)**

1. Acessar as configurações da conta e, caso o Chat Search não esteja ativo, habilitá-lo.
2. Formular uma primeira consulta ampla, referente a um tema geral já discutido anteriormente com o Claude.
3. Observar o número de resultados retornados.
4. Refinar a consulta, incorporando um elemento mais específico — um tipo de produto, uma decisão tomada ou uma referência temporal aproximada.
5. Repetir o refinamento, se necessário, até obter entre uma e três conversas claramente pertinentes.
6. Abrir a conversa mais relevante dentre os resultados obtidos.
7. Decidir, com base no critério apresentado no texto descritivo, se a continuidade deve ocorrer diretamente naquela conversa ou por meio de uma nova conversa com contexto transcrito, registrando a decisão e sua justificativa em uma frase.

**Critério de êxito:** o participante reduz uma consulta inicial ampla a um resultado específico e pertinente em, no máximo, três rodadas de refinamento, e justifica de forma coerente a escolha entre continuar na conversa antiga ou transferir o contexto para uma nova.

---

# Módulo 4 — Memory: A Memória Automática do Claude

> Módulo subsequente ao Chat Search (Módulo 3); desloca o foco da busca ativa para o mecanismo automático de retenção de contexto.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Diferenciar a Memory das Custom Instructions quanto à natureza — automática e inferida, em vez de permanente e redigida diretamente.
2. Ativar a Memory nas configurações da conta e verificar o que já foi registrado a seu respeito.
3. Selecionar o tipo de informação apropriado para constar na Memory, resguardando dados sensíveis de terceiros.
4. Revisar e corrigir, mediante instrução direta, um conteúdo desatualizado ou incorreto registrado na Memory.

### Texto Descritivo

A Memory distingue-se das Custom Instructions por sua natureza automática: em vez de um perfil redigido diretamente pelo participante, a Memory resulta da observação, pelo próprio Claude, das conversas realizadas ao longo do tempo, das quais são inferidos padrões — cargo, público atendido, preferências recorrentes — posteriormente disponibilizados em conversas futuras. Essa atualização, todavia, não ocorre em tempo real: observa-se uma defasagem da ordem de vinte e quatro a quarenta e oito horas entre a conversa em que uma informação surge e o momento em que ela passa a integrar a Memory.

Embora o conteúdo da Memory resulte primariamente de inferência, o participante pode influenciá-lo de forma direta, mediante instrução explícita — por exemplo, "lembre que eu trabalho com…". Recomenda-se reservar a esse mecanismo informações de caráter genérico e estável, tais como cargo, público atendido, objetivos de trabalho e preferências de estilo, evitando-se, em contrapartida, o registro de dados sensíveis de terceiros: nomes completos de indivíduos identificáveis, sobretudo menores de idade, informações de saúde, dados financeiros ou credenciais de acesso. Quando a informação envolver terceiros, recomenda-se sua generalização — por exemplo, referir-se a uma turma heterogênea, com alunos de diferentes ritmos de aprendizagem, em vez de nomear indivíduos e suas condições específicas.

A responsabilidade pelo conteúdo compartilhado com o Claude, inclusive aquele que alimenta a Memory, recai sobre o próprio participante, e não sobre a ferramenta: legislações de proteção de dados pessoais, como a Lei Geral de Proteção de Dados, aplicam-se à informação fornecida a serviços de terceiros, o que reforça a necessidade de critério na seleção do que é compartilhado.

Por fim, a Memory admite revisão e correção. Recomenda-se, com periodicidade da ordem de duas a quatro semanas, solicitar ao Claude uma síntese do que foi registrado a respeito do participante, verificando a atualidade de cada item e corrigindo, mediante instrução direta, qualquer informação desatualizada ou equivocada — mudança de cargo, por exemplo, ou alteração relevante no público atendido.

### Exercício Prático

**Ativação, Contribuição e Auditoria da Memory (18 min)**

1. Acessar as configurações da conta e, caso a Memory não esteja ativa, habilitá-la.
2. Registrar, em uma nova conversa, uma instrução explícita do tipo "lembre que eu…", contendo de duas a três informações genéricas e seguras a respeito do próprio trabalho (cargo, público atendido ou preferências), sem menção a terceiros identificáveis.
3. Solicitar ao Claude, na mesma ou em nova conversa, uma síntese do que foi registrado a seu respeito, utilizando uma pergunta do tipo "o que você sabe sobre mim até agora?".
4. Registrar a resposta obtida e compará-la às informações fornecidas no passo 2.
5. Caso alguma informação relevante ainda não conste da síntese, anotar que a atualização integral pode ocorrer somente após o intervalo de vinte e quatro a quarenta e oito horas mencionado no texto descritivo.

**Critério de êxito:** o participante fornece ao menos duas informações genéricas e adequadamente resguardadas, sem dados sensíveis de terceiros, e executa corretamente o procedimento de auditoria, ainda que o reflexo integral na Memory dependa do intervalo de atualização próprio do mecanismo.

---

# Módulo 5 — Projects: Isolando o Contexto por Frente de Trabalho

> Módulo subsequente à Memory (Módulo 4); desloca o foco de mecanismos globais — válidos em toda a conta — para um mecanismo de escopo isolado, restrito a uma frente de trabalho específica.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Justificar a razão pela qual frentes de trabalho distintas se beneficiam de contextos isolados, em vez de um único contexto global.
2. Criar um Project, preenchendo nome e descrição de forma que reflitam o resultado esperado.
3. Redigir Instruções de Projeto específicas para aquela frente de trabalho, distintas das Custom Instructions globais.
4. Decidir, diante de uma nova tarefa, se ela deve ser conduzida no contexto global (Custom Instructions e Memory) ou em um Project isolado.

### Texto Descritivo

Um Project constitui um contexto isolado dentro da conta do Claude, dotado de histórico de conversas e instruções próprios, sem interferência de outras frentes de trabalho. Distingue-se, assim, das Custom Instructions e da Memory, ambas de escopo global — válidas em todas as conversas da conta —, ao restringir-se a uma finalidade específica: por exemplo, um currículo em elaboração, uma consultoria em andamento ou uma linha de pesquisa determinada.

A justificativa para o uso de um Project reside na prevenção de mistura de contexto: um participante que conduza, simultaneamente, frentes de trabalho distintas — um projeto educacional e uma consultoria, por exemplo — corre o risco de que o Claude confunda público-alvo, tom ou decisões já tomadas, caso todo o histórico permaneça em um único espaço global. Cada Project mantido separadamente evita esse risco, funcionando como um "Claude" próprio para cada finalidade.

A criação de um Project requer o preenchimento de um nome, que deve identificar o resultado esperado — e não o processo —, e de uma descrição breve, que explicite a finalidade e o público envolvidos. As Instruções de Projeto, por sua vez, cumprem função análoga à das Custom Instructions, porém restrita àquele contexto específico: convém que reiterem, quando pertinente, o papel do participante naquela frente de trabalho, o público-alvo específico, os objetivos daquele Project em particular e eventuais restrições ou preferências que não se apliquem às demais conversas da conta.

A decisão entre conduzir uma tarefa no contexto global ou em um Project isolado depende, primordialmente, da natureza da tarefa: recomenda-se o contexto global para solicitações pontuais, que se esgotam em uma única troca e não exigem retomada futura; recomenda-se, em contrapartida, um Project para tarefas que se estendem por múltiplas sessões, que resultam em documentos reutilizáveis ou que exigem regras de comportamento distintas das demais conversas da conta.

### Exercício Prático

**Criação de um Project com Instruções Específicas (18 min)**

1. Acessar a área de Projects da conta e selecionar a opção de criação de um novo Project.
2. Preencher o campo "Nome" com um título que identifique o resultado esperado de uma frente de trabalho real ou hipotética do participante.
3. Preencher o campo "Descrição" com uma frase que explicite a finalidade e o público envolvidos.
4. Acessar a seção de instruções do Project e redigir, especificamente para essa frente de trabalho, o papel do participante, o público-alvo e ao menos uma restrição ou preferência que não conste nas Custom Instructions globais já redigidas no Módulo 2.
5. Salvar as instruções e iniciar uma conversa dentro do Project, formulando uma pergunta relacionada à finalidade declarada.
6. Comparar a resposta obtida à que seria esperada em uma conversa comum, fora do Project, identificando ao menos uma diferença atribuível às Instruções de Projeto.

**Critério de êxito:** o Project é criado com nome, descrição e instruções específicas preenchidos, e o participante identifica corretamente ao menos uma diferença entre a resposta obtida dentro do Project e o que se esperaria de uma conversa comum sem esse contexto.

---

# Módulo 6 — Síntese e Aplicação Integrada

> Módulo de encerramento: integra os quatro mecanismos tratados nos Módulos 2 a 5 — Custom Instructions, Chat Search, Memory e Projects — em um único fluxo de trabalho contínuo.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Articular, em um único fluxo de trabalho, os quatro mecanismos de continuidade estudados ao longo do curso.
2. Aplicar o fluxo integrado a um cenário concreto de retomada de trabalho anterior.
3. Avaliar criticamente o resultado obtido a partir de critérios objetivos.

### Texto Descritivo

Os quatro mecanismos tratados nos módulos anteriores não constituem alternativas concorrentes, mas camadas complementares de um mesmo sistema de continuidade. As Custom Instructions estabelecem a identidade permanente do participante, válida em qualquer conversa; a Memory reforça, de forma automática e gradual, padrões observados ao longo do tempo; o Chat Search permite a recuperação ativa de conversas específicas quando a informação necessária não está disponível de outra forma; e os Projects isolam frentes de trabalho que exigem contexto próprio, sem interferência mútua. A escolha, em uma situação concreta, não é entre esses mecanismos, mas a combinação apropriada entre eles.

Um fluxo típico de retomada de trabalho começa pela identificação da natureza da tarefa: caso se trate de continuação de uma frente já isolada em um Project, o participante retorna diretamente a ele, valendo-se do histórico e das instruções ali registrados; caso a informação relevante esteja dispersa em conversas globais anteriores, recorre-se ao Chat Search para localizá-la, decidindo-se, em seguida, entre prosseguir na conversa recuperada ou transportar o contexto para uma nova interação. Em qualquer caso, as Custom Instructions e a Memory operam de forma subjacente, reduzindo a necessidade de reexplicar informações estáveis a respeito do próprio participante.

Cumpre reiterar, como princípio transversal a todo o sistema, que a responsabilidade pela qualidade e pela adequação do conteúdo produzido permanece do participante: o Claude executa a partir do contexto e das instruções fornecidas, mas cabe ao usuário revisar cada resultado antes de sua utilização efetiva, bem como exercer critério quanto ao que é registrado em Memory ou em Instruções de Projeto, conforme já discutido no Módulo 4. Esse princípio de supervisão ativa constitui o critério final de qualidade de todo o sistema de continuidade apresentado.

A prática continuada dos quatro mecanismos, e não a leitura isolada deste curso, é o que consolida a transição de um uso fragmentado do Claude para um uso sistemático, no qual cada nova conversa se apoia no trabalho já realizado. A trilha prática ("Hands-on") que complementa este curso introdutório aprofunda cada um dos quatro mecanismos por meio de oficinas orientadas à produção de resultados concretos.

### Exercício Prático — Atividade Integradora

**Retomando um Trabalho Anterior: Aplicação dos Quatro Mecanismos (18 min)**

1. Selecionar um tema ou projeto, real ou hipotético, discutido com o Claude há pelo menos algumas semanas — ou, na ausência de histórico suficiente, simular esse cenário.
2. Utilizar o Chat Search (Módulo 3) para localizar a conversa correspondente, aplicando o refinamento progressivo estudado.
3. Decidir, com base na natureza da tarefa, se a retomada deve ocorrer na conversa localizada, em uma nova conversa global (apoiada pelas Custom Instructions redigidas no Módulo 2) ou dentro do Project criado no Módulo 5.
4. Formular a solicitação de continuidade, verificando se a resposta obtida reflete tanto o contexto recuperado quanto o perfil e as preferências já registrados.
5. Preencher a tabela de Critérios de avaliação a seguir.

| Critério | Atendido? |
|---|---|
| A conversa ou o contexto anterior foi localizado por meio de busca eficaz | |
| A resposta obtida reflete as Custom Instructions ou as Instruções de Projeto pertinentes | |
| Nenhum dado sensível de terceiros foi exposto ao longo do processo | |
| O participante seria capaz de repetir esse fluxo em uma situação real de trabalho | |

---

## Encerramento

O presente curso cumpriu a finalidade de introduzir o participante aos quatro mecanismos de continuidade disponíveis no Claude — Custom Instructions, Chat Search, Memory e Projects —, articulados como camadas complementares de um mesmo sistema de trabalho. Recomenda-se a prática regular desses mecanismos, de modo que a redação de instruções específicas e a revisão periódica do que é retido pela ferramenta se consolidem como hábito.

O aprofundamento de cada mecanismo — com exercícios adicionais de busca, redação de instruções e estruturação de Projects — é tratado na trilha prática que complementa este curso introdutório, na qual cada conceito é explorado por meio de oficinas orientadas à produção de resultados concretos.

> **Síntese:** a continuidade no trabalho com o Claude não é uma propriedade automática da ferramenta, mas o resultado de escolhas deliberadas sobre o que se registra, o que se busca e o que se isola em cada frente de trabalho.
