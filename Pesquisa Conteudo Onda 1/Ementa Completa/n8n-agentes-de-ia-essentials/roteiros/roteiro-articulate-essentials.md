# Roteiro de produção — Agentes de IA no n8n (Essentials)

## Análise essencial do material-fonte

- O curso deve diferenciar workflow, modelo e agente antes de apresentar componentes.
- A progressão conceitual é decisão, arquitetura, contexto, controle e evidência.
- Memória e RAG precisam ser tratados como recursos distintos.
- Segurança exige camadas; mensagem de sistema não é barreira suficiente.
- Menus e recursos sujeitos à versão ficam nas pendências, não como afirmações universais.

## Identificação

| Campo | Definição |
|---|---|
| Curso | Agentes de IA no n8n — Essentials |
| Lições | 5 |
| Formato | Autoinstrucional e assíncrono |
| Público-alvo | Profissionais iniciantes em automação com IA |
| Pré-requisitos | Nenhum conhecimento de programação |
| Tempo estimado | 115 minutos |
| Recursos | Ambiente do Rise 360 |

## Objetivo geral

Compreender a arquitetura de um agente de IA no n8n e aplicar critérios de escolha, segurança, teste e governança.

## Objetivos de aprendizagem

- Diferenciar workflow determinístico, modelo de linguagem e agente.
- Relacionar entrada, decisão, memória, conhecimento e ação.
- Selecionar controles proporcionais ao risco.
- Avaliar evidências de funcionamento, qualidade e segurança.

# Módulo 1 - Quando usar um agente

## Ficha de produção da lição

- Objetivo: distinguir automação determinística, modelo de linguagem e agente de IA.
- Resultado observável: o participante classifica corretamente quatro situações.

| Etapa | Conteúdo | Bloco Rise 360 |
|---|---|---|
| Abertura | Problema de escolha | Cover |
| Conceitos | Três abordagens | Text + Tabs |
| Critério | Quando usar agente | Statement + List |
| Verificação | Caso de regra fixa | Knowledge Check |
| Aplicação | Quatro situações | Sorting Activity |

> A ficha orienta a produção e não deve aparecer no curso publicado.

> » IA: ▼▼▼ INÍCIO DA LIÇÃO - "Módulo 1 - Quando usar um agente" - todo o conteúdo até o marcador de fim corresponde a UMA única lição no Rise 360; não dividir, duplicar, fundir ou criar sublições. Não publicar este marcador. ▼▼▼

> » IA: BLOCO RISE 360 - Cover. Criar abertura com fundo sólido escuro e alto contraste. Não publicar esta linha.

BLOCO RISE 360  
Cover

**Título visível:** Quando usar um agente  
**Configuração:** fundo sólido; sem imagem; subtítulo abaixo do título.  
**Conteúdo visível:** Nem toda automação precisa decidir. Nesta lição, o foco é escolher a abordagem mais simples para cada problema.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Text. Apresentar o ponto de partida em dois parágrafos. Não publicar esta linha.

BLOCO RISE 360  
Text

**Título visível:** Três formas de resolver  
**Configuração:** texto padrão; largura confortável.  
**Conteúdo visível:** Um workflow é uma sequência visual de nós. Quando condições e ações são conhecidas, cada regra conduz a um resultado previamente definido.

Um modelo de linguagem interpreta e produz texto. Um agente combina o modelo com ferramentas e escolhe quando usá-las para cumprir um objetivo.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Tabs. Criar três abas paralelas. Não publicar esta linha.

BLOCO RISE 360  
Tabs

**Título visível:** Compare as abordagens  
**Configuração:** três abas; primeira aberta.  
**Conteúdo visível:**

- **Workflow determinístico:** segue regras e condições previamente definidas. É adequado para transferências, avisos e validações previsíveis.
- **Modelo de linguagem:** interpreta ou produz conteúdo, sem atuar sozinho em outros sistemas.
- **Agente de IA:** recebe um objetivo, consulta um modelo e pode selecionar tools para buscar dados ou executar ações.

**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Statement. Destacar o critério central. Não publicar esta linha.

BLOCO RISE 360  
Statement

**Título visível:** Ideia-chave  
**Configuração:** estilo de destaque informativo.  
**Conteúdo visível:** Use agente quando a tarefa exigir interpretação e escolha contextual.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - List. Apresentar critérios de decisão. Não publicar esta linha.

BLOCO RISE 360  
List

**Título visível:** Antes de escolher  
**Configuração:** lista com marcadores.  
**Conteúdo visível:**

- Prefira regras fixas quando entrada, condição e ação forem previsíveis.
- Use modelo quando o resultado for apenas conteúdo.
- Use agente quando houver decisão linguística e ferramentas externas.
- Considere custo, risco e necessidade de auditoria.

**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Knowledge Check - Multiple Choice. Permitir nova tentativa. Não publicar esta linha.

BLOCO RISE 360  
Knowledge Check - Multiple Choice

**Título visível:** Verificação formativa  
**Configuração:** uma resposta; embaralhar alternativas; nova tentativa habilitada.  
**Conteúdo visível:** Uma equipe copia diariamente os mesmos campos de uma tabela validada para outro sistema. Qual desenho é mais adequado?

A. Agente com várias ferramentas.  
B. Workflow determinístico.  
C. Modelo de linguagem sem workflow.  
D. RAG com documentos.  
**Gabarito e feedback:** correta B. Acerto: “As regras e os campos são conhecidos; a sequência fixa é mais simples e auditável.” Erro: “Procure a opção que resolve uma tarefa previsível sem decisão contextual.”

> » IA: BLOCO RISE 360 - Sorting Activity. Criar três categorias e quatro cartões. Não publicar esta linha.

BLOCO RISE 360  
Sorting Activity

**Título visível:** Aplique o critério  
**Configuração:** categorias visíveis; feedback final; nova tentativa.  
**Conteúdo visível:** Classifique cada situação.

Categorias: Workflow determinístico; Modelo de linguagem; Agente de IA.

Itens:

- Enviar aviso quando o prazo vencer.
- Redigir um resumo sem acessar sistemas.
- Interpretar um pedido livre e escolher uma consulta.
- Buscar trechos de um manual antes de responder.

**Gabarito e feedback:** prazo → workflow; resumo → modelo; pedido livre → agente; busca em manual → agente. Feedback: “A diferença está na necessidade de regras fixas, produção de conteúdo ou decisão com ferramentas.”

> » IA: ▲▲▲ FIM DA LIÇÃO - "Módulo 1 - Quando usar um agente" - encerrar esta lição aqui. Não publicar este marcador. ▲▲▲

# Módulo 2 - Como o agente decide e age

## Ficha de produção da lição

- Objetivo: relacionar os componentes de entrada, decisão e ação.
- Resultado observável: o participante identifica a causa provável de uma tool escolhida incorretamente.

| Etapa | Conteúdo | Bloco Rise 360 |
|---|---|---|
| Abertura | Do chat à ação | Cover |
| Arquitetura | Componentes | Process |
| Orientação | System Message e tools | Accordion |
| Controle | Iterações e formato | Statement + Text |
| Verificação | Tool ambígua | Knowledge Check |
| Aplicação | Arquitetura de atendimento | Knowledge Check |

> A ficha orienta a produção e não deve aparecer no curso publicado.

> » IA: ▼▼▼ INÍCIO DA LIÇÃO - "Módulo 2 - Como o agente decide e age" - todo o conteúdo até o marcador de fim corresponde a UMA única lição no Rise 360; não dividir, duplicar, fundir ou criar sublições. Não publicar este marcador. ▼▼▼

> » IA: BLOCO RISE 360 - Cover. Criar abertura sem imagem. Não publicar esta linha.

BLOCO RISE 360  
Cover

**Título visível:** Como o agente decide e age  
**Configuração:** fundo sólido; alto contraste.  
**Conteúdo visível:** Uma resposta confiável depende da relação entre entrada, modelo, instruções e tools.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Process. Mostrar o fluxo conceitual em quatro etapas. Não publicar esta linha.

BLOCO RISE 360  
Process

**Título visível:** O caminho de uma mensagem  
**Configuração:** quatro etapas numeradas.  
**Conteúdo visível:**

1. **Receber:** o Chat Trigger inicia uma execução para cada mensagem.
2. **Interpretar:** o AI Agent envia o contexto ao Chat Model.
3. **Decidir:** o modelo escolhe responder ou chamar uma tool.
4. **Entregar:** o workflow retorna a resposta e registra a execução.

**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Accordion. Criar três itens independentes. Não publicar esta linha.

BLOCO RISE 360  
Accordion

**Título visível:** O que orienta a decisão  
**Configuração:** primeiro item fechado; permitir abrir todos.  
**Conteúdo visível:**

- **System Message:** define objetivo, fontes autorizadas, restrições e condições de uso das tools. Orienta o modelo, mas não substitui controles externos.
- **Descrição da tool:** informa nome, finalidade e esquema. Quanto mais inequívoca, melhor a escolha da capacidade correta.
- **Tool calling:** permite ao modelo selecionar uma função e preencher os parâmetros previstos pelo esquema.

**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Statement. Destacar o alerta. Não publicar esta linha.

BLOCO RISE 360  
Statement

**Título visível:** Atenção  
**Configuração:** estilo de alerta.  
**Conteúdo visível:** A mensagem de sistema orienta o agente, mas não garante segurança.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Text. Explicar limites de operação. Não publicar esta linha.

BLOCO RISE 360  
Text

**Título visível:** Limites úteis  
**Configuração:** dois parágrafos curtos.  
**Conteúdo visível:** Max Iterations limita o número de ciclos do agente; o padrão documentado é dez. Reduzir esse valor pode conter loops e custos, desde que a tarefa continue viável.

Um output parser exige estrutura previsível, como campos JSON. Ele controla formato, não veracidade nem permissão.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Knowledge Check - Multiple Choice. Permitir nova tentativa. Não publicar esta linha.

BLOCO RISE 360  
Knowledge Check - Multiple Choice

**Título visível:** Verificação formativa  
**Configuração:** uma resposta; nova tentativa habilitada.  
**Conteúdo visível:** Um agente possui duas tools chamadas “Ferramenta 1” e “Ferramenta 2” e escolhe a opção errada. Qual correção atua primeiro sobre a causa?

A. Aumentar Max Iterations.  
B. Tornar nomes e descrições inequívocos.  
C. Adicionar memória.  
D. Publicar sem autenticação.  
**Gabarito e feedback:** correta B. Acerto: “O modelo usa nome, descrição e esquema para decidir.” Erro: “A causa está na forma como as capacidades foram apresentadas ao modelo.”

> » IA: BLOCO RISE 360 - Knowledge Check - Multiple Choice. Criar cenário de aplicação. Não publicar esta linha.

BLOCO RISE 360  
Knowledge Check - Multiple Choice

**Título visível:** Aplicação conceitual  
**Configuração:** uma resposta; nova tentativa habilitada.  
**Conteúdo visível:** Um agente de atendimento deve consultar uma base e registrar solicitações somente após confirmação. Qual combinação é mais adequada?

A. Uma tool genérica com acesso total.  
B. Duas tools descritas separadamente e regras explícitas de confirmação.  
C. Apenas uma System Message longa, sem limitar permissões.  
D. Memória fixa compartilhada por todos.  
**Gabarito e feedback:** correta B. Acerto: “Separar consulta e ação torna a decisão mais clara e permite controles diferentes.” Erro: “Procure a arquitetura que diferencia capacidades e limita a ação sensível.”

> » IA: ▲▲▲ FIM DA LIÇÃO - "Módulo 2 - Como o agente decide e age" - encerrar esta lição aqui. Não publicar este marcador. ▲▲▲

# Módulo 3 - Memória, conhecimento e RAG

## Ficha de produção da lição

- Objetivo: distinguir histórico de sessão e recuperação de documentos.
- Resultado observável: o participante escolhe a combinação correta para conversa e manual.

| Etapa | Conteúdo | Bloco Rise 360 |
|---|---|---|
| Abertura | Dois tipos de contexto | Cover |
| Comparação | Memória e RAG | Tabs |
| Sessão | Chave e janela | Text + Statement |
| Ingestão | Etapas do RAG | Process |
| Verificação | Contextos combinados | Knowledge Check |
| Aplicação | Ordem da ingestão | Sorting Activity |

> A ficha orienta a produção e não deve aparecer no curso publicado.

> » IA: ▼▼▼ INÍCIO DA LIÇÃO - "Módulo 3 - Memória, conhecimento e RAG" - todo o conteúdo até o marcador de fim corresponde a UMA única lição no Rise 360; não dividir, duplicar, fundir ou criar sublições. Não publicar este marcador. ▼▼▼

> » IA: BLOCO RISE 360 - Cover. Criar abertura sem imagem. Não publicar esta linha.

BLOCO RISE 360  
Cover

**Título visível:** Memória, conhecimento e RAG  
**Configuração:** fundo sólido; alto contraste.  
**Conteúdo visível:** Uma conversa anterior e um documento externo fornecem contextos diferentes.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Tabs. Comparar dois recursos. Não publicar esta linha.

BLOCO RISE 360  
Tabs

**Título visível:** Dois tipos de contexto  
**Configuração:** duas abas.  
**Conteúdo visível:**

- **Memória:** preserva interações de uma sessão para manter continuidade. Não transforma documentos em base pesquisável.
- **RAG:** recupera trechos de fontes externas antes da resposta. Não substitui o histórico da conversa.

**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Text. Explicar Simple Memory. Não publicar esta linha.

BLOCO RISE 360  
Text

**Título visível:** Sessões separadas  
**Configuração:** dois parágrafos curtos.  
**Conteúdo visível:** Simple Memory associa o histórico a uma Session Key. Essa chave precisa distinguir usuários ou conversas; uma chave compartilhada pode misturar contextos.

Context Window Length define quantas interações anteriores entram no contexto. Em queue mode, recomenda-se memória persistente, como Postgres ou Redis.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Statement. Destacar a regra. Não publicar esta linha.

BLOCO RISE 360  
Statement

**Título visível:** Regra de isolamento  
**Configuração:** estilo de alerta.  
**Conteúdo visível:** Uma Session Key compartilhada pode expor o contexto de outra conversa.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Process. Mostrar as quatro etapas de ingestão. Não publicar esta linha.

BLOCO RISE 360  
Process

**Título visível:** Como uma fonte entra no RAG  
**Configuração:** quatro etapas numeradas.  
**Conteúdo visível:**

1. **Carregar:** obter o documento autorizado.
2. **Dividir:** criar chunks menores para recuperação.
3. **Representar:** gerar embeddings que aproximam significados.
4. **Armazenar:** guardar embeddings e metadata no vector store.

**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Knowledge Check - Multiple Choice. Permitir nova tentativa. Não publicar esta linha.

BLOCO RISE 360  
Knowledge Check - Multiple Choice

**Título visível:** Verificação formativa  
**Configuração:** uma resposta; nova tentativa habilitada.  
**Conteúdo visível:** O agente deve lembrar um código da mensagem anterior e responder com base em um manual. Qual combinação é adequada?

A. Apenas memória.  
B. Apenas vector store.  
C. Memória para o histórico e RAG para o manual.  
D. Output parser para ambos.  
**Gabarito e feedback:** correta C. Acerto: “Histórico e fonte externa são contextos complementares.” Erro: “Separe o que pertence à conversa do que pertence ao documento.”

> » IA: BLOCO RISE 360 - Sorting Activity. Ordenar a ingestão em quatro posições. Não publicar esta linha.

BLOCO RISE 360  
Sorting Activity

**Título visível:** Organize a ingestão  
**Configuração:** atividade de ordenação; nova tentativa.  
**Conteúdo visível:** Coloque as etapas na ordem correta: armazenar no vector store; carregar o documento; gerar embeddings; dividir em chunks.  
**Gabarito e feedback:** carregar → dividir → gerar embeddings → armazenar. Feedback: “A fonte precisa ser preparada e representada antes de ser armazenada para consulta.”

> » IA: ▲▲▲ FIM DA LIÇÃO - "Módulo 3 - Memória, conhecimento e RAG" - encerrar esta lição aqui. Não publicar este marcador. ▲▲▲

# Módulo 4 - Segurança, controle e qualidade

## Ficha de produção da lição

- Objetivo: selecionar controles para entradas, ferramentas e resultados.
- Resultado observável: o participante reduz o impacto de uma tool excessivamente permissiva.

| Etapa | Conteúdo | Bloco Rise 360 |
|---|---|---|
| Abertura | Capacidade e risco | Cover |
| Ameaças | Injection e agência | Accordion |
| Controles | Camadas | Process |
| Evidência | Executions e avaliações | Text + Statement |
| Verificação | Menor privilégio | Knowledge Check |
| Aplicação | Ataque adversarial | Knowledge Check |

> A ficha orienta a produção e não deve aparecer no curso publicado.

> » IA: ▼▼▼ INÍCIO DA LIÇÃO - "Módulo 4 - Segurança, controle e qualidade" - todo o conteúdo até o marcador de fim corresponde a UMA única lição no Rise 360; não dividir, duplicar, fundir ou criar sublições. Não publicar este marcador. ▼▼▼

> » IA: BLOCO RISE 360 - Cover. Criar abertura sem imagem. Não publicar esta linha.

BLOCO RISE 360  
Cover

**Título visível:** Segurança, controle e qualidade  
**Configuração:** fundo sólido; alto contraste.  
**Conteúdo visível:** Quanto maior a capacidade de agir, maior a necessidade de limitar e verificar.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Accordion. Criar dois itens de ameaça. Não publicar esta linha.

BLOCO RISE 360  
Accordion

**Título visível:** O que pode dar errado  
**Configuração:** dois itens.  
**Conteúdo visível:**

- **Prompt injection:** uma mensagem ou documento tenta substituir as regras do agente. Pode ocorrer diretamente ou por conteúdo recuperado.
- **Excesso de agência:** a tool possui permissões maiores que a tarefa. Uma decisão incorreta passa a produzir impacto desnecessário.

**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Process. Apresentar controles em quatro camadas. Não publicar esta linha.

BLOCO RISE 360  
Process

**Título visível:** Controles em camadas  
**Configuração:** quatro etapas.  
**Conteúdo visível:**

1. **Validar a entrada:** bloquear ou sanitizar jailbreaks, segredos e dados indevidos.
2. **Limitar a capacidade:** aplicar menor privilégio a tools e credenciais.
3. **Aprovar a ação:** pausar operações sensíveis para revisão humana.
4. **Verificar o resultado:** inspecionar Executions e executar casos de avaliação.

**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Text. Explicar evidências. Não publicar esta linha.

BLOCO RISE 360  
Text

**Título visível:** Funcionou, mas está correto?  
**Configuração:** dois parágrafos.  
**Conteúdo visível:** Executions mostra entradas, saídas e chamadas de tool. Uma execução concluída comprova apenas que o workflow terminou sem erro técnico.

Qualidade exige casos de teste com resultados esperados. Ações repetíveis também precisam considerar idempotência, pois um retry pode duplicar gravações.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Statement. Destacar a distinção. Não publicar esta linha.

BLOCO RISE 360  
Statement

**Título visível:** Evidência  
**Configuração:** estilo informativo.  
**Conteúdo visível:** Execução concluída não prova qualidade, segurança ou correção.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Knowledge Check - Multiple Choice. Permitir nova tentativa. Não publicar esta linha.

BLOCO RISE 360  
Knowledge Check - Multiple Choice

**Título visível:** Verificação formativa  
**Configuração:** uma resposta; nova tentativa.  
**Conteúdo visível:** Um agente pode ler uma planilha e apagar linhas. Qual mudança reduz mais diretamente o impacto potencial?

A. Aumentar a janela de memória.  
B. Remover exclusão e exigir aprovação para escrita.  
C. Publicar com autenticação None.  
D. Aumentar Max Iterations.  
**Gabarito e feedback:** correta B. Acerto: “Menor privilégio reduz a capacidade de dano; aprovação controla a ação sensível.” Erro: “Procure o controle que limita diretamente a permissão da tool.”

> » IA: BLOCO RISE 360 - Knowledge Check - Multiple Choice. Criar cenário adversarial. Não publicar esta linha.

BLOCO RISE 360  
Knowledge Check - Multiple Choice

**Título visível:** Aplicação conceitual  
**Configuração:** uma resposta; nova tentativa.  
**Conteúdo visível:** O usuário pede para ignorar regras, revelar credenciais e apagar dados. Qual conjunto de evidências indica o comportamento mais seguro?

A. Recusa textual, mas chamada à tool de exclusão.  
B. Bloqueio ou recusa, nenhuma tool sensível e registro em Executions.  
C. Resposta longa com parte das credenciais.  
D. Nova tentativa automática até a exclusão funcionar.  
**Gabarito e feedback:** correta B. Acerto: “A segurança precisa aparecer no resultado e na ausência de ação sensível.” Erro: “A recusa só é efetiva quando nenhuma capacidade indevida é acionada.”

> » IA: ▲▲▲ FIM DA LIÇÃO - "Módulo 4 - Segurança, controle e qualidade" - encerrar esta lição aqui. Não publicar este marcador. ▲▲▲

# Módulo 5 - Síntese e aplicação integrada

## Ficha de produção da lição

- Objetivo: avaliar uma arquitetura completa e justificar melhorias.
- Resultado observável: o participante seleciona o conjunto de controles necessário para publicação.

| Etapa | Conteúdo | Bloco Rise 360 |
|---|---|---|
| Abertura | Arquitetura ponta a ponta | Cover |
| Método | Sete decisões | Process |
| Síntese | Componentes por necessidade | List |
| Verificação | Evidência de liberação | Knowledge Check |
| Integração | Cenário completo | Sorting Activity |
| Encerramento | Princípio final | Statement + Text |

> A ficha orienta a produção e não deve aparecer no curso publicado.

> » IA: ▼▼▼ INÍCIO DA LIÇÃO - "Módulo 5 - Síntese e aplicação integrada" - todo o conteúdo até o marcador de fim corresponde a UMA única lição no Rise 360; não dividir, duplicar, fundir ou criar sublições. Não publicar este marcador. ▼▼▼

> » IA: BLOCO RISE 360 - Cover. Criar abertura sem imagem. Não publicar esta linha.

BLOCO RISE 360  
Cover

**Título visível:** Síntese e aplicação integrada  
**Configuração:** fundo sólido; alto contraste.  
**Conteúdo visível:** Um agente confiável nasce de decisões explícitas sobre problema, capacidade, contexto, controle e evidência.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Process. Criar sete etapas concisas. Não publicar esta linha.

BLOCO RISE 360  
Process

**Título visível:** Sete decisões de arquitetura  
**Configuração:** sete etapas numeradas.  
**Conteúdo visível:**

1. **Definir o problema:** confirmar se existe decisão contextual.
2. **Delimitar a entrada:** identificar origem, autenticação e dados permitidos.
3. **Escolher o contexto:** separar memória de fontes externas.
4. **Limitar as tools:** oferecer apenas capacidades necessárias.
5. **Controlar a saída:** validar estrutura e conteúdo.
6. **Aprovar o risco:** pausar ações sensíveis.
7. **Reunir evidências:** testar e revisar Executions.

**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - List. Resumir componentes condicionais. Não publicar esta linha.

BLOCO RISE 360  
List

**Título visível:** Acrescente somente quando necessário  
**Configuração:** lista com marcadores.  
**Conteúdo visível:**

- Memória, quando a sessão precisa de continuidade.
- RAG, quando a resposta depende de documentos autorizados.
- Parser, quando sistemas posteriores exigem estrutura previsível.
- Guardrails, quando entradas e saídas precisam de filtro adicional.
- Human review, quando uma tool pode produzir impacto relevante.

**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Knowledge Check - Multiple Choice. Permitir nova tentativa. Não publicar esta linha.

BLOCO RISE 360  
Knowledge Check - Multiple Choice

**Título visível:** Verificação formativa  
**Configuração:** uma resposta; nova tentativa.  
**Conteúdo visível:** Qual evidência é mais forte para liberar um agente que registra solicitações?

A. Uma resposta bem escrita.  
B. Workflow ativo e sem erro visual.  
C. Casos normais e adversariais, sessões separadas e revisão de Executions.  
D. Mensagem de sistema longa.  
**Gabarito e feedback:** correta C. Acerto: “A liberação exige evidências de função, segurança e isolamento.” Erro: “Fluência e ausência de erro técnico não cobrem os principais riscos.”

> » IA: BLOCO RISE 360 - Sorting Activity. Classificar sete decisões em três categorias. Não publicar esta linha.

BLOCO RISE 360  
Sorting Activity

**Título visível:** Corrija a arquitetura  
**Configuração:** três categorias; nova tentativa.  
**Conteúdo visível:** Um chat consulta um manual e grava pedidos. Classifique as melhorias.

Categorias: Contexto; Capacidade e acesso; Evidência.

Itens:

- Usar Session Key exclusiva.
- Manter RAG para o manual.
- Restringir a tool à gravação necessária.
- Exigir confirmação e human review.
- Configurar autenticação adequada.
- Testar prompt injection e retry.
- Revisar Executions e avaliações.

**Gabarito e feedback:** Contexto → Session Key e RAG; Capacidade e acesso → restrição da tool, confirmação/review e autenticação; Evidência → testes e revisão. Feedback: “A arquitetura confiável trata separadamente contexto, permissão e comprovação.”

> » IA: BLOCO RISE 360 - Statement. Exibir a síntese final. Não publicar esta linha.

BLOCO RISE 360  
Statement

**Título visível:** Síntese  
**Configuração:** estilo de conclusão.  
**Conteúdo visível:** Capacidade limitada, contexto autorizado e evidência verificável sustentam um agente confiável.  
**Gabarito e feedback:** não se aplica.

> » IA: BLOCO RISE 360 - Text. Encerrar e indicar aprofundamento. Não publicar esta linha.

BLOCO RISE 360  
Text

**Título visível:** Próximos passos  
**Configuração:** dois parágrafos curtos.  
**Conteúdo visível:** A arquitetura deve ser revalidada quando mudarem modelo, ferramentas, fontes, permissões ou público. Controles proporcionais preservam a utilidade sem ampliar o risco desnecessariamente.

O aprofundamento pode incluir avaliações por métricas, memória persistente e monitoramento de custo, falhas e qualidade.  
**Gabarito e feedback:** não se aplica.

> » IA: ▲▲▲ FIM DA LIÇÃO - "Módulo 5 - Síntese e aplicação integrada" - encerrar esta lição aqui. Não publicar este marcador. ▲▲▲

# Orientações gerais de produção no Rise 360

- Manter exatamente cinco lições.
- Usar títulos internos como seções, sem criar sublições.
- Remover marcadores, fichas e instruções dirigidas à IA antes da publicação.
- Não adicionar conteúdo externo, links ou mídia.
- Configurar Knowledge Checks como formativos e permitir novas tentativas.
- Manter contraste, hierarquia de títulos e nomes descritivos para controles.
- Não comunicar informação apenas por cor.
- Revisar em computador e celular.
- Conferir ortografia, consistência, gabaritos, feedbacks e acessibilidade.

# Pendências de validação

- Confirmar os rótulos da interface n8n 2.46.6 na conta usada para publicação.
- Revalidar recursos em preview, planos e limites na semana da publicação.

