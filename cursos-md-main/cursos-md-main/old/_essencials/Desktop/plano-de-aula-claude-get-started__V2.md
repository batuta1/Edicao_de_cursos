<link rel="stylesheet" href="../../.css/style.css">

# (Plano de Aula) Claude: Comece a usar o aplicativo para desktop — Curso Essentials

*Claude: Get Started with the Desktop App — Curso Essentials*

---

## Identificação

| Campo | Definição |
|---|---|
| **Curso** | Claude: Comece a usar o aplicativo para desktop — Curso Essentials |
| **Natureza** | Autoinstrucional, assíncrono, integrante da trilha "Essentials" |
| **Carga horária** | 130 minutos (distribuídos em 6 módulos de conteúdo e 1 módulo de síntese) |
| **Público-alvo** | Docentes do ensino superior iniciantes em Inteligência Artificial; analistas administrativos; alunos do ensino superior sem experiência prévia com ferramentas de IA |
| **Pré-requisitos** | Nenhum conhecimento técnico em Inteligência Artificial ou programação; capacidade de navegar em sistema operacional Windows ou macOS (criar pastas, abrir arquivos, instalar programas) |
| **Recursos necessários** | Computador com sistema operacional Windows 10/11 ou macOS 12 ou superior; conta Anthropic com plano Pro, Max, Team ou Enterprise; conexão à internet; aplicativo Claude Desktop instalado (instruções fornecidas no Módulo 1) |

---

### Objetivo Geral

O presente curso visa proporcionar ao participante os fundamentos necessários para instalar, configurar e utilizar o aplicativo Claude Desktop de forma autônoma e segura. Ao concluir o curso, espera-se que o participante seja capaz de abrir um projeto no aplicativo, utilizar cada uma das três interfaces de trabalho disponíveis (Chat, Code e Cowork) com propriedade e consciência de seus limites, formular solicitações eficazes ao assistente e adotar práticas elementares de proteção de dados, transformando o Claude Desktop em recurso produtivo para suas atividades acadêmicas ou profissionais.

---

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Verificar a compatibilidade do sistema operacional e do plano de assinatura, instalar o Claude Desktop corretamente e realizar o primeiro acesso autenticado.
2. Distinguir as três interfaces do aplicativo — Chat, Code e Cowork — e selecionar a mais adequada a cada tipo de tarefa, conhecendo os limites e as boas práticas específicas de cada uma.
3. Utilizar a interface Chat para consultas conceituais, elaboração de textos e apoio a decisões, calibrando solicitações iterativamente para obter resultados progressivamente mais precisos.
4. Acionar a interface Cowork para delegação de tarefas autônomas, definindo o escopo da missão com clareza e avaliando criticamente o relatório de execução produzido pelo assistente.
5. Estruturar um projeto de trabalho com organização mínima de arquivos e configurar proteções básicas de dados sensíveis, incluindo o uso de `.gitignore`.
6. Redigir solicitações claras e contextualizadas ao assistente, revisar as alterações propostas por meio da visualização de diferenças (*diff view*) e acionar o controle de versão para registrar ou reverter mudanças.

---

### Estrutura e Sequência dos Módulos

Os módulos estão organizados em progressão cumulativa: cada um pressupõe os conhecimentos construídos no anterior e desloca gradualmente o foco da instalação e do ambiente para o uso produtivo e responsável do aplicativo. O participante que concluir os módulos na ordem proposta terá, ao final, uma visão integrada do fluxo de trabalho com o Claude Desktop.

| Módulo | Título | Referência | Tempo estimado |
|---|---|---|---|
| 1 | Verificação do ambiente e instalação do Claude Desktop | Módulos 0 e 2 do material-fonte | 20 min |
| 2 | As três interfaces de trabalho: Chat, Code e Cowork | Módulos 1 e 3 do material-fonte | 15 min |
| 3 | A interface Chat: consulta, elaboração e iteração | Módulos 1, 3 e 6 do material-fonte | 20 min |
| 4 | A interface Cowork: delegação autônoma de tarefas | Módulos 1 e 16 do material-fonte | 20 min |
| 5 | Organização de projetos e proteção de dados | Módulos 2B, 2C e 4 do material-fonte | 20 min |
| 6 | Formulação de solicitações e revisão de resultados | Módulos 5–8 do material-fonte (seções de prompts e diff view) | 20 min |
| 7 (Síntese) | Síntese e Aplicação Integrada | Todos os módulos anteriores | 15 min |

---

<div style="page-break-after: always;"></div>

# Módulo 1 — 🖥️ Verificação do Ambiente e Instalação do Claude Desktop

> *Este é o ponto de partida do curso. Antes de qualquer uso do aplicativo, é necessário confirmar que o ambiente de trabalho — sistema operacional, plano de assinatura e requisitos técnicos — está em conformidade com os pré-requisitos da ferramenta.*

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Identificar o sistema operacional e a arquitetura do processador do computador disponível e verificar se são compatíveis com o Claude Desktop.
2. Localizar e confirmar o plano de assinatura Anthropic ativo, distinguindo quais planos permitem o uso do aplicativo.
3. Baixar o instalador correto para o sistema identificado, executar a instalação e realizar o primeiro login no aplicativo.
4. Realizar a verificação pós-instalação por meio de uma lista de conferência (*checklist*), confirmando que as três interfaces principais estão acessíveis.

### Texto Descritivo

O Claude Desktop é a versão em formato de aplicativo instalável do assistente Claude, desenvolvido pela Anthropic. Diferentemente do acesso via navegador (disponível em claude.ai), a versão para desktop permite que o assistente leia e modifique diretamente arquivos armazenados no computador do usuário — característica que amplia significativamente o escopo de tarefas possíveis, mas que também exige atenção à compatibilidade e à segurança antes da instalação.

O primeiro passo consiste em identificar o sistema operacional e a arquitetura do processador. O Claude Desktop é compatível com Windows 10 e 11 (nas arquiteturas x64 e ARM64) e com macOS 12 ou superior (tanto em processadores Intel quanto em Apple Silicon, como as linhas M1, M2 e M3). Sistemas Linux não são suportados de forma nativa — usuários desse ambiente podem recorrer à interface de linha de comando (*CLI*) ou ao acesso via navegador. Para verificar essas informações no Windows, acessa-se *Configurações > Sistema > Sobre* e observa-se o campo "Tipo de sistema". No macOS, o caminho equivalente é o menu Apple (*⌘*) > *Sobre este Mac*, onde se localiza o campo "Chip" (para Apple Silicon) ou "Processador" (para Intel).

O segundo pré-requisito é o plano de assinatura Anthropic. O acesso ao Claude Desktop requer, no mínimo, o plano Pro. O plano gratuito (Free) não inclui esse recurso; ao tentar acessar a aba Code com esse plano, o aplicativo exibirá uma mensagem de atualização necessária (*Upgrade Required*). Para verificar o plano ativo, o participante deve acessar claude.ai, fazer login e localizar a seção de conta ou faturamento (*Billing*). Convém registrar que instituições de ensino superior podem dispor de acordos com a Anthropic que viabilizam o acesso para docentes e discentes; recomenda-se consultar a área de tecnologia da informação da instituição antes de adquirir individualmente um plano pago.

Confirmados os pré-requisitos, o participante deve acessar o site oficial da Anthropic, localizar a página de *download* do Claude Desktop e selecionar o instalador correspondente à arquitetura do processador identificada. O uso de um instalador incompatível — por exemplo, a versão x64 em um computador com processador ARM64 — é uma das causas mais frequentes de falha de inicialização do aplicativo, muitas vezes manifestada como ausência de resposta ao duplo clique no atalho.

> 📸 **Captura de Tela sugerida:** Tela de *Configurações > Sistema > Sobre* (Windows) ou *Sobre este Mac* (macOS) com o campo de arquitetura destacado — útil como registro de conferência antes da instalação.

Após concluir a instalação, o aplicativo solicitará autenticação com as credenciais da conta Anthropic. O processo envolve a abertura temporária do navegador padrão para verificação adicional de segurança; trata-se de comportamento esperado e não indica erro. Concluído o login, o participante terá acesso às três interfaces principais do aplicativo: Chat, Code e Cowork, cujas funções serão detalhadas no módulo seguinte.

---

### Exercício Prático

**Checklist de Verificação do Ambiente** *(estimativa: 10 minutos)*

Registre as respostas a cada item em um arquivo de texto simples ou em papel. Em seguida, compare os resultados com os critérios de êxito descritos abaixo.

1. Acesse as configurações do sistema operacional e anote: (a) nome e versão do sistema operacional; (b) arquitetura do processador (x64, ARM64, Intel ou Apple Silicon).
2. Acesse claude.ai, faça login e identifique o plano de assinatura ativo.
3. Com base nas informações anotadas, indique qual instalador do Claude Desktop deve ser baixado (ex.: *Windows x64*, *macOS Apple Silicon*).
4. Realize o *download*, a instalação e o primeiro login no aplicativo.
5. Abra o aplicativo e confirme a presença das abas Chat, Code e Cowork.

**Critério de êxito:** O participante deverá ser capaz de registrar, sem consulta adicional, o sistema operacional, a arquitetura do processador e o plano de assinatura corretos, e apresentar captura de tela do aplicativo aberto e autenticado com as três abas visíveis.

---

### Mão na massa

Após concluir a instalação, utilize o prompt a seguir na aba **Chat** do Claude Desktop, substituindo os campos entre colchetes por informações reais:

> *"Estou começando a usar o Claude Desktop. Meu sistema operacional é [Windows 11 / macOS 14] e meu principal interesse é [descreva sua área: docência, análise de dados, redação acadêmica, etc.]. Que tipos de tarefas você pode me ajudar a realizar neste aplicativo?"*

Observe a resposta e anote duas ou três possibilidades que pareçam relevantes para sua rotina.

---

<div style="page-break-after: always;"></div>

# Módulo 2 — 🗂️ As Três Interfaces de Trabalho: Chat, Code e Cowork

> *Com o aplicativo instalado e autenticado (Módulo 1), o foco desloca-se agora para a compreensão das três interfaces que organizam o Claude Desktop, determinando qual delas acionar para cada tipo de tarefa.*

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Descrever a finalidade de cada uma das três interfaces — Chat, Code e Cowork — e indicar exemplos concretos de uso para cada uma.
2. Diferenciar o Claude Desktop do acesso via navegador (claude.ai), enumerando ao menos três capacidades exclusivas da versão instalada.
3. Selecionar, diante de uma tarefa descrita, a interface mais adequada e justificar a escolha.
4. Reconhecer os limites da interface Cowork para iniciantes e identificar o momento oportuno para explorá-la.

### Texto Descritivo

O Claude Desktop organiza suas funções em três interfaces principais, apresentadas como abas na parte superior da janela do aplicativo. Compreender a diferença entre elas é fundamental para aproveitar o potencial da ferramenta sem desperdício de tempo.

A aba **Chat** reproduz a experiência já familiar do acesso via navegador: o participante digita uma pergunta ou solicitação e o assistente responde em texto. É o espaço indicado para consultas conceituais ("O que é um algoritmo?"), comparações entre opções, resumos de leitura e qualquer tarefa que não envolva a leitura ou modificação de arquivos armazenados no computador. Nessa interface, o Claude não acessa o sistema de arquivos local — toda informação processada é aquela explicitamente digitada ou colada pelo participante.

A aba **Code** representa o diferencial central do aplicativo em relação ao acesso via navegador. Nela, o participante seleciona uma pasta do computador — denominada "projeto" — e o assistente passa a ter acesso de leitura a todos os arquivos contidos nessa pasta. A partir desse ponto, é possível solicitar correções, melhorias, criação de novos arquivos e execução de comandos no terminal integrado, tudo sem a necessidade de copiar e colar manualmente o conteúdo dos arquivos. Todas as alterações propostas pelo assistente são apresentadas em uma visualização de diferenças (*diff view*) antes de serem aplicadas, permitindo que o participante as revise e aceite ou rejeite.

> 📸 **Captura de Tela sugerida:** A interface da aba Code com um projeto aberto no painel lateral (*sidebar*) à esquerda e a área de chat ao centro — ilustra visualmente a diferença entre as abas Chat e Code para o participante ainda não familiarizado com o layout.

A aba **Cowork** disponibiliza um modo de execução autônoma: o assistente realiza uma sequência de tarefas em segundo plano, sem necessidade de supervisão contínua pelo participante. Uma analogia formal seria a delegação de uma tarefa a um colaborador com autonomia para executá-la integralmente e entregar o resultado. Por envolver maior grau de automação e, consequentemente, maior risco de alterações não supervisionadas, essa interface é indicada para usuários com experiência prévia no aplicativo. Recomenda-se que iniciantes a explorem apenas após consolidar o uso das abas Chat e Code.

A distinção entre as três abas pode ser resumida da seguinte forma: Chat é o espaço de consulta e conversa; Code é o espaço de trabalho colaborativo sobre arquivos reais; Cowork é o espaço de delegação autônoma. A escolha errada da interface não compromete permanentemente o trabalho, mas pode gerar retrabalho — por exemplo, solicitar na aba Chat uma alteração em um arquivo que só pode ser efetuada na aba Code.

---

### Exercício Prático

**Múltipla Escolha: Identificação da Interface Adequada** *(estimativa: 5 minutos)*

Para cada situação abaixo, indique qual interface — Chat, Code ou Cowork — seria a mais adequada. Em seguida, confira o gabarito e leia a fundamentação.

1. Um docente deseja obter uma explicação sobre o conceito de inteligência artificial generativa para incluir em sua ementa.
2. Uma analista precisa que o assistente revise e corrija os termos técnicos em um relatório salvo em sua pasta de trabalho.
3. Um estudante quer saber a diferença entre citação direta e indireta segundo as normas da ABNT.
4. Uma coordenadora deseja que o assistente execute, de forma autônoma, a revisão de cinquenta arquivos de texto e gere um relatório consolidado ao final.

**Gabarito:**
1. Chat — não há arquivo a ser acessado; trata-se de consulta conceitual.
2. Code — o arquivo está armazenado localmente e precisa ser lido e modificado pelo assistente.
3. Chat — consulta conceitual sem necessidade de acesso a arquivos.
4. Cowork — tarefa longa, com múltiplos arquivos, adequada ao modo autônomo (recomendada apenas a usuários experientes).

**Fundamentação:** A escolha da interface correta reduz erros e retrabalho. A aba Code exige que o projeto esteja previamente configurado (tema do Módulo 3); a aba Cowork pressupõe familiaridade com os modos de permissão do aplicativo.

---

### Mão na massa

Na aba **Chat**, utilize o prompt abaixo, ajustando o tema ao seu interesse:

> *"Explique, de forma clara e sem jargões, o conceito de [insira um tema de sua área: ex. 'aprendizado de máquina', 'análise de dados qualitativos', 'gestão por processos']. Em seguida, liste três aplicações práticas desse conceito que poderiam ser úteis para [sua área de atuação]."*

Observe como o assistente estrutura a resposta e avalie se o nível de detalhamento atende às suas necessidades. Caso a resposta seja muito técnica ou muito superficial, experimente ajustar o prompt adicionando a instrução: *"Considere que o leitor não tem formação na área."* ou *"Aprofunde a explicação com exemplos acadêmicos."*

---

<div style="page-break-after: always;"></div>

# Módulo 3 — 💬 A Interface Chat: Consulta, Elaboração e Iteração

> *Com as três interfaces apresentadas em panorama (Módulo 2), este módulo aprofunda o uso da aba Chat — a interface de entrada mais imediata do Claude Desktop —, explorando suas possibilidades além da pergunta simples e desenvolvendo a capacidade de refinar solicitações iterativamente.*

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Identificar as categorias de tarefas mais adequadas à interface Chat — consultas conceituais, elaboração de textos, sínteses, comparações e apoio a decisões — e distingui-las das tarefas que exigem a aba Code.
2. Estruturar solicitações progressivamente mais precisas por meio de iteração: avaliar a resposta recebida, identificar o que faltou e reformular o pedido com informações adicionais.
3. Utilizar recursos de contextualização disponíveis na interface Chat, como o anexo de arquivos e a referência a documentos, para enriquecer o insumo fornecido ao assistente.
4. Reconhecer as limitações inerentes ao Chat — ausência de acesso ao sistema de arquivos local e ausência de memória entre sessões — e adotar estratégias para contorná-las.

### Texto Descritivo

A interface Chat é, funcionalmente, a porta de entrada mais acessível do Claude Desktop: não requer a abertura de um projeto, não pressupõe conhecimento de controle de versão e responde a qualquer solicitação digitada, da mais simples à mais elaborada. Precisamente por isso, corre-se o risco de subutilizá-la — restringindo seu uso a perguntas pontuais — ou de sobrecarregá-la com pedidos que só a aba Code pode atender de forma satisfatória.

O Chat é o espaço adequado para tarefas de natureza conversacional e intelectual que não dependam de arquivos armazenados localmente. Entre os casos de uso mais produtivos para o público-alvo deste curso, destacam-se: a elaboração e revisão de textos acadêmicos ou institucionais quando o conteúdo é fornecido diretamente na conversa; a síntese de documentos cujo texto é colado ou anexado à solicitação; a comparação entre conceitos, abordagens ou autores; o apoio à tomada de decisões por meio de análise de cenários; e a geração de estruturas iniciais — ementas, roteiros, checklists, esboços de relatório — que o participante refinará posteriormente.

Um aspecto frequentemente negligenciado por usuários iniciantes é a natureza iterativa do Chat. A primeira resposta raramente é a ideal; trata-se de um ponto de partida. O participante que avalia a resposta recebida, identifica o que faltou — nível de detalhe, tom, formato, escopo — e reformula a solicitação com essa informação adicional obtém, sistematicamente, resultados de qualidade superior. Essa capacidade de refinamento progressivo é, em essência, a competência central do uso produtivo do Chat.

> 📸 **Captura de Tela sugerida:** Uma conversa na aba Chat com ao menos dois turnos visíveis — a solicitação inicial, a resposta do assistente e a reformulação do pedido com o refinamento — ilustra concretamente o ciclo iterativo descrito neste módulo.

Cumpre registrar duas limitações estruturais do Chat. Primeira: o assistente não acessa arquivos do computador do participante nessa interface — toda informação precisa ser fornecida explicitamente, seja digitada, seja colada, seja anexada como arquivo. Segunda: o Claude não retém memória entre sessões distintas; ao fechar e reabrir o aplicativo, o contexto da conversa anterior é perdido. Convém, portanto, manter um registro próprio das solicitações e respostas mais relevantes — ou transferir o trabalho em andamento para um arquivo no projeto, acessível via aba Code nas sessões seguintes.

---

### Exercício Prático

**Refinamento Iterativo de Solicitação** *(estimativa: 10 minutos)*

Este exercício simula um ciclo real de uso do Chat, com duas rodadas de refinamento.

1. Abra a aba Chat do Claude Desktop.
2. Envie a seguinte solicitação inicial, substituindo o campo entre colchetes por um tema de sua área:

> "Elabore um parágrafo introdutório sobre [tema escolhido]."

3. Leia a resposta recebida e anote, em uma linha, o que está faltando ou o que poderia ser melhor (por exemplo: tom muito informal, falta de referência ao contexto institucional, extensão inadequada).
4. Envie uma segunda solicitação incorporando essa observação. Exemplo de reformulação:

> "Reescreva o parágrafo, agora em registro formal e impessoal, adequado para um documento acadêmico, com no máximo 80 palavras. Não utilize a primeira pessoa do plural."

5. Compare a primeira e a segunda resposta. Identifique, objetivamente, em que aspectos a segunda é superior.
6. Opcionalmente, realize uma terceira rodada com mais um critério de refinamento.

**Critério de êxito:** O participante deverá ser capaz de demonstrar, pela comparação entre a primeira e a segunda (ou terceira) resposta, que a reformulação explícita da solicitação produziu resultado mensurável — em tom, extensão, estrutura ou precisão de conteúdo.

---

### Mão na massa

Na aba **Chat**, selecione um documento de texto de sua rotina profissional ou acadêmica — uma ementa, um trecho de relatório, um e-mail institucional — e utilize o prompt base abaixo, adaptando os campos entre colchetes:

> *"O texto a seguir é [descreva o gênero: ex. 'uma ementa de disciplina', 'um trecho de relatório de gestão', 'um e-mail institucional']. Revise-o quanto à clareza, coesão e adequação ao registro formal. Apresente o texto revisado completo e, em seguida, liste em tópicos as principais alterações realizadas e o motivo de cada uma.*
>
> [Cole aqui o texto a ser revisado]"*

Avalie o resultado, identifique um aspecto que ainda pode ser melhorado e reformule o pedido com esse critério adicional.

---

<div style="page-break-after: always;"></div>

# Módulo 4 — 🤖 A Interface Cowork: Delegação Autônoma de Tarefas

> *Com o Chat explorado em profundidade (Módulo 3), este módulo apresenta a interface Cowork — o modo de operação autônoma do Claude Desktop —, enfatizando as condições necessárias para seu uso responsável e os critérios de avaliação do trabalho entregue pelo assistente.*

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Descrever o funcionamento da interface Cowork e diferenciá-la do Chat e do Code quanto ao grau de autonomia concedido ao assistente e ao nível de supervisão exigido do participante.
2. Identificar categorias de tarefas adequadas ao Cowork — aquelas com escopo bem definido, critérios claros de entrega e baixo risco em caso de erro — e distingui-las de tarefas que exigem supervisão contínua.
3. Redigir uma definição de missão (*task brief*) suficientemente detalhada para que o assistente execute a tarefa de forma autônoma com resultado previsível.
4. Avaliar o relatório de execução produzido pelo Cowork, identificando o que foi realizado, o que eventualmente não foi e quais ajustes são necessários para uma segunda execução.

### Texto Descritivo

A interface Cowork representa o nível mais avançado de delegação disponível no Claude Desktop: o participante define uma tarefa, o assistente a executa de forma autônoma — em segundo plano, sem necessidade de interação contínua — e entrega um resultado ao final. A analogia mais precisa é a de uma instrução escrita passada a um colaborador com alto grau de autonomia: o resultado depende tanto da competência do colaborador quanto da clareza da instrução recebida.

O funcionamento prático do Cowork difere das demais interfaces em dois aspectos centrais. Primeiro, o assistente age sem solicitar aprovação a cada etapa — ao contrário do que ocorre na aba Code, onde cada alteração é apresentada em *diff view* para revisão. Segundo, o participante não acompanha o processo em tempo real; recebe o resultado ao final da execução. Essas características tornam o Cowork especialmente adequado para tarefas repetitivas, de longa duração ou compostas por múltiplas etapas claramente sequenciadas — como a revisão de um conjunto de documentos, a geração de uma série de sumários padronizados ou a reorganização de uma estrutura de arquivos segundo critérios predefinidos.

A consequência direta dessa autonomia é que a qualidade da *task brief* — a instrução que define a missão — determina em grande medida a qualidade do resultado. Uma instrução vaga produz um resultado vago; uma instrução com escopo definido, critérios de entrega explícitos e restrições claras tende a produzir um resultado próximo do esperado. Recomenda-se que a *task brief* contenha, no mínimo: (a) a descrição do que deve ser feito; (b) os arquivos ou fontes de informação relevantes; (c) o formato esperado do resultado; e (d) o que o assistente não deve alterar ou ultrapassar.

> 📸 **Captura de Tela sugerida:** A interface do Cowork com uma missão em execução ou concluída — mostrando o painel de status da tarefa e o relatório de entrega — contextualiza visualmente o modo de operação autônomo descrito neste módulo.

Convém destacar que o Cowork é indicado para participantes que já se sentem confortáveis com o Chat e o Code. Usuários iniciantes que utilizarem o Cowork sem essa base prévia correm o risco de não identificar erros no resultado entregue — pois a identificação de um erro pressupõe compreensão suficiente do que seria o resultado correto. Depreende-se, portanto, que o uso responsável do Cowork é inseparável da capacidade crítica desenvolvida nos módulos anteriores.

---

### Exercício Prático

**Elaboração e Avaliação de uma Task Brief** *(estimativa: 10 minutos)*

Este exercício é composto de duas partes: a elaboração de uma instrução de missão bem estruturada e a avaliação de uma instrução deficiente.

**Parte 1 — Avalie a instrução abaixo e identifique o que está faltando:**

> "Revise meus documentos e me diga o que está errado."

Registre, em tópicos, ao menos três problemas com essa instrução (considere: quais documentos? critério de "errado"? formato da resposta? o que não deve ser alterado?).

**Parte 2 — Reescreva a instrução aplicando os quatro elementos recomendados:**

Utilizando o seguinte cenário hipotético — "você possui uma pasta com dez atas de reunião em formato `.txt` e deseja que o assistente gere um sumário padronizado de cada uma" — redija uma *task brief* completa que contenha:

- Descrição da tarefa
- Identificação dos arquivos relevantes
- Formato esperado do resultado (extensão, estrutura, extensão máxima por sumário)
- Restrição explícita (o que o assistente não deve fazer — por exemplo, não alterar os arquivos originais)

**Critério de êxito:** A *task brief* elaborada pelo participante deverá ser suficientemente precisa para que outra pessoa — sem conhecimento prévio do contexto — consiga executar a tarefa corretamente com base apenas nela.

---

### Mão na massa

Utilize o prompt base abaixo na aba **Chat** para simular o planejamento de uma missão Cowork antes de executá-la de verdade. Adapte os campos entre colchetes à sua realidade:

> *"Vou usar a interface Cowork do Claude Desktop para realizar a seguinte tarefa: [descreva a tarefa em uma frase]. Os arquivos envolvidos são [descreva os arquivos ou o tipo de conteúdo]. O resultado esperado é [descreva o formato e o conteúdo do entregável]. Avalie se essa tarefa é adequada para execução autônoma no Cowork ou se seria melhor realizá-la na aba Code com supervisão. Se adequada, sugira como eu deveria escrever a instrução de missão."*

Com base na resposta, decida se a tarefa que você tem em mente é realmente adequada para o Cowork ou se requer supervisão mais próxima via Code.

---

<div style="page-break-after: always;"></div>

# Módulo 5 — 📁 Organização de Projetos e Proteção de Dados

> *Com as interfaces Chat e Cowork aprofundadas nos Módulos 3 e 4, este módulo desloca o foco para a configuração do ambiente de trabalho da aba Code: como estruturar uma pasta-projeto, quais arquivos o assistente pode acessar e como proteger informações sensíveis.*

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Criar uma estrutura mínima de pasta-projeto compatível com o Claude Desktop, incluindo arquivo principal, arquivo `README.md` e arquivo `.gitignore`.
2. Identificar categorias de arquivos sensíveis (credenciais, dados pessoais, chaves de acesso) e adotar as medidas básicas para protegê-los do acesso não intencional pelo assistente.
3. Selecionar, ao abrir um projeto no aplicativo, a pasta de escopo mínimo necessário — evitando conceder ao assistente acesso à totalidade do sistema de arquivos do usuário.
4. Inicializar um repositório Git em um projeto e utilizar os comandos básicos (`git status`, `git diff`, `git add`, `git commit`, `git checkout`) para rastrear e, se necessário, reverter alterações realizadas pelo assistente.

### Texto Descritivo

Na aba Code do Claude Desktop, o ponto de partida é a seleção de uma pasta do computador — denominada "projeto". A partir dessa seleção, o assistente obtém acesso de leitura a todos os arquivos de texto contidos nessa pasta: arquivos de código, documentos de texto, arquivos de configuração e qualquer outro conteúdo em formato legível. Depreende-se, portanto, que a escolha da pasta a ser compartilhada com o assistente não é uma decisão trivial.

A recomendação essencial para iniciantes é a de escopo mínimo: em vez de abrir uma pasta ampla — como a pasta de usuário do sistema operacional, que pode conter documentos pessoais, fotografias e outros dados irrelevantes para a tarefa em questão — deve-se criar e abrir apenas a subpasta específica do projeto em andamento. Assim, o assistente acessa somente o que é necessário para a tarefa solicitada.

Dentro da pasta-projeto, convém adotar uma estrutura mínima de organização. Além do arquivo principal de trabalho, recomenda-se a criação de um arquivo `README.md` — um documento de texto simples que descreve o propósito do projeto, seu conteúdo e instruções de uso. O assistente lê esse arquivo prioritariamente ao abrir um projeto, o que permite contextualizar rapidamente o escopo do trabalho. O segundo arquivo recomendado é o `.gitignore`, que especifica quais arquivos e pastas devem ser ignorados pelo sistema de controle de versão Git — e, por extensão, protegidos de compartilhamento inadvertido.

> 📸 **Captura de Tela sugerida:** Estrutura de pasta-projeto no explorador de arquivos (Windows Explorer ou Finder do macOS) mostrando os arquivos `main.py` (ou equivalente), `README.md` e `.gitignore` — auxilia o participante a visualizar a organização mínima recomendada.

O tema das credenciais merece atenção especial. Credenciais são informações de acesso — senhas de banco de dados, chaves de API, tokens de autenticação — que, se expostas, podem comprometer sistemas ou contas. No contexto do Claude Desktop, o risco ocorre quando essas informações estão armazenadas em arquivos de texto dentro da pasta-projeto aberta no aplicativo. A prática recomendada é isolá-las em um arquivo separado, convencionalmente chamado `.env`, e incluir esse arquivo na lista de exclusões do `.gitignore`. Dessa forma, o arquivo existirá no computador, mas não será rastreado pelo Git nem precisará ser enviado a repositórios remotos.

O controle de versão com Git representa uma camada adicional de segurança no trabalho com o Claude Desktop. O Git — sistema amplamente utilizado para registro de alterações em arquivos de texto — permite que o participante visualize exatamente o que o assistente modificou (por meio do comando `git diff`), aprove as mudanças (com `git add` e `git commit`) ou as descarte completamente (com `git checkout .`). Para usuários sem experiência prévia em Git, convém tratar esses comandos, inicialmente, como uma ferramenta de "desfazer" avançada: se o assistente fizer algo indesejado, o comando `git checkout .` restaura todos os arquivos ao estado do último *commit* registrado.

---

### Exercício Prático

**Criação de Estrutura Mínima de Projeto** *(estimativa: 10 minutos)*

Siga os passos abaixo para criar, no computador, a estrutura mínima de uma pasta-projeto compatível com o Claude Desktop.

1. Crie uma nova pasta chamada `meu-primeiro-projeto` em um local de fácil acesso (por exemplo, dentro de uma pasta `Projetos` na pasta de usuário).
2. Dentro dessa pasta, crie um arquivo chamado `README.md` com o seguinte conteúdo mínimo:

```
# Meu Primeiro Projeto
Projeto de aprendizagem criado durante o curso Essentials.
Finalidade: explorar o Claude Desktop de forma segura.
```

3. Crie um arquivo chamado `.gitignore` com o seguinte conteúdo:

```
.env
*.key
*.pem
```

4. Crie um arquivo de texto chamado `.env` com o conteúdo fictício abaixo (apenas para fins de exercício):

```
CHAVE_API=exemplo_nao_usar_em_producao
```

5. Abra o Claude Desktop, acesse a aba Code, clique em "Open Project" e selecione a pasta `meu-primeiro-projeto`.
6. Verifique que a lista de arquivos no painel lateral apresenta o `README.md` e o `.gitignore`, mas **não** o arquivo `.env` como arquivo de trabalho ativo.

> 📸 **Captura de Tela sugerida:** Painel lateral da aba Code com o projeto carregado — registre como evidência de conclusão do exercício.

**Critério de êxito:** O participante deverá ser capaz de descrever, sem consulta, a finalidade de cada um dos três arquivos criados (`README.md`, `.gitignore` e `.env`) e explicar por que o arquivo `.env` deve ser listado no `.gitignore`.

---

### Mão na massa

Com o projeto aberto na aba **Code**, utilize o prompt abaixo, adaptando o tema ao seu interesse:

> *"Estou criando um projeto sobre [descreva o tema: ex. 'organização de referências bibliográficas', 'controle de notas de alunos', 'análise de textos acadêmicos']. Com base nos arquivos que você pode ver nesta pasta, sugira quais outros arquivos ou seções do README.md eu deveria criar para que o projeto fique bem documentado e organizado."*

Avalie as sugestões recebidas e, se pertinentes, implemente-as na pasta-projeto criada no exercício prático.

---

<div style="page-break-after: always;"></div>

# Módulo 6 — ✍️ Formulação de Solicitações e Revisão de Resultados

> *Com o projeto estruturado e protegido (Módulo 5), este módulo concentra-se na etapa central do uso produtivo da aba Code: como redigir solicitações que gerem resultados precisos e como revisar, aprovar ou rejeitar as alterações propostas pelo assistente.*

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Redigir solicitações (*prompts*) claras, contextualizadas e com escopo delimitado, distinguindo-as de solicitações vagas que tendem a produzir resultados genéricos ou imprecisos.
2. Utilizar a visualização de diferenças (*diff view*) para comparar a versão original e a versão proposta pelo assistente, identificando as alterações realizadas.
3. Aplicar o fluxo de trabalho de revisão: aceitar alterações aprovadas, rejeitar as indesejadas e, quando pertinente, registrar as mudanças no histórico do Git.
4. Reconhecer situações em que é necessário interromper o assistente e redirecionar a solicitação, evitando a execução de alterações não autorizadas.

### Texto Descritivo

A qualidade dos resultados produzidos por um assistente de inteligência artificial é diretamente proporcional à clareza da solicitação que o origina. Esse princípio, embora simples, tem implicações práticas importantes: uma solicitação vaga ("melhore este texto") produz resultados genéricos e muitas vezes inadequados ao contexto; uma solicitação precisa ("revise o parágrafo introdutório deste relatório, mantendo o registro formal e substituindo termos coloquiais por equivalentes acadêmicos") orienta o assistente com clareza e aumenta a probabilidade de uma resposta útil na primeira tentativa.

Uma solicitação eficaz, no contexto do Claude Desktop, tende a conter três elementos: (a) a descrição do que deve ser feito; (b) o escopo — qual arquivo, seção ou trecho está em questão; e (c) os critérios ou restrições relevantes — tom desejado, formato de saída, limitações a observar. Não é necessário redigir solicitações longas ou complexas; a precisão é mais importante que a extensão. Cumpre registrar que o assistente não possui memória entre sessões distintas: ao iniciar uma nova sessão, todo contexto relevante deve ser fornecido novamente, seja por meio de um arquivo `README.md` bem redigido, seja pela inclusão de informações diretamente na solicitação.

Após o assistente propor uma alteração na aba Code, o aplicativo apresenta a *diff view* — uma visualização que exibe, lado a lado ou de forma sequencial, o conteúdo original (marcado em vermelho ou com sinal de subtração) e o conteúdo proposto (marcado em verde ou com sinal de adição). Trata-se de uma representação análoga ao recurso "controle de alterações" de processadores de texto, porém aplicada a qualquer tipo de arquivo de texto. O participante deve revisar essa visualização antes de aceitar qualquer modificação.

> 📸 **Captura de Tela sugerida:** A *diff view* do Claude Desktop com um exemplo de alteração proposta — linhas removidas destacadas em vermelho e linhas adicionadas em verde — auxilia o participante a familiarizar-se com a interface antes de utilizá-la em um projeto real.

Observa-se que o assistente, por padrão, solicita confirmação antes de aplicar alterações. Recomenda-se que iniciantes mantenham essa configuração padrão ativa. Caso o assistente inicie uma sequência de alterações que pareça inadequada, é possível interrompê-la por meio do botão de parada disponível na interface; em seguida, a solicitação pode ser reformulada com maior precisão. Após aceitar alterações, convém registrá-las no Git (`git add .` seguido de `git commit -m "descrição breve da alteração"`), criando um ponto de restauração no histórico do projeto. Caso as alterações sejam rejeitadas, o comando `git checkout .` restaura todos os arquivos ao estado anterior.

---

### Exercício Prático

**Refinamento de Solicitações** *(estimativa: 10 minutos)*

Abaixo estão três pares de solicitações. Para cada par, identifique qual das duas é mais provável de gerar um resultado preciso e explique, em uma frase, o motivo. Em seguida, confira o gabarito.

**Par 1:**
- (A) "Melhore meu texto."
- (B) "Revise o segundo parágrafo do arquivo `introducao.md`, corrigindo erros gramaticais e substituindo verbos no infinitivo por construções impessoais adequadas ao registro acadêmico."

**Par 2:**
- (A) "Crie um resumo do documento aberto, com no máximo 150 palavras, destacando o objetivo principal e os três pontos centrais do argumento."
- (B) "Faça um resumo."

**Par 3:**
- (A) "Verifique se há inconsistências."
- (B) "Verifique se os dados numéricos na tabela do arquivo `relatorio.md` são consistentes com os valores mencionados no texto descritivo do mesmo arquivo e aponte qualquer divergência encontrada."

**Gabarito:** Em todos os pares, a opção mais precisa é a (B) no Par 1, a (A) no Par 2 e a (B) no Par 3. Depreende-se que a presença de escopo delimitado (arquivo específico, seção específica), critérios explícitos (registro acadêmico, limite de palavras, tipo de inconsistência) e descrição clara da ação esperada são os elementos que distinguem solicitações eficazes de solicitações genéricas.

**Critério de êxito:** O participante deverá ser capaz de, diante de uma solicitação genérica fornecida pelo instrutor (ou por si mesmo), reformulá-la incorporando os três elementos descritos — ação, escopo e critérios — sem consulta ao material.

---

### Mão na massa

Com um arquivo de texto aberto na aba **Code** (pode ser o `README.md` criado no Módulo 3), utilize o prompt abaixo, adaptando o conteúdo entre colchetes:

> *"Analise o arquivo [nome do arquivo] e reescreva [o parágrafo X / a seção Y / a frase Z] de modo que o texto esteja adequado ao registro formal acadêmico em língua portuguesa, evitando a segunda pessoa do singular e construções coloquiais. Mantenha o significado original e não ultrapasse [número] palavras."*

Observe a *diff view* apresentada pelo assistente, avalie se as alterações propostas atendem ao critério solicitado e, em seguida, aceite ou rejeite. Se aceitar, registre a alteração com `git commit`.

---

<div style="page-break-after: always;"></div>

# Módulo 7 — 🏁 Síntese e Aplicação Integrada

> *Este módulo articula, em uma atividade única, as competências desenvolvidas nos seis módulos anteriores: verificação do ambiente, uso das três interfaces (panorama, Chat e Cowork), organização do projeto e formulação de solicitações eficazes na aba Code.*

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Executar, de forma autônoma, o fluxo completo de trabalho com o Claude Desktop: da verificação do ambiente à revisão e registro de uma alteração real em um projeto.
2. Selecionar a interface adequada — Chat, Code ou Cowork — para cada etapa de uma tarefa composta, justificando a escolha.
3. Avaliar criticamente os resultados produzidos pelo assistente em cada interface, identificando pontos de melhoria nas solicitações formuladas.
4. Demonstrar, por meio de evidências documentadas (capturas de tela e registro no Git), que as boas práticas de organização e proteção de dados foram observadas.

### Texto Descritivo

A consolidação de competências em ferramentas digitais ocorre, de modo geral, pela integração progressiva de habilidades isoladas em fluxos de trabalho completos. Nos módulos anteriores, cada etapa foi trabalhada de forma independente: a instalação, a compreensão panorâmica das interfaces, o aprofundamento no Chat, o uso responsável do Cowork, a organização do projeto e a formulação de solicitações na aba Code. Este módulo final propõe a execução integrada dessas etapas em uma atividade única, que simula um cenário real de uso do Claude Desktop.

Convém retomar, neste ponto, o fio condutor percorrido ao longo do curso. O Claude Desktop é, em essência, uma ferramenta de amplificação: seu valor está diretamente ligado à qualidade das instruções fornecidas pelo usuário e à sua capacidade de revisar criticamente os resultados. Um assistente de inteligência artificial não substitui o julgamento profissional ou acadêmico do participante; ao contrário, potencializa a produtividade quando o participante sabe exatamente o que deseja, como solicitá-lo e como avaliar o que foi entregue.

A atividade integradora a seguir foi estruturada para que o participante percorra, em sequência, cada uma das etapas do fluxo de trabalho: verificação do ambiente (Módulo 1), panorama das interfaces (Módulo 2), uso do Chat para elaboração de conteúdo (Módulo 3), avaliação da pertinência do Cowork (Módulo 4), organização e proteção do projeto (Módulo 5) e formulação de solicitação eficaz com revisão do resultado na aba Code (Módulo 6). A tabela de critérios de avaliação ao final da atividade serve como instrumento de autoavaliação.

> 📸 **Captura de Tela sugerida:** Histórico do Git (`git log`) ao final da atividade integradora, mostrando ao menos dois *commits* registrados durante a sessão — evidência de que o participante executou o fluxo completo de trabalho.

---

### Exercício Prático

**Atividade Integradora: Fluxo Completo de Trabalho com o Claude Desktop** *(estimativa: 15 minutos)*

Realize as etapas abaixo em sequência. Para cada etapa concluída, registre uma captura de tela como evidência.

**Etapa 1 — Verificação do ambiente** *(Módulo 1)*
Abra o Claude Desktop, confirme que está autenticado e que as três interfaces estão acessíveis. Anote a versão do aplicativo, disponível em *Help > About* (Windows) ou no menu do aplicativo (macOS).

**Etapa 2 — Escolha da interface** *(Módulo 2)*
Descreva em um parágrafo curto a tarefa que você vai executar nesta atividade integradora e indique qual interface — Chat, Code ou Cowork — seria adequada para cada parte dela. Justifique as escolhas.

**Etapa 3 — Elaboração via Chat com refinamento** *(Módulo 3)*
Na aba **Chat**, formule uma solicitação sobre um tema de sua área de interesse — por exemplo, peça ao assistente que sugira três perguntas de pesquisa relevantes para o tema escolhido. Após receber a resposta, refine-a com pelo menos um critério adicional (tom, extensão, formato) e registre ambas as respostas para comparação.

**Etapa 4 — Avaliação da pertinência do Cowork** *(Módulo 4)*
Com base na tarefa definida na Etapa 2, avalie se alguma parte dela seria adequada para execução autônoma via Cowork. Redija uma *task brief* hipotética de duas a quatro frases para essa parte, mesmo que opte por não executá-la agora.

**Etapa 5 — Organização do projeto** *(Módulo 5)*
Abra, na aba **Code**, a pasta-projeto criada no Módulo 5. Confirme que o `.gitignore` está presente e que o arquivo `.env` não aparece como arquivo de trabalho ativo. Execute `git status` no terminal e verifique que o estado do repositório está limpo (sem alterações pendentes).

**Etapa 6 — Solicitação eficaz e revisão** *(Módulo 6)*
No projeto aberto, formule uma solicitação ao assistente que envolva a edição de um arquivo existente (por exemplo, acrescente ao `README.md` uma seção "Objetivos" com base nas perguntas de pesquisa obtidas na Etapa 3). Revise a *diff view*, aceite as alterações e registre-as com `git commit -m "Módulo 7: adiciona seção Objetivos ao README"`.

**Etapa 7 — Verificação final**
Execute `git log` e confirme a presença do *commit* registrado. Registre captura de tela do histórico.

**Critérios de avaliação**

| Critério | Atendido? |
|---|---|
| O aplicativo está autenticado e as três interfaces estão acessíveis | ☐ Sim ☐ Não |
| A justificativa de escolha de interfaces (Etapa 2) está documentada | ☐ Sim ☐ Não |
| A solicitação no Chat foi refinada com ao menos um critério adicional e as duas respostas foram comparadas | ☐ Sim ☐ Não |
| Uma *task brief* hipotética para o Cowork foi elaborada com os quatro elementos recomendados | ☐ Sim ☐ Não |
| O projeto aberto na aba Code possui `README.md` e `.gitignore` | ☐ Sim ☐ Não |
| O arquivo `.env` está protegido (não aparece como arquivo de trabalho ativo) | ☐ Sim ☐ Não |
| A *diff view* foi revisada antes da aceitação das alterações | ☐ Sim ☐ Não |
| O *commit* com mensagem descritiva foi registrado no histórico do Git | ☐ Sim ☐ Não |
| As capturas de tela documentam cada etapa realizada | ☐ Sim ☐ Não |

---

### Mão na massa

Ao final da atividade integradora, retorne à aba **Chat** e utilize o prompt abaixo para uma reflexão orientada:

> *"Com base no que aprendi sobre o Claude Desktop neste curso — instalação, diferença entre Chat, Code e Cowork, organização de projetos e formulação de solicitações —, gostaria de usar a ferramenta para [descreva uma tarefa concreta da sua rotina acadêmica ou profissional]. Indique qual interface seria mais adequada para essa tarefa, que tipo de projeto eu deveria criar, quais arquivos incluir e como deveria formular a primeira solicitação para obter um resultado útil."*

Use a resposta como ponto de partida para o próximo projeto real que pretende desenvolver com o aplicativo.

---

<div style="page-break-after: always;"></div>

## Encerramento

O presente curso percorreu, de forma progressiva e integrada, as etapas fundamentais para o uso autônomo do Claude Desktop: a verificação e configuração do ambiente, a compreensão panorâmica das três interfaces de trabalho, o aprofundamento nas possibilidades do Chat com refinamento iterativo, o uso responsável da interface Cowork para delegação autônoma, a organização segura de projetos e a formulação de solicitações eficazes com revisão crítica dos resultados na aba Code. Ao concluir as atividades propostas, o participante dispõe dos elementos necessários para incorporar o aplicativo à sua rotina acadêmica ou profissional de forma consciente e produtiva. Recomenda-se, contudo, que a consolidação dessas competências se dê por meio da prática regular: a familiaridade com qualquer ferramenta digital aprofunda-se com o uso continuado, e cada sessão de trabalho oferece oportunidades de refinamento das solicitações e de expansão do repertório de casos de uso.

Para os participantes que desejem avançar além dos conteúdos abordados neste curso Essentials, sugere-se a exploração dos seguintes temas: a configuração do arquivo `.claude.md`, que permite definir regras e preferências persistentes para o assistente em cada projeto; o uso da interface Cowork para automação de tarefas repetitivas; a integração do Claude Desktop com ambientes de desenvolvimento integrado (*IDEs*) como VS Code e PyCharm; e os Módulos de Nível 2 do material-fonte, que abordam casos de uso avançados, incluindo a utilização de servidores MCP (*Model Context Protocol*) para expansão das capacidades do assistente. A trilha "Essentials" da qual este curso faz parte inclui outros módulos complementares que cobrem ferramentas e fluxos de trabalho adicionais.

> **Síntese:** O Claude Desktop é uma ferramenta de amplificação — amplifica o entendimento de quem compreende o que solicita e revisa o que recebe; a produtividade genuína emerge não da delegação irrefletida, mas da colaboração crítica entre o participante e o assistente.
