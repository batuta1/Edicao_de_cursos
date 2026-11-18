# Plano de Aula — IA para Análise de Dados (Essentials)

> *» IA: Bloco Cover — título verbatim. Subtítulo: "Carregar, explorar, visualizar e interpretar dados com o ChatGPT — conferindo cada número na fonte oficial". Não traduzir "ChatGPT", "Julius AI" nem "Análise de dados".*

## Identificação

> *» IA: Bloco Table — tabela verbatim.*

| Campo | Definição |
|---|---|
| Curso | IA para Análise de Dados (Essentials) |
| Natureza | Autoinstrucional, introdutório e prático |
| Carga horária | 127 minutos (sem contar o tempo de processamento das respostas) |
| Público-alvo | Analistas, profissionais de finanças e planejamento, pesquisadores; profissionais de escritórios de advocacia, departamentos jurídicos e compliance; servidores e equipes de regulação, gestores de saúde, engenheiros e técnicos, gestores escolares e profissionais de comunicação |
| Pré-requisitos | Excel básico (o curso funciona para quem cursou apenas *Claude Excel - Essentials*); nenhuma programação; nenhuma estatística além de média e porcentagem |
| Recursos necessários | Computador com navegador e internet; conta ChatGPT (o plano Free atende, com limite de 3 envios de arquivo por dia); conta Julius AI gratuita, opcional; pasta com três bases públicas baixadas no Módulo 0 |

### Objetivo Geral

> *» IA: Bloco Text — verbatim.*

O curso tem por finalidade capacitar o participante a analisar bases de dados sem programar, por meio do recurso Análise de dados do ChatGPT: carregar o arquivo, compreender e limpar a base, explorá-la com os conceitos estatísticos mínimos, gerar gráficos honestos e interpretar os resultados, sempre com verificação contra número oficial publicado. O Julius AI é apresentado como segunda opinião opcional. Como produto final, o participante entrega uma análise curta do IPCA de 2020 a 2025, com tabela, gráfico, premissas e resumo executivo conferidos com o IBGE.

### Competências a Desenvolver

> *» IA: Bloco List — numerada, verbatim, sem acréscimos.*

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Explicar como o assistente chega a um número e por que esse número precisa ser conferido.
2. Decidir, antes de cada envio, se uma base pode ser enviada ao assistente e em que tipo de conta.
3. Carregar uma base pública brasileira e corrigir a leitura de separador, decimal e codificação.
4. Explorar a base escolhendo entre média e mediana, valor absoluto e taxa, valor nominal e real.
5. Produzir e reconhecer gráficos honestos, evitando as táticas de distorção documentadas.
6. Conferir resultados com a rotina de cinco verificações e comunicá-los com premissas e limitações.

### Estrutura e Sequência dos Módulos

> *» IA: Bloco Text — verbatim.*

Os módulos são cumulativos: cada um pressupõe o anterior. O princípio "o número só vale depois da conferência" é apresentado no Módulo 1 e retomado nos Módulos 3, 5 e 6. Um caso-guia — o IPCA mensal do Banco Central, com gabarito do IBGE — atravessa os Módulos 1, 3, 4, 6 e 7.

> *» IA: Bloco Table — verbatim.*

| Módulo | Título | Referência | Tempo |
|---|---|---|---|
| 0 | Preparação e Verificação Inicial | Página de planos do ChatGPT; ajuda "Envio de arquivos"; Banco Central, IBGE, CVM | 7 min |
| 1 | Análise de Dados com IA: o que é e como funciona | Ajuda "Análise de dados com o ChatGPT"; documentação do Julius | 19 min |
| 2 | Dados, Privacidade e Sigilo | Ajudas de controles de dados; política do Julius; LGPD; ANPD; OAB | 15 min |
| 3 | Carregar, Entender e Limpar a Base | Ajudas "Extraindo insights" e "Análise de dados"; bases públicas | 16 min |
| 4 | Explorar sem Cair em Armadilhas | OpenAI Academy; IBGE; Banco Central | 16 min |
| 5 | Gráficos Honestos | Ajuda "Extraindo insights"; IEEE VIS 2025; VisEval | 22 min |
| 6 | Verificar e Comunicar | JMIR 2025; CVM; CNJ; OpenAI Academy | 16 min |
| 7 | Síntese e Aplicação Integrada | — | 16 min |

---

# Módulo 0 — Preparação e Verificação Inicial

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 0" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Ponto de partida: verifica a conta, o limite de envio e as bases antes de qualquer análise.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Identificar o próprio plano do ChatGPT e o limite de envio de arquivos correspondente.
2. Localizar o comando de envio de arquivos.
3. Baixar três bases públicas por link direto e organizá-las numa pasta.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir.*

O recurso utilizado no curso chama-se Análise de dados e está presente em todos os planos do ChatGPT. Na página oficial de preços, o plano Free aparece com análise de dados "Limitado". O limite que mais afeta o estudo é o de envio de arquivos: segundo a central de ajuda da OpenAI, "usuários do plano gratuito têm um limite de 3 uploads de arquivos por dia", e a empresa pode reduzir esse limite nos horários de pico. Por essa razão, os exercícios do curso utilizam no máximo um envio por módulo.

> *» IA: Bloco Table — verbatim.*

| Plano | Preço (pt-BR, nov/2026) | Análise de dados |
|---|---|---|
| Free | R$ 0 | Limitado; 3 envios de arquivo por dia |
| Go | R$ 39,99/mês | Incluída |
| Plus | R$ 99,90/mês | Incluída |

> *» IA: Bloco Text — verbatim; não resumir.*

As bases do curso são públicas, gratuitas e acessíveis sem cadastro. Cada uma tem um número oficial publicado que funciona como gabarito, o que permite ao participante conferir sozinho o próprio resultado. Recomenda-se criar uma pasta denominada `analise-ia` e salvar nela os três arquivos.

> *» IA: Bloco Table — tabela verbatim; preservar os endereços.*

| Arquivo | Conteúdo | Endereço | Gabarito oficial |
|---|---|---|---|
| `ipca.csv` | IPCA mensal 2020–2025 (Banco Central, série 433) | `api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2020&dataFinal=31/12/2025` | 2024: 4,83%; 2025: 4,26% (IBGE) |
| `populacao-uf.csv` | População por UF, Censo 2022 (IBGE, tabela 4709) | `apisidra.ibge.gov.br/values/t/4709/n3/all/v/93/p/2022?formato=csv` | Brasil: 203.080.756 |
| `cad_cia_aberta.csv` | Cadastro de companhias abertas (CVM) | `dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv` | 2.680 linhas, codificação latin-1 |

> *» IA: Statement — preservar o emoji e o breadcrumb.*

> 💡 Quando o navegador exibir o conteúdo do arquivo na tela em vez de baixá-lo, recomenda-se `Navegador > Arquivo > Salvar como`, com a extensão `.csv`. Não é necessário abrir as bases no Excel: elas seguem diretamente para o ChatGPT.

### Exercício Prático

> *» IA: Process — passos verbatim; preservar os breadcrumbs.*

**Verificação inicial (7 min)**

1. Acessar `chatgpt.com` e identificar o plano em `ChatGPT > Perfil (canto inferior esquerdo)`.
2. Localizar o comando `ChatGPT > Caixa de mensagem > +`, sem enviar nada.
3. Baixar as três bases e conferir que a pasta `analise-ia` contém os três arquivos.

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: plano identificado em `ChatGPT > Perfil`, comando `+` localizado e três arquivos na pasta `analise-ia`.

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Uso o ChatGPT no plano [Free/Go/Plus]. Vou analisar planilhas públicas. Explique, em cinco tópicos
curtos, o que o recurso de análise de dados faz neste plano, qual é o limite de envio de arquivos e
onde confiro essas informações na central de ajuda oficial.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 0" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 1 — Análise de Dados com IA: o que é e como funciona

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe a conta verificada no Módulo 0; desloca o foco para o funcionamento do recurso.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Explicar que o ChatGPT escreve e executa código para produzir os números de uma análise.
2. Identificar os formatos aceitos e os limites do recurso.
3. Descrever o papel do Julius AI como segunda opinião.
4. Enunciar as sete etapas de uma análise e o princípio da conferência.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir; não traduzir "Code Interpreter", "Advanced Data Analysis", "Generated code" nem "Data Explorer".*

Análise de dados com inteligência artificial, no sentido deste curso, consiste em enviar uma base a um assistente e formular perguntas em linguagem natural, sem escrever fórmulas. O ChatGPT não estima os números: segundo a documentação oficial, para tarefas de análise de dados ele "escreve e executa código Python em um ambiente de notebook Jupyter com estado". Em termos simples, o assistente redige uma receita de cálculo — o código —, executa-a sobre o arquivo e relata o resultado. A expressão "com estado" significa que cada passo lembra o anterior, à semelhança de um caderno de laboratório; se o ambiente for reiniciado, essa memória se perde e o arquivo precisa ser enviado novamente.

O recurso já se chamou Code Interpreter e, depois, Advanced Data Analysis. Atualmente, não é ativado em nenhuma configuração: é acionado ao anexar um arquivo e solicitar uma análise. Aceita planilhas (`.csv`, `.xls`, `.xlsx`, `.tsv`, `.ods`), arquivos de dados (`.json`, `.xml`), textos e PDFs. A própria OpenAI adverte que valores de tabelas em PDF digitalizado ou em imagem podem não ser extraídos de forma confiável e recomenda, quando a exatidão importar, o envio de planilha ou de arquivo de texto. Cumpre registrar ainda que o ambiente Python "não pode fazer solicitações externas na web": a base deve ser baixada antes e enviada como arquivo.

O Julius AI é um espaço de trabalho especializado no mesmo tipo de tarefa. Escreve código em Python ou R, exibe cada etapa com os rótulos "Generating code" e "Generated code" e oferece o Data Explorer, painel que mostra as tabelas produzidas durante a análise. Neste curso, desempenha o papel de segunda opinião opcional: a interface é em inglês, embora as respostas possam ser obtidas em português por instrução; o plano gratuito concede 75 créditos iniciais e 25 diários; e os arquivos são apagados após uma hora de inatividade.

Decorre desse funcionamento o princípio que orienta todo o curso: o número só vale depois da conferência. A OpenAI recomenda revisar "o código gerado, as saídas e as suposições antes de confiar no resultado", pois um código correto pode operar sobre uma premissa equivocada. A análise organiza-se em sete etapas — carregar, entender, limpar, explorar, visualizar, interpretar e comunicar —, e a verificação atravessa todas elas.

> *» IA: Bloco Table — verbatim.*

| Etapa | Pergunta que responde | Módulo |
|---|---|---|
| Carregar e entender | O que há no arquivo? | 3 |
| Limpar | O arquivo foi lido corretamente? | 3 |
| Explorar | O que os números dizem? | 4 |
| Visualizar | Como mostrar sem distorcer? | 5 |
| Interpretar e comunicar | O que se pode e o que não se pode concluir? | 6 |

> *» IA: Statement — preservar o emoji e o breadcrumb.*

> 📌 O comando que exibe o código executado aparece ao final da resposta do ChatGPT. O rótulo exato deve ser conferido na interface (referido em guias externos como "Ver análise"). Na ausência do comando, basta solicitar: "Mostre o código Python que foi executado".

### Exercício Prático

> *» IA: Knowledge Check — questão de múltipla escolha; alternativas e gabarito verbatim.*

**Questão (4 min)**

Um analista envia uma planilha ao ChatGPT e recebe um total. Qual procedimento é coerente com a orientação oficial da OpenAI?

(a) Aceitar o total, pois foi calculado por código.
(b) Revisar o código, as saídas e as suposições, e conferir o total com uma fonte independente.
(c) Repetir a pergunta até obter o mesmo número duas vezes.
(d) Ativar o modo de análise avançada nas configurações.

> *» IA: Statement — gabarito verbatim.*

**Gabarito:** (b). Código executado pode estar correto sobre uma premissa errada; a alternativa (c) não verifica nada; a alternativa (d) descreve uma configuração inexistente.

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Vou enviar uma planilha. Antes de calcular, explique em linguagem simples que passos de código você
vai executar, que suposições vai adotar sobre o arquivo e como eu posso conferir o resultado depois.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 2 — Dados, Privacidade e Sigilo

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe o funcionamento visto no Módulo 1; antecede o primeiro envio real de arquivo.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Configurar os controles de dados do ChatGPT e abrir um chat temporário.
2. Descrever a política de uso de conteúdo do Julius AI.
3. Classificar uma base no semáforo de dados à luz da LGPD e do sigilo profissional.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir; preservar os breadcrumbs.*

Nos espaços pessoais Free, Plus e Pro, segundo a central de ajuda da OpenAI, "o compartilhamento de dados para treinamento fica ativado por padrão". A opção é desligada em `ChatGPT > Perfil > Configurações > Controles de dados > Melhorar o modelo para todo mundo`. O chat temporário não aparece no histórico, não cria memórias e não é usado para treinar modelos, mas pode ser retido por até 30 dias por motivos de segurança. Conversas excluídas são apagadas dos sistemas em até 30 dias; arquivos guardados na Biblioteca precisam ser excluídos à parte. Nos planos Business, Enterprise e Edu, a OpenAI informa que não utiliza entradas e saídas para treinar modelos por padrão.

No Julius AI, a documentação declara que os Termos de Serviço e a Política de Privacidade permitem compartilhar o conteúdo do usuário, incluindo prompts, arquivos enviados e saídas, com provedores de tecnologia de inteligência artificial, para que estes avaliem, aprimorem e desenvolvam os próprios modelos. A recusa é feita por e-mail ao endereço privacy@julius.ai. Os dados podem ser armazenados nos Estados Unidos. Depreende-se que o Julius, no uso pessoal, deve receber apenas dados públicos.

A Lei Geral de Proteção de Dados (LGPD) protege toda informação que identifique uma pessoa. A Autoridade Nacional de Proteção de Dados (ANPD) publicou, até o momento, apenas um estudo preliminar sobre anonimização e pseudonimização. Pseudonimizar consiste em substituir o identificador — nome, CPF, número de processo vinculado a pessoa — por um código e guardar a tabela de correspondência fora da ferramenta. Para a advocacia, a Recomendação 001/2024 do Conselho Federal da OAB orienta supervisionar os resultados, preservar o sigilo profissional e comunicar ao cliente o uso de inteligência artificial.

> *» IA: Bloco Table — verbatim.*

| Cor | O que é | Exemplo | Conduta |
|---|---|---|---|
| Verde | Dado público ou agregado | IPCA, população por UF | Pode ser enviado |
| Amarelo | Dado interno sem pessoa identificável | Vendas por região | Somente sob política da organização e em conta corporativa |
| Vermelho | Dado pessoal, sensível ou sigiloso | CPF, prontuário, processo com partes, carteira de clientes | Não enviar em conta pessoal; pseudonimizar ou agregar antes |

### Exercício Prático

> *» IA: Process — passos verbatim; preservar os breadcrumbs.*

**Configurar antes de enviar e classificar (15 min)**

1. Abrir `ChatGPT > Perfil > Configurações > Controles de dados` e decidir sobre "Melhorar o modelo para todo mundo".
2. Abrir um chat temporário em `ChatGPT > Novo chat > Chat temporário` e fechá-lo.
3. Classificar no semáforo: (1) IPCA mensal; (2) planilha de honorários com nome dos clientes; (3) número de atendimentos por unidade de saúde, sem pacientes; (4) lista de alunos com notas; (5) demonstração de resultado publicada por companhia aberta.

> *» IA: Statement — gabarito verbatim; preservar o emoji.*

> 🏁 Ponto de controle: estado da opção registrado em `Configurações > Controles de dados`. Gabarito do semáforo: (1) verde; (2) vermelho; (3) verde ou amarelo, conforme a política do órgão; (4) vermelho; (5) verde.

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Tenho uma planilha com as colunas [listar colunas, sem enviar os dados]. Indique quais colunas
identificam pessoas, como pseudonimizá-las antes do envio e que versão agregada da planilha
permitiria responder à pergunta [pergunta] sem dados pessoais.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 3 — Carregar, Entender e Limpar a Base

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe os controles de dados configurados no Módulo 2; inicia o trabalho com arquivos.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Enviar uma base e expandir a tabela interativa.
2. Solicitar o "Raio X" da base antes de qualquer cálculo.
3. Reconhecer separador, decimal, codificação e cabeçalho típicos de dados públicos brasileiros.
4. Corrigir a leitura de um arquivo com acentos corrompidos.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir; preservar os breadcrumbs.*

O envio é feito em `ChatGPT > Caixa de mensagem > + > Adicionar fotos e arquivos`. Ao carregar uma planilha, conforme a central de ajuda, "o ChatGPT cria automaticamente uma visualização interativa da tabela"; o ícone de duas setas, no canto superior direito, amplia a visualização, e linhas ou colunas podem ser selecionadas com Ctrl (Windows) ou Command (Mac) para perguntas sobre o trecho destacado.

Antes de qualquer cálculo, recomenda-se o "Raio X" da base: número de linhas e colunas, tipo de cada coluna (número, texto, data), período coberto e valores vazios. O procedimento equivale a conferir o conteúdo de uma caixa antes de assinar o recebimento. A central de ajuda recomenda dados com nomes de coluna claros e um registro por linha, e adverte que um arquivo pode ser enviado com sucesso e, ainda assim, não ser analisado por inteiro; o Raio X permite perceber essa situação.

Os dados públicos brasileiros apresentam características que confundem a leitura automática. Codificação é o "alfabeto" em que o arquivo foi gravado: lido com o alfabeto errado, "RECUPERAÇÃO" torna-se "RECUPERA��O". Convém declarar o formato já no pedido e solicitar a releitura quando necessário.

> *» IA: Bloco Table — verbatim.*

| Característica | Onde aparece | O que pode dar errado |
|---|---|---|
| Separador ponto e vírgula | Banco Central, IBGE, CVM, CNJ | Tudo lido como uma única coluna |
| Vírgula decimal (`0,21`) | Banco Central | Número lido como texto |
| Codificação latin-1 | CVM, CNJ | Acentos corrompidos |
| Cabeçalho em duas linhas | IBGE/SIDRA (códigos na primeira, nomes na segunda) | Primeira linha de dados tratada como cabeçalho |
| Escala ("MIL") | CVM | Valor mil vezes menor |

> *» IA: Accordion — título = problema, corpo = solução; verbatim.*

| Problema | Solução |
|---|---|
| Acentos corrompidos | Solicitar: "Releia o arquivo com codificação latin-1" |
| Número tratado como texto | Solicitar: "Converta a coluna valor considerando vírgula decimal" |
| Mensagem de limite de envio atingido | Aguardar o horário indicado; tentativas que falham podem contar para o limite |
| Resultado aparentemente parcial | Solicitar o número de linhas lidas e compará-lo com o Raio X |

### Exercício Prático

> *» IA: Process — passos verbatim; preservar os breadcrumbs.*

**Raio X de duas bases (16 min, dois envios)**

1. Em `ChatGPT > Caixa de mensagem > + > Adicionar fotos e arquivos`, enviar `ipca.csv` com o pedido: "Antes de calcular qualquer coisa, informe número de linhas e colunas, tipo de cada coluna, período coberto e valores vazios."
2. Expandir a tabela pelo ícone de duas setas e conferir as primeiras linhas.
3. Na mesma conversa, enviar `cad_cia_aberta.csv` e solicitar as cinco primeiras linhas; se os acentos estiverem corrompidos, solicitar a releitura em latin-1.

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: `ipca.csv` com 72 linhas, colunas `data` e `valor`, de janeiro de 2020 a dezembro de 2025, e `valor` reconhecido como número; cadastro exibido com acentos corretos.

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Este arquivo usa [ponto e vírgula] como separador, [vírgula] como decimal, datas no formato
[dd/mm/aaaa] e codificação [latin-1]. Leia respeitando isso e, antes de qualquer cálculo, informe:
número de linhas e colunas, tipo de cada coluna, período coberto e valores vazios por coluna.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 4 — Explorar sem Cair em Armadilhas

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe a base lida corretamente no Módulo 3; desloca o foco da leitura para o significado dos números.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Escolher entre média e mediana conforme a distribuição dos dados.
2. Comparar grupos de tamanhos diferentes por meio de taxas.
3. Distinguir valor nominal de valor real e variação percentual de ponto percentual.
4. Separar correlação de causalidade na redação de conclusões.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir.*

O ChatGPT calcula somas, médias, medianas, mínimos, máximos e desvio padrão com rapidez; a escolha da medida adequada, porém, permanece com o analista. A média divide o total igualmente entre os casos; a mediana é o valor central da fila ordenada. Quando há valores muito altos, a média se desloca e deixa de representar o caso típico: a população média das 27 unidades da federação é de cerca de 7,52 milhões, influenciada por São Paulo (44,4 milhões), enquanto a mediana é de 3,94 milhões.

Comparações entre grupos de tamanhos diferentes exigem taxas. Um tribunal de um estado populoso recebe naturalmente mais processos; a comparação justa divide o número de processos pela população e multiplica por 100 mil. Do mesmo modo, valores monetários de anos diferentes só são comparáveis após correção pela inflação: R$ 1.000 de janeiro de 2024 equivalem a cerca de R$ 1.092,96 em dezembro de 2025, pelo IPCA acumulado nos dois anos.

Diferenças entre taxas medem-se em pontos percentuais. O IPCA passou de 4,83% em 2024 para 4,26% em 2025, uma queda de 0,57 ponto percentual — forma utilizada pelo próprio IBGE. Por fim, duas variáveis que crescem juntas não provam que uma causa a outra. A OpenAI recomenda instruir o assistente a "não tratar correlações como causas" e a "apontar quaisquer limitações nos dados".

> *» IA: Bloco Table — verbatim.*

| Conceito | Definição simples | Exemplo nas bases |
|---|---|---|
| Média × mediana | Média divide o total igualmente; mediana é o valor central | Média das UFs ≈ 7,52 milhões; mediana 3,94 milhões |
| Valor atípico | Ponto muito fora do padrão: erro ou fato relevante | Lucro aparentemente mil vezes maior por erro de escala |
| Taxa por 100 mil | Divide pelo tamanho da população | Processos por 100 mil habitantes |
| Nominal × real | Valor corrigido pela inflação | R$ 1.000 (jan/2024) ≈ R$ 1.092,96 (dez/2025) |
| % × ponto percentual | Diferença entre taxas | IPCA caiu 0,57 p.p. de 2024 para 2025 |
| Correlação × causa | Variar junto não prova causa | Mais processos onde há mais habitantes |

### Exercício Prático

> *» IA: Process — passo verbatim.*

**O acumulado do caso-guia (6 min)**

1. Na conversa do IPCA, solicitar: "Calcule o IPCA acumulado de 2024 e de 2025 a partir das taxas mensais e mostre a fórmula usada."

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: 2024 = 4,83% e 2025 = 4,26%, com fórmula de composição (produto de 1 + taxa/100, menos 1).

> *» IA: Knowledge Check — questão de múltipla escolha; alternativas e gabarito verbatim.*

**Questão (4 min)**

O IPCA foi 4,83% em 2024 e 4,26% em 2025. A frase correta é:

(a) A inflação caiu 0,57%.
(b) A inflação caiu 0,57 ponto percentual.
(c) A inflação caiu 11,8 pontos percentuais.

**Gabarito:** (b). A queda relativa seria de cerca de 11,8%, e não de 11,8 pontos percentuais.

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Analise a coluna [coluna]. Informe média e mediana e diga qual representa melhor o caso típico.
Se eu for comparar grupos de tamanhos diferentes, proponha a taxa adequada. Não trate correlações
como causas e liste as limitações dos dados.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 5 — Gráficos Honestos

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 5" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe os conceitos do Módulo 4; desloca o foco dos números para a sua representação visual.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Solicitar, ajustar e baixar um gráfico no ChatGPT.
2. Alternar um gráfico entre as versões interativa e estática.
3. Identificar as oito táticas de gráfico enganoso documentadas.
4. Aplicar uma lista de conferência de honestidade e acessibilidade.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir; não traduzir termos de interface.*

O ChatGPT gera gráficos estáticos de linhas, barras, pizza, histogramas, dispersão, diagramas de caixa, mapas de calor, área, radar, mapas de árvore, bolhas e cascata. Os gráficos de barras, linhas, pizza e dispersão podem ser exibidos como interativos, por meio do comando "Alternar para gráfico interativo"; o retorno é feito por "Alternar para gráfico estático". As cores podem ser editadas por paleta ou por código hexadecimal, e o download padrão gera um arquivo PNG. No Julius AI, o gráfico é descrito em linguagem natural e salvo pelo botão direito do mouse.

Estudo apresentado em 2025 na conferência IEEE VIS, de referência em visualização de dados, reuniu oito táticas de gráfico enganoso: eixo truncado, distorção de proporção, eixo duplo, eixo invertido, projeção distorcida (como o efeito 3D), desproporção entre dado e desenho, codificação contínua inadequada e codificação categórica inadequada. No experimento, diante de um gráfico com eixo invertido, um modelo de inteligência artificial concordou fortemente que uma série em queda estava em alta. Depreende-se que solicitar à IA que "confira o gráfico" não substitui a leitura humana.

Outro estudo, o VisEval (2024), classificou as falhas de gráficos gerados por modelos de linguagem em três grupos: código que não produz o gráfico, gráfico que utiliza coluna ou legenda erradas e gráfico de leitura difícil. A conferência de um gráfico, portanto, inclui verificar se ele mostra exatamente as colunas pedidas, além de verificar a forma.

> *» IA: Bloco Table — verbatim.*

| Pergunta de conferência | Problema que evita |
|---|---|
| O eixo das barras começa em zero? | Eixo truncado |
| O eixo cresce na direção habitual? | Eixo invertido |
| Há uma única escala? | Eixo duplo |
| O gráfico mostra as colunas pedidas, com a legenda correta? | Coluna ou legenda erradas |
| O título enuncia a conclusão e a fonte está no rodapé? | Leitura sem contexto |
| As cores se distinguem sem depender de vermelho e verde? | Exclusão de pessoas daltônicas |

### Exercício Prático

> *» IA: Process — passos verbatim; preservar os breadcrumbs.*

**O mesmo dado, duas histórias (16 min, um envio)**

1. Em `ChatGPT > Caixa de mensagem > + > Adicionar fotos e arquivos`, enviar `populacao-uf.csv` e solicitar: "A primeira linha tem códigos e a segunda os nomes das colunas. Faça um gráfico de barras horizontais das 10 UFs mais populosas, ordenado, com eixo começando em zero, título com a conclusão e fonte IBGE Censo 2022 no rodapé."
2. Usar o comando `Gráfico > Alternar para gráfico interativo` e passar o cursor sobre as barras.
3. Solicitar a mesma figura com o eixo começando em 5 milhões.
4. Comparar as duas versões e baixar a honesta pelo ícone de download do gráfico.

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: arquivo PNG salvo na pasta `analise-ia` e justificativa escrita de por que a versão com eixo em 5 milhões exagera as diferenças (eixo truncado).

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Faça um gráfico de [tipo] de [coluna] por [categoria]. Eixo começando em zero, ordenado do maior
para o menor, título que enuncie a conclusão, fonte [fonte] no rodapé e cores distinguíveis por
pessoas daltônicas. Depois, escreva um texto alternativo de duas frases para o gráfico.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 5" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 6 — Verificar e Comunicar

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 6" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe o ciclo completo dos Módulos 3 a 5; retoma o princípio da conferência do Módulo 1.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Relatar erros documentados de assistentes de IA em análise de dados.
2. Aplicar a rotina de cinco conferências a um resultado.
3. Redigir um resumo executivo com achados, premissas, limitações e fonte.
4. Reconhecer quando a pergunta exige um especialista.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir.*

Estudo publicado no Journal of Medical Internet Research em 2025 avaliou o ChatGPT com execução de código em dados de pesquisa em saúde. A ferramenta acertou o tratamento dos dados e a estatística descritiva em todas as tentativas; na estatística inferencial, contudo, acertou 32,5% com pedidos básicos, 81,3% com pedidos intermediários e 92,5% com pedidos detalhados. O grau de detalhamento do pedido alterou o resultado tanto quanto a própria ferramenta, e os autores concluem que a aplicação exige construção cuidadosa do pedido e supervisão humana.

As bases deste curso contêm armadilhas reais, de natureza semelhante. Na base de demonstrações financeiras da CVM, oito empresas informam valores em reais e as demais em milhares: sem a conversão, uma companhia com lucro de R$ 653 milhões aparece acima da Petrobras, cujo lucro atribuído aos acionistas controladores foi de R$ 36,6 bilhões. Na base do Justiça em Números, do Conselho Nacional de Justiça, há linhas de total por ramo misturadas às linhas de cada tribunal, e a soma direta dos casos novos de 2025 resulta no dobro dos 40,9 milhões publicados. Em ambos os casos, o código executa sem erro; a falha está na premissa.

Para comunicar, a OpenAI recomenda iniciar pela decisão a ser apoiada ("Estou tentando decidir ___, com base em ___"), solicitar um resumo executivo e pedir que o assistente mostre como chegou aos números, incluindo suposições e fórmulas. Um resumo honesto contém achados, premissas, limitações e fonte com data de extração. Quando a pergunta exigir inferência estatística, previsão ou modelagem, recomenda-se recorrer a um especialista ou ao curso *Dados com Python e IA*.

> *» IA: Bloco Table — verbatim.*

| Conferência | Procedimento |
|---|---|
| 1. Contar linhas | Antes e depois de cada filtro |
| 2. Recalcular um total | Na planilha ou manualmente |
| 3. Ler o cálculo | Abrir o código e localizar a fórmula principal |
| 4. Comparar com número oficial | IBGE, Banco Central, CVM, CNJ |
| 5. Listar premissas | Separador, filtros, linhas excluídas, escala |

### Exercício Prático

> *» IA: Process — passo verbatim.*

**Mostre o cálculo (6 min)**

1. Na conversa do IPCA, solicitar o código do acumulado de 2024 e, em seguida: "Calcule também somando as taxas mensais. Qual dos dois é o correto e por quê?"

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: composição = 4,83% (igual ao IBGE); soma = 4,73% (incorreta); a diferença entre multiplicar e somar foi localizada no código.

> *» IA: Knowledge Check — questão de múltipla escolha; alternativas e gabarito verbatim.*

**Questão (4 min)**

Ao ordenar o lucro das companhias da CVM, uma empresa pouco conhecida aparece muito acima da segunda colocada. Qual é a primeira hipótese a investigar?

(a) Fraude contábil.
(b) Escala do valor (milhares ou reais).
(c) Erro do ChatGPT na ordenação.

**Gabarito:** (b). Na base de 2024, oito empresas informam valores em reais e as demais em milhares.

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Estou tentando decidir [decisão], com base em [dados]. Antes do resumo, liste: linhas lidas e
descartadas, filtros aplicados, unidades e escalas, fórmulas usadas e o número oficial com que posso
comparar o resultado. Depois, escreva um resumo executivo de cinco linhas com achados, premissas e
limitações, sem afirmações de causa.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 6" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Módulo 7 — Síntese e Aplicação Integrada

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Módulo 7" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja títulos dentro de exemplos de código. ▼▼▼*

> Pressupõe todos os módulos anteriores; integra as competências numa única análise do caso-guia.

### Objetivos de Aprendizagem

> *» IA: Bloco List — verbatim, sem acréscimos.*

Ao final deste módulo, o participante deverá ser capaz de:

1. Conduzir uma análise completa de base pública, do envio ao resumo.
2. Conferir o resultado com o número oficial e registrar as diferenças.
3. Entregar tabela, gráfico, premissas e resumo executivo coerentes entre si.

### Texto Descritivo

> *» IA: Bloco Text — verbatim; não resumir.*

A atividade integradora reúne, numa conversa nova, as competências desenvolvidas no curso, aplicadas ao caso-guia: a série mensal do IPCA de 2020 a 2025. O envio do arquivo consome um dos três envios diários do plano Free.

Pequenas diferenças entre o acumulado calculado a partir das taxas mensais e o valor publicado pelo IBGE, da ordem de 0,01 ponto percentual, podem ocorrer em alguns anos, porque o Banco Central divulga as taxas mensais arredondadas em duas casas. Essa diferença deve ser registrada como limitação, e não corrigida para coincidir com o gabarito.

### Exercício Prático

> *» IA: Process — passos verbatim; preservar os breadcrumbs.*

**Atividade integradora (16 min)**

1. (Módulo 2) Confirmar o estado de `Configurações > Controles de dados`.
2. (Módulo 3) Enviar `ipca.csv` e solicitar o Raio X.
3. (Módulo 4) Solicitar a tabela do IPCA acumulado de cada ano de 2020 a 2025, por composição.
4. (Módulo 5) Solicitar gráfico de barras anual com eixo em zero, título com a conclusão e fonte.
5. (Módulo 6) Conferir 2024 e 2025 com o IBGE, solicitar as premissas e um resumo executivo de cinco linhas.

> *» IA: Checklist — tabela de critérios verbatim.*

| Critério | Atendido? |
|---|---|
| Raio X correto (72 linhas, 2020–2025) | |
| 2024 = 4,83% e 2025 = 4,26% | |
| Gráfico com eixo em zero, título-conclusão e fonte | |
| Premissas listadas (separador, decimal, composição) | |
| Resumo sem afirmação causal e com limitação registrada | |

> *» IA: Statement — critério de êxito; preservar o emoji.*

> 🏁 Ponto de controle: os cinco critérios atendidos na mesma conversa, com o resumo executivo como última resposta.

### Mão na massa

> *» IA: Statement — prompt-base verbatim, entre aspas triplas.*

"""
Analise esta base de [tema]. Etapas: 1) Raio X; 2) [cálculo principal]; 3) gráfico honesto com
fonte; 4) comparação com o número oficial [número e fonte]; 5) premissas e limitações; 6) resumo
executivo de cinco linhas para [público]. Mostre o código das etapas 2 e 4.
"""

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Módulo 7" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Encerramento

> *» IA: Bloco Text — verbatim.*

O curso apresentou a análise de dados com assistentes de inteligência artificial como um ciclo de sete etapas, sustentado pela conferência contra fonte oficial. Recomenda-se praticar com bases públicas de gabarito conhecido antes de levar a ferramenta a dados de trabalho, e sempre sob a política de dados da organização.

Para aprofundamento, o curso *IA para Análise de Dados - Hands On* conduz análises completas de bases da CVM e do CNJ; *Dados com Python e IA* leva o mesmo ciclo para código próprio e reprodutível; *Jurimetria com IA* aplica-o a dados judiciais.

> *» IA: Statement — citação final verbatim.*

> **Síntese:** a IA escreve o cálculo; a responsabilidade pelo número continua de quem o assina.
