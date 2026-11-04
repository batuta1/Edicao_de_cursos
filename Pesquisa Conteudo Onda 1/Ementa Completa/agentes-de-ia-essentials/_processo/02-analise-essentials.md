# Análise Crítica 360 — Agentes de IA - Essentials (v1.0)

Entrada: `_processo/01-v1-essentials.md` + `_processo/00-contornos.md`. Trilha: Essentials.
Leitura feita como se o texto fosse de outra pessoa.

## 1. Sumário Executivo

**Nota: 3,5/10.** A v1.0 acerta o esqueleto (conceito → formular → acompanhar → revisar) e a
fórmula O-F-L-C-P, mas não se sustenta como curso autoinstrucional nem como material factualmente
correto em outubro de 2026.

Principais constatações:

- **Erro factual grave:** ensina a ativar o "modo agente do ChatGPT" pelo menu de ferramentas ou
  `/agent`. A ajuda oficial pt-BR diz que o agente do ChatGPT "não está mais disponível"; o caminho
  atual é o seletor **Work**. O aluno trava no primeiro passo.
- **Sem caminho gratuito:** "conta no ChatGPT, no Claude ou no Manus" ignora que Work exige Plus e
  Cowork exige Pro. Só o Manus Free tem agente. Um aluno sem assinatura não executa o Módulo 3.
- **Segurança chega tarde:** riscos, pasta dedicada e modo Manual aparecem no Módulo 4, depois de o
  Módulo 3 já ter mandado o aluno delegar "a tarefa do Módulo 2" — que é "Organize meus arquivos",
  uma tarefa de **escrita** sobre arquivos reais.
- **Exercícios não executáveis sozinho:** "Abrir uma das ferramentas" e "delegar" sem material,
  sem pasta, sem critério verificável ("a tarefa é concluída").
- **Carga horária fora do alvo:** 80 min contra 100–130 min do prompt-mestre; módulos com dois
  parágrafos de texto descritivo (o modelo pede 3 a 5).
- **Potencial perdido:** não trata *por que* a revisão importa (benchmarks independentes), injeção de
  prompt com caso brasileiro (STJ), modos de aprovação, menor privilégio, custo/créditos, escolha
  entre ferramentas.

## 2. Pontos Positivos (Fortalezas)

| Acerto | Por que manter |
|---|---|
| Sequência definir → acompanhar → revisar → riscos | Espelha exatamente a tarefa observável do catálogo; é o eixo do curso. |
| Distinção chat × automação × agente no Módulo 1 | Resolve a confusão mais comum do público ("já uso ChatGPT, isso é agente?"). |
| Fórmula O-F-L-C-P com exemplo antes/depois | Ferramenta mental transferível para qualquer produto; serve aos dois públicos. |
| Definições com fonte (Anthropic, Google Cloud) | Ancoram o conceito em documento oficial, não em opinião. |
| Menção à Recomendação 001/2024/CFOAB | Necessária para a trilha J5, onde o curso é o primeiro. |
| Registro formal e impessoal | Tom correto para Essentials, sem "você". |

## 3. Pontos Negativos e Gargalos (Debilidades)

**Clareza pedagógica**
- Não há Módulo 0: o aluno não sabe qual ferramenta usar, que plano precisa, nem o que preparar.
- O exercício do Módulo 1 tem três itens com resposta óbvia; não exercita o caso limítrofe (chat com
  pesquisa na web, que parece agente mas não é).
- Módulo 2 manda reescrever "Organize meus arquivos", tarefa de escrita em arquivos, sem dizer que
  pasta usar — e o Módulo 3 delega exatamente esse pedido.
- Critérios de êxito vagos: "a tarefa é concluída" não distingue concluída de correta.
- Síntese sem conteúdo: dois parágrafos, atividade "escolher uma tarefa do próprio trabalho" convida
  o aluno a usar dados reais (inclusive de clientes) no primeiro contato.
- Não há fio condutor; os módulos não se referem uns aos outros.

**Rigor técnico**
- `/agent` e "modo agente" descontinuados (ver Sumário).
- "Manual, Auto ou Skip" sem explicar o que cada modo faz e que Skip dispensa a triagem de segurança.
- Nenhuma menção a créditos (Manus), franquia compartilhada (Work/Codex) ou limite de sessão (Claude).
- Nenhuma referência a rótulos pt-BR nem aviso de que a interface varia por rollout.
- "Todas permitem delegar tarefas que envolvem pesquisa, leitura de arquivos e produção de
  documentos" — genérico; omite que pasta local exige app desktop e permissão explícita.

**Engajamento / aderência ao público**
- Nenhum exemplo de escritório ou jurídico concreto; nenhum caso real (há quatro brasileiros na
  pesquisa).
- Para o jurídico, a menção à OAB é uma frase; não traduz em regra operacional (o que nunca entra
  numa tarefa).

**Potencial oculto**
- Não explora: ciclo planejar-agir-observar-ajustar; ferramentas de leitura × escrita (NIST);
  checkpoints; ações consequenciais; observabilidade; injeção de prompt com caso STJ; "terminou ≠
  correto" com dados independentes; critérios de escolha entre ferramentas.

**Não verificado:** a tela logada das três ferramentas não foi observada por esta análise; os
rótulos sugeridos nas correções vêm da ajuda pt-BR e devem ser marcados [conferir].

## 4. Matriz de Soluções e Melhorias

| ID | Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|---|
| E1 | "Modo agente"/`/agent` descontinuados | Mód. 3 | Substituir por seletor **Work** (`ChatGPT > Novo chat > Work`); citar "modo agente" só como nome histórico, com a frase oficial de descontinuação | Crítica |
| E2 | Sem caminho gratuito | Identificação, Mód. 3 | Acrescentar tabela de planos (Work = Plus; Cowork = Pro; Manus Agent = Free) e definir Manus Free como caminho principal, Work/Cowork como opcionais | Crítica |
| E3 | Sem Módulo 0 | Antes do Mód. 1 | Criar Módulo 0: escolha do caminho, conta, pasta `Treino_Agente`, download do Guia do TCU, registro de rótulos | Crítica |
| E4 | Segurança depois do primeiro uso | Mód. 4 | Criar módulo de segurança **antes** do primeiro uso real (novo Mód. 2), com fórmula de risco, menor privilégio, modos de aprovação, dados proibidos, OAB | Crítica |
| E5 | Exercício de escrita sobre arquivos reais | Mód. 2–3 | Trocar "Organize meus arquivos" por tarefa **somente leitura** sobre documento público (Guia do TCU); escrita só em pasta de treino, com aprovação | Crítica |
| E6 | Exercício do Mód. 3 sem material nem critério | Mód. 3 | Procedimento numerado com breadcrumbs; critério: plano exibido antes da execução, parada respeitada, tabela com página em todas as linhas | Alta |
| E7 | Injeção de prompt só citada | Mód. 4 | Explicar com analogia e caso STJ (02/09/2026); separar de alucinação | Alta |
| E8 | "Terminou" confundido com "correto" | Mód. 3–4 | Novo módulo de revisão com dados independentes (HAL Princeton 35–42%; AI Agent Index) e ressalvas; exercício de amostragem por página | Alta |
| E9 | Modos de aprovação sem explicação | Mód. 3 | Tabela Manual/Auto/Pular com consequência de cada um; recomendar Manual; avisar que Pular dispensa triagem | Alta |
| E10 | Custo/créditos ausentes | — | Explicar créditos do Manus (300/dia, custo imprevisível), franquia variável de Work e limite de 5 h do Claude; regra: tarefa pequena, um assunto por tarefa | Alta |
| E11 | Atividade integradora com dados reais | Mód. 5 | Atividade por perfil com documento público (CGU para escritório; OAB 001/2024 para jurídico); proibir dado real | Alta |
| E12 | Carga horária 80 min, textos curtos | Todos | Reescrever com 3–5 parágrafos por módulo; recalcular pela MET para 100–130 min | Alta |
| E13 | Sem fio condutor | Todos | Plantar a analogia do **assistente recém-contratado com ordem de serviço** no Mód. 1 e retomá-la nos demais | Média |
| E14 | Exercício do Mód. 1 trivial | Mód. 1 | Incluir caso limítrofe (chat com busca na web) e fundamentação de cada alternativa | Média |
| E15 | Sem escada de autonomia nem leitura × escrita | Mód. 1 | Acrescentar escada didática (0–4, declarada como não oficial) e classificação NIST de ferramentas | Média |
| E16 | Sem como interromper/redirecionar | Mód. 3 | Descrever pausa, redirecionamento e "assumir o controle" nas três ferramentas, com breadcrumbs [conferir] | Média |
| E17 | Sem casos reais | Mód. 1 | Inserir um caso de escritório (CAIXA, ressalva de fornecedor) e o caso STJ; não usar números de fornecedor como prova | Média |
| E18 | Sem critério para escolher ferramenta | — | Tabela comparativa por superfície, plano, aprovação, custo; regra "escolher por acesso e controle, não por inteligência" | Média |
| E19 | Rótulos sem aviso de variação | Todos | Nota de vigência + Anexo de rótulos pt-BR/inglês com [conferir] | Média |
| E20 | Encerramento genérico | Encerramento | Caminhos concretos: Claude Cowork - Essentials, MCP - Essentials, Multiagentes, N8N | Baixa |

## 5. Roadmap de Expansão

| Tópico | Destino |
|---|---|
| Ciclo planejar-agir-observar-ajustar; ferramentas leitura × escrita | **Neste curso** (Mód. 1) |
| Injeção de prompt com caso STJ e arquivo-isca sintético | **Neste curso** (Mód. 2 e exercício do Mód. 5) |
| Comparação e escolha entre Work, Cowork e Manus | **Neste curso** (Mód. 5) |
| Tarefas agendadas, Projects, memória | Só menção; detalhamento em *Claude Cowork - Essentials* |
| Conectores e MCP | *MCP - Essentials* (próximo da trilha T3) |
| Vários agentes coordenados | *Multiagentes - Essentials* |
| Agentes de navegador (Atlas, Claude in Chrome) | *Agentes Web - Hands On* |
| Agentes em automações | *N8N: Agentes de IA - Essentials 6* |
| Política de uso de agentes no escritório (piloto) | Anexo do roteiro final, como checklist |
