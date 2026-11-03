# OpenAI Codex: Do Primeiro Prompt aos Fluxos Profissionais com Agentes de IA

> Roteiro completo de curso — versão reformulada a partir da auditoria crítica do roteiro original. Todas as lacunas identificadas (configuração inicial, diferenciação de clientes, execução local x nuvem, precisão sobre acesso à internet, recursos avançados subaproveitados e casos reais genéricos) foram incorporadas diretamente na estrutura abaixo.

---

## Visão Geral do Curso

### Objetivo Geral

Ao final deste curso, o aluno será capaz de instalar, configurar e operar o Codex em qualquer um de seus clientes (Web, CLI, IDE, Desktop), escrever prompts eficazes, delegar tarefas com segurança, revisar criticamente o trabalho de um agente, orientar o Codex com AGENTS.md, trabalhar com múltiplos agentes em paralelo e aplicar o Codex tanto a projetos de programação quanto a tarefas de conhecimento (pesquisa, dados, documentos, relatórios).

### O Aluno Será Capaz de

- explicar a diferença entre um chat de IA convencional e um agente de IA como o Codex;
- instalar e autenticar o Codex em qualquer cliente (Web, CLI, IDE, Desktop);
- conectar um repositório GitHub e configurar permissões corretamente;
- escrever prompts com objetivo, contexto, restrições e critérios de sucesso claros;
- decompor tarefas complexas em tarefas menores e delegá-las a múltiplos agentes em paralelo;
- criar e manter arquivos AGENTS.md eficazes;
- ler logs, testes e evidências para decidir quando aceitar, revisar ou re-testar uma alteração;
- aplicar boas práticas de segurança, privacidade e permissões (incluindo os riscos do acesso à internet);
- usar recursos avançados: Memória, Tarefas Agendadas, Browser/Modo de Desenvolvedor, Uso do Computador, Sites e Plugins;
- integrar o Codex ao fluxo de trabalho diário, individual ou em equipe;
- aplicar o Codex a tarefas de conhecimento além da programação (pesquisa, dados, documentos, educação, setor público);
- planejar e entregar um projeto completo utilizando delegação a agentes.

### Pré-requisitos

Nenhum conhecimento prévio obrigatório. Conhecimentos básicos de informática são suficientes para acompanhar todo o curso. Noções de programação e de linha de comando são recomendadas — mas não exigidas — para tirar o máximo proveito dos Módulos 3, 4 e 8.

### Perfil do Aluno

Iniciantes em IA agente, profissionais administrativos, pesquisadores, analistas de dados, estudantes, gestores, programadores e qualquer pessoa que deseje aprender a delegar trabalho a agentes de IA de forma segura e produtiva.

### Filosofia Pedagógica

Toda aula segue o mesmo ciclo, validado na auditoria anterior como uma boa prática a ser preservada:

```
Introdução curta → Conceito → Demonstração → Passo a passo →
Prints sugeridos → Hands-on (2–10 min) → Troubleshooting (quando aplicável) →
Boas práticas → Resumo → Próximos passos
```

O aluno nunca fica mais de dez minutos sem interagir de fato com o Codex — e, diferente do roteiro original, toda "pílula hands-on" envolve uma ação real na ferramenta, não apenas uma reflexão escrita.

### Convenções Usadas Neste Roteiro

| Ícone | Significado |
|---|---|
| 📸 | Sugestão de print — descreve exatamente o que deve aparecer na captura de tela |
| 💡 | Dica — boas práticas profissionais |
| ⚠️ | Atenção — cuidados importantes, más interpretações comuns |
| 🚀 | Produtividade — atalhos e estratégias para acelerar o trabalho |
| 🔒 | Segurança — privacidade, permissões e proteção de dados |
| 🔧 | Troubleshooting — sintoma, causa e solução |

---

## Estrutura Modular (Visão Geral)

| Módulo | Título | Nº de Aulas | Foco |
|---|---|---|---|
| 0 | Fundamentos e Configuração | 5 | Onboarding completo — lacuna crítica corrigida |
| 1 | Primeiro Contato com o Codex | 3 | Conceito de agente e ciclo básico de execução |
| 2 | Comunicação Eficaz com Agentes | 4 | Engenharia de prompts e decomposição de tarefas |
| 3 | Integrando a Projetos Reais | 5 | Bugs, features, documentação, GitHub e PRs |
| 4 | AGENTS.md | 4 | Orientação persistente do agente |
| 5 | Revisão Crítica | 3 | Logs, testes, evidências e confiança calibrada |
| 6 | Segurança, Privacidade e Limites | 4 | Sandbox, internet opcional, RBAC, dados |
| 7 | Recursos Avançados | 5 | Memória, Tarefas Agendadas, Browser, Computer Use, Sites/Plugins |
| 8 | Fluxos Profissionais e Automação | 4 | Rotina diária, automação, uso em equipe |
| 9 | Casos Reais Além da Programação | 5 | Pesquisa, dados, vendas, educação, acessibilidade |
| 10 | Projeto Final | 1 (multi-etapas) | Aplicação integrada de todo o conteúdo |

**Progressão pedagógica:** Introdução → Instalação e Configuração → Primeiras Tarefas → Integração com Projetos → Fluxos Profissionais → Automação → Agentes Especializados → Recursos Avançados → Casos Reais → Projeto Final. Nenhum conceito avançado é introduzido antes de seus fundamentos.

---

# Módulo 0 — Fundamentos e Configuração

### Objetivo do Módulo

Eliminar a principal lacuna identificada na auditoria: preparar o ambiente do aluno completamente antes de qualquer hands-on, incluindo diferenciação clara entre os clientes do Codex e entre execução local e em nuvem.

---

## Aula 0.1 — O que é o Codex e por que ele é diferente

### Introdução

Um chat de IA responde. Um agente de IA *trabalha*. Esta aula estabelece essa diferença antes de qualquer configuração técnica.

### Objetivos da Aula

- Entender o conceito de agente de IA versus chat conversacional.
- Compreender os pilares do Codex: execução independente, ambiente isolado, tarefas paralelas.

### Habilidades Esperadas

Ao final desta aula, o aluno será capaz de explicar, com suas próprias palavras, em que situação usaria um chat tradicional e em que situação delegaria uma tarefa ao Codex.

### Conceitos

- IA conversacional x IA agente.
- Execução independente em ambiente isolado (sandbox).
- Tarefas assíncronas: o Codex trabalha enquanto o aluno faz outra coisa.
- Evidências verificáveis: logs de terminal e resultados de teste como prova do trabalho realizado.

### Demonstração

O instrutor executa a mesma tarefa duas vezes: primeiro pedindo ao ChatGPT tradicional para "explicar como corrigir um bug", depois delegando ao Codex a tarefa real de "corrigir o bug no repositório X". A diferença de resultado (explicação x código corrigido, testado e pronto para revisão) é o núcleo da aula.

### 📸 Sugestão de Prints

- Tela dividida mostrando, à esquerda, uma conversa comum no ChatGPT respondendo uma pergunta sobre código; à direita, a interface do Codex com uma tarefa em execução, mostrando barra de progresso, arquivos sendo modificados e um log de terminal ao vivo.
- Destaque visual (seta ou contorno) sobre o botão "Gerar código" e sobre o botão "Perguntar" na barra lateral do Codex.

### Hands-on (5 min)

Sem precisar de conta configurada ainda: o aluno assiste a um vídeo de 2 minutos comparando as duas execuções e preenche uma tabela de 3 linhas com cenários do seu próprio dia a dia, classificando cada um como "Chat" ou "Codex".

> 💡 **Dica:** se a tarefa gera um artefato (código, documento, relatório) que precisa ser testado ou revisado, é trabalho para agente. Se é uma dúvida pontual, é trabalho para chat.

### Resumo da Aula

O Codex não é um chat mais esperto — é um executor de trabalho que roda de forma independente, com evidências verificáveis do que fez.

### Próximos Passos

Antes de usar o Codex, é preciso entender onde ele roda: os quatro clientes disponíveis.

---

## Aula 0.2 — Conhecendo os Clientes do Codex e a Diferença Local x Nuvem

### Introdução

Esta é a aula que corrige a maior ambiguidade do roteiro anterior: "o Codex" não é uma única interface. Existem quatro superfícies de acesso e dois modos de execução, cada um com implicações diferentes.

### Objetivos da Aula

- Diferenciar os quatro clientes oficiais: Web, CLI, extensão de IDE, aplicativo Desktop.
- Diferenciar **Codex Local** (CLI, IDE, Desktop) de **Codex Cloud** (tarefas delegadas em ambiente de nuvem gerenciado pela OpenAI).
- Saber qual cliente escolher para cada tipo de tarefa.

### Habilidades Esperadas

Ao final desta aula, o aluno será capaz de indicar corretamente qual cliente usar diante de um cenário dado (ex.: "quero delegar uma tarefa longa e continuar trabalhando" → Codex Cloud/Web ou Desktop; "quero editar um arquivo agora, no meu terminal" → CLI local).

### Conceitos

| Cliente | Onde roda | Execução | Melhor para |
|---|---|---|---|
| Codex na Web | Navegador | Nuvem | Delegar tarefas, acompanhar múltiplos agentes |
| Codex CLI | Terminal local | Local | Edição rápida, fluxo de desenvolvimento interativo |
| Extensão de IDE | VS Code e forks | Local | Trabalhar dentro do editor já em uso |
| App Desktop (modo Codex) | Aplicativo do ChatGPT | Local e Nuvem | Unifica os dois modos, Browser e Computer Use |

- **Codex Local:** cobre CLI, extensão de IDE e fluxos no Desktop — o código roda no dispositivo do usuário.
- **Codex Cloud:** cobre tarefas delegadas que rodam em ambiente isolado, pré-carregado com o repositório, na infraestrutura da OpenAI.
- Workspaces gerenciados podem controlar Codex Local e Codex Cloud separadamente (relevante para equipes — retomado no Módulo 6).

### 📸 Sugestão de Prints

- Diagrama (a ser desenhado pela equipe de design) com os quatro clientes ao redor de um círculo central "Codex", com setas indicando "Local" (CLI, IDE, Desktop) de um lado e "Nuvem" (tarefas delegadas) do outro.
- Captura de tela da barra lateral do ChatGPT mostrando o ícone do Codex, ao lado da tela do terminal com a CLI instalada e um trecho do VS Code com a extensão do Codex ativa no painel lateral.

### Hands-on (5 min)

O aluno acessa o Codex pela Web (sem precisar instalar nada ainda) e navega pelas opções "Gerar código" e "Perguntar", identificando na interface se está vendo uma execução local ou uma tarefa em nuvem.

> ⚠️ **Atenção:** tarefas na nuvem geralmente levam de 1 a 30 minutos, dependendo da complexidade — isso é esperado, não é lentidão do sistema.

### Resumo da Aula

Existem quatro portas de entrada para o mesmo agente, e escolher a porta certa evita confusão nas próximas aulas práticas.

### Próximos Passos

Com os clientes mapeados, o próximo passo é criar a conta e conectar o repositório de trabalho.

---

## Aula 0.3 — Criando Conta, Conectando o GitHub e Entendendo Planos e Limites

### Introdução

Esta aula resolve a segunda lacuna crítica da auditoria: nenhuma aula anterior ensinava a configurar conta antes do primeiro hands-on real.

### Objetivos da Aula

- Criar/entrar com a conta ChatGPT no cliente escolhido.
- Conectar um repositório do GitHub ao Codex.
- Entender planos disponíveis (Free, Go, Plus, Pro, Team, Enterprise, Edu) e como funciona o pool de uso agentivo.

### Habilidades Esperadas

Ao final desta aula, o aluno terá uma conta conectada, um repositório de teste vinculado, e saberá onde consultar seu consumo de uso.

### Conceitos

- O Codex está incluído nos planos do ChatGPT, incluindo Free e Go, com limites que variam por plano.
- Uso do Codex, ChatGPT Work e Workspace Agents compartilham o mesmo pool de uso agentivo — tarefas maiores e mais longas consomem mais.
- Termos de Uso e Política de Privacidade do ChatGPT (ou o contrato correspondente para Enterprise/Business) regem os dados compartilhados entre Codex e ChatGPT.

### Passo a Passo

1. Acessar `chatgpt.com` e entrar com a conta (ou criar uma nova).
2. Abrir o cliente Codex desejado (Web, Desktop, CLI ou extensão de IDE).
3. Seguir o fluxo de conexão com o GitHub: autorizar o acesso do Codex ao repositório de teste.
4. Acessar a página de uso do Codex para visualizar o limite disponível no plano atual.

### 📸 Sugestão de Prints

- Tela de login do ChatGPT com o campo de e-mail em destaque.
- Caixa de diálogo de autorização do GitHub, mostrando claramente quais permissões estão sendo concedidas (leitura/escrita de repositório) — com uma seta apontando para o botão "Autorizar".
- Tela de "Uso do Codex", mostrando a barra de consumo e o texto de redefinição do limite.

### Hands-on (8 min)

O aluno conecta um repositório próprio (ou um repositório de exemplo fornecido pelo curso) e confirma, na interface, que o Codex reconhece a estrutura de arquivos do projeto.

### 🔧 Troubleshooting

| Sintoma | Causa provável | Solução |
|---|---|---|
| Botão "Conectar GitHub" não aparece | Sessão do ChatGPT expirada | Sair e entrar novamente na conta |
| Repositório não aparece na lista | Permissão da organização do GitHub não concedida | Verificar configurações de acesso da organização no GitHub e reautorizar |
| Mensagem de limite atingido logo no início | Plano Free/Go com uso já consumido por outra atividade (Work, Workspace Agents) | Consultar a página de uso do Codex e considerar upgrade ou aguardar redefinição |

> 🔒 **Segurança:** revise sempre quais permissões está concedendo ao autorizar o GitHub — prefira repositórios de teste enquanto ainda está aprendendo.

### Resumo da Aula

Conta criada, repositório conectado e consumo de uso mapeado — a base está pronta para a primeira tarefa real.

### Próximos Passos

Agora é hora de instalar a CLI, para quem deseja o fluxo local de linha de comando.

---

## Aula 0.4 — Instalando e Autenticando a CLI (Windows, macOS e Linux)

### Introdução

A CLI é o cliente mais sensível a diferenças de sistema operacional — e o roteiro anterior não tratava disso. Esta aula cobre os três ambientes mais comuns entre os alunos.

### Objetivos da Aula

- Instalar a CLI do Codex no sistema operacional do aluno.
- Autenticar a CLI usando a conta do ChatGPT (sem precisar gerar token manualmente).

### Habilidades Esperadas

Ao final desta aula, o aluno executa o comando de verificação da CLI e recebe confirmação de autenticação bem-sucedida.

### Conceitos

- A CLI do Codex é um agente de programação leve e de código aberto, executado no terminal.
- Autenticação simplificada: basta iniciar sessão com a conta do ChatGPT e selecionar a organização de API desejada — o token é gerado e configurado automaticamente.
- Usuários Plus e Pro que autenticam a CLI via ChatGPT podem resgatar créditos promocionais de API por tempo limitado (verificar condições vigentes).

### Passo a Passo (por sistema operacional)

**Windows (PowerShell):**
1. Instalar o gerenciador de pacotes recomendado (ou baixar o instalador da CLI).
2. Executar o comando de instalação da CLI.
3. Executar o comando de login e seguir o fluxo de autenticação via navegador.

**macOS/Linux (terminal):**
1. Instalar via gerenciador de pacotes (ex.: Homebrew no macOS).
2. Executar o comando de instalação.
3. Executar o comando de login.

### 📸 Sugestão de Prints

- Terminal do Windows PowerShell mostrando o comando de instalação sendo executado, com o resultado de sucesso destacado.
- Tela do navegador aberta automaticamente pelo fluxo de login da CLI, mostrando a tela "Autorizar CLI do Codex" com o botão de confirmação em destaque.
- Terminal mostrando a mensagem final "Autenticado com sucesso" com o nome da organização selecionada.

### Hands-on (7 min)

O aluno instala a CLI, executa o login e roda um comando simples de verificação de versão para confirmar que a instalação foi concluída.

### 🔧 Troubleshooting

| Sintoma | Causa provável | Solução |
|---|---|---|
| Comando não reconhecido após instalação (Windows) | Variável de ambiente PATH não atualizada | Fechar e reabrir o terminal, ou adicionar manualmente o caminho de instalação ao PATH |
| Login trava no navegador | Bloqueador de pop-up ou sessão do ChatGPT expirada | Permitir pop-ups para o domínio do ChatGPT e tentar novamente |
| Erro de permissão ao instalar (macOS/Linux) | Falta de permissão de escrita no diretório padrão | Usar o gerenciador de pacotes recomendado em vez de instalação manual |

> 🚀 **Produtividade:** salve o comando de login como atalho — em máquinas compartilhadas, você pode alternar rapidamente entre organizações de API sem reconfigurar tudo manualmente.

### Resumo da Aula

A CLI está instalada e autenticada — o fluxo local de trabalho já está disponível, independentemente do sistema operacional.

### Próximos Passos

Falta configurar a extensão de IDE e o aplicativo Desktop, os outros dois clientes locais.

---

## Aula 0.5 — Configurando a Extensão de IDE e o Aplicativo Desktop

### Introdução

Encerrando o Módulo 0, o aluno configura os dois clientes restantes, cobrindo todas as formas de acesso apresentadas na Aula 0.2.

### Objetivos da Aula

- Instalar e autenticar a extensão do Codex no VS Code (ou fork compatível).
- Instalar e configurar o modo Codex no aplicativo Desktop do ChatGPT.

### Habilidades Esperadas

Ao final desta aula, o aluno terá os quatro clientes (Web, CLI, IDE, Desktop) configurados e prontos para uso.

### Conceitos

- A extensão Codex para VS Code é compatível com a maioria dos forks do VS Code; para outras IDEs, a alternativa é rodar a CLI no terminal integrado.
- O aplicativo Desktop do ChatGPT reúne, em um só lugar, o modo Codex, incluindo recursos exclusivos como Browser com Modo de Desenvolvedor e Gravar/Reproduzir (tratados no Módulo 7).

### Passo a Passo

1. Abrir a loja de extensões do VS Code e buscar "Codex".
2. Instalar e autenticar com a conta do ChatGPT já usada nas aulas anteriores.
3. Baixar e instalar o aplicativo Desktop do ChatGPT.
4. Ativar o "modo Codex" nas configurações do aplicativo e seguir o fluxo de login.

### 📸 Sugestão de Prints

- Painel de extensões do VS Code com "Codex" já instalado, ícone na barra lateral esquerda em destaque.
- Tela de configurações do aplicativo Desktop do ChatGPT, com o caminho `Configurações > Codex` visível e o toggle de ativação destacado.

### Hands-on (5 min)

O aluno abre um projeto local no VS Code, aciona o painel do Codex e envia uma pergunta simples sobre um arquivo do projeto ("o que este arquivo faz?"), confirmando que a extensão está funcional.

### 🔧 Troubleshooting

| Sintoma | Causa provável | Solução |
|---|---|---|
| Extensão não aparece no painel lateral | IDE é um fork não totalmente compatível | Usar a CLI no terminal integrado da IDE como alternativa |
| App Desktop não reconhece login | Cache de sessão corrompido | Sair da conta no app, limpar cache e autenticar novamente |

> 💡 **Dica:** use a extensão de IDE para edições rápidas e contextuais durante o desenvolvimento, e reserve o Codex Cloud (Web/Desktop) para tarefas mais longas que rodam em segundo plano.

### Resumo da Aula

Ambiente 100% configurado: conta, GitHub, CLI, IDE e Desktop. O Módulo 0 encerra a principal debilidade identificada na auditoria.

### Próximos Passos

Com tudo configurado, é hora do primeiro contato real com uma tarefa do Codex.

---

# Módulo 1 — Primeiro Contato com o Codex

### Objetivo do Módulo

Construir confiança inicial através de interações simples e reais, consolidando o entendimento do ciclo completo de execução.

---

## Aula 1.1 — Seu Primeiro Prompt: Perguntar x Gerar Código

### Objetivos da Aula

- Diferenciar os dois modos de interação do Codex: "Perguntar" (question) e "Gerar código" (code).
- Executar a primeira interação real com o agente.

### Habilidades Esperadas

Ao final desta aula, o aluno terá enviado pelo menos um prompt de cada tipo e interpretado corretamente a resposta.

### Conceitos

- "Perguntar": o Codex responde sobre a base de código sem alterar arquivos.
- "Gerar código": o Codex executa uma tarefa real, editando arquivos, rodando testes e produzindo um resultado verificável.

### Demonstração

O instrutor envia "Perguntar: o que faz a função X neste repositório?" e, em seguida, "Gerar código: adicione um comentário explicando a função X" — mostrando a diferença de comportamento e de tempo de resposta.

### 📸 Sugestão de Prints

- Interface do Codex com o campo de prompt e os dois botões ("Perguntar" e "Gerar código") lado a lado, com uma seta indicando a diferença de ícone entre eles.
- Resultado da pergunta (texto explicativo) versus resultado da geração de código (diff de arquivo com linhas adicionadas em verde).

### Hands-on (5 min)

No repositório de teste conectado na Aula 0.3, o aluno faz uma pergunta sobre um arquivo e depois pede uma alteração simples (ex.: adicionar um comentário ou renomear uma variável).

> 💡 **Dica:** comece sempre com "Perguntar" quando não conhece bem o código — isso reduz o risco de pedir uma alteração mal informada.

### Resumo da Aula

O Codex tem dois modos de interação bem distintos, e escolher o modo certo evita expectativas erradas sobre o resultado.

### Próximos Passos

Entender o que acontece "por trás" da tela enquanto o Codex executa uma tarefa de geração de código.

---

## Aula 1.2 — Como o Codex Trabalha: Ambiente Isolado, Logs e Testes

### Objetivos da Aula

- Entender o conceito de ambiente isolado (sandbox) pré-carregado com o repositório.
- Acompanhar o progresso de uma tarefa em tempo real.

### Habilidades Esperadas

Ao final desta aula, o aluno saberá localizar e interpretar o log de execução de uma tarefa em andamento.

### Conceitos

- Cada tarefa roda em um ambiente próprio, isolado e pré-configurado com o repositório.
- O Codex lê e edita arquivos, executa comandos como testes, linters e verificadores de tipo.
- Evidências verificáveis: citações de logs de terminal e resultados de teste comprovam cada ação tomada.

### Analogia

> Imagine contratar um estagiário extremamente competente e entregar a ele uma sala inteira só para trabalhar — com a porta de vidro, para você acompanhar tudo o que ele faz.

### 📸 Sugestão de Prints

- Tela de acompanhamento de tarefa em execução, mostrando: barra de progresso, lista de arquivos sendo modificados, painel de log de terminal com comandos sendo executados em tempo real.
- Zoom no trecho do log mostrando a execução de uma suíte de testes com resultado "passed"/"failed" destacado.

### Hands-on (6 min)

O aluno abre uma tarefa simples (ex.: "adicione um teste unitário para a função Y") e acompanha o log até a conclusão, identificando o momento em que os testes rodaram.

### 🔧 Troubleshooting

| Sintoma | Causa provável | Solução |
|---|---|---|
| Tarefa parece travada | Tarefas complexas podem levar até 30 minutos | Aguardar e verificar o log — a ausência de novas linhas por poucos minutos é normal em builds grandes |
| Log mostra erro de dependência ausente | Ambiente sandbox não tem a dependência pré-instalada | Adicionar a dependência ao script de configuração do ambiente (retomado no Módulo 4) |

### Resumo da Aula

Toda ação do Codex é auditável — logs e testes são a prova, não uma caixa-preta.

### Próximos Passos

Ver o ciclo completo, do prompt até a Pull Request.

---

## Aula 1.3 — O Fluxo Completo: do Prompt ao Pull Request

### Objetivos da Aula

- Visualizar o ciclo integral de uma tarefa: Prompt → Execução → Testes → Resultado → Revisão → Pull Request.

### Habilidades Esperadas

Ao final desta aula, o aluno executa uma pequena alteração de ponta a ponta, incluindo a abertura de uma Pull Request.

### Conceitos

```
Prompt → Execução → Testes → Resultado → Revisão → Pull Request
```

- Ao concluir, o Codex disponibiliza as alterações no próprio ambiente e oferece opções: revisar, pedir nova rodada, abrir PR no GitHub, ou integrar diretamente ao ambiente local.

### 📸 Sugestão de Prints

- Tela de conclusão de tarefa, com os botões "Ver alterações", "Pedir revisão", "Abrir Pull Request" visíveis e numerados na ordem do fluxo.
- Tela do GitHub mostrando a Pull Request recém-criada pelo Codex, com título, descrição automática e lista de arquivos alterados.

### Hands-on (8 min)

O aluno executa uma pequena alteração no projeto de teste e conclui o ciclo abrindo uma Pull Request real no repositório conectado.

> 🚀 **Produtividade:** revise o diff diretamente na interface do Codex antes de abrir a PR — é mais rápido que alternar para o GitHub a cada verificação.

### Resumo da Aula

O ciclo completo — do prompt à PR — já foi percorrido pelo aluno na prática, uma vez.

### Próximos Passos

Agora que o fluxo básico está dominado, o próximo módulo ensina a escrever prompts realmente eficazes.

---

# Módulo 2 — Comunicação Eficaz com Agentes

### Objetivo do Módulo

Desenvolver a habilidade central de qualquer usuário avançado de Codex: comunicar-se com precisão com um agente de IA.

---

## Aula 2.1 — Anatomia de um Bom Prompt

### Objetivos da Aula

- Identificar os quatro elementos de um prompt eficaz: objetivo, contexto, restrições, critérios de sucesso.

### Habilidades Esperadas

Ao final desta aula, o aluno escreve um prompt contendo, de forma explícita, os quatro elementos.

### Conceitos

- **Objetivo:** o que deve ser feito, de forma específica.
- **Contexto:** onde, em qual arquivo, módulo ou fluxo.
- **Restrições:** o que não deve ser alterado, estilo a seguir, dependências permitidas.
- **Critérios de sucesso:** como saber que a tarefa foi concluída corretamente (ex.: "todos os testes devem passar").

### 📸 Sugestão de Prints

- Um prompt real anotado, com cada trecho colorido e rotulado ("Objetivo", "Contexto", "Restrição", "Critério de sucesso") sobre a própria caixa de texto do Codex.

### Hands-on (5 min)

O aluno reescreve um prompt vago fornecido pelo curso, marcando explicitamente onde incluiu cada um dos quatro elementos.

> 💡 **Dica:** um prompt sem critério de sucesso deixa o Codex "adivinhando" quando parar — sempre inclua um.

### Resumo da Aula

Um prompt eficaz reduz retrabalho porque elimina ambiguidade antes mesmo da execução.

### Próximos Passos

Comparar, na prática, um prompt ruim, um médio e um excelente.

---

## Aula 2.2 — Prompt Ruim, Médio e Excelente na Prática

### Objetivos da Aula

- Comparar resultados reais gerados por três níveis de qualidade de prompt.

### Habilidades Esperadas

Ao final desta aula, o aluno identifica, olhando apenas para um prompt, se ele tende a gerar um resultado ambíguo ou preciso.

### Demonstração

| Nível | Prompt | Resultado típico |
|---|---|---|
| Ruim | "Conserte o bug." | Codex pode não localizar o bug certo, ou perguntar detalhes, consumindo tempo |
| Médio | "Corrija o bug de login que ocorre no arquivo `auth.py`." | Localiza o arquivo, mas pode não saber qual comportamento é o esperado |
| Excelente | "No arquivo `auth.py`, o login falha quando o e-mail contém maiúsculas. Corrija normalizando o e-mail para minúsculas antes da comparação. Critério de sucesso: todos os testes em `test_auth.py` devem passar." | Resultado preciso, testável e revisável de imediato |

### 📸 Sugestão de Prints

- Três capturas de tela lado a lado mostrando o mesmo repositório recebendo os três prompts, com o tempo de execução e o resultado (diff) de cada um visíveis.

### Hands-on (7 min)

O aluno envia os três níveis de prompt (fornecidos pelo curso) para o mesmo bug em um repositório de exemplo e compara os três resultados obtidos.

> ⚠️ **Atenção:** prompts vagos não geram necessariamente resultados errados — mas aumentam a chance de retrabalho e de decisões arbitrárias do agente.

### Resumo da Aula

A diferença entre um prompt médio e um excelente é medida em minutos economizados de revisão e correção.

### Próximos Passos

Prompts excelentes ainda não resolvem tarefas grandes demais — é preciso saber dividi-las.

---

## Aula 2.3 — Dividindo Tarefas Grandes em Tarefas Pequenas

### Objetivos da Aula

- Aplicar a técnica de decomposição de tarefas complexas.

### Habilidades Esperadas

Ao final desta aula, o aluno divide um projeto fictício em pelo menos cinco tarefas menores, cada uma com escopo bem definido.

### Analogia

> Você não pede a um pedreiro para "construir uma casa inteira" de uma vez — você pede a fundação, depois as paredes, depois o telhado.

### Conceitos

- Tarefas com escopo bem definido são executadas com mais precisão e são mais fáceis de revisar.
- Tarefas grandes demais aumentam o risco de resultados parciais ou decisões arbitrárias do agente.

### 📸 Sugestão de Prints

- Quadro (Kanban simples) com uma tarefa grande no topo ("Criar sistema de cadastro de usuários") sendo desmembrada em 5 cartões menores abaixo ("Criar modelo de dados", "Criar endpoint de cadastro", "Criar validação de e-mail", "Escrever testes", "Escrever documentação").

### Hands-on (8 min)

O aluno recebe a descrição de um projeto fictício e escreve cinco prompts menores, cada um seguindo a estrutura da Aula 2.1.

> 🚀 **Produtividade:** tarefas pequenas e bem definidas também são mais fáceis de rodar em paralelo — tema da próxima aula.

### Resumo da Aula

Decompor bem uma tarefa é o que torna viável delegar trabalho complexo com segurança.

### Próximos Passos

Com tarefas pequenas em mãos, é hora de rodar várias delas ao mesmo tempo.

---

## Aula 2.4 — Múltiplos Agentes em Paralelo

### Objetivos da Aula

- Executar mais de uma tarefa do Codex simultaneamente.
- Entender por que este é um dos maiores diferenciais do Codex frente a um assistente de chat único.

### Habilidades Esperadas

Ao final desta aula, o aluno terá pelo menos duas tarefas rodando ao mesmo tempo no mesmo repositório (ou em repositórios diferentes).

### Conceitos

- Cada tarefa roda em seu próprio ambiente isolado — por isso, várias podem ser executadas ao mesmo tempo sem conflito.
- Uso real documentado: mais da metade dos usuários avançados do Codex mantém mais de uma tarefa em execução simultânea ao longo do dia — o usuário passa a atuar como orquestrador de fluxos de trabalho, não como executor de uma tarefa por vez.

### Exemplo

| Agente | Tarefa |
|---|---|
| Agente 1 | Corrige testes que estão falhando |
| Agente 2 | Escreve documentação do módulo X |
| Agente 3 | Refatora uma função duplicada |
| Agente 4 | Investiga a causa de um bug relatado |

### 📸 Sugestão de Prints

- Painel do Codex mostrando quatro tarefas em cartões simultâneos, cada um com seu próprio status (executando, testando, concluído, aguardando revisão).

### Hands-on (8 min)

O aluno planeja e dispara quatro tarefas paralelas para o projeto fictício da Aula 2.3, acompanhando o painel de status de todas ao mesmo tempo.

> 💡 **Dica:** atribua tarefas com escopo bem definido a vários agentes simultâneos — e experimente tipos diferentes de tarefa para descobrir os limites reais do modelo no seu contexto.

### Resumo da Aula

Trabalhar em paralelo é o que transforma um usuário individual em algo próximo de uma pequena equipe de execução.

### Próximos Passos

Sair dos exemplos fictícios e aplicar tudo isso a um projeto real.

---

# Módulo 3 — Integrando o Codex a Projetos Reais

### Objetivo do Módulo

Ganhar confiança prática com tarefas reais de manutenção e evolução de código, incluindo o fluxo completo com o GitHub.

---

## Aula 3.1 — Conectando um Repositório Existente

### Objetivos da Aula

- Conectar um repositório real (não mais o de teste) e revisar suas permissões.

### Habilidades Esperadas

Ao final desta aula, o aluno terá um repositório real do seu trabalho ou estudo conectado e configurado corretamente.

### Conceitos

- Permissões de leitura/escrita concedidas ao Codex no GitHub.
- Script de configuração de ambiente: dependências pré-instaladas que o Codex poderá usar durante a execução (aprofundado no Módulo 4).

### 📸 Sugestão de Prints

- Tela de configurações do repositório no GitHub mostrando o app do Codex instalado, com as permissões concedidas listadas.

### Hands-on (6 min)

O aluno conecta um repositório próprio (pessoal ou de estudo) e confirma que o Codex consegue listar corretamente sua estrutura de pastas.

> 🔒 **Segurança:** revise periodicamente quais repositórios têm o Codex conectado, especialmente em contas usadas para projetos sensíveis.

### Resumo da Aula

Repositório real conectado — o curso agora trabalha com o contexto de trabalho do próprio aluno.

### Próximos Passos

Primeira tarefa real: corrigir um bug.

---

## Aula 3.2 — Corrigindo um Bug Real

### Objetivos da Aula

- Aplicar o ciclo completo (prompt → execução → resultado → validação) a um bug real ou proposital.

### Habilidades Esperadas

Ao final desta aula, o aluno corrige um bug de ponta a ponta e valida o resultado com testes.

### Passo a Passo

1. Identificar e descrever o bug com precisão.
2. Escrever o prompt seguindo a estrutura da Aula 2.1.
3. Acompanhar a execução e os testes.
4. Validar manualmente o resultado antes de aceitar.

### 📸 Sugestão de Prints

- Diff mostrando a linha de código corrigida, com o resultado do teste que antes falhava agora passando (indicador verde).

### Hands-on (8 min)

O aluno corrige um bug proposital fornecido pelo curso (ou um bug real de seu próprio repositório).

### 🔧 Troubleshooting

| Sintoma | Causa provável | Solução |
|---|---|---|
| Codex "corrige" o sintoma, não a causa | Prompt não descreveu o comportamento esperado | Reescrever o prompt incluindo o comportamento correto esperado, não apenas o erro observado |
| Testes continuam falhando após a correção | Script de configuração do ambiente não instalou todas as dependências | Revisar o script de configuração (Módulo 4) |

### Resumo da Aula

Corrigir um bug real reforça, na prática, todo o ciclo ensinado desde o Módulo 1.

### Próximos Passos

Ir além da correção: criar algo novo.

---

## Aula 3.3 — Criando um Recurso Novo

### Objetivos da Aula

- Solicitar, revisar e aceitar uma funcionalidade nova.

### Habilidades Esperadas

Ao final desta aula, o aluno adiciona uma função simples ao projeto e a revisa antes de aceitar.

### Passo a Passo

1. Descrever a funcionalidade desejada com objetivo, contexto, restrições e critério de sucesso.
2. Acompanhar a execução.
3. Revisar o código gerado antes de integrar.
4. Aceitar ou solicitar ajustes.

### 📸 Sugestão de Prints

- Tela de revisão de código do Codex mostrando o botão "Solicitar ajustes" ao lado do botão "Aceitar", com o diff completo da nova função visível acima.

### Hands-on (8 min)

O aluno adiciona uma função simples (ex.: um novo endpoint, um novo cálculo, uma nova seção de relatório) ao projeto conectado.

> 💡 **Dica:** peça sempre para o Codex incluir testes junto com a nova funcionalidade — isso já embute a validação no próprio resultado.

### Resumo da Aula

Criar algo novo segue o mesmo ciclo de corrigir algo quebrado — a diferença está na clareza do critério de sucesso.

### Próximos Passos

Uma tarefa frequentemente esquecida: documentação.

---

## Aula 3.4 — Gerando Documentação Automaticamente

### Objetivos da Aula

- Usar o Codex para gerar README, comentários e explicações técnicas.

### Habilidades Esperadas

Ao final desta aula, o aluno gera a documentação de um pequeno projeto e avalia sua qualidade.

### Conceitos

- README como porta de entrada de qualquer projeto.
- Comentários explicando o "porquê", não o "o quê" (boa prática também para revisão humana, não só para o Codex).

### 📸 Sugestão de Prints

- Comparação antes/depois de um `README.md` — vazio ou incompleto à esquerda, gerado e estruturado (instalação, uso, exemplos) à direita.

### Hands-on (7 min)

O aluno pede ao Codex para gerar (ou atualizar) o `README.md` do projeto conectado.

> ⚠️ **Atenção:** documentação gerada automaticamente também precisa de revisão humana — verifique se reflete o comportamento real do sistema.

### Resumo da Aula

Documentação deixa de ser a tarefa "para depois" quando pode ser delegada com o mesmo rigor de uma correção de bug.

### Próximos Passos

Fechar o ciclo do módulo revisando e abrindo Pull Requests de forma profissional.

---

## Aula 3.5 — Abrindo e Revisando Pull Requests no GitHub

### Objetivos da Aula

- Entender o fluxo técnico completo de uma Pull Request gerada pelo Codex.

### Habilidades Esperadas

Ao final desta aula, o aluno abre uma PR a partir de uma tarefa do Codex, revisa o conteúdo no GitHub e a aprova (ou solicita alterações).

### Passo a Passo

1. Concluir uma tarefa no Codex.
2. Selecionar "Abrir Pull Request".
3. No GitHub, revisar a descrição gerada automaticamente, o diff completo e o resultado dos checks de CI (se configurados).
4. Aprovar, comentar ou solicitar alterações.

### 📸 Sugestão de Prints

- Tela da Pull Request no GitHub com a descrição gerada pelo Codex, a lista de arquivos alterados, e o status dos checks de CI (verde/vermelho) visíveis.

### Hands-on (8 min)

O aluno completa o ciclo: da tarefa no Codex até a aprovação (ou solicitação de mudanças) da PR no GitHub.

### 🔧 Troubleshooting

| Sintoma | Causa provável | Solução |
|---|---|---|
| Botão "Abrir Pull Request" desabilitado | Repositório conectado sem permissão de escrita | Revisar as permissões concedidas na Aula 3.1 |
| PR aberta sem descrição completa | Prompt original não tinha contexto suficiente | Editar manualmente a descrição da PR antes de solicitar revisão de terceiros |

### Resumo da Aula

O ciclo prompt → PR está completo e testado na prática — o aluno já concluiu, sozinho, um fluxo real de contribuição de código.

### Próximos Passos

Aprender a orientar o Codex de forma permanente com o AGENTS.md.

---

# Módulo 4 — AGENTS.md

### Objetivo do Módulo

Ensinar o aluno a instruir o Codex de forma persistente, reduzindo ambiguidade em todas as tarefas futuras.

---

## Aula 4.1 — O que é e Por Que Importa

### Objetivos da Aula

- Entender o papel do arquivo AGENTS.md como guia permanente do agente.

### Habilidades Esperadas

Ao final desta aula, o aluno lê um AGENTS.md real e identifica suas seções principais.

### Analogia

> Novo funcionário → manual da empresa → muito menos erros. O AGENTS.md é o manual da empresa entregue ao Codex antes mesmo de sua primeira tarefa.

### Conceitos

- AGENTS.md, assim como um README.md, informa ao Codex como navegar pela base de código, quais comandos usar em testes e como seguir os padrões do projeto.
- O desempenho do Codex melhora com ambientes bem definidos, configurações de teste confiáveis e documentação clara — mas o modelo também tem desempenho sólido mesmo sem AGENTS.md, especialmente em bases de código simples.

### 📸 Sugestão de Prints

- Um arquivo `AGENTS.md` real aberto no editor, com as seções "Comandos", "Testes", "Convenções" e "Arquitetura" destacadas com cores diferentes.

### Hands-on (5 min)

O aluno lê um AGENTS.md de exemplo fornecido pelo curso e responde: "que erro este arquivo provavelmente evita?"

### Resumo da Aula

Um bom AGENTS.md transforma instruções repetidas em prompts em uma configuração permanente do projeto.

### Próximos Passos

Entender a anatomia de um AGENTS.md eficaz antes de criar o seu.

---

## Aula 4.2 — Anatomia de um AGENTS.md Eficaz

### Objetivos da Aula

- Identificar os quatro blocos de conteúdo essenciais de um bom AGENTS.md.

### Habilidades Esperadas

Ao final desta aula, o aluno consegue apontar, em qualquer AGENTS.md, onde estão (ou faltam) esses quatro blocos.

### Conceitos

- **Comandos:** como rodar o projeto, instalar dependências, iniciar o servidor local.
- **Testes:** como rodar a suíte de testes e o que é considerado sucesso.
- **Convenções:** estilo de código, nomenclatura, padrões do time.
- **Arquitetura:** visão geral de como as partes do sistema se conectam.

### 📸 Sugestão de Prints

- Template em branco de AGENTS.md com os quatro blocos como títulos de seção, ao lado de um exemplo preenchido lado a lado.

### Hands-on (6 min)

O aluno avalia dois AGENTS.md fornecidos pelo curso (um completo, um incompleto) e lista o que falta no segundo.

> 💡 **Dica:** comece pequeno — um AGENTS.md com apenas "Comandos" e "Testes" já reduz retrabalho significativamente frente a nenhum arquivo.

### Resumo da Aula

Um AGENTS.md eficaz não precisa ser extenso — precisa cobrir o que o agente mais frequentemente erraria sem essa informação.

### Próximos Passos

Criar o primeiro AGENTS.md do zero.

---

## Aula 4.3 — Criando seu Primeiro AGENTS.md (com `/init`)

### Objetivos da Aula

- Gerar um scaffold inicial de AGENTS.md usando o comando `/init`.
- Editá-lo manualmente para refletir as particularidades do projeto.

### Habilidades Esperadas

Ao final desta aula, o aluno terá um AGENTS.md funcional no repositório conectado.

### Passo a Passo

1. No aplicativo Desktop (ou CLI), executar o comando `/init` dentro do projeto conectado.
2. Revisar o scaffold gerado automaticamente pelo Codex.
3. Ajustar manualmente comandos, testes e convenções que o scaffold não capturou corretamente.
4. Commitar o arquivo no repositório.

### 📸 Sugestão de Prints

- Terminal ou app Desktop mostrando o comando `/init` sendo executado, seguido do arquivo `AGENTS.md` recém-criado se abrindo automaticamente no editor.

### Hands-on (8 min)

O aluno executa `/init` no projeto conectado desde a Aula 3.1 e ajusta manualmente ao menos uma seção do resultado.

> 🚀 **Produtividade:** `/init` usa o mesmo fluxo de inicialização da CLI — é a forma mais rápida de começar, mesmo que o resultado precise de ajustes manuais depois.

### Resumo da Aula

Criar um AGENTS.md do zero leva minutos com `/init`; refiná-lo é o trabalho que realmente reduz erros futuros.

### Próximos Passos

Escalar essa prática para projetos grandes, com múltiplos módulos.

---

## Aula 4.4 — AGENTS.md em Projetos Grandes e Monorepos

### Objetivos da Aula

- Entender como organizar múltiplos arquivos AGENTS.md em projetos com vários módulos ou monorepos.

### Habilidades Esperadas

Ao final desta aula, o aluno planeja a hierarquia de AGENTS.md para um projeto fictício com três módulos distintos.

### Conceitos

- É possível ter um AGENTS.md na raiz do repositório (regras gerais) e AGENTS.md específicos em subpastas (regras locais que complementam ou sobrepõem as gerais).
- Útil quando diferentes partes do projeto têm stacks, convenções ou comandos de teste diferentes (ex.: back-end em Python, front-end em TypeScript).

### 📸 Sugestão de Prints

- Árvore de diretórios de um monorepo fictício, com um `AGENTS.md` na raiz e outros dois em `backend/` e `frontend/`, cada um com um ícone de destaque.

### Hands-on (7 min)

O aluno desenha (em texto) a estrutura de AGENTS.md que criaria para um projeto fictício com back-end, front-end e infraestrutura.

> ⚠️ **Atenção:** AGENTS.md desatualizado é pior do que a ausência dele — revise o arquivo sempre que convenções do projeto mudarem.

### Resumo da Aula

Projetos grandes se beneficiam de AGENTS.md em camadas, não de um único arquivo genérico tentando cobrir tudo.

### Próximos Passos

Com o agente bem orientado, o próximo passo é aprender a revisar criticamente o que ele entrega.

---

# Módulo 5 — Revisão Crítica

### Objetivo do Módulo

Reforçar que IA não substitui revisão humana — e ensinar como revisar com eficiência.

---

## Aula 5.1 — Lendo Logs, Testes e Evidências

### Objetivos da Aula

- Interpretar corretamente logs de terminal, resultados de teste e outras evidências deixadas pelo Codex.

### Habilidades Esperadas

Ao final desta aula, o aluno localiza, em um log real, o ponto exato onde ocorreu uma falha.

### Conceitos

- O Codex relata explicitamente incertezas ou falhas de teste — essas mensagens não devem ser ignoradas.
- Evidências existem justamente para permitir decisões informadas, não para serem apenas "confirmadas".

### 📸 Sugestão de Prints

- Log de terminal real com uma linha de erro destacada em vermelho e uma anotação lateral explicando o que ela significa.

### Hands-on (6 min)

O aluno recebe um log com uma falha de teste proposital e identifica a linha exata e a causa provável.

### Resumo da Aula

Um log bem lido economiza rodadas inteiras de correção desnecessária.

### Próximos Passos

Saber quando aceitar, revisar mais a fundo, ou pedir mais testes.

---

## Aula 5.2 — Quando Aceitar, Revisar ou Testar Mais

### Objetivos da Aula

- Aplicar critérios objetivos para decidir o nível de escrutínio necessário para cada entrega.

### Habilidades Esperadas

Ao final desta aula, o aluno classifica corretamente três cenários fornecidos como "pode aceitar", "deve revisar" ou "precisa testar mais".

### Conceitos

```
Pode aceitar → deve revisar → precisa testar mais
```

- Fatores que aumentam a necessidade de revisão: mudanças em áreas críticas (autenticação, pagamentos, dados sensíveis), testes insuficientes, tarefas com prompt ambíguo.

### 📸 Sugestão de Prints

- Fluxograma de decisão simples (semáforo verde/amarelo/vermelho) aplicado a três exemplos de PR.

### Hands-on (7 min)

O aluno classifica três Pull Requests fictícias fornecidas pelo curso segundo o critério acima.

> 🔒 **Segurança:** mudanças em autenticação, permissões ou manipulação de dados sensíveis sempre exigem revisão manual completa, independentemente da confiança no resultado.

### Resumo da Aula

Nem toda entrega exige o mesmo nível de escrutínio — mas toda entrega exige algum nível.

### Próximos Passos

Conhecer os erros mais comuns cometidos por quem revisa agentes de IA.

---

## Aula 5.3 — Erros Comuns de Revisão

### Objetivos da Aula

- Reconhecer e evitar os três erros mais frequentes ao revisar trabalho de agentes.

### Habilidades Esperadas

Ao final desta aula, o aluno audita uma PR real (própria ou de exemplo) aplicando checklist de revisão.

### Conceitos (Erros Comuns)

- Aceitar tudo automaticamente, sem ler o diff.
- Ignorar testes que falharam "porque provavelmente não é nada importante".
- Não revisar as alterações antes de integrar ao ambiente de produção.

### 📸 Sugestão de Prints

- Checklist visual de revisão com as quatro perguntas: "Rodou testes? Conferiu arquivos? Entende a mudança? Revisou segurança?" — cada uma com uma caixa de marcação.

### Hands-on (8 min)

O aluno revisa uma Pull Request real (do próprio repositório ou de exemplo) aplicando o checklist completo.

### Resumo da Aula

Revisão criteriosa é a etapa que transforma velocidade de execução em confiabilidade de entrega.

### Próximos Passos

Aprofundar segurança, privacidade e limites da plataforma.

---

# Módulo 6 — Segurança, Privacidade e Limites

### Objetivo do Módulo

Corrigir a principal imprecisão técnica identificada na auditoria (acesso à internet) e cobrir controles empresariais de forma completa.

---

## Aula 6.1 — Modelo de Segurança: Sandbox e Acesso à Internet Opcional

### Objetivos da Aula

- Entender o modelo de execução em ambiente isolado (sandbox).
- Entender que o acesso à internet durante tarefas é **opcional e configurável** pelo usuário — não uma proibição absoluta.

### Habilidades Esperadas

Ao final desta aula, o aluno decide corretamente, diante de um cenário dado, se deve habilitar ou não o acesso à internet para uma tarefa específica.

### Conceitos

- Por padrão, o agente do Codex opera em um ambiente de nuvem isolado, com acesso limitado ao código fornecido pelo repositório e às dependências pré-instaladas via script de configuração.
- **Atualização relevante:** usuários já podem permitir que o Codex acesse a internet durante a execução de tarefas específicas — isso amplia capacidades (ex.: consultar documentação externa, baixar pacotes), mas também amplia a superfície de risco.
- Riscos ao habilitar internet: exposição a conteúdo externo não confiável (risco de instruções maliciosas embutidas em páginas — *prompt injection*), possibilidade de exfiltração de dados se mal configurado.

### 📸 Sugestão de Prints

- Tela de configuração da tarefa mostrando o toggle "Permitir acesso à internet" desativado por padrão, com um ícone de aviso ao lado explicando a implicação de ativá-lo.

### Hands-on (6 min)

O aluno analisa três cenários fornecidos (ex.: "corrigir um bug local", "buscar a versão mais recente de uma biblioteca externa", "processar dados sensíveis de clientes") e decide, para cada um, se habilitaria o acesso à internet.

> 🔒 **Segurança:** habilite o acesso à internet apenas quando a tarefa exigir explicitamente, e nunca em tarefas que envolvam dados sensíveis ou credenciais.

> ⚠️ **Atenção:** "o Codex não acessa a internet" deixou de ser uma regra absoluta — trate-a como uma configuração a ser avaliada tarefa a tarefa, não como uma garantia permanente.

### Resumo da Aula

O modelo de segurança do Codex é sandbox-por-padrão, com internet como exceção configurável e consciente — não uma regra fixa.

### Próximos Passos

Entender como esse controle se estende a permissões e workspaces em equipes.

---

## Aula 6.2 — Permissões, RBAC e Controles de Workspace

### Objetivos da Aula

- Entender como administradores de workspace configuram o Codex para equipes.

### Habilidades Esperadas

Ao final desta aula, o aluno explica a diferença entre Codex Local e Codex Cloud do ponto de vista de controle administrativo.

### Conceitos

- RBAC (controle de acesso baseado em função): acesso ao Codex pode ser concedido a funções de usuário específicas dentro de um workspace.
- Workspaces gerenciados controlam separadamente Codex Local (CLI, extensão de IDE, fluxos no desktop) e Codex Cloud (tarefas delegadas em nuvem).
- Administradores/proprietários configuram modelo padrão, nível de raciocínio e comportamento inicial em `Configurações do workspace → Modelos`; requisitos obrigatórios (`requirements.toml`) têm prioridade sobre os padrões do workspace, que por sua vez têm prioridade sobre a escolha individual do membro.

### 📸 Sugestão de Prints

- Tela de administração de workspace mostrando `Configurações → Modelos`, com os campos "modelo padrão", "nível de raciocínio" e "comportamento de novo chat" visíveis.

### Hands-on (5 min) — *nota: aula conceitual para quem não é administrador de workspace*

O aluno lê um cenário fictício de política de workspace e determina qual configuração (requisito obrigatório, padrão do workspace ou escolha do membro) prevalece.

### Resumo da Aula

Em contextos empresariais, o controle sobre o Codex é hierárquico e granular — relevante mesmo para quem não administra o workspace, pois explica por que certas opções aparecem bloqueadas.

### Próximos Passos

Entender como os dados do aluno são tratados pela OpenAI.

---

## Aula 6.3 — Dados, Privacidade e Controles de Treinamento

### Objetivos da Aula

- Entender as políticas de uso de dados para treinamento de modelos, e como desativá-las quando aplicável.

### Habilidades Esperadas

Ao final desta aula, o aluno localiza e ajusta, na própria conta, a configuração de controle de dados relevante ao seu plano.

### Conceitos

- **Business, Enterprise e Edu:** por padrão, entradas e saídas não são usadas para melhorar os modelos (organizações da API podem optar por compartilhar dados, exceto clientes com zero retenção de dados).
- **Pro e Plus:** conversas podem ser usadas para melhorar modelos, a menos que o treinamento seja desativado manualmente nos controles de dados do ChatGPT.
- Fluxos locais rodam no dispositivo do usuário; tarefas na nuvem rodam em ambientes gerenciados pela OpenAI — a distinção da Aula 0.2 volta a ser relevante aqui do ponto de vista de dados.

### 📸 Sugestão de Prints

- Tela de `Controles de Dados` do ChatGPT, com o toggle de "Melhorar o modelo para todos" destacado.

### Hands-on (5 min)

O aluno localiza a configuração de controle de dados em sua própria conta e decide, com justificativa, se deve manter ativada ou desativar.

> 🔒 **Segurança:** em contas usadas para projetos com informações confidenciais, avalie desativar o compartilhamento de dados para treinamento, mesmo em planos pessoais.

### Resumo da Aula

Entender onde seus dados vão é parte da responsabilidade de qualquer usuário profissional de IA agente.

### Próximos Passos

Consolidar tudo em um checklist prático de desenvolvimento seguro.

---

## Aula 6.4 — Checklist de Desenvolvimento Seguro

### Objetivos da Aula

- Consolidar as boas práticas de segurança vistas no módulo em um checklist aplicável a qualquer tarefa.

### Habilidades Esperadas

Ao final desta aula, o aluno aplica o checklist completo a uma tarefa real antes de aceitar o resultado.

### Checklist

Antes de aceitar uma alteração:

- [ ] Rodou os testes?
- [ ] Conferiu os arquivos alterados?
- [ ] Entende completamente a mudança?
- [ ] Revisou implicações de segurança (permissões, dados sensíveis, acesso à internet)?
- [ ] Verificou se o acesso à internet foi necessário e usado de forma consciente?
- [ ] Confirmou os controles de dados adequados ao contexto do projeto?

### 📸 Sugestão de Prints

- O checklist acima como uma imagem de card único, em formato para impressão/fixação, com cada item como caixa de marcação.

### Hands-on (6 min)

O aluno aplica o checklist completo à última tarefa que executou no curso.

### Resumo da Aula

Segurança em IA agente não é um módulo isolado — é um hábito aplicado a cada tarefa, do início ao fim do curso.

### Próximos Passos

Explorar os recursos mais avançados da plataforma.

---

# Módulo 7 — Recursos Avançados

### Objetivo do Módulo

Cobrir o conjunto de funcionalidades do Codex que ficam sistematicamente de fora de tutoriais introdutórios — a principal lacuna de "potencial subutilizado" identificada na auditoria.

---

## Aula 7.1 — Memória e Continuidade de Contexto

### Objetivos da Aula

- Entender como o Codex pode reter contexto entre sessões através de Memórias.

### Habilidades Esperadas

Ao final desta aula, o aluno identifica um cenário em que ativar Memórias economizaria tempo de reexplicação de contexto.

### Conceitos

- Memórias permitem que o Codex se lembre de contexto relevante ao longo do tempo, reduzindo a necessidade de repetir informações em cada nova tarefa.
- Gerenciamento de dados armazenados por esse recurso pode ser revisado e ajustado pelo usuário.

### 📸 Sugestão de Prints

- Tela de configurações de Memória do Codex, mostrando uma lista de itens memorizados com opção de exclusão individual.

### Hands-on (5 min)

O aluno revisa (ou ativa) as configurações de Memória em sua conta e identifica um exemplo de informação que valeria a pena reter entre sessões (ex.: convenções do time, preferências de estilo).

> 💡 **Dica:** memórias são especialmente úteis para preferências estáveis (padrões de código, tom de documentação) — não para dados sensíveis ou temporários.

### Resumo da Aula

Memória reduz o custo de "reexplicar o óbvio" a cada nova tarefa.

### Próximos Passos

Automatizar tarefas que se repetem em intervalos regulares.

---

## Aula 7.2 — Tarefas Agendadas

### Objetivos da Aula

- Configurar uma tarefa recorrente para ser executada automaticamente pelo Codex.

### Habilidades Esperadas

Ao final desta aula, o aluno cria uma tarefa agendada funcional.

### Conceitos

- Tarefas Agendadas permitem que o Codex continue o trabalho ao longo do tempo, sem intervenção manual repetida (ex.: gerar um relatório toda segunda-feira, verificar dependências desatualizadas semanalmente).

### 📸 Sugestão de Prints

- Tela de criação de Tarefa Agendada, com campos de frequência (diária, semanal), prompt associado e repositório-alvo visíveis.

### Hands-on (7 min)

O aluno configura uma tarefa agendada fictícia (ex.: "toda sexta-feira, gerar um resumo dos commits da semana").

> 🚀 **Produtividade:** tarefas agendadas são ideais para eliminar lembretes mentais de manutenção recorrente — o mesmo princípio por trás da redução de troca de contexto abordada no Módulo 8.

### Resumo da Aula

O que antes exigia lembrete manual agora roda sozinho, no horário certo.

### Próximos Passos

Conhecer o navegador integrado e o Modo de Desenvolvedor.

---

## Aula 7.3 — Browser Integrado e Modo de Desenvolvedor (CDP)

### Objetivos da Aula

- Entender o uso do navegador integrado do Codex e o Modo de Desenvolvedor para depuração avançada.

### Habilidades Esperadas

Ao final desta aula, o aluno habilita o Modo de Desenvolvedor (em ambiente de teste) e entende o escopo de acesso concedido.

### Conceitos

- O Modo de Desenvolvedor dá ao Codex acesso controlado ao Chrome DevTools Protocol (CDP), permitindo inspecionar saída de console, tráfego de rede, estado da página e desempenho de JavaScript.
- Habilitado em `Configurações > Navegador > Habilitar acesso total ao CDP`, no aplicativo Desktop.
- O Codex solicita aprovação explícita antes de usar acesso total ao CDP para inspecionar um site.
- Administradores de workspace podem desabilitar esse recurso globalmente (`browser_use_full_cdp_access = false`); desabilitar o uso do Browser como um todo também desabilita o CDP.

### 📸 Sugestão de Prints

- Tela `Configurações > Navegador` do app Desktop, com o toggle "Habilitar acesso total ao CDP em Modo de desenvolvedor" em destaque, e a caixa de diálogo de aprovação explícita que aparece antes do uso.

### Hands-on (7 min)

Em um ambiente de teste, o aluno habilita o Modo de Desenvolvedor e observa a caixa de aprovação explícita antes de autorizar uma inspeção de página.

> 🔒 **Segurança:** acesso total ao CDP permite inspecionar partes internas sensíveis do navegador — habilite apenas quando necessário, e revogue depois do uso em máquinas compartilhadas.

### 🔧 Troubleshooting

| Sintoma | Causa provável | Solução |
|---|---|---|
| Opção de Modo de Desenvolvedor não aparece | Uso do navegador no app ainda não foi habilitado | Habilitar primeiro "navegador no app" antes de ativar o Modo de Desenvolvedor |
| Administrador não consegue habilitar para a equipe | Política de workspace bloqueando o recurso | Verificar `browser_use_full_cdp_access` nas configurações do Codex na nuvem |

### Resumo da Aula

O navegador integrado transforma o Codex em uma ferramenta de depuração de front-end, não só de back-end.

### Próximos Passos

Conhecer o Uso do Computador e o recurso de Gravar e Reproduzir.

---

## Aula 7.4 — Uso do Computador e Gravar/Reproduzir

### Objetivos da Aula

- Entender o recurso de Uso do Computador (Computer Use) e como transformar um fluxo de trabalho manual em uma habilidade reutilizável com Gravar e Reproduzir.

### Habilidades Esperadas

Ao final desta aula, o aluno identifica um fluxo de trabalho pessoal que seria um bom candidato para gravação e reprodução.

### Conceitos

- Uso do Computador permite ao Codex interagir com aplicações na tela do usuário, além do código.
- Gravar e Reproduzir (disponível no app Desktop, macOS, para usuários qualificados) permite demonstrar um fluxo de trabalho uma vez e transformá-lo em uma habilidade reutilizável — útil para fluxos estáveis e repetíveis, mais fáceis de mostrar do que de descrever.
- Exige Uso do Computador habilitado; disponibilidade inicial exclui União Europeia, Suíça e Reino Unido.
- Durante a gravação, o Codex observa ações e conteúdo das janelas necessários para aprender o fluxo — recomenda-se manter as gravações focadas na tarefa e evitar inserir segredos ou dados sensíveis.

### 📸 Sugestão de Prints

- Tela do app Desktop mostrando o botão "Iniciar Gravação", seguida de uma captura da lista de "Habilidades gravadas" disponíveis para reprodução.

### Hands-on (6 min)

O aluno lista, por escrito, um fluxo de trabalho manual e repetitivo do seu dia a dia que seria um bom candidato a "Gravar e Reproduzir" (sem necessariamente executar a gravação, dependendo da disponibilidade regional).

> ⚠️ **Atenção:** nunca insira senhas, números de cartão ou outros dados sensíveis durante uma gravação — o Codex registra o conteúdo das janelas durante o processo.

### Resumo da Aula

Fluxos difíceis de descrever em texto, mas fáceis de demonstrar, ganham um caminho de automação através da gravação.

### Próximos Passos

Conhecer Sites e Plugins, os recursos que estendem o Codex além do código.

---

## Aula 7.5 — Sites e Plugins

### Objetivos da Aula

- Entender o recurso Sites (criação e publicação de páginas) e o Diretório de Plugins do Codex.

### Habilidades Esperadas

Ao final desta aula, o aluno descreve o que gostaria de criar usando Sites e identifica um plugin relevante ao seu contexto de trabalho.

### Conceitos

- **Sites:** disponível em planos pagos (exceto Free e Go), em regiões com suporte (não disponível, no momento, no Espaço Econômico Europeu, Suíça ou Reino Unido). O usuário descreve o que quer criar, revisa a prévia gerada e usa os controles de compartilhamento disponíveis. Administradores de workspace controlam se membros podem criar e publicar Sites publicamente.
- **Plugins:** visíveis no Diretório de Plugins conforme o plano; um plugin pode incluir habilidades, apps e modelos de app. Em workspaces Business/Enterprise/Edu, administradores gerenciam instalação (`Configurações do workspace > Plugins`) e acesso a apps subjacentes (`Configurações do workspace > Apps`).

### 📸 Sugestão de Prints

- Tela do Diretório de Plugins do Codex, com um plugin de exemplo selecionado mostrando status "Disponível" versus "Instalado".
- Fluxo de criação de um Site: da descrição em texto até a prévia gerada, com o botão de controle de compartilhamento visível.

### Hands-on (6 min)

O aluno descreve, em texto, uma página simples que gostaria de criar com Sites (ex.: uma landing page de um projeto pessoal) e navega pelo Diretório de Plugins procurando algo relevante ao seu contexto de trabalho.

> 💡 **Dica:** Sites é ideal para protótipos e páginas simples de compartilhamento rápido — não substitui um processo completo de desenvolvimento web para produtos críticos.

### Resumo da Aula

Sites e Plugins ampliam o Codex para além da edição de repositórios — encerrando o mapeamento completo dos recursos da plataforma.

### Próximos Passos

Levar tudo isso para dentro da rotina profissional diária.

---

# Módulo 8 — Fluxos Profissionais e Automação

### Objetivo do Módulo

Integrar o Codex ao dia a dia de trabalho, individual e em equipe.

---

## Aula 8.1 — Rotina Diária com Agentes

### Objetivos da Aula

- Desenhar uma rotina diária realista de uso do Codex.

### Habilidades Esperadas

Ao final desta aula, o aluno planeja sua própria rotina diária de delegação de tarefas.

### Conceitos

- Hábitos documentados de equipes reais: triagem de novos problemas pela manhã, planejamento de tarefas no início do dia, delegação de tarefas em segundo plano para dar sequência ao trabalho ao longo do dia.
- Redução de troca de contexto: delegar tarefas de escopo definido libera atenção para o trabalho de maior valor.

### 📸 Sugestão de Prints

- Agenda visual de um dia de trabalho fictício, com blocos de tempo mostrando "Planejamento (manhã)", "Tarefas delegadas em paralelo", "Revisão (tarde)".

### Hands-on (7 min)

O aluno escreve sua própria rotina diária ideal de uso do Codex, com pelo menos três momentos de delegação ao longo do dia.

### Resumo da Aula

O maior ganho de produtividade não vem de uma tarefa isolada, mas de um hábito diário de delegação.

### Próximos Passos

Automatizar tarefas repetitivas de forma sistemática.

---

## Aula 8.2 — Automatizando Tarefas Repetitivas

### Objetivos da Aula

- Identificar e automatizar tarefas repetitivas usando Tarefas Agendadas e prompts reutilizáveis.

### Habilidades Esperadas

Ao final desta aula, o aluno tem ao menos um prompt reutilizável documentado para uma tarefa recorrente própria.

### Conceitos

- Tarefas repetitivas e com escopo bem definido (refatorar, renomear, escrever testes) são as que mais se beneficiam de automação, conforme observado em equipes que já usam o Codex no dia a dia.
- Prompts reutilizáveis: templates salvos que podem ser adaptados rapidamente para tarefas semelhantes.

### 📸 Sugestão de Prints

- Uma biblioteca pessoal de prompts salvos, organizada por categoria (ex.: "Correção de bugs", "Documentação", "Testes").

### Hands-on (7 min)

O aluno documenta um prompt reutilizável para uma tarefa que executa com frequência.

> 🚀 **Produtividade:** mantenha uma biblioteca de prompts testados — reutilizar um prompt validado é mais rápido e mais confiável do que escrever um novo a cada vez.

### Resumo da Aula

Automatizar o repetitivo é o que libera tempo para o trabalho que realmente exige criatividade humana.

### Próximos Passos

Levar essa prática para o contexto de equipes.

---

## Aula 8.3 — Codex em Equipe: RBAC, API de Compliance e Enterprise Analytics

### Objetivos da Aula

- Entender os recursos voltados a uso corporativo do Codex.

### Habilidades Esperadas

Ao final desta aula, o aluno explica a um colega hipotético não-técnico o que são RBAC, API de Compliance e Enterprise Analytics, em uma frase cada.

### Conceitos

- **RBAC:** controle de acesso ao Codex por função dentro da organização.
- **API de Compliance:** superfície de logs que cobre o uso do Codex, incluindo clientes locais (CLI, extensão de IDE) e uso na web ou delegado na nuvem — separada dos endpoints específicos de tarefas na nuvem.
- **Codex Enterprise Analytics:** disponível para workspaces Enterprise com Codex habilitado; requer chave de API da organização com acesso habilitado.

### 📸 Sugestão de Prints

- Painel fictício de Enterprise Analytics mostrando métricas agregadas de uso por equipe (número de tarefas, taxa de aprovação de PRs).

### Hands-on (5 min) — *aula conceitual*

O aluno lista, para sua própria organização (real ou hipotética), quem deveria ter acesso a cada função (RBAC) e por quê.

### Resumo da Aula

Ferramentas de governança não são burocracia — são o que permite escalar o uso de agentes de IA com segurança em uma equipe inteira.

### Próximos Passos

Consolidar tudo em um conjunto final de boas práticas.

---

## Aula 8.4 — Boas Práticas Consolidadas

### Objetivos da Aula

- Revisar e consolidar todas as boas práticas apresentadas ao longo do curso.

### Habilidades Esperadas

Ao final desta aula, o aluno aplica o checklist consolidado a uma tarefa de sua escolha.

### Checklist Consolidado

Sempre:

- [ ] Escreva objetivos claros (objetivo, contexto, restrições, critério de sucesso).
- [ ] Limite o escopo de cada tarefa.
- [ ] Revise resultados antes de aceitar.
- [ ] Execute e confira os testes.
- [ ] Documente o que foi feito.
- [ ] Reutilize prompts validados.
- [ ] Avalie se o acesso à internet é realmente necessário.
- [ ] Confirme os controles de dados adequados ao projeto.

### 📸 Sugestão de Prints

- Versão final e ilustrada do checklist acima, em formato de pôster/resumo visual para fixação.

### Hands-on (8 min)

O aluno aplica o checklist consolidado a uma tarefa real, do início ao fim.

### Resumo da Aula

Este checklist é o resumo prático de tudo o que sustenta um uso profissional e responsável do Codex.

### Próximos Passos

Ver como esse conjunto de práticas se aplica além da programação.

---

# Módulo 9 — Casos Reais Além da Programação

### Objetivo do Módulo

Substituir hands-on genéricos por estudos de caso reais e documentados, mostrando a expansão do Codex para o trabalho de conhecimento.

---

## Aula 9.1 — Pesquisa: o Caso GroundVue

### Objetivos da Aula

- Analisar como o Codex é usado para pesquisa e organização de informação em larga escala.

### Habilidades Esperadas

Ao final desta aula, o aluno cria um pequeno fluxo de pesquisa automatizado usando o Codex.

### Estudo de Caso

A GroundVue, fundada por Travis Hoppe, Ann Lewis e Shannon Arvizu, ajuda governos a aprenderem uns com os outros tornando reuniões públicas pesquisáveis e comparáveis em escala. Com informações críticas espalhadas por vídeos, sites e plataformas locais de aproximadamente 90.000 órgãos governamentais, a GroundVue usa o Codex para localizar fontes públicas de difícil acesso e construir sistemas que coletam e organizam essas informações continuamente. Tarefas que antes levavam dias ou semanas agora levam minutos, permitindo que uma equipe pequena realize um trabalho que antes exigiria grandes grupos de tecnólogos e pesquisadores.

### 📸 Sugestão de Prints

- Diagrama simples: "Fontes dispersas (vídeos, sites, plataformas locais)" → "Codex coleta e organiza" → "Base pesquisável e comparável".

### Hands-on (8 min)

O aluno usa o Codex para criar um pequeno relatório automaticamente a partir de um conjunto de textos ou links fornecidos pelo curso, replicando em pequena escala o princípio usado pela GroundVue.

### Resumo da Aula

O Codex aplicado à pesquisa transforma informação fragmentada em conhecimento estruturado — em uma fração do tempo.

### Próximos Passos

Aplicar o mesmo princípio à análise de dados.

---

## Aula 9.2 — Análise de Dados e Ciência de Dados

### Objetivos da Aula

- Usar o Codex para limpar dados, construir modelos simples e automatizar análises.

### Habilidades Esperadas

Ao final desta aula, o aluno gera uma análise simples de um conjunto de dados usando o Codex.

### Conceitos

- Cientistas de dados usam o Codex para limpar datasets, construir modelos e automatizar análises.
- Entre trabalhadores do conhecimento, Análise de Dados é a categoria de tarefa com crescimento mais acelerado, com rotulagem de dados dominando o volume de uso.

### 📸 Sugestão de Prints

- Planilha "antes" (dados brutos, inconsistentes) e "depois" (dados limpos, com gráfico resumo gerado) lado a lado.

### Hands-on (8 min)

O aluno pede ao Codex para limpar uma planilha de exemplo com inconsistências propositais e gerar um resumo estatístico simples.

> 💡 **Dica:** para tarefas de dados, seja específico sobre o formato de saída esperado (ex.: "gere uma tabela com colunas X, Y, Z") — isso reduz retrabalho de formatação.

### Resumo da Aula

Análise de dados é hoje a área de crescimento mais rápido entre trabalhadores do conhecimento usando o Codex — e a barreira de entrada é menor do que parece.

### Próximos Passos

Ver como o Codex conecta descoberta de cliente, vendas e produto.

---

## Aula 9.3 — Vendas e Desenvolvimento de Produto: o Caso Proaction

### Objetivos da Aula

- Analisar como o Codex conecta descoberta de cliente, vendas e desenvolvimento de produto.

### Habilidades Esperadas

Ao final desta aula, o aluno cria um protótipo simples de proposta personalizada usando o Codex.

### Estudo de Caso

A Proaction ajuda frotas a gerenciar veículos e equipamentos cujos dados estão espalhados entre sistemas de telemetria, plataformas de manutenção, planilhas e memória institucional. Usando o Codex, o cofundador Colin Knudsen transforma conversas com clientes em propostas personalizadas, protótipos de fluxo de trabalho e demonstrações funcionais adaptadas à operação de cada prospect. Em vez de depender de discursos de venda genéricos, a Proaction consegue construir e validar soluções antes mesmo da assinatura de um contrato — ajudando uma startup de cinco pessoas a competir muito acima do seu tamanho.

### 📸 Sugestão de Prints

- Fluxo simples: "Conversa com cliente" → "Codex gera protótipo/proposta personalizada" → "Demonstração funcional antes do contrato".

### Hands-on (8 min)

A partir de uma transcrição fictícia de conversa com cliente (fornecida pelo curso), o aluno pede ao Codex para gerar um esboço de proposta personalizada.

### Resumo da Aula

O Codex permite que equipes pequenas conectem descoberta, vendas e produto sem depender de múltiplas equipes especializadas.

### Próximos Passos

Ver a aplicação do Codex na educação.

---

## Aula 9.4 — Educação: o Caso Taiyo Inoue

### Objetivos da Aula

- Usar o Codex para automatizar tarefas administrativas recorrentes, como no contexto educacional.

### Habilidades Esperadas

Ao final desta aula, o aluno cria um script simples para automatizar uma tarefa administrativa repetitiva.

### Estudo de Caso

O professor de matemática Taiyo Inoue usa o Codex para automatizar uma das partes menos recompensadoras e mais demoradas do ensino: manter informações de curso em um sistema de gestão de aprendizagem (LMS). Ao gerar scripts que atualizam tarefas, calendários, materiais e avisos no Canvas, o Codex assume um trabalho que antes consumia horas de esforço manual toda semana. Inoue estima que o fluxo de trabalho economiza de quatro a cinco horas semanais — tempo que ele reinveste em aulas colaborativas presenciais para seus alunos na California State University.

### 📸 Sugestão de Prints

- Comparação "antes" (lista de tarefas manuais no LMS) e "depois" (script automatizado rodando, com o tempo economizado destacado: "4-5h/semana").

### Hands-on (8 min)

O aluno cria um plano de aula (ou um script fictício de atualização de calendário) usando o Codex, aplicando o mesmo princípio do caso estudado.

### Resumo da Aula

Automação administrativa não é sobre substituir o ensino — é sobre devolver tempo para a parte do trabalho que só um humano pode fazer bem.

### Próximos Passos

Encerrar o módulo com um caso de uso pessoal e de acessibilidade.

---

## Aula 9.5 — Uso Pessoal e Acessibilidade: o Caso Luke Xing

### Objetivos da Aula

- Entender como o Codex viabiliza soluções pessoais e altamente específicas, sem depender de software comercial.

### Habilidades Esperadas

Ao final desta aula, o aluno descreve, em prompt completo, uma ferramenta pessoal que resolveria um problema específico da própria vida.

### Estudo de Caso

Luke Xing usou o Codex para construir um aplicativo desktop que ajuda a compensar uma perda auditiva significativa e variável em seu ouvido esquerdo. Descrevendo o problema em linguagem simples ao Codex, ele criou uma ferramenta que testa a audição em diferentes frequências e ajusta a saída de áudio para diferentes dispositivos, ajudando a restaurar o equilíbrio em músicas, chamadas e escuta cotidiana. O aplicativo não é um dispositivo médico, mas uma solução pessoal para um desafio altamente específico que o software comercial não havia endereçado.

### 📸 Sugestão de Prints

- Interface fictícia do aplicativo descrito (um simples equalizador por frequência com ajuste manual), com anotação: "criado a partir de uma descrição em linguagem natural, sem escrever código manualmente".

### Hands-on (8 min)

O aluno escreve um prompt completo (seguindo a estrutura da Aula 2.1) descrevendo uma ferramenta pessoal que gostaria de construir para um problema real do seu próprio cotidiano.

> 💡 **Dica:** você não precisa saber programar para descrever um problema com precisão — a clareza do problema importa mais do que o vocabulário técnico usado para descrevê-lo.

### Resumo da Aula

Cada aluno, independentemente da formação técnica, sai deste módulo com prova concreta de que já pode construir a ferramenta que precisa, em vez de esperar por ela.

### Próximos Passos

Aplicar tudo o que foi aprendido em um projeto final completo.

---

# Módulo 10 — Projeto Final

### Objetivo

Aplicar de forma integrada todo o conteúdo do curso em um projeto real e completo, do planejamento à entrega.

### Habilidades Esperadas

Ao final do projeto, o aluno terá conduzido, de forma autônoma, um ciclo completo de delegação a agentes de IA — do planejamento à entrega revisada.

### Etapas do Projeto

```
Planejamento → Divisão em tarefas → Prompt → Execução →
Revisão → Correções → Entrega
```

1. **Planejamento:** escolher o tipo de projeto (pequeno sistema, documentação, automação, pesquisa ou relatório) e definir seu objetivo geral.
2. **Divisão em tarefas:** aplicar a técnica da Aula 2.3 para quebrar o projeto em tarefas pequenas e bem definidas.
3. **Prompt:** escrever cada prompt seguindo a estrutura da Aula 2.1 (objetivo, contexto, restrições, critério de sucesso).
4. **Execução:** delegar as tarefas, aproveitando paralelismo (Aula 2.4) sempre que possível.
5. **Revisão:** aplicar o checklist consolidado da Aula 8.4 a cada entrega.
6. **Correções:** solicitar ajustes quando necessário, documentando o motivo.
7. **Entrega:** finalizar o projeto (incluindo, se aplicável, Pull Request e documentação gerada).

### Opções de Projeto

- Pequeno sistema funcional.
- Documentação completa de um projeto existente.
- Automação de uma tarefa repetitiva real (pessoal ou profissional).
- Pequeno projeto de pesquisa (nos moldes da Aula 9.1).
- Relatório ou análise de dados (nos moldes da Aula 9.2).

### 📸 Sugestão de Prints

- Um "diário de bordo" visual do projeto do aluno, com cada etapa (planejamento, tarefas, execução, revisão, entrega) documentada com uma captura de tela própria.

### Rubrica de Avaliação

| Critério | O que é avaliado |
|---|---|
| Clareza do prompt | Presença explícita de objetivo, contexto, restrições e critério de sucesso |
| Organização das tarefas | Qualidade da divisão em tarefas menores e uso de paralelismo quando aplicável |
| Revisão crítica dos resultados | Evidência de leitura de logs/testes e aplicação do checklist de segurança |
| Uso de boas práticas | Uso de AGENTS.md, reaproveitamento de prompts, documentação gerada |
| Qualidade da entrega final | Funcionalidade, clareza e completude do resultado entregue |

> 🚀 **Produtividade:** use ao menos dois agentes em paralelo em alguma etapa do projeto — é a habilidade mais associada ao ganho real de produtividade em usuários avançados do Codex.

### Resumo do Curso

O aluno percorreu o caminho completo: da diferença entre chat e agente até a entrega autônoma de um projeto real, passando por configuração, prompts, AGENTS.md, revisão crítica, segurança, recursos avançados e casos reais de uso além da programação.

### O que o Aluno Deve Lembrar ao Concluir o Curso

- O Codex é um agente que executa trabalho, não apenas responde perguntas — e existe em quatro clientes (Web, CLI, IDE, Desktop), com execução local ou em nuvem.
- Bons resultados dependem de objetivos claros, contexto suficiente, restrições explícitas e critérios de sucesso mensuráveis.
- Trabalhos complexos devem ser divididos em partes menores e, sempre que possível, executados em paralelo.
- AGENTS.md ajuda o agente a compreender padrões e expectativas do projeto — e pode ser criado rapidamente com `/init`.
- Logs, testes e evidências fazem parte do processo de validação e nunca devem ser ignorados.
- A revisão humana continua sendo indispensável antes de integrar qualquer alteração — especialmente em áreas sensíveis.
- O acesso à internet durante tarefas é uma configuração opcional e consciente, não uma proibição absoluta nem uma permissão irrestrita.
- Recursos avançados (Memória, Tarefas Agendadas, Browser/Modo de Desenvolvedor, Uso do Computador, Sites, Plugins, RBAC) ampliam significativamente o que é possível automatizar.
- O maior ganho de produtividade vem da combinação entre delegação inteligente, revisão crítica e integração do Codex ao fluxo diário de trabalho — dentro e fora da programação.
