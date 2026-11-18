# Plano de Aula — ChatGPT no Excel e Google Sheets (Essentials)

---

## Identificação

| Campo | Definição |
|---|---|
| Curso | ChatGPT no Excel e Google Sheets — Essentials |
| Natureza | Curto, introdutório e prático |
| Carga horária | 85 minutos (aproximadamente 1h25) |
| Público-alvo | Profissionais que utilizam planilhas no cotidiano — analistas, contadores, servidores públicos, estudantes e demais usuários de Excel ou Google Sheets — sem experiência prévia com ferramentas de inteligência artificial |
| Pré-requisitos | Conhecimento básico de Excel ou de Google Sheets; conta ativa no ChatGPT, em qualquer plano que contemple o recurso (Free, Go, Plus, Pro, Business, Enterprise, Edu ou K-12). Nenhum conhecimento prévio em inteligência artificial é exigido |
| Recursos necessários | Computador com acesso ao Excel ou ao Google Sheets (aplicativo de mesa ou versão web); conexão à internet; conta ativa no ChatGPT |

---

### Objetivo Geral

O presente curso tem por finalidade capacitar o participante a compreender, instalar e utilizar, de forma autônoma e segura, o recurso do ChatGPT integrado diretamente ao Excel e ao Google Sheets — um assistente de inteligência artificial (isto é, um sistema capaz de interpretar linguagem natural e gerar respostas ou executar ações a partir dela) que passa a operar dentro da própria planilha, em vez de exigir que o usuário copie e cole dados em uma janela externa. Ao término do curso, espera-se que o participante seja capaz de instalar o recurso no ambiente que utiliza, redigir instruções (denominadas "prompts") claras o suficiente para obter resultados úteis, e aplicar um critério mínimo de verificação antes de aceitar qualquer alteração sugerida pela inteligência artificial em sua planilha.

---

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Reconhecer o funcionamento do ChatGPT integrado ao Excel e ao Google Sheets, distinguindo-o do uso da ferramenta "por fora" da planilha.
2. Instalar corretamente o recurso no Excel ou no Google Sheets, identificando previamente se o seu plano de acesso permite essa instalação.
3. Utilizar linguagem natural para criar, atualizar e organizar dados em uma planilha, por meio de instruções dirigidas à inteligência artificial.
4. Elaborar prompts específicos e objetivos, e aplicar um critério básico de verificação antes de aceitar uma alteração proposta pela inteligência artificial.

---

### Estrutura e Sequência dos Módulos

Os módulos seguem progressão cumulativa: cada bloco pressupõe o domínio do anterior, partindo do reconhecimento conceitual da ferramenta, avançando pela instalação e pelo uso conversacional básico, até a formulação de instruções mais precisas e a verificação de resultados. O módulo final integra as quatro competências em uma única sequência de aplicação prática.

| Módulo | Título | Referência (material-fonte) | Tempo |
|---|---|---|---|
| 1 | O que é o ChatGPT para Planilhas | RoteiroCompletoChatGPT_Excel.md — Módulo 1, Aulas 1 e 2 | 15 min |
| 2 | Instalação sem Mistério | RoteiroCompletoChatGPT_Excel.md — Módulo 1, Aulas 3 e 4 | 20 min |
| 3 | Conversando com a Planilha | CursoCriadoChatGPT.txt — Módulo 2 | 18 min |
| 4 | Prompts Eficazes e Verificação Básica | ANALISE_CRITICA_CHATGPT_EXCEL_GOOGLE_SHEETS.md — recomendações sobre engenharia de prompt e verificação | 17 min |
| 5 | Síntese e Aplicação Integrada | Integração dos Módulos 1 a 4 | 15 min |

---
---

# Módulo 1 — O que é o ChatGPT para Planilhas

> Ponto de partida do curso: nenhum conhecimento prévio é pressuposto.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Definir, com as próprias palavras, o que é a barra lateral do ChatGPT dentro do Excel ou do Google Sheets.
2. Diferenciar o uso do ChatGPT integrado à planilha do uso "por fora" dela (copiar dados, colar em uma janela externa e trazer o resultado de volta manualmente).
3. Identificar, a partir do próprio plano de assinatura, se possui acesso ao recurso e em que profundidade.
4. Reconhecer que Excel e Google Sheets constituem ambientes independentes, sem compartilhamento de histórico de conversa entre si.

### Texto Descritivo

O ChatGPT para Planilhas é um recurso que incorpora, diretamente ao Excel ou ao Google Sheets, um painel de conversa — denominado barra lateral — capaz de ler o conteúdo de células, fórmulas e nomes de abas da planilha aberta. Trata-se, em essência, de um assistente de inteligência artificial (ou seja, um programa capaz de interpretar pedidos formulados em linguagem natural e responder ou agir a partir deles) que passa a "enxergar" a planilha sem que o usuário precise descrever sua estrutura a cada pergunta. A analogia mais adequada é a de um colega de trabalho que já está observando a planilha ao lado do usuário: não é necessário explicar onde estão os dados, apenas indicar o que se deseja fazer com eles.

Essa característica distingue o recurso do uso "por fora" da ferramenta, prática na qual o usuário copia trechos da planilha, cola-os em uma janela separada do ChatGPT, aguarda uma resposta e, em seguida, transporta manualmente o resultado de volta para a planilha original. Tal método, embora funcional, consome tempo e introduz risco de erro de transcrição a cada etapa. A integração direta elimina essas duas etapas intermediárias, permitindo que o pedido e a resposta ocorram no mesmo ambiente em que os dados residem.

Cumpre registrar que o acesso ao recurso não é uniforme entre todos os planos de assinatura do ChatGPT. Os planos Free e Go oferecem acesso, porém limitado, sujeito a restrições de uso mais frequentes. Os planos Plus e Pro oferecem acesso sujeito ao limite de uso chamado "agêntico" — expressão que designa a quantidade de ações que a inteligência artificial pode executar de forma autônoma dentro de um determinado período. Já os planos corporativos e educacionais (Business, Enterprise, Edu e K-12) dependem de habilitação prévia por parte de um administrador de tecnologia da informação, já que, nesses ambientes, o recurso normalmente vem desligado por padrão.

| Plano | Acesso ao recurso | Nível de uso |
|---|---|---|
| Free / Go | Sim, limitado | Uso básico, sujeito a limites frequentes |
| Plus / Pro | Sim | Sujeito ao limite de uso agêntico da conta |
| Business / Enterprise / Edu / K-12 | Sim, via workspace | Depende de habilitação pelo administrador |

Por fim, convém esclarecer que o Excel e o Google Sheets constituem dois ambientes de instalação e de uso independentes: embora sigam os mesmos princípios de funcionamento, cada um possui sua própria barra lateral, com histórico de conversa próprio, não compartilhado entre as duas plataformas. Essa distinção será retomada no Módulo 2, no momento da instalação em cada um dos ambientes.

### Exercício Prático

**Verificação do próprio plano de acesso (5 min)**

1. Consultar, na própria conta do ChatGPT, qual é o plano de assinatura atualmente ativo.
2. Comparar o plano identificado com a tabela apresentada no Texto Descritivo.
3. Registrar, em uma frase, se o acesso é completo, limitado ou dependente de habilitação administrativa.

**Critério de êxito:** o participante deverá ter classificado corretamente o próprio nível de acesso em uma das três categorias da tabela (completo, limitado ou dependente de administrador), condição necessária para conduzir a instalação no Módulo 2.

---

# Módulo 2 — Instalação sem Mistério

> Pressupõe o reconhecimento do próprio nível de acesso (Módulo 1); desloca o foco da compreensão conceitual para a execução do procedimento de instalação.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Executar o procedimento de instalação do recurso no Excel, a partir do Microsoft Marketplace.
2. Executar o procedimento de instalação do recurso no Google Sheets, a partir do Google Workspace Marketplace.
3. Explicar, em linguagem simples, o que é o Controle de Acesso Baseado em Funções (RBAC) e por que ele pode impedir o uso do recurso mesmo após a instalação técnica.
4. Diagnosticar ao menos dois erros comuns de instalação e indicar sua respectiva solução.

### Texto Descritivo

A instalação do ChatGPT no Excel ocorre por meio do Microsoft Marketplace, uma loja de suplementos (programas complementares que estendem as funcionalidades do Excel) acessível pelo menu "Página Inicial". O procedimento individual compreende localizar a opção "Suplementos", buscar pelo termo "ChatGPT", confirmar tratar-se do suplemento oficial da OpenAI, instalá-lo e, por fim, autenticar-se com a conta ChatGPT correspondente ao plano identificado no Módulo 1. Em ambientes corporativos, o procedimento é conduzido por um administrador, que distribui o suplemento a usuários ou grupos específicos a partir do Microsoft 365 admin center, mediante o envio de um arquivo de manifesto técnico.

No Google Sheets, o procedimento equivalente ocorre pelo menu "Extensões", que dá acesso ao Google Workspace Marketplace. Ali, o usuário localiza o complemento oficial do ChatGPT, aceita as permissões solicitadas — leitura e edição da planilha ativa — e autentica-se com a conta compatível. Também nesse ambiente existe um mecanismo de controle corporativo, denominado Controle de Acesso Baseado em Funções (em inglês, Role-Based Access Control, ou RBAC): trata-se do procedimento pelo qual uma organização determina quais cargos ou departamentos podem utilizar determinado recurso, independentemente de o usuário individual já ter concedido as permissões técnicas exigidas pelo complemento.

Depreende-se, portanto, que existem duas camadas distintas de autorização: a permissão técnica, concedida pelo próprio usuário ao aceitar o funcionamento do suplemento ou complemento sobre sua planilha, e a permissão administrativa, concedida pela organização por meio do RBAC. A posse da primeira não implica a posse da segunda — situação frequente em contas corporativas, na qual o usuário conclui a instalação técnica, mas permanece impedido de utilizar o recurso até que um administrador o habilite.

Os erros mais comuns nesta etapa decorrem justamente da confusão entre essas duas camadas, ou de instabilidades pontuais de carregamento, conforme sintetizado a seguir.

| Erro comum | Causa provável | Solução |
|---|---|---|
| O suplemento ou complemento não aparece na busca da loja | Conta corporativa com acesso à loja restrito | Verificar com o administrador de tecnologia da informação |
| A barra lateral não abre após a instalação | Falha temporária de carregamento | Fechar e reabrir o Excel ou recarregar o Google Sheets |
| "Instalado, mas o uso continua bloqueado" | RBAC ainda não habilitado para o usuário | Solicitar habilitação ao administrador |

### Exercício Prático

**Instalação guiada (10 min)**

1. Abrir o Excel ou o Google Sheets, conforme o ambiente disponível ao participante.
2. Localizar o menu de suplementos (Excel) ou de extensões (Google Sheets).
3. Buscar e instalar o recurso oficial do ChatGPT.
4. Autenticar-se com a conta correspondente ao plano identificado no Módulo 1.
5. Confirmar a abertura da barra lateral.

**Critério de êxito:** confirmação, por meio de checklist, dos quatro itens seguintes — recurso localizado; instalação concluída; autenticação realizada; barra lateral aberta. Caso algum item não seja alcançável no momento da aula (por exemplo, ausência de permissão administrativa), o participante deverá registrar por escrito qual das causas da tabela de erros comuns corresponde à sua situação.

---

# Módulo 3 — Conversando com a Planilha

> Pressupõe a barra lateral instalada e aberta (Módulo 2); desloca o foco da instalação para o uso conversacional do recurso sobre dados reais.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Utilizar linguagem natural para solicitar a criação de uma planilha simples.
2. Solicitar uma atualização incremental sobre uma planilha já existente.
3. Solicitar a limpeza ou a organização de dados, definindo previamente o critério a ser aplicado.
4. Solicitar a explicação de uma fórmula já existente na planilha.

### Texto Descritivo

Uma vez instalada, a barra lateral do ChatGPT pode ser utilizada para quatro finalidades centrais no uso cotidiano: criar, atualizar, limpar e explicar. Criar corresponde a solicitar, em linguagem natural, a geração de uma estrutura nova — por exemplo, uma lista de controle de despesas com colunas de data, categoria e valor. Atualizar corresponde a pedir uma alteração incremental sobre algo já existente, como a inclusão de uma nova coluna ou o ajuste de uma fórmula, sem a necessidade de reconstruir a planilha inteira.

Limpar refere-se à padronização de dados inconsistentes — rótulos escritos de formas diferentes, duplicatas aparentes ou fórmulas quebradas. Recomenda-se, nesse caso, que o participante explicite à inteligência artificial qual é o critério de limpeza desejado (por exemplo, "remova linhas cujo campo de valor esteja vazio"), evitando que a ferramenta aplique um critério próprio, potencialmente divergente da intenção do usuário. Explicar, por fim, corresponde a solicitar que a inteligência artificial descreva, célula por célula ou de forma consolidada, a lógica de uma fórmula existente — recurso particularmente útil ao se deparar com planilhas herdadas de terceiros.

Um recurso transversal a essas quatro finalidades é o símbolo "@", utilizado para direcionar o pedido a uma aba específica dentro de uma pasta de trabalho com múltiplas abas — por exemplo, "@Orçamento resuma os totais por categoria". Sem esse direcionamento, a inteligência artificial pode considerar o contexto da aba ativa, o que nem sempre corresponde à intenção do usuário em planilhas mais complexas.

Convém registrar, desde já, um hábito que será aprofundado no Módulo 4: antes de aceitar qualquer alteração proposta pela inteligência artificial, recomenda-se revisar o resultado apresentado, e não presumir sua correção automaticamente. Esse princípio — revisar antes de confiar — constitui o fio condutor da etapa final deste curso.

### Exercício Prático

**Criação e atualização de uma planilha simples (8 min)**

1. Na barra lateral, solicitar a criação de uma lista de controle de despesas com três colunas (data, categoria e valor).
2. Conferir o resultado gerado na planilha.
3. Solicitar uma atualização incremental, como a inclusão de uma quarta coluna de observações.
4. Conferir se a atualização preservou os dados já existentes.

**Critério de êxito:** a planilha final deverá conter as quatro colunas solicitadas, com os dados da etapa de criação preservados após a etapa de atualização — evidência de que o pedido incremental não substituiu, mas complementou, a estrutura anterior.

---

# Módulo 4 — Prompts Eficazes e Verificação Básica

> Pressupõe familiaridade com o uso conversacional básico (Módulo 3); desloca o foco da execução de comandos simples para a qualidade da instrução fornecida e para a verificação do resultado.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Identificar os elementos que compõem um prompt eficaz.
2. Reescrever um prompt vago, transformando-o em uma instrução específica e objetiva.
3. Aplicar o hábito de solicitar um plano de ação antes de aceitar uma edição de maior porte.
4. Aplicar um critério mínimo de verificação sobre uma resposta gerada pela inteligência artificial, antes de aceitá-la.

### Texto Descritivo

Denomina-se prompt a instrução fornecida à inteligência artificial em linguagem natural. Um prompt eficaz costuma reunir três elementos: o objetivo específico da solicitação (o que exatamente se deseja obter), o escopo delimitado (sobre quais dados, colunas ou abas a solicitação deve incidir) e, quando pertinente, o formato esperado do resultado (por exemplo, uma tabela, um resumo em texto ou uma fórmula). A ausência desses elementos tende a gerar respostas genéricas, que exigem novas rodadas de ajuste até se aproximarem da necessidade real do usuário.

A diferença de qualidade entre um prompt vago e um prompt específico pode ser observada no contraste a seguir. Um prompt vago, como "organize esta planilha", não define o que significa organizar, tampouco delimita o escopo da ação. Um prompt específico, como "@Despesas: agrupe os valores por categoria e ordene do maior para o menor, sem alterar a coluna de data", define objetivo, escopo e critério de execução em uma única instrução, reduzindo a margem de interpretação da inteligência artificial.

Recomenda-se, ainda, que, diante de alterações de maior porte, o participante solicite previamente um plano de ação — isto é, peça à inteligência artificial que descreva os passos que pretende executar antes de aplicá-los à planilha. Essa prática permite identificar, antes da execução, eventuais desvios entre o que foi pedido e o que seria efetivamente realizado.

Por fim, retomando o princípio apresentado no Módulo 3, convém aplicar um critério mínimo de verificação antes de aceitar qualquer resultado gerado pela inteligência artificial: conferir se os valores numéricos permanecem coerentes com os dados originais, se nenhuma linha ou coluna foi removida sem solicitação expressa, e se a lógica de eventual fórmula alterada corresponde ao que foi pedido. Tal verificação não substitui o julgamento do usuário — apenas o orienta, reduzindo o risco de aceitar, por comodidade, uma alteração incorreta.

### Exercício Prático

**Questão de múltipla escolha**

Um usuário deseja que a inteligência artificial identifique, em uma planilha de vendas, quais vendedores não atingiram a meta mensal, e que apresente o resultado em uma tabela ordenada do menor para o maior valor vendido. Qual das opções a seguir constitui o prompt mais eficaz para esse pedido?

A) "Veja quem não vendeu bem este mês."

B) "@Vendas: liste os vendedores cujo valor vendido seja inferior à meta na coluna 'Meta', em uma tabela ordenada do menor para o maior valor vendido."

C) "Analise minha planilha de vendas."

D) "Me ajude com as vendas do mês."

**Gabarito:** alternativa B.

**Fundamentação:** a alternativa B delimita o escopo (aba "Vendas"), define o objetivo específico (vendedores abaixo da meta, com base em coluna nomeada) e especifica o formato esperado (tabela ordenada do menor para o maior). As demais alternativas carecem de ao menos dois desses três elementos, exigindo que a inteligência artificial presuma informações não fornecidas.

---
---

# Módulo 5 — Síntese e Aplicação Integrada

> Pressupõe o domínio cumulativo dos Módulos 1 a 4; desloca o foco da aprendizagem de competências isoladas para sua aplicação combinada em uma única sequência de trabalho.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Confirmar as condições de acesso e instalação do recurso na própria conta.
2. Utilizar linguagem natural para criar e atualizar uma planilha simples.
3. Redigir um prompt específico, contendo objetivo, escopo e formato esperado.
4. Aplicar o critério mínimo de verificação antes de aceitar o resultado gerado.

### Texto Descritivo

O presente módulo não introduz conteúdo novo; sua função é articular, em uma única sequência prática, as quatro competências desenvolvidas ao longo do curso. Parte-se do pressuposto de que o participante já reconhece o que é o recurso (Módulo 1), já sabe instalá-lo ou já identificou o obstáculo que o impede de fazê-lo (Módulo 2), já é capaz de conduzir uma conversa básica com a planilha (Módulo 3) e já compreende os elementos de um prompt eficaz, bem como o hábito de verificação (Módulo 4).

A atividade a seguir reproduz, em escala reduzida, o ciclo completo de uso da ferramenta em um contexto de trabalho real: partir de uma necessidade concreta, formular uma instrução específica, obter um resultado e verificá-lo antes de considerá-lo concluído. Tal ciclo — pedido, execução, verificação — constitui o padrão de uso recomendado para qualquer aplicação futura do recurso, independentemente da complexidade da tarefa.

Observa-se que a etapa de verificação, retomada aqui pela terceira vez no curso (Módulos 3, 4 e 5), não é um passo opcional: é ela que diferencia o uso responsável do recurso de uma aceitação automática de resultados gerados por inteligência artificial, prática desaconselhada inclusive em tarefas de baixa complexidade.

### Exercício Prático

**Atividade Integradora — Ciclo Completo de Uso (15 min)**

1. Confirmar que o recurso está instalado e a barra lateral, aberta (ou registrar por escrito o obstáculo identificado no Módulo 2, caso a instalação não tenha sido concluída).
2. Redigir um prompt específico — contendo objetivo, escopo e formato esperado — solicitando a criação de uma planilha simples de controle de tarefas, com colunas de tarefa, responsável e prazo.
3. Solicitar uma atualização incremental sobre a planilha criada, como a inclusão de uma coluna de status.
4. Aplicar o critério mínimo de verificação apresentado no Módulo 4 sobre o resultado obtido.
5. Registrar, em uma frase, se a resposta da inteligência artificial foi aceita, ajustada ou rejeitada, e por quê.

| Critério de avaliação | Atendido? |
|---|---|
| Instalação confirmada ou obstáculo corretamente diagnosticado | |
| Planilha criada por meio de linguagem natural, com as três colunas solicitadas | |
| Prompt de atualização contendo objetivo, escopo e formato específicos | |
| Verificação aplicada antes da aceitação do resultado | |
| Registro escrito da decisão final (aceito, ajustado ou rejeitado) e de sua justificativa | |

---

## Encerramento

O curso cumpriu sua finalidade ao conduzir o participante do reconhecimento inicial da ferramenta até sua aplicação integrada em uma sequência real de trabalho, abrangendo o entendimento conceitual, a instalação, o uso conversacional básico e a formulação de instruções específicas acompanhadas de verificação. Recomenda-se a prática regular do recurso em tarefas cotidianas de planilha, de modo que o ciclo de pedido, execução e verificação se torne um hábito consolidado, e não um procedimento aplicado apenas em contexto de treinamento.

Para aprofundamento, sugere-se a exploração de tópicos não abordados nesta versão introdutória, tais como a automação de tarefas recorrentes por meio de playbooks reutilizáveis (denominados Skills), a conexão a fontes de dados externas e um checklist de auditoria mais detalhado para alterações de maior impacto — temas tratados em versões estendidas desta trilha.

> **Síntese:** o valor do ChatGPT integrado à planilha não está em substituir o julgamento de quem a utiliza, mas em reduzir o tempo entre a formulação de um pedido claro e a obtenção de um resultado verificável.
