# Roteiro Articulate 360 — Claude Code no VS Code — Curso Hands-on

**Plataformas e Integrações: Use o Claude Code no VS Code — Curso Hands-on**

---

## Identificação

| Campo | Definição |
|---|---|
| **Curso** | Claude Code no VS Code — Curso Hands-on |
| **Natureza** | Autoinstrucional, orientado à prática e à produção de entregáveis verificáveis |
| **Plataforma de desenvolvimento** | Articulate 360 |
| **Ferramenta sugerida** | Rise 360 (estrutura modular e blocos responsivos) com apoio de Storyline 360 para interações de cenário e quiz ramificado |
| **Carga horária** | 100 minutos (4 módulos práticos de 20 minutos cada + 1 módulo de síntese de 20 minutos) |
| **Público-alvo** | Docentes do ensino superior iniciantes em Inteligência Artificial; analistas administrativos; alunos de graduação e pós-graduação sem experiência prévia com IA aplicada ao código |
| **Pré-requisitos** | VS Code instalado (versão 1.95 ou superior); conta ativa na plataforma Anthropic (claude.ai); acesso à internet; familiaridade elementar com criação e salvamento de arquivos em um editor de texto |
| **Recursos necessários** | Computador pessoal com sistema operacional Windows, macOS ou Linux; VS Code; navegador atualizado; terminal de sistema operacional (cmd, PowerShell, Bash ou Zsh); conexão estável à internet |
| **Produto final do participante** | Arquivo `turma.py` refatorado, documentado com docstrings e cabeçalho de módulo, com tratamento de entradas inválidas e comportamento validado via terminal |

---

## Objetivo Geral

O curso tem por finalidade desenvolver no participante a competência operacional de instalar, configurar e utilizar a extensão Claude Code no ambiente VS Code para a execução de tarefas práticas de análise, refatoração e depuração de código, com revisão crítica de cada sugestão gerada pelo assistente antes de sua aplicação. Ao concluir o percurso, o participante terá produzido um módulo de código transformado — partindo de um estado inicial com problemas de legibilidade, ausência de documentação e bug lógico, chegando a uma versão limpa, documentada e validada —, demonstrando domínio do ciclo Analisar → Planejar → Revisar → Aceitar como método de uso responsável de assistentes de Inteligência Artificial em contextos profissionais e acadêmicos.

---

## Competências Práticas a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Instalar a extensão Claude Code no VS Code, gerar uma chave de API no console da Anthropic e configurar a autenticação de forma segura, sem exposição da credencial em arquivos versionados ou compartilhados.
2. Formular prompts contextualizados que referenciem o arquivo aberto, descrevam o comportamento atual e o comportamento esperado, e delimitem o escopo da ação solicitada ao assistente.
3. Aplicar o ciclo de refatoração assistida — Analisar, Planejar, Revisar o diff e Aceitar ou Rejeitar — para modificar código com segurança e compreensão de cada alteração proposta.
4. Descrever um comportamento inesperado de código ao assistente, interpretar o diagnóstico recebido e validar a correção por meio de execução no terminal integrado do VS Code.

---

## Estrutura Geral do Curso

O curso é organizado em progressão cumulativa: cada módulo pressupõe o produto parcial gerado no módulo anterior e acrescenta uma habilidade nova ao repertório operacional do participante. O Módulo 1 estabelece o ambiente funcional; o Módulo 2 desenvolve a habilidade de leitura assistida de código; o Módulo 3 introduz o ciclo seguro de refatoração; o Módulo 4 aplica o mesmo ciclo à depuração de um erro real; e o Módulo 5 integra todas as habilidades em uma entrega final verificável.

| Módulo | Foco prático | Produto parcial | Interação principal | Tempo |
|---|---|---|---|---|
| 1 — Instalação e Configuração | Instalar a extensão e autenticar com chave de API | Extensão Claude Code funcional e autenticada no VS Code | Demonstração passo a passo + checklist de verificação | 20 min |
| 2 — Leitura Assistida de Código | Formular prompts contextualizados para análise de código | Arquivo `notas.py` analisado e explicado pelo assistente | Cenário prático de comparação de prompts + atividade guiada | 20 min |
| 3 — Refatoração com Revisão | Aplicar o ciclo Analisar → Planejar → Revisar → Aceitar | Arquivo `notas.py` refatorado com docstring, type hints e tratamento de lista vazia | Process block do ciclo + atividade de revisão de diff | 20 min |
| 4 — Depuração Assistida | Identificar, descrever e corrigir um bug lógico com auxílio do Claude | Arquivo `notas.py` corrigido com comportamento validado no terminal | Cenário de depuração + knowledge check | 20 min |
| 5 — Síntese e Aplicação Integrada | Refatorar um módulo legado completo integrando todas as habilidades | Arquivo `turma.py` refatorado, documentado e validado | Atividade integradora com checklist de critérios | 20 min |

---

<div style="page-break-after: always;"></div>

# Módulo 1 — Instalação e Configuração do Ambiente

## Encadeamento

Este é o ponto de partida do curso. O Módulo 1 estabelece a infraestrutura operacional sem a qual nenhuma das práticas subsequentes é possível.

## Finalidade Prática

Neste módulo, o participante instalará a extensão Claude Code no VS Code, gerará uma chave de API no console da Anthropic e realizará a autenticação da extensão. O produto parcial é um ambiente funcional: extensão instalada, autenticada e capaz de responder a uma mensagem de verificação.

## Objetivos de Aprendizagem Prática

Ao final deste módulo, o participante deverá ser capaz de:

1. Acessar o painel de extensões do VS Code e instalar a extensão Claude Code publicada pela Anthropic Inc.
2. Acessar o console da Anthropic, gerar uma chave de API e copiá-la antes de fechar a tela de confirmação.
3. Configurar a chave de API na extensão por meio do comando `Claude Code: Sign In`, sem registrá-la em arquivos de projeto.
4. Validar a instalação enviando uma mensagem de teste ao assistente e confirmando o recebimento de resposta.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 1.1 | Abertura do módulo | Título, foco prático e produto parcial esperado | Ícone do VS Code + ícone da Anthropic lado a lado |
| 1.2 | Texto curto explicativo | O que é a extensão Claude Code e por que ela precisa de autenticação | Diagrama simples: VS Code ↔ Extensão ↔ Servidores Anthropic |
| 1.3 | Demonstração passo a passo | Abertura do painel de extensões e instalação da extensão | Captura de tela: painel de extensões com resultado da busca "claude code" e publicador "Anthropic Inc." destacado |
| 1.4 | Demonstração passo a passo | Acesso ao console Anthropic e geração de chave de API | Captura de tela: tela de API Keys do console com o botão "Create API Key" destacado |
| 1.5 | Captura de tela anotada | Localização do campo de nome da chave e cópia da sequência gerada | Captura de tela: chave gerada com início "sk-ant-" e aviso "copiada apenas uma vez" destacado em vermelho |
| 1.6 | Demonstração passo a passo | Inserção da chave via comando `Claude Code: Sign In` na paleta de comandos | Captura de tela: paleta de comandos aberta com o comando digitado |
| 1.7 | Atividade guiada | Envio de mensagem de verificação: "Olá! Quanto é 7 vezes 8?" | Captura de tela: painel do Claude Code com resposta visível |
| 1.8 | Checklist | Verificação dos critérios de conclusão do módulo | Lista marcável com 4 itens |
| 1.9 | Knowledge check | Questão de múltipla escolha sobre segurança da chave de API | Feedback imediato com explicação da resposta correta |
| 1.10 | Fechamento | Produto parcial obtido e antecipação do Módulo 2 | Ícone de verificação + texto de transição |

## Conteúdo Instrucional Enxuto

A extensão Claude Code é um componente adicional que se instala dentro do VS Code — o editor de código — e permite que o assistente de Inteligência Artificial da Anthropic acesse o conteúdo dos arquivos abertos no editor, respondendo a perguntas e sugerindo modificações diretamente no ambiente de trabalho. Sem essa extensão, o uso do Claude exigiria cópia e colagem manual do código em uma interface web separada, o que é mais trabalhoso e propenso a perda de contexto.

A autenticação é feita por meio de uma chave de API — uma sequência alfanumérica única que funciona como credencial de acesso ao serviço. Essa chave é gerada no console da Anthropic, plataforma web separada da interface de chat, e deve ser tratada com o mesmo cuidado reservado a senhas: nunca deve ser registrada em arquivos de código, documentos compartilhados ou repositórios Git. Uma vez inserida na extensão, o sistema operacional a armazena de forma segura, sem necessidade de inseri-la novamente a cada uso.

Recomenda-se verificar, antes de iniciar, se a versão do VS Code instalada é 1.95 ou superior. Versões anteriores podem não ser compatíveis com a extensão. A verificação é feita em *Help → About* (Windows e Linux) ou *Code → About* (macOS).

## Demonstração Guiada

1. Abrir o VS Code e pressionar `Ctrl + Shift + X` (Windows/Linux) ou `Cmd + Shift + X` (macOS) para acessar o painel de extensões.
2. Digitar "claude code" no campo de busca e localizar a extensão publicada por **Anthropic Inc.**

   Captura de tela recomendada: painel de extensões com o resultado da busca, destacando em caixa vermelha o nome do publicador "Anthropic Inc." abaixo do título da extensão e o botão "Install" em azul.

3. Clicar em **Install** e aguardar a conclusão (30 a 60 segundos). Se solicitado, recarregar a janela pelo comando `Developer: Reload Window` na paleta de comandos.
4. Acessar [console.anthropic.com](https://console.anthropic.com) no navegador, navegar até **API Keys** e clicar em **Create API Key**. Atribuir um nome descritivo (exemplo: "VS Code — Uso Pessoal") e clicar em **Create Key**.

   Captura de tela recomendada: tela de confirmação da chave gerada, mostrando a sequência iniciada com "sk-ant-" e o aviso de cópia única em destaque.

5. Copiar a chave gerada imediatamente. Voltar ao VS Code, pressionar `Ctrl + Shift + P` (ou `Cmd + Shift + P`), buscar `Claude Code: Sign In` e colar a chave quando solicitado.
6. Clicar no ícone do Claude Code na barra lateral esquerda, digitar "Olá! Quanto é 7 vezes 8?" no campo de texto e pressionar Enter.

   Captura de tela recomendada: painel do Claude Code exibindo a resposta do assistente, com o ícone de raio (⚡) visível na barra lateral.

7. Resultado esperado: o assistente responde à pergunta sem exibir mensagem de erro de autenticação.

## Atividade Hands-on

### Atividade prática — Instalação e verificação do ambiente (15 minutos)

Tarefa:
Instalar a extensão Claude Code, autenticar com chave de API e confirmar o funcionamento por meio de uma mensagem de teste.

Procedimento:
1. Abrir o painel de extensões do VS Code (`Ctrl + Shift + X` ou `Cmd + Shift + X`) e instalar a extensão publicada por Anthropic Inc.
2. Acessar o console da Anthropic, gerar uma chave de API com nome descritivo e copiá-la antes de fechar a tela.
3. Inserir a chave na extensão pelo comando `Claude Code: Sign In` na paleta de comandos.
4. Enviar a mensagem "Olá! Quanto é 7 vezes 8?" no painel do Claude Code e aguardar resposta.

Produto parcial esperado:
Ambiente VS Code com extensão Claude Code instalada, autenticada e responsiva.

Critério de êxito:
O assistente responde à mensagem de verificação sem exibir erro de autenticação, e o ícone da extensão está visível na barra lateral esquerda do VS Code.

## Checkpoint de Aprendizagem

**Questão de múltipla escolha:**

Ao gerar uma chave de API no console da Anthropic, qual das ações a seguir representa a prática mais segura?

(A) Salvar a chave em um arquivo `.env` dentro da pasta do projeto e incluí-la no Git junto com o restante do código.
(B) Copiar a chave imediatamente após a geração, inseri-la na extensão e não registrá-la em nenhum arquivo compartilhável.
(C) Anotar a chave em um comentário dentro de um arquivo Python para fácil acesso posterior.
(D) Compartilhar a chave com colegas por e-mail para que todos possam usar a mesma conta.

**Gabarito:** Alternativa (B).

**Fundamentação:** A chave de API é uma credencial de acesso que deve ser tratada como senha. Registrá-la em arquivos versionados, comentários de código ou mensagens eletrônicas expõe a conta da Anthropic a uso não autorizado. O sistema operacional armazena a chave de forma segura após a inserção na extensão, dispensando qualquer registro adicional.

## Prompt ou Modelo Editável

Modelo de primeiro contato para verificação do ambiente:

```text
Olá! Acabo de configurar a extensão Claude Code no VS Code.
Estou trabalhando na área de [ÁREA DE ATUAÇÃO: docência, administração, análise de dados, etc.].
Confirme que está funcionando respondendo: "Ambiente configurado com sucesso."
```

## Fechamento do Módulo

Neste módulo, foi produzido o produto essencial que viabiliza todo o percurso: um ambiente VS Code com a extensão Claude Code instalada, autenticada e operacional. Esse ambiente será o espaço de trabalho de todos os módulos seguintes. O Módulo 2 aproveitará essa infraestrutura para introduzir a habilidade central do curso: a formulação de prompts que permitem ao assistente analisar o código aberto no editor com precisão e utilidade.

<div style="page-break-after: always;"></div>

# Módulo 2 — Leitura Assistida de Código

## Encadeamento

O Módulo 2 pressupõe o ambiente configurado no Módulo 1 e desloca o foco da infraestrutura para o uso produtivo: a formulação de perguntas que geram respostas úteis.

## Finalidade Prática

Neste módulo, o participante criará o arquivo `notas.py` com um trecho de código de referência, enviará dois prompts ao assistente — um vago e um contextualizado — e comparará os resultados. Em seguida, aprofundará a análise com perguntas sobre comportamentos de borda. O produto parcial é o arquivo `notas.py` analisado, com o participante capaz de articular a diferença entre um prompt genérico e um prompt contextualizado.

## Objetivos de Aprendizagem Prática

Ao final deste módulo, o participante deverá ser capaz de:

1. Criar o arquivo `notas.py` no VS Code e inserir o código de referência do módulo.
2. Comparar a qualidade das respostas obtidas com um prompt vago versus um prompt contextualizado para o mesmo arquivo.
3. Formular prompts que identifiquem o arquivo, descrevam o elemento de código e delimitam o escopo da resposta esperada.
4. Aplicar prompts de aprofundamento para investigar comportamentos de borda sem autorizar modificações no arquivo.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 2.1 | Abertura do módulo | Título, foco prático e produto parcial | Ícone de lupa sobre bloco de código |
| 2.2 | Texto curto explicativo | O que é um prompt e por que o contexto importa | Diagrama de comparação: prompt vago × prompt contextualizado |
| 2.3 | Demonstração passo a passo | Criação do arquivo `notas.py` e inserção do código de referência | Captura de tela: VS Code com o arquivo criado e código visível |
| 2.4 | Cenário prático | Envio do prompt vago "O que esse código faz?" e leitura da resposta | Captura de tela: painel do Claude Code com resposta genérica |
| 2.5 | Cenário prático | Envio do prompt contextualizado com nome do arquivo e da função | Captura de tela: painel do Claude Code com resposta detalhada e estruturada |
| 2.6 | Tabs | Comparação lado a lado: prompt vago × prompt contextualizado | Dois painéis com texto das respostas destacando diferenças |
| 2.7 | Atividade guiada | Envio de perguntas de aprofundamento sobre comportamento com lista vazia | Captura de tela: resposta do Claude identificando o risco da divisão por zero |
| 2.8 | Accordion | Anatomia de um bom prompt: três elementos com exemplos | Ícones para cada elemento (arquivo, comportamento, escopo) |
| 2.9 | Knowledge check | Questão de associação: classificar prompts como vagos ou contextualizados | Feedback com justificativa por item |
| 2.10 | Fechamento | Produto parcial e transição para o Módulo 3 | Ícone de arquivo analisado + texto de transição |

## Conteúdo Instrucional Enxuto

Um prompt é o texto que o participante digita no campo de entrada do assistente para orientar a resposta esperada. A qualidade da resposta depende diretamente da qualidade do prompt: quanto mais preciso e contextualizado for o texto de entrada, mais útil e específica será a resposta gerada. Um prompt que menciona apenas "o código" não informa ao assistente qual arquivo deve ser analisado, qual elemento específico é relevante nem qual aspecto se deseja investigar.

O Claude Code acessa automaticamente o conteúdo do arquivo que está em foco no editor — ou seja, aquele no qual o cursor está posicionado. Mesmo assim, recomenda-se sempre mencionar explicitamente o nome do arquivo e o nome da função ou trecho relevante no corpo do prompt. Essa prática reduz ambiguidades, especialmente quando há múltiplos arquivos abertos simultaneamente.

Um prompt contextualizado bem estruturado contém três elementos: (1) identificação do elemento de código — nome do arquivo e da função; (2) descrição do comportamento atual e do que se deseja entender; e (3) delimitação do escopo da resposta — se o participante deseja apenas uma explicação, uma análise de riscos ou uma sugestão de melhoria, sem autorização para modificar o arquivo.

## Demonstração Guiada

1. Abrir o VS Code e criar um novo arquivo com `Ctrl + N` (ou `Cmd + N`). Definir a linguagem como Python pelo comando `Change Language Mode` na paleta de comandos.
2. Inserir o código de referência da função `processar_notas()` e salvar o arquivo como `notas.py`.

   Captura de tela recomendada: VS Code com o arquivo `notas.py` aberto, mostrando o código completo da função e o nome do arquivo visível na aba superior.

3. Abrir o painel do Claude Code e enviar o prompt: "O que esse código faz?" Registrar a resposta (geralmente genérica ou com solicitação de mais detalhes).
4. Enviar em seguida o prompt contextualizado:

   "Tenho o arquivo notas.py aberto. Ele contém uma função chamada processar_notas(). Explique o que ela faz, passo a passo, como se eu nunca tivesse visto Python na vida."

   Captura de tela recomendada: painel do Claude Code com a resposta detalhada ao prompt contextualizado, com o arquivo `notas.py` visível ao fundo no editor.

5. Comparar as duas respostas e identificar as diferenças em nível de detalhe e utilidade.
6. Enviar o prompt de aprofundamento: "Essa função tem algum problema se eu passar uma lista vazia para ela? O que acontece?"
7. Enviar: "Como eu poderia corrigir esse problema? Não mexa no arquivo ainda — só me mostre como ficaria o código corrigido."
8. Resultado esperado: o assistente descreve o risco de divisão por zero com lista vazia e apresenta uma sugestão de correção sem alterar o arquivo.

## Atividade Hands-on

### Atividade prática — Formulação de prompts contextualizados (15 minutos)

Tarefa:
Criar o arquivo `notas.py`, enviar um prompt vago e um prompt contextualizado para a mesma função e registrar a diferença de qualidade nas respostas obtidas.

Procedimento:
1. Criar o arquivo `notas.py` no VS Code com o código de referência da função `processar_notas()`.
2. Enviar o prompt vago: "O que esse código faz?" e ler a resposta.
3. Enviar o prompt contextualizado mencionando o nome do arquivo, o nome da função e solicitando explicação passo a passo sem modificar o arquivo.
4. Enviar o prompt de aprofundamento sobre o comportamento com lista vazia e ler o diagnóstico do assistente.

Produto parcial esperado:
Arquivo `notas.py` criado e analisado pelo assistente, com o participante apto a formular prompts que identificam arquivo, elemento e escopo de forma explícita.

Critério de êxito:
O participante é capaz de formular um prompt contextualizado que obtém do assistente uma explicação detalhada da função `processar_notas()` e a identificação do risco com lista vazia — sem que nenhuma modificação seja aplicada ao arquivo.

## Checkpoint de Aprendizagem

**Questão de associação:**

Associe cada prompt à sua classificação correta (Vago ou Contextualizado):

| Prompt | Classificação |
|---|---|
| "O que esse código faz?" | ? |
| "Tenho o arquivo notas.py aberto com a função processar_notas(). Explique o que ela faz sem modificar o arquivo." | ? |
| "Melhore isso." | ? |
| "Analise a função processar_notas() no arquivo notas.py. Liste os problemas de legibilidade. Não mexa no código ainda." | ? |

**Gabarito:**

| Prompt | Classificação |
|---|---|
| "O que esse código faz?" | Vago |
| "Tenho o arquivo notas.py aberto com a função processar_notas(). Explique o que ela faz sem modificar o arquivo." | Contextualizado |
| "Melhore isso." | Vago |
| "Analise a função processar_notas() no arquivo notas.py. Liste os problemas de legibilidade. Não mexa no código ainda." | Contextualizado |

## Prompt ou Modelo Editável

Modelo de prompt contextualizado para análise de código:

```text
Tenho o arquivo [NOME DO ARQUIVO] aberto no editor.
Ele contém uma função chamada [NOME DA FUNÇÃO] que [DESCREVA O QUE ELA FAZ EM UMA FRASE].
Explique o que essa função faz, passo a passo, identificando possíveis problemas ou riscos.
Não modifique o arquivo ainda.
```

## Fechamento do Módulo

Neste módulo, o arquivo `notas.py` foi criado e analisado com o auxílio do assistente. O participante experimentou a diferença entre prompts vagos e contextualizados e passou a formular perguntas com os três elementos essenciais: identificação do arquivo, descrição do comportamento e delimitação do escopo. O Módulo 3 aproveitará esse arquivo e essa habilidade para introduzir o próximo nível: modificar o código com segurança, por meio do ciclo de revisão que impede alterações não compreendidas.

<div style="page-break-after: always;"></div>

# Módulo 3 — Refatoração com Revisão

## Encadeamento

O Módulo 3 parte do arquivo `notas.py` analisado no Módulo 2 e introduz a habilidade de modificar código de forma segura, mediante o ciclo Analisar → Planejar → Revisar → Aceitar.

## Finalidade Prática

Neste módulo, o participante solicitará ao assistente uma análise dos problemas de legibilidade do arquivo `notas.py`, revisará o plano de refatoração proposto, inspecionará o diff gerado e aceitará ou rejeitará as mudanças de forma consciente. O produto parcial é o arquivo `notas.py` refatorado, com type hints, docstring e tratamento do caso de lista vazia.

## Objetivos de Aprendizagem Prática

Ao final deste módulo, o participante deverá ser capaz de:

1. Solicitar ao assistente uma análise de problemas de legibilidade sem autorizar modificações no arquivo.
2. Revisar o plano de refatoração proposto pelo assistente e vetar etapas com as quais não concorda.
3. Interpretar o diff viewer do VS Code, identificando linhas removidas (vermelho, sinal `–`) e linhas adicionadas (verde, sinal `+`).
4. Aceitar ou rejeitar a refatoração proposta e, em caso de rejeição, solicitar uma nova proposta com parâmetros alterados.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 3.1 | Abertura do módulo | Título, foco prático e produto parcial | Ícone de ciclo com quatro setas rotuladas |
| 3.2 | Process block | Ciclo de quatro etapas: Analisar → Planejar → Revisar → Aceitar/Rejeitar | Diagrama de processo com etapas clicáveis e descrição de cada uma |
| 3.3 | Texto curto explicativo | O que são type hints e docstrings, com exemplos mínimos | Bloco de código comparativo: antes (sem) e depois (com) |
| 3.4 | Demonstração passo a passo | Envio do prompt de análise e leitura da lista de problemas | Captura de tela: resposta do Claude com lista de problemas identificados |
| 3.5 | Demonstração passo a passo | Envio do prompt de planejamento e revisão do plano proposto | Captura de tela: resposta do Claude com plano detalhado por etapas |
| 3.6 | Captura de tela anotada | Diff viewer do VS Code com linhas removidas (vermelho) e adicionadas (verde) | Captura de tela anotada com legendas: "linha removida", "linha adicionada", "botões Accept/Reject" |
| 3.7 | Atividade guiada | Execução completa do ciclo no arquivo `notas.py` | Captura de tela: arquivo `notas.py` após aceitação com docstring visível |
| 3.8 | Labeled graphic | Anatomia do diff viewer: linhas, símbolos e botões | Imagem interativa com hotspots explicativos |
| 3.9 | Knowledge check | Verdadeiro ou falso sobre o ciclo de refatoração | Feedback com justificativa |
| 3.10 | Fechamento | Produto parcial e transição para o Módulo 4 | Ícone de arquivo refatorado + texto de transição |

## Conteúdo Instrucional Enxuto

Refatoração é o processo de reescrever ou reorganizar um trecho de código sem alterar o seu comportamento externo. O código refatorado continua produzindo os mesmos resultados, porém de forma mais clara, mais organizada e mais fácil de manter. Esse tipo de modificação é frequente tanto em ambientes de desenvolvimento de software quanto em contextos acadêmicos nos quais scripts são produzidos e precisam ser compartilhados ou reutilizados.

O ciclo Analisar → Planejar → Revisar → Aceitar constitui o método seguro de refatoração assistida por IA. Sua lógica central é a de que nenhuma modificação deve ser aplicada ao arquivo sem que o participante compreenda e aprove o que está sendo feito. A etapa de revisão do diff — a visualização comparativa entre o código original e o código proposto — é o mecanismo que garante esse controle. Linhas em vermelho correspondem ao código que será removido; linhas em verde correspondem ao novo código que será inserido. Nenhuma alteração é efetivada até que o botão **Accept** seja clicado.

Type hints são anotações que indicam o tipo de dado esperado em cada parâmetro e no retorno de uma função (exemplo: `notas: list[float]`). Docstrings são comentários estruturados que descrevem o propósito da função, seus parâmetros e o valor retornado. Ambos aumentam a legibilidade e facilitam a compreensão do código por outros leitores — ou pelo próprio autor após um período sem contato com o material.

## Demonstração Guiada

1. Abrir o arquivo `notas.py` no VS Code e o painel do Claude Code.
2. Enviar o prompt de análise: "Analise a função processar_notas() no arquivo notas.py. Liste os problemas de legibilidade e organização que você encontrar. Não mexa no código ainda."

   Captura de tela recomendada: resposta do assistente com lista numerada de problemas identificados, incluindo ausência de type hints, docstring e tratamento de lista vazia.

3. Enviar o prompt de planejamento: "Mostre-me o plano de mudanças que você faria, passo a passo. Liste cada alteração e explique por que ela melhora o código. Ainda não aplique nada."
4. Ler o plano. Se houver alguma etapa que não seja desejada, enviá-la como exclusão: "Concordo com tudo, exceto [etapa]. Prossiga sem ela."
5. Enviar o prompt de execução: "Agora aplique as mudanças. Antes de confirmar, mostre-me o diff."

   Captura de tela recomendada: diff viewer do VS Code exibindo linhas removidas em vermelho com sinal `–` e linhas adicionadas em verde com sinal `+`, com os botões Accept e Reject visíveis no canto superior direito.

6. Ler cada linha do diff. Para cada mudança que não estiver clara, enviar: "Explique essa linha específica antes de eu aceitar."
7. Clicar em **Accept** após compreender e aprovar todas as alterações.
8. Resultado esperado: o arquivo `notas.py` contém a função refatorada com type hints, docstring e tratamento do caso de lista vazia.

   Captura de tela recomendada: arquivo `notas.py` após aceitação, mostrando a docstring visível abaixo do cabeçalho da função e as type hints nos parâmetros.

## Atividade Hands-on

### Atividade prática — Refatoração com ciclo de revisão (15 minutos)

Tarefa:
Executar o ciclo completo de refatoração no arquivo `notas.py`, analisando, planejando, revisando o diff e aceitando ou rejeitando cada mudança de forma consciente.

Procedimento:
1. Enviar o prompt de análise ao assistente e ler a lista de problemas de legibilidade identificados.
2. Solicitar o plano de mudanças e revisar cada etapa, vetando aquelas com as quais não se concorda.
3. Autorizar a execução das mudanças e solicitar o diff antes da confirmação.
4. Ler o diff linha a linha; solicitar explicação para qualquer mudança que não esteja clara.
5. Clicar em Accept após compreender e aprovar todas as alterações. Salvar o arquivo.

Produto parcial esperado:
Arquivo `notas.py` refatorado com type hints nos parâmetros e no retorno, docstring descrevendo a função, seus argumentos e seu retorno, e tratamento do caso de lista vazia.

Critério de êxito:
O arquivo `notas.py` salvo contém: (a) type hints na assinatura da função; (b) docstring com descrição, seção Args e seção Returns; (c) bloco condicional que retorna valores padrão quando a lista de entrada está vazia.

## Checkpoint de Aprendizagem

**Verdadeiro ou Falso:**

| Afirmação | V / F |
|---|---|
| O diff viewer aplica as mudanças automaticamente ao arquivo assim que é exibido. | ? |
| O participante pode rejeitar o diff e solicitar uma nova proposta com parâmetros diferentes. | ? |
| Type hints alteram o comportamento da função em tempo de execução. | ? |
| A docstring é um comentário estruturado que descreve o propósito da função. | ? |

**Gabarito:**

| Afirmação | Resposta |
|---|---|
| O diff viewer aplica as mudanças automaticamente ao arquivo assim que é exibido. | Falso — as mudanças só são aplicadas após o clique em Accept. |
| O participante pode rejeitar o diff e solicitar uma nova proposta com parâmetros diferentes. | Verdadeiro. |
| Type hints alteram o comportamento da função em tempo de execução. | Falso — são anotações informativas que não afetam a execução. |
| A docstring é um comentário estruturado que descreve o propósito da função. | Verdadeiro. |

## Prompt ou Modelo Editável

Modelo de prompt para o ciclo de refatoração:

```text
Analise a função [NOME DA FUNÇÃO] no arquivo [NOME DO ARQUIVO].
Liste os problemas de legibilidade, organização e robustez que você identificar.
Não modifique o arquivo ainda.

Em seguida, proponha um plano de refatoração que inclua:
1. Renomeação de variáveis, se necessário
2. Adição de type hints
3. Adição de docstring no estilo Google
4. Tratamento de entradas inválidas ou vazias

Após minha aprovação do plano, aplique as mudanças e mostre o diff antes de confirmar.
```

## Fechamento do Módulo

O arquivo `notas.py` está agora refatorado, documentado e mais robusto. O participante executou pela primeira vez o ciclo completo de refatoração assistida e comprovou que é possível aceitar sugestões de IA com compreensão e controle. No Módulo 4, o mesmo arquivo será utilizado em um novo cenário: um bug lógico será introduzido intencionalmente, e o participante aprenderá a descrevê-lo ao assistente, interpretar o diagnóstico e validar a correção antes de aplicá-la.

<div style="page-break-after: always;"></div>

# Módulo 4 — Depuração Assistida

## Encadeamento

O Módulo 4 parte do arquivo `notas.py` refatorado no Módulo 3 e aplica o mesmo ciclo de revisão a uma situação nova: a identificação e correção de um bug lógico real, com validação via terminal.

## Finalidade Prática

Neste módulo, o participante introduzirá um erro intencional no arquivo `notas.py`, observará o comportamento incorreto no terminal, descreverá o problema ao assistente com precisão, interpretará o diagnóstico recebido e aceitará a correção após revisão do diff. O produto parcial é o arquivo `notas.py` com o bug corrigido e o comportamento validado por teste no terminal.

## Objetivos de Aprendizagem Prática

Ao final deste módulo, o participante deverá ser capaz de:

1. Introduzir uma modificação intencional em um arquivo de código e identificar o comportamento incorreto resultante por meio de execução no terminal.
2. Formular um prompt de depuração que descreva o comportamento esperado, o comportamento obtido e o input de teste utilizado.
3. Interpretar o diagnóstico do assistente e confirmar que a causa raiz identificada faz sentido antes de autorizar a correção.
4. Validar a correção por meio de nova execução no terminal e comparar o resultado com o comportamento esperado.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 4.1 | Abertura do módulo | Título, foco prático e produto parcial | Ícone de bug + ícone de terminal |
| 4.2 | Texto curto explicativo | O que é um bug lógico e por que é mais difícil de detectar que um erro de sintaxe | Comparação: erro de sintaxe (programa não roda) × bug lógico (programa roda com resultado errado) |
| 4.3 | Demonstração passo a passo | Introdução do bug: troca de `>=` por `>` na condição de aprovação | Captura de tela: linha modificada no arquivo com o operador errado destacado |
| 4.4 | Demonstração passo a passo | Abertura do terminal integrado e execução do comando de teste | Captura de tela: terminal exibindo o resultado incorreto `(6.5, 2)` |
| 4.5 | Scenario block | Composição do prompt de depuração com os três elementos obrigatórios | Painel interativo: participante monta o prompt selecionando os elementos corretos |
| 4.6 | Demonstração passo a passo | Envio do prompt ao Claude e leitura do diagnóstico | Captura de tela: resposta do Claude identificando a condição `n > 6` como causa raiz |
| 4.7 | Demonstração passo a passo | Autorização da correção e revisão do diff | Captura de tela: diff mostrando apenas a troca de `>` por `>=` |
| 4.8 | Demonstração passo a passo | Nova execução no terminal e confirmação do resultado correto | Captura de tela: terminal exibindo o resultado correto `(6.5, 3)` |
| 4.9 | Checklist | Critérios de um bom prompt de depuração | Lista interativa com três itens marcáveis |
| 4.10 | Knowledge check | Questão de múltipla escolha sobre formulação de prompt de depuração | Feedback com explicação da resposta correta |
| 4.11 | Fechamento | Produto parcial e transição para o Módulo 5 | Ícone de terminal com resultado correto + texto de transição |

## Conteúdo Instrucional Enxuto

Um bug lógico é um erro em que o programa executa sem interrupção, mas produz um resultado incorreto. Diferentemente de um erro de sintaxe — que impede o programa de rodar e gera uma mensagem de erro explícita —, o bug lógico exige que o participante compare o resultado obtido com o resultado esperado para identificar que algo está errado. Esse tipo de erro é mais comum e, em geral, mais difícil de diagnosticar.

O terminal integrado do VS Code é o espaço onde o código é executado diretamente, permitindo observar o resultado real de uma função com um conjunto específico de entradas. Para abri-lo, utiliza-se o atalho `` Ctrl + ` `` (Windows e Linux) ou `` Cmd + ` `` (macOS). O comando de teste utilizado neste módulo — `python3 -c "..."` — executa uma instrução Python diretamente no terminal, sem a necessidade de criar um arquivo de teste separado.

Para obter um diagnóstico preciso do assistente, o prompt de depuração deve conter obrigatoriamente três elementos: (1) o input utilizado no teste — os dados que foram fornecidos à função; (2) o resultado esperado — o que deveria ter sido retornado; e (3) o resultado obtido — o que foi efetivamente retornado. Com esses três elementos, o assistente pode comparar o comportamento declarado com o código e identificar a discrepância com maior eficiência.

## Demonstração Guiada

1. Abrir `notas.py` no VS Code. Localizar a linha com a condição de aprovação (`n >= 6`) e alterar para `n > 6`. Salvar o arquivo.

   Captura de tela recomendada: linha modificada no editor com o operador `>` em destaque e o operador correto `>=` riscado ao lado, para contraste visual.

2. Abrir o terminal integrado com `` Ctrl + ` `` (ou `` Cmd + ` ``) e executar:

   `python3 -c "from notas import processar_notas; print(processar_notas([5, 6, 7, 8]))"`

   Captura de tela recomendada: terminal do VS Code exibindo o resultado incorreto `(6.5, 2)`, com destaque sobre o valor 2 e legenda indicando que o esperado era 3.

3. Abrir o painel do Claude Code e enviar o prompt de depuração:

   "Tenho o arquivo notas.py aberto. A função processar_notas() está retornando um resultado errado. Passei a lista [5, 6, 7, 8] e esperava o resultado (6.5, 3) — média 6,5 e 3 aprovados (notas 6, 7 e 8). Mas recebi (6.5, 2). Analise o código e aponte onde está o erro. Não corrija ainda."

   Captura de tela recomendada: resposta do Claude identificando a condição `n > 6` como causa da exclusão da nota exatamente igual a 6.

4. Ler o diagnóstico e confirmar que faz sentido. Enviar: "Corrija apenas a linha com a condição de aprovação. Mostre o diff antes de aplicar."
5. Revisar o diff — a única mudança deve ser a troca de `> 6` por `>= 6`. Aceitar.
6. Executar novamente o comando de teste no terminal.

   Captura de tela recomendada: terminal exibindo o resultado correto `(6.5, 3)`, com destaque sobre o valor 3.

7. Resultado esperado: o terminal retorna `(6.5, 3)`, confirmando que o bug foi eliminado.

## Atividade Hands-on

### Atividade prática — Diagnóstico e correção de bug lógico (15 minutos)

Tarefa:
Introduzir intencionalmente o bug lógico no arquivo `notas.py`, observar o comportamento incorreto no terminal, formular o prompt de depuração com os três elementos obrigatórios e corrigir o erro após revisão do diff.

Procedimento:
1. Localizar a linha de aprovação em `notas.py` e substituir `>= 6` por `> 6`. Salvar o arquivo.
2. Abrir o terminal integrado e executar o comando de teste com a lista `[5, 6, 7, 8]`. Registrar o resultado obtido.
3. Formular o prompt de depuração contendo: o nome do arquivo, o input de teste, o resultado esperado e o resultado obtido. Solicitar diagnóstico sem correção imediata.
4. Ler o diagnóstico do assistente. Confirmar que a causa raiz identificada faz sentido. Autorizar a correção e revisar o diff.
5. Aceitar a correção, salvar o arquivo e executar o comando de teste novamente para validar.

Produto parcial esperado:
Arquivo `notas.py` com o operador de aprovação restaurado para `>= 6` e comportamento validado por execução no terminal — resultado `(6.5, 3)` para a lista `[5, 6, 7, 8]`.

Critério de êxito:
A execução do comando de teste no terminal retorna `(6.5, 3)` após a correção, confirmando que a nota 6 volta a ser contabilizada como aprovada.

## Checkpoint de Aprendizagem

**Questão de múltipla escolha:**

Qual dos prompts a seguir está mais bem estruturado para obter um diagnóstico eficiente do assistente sobre um bug lógico?

(A) "Meu código está com erro. Pode ajudar?"

(B) "A função processar_notas() retornou (6.5, 2) quando passei a lista [5, 6, 7, 8]. Esperava (6.5, 3). Analise o arquivo notas.py aberto e aponte a causa do erro. Não corrija ainda."

(C) "Tem um bug. Corrija tudo."

(D) "O código não funciona. Reescreva a função do zero."

**Gabarito:** Alternativa (B).

**Fundamentação:** O prompt (B) contém os três elementos essenciais de um bom prompt de depuração: o input de teste, o resultado esperado e o resultado obtido. Além disso, delimita o escopo (diagnóstico sem correção imediata), o que permite ao participante validar o raciocínio do assistente antes de autorizar qualquer modificação. Os demais prompts são vagos, não fornecem informações para diagnóstico ou solicitam modificações sem revisão prévia.

## Prompt ou Modelo Editável

Modelo de prompt para depuração de bug lógico:

```text
Tenho o arquivo [NOME DO ARQUIVO] aberto.
A função [NOME DA FUNÇÃO] está retornando um resultado incorreto.

Input de teste utilizado: [DESCREVA O INPUT — ex.: lista [5, 6, 7, 8]]
Resultado esperado: [EX.: (6.5, 3)]
Resultado obtido: [EX.: (6.5, 2)]

Analise o código e aponte onde está o erro.
Não corrija ainda — apenas indique a causa raiz.
```

## Fechamento do Módulo

Neste módulo, o participante completou o repertório operacional do curso: instalação, formulação de prompts, refatoração com revisão e depuração assistida. O arquivo `notas.py` passou por todas as etapas de transformação — criado, analisado, refatorado e depurado — e está agora em um estado consistente e validado. O Módulo 5 apresentará um módulo de código inédito e mais complexo, exigindo que o participante aplique todas essas habilidades de forma autônoma e integrada para produzir a entrega final do curso.

<div style="page-break-after: always;"></div>

# Módulo 5 — Síntese e Aplicação Integrada

## Encadeamento

O Módulo 5 não introduz habilidades novas. Seu propósito é consolidar, em uma entrega única, todas as práticas desenvolvidas nos módulos anteriores, aplicando-as a um módulo de código inédito e mais complexo.

## Finalidade da Síntese

Neste módulo, o participante receberá o arquivo `turma.py` — um módulo com problemas de legibilidade, ausência de documentação, bug lógico e riscos com entradas inválidas — e deverá transformá-lo em uma versão limpa, documentada e validada, utilizando o Claude Code como copiloto em cada etapa. O produto final integra os quatro produtos parciais dos módulos anteriores: ambiente configurado, capacidade de formular prompts contextualizados, domínio do ciclo de refatoração e habilidade de depuração com validação.

## Roteiro de Telas para Articulate 360

| Tela | Tipo de bloco/interação | Conteúdo ou ação esperada | Recurso visual recomendado |
|---|---|---|---|
| 5.1 | Abertura do módulo | Título, missão e produto final esperado | Diagrama de síntese: quatro módulos convergindo para o produto final |
| 5.2 | Texto curto explicativo | Apresentação do arquivo `turma.py` e seus problemas | Bloco de código com o arquivo legado destacando os problemas (nomes ininteligíveis, ausência de docstrings, bug lógico) |
| 5.3 | Process block | Sequência de execução da atividade integradora: 5 etapas | Diagrama de processo numerado com ícones por etapa |
| 5.4 | Atividade guiada | Criação do arquivo `turma.py` e envio do prompt de leitura | Captura de tela: arquivo criado no VS Code com as funções `proc()` e `rel()` visíveis |
| 5.5 | Atividade guiada | Envio do prompt de diagnóstico completo | Captura de tela: resposta do Claude listando problemas identificados |
| 5.6 | Atividade guiada | Revisão e aprovação do plano de refatoração | Captura de tela: plano de refatoração proposto pelo assistente |
| 5.7 | Atividade guiada | Revisão do diff e aceitação das mudanças | Captura de tela: diff viewer com as alterações propostas |
| 5.8 | Atividade guiada | Geração e inserção do cabeçalho de módulo | Captura de tela: topo do arquivo `turma.py` com o cabeçalho gerado |
| 5.9 | Atividade guiada | Execução do teste no terminal e validação do resultado | Captura de tela: terminal com resultado coerente para as turmas de teste |
| 5.10 | Checklist | Critérios de conclusão da entrega final | Lista de 8 itens marcáveis |
| 5.11 | Download block | Modelo de cabeçalho de módulo editável | Arquivo de texto para download e adaptação |
| 5.12 | Encerramento | Competência consolidada e caminhos de aprofundamento | Ícone de conquista + texto de encerramento |

## Atividade Integradora

### Atividade integradora — Refatoração completa do módulo `turma.py` (20 minutos)

Tarefa:
Transformar o arquivo `turma.py` — um módulo legado com múltiplos problemas — em uma versão limpa, documentada e validada, aplicando de forma integrada e autônoma todas as habilidades desenvolvidas no curso.

Procedimento:
1. Criar o arquivo `turma.py` no VS Code com o código legado fornecido e enviar o prompt de leitura: "Tenho o arquivo turma.py aberto. Ele contém duas funções com nomes e variáveis pouco legíveis. Explique o que cada função faz, em linguagem simples, sem modificar nada."
2. Enviar o prompt de diagnóstico completo: "Agora liste todos os problemas de qualidade que você encontra: nomes ruins, bugs, ausência de documentação, riscos com entradas inválidas. Não corrija ainda." Ler a lista e identificar os problemas que fazem sentido.
3. Enviar o prompt de planejamento: "Proponha um plano de refatoração completo: nomes novos para as funções e variáveis, adição de type hints, tratamento de lista vazia e docstrings. Liste o plano antes de aplicar." Revisar e vetar etapas com as quais não se concorda.
4. Autorizar a execução das mudanças: "Aplique o plano completo. Mostre o diff antes de confirmar." Revisar o diff linha a linha e aceitar após compreender cada alteração.
5. Solicitar o cabeçalho de módulo: "Gere um cabeçalho de módulo para o arquivo turma.py com: descrição do que o módulo faz, exemplo de uso das duas funções e uma nota sobre o que fazer se a lista de entrada estiver vazia." Inserir o cabeçalho no topo do arquivo, salvar e executar o comando de teste no terminal para validar.

Produto final esperado:
Arquivo `turma.py` refatorado, contendo: funções com nomes descritivos; variáveis legíveis; type hints nos parâmetros e no retorno de ao menos uma função; docstring em ao menos uma função; tratamento do caso de lista vazia; cabeçalho de módulo com descrição, exemplos e nota de uso; comportamento validado por execução no terminal.

## Critérios de Avaliação

| Critério | Descrição | Atendido? |
|---|---|---|
| Legibilidade | O arquivo não contém variáveis de nome único (`x`, `r`, `d`, `i`, `t`, `m`, `ap`) | ☐ Sim / ☐ Não |
| Nomenclatura | As duas funções têm nomes que descrevem o que elas fazem | ☐ Sim / ☐ Não |
| Tipagem | Type hints estão presentes nos parâmetros e no retorno de ao menos uma função | ☐ Sim / ☐ Não |
| Documentação | Há docstring descritiva em ao menos uma função | ☐ Sim / ☐ Não |
| Robustez | O código trata o caso de lista vazia sem interromper a execução | ☐ Sim / ☐ Não |
| Completude | O cabeçalho de módulo está presente no topo do arquivo | ☐ Sim / ☐ Não |
| Validação | O teste no terminal retornou valores coerentes com as entradas fornecidas | ☐ Sim / ☐ Não |
| Compreensão | O participante é capaz de explicar, com suas próprias palavras, o que cada função faz | ☐ Sim / ☐ Não |

## Encerramento da Síntese

O Módulo 5 marca a consolidação da competência prática central do curso: a capacidade de utilizar o Claude Code como copiloto em um ciclo de trabalho que combina leitura assistida, refatoração com revisão e depuração com validação, mantendo o participante como responsável por cada decisão aplicada ao código. O produto final — o arquivo `turma.py` transformado — é evidência concreta de que essa competência foi desenvolvida e exercida de forma autônoma.

<div style="page-break-after: always;"></div>

# Orientações para Produção no Articulate 360

## Organização Visual

- Utilizar blocos curtos e progressivos, com no máximo uma ação principal por tela.
- Evitar telas com excesso de texto corrido; priorizar listas numeradas, checklists, tabelas e blocos de processo.
- Inserir capturas de tela em todas as etapas que envolvam interação com interface — botões, menus, janelas, painéis e resultados visuais.
- Utilizar anotações (setas, caixas de destaque, legendas) nas capturas de tela para indicar exatamente o elemento sobre o qual o participante deve agir.
- Manter consistência visual entre os módulos: mesma paleta de cores, tipografia e estilo de ícones.
- Reservar destaque visual (cor diferenciada, borda ou ícone) para alertas de segurança — em especial nas telas sobre manipulação da chave de API.

## Interações Recomendadas

- **Process blocks:** ciclo de refatoração (Módulo 3) e sequência de depuração (Módulo 4).
- **Tabs:** comparação entre prompt vago e prompt contextualizado (Módulo 2).
- **Accordion:** anatomia de um bom prompt (Módulo 2) e anatomia do diff viewer (Módulo 3).
- **Knowledge checks:** ao final de cada módulo, com feedback imediato e justificativa da resposta correta.
- **Checklists:** verificação de instalação (Módulo 1) e critérios da entrega final (Módulo 5).
- **Scenario blocks:** composição do prompt de depuração (Módulo 4) — o participante monta o prompt selecionando os elementos corretos em painel interativo.
- **Labeled graphics:** anatomia do diff viewer com hotspots interativos (Módulo 3).
- **Download blocks:** modelos editáveis de prompt (ao final de cada módulo) e modelo de cabeçalho de módulo (Módulo 5).

## Padrão de Linguagem das Telas

Cada tela deve conter:

- **Título curto:** identifica o foco da tela em até cinco palavras.
- **Instrução objetiva:** orienta a ação esperada do participante em uma frase.
- **Uma ação principal:** cada tela deve exigir ou apresentar apenas um elemento de atenção.
- **Feedback imediato:** sempre que houver interação (knowledge check, scenario, checklist), o feedback deve aparecer logo após a resposta do participante, com justificativa.
- **Indicação clara de avanço:** botão de continuação ou seta de próxima tela visíveis e destacados.

---

## Encerramento

O presente roteiro instrucional estabelece a estrutura completa para a implementação do curso "Claude Code no VS Code — Hands-on" na plataforma Articulate 360, organizando o percurso em quatro módulos práticos de progressão cumulativa e um módulo de síntese com entrega verificável. Cada módulo foi estruturado para gerar um produto parcial concreto — do ambiente configurado ao arquivo de código refatorado, documentado e validado —, garantindo que o participante acumule evidências de competência ao longo de todo o trajeto, e não apenas ao final.

Para que o aprendizado se consolide de forma duradoura, recomenda-se que o participante aplique o ciclo Analisar → Planejar → Revisar → Aceitar a arquivos reais de seu próprio contexto profissional ou acadêmico imediatamente após a conclusão do curso. O aprofundamento pode ocorrer pela exploração de funcionalidades não abordadas neste nível introdutório — entre elas, a geração de testes unitários assistida, a referência a múltiplos arquivos por meio da sintaxe `@nomearquivo` e o uso do terminal integrado para execução de pipelines de validação mais elaborados. A prática regular em situações reais é o fator determinante para a consolidação das competências desenvolvidas.

**Síntese:** A competência prática em IA aplicada ao código não se adquire pela leitura de conceitos, mas pelo exercício repetido do ciclo de revisão — formular, analisar, revisar e decidir — em situações reais e progressivamente mais complexas.
