# Plano de Aula — Fundamentos do Codex (Essentials)

---

## Identificação

| Campo | Definição |
|---|---|
| Curso | Fundamentos do Codex — Agente de Inteligência Artificial da OpenAI (Essentials) |
| Natureza | Curso curto, introdutório e prático |
| Carga horária | 90 minutos |
| Público-alvo | Profissionais iniciantes em inteligência artificial agente — pessoal administrativo, pesquisadores, analistas, estudantes, gestores e programadores interessados em compreender e operar o Codex |
| Pré-requisitos | Não há conhecimento prévio obrigatório; recomenda-se possuir conta ativa na plataforma ChatGPT |
| Recursos necessários | Computador com acesso à internet, navegador atualizado e conta na plataforma ChatGPT |

---

### Objetivo Geral

O presente curso tem por finalidade introduzir o participante aos fundamentos conceituais e operacionais do Codex, agente de inteligência artificial disponibilizado pela OpenAI para a execução de tarefas de engenharia de software e de trabalho de conhecimento. Ao término do curso, espera-se que o participante seja capaz de distinguir um agente de inteligência artificial de um chat conversacional convencional, de formular instruções eficazes para a delegação de tarefas, de interpretar criticamente as evidências produzidas durante a execução de uma tarefa e de reconhecer os principais cuidados de segurança e privacidade envolvidos nessa prática, consolidando tais competências por meio de uma atividade integradora final.

---

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Diferenciar o funcionamento de um agente de inteligência artificial do funcionamento de um chat conversacional tradicional.
2. Formular instruções (prompts) que contenham objetivo, contexto, restrições e critério de sucesso.
3. Interpretar evidências de execução — registros de log e resultados de teste — para decidir entre aceitar, revisar ou solicitar nova execução de uma tarefa.
4. Aplicar princípios básicos de segurança e privacidade na delegação de tarefas a agentes de inteligência artificial.

---

### Estrutura e Sequência dos Módulos

Os módulos que compõem este curso seguem uma progressão cumulativa: parte-se da conceituação do que constitui um agente de inteligência artificial, avança-se para a formulação de instruções eficazes e para a compreensão do ciclo de execução e revisão, e conclui-se com os princípios de segurança que permeiam toda a prática de delegação. Cada módulo pressupõe o domínio conceitual consolidado no módulo antecedente.

| Módulo | Título | Referência (material-fonte) | Tempo |
|---|---|---|---|
| 1 | O que é o Codex e sua distinção frente a um chat convencional | Comunicado oficial de lançamento do Codex e artigo da Central de Ajuda da OpenAI | 18 min |
| 2 | Comunicação eficaz com agentes de inteligência artificial | Roteiro pedagógico interno consolidado sobre comunicação com agentes | 18 min |
| 3 | Execução, evidências e revisão crítica | Comunicado oficial de lançamento do Codex e roteiro pedagógico interno consolidado | 20 min |
| 4 | Segurança, privacidade e limites de uso | Artigo da Central de Ajuda da OpenAI — "Usando o Codex com seu plano ChatGPT" | 18 min |
| 5 (Síntese) | Síntese e Aplicação Integrada | Integração dos módulos 1 a 4 | 16 min |

---

# Módulo 1 — O que é o Codex e sua Distinção Frente a um Chat Convencional

> Este módulo constitui o ponto de partida do curso, não pressupondo conhecimento prévio sobre agentes de inteligência artificial.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Definir o conceito de agente de inteligência artificial.
2. Distinguir situações em que um chat convencional é suficiente daquelas em que a delegação a um agente é mais apropriada.
3. Descrever os elementos que compõem o ciclo de execução do Codex — ambiente isolado, execução independente e evidências verificáveis.

### Texto Descritivo

Um chat conversacional convencional caracteriza-se por responder a perguntas: recebe uma pergunta em linguagem natural e devolve uma resposta em texto, sem alterar nenhum artefato externo a essa conversa. Um agente de inteligência artificial, por sua vez, distingue-se justamente por *executar* trabalho: além de interpretar uma instrução, ele realiza ações concretas sobre um ambiente — lê e edita arquivos, executa comandos e produz um resultado verificável. O Codex, agente de inteligência artificial disponibilizado pela OpenAI, insere-se nessa segunda categoria, sendo aplicável tanto a tarefas de engenharia de software (programar funcionalidades, corrigir erros, propor alterações para revisão) quanto a tarefas de trabalho de conhecimento mais amplas, como pesquisa, organização de dados e elaboração de documentos.

Do ponto de vista operacional, cada tarefa atribuída ao Codex é processada em um ambiente isolado e próprio, previamente configurado com o projeto ou repositório sobre o qual a tarefa deve ser executada. Esse ambiente permite que o agente leia e edite arquivos, execute estruturas de teste, analisadores de código e verificadores de tipo, de forma independente da atividade que o usuário realiza simultaneamente. O tempo de execução de uma tarefa varia, em geral, de um a trinta minutos, a depender de sua complexidade.

Tal dinâmica pode ser comparada, guardadas as devidas proporções, à atribuição de uma tarefa específica a um profissional qualificado, ao qual se concede autonomia para executá-la em ambiente próprio, ficando o resultado sujeito a posterior verificação. Essa verificação é viabilizada por um princípio central do funcionamento do Codex, que será retomado adiante neste curso: o princípio das evidências verificáveis. Ao concluir uma tarefa, o agente disponibiliza registros de execução (logs de terminal) e resultados de teste que permitem ao usuário acompanhar, passo a passo, o que foi efetivamente realizado — o trabalho do agente não constitui, portanto, uma operação de caixa-preta.

Cumpre registrar que o acesso ao Codex ocorre por meio de diferentes interfaces — incluindo a interface web do ChatGPT, uma interface de linha de comando, uma extensão para editores de código e uma aplicação de desktop —, cada qual mais adequada a um contexto de uso específico. Este curso concentra-se na interface web, por constituir a via de acesso mais direta para o público iniciante, sem prejuízo de o participante explorar as demais interfaces em momento posterior.

A distinção entre chat e agente, apresentada neste módulo introdutório, constitui o fundamento sobre o qual se apoiam os módulos subsequentes: somente a partir da compreensão de que o Codex executa trabalho — e não apenas responde a perguntas — é possível formular instruções adequadas e avaliar criticamente os resultados produzidos.

### Exercício Prático

**Questão de Verificação Conceitual (8 min)**

Das situações a seguir, qual delas representa o cenário mais adequado para delegação a um agente de inteligência artificial como o Codex, e não a um chat convencional?

(a) Esclarecer o significado de um termo técnico.
(b) Corrigir um erro identificado em um arquivo de código-fonte e executar os testes correspondentes.
(c) Obter uma opinião geral sobre determinado tema.
(d) Traduzir uma frase isolada para outro idioma.

**Gabarito:** alternativa (b).

**Fundamentação:** apenas a alternativa (b) descreve uma tarefa que exige execução de ação sobre um artefato externo (o arquivo de código) seguida de verificação objetiva do resultado (a execução dos testes) — características centrais do trabalho de um agente. As demais alternativas limitam-se a solicitar uma resposta em texto, cenário para o qual um chat convencional já é suficiente.

---

# Módulo 2 — Comunicação Eficaz com Agentes de Inteligência Artificial

> Este módulo pressupõe a distinção entre chat e agente estabelecida no módulo anterior, deslocando o foco para a formulação da instrução dirigida ao Codex.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Identificar os quatro elementos constitutivos de uma instrução eficaz.
2. Redigir uma instrução que contenha objetivo, contexto, restrições e critério de sucesso.
3. Aplicar a técnica de decomposição de tarefas complexas em tarefas menores.
4. Reconhecer as vantagens da execução paralela de múltiplas tarefas.

### Texto Descritivo

A qualidade do resultado produzido por um agente de inteligência artificial relaciona-se diretamente com a qualidade da instrução que lhe é fornecida. Uma instrução eficaz — também designada, no contexto de agentes de inteligência artificial, pelo termo técnico "prompt" — compõe-se de quatro elementos: o objetivo, que especifica de forma precisa o que deve ser realizado; o contexto, que indica onde a alteração deve ocorrer (por exemplo, em qual arquivo ou módulo); as restrições, que delimitam o que não deve ser alterado e quais padrões devem ser seguidos; e o critério de sucesso, que estabelece como se pode verificar objetivamente que a tarefa foi concluída de forma satisfatória.

A ausência de qualquer um desses quatro elementos tende a produzir resultados imprecisos. Uma instrução como "corrija o problema no sistema" carece de contexto e de critério de sucesso, obrigando o agente a inferir informações não fornecidas. Já uma instrução como "no arquivo de autenticação, corrija a falha que ocorre quando o e-mail contém letras maiúsculas, normalizando-o para minúsculas antes da comparação; o critério de sucesso é que todos os testes do módulo de autenticação passem a ser aprovados" contempla os quatro elementos e viabiliza um resultado preciso e prontamente revisável.

Quando a tarefa pretendida ultrapassa determinado grau de complexidade, recomenda-se sua decomposição em tarefas menores, cada uma com escopo bem definido. Tal procedimento é comparável, no campo da construção civil, à execução faseada de uma edificação, na qual fundação, estrutura e acabamento correspondem a etapas distintas, executadas e verificadas separadamente. Tarefas de escopo reduzido são executadas com maior precisão pelo agente e revisadas com maior facilidade pelo usuário, reduzindo a probabilidade de resultados parciais ou de decisões arbitrárias por parte do agente diante de ambiguidades.

A decomposição de tarefas viabiliza, ainda, sua execução em paralelo: como cada tarefa é processada em ambiente isolado e próprio, é possível atribuir diversas tarefas ao Codex simultaneamente, sem que ocorra conflito entre elas. Levantamentos setoriais recentes indicam que uma parcela crescente dos usuários avançados do Codex mantém mais de uma tarefa em execução simultânea ao longo do dia, evidenciando uma transição do uso sequencial — uma tarefa por vez — para um uso paralelo, no qual o usuário assume o papel de orquestrador de múltiplos fluxos de trabalho.

A comunicação eficaz, tal como apresentada neste módulo, constitui insumo direto para o módulo subsequente: é a partir de uma instrução bem formulada que se torna possível acompanhar e avaliar criticamente a execução realizada pelo agente.

### Exercício Prático

**Redação de uma Instrução Estruturada (10 min)**

1. Parta da seguinte instrução vaga, fornecida como ponto de partida: "Melhore este projeto."
2. Reescreva-a de modo a contemplar, de forma explícita e identificável, os quatro elementos apresentados no Texto Descritivo: objetivo, contexto, restrições e critério de sucesso.
3. Releia a versão reescrita e verifique se ela permite antecipar, com clareza, qual seria o resultado esperado da execução.

**Critério de êxito:** a instrução reescrita permite identificar, de forma segmentada, cada um dos quatro elementos constitutivos, e seu critério de sucesso é formulado de maneira objetivamente verificável, não admitindo múltiplas interpretações sobre quando a tarefa estaria concluída.

---

# Módulo 3 — Execução, Evidências e Revisão Crítica

> A partir da instrução formulada no módulo anterior, este módulo desloca o foco para o que ocorre durante e após a execução da tarefa pelo Codex.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Descrever o ciclo completo de execução de uma tarefa, da instrução até a proposta de integração do resultado.
2. Interpretar registros de log e resultados de teste como evidências verificáveis do trabalho executado.
3. Aplicar critérios objetivos para decidir entre aceitar, revisar ou solicitar nova execução de uma entrega.

### Texto Descritivo

A execução de uma tarefa pelo Codex segue um ciclo identificável, que compreende as seguintes etapas: formulação da instrução; execução propriamente dita, no ambiente isolado descrito no Módulo 1; execução de testes automatizados sobre a alteração realizada; disponibilização do resultado ao usuário; revisão desse resultado; e, quando aplicável, proposta formal de integração da alteração ao projeto original, usualmente por meio de uma solicitação de incorporação de código (pull request). Ao concluir uma tarefa, o agente disponibiliza as alterações realizadas no próprio ambiente de execução, permitindo ao usuário optar entre solicitar nova revisão, abrir a referida solicitação de incorporação ou integrar o resultado diretamente ao seu ambiente de trabalho local.

Conforme apresentado no Módulo 1, o funcionamento do Codex não constitui uma operação de caixa-preta: cada tarefa concluída é acompanhada de evidências verificáveis, compostas essencialmente por registros de log do terminal e por resultados de testes automatizados. Tais evidências permitem ao usuário compreender exatamente quais comandos foram executados, quais arquivos foram alterados e se as verificações automatizadas aplicáveis foram bem-sucedidas. Quando surgem incertezas ou falhas durante a execução, o agente reporta essas ocorrências de forma explícita, cabendo ao usuário considerá-las antes de qualquer decisão — a omissão dessa etapa configura um dos equívocos mais frequentes na utilização de agentes de inteligência artificial.

A leitura dessas evidências subsidia a decisão central desta etapa do processo: aceitar o resultado, submetê-lo a uma revisão mais aprofundada, ou solicitar nova execução com ajustes na instrução original. Tal decisão não deve ser uniforme para todas as tarefas: alterações em áreas sensíveis de um projeto — como autenticação, tratamento de dados pessoais ou processos de pagamento — exigem grau de escrutínio mais elevado do que alterações de baixo impacto, independentemente do nível de confiança que o usuário deposite no agente.

Não obstante a sofisticação do processo de execução, permanece essencial que o resultado produzido pelo agente seja revisado e validado manualmente pelo usuário antes de sua integração e efetiva utilização. Essa orientação, explicitada pela própria OpenAI em sua documentação oficial, reflete um princípio que permeia a totalidade deste curso: a revisão humana não constitui uma etapa opcional, tampouco dispensável em função da qualidade aparente do resultado.

Os elementos aqui apresentados — evidências verificáveis e critérios de decisão sobre revisão — serão retomados no módulo subsequente, no qual se discutem os cuidados de segurança e privacidade aplicáveis a todo o ciclo de execução.

### Exercício Prático

**Leitura Crítica de um Registro de Execução (10 min)**

1. Considere um registro de execução (log) hipotético no qual conste a seguinte sequência: alteração de um arquivo de cálculo de preços; execução da suíte de testes correspondente; e o resultado "1 teste falhou: `test_desconto_aplicado`".
2. A partir dessa informação, indique qual das três decisões apresentadas no Texto Descritivo — aceitar, revisar ou solicitar nova execução — seria a mais adequada.
3. Justifique a decisão com base nos critérios apresentados neste módulo.

**Critério de êxito:** o participante seleciona a decisão "solicitar nova execução" (ou, alternativamente, "revisar antes de decidir"), justificando-a com base na existência de um teste automatizado não aprovado — situação que, conforme o Texto Descritivo, não deve ser ignorada nem seguida de aceitação automática do resultado.

---

# Módulo 4 — Segurança, Privacidade e Limites de Uso

> Consolidados os módulos anteriores quanto ao funcionamento e à revisão do Codex, este módulo desloca o foco para os cuidados que permeiam toda a prática de delegação a agentes de inteligência artificial.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Descrever o modelo padrão de execução em ambiente isolado (sandbox) adotado pelo Codex.
2. Reconhecer que o acesso à internet durante a execução de tarefas constitui configuração opcional, e não vedação absoluta.
3. Identificar os principais controles de dados e privacidade aplicáveis conforme o tipo de plano contratado.

### Texto Descritivo

O modelo de segurança do Codex fundamenta-se na execução das tarefas em ambiente isolado, tecnicamente designado "sandbox". Por padrão, esse ambiente restringe o acesso do agente ao código fornecido explicitamente pelo repositório sob análise e às dependências previamente instaladas por meio de um script de configuração definido pelo usuário, sem acesso a sítios eletrônicos, interfaces de programação de aplicação (API) ou outros serviços externos.

Cumpre registrar uma atualização relevante nesse modelo: usuários já podem, mediante configuração explícita, permitir que o Codex acesse a internet durante a execução de tarefas específicas. Tal possibilidade amplia as capacidades do agente — permitindo, por exemplo, a consulta a documentação externa ou o download de pacotes de software —, mas amplia, na mesma medida, a superfície de risco da tarefa, por expor o agente a conteúdo externo não verificado, com potencial de conter instruções maliciosas embutidas (fenômeno tecnicamente designado "injeção de instruções", ou *prompt injection*), bem como risco de exfiltração de dados em configurações inadequadas. Depreende-se, portanto, que o acesso à internet deve ser tratado como uma decisão consciente, avaliada tarefa a tarefa, e não como uma característica permanentemente ativa ou permanentemente vedada.

Quanto aos controles de dados, convém observar que estes variam conforme o tipo de plano contratado. Em planos empresariais e educacionais, entradas e saídas processadas pelo Codex não são utilizadas, por padrão, para o aperfeiçoamento dos modelos da OpenAI — ressalvada a possibilidade de organizações usuárias da interface de programação de aplicação optarem, voluntariamente, por compartilhar tais dados, exceto quando adotada política de retenção zero de dados. Em planos de uso pessoal, as conversas podem ser utilizadas para o aperfeiçoamento dos modelos, salvo desativação manual dessa opção nos controles de dados disponibilizados pela plataforma.

Adicionalmente, o uso do Codex está sujeito a limites quantitativos, associados a um conjunto compartilhado de uso agentivo, cuja disponibilidade varia conforme o plano contratado e a complexidade das tarefas executadas. Recomenda-se, nesse sentido, que o participante consulte a página oficial de uso e de preços da OpenAI para obter os valores vigentes, uma vez que tais parâmetros estão sujeitos a atualização periódica e não devem ser tomados como fixos.

Os cuidados aqui apresentados não substituem, mas complementam, os princípios de comunicação eficaz e de revisão crítica discutidos nos módulos anteriores: convém que a atenção do usuário seja redobrada precisamente nos cenários em que uma tarefa envolva acesso à internet, dados sensíveis, ou áreas críticas do projeto.

### Exercício Prático

**Questão de Verificação Conceitual (8 min)**

Sobre o modelo de segurança do Codex, assinale a alternativa correta:

(a) O acesso à internet durante a execução de tarefas é permanentemente vedado, sem exceção.
(b) O acesso à internet constitui configuração opcional, que amplia tanto as capacidades quanto os riscos da tarefa.
(c) Todos os planos utilizam, por padrão e sem possibilidade de desativação, os dados do usuário para o treinamento de modelos.
(d) O ambiente de execução do Codex é, invariavelmente, compartilhado entre diferentes tarefas de um mesmo usuário.

**Gabarito:** alternativa (b).

**Fundamentação:** conforme apresentado no Texto Descritivo, o acesso à internet não constitui regra fixa em nenhum dos dois sentidos, mas configuração habilitável pelo usuário, tarefa a tarefa, com implicações diretas tanto de capacidade quanto de risco. As demais alternativas contradizem informações apresentadas neste módulo: os controles de dados admitem desativação (alternativa c) e cada tarefa é processada em ambiente isolado e próprio (alternativa d).

---

# Módulo 5 — Síntese e Aplicação Integrada

> Este módulo integra as competências desenvolvidas nos quatro módulos anteriores em uma única atividade aplicada.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Articular, em uma única tarefa, a formulação de instrução, a execução e a revisão crítica do resultado.
2. Aplicar os cuidados de segurança e privacidade pertinentes ao cenário proposto.
3. Avaliar o próprio desempenho a partir de critérios objetivos.

### Texto Descritivo

Os módulos precedentes apresentaram, de forma segmentada, os quatro pilares que sustentam a utilização responsável e eficaz do Codex: a compreensão do que distingue um agente de um chat convencional (Módulo 1); a formulação de instruções estruturadas (Módulo 2); a leitura de evidências e a decisão informada sobre aceitar, revisar ou solicitar nova execução (Módulo 3); e os cuidados de segurança e privacidade que atravessam todo o processo (Módulo 4). O presente módulo propõe-se a articular tais competências em uma única atividade, na qual o participante assume, de forma integrada, o papel de responsável por uma tarefa delegada a um agente de inteligência artificial, do planejamento à decisão final.

Convém retomar, nesta síntese, os dois fios condutores que perpassam o curso. O primeiro consiste no princípio das evidências verificáveis, plantado no Módulo 1 e retomado no Módulo 3: toda ação executada pelo agente é passível de verificação objetiva, e essa verificação constitui pré-requisito para qualquer decisão de aceitação. O segundo consiste na centralidade da revisão humana, discutida nos Módulos 3 e 4: independentemente da qualidade aparente do resultado ou da configuração de segurança adotada, cabe ao usuário — nunca ao agente — a decisão final sobre a integração de uma alteração.

A atividade integradora proposta a seguir não exige acesso efetivo ao Codex, podendo ser conduzida de forma inteiramente descritiva; ainda assim, recomenda-se, a título de consolidação prática, que o participante reproduza cada etapa em ambiente real sempre que tal acesso estiver disponível.

### Exercício Prático

**Atividade Integradora (16 min)**

1. Selecione um cenário simples, real ou hipotético, que demande uma alteração pontual em um documento ou trecho de código.
2. Redija uma instrução completa para esse cenário, contendo objetivo, contexto, restrições e critério de sucesso, conforme os princípios apresentados no Módulo 2.
3. Descreva, em prosa, como se daria o acompanhamento da execução dessa tarefa, indicando quais evidências específicas (registros de log, resultados de teste) seriam verificadas antes de qualquer decisão, conforme o Módulo 3.
4. Indique se o cenário proposto demandaria a habilitação de acesso à internet e, em caso afirmativo, quais cuidados adicionais seriam adotados, conforme o Módulo 4.
5. Registre a decisão final — aceitar, revisar ou solicitar nova execução — acompanhada de sua justificativa.

**Critérios de avaliação**

| Critério | Atendido? |
|---|---|
| A instrução contempla, de forma identificável, objetivo, contexto, restrições e critério de sucesso | [ ] |
| A descrição da execução menciona evidências verificáveis específicas ao cenário proposto | [ ] |
| A necessidade (ou dispensa) de acesso à internet está corretamente identificada e justificada | [ ] |
| A decisão final é coerente com os critérios de revisão apresentados no Módulo 3 | [ ] |

---

## Encerramento

O presente curso cumpriu a finalidade de introduzir o participante aos fundamentos conceituais e operacionais do Codex, contemplando a distinção entre agente e chat convencional, a formulação de instruções eficazes, a leitura crítica de evidências de execução e os cuidados de segurança e privacidade inerentes à delegação de tarefas a agentes de inteligência artificial. Recomenda-se a prática regular desses princípios em cenários reais, uma vez que a proficiência na utilização de agentes de inteligência artificial consolida-se, sobretudo, pela repetição consciente do ciclo de instrução, execução e revisão.

Para o aprofundamento dos temas aqui introduzidos, recomenda-se a continuidade dos estudos por meio da trilha prática (Hands-on) sobre o mesmo tema, na qual os conceitos ora apresentados são exercitados em cenários guiados, bem como a exploração posterior de recursos adicionais da plataforma, tais como arquivos de orientação persistente para o agente, execução paralela de múltiplas tarefas e integrações voltadas a contextos empresariais.

> **Síntese:** compreender um agente de inteligência artificial como o Codex consiste em articular instruções claras, evidências verificáveis e revisão crítica constante — não em delegar tarefas sem o devido acompanhamento.
