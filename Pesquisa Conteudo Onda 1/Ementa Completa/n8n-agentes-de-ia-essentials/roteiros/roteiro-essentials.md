# Plano de Aula — Agentes de IA no n8n (Essentials)

## Identificação

| Campo | Definição |
|---|---|
| Curso | Agentes de IA no n8n — Essentials |
| Natureza | Curto, introdutório, conceitual e autoinstrucional |
| Carga horária | 115 minutos |
| Público-alvo | Profissionais iniciantes em automação com IA |
| Pré-requisitos | Familiaridade básica com navegador; sem programação obrigatória |
| Recursos necessários | Apenas o ambiente do curso |
| Referência | Conteúdo bruto e documentação oficial reunidos em 05/11/2026 |

## Objetivo Geral

Compreender a arquitetura de um agente de IA no n8n e aplicar critérios de escolha, segurança, teste e governança a cenários de automação.

## Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. diferenciar workflow determinístico, modelo de linguagem e agente de IA;
2. relacionar os componentes de entrada, decisão, memória, conhecimento e ação;
3. selecionar controles proporcionais ao risco de cada ferramenta;
4. avaliar evidências de funcionamento, qualidade e segurança.

## Estrutura e Sequência dos Módulos

Os módulos avançam da definição do agente para a arquitetura, o contexto, os controles e a decisão integrada.

| Módulo | Título | Tempo |
|---|---|---:|
| 1 | Quando usar um agente | 23 min |
| 2 | Como o agente decide e age | 23 min |
| 3 | Memória, conhecimento e RAG | 23 min |
| 4 | Segurança, controle e qualidade | 23 min |
| 5 | Síntese e aplicação integrada | 23 min |

---

# Módulo 1 — Quando usar um agente

> Ponto de partida: distinguir decisão probabilística de sequência programada evita complexidade desnecessária.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

- definir workflow, modelo de linguagem e agente de IA;
- reconhecer tarefas apropriadas a cada abordagem;
- justificar quando um agente acrescenta valor.

### Texto Descritivo

Um workflow é uma sequência visual de nós que recebe dados, executa operações e entrega resultados. Quando as regras são conhecidas e estáveis, a automação determinística costuma ser a opção mais simples: cada condição conduz a uma ação previamente definida.

Um modelo de linguagem interpreta e produz texto, mas não atua sozinho sobre outros sistemas. Um agente combina o modelo com ferramentas. Diante de um objetivo, o modelo escolhe se deve responder diretamente ou chamar uma ferramenta, além de preencher os parâmetros exigidos por ela.

No n8n 2.46.6, o nó AI Agent trabalha segundo o padrão Tools Agent. A configuração antiga por tipo de agente foi descontinuada. O uso de agente é pertinente quando a tarefa contém variação linguística ou escolha contextual; não é necessário quando uma regra fixa resolve o problema com maior previsibilidade.

### Verificação Formativa

Uma equipe deve copiar diariamente os mesmos campos de uma tabela validada para outro sistema. Qual desenho é mais adequado?

A. Agente com várias ferramentas, porque toda automação deve usar IA.  
B. Workflow determinístico, porque as regras e os campos são conhecidos.  
C. Modelo de linguagem sem workflow, porque ele substitui integrações.  
D. RAG, porque toda transferência de dados exige documentos.

**Gabarito:** B.  
**Feedback:** A tarefa não exige interpretação contextual. Uma sequência fixa tende a ser mais simples, barata e auditável.

### Aplicação Conceitual

Classifique cada situação:

- enviar um aviso quando o prazo vencer: workflow determinístico;
- interpretar um pedido escrito livremente e escolher uma consulta: agente;
- redigir um resumo sem acessar sistemas: modelo de linguagem;
- buscar trechos de um manual antes de responder: agente com RAG.

---

# Módulo 2 — Como o agente decide e age

> O módulo anterior definiu o agente; agora o foco se desloca para os componentes que sustentam sua decisão.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

- relacionar Chat Trigger, Chat Model, AI Agent e tools;
- explicar o papel da mensagem de sistema e das descrições de ferramenta;
- reconhecer limites de iteração e formato como mecanismos de controle.

### Texto Descritivo

O Chat Trigger inicia uma execução quando uma mensagem chega. Em um chat hospedado ou incorporado, cada nova mensagem dispara uma execução do workflow. O AI Agent recebe a entrada, consulta o Chat Model e decide qual ferramenta usar. O modelo precisa oferecer tool calling, isto é, capacidade de selecionar uma função e produzir seus argumentos.

A mensagem de sistema define objetivo, fontes autorizadas, restrições e condições de uso das ferramentas. Ela orienta o comportamento, mas não constitui barreira de segurança. A descrição de cada tool também é decisiva: nome, finalidade e esquema informam ao modelo quando e como chamar a capacidade externa.

O limite Max Iterations reduz loops e custos; o padrão documentado é dez. O formato de saída pode ser controlado por parser estruturado. Esses recursos restringem a operação, mas não substituem permissões mínimas, validação e monitoramento.

### Verificação Formativa

Um agente possui duas tools com nomes vagos, “Ferramenta 1” e “Ferramenta 2”, e chama a opção errada. Qual correção atua primeiro sobre a causa?

A. Aumentar Max Iterations.  
B. Tornar nomes e descrições inequívocos.  
C. Adicionar memória.  
D. Publicar o chat sem autenticação.

**Gabarito:** B.  
**Feedback:** O modelo decide com base no nome, na descrição e no esquema de cada tool; rótulos vagos prejudicam a seleção.

### Aplicação Conceitual

Considere um agente de atendimento. A mensagem de sistema deve delimitar o assunto, exigir consulta à fonte e proibir ações não autorizadas. A tool de busca deve informar que retorna trechos da base. A tool de registro deve declarar que grava uma solicitação somente após confirmação. Essa combinação separa intenção, conhecimento e ação.

---

# Módulo 3 — Memória, conhecimento e RAG

> Depois da decisão e das ferramentas, examinam-se as duas formas de fornecer contexto: histórico da sessão e fontes externas.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

- distinguir memória de base de conhecimento;
- explicar Session Key e Context Window Length;
- ordenar as etapas de ingestão e consulta em RAG.

### Texto Descritivo

Memória e conhecimento resolvem problemas diferentes. A memória preserva partes da conversa para manter continuidade. A Simple Memory associa o histórico a uma Session Key e recupera uma quantidade definida de interações. Se a chave não separar usuários ou conversas, contextos podem ser misturados. Em queue mode, a documentação recomenda memória persistente, como Postgres ou Redis, em vez de Simple Memory.

RAG, sigla de geração aumentada por recuperação, permite consultar fontes externas antes da resposta. Na ingestão, um carregador obtém o documento, um divisor cria chunks, um modelo gera embeddings e um vector store armazena essas representações. Na consulta, o vector store localiza trechos semanticamente próximos e os oferece ao agente como contexto.

Memória não transforma um documento em fonte pesquisável, e RAG não substitui o histórico da conversa. Uma arquitetura pode usar ambos: memória para continuidade da sessão e RAG para respostas sustentadas por uma base autorizada.

### Verificação Formativa

O agente deve lembrar o número informado na mensagem anterior e também responder com base em um manual. Qual combinação é adequada?

A. Apenas Simple Memory.  
B. Apenas vector store.  
C. Memória para o histórico e RAG para o manual.  
D. Structured Output Parser para ambos.

**Gabarito:** C.  
**Feedback:** O histórico conversacional e a recuperação de documentos são contextos diferentes e complementares.

### Aplicação Conceitual

Ordene a ingestão de uma fonte: carregar o documento; dividir em chunks; gerar embeddings; armazenar no vector store. Depois, na consulta, o agente chama a ferramenta de busca, recebe trechos relevantes e compõe uma resposta limitada por essas evidências.

---

# Módulo 4 — Segurança, controle e qualidade

> Com contexto e ferramentas definidos, o foco passa a ser limitar dano e verificar o comportamento observado.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

- reconhecer prompt injection e excesso de agência;
- selecionar controles preventivos, detectivos e de aprovação;
- diferenciar sucesso técnico de qualidade da resposta.

### Texto Descritivo

Prompt injection ocorre quando uma entrada tenta substituir as regras do agente. Pode chegar diretamente pela mensagem ou indiretamente por um documento recuperado. Uma mensagem de sistema não elimina o risco. Quanto mais ampla a permissão da ferramenta, maior o impacto de uma decisão incorreta.

O controle deve ocorrer em camadas. Guardrails podem bloquear ou sanitizar jailbreaks, dados pessoais, chaves, URLs e assuntos fora de escopo. O Structured Output Parser exige campos e tipos previsíveis. Credenciais e ferramentas devem seguir menor privilégio. A revisão humana pausa ferramentas sensíveis para aprovação ou negação antes da ação.

Executions permite examinar entradas, saídas e chamadas de ferramenta. Uma execução concluída comprova apenas que o workflow terminou sem erro técnico. Qualidade requer casos de teste e resultados esperados; ações repetíveis também devem considerar idempotência, pois um retry pode duplicar gravações.

### Verificação Formativa

Um agente pode ler uma planilha e apagar linhas. Qual mudança reduz mais diretamente o impacto potencial?

A. Aumentar a janela de memória.  
B. Remover a permissão de exclusão e exigir aprovação para escrita.  
C. Publicar o chat com autenticação None.  
D. Aumentar Max Iterations.

**Gabarito:** B.  
**Feedback:** Menor privilégio reduz a capacidade de dano; revisão humana acrescenta controle antes da ação sensível.

### Aplicação Conceitual

Em um teste adversarial, o usuário pede que o agente ignore as regras, revele credenciais e apague dados. A resposta segura combina bloqueio ou recusa, ausência de chamada à tool sensível e registro em Executions. Somente recusar em linguagem natural, sem limitar a ferramenta, é controle insuficiente.

---

# Módulo 5 — Síntese e Aplicação Integrada

> O módulo final reúne arquitetura, contexto, ferramentas, controles e evidências em uma única decisão.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

- avaliar uma arquitetura de agente de ponta a ponta;
- identificar controles ausentes em um cenário;
- justificar uma solução proporcional ao risco.

### Texto Descritivo

Uma arquitetura confiável começa pelo problema, não pela ferramenta. Primeiro se verifica se a tarefa realmente exige interpretação e escolha. Depois se delimitam entrada, fontes, ferramentas, memória, saída esperada e condições de parada. Por fim, definem-se permissões, validações, aprovação e evidências de teste.

O desenho mínimo combina Chat Trigger, AI Agent, Chat Model e ao menos uma tool. Memória é acrescentada quando o histórico da sessão é necessário. RAG entra quando respostas precisam se apoiar em documentos. Formato estruturado, guardrails e revisão humana são selecionados conforme o risco da entrada e da ação.

A publicação ocorre somente após testes funcionais, adversariais e de separação de sessão. O histórico de execuções sustenta a auditoria, enquanto avaliações com casos conhecidos medem qualidade. Mudanças em modelos, planos e interface exigem revalidação periódica.

### Verificação Formativa

Qual evidência é mais forte para liberar um agente que registra solicitações?

A. Uma resposta bem escrita em um único teste.  
B. Workflow ativo e sem erro visual.  
C. Casos normais e adversariais, negação de ação, separação de sessão e revisão de Executions.  
D. Mensagem de sistema longa.

**Gabarito:** C.  
**Feedback:** A liberação exige evidências variadas de função, segurança e isolamento, não apenas fluência textual.

### Atividade Integradora

Uma área quer um chat que responda com base em um manual e registre pedidos em uma planilha. A arquitetura proposta possui Chat Trigger público sem autenticação, AI Agent, modelo, Simple Memory com chave fixa, vector store, tool de escrita ampla e nenhuma revisão.

Decisões esperadas:

1. manter RAG para o manual;
2. substituir a chave fixa por identificador exclusivo de sessão;
3. restringir a tool à operação necessária;
4. exigir confirmação e human review antes de gravar;
5. configurar autenticação adequada;
6. testar prompt injection, sessões distintas e duplicidade após retry;
7. revisar Executions e executar casos de avaliação.

**Feedback:** O desenho preserva a utilidade do agente, mas reduz exposição, mistura de contexto e ações indevidas.

## Encerramento

O curso apresentou critérios para reconhecer, decompor e avaliar agentes de IA no n8n. A compreensão da arquitetura permite escolher componentes por necessidade, em vez de acumular recursos sem finalidade.

O aprofundamento recomendado inclui prática com workflows de teste, estudo de avaliações por métricas e validação das políticas do provedor de modelo e da organização.

> **Síntese:** um agente confiável combina capacidade limitada, contexto autorizado, ação controlada e evidência verificável.

## Pendências de validação

- Confirmar rótulos e posição dos controles na conta usada para publicar o curso.
- Revalidar recursos em preview, planos e limites na semana da publicação.

