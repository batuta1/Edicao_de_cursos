# Roteiro Final — ChatGPT no Word (Essentials)

**Público-Alvo:** professores universitários, de qualquer área, inteiramente novatos no uso de
inteligência artificial generativa para trabalho de escrita.

**Objetivo Geral:** habilitar o docente do ensino superior a empregar o ChatGPT como assistente de
redação na produção de documentos do Microsoft Word, compreendendo os caminhos de integração
disponíveis, os critérios de formulação de instruções eficazes, o tratamento dado aos dados
enviados e os limites de confiabilidade da ferramenta. Ao término, espera-se que o participante
disponha de um repertório verificável de procedimentos aplicáveis à sua rotina de escrita acadêmica
e administrativa.

**Pré-requisitos:** uso básico do Microsoft Word (abrir, digitar, salvar, aplicar estilo de título);
conta ativa no ChatGPT, ainda que no plano gratuito; nenhum conhecimento prévio de inteligência
artificial.

**Carga horária:** 129 minutos (detalhamento em `../ementa completa/carga-horaria-essentials.md`).

---

## Estrutura do Curso

| Nível | Módulos | Finalidade |
|---|---|---|
| Nível 0 — Preparação | Módulo 0 | Verificar acesso, entender o tratamento dos dados e decidir sobre autoria antes de qualquer uso |
| Nível 1 — Fundamentos | Módulos 1 e 2 | Compreender os caminhos disponíveis e aprender a formular instruções |
| Nível 2 — Aplicação | Módulos 3 e 4 | Aplicar as operações de escrita e converter tarefas repetidas em modelos |
| Nível 3 — Integração | Módulo 5 | Articular as competências em atividade única |

**Anexos:** não há anexos. Os assuntos deslocados para fora do curso constam do Roadmap de Expansão
em `../ementa completa/02-analise-essentials.md`.

> **Fio condutor do curso.** O conceito plantado no Módulo 0 — *o sistema produz o texto mais
> plausível, não o mais verdadeiro* — é retomado nominalmente no Módulo 3, quando se trata de
> revisão, e no Módulo 5, quando se trata da responsabilidade sobre o documento assinado.

> **Nota sobre a auditoria.** Todos os doze gargalos da matriz de soluções de
> `../ementa completa/02-analise-essentials.md` foram endereçados neste roteiro. Duas decisões
> declaradas: (a) o troubleshooting de formatação foi alocado ao Módulo 3, e não ao Módulo 4, porque
> foi para lá que o conteúdo de resumo e estruturação migrou; (b) suplementos de terceiros para o
> Word aparecem uma vez, no Módulo 1, como categoria com critério de avaliação, e não como
> recomendação — conforme decidido no Roadmap de Expansão.

---

# Módulo 0 — Antes de colar qualquer coisa

> Ponto de partida do curso. Nenhum módulo posterior deve ser iniciado sem que as verificações deste
> módulo estejam concluídas.

## Descrição

- **Objetivos da Aula:** apresentar a natureza do sistema e sua consequência para o trabalho
  acadêmico; expor o tratamento dado aos dados enviados em cada plano do ChatGPT; nomear as decisões
  de autoria que antecedem o uso; e conduzir a verificação de acesso e a criação da cópia de
  trabalho.
- **Habilidades Esperadas:** ao final, o participante identifica sozinho o próprio plano e o que ele
  faz com o texto enviado, sabe onde desativar o uso do conteúdo para treinamento, reconhece o que
  não deve ser inserido no sistema, e mantém o hábito de trabalhar sobre cópia.

### O que o sistema é, e o que decorre disso

- **📸 Sugestão de Prints:** tela inicial do ChatGPT no navegador, com o campo de mensagem vazio em
  destaque e o seletor de modelo visível no topo. A captura deve mostrar a interface limpa, antes de
  qualquer conversa, para o participante reconhecer o ponto de partida.

Convém iniciar por uma definição operacional. Um modelo de linguagem é um sistema computacional
treinado para prever, a partir de um texto recebido, qual continuação é mais provável. Dessa
descrição decorre a consequência mais importante para o trabalho acadêmico: **o sistema produz o
texto mais plausível, e não necessariamente o mais verdadeiro**. A plausibilidade é uma propriedade
da forma; a verdade é uma propriedade do conteúdo. O ChatGPT é excelente na primeira e não oferece
garantia sobre a segunda.

Essa formulação não é um alerta isolado. É a premissa da qual decorrem, por dedução, todas as
cautelas apresentadas no restante do curso: por que se confere cada número, por que não se aceita
referência bibliográfica sem conferência, por que a responsabilidade permanece com quem assina.

### O que acontece com o texto enviado

- **📸 Sugestão de Prints:** tela de configurações do ChatGPT com a seção de controles de dados
  aberta, destacando a opção de uso do conteúdo para melhoria dos modelos e o estado do seletor.

Cumpre registrar que o conteúdo inserido no sistema sai do computador do participante e é processado
em servidores de terceiros. O tratamento posterior varia conforme o plano contratado.

| Plano | Conteúdo usado para aperfeiçoar os modelos? |
|---|---|
| Plus e Pro | Sim, por padrão, salvo desativação pelo participante nos controles de dados |
| Business, Enterprise e Edu | Não, por padrão |

Quanto à retenção, as conversas permanecem na conta até serem excluídas; após a exclusão da conversa
ou da conta, os dados são apagados dos sistemas em até trinta dias, ressalvadas as hipóteses de
retenção por obrigação legal ou de segurança.

> ⚠️ **Informação sujeita a alteração.** Planos, políticas de retenção e controles de dados mudam
> com frequência. Recomenda-se conferir a situação vigente na própria conta antes de tomar decisão
> institucional com base nesta tabela.

Decorre daí a lista do que **não** deve ser inserido no sistema, qualquer que seja o plano: dado
identificável de aluno (nome associado a nota, frequência, ocorrência disciplinar ou condição de
saúde); resultado de pesquisa ainda não publicado; parecer sigiloso de avaliação por pares; conteúdo
submetido a acordo de confidencialidade; e dado pessoal de terceiros obtido em contexto de pesquisa.

### Autoria e uso declarado

Antes de o participante utilizar a ferramenta em documento institucional, três perguntas precisam de
resposta. Elas não são respondidas por este curso, porque a resposta é institucional e varia:

1. O que a norma da própria instituição estabelece sobre o uso de sistemas de inteligência
   artificial na produção de documentos acadêmicos e administrativos?
2. O uso precisa ser declarado no documento? Em que forma — nota de rodapé, seção de métodos,
   declaração de autoria?
3. Que orientação será dada aos alunos, uma vez que a mesma ferramenta lhes está disponível?

Recomenda-se que o participante consulte a norma vigente em sua instituição antes de prosseguir. Na
ausência de norma, convém adotar o critério mais conservador disponível na área.

### Verificação inicial

- **📸 Sugestão de Prints:** janela do explorador de arquivos mostrando dois arquivos lado a lado —
  o documento original e a cópia com sufixo `-copia-curso` — para o participante confirmar que a
  duplicação ocorreu.

Quatro verificações antecedem o Módulo 1.

1. **Acesso.** Abrir `chatgpt.com` no navegador e confirmar que a conta está conectada.
2. **Plano.** Identificar o plano em uso no menu de perfil da conta e localizar a linha
   correspondente na tabela acima.
3. **Controles de dados.** Nos planos Plus e Pro, localizar os controles de dados e decidir se o uso
   do conteúdo para aperfeiçoamento dos modelos permanecerá ativo.
4. **Cópia de trabalho.** No Word, abrir o documento que será usado nos exercícios,
   `Arquivo > Salvar como`, acrescentar o sufixo `-copia-curso` ao nome, salvar e fechar o original.

### Exercício Prático

**Verificação de prontidão (7 min)**

Execute as quatro verificações acima e registre o resultado.

**Critério de êxito:** o participante consegue afirmar, sem consultar o material, (a) qual é o seu
plano, (b) se o conteúdo enviado é usado para aperfeiçoar os modelos nesse plano, (c) três itens que
não deve inserir no sistema, e (d) o nome do arquivo de cópia criado, visível na pasta ao lado do
original.

### Solução de Problemas — Acesso

| Situação | Procedimento |
|---|---|
| A conta não conecta | Verificar se o acesso está sendo feito com o endereço institucional ou pessoal; são contas distintas, com planos distintos. |
| O plano não aparece no menu de perfil | Em contas institucionais, o plano pode ser definido pelo espaço de trabalho e não ser exibido ao membro. Consultar quem administra o espaço. |
| Os controles de dados não estão disponíveis | Ocorre em planos administrados institucionalmente, em que a configuração é definida centralmente. Não é falha. |
| O comando `Salvar como` não aparece no Word na web | No Word na web, o caminho equivalente é `Arquivo > Salvar uma cópia`. |

---

# Módulo 1 — O que o ChatGPT faz com um documento do Word

> Pressupõe as verificações do Módulo 0 e desloca o foco da preparação para os caminhos concretos de
> trabalho com o documento.

## Descrição

- **Objetivos da Aula:** apresentar os três caminhos de uso do ChatGPT com documentos do Word;
  esclarecer a inexistência de suplemento oficial da OpenAI para o Word; expor os limites concretos
  de envio de arquivos; e declarar o que não sobrevive ao envio.
- **Habilidades Esperadas:** ao final, o participante seleciona sozinho o caminho adequado a uma
  tarefa concreta, estima se um arquivo cabe nos limites de envio, e sabe que a conversa de revisão
  do documento não é vista pelo sistema.

### Os três caminhos

- **📸 Sugestão de Prints:** janela do ChatGPT com o ícone de anexo do campo de mensagem em
  destaque, e o seletor de arquivos aberto mostrando um arquivo `.docx` selecionado.

Cumpre registrar, antes dos caminhos, um ponto que costuma gerar frustração. **Não existe suplemento
oficial da OpenAI para o Microsoft Word.** Existe suplemento oficial para o Excel e para o
PowerPoint; para o Word, não. O participante que procurar uma barra lateral do ChatGPT dentro do
Word, semelhante à do Microsoft Copilot, não a encontrará. Disso não decorre que a ferramenta seja
inútil para quem escreve no Word — decorre apenas que o trabalho se dá por outros caminhos.

| Caminho | Como funciona | Quando convém | Limitação principal |
|---|---|---|---|
| **Copiar e colar** | O texto é levado ao navegador e o resultado é trazido de volta ao documento | Trechos, parágrafos, seções; qualquer versão do Word; qualquer plano | Trabalhoso em documentos longos; a formatação não acompanha |
| **Envio do arquivo** | O `.docx` é anexado à conversa e lido pelo sistema | Compreender, resumir, extrair informação do documento inteiro | O sistema lê o texto extraído; não devolve o arquivo formatado |
| **Solicitação de arquivo pronto** | O sistema gera um `.docx` para download | Documento novo, produzido a partir de instruções ou de material anexado | Não herda os estilos de um documento existente; disponibilidade varia por plano |

Existe ainda uma quarta possibilidade, mencionada aqui uma única vez: suplementos de terceiros
disponíveis na loja de suplementos do Office. Eles reduzem o vaivém entre janelas, mas apresentam
três limitações que o docente deve pesar antes de adotar qualquer um — costumam ver apenas o texto
selecionado, e não o documento inteiro; devolvem texto simples, o que pode descartar formatação de
caractere; e não propõem as alterações na forma de alterações controladas, de modo que não há
comparação a revisar. Acresce que a instalação frequentemente depende de autorização institucional.
O curso não recomenda nenhum suplemento nominalmente; oferece o critério.

### Limites de envio

- **📸 Sugestão de Prints:** mensagem de erro exibida pelo ChatGPT ao atingir limite de envio de
  arquivos, com o texto do aviso legível.

| Limite | Valor |
|---|---|
| Tamanho máximo por arquivo | 512 MB |
| Extensão máxima de arquivo de texto | 2 milhões de tokens |
| Envios por janela móvel | Até 80 arquivos a cada 3 horas |
| Envios diários no plano gratuito | 3 |
| Arquivos por projeto — Plus | Até 20 |
| Arquivos por projeto — Pro, Team, Education e Business | Até 40 |
| Armazenamento por usuário | 25 GB |

> 📌 **Observação.** Um documento do Word em texto corrido dificilmente se aproxima desses limites.
> O limite que efetivamente restringe o participante do plano gratuito é o de três envios por dia.

### O que não sobrevive ao envio

Observa-se uma limitação relevante e pouco conhecida: o que é lido pelo sistema é o **texto extraído**
do documento. Comentários de margem e marcas de alterações controladas não acompanham o envio. Em
outras palavras, a conversa de revisão que ocorre dentro do documento — as observações do
coorientador, as objeções do parecerista, o histórico do que foi alterado — permanece invisível ao
sistema.

Convém, quando essa conversa importa, adotar um dos dois procedimentos: copiar manualmente o texto
dos comentários relevantes para a conversa, junto com o trecho a que se referem; ou trabalhar por
trecho, pelo caminho de copiar e colar, tratando cada observação separadamente.

Registre-se ainda que, nos planos que não sejam Enterprise, a leitura de arquivos é baseada em
texto: imagens incorporadas ao documento são descartadas. Um documento cujo argumento esteja em
gráficos e figuras será lido de forma incompleta.

### Exercício Prático — Pílula Hands-on

**Envio e reconhecimento de um documento (6 min)**

1. Anexe à conversa a cópia de trabalho criada no Módulo 0.
2. Solicite: *"Descreva a estrutura deste documento: quais são as seções e o que cada uma trata, em
   uma frase por seção. Não resuma o conteúdo."*
3. Compare a resposta com o documento aberto no Word.
4. Verifique se algum comentário de margem existente no documento foi mencionado.

**Critério de êxito:** o participante confirma que a estrutura descrita corresponde à do documento e
constata que nenhum comentário de margem foi mencionado, ainda que existam no arquivo.

### Solução de Problemas — Envio de arquivo

| Situação | Procedimento |
|---|---|
| "Limite de upload atingido" sem envios recentes | Confirmar que se está na conta e no plano corretos. Tentativas de envio que falharam também contam para o limite. |
| O arquivo não é aceito | Conferir a extensão. Documentos em formatos antigos podem precisar ser salvos como `.docx` em `Arquivo > Salvar como`. |
| O sistema não menciona um trecho que existe no documento | Verificar se o trecho está em imagem, caixa de texto ou tabela complexa. A leitura é do texto extraído. |
| O documento é longo demais | Trabalhar por seção, pelo caminho de copiar e colar. |

---

# Módulo 2 — A anatomia de uma boa instrução

> Pressupõe o Módulo 1 e desloca o foco do que a ferramenta faz para como se formula o pedido.

## Descrição

- **Objetivos da Aula:** apresentar os quatro elementos que compõem uma instrução eficaz; introduzir
  a restrição de preservação; e demonstrar o efeito da solicitação de plano prévio em alterações
  extensas.
- **Habilidades Esperadas:** ao final, o participante converte sozinho uma instrução vaga em uma
  instrução específica contendo tarefa, público, extensão, registro e ao menos uma restrição de
  preservação.

### Os quatro elementos

- **📸 Sugestão de Prints:** duas conversas do ChatGPT lado a lado, à esquerda a instrução vaga
  ("melhore este parágrafo") com sua resposta, à direita a instrução específica com a sua. O
  contraste entre as duas respostas deve ser legível na captura.

Denomina-se instrução — ou, no jargão corrente, *prompt* — o texto que o usuário fornece ao sistema
descrevendo o que deseja. Observa-se uma correspondência direta: a instrução vaga produz o texto
genérico; a instrução específica produz o texto utilizável.

Quatro elementos costumam ser suficientes:

| Elemento | Pergunta que responde | Exemplo |
|---|---|---|
| **Tarefa** | Que operação se pretende? | redigir, reescrever, resumir, estruturar, revisar |
| **Público** | Para quem o texto se destina? | alunos de primeiro período; colegiado; agência de fomento |
| **Extensão** | Qual o tamanho? | 120 palavras; 5 itens; 2 parágrafos |
| **Registro** | Em que tom? | formal e impessoal; acessível, sem jargão de área |

O quinto elemento, não obrigatório mas decisivo, é a **restrição de preservação**: a declaração
explícita do que não deve mudar. Em uma reescrita, convém declarar que a terminologia técnica deve
ser preservada, que as citações não devem ser alteradas e que a ordem dos argumentos deve permanecer.
A ausência dessa declaração autoriza o sistema a reorganizar o texto de maneiras que o autor não
pretendia.

### O plano antes da execução

Para alterações extensas, recomenda-se solicitar um plano antes da execução. A formulação *"antes de
reescrever, descreva o que pretende alterar e por quê"* transfere ao docente a decisão sobre o
escopo, evitando que o sistema produza uma versão inteira em direção equivocada. O procedimento
custa uma troca de mensagens e economiza a leitura de um texto que seria descartado.

### Exemplo Aplicado

Instrução vaga:

"""
Melhore este parágrafo.
"""

A mesma instrução com os cinco elementos:

"""
Reescreva o parágrafo abaixo para a introdução de um plano de ensino destinado a alunos de primeiro
período. O texto deve ser acessível, sem jargão de área, com no máximo cento e vinte palavras.
Preserve os nomes das disciplinas, a ordem dos tópicos e todos os números.

[colar o parágrafo]
"""

### Exercício Prático — Pílula Hands-on

**Conversão de instrução (6 min)**

1. Escolha um parágrafo da sua cópia de trabalho.
2. Envie a instrução vaga "melhore este parágrafo" seguida do texto. Leia o resultado.
3. Reescreva a instrução com os cinco elementos e envie novamente o mesmo parágrafo.
4. Compare as duas respostas.

**Critério de êxito:** a segunda instrução contém os quatro elementos obrigatórios e ao menos uma
restrição de preservação, e o participante consegue apontar uma diferença concreta entre as duas
respostas — extensão, tom ou preservação de termo.

---

# Módulo 3 — As quatro operações da escrita

> Pressupõe o Módulo 2 e desloca o foco da formulação da instrução para a sua aplicação nas
> operações mais frequentes da escrita acadêmica.

## Descrição

- **Objetivos da Aula:** apresentar as quatro operações — redigir, reescrever, resumir, estruturar —
  e o critério de emprego de cada uma; expor o comportamento do sistema na revisão e o que ela não
  alcança; e demonstrar o tratamento da formatação na passagem para o Word.
- **Habilidades Esperadas:** ao final, o participante executa sozinho as quatro operações sobre
  texto próprio, obtém resultado sem símbolos de formatação estranhos ao Word, e verifica dados
  factuais antes de incorporar qualquer trecho ao documento.

### As quatro operações

- **📸 Sugestão de Prints:** documento do Word com um parágrafo selecionado e o menu
  `Página Inicial > Colar` aberto, mostrando as opções de colagem, com "Manter somente texto" ou
  "Colar Especial" em destaque.

| Operação | O que faz | Quando convém | Cuidado principal |
|---|---|---|---|
| **Redigir** | Produz uma versão inicial a partir de descrição | Vencer a página em branco | O resultado é matéria bruta, não produto |
| **Reescrever** | Reformula um trecho segundo critério declarado | O parágrafo que não funciona | Números e citações trocam de lugar |
| **Resumir** | Reduz preservando o essencial | Sínteses, resumos executivos, ementas | Especificar o formato; o padrão tende à lista |
| **Estruturar** | Propõe seções antes da escrita | Documento ainda não escrito | Ponto de partida, não arquitetura definitiva |

Quanto à reescrita, cumpre destacar o procedimento que mais eleva a qualidade do resultado: caso a
primeira reformulação não sirva, recomenda-se **declarar o que está errado nela**, em vez de
solicitar genericamente outra versão. A instrução "está longo demais e perdeu o termo técnico X"
produz resultado superior à instrução "tente de novo". O participante exerce, aqui, o papel de
editor — papel que já lhe é familiar.

Observa-se, quanto ao registro, que o sistema tende a um tom neutro e vagamente corporativo, que
destoa da voz de um docente experiente. Recomenda-se fornecer ao sistema um parágrafo do próprio
autor como referência de estilo, ou ajustar o resultado antes de qualquer uso externo.

### A revisão e o seu limite

A operação de revisão exige a cautela mais explícita. O sistema identifica com facilidade construções
obscuras, períodos excessivamente longos, repetição de ideias e inconsistência de terminologia. Não
identifica erro factual do próprio autor, e **pode introduzir erro factual novo**.

Retoma-se aqui o conceito plantado no Módulo 0: o sistema produz o texto mais plausível, não o mais
verdadeiro. Uma referência bibliográfica inventada é perfeitamente plausível — tem autor verossímil,
título verossímil, ano verossímil e periódico verossímil. É por isso que ela passa despercebida, e é
por isso que toda referência precisa ser conferida na fonte. O mesmo vale para número, data, menção a
legislação e citação direta.

Depreende-se que o sistema é auxiliar de forma, não fiador de conteúdo.

### Exercício Prático — Pílula Hands-on

**Resumo com formato determinado (6 min)**

1. Selecione uma seção da sua cópia de trabalho, com ao menos duas páginas.
2. Solicite: *"Resuma o texto abaixo em exatamente cinco itens, cada um com no máximo vinte palavras.
   Texto puro, sem símbolos de formatação. Preserve todos os números exatamente como estão."*
3. Cole o resultado no Word.
4. Confira, um a um, se os números do resumo correspondem aos do original.

**Critério de êxito:** o resumo tem cinco itens, respeita o limite de palavras, cola no Word sem
símbolos estranhos, e o participante conferiu ao menos um dado numérico contra o texto original.

### Solução de Problemas — Formatação na passagem para o Word

| Situação | Procedimento |
|---|---|
| O texto cola com fundo cinza e fonte do navegador | Desfazer e colar por `Página Inicial > Colar > Colar Especial > Texto não formatado` (Word de desktop) ou `Página Inicial > Colar > Manter somente texto` (Word na web). |
| O texto vem com `##`, `**` e `-` no meio | Prevenir na instrução: "texto puro, sem símbolos de formatação". Para limpar o que já foi colado, usar `Página Inicial > Localizar e Selecionar > Substituir` (atalho `Ctrl + H`), buscando `##` e substituindo por vazio; repetir para `**`. |
| Os títulos perderam o estilo | Esperado: a formatação não acompanha a colagem. Reaplicar em `Página Inicial > Estilos`. |
| O resumo veio em lista quando se queria parágrafo | Especificar o formato na instrução: "em um único parágrafo corrido, sem lista". |

---

# Módulo 4 — Do documento avulso ao modelo reutilizável

> Pressupõe o Módulo 3 e desloca o foco da tarefa isolada para o trabalho que se repete a cada
> semestre.

## Descrição

- **Objetivos da Aula:** distinguir arquivo de referência de modelo reutilizável; apresentar o
  critério de escolha entre um e outro; e descrever o fluxo de criação e uso de um modelo,
  observadas as condicionantes de plano.
- **Habilidades Esperadas:** ao final, o participante identifica em sua própria rotina ao menos um
  documento que se repete e decide, com critério, se o caso pede arquivo de referência ou modelo.

### Discussão Orientada — quando um, quando outro

- **📸 Sugestão de Prints:** campo de mensagem do ChatGPT com o menu de menções aberto após a
  digitação do símbolo `@`, mostrando a lista de opções disponíveis na conta.

O docente reescreve, a cada semestre, documentos da mesma família: plano de ensino, relatório de
atividades, parecer de projeto, orientação de trabalho, comunicado de disciplina. A estrutura é a
mesma; muda o conteúdo. Há dois recursos para esse caso, e a distinção entre eles é o objeto deste
módulo.

| | **Arquivo de referência** | **Modelo reutilizável** |
|---|---|---|
| O que é | Um documento anexado como exemplo para a tarefa em curso | Um arquivo de exemplo somado a instruções reutilizáveis e ao formato de saída esperado |
| Quando convém | Solicitação pontual | Fluxo que se repete |
| Custo de preparação | Nenhum | Uma configuração inicial |
| Ganho | O resultado segue a estrutura do exemplo | O formato não precisa ser explicado a cada vez |

O critério de decisão é simples: **se o participante fará isso uma vez, use arquivo de referência; se
fará todo semestre, vale criar um modelo.**

Convém, ao empregar um arquivo de referência, declarar explicitamente o que deve ser seguido e o que
deve ser substituído. A formulação *"use os títulos, a estrutura das tabelas e o tom deste plano de
ensino, e substitua o conteúdo pelas anotações da nova disciplina"* é mais eficaz do que anexar o
arquivo e pedir "faça igual a este".

> ⚠️ **Condicionante de disponibilidade.** O fluxo de criação e uso de modelos depende do plano
> contratado, das configurações do espaço de trabalho e da interface utilizada. Recomenda-se
> verificar a disponibilidade na própria conta antes de planejar trabalho em torno do recurso.

### Demonstração Técnica — o fluxo de um modelo

Onde o recurso estiver disponível, o fluxo observa quatro etapas:

1. **Partir de um arquivo existente.** Um documento do Word, uma pasta de trabalho do Excel, uma
   apresentação do PowerPoint ou um link para arquivo do Google Workspace.
2. **Acionar o criador de modelos.** No campo de mensagem, selecionar a opção de criação de modelos
   pelo menu de menções (`@`), anexar o arquivo de referência e descrever o que deve permanecer
   igual, o que deve mudar e que informação será fornecida a cada novo arquivo.
3. **Instalar o modelo**, quando a opção for oferecida ao término da criação.
4. **Usar o modelo.** Selecionar a categoria pretendida pelo menu de menções, escolher o modelo,
   descrever o arquivo desejado e fornecer o material de origem daquela tarefa.

> 📌 **Não esqueça.** A escolha de um modelo não inicia a tarefa automaticamente: ela apenas prepara
> a instrução, que ainda precisa ser enviada.

Cumpre registrar que modelos criados na web e modelos salvos localmente pelo aplicativo de desktop
são conjuntos separados e não se sincronizam entre si. Cumpre registrar, ainda, que modelos criados
são pessoais: disponibilizá-los à equipe exige empacotamento e publicação por quem administra o
espaço de trabalho.

### Exercício Prático

**Identificação do caso adequado (4 min)**

Para cada situação, indicar se o caso pede arquivo de referência (R) ou modelo reutilizável (M):

1. O docente precisa redigir, uma única vez, um parecer sobre um projeto, e quer que ele siga a
   estrutura de um parecer anterior.
2. O docente elabora relatório de atividades no mesmo formato ao fim de cada semestre.
3. O docente precisa converter as anotações de uma reunião em ata, seguindo o formato das atas
   anteriores do colegiado, o que ocorre mensalmente.
4. O docente quer que um comunicado isolado tenha o mesmo tom de um comunicado bem recebido no
   semestre passado.

**Gabarito:** 1 — R; 2 — M; 3 — M; 4 — R.

**Fundamentação:** a frequência é o critério. Situações 2 e 3 se repetem em calendário previsível e
amortizam o custo de configuração; 1 e 4 são pontuais.

---

# Módulo 5 — Síntese e Aplicação Integrada

> Pressupõe todos os módulos anteriores e os articula em uma única atividade de produção.

## Descrição

- **Objetivos da Aula:** apresentar as quatro operações como etapas de um fluxo único, e não como
  procedimentos isolados; e situar a verificação como disposição permanente, não como etapa final.
- **Habilidades Esperadas:** ao final, o participante conduz sozinho um documento curto do
  planejamento ao envio, aplicando as operações em sequência e verificando cada dado factual antes
  de assinar.

### O fluxo completo

- **📸 Sugestão de Prints:** documento do Word finalizado, com painel de navegação aberto à esquerda
  exibindo a hierarquia de títulos, para evidenciar que os estilos foram aplicados.

Cumpre articular o que foi tratado de modo disperso. As quatro operações não são procedimentos
isolados, mas etapas de um mesmo fluxo:

| Etapa | Operação | O que se obtém |
|---|---|---|
| 1 | Estruturar | Proposta de seções, ajustada pelo autor |
| 2 | Redigir | Versão inicial de cada seção |
| 3 | Reescrever | Seções fracas reformuladas com critério declarado |
| 4 | Resumir | Abertura ou resumo executivo do documento |
| 5 | Revisar | Diagnóstico de trechos obscuros e inconsistências |
| 6 | Verificar | Conferência de todo dado factual na fonte |

Observa-se que a etapa 6 não é uma sexta operação acrescentada ao fim, mas uma disposição que
acompanha todas as demais. Retoma-se, pela última vez, o conceito do Módulo 0: cada trecho produzido
com apoio do sistema carrega o risco de conter afirmação plausível e falsa. **A responsabilidade
sobre o texto assinado permanece integralmente com o docente**, e nenhuma etapa do fluxo transfere
essa responsabilidade.

### Exercício Prático — Atividade Integradora

**Produção de um documento completo (6 min de execução assistida; o documento pode ser concluído
depois)**

1. Escolha um documento curto de sua rotina: comunicado ao colegiado, orientação de atividade,
   resumo de projeto.
2. Solicite uma proposta de estrutura em seções, declarando público e finalidade. Ajuste a lista.
3. Solicite a versão inicial da seção mais longa.
4. Solicite uma reescrita dessa seção, com critério declarado e restrição de preservação.
5. Solicite um resumo de três frases para abrir o documento.
6. Monte o documento no Word, aplique os estilos e confira todo dado factual.

**Critérios de avaliação**

| Critério | Atendido? |
|---|---|
| A estrutura foi solicitada com público e finalidade declarados | |
| A instrução de reescrita continha critério e ao menos uma restrição de preservação | |
| O resumo respeita o formato pedido | |
| Nenhum dado identificável de aluno ou informação sigilosa foi inserido no sistema | |
| Todo dado numérico, data e referência foi conferido contra a fonte | |
| O documento final está no Word, com estilos aplicados e sem símbolos de formatação estranhos | |
| A decisão sobre declaração de uso, tratada no Módulo 0, foi tomada | |

---

# Encerramento

O curso cumpriu a finalidade de estabelecer um repertório mínimo e verificável de uso do ChatGPT na
produção de documentos do Microsoft Word, precedido das verificações de acesso, tratamento de dados
e autoria que a natureza institucional do trabalho docente exige. Recomenda-se prática regular sobre
documentos reais, uma vez que a competência aqui tratada se consolida pelo uso e não pela leitura;
sugere-se manter, nas primeiras semanas, um registro das instruções que produziram bom resultado,
formando repertório próprio.

Apontam-se, como caminhos de aprofundamento, a exploração dos recursos de leitura para análise de
material de terceiros — comparação de documentos, aplicação de rubricas de avaliação, extração de
citações —, o estudo dos suplementos de terceiros disponíveis no ambiente institucional segundo o
critério apresentado no Módulo 1, e a comparação com as demais ferramentas de escrita assistida
contratadas pela instituição.

> **Síntese:** a ferramenta escreve; a responsabilidade pelo que está escrito permanece de quem
> assina.
