# Plano de Aula - Agentes Web (Essentials)

## Identificacao

| Campo | Definicao |
|---|---|
| Curso | Agentes Web - Essentials |
| Natureza | Curto, introdutorio, conceitual e autoinstrucional |
| Carga horaria | 122 minutos |
| Publico-alvo | Profissionais que ja usam assistentes de IA |
| Pre-requisitos | Agentes de IA - Essentials e uso basico de navegador |
| Recursos necessarios | Dispositivo com acesso ao Rise 360; nenhuma conta de agente e exigida |

### Objetivo Geral

Compreender como agentes web planejam e executam acoes, distinguir modalidades de navegacao assistida e tomar decisoes de delegacao com limites, supervisao e verificacao.

### Competencias a Desenvolver

Concluido o curso, o participante devera demonstrar capacidade de:

1. diferenciar agente web, copiloto, deep research e RPA;
2. reconhecer permissoes, dados e efeitos envolvidos numa tarefa;
3. analisar riscos de prompt injection e acoes consequenciais;
4. aplicar o ciclo escopo-plano-permissoes-execucao-verificacao.

### Estrutura e Sequencia dos Modulos

O percurso parte dos requisitos e conceitos, avanca para arquitetura de controle e riscos e termina com uma decisao integrada.

| Modulo | Titulo | Referencia | Tempo |
|---|---|---|---:|
| 0 | Preparacao e limites | secoes 2, 7 e 18 | 27 min |
| 1 | O que torna um navegador agentico | secoes 1, 4 e 10 | 25 min |
| 2 | Delegacao, permissoes e intervencao | secoes 3, 5 e 7 | 29 min |
| 3 | Seguranca, privacidade e prompt injection | secoes 8 e 9 | 29 min |
| 4 | Sintese e Aplicacao Integrada | secoes 6, 13 e 14 | 12 min |

---

# Modulo 0 - Preparacao e limites

> Ponto de partida: os requisitos e as fronteiras sao definidos antes de qualquer contato com uma ferramenta.

### Objetivos de Aprendizagem

- identificar recursos e pre-requisitos;
- distinguir ambientes de treino e producao;
- classificar dados e acoes por sensibilidade.

### Texto Descritivo

Um agente web pode ler e alterar o estado de paginas e contas. Por isso, a preparacao exige objetivo observavel, dominios autorizados, dados permitidos, acoes proibidas e ponto de parada.

Recomenda-se conta de treinamento sem cartao, dados de clientes ou acesso produtivo. Planos e menus variam por regiao e data; disponibilidade nao deve ser pressuposta.

### Verificacao Formativa

**Cenario:** Qual preparacao reduz mais o risco? A) usar a conta corporativa principal; B) definir sites, dados, acoes e parada; C) permitir todos os sites. **Gabarito:** B. **Feedback:** limites explicitos reduzem privilegio e ambiguidade.

### Aplicacao Conceitual

Classifique como seguro ou inseguro: conta de teste sem dados reais; cartao salvo; dominio permitido; instrucao "pare antes de enviar". **Gabarito:** seguros: conta de teste, dominio e parada; inseguro: cartao salvo.

---

# Modulo 1 - O que torna um navegador agentico

> Com os limites definidos, o foco passa para as diferencas entre conversar, pesquisar e agir.

### Objetivos de Aprendizagem

- definir agente web;
- comparar browser local e remoto;
- diferenciar agente, copiloto, deep research e RPA.

### Texto Descritivo

Um agente web combina modelo e ferramentas de navegador para perseguir um objetivo em varias etapas. Um copiloto pode apenas explicar a pagina; deep research coleta e sintetiza; RPA segue regras deterministicas.

O Comet atua no navegador local e pode usar abas e sessoes do dispositivo. O navegador em nuvem do ChatGPT Work funciona em maquina remota e mantem sessoes proprias. Isolamento reduz certos riscos, mas nao elimina prompt injection.

Atlas e o antigo ChatGPT agent sao referencias historicas encerradas, nao fluxos atuais.

### Verificacao Formativa

**Pergunta:** Qual opcao descreve RPA? A) adapta o plano por linguagem natural; B) segue passos e seletores predefinidos; C) apenas resume fontes. **Gabarito:** B.

### Aplicacao Conceitual

Uma ferramenta apenas resume a aba atual. Trata-se de copiloto contextual, nao de agente completo, pois nao planeja nem executa uma sequencia de acoes.

---

# Modulo 2 - Delegacao, permissoes e intervencao

> A distincao conceitual passa a orientar a decisao sobre o que delegar e quando interromper.

### Objetivos de Aprendizagem

- construir um escopo pelo modelo LIMITE;
- reconhecer takeover e confirmacao;
- verificar processo, conteudo e efeito.

### Texto Descritivo

O ciclo seguro e composto por escopo, plano, permissoes, execucao observada, pausa ou takeover, conferencia, aprovacao ou cancelamento e registro. Takeover e a transferencia temporaria de controle ao humano para login, MFA, CAPTCHA ou etapa sensivel.

Acoes reversiveis, como ler e preencher sem enviar, admitem maior delegacao. Enviar, publicar, comprar, excluir, aceitar termos e alterar contas exigem retencao humana.

A verificacao final cobre tres camadas: o processo permaneceu nos limites; o conteudo confere com as fontes; e o efeito real do site corresponde ao relato do agente.

### Verificacao Formativa

**Cenario:** O agente pede confirmacao para finalizar uma compra. A decisao correta e: A) autorizar sem revisar; B) conferir fornecedor, total, datas e cancelamento e concluir sob controle humano; C) enviar CVV pelo chat. **Gabarito:** B.

### Aplicacao Conceitual

Ordene o ciclo: conferir efeito; definir escopo; observar execucao; revisar plano; registrar. **Gabarito:** definir escopo, revisar plano, observar, conferir, registrar.

---

# Modulo 3 - Seguranca, privacidade e prompt injection

> O ciclo de controle e submetido aos riscos que podem desviar o agente ou expor dados.

### Objetivos de Aprendizagem

- explicar prompt injection indireta;
- reconhecer sintomas de desvio;
- escolher resposta de contencao.

### Texto Descritivo

Prompt injection indireta ocorre quando uma pagina, imagem, e-mail ou documento inclui instrucoes dirigidas ao agente. O risco surge da mistura entre instrucoes confiaveis e dados externos nao confiaveis.

Sinais incluem mudanca de objetivo, dominio inesperado, pedido de segredo, tentativa de copiar dados de outra aba ou insistencia em enviar. A resposta adequada e parar, negar autorizacao, fechar a pagina, revisar sessoes e registrar o incidente.

Defesas em profundidade e confirmacoes reduzem risco, mas fabricantes e pesquisas reconhecem que nao existe eliminacao completa. O principio do menor privilegio continua indispensavel.

### Verificacao Formativa

**Pergunta:** Uma pagina diz ao agente para ignorar o usuario e abrir outro dominio. O que fazer? A) seguir; B) parar, registrar URL e revisar; C) fornecer senha. **Gabarito:** B.

### Aplicacao Conceitual

Classifique: texto oculto em imagem; CAPTCHA; preco divergente; pedido de token. **Gabarito:** injection possivel; intervencao humana; falha de verificacao; tentativa de exfiltracao.

---

# Modulo 4 - Sintese e Aplicacao Integrada

> A etapa final integra conceitos, limites, intervencao e verificacao em uma unica decisao.

### Objetivos de Aprendizagem

- analisar um plano de delegacao;
- identificar falhas criticas;
- propor uma sequencia segura.

### Texto Descritivo

Um profissional pede ao agente que compare servicos, preencha um formulario e envie o melhor resultado. O pedido nao define fontes, dados, parada nem evidencia. O plano seguro restringe dominios, usa dados ficticios, proibe envio, exige apresentacao do plano e termina com conferencia humana.

### Verificacao Formativa

**Pergunta:** Qual falha deve ser corrigida primeiro? A) ausencia de emoji; B) ausencia de limites e parada; C) tabela sem cor. **Gabarito:** B.

### Aplicacao Conceitual

**Atividade integradora:** escolha a sequencia correta: delimitar sites/dados/acoes; revisar plano; executar sob observacao; pausar diante de conflito; conferir fontes e estado; aprovar ou cancelar; registrar. **Gabarito:** a sequencia apresentada.

## Encerramento

O percurso estabeleceu criterios para compreender e governar agentes web. Recomenda-se retomar o ciclo de controle antes de cada nova delegacao.

O aprofundamento pode incluir governanca corporativa, avaliacao de agentes e automacao deterministica para processos estaveis.

> **Sintese:** autonomia util depende de privilegio limitado, observacao e verificacao humana.

