# Gemini Chat — Essentials (roteiro final)

**Público-Alvo:** pessoas que ainda não usam IA no dia a dia (T1, posição 3 de 6); advogados,
assessores, estudantes e professores de Direito (J1, posição 3 de 5); profissionais das trilhas de
fundamentos das demais áreas.

**Objetivo Geral:** capacitar o participante a utilizar o app Gemini do Google para pesquisa,
redação, imagem e análise de arquivos, integrado aos apps do Google, com proteção de dados e
verificação de respostas, e a situá-lo em relação ao ChatGPT e ao Claude. Produto final: uma
habilidade (assistente personalizado) aplicada a uma tarefa e um quadro comparativo entre o Gemini
e outro assistente da trilha.

**Pré-requisitos:** nenhum conhecimento técnico; recomendável ter cursado *Claude Chat - Essentials*
e *ChatGPT Chat - Essentials*. Conta Google pessoal; idade mínima de 13 anos (18 anos para
habilidades).

## Estrutura do Curso

| Nível | Módulos | Tempo |
|---|---|---|
| Nível 0 — Preparação | Módulo 0 — Preparação e verificação inicial | 11 min |
| Nível 1 — Fundamentos | Módulo 1 — O que é o Gemini e como conversar; Módulo 2 — Dados, privacidade e sigilo | 46 min |
| Nível 2 — Recursos | Módulo 3 — Personalização e habilidades; Módulo 4 — Pesquisa, verificação e redação; Módulo 5 — Arquivos, imagem e apps do Google | 54 min |
| Nível 3 — Integração | Módulo 6 — Síntese e comparação com ChatGPT e Claude | 16 min |
| **Total** | 7 módulos (6 de conteúdo + síntese) | **127 min** |

Fio condutor: **alucinação** (M1 → M4 → M6) e **Histórico do Gemini** (M2 → M3, memória → M5,
apps conectados exigem o Histórico ativado).

> Dados de planos e recursos conferidos na página oficial de assinaturas (pt-BR), nas notas de
> versão e na Central de Ajuda do Gemini em 17/11/2026. Em novembro de 2026, os Gems estão sendo
> substituídos por habilidades; o curso ensina habilidades.

---

## Módulo 0 — Preparação e verificação inicial

### 0.1 Conta, idade e plano

- **📸 Sugestão de Prints:** página `gemini.google/br/subscriptions` com os quatro cartões de plano
  (sem custo financeiro, Google AI Plus, Google AI Pro, Google AI Ultra) visíveis; destacar o preço
  em reais e a lista de recursos do plano sem custo.

O Gemini é acessado em `gemini.google.com`, pelos apps Android e iOS e por apps de computador para
Windows (atalho Alt + Espaço, segundo as notas de versão) e macOS. Exige conta Google: o curso usa
conta **pessoal**, porque contas de trabalho ou escola (Google Workspace) seguem termos e recursos
definidos pela organização.

| Plano | Preço no Brasil | Uso |
|---|---|---|
| Sem custo financeiro | R$ 0 | Base; inclui imagens, Deep Research, Gemini Live, Canvas e habilidades com uso limitado |
| Google AI Plus | R$ 24,99/mês | 2× o gratuito |
| Google AI Pro | R$ 96,99/mês | 4× o gratuito; maiores de 18 anos |
| Google AI Ultra | a partir de R$ 779,90/mês | 5× ou 20× o Pro; maiores de 18 anos |

Fonte: página oficial de assinaturas, 17/11/2026. Os limites são baseados em computação e
renovam-se de 5 em 5 horas até um teto semanal. Todos os exercícios cabem no plano gratuito.

### 0.2 Mapa da tela

- **📸 Sugestão de Prints:** `gemini.google.com` com conta logada e barra lateral aberta; numerar:
  (1) "Abrir barra lateral"; (2) "Novo chat" e, ao lado, o ícone de chat temporário; (3) seletor de
  modelo; (4) caixa de mensagem com "+" (envio de arquivos) e "Ferramentas"; (5) microfone; (6)
  "Personalizar" no menu à esquerda; (7) foto do perfil.

| Elemento | Onde | Para que serve |
|---|---|---|
| Barra lateral | Ícone "Abrir barra lateral", à esquerda | Conversas recentes, busca, Personalizar, configurações |
| Novo chat / Chat temporário | Topo da barra lateral | Conversa nova; conversa fora do Histórico |
| Seletor de modelo | Junto à caixa de mensagem | Escolher entre resposta rápida e raciocínio |
| "+" | Caixa de mensagem | Enviar arquivos, adicionar do Drive |
| Ferramentas | Caixa de mensagem | Canvas, Deep Research, imagens |
| Personalizar | Menu à esquerda | Como o Gemini responde, apps conectados, habilidades |

### Solução de Problemas

| Situação | Procedimento |
|---|---|
| "Este recurso não está disponível para sua conta" | Conta de trabalho/escola ou idade; usar conta pessoal de maior de 18 anos para habilidades |
| Tela diferente da descrita | Localizar pela função; o Google renomeia recursos com frequência |
| Limite atingido | Aguardar a renovação (ciclos de 5 horas) ou seguir a rota alternativa do exercício |

### Pílula Hands-on — Verificação inicial (4 min)

1. Entrar em `gemini.google.com` com a conta pessoal.
2. Localizar os seis elementos da tabela.
3. Identificar o plano da conta em `Foto do perfil > Configurações` ou na página de assinaturas.

**Critério de êxito:** seis elementos localizados; plano e tipo de conta (pessoal) confirmados.

## Descrição

- **Objetivos da Aula:** apresentar acesso, tipos de conta, idade mínima, planos e interface.
- **Habilidades Esperadas:** entrar no Gemini com a conta adequada, reconhecer o próprio plano e
  localizar sozinho os elementos usados no curso.

---

## Módulo 1 — O que é o Gemini e como conversar

### 1.1 Identidade

- **📸 Sugestão de Prints:** resposta do Gemini com o seletor de modelo aberto, mostrando as opções
  de resposta rápida e de raciocínio disponíveis no plano gratuito.

O nome "Gemini" designa coisas distintas, e a confusão é frequente:

| Nome | O que é |
|---|---|
| App Gemini | O assistente de conversa (objeto deste curso), sucessor do Bard, renomeado em fevereiro de 2024 |
| Modelos Gemini | Os "motores" de IA (em novembro de 2026, família Gemini 4: Hydrogen, Argon, Carbon; e modelos Flash) |
| Gemini no Google Workspace | O assistente dentro do Gmail, Documentos, Planilhas e Meet (curso *Gemini Workspace - Essentials*) |
| Google Assistente | O assistente de voz anterior, sendo substituído pelo Gemini no celular |

O núcleo é um **modelo de linguagem**, que produz texto prevendo a continuação mais provável de um
pedido. Daí a **alucinação**: resposta errada dita com confiança, consequência do funcionamento e
não defeito raro. O tema é retomado no Módulo 4. O seletor oferece, em essência, **resposta
rápida** e **raciocínio**; os nomes comerciais mudam, e convém escolher pela função.

### 1.2 Anatomia do pedido segundo o Google

O guia oficial de prompts do Google organiza o pedido em quatro elementos: **persona** (quem o
Gemini deve ser), **tarefa** (o que fazer), **contexto** (situação e dados) e **formato** (como
entregar). Corresponde ao quadro tarefa/contexto/público/formato visto no curso do ChatGPT, com a
persona no lugar do público.

| Pedido vago | Pedido estruturado |
|---|---|
| "Faça um aviso do evento." | "Você é assessor de comunicação de uma associação de bairro (persona). Escreva um aviso (tarefa) sobre um mutirão de orientação gratuita no sábado, das 9h às 17h, no centro comunitário, para moradores sem familiaridade com termos jurídicos (contexto). Até 80 palavras, com título e três tópicos (formato)." |

Variação jurídica: "Você é advogado de um núcleo de prática jurídica. Explique a um cidadão, em 5
linhas e sem jargão, o que é a audiência de conciliação."

A conversa é cumulativa: refina-se com mensagens de acompanhamento, editando a própria mensagem ou
pedindo nova versão da resposta.

### Pílula Hands-on — Do vago ao estruturado (6 min)

1. Enviar: "Faça um aviso do evento."
2. Enviar a versão estruturada do exemplo.
3. Pedir: "Agora em versão para WhatsApp, com no máximo 3 linhas."

**Critério de êxito:** a segunda resposta tem título, três tópicos e até 80 palavras; a terceira,
até 3 linhas.

### Avaliação — questão (4 min)

Ao pedir "quais são os direitos do consumidor que compra pela internet?", o Gemini cita "art. 49
da Lei 8.078/1990, prazo de 15 dias". A conduta adequada é:

a) aceitar, pois há número de lei; b) pedir ao Gemini que confirme; c) conferir o artigo no texto
oficial do Planalto; d) trocar de modelo e aceitar a nova resposta.

**Gabarito:** c. O art. 49 prevê 7 dias; o número de lei dá aparência de precisão, mas não prova.

## Descrição

- **Objetivos da Aula:** distinguir app, modelos, Workspace e Assistente; explicar modelo de
  linguagem, alucinação e seletor; apresentar persona, tarefa, contexto e formato.
- **Habilidades Esperadas:** redigir um pedido estruturado, refiná-lo e reconhecer quando a
  resposta exige conferência.

---

## Módulo 2 — Dados, privacidade e sigilo

### 2.1 O Histórico do Gemini

- **📸 Sugestão de Prints:** `myactivity.google.com/product/gemini` com o controle do Histórico e a
  opção de exclusão automática visível (18 meses destacado); segundo print de um chat temporário
  aberto, com o indicador de chat temporário no topo.

A configuração central chama-se **Histórico do Gemini** (nomes anteriores: "Atividade nos Apps do
Gemini" e "Manter atividade") e é gerida em `myactivity.google.com/product/gemini`. Segundo a
Central de privacidade dos apps do Gemini (17/11/2026):

| Situação | O que ocorre |
|---|---|
| Histórico ativado | Conversas ficam salvas e podem ser usadas para melhorar os serviços e treinar modelos, conforme as configurações; exclusão automática padrão de 18 meses (opções: 3 ou 36 meses, ou nunca) |
| Revisão humana | Um subconjunto de conversas é lido por revisores; as revisadas ficam até 3 anos, mesmo após exclusão |
| Histórico desativado | Conversas futuras não aparecem no Histórico, não treinam modelos (salvo feedback enviado) e ficam salvas por cerca de 2 meses; alguns apps conectados deixam de funcionar |
| Chat temporário | Não entra no Histórico nem personaliza; fica cerca de 2 meses; não treina modelos |
| Conta Google Workspace | Dados da organização não são usados para treinar modelos nem para anúncios (página de planos do Workspace) |

O próprio Google recomenda não inserir informação confidencial que não se queira ver lida por
revisores.

### 2.2 O semáforo de dados

| Sinal | Exemplos | Conduta |
|---|---|---|
| Verde | Textos públicos, dados fictícios, conteúdo próprio sem dados pessoais | Pode enviar |
| Amarelo | Documentos internos sem dados pessoais | Só com autorização, preferencialmente em conta Workspace da organização |
| Vermelho | Dados pessoais de terceiros, segredos comerciais, documentos de clientes, processos sob segredo | Não enviar em conta pessoal |

A LGPD (Lei 13.709/2018) exige base legal e finalidade para tratar dados pessoais; para o público
jurídico, acresce o sigilo profissional. Conectar ao Gemini um Gmail pessoal que recebe e-mails de
clientes coloca esses e-mails ao alcance das perguntas — decisão a tomar antes de conectar
(Módulo 5).

### Pílula Hands-on — Configurar o Histórico (7 min)

1. Abrir `myactivity.google.com/product/gemini`.
2. Verificar se o Histórico está ativado e qual é o prazo de exclusão automática; ajustar, se
   desejado.
3. No Gemini, abrir um chat temporário (ícone ao lado de "Novo chat"), enviar uma pergunta e
   confirmar que ela não aparece nas conversas recentes.

**Critério de êxito:** estado do Histórico e prazo de exclusão anotados; chat temporário ausente da
lista.

### Discussão orientada (8 min)

Classificar: (1) notícia de jornal; (2) planilha de inscritos com nome e telefone; (3) e-mail de
cliente com relato de processo; (4) planilha de inscritos só com códigos (I01, I02...) e tema; (5)
rascunho próprio de artigo de opinião.
**Gabarito:** 1 verde; 2 vermelho; 3 vermelho; 4 verde (sem dado que identifique pessoa); 5 verde.

## Descrição

- **Objetivos da Aula:** explicar o Histórico do Gemini, a revisão humana, os prazos de retenção, o
  chat temporário, a diferença entre conta pessoal e Workspace e o semáforo de dados.
- **Habilidades Esperadas:** configurar o Histórico, abrir chat temporário e decidir sozinho o que
  pode ser enviado ou conectado.

---

## Módulo 3 — Personalização e habilidades

### 3.1 Personalizar, memória e informações salvas

- **📸 Sugestão de Prints:** menu à esquerda com "Personalizar" aberto, mostrando as áreas de
  instruções de resposta, apps e habilidades; segundo print de
  `gemini.google.com/personalization-settings` com a lista de memórias.

Desde outubro de 2026, o item **Personalizar**, no menu à esquerda, reúne em um só lugar como o
Gemini responde, os apps conectados e as habilidades. Três camadas dão continuidade:

| Recurso | O que guarda | Onde gerenciar |
|---|---|---|
| Informações salvas | Preferências e fatos que o usuário escreve ("responda sempre em tópicos") | `gemini.google.com/saved-info` |
| Memória | Fatos extraídos de conversas anteriores do Histórico (antes "conversas anteriores") | `gemini.google.com/personalization-settings`; perguntar "o que você sabe sobre mim?" |
| Habilidades | Instruções reutilizáveis para tarefas específicas | `Personalizar > Habilidades` [conferir] |

Retoma-se o Módulo 2: a memória depende do Histórico; com ele desativado, não há personalização
por conversas anteriores. Desde março de 2026, é possível importar memória e histórico de outros
assistentes; convém aplicar o semáforo antes, porque a importação traz para o Google o que estava
em outra empresa.

### 3.2 Habilidades (antigos Gems)

Uma **habilidade** é um conjunto salvo de instruções que diz ao Gemini como executar uma tarefa —
análoga a uma receita guardada. Pode ser criada "com o Gemini" (descreve-se o objetivo e o
assistente redige as instruções) ou manualmente (nome, descrição, instruções), acionada digitando
"/" ou "@" seguido do nome, ou automaticamente quando o pedido corresponde, e combinada com outras.
As habilidades substituem os **Gems**: em contas pessoais, os Gems são descontinuados em novembro
de 2026 e migram como rascunhos inativos, que precisam ser revisados e ativados. Disponíveis no
plano gratuito, por ora para maiores de 18 anos.

### Solução de Problemas

| Situação | Procedimento |
|---|---|
| Não há "Habilidades" | Conta menor de 18 anos, conta Workspace ou liberação incompleta; usar a rota: colar as instruções no início da conversa |
| A habilidade não é acionada | Digitar "/" e escolher pelo nome; conferir se está ativa |
| Gems antigos sumiram | Procurar em Personalizar como rascunhos inativos e ativá-los |

### Pílula Hands-on — Habilidade "Texto claro" (6 min)

1. Em `Personalizar > Habilidades > Criar manualmente` [conferir], criar "Texto claro" com a
   instrução: "Reescreva o texto recebido em linguagem simples, frases de até 20 palavras, sem
   jargão; liste ao final os termos técnicos que foram substituídos."
2. Em conversa nova, digitar "/Texto claro" e colar: "O requerente pleiteia a concessão de tutela
   de urgência, ante a presença do periculum in mora."

**Critério de êxito:** texto reescrito sem "periculum in mora" e "tutela de urgência" no corpo,
com os termos listados ao final.

## Descrição

- **Objetivos da Aula:** apresentar Personalizar, informações salvas, memória, importação e
  habilidades, e a transição dos Gems.
- **Habilidades Esperadas:** registrar preferências, revisar a memória e criar e acionar sozinho
  uma habilidade.

---

## Módulo 4 — Pesquisa, verificação e redação

### 4.1 Pesquisa com fontes e verificação

- **📸 Sugestão de Prints:** resposta com fontes da Pesquisa Google visíveis; segundo print do menu
  de opções da resposta aberto, com a opção de verificar a resposta com a Pesquisa Google destacada.

O Gemini consulta a Pesquisa Google quando a pergunta envolve fatos atuais e pode indicar as fontes.
A resposta oferece ainda a opção de **verificar a resposta** com a Pesquisa Google [conferir
rótulo], que marca trechos com conteúdo semelhante ou divergente na web. Retoma-se a alucinação do
Módulo 1: marcação não é prova. Procedimento: **abrir** a fonte, **localizar** o trecho,
**avaliar** a fonte e **triangular**; em direito, saúde e finanças, a fonte final é a oficial.

### 4.2 Redação no Canvas

O **Canvas** (`Ferramentas > Canvas`) abre um documento ao lado da conversa: o texto pode ser
editado diretamente ou por trechos selecionados ("mais formal", "mais curto"), e exportado para o
Documentos Google. O **Deep Research** (`Ferramentas > Deep Research`) gera relatórios longos a
partir de muitas fontes — objeto do curso *Deep Research - Hands On*.

### Solução de Problemas

| Situação | Procedimento |
|---|---|
| Resposta sem fontes | Pedir "pesquise e indique os links das fontes" |
| Verificação marca trecho como divergente | Abrir a fonte; não usar a afirmação até conferir |
| Canvas não aparece | Procurar em Ferramentas; ou pedir "abra no Canvas" |

### Pílula Hands-on — Conferir e redigir (6 min)

1. Perguntar: "Como a LGPD define 'dado pessoal'? Indique a lei, o artigo e o link oficial."
2. Conferir em `planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm`, art. 5º, I.
3. Em `Ferramentas > Canvas`, pedir um parágrafo de 5 linhas explicando a definição a um leigo.

**Critério de êxito:** definição conferida no art. 5º, I ("informação relacionada a pessoa natural
identificada ou identificável"); parágrafo no Canvas.

## Descrição

- **Objetivos da Aula:** explicar a pesquisa com fontes, a verificação da resposta, o procedimento
  de conferência, o Canvas e onde fica o Deep Research.
- **Habilidades Esperadas:** pesquisar, verificar e conferir na fonte oficial e redigir e ajustar
  sozinho um texto no Canvas.

---

## Módulo 5 — Arquivos, imagem e apps do Google

### 5.1 Arquivos

- **📸 Sugestão de Prints:** menu "+" aberto, com "Fazer upload de arquivos" e "Adicionar do Drive"
  visíveis; segundo print de uma resposta com tabela e gráfico gerados a partir de planilha.

O "+" envia documentos, planilhas, imagens, áudio e vídeo, do computador ou do Drive. Limites
oficiais (17/11/2026): até 10 arquivos por comando; 100 MB por arquivo (vídeo até 2 GB); no
gratuito, vídeo até 5 min e áudio até 10 min no total. O Gemini resume PDFs, calcula e organiza
planilhas e gera gráficos. Retoma-se o semáforo do Módulo 2.

### 5.2 Imagem

A geração e a edição de imagens funcionam pela conversa ("crie uma imagem de...") ou por
`Ferramentas > Imagens` [conferir], com uso limitado no gratuito. Imagem como assunto principal é
tema de *Imagem com IA*.

### 5.3 Apps do Google conectados

O Gemini pode consultar Gmail, Drive e Agenda da conta e criar eventos, quando autorizado em
`Personalizar > Apps` [conferir]. Retoma-se o Histórico do Módulo 2: **os apps conectados exigem o
Histórico ativado** — logo, conectar é uma decisão de dados. Recomenda-se conectar apenas contas
cujo conteúdo esteja em sinal verde e desconectar quando não houver uso. Outros 40+ apps de
terceiros podem ser conectados, a maioria em inglês e nos EUA.

| Recurso | O que é | Curso que aprofunda |
|---|---|---|
| Deep Research | Relatórios a partir de muitas fontes | Deep Research - Hands On |
| Gemini Live | Conversa por voz, com câmera e tela | — |
| Gemini Notebook / NotebookLM | Pesquisa e escrita sobre fontes próprias | NotebookLM - Essentials |
| Gemini no Workspace | Gemini dentro do Gmail, Documentos, Meet | Gemini Workspace - Essentials |

### Solução de Problemas

| Situação | Procedimento |
|---|---|
| "Não consigo acessar seu Gmail" | Conferir se o Histórico está ativado e o app conectado em Personalizar |
| Planilha lida errada | Pedir "mostre as 5 primeiras linhas e as colunas" |
| Arquivo recusado | Limite de 100 MB ou 10 arquivos; dividir ou colar o texto |

### Pílula Hands-on — Planilha e imagem (6 min)

1. Salvar `atendimentos.csv` com: "dia,atendimentos / seg,14 / ter,22 / qua,18" (uma linha por
   item, sem as barras).
2. Enviar pelo "+" e pedir: "total, média por dia e gráfico de barras".
3. Pedir: "Crie um ícone simples de balança da justiça, estilo plano, fundo branco."

**Critério de êxito:** total 54, média 18, gráfico de três barras; imagem gerada ou limite
registrado.

## Descrição

- **Objetivos da Aula:** apresentar envio de arquivos e limites, imagem, apps do Google e sua
  relação com o Histórico, e o mapa dos demais recursos.
- **Habilidades Esperadas:** analisar uma planilha, gerar uma imagem e decidir sozinho se e quando
  conectar Gmail, Drive e Agenda.

---

## Módulo 6 — Síntese e comparação com ChatGPT e Claude

### 6.1 Tabela de simetria

| Função | Gemini | ChatGPT | Claude |
|---|---|---|---|
| Preferências permanentes | Informações salvas / Personalizar | Instruções personalizadas | Preferências do perfil [conferir] |
| Lembrar entre conversas | Memória | Memória | Memória |
| Fora do histórico | Chat temporário | Chat temporário | Chat incógnito [conferir] |
| Instruções reutilizáveis | Habilidades | GPTs / instruções de projeto | Projetos / Skills |
| Pasta de trabalho | — (sem equivalente direto) | Projetos | Projetos |
| Informação atual | Pesquisa Google + verificação | Buscar | Pesquisa na web |
| Documento lado a lado | Canvas | Canvas | Artefatos |
| Apps conectados | Gmail, Drive, Agenda (exigem Histórico) | Plugins/apps | Conectores |

Disponibilidade por plano muda; conferir nas páginas oficiais. O diferencial do Gemini é a
integração nativa com a conta Google; a contrapartida é a dependência do Histórico ativado.

### Atividade integradora (6 min + 4 min de avaliação)

Com dados públicos ou fictícios: "Explique a um cidadão, em 5 tópicos, o que é dado pessoal na
LGPD, com fonte oficial." (Perfil jurídico: acrescentar "e diferencie dado pessoal de dado pessoal
sensível, art. 5º, I e II".)

1. Executar no Gemini com a habilidade "Texto claro" ("/Texto claro" após a resposta).
2. Executar o mesmo pedido no ChatGPT ou no Claude.
3. Conferir uma afirmação de cada resposta no Planalto.
4. Registrar: formato, fontes, erro encontrado, preferência e motivo.

| Critério | Atendido? |
|---|---|
| Pedido com persona, tarefa, contexto e formato | |
| Nenhum dado de sinal vermelho | |
| Habilidade aplicada no Gemini | |
| Uma afirmação de cada ferramenta conferida no Planalto | |
| Comparação com preferência justificada | |

## Descrição

- **Objetivos da Aula:** relacionar recursos equivalentes nos três assistentes e integrar as
  competências numa tarefa.
- **Habilidades Esperadas:** executar uma tarefa completa no Gemini com segurança e verificação e
  justificar sozinho a escolha do assistente.

---

## Encerramento

O curso apresentou o app Gemini: identidade, pedido estruturado, Histórico e privacidade,
personalização e habilidades, pesquisa verificada, Canvas, arquivos, imagem e apps do Google.
Recomenda-se prática regular com tarefas de baixo risco, decidindo antes o que pode ser enviado e
conectado, e conferindo as afirmações relevantes.

Para aprofundamento: *Gemini Chat - Hands On* (caso completo com habilidade, planilha, Gmail,
Agenda e Canvas), *Gemini Workspace - Essentials*, *NotebookLM - Essentials* e *Deep Research -
Hands On*.

> **Síntese:** o Gemini rende mais quando conhece a conta do usuário — e por isso exige que o
> usuário decida, antes, o que ele pode conhecer.

---

## Rastreabilidade da auditoria

| Achado | Destino |
|---|---|
| G1 | Habilidades (M3, M6); Gems só como nome antigo; rota sem habilidades |
| G2 | Módulo 0 |
| G3 | Módulo 2 |
| G4 | M5.3 (apps exigem Histórico; decisão antes de conectar) |
| G5 | Tabela de identidade (M1) |
| G6 | Alucinação M1 → M4 → M6; verificação com Pesquisa Google e fonte oficial |
| G7 | Módulo 3 |
| G8 | Pílulas com dados embutidos e critérios observáveis |
| G9 | Tabela de três colunas e integradora (M6) |
| G10 | Limites oficiais e rotas (M5) |
| G11 | "Mão na massa" na versão Articulate; 127 min |
| Roadmap | Importação de memória (M3), app Windows (M0), Live e Deep Research no mapa (M5); YouTube não incluído por falta de fonte oficial lida sobre o recurso — decisão consciente |
