# Análise Crítica 360° — Roteiro Base "Claude Skills Para Leigos"

**Documento analisado:** `roteiro-curso-claude-skills.md` (Etapa 1)
**Público-alvo de referência:** professores universitários, sem pré-requisitos técnicos
**Data da análise:** 15 de agosto de 2026
**Natureza:** auditoria externa, sem complacência com o material de origem

---

## 1. Sumário Executivo

### Nível geral de qualidade

**Bom**, com um teto claramente definido por três problemas estruturais que impedem a nota superior.

### Maturidade pedagógica

O roteiro demonstra domínio da progressão conceitual e usa analogias genuinamente adequadas ao público (plano de aula para substituto, lombadas na estante, texto de apoio *versus* roteiro do monitor). O vocabulário técnico é introduzido no momento de uso, sem acúmulo prévio. A escolha de centrar o curso no claude.ai, tratando Claude Code como horizonte, é acertada e coerente com o público declarado.

Contudo, o material **viola o próprio princípio pedagógico que enuncia**. O prompt da Etapa 1 determina: "evite excesso de teoria antes da primeira prática; o participante deve experimentar alguma criação já no início do curso". O participante só cria uma Skill de verdade no **Módulo 4** — depois de três módulos inteiramente conceituais. As Pílulas dos Módulos 1, 2 e 3 são, respectivamente, um exercício de papel, uma pergunta ao chat e a redação de um arquivo que não vai a lugar nenhum. Nenhuma delas produz o "resultado visível rápido" exigido.

### Maturidade técnica

Alta, com uma ressalva importante. O conteúdo é fiel ao material-fonte e evita as invenções mais comuns (não atribui à ferramenta capacidades inexistentes, sinaliza limites, distingue superfícies). A distinção Skill × MCP × plugin está correta, assim como o tratamento de progressive disclosure e as regras de validação de `name` e `description`.

A ressalva: o roteiro afirma que a criação de Skills próprias exige plano **Pro, Max, Team ou Enterprise**. O material-fonte é **contraditório** neste ponto — uma passagem menciona disponibilidade para Free, Pro, Max, Team e Enterprise; outra restringe a Pro, Max, Team e Enterprise. O roteiro escolheu uma das versões sem sinalizar a divergência. Como esse é o pré-requisito de acesso do curso inteiro, é uma afirmação que precisa de verificação antes da publicação.

### Qualidade do fluxo

O ciclo pretendido — descrever → gerar → observar → avaliar → refinar — está **enunciado** no Módulo 9, mas não é **praticado** ao longo do curso. O participante nunca é levado a olhar uma saída ruim, identificar o problema, corrigir a Skill e comparar. O curso fala sobre iteração; não a exercita.

### Principais forças

1. Analogias precisas e ancoradas no cotidiano docente real, não decorativas.
2. Honestidade intelectual consistente: limites declarados, riscos nomeados, pesquisas apresentadas com a devida qualificação de status.
3. O Módulo 5 (`description`) e o Módulo 6 (concisão) são pedagogicamente excelentes, com comparações "ruim vs. melhor" concretas.
4. O Módulo 10 (capability uplift × encoded preference) entrega ao docente um critério de decisão genuinamente útil e pouco óbvio.

### Principais fragilidades

1. Três módulos de teoria antes da primeira criação real.
2. O Módulo 8 ensina uma solução (`disable-model-invocation`) e a retira no mesmo módulo — o campo não funciona na superfície em que o curso opera.
3. Nenhum momento do curso mostra uma **saída** produzida por uma Skill, nem uma comparação antes/depois de resultado real.
4. Passos implícitos em atividades críticas: como desativar uma Skill (exigido no Módulo 9, nunca ensinado), como atualizar uma Skill já enviada (nunca abordado).
5. Ausência total de indicação de recursos visuais, num curso cujo momento decisivo é uma navegação de interface.

### Principal risco para o participante

**Travar no Módulo 4 e abandonar o curso.** É o único módulo que exige uma operação de interface real, e ele concentra simultaneamente: uma dependência de plano paga não confirmada, um caminho de menu declaradamente instável, uma operação de compactação com armadilha conhecida (compactar o arquivo em vez da pasta), uma armadilha de gravação no Bloco de Notas e uma estimativa de tempo irreal ("2 minutos"). Um docente que trave aqui não tem nenhum caminho alternativo oferecido, e perde o único momento em que o curso sai do plano conceitual.

### Principal oportunidade

**Antecipar a criação para o Módulo 1 usando uma Skill pronta.** O participante pode experimentar o efeito de uma Skill — pedindo um documento Word ou uma planilha, que acionam Skills prontas da Anthropic — antes de entender o que é uma Skill. Isso entrega a experiência primeiro e a explicação depois, invertendo a ordem atual e cumprindo o princípio declarado no próprio prompt de origem.

### Avaliação geral

## **BOM**

Material sólido, tecnicamente confiável e bem escrito, que ainda não é um curso executável de ponta a ponta por um iniciante sem apoio. As correções necessárias são estruturais, mas não exigem refazer o conteúdo: exigem reordenar, desmembrar e instrumentar.

---

## 2. Pontos Positivos — Fortalezas

### 2.1 As analogias fazem trabalho pedagógico real

Não são enfeite. A analogia do plano de aula para o professor substituto (Módulo 1) carrega três informações simultâneas: que a Skill é escrita por quem domina o procedimento, que ela é lida por quem não tem o contexto, e que os detalhes tácitos ("não comece pela definição de epistemologia") são justamente o conteúdo valioso.

**Princípio aplicado:** ancoragem em esquema mental preexistente. **Benefício ao iniciante:** o participante entende a *função* da Skill antes de ver qualquer sintaxe, o que reduz a ansiedade diante do arquivo técnico no Módulo 3.

A analogia das lombadas na estante (Módulo 2) é ainda melhor, porque explica os três níveis de carregamento de uma vez e sustenta o resto do curso — o Módulo 7 se apoia nela sem precisar reexplicar.

### 2.2 Honestidade sobre limites e riscos

O roteiro nunca apresenta a ferramenta como infalível. Diz que a Skill vai "funcionar em linhas gerais e errar nos detalhes" (Módulo 4). Diz que não sincroniza entre superfícies. Diz que Skills não estão cobertas por retenção zero de dados. Apresenta os estudos acadêmicos com a qualificação correta — "pesquisa recente sobre ecossistemas públicos, não veredito definitivo, e não avaliação do repositório oficial".

**Princípio de UX aplicado:** calibração de expectativa. **Benefício:** um docente que espera perfeição abandona na primeira falha; um docente avisado de que a primeira versão erra nos detalhes trata o erro como etapa, não como fracasso.

### 2.3 O Módulo 5 é o melhor do roteiro

A separação explícita entre os dois problemas — "o Claude escolheu a Skill certa?" e "depois de escolher, executou corretamente?" — é a distinção mais valiosa do curso inteiro, e ela é ensinada com clareza. A tabela de três casos docentes (rubrica, ABNT, plano de ensino), com coluna "fraca" e coluna "forte", permite ao participante ver o padrão e replicá-lo sem entender teoria nenhuma.

**Benefício:** este é o módulo que efetivamente distingue quem sai do curso sabendo fazer Skills que funcionam de quem sai sabendo fazer Skills que existem.

### 2.4 Ruim vs. melhor usado com disciplina

O padrão aparece nos Módulos 2, 5, 6, 7 e 8, sempre com os dois lados concretos e comparáveis, nunca com um contraexemplo caricato. O par do Módulo 6 (o parágrafo sobre rubricas inflado × "Atribua nota por critério antes da nota final") é particularmente eficaz porque o contraexemplo é plausível — é exatamente o que um docente escreveria.

### 2.5 O Módulo 10 entrega um critério, não uma informação

A distinção entre Skills de ampliação de capacidade e Skills de preferência codificada, seguida da conclusão de que "a maior parte das suas melhores Skills será do segundo tipo", dá ao participante uma **régua de decisão** aplicável a casos que o curso não cobriu. É o tipo de conteúdo que sobrevive ao curso.

### 2.6 Tom calibrado

Formal sem ser rígido, acessível sem ser condescendente. Não há infantilização, não há linguagem publicitária, e o humor — quando aparece — é discreto. Adequado a um público que é especialista em outra área e novato nesta.

---

## 3. Pontos Negativos e Gargalos — Debilidades

### Criticidade ALTA — impede execução ou compreensão

---

**A1. Três módulos de teoria antes da primeira criação real**

O prompt de origem determina experimentação no início. O roteiro entrega três módulos conceituais (1, 2, 3) e só cria no Módulo 4. As Pílulas dos três primeiros módulos não produzem resultado observável: a do Módulo 1 é uma reflexão em papel; a do Módulo 2 é uma pergunta cuja resposta pode ser uma lista vazia; a do Módulo 3 produz um arquivo que fica parado no disco.

**Impacto:** perda de engajamento na faixa em que a desistência é maior. O participante lê sobre uma coisa que ainda não viu funcionar.

---

**A2. O Módulo 8 ensina uma solução e a retira no mesmo módulo**

O módulo apresenta `disable-model-invocation: true` como a segunda correção para o problema "dispara demais", com exemplo de código e recomendação da Anthropic. Três parágrafos depois, um bloco de "Atenção" informa que o campo é extensão do Claude Code e que **incluí-lo faz o envio ao claude.ai falhar com erro**.

Ou seja: o curso ensina ao participante uma solução que, se ele aplicar na superfície onde o curso opera, **quebra a Skill dele**.

**Impacto:** é o defeito mais grave do roteiro. Um participante que leia rápido aplica o campo, o upload falha, e ele não tem como diagnosticar por quê. Fere diretamente a restrição do prompt de origem: "não invente recursos que a ferramenta não possua" — aqui o recurso existe, mas não onde o curso o coloca.

---

**A3. Nenhuma saída de Skill é mostrada em nenhum momento**

O curso inteiro trata de como escrever uma Skill. Em nenhum ponto ele exibe: uma resposta do Claude sem Skill, a mesma resposta com Skill, e a diferença entre as duas. O participante nunca vê o produto do que está construindo.

**Impacto:** compromete o objetivo central declarado no prompt de origem — desenvolver a capacidade de reconhecer "por que esta versão ficou melhor que a anterior". Sem material comparativo, essa capacidade não se desenvolve; ela é apenas descrita.

---

**A4. Passos implícitos em atividades obrigatórias**

Dois casos concretos:

- **Módulo 9, Pílula, passo 2:** "desative a Skill e faça um pedido típico". O curso nunca ensinou a desativar uma Skill. O participante não sabe onde fica esse controle nem se ele existe.
- **Módulo 4:** ensina a enviar uma Skill. Nunca ensina a **atualizar** uma Skill já enviada — e o curso inteiro depende de iteração (Módulos 6, 8, 9 pedem alterações). O participante refina o arquivo e não sabe como colocar a versão nova no ar.

**Impacto:** o Módulo 9, que é o módulo de avaliação e portanto o mais importante metodologicamente, é **inexecutável como escrito**.

---

**A5. Tempo declarado incompatível com a atividade no Módulo 4**

A Pílula do Módulo 4 diz "2 minutos — mais o tempo de upload". A atividade real compreende: escrever o `SKILL.md`, salvar com extensão correta, criar pasta, compactar, localizar a área de Skills nas configurações, enviar, abrir conversa nova, formular pedido e avaliar. Para um iniciante que nunca compactou uma pasta, isso é de 15 a 25 minutos.

**Impacto:** quebra de confiança no material. O participante que leva vinte minutos numa atividade anunciada como de dois conclui que o problema é ele.

---

**A6. Pré-requisito de acesso não verificado, com fonte contraditória**

A seção "Antes de Começar" afirma que a criação de Skills exige Pro, Max, Team ou Enterprise. O material-fonte contém as duas versões — uma incluindo o plano Free, outra excluindo. O roteiro adotou uma sem sinalizar a divergência.

**Impacto:** se a informação estiver errada para menos, o curso afasta participantes que poderiam fazê-lo. Se estiver errada para mais, participantes se inscrevem e travam no Módulo 4. Em ambos os casos, o dano ocorre no ponto mais frágil do percurso.

---

### Criticidade MÉDIA — prejudica a aprendizagem sem impedi-la

---

**M1. Referência para a frente no Módulo 6**

O ciclo de verificação do Módulo 6 usa o exemplo "seguindo o guia em `criterios.md`", mas arquivos de apoio só são apresentados no Módulo 7. O participante encontra uma construção que ainda não faz sentido.

---

**M2. `allowed-tools` aparece duas vezes como jargão puro**

O campo é citado nos Módulos 8 e 12 dentro da lista de campos aceitos pela especificação, sem nenhuma explicação. Num curso que se compromete a explicar todo termo técnico no momento em que surge, é uma quebra de contrato.

---

**M3. Densidade excessiva do Módulo 12 para o público declarado**

O módulo apresenta `context: fork`, injeção dinâmica de contexto, `.claude/commands/`, regras de precedência entre três níveis de instalação e a tabela de seis mecanismos. Para um público a quem o próprio módulo diz "para a maioria dos docentes, não é necessário", é informação demais.

---

**M4. Pílula do Módulo 2 pode produzir resultado vazio**

"Quais Skills você tem disponíveis agora?" pressupõe que haja Skills instaladas. Para um participante recém-chegado, a resposta pode ser vazia ou muito curta, e a atividade não demonstra nada. Falta um caminho alternativo.

---

**M5. Armadilha de codificação não sinalizada no Módulo 3**

O roteiro alerta corretamente sobre o Bloco de Notas gravar `SKILL.md.txt`, mas não menciona codificação de caracteres. Um arquivo em português com acentos gravado em codificação inadequada pode exibir caracteres corrompidos. Para um público brasileiro escrevendo em português, é uma armadilha provável.

---

**M6. O Módulo 11 pede ao docente uma auditoria que ele não tem meios de fazer**

A lista de conferência inclui "verifiquei se existe uma pasta `scripts/` e olhei o que há dentro". Um professor de Direito ou de Enfermagem olhando um script em Python não consegue avaliar se ele é malicioso. O roteiro reconhece isso em uma frase, mas mantém a lista como se ela fosse executável.

---

**M7. Não há carga horária declarada**

O curso não informa duração total nem por módulo. Um docente que precise encaixá-lo na agenda não tem como planejar.

---

### Criticidade BAIXA — clareza e acabamento

---

**B1.** O glossário não traz "acionamento" (ou *triggering*), termo usado sistematicamente do Módulo 5 em diante.

**B2.** O glossário não traz "superfície", termo estruturante usado nos Módulos 4 e 12.

**B3.** O Módulo 4 usa "unidades de texto (tokens)" e o Módulo 2 usa "tokens" direto — pequena inconsistência terminológica num roteiro que, no Módulo 6, prega consistência terminológica.

**B4.** O mapa do curso classifica os Módulos 1, 2 e 3 todos como "Entender", o que torna a coluna "fase da jornada" pouco informativa justamente no trecho mais longo de teoria.

**B5.** Não há indicação de tempo de leitura nem de esforço por módulo.

---

## 4. Matriz de Soluções e Melhorias

| Problema identificado | Criticidade | Impacto no aluno | Solução recomendada | Tipo de intervenção |
|---|---|---|---|---|
| **A1** Três módulos de teoria antes da primeira criação | Alta | Desengajamento na faixa de maior desistência | Criar um "Módulo 0 — Veja acontecer": pedir ao Claude a criação de um documento Word ou planilha, que aciona uma Skill pronta da Anthropic sem nenhuma instalação. O participante *usa* uma Skill nos primeiros cinco minutos e só depois descobre o nome do que usou | Reorganização + exercício novo |
| **A2** `disable-model-invocation` ensinado e depois invalidado | Alta | Participante aplica o campo e o upload falha, sem meio de diagnóstico | Remover o campo do Módulo 8. Substituir a solução por "estreitar a descrição" (que funciona em toda superfície) e mover o controle de invocação inteiro para o módulo de horizonte, apresentado como recurso exclusivo do Claude Code | Correção técnica + reorganização |
| **A3** Nenhuma saída de Skill exibida | Alta | Não desenvolve a alfabetização crítica que é o objetivo declarado do curso | Inserir uma seção "Antes e Depois" em pelo menos quatro aulas, com o texto real do pedido, a resposta sem Skill, a resposta com Skill e três perguntas dirigidas sobre o que mudou | Exemplo + exercício |
| **A4** Desativar e atualizar Skills nunca ensinados | Alta | Módulo 9 inexecutável; iteração impossível | Criar uma aula dedicada ao ciclo de vida da Skill: ativar, desativar, substituir por versão nova, excluir. Posicioná-la imediatamente após a primeira criação | Conceito adicional (aula nova) |
| **A5** "2 minutos" para atividade de 15–25 min | Alta | Quebra de confiança no material | Recalibrar todos os tempos. Desmembrar a atividade do Módulo 4 em três blocos cronometrados separadamente: preparar o arquivo, empacotar, enviar e testar | Reescrita |
| **A6** Plano exigido não verificado, fonte contraditória | Alta | Barreira de entrada incorreta em qualquer das direções | Reescrever o pré-requisito em formulação condicional, com instrução explícita de verificação na própria conta, e marcar com "Nota de versão". Acrescentar caminho alternativo para quem não tiver o plano: acompanhar as aulas escrevendo os arquivos, sem enviar | Correção técnica + reescrita |
| **M1** `criterios.md` citado antes de existirem arquivos de apoio | Média | Confusão momentânea | Trocar o exemplo do Módulo 6 por um que não dependa de arquivo externo, ou antecipar uma menção de uma linha | Reescrita |
| **M2** `allowed-tools` sem explicação | Média | Jargão não resolvido, quebra do contrato do curso | Explicar em uma frase no primeiro aparecimento: campo que pré-autoriza determinadas ferramentas durante a execução da Skill | Reescrita |
| **M3** Módulo 12 denso demais | Média | Sobrecarga no fechamento | Reduzir a três blocos: as três superfícies e sua não sincronização; Skill × MCP; critério de decisão sobre avançar. Recolher o restante para uma tabela-anexo marcada como consulta opcional | Reorganização |
| **M4** Pílula do Módulo 2 pode dar resultado vazio | Média | Atividade não demonstra o conceito | Acrescentar caminho alternativo: se a lista vier vazia, pedir um documento Word e observar o Claude anunciar o uso de uma Skill pronta | Exercício |
| **M5** Codificação de caracteres não sinalizada | Média | Acentuação corrompida sem causa aparente | Acrescentar instrução explícita de gravar em UTF-8 e o sintoma de quando não se grava | Correção técnica |
| **M6** Auditoria de scripts fora do alcance do público | Média | Falsa sensação de segurança ou paralisia | Reescrever a lista em dois níveis: verificações que qualquer docente faz sozinho (leitura do SKILL.md, coerência entre descrição e conteúdo, procedência) e um critério de corte explícito — havendo pasta `scripts/`, não instalar sem apoio técnico | Reescrita |
| **M7** Sem carga horária | Média | Impossível planejar | Declarar tempo estimado por aula e total no mapa do curso | Reescrita |
| **B1–B2** Glossário incompleto | Baixa | Consulta falha nos termos mais usados | Acrescentar "acionamento" e "superfície" | Reescrita |
| **B3** Inconsistência "token"/"unidade de texto" | Baixa | Ruído menor | Padronizar: definir "token" uma vez e usar o termo daí em diante | Reescrita |
| **B4** Coluna "fase da jornada" pouco informativa | Baixa | Mapa menos útil | Redistribuir as fases após a reorganização de A1 | Reorganização |
| **Geral** Nenhuma indicação visual em curso de interface | Alta | Navegação de menu explicada só por texto | Especificar recursos visuais aula a aula (detalhado na seção 5 e no roadmap) | Screenshot / GIF |

---

## 5. Análise das Pílulas Hands-on

Avaliação individual das doze atividades do Roteiro Base.

---

### Pílula 1 — Identificar o candidato a primeira Skill

| Aspecto | Avaliação |
|---|---|
| Objetivo | Reconhecer um procedimento repetitivo próprio |
| Dificuldade estimada | Baixa |
| Clareza | Alta |
| Tempo realista | 3–5 min (declarado: 2) |
| Conhecimento prévio exigido | Ter usado alguma IA antes — **e o curso declara não exigir isso** |
| Ponto provável de dificuldade | Participante que nunca usou IA não tem "instrução que já colei mais de duas vezes" e fica sem resposta |
| Melhoria recomendada | Oferecer alternativa: "se você nunca usou, pense numa instrução que você repete para monitores ou bolsistas a cada semestre" |

**Classificação: AJUSTAR**

---

### Pílula 2 — Perguntar quais Skills estão disponíveis

| Aspecto | Avaliação |
|---|---|
| Objetivo | Observar o Nível 1 do carregamento progressivo |
| Dificuldade estimada | Baixa |
| Clareza | Alta |
| Tempo realista | 2 min (adequado) |
| Conhecimento prévio exigido | Nenhum |
| Ponto provável de dificuldade | Resposta vazia ou genérica em conta sem Skills instaladas; a atividade não demonstra nada |
| Melhoria recomendada | Acrescentar segundo passo com resultado garantido: pedir "crie um documento Word com um resumo de uma página sobre X" e observar o anúncio de uso de Skill |

**Classificação: AJUSTAR**

---

### Pílula 3 — Escrever um SKILL.md no Bloco de Notas

| Aspecto | Avaliação |
|---|---|
| Objetivo | Produzir um arquivo válido sem instalar nada |
| Dificuldade estimada | Média |
| Clareza | Média |
| Tempo realista | 6–10 min (declarado: 2) |
| Conhecimento prévio exigido | Salvar arquivo com extensão específica — não trivial para o público |
| Ponto provável de dificuldade | Extensão `.txt` indevida (alertado), codificação de caracteres (**não alertado**), e o fato de o arquivo não produzir nenhum efeito observável |
| Melhoria recomendada | Acrescentar instrução de UTF-8 com o sintoma correspondente; encadear a atividade diretamente com a criação real, para que o arquivo tenha destino |

**Classificação: AJUSTAR**

---

### Pílula 4 — Subir a primeira Skill

| Aspecto | Avaliação |
|---|---|
| Objetivo | Colocar uma Skill no ar e vê-la acionar |
| Dificuldade estimada | **Alta** |
| Clareza | Média — os passos existem, mas concentram cinco operações distintas |
| Tempo realista | **15–25 min** (declarado: 2) |
| Conhecimento prévio exigido | Compactar pasta, navegar em configurações, gravar arquivo corretamente |
| Ponto provável de dificuldade | Este é **o** ponto de abandono do curso. Cinco falhas possíveis em sequência: extensão errada, codificação, ZIP do arquivo em vez da pasta, menu não localizado, plano insuficiente |
| Melhoria recomendada | Desmembrar em três atividades independentes, cada uma com critério de êxito próprio, e acrescentar solução de problemas para cada um dos cinco pontos de falha |

**Classificação: SUBSTITUIR**

**Atividade proposta em substituição — três blocos encadeados:**

- **4a. Preparar o arquivo (5 min).** Escrever o `SKILL.md`, gravar em UTF-8 dentro de uma pasta nomeada corretamente. *Êxito:* ao reabrir, o cabeçalho aparece entre as duas linhas de hifens e os acentos estão corretos.
- **4b. Empacotar (3 min).** Compactar a **pasta**. *Êxito:* ao abrir o ZIP, aparece uma pasta, e o `SKILL.md` está dentro dela — não solto na raiz.
- **4c. Enviar e acionar (7 min).** Enviar, abrir conversa nova, fazer um pedido sem citar o nome da Skill. *Êxito:* o Claude anuncia o uso da Skill e o formato da resposta corresponde ao especificado.

---

### Pílula 5 — Reescrever a descrição

| Aspecto | Avaliação |
|---|---|
| Objetivo | Garantir as duas metades da descrição e cobertura de vocabulário |
| Dificuldade estimada | Baixa |
| Clareza | Alta |
| Tempo realista | 4 min (declarado: 2) |
| Conhecimento prévio exigido | A Skill do módulo anterior |
| Ponto provável de dificuldade | O passo 3 pede três formulações alternativas; participantes tendem a produzir três variações da mesma frase, sem perceber |
| Melhoria recomendada | Instruir explicitamente que as três frases usem vocabulários distintos — uma formal, uma coloquial, uma abreviada |

**Classificação: MANTER** (com o ajuste acima)

---

### Pílula 6 — Enxugar o corpo

| Aspecto | Avaliação |
|---|---|
| Objetivo | Converter texto explicativo em procedimento acionável |
| Dificuldade estimada | Média |
| Clareza | Alta |
| Tempo realista | 5 min (declarado: 2) |
| Conhecimento prévio exigido | A Skill do Módulo 4 |
| Ponto provável de dificuldade | Sem um antes/depois de **resultado**, o participante enxuga o texto sem saber se melhorou |
| Melhoria recomendada | Fechar o ciclo: após enxugar, reenviar a Skill e comparar a saída com a da versão anterior |

**Classificação: AJUSTAR**

---

### Pílula 7 — Dividir em núcleo e apoio

| Aspecto | Avaliação |
|---|---|
| Objetivo | Aplicar carregamento progressivo à própria Skill |
| Dificuldade estimada | Média |
| Clareza | Alta — a marcação S/AV é um dispositivo eficaz |
| Tempo realista | 5 min (declarado: 2) |
| Conhecimento prévio exigido | Criar arquivo adicional na pasta |
| Ponto provável de dificuldade | Skills iniciantes costumam ser pequenas demais para justificar divisão; o exercício pode parecer artificial |
| Melhoria recomendada | Fornecer uma Skill inflada pronta, de propósito, para o participante dividir — em vez de exigir que ele divida a própria, que talvez não precise |

**Classificação: AJUSTAR**

---

### Pílula 8 — Provocar uma falha de acionamento

| Aspecto | Avaliação |
|---|---|
| Objetivo | Observar a distância entre linguagem real e descrição escrita |
| Dificuldade estimada | Baixa |
| Clareza | Alta |
| Tempo realista | 4 min (declarado: 2) |
| Conhecimento prévio exigido | Skill instalada e funcionando |
| Ponto provável de dificuldade | Nenhum relevante |
| Melhoria recomendada | Pedir registro escrito da palavra faltante, para alimentar a correção seguinte |

**Classificação: MANTER** — é a melhor atividade do roteiro. Provoca a falha deliberadamente, o que ensina mais que o sucesso.

---

### Pílula 9 — Comparar com e sem Skill

| Aspecto | Avaliação |
|---|---|
| Objetivo | Produzir evidência em vez de impressão |
| Dificuldade estimada | Média |
| Clareza | **Baixa** — o passo 2 exige uma operação nunca ensinada |
| Tempo realista | 8–10 min (declarado: 2) |
| Conhecimento prévio exigido | Desativar uma Skill — **não ensinado em lugar nenhum** |
| Ponto provável de dificuldade | O participante não encontra como desativar e abandona a atividade metodologicamente mais importante do curso |
| Melhoria recomendada | Ensinar o ciclo de vida antes; e oferecer alternativa que não dependa de desativação — comparar com o registro de uma resposta obtida antes de a Skill existir |

**Classificação: SUBSTITUIR**

**Atividade proposta em substituição:** antes de criar a Skill (na aula de criação), o participante registra a resposta do Claude ao pedido típico **sem** nenhuma Skill, e guarda o texto. Nesta aula, ele repete o mesmo pedido com a Skill ativa e compara contra o registro guardado, avaliando por três critérios escritos previamente. Elimina a dependência de desativar e ainda ensina a prática correta — estabelecer a linha de base *antes* de intervir.

---

### Pílula 10 — Montar a fila de Skills

| Aspecto | Avaliação |
|---|---|
| Objetivo | Priorizar o que vale virar Skill |
| Dificuldade estimada | Baixa |
| Clareza | Alta |
| Tempo realista | 5 min (declarado: 2) |
| Conhecimento prévio exigido | Nenhum |
| Ponto provável de dificuldade | A classificação AC/PC pode confundir; os exemplos do módulo ajudam, mas não há caso ambíguo trabalhado |
| Melhoria recomendada | Acrescentar um exemplo de caso limítrofe resolvido, mostrando o raciocínio de classificação |

**Classificação: MANTER** (com o acréscimo acima)

---

### Pílula 11 — Auditar a própria Skill como se fosse alheia

| Aspecto | Avaliação |
|---|---|
| Objetivo | Exercitar o olhar de auditoria |
| Dificuldade estimada | Baixa |
| Clareza | Média |
| Tempo realista | 4 min (declarado: 2) |
| Conhecimento prévio exigido | Nenhum — o que é justamente o problema |
| Ponto provável de dificuldade | A própria Skill do participante não contém scripts nem chamadas externas, então os itens mais importantes da lista não são exercitados. O exercício valida uma lista que nunca foi testada em material de risco |
| Melhoria recomendada | Fornecer duas Skills fictícias de exemplo — uma limpa e uma com sinal de alerta plantado (uma instrução que não corresponde à descrição, por exemplo) — e pedir que o participante identifique qual é qual |

**Classificação: SUBSTITUIR**

---

### Pílula 12 — Posicionar-se no mapa

| Aspecto | Avaliação |
|---|---|
| Objetivo | Decidir conscientemente sobre avançar para o Claude Code |
| Dificuldade estimada | Baixa |
| Clareza | Alta |
| Tempo realista | 2 min (adequado) |
| Conhecimento prévio exigido | Nenhum |
| Ponto provável de dificuldade | Nenhum |
| Melhoria recomendada | Nenhuma relevante. É uma atividade de fechamento honesta, que legitima a decisão de não avançar |

**Classificação: MANTER**

---

### Síntese das doze atividades

| Classificação | Quantidade | Pílulas |
|---|---|---|
| Manter | 4 | 5, 8, 10, 12 |
| Ajustar | 5 | 1, 2, 3, 6, 7 |
| Substituir | 3 | 4, 9, 11 |

**Observação transversal:** **onze das doze atividades declaram 2 minutos**, e o tempo realista médio é de aproximadamente 5. As três substituições concentram-se justamente nos momentos decisivos do percurso — a primeira criação, a avaliação e a auditoria.

---

## 6. Lacunas de Conteúdo

### 6.1 Essenciais — ausência compromete o uso básico

**E1. Ciclo de vida da Skill.** Ativar, desativar, substituir por versão nova, excluir. É pré-requisito de qualquer iteração, e o curso pede iteração desde o Módulo 6.

**E2. Solução de problemas de empacotamento.** O que fazer quando o envio falha. Os erros previsíveis são conhecidos e nomeáveis: estrutura de ZIP incorreta, cabeçalho malformado, campo não permitido pela especificação, nome fora das regras de validação. Nenhum é tratado.

**E3. Verificação do plano e caminho alternativo.** Como confirmar na própria conta se a criação de Skills está disponível, e o que fazer se não estiver. Sem isso, parte do público é surpreendida no meio do curso.

**E4. Um exemplo completo, do começo ao fim, com saída real.** Um caso único acompanhado do início ao fim — problema, primeira versão, saída insatisfatória, diagnóstico, correção, saída melhorada. O curso tem fragmentos de exemplo espalhados, mas nenhum percurso completo.

**E5. Codificação de caracteres.** Trivial de ensinar, cara de descobrir sozinho, e praticamente certa de ocorrer com um público escrevendo em português no Bloco de Notas.

---

### 6.2 Intermediárias — ampliam a autonomia

**I1. Onde a Skill termina e o pedido começa.** O curso não dá critério para decidir o que fica na Skill e o que continua sendo dito na conversa. É uma dúvida prática constante.

**I2. Quando dividir uma Skill em duas.** O Módulo 10 dá a regra do "sem 'e' no nome", mas não trabalha o caso concreto de uma Skill que cresceu e precisa ser desmembrada.

**I3. Trabalho com modelos e documentos anexos.** Como incluir na Skill o formulário institucional, a planilha-padrão, o modelo de parecer. Mencionado no Módulo 3 (pasta `templates/`) e nunca retomado — é justamente o caso de uso mais frequente na rotina docente.

**I4. Uso da ferramenta como parceira de crítica.** O Módulo 10 menciona em três linhas. Merece tratamento próprio: pedir crítica do resultado, pedir crítica da própria Skill, e a delimitação clara de que a decisão final é do docente.

**I5. Compartilhamento com colegas.** O curso informa que Skills no claude.ai são individuais, mas não ensina o procedimento prático de passar uma Skill adiante — que é simplesmente enviar o ZIP e orientar o colega a subi-lo.

---

### 6.3 Avançadas — horizonte legítimo

**A1. Skills com scripts.** Todo o eixo de operações determinísticas, validação automática e o padrão "planejar → validar → executar". Tecnicamente rico e fora do alcance do público-alvo declarado — deve permanecer como menção, não como conteúdo.

**A2. Avaliação automatizada com `skill-creator`.** O curso cita a ferramenta; a operação depende de ambiente que o público não usa. Manter como indicação.

**A3. Distribuição institucional.** Plugins, configurações gerenciadas, distribuição para um departamento inteiro. Interessa a coordenações e núcleos de apoio pedagógico, não ao docente individual.

**A4. Skills nas demais superfícies.** API e Claude Code em profundidade. Corretamente tratados como horizonte.

---

## 7. Roadmap de Expansão

### Nível 1 — Criando

Consolidar a capacidade de produzir uma Skill que funciona.

| Tópico | O que ensinar | Por que ensinar | Atividade prática sugerida |
|---|---|---|---|
| **Usar antes de entender** | Acionar uma Skill pronta pedindo um documento ou planilha | Entrega experiência antes de teoria e cumpre o princípio pedagógico declarado | Pedir um documento Word de uma página; observar o anúncio de uso de Skill; abrir o arquivo gerado |
| **Ciclo de vida** | Ativar, desativar, substituir, excluir | Pré-requisito de toda iteração posterior | Enviar uma Skill, alterar uma linha, reenviar, confirmar que a versão nova está no ar |
| **Empacotamento sem erro** | Estrutura correta do ZIP, gravação em UTF-8, regras de nome | Concentra as falhas de abandono | Empacotar, abrir o próprio ZIP e conferir a estrutura antes de enviar |
| **Primeira comparação** | Registrar a linha de base antes de criar a Skill | Instala desde cedo o hábito de decidir por evidência | Guardar a resposta sem Skill; comparar depois |

---

### Nível 2 — Refinando

Desenvolver o julgamento sobre qualidade.

| Tópico | O que ensinar | Por que ensinar | Atividade prática sugerida |
|---|---|---|---|
| **Diagnóstico de acionamento** | Distinguir falso negativo de falso positivo e tratar cada um | São problemas diferentes com correções diferentes; confundi-los leva à correção errada | Rodar cinco pedidos, classificar cada resultado nas duas categorias, corrigir a descrição uma vez e repetir |
| **Graus de liberdade** | Reconhecer quando prescrever e quando dar direção | Erro comum nos dois extremos: instrução engessada ou vaga demais | Pegar uma instrução própria e reescrevê-la nos dois extremos; observar qual produz melhor resultado e por quê |
| **Antes e depois de resultado** | Ler duas saídas e nomear a diferença | É a competência central declarada do curso e a que menos se desenvolve sozinha | Comparar duas saídas reais; nomear três diferenças concretas antes de qualquer explicação |
| **Modelos e anexos** | Incluir formulário, planilha ou modelo institucional na pasta | Caso de uso mais frequente da rotina docente, hoje ausente | Acrescentar um modelo real à Skill e instruí-la a preenchê-lo |

---

### Nível 3 — Construindo experiências

Passar de uma Skill isolada a um conjunto que sustenta um fluxo de trabalho.

| Tópico | O que ensinar | Por que ensinar | Atividade prática sugerida |
|---|---|---|---|
| **Conjunto coerente de Skills** | Decompor um fluxo em Skills de responsabilidade única | Skills abrangentes funcionam pior — constatação da própria Anthropic | Mapear o fluxo completo de uma disciplina e desenhar de duas a três Skills que o cubram sem sobreposição |
| **Ferramenta como parceira de crítica** | Pedir crítica do resultado e da própria Skill, mantendo a decisão com o docente | Amplia o uso sem transferir responsabilidade | Pedir ao Claude três fragilidades da própria Skill; decidir explicitamente quais acatar e registrar por quê |
| **Compartilhar com colegas** | Enviar o ZIP e orientar a instalação; coletar retorno de uso | Transforma trabalho individual em ativo do departamento | Entregar a Skill a um colega, observar o uso e anotar onde ele travou |
| **Manutenção ao longo do tempo** | Revalidar a Skill quando a ferramenta muda | O ecossistema muda rápido; Skills envelhecem em silêncio | Definir um gatilho de revisão e registrar a data da última validação dentro da própria Skill |

---

## 8. Recomendações Prioritárias

As dez intervenções mais importantes, em ordem de prioridade.

---

**1. Remover `disable-model-invocation` do módulo de diagnóstico**

- **Problema que resolve:** o curso ensina uma solução que quebra a Skill do participante na superfície em que ele trabalha (A2).
- **Impacto esperado:** elimina o único ponto do roteiro capaz de causar dano ativo. Substituir por "estreitar a descrição", que funciona em toda superfície, e deslocar o controle de invocação para o módulo de horizonte, claramente rotulado como exclusivo do Claude Code.
- **Esforço estimado:** Baixo

---

**2. Criar um módulo de abertura em que o participante usa uma Skill antes de saber o que é**

- **Problema que resolve:** três módulos de teoria antes da primeira prática (A1).
- **Impacto esperado:** o participante experimenta o efeito nos primeiros minutos, sem instalar nada, usando as Skills prontas da Anthropic. Reduz a desistência inicial e cumpre o princípio pedagógico declarado no prompt de origem.
- **Esforço estimado:** Médio

---

**3. Desmembrar a primeira criação em três atividades cronometradas, com solução de problemas**

- **Problema que resolve:** o ponto de abandono do curso, com cinco falhas possíveis em sequência e tempo declarado irreal (A5, Pílula 4).
- **Impacto esperado:** cada bloco tem critério de êxito próprio; quem trava sabe exatamente onde travou e encontra a correção ali mesmo.
- **Esforço estimado:** Médio

---

**4. Inserir uma aula de ciclo de vida logo após a primeira criação**

- **Problema que resolve:** ativar, desativar, substituir e excluir nunca são ensinados, o que torna o módulo de avaliação inexecutável (A4, E1).
- **Impacto esperado:** desbloqueia toda a iteração posterior. Sem isso, os módulos 6 a 9 pedem alterações que o participante não consegue colocar no ar.
- **Esforço estimado:** Baixo

---

**5. Acrescentar "Antes e Depois" com saídas reais em pelo menos quatro aulas**

- **Problema que resolve:** o curso nunca exibe o produto de uma Skill (A3).
- **Impacto esperado:** desenvolve a competência central declarada — reconhecer por que uma versão ficou melhor —, que hoje é apenas descrita. É a diferença entre um curso que informa e um curso que forma julgamento.
- **Esforço estimado:** Alto

---

**6. Reescrever o pré-requisito de plano em formulação verificável, com caminho alternativo**

- **Problema que resolve:** afirmação não confirmada, com fonte contraditória, no pré-requisito de acesso do curso inteiro (A6).
- **Impacto esperado:** ninguém é afastado indevidamente nem surpreendido no meio do percurso. Quem não tiver o plano acompanha escrevendo os arquivos, sem enviar.
- **Esforço estimado:** Baixo

---

**7. Especificar os recursos visuais aula a aula**

- **Problema que resolve:** ausência total de indicação visual num curso cujo momento decisivo é uma navegação de interface.
- **Impacto esperado:** substitui por imagem as explicações textuais mais frágeis. Prioridade nos quatro pontos críticos: a tela de Skills nas configurações, com o botão de envio destacado; a sequência de compactação da pasta, mostrando a estrutura correta dentro do ZIP; a comparação lado a lado de uma resposta com e sem Skill; e o `SKILL.md` aberto com cabeçalho e corpo visualmente separados. Nos três primeiros casos, sequência numerada de capturas; no segundo, um vídeo curto resolve melhor que qualquer texto.
- **Esforço estimado:** Alto

---

**8. Substituir a atividade de auditoria por um exercício de discriminação**

- **Problema que resolve:** o participante audita a própria Skill, que não contém nenhum dos riscos que a lista procura (Pílula 11, M6).
- **Impacto esperado:** duas Skills fictícias — uma limpa, uma com incoerência plantada entre descrição e conteúdo — tornam o exercício verificável e ensinam o sinal de alerta que um docente **consegue** reconhecer sozinho, sem exigir leitura de código.
- **Esforço estimado:** Médio

---

**9. Recalibrar todos os tempos e declarar a carga horária**

- **Problema que resolve:** onze das doze atividades declaram dois minutos; o tempo real médio é de cinco. O curso não informa duração total (A5, M7).
- **Impacto esperado:** restaura a confiança no material e torna o curso planejável na agenda docente.
- **Esforço estimado:** Baixo

---

**10. Ensinar a incluir modelos e documentos institucionais na Skill**

- **Problema que resolve:** o caso de uso mais frequente da rotina docente está ausente (I3).
- **Impacto esperado:** conecta o curso ao trabalho real. Formulário de plano de ensino, modelo de parecer, planilha de notas — é onde a Skill deixa de ser exercício e passa a economizar tempo de verdade.
- **Esforço estimado:** Médio

---

## Nota final de verificação

Três afirmações do Roteiro Base dependem de informação que muda com frequência e **devem ser reconferidas na ferramenta antes de qualquer publicação**:

1. **Planos em que a criação de Skills próprias está disponível.** O material-fonte é contraditório; o roteiro adotou uma das versões sem sinalizar.
2. **O caminho de menu para a área de Skills.** O roteiro já marca o ponto com "Nota de versão", o que é correto, mas o caminho precisa ser confirmado na interface vigente.
3. **A lista de campos de cabeçalho aceitos fora do Claude Code.** Seis campos são citados. Como incluir um campo indevido causa falha explícita no envio, um erro aqui trava o participante exatamente no módulo de maior risco.
