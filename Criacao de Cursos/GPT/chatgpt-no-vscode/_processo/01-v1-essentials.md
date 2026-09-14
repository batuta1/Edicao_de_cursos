# Plano de Aula — ChatGPT (Codex) no VS Code (Essentials)

## Identificação

| Campo | Definição |
|---|---|
| Curso | ChatGPT (Codex) no VS Code — Essentials |
| Natureza | Curto, introdutório, prático e autoinstrucional |
| Carga horária | 100 a 130 minutos |
| Público-alvo | Professores universitários que não programam |
| Pré-requisitos | Saber criar pastas e mover arquivos; conta no ChatGPT; nenhum conhecimento de programação |
| Recursos necessários | Computador com permissão de instalar programas; VS Code; extensão Codex; internet; conta ChatGPT |

### Objetivo Geral

O curso destina-se a habilitar o docente do ensino superior, ainda que sem qualquer conhecimento de
programação, a empregar o Codex no Visual Studio Code como assistente para trabalho com arquivos:
organização de material, consulta a conjuntos de documentos, conversão de formatos e produção de
análises simples. Ao término, espera-se que o participante compreenda o modelo de permissões da
ferramenta e saiba operá-la sobre uma pasta de trabalho própria.

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Instalar o Visual Studio Code e a extensão Codex.
2. Descrever tarefas de manipulação de arquivos em linguagem natural.
3. Operar o modelo de aprovações do Codex.
4. Avaliar criticamente o resultado antes de aceitá-lo.

### Estrutura e Sequência dos Módulos

Os módulos observam progressão cumulativa: o primeiro apresenta a ferramenta, o segundo trata da
instalação, o terceiro e o quarto tratam do uso, e o quinto integra as competências.

| Módulo | Título | Referência (material-fonte) | Tempo |
|---|---|---|---|
| 1 | O que é o Codex | Central de Ajuda da OpenAI | 25 min |
| 2 | Instalação e primeiro contato | Central de Ajuda da OpenAI — primeiros passos | 25 min |
| 3 | Como pedir uma tarefa | Anúncio do GPT-5-Codex | 25 min |
| 4 | Permissões e segurança | Central de Ajuda da OpenAI — controles de dados | 25 min |
| 5 | Síntese e Aplicação Integrada | — | 20 min |

---

# Módulo 1 — O que é o Codex

> Ponto de partida do curso: estabelece o que a ferramenta é e onde ela opera.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Definir o que é o Codex.
2. Enumerar os clientes pelos quais ele pode ser acessado.
3. Reconhecer que o Codex está incluído nos planos do ChatGPT.

### Texto Descritivo

O Codex é descrito pela OpenAI como um agente de inteligência artificial que auxilia a escrever,
revisar e entregar código. Diferentemente de uma conversa comum no ChatGPT, o Codex atua sobre
arquivos: lê o conteúdo de uma pasta, executa comandos e produz alterações.

Convém esclarecer o termo agente. Enquanto um sistema de conversa responde com texto, um agente
executa ações. A distinção é relevante porque as consequências são diferentes: um texto equivocado
se descarta; uma alteração equivocada em arquivo precisa ser desfeita.

O Codex pode ser acessado por quatro clientes: o aplicativo do ChatGPT para desktop, em modo Codex; a
interface de linha de comando; a extensão para ambientes de desenvolvimento integrado; e a versão
para a web. A extensão para o Visual Studio Code é compatível com a maioria das variações do editor.

Registre-se que o Codex está incluído nos planos do ChatGPT, inclusive nos planos Free e Go, com
limites de uso que variam conforme o plano contratado.

### Exercício Prático

**Identificação do cliente (6 min)**

Qual cliente do Codex é o objeto deste curso?

- (a) A interface de linha de comando
- (b) A extensão para o Visual Studio Code
- (c) A versão para a web
- (d) O aplicativo do ChatGPT para desktop

**Gabarito:** (b).

**Fundamentação:** o curso trata do uso do Codex dentro do Visual Studio Code, por meio da extensão
correspondente.

---

# Módulo 2 — Instalação e primeiro contato

> Pressupõe o Módulo 1 e desloca o foco do que a ferramenta é para como obtê-la.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Instalar o Visual Studio Code.
2. Instalar a extensão Codex.
3. Conectar a extensão à conta do ChatGPT.

### Texto Descritivo

O Visual Studio Code é um editor de texto gratuito, distribuído pela Microsoft, disponível para
Windows, macOS e Linux. Embora seja um programa destinado a quem escreve software, sua função básica
é a de abrir uma pasta e mostrar os arquivos que ela contém — o que basta ao propósito deste curso.

A extensão Codex é instalada a partir do painel de extensões do próprio editor. Uma vez instalada, é
necessário entrar com a conta do ChatGPT.

No Windows, o Codex oferece ferramentas adicionais. O comando de diagnóstico permite verificar
problemas de inicialização, conectividade e desempenho. Quando há mais de uma distribuição do
subsistema Windows para Linux instalada, é possível escolher qual será utilizada.

Caso a organização gerencie as atualizações dos aplicativos, o administrador precisa implantar a
versão aprovada antes que os recursos que a exigem possam ser utilizados.

### Exercício Prático

**Instalação (6 min)**

1. Instale o Visual Studio Code.
2. Instale a extensão Codex pelo painel de extensões.
3. Entre com a sua conta do ChatGPT.
4. Abra uma pasta qualquer.

**Critério de êxito:** o painel do Codex está visível no editor e a conta está conectada.

---

# Módulo 3 — Como pedir uma tarefa

> Pressupõe o Módulo 2 e desloca o foco da instalação para o uso.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Formular um pedido em linguagem natural.
2. Fornecer contexto adequado à tarefa.
3. Acompanhar a execução.

### Texto Descritivo

O pedido ao Codex é feito em linguagem natural, no painel da extensão. Não é necessário conhecer
comandos nem sintaxe: descreve-se o que se pretende e o sistema propõe como fazer.

Observa-se que o Codex aproveita o contexto do editor. Quando um arquivo está aberto ou um trecho
está selecionado, o pedido pode ser mais curto, porque o sistema já sabe a que se refere.

O sistema acompanha o progresso de tarefas complexas por meio de uma lista de tarefas, e apresenta as
alterações propostas de forma que possam ser conferidas antes de aceitas.

Recomenda-se revisar o trabalho do agente antes de aplicar alterações. O próprio fabricante fornece
citações, registros de terminal e resultados de testes para auxiliar nessa revisão.

### Exercício Prático

**Primeiro pedido (6 min)**

1. Abra uma pasta com alguns arquivos.
2. Peça ao Codex uma descrição do conteúdo da pasta.
3. Confira a resposta contra o que você vê no editor.

**Critério de êxito:** a descrição corresponde ao conteúdo real da pasta.

---

# Módulo 4 — Permissões e segurança

> Pressupõe o Módulo 3 e desloca o foco do uso para o controle sobre o que o agente pode fazer.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Distinguir os três níveis de aprovação.
2. Reconhecer o funcionamento do ambiente isolado.
3. Identificar o tratamento dado aos dados por plano.

### Texto Descritivo

Por padrão, o Codex é executado em ambiente isolado, com acesso à rede desabilitado, tanto localmente
quanto na nuvem. A finalidade declarada é impedir ações danosas e reduzir o risco de instruções
maliciosas provenientes de fontes não confiáveis.

O sistema pode solicitar permissão antes de ações potencialmente perigosas. Na interface de linha de
comando, os modos de aprovação foram simplificados em três níveis: somente leitura com aprovações
explícitas; automático, com acesso ao espaço de trabalho mas exigindo aprovação fora dele; e acesso
total, com leitura de arquivos em qualquer lugar e execução de comandos com acesso à rede.

Quanto aos dados, os controles de treinamento do ChatGPT aplicam-se ao conteúdo processado pelo
Codex. Fluxos de trabalho locais são executados no dispositivo do participante; tarefas na nuvem são
executadas em ambientes gerenciados pela OpenAI. Nos planos Business, Enterprise e Edu, as entradas e
saídas não são usadas para melhorar os modelos por padrão. Nos planos Pro e Plus, as conversas podem
ser usadas, salvo desativação nos controles de dados.

Recomenda-se sempre revisar o trabalho do agente antes de aplicar alterações.

### Exercício Prático

**Identificação do nível (6 min)**

Qual nível de aprovação é mais adequado a quem está aprendendo a usar a ferramenta?

- (a) Somente leitura com aprovações explícitas
- (b) Automático
- (c) Acesso total

**Gabarito:** (a).

**Fundamentação:** o modo somente leitura impede alterações não intencionais enquanto o participante
ainda não domina o comportamento do agente.

---

# Módulo 5 — Síntese e Aplicação Integrada

> Pressupõe todos os módulos anteriores e os articula em uma única atividade.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Encadear pedido, revisão e aprovação em um fluxo único.
2. Aplicar critérios de verificação sobre o resultado.
3. Julgar quando a ferramenta é apropriada à tarefa.

### Texto Descritivo

Cumpre articular o que foi tratado. O uso do Codex observa um ciclo: descreve-se a tarefa, o sistema
propõe uma execução, o participante revisa a proposta e aprova ou recusa.

Observa-se que a revisão é a etapa insubstituível. A recomendação do fabricante é explícita: convém
sempre revisar o trabalho do agente antes de aplicar alterações ou colocá-las em produção.

Convém, por último, delimitar o que não deve ser processado. Dados identificáveis de aluno,
resultados não publicados e informações sob confidencialidade merecem cautela, conforme o plano e a
configuração de dados em uso.

### Exercício Prático

**Atividade Integradora — uma tarefa completa (10 min)**

1. Escolha uma pasta de trabalho sua.
2. Descreva uma tarefa de organização.
3. Revise a proposta do agente.
4. Aprove ou recuse.
5. Confira o resultado.

**Critérios de avaliação**

| Critério | Atendido? |
|---|---|
| A tarefa foi descrita de forma específica | |
| A proposta foi revisada antes da aprovação | |
| O resultado foi conferido | |
| Nenhum dado sensível foi processado | |

---

# Encerramento

O curso cumpriu a finalidade de estabelecer um repertório mínimo de uso do Codex no Visual Studio
Code para trabalho com arquivos. Recomenda-se prática regular, uma vez que a competência se consolida
pelo uso.

Apontam-se, como caminhos de aprofundamento, o uso de instruções de projeto, a exploração da
interface de linha de comando, e a integração com serviços conectados.

> **Síntese:** o agente executa; a decisão sobre o que aceitar permanece de quem revisa.
