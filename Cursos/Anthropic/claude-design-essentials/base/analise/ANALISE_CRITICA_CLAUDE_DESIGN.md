# Análise Crítica 360° — Curso Claude Design
### Auditoria Pedagógica, Técnica e de UX

**Material analisado:** `roteiro-curso-claude-design.md` (11 módulos + mapa do curso + glossário, 520 linhas).
**Material de referência técnica usado para checagem de fatos:** `conteúdo bruto claude design.txt` (documentação oficial, tutoriais e relatos de uso real do Claude Design).
**Materiais não fornecidos para esta rodada de análise:** screenshots, GIFs, vídeos ou protótipos visuais do curso. Isso, por si só, já é o primeiro achado da auditoria — não existe hoje nenhum artefato visual associado a um curso sobre uma ferramenta 100% visual. O ponto é desenvolvido na Seção 3.

Todas as citações abaixo referenciam linhas do arquivo `roteiro-curso-claude-design.md`.

---

# 1. Sumário Executivo

O roteiro tem uma **espinha dorsal pedagógica sólida**: a progressão entender → criar → observar → modificar → refinar → aplicar é respeitada de verdade (não é só um rótulo), os módulos se referenciam uns aos outros de forma consistente (M11 recapitula M1–M10 nominalmente, linhas 455–462), e o curso evita com sucesso a armadilha mais comum desse tipo de material: virar um curso de engenharia de prompt disfarçado. Os pedidos ensinados são sempre curtos, na língua do professor, e o material ensina a dar **feedback específico** — uma habilidade transferível — em vez de "fórmulas mágicas" de prompt.

Ao mesmo tempo, a auditoria encontrou um padrão recorrente: **o roteiro descreve corretamente o "porquê" do design, mas presume conhecimento operacional da interface que um usuário completamente novato não tem.** Isso aparece de três formas concretas:

1. **Zero recursos visuais.** Um curso sobre uma ferramenta visual, ensinado inteiramente em texto corrido e tabelas markdown, sem nenhum screenshot, comparação de imagem ou GIF. As comparações "ruim vs. melhor" (M4, M5, M6) são descritas em palavras quando deveriam ser vistas.
2. **Lacunas de navegação no primeiro contato.** O Módulo 1 pede para "abrir o Claude Design e começar um novo projeto" (linha 83) sem nenhuma orientação sobre a tela inicial, escolha de template ou perguntas de esclarecimento que a ferramenta faz antes de gerar — todas documentadas e recorrentes no material de referência.
3. **Mecânica de comparação nunca explicada.** Cinco módulos (4, 5, 6, 8, 10) pedem explicitamente para o professor "comparar a versão antes e depois" — mas o roteiro nunca explica *como* ver a versão anterior depois que o Claude já atualizou a tela. Essa é a lacuna mais séria encontrada, porque ela mina o mecanismo pedagógico central do curso (observar → comparar → refinar), não um detalhe periférico.

Nenhum erro factual grave foi encontrado — o roteiro não afirma nada tecnicamente falso sobre o Claude Design. O risco está em **omissões que geram expectativas erradas** (tempo de geração, limites de uso, indisponibilidade mobile, ausência de geração de imagens) e não em informação incorreta.

**Resposta à pergunta-critério da auditoria:** *o aluno termina o curso sabendo pedir, ou sabendo decidir?* — O roteiro está desenhado, com sinceridade, para o segundo resultado: o checklist de observação (M2), os "seis ingredientes" (M3) e a regra do feedback específico (M8) são ferramentas de decisão, não scripts de prompt. O problema é que, hoje, um iniciante real corre risco de travar em pontos de navegação e mecânica de interface *antes* de chegar a exercitar esse raciocínio — o que compromete a entrega da promessa pedagógica não por falha de conceito, mas por falta de andaimes operacionais.

### Avaliação por dimensão

| Dimensão | Avaliação |
|---|---|
| Maturidade pedagógica (estrutura, progressão, analogias) | **Muito Bom** |
| Rigor técnico (precisão sobre a ferramenta) | **Regular** — sem erros, mas com omissões de risco |
| Qualidade do fluxo entre módulos | **Muito Bom** |
| UX do material como produto (formato, recursos visuais) | **Regular** — ausência total de imagens é um problema estrutural |
| Ensino de conceitos de design (não só de prompting) | **Bom** — forte, mas com uma lacuna nomeada (alinhamento) e uma ausente (acessibilidade) |
| **Avaliação geral** | **Bom** |

**Principal risco para a experiência do aluno:** um docente sem qualquer familiaridade com IA abre o Claude Design pela primeira vez no Módulo 1, encontra uma tela com opções de template e um sistema de design que o curso não prepara para explicar, e trava antes mesmo do primeiro rascunho — o que é exatamente o tipo de fricção que o curso foi desenhado para evitar.

**Principal oportunidade:** o roteiro já pensa como um bom instrutor. O que falta é pensar como um bom *produto* — adicionar os recursos visuais, avisos operacionais e mecânicas de comparação que transformam "teoria bem explicada" em "experiência que um iniciante conclui sozinho, sem travar."

---

# 2. Pontos Positivos — Fortalezas

**1. A progressão evita a armadilha do "curso de prompt engineering."**
O material nunca pede prompts longos ou "perfeitos". Os pedidos são sempre frases curtas e específicas ("aumente o contraste entre título e texto", linha 197) e o curso ensina a *qualidade do feedback* como habilidade central (M8, linha 348) usando uma analogia que o público-alvo já domina — corrigir atividades. Isso é exatamente o comportamento que a especificação pedagógica exige e que a maioria dos materiais concorrentes sobre ferramentas de IA erra, indo para o lado da "receita de prompt mágico". Beneficia diretamente o iniciante porque reduz a ansiedade da "página em branco": o aluno nunca precisa adivinhar uma fórmula, só descrever o que já sabe (seu conteúdo, seu público).

**2. Placeholders nos exemplos de prompt reduzem a barreira de entrada.**
Frases como `"Crie uma página simples de apresentação da minha disciplina [nome da disciplina], para alunos de [idade/série]..."` (linha 84) são preenchíveis, não precisam ser reescritas do zero. É uma técnica de scaffolding real (andaime cognitivo): o aluno adapta em vez de compor, o que é mensuravelmente mais fácil para quem nunca "conversou com uma IA" antes.

**3. O framework dos "Seis Ingredientes" (Módulo 3) é a decisão estrutural mais forte do curso.**
Nomear conteúdo, hierarquia, cores, tipografia, espaçamento e componentes como um vocabulário compartilhado dá ao aluno uma ferramenta de diagnóstico reutilizável: em vez de "não gostei", ele aprende a dizer "é hierarquia" ou "é espaçamento". Isso é precisamente o que separa um curso que ensina a *pedir* de um curso que ensina a *decidir* — e é a peça-chave que sustenta a resposta positiva à pergunta-critério desta auditoria.

**4. O checklist de observação do Módulo 2 antecede a ação, não a segue.**
Colocar "avaliação crítica" como o segundo módulo — antes de qualquer módulo de ajuste técnico — é uma escolha pedagógica correta e pouco comum: a maioria dos tutoriais desse tipo ensina a mexer primeiro e a avaliar depois (se é que ensina a avaliar). Isso constrói diretamente a capacidade que a especificação do curso pede: "não aceitar automaticamente a primeira versão".

**5. Cross-referencing consistente entre módulos.**
M2 é retomado explicitamente no M8 (linha 367), M1 e M10 são retomados no M11 (linhas 455–462), M3 anuncia corretamente que será aprofundado (linha 145). O curso se comporta como uma sequência coesa, não como 11 artigos independentes empacotados juntos — isso reduz a carga cognitiva de quem faz o curso em sessões espaçadas, porque cada módulo reancora o que veio antes.

**6. A explicação de código no Módulo 9 (linha 389) é um modelo de como lidar com o limite entre design e programação.**
"Você não precisa entender esse código para usar a ferramenta, da mesma forma que não precisa entender de motor para dirigir um carro" comunica exatamente o nível certo de abstração para o público — reconhece a existência do código sem transformar a aula em programação, e sem esconder a informação a ponto de criar mistério desnecessário.

**7. Terminologia técnica é introduzida com disciplina.**
"Canvas" (linha 20), "Tweaks" (linha 344), "sistema de design" (linha 313) e "design responsivo" (linha 424) são todos explicados imediatamente, entre parênteses ou em uma frase, no momento em que aparecem pela primeira vez — nenhum termo técnico é usado sem gloss. Esse é um padrão editorial correto e deve ser mantido como regra em qualquer expansão futura do curso.

---

# 3. Pontos Negativos e Gargalos — Debilidades

## Criticidade Alta

**3.1 — Nenhum recurso visual em um curso sobre uma ferramenta 100% visual.**
Do início ao fim, o roteiro é texto e tabelas markdown. As comparações "ruim vs. melhor" dos Módulos 4, 5 e 6 (linhas 187–189, 230–235, 270–274) descrevem em palavras uma diferença que deveria ser *vista* em menos de um segundo. Para um público que "precisa compreender primeiro o que está acontecendo na tela antes de receber explicações técnicas" (premissa do próprio curso), isso é uma contradição estrutural entre o método de ensino e o objetivo de aprendizagem.

**3.2 — Lacuna de navegação no primeiro contato com a ferramenta (Módulo 1, linha 83).**
"Abra o Claude Design e comece um novo projeto" presume que o aluno sabe localizar o botão, escolher entre os tipos de projeto disponíveis (protótipo, apresentação, documento, wireframe, animação) e decidir se configura um sistema de design antes ou depois. Nenhuma dessas decisões é preparada pelo curso. Esse é o primeiro passo do curso inteiro — se travar aqui, o aluno abandona antes do primeiro resultado visível, o que é o pior lugar possível para uma fricção de UX acontecer.

**3.3 — A mecânica de "comparar antes e depois" nunca é explicada, mas é usada como exercício-chave em 5 módulos.**
Linhas 206, 251, 288, 370 e 438 pedem, cada uma, para o aluno comparar a versão anterior com a nova. Mas o material de referência técnica confirma que preservar uma versão anterior exige uma ação deliberada — pedir ao Claude para "salvar o que temos e tentar uma abordagem diferente" antes de seguir adiante — e não é algo automático ou visualmente óbvio na tela. Como o próprio Módulo 8 só ensina esse comando de "salvar versão" (linha 361) depois que os Módulos 4, 5 e 6 já pediram comparações "antes/depois", existe uma dependência invertida: o curso pede uma habilidade no Módulo 4 que só é ensinada no Módulo 8. Isso não é um problema cosmético — é uma falha de sequenciamento que compromete o mecanismo pedagógico central do curso.

**3.4 — Ausência total de aviso sobre tempo real de geração e risco de perda de trabalho.**
O material de referência documenta explicitamente que a criação de um sistema de design ou de uma primeira página em alta fidelidade pode levar de 5 a 10 minutos, e alerta que fechar ou atualizar a aba durante esse processo **descarta o trabalho e obriga a recomeçar do zero**. O roteiro rotula suas atividades como "Mão na Massa (2 minutos)" sem qualificar que boa parte desse tempo é geração automática fora do controle do aluno, e nunca menciona o risco de fechar a aba. Um professor que feche a aba por impaciência ou distração perde o trabalho sem entender por quê — e sem o curso ter avisado que isso podia acontecer.

**3.5 — Nenhuma menção a limites de uso da ferramenta.**
O Claude Design consome a mesma cota de uso do plano Claude do aluno, e projetos com muitas iterações consomem mais. Um curso de 11 módulos com múltiplas rodadas de refinamento por módulo, culminando em um projeto final de 10–15 minutos, é exatamente o tipo de uso intensivo que pode esbarrar em limite de plano no meio da jornada — especialmente relevante para o público de escola pública, que provavelmente não tem plano corporativo com uso ampliado. Isso pode interromper a atividade sem que o aluno entenda a causa, uma falha de criticidade alta pela própria definição usada nesta auditoria ("problemas que podem impedir o aluno de executar a atividade").

**3.6 — Disponibilidade em dispositivo móvel não verificada, mas presumida.**
A especificação do curso exige atividades "possíveis em computador ou smartphone sempre que a funcionalidade utilizada permitir". O material de referência indica que o Claude Design está disponível apenas em navegador web e desktop, sem aplicativo móvel dedicado — o comportamento em navegador de celular não está documentado como equivalente. O roteiro não verifica nem sinaliza essa restrição em nenhum lugar, incluindo a seção "Antes de Começar" (linhas 16–20), que seria o local correto para isso.

## Criticidade Média

**3.7 — Módulos 2 e 3, em sequência, não envolvem nenhuma interação com o Claude Design.**
Logo depois da primeira criação (Módulo 1), o aluno passa por dois módulos inteiros (linhas 90–167) sem tocar na ferramenta novamente. Pedagogicamente cada um se justifica isoladamente (observar antes de agir; mapear conceitos antes de praticar), mas em sequência criam um intervalo longo sem retorno visual — arriscado justamente no momento em que o engajamento inicial é mais frágil.

**3.8 — Conceito de "alinhamento" nunca é nomeado.**
Os seis ingredientes do Módulo 3 (linhas 147–154) cobrem conteúdo, hierarquia, cores, tipografia, espaçamento e componentes, mas alinhamento — um dos pilares clássicos de design visual e citado explicitamente na especificação desta auditoria — não aparece como conceito nomeado em nenhum módulo. Parte da intuição de alinhamento é absorvida implicitamente por "espaçamento" e "hierarquia", mas nunca é ensinada como habilidade própria (ex.: elementos desalinhados mesmo com espaçamento correto).

**3.9 — Acessibilidade não é mencionada em nenhum momento do curso.**
A palavra "acessibilidade" não aparece nas 520 linhas do roteiro. O Módulo 5 chega perto (contraste para legibilidade, linha 245) mas trata isso como conforto de leitura, não como requisito de acessibilidade (contraste mínimo, texto alternativo, tamanho de fonte para baixa visão, paletas seguras para daltonismo). Em contexto de escola pública, com turmas heterogêneas, essa é uma lacuna de conteúdo relevante e de fácil correção, já que o Claude pode literalmente ser instruído a "avaliar a acessibilidade e o contraste desta página" — um recurso real da ferramenta que o curso nunca menciona.

**3.10 — Bug conhecido de comentários não é mencionado.**
O Módulo 8 ensina "comentário direto no elemento" como um dos três métodos de refinamento (linha 343) sem mencionar que essa funcionalidade tem uma falha intermitente documentada (comentários que ocasionalmente não são registrados) e um workaround simples e conhecido (colar o comentário no chat). Sem esse aviso, um professor que usar esse método e não ver reação pode concluir, erroneamente, que fez algo errado ou que a ferramenta travou.

**3.11 — Exemplos genéricos demais em quatro módulos consecutivos.**
Módulos 4, 5, 6 e 8 (linhas 203, 249, 286, 367) referenciam "sua página" de forma genérica, sem ancorar em um cenário escolar concreto e novo a cada módulo — diferente de M1 (apresentação de disciplina), M7 (cards de tópicos) e M9 (pergunta com resposta escondida), que têm cenário próprio. Isso é uma oportunidade perdida de reforçar aplicabilidade educacional a cada módulo, especialmente porque a especificação do curso pede variedade de contextos escolares.

**3.12 — Estimativa de tempo do projeto final provavelmente otimista.**
"10 a 15 minutos" (linha 485) para um projeto completo de alta fidelidade com dois refinamentos não parece contabilizar o tempo real de geração da IA (5–10 minutos só na primeira geração, segundo o material de referência), o que deixaria pouquíssimo tempo para as duas rodadas de refinamento pedidas.

## Criticidade Baixa

**3.13 — Três tipos de callout (prompt para copiar, aviso, conceito essencial) usam o mesmo estilo visual de bloco de citação.**
Linhas como 79, 124, 193 e 245 usam a mesma formatação markdown (`>`) para funções semanticamente diferentes: um prompt para copiar, uma nota de cautela e uma definição de conceito. Em markdown puro isso é aceitável, mas prejudica a leitura rápida e precisa ser resolvido antes da conversão para Word (cores ou ícones diferentes por tipo de callout).

**3.14 — O Módulo 2 não produz nenhuma mudança visível na tela.**
É o único módulo cujo "Mão na Massa" não gera nenhum resultado visual perceptível (linhas 126–130) — o exercício é inteiramente reflexivo e escrito. Isso é defensável dado o objetivo do módulo (observar, não agir), mas quebra a promessa geral da especificação de que toda pílula hands-on deve "produzir um resultado visível rapidamente".

**3.15 — A seção "Antes de Começar" não menciona a necessidade de uma conta Claude.ai.**
Presume, implicitamente, que o aluno já tem login e sabe acessar `claude.ai/design` (linha 18). Para o público-alvo declarado ("pode nunca ter utilizado ferramentas de IA"), isso é uma lacuna pequena, mas real.

---

# 4. Matriz de Soluções e Melhorias

| Problema identificado | Criticidade | Impacto no aluno | Solução recomendada | Tipo de intervenção |
|---|---|---|---|---|
| M1 não orienta a navegação inicial (linha 83) | Alta | Pode travar antes do primeiro resultado | Adicionar, logo após a linha 83, um screenshot numerado da tela inicial do Claude Design com callouts apontando: campo de prompt, seletor de template, botão "começar em branco" | Screenshot |
| Comparação "antes/depois" nunca explicada mecanicamente, usada em 5 módulos (linhas 206, 251, 288, 370, 438) | Alta | Exercício-chave pode falhar por falta de instrução operacional | Mover a explicação de "salvar versão antes de mudar" do Módulo 8 (linha 361) para uma caixa de destaque no Módulo 1 ou na seção "Antes de Começar", com instrução explícita de like "peça para o Claude salvar esta versão antes de pedir a próxima mudança, assim você pode comparar depois" | Reescrita + reorganização |
| Nenhuma comparação visual real nas tabelas "ruim vs. melhor" (linhas 187–189, 230–235, 270–274) | Alta | Conceito abstrato demais para quem "precisa ver antes de entender" | Substituir cada tabela textual por um par de screenshots lado a lado (mesma página, uma sem o ajuste e outra com), mantendo a legenda "Sem hierarquia / Com hierarquia" etc. como título da imagem | Screenshot / comparação lado a lado |
| Sem aviso de tempo de geração nem do risco de fechar a aba | Alta | Perda de trabalho sem entender a causa; frustração e possível abandono | Adicionar, na seção "Antes de Começar" e reforçado no Módulo 1: "A primeira geração pode levar de 5 a 10 minutos. Não feche nem atualize a aba enquanto isso acontece — você perderia o trabalho e teria que recomeçar." | Reescrita (conceito adicional) |
| Sem menção a limites de uso do plano | Alta | Atividade pode ser interrompida sem explicação no meio do curso | Adicionar uma nota curta em "Antes de Começar": o Claude Design usa a mesma cota do seu plano Claude; se atingir o limite, é possível continuar aguardando o próximo ciclo ou verificando o uso na conta | Conceito adicional |
| Disponibilidade mobile não verificada nem sinalizada | Alta | Professor tenta pelo celular e tem experiência quebrada | Verificar o comportamento atual em navegador mobile antes da próxima turma; até lá, declarar explicitamente em "Antes de Começar" que o uso recomendado é em computador | Correção técnica |
| Nenhuma orientação para as perguntas de esclarecimento que o Claude faz antes de gerar | Média/Alta | Aluno não sabe o que fazer ao ver uma tela de perguntas não descrita no curso | Adicionar ao passo 2 do Mão na Massa do Módulo 1 (linha 84): "O Claude pode responder com perguntas sobre estilo, tom ou formato antes de gerar — é normal, responda com uma frase curta cada" + screenshot de exemplo | Screenshot + reescrita |
| Dois módulos consecutivos (2 e 3) sem interação com a ferramenta (linhas 90–167) | Média | Risco de queda de engajamento logo após a primeira criação | Adicionar ao Módulo 2 um micro-passo opcional de interação (ex.: pedir ao Claude "o que você acha que está confuso nesta página?" e comparar com a própria avaliação do aluno) | Exercício adicional |
| Acessibilidade ausente do curso | Média | Lacuna de conteúdo relevante para contexto de escola pública | Adicionar um bloco no Módulo 5 ensinando a pedir diretamente "avalie a acessibilidade e o contraste desta página" como parte do "Como pedir ao Claude" | Conceito adicional |
| Bug conhecido de comentários não mencionado | Média | Professor pode achar que "quebrou algo" ao usar comentário direto | Adicionar nota no Módulo 8, junto à explicação do método 2 (linha 343): "Se o comentário não parecer ter efeito, cole o mesmo texto no chat — é um problema conhecido da versão beta" | Reescrita |
| Alinhamento não é nomeado como conceito | Média | Lacuna conceitual em relação a fundamentos de design | Adicionar "Alinhamento" como observação dentro do Módulo 6 (espaçamento), com uma frase e um exemplo de pedido: "alinhe estes elementos à mesma margem esquerda" | Conceito adicional |
| Exemplos genéricos ("sua página") em M4, M5, M6, M8 (linhas 203, 249, 286, 367) | Média | Menor reforço de aplicabilidade educacional a cada módulo | Ancorar cada hands-on em um cenário escolar específico e diferente (ex.: M6 = "seu cronograma de provas está lotado"; M8 = "o cabeçalho do seu painel de projeto") | Reescrita |
| Estimativa de tempo do projeto final (linha 485) | Média | Expectativa de tempo irreal para o exercício mais complexo do curso | Ajustar para "15 a 20 minutos, considerando o tempo de geração da IA" e dividir em checkpoints (5 min descrever, 5–10 min aguardar geração, 5 min refinar) | Reescrita |
| Três tipos de callout com a mesma formatação visual (linhas 79, 124, 193, 245) | Baixa | Leitura rápida prejudicada; problema maior na conversão para Word | Definir três estilos de caixa de destaque distintos: azul para "experimente pedir", amarelo para "nota honesta/aviso", verde para "conceito essencial" | Melhoria visual |
| Mão na Massa do M2 não gera resultado visível (linhas 126–130) | Baixa | Descumpre a promessa geral de "resultado visível rápido" | Adicionar um passo 4 opcional: "Se quiser, peça ao Claude para aplicar só o ajuste mais urgente que você identificou, e guarde o antes/depois para o Módulo 8" | Exercício adicional |
| "Antes de Começar" não menciona conta Claude.ai | Baixa | Pequena fricção de entrada para usuário 100% novato | Adicionar uma linha: "Você vai precisar de uma conta gratuita em claude.ai — se ainda não tiver, crie antes de começar" | Reescrita |
| Ausência de recurso de referência visual (upload de print/foto) como técnica de ensino | Média | Oportunidade perdida para público sem vocabulário de design | Adicionar no Módulo 1 ou 5 uma menção a "se você tiver uma foto de um mural ou site que gosta, pode anexá-la e pedir 'algo parecido com isso'" | Conceito adicional |

---

# 5. Análise das Pílulas Hands-on

Para cada módulo: objetivo, dificuldade estimada, clareza, tempo realista, conhecimento prévio exigido, ponto provável de dificuldade, melhoria recomendada e classificação final.

### Módulo 1 — Primeira página
- **Objetivo:** gerar o primeiro rascunho visual a partir de uma descrição.
- **Dificuldade estimada:** Baixa em conceito, Média em execução (por causa da navegação inicial).
- **Clareza das instruções:** boa na frase de prompt (preenchível), fraca na navegação prévia ("abra e comece um novo projeto").
- **Tempo realista:** 2 minutos para escrever o pedido + 3 a 10 minutos de espera não contabilizados no rótulo do exercício.
- **Conhecimento prévio exigido:** login em claude.ai; noção de onde fica o botão de novo projeto — nenhum dos dois é ensinado antes.
- **Ponto provável de dificuldade:** tela inicial com opções de template e sistema de design não descritas pelo curso.
- **Melhoria recomendada:** screenshot numerado da tela inicial + aviso de tempo de geração (ver Matriz, itens 1 e 4).
- **Classificação: Ajustar.**

### Módulo 2 — Checklist de observação
- **Objetivo:** desenvolver avaliação crítica antes de agir.
- **Dificuldade estimada:** Baixa.
- **Clareza das instruções:** alta — perguntas objetivas, passo a passo simples.
- **Tempo realista:** 2 minutos é realista para esta atividade especificamente (é a única totalmente desconectada do tempo de geração da IA).
- **Conhecimento prévio exigido:** nenhum além do resultado do Módulo 1.
- **Ponto provável de dificuldade:** nenhum funcional; o risco é de engajamento, não de execução (não produz mudança visível).
- **Melhoria recomendada:** manter o checklist como está; considerar o passo 4 opcional sugerido na Matriz para gerar uma pequena mudança visível.
- **Classificação: Ajustar** (ajuste leve, o núcleo do exercício está correto).

### Módulo 3 — Seis ingredientes
- **Objetivo:** reconhecer os componentes de qualquer design em exemplos do cotidiano.
- **Dificuldade estimada:** Baixa.
- **Clareza das instruções:** alta.
- **Tempo realista:** 2 minutos é factível — é observação de algo que já existe, sem espera de geração.
- **Conhecimento prévio exigido:** nenhum.
- **Ponto provável de dificuldade:** nenhum identificado.
- **Melhoria recomendada:** nenhuma estrutural; opcionalmente adicionar um exemplo pré-selecionado (ex.: "se preferir, use o site da sua secretaria de educação") para quem trava na escolha do próprio exemplo.
- **Classificação: Manter.**

### Módulo 4 — Hierarquia visual
- **Objetivo:** aplicar contraste de tamanho/peso para guiar o olhar.
- **Dificuldade estimada:** Baixa em conceito, Média em execução por causa da comparação antes/depois não instruída.
- **Clareza das instruções:** alta no pedido de prompt; ambígua no "compare antes e depois" (item 3.3).
- **Tempo realista:** 2 minutos de digitação + tempo de geração da edição (normalmente mais rápido que a primeira geração, mas não é dito no curso).
- **Conhecimento prévio exigido:** ter completado o Módulo 1.
- **Ponto provável de dificuldade:** não saber como recuperar a versão "antes" para comparar.
- **Melhoria recomendada:** aplicar a correção da Matriz sobre mecânica de comparação; considerar sugerir "tire um print antes de pedir a mudança" como solução simples e imediata, sem depender de nenhuma funcionalidade específica da ferramenta.
- **Classificação: Ajustar.**

### Módulo 5 — Cores e tipografia
- **Objetivo:** melhorar legibilidade e tom via cor e fonte.
- **Dificuldade estimada:** Baixa.
- **Clareza das instruções:** alta.
- **Tempo realista:** realista, mesma ressalva de tempo de geração do Módulo 4.
- **Conhecimento prévio exigido:** Módulo 1 completo.
- **Ponto provável de dificuldade:** mesmo problema de comparação antes/depois do Módulo 4.
- **Melhoria recomendada:** incluir a sugestão de pedir avaliação de acessibilidade/contraste diretamente ao Claude, em vez de depender só de "leia em voz alta" (linha 245).
- **Classificação: Ajustar.**

### Módulo 6 — Espaçamento
- **Objetivo:** identificar e corrigir aglomeração visual.
- **Dificuldade estimada:** Baixa.
- **Clareza das instruções:** boa, mas o "veja se ficou mais fácil de escanear" (linha 288) é mais fraco como critério de sucesso do que o "compare antes e depois" explícito de outros módulos.
- **Tempo realista:** realista.
- **Conhecimento prévio exigido:** Módulo 1 completo.
- **Ponto provável de dificuldade:** identificar sozinho qual seção está "apertada" sem um exemplo visual de referência do que conta como apertado.
- **Melhoria recomendada:** trocar o critério de sucesso do passo 3 por uma comparação explícita antes/depois, igual aos Módulos 4 e 5, para manter consistência de padrão entre módulos.
- **Classificação: Ajustar.**

### Módulo 7 — Componentes (cards)
- **Objetivo:** organizar uma lista de tópicos em cards consistentes.
- **Dificuldade estimada:** Baixa.
- **Clareza das instruções:** alta — pedido de prompt bem definido, com placeholder de lista.
- **Tempo realista:** realista.
- **Conhecimento prévio exigido:** nenhum module anterior estritamente necessário (funciona até como exercício isolado).
- **Ponto provável de dificuldade:** nenhum relevante identificado.
- **Melhoria recomendada:** nenhuma estrutural necessária.
- **Classificação: Manter.**

### Módulo 8 — Ciclo de refinamento
- **Objetivo:** praticar as três formas de dar feedback e a regra do feedback específico.
- **Dificuldade estimada:** Média — é o módulo com mais conceitos operacionais simultâneos (chat, comentário, Tweaks).
- **Clareza das instruções:** boa na regra de ouro do feedback; fraca na localização física dos três métodos na tela.
- **Tempo realista:** realista para a parte de digitação; a expectativa de "rodada única" pode não se sustentar sem apoio visual de onde clicar.
- **Conhecimento prévio exigido:** Módulo 2 (reaproveita a frase escrita lá).
- **Ponto provável de dificuldade:** não encontrar onde fica o painel de Tweaks ou como comentar diretamente em um elemento; possível confusão com o bug de comentários não mencionado (item 3.10).
- **Melhoria recomendada:** screenshot com os três métodos numerados na interface real + nota sobre o bug de comentários.
- **Classificação: Ajustar.**

### Módulo 9 — Interatividade
- **Objetivo:** criar um elemento que reage a clique.
- **Dificuldade estimada:** Baixa em conceito, Média em execução.
- **Clareza das instruções:** boa — inclui até o passo de testar o resultado (linha 401), o que é uma prática melhor que a maioria dos outros módulos.
- **Tempo realista:** depende do tempo de geração da edição, não contabilizado.
- **Conhecimento prévio exigido:** Módulo 1 completo.
- **Ponto provável de dificuldade:** não ficar claro se o clique deve ser testado no modo de edição ou em um modo de "apresentação/preview" separado — a distinção não é feita pelo curso.
- **Melhoria recomendada:** um GIF curto mostrando o clique revelando o conteúdo escondido resolveria esse módulo inteiro de uma vez — é o caso mais forte de todo o curso para esse tipo de recurso, porque o próprio conceito ensinado é movimento/interação, algo que texto estático não consegue transmitir.
- **Classificação: Ajustar.**

### Módulo 10 — Adaptação de público
- **Objetivo:** adaptar uma página existente para outro público ou dispositivo.
- **Dificuldade estimada:** Baixa.
- **Clareza das instruções:** alta, inclusive com nota de cautela sobre simplificação excessiva (linha 432) — um dos melhores momentos de pensamento crítico do curso.
- **Tempo realista:** realista, mesma ressalva de tempo de geração.
- **Conhecimento prévio exigido:** qualquer página de módulo anterior.
- **Ponto provável de dificuldade:** nenhum crítico identificado.
- **Melhoria recomendada:** nenhuma estrutural; um screenshot comparando as duas versões lado a lado potencializaria o exercício, mas não é bloqueante.
- **Classificação: Manter.**

### Módulo 11 — Projeto final (capstone)
- **Objetivo:** aplicar o ciclo completo em um material real.
- **Dificuldade estimada:** Média-Alta — é o exercício mais longo e com mais decisões encadeadas do curso.
- **Clareza das instruções:** boa na estrutura de passos; a estimativa de tempo é o problema central (item 3.12).
- **Tempo realista:** provavelmente 15 a 25 minutos reais, não 10 a 15.
- **Conhecimento prévio exigido:** todos os módulos anteriores — é o único exercício verdadeiramente cumulativo, o que é correto para um capstone.
- **Ponto provável de dificuldade:** subestimar o tempo necessário e desistir no meio por achar que "está demorando demais" (agravado pela falta de aviso sobre tempo de geração, item 3.4).
- **Melhoria recomendada:** ajustar tempo para 15–20 minutos com checkpoints explícitos; adicionar um passo final de reflexão comparando o resultado com a página do Módulo 1, criando um momento de fechamento emocional que hoje não existe.
- **Classificação: Ajustar.**

**Observação geral desta seção:** nenhuma das 11 atividades precisa ser **substituída**. Todas têm um núcleo pedagógico correto — o problema nunca é "o exercício errado", é "o exercício certo com apoio operacional insuficiente". Isso é, em si, um sinal positivo sobre a qualidade do desenho instrucional de base.

---

# 6. Lacunas de Conteúdo

## Lacunas essenciais
*(sem isso, o aluno arrisca não conseguir concluir o curso sozinho)*

- Orientação de navegação da tela inicial do Claude Design (novo projeto, tipos de template, opção de começar em branco).
- Como responder às perguntas de esclarecimento que a ferramenta faz antes de gerar (hoje só mencionado conceitualmente no Módulo 1, nunca praticado).
- Aviso de tempo real de geração e o risco de perda de trabalho ao fechar a aba durante a criação.
- Mecânica explícita de como preservar e comparar uma versão anterior — hoje pressuposta em cinco módulos e ensinada só no Módulo 8.
- Aviso sobre limites de uso do plano Claude.
- Verificação e comunicação clara sobre disponibilidade em dispositivos móveis.

## Lacunas intermediárias
*(ampliam significativamente a autonomia do aluno, mas não impedem a conclusão do curso)*

- Anexar referências visuais (fotos, prints, moodboards) como atalho para quem não tem vocabulário de design — recurso real da ferramenta, citado no material de referência, nunca mencionado no curso.
- Upload de documentos já existentes (planos de aula em Word, slides em PowerPoint) para gerar a página a partir de material que o professor já produziu, em vez de descrever tudo do zero em texto.
- Pedir diretamente ao Claude para avaliar acessibilidade e contraste da página.
- Conceito de alinhamento como habilidade nomeada.
- Bug conhecido de comentários que somem e o workaround de colar no chat.
- Como localizar e reabrir um projeto já iniciado em uma sessão anterior (nenhum módulo ensina a "voltar" a um projeto salvo).

## Lacunas avançadas
*(demonstram potencial maior da ferramenta; não necessárias para uma introdução, mas valiosas para uma segunda etapa do curso)*

- Estados de interface (selecionado, correto/errado, carregando) aplicados a quizzes e atividades interativas.
- Fluxos de várias telas (ex.: uma sequência de onboarding de estudante em 3–4 passos).
- Conexão com Google Drive ou documentos vivos como fonte de conteúdo.
- Visualizações de dados simples (gráfico de desempenho de turma, cronograma com dados reais).
- Handoff para Claude Code, para o caso raro de um material precisar virar um site mantido por terceiros (ex.: TI da escola).
- Ditado por voz como alternativa de entrada para professores menos confortáveis digitando descrições longas.

---

# 7. Roadmap de Expansão — Explorando o Potencial

## Nível 1 — Criando
*Já amplamente coberto pelos Módulos 1, 3, 4, 5, 6 e 7 do curso atual. Recomendações de reforço:*

- **O que ensinar:** navegação da tela inicial e resposta às perguntas de esclarecimento do Claude.
  **Por que ensinar:** é o maior ponto de fricção identificado nesta auditoria (item 3.2) e antecede todo o resto do curso.
  **Atividade prática:** um "tour guiado" de 2 minutos pela tela inicial antes do primeiro prompt, com screenshot numerado.

- **O que ensinar:** anexar uma referência visual (foto de um mural, print de um site) junto ao pedido em texto.
  **Por que ensinar:** reduz a dependência de vocabulário de design para descrever estilo — mostrar substitui descrever.
  **Atividade prática:** tirar uma foto de um material físico já usado em sala (cartaz, mural) e pedir ao Claude "crie algo no mesmo espírito visual disso, mas para [novo conteúdo]".

## Nível 2 — Refinando
*Parcialmente coberto pelos Módulos 2, 8 e 10. Recomendações de reforço e expansão:*

- **O que ensinar:** acessibilidade prática (contraste mínimo, tamanho de fonte, pedir auditoria diretamente ao Claude).
  **Por que ensinar:** turmas de escola pública são heterogêneas; acessibilidade não é luxo de design profissional, é requisito pedagógico.
  **Atividade prática:** pedir ao Claude "avalie esta página em termos de acessibilidade e contraste, e liste o que poderia melhorar" e comparar a lista com a percepção própria do professor.

- **O que ensinar:** comparação de versões como hábito (salvar antes de mudar, nomear versões).
  **Por que ensinar:** é o alicerce mecânico que faltava para toda a lógica de "observar e refinar" do curso atual.
  **Atividade prática:** pedir explicitamente para o Claude "salvar esta versão" antes de cada rodada de ajuste ao longo de um mini-projeto de 3 iterações, e ao final revisar as três versões lado a lado.

- **O que ensinar:** consistência entre múltiplas páginas de um mesmo projeto (ex.: página de disciplina + página de atividade usando o mesmo estilo).
  **Por que ensinar:** professores frequentemente precisam de mais de uma peça visual coerente entre si (ex.: cronograma + página de disciplina + material para família).
  **Atividade prática:** criar duas páginas diferentes pedindo explicitamente para "manter o mesmo estilo visual da página anterior".

## Nível 3 — Construindo experiências
*Praticamente ausente do curso atual — é onde a maior expansão de conteúdo deve acontecer.*

- **O que ensinar:** construção de um quiz interativo simples de revisão (pergunta, alternativas, feedback de certo/errado).
  **Por que ensinar:** o Módulo 9 já cita "quiz" como exemplo (linha 385), mas nunca chega a construir um — é a extensão natural e mais desejada do conceito de interatividade já introduzido.
  **Atividade prática:** transformar 3 perguntas de uma prova em um quiz clicável com feedback imediato.

- **O que ensinar:** painel de acompanhamento simples (dashboard) com dados reais de turma (frequência, entregas, notas por categoria).
  **Por que ensinar:** já está na lista de exemplos do Módulo 11 (linha 479) como ideia, mas nunca é ensinado como habilidade — dashboards exigem pensar em hierarquia de dados, não só de texto.
  **Atividade prática:** transformar uma planilha simples de acompanhamento em um painel visual com cards de resumo.

- **O que ensinar:** infográfico de dados de um projeto interdisciplinar ou feira de ciências.
  **Por que ensinar:** combina tudo que o curso já ensina (hierarquia, cor, componentes) com uma habilidade nova — representar números e comparações visualmente, não só texto.
  **Atividade prática:** transformar os resultados de uma pesquisa simples feita com a turma (ex.: enquete de preferências) em um infográfico de uma página.

- **O que ensinar:** fluxo de várias telas para um material de orientação de estudantes (ex.: 3 telas — regras, cronograma, contato).
  **Por que ensinar:** introduz a ideia de "experiência" (mais de uma tela conectada), não apenas "página única", preparando o aluno para pensar em jornada, não só em layout.
  **Atividade prática:** criar uma sequência de 3 telas conectadas por botões de "próximo".

- **O que ensinar:** biblioteca pessoal de componentes reutilizáveis (o mesmo card ou cabeçalho usado em vários projetos ao longo do ano letivo).
  **Por que ensinar:** conecta diretamente ao conceito de "sistema de design" já mencionado en passant no Módulo 7 (linha 313), tornando-o prático em vez de apenas nomeado.
  **Atividade prática:** revisitar um card criado semanas antes e pedir para "usar este mesmo estilo de card" em um novo projeto.

---

# 8. Recomendações Prioritárias

1. **Adicionar orientação visual de navegação no Módulo 1 (screenshot numerado da tela inicial).**
   - Problema que resolve: item 3.2 — travamento no primeiro contato com a ferramenta.
   - Impacto esperado: reduz drasticamente a taxa de abandono no exercício mais importante do curso (o primeiro).
   - Esforço estimado: **Baixo**.

2. **Explicar a mecânica de "salvar e comparar versões" logo no Módulo 1 ou na seção "Antes de Começar", não só no Módulo 8.**
   - Problema que resolve: item 3.3 — dependência invertida entre módulos, exercício-chave sem base operacional.
   - Impacto esperado: destrava o mecanismo pedagógico central do curso (observar → comparar → refinar) em 5 módulos de uma só vez.
   - Esforço estimado: **Médio** (requer reescrever uma instrução recorrente, não só adicionar um parágrafo).

3. **Adicionar aviso de tempo de geração e risco de fechar a aba.**
   - Problema que resolve: item 3.4 — perda de trabalho sem explicação, risco real de abandono do curso.
   - Impacto esperado: alto, evita frustração na primeira experiência com a ferramenta.
   - Esforço estimado: **Baixo**.

4. **Inserir comparações visuais reais (screenshots antes/depois) substituindo as tabelas textuais dos Módulos 4, 5 e 6.**
   - Problema que resolve: item 3.1 — o problema estrutural mais visível do curso, um material sobre design sem nenhuma imagem.
   - Impacto esperado: alto — alinha o método de ensino ao princípio pedagógico central do próprio curso ("ver antes de entender").
   - Esforço estimado: **Alto** (requer capturar telas reais da ferramenta em uso).

5. **Adicionar aviso sobre limites de uso do plano Claude.**
   - Problema que resolve: item 3.5 — interrupção inesperada de atividade no meio do curso.
   - Impacto esperado: médio-alto, evita frustração silenciosa e sem explicação.
   - Esforço estimado: **Baixo**.

6. **Ensinar o recurso de anexar referência visual (foto/print) como atalho de estilo.**
   - Problema que resolve: lacuna intermediária — funcionalidade poderosa e muito acessível para quem não tem vocabulário de design, hoje ausente do curso.
   - Impacto esperado: alto ganho de autonomia com baixo custo de explicação.
   - Esforço estimado: **Baixo**.

7. **Adicionar bloco sobre acessibilidade no Módulo 5, incluindo o pedido direto de auditoria ao Claude.**
   - Problema que resolve: item 3.9 — lacuna de conteúdo relevante para o contexto de escola pública.
   - Impacto esperado: médio-alto, relevância pedagógica direta para o público-alvo.
   - Esforço estimado: **Médio**.

8. **Verificar e declarar explicitamente a disponibilidade (ou não) em navegador mobile.**
   - Problema que resolve: item 3.6 — descumprimento silencioso de um requisito da própria especificação do curso.
   - Impacto esperado: médio, evita expectativa quebrada em parte do público que só tem acesso a smartphone.
   - Esforço estimado: **Baixo** (verificação) + **Baixo** (declaração no texto).

9. **Adicionar nota sobre o bug conhecido de comentários no Módulo 8.**
   - Problema que resolve: item 3.10 — confusão evitável ao usar um dos três métodos de refinamento ensinados.
   - Impacto esperado: médio, previne uma frustração pontual mas recorrente.
   - Esforço estimado: **Baixo**.

10. **Diferenciar visualmente os três tipos de callout (prompt, aviso, conceito) antes da conversão para Word.**
    - Problema que resolve: item 3.13 — leitura rápida prejudicada, mais crítico ainda no documento final em Word.
    - Impacto esperado: médio, melhora a usabilidade do material como produto de leitura.
    - Esforço estimado: **Baixo**.

---

## Nota de fechamento

O roteiro atual já ultrapassa o nível de "tutorial de prompts" e se comporta como um curso de raciocínio de design — essa é a parte difícil de acertar, e está acertada. O que falta para chegar ao nível de "curso profissional de introdução ao Claude Design" não é reescrever a pedagogia: é **construir os andaimes operacionais ao redor dela** — imagens, avisos de comportamento real da ferramenta e uma mecânica de comparação explícita — para que o raciocínio bem desenhado não seja interrompido por fricções de interface que o público-alvo, por definição, não tem repertório prévio para contornar sozinho.
