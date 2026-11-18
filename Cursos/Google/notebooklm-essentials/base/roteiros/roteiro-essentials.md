# NotebookLM - Essentials — Roteiro Final

**Público-Alvo:** estudantes, pesquisadores, jornalistas e analistas (trilha Pesquisa com IA);
professores, coordenadores pedagógicos e designers instrucionais (trilha IA para educadores);
advogados, assessores jurídicos, estudantes e professores de Direito (trilha Pesquisa e
fundamentação jurídica).

**Objetivo Geral:** capacitar o participante a utilizar o NotebookLM — denominado Gemini Notebook
desde 16/07/2026 — para estudar e sintetizar um conjunto delimitado de fontes próprias, com
segurança e com verificação sistemática das citações. Ao final, o participante terá montado um
notebook com quatro fontes públicas, obtido respostas auditadas por meio das citações e gerado,
no painel Estúdio, documento de resumo, guia de estudo e Resumo em Áudio.

**Pré-requisitos:** uso básico de um assistente de IA (ChatGPT, Claude ou Gemini); Conta Google
pessoal, de trabalho ou escolar; nenhum conhecimento técnico. Plano gratuito suficiente.

**Recursos necessários:** computador com navegador atualizado e internet; acesso a
`notebook.google.com`.

> Nota de vigência: dados de planos, limites e rótulos de interface foram extraídos da Central de
> Ajuda oficial consultada em 17/10/2026. Itens marcados com **[conferir]** dependem de validação
> na conta usada para a produção do curso.

## Estrutura do Curso

| Nível | Módulo | Título | Tempo |
|---|---|---|---|
| Nível 0 — Pré-filtro | 0 | Preparação e Verificação Inicial | 7 min |
| Nível 1 — Fundamentos | 1 | O que é o NotebookLM: respostas ancoradas em fontes | 25 min |
| Nível 1 — Fundamentos | 2 | Segurança, Privacidade e Uso Responsável | 19 min |
| Nível 2 — Operação | 3 | Fontes: tipos, limites e montagem do notebook | 20 min |
| Nível 2 — Operação | 4 | Conversa com citações e auditoria das respostas | 20 min |
| Nível 2 — Operação | 5 | Painel Estúdio: resumo, guia de estudo e Resumo em Áudio | 20 min |
| Síntese | 6 | Síntese e Aplicação Integrada | 18 min |
| **Total** | | | **129 min** |

Tempos apurados pela MET em `carga-horaria/carga-horaria-essentials.md`.

**Anexos:** A — Kit de fontes do Caderno LGPD; B — Rastreabilidade da auditoria.

**Fio condutor:** a analogia da **prova com consulta**, plantada no Módulo 1, é retomada no
Módulo 2 (o que pode ser entregue para consulta), no Módulo 4 (conferir a consulta) e no Módulo 5
(o artefato também é uma síntese falível).

**Fronteira do curso:** Deep Research (pesquisa automatizada na web), checagem acadêmica sistemática
de citações e comparação com Projetos de outras ferramentas são tratados, respectivamente, nos
cursos *Deep Research - Hands On*, *Checagem de Fontes e Citações - Essentials* e *RAG e Bases de
Conhecimento - Essentials*.

---

## Módulo 0 — Preparação e Verificação Inicial

> Ponto de partida: módulo de pré-filtro, anterior a qualquer uso da ferramenta.

### 0.1 Verificação de acesso e ambiente

- **📸 Sugestão de Prints:** (1) navegador no computador com a barra de endereço exibindo
  `notebook.google.com` e a tela inicial da ferramenta, com o botão "Criar novo notebook" destacado
  por contorno; (2) canto superior direito da tela, com o avatar da Conta Google destacado e o menu
  da conta aberto mostrando o endereço de e-mail em uso; (3) eventual mensagem de serviço
  indisponível exibida a contas Workspace não habilitadas, se for possível reproduzi-la.

O NotebookLM é utilizado, neste curso, pela versão web, acessada no navegador do computador.
Existem aplicativos para Android (versão 10 ou posterior) e para iPhone/iPad, mas eles não oferecem
paridade de recursos: configuração do chat, notas, mapas mentais, relatórios e tabelas de dados,
entre outros, estão disponíveis integralmente apenas no navegador. Recomenda-se, portanto, que o
celular seja reservado a usos complementares, como a escuta de Resumos em Áudio.

O acesso exige uma Conta Google. Cumpre distinguir dois casos. Em **conta pessoal** (por exemplo, um
endereço Gmail), o serviço está disponível diretamente, no plano gratuito. Em **conta de trabalho ou
escolar** (Google Workspace ou Workspace for Education), o serviço depende de o administrador do
domínio tê-lo habilitado para o usuário; se a tela inicial não abrir, a causa provável é essa, e
a solução cabe ao setor de tecnologia da instituição. A diferença entre os dois tipos de conta será
retomada no Módulo 2, pois altera o tratamento dos dados.

Convém registrar, desde já, o nome exibido pela ferramenta. Em 16/07/2026, o Google renomeou o
NotebookLM para **Gemini Notebook**; a mudança, contudo, ainda não alcançou uniformemente a interface
e as páginas de ajuda, de modo que ambos os nomes podem aparecer. Trata-se do mesmo produto. Para
evitar ambiguidade, este curso indica a navegação a partir do endereço `notebook.google.com`, que não
depende da marca.

O plano gratuito (Standard) é suficiente para todas as atividades. Segundo a ajuda oficial consultada
em 17/10/2026, ele admite 100 notebooks, 50 fontes por notebook, 50 conversas por dia, 3 Resumos em
Áudio por dia e 10 relatórios por dia. Desde 02/09/2026, a documentação descreve também limites
baseados em consumo computacional, renovados a cada cinco horas até um teto semanal. Recomenda-se,
por isso, não gerar artefatos repetidamente durante o curso.

### 0.2 Prompt-base (Mão na massa) — registro de verificação

Modelo de registro para preenchimento pelo participante:

"""
Conta utilizada: [endereço de e-mail]
Tipo de conta: [pessoal | trabalho | escolar]
Nome exibido pela ferramenta: [NotebookLM | Gemini Notebook]
Idioma da interface: [português | inglês | misto]
Dispositivo para o curso: computador, navegador [nome]
"""

### Pílula Hands-on — Verificação de acesso (7 min)

1. Abrir o navegador no computador e acessar `notebook.google.com`.
2. Entrar com a Conta Google escolhida.
3. Confirmar, no canto superior direito, qual conta está ativa.
4. Localizar o botão "Criar novo notebook" na tela inicial, sem clicá-lo ainda.
5. Preencher o registro de verificação.

**Critério de êxito:** a tela inicial exibe o botão "Criar novo notebook" e o registro está
preenchido com tipo de conta e nome exibido.

### Solução de Problemas

| Situação | Causa provável | Procedimento |
|---|---|---|
| A ferramenta informa que o serviço não está disponível | Conta Workspace/Education não habilitada | Solicitar habilitação ao administrador ou usar conta pessoal com fontes públicas |
| A interface está em inglês | Idioma da Conta Google | Ajustar o idioma da Conta Google ou seguir os nomes em inglês indicados entre parênteses neste curso |
| Abriu outra conta | Várias contas no navegador | Trocar de conta pelo avatar no canto superior direito |

## Descrição

- **Objetivos da Aula:** apresentar os requisitos de acesso, a diferença entre conta pessoal e conta
  institucional, a coexistência dos nomes NotebookLM e Gemini Notebook e os limites do plano gratuito.
- **Habilidades Esperadas:** o participante acessa a ferramenta sozinho, identifica o tipo de conta
  em uso e reconhece o produto independentemente do nome exibido.

---

## Módulo 1 — O que é o NotebookLM: respostas ancoradas em fontes

> Pré-requisito: Módulo 0. Desloca-se o foco do acesso para o conceito que distingue a ferramenta.

### 1.1 Texto descritivo — ancoragem, citações e estrutura

- **📸 Sugestão de Prints:** notebook aberto com as três áreas visíveis — painel Fontes à esquerda,
  painel Conversa ao centro e painel Estúdio à direita —, cada uma identificada por rótulo
  sobreposto; e uma resposta da Conversa com um número de citação sob o cursor, exibindo a caixa
  com o trecho da fonte.

O NotebookLM é um assistente de pesquisa e estudo desenvolvido pelo Google. Lançado publicamente em
julho de 2023, chegou ao Brasil em junho de 2024, com suporte ao português, e passou a chamar-se
Gemini Notebook em julho de 2026. Sua unidade de trabalho é o **notebook** (caderno): um contêiner
dedicado a um tema, que reúne as **fontes** — documentos, páginas, vídeos ou áudios escolhidos pelo
usuário —, a conversa sobre elas, as notas e os materiais gerados. Pode-se compreendê-lo como uma
pasta de pesquisa que, além de guardar os documentos, é capaz de lê-los e explicá-los.

O princípio que distingue a ferramenta de um chat de IA de uso geral denomina-se **ancoragem**
(em inglês, *grounding*): as respostas são produzidas a partir do conjunto de fontes selecionado.
Um chat geral pode recorrer ao conhecimento interno do modelo, à web e a outras ferramentas; o
notebook privilegia o corpus delimitado pelo usuário. A analogia adequada é a de uma **prova com
consulta**, na qual o estudante somente pode utilizar os textos entregues. Essa analogia servirá de
fio condutor ao curso: ela indica o que a ancoragem oferece — respostas restritas a material
conhecido — e também o que não oferece, pois um estudante com consulta ainda pode interpretar mal o
texto que tem diante de si.

Cada resposta é acompanhada de **citações** numeradas. Ao posicionar o cursor sobre o número,
exibe-se o trecho utilizado; ao clicá-lo, abre-se a fonte na posição correspondente. Cumpre
registrar que a citação é um caminho para a conferência, e não um selo automático de veracidade: o
modelo seleciona trechos, resume e relaciona ideias, podendo citar um trecho real que não sustenta a
frase inteira, omitir uma ressalva ou conciliar indevidamente fontes divergentes. Depreende-se que a
abertura da citação integra o fluxo de trabalho, e não constitui etapa opcional.

A interface organiza-se em três painéis. O painel **Fontes** (*Sources*) lista os materiais
importados, cada qual com uma caixa de seleção que define se ele participa da conversa. O painel
**Conversa** (*Chat*) recebe perguntas em linguagem natural. O painel **Estúdio** (*Studio*) produz
**artefatos** — saídas persistentes e reutilizáveis, como relatórios, guias de estudo, Resumos em
Áudio, mapas mentais, cartões de estudo e testes. Convém distinguir, desde já, a resposta da
conversa, que é efêmera e conversacional, do artefato, que é um objeto salvo no notebook.

Observa-se, por fim, que a ferramenta é especialmente adequada a quem precisa estudar, comparar e
explicar um conjunto delimitado de materiais: o estudante diante de artigos para uma prova, o
professor que prepara um guia para a turma, o advogado que organiza legislação e decisões públicas,
o jornalista que trabalha com os documentos de uma apuração. Quando o problema é descobrir páginas
atuais na web, outras ferramentas são mais indicadas — tema retomado no Módulo 6.

### 1.2 Exemplo aplicado — chat geral × notebook e anatomia de um pedido ancorado

- **📸 Sugestão de Prints:** não se aplica (conteúdo tabular e textual).

| Aspecto | Chat de IA de uso geral | Notebook do NotebookLM |
|---|---|---|
| Base da resposta | Conhecimento do modelo, web, memória e ferramentas | Fontes selecionadas no painel Fontes |
| Delimitação do que conta como evidência | Implícita | Explícita, por caixa de seleção |
| Verificação | Depende de a ferramenta citar páginas | Citação abre o trecho exato da fonte |
| Pergunta fora do material | Responde com conhecimento geral | Tende a recusar ou responder de modo insuficiente |
| Risco residual | Invenção de fatos e referências | Interpretação incorreta de trecho real |

Um pedido ancorado bem formulado contém cinco elementos: tarefa, escopo, formato, tratamento de
divergências e exigência de citação. O prompt-base a seguir exemplifica a estrutura e será
utilizado no Módulo 4.

### 1.3 Prompt-base (Mão na massa) — pedido ancorado

"""
Explique [tema] para uma pessoa iniciante. Use somente as fontes selecionadas.
Para cada afirmação central, inclua uma citação. Se as fontes divergirem, apresente
as versões separadamente. Se a informação não estiver nas fontes, escreva
"não encontrado nas fontes".
"""

### Pílula Hands-on — Verificação de compreensão (4 min)

**Questão 1.** Uma resposta do notebook traz a citação [2] ao final de uma frase decisiva. Qual
conduta é a recomendada?

a) Aceitar a frase, pois a citação comprova sua veracidade.
b) Abrir a citação e comparar a frase gerada com o trecho original.
c) Reformular a pergunta até obter uma resposta sem citação.
d) Copiar a resposta para outro chat e pedir confirmação.

**Gabarito:** b. A citação indica de onde a resposta partiu, mas a frase gerada pode exagerar,
inverter ou combinar trechos; a conferência no original é parte do fluxo.

**Questão 2.** Na analogia da prova com consulta, o que corresponde ao "material entregue"?

a) O conhecimento interno do modelo de IA.
b) Os resultados de uma busca na web.
c) As fontes marcadas no painel Fontes.
d) O histórico de conversas da Conta Google.

**Gabarito:** c. A ancoragem restringe a resposta ao conjunto de fontes selecionado.

## Descrição

- **Objetivos da Aula:** apresentar o conceito de notebook e fonte, o princípio da ancoragem, a
  função e o limite das citações, os três painéis da interface e a distinção entre resposta e
  artefato.
- **Habilidades Esperadas:** o participante explica, com as próprias palavras, por que uma resposta
  com citação ainda precisa ser conferida, e identifica em que situações um notebook é preferível a
  um chat geral.

---

## Módulo 2 — Segurança, Privacidade e Uso Responsável

> Pré-requisito: Módulo 1. Antes do primeiro upload, o foco desloca-se do conceito para o que pode ser entregue à "consulta".

### 2.1 Texto descritivo — dados, contas e compartilhamento

- **📸 Sugestão de Prints:** (1) janela "Compartilhar" de um notebook aberta, com o campo de pessoas,
  o seletor de papel exibindo "Leitor" e "Editor" e a opção de acesso por link destacada; (2) botões
  de avaliação positiva/negativa (feedback) de uma resposta da Conversa, destacados com um aviso
  sobreposto.

Retomando a analogia do Módulo 1: se o notebook é uma prova com consulta, cumpre decidir o que pode
ser entregue para consulta. Toda fonte importada é enviada aos servidores do Google e processada
remotamente. A primeira decisão de segurança, portanto, ocorre antes do upload, e não depois.

O tratamento dos dados difere conforme o tipo de conta. Em **conta pessoal**, o Google informa que os
dados do notebook não são usados diretamente para treinar os modelos fundamentais, **salvo quando o
usuário envia feedback**: ao avaliar uma resposta positiva ou negativamente, o pacote enviado pode
incluir o prompt, as fontes, os uploads e as saídas, pode ser revisado por pessoas e pode ser retido,
desassociado da conta, por até três anos. Recomenda-se, por conseguinte, não enviar feedback em
notebooks com material sensível. Em **contas Workspace e Education**, a documentação informa que
uploads, consultas e respostas não são revisados por pessoas nem usados para treinar modelos
generativos, aplicando-se os termos contratuais da instituição. Essa garantia, contudo, não dispensa
o cumprimento dos deveres legais de quem trata os dados.

No Brasil, o uso de documentos com dados pessoais submete-se à Lei Geral de Proteção de Dados (Lei
nº 13.709/2018). Antes de carregar dados pessoais, convém definir a finalidade, a base legal, o acesso
e o tempo de permanência, e aplicar a **minimização**: remover CPF, endereço, contatos, prontuários,
avaliações individuais e outros identificadores que não sejam indispensáveis. A Autoridade Nacional
de Proteção de Dados (ANPD) alerta que dados pessoais podem surgir em todo o ciclo da IA generativa —
nos documentos de entrada, nos prompts e nas saídas — e que a anonimização imperfeita pode permitir a
reidentificação. Na advocacia, acresce-se o **sigilo profissional**: peças, comunicações com o
cliente e estratégia processual não devem ser inseridas em conta pessoal sem autorização e controles
institucionais, conforme a recomendação do Conselho Federal da OAB sobre o uso de IA.

O compartilhamento constitui o segundo ponto de exposição. Um notebook pode ser compartilhado com
pessoas específicas, nos papéis de **Leitor** (acesso de leitura às fontes e notas e uso da conversa)
ou **Editor** (pode adicionar e remover fontes e compartilhar). Em conta pessoal, admite-se ainda o
acesso por link a qualquer pessoa com Conta Google. Cumpre advertir que a opção de exibir apenas a
conversa ("visualização da conversa" **[conferir rótulo]**) oculta fontes e artefatos na apresentação,
mas **não revoga** o acesso subjacente do destinatário: não deve ser usada para simular proteção de
documento sigiloso. Recomenda-se o princípio do menor privilégio — Leitor em vez de Editor, pessoas
específicas em vez de link público — e a remoção das fontes quando a finalidade se encerrar.

Para orientar a decisão, propõe-se uma classificação em três níveis. **Verde:** material público e
oficial, como leis, guias de órgãos públicos e artigos de acesso aberto — pode ser usado em qualquer
conta. **Amarelo:** material interno sem dados pessoais — somente em conta institucional autorizada.
**Vermelho:** dados pessoais de alunos, clientes, pacientes ou fontes jornalísticas, e documentos
sob sigilo — não deve ser carregado sem base legal, ambiente institucional aprovado e minimização
prévia. Todas as atividades deste curso utilizam exclusivamente material verde.

### 2.2 Prompt-base (Mão na massa) — ficha de decisão antes do upload

Ficha a ser preenchida antes de importar qualquer fonte própria (será aplicada no Módulo 6):

"""
Fonte: [título]
Origem e autoria: [quem publicou]
Contém dados pessoais? [não | sim — quais]
Contém informação sob sigilo? [não | sim — qual]
Classificação: [verde | amarelo | vermelho]
Conta adequada: [pessoal | institucional | nenhuma]
Compartilhamento previsto: [nenhum | Leitor | Editor] com [quem]
Decisão: [importar | importar após minimização | não importar]
"""

### Pílula Hands-on — Análise de cenários (4 min)

**Questão.** Qual dos cenários a seguir representa uso adequado do NotebookLM?

a) Uma professora importa, em sua conta Gmail pessoal, a planilha com nomes e notas da turma para
gerar devolutivas individuais.
b) Um advogado importa, em conta pessoal, a petição inicial de um cliente para obter um resumo dos
argumentos.
c) Uma estudante importa a LGPD, publicada no portal do Planalto, e um artigo científico de acesso
aberto para preparar-se para uma prova.
d) Um jornalista compartilha com um colega, em "visualização da conversa", um notebook com
documentos de uma fonte sigilosa, supondo que os documentos ficam ocultos.

**Gabarito:** c. **Fundamentação:** (a) dados pessoais de alunos em conta pessoal, sem minimização —
nível vermelho; (b) documento sob sigilo profissional em conta pessoal — nível vermelho;
(c) material público e oficial — nível verde; (d) a visualização da conversa não revoga o acesso às
fontes subjacentes.

## Descrição

- **Objetivos da Aula:** apresentar o tratamento de dados em conta pessoal e institucional, o risco
  do feedback, os princípios de finalidade e minimização da LGPD, o sigilo profissional, os papéis de
  compartilhamento e a classificação verde/amarelo/vermelho.
- **Habilidades Esperadas:** o participante decide, antes de qualquer upload, se uma fonte pode ser
  importada, em qual conta e com qual compartilhamento, e justifica a decisão.

---

## Módulo 3 — Fontes: tipos, limites e montagem do notebook

> Pré-requisito: Módulo 2. Com os critérios de segurança definidos, o foco desloca-se para a montagem do corpus.

### 3.1 Demonstração técnica — tipos de fonte, limites e importação

- **📸 Sugestão de Prints:** (1) tela inicial com "Criar novo notebook" destacado; (2) janela de
  importação aberta após "Fazer upload de uma fonte", com as opções de origem visíveis (arquivo,
  Google Drive, link/site, YouTube, texto colado) e a opção de arquivo destacada; (3) painel Fontes
  com quatro fontes listadas e as caixas de seleção marcadas; (4) fonte do Google Drive com o aviso
  "Clique para sincronizar com o Google Drive" destacado.

A montagem de um notebook inicia-se em `notebook.google.com > Criar novo notebook` (*Create new
notebook*). A ferramenta abre, em seguida, a janela de importação, acessível também pelo painel
Fontes, por meio da opção "Fazer upload de uma fonte" (*Upload a source*). Nela, escolhe-se a origem
do material: arquivo do computador, Google Drive, link de site, vídeo do YouTube, áudio, texto colado
ou uma opção de pesquisa. Concluída a importação, a fonte aparece no painel Fontes, acompanhada de uma
caixa de seleção.

São aceitos, na versão web: PDF, DOCX, TXT, Markdown, CSV, PPTX, ePub, imagens, arquivos de áudio
(transcritos automaticamente), Google Docs, Google Slides, Google Sheets, URLs da web, vídeos públicos
do YouTube com legenda, texto colado e conversas do Gemini. Os limites, segundo a ajuda oficial
consultada em 17/10/2026, são os seguintes:

| Limite | Valor |
|---|---|
| Tamanho de cada fonte | até 500.000 palavras |
| Arquivo enviado do computador | até 200 MB |
| Google Slides | até 100 slides |
| Google Sheets | até 100.000 tokens |
| Fontes por notebook (plano gratuito) | 50 |

Cada tipo de fonte comporta particularidades que convém conhecer antes do uso. A importação de uma
**URL comum** traz apenas o texto HTML daquela página — sem imagens, vídeos incorporados ou páginas
vinculadas — e não alcança conteúdo atrás de *paywall* (bloqueio de assinatura); uma URL que aponta
diretamente para um PDF é tratada como PDF. Do **YouTube**, importa-se somente a transcrição de vídeos
públicos com legenda; vídeos publicados há menos de 72 horas podem falhar. Um **PDF digitalizado** como
imagem, sem texto selecionável, tende a produzir pouco ou nenhum conteúdo útil, exigindo **OCR**
(reconhecimento óptico de caracteres, isto é, a conversão da fotografia de uma página em letras
selecionáveis) por ferramenta autorizada. Arquivos do **Google Drive** são cópias atualizadas
periodicamente e ao abrir o notebook, com comando manual de sincronização; comentários e notas de
rodapé não são importados.

Distingue-se, ainda, a fonte enviada da fonte sugerida. A ferramenta oferece uma busca interna
("Pesquisa Rápida", lançada como *Discover Sources*) que recomenda páginas da web ou arquivos do Drive
a partir de uma descrição. Uma recomendação, porém, não é fonte do notebook até ser importada, e sua
autoria, data e qualidade precisam ser avaliadas antes — com a mesma ficha do Módulo 2. A pesquisa
automatizada em larga escala (*Deep Research*) é objeto de curso próprio.

Recomenda-se, por fim, iniciar com um corpus pequeno e coeso, nomear o notebook pelo tema e conferir
cada fonte importada antes de ampliar o conjunto. Para as atividades deste curso, adota-se o
**Caderno LGPD**, composto de quatro fontes públicas e oficiais, de nível verde, comuns aos três
públicos (Anexo A).

### 3.2 Prompt-base (Mão na massa) — conferência do corpus

"""
Liste as fontes deste notebook. Para cada uma, informe: título, tipo de documento,
órgão responsável e, em uma frase, o tema central. Inclua uma citação por fonte.
"""

### Pílula Hands-on — Montagem do Caderno LGPD (6 min)

1. Baixar para o computador os dois PDFs da ANPD indicados no Anexo A e abrir cada um para confirmar
   que se trata do guia (21 e 58 páginas, respectivamente), e não de uma página do portal.
2. Acessar `notebook.google.com > Criar novo notebook`.
3. Na janela de importação, escolher a opção de arquivo do computador e selecionar o primeiro PDF.
4. No painel Fontes, acionar a opção de adicionar fonte **[conferir rótulo]** e importar o segundo PDF.
5. Repetir a operação escolhendo a opção de link/site **[conferir rótulo]** e colar o endereço da LGPD.
6. Repetir com o endereço da página "Titular de Dados".
7. Renomear o notebook para "LGPD — revisão", clicando no título exibido no topo **[conferir]**.
8. Confirmar que as quatro caixas de seleção estão marcadas e enviar, no painel Conversa, o
   prompt-base de conferência do corpus.

**Critério de êxito:** o painel Fontes lista quatro fontes com caixas marcadas; a resposta ao
prompt-base apresenta quatro itens, cada qual com citação que abre a fonte correspondente.

### Solução de Problemas

| Situação | Causa provável | Procedimento |
|---|---|---|
| O "PDF" baixado abre como página da web | O link salvou a página do portal, não o arquivo | Usar o link direto do Anexo A e confirmar o número de páginas |
| O PDF não é importado | Arquivo acima de 200 MB ou de 500.000 palavras, protegido contra cópia ou corrompido | Verificar tamanho e proteção; obter outra versão |
| O PDF é importado, mas as respostas não o citam | PDF digitalizado sem texto selecionável | Aplicar OCR em ferramenta autorizada ou obter versão acessível; conferir números e nomes |
| O site entra incompleto | URL comum importa só o texto HTML da página | Importar separadamente as páginas relevantes |
| O vídeo do YouTube é recusado | Vídeo privado, sem legenda ou com menos de 72 horas | Conferir legenda no player; aguardar; usar transcrição obtida legalmente |
| Fonte do Drive desatualizada | Cópia ainda não sincronizada | Reabrir o notebook e usar "Clique para sincronizar com o Google Drive" |

## Descrição

- **Objetivos da Aula:** apresentar os tipos de fonte aceitos, seus limites, as particularidades de
  sites, YouTube, PDFs digitalizados e Drive, a distinção entre fonte enviada e fonte sugerida e o
  procedimento de montagem do notebook.
- **Habilidades Esperadas:** o participante monta sozinho um notebook com fontes de tipos diferentes,
  confere se cada fonte foi lida corretamente e diagnostica a causa de uma importação malsucedida.

---

## Módulo 4 — Conversa com citações e auditoria das respostas

> Pré-requisito: Módulo 3 (Caderno LGPD montado). O foco desloca-se da montagem para a consulta verificada.

### 4.1 Demonstração técnica — perguntar, selecionar fontes e conferir

- **📸 Sugestão de Prints:** (1) painel Fontes com apenas uma caixa marcada (LGPD) e as demais
  desmarcadas, destacadas por contorno; (2) resposta na Conversa com citação sob o cursor e a caixa
  de trecho visível; (3) fonte aberta após clique na citação, com o trecho realçado; (4) menu de
  configuração do chat aberto, com as opções "Default", "Learning Guide" e "Custom" e o seletor de
  tamanho de resposta; (5) opção de salvar a resposta como nota destacada.

No painel Conversa, a pergunta é redigida em linguagem natural e enviada. A resposta considera
apenas as fontes cujas caixas estão marcadas no painel Fontes. Essa seleção é um instrumento de
precisão: ao desmarcar fontes, delimita-se ainda mais a "consulta" permitida, o que facilita a
identificação da origem de cada afirmação e a comparação entre documentos.

Retomando o fio condutor, este módulo trata de **conferir a consulta**. Recomenda-se abrir ao menos
duas citações de toda resposta que vá orientar uma decisão, uma aula, uma notícia ou uma peça. O
procedimento consiste em posicionar o cursor sobre o número, ler o trecho exibido, clicar para abrir a
fonte no contexto e comparar a frase gerada com o original, classificando a correspondência como
total, parcial ou ausente. Textos muito curtos podem não gerar citações específicas; nesse caso,
convém formular pergunta mais precisa.

A qualidade da resposta depende da estrutura do pedido. Recomenda-se separar etapas: primeiro,
pedir que se extraia o que cada fonte afirma; depois, que se compare; por último, que se proponham
hipóteses — preservando a diferença entre evidência e inferência. Convém também solicitar
expressamente a marcação "não encontrado nas fontes" quando o corpus não sustentar a conclusão, em
vez de admitir o preenchimento de lacunas com conhecimento geral. Quando a ferramenta responde que
não consegue responder, as causas oficiais são pergunta pouco clara, informação ausente das fontes ou
bloqueio de segurança.

O comportamento da conversa pode ser ajustado em `Conversa > Configure Chat` **[conferir rótulo
pt-BR]**: o estilo "Default" (padrão), "Learning Guide" (guia de aprendizagem, que conduz o estudo por
perguntas e pistas) ou "Custom" (personalizado, com objetivo e tom definidos pelo usuário), e o
tamanho da resposta "Default", "Longer" ou "Shorter". Uma resposta útil pode ser salva como **nota**
(*Save to note*), preservando tabelas e citações clicáveis; notas podem, ainda, ser usadas como fonte
e exportadas para o Google Docs — neste caso, sem sincronização de volta.

### 4.2 Prompt-base (Mão na massa) — pergunta comparativa ancorada

"""
Compare dado pessoal, dado pessoal sensível e dado anonimizado. Para cada conceito,
apresente a definição legal, um exemplo e a citação do trecho da lei. Explique para
iniciantes. Se as fontes divergirem, mostre as versões separadamente.
"""

### Pílula Hands-on — Auditoria de citação (6 min)

1. No Caderno LGPD, com as quatro fontes marcadas, enviar o prompt-base acima.
2. Abrir três citações da resposta e preencher a ficha:

"""
Citação nº | Frase gerada | Trecho original | Correspondência (total/parcial/ausente)
"""

3. No painel Fontes, desmarcar todas as fontes exceto a LGPD e reenviar o mesmo prompt.
4. Registrar uma diferença observada entre as duas respostas.
5. Salvar a melhor resposta como nota.

**Critério de êxito:** ficha com três citações conferidas, com ao menos uma classificação
justificada; diferença entre as respostas registrada; nota salva no notebook.

### Solução de Problemas

| Situação | Causa provável | Procedimento |
|---|---|---|
| Resposta errada apesar de fonte correta | Síntese probabilística | Reduzir as fontes marcadas, pedir citação por afirmação, reformular de modo específico |
| "Não consigo responder" | Pergunta vaga, dado ausente ou bloqueio | Indicar fonte, recorte e formato; se o dado não existir, adicionar fonte adequada |
| Citação genérica ou ausente | Trecho muito curto ou pergunta ampla | Fazer pergunta mais precisa ou usar versão da fonte com melhor estrutura textual |
| Configuração do chat não aparece | Uso pelo aplicativo móvel | Usar o navegador no computador |

## Descrição

- **Objetivos da Aula:** apresentar a seleção de fontes, o procedimento de auditoria de citações, a
  estruturação de pedidos ancorados, a configuração do chat e o uso de notas.
- **Habilidades Esperadas:** o participante formula pergunta ancorada, delimita as fontes consultadas
  e classifica, sozinho, se uma frase gerada é sustentada pelo trecho citado.

---

## Módulo 5 — Painel Estúdio: resumo, guia de estudo e Resumo em Áudio

> Pré-requisito: Módulo 4. O foco desloca-se da resposta efêmera para o artefato reutilizável.

### 5.1 Demonstração técnica — artefatos do Estúdio

- **📸 Sugestão de Prints:** (1) painel Estúdio com a lista de artefatos visível (Resumo em Áudio,
  Resumo em Vídeo, Mapa mental, Relatórios, Tabela de dados, Cartões de estudo, Teste, Apresentações,
  Infográficos); (2) Relatórios aberto, com os modelos "Guia de estudo", "Documento de resumo" e
  "Perguntas frequentes" destacados; (3) janela "Personalizar" do Resumo em Áudio com formato, idioma
  "Português (Brasil)" e duração visíveis; (4) player de áudio gerado no Estúdio.

O painel Estúdio transforma as fontes em artefatos persistentes. Segundo a ajuda oficial, estão
disponíveis: Resumos em Áudio, Resumos em Vídeo, Mapas mentais, Relatórios, Tabela de dados, Cartões
de estudo, Testes, Apresentações de slides e Infográficos. Retomando o fio condutor, cumpre lembrar
que **todo artefato é também uma síntese gerada** a partir da "consulta" — e, como tal, falível:
precisa ser revisado contra as fontes antes de ser distribuído.

Os **Relatórios** reúnem documentos estruturados em `Estúdio > Relatórios`, com modelos prontos —
**Documento de resumo** (*briefing*), **Guia de estudo** e **Perguntas frequentes** —, formatos
sugeridos conforme o conteúdo e a opção de descrever um formato próprio. Convém registrar que o termo
"resumo" pode designar tanto uma resposta da conversa quanto este modelo de relatório; neste curso, o
resumo exigido como produto é o Documento de resumo. A "linha do tempo" não figura como botão fixo na
lista atual e deve ser solicitada por relatório personalizado ou por pergunta **[conferir]**.

O **Resumo em Áudio** (*Audio Overview*) é uma narrativa gerada a partir das fontes — não uma leitura
literal delas — e pode conter erros. É configurado em `Estúdio > Resumo em Áudio > Personalizar`, onde
se escolhem o formato — Conversa aprofundada (*Deep Dive*), Resumo (*The Brief*, com um apresentador e
menos de dois minutos), Crítica (*Critique*) ou Debate —, o idioma (português do Brasil compatível
desde abril de 2025), a duração e uma orientação de foco. A duração mais longa (*Longer*) é documentada
apenas para inglês, assim como o modo interativo, em que o ouvinte conversa por voz com os
apresentadores. A geração pode levar alguns minutos; recomenda-se dispará-la e prosseguir com outra
tarefa.

Os **Cartões de estudo** e **Testes** são configurados em quantidade e dificuldade, com instrução
opcional, e permitem acompanhar o progresso; os cartões podem ser exportados em CSV. O **Mapa mental**
apresenta os temas em ramos expansíveis, e a seleção de um nó gera perguntas sobre ele. Os Resumos em
Vídeo nos formatos Explicador e Curto aceitam português; o formato Cinematográfico exige plano Ultra,
idade mínima de 18 anos e inglês, e não integra este curso. No plano gratuito, os limites diários
consultados em 17/10/2026 são de 3 Resumos em Áudio, 3 Resumos em Vídeo e 10 unidades de relatórios,
cartões, testes e mapas mentais.

### 5.2 Prompt-base (Mão na massa) — orientação do áudio e do guia

"""
Produza um resumo curto em português do Brasil para iniciantes. Enfatize os direitos
do titular de dados e as diferenças entre dado pessoal, sensível e anonimizado.
Não apresente aconselhamento jurídico.
"""

### Pílula Hands-on — Produção dos artefatos de estudo (6 min)

1. No Caderno LGPD, abrir `Estúdio > Resumo em Áudio > Personalizar`.
2. Escolher o formato Resumo (*The Brief*), idioma Português (Brasil) e colar o prompt-base no campo
   de orientação; acionar "Gerar".
3. Enquanto o áudio é gerado, abrir `Estúdio > Relatórios > Guia de estudo` e gerar o guia.
4. Abrir `Estúdio > Relatórios > Documento de resumo` e gerar o documento.
5. Conferir, no guia de estudo, uma afirmação contra a fonte citada.
6. Reproduzir os primeiros trinta segundos do áudio.

**Critério de êxito:** o Estúdio exibe o guia de estudo, o documento de resumo e o player do Resumo
em Áudio, que reproduz em português; uma afirmação do guia foi conferida na fonte.

### Solução de Problemas

| Situação | Causa provável | Procedimento |
|---|---|---|
| O áudio demora ou apresenta erro | Geração assíncrona; demanda; cota | Aguardar; reduzir a orientação; tentar novamente mais tarde; usar "Gerar mais tarde", se oferecido **[conferir]** |
| Limite atingido | Cota diária (3 áudios no gratuito) ou de consumo computacional | Aguardar a renovação indicada na conta; não regenerar sem necessidade |
| O áudio saiu em inglês | Idioma não selecionado em Personalizar | Gerar novamente com Português (Brasil) |
| Não se encontra "Guia de estudo" | Ele está dentro de Relatórios | `Estúdio > Relatórios > Guia de estudo` |
| Opção "Cinematic" indisponível | Recurso Ultra, 18+, inglês | Usar Explicador ou Curto; não é exigido no curso |

## Descrição

- **Objetivos da Aula:** apresentar os artefatos do Estúdio, a localização dos modelos de relatório, a
  configuração do Resumo em Áudio, os recursos de estudo (cartões, testes, mapa mental) e os limites do
  plano gratuito.
- **Habilidades Esperadas:** o participante gera, sozinho, documento de resumo, guia de estudo e Resumo
  em Áudio em português a partir de um notebook, e revisa ao menos uma afirmação de um artefato contra
  a fonte.

---

## Módulo 6 — Síntese e Aplicação Integrada

> Pré-requisito: Módulos 0 a 5. O foco desloca-se da operação para a decisão de uso e a aplicação ao perfil profissional.

### 6.1 Discussão orientada — quando usar o NotebookLM

- **📸 Sugestão de Prints:** não se aplica (discussão de cenários).

O percurso do curso compõe um fluxo de cinco etapas: **decidir** o que pode ser consultado (Módulo 2),
**reunir** o corpus (Módulo 3), **perguntar** de forma ancorada (Módulo 4), **conferir** as citações
(Módulo 4) e **produzir** artefatos revisados (Módulo 5). A escolha da ferramenta depende da etapa em
que se encontra o problema.

| Situação | Ferramenta recomendada | Fundamento |
|---|---|---|
| A evidência deve vir de material já selecionado | NotebookLM | Ancoragem e citação ao trecho |
| O primeiro problema é descobrir páginas atuais na web | Buscador com IA (ex.: Perplexity) | Orientado à web com citações |
| Pesquisa ampla e automatizada em muitas páginas | Deep Research | Curso *Deep Research - Hands On* |
| Produção geral persistente além de um corpus | Projetos de assistentes gerais | Curso *RAG e Bases de Conhecimento - Essentials* |

Cenários para reflexão: (a) um estudante que precisa de um panorama inicial de um tema ainda sem
bibliografia; (b) uma professora que dispõe do plano de ensino e de três textos e precisa de um guia
para a turma; (c) um advogado que precisa organizar legislação e decisões públicas já reunidas;
(d) uma jornalista que precisa reconstruir a cronologia a partir de comunicados oficiais. Observa-se
que (b), (c) e (d) partem de corpus definido — terreno do notebook —, ao passo que (a) começa pela
descoberta de fontes.

### 6.2 Prompt-base (Mão na massa) — recorte por perfil

"""
[Estudante] Atue como guia de aprendizagem: faça uma pergunta por vez sobre os direitos
do titular, espere a resposta, dê uma pista antes do gabarito e cite o trecho.

[Educador] Com base apenas nas fontes selecionadas, crie um guia de uma página para
[nível de ensino], com pré-requisitos, ideias essenciais, três equívocos comuns e
perguntas de recuperação. Cite cada item.

[Direito] Monte um quadro com artigo, obrigação, exemplo e evidência citada. Não
ofereça aconselhamento jurídico e marque o que não estiver nas fontes.

[Jornalismo/Análise] Extraia órgãos, datas, obrigações e alegações. Separe fato
documentado de inferência e mostre a citação de cada linha.
"""

### Pílula Hands-on — Atividade integradora (6 min)

1. No Caderno LGPD, escolher o perfil e enviar o prompt-base correspondente.
2. Auditar duas citações da resposta com a ficha do Módulo 4.
3. Gerar no Estúdio um artefato adequado ao perfil (cartões ou teste, para estudante; relatório
   personalizado, para educador; relatório ou tabela de dados, para Direito e jornalismo).
4. Preencher a ficha de decisão do Módulo 2 para o compartilhamento do notebook (com quem, em que
   papel, ou decisão de não compartilhar).

**Extensão opcional (fora da carga horária):** repetir o fluxo com um tema próprio, usando três fontes
de nível verde avaliadas pela ficha de decisão.

### Critérios de avaliação

| Critério | Atendido? |
|---|---|
| O Caderno LGPD contém as quatro fontes | |
| Foi feita ao menos uma pergunta ancorada com citações auditadas na ficha | |
| O documento de resumo e o guia de estudo foram gerados e uma afirmação foi conferida | |
| O Resumo em Áudio foi gerado em português | |
| O artefato do perfil foi gerado | |
| A decisão de compartilhamento foi registrada com justificativa | |

## Descrição

- **Objetivos da Aula:** articular as etapas decidir–reunir–perguntar–conferir–produzir, situar o
  NotebookLM entre ferramentas vizinhas e aplicar o fluxo ao perfil profissional.
- **Habilidades Esperadas:** o participante decide quando usar o NotebookLM e conduz, sem roteiro, o
  fluxo completo em um notebook, entregando artefatos revisados e decisão de compartilhamento
  justificada.

---

## Encerramento

O curso cumpriu a finalidade de habilitar o participante a estudar e sintetizar fontes próprias com o
NotebookLM, distinguindo a resposta ancorada da resposta verdadeira e tratando a citação como ponto de
partida da conferência. Recomenda-se a prática regular — um notebook por tema ou por decisão, com
corpus pequeno e conferido — e a revisão periódica dos limites e rótulos da ferramenta, que mudaram
diversas vezes em 2026.

Como caminhos de aprofundamento, indicam-se, nas trilhas do IAClube, *Deep Research - Hands On* (pesquisa
ampla automatizada), *Checagem de Fontes e Citações - Essentials* (verificação acadêmica sistemática),
*Educação com IA: Planejamento e Avaliação - Essentials* e *Pesquisa jurídica com IA - Hands On*.

> **Síntese:** a inteligência artificial ajuda a estudar melhor quando trabalha sobre as fontes certas
> — e quem responde pela resposta é quem confere a citação.

---

## Anexo A — Kit de fontes do Caderno LGPD

Quatro fontes públicas, gratuitas, oficiais e em português, de nível verde.

| # | Fonte | Tipo | Endereço |
|---|---|---|---|
| 1 | Lei nº 13.709/2018 — LGPD, texto compilado (Planalto) | HTML (link) | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm |
| 2 | Guia Orientativo sobre Segurança da Informação para Agentes de Tratamento de Pequeno Porte (ANPD, v1.0, out. 2021, 21 p.) | PDF (baixar) | https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-vf.pdf/@@download/file |
| 3 | Tratamento de dados pessoais para fins acadêmicos — Guia orientativo (ANPD, v1.0, 58 p.) | PDF (baixar) | https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/web-guia-anpd-tratamento-de-dados-para-fins-academicos.pdf/@@display-file/file |
| 4 | Titular de Dados (ANPD) | HTML (link) | https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados |

Cópias de referência dos PDFs 2 e 3 estão em `conteudo-bruto/notebooklm-essentials/`. Os links devem
ser testados na semana de publicação: o endereço do PDF 2 sem o sufixo `@@download/file` devolve a
página do portal, e não o arquivo.

## Anexo B — Rastreabilidade da auditoria

| Achado | Destino neste roteiro |
|---|---|
| E1 Segurança antes do upload | Módulo 2, inteiro, antes do Módulo 3 |
| E2 Pré-filtro de acesso | Módulo 0 |
| E3 Corpus indefinido | Caderno LGPD (Anexo A), usado dos Módulos 3 a 6 |
| E4 Citação aceita como prova | Ficha de auditoria (Módulo 4); Questão 1 do Módulo 1 |
| E5 Caminho de menu incorreto | `Estúdio > Relatórios > Guia de estudo` (Módulo 5) |
| E6 Marca em transição | Módulo 0 e Módulo 1, navegação por `notebook.google.com` |
| E7 Limitações de fonte | Tabela e Solução de Problemas do Módulo 3 |
| E8 Seleção de fontes | Módulo 4, passo 3 da pílula |
| E9 Áudio sem parâmetros | Módulo 5 (Personalizar, formatos, geração assíncrona) |
| E10 "Resumo" ambíguo | Módulo 1 (resposta × artefato) e Módulo 5 (Documento de resumo) |
| E11 Fio condutor | Prova com consulta: Módulos 1, 2, 4 e 5 |
| E12 Exemplos por público | Módulo 1 (último parágrafo), Módulo 2 (cenários), Módulo 6 (perfis) |
| E13 Diferenciais | Configure Chat, notas (Módulo 4); cartões, testes, mapa (Módulo 5) |
| E14 Fronteira com outras ferramentas | Módulo 6.1 |
| E15 Carga horária | 129 min apurados pela MET |
| E16 Textos curtos | Textos com 4–5 parágrafos |
| E17 Cotas sem data | Datadas em 17/10/2026 (Módulos 0, 3 e 5) |
| Decisão consciente | Tabela de dados, Apresentações e Infográficos apenas citados; prática fica para curso seguinte, para não estourar a carga horária |
