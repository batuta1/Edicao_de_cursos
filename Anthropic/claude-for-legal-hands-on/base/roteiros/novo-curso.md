<link rel="stylesheet" href="../.css/style.css">

# Relatório de Roteiro de Curso
## "Claude for Legal – ecossistema para o setor jurídico" (versão revisada e detalhada)

> **Base desta reconstrução:** `ANALISE_CRITICA_CLAUDE.md` — todas as correções de criticidade P0 e P1 foram incorporadas: disponibilidade por plano, distinção entre simulação no chat e integração real, permissões de conectores MCP, limites do Microsoft 365, escopo real de auditoria (Enterprise), tratamento de LGPD/sigilo profissional e prática observável (não apenas conceitual) em cada aula.
> **Público-alvo:** estudantes de Direito e profissionais em início de carreira, com foco em aplicação prática: análise contratual, peças processuais, jurimetria, automação e conformidade/LGPD.
> **Legenda de disponibilidade** (aplicada a cada aula quando pertinente): 🟢 Todos os planos · 🟡 Plano pago · 🔴 Admin/Enterprise necessário · 🧪 Beta/Prévia de pesquisa · 💭 Simulação conceitual (sem recurso real correspondente)

---

## Módulo 1 — Fundamentos Seguros: Primeiro Acesso e Prompting Jurídico Responsável

### Aula 1.1 — Mapeando o ecossistema: onde o Claude realmente aparece no seu fluxo de trabalho

- **Subseções da Aula:**
  - Diferenças entre Claude Web, Claude Desktop, aplicativo mobile, Projects e Claude Cowork
  - Matriz "Plano × Superfície × Recurso": o que está disponível em Free, Pro, Team e Enterprise
  - Como identificar se um recurso precisa de habilitação administrativa antes de tentar usá-lo

- **Sugestão de Breadcrumb:**
  - Claude Web → Ícone de perfil → Configurações → Plano e cobrança (rótulos "Free/Pro/Team/Enterprise")
  - Claude Web → Configurações → Conta → Plano ativo da conta do aluno
  - Material do curso → Anexo → Tabela "Plano × Superfície × Recurso" (Projects, Cowork, conectores MCP)

- **Descrição:**
  - **Objetivos da Aula:** Mapear as superfícies do Claude disponíveis para o aluno e **identificar**, antes de qualquer prática, quais recursos exigem plano pago ou aprovação administrativa — evitando frustração por tentar reproduzir um passo indisponível na própria conta.
  - **Habilidades Esperadas:** Reconhecer o plano e a superfície em uso; localizar a documentação oficial de requisitos; diagnosticar corretamente "recurso ausente por plano" versus "erro de operação".

### Aula 1.2 — Prompting jurídico responsável: contexto, tarefa, restrição e formato

- **Subseções da Aula:**
  - Estrutura de prompt jurídico: contexto do caso, tarefa objetiva, restrições (jurisdição, formato, tom) e pedido explícito de incerteza
  - Por que pedir "cite as fontes e marque o que não tem certeza" reduz o risco de alucinação, sem eliminá-lo
  - Diferença entre pedir uma opinião jurídica e pedir uma organização/síntese de informação fornecida pelo próprio usuário

- **Sugestão de Breadcrumb:**
  - Claude Web → Nova conversa → Caixa de mensagem → Prompt "fraco" × Prompt "reestruturado" (comparação lado a lado)
  - Claude Web → Conversa ativa → Resposta gerada → Trecho sinalizado como "não verificado"

- **Descrição:**
  - **Objetivos da Aula:** Configurar prompts jurídicos com contexto, tarefa e restrições claras, e **exigir do modelo** a sinalização de incertezas como parte do resultado esperado.
  - **Habilidades Esperadas:** Redigir prompts estruturados replicáveis; reconhecer respostas com excesso de confiança aparente; aplicar o princípio de "nenhuma citação sem fonte confirmável".

### Aula 1.3 — Protocolo de verificação: da resposta da IA à fonte primária

- **Subseções da Aula:**
  - Ficha de verificação "Afirmação → Fonte → Trecho → Data → Revisão"
  - Fontes oficiais para conferência no Brasil (diários oficiais, tribunais, portais de legislação) versus bases internacionais mencionadas pelo modelo
  - Quando uma citação "plausível" não é o mesmo que uma citação real

- **Sugestão de Breadcrumb:**
  - Material do curso → Anexo → Ficha de verificação "Afirmação → Fonte → Trecho → Data → Revisão" (preenchida)
  - Fonte oficial (portal do tribunal/legislação) → Busca → Resultado comparado à citação do Claude

- **Descrição:**
  - **Objetivos da Aula:** Analisar criticamente uma resposta gerada pela IA, **mapeando** cada afirmação relevante à sua fonte primária antes de qualquer uso acadêmico ou profissional.
  - **Habilidades Esperadas:** Preencher a ficha de verificação de forma consistente; distinguir fonte primária de menção genérica; documentar a revisão humana como parte do entregável.

---

## Módulo 2 — Análise Contratual com IA: do Upload à Matriz de Riscos

### Aula 2.1 — Organizando contratos fictícios em um Project

- **Subseções da Aula:**
  - Diferença entre enviar um arquivo isolado no chat, adicionar conhecimento a um Project e usar uma extensão local de arquivos
  - Criação de um Project "Contratos — Estudo de Caso" e adição de dois ou três contratos fictícios (nunca dados reais de cliente)
  - Limites de contexto: por que o Project organiza informação, mas não garante recuperação perfeita de tudo que foi carregado

- **Sugestão de Breadcrumb:**
  - Claude Web → Projects → Novo Project → Nome "Contratos — Estudo de Caso" → Upload de arquivos
  - Claude Web → Projects → Contratos — Estudo de Caso → Painel lateral → Documentos anexados e conversas vinculadas

- **Descrição:**
  - **Objetivos da Aula:** Configurar um Project dedicado à análise contratual, **organizando** documentos fictícios de forma rastreável e sabendo reconhecer os limites de memória do recurso.
  - **Habilidades Esperadas:** Criar e nomear um Project; anexar múltiplos documentos; verificar, por amostragem, se uma resposta realmente usou o conteúdo de um arquivo específico.

### Aula 2.2 — Análise clausular e construção de matriz de riscos

- **Subseções da Aula:**
  - Prompt estruturado para revisão clausula-a-clausula (definição de termos, obrigações, penalidades, vigência)
  - Construção de uma matriz de risco com colunas obrigatórias: cláusula, risco identificado, gravidade, **evidência/trecho citado**, recomendação
  - Tratamento de contratos com cláusulas contraditórias ou incompletas entre os documentos comparados

- **Sugestão de Breadcrumb:**
  - Claude Web → Projects → Contratos — Estudo de Caso → Chat → Prompt de análise de risco → Resposta em tabela (coluna "Evidência" em destaque)
  - Claude Web → Chat → Resposta → Cláusulas conflitantes (Contrato A × Contrato B)

- **Descrição:**
  - **Objetivos da Aula:** Analisar cláusulas contratuais fictícias e **mapear** riscos jurídicos em uma matriz estruturada, exigindo evidência textual para cada apontamento.
  - **Habilidades Esperadas:** Redigir prompts de análise clausular; construir e interpretar uma matriz de risco; identificar contradições entre documentos e reportá-las de forma verificável.

### Aula 2.3 — Redlining real no Word com Claude for Microsoft 365 🟡🔴

- **Subseções da Aula:**
  - Pré-requisitos: plano pago do Claude, suplemento instalado (via Microsoft Marketplace ou implantado pelo administrador em contas Team/Enterprise) e documento aberto no Word
  - Diferença entre "reescrever um trecho no chat" (simulação) e o **redlining real**, com Controlar Alterações ativo e justificativa por cláusula
  - Limitações atuais: o suplemento não abre, cria ou alterna arquivos por conta própria; sessões não mantêm histórico entre uma abertura e outra do documento

- **Sugestão de Breadcrumb:**
  - Word → Suplementos → Claude for Microsoft 365 → Painel lateral aberto ao lado do documento
  - Word → Guia Revisão → Controlar Alterações (ativado) → Cláusula marcada (inserção/exclusão) + comentário do Claude

- **Descrição:**
  - **Objetivos da Aula:** Configurar e utilizar o suplemento do Claude for Microsoft 365 para **executar** um redlining real em um contrato de teste, com rastreabilidade de cada alteração.
  - **Habilidades Esperadas:** Verificar pré-requisitos de plano e instalação antes de iniciar; operar o suplemento dentro do Word; diferenciar formalmente redlining real de reescrita conversacional feita fora do documento.

> 💭 **Nota editorial obrigatória nesta aula:** caso o aluno não tenha o suplemento disponível (plano gratuito ou ausência de aprovação administrativa), a aula deve indicar explicitamente a alternativa: "Simulação no chat — não substitui o redlining real do Word" antes de qualquer exercício alternativo.

---

## Módulo 3 — Peças Processuais e Pesquisa Jurídica Verificável

### Aula 3.1 — Síntese de jurisprudência com rastreamento de fonte

- **Subseções da Aula:**
  - Prompt de pesquisa jurisprudencial exigindo tribunal, número do processo, data e trecho literal
  - Cruzamento obrigatório com fontes oficiais brasileiras (portais de tribunais, DJe, bases de jurisprudência reconhecidas)
  - Tratamento de segredo de justiça e dados pessoais sensíveis eventualmente presentes em decisões

- **Sugestão de Breadcrumb:**
  - Claude Web → Chat → Resposta → Lista de julgados hipotéticos → Coluna "verificar em fonte oficial" destacada
  - Portal do Tribunal → Busca por número do processo → Resultado comparado ao julgado citado

- **Descrição:**
  - **Objetivos da Aula:** Sintetizar jurisprudência com apoio da IA e **validar** cada julgado citado em fonte oficial brasileira antes de sua utilização em qualquer peça.
  - **Habilidades Esperadas:** Redigir prompts de pesquisa jurisprudencial; realizar a conferência cruzada em fonte primária; identificar quando um julgado está sob segredo de justiça e tratar a informação de forma adequada.

### Aula 3.2 — Estruturação assistida de peças processuais (petição inicial e contestação)

- **Subseções da Aula:**
  - Estrutura padrão de uma peça (endereçamento, qualificação, fatos, fundamentos, pedidos) e como pedir ao Claude apoio em cada seção separadamente
  - Uso de um Project de "caso fictício" para manter fatos e fundamentos consistentes entre petição e contestação
  - Prevenção de "alucinação de fundamento": exigir que cada tese jurídica citada venha acompanhada da base legal ou doutrinária correspondente

- **Sugestão de Breadcrumb:**
  - Claude Web → Projects → Caso Fictício → Chat → Rascunho de petição (seções numeradas: Fatos, Fundamentos, Pedidos)
  - Claude Web → Projects → Caso Fictício → Petição × Contestação (comparação lado a lado, consistência factual)

- **Descrição:**
  - **Objetivos da Aula:** Estruturar minutas de peças processuais fictícias com apoio da IA, **automatizando** a organização textual sem delegar a estratégia jurídica ao modelo.
  - **Habilidades Esperadas:** Construir uma minuta seção por seção; manter consistência factual entre peças de um mesmo Project; identificar fundamentos jurídicos que precisam de verificação antes do protocolo.

### Aula 3.3 — Revisão humana e registro de responsabilidade profissional

- **Subseções da Aula:**
  - Checklist de revisão antes de qualquer peça ou parecer seguir para protocolo ou entrega
  - Como registrar, no próprio fluxo de trabalho, quem revisou, o que foi alterado e com base em qual fonte
  - Diferença entre apoio de pesquisa sob supervisão e substituição do julgamento profissional (vedada em qualquer hipótese)

- **Sugestão de Breadcrumb:**
  - Material do curso → Modelo → "Carimbo de revisão" (revisor, data, fontes conferidas)
  - Material do curso → Checklist de revisão humana → Aula 3.2 (preenchido)

- **Descrição:**
  - **Objetivos da Aula:** Aplicar um protocolo formal de revisão humana a todo conteúdo jurídico produzido com apoio de IA, **documentando** a responsabilidade profissional sobre o resultado final.
  - **Habilidades Esperadas:** Preencher um checklist de revisão; registrar a cadeia de verificação de um documento; justificar, em linguagem profissional, por que a revisão humana é etapa obrigatória e não opcional.

---

## Módulo 4 — Jurimetria e Análise de Dados Jurídicos

### Aula 4.1 — Introdução à jurimetria com apoio de IA

- **Subseções da Aula:**
  - O que é jurimetria e que tipos de pergunta ela responde (tempo médio de processo, taxa de sucesso por tese, distribuição por vara/tribunal)
  - Diferença entre pedir uma "opinião" sobre tendência jurisprudencial e pedir uma **análise de dados fornecidos** pelo próprio aluno
  - Preparação de uma planilha fictícia simples (número do caso, tribunal, resultado, duração) para uso nas aulas seguintes

- **Sugestão de Breadcrumb:**
  - Excel/Google Sheets → Planilha "Processos" → Colunas padronizadas (caso, tribunal, resultado, duração)
  - Claude Web → Chat → Planilha anexada → Prompt de resumo estatístico descritivo

- **Descrição:**
  - **Objetivos da Aula:** Analisar um conjunto de dados jurídicos fictício, **distinguindo** claramente estatística descritiva (baseada nos dados fornecidos) de inferência ou opinião não fundamentada do modelo.
  - **Habilidades Esperadas:** Preparar uma base de dados jurídica minimamente estruturada; formular perguntas analíticas objetivas; reconhecer quando uma resposta extrapola os dados fornecidos.

### Aula 4.2 — Upload de planilhas e geração de tabelas analíticas

- **Subseções da Aula:**
  - Upload da planilha fictícia diretamente no chat ou dentro de um Project de jurimetria
  - Prompt para gerar tabela cruzada (ex.: resultado por tribunal, duração média por tipo de ação)
  - Verificação manual de uma amostra dos cálculos gerados antes de confiar no resultado completo

- **Sugestão de Breadcrumb:**
  - Claude Web → Chat → Anexo → Planilha fictícia → Resposta → Artifact de tabela cruzada
  - Material do curso → Verificação manual → Linha da tabela × Planilha original (comparação)

- **Descrição:**
  - **Objetivos da Aula:** Automatizar a geração de tabelas analíticas a partir de dados jurídicos fictícios, **verificando** por amostragem a exatidão dos cálculos apresentados.
  - **Habilidades Esperadas:** Anexar corretamente uma planilha; interpretar uma tabela cruzada gerada pela IA; realizar conferência manual de amostra antes de aceitar o resultado como válido.

### Aula 4.3 — Visualização de dados e relatório executivo de jurimetria

- **Subseções da Aula:**
  - Solicitação de gráfico (Artifact) a partir da tabela analítica da Aula 4.2
  - Boas práticas de relatório executivo: título, achados principais, limitações da amostra e fonte dos dados
  - Discussão crítica: o que a jurimetria pode e não pode prever com uma amostra fictícia pequena

- **Sugestão de Breadcrumb:**
  - Claude Web → Chat → Resposta → Artifact de gráfico (barras/linha) → Dados jurídicos fictícios
  - Material do curso → Relatório executivo (texto ou slide) → Seção "Limitações da análise"

- **Descrição:**
  - **Objetivos da Aula:** Produzir um relatório executivo de jurimetria com visualização de dados, **automatizando** a apresentação, mas **explicitando** as limitações estatísticas da amostra utilizada.
  - **Habilidades Esperadas:** Gerar e interpretar visualizações de dados jurídicos; redigir um relatório executivo com seção de limitações; comunicar achados de jurimetria de forma tecnicamente honesta.

---

## Módulo 5 — Automação de Rotinas Jurídicas: MCP, Cowork e Plugins

### Aula 5.1 — Entendendo MCP: conectores, permissões e o princípio do menor privilégio

- **Subseções da Aula:**
  - Arquitetura MCP em linguagem visual: cliente (Claude), servidor (o sistema conectado), ferramenta (a ação disponível) e fonte de dados
  - Conectores remotos (operados a partir da infraestrutura da Anthropic) versus extensões locais (rodando na máquina do usuário)
  - Leitura versus escrita: por que todo conector deve ser avaliado por "o que ele pode ler" e "o que ele pode alterar", nunca assumido como acesso "universal"

- **Sugestão de Breadcrumb:**
  - Material do curso → Diagrama → Cliente (Claude) → Servidor MCP → Sistema jurídico (fluxo de dados)
  - Claude Web → Configurações → Conectores → Painel de permissões concedidas (leitura/escrita, escopo)

- **Descrição:**
  - **Objetivos da Aula:** Mapear a arquitetura de um conector MCP e **avaliar**, antes de qualquer conexão, o escopo de leitura/escrita e a origem (remota ou local) do conector.
  - **Habilidades Esperadas:** Explicar o fluxo cliente-servidor-ferramenta de um conector MCP; identificar se um conector é de leitura, escrita ou ambos; aplicar o princípio do menor privilégio ao conceder permissões.

### Aula 5.2 — Laboratório seguro de conector MCP com fonte não sensível

- **Subseções da Aula:**
  - Escolha de um conector de baixo risco (ex.: uma base de jurisprudência pública) para o primeiro laboratório
  - Passo a passo: conectar, consultar, confirmar a origem da resposta e desconectar ao final
  - Reconhecimento de riscos de conectores de terceiros e de conteúdo externo manipulado (prompt injection)

- **Sugestão de Breadcrumb:**
  - Claude Web → Configurações → Conectores → Conectar novo conector → Tela de autorização (consentimento/OAuth)
  - Claude Web → Chat → Resposta → Origem do conector identificada explicitamente

- **Descrição:**
  - **Objetivos da Aula:** Configurar um conector MCP de baixo risco em ambiente controlado e **executar** um ciclo completo de conexão, consulta, verificação de origem e desconexão.
  - **Habilidades Esperadas:** Conceder e revogar permissões de um conector; confirmar a origem de uma informação retornada via MCP; reconhecer sinais de conteúdo externo potencialmente manipulado.

### Aula 5.3 — Claude Cowork para tarefas jurídicas multi-documento 🟡🧪

- **Subseções da Aula:**
  - Quando usar o chat comum e quando usar Cowork: complexidade da tarefa, volume de documentos e necessidade de supervisão
  - Requisitos: plano pago, consumo de uso superior ao chat, modos local/remoto e etapas de aprovação antes de ações sensíveis
  - Estrutura de uma tarefa Cowork com checkpoints: plano de execução, amostra revisada, execução completa, revisão final

- **Sugestão de Breadcrumb:**
  - Claude Cowork → Nova tarefa → Descrição da tarefa + lista de documentos-fonte
  - Claude Cowork → Tarefa em execução → Checkpoint intermediário → Aprovação humana pendente

- **Descrição:**
  - **Objetivos da Aula:** Delegar uma tarefa jurídica multi-documento fictícia ao Claude Cowork, **automatizando** etapas repetitivas sem eliminar pontos de aprovação humana.
  - **Habilidades Esperadas:** Estruturar uma tarefa Cowork com checkpoints claros; revisar uma amostra antes da execução completa; identificar quando uma tarefa depende de recursos locais versus remotos.

### Aula 5.4 — Plugins e playbooks: empacotando o padrão do escritório, sem substituir expertise

- **Subseções da Aula:**
  - Diferença entre plugin, skill, conector e um simples prompt salvo
  - Como um playbook traduz política jurídica interna (tolerância a risco, estilo, escalonamento) em critérios que o Claude pode seguir de forma consistente
  - Teste de qualidade de um playbook com casos fictícios e conjunto de resultados esperados

- **Sugestão de Breadcrumb:**
  - Claude Web → Plugins → Plugin Jurídico → Entrevista de configuração (playbook, escalonamento, estilo)
  - Claude Web → Chat → Resposta com plugin ativado × Resposta sem plugin (mesmo contrato fictício)

- **Descrição:**
  - **Objetivos da Aula:** Configurar um plugin jurídico com um playbook de teste e **automatizar** a aplicação consistente de critérios predefinidos a múltiplos documentos fictícios.
  - **Habilidades Esperadas:** Diferenciar plugin, skill e conector; parametrizar um playbook simples; validar a consistência de um plugin com um conjunto de casos de teste antes de qualquer uso real.

---

## Módulo 6 — Conformidade, LGPD e Segurança de Dados no Uso Jurídico da IA

### Aula 6.1 — Classificação de dados: o que pode e o que não pode ser inserido no Claude

- **Subseções da Aula:**
  - Categorias de dados sensíveis no contexto jurídico brasileiro: dados pessoais (LGPD), dados pessoais sensíveis, segredo de justiça e sigilo profissional
  - Checklist "Posso inserir este dado?" antes de qualquer upload ou colagem de conteúdo real
  - Técnicas de anonimização e pseudonimização para uso de casos reais em contexto de estudo

- **Sugestão de Breadcrumb:**
  - Material do curso → Checklist "Posso inserir este dado?" → Cenário permitido × Cenário vedado
  - Material do curso → Documento fictício → Antes/Depois da anonimização

- **Descrição:**
  - **Objetivos da Aula:** Classificar dados jurídicos quanto à sensibilidade e **decidir**, com base em critério explícito, se determinada informação pode ser inserida em uma ferramenta de IA.
  - **Habilidades Esperadas:** Aplicar o checklist de classificação de dados; realizar anonimização básica de um documento; justificar formalmente a decisão de uso ou não uso de um dado real.

### Aula 6.2 — Governança: planos, retenção, permissões e o real alcance dos logs de auditoria

- **Subseções da Aula:**
  - Tratamento de dados por tipo de conta: em contas de consumo (Free/Pro/Max) o usuário controla o uso de conversas para melhoria do produto; em produtos comerciais, entradas e saídas não são usadas para treinamento por padrão, salvo hipóteses específicas (ex.: feedback explícito)
  - Logs de auditoria são recurso disponível apenas em organizações **Enterprise** — não em Team — e não substituem a documentação jurídica da revisão humana
  - Papéis de governança: usuário, supervisor jurídico, TI, segurança/privacidade e proprietário do processo

- **Sugestão de Breadcrumb:**
  - Claude Web → Configurações → Privacidade → Uso de conversas para melhoria do produto (conta de consumo)
  - Material do curso → Tabela "Plano × Governança" (Free/Pro/Max/Team/Enterprise) → Logs de auditoria (presença/ausência)

- **Descrição:**
  - **Objetivos da Aula:** Mapear corretamente o regime de tratamento de dados por tipo de plano e **corrigir** a premissa comum de que "não treinar com os dados" equivale a "qualquer dado pode ser inserido".
  - **Habilidades Esperadas:** Explicar a diferença de tratamento de dados entre planos de consumo e comerciais; identificar corretamente em qual plano os logs de auditoria estão disponíveis; atribuir papéis de governança a um fluxo de trabalho jurídico simulado.

### Aula 6.3 — Simulação de incidente e resposta: quando algo sai do combinado

- **Subseções da Aula:**
  - Cenário fictício: um dado sensível foi inserido por engano em uma sessão sem as permissões adequadas
  - Etapas de resposta a incidente: identificar, conter, documentar, comunicar e revisar o processo
  - Revisão trimestral de catálogo de plugins/conectores, planos e recursos em beta como prática de governança contínua

- **Sugestão de Breadcrumb:**
  - Material do curso → Fluxograma → Identificar → Conter → Documentar → Comunicar → Revisar
  - Material do curso → Modelo de relatório de incidente (preenchido, cenário fictício)

- **Descrição:**
  - **Objetivos da Aula:** Simular a resposta a um incidente de uso inadequado de dados em ferramenta de IA jurídica, **documentando** cada etapa do processo de contenção e revisão.
  - **Habilidades Esperadas:** Aplicar um fluxo estruturado de resposta a incidente; redigir um relatório de incidente completo; propor uma revisão periódica de governança para um fluxo de trabalho jurídico com IA.

---

## Módulo 7 — Legal Operations Avançado: Automação em Lote e Caminho para Produção (Trilha Opcional)

### Aula 7.1 — Introdução não técnica a Claude Code para operações jurídicas

- **Subseções da Aula:**
  - O que é Claude Code e por que ele é relevante para operações jurídicas em escala (auditoria de contratos em lote, extração estruturada de cláusulas)
  - Diferença entre um protótipo acadêmico feito no chat e um script reprodutível revisado por equipe técnica
  - Quando vale a pena migrar uma rotina do chat para uma automação de código

- **Sugestão de Breadcrumb:**
  - Claude Code → Editor → Script de extração de cláusulas → Múltiplos arquivos fictícios
  - Material do curso → Comparativo → Prompt manual (50×) × Script (1× sobre 50 arquivos)

- **Descrição:**
  - **Objetivos da Aula:** Compreender, em linguagem não técnica, o papel do Claude Code em rotinas jurídicas repetitivas e **mapear** quando uma tarefa deixou de ser adequada para o chat manual.
  - **Habilidades Esperadas:** Explicar a diferença entre uso conversacional e automação reprodutível; identificar candidatos válidos à automação em lote; dialogar com uma equipe técnica sobre requisitos jurídicos do script.

### Aula 7.2 — Extração estruturada de cláusulas em lote (estudo de caso fictício)

- **Subseções da Aula:**
  - Definição de um esquema estruturado de extração (ex.: partes, vigência, multa, foro) aplicável a múltiplos contratos fictícios
  - Validação do esquema com testes e registro de exceções (contratos que não seguem o padrão esperado)
  - Auditoria dos resultados: amostragem manual para conferir a extração automática

- **Sugestão de Breadcrumb:**
  - Material do curso → Tabela de esquema estruturado (schema) → Campos definidos para extração
  - Material do curso → Planilha de saída → Dados extraídos + coluna "Exceções"

- **Descrição:**
  - **Objetivos da Aula:** Automatizar a extração estruturada de cláusulas de um lote de contratos fictícios, **validando** o esquema utilizado e registrando exceções encontradas.
  - **Habilidades Esperadas:** Definir um esquema de extração estruturada; executar e auditar por amostragem uma extração em lote; registrar e tratar exceções de forma documentada.

### Aula 7.3 — Do protótipo acadêmico ao piloto corporativo controlado

- **Subseções da Aula:**
  - Critérios para transformar um exercício de sala de aula em um piloto real: dados aprovados, escopo limitado, métricas de sucesso
  - Métricas de avaliação de um piloto: precisão, tempo economizado, taxa de correção humana e incidentes de citação
  - Avaliação de fornecedor: DPA, retenção, residência de dados, subprocessadores e resposta a incidentes, antes de qualquer adoção institucional

- **Sugestão de Breadcrumb:**
  - Material do curso → "Ficha de piloto" → Escopo, métricas e critérios de sucesso (cenário fictício)
  - Material do curso → Checklist de avaliação de fornecedor → DPA, retenção, subprocessadores

- **Descrição:**
  - **Objetivos da Aula:** Estruturar a transição de um protótipo acadêmico para um piloto corporativo controlado, **avaliando** métricas de sucesso e requisitos de conformidade do fornecedor.
  - **Habilidades Esperadas:** Elaborar uma ficha de piloto com escopo e métricas; aplicar um checklist básico de avaliação de fornecedor; justificar a diferença de rigor exigido entre um exercício acadêmico e uma adoção institucional.

---

## Quadro-Síntese de Encerramento

| Módulo | Foco prático | Competência-chave consolidada |
|---|---|---|
| 1 | Fundamentos e prompting responsável | Verificar disponibilidade e fonte antes de confiar na resposta |
| 2 | Análise contratual | Construir matriz de risco com evidência obrigatória |
| 3 | Peças processuais e pesquisa jurídica | Validar jurisprudência em fonte oficial e documentar revisão humana |
| 4 | Jurimetria | Distinguir estatística descritiva de inferência não fundamentada |
| 5 | MCP, Cowork e Plugins | Aplicar o menor privilégio e manter pontos de aprovação humana |
| 6 | Conformidade e LGPD | Classificar dados e conhecer o real alcance da governança por plano |
| 7 (opcional) | Automação em lote e piloto corporativo | Migrar de protótipo para produção com métricas e avaliação de fornecedor |

> ✅ **Princípio transversal do curso:** nenhuma aula deste roteiro trata a saída do Claude como conclusão final. Toda aula prática termina em **verificação em fonte primária, documento fictício conferido ou checklist de revisão humana assinado** — nunca apenas na resposta gerada pelo modelo.

---

*Roteiro reconstruído a partir das correções e do roadmap propostos em `ANALISE_CRITICA_CLAUDE.md`, com foco em aplicação prática no setor jurídico brasileiro: análise contratual, peças processuais, jurimetria, automação (MCP/Cowork/Plugins) e conformidade/LGPD.*
