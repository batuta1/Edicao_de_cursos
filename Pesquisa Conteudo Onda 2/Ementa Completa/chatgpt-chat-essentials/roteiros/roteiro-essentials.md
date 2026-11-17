# ChatGPT Chat — Essentials (roteiro final)

**Público-Alvo:** pessoas que ainda não usam IA no dia a dia (T1 — Começando com assistentes de
IA); advogados, assessores, estudantes e professores de Direito (J1); profissionais de outras áreas
nas trilhas de fundamentos.

**Objetivo Geral:** capacitar o participante a conduzir conversas produtivas e seguras no ChatGPT —
formulando pedidos estruturados, protegendo dados, personalizando e dando continuidade ao trabalho,
buscando informação atual com fontes, trabalhando com arquivos, voz, imagem e Canvas — e a comparar
o ChatGPT com o Claude Chat. Produto final: um quadro comparativo fundamentado de uma mesma tarefa
executada nas duas ferramentas.

**Pré-requisitos:** nenhum conhecimento técnico; recomendável ter cursado *Claude Chat - Essentials*.
Conta ChatGPT gratuita (Free), computador com navegador atualizado e internet.

## Estrutura do Curso

| Nível | Módulos | Tempo |
|---|---|---|
| Nível 0 — Preparação | Módulo 0 — Preparação e verificação inicial | 11 min |
| Nível 1 — Fundamentos | Módulo 1 — Conversa produtiva; Módulo 2 — Dados, privacidade e sigilo | 46 min |
| Nível 2 — Recursos | Módulo 3 — Personalização e projetos; Módulo 4 — Busca e verificação; Módulo 5 — Arquivos, voz, imagem e Canvas | 54 min |
| Nível 3 — Integração | Módulo 6 — Síntese e comparação com o Claude Chat | 16 min |
| **Total** | 7 módulos (6 de conteúdo + síntese) | **127 min** |

Fio condutor: a **alucinação** é plantada no Módulo 1 e retomada nos Módulos 4 (busca e
verificação) e 6 (comparação); o **semáforo de dados** é plantado no Módulo 2 e retomado nos
Módulos 3 (memória e projetos) e 5 (envio de arquivos).

> Dados de planos e recursos conferidos na página oficial de preços do ChatGPT (pt-BR) em
> 17/11/2026. Planos, nomes de modelos e rótulos de menu mudam com frequência; o curso ensina a
> lógica de cada recurso e indica onde conferir.

---

## Módulo 0 — Preparação e verificação inicial

### 0.1 Conta e plano

- **📸 Sugestão de Prints:** página `chatgpt.com/pt-BR/pricing` com a aba "Individual" selecionada
  e as colunas Free, Go, Plus e Pro visíveis; destacar a coluna Free e a linha "Projetos" da
  tabela comparativa.

O ChatGPT é acessado em `chatgpt.com`, por aplicativo de desktop (Windows e macOS) ou por
aplicativo de celular (iOS e Android). O curso utiliza a versão web e o plano gratuito. Os planos
individuais vigentes são Free, Go, Plus e Pro; os planos Business, Enterprise e Edu destinam-se a
organizações.

| Recurso | Free | Go | Plus | Pro |
|---|---|---|---|---|
| Conversas de texto | Ilimitadas* | Ilimitadas* | Ilimitadas* | Ilimitadas* |
| Buscar (web) | Sim | Sim | Sim | Sim |
| Projetos | Sim | Sim | Sim | Sim |
| Upload de arquivos / análise de dados | Limitado | Sim | Sim | Sim |
| Criação de imagens / voz / memória | Limitado | Sim/ampliado | Ampliado | Ampliado |
| Tarefas agendadas | Não | Sim | Sim | Sim |
| Tabelas e gráficos interativos | Não | Não | Sim | Sim |

\*Sujeitas a proteções contra abuso. Fonte: página oficial de preços, 17/11/2026.

Cumpre registrar que "limitado" significa cota que se renova com o tempo: atingido o limite, o
recurso fica indisponível até a renovação ou a conversa passa a um modelo mais simples. Todos os
exercícios do curso foram desenhados para caber no Free; onde houver risco de limite, o roteiro
indica alternativa.

### 0.2 Mapa da tela

- **📸 Sugestão de Prints:** tela inicial de `chatgpt.com` com conta logada, janela de 1366 px;
  numerar: (1) barra lateral com "Novo chat", "Buscar chats" e "Projetos"; (2) seletor de modelo
  no topo; (3) caixa de mensagem com o botão "+" à esquerda e o ícone de voz à direita; (4) botão
  "Temporário" no canto superior direito; (5) foto/nome do perfil no canto inferior esquerdo.

| Elemento | Onde fica | Para que serve |
|---|---|---|
| Barra lateral | À esquerda | Novo chat, busca nas conversas, projetos, histórico |
| Seletor de modelo | Topo da conversa | Escolher entre resposta rápida e raciocínio |
| Botão "+" | À esquerda da caixa de mensagem | Anexar arquivos e ativar ferramentas (busca, imagem, Canvas) |
| Voz | À direita da caixa de mensagem | Conversa falada |
| Temporário | Canto superior direito de um chat novo | Conversa fora do histórico e da memória |
| Perfil | Canto inferior esquerdo | Configurações, personalização, controles de dados |

### Solução de Problemas

| Situação | Procedimento |
|---|---|
| A página pede login a cada acesso | Verificar se o navegador bloqueia cookies de `chatgpt.com`; usar janela normal, não anônima |
| A tela difere da descrição | A interface muda com frequência; localizar o elemento pela função (ex.: ícone de engrenagem = configurações) |
| Mensagem de limite atingido | Aguardar a renovação indicada na própria mensagem; seguir a rota alternativa do exercício |

### Pílula Hands-on — Verificação inicial (4 min)

1. Entrar em `chatgpt.com` com a conta.
2. Localizar os seis elementos da tabela "Mapa da tela".
3. Abrir `chatgpt.com/pt-BR/pricing` e anotar o plano da própria conta.

**Critério de êxito:** seis elementos localizados e plano identificado.

## Descrição

- **Objetivos da Aula:** apresentar as formas de acesso, os planos e o mapa da interface.
- **Habilidades Esperadas:** entrar no ChatGPT, reconhecer o próprio plano e localizar sozinho
  os elementos da tela usados no curso.

---

## Módulo 1 — Conversa produtiva

### 1.1 O que é o ChatGPT e como ele responde

- **📸 Sugestão de Prints:** seletor de modelo aberto no topo da conversa, mostrando as opções de
  resposta rápida e de raciocínio disponíveis na conta Free; destacar a opção selecionada.

O ChatGPT é um assistente de inteligência artificial generativa da OpenAI. Seu núcleo é um modelo
de linguagem: um sistema treinado com grandes volumes de texto que produz respostas prevendo,
passo a passo, a continuação mais provável de um pedido. Uma analogia útil é a de um redator muito
experiente que nunca consulta arquivos durante a escrita: escreve com fluência, mas pode errar
datas, números e referências sem perceber.

Esse erro dito com confiança denomina-se **alucinação**. Não se trata de defeito ocasional, mas de
consequência do modo de funcionamento; por isso, toda resposta que contenha fato verificável deve
ser conferida (o tema é retomado no Módulo 4). O pedido redigido pelo usuário denomina-se
**prompt**, e o conjunto de mensagens que o modelo considera ao responder denomina-se
**contexto** — limitado pela janela de contexto do plano (no Free, cerca de 12 páginas de texto
de entrada no modo de resposta rápida, segundo a página de preços).

O seletor de modelo oferece, em essência, duas famílias: **resposta rápida**, adequada a tarefas
simples, e **raciocínio**, que demora mais e "pensa" antes de responder, adequado a análise,
cálculo e planejamento. Os nomes comerciais dos modelos mudaram várias vezes em 2026; convém
escolher pela função, não pelo nome.

### 1.2 Anatomia de um pedido

- **📸 Sugestão de Prints:** duas respostas lado a lado (ou em sequência) ao pedido vago e ao
  estruturado do exemplo abaixo; destacar a diferença de formato.

Recomenda-se que o pedido contenha quatro elementos: **tarefa** (o que fazer), **contexto** (para
quê e em que situação), **público** (para quem) e **formato** (como entregar).

| Pedido vago | Pedido estruturado |
|---|---|
| "Escreva sobre reunião." | "Escreva um e-mail curto (tarefa) convocando a equipe de atendimento para uma reunião de 30 min na quinta às 14h sobre o aumento de reclamações (contexto). Os destinatários são colegas, tom cordial (público). Até 6 linhas, com assunto (formato)." |

Variação jurídica: "Explique a diferença entre prescrição e decadência (tarefa) para um cliente
leigo que perdeu prazo de reclamação (contexto e público), em 5 linhas, sem jargão (formato)."

A conversa é cumulativa: em vez de recomeçar, convém refinar ("mais curto", "em tabela"). Três
comandos de interface sustentam esse refinamento: **editar** a própria mensagem (ícone de lápis ao
passar o cursor sobre ela), **tentar novamente** (gerar outra versão da resposta) e **ramificar**
(abrir um novo chat a partir de um ponto da conversa, preservando o original).

### Solução de Problemas

| Situação | Procedimento |
|---|---|
| Resposta genérica | Acrescentar contexto e formato; pedir "faça-me três perguntas antes de responder" |
| Resposta longa demais | Fixar o formato ("até 5 linhas", "em tabela de 3 colunas") |
| A conversa "esqueceu" o início | Conversas muito longas excedem o contexto; abrir chat novo com um resumo da anterior |

### Pílula Hands-on — Do vago ao estruturado (6 min)

1. Enviar: "Escreva sobre reunião."
2. Editar a mesma mensagem (ícone de lápis) para a versão estruturada do exemplo.
3. Pedir: "Agora em tom mais formal e com três tópicos de pauta."

**Critério de êxito:** a última resposta tem assunto, até 6 linhas de corpo (mais a pauta) e os
três tópicos.

### Avaliação — questão (4 min)

Um assistente apresentou o "art. 52 da Lei 8.078/1990" como fundamento, com redação convincente.
A conduta adequada é:

a) aceitar, pois a redação é precisa; b) pedir ao ChatGPT que confirme; c) conferir o texto na
fonte oficial (Planalto) antes de usar; d) trocar para o modelo de raciocínio e aceitar.

**Gabarito:** c. Fluência não é evidência; o próprio modelo pode confirmar o erro (b), e modelos de
raciocínio também alucinam (d).

## Descrição

- **Objetivos da Aula:** explicar modelo de linguagem, prompt, contexto, alucinação e as famílias
  do seletor; apresentar a anatomia do pedido e os comandos de refinamento.
- **Habilidades Esperadas:** redigir um pedido com tarefa, contexto, público e formato; refinar a
  resposta editando, regenerando ou ramificando; reconhecer quando uma resposta precisa de
  conferência.

---

## Módulo 2 — Dados, privacidade e sigilo

### 2.1 O que acontece com o que se digita

- **📸 Sugestão de Prints:** `Configurações > Controles de dados` aberto, com a chave "Melhorar o
  modelo para todos" visível e destacada; segundo print com um chat novo e o botão "Temporário"
  ativado no canto superior direito.

Nas contas pessoais (Free, Go, Plus, Pro), o conteúdo das conversas pode ser usado para treinar
modelos, com opção de não participação (página de preços, linha "Privacidade"). A chave
correspondente fica em `Perfil > Configurações > Controles de dados > Melhorar o modelo para todos`;
desativada, vale para toda a conta e as conversas continuam no histórico. Nos planos Business,
Enterprise e Edu, a OpenAI declara não usar os dados para treinar por padrão.

O **chat temporário** não aparece no histórico, não cria nem usa memórias e não é usado para
treinamento; a OpenAI pode manter uma cópia por até 30 dias por razões de segurança. Desde
setembro de 2026, o chat temporário pode ser personalizado para usar instruções personalizadas e
memória sem gravar nada novo. Convém observar que nenhum desses controles torna seguro inserir
informação sigilosa: eles reduzem o uso, não eliminam o tratamento dos dados pela empresa.

Em `Controles de dados` encontram-se também **Exportar dados** (cópia do histórico enviada por
e-mail) e a exclusão de conversas e da conta.

### 2.2 O semáforo de dados

| Sinal | Exemplos | Conduta |
|---|---|---|
| Verde | Textos públicos, dados fictícios, conteúdo próprio sem dados pessoais | Pode enviar |
| Amarelo | Documentos internos sem dados pessoais, rascunhos de trabalho | Só com autorização da organização e preferencialmente em conta corporativa |
| Vermelho | Dados pessoais de terceiros (CPF, saúde, endereço), segredos comerciais, peças e documentos de clientes, processos sob segredo de justiça | Não enviar em conta pessoal; anonimizar ou usar ferramenta contratada pela organização |

A Lei Geral de Proteção de Dados (LGPD, Lei 13.709/2018) exige base legal e finalidade para
tratar dados pessoais; colar dados de terceiros num serviço externo é tratamento. Para o público
jurídico, acresce o dever de sigilo profissional: documentos de cliente são, por definição, sinal
vermelho em conta pessoal.

### Pílula Hands-on — Configurar os controles (7 min)

1. Abrir `Perfil > Configurações > Controles de dados`.
2. Decidir, de forma justificada, manter ou desativar "Melhorar o modelo para todos".
3. Abrir um chat novo, ativar "Temporário" e confirmar que a conversa não aparece no histórico da
   barra lateral após recarregar a página.

**Critério de êxito:** decisão registrada e chat temporário ausente do histórico.

### Discussão orientada (8 min)

Classificar no semáforo: (1) notícia de jornal; (2) planilha de clientes com CPF; (3) minuta de
contrato com nomes das partes; (4) a mesma minuta com nomes trocados por "Parte A" e "Parte B";
(5) e-mail interno sobre férias da equipe.
**Gabarito:** 1 verde; 2 vermelho; 3 vermelho; 4 amarelo (verde se não houver outro dado
identificável e a organização permitir); 5 amarelo.

## Descrição

- **Objetivos da Aula:** apresentar os controles de dados, o chat temporário e seus limites, a
  diferença entre contas pessoais e corporativas e o semáforo de dados à luz da LGPD e do sigilo
  profissional.
- **Habilidades Esperadas:** configurar sozinho os controles de dados, abrir um chat temporário e
  decidir, antes de cada envio, se um conteúdo pode ir para o ChatGPT.

---

## Módulo 3 — Personalização e projetos

### 3.1 Instruções personalizadas e memória

- **📸 Sugestão de Prints:** `Configurações > Personalização` aberto, com o campo de instruções
  personalizadas preenchido com o exemplo abaixo; segundo print em `Personalização > Memória`
  mostrando a lista de memórias salvas e o botão de excluir ao lado de uma delas.

Três recursos dão continuidade ao trabalho e costumam ser confundidos:

| Recurso | O que guarda | Quem decide | Onde gerenciar |
|---|---|---|---|
| Instruções personalizadas | Quem é o usuário e como prefere as respostas | O usuário, por escrito | `Configurações > Personalização` |
| Memória | Fatos aprendidos nas conversas (memórias salvas) e referência ao histórico de chats | O ChatGPT, com controle do usuário | `Configurações > Personalização > Memória` |
| Projeto | Conversas, arquivos e instruções de um assunto | O usuário, por projeto | Barra lateral > Projetos |

As instruções valem para as conversas novas até serem alteradas. A memória pode ser vista,
editada, apagada item a item ou desativada; pedir "o que você lembra sobre mim?" mostra o que está
em uso. Retoma-se aqui o semáforo do Módulo 2: memória é dado guardado, e nada de sinal vermelho
deve virar memória.

### 3.2 Projetos

- **📸 Sugestão de Prints:** janela de criação de projeto com o nome preenchido e o menu de
  configurações de memória aberto, mostrando "Padrão" e "Apenas do projeto"; segundo print da
  página do projeto com as áreas de instruções e arquivos.

Um projeto funciona como pasta de trabalho inteligente: as conversas dentro dele compartilham
instruções e arquivos. Na criação, escolhe-se a memória: **padrão** (o projeto pode usar memórias
gerais) ou **apenas do projeto** (o projeto só usa o que está nele — recomendado para assuntos que
não devem se misturar). Projetos compartilhados ficam sempre "apenas do projeto". Limite de
arquivos por projeto: 5 no Free, 25 no Go e Plus, 40 no Pro, Business, Enterprise e Edu.

### Solução de Problemas

| Situação | Procedimento |
|---|---|
| O ChatGPT continua usando uma preferência antiga | Conferir instruções personalizadas e memórias salvas; apagar o item |
| Não é possível mudar a memória de um projeto | A opção é escolhida na criação; em projetos não compartilhados, a mudança passou a ser permitida em 2026 — conferir nas configurações do projeto |
| Limite de arquivos do projeto | No Free, até 5; colar o texto na conversa como alternativa |

### Pílula Hands-on — Continuidade configurada (6 min)

1. Em `Configurações > Personalização`, registrar: "Respostas em português do Brasil, objetivas,
   com no máximo 8 linhas, salvo pedido diferente."
2. Criar o projeto "Curso ChatGPT" com memória "Apenas do projeto" e a instrução: "Ao final de
   cada resposta, indicar o que precisa ser conferido em fonte externa."
3. No projeto, perguntar: "Quais são os três cuidados mais importantes ao usar IA no trabalho?"

**Critério de êxito:** resposta com até 8 linhas que termina indicando o que conferir.

## Descrição

- **Objetivos da Aula:** distinguir instruções personalizadas, memória e projetos; apresentar a
  memória do projeto e os limites por plano.
- **Habilidades Esperadas:** escrever instruções personalizadas, revisar e apagar memórias e criar
  sozinho um projeto com instruções e memória restrita.

---

## Módulo 4 — Busca e verificação

### 4.1 Busca na web com fontes

- **📸 Sugestão de Prints:** resposta com busca ativada, mostrando as citações em linha e o painel
  de fontes aberto à direita; destacar uma citação e o link correspondente.

O modelo, sozinho, conhece o mundo até a data de seu treinamento. A **busca** permite consultar
páginas atuais e citar as fontes. O ChatGPT decide sozinho quando buscar (perguntas sobre fatos
recentes, preços, notícias), mas a busca pode ser forçada em `+ > Buscar` [conferir rótulo] ou
pedindo "pesquise na web". As fontes aparecem como citações em linha e em lista de fontes.

### 4.2 Conferir uma resposta

Retoma-se a alucinação do Módulo 1: uma resposta com link continua podendo estar errada — o link
pode não dizer o que a frase afirma. Procedimento de conferência em quatro passos:

1. **Abrir** a fonte citada (não basta ver o link).
2. **Localizar** o trecho que sustenta a afirmação.
3. **Avaliar** a fonte: oficial, imprensa, blog, fórum?
4. **Triangular** fatos importantes com uma segunda fonte independente.

Para direito, saúde e finanças, a fonte final é a oficial (Planalto, tribunais, órgãos reguladores)
e a resposta não substitui profissional habilitado.

### Solução de Problemas

| Situação | Procedimento |
|---|---|
| Resposta sem fontes | Pedir "pesquise na web e cite as fontes com link" |
| Fonte não contém a informação | Registrar como não sustentada e pedir outra fonte; não usar a afirmação |
| Fonte de baixa qualidade | Pedir "use apenas fontes oficiais" ou indicar o site (`site gov.br`) |

### Pílula Hands-on — Conferência na fonte (6 min)

1. Perguntar com busca: "Qual é o prazo de arrependimento em compras pela internet segundo o
   Código de Defesa do Consumidor? Cite a fonte oficial."
2. Abrir a fonte e localizar o artigo.
3. Conferir em `planalto.gov.br/ccivil_03/leis/l8078compilado.htm` (art. 49).

**Critério de êxito:** prazo de 7 dias confirmado no art. 49 do texto oficial.

## Descrição

- **Objetivos da Aula:** explicar quando e como a busca é acionada, como ler as citações e o
  procedimento de conferência em quatro passos.
- **Habilidades Esperadas:** forçar uma busca, abrir e avaliar fontes e decidir sozinho se uma
  afirmação está sustentada.

---

## Módulo 5 — Arquivos, voz, imagem e Canvas

### 5.1 Arquivos e análise de dados

- **📸 Sugestão de Prints:** menu do botão "+" aberto, mostrando a opção de adicionar fotos e
  arquivos e as ferramentas disponíveis; segundo print com uma planilha anexada e uma tabela de
  resultado na resposta.

O botão "+" permite anexar documentos (PDF, Word, texto), planilhas (CSV, Excel) e imagens. Com
planilhas, o ChatGPT executa **análise de dados**: calcula, organiza tabelas e gera gráficos que
podem ser baixados. No Free, uploads e análise de dados são limitados e tabelas/gráficos
interativos não estão disponíveis (gráfico estático, sim). Limite por arquivo informado na ajuda:
512 MB. Retoma-se o semáforo do Módulo 2: arquivo enviado é dado tratado.

### 5.2 Voz, imagem e Canvas

| Recurso | O que faz | Onde | Free |
|---|---|---|---|
| Voz | Conversa falada; com vídeo nos planos pagos | Ícone de voz na caixa de mensagem | Limitado; com vídeo, não |
| Visão | Lê imagens e fotos enviadas (ex.: foto de um quadro) | "+" > anexar | Limitado |
| Criar imagem | Gera e edita imagens a partir de descrição | "+" > Criar imagem, ou pedir na conversa | Limitado |
| Canvas | Área de edição lado a lado para textos longos e revisão por trechos | "+" > Canvas, ou "abra no canvas" | [conferir disponibilidade] |
| Modo Estudo | Explica passo a passo, com perguntas ao aluno | "+" > Modo Estudo [conferir] | Sim |

### 5.3 Mapa de outros recursos

| Recurso | O que é | Curso que aprofunda |
|---|---|---|
| Pesquisa aprofundada | Relatório longo a partir de muitas fontes | Deep Research - Hands On |
| GPTs | Assistentes prontos ou criados para uma tarefa | GPTs e Ferramentas do ChatGPT |
| Plugins e apps | Conexão com outros serviços | MCP com ChatGPT |
| Tarefas agendadas | Pedidos executados em horário marcado (Go e acima) | — |
| Codex | Programação | ChatGPT CODEX |

### Solução de Problemas

| Situação | Procedimento |
|---|---|
| "Limite de uploads atingido" | Colar o texto na conversa; para planilha pequena, colar as linhas |
| Planilha lida com colunas trocadas | Pedir "mostre as 5 primeiras linhas e os nomes das colunas" antes de analisar |
| Imagem diferente do pedido | Descrever sujeito, estilo, cores e enquadramento; pedir ajuste de um elemento por vez |

### Pílula Hands-on — Arquivo e imagem (6 min)

1. Criar um arquivo de texto com: "mes,visitas\nset,120\nout,150\nnov,90" e salvá-lo como
   `visitas.csv`.
2. Anexar e pedir: "Calcule o total e a média mensal e faça um gráfico de barras."
3. Pedir uma imagem: "Ícone simples de calendário, fundo branco, estilo plano."

**Critério de êxito:** total 360, média 120 e gráfico de três barras; imagem gerada (ou mensagem
de limite registrada).

## Descrição

- **Objetivos da Aula:** apresentar envio de arquivos e análise de dados, voz, visão, imagem,
  Canvas e Modo Estudo, os limites do Free e o mapa dos demais recursos.
- **Habilidades Esperadas:** anexar um arquivo, obter cálculo e gráfico de uma planilha, gerar uma
  imagem e indicar sozinho qual recurso usar para cada tarefa.

---

## Módulo 6 — Síntese e comparação com o Claude Chat

### 6.1 Tabela de simetria

| Função | ChatGPT | Claude |
|---|---|---|
| Preferências permanentes | Instruções personalizadas | Preferências pessoais / instruções do perfil [conferir] |
| Lembrar entre conversas | Memória (memórias salvas e histórico) | Memória |
| Conversa fora do histórico | Chat temporário | Chat anônimo (incógnito) [conferir] |
| Pasta de trabalho | Projetos | Projetos |
| Informação atual | Buscar | Pesquisa na web |
| Documento editável lado a lado | Canvas | Artefatos |
| Gerar imagem | Criar imagem | Não gera imagem fotográfica nativa; cria diagramas e SVG em artefatos |
| Voz | Voz | Modo de voz |

Disponibilidade por plano muda; conferir nas páginas oficiais de preços de cada ferramenta. Cumpre
registrar que a escolha entre ferramentas raramente é absoluta: depende da tarefa, do plano e da
política de dados da organização.

### Atividade integradora (6 min + 4 min de avaliação)

Executar a mesma tarefa nas duas ferramentas, com dados fictícios. Perfil geral: "Resuma em 5
tópicos as regras de arrependimento em compras on-line no Brasil, com fonte oficial." Perfil
jurídico: "Prepare um quadro de 3 linhas comparando arrependimento (art. 49), vício do produto
(art. 18) e prazo para reclamar (art. 26) do CDC, com fonte oficial."

1. Executar no ChatGPT, dentro do projeto "Curso ChatGPT", com busca.
2. Executar no Claude com o mesmo pedido.
3. Conferir uma afirmação de cada resposta na fonte oficial (Módulo 4).
4. Registrar em tabela: formato, fontes, erro encontrado (se houver), preferência e motivo.

| Critério | Atendido? |
|---|---|
| Pedido com tarefa, contexto, público e formato | |
| Nenhum dado de sinal vermelho utilizado | |
| Projeto e busca utilizados no ChatGPT | |
| Uma afirmação de cada ferramenta conferida na fonte oficial | |
| Tabela comparativa com preferência justificada | |

## Descrição

- **Objetivos da Aula:** relacionar os recursos equivalentes do ChatGPT e do Claude e integrar as
  competências do curso numa tarefa única.
- **Habilidades Esperadas:** executar uma tarefa completa com segurança, verificação e
  continuidade, e justificar sozinho a escolha da ferramenta.

---

## Encerramento

O curso apresentou o ChatGPT como assistente de conversa: do pedido estruturado à proteção de
dados, da continuidade por instruções, memória e projetos à busca verificada, aos arquivos e aos
recursos de voz e imagem. Recomenda-se prática diária com tarefas reais de baixo risco, sempre com
o semáforo de dados e a conferência das afirmações importantes.

Para aprofundamento: *ChatGPT Chat - Hands On* (caso completo com projeto, arquivos, busca e
análise de dados), *Gemini Chat - Essentials* (terceiro assistente da trilha) e os cursos indicados
no mapa de recursos.

> **Síntese:** o ChatGPT amplia a capacidade de quem pergunta bem, protege os dados e confere o
> que importa.

---

## Rastreabilidade da auditoria

| Achado | Destino |
|---|---|
| E1 | Módulo 0 (conta, planos, mapa da tela) |
| E2 | Módulo 2 (controles, chat temporário, semáforo, LGPD, sigilo) |
| E3 | Alucinação plantada no M1, retomada no M4 e na integradora |
| E4 | Todas as pílulas com passos e critério observável |
| E5 | Avisos de limite nos M0, M3 e M5 e rotas alternativas |
| E6 | Tabela instruções × memória × projeto (M3) |
| E7 | Seletor explicado por função (M1) |
| E8 | Busca (M4) separada de arquivos, voz, imagem (M5) |
| E9 | Mapa de outros recursos (M5) |
| E10 | Integradora fixa, fictícia, com dois perfis (M6) |
| E11 | Tabela de simetria (M6); plano por linha não incluído: decisão consciente, porque os planos do Claude e do ChatGPT mudaram várias vezes em 2026 — remete às páginas oficiais |
| E12 | "Mão na massa" na versão Articulate; carga 127 min |
| E13 | Exemplos neutros com variação jurídica (M1, M6) |
