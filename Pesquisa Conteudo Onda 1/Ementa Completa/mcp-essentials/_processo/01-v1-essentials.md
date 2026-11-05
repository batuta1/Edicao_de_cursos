# Plano de Aula — MCP (Model Context Protocol) (Essentials)

## Identificação

| Campo | Definição |
|---|---|
| Curso | MCP - Essentials |
| Natureza | Curto, introdutório e prático |
| Carga horária | 90 minutos |
| Público-alvo | Profissionais que desejam delegar tarefas a assistentes de IA; curiosos técnicos; desenvolvedores e equipes de TI |
| Pré-requisitos | Uso básico de Claude ou ChatGPT; não exige programação |
| Recursos necessários | Computador com internet; conta Claude ou ChatGPT |

### Objetivo Geral

O curso tem por finalidade apresentar o Model Context Protocol (MCP) como padrão aberto de conexão
entre assistentes de inteligência artificial e ferramentas externas, habilitando o participante a
instalar e utilizar conectores MCP no Claude e no ChatGPT. Como produto final, espera-se que o
participante tenha conectado ao menos um serviço externo a um assistente e realizado com ele uma
consulta e uma ação.

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Explicar o que é o MCP e qual problema ele resolve.
2. Descrever a arquitetura do protocolo e suas primitivas.
3. Instalar conectores MCP no Claude e no ChatGPT.
4. Utilizar conectores com segurança.

### Estrutura e Sequência dos Módulos

Os módulos seguem progressão cumulativa: do conceito à arquitetura, da arquitetura à instalação, da
instalação ao uso, encerrando com a síntese.

| Módulo | Título | Referência (material-fonte) | Tempo |
|---|---|---|---|
| 1 | O que é o MCP | Anúncio Anthropic (2024); AAIF (2025) | 15 min |
| 2 | Arquitetura e funcionamento do protocolo | Especificação 2026-07-28; Architecture overview | 20 min |
| 3 | Instalando conectores no Claude e no ChatGPT | Ajuda Claude; documentação OpenAI Plugins | 20 min |
| 4 | Uso seguro de conectores | Security Best Practices; ajuda Claude | 15 min |
| 5 | Síntese e Aplicação Integrada | — | 20 min |

---

# Módulo 1 — O que é o MCP

> Ponto de partida do curso: apresenta-se o protocolo e o problema que motivou sua criação.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Definir o Model Context Protocol.
2. Identificar o problema de integração que o protocolo resolve.
3. Reconhecer as principais organizações envolvidas na governança do protocolo.

### Texto Descritivo

O Model Context Protocol (MCP) é uma especificação aberta que padroniza a forma como aplicações de
inteligência artificial se conectam a ferramentas e fontes de dados externas. Foi anunciado pela
Anthropic em 25 de novembro de 2024, acompanhado de especificação, kits de desenvolvimento e
servidores de referência publicados em código aberto.

Antes do MCP, cada assistente de IA precisava de uma integração própria para cada serviço, o que
multiplicava o esforço de desenvolvimento. A documentação oficial compara o protocolo a uma porta
USB-C: assim como um padrão físico comum permite ligar muitos dispositivos a muitos aparelhos, um
padrão de software comum permite ligar muitos assistentes a muitas fontes de dados.

Em 9 de dezembro de 2025, a Linux Foundation anunciou a Agentic AI Foundation, à qual o MCP foi
doado como projeto fundador. Empresas como Anthropic, OpenAI, Block, Google e Microsoft participam
da iniciativa, o que consolidou o protocolo como padrão de mercado.

### Exercício Prático

**Questão de verificação (5 min)**

Qual alternativa descreve corretamente o MCP?

a) Um modelo de linguagem desenvolvido pela Anthropic.
b) Um padrão aberto para conectar assistentes de IA a ferramentas e dados externos.
c) Um aplicativo de automação semelhante ao Zapier.
d) Um plugin exclusivo do ChatGPT.

**Gabarito:** b. O MCP é um protocolo, não um modelo nem um produto específico.

---

# Módulo 2 — Arquitetura e funcionamento do protocolo

> Pré-requisito: Módulo 1. Desloca-se o foco da finalidade para o funcionamento interno.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Distinguir host, client e server.
2. Diferenciar tools, resources e prompts.
3. Descrever os transportes stdio e Streamable HTTP.
4. Explicar as mudanças da revisão 2026-07-28.

### Texto Descritivo

A arquitetura do MCP organiza-se em três papéis. O host é a aplicação de IA utilizada pelo usuário,
como o Claude Desktop ou o ChatGPT. O client é o componente, interno ao host, que mantém a ligação
com um servidor específico. O server é o programa que expõe capacidades ao assistente.

Os servidores oferecem três primitivas: tools (funções executáveis), resources (conteúdos
endereçáveis por URI) e prompts (modelos reutilizáveis de mensagem). As mensagens trocadas seguem o
formato JSON-RPC 2.0.

Há dois transportes. O stdio é utilizado por servidores locais, que trocam mensagens pela entrada e
saída padrão do processo. O Streamable HTTP é utilizado por servidores remotos.

A revisão 2026-07-28 tornou o núcleo do protocolo sem estado (stateless), removeu o handshake
`initialize` e o cabeçalho `Mcp-Session-Id`, introduziu o método `server/discover` e o padrão
Multi Round-Trip Requests (MRTR), transferiu Tasks para extensão e endureceu a autorização via
OAuth. Roots, Sampling e Logging foram depreciados.

### Exercício Prático

**Associação de conceitos (5 min)**

Associar cada termo à sua definição: host, client, server, tool, resource, prompt.

**Critério de êxito:** seis associações corretas.

---

# Módulo 3 — Instalando conectores no Claude e no ChatGPT

> Pré-requisito: Módulo 2. Desloca-se o foco da teoria para a instalação.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Adicionar um conector personalizado no Claude.
2. Adicionar um servidor MCP personalizado no ChatGPT.
3. Instalar uma extensão no Claude Desktop.

### Texto Descritivo

No Claude, conectores remotos personalizados são adicionados em Customize > Connectors > Add custom
connector, informando nome e URL do servidor. Em seguida, o conector é habilitado na conversa pelo
botão "+".

No ChatGPT, o caminho atual passa pela área de Plugins: seleciona-se o botão "+", escolhe-se "Add
custom MCP server", informa-se a URL e cria-se o plugin, que passa a ser chamado no chat com "@".

No Claude Desktop, é possível instalar extensões locais em Settings > Extensions, a partir de um
diretório de extensões ou de um pacote `.mcpb`.

### Exercício Prático

**Instalação de um conector (10 min)**

1. Escolher um conector de interesse no diretório do Claude ou do ChatGPT.
2. Instalá-lo seguindo o caminho indicado.
3. Fazer uma pergunta que exija o uso do conector.

**Critério de êxito:** o conector aparece como instalado.

---

# Módulo 4 — Uso seguro de conectores

> Pré-requisito: Módulo 3. Desloca-se o foco da instalação para os riscos.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Identificar riscos associados ao uso de conectores.
2. Aplicar boas práticas de segurança.
3. Reconhecer tentativas de prompt injection.

### Texto Descritivo

Conectar um servidor não verificado pode dar a terceiros acesso aos dados enviados e permitir ações
nas contas autorizadas. Entre os riscos conhecidos estão o tool poisoning, isto é, a manipulação da
descrição de uma ferramenta para induzir o modelo a agir fora da intenção do usuário, e a prompt
injection indireta, em que instruções maliciosas aparecem em documentos ou páginas lidos pelo
assistente.

Recomenda-se começar com ferramentas somente leitura, conceder o menor privilégio possível, revisar
cada chamada antes de aprová-la e evitar a opção de permitir sempre com servidores de terceiros.

### Exercício Prático

**Questão de verificação (5 min)**

Qual prática reduz o risco de uso de conectores?

a) Usar sempre "Allow always" para agilizar.
b) Começar com ferramentas somente leitura.
c) Instalar o maior número possível de conectores.
d) Colar tokens de acesso no prompt.

**Gabarito:** b.

---

# Módulo 5 — Síntese e Aplicação Integrada

> Pré-requisito: Módulos 1 a 4. Integram-se conceito, instalação e segurança.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Integrar os conceitos do curso em um uso completo de conector.
2. Avaliar a segurança de um conector antes de usá-lo.

### Texto Descritivo

O uso de conectores MCP articula três dimensões: compreender o que o protocolo faz, saber
instalá-lo nas ferramentas e utilizá-lo com segurança. Recomenda-se que o participante, ao adotar
um novo conector, percorra sempre essa sequência.

### Exercício Prático

**Atividade integradora (15 min)**

1. Escolher um serviço do cotidiano profissional (por exemplo, Google Drive ou Notion).
2. Conectá-lo ao Claude ou ao ChatGPT.
3. Realizar uma consulta e uma ação com o conector.
4. Registrar os cuidados de segurança adotados.

**Critérios de avaliação**

| Critério | Atendido? |
|---|---|
| O conector foi instalado | |
| Uma consulta foi realizada | |
| Uma ação foi realizada | |
| Os cuidados de segurança foram registrados | |

---

# Encerramento

O curso apresentou o MCP como padrão aberto de conexão entre assistentes de IA e ferramentas
externas, percorrendo sua origem, sua arquitetura, a instalação de conectores e os cuidados de
segurança. Recomenda-se a prática regular com conectores de baixo risco.

Para aprofundamento, recomendam-se a documentação oficial em modelcontextprotocol.io, os cursos da
Anthropic Academy e o curso gratuito de MCP da Hugging Face.

> **Síntese:** o MCP é a tomada universal que liga o assistente ao mundo; cabe ao usuário decidir o
> que conectar.
