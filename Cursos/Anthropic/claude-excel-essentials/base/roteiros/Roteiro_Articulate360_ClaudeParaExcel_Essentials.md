# Roteiro de Produção — Articulate 360
## Curso: Claude para Excel — Consultoria Analítica, Fórmulas Complexas e Automação (Essentials)

---

**Ferramenta-alvo:** Storyline 360 (principal) + Rise 360 (alternativo para versão linear)
**Público-alvo:** Docentes do ensino superior iniciantes em IA; analistas administrativos; discentes do ensino superior
**Duração estimada:** 90 minutos (4 módulos de conteúdo + 1 módulo de síntese)
**Narração:** Locutor humano (recomendado) ou TTS
**Branching:** Não — progressão linear cumulativa
**Sistema/aplicativo referenciado:** Microsoft Excel (versão 2019 e 365) + Claude em claude.ai (navegador)

---

## SLIDES DE ABERTURA E NAVEGAÇÃO GERAL

---


────────────────────────────────

SLIDE 01 — ABERTURA DO CURSO
Tipo: Título
Duração estimada: 25s

────────────────────────────────

VISUAL
Fundo com textura sutil na cor institucional. Título principal em tipografia grande. Subtítulo: "Trilha Essentials — 90 minutos". Logo do curso à esquerda. Animação: fade-in do título (0,5s), fade-in do subtítulo (0,8s).

NARRAÇÃO
Bem-vindo ao curso Claude para Excel: Consultoria Analítica, Fórmulas Complexas e Automação — Trilha Essentials. [PAUSA]
Neste curso você vai aprender a usar o Claude como consultor técnico especializado no contexto do Microsoft Excel: estruturando perguntas analíticas com precisão, solicitando e interpretando fórmulas complexas, diagnosticando bases de dados com problemas de qualidade e identificando possibilidades de automação. [PAUSA]
Ao final, você terá um fluxo de consultoria com IA que poderá aplicar de forma autônoma em situações reais da sua área.

INTERAÇÃO
Botão "Iniciar" — avança para o Slide 02.

NAVEGAÇÃO
Restrita — botão "Próximo" da barra padrão oculto; aluno usa apenas o botão "Iniciar".


────────────────────────────────

SLIDE 02 — VISÃO GERAL DO CURSO E COMPETÊNCIAS
Tipo: Conteúdo
Duração estimada: 45s

────────────────────────────────

VISUAL
Linha do tempo horizontal com 5 etapas, cada uma com ícone distinto: bússola (M1), engrenagem de prompt (M2), grade de fórmulas (M3), lupa sobre dados (M4), bandeira de chegada (M5). Abaixo da linha do tempo, quatro blocos com as competências a desenvolver surgindo em sequência com delay de 0,3s.

NARRAÇÃO
O curso está organizado em cinco módulos em progressão cumulativa. [PAUSA]
No Módulo 1 você vai compreender o papel do Claude como consultor técnico e configurar o ambiente de trabalho.
No Módulo 2 você vai dominar a engenharia de prompts analíticos para obter respostas técnicas precisas.
No Módulo 3 você vai aprender e aplicar as principais funções de busca e lógica condicional do Excel.
No Módulo 4 você vai diagnosticar e tratar problemas de qualidade em bases de dados.
E no Módulo 5 você vai integrar tudo em um fluxo completo de consultoria. [PAUSA]
Cada módulo pressupõe o anterior — siga a sequência proposta.

INTERAÇÃO
Nenhuma — slide informativo.

NAVEGAÇÃO
Livre após 12 segundos (botão "Próximo" liberado com timer).

---

## MÓDULO 1 — CLAUDE COMO CONSULTOR TÉCNICO: FUNDAMENTOS DA PARCERIA ANALÍTICA

---


────────────────────────────────

SLIDE 03 — ABERTURA DO MÓDULO 1
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de bússola, número e título do módulo. Subtítulo: "Duração estimada: 20 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 1 — Claude como Consultor Técnico: Fundamentos da Parceria Analítica. [PAUSA]
Este módulo introduz o paradigma central do curso: usar o Claude não como um buscador de respostas prontas, mas como um consultor técnico que exige do interlocutor clareza de contexto e precisão de objetivos.

INTERAÇÃO
Botão "Começar" — avança para Slide 04.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 04 — O INTERVALO ENTRE O PROBLEMA E O ESPECIALISTA
Tipo: Conteúdo
Duração estimada: 40s

────────────────────────────────

VISUAL
Diagrama com três elementos em linha:
Ícone de planilha com problema (esquerda) → ponto de interrogação grande (centro) → ícone de especialista humano distante (direita, com seta longa).
Abaixo do ponto de interrogação: ícone do Claude com rótulo "Consultor técnico disponível imediatamente".
Texto abaixo: "O Excel é amplamente usado — mas muitos usuários ficam restritos a operações elementares por falta de suporte técnico especializado. O Claude atua precisamente nesse intervalo."
Animação: elementos surgem em sequência da esquerda para a direita.

NARRAÇÃO
O Microsoft Excel é uma das ferramentas de análise de dados mais usadas em ambientes acadêmicos e administrativos. Contudo, um número expressivo de usuários permanece restrito a operações elementares — soma, filtro, cópia de fórmulas — por não dispor de suporte técnico imediato. [PAUSA]
É exatamente nesse intervalo entre o problema e o especialista humano que o Claude pode atuar de forma relevante. Ele não substitui o especialista — mas está disponível a qualquer momento e exige apenas que você saiba perguntar bem.

INTERAÇÃO
Nenhuma — slide expositivo com diagrama.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 05 — CONSULTOR TÉCNICO: O QUE ISSO SIGNIFICA?
Tipo: Conteúdo com analogia
Duração estimada: 45s

────────────────────────────────

VISUAL
Dois blocos contrastados lado a lado:
Esquerda — "Busca em mecanismo de pesquisa": ícone de lupa, texto: "Qualidade do resultado depende pouco da qualidade da pergunta."
Direita — "Consulta ao Claude (consultor técnico)": ícone de conversa estruturada, texto: "Qualidade da resposta é diretamente proporcional à qualidade do pedido."
Abaixo: analogia médica em caixa de destaque — "Perguntar vagamente ao Claude é como ir ao médico e dizer apenas 'não estou bem'. Uma pergunta detalhada gera um diagnóstico preciso."
Animação: blocos surgem simultaneamente; caixa de analogia surge com delay de 0,8s.

NARRAÇÃO
Entender o que é um consultor técnico neste contexto é fundamental. Um consultor não apenas responde perguntas — ele solicita informações adicionais quando o problema está mal definido, apresenta múltiplas abordagens com vantagens e limitações, e explica o raciocínio por trás de cada sugestão. [PAUSA]
O Claude opera de forma análoga. Quanto mais detalhado e estruturado for o seu pedido, mais precisa e útil será a resposta. [PAUSA]
Uma analogia: consultar o Claude com uma pergunta vaga é como ir ao médico e dizer apenas "não estou bem". Já uma descrição detalhada do problema permite um diagnóstico concreto e adaptado ao seu cenário.

INTERAÇÃO
Nenhuma — slide expositivo com contraste visual.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 06 — O AMBIENTE DE TRABALHO RECOMENDADO
Tipo: Conteúdo com instrução técnica
Duração estimada: 40s

────────────────────────────────

VISUAL
Diagrama mostrando dois painéis lado a lado: Excel (à esquerda) e claude.ai no navegador (à direita). Setas bidirecionais entre os dois indicando o ciclo iterativo: "Formular dúvida → Copiar solução → Aplicar no Excel → Validar e refinar". Abaixo: nota técnica — "Versão recomendada: Excel 2019 ou Microsoft 365. Acesso ao Claude: claude.ai (conta gratuita ou Pro)."

[PRINT]
Nome: Ambiente de trabalho com Excel e claude.ai abertos lado a lado
Caminho: Tela do computador com Microsoft Excel aberto à esquerda e claude.ai aberto no navegador à direita, ambos visíveis simultaneamente
Destaque: mostrar a disposição lado a lado como ambiente de trabalho recomendado para o ciclo de consultoria
Modo: Estática

NARRAÇÃO
O ambiente de trabalho recomendado é simples: mantenha o Excel e o Claude abertos lado a lado, seja na mesma tela ou em monitores distintos. [PAUSA]
Essa disposição facilita o ciclo de consultoria: você formula a dúvida no Claude, copia a solução gerada, aplica no Excel e retorna ao Claude para validar ou refinar. [PAUSA]
Esse fluxo não é linear — é iterativo. E a familiaridade com essa iteração é, em si, uma competência a ser desenvolvida ao longo deste curso.

INTERAÇÃO
Nenhuma — slide de instrução técnica com print ilustrativo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 07 — AS CINCO ETAPAS DO CICLO DE CONSULTORIA
Tipo: Conteúdo interativo (linha do tempo clicável)
Duração estimada: 55s

────────────────────────────────

VISUAL
Linha do tempo horizontal com 5 etapas clicáveis, cada uma com ícone e título curto:
1. Diagnóstico — ícone de lupa
2. Exploração — ícone de bifurcação/opções
3. Implementação — ícone de ferramenta sobre planilha
4. Validação — ícone de checklist
5. Escalação — ícone de seta expandindo
Cada etapa, ao ser clicada, abre layer com definição e exemplo prático.

NARRAÇÃO
O ciclo de consultoria com o Claude segue cinco etapas — e esse padrão vai se repetir em todos os módulos. Clique em cada etapa para explorar. [PAUSA]
Diagnóstico: identificar e descrever o problema com precisão. [PAUSA]
Exploração: solicitar ao Claude múltiplas abordagens possíveis. [PAUSA]
Implementação: aplicar a solução em um subconjunto controlado — nunca direto na base completa. [PAUSA]
Validação: conferir o resultado com dados de teste, incluindo casos extremos. [PAUSA]
Escalação: aplicar a solução aprovada à base completa.

INTERAÇÃO
Etapa 1 "Diagnóstico" — abre layer com: Definição: "Identificar e descrever o problema com precisão suficiente para o Claude entender o contexto." Exemplo: "Tenho 10.000 registros com duplicatas por e-mail. Quero manter apenas o registro mais antigo."
Etapa 2 "Exploração" — abre layer com: Definição: "Solicitar múltiplas abordagens e comparar vantagens e limitações antes de escolher." Exemplo: "Quais são as formas possíveis de remover duplicatas no Excel 2019? Apresente vantagens e limitações de cada uma."
Etapa 3 "Implementação" — abre layer com: Definição: "Aplicar a solução em um subconjunto pequeno e controlado antes de expandir." Exemplo: "Aplicar a fórmula sugerida nas primeiras 20 linhas da planilha e verificar o resultado."
Etapa 4 "Validação" — abre layer com: Definição: "Testar com dados extremos: valores vazios, negativos, fora do intervalo esperado." Exemplo: "O que acontece com a fórmula quando a célula de nota está vazia? Quando o ID não existe na tabela de referência?"
Etapa 5 "Escalação" — abre layer com: Definição: "Aplicar a solução aprovada à base completa e documentar o procedimento." Exemplo: "Arrastar a fórmula validada para as 10.000 linhas e registrar o prompt utilizado."
Todas as 5 etapas devem ser clicadas para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após clique nas cinco etapas.


────────────────────────────────

SLIDE 08 — O CLAUDE NÃO É INFALÍVEL
Tipo: Conteúdo de alerta
Duração estimada: 35s

────────────────────────────────

VISUAL
Ícone de alerta (triângulo laranja). Três situações em cartões menores:
1. Contexto insuficiente → resposta genérica
2. Versão do Excel desconhecida → função incompatível sugerida
3. Configuração regional diferente → nome de função errado (ex.: VLOOKUP vs PROCV)
Abaixo: regra em destaque — "Sempre teste em um subconjunto controlado antes de aplicar em dados reais."
Animação: ícone de alerta pulsa uma vez ao entrar; cartões surgem em sequência.

NARRAÇÃO
Antes de avançar, uma ressalva fundamental: o Claude não é infalível. [PAUSA]
Erros ocorrem especialmente quando o contexto fornecido é insuficiente, quando a tarefa envolve versões antigas do Excel ou quando configurações regionais alteram os nomes das funções — VLOOKUP em inglês vira PROCV em português, por exemplo. [PAUSA]
Por essa razão, o ciclo de consultoria inclui obrigatoriamente uma etapa de validação. Antes de aplicar qualquer solução em dados reais, teste-a em um subconjunto pequeno e controlado. Esse hábito vai ser reforçado em todos os módulos seguintes.

INTERAÇÃO
Nenhuma — slide de alerta informativo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 09 — EXERCÍCIO PRÁTICO: CONFIGURAR O AMBIENTE E REALIZAR A PRIMEIRA CONSULTA
Tipo: Instrução prática
Duração estimada: 40s

────────────────────────────────

VISUAL
Passo a passo numerado com 6 etapas. Tabela de dados do exercício (ID, Nome, Receita — 5 clientes) em caixa de destaque. Prompt-base em caixa monoespaçada. Barra de progresso: "Exercício 1 de 5". Animação: etapas surgem em sequência com delay de 0,4s.

[PRINT]
Nome: Janela do Claude com resposta ao prompt de classificação ao lado da planilha Excel com fórmula aplicada na coluna D
Caminho: claude.ai (navegador) com resposta visível + Microsoft Excel com coluna D preenchida com "Acima da Média" / "Abaixo da Média"
Destaque: destacar a resposta do Claude à esquerda e a coluna D da planilha com a fórmula aplicada à direita
Modo: Estática

NARRAÇÃO
Agora configure o ambiente e realize a primeira consulta. [PAUSA]
Abra o Excel e crie a planilha com os dados dos cinco clientes — ID, Nome e Receita. Acesse o claude.ai e abra uma nova conversa. Cole a tabela no chat junto com o prompt exibido na tela. Leia a resposta com atenção: o Claude entendeu a estrutura dos dados? Sugeriu uma fórmula específica? Explicou o raciocínio? [PAUSA]
Implemente a fórmula na célula D2 e arraste até D6. Verifique se os resultados fazem sentido com os dados.

INTERAÇÃO
Botão "Ver tabela de dados" — abre layer com a tabela dos 5 clientes formatada.
Botão "Ver prompt-base" — abre layer com o prompt completo e botão "Copiar prompt".
Botão "Concluí o exercício" — avança para Slide 10.

NAVEGAÇÃO
Restrita — avanço via botão "Concluí o exercício".


────────────────────────────────

SLIDE 10 — CHECKLIST DE CONCLUSÃO DO MÓDULO 1
Tipo: Avaliação de êxito
Duração estimada: 25s

────────────────────────────────

VISUAL
Quatro itens de checklist interativo:
☐ Excel e Claude abertos lado a lado no ambiente de trabalho
☐ Tabela de 5 clientes criada na planilha
☐ Prompt enviado ao Claude e resposta recebida
☐ Fórmula implementada na coluna D e resultado verificado
Ao marcar os quatro: camada de parabéns + botão "Avançar para o Módulo 2".

NARRAÇÃO
Confirme os quatro critérios antes de avançar. [PAUSA]
Se a resposta do Claude foi genérica, verifique se o prompt incluía a estrutura dos dados e o objetivo específico — esse é o tema central do próximo módulo.

INTERAÇÃO
Checkboxes 1 a 4 — clicáveis individualmente.
Ao marcar os quatro: camada de parabéns + botão "Avançar para o Módulo 2".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os quatro checkboxes marcados.

---

## MÓDULO 2 — ENGENHARIA DE PROMPTS: COMO ESTRUTURAR PERGUNTAS ANALÍTICAS

---


────────────────────────────────

SLIDE 11 — ABERTURA DO MÓDULO 2
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de engrenagem de prompt, número e título do módulo. Subtítulo: "Duração estimada: 25 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 2 — Engenharia de Prompts: Como Estruturar Perguntas Analíticas. [PAUSA]
O foco desloca-se da compreensão do papel do Claude para a habilidade central que determina a qualidade de toda interação: a construção de um prompt bem estruturado.

INTERAÇÃO
Botão "Começar" — avança para Slide 12.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 12 — O PRINCÍPIO CENTRAL: QUALIDADE DO PROMPT, QUALIDADE DA RESPOSTA
Tipo: Conteúdo
Duração estimada: 35s

────────────────────────────────

VISUAL
Equação visual em destaque tipográfico: "Prompt impreciso → lacunas preenchidas com suposições → resposta superficial." Abaixo: versão positiva — "Prompt detalhado → modelo interpreta com precisão → resposta acionável." Ícone de seta bidirecional entre prompt e resposta.
Animação: equação negativa surge primeiro; versão positiva surge com delay de 0,8s.

NARRAÇÃO
Um modelo de linguagem não lê nas entrelinhas — ele interpreta literalmente o que lhe é fornecido. Quando o contexto está ausente, o modelo preenche as lacunas com suposições genéricas, resultando em respostas superficiais. [PAUSA]
Esse princípio pode ser sintetizado assim: a qualidade da resposta gerada pelo Claude é diretamente proporcional à qualidade do pedido que a originou. [PAUSA]
É exatamente por isso que dominar a estrutura de um bom prompt é a competência mais importante deste curso — ela multiplica o valor de todas as outras.

INTERAÇÃO
Nenhuma — slide expositivo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 13 — A ESTRUTURA DE SEIS SEÇÕES DO PROMPT ANALÍTICO
Tipo: Conteúdo interativo (acordeão / cartões expansíveis)
Duração estimada: 60s

────────────────────────────────

VISUAL
Seis seções em accordion expansível, cada uma com rótulo, ícone e descrição expandida ao clicar:
1. CONTEXTO — ícone de mapa
2. DADOS — ícone de tabela
3. OBJETIVO — ícone de alvo
4. RESTRIÇÕES — ícone de barreira
5. EXEMPLO — ícone de amostra
6. PERGUNTA — ícone de ponto de interrogação
Cada seção expandida mostra definição + exemplo de preenchimento.

NARRAÇÃO
O material-fonte propõe uma estrutura de seis seções para qualquer prompt analítico. Pense nela como um briefing que você entregaria a um consultor externo antes de uma reunião técnica. Explore cada seção clicando nos painéis. [PAUSA]
Contexto: o que é o projeto e por que ele importa. Dados: tamanho, fonte e período da base. Objetivo: o que você pretende obter. Restrições: limitações técnicas, operacionais ou legais. Exemplo: uma amostra real de 5 a 10 linhas. E Pergunta: no máximo três a cinco questões específicas. [PAUSA]
Essa estrutura não é burocrática — é o equivalente de dizer ao consultor tudo o que ele precisa saber antes de começar a trabalhar.

INTERAÇÃO
Painel 1 "CONTEXTO" — expande com: Definição: "O que é o projeto e por que ele importa." Exemplo: "Base de dados de clientes de uma universidade. O objetivo é evitar envio duplicado de comunicações."
Painel 2 "DADOS" — expande com: Definição: "Tamanho, fonte, período e estrutura da base." Exemplo: "Arquivo: clientes.xlsx. Colunas: ID, Nome, Email, Data_Cadastro, Status. Tamanho: ~3.000 registros."
Painel 3 "OBJETIVO" — expande com: Definição: "O que você pretende obter com a consulta." Exemplo: "Manter apenas o registro com Data_Cadastro mais antiga para cada e-mail. Listar IDs removidos para auditoria."
Painel 4 "RESTRIÇÕES" — expande com: Definição: "Limitações técnicas, operacionais ou legais que o Claude deve respeitar." Exemplo: "Excel versão 2019 (sem XLOOKUP disponível). Não alterar a planilha original."
Painel 5 "EXEMPLO" — expande com: Definição: "Amostra real ou fictícia representativa com 5 a 10 linhas." Exemplo: "Tabela com ID, Nome, Email e Data_Cadastro mostrando registros duplicados."
Painel 6 "PERGUNTA" — expande com: Definição: "De 1 a 3 perguntas específicas e mensuráveis." Exemplo: "Qual a melhor abordagem para identificar e remover as duplicatas? Prefiro solução replicável mensalmente."
Todos os 6 painéis devem ser abertos para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após abertura dos seis painéis.


────────────────────────────────

SLIDE 14 — OS QUATRO TIPOS DE ANÁLISE E SEUS PROMPTS
Tipo: Conteúdo interativo (carrossel)
Duração estimada: 50s

────────────────────────────────

VISUAL
Carrossel com 4 cartões, cada um com tipo de análise, pergunta-chave, ênfase no prompt e exemplo:
1. Descritiva — "O que aconteceu?" → ênfase em métricas desejadas
2. Comparativa — "Como se comparam os grupos?" → ênfase em delimitação dos grupos
3. Diagnóstica — "Por que isso ocorreu?" → ênfase em descrição precisa da anomalia
4. Preditiva/Risco — "O que acontecerá?" → ênfase nas variáveis suspeitas
Setas de navegação lateral.

NARRAÇÃO
Diferentes tipos de problema analítico exigem ênfases distintas dentro da estrutura de seis seções. Explore os quatro tipos. [PAUSA]
A análise descritiva responde "o que aconteceu?" e beneficia-se de uma descrição detalhada das métricas desejadas. [PAUSA]
A comparativa responde "como se comparam os grupos?" e requer que os grupos estejam claramente delimitados no prompt. [PAUSA]
A diagnóstica responde "por que isso ocorreu?" e demanda a descrição precisa da anomalia observada. [PAUSA]
E a preditiva ou de risco pressupõe que você especifique as variáveis que suspeita serem relevantes.

INTERAÇÃO
Seta "anterior" e seta "próximo" — navegam entre os 4 cartões.
Todos os 4 devem ser visitados para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após visita aos quatro cartões.


────────────────────────────────

SLIDE 15 — QUANDO A RESPOSTA É INSATISFATÓRIA: TRÊS SITUAÇÕES
Tipo: Conteúdo interativo (hotspot)
Duração estimada: 45s

────────────────────────────────

VISUAL
Diagrama com três ícones de situação clicáveis:
1. Resposta genérica — ícone de nuvem vaga
2. Entendimento equivocado da estrutura — ícone de tabelas mal conectadas
3. Solução correta, mas impraticável — ícone de fórmula complexa com X
Cada ícone abre layer com descrição do problema e solução de reformulação do prompt.

NARRAÇÃO
Saber o que fazer quando a resposta do Claude é insatisfatória é tão importante quanto saber formular o prompt inicial. Clique nos três ícones para explorar as situações mais recorrentes. [PAUSA]
A resposta genérica ocorre quando o prompt carece de especificidade — a solução é acrescentar o dado que estava implícito. [PAUSA]
O entendimento equivocado da estrutura ocorre quando o Claude supõe uma operação diferente da desejada — uma descrição explícita da estrutura resolve. [PAUSA]
E a solução tecnicamente correta, mas impraticável, ocorre quando o Claude sugere uma fórmula complexa quando uma solução mais simples seria mais sustentável — informe a restrição de legibilidade e peça uma alternativa.

INTERAÇÃO
Ícone 1 "Resposta genérica" — abre layer com: Problema: "Prompt carecia de especificidade; Claude preencheu lacunas com suposições." Solução: "Reformular acrescentando: contexto do projeto, exemplo de dados e restrição de versão do Excel."
Ícone 2 "Entendimento equivocado" — abre layer com: Problema: "Claude interpretou uma concatenação como junção (join) de tabelas." Solução: "Descrever explicitamente a estrutura: 'Quero concatenar as colunas A e B em uma nova coluna C, não cruzar tabelas.'"
Ícone 3 "Solução impraticável" — abre layer com: Problema: "Claude sugeriu fórmula matricial de grande complexidade." Solução: "Informar a restrição: 'Prefiro uma solução com colunas auxiliares, mais legível para a equipe que vai manter a planilha.'"
Os três ícones devem ser clicados para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após clique nos três ícones.


────────────────────────────────

SLIDE 16 — EXERCÍCIO PRÁTICO: PROMPT VAGO VS. PROMPT ESTRUTURADO
Tipo: Instrução prática com questão de múltipla escolha
Duração estimada: 55s

────────────────────────────────

VISUAL
Passo a passo de 4 etapas para o experimento. Dois campos de código monoespaçado lado a lado — prompt vago (esquerda, fundo vermelho claro) e prompt estruturado (direita, fundo verde claro). Barra de progresso: "Exercício 2 de 5".

[PRINT]
Nome: Duas respostas do Claude lado a lado — prompt vago vs. prompt estruturado
Caminho: claude.ai (navegador) — janela ou abas com a resposta ao prompt vago e a resposta ao prompt estruturado, capturadas para comparação
Destaque: destacar a diferença de especificidade e acionabilidade entre as duas respostas
Modo: Estática (dois prints sequenciais ou montagem lado a lado)

NARRAÇÃO
Agora você vai comprovar na prática a diferença que o prompt faz. [PAUSA]
Primeiro, no Claude, envie o prompt vago: "Tenho duplicatas na minha planilha. Como removo?" Observe se a resposta é genérica ou específica. [PAUSA]
Em seguida, envie o prompt estruturado exibido na tela — com Contexto, Dados, Objetivo, Restrições, Exemplo e Pergunta. Compare as duas respostas. [PAUSA]
Depois, responda à questão na tela com base no que você observou.

INTERAÇÃO
Botão "Ver prompt vago" — exibe o prompt curto em layer.
Botão "Ver prompt estruturado" — exibe o prompt completo com as seis seções e botão "Copiar prompt".

Questão de múltipla escolha:
Tipo: Pick-one (Storyline freeform)
Enunciado: "Com base no experimento, qual afirmação descreve melhor a diferença entre as duas respostas do Claude?"
Alternativas:
A) "As respostas foram equivalentes, pois o Claude sempre entende o contexto implícito."
B) "O prompt estruturado gerou uma resposta mais específica e acionável porque forneceu contexto, estrutura de dados, restrições e exemplo concreto."
C) "O prompt vago foi mais eficiente por ser mais curto e direto."
D) "A qualidade da resposta dependeu exclusivamente da versão do Claude, não do prompt."
Gabarito: B
Tentativas: 2
Feedback B (correto): "Correto! O prompt estruturado fornece ao Claude as informações necessárias para propor uma solução específica — respeitando inclusive as restrições de versão do Excel informadas."
Feedback A/C/D (incorreto — 1ª tentativa): "Revise o experimento e tente novamente. A diferença entre as respostas está diretamente ligada ao que foi fornecido no prompt."
Feedback A/C/D (incorreto — 2ª tentativa): "A resposta correta é B. O modelo interpreta literalmente o que recebe — sem contexto, preenche lacunas com suposições genéricas."

Botão "Concluir Módulo 2" — aparece após submissão, avança para Slide 17.

NAVEGAÇÃO
Restrita — avanço via botão "Concluir Módulo 2", liberado após submissão da questão.


────────────────────────────────

SLIDE 17 — CHECKLIST DE CONCLUSÃO DO MÓDULO 2
Tipo: Avaliação de êxito
Duração estimada: 20s

────────────────────────────────

VISUAL
Três itens de checklist interativo:
☐ Prompt vago e prompt estruturado enviados ao Claude
☐ Diferença de especificidade entre as respostas identificada
☐ Questão de múltipla escolha respondida
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 3".

NARRAÇÃO
Confirme os três critérios. [PAUSA]
A estrutura de seis seções que você aprendeu aqui vai ser usada nos próximos módulos — especialmente para solicitar fórmulas e diagnósticos de dados.

INTERAÇÃO
Checkboxes 1 a 3 — clicáveis individualmente.
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 3".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os três checkboxes marcados.

---

## MÓDULO 3 — FÓRMULAS DE BUSCA E LÓGICA CONDICIONAL NO EXCEL

---


────────────────────────────────

SLIDE 18 — ABERTURA DO MÓDULO 3
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de grade de fórmulas, número e título do módulo. Subtítulo: "Duração estimada: 25 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 3 — Fórmulas de Busca e Lógica Condicional no Excel. [PAUSA]
Com domínio da estruturação de prompts, você está preparado para aprofundar-se nas fórmulas mais demandadas em análise de dados: as funções de busca e as de lógica condicional.

INTERAÇÃO
Botão "Começar" — avança para Slide 19.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 19 — FUNÇÕES DE BUSCA: O QUE SÃO E PARA QUÊ SERVEM
Tipo: Conteúdo
Duração estimada: 35s

────────────────────────────────

VISUAL
Diagrama de cruzamento de tabelas: Tabela A (Matrícula, Nota) + Tabela B (Matrícula, Nome) → resultado com Nome trazido para Tabela A pela Matrícula. Legenda: "Funções de busca = mecanismo de cruzamento de tabelas (equivalente ao JOIN em bancos de dados relacionais)." Animação: tabelas surgem primeiro; seta de cruzamento e resultado surgem em sequência.

NARRAÇÃO
As funções de busca constituem um dos recursos mais usados — e mais mal compreendidos — do Excel. [PAUSA]
Sua função essencial é simples: dado um valor em uma célula, localizar esse mesmo valor em outra tabela e retornar uma informação associada a ele. É um mecanismo de cruzamento de tabelas — análogo ao que em bancos de dados relacionais chamamos de junção, ou JOIN. [PAUSA]
Você usa uma função de busca sempre que precisa "trazer" um dado de uma tabela para outra com base em um identificador comum.

INTERAÇÃO
Nenhuma — slide expositivo com diagrama.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 20 — PROCV, XLOOKUP E ÍNDICE/CORRESP: QUANDO USAR CADA UM
Tipo: Conteúdo interativo (tabela comparativa clicável)
Duração estimada: 60s

────────────────────────────────

VISUAL
Tabela comparativa com três linhas (PROCV, XLOOKUP, ÍNDICE/CORRESP) e quatro colunas (Versão necessária, Direção de busca, Múltiplas condições, Limitação principal). Cada linha da tabela é clicável e abre uma layer com explicação detalhada, sintaxe básica e exemplo de uso.

NARRAÇÃO
Existem três abordagens principais para buscas no Excel. Clique em cada função para explorar. [PAUSA]
O PROCV é a mais conhecida — mas tem uma limitação crítica: só retorna valores à direita da coluna de busca. E é sensível à inserção de novas colunas. [PAUSA]
O XLOOKUP resolve essas limitações e incorpora o tratamento de erros nativamente — mas requer Excel 365 ou 2021 em diante. [PAUSA]
E a combinação ÍNDICE/CORRESP é a mais flexível: permite múltiplas condições simultâneas de busca, ao custo de uma sintaxe mais complexa.

INTERAÇÃO
Linha "PROCV" — abre layer com:
  Versão: "Todas as versões do Excel."
  Limitação: "Só busca à direita. Sensível à inserção de colunas. Exige IFERROR para tratar erros."
  Sintaxe: "=PROCV(valor_procurado; tabela; núm_coluna; [correspondência])"
  Quando usar: "Buscas simples em Excel 2019 ou anterior, sem necessidade de flexibilidade."
Linha "XLOOKUP" — abre layer com:
  Versão: "Excel 365 ou 2021+."
  Limitação: "Não disponível em versões antigas."
  Sintaxe: "=XLOOKUP(valor; intervalo_busca; intervalo_retorno; [se_não_encontrado])"
  Quando usar: "Padrão recomendado para buscas simples em versões modernas."
Linha "ÍNDICE/CORRESP" — abre layer com:
  Versão: "Todas as versões do Excel."
  Limitação: "Sintaxe mais complexa; requer prática."
  Sintaxe: "=ÍNDICE(intervalo_retorno; CORRESP(valor; intervalo_busca; 0))"
  Quando usar: "Buscas com múltiplas condições ou quando a coluna de retorno é à esquerda."
As três linhas devem ser clicadas para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após clique nas três linhas.


────────────────────────────────

SLIDE 21 — SE, IFS E SWITCH: LÓGICA CONDICIONAL
Tipo: Conteúdo interativo (carrossel)
Duração estimada: 50s

────────────────────────────────

VISUAL
Carrossel com 3 cartões, cada um com a função, caso de uso ideal, sintaxe e exemplo:
1. SE (IF) — condição única ou dois resultados
2. IFS — múltiplas categorias sem aninhamento
3. SWITCH — valores discretos e bem definidos (códigos, categorias)
Setas de navegação lateral.

NARRAÇÃO
Para lógica condicional, o Excel oferece três funções principais. Explore cada cartão. [PAUSA]
A função SE avalia uma condição e retorna um valor se verdadeira e outro se falsa. Quando há mais de duas categorias, é necessário encadear múltiplos SE — o que torna a fórmula progressivamente difícil de ler. [PAUSA]
O IFS resolve esse problema listando pares condição–resultado sem aninhamento. Muito mais legível para três ou mais categorias. [PAUSA]
E o SWITCH é recomendado quando as condições envolvem valores discretos e bem definidos — códigos, abreviações, categorias — pois sua sintaxe é mais concisa nesses casos.

INTERAÇÃO
Seta "anterior" e seta "próximo" — navegam entre os 3 cartões.
Todos os 3 devem ser visitados para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após visita aos três cartões.


────────────────────────────────

SLIDE 22 — O CLAUDE PARA GERAÇÃO E EXPLICAÇÃO DE FÓRMULAS
Tipo: Conteúdo
Duração estimada: 35s

────────────────────────────────

VISUAL
Dois blocos em destaque:
Bloco 1 — "Peça a fórmula": ícone de código. Texto: "Forneça exemplos concretos de dados de entrada e do resultado esperado."
Bloco 2 — "Peça a explicação de cada argumento": ícone de livro aberto. Texto: "Acelera o aprendizado e reduz a dependência futura do Claude para situações similares."
Abaixo: regra de ouro em caixa destacada — "Toda fórmula recebida deve ser validada em um subconjunto controlado antes de aplicação à base completa."
Animação: blocos surgem simultaneamente; caixa de regra surge com delay de 0,7s.

NARRAÇÃO
O Claude é particularmente útil para a geração de fórmulas quando você fornece exemplos concretos de dados de entrada e do resultado esperado. [PAUSA]
Uma prática que acelera o aprendizado: peça não apenas a fórmula, mas a explicação de cada argumento. Isso reduz sua dependência futura da ferramenta para situações similares. [PAUSA]
E a regra de ouro que vale para qualquer fórmula recebida do Claude: valide em um subconjunto controlado antes de aplicar à base completa.

INTERAÇÃO
Nenhuma — slide expositivo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 23 — EXERCÍCIO PRÁTICO: SELECIONAR A FUNÇÃO CORRETA E APLICAR IFS
Tipo: Instrução prática
Duração estimada: 55s

────────────────────────────────

VISUAL
Passo a passo de 6 etapas. Descrição do cenário (Tabela Alunos e Tabela Notas) em caixa de destaque. Prompt-base em caixa monoespaçada. Barra de progresso: "Exercício 3 de 5".

[PRINT]
Nome: Planilha Excel com colunas I (Nome_Aluno por PROCV/ÍNDICE+CORRESP) e J (Situação por IFS) preenchidas
Caminho: Microsoft Excel > aba "Tabela Notas" > coluna I com nome do aluno buscado e coluna J com classificação por IFS
Destaque: destacar as colunas I e J com resultados corretos e o caso de matrícula inexistente com tratamento de erro visível
Modo: Estática

[PRINT]
Nome: Trecho do chat com o Claude que gerou as fórmulas de busca e IFS
Caminho: claude.ai (navegador) > conversa com prompt estruturado e resposta do Claude com fórmulas PROCV ou ÍNDICE/CORRESP e IFS
Destaque: destacar o prompt enviado e a resposta com a fórmula e explicação dos argumentos
Modo: Estática

NARRAÇÃO
Agora aplique na prática. [PAUSA]
Monte as duas tabelas em abas distintas — Tabela Alunos e Tabela Notas. Envie ao Claude o prompt exibido na tela para solicitar a fórmula de busca adequada, informando a versão do Excel. Implemente a fórmula na coluna I e teste com ao menos uma matrícula inexistente para verificar o tratamento de erro. [PAUSA]
Em seguida, adicione na coluna J uma fórmula IFS que classifique cada aluno em Aprovado, Recuperação ou Reprovado. Solicite ao Claude que valide a lógica e sugira como tratar células de nota vazias.

INTERAÇÃO
Botão "Ver prompt de busca" — abre layer com o prompt completo do exercício e botão "Copiar prompt".
Botão "Ver regras IFS" — abre layer com as regras de classificação (Nota ≥ 7 = Aprovado; ≥ 5 = Recuperação; < 5 = Reprovado).
Botão "Concluí o exercício" — avança para Slide 24.

NAVEGAÇÃO
Restrita — avanço via botão "Concluí o exercício".


────────────────────────────────

SLIDE 24 — CHECKLIST DE CONCLUSÃO DO MÓDULO 3
Tipo: Avaliação de êxito
Duração estimada: 20s

────────────────────────────────

VISUAL
Quatro itens de checklist interativo:
☐ Fórmula de busca implementada na coluna I com tratamento de erro
☐ Matrícula inexistente testada e erro tratado corretamente
☐ Fórmula IFS implementada na coluna J com as três classificações
☐ Claude consultado para validação da lógica de célula vazia
Ao marcar os quatro: camada de parabéns + botão "Avançar para o Módulo 4".

NARRAÇÃO
Confirme os quatro critérios. [PAUSA]
Se a fórmula de busca não funcionou, verifique se a coluna de busca e a coluna de retorno estão nos intervalos corretos — e se a versão do Excel que informou ao Claude corresponde à que está usando.

INTERAÇÃO
Checkboxes 1 a 4 — clicáveis individualmente.
Ao marcar os quatro: camada de parabéns + botão "Avançar para o Módulo 4".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os quatro checkboxes marcados.

---

## MÓDULO 4 — DIAGNÓSTICO E TRATAMENTO DE BASES DE DADOS

---


────────────────────────────────

SLIDE 25 — ABERTURA DO MÓDULO 4
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de lupa sobre dados, número e título do módulo. Subtítulo: "Duração estimada: 10 minutos". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 4 — Diagnóstico e Tratamento de Bases de Dados. [PAUSA]
O foco desloca-se das fórmulas de cálculo para a etapa que as precede logicamente: garantir que os dados sobre os quais você vai aplicar as fórmulas sejam confiáveis, consistentes e livres de anomalias.

INTERAÇÃO
Botão "Começar" — avança para Slide 26.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 26 — GARBAGE IN, GARBAGE OUT
Tipo: Conteúdo
Duração estimada: 35s

────────────────────────────────

VISUAL
Ícone de lata de lixo com uma fórmula complexa dentro — resultado: gráfico com dados incorretos saindo. Abaixo: texto em destaque — "'Garbage in, garbage out': fórmulas sofisticadas e visualizações elaboradas perdem completamente sua utilidade quando aplicadas sobre dados imprecisos, incompletos ou inconsistentes." Em contraste: ícone de base de dados limpa → fórmulas → resultado confiável.
Animação: cenário negativo surge primeiro; cenário positivo surge com delay de 0,7s.

NARRAÇÃO
Antes de qualquer análise, é necessário assegurar a qualidade dos dados. Esse princípio, consagrado na ciência de dados pela expressão "garbage in, garbage out" — lixo entra, lixo sai —, significa que fórmulas sofisticadas e visualizações elaboradas perdem completamente sua utilidade quando aplicadas sobre dados imprecisos ou inconsistentes. [PAUSA]
O diagnóstico prévio da base é, portanto, uma etapa incontornável do trabalho analítico. E o Claude pode atuar como orientador metodológico nessa etapa — desde que você forneça uma amostra representativa e descreva o padrão esperado para cada coluna.

INTERAÇÃO
Nenhuma — slide expositivo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 27 — AS QUATRO CATEGORIAS DE PROBLEMAS EM BASES DE DADOS
Tipo: Conteúdo interativo (hotspot)
Duração estimada: 50s

────────────────────────────────

VISUAL
Diagrama com quatro quadrantes clicáveis, cada um com ícone e título:
1. Campos vazios — ícone de célula em branco
2. Inconsistência de formatos — ícone de data com dois padrões
3. Duplicação de registros — ícone de duas linhas idênticas
4. Anomalias/Outliers — ícone de valor fora da escala
Cada quadrante abre layer com definição, exemplo real e impacto na análise.

NARRAÇÃO
Os problemas mais comuns em bases de dados de uso cotidiano podem ser agrupados em quatro categorias. Clique em cada quadrante para explorar. [PAUSA]
Campos vazios: colunas obrigatórias não preenchidas por falhas de entrada de dados ou migrações de sistema. [PAUSA]
Inconsistência de formatos: datas em padrões distintos na mesma coluna, números armazenados como texto, telefones com e sem parênteses. [PAUSA]
Duplicação de registros: o mesmo cliente ou aluno aparece mais de uma vez com identificadores distintos — consequência frequente de integrações entre sistemas. [PAUSA]
E anomalias ou outliers: valores numericamente possíveis, mas improváveis no contexto — como uma data de nascimento no século XVIII em um cadastro de funcionários ativos.

INTERAÇÃO
Quadrante 1 "Campos vazios" — abre layer com: Definição: "Colunas obrigatórias sem preenchimento." Exemplo: "Campo Nome vazio em um registro de cadastro." Impacto: "Fórmulas IFS retornam resultado incorreto; registros invisíveis em relatórios."
Quadrante 2 "Inconsistência de formatos" — abre layer com: Definição: "Mesmo tipo de dado com padrões distintos na mesma coluna." Exemplo: "Datas em DD/MM/AAAA e AAAA-MM-DD na mesma coluna Data_Cadastro." Impacto: "Ordenações incorretas; erros de cálculo de intervalos de tempo."
Quadrante 3 "Duplicação de registros" — abre layer com: Definição: "Mesmo registro aparece mais de uma vez com ID ou variações diferentes." Exemplo: "ID 202 aparece duas vezes com capitalização diferente no nome." Impacto: "Contagens infladas; envio duplicado de comunicações; distorção de métricas."
Quadrante 4 "Anomalias/Outliers" — abre layer com: Definição: "Valor numericamente possível, mas improvável no contexto." Exemplo: "Data de nascimento em 1850 em cadastro de funcionários ativos." Impacto: "Distorção de médias e estatísticas descritivas; erros de segmentação."
Todos os 4 quadrantes devem ser clicados para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após clique nos quatro quadrantes.


────────────────────────────────

SLIDE 28 — FUNÇÕES DE NORMALIZAÇÃO DE TEXTO
Tipo: Conteúdo de referência (carrossel)
Duração estimada: 40s

────────────────────────────────

VISUAL
Carrossel com 3 cartões de funções de normalização:
1. REMOVER.ESPAÇOS — remove espaços em excesso no início, fim e entre palavras
2. PRI.MAIÚSCULA — converte para capitalização de nomes próprios
3. SUBS / SUBSTITUIR — troca um padrão de caracteres por outro (ex.: padronizar separadores de telefone)
Cada cartão com: nome da função, sintaxe, exemplo antes/depois e caso de uso.

NARRAÇÃO
Para normalização de texto, o Excel dispõe de três funções essenciais. Explore os cartões. [PAUSA]
REMOVER.ESPAÇOS elimina espaços em excesso no início, no fim e entre palavras — problema muito comum em dados copiados de sistemas legados. [PAUSA]
PRI.MAIÚSCULA converte o texto para capitalização de nomes próprios — primeira letra de cada palavra em maiúscula. [PAUSA]
E SUBS, ou SUBSTITUIR, permite trocar um padrão de caracteres por outro — útil para padronizar separadores em telefones, por exemplo.

INTERAÇÃO
Seta "anterior" e seta "próximo" — navegam entre os 3 cartões.
Todos os 3 devem ser visitados para liberar navegação.

NAVEGAÇÃO
Restrita — botão "Próximo" liberado após visita aos três cartões.


────────────────────────────────

SLIDE 29 — ABORDAGENS PARA REMOÇÃO DE DUPLICATAS
Tipo: Conteúdo comparativo
Duração estimada: 35s

────────────────────────────────

VISUAL
Três cartões comparativos:
1. Fórmulas — "Identificam duplicatas, mas não as removem. Útil para sinalização."
2. Power Query — "Recomendado para até 10.000 registros. Visual, auditável, integrado ao Excel." Badge: "Recomendado para este curso"
3. VBA / Python — "Potente para grandes volumes. Exige familiaridade com programação. Fora do escopo Essentials."
Animação: cartões surgem em sequência com delay de 0,4s.

NARRAÇÃO
Para o tratamento de duplicatas, a escolha da abordagem depende do volume de dados e das regras de negócio. [PAUSA]
Fórmulas podem identificar duplicatas, mas não as removem diretamente — são úteis para sinalização antes de uma limpeza manual. [PAUSA]
O Power Query é a solução recomendada para bases de até 10.000 registros: é visual, auditável e integrado ao Excel sem necessidade de programação. [PAUSA]
Macros VBA e Python são mais potentes para grandes volumes, mas exigem familiaridade com programação — estão fora do escopo desta trilha Essentials.

INTERAÇÃO
Nenhuma — slide comparativo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 30 — EXERCÍCIO PRÁTICO: DIAGNOSTICAR E NORMALIZAR UMA BASE COM PROBLEMAS
Tipo: Instrução prática
Duração estimada: 50s

────────────────────────────────

VISUAL
Tabela de dados com problemas intencionais (ID, Nome, Email, Data_Cadastro, Telefone — 5 registros com inconsistências) em caixa de destaque. Passo a passo de 4 etapas. Barra de progresso: "Exercício 4 de 5".

[PRINT]
Nome: Planilha Excel com coluna de nomes normalizados (PRI.MAIÚSCULA + REMOVER.ESPAÇOS) e coluna de sinalização de duplicatas
Caminho: Microsoft Excel > aba "Dados_Brutos" > coluna adicional com nomes normalizados e coluna F com "DUPLICADO" / "OK" para cada ID
Destaque: destacar as linhas com ID 202 sinalizadas como "DUPLICADO" e os nomes normalizados com capitalização consistente
Modo: Estática

[PRINT]
Nome: Prompt de diagnóstico de qualidade enviado ao Claude e resposta com fórmulas sugeridas
Caminho: claude.ai (navegador) > prompt estruturado de diagnóstico enviado > resposta do Claude com fórmulas para cada problema identificado
Destaque: destacar o prompt com os problemas descritos e a resposta com a sequência de limpeza recomendada
Modo: Estática

NARRAÇÃO
Agora você vai diagnosticar e normalizar uma base com problemas reais. [PAUSA]
Reproduza a tabela exibida na tela em uma aba chamada "Dados_Brutos". Envie ao Claude o prompt de diagnóstico mostrado a seguir — descrevendo os problemas identificados visualmente e solicitando fórmulas com ordem de prioridade de limpeza. [PAUSA]
Implemente pelo menos uma normalização: use PRI.MAIÚSCULA combinado com REMOVER.ESPAÇOS para a coluna Nome. E na coluna F, crie uma fórmula que sinalize os IDs duplicados com "DUPLICADO" e os demais com "OK".

INTERAÇÃO
Botão "Ver tabela com problemas" — abre layer com a tabela de dados do exercício.
Botão "Ver prompt de diagnóstico" — abre layer com o prompt completo (problemas identificados, versão do Excel) e botão "Copiar prompt".
Botão "Concluí o exercício" — avança para Slide 31.

NAVEGAÇÃO
Restrita — avanço via botão "Concluí o exercício".


────────────────────────────────

SLIDE 31 — CHECKLIST DE CONCLUSÃO DO MÓDULO 4
Tipo: Avaliação de êxito
Duração estimada: 20s

────────────────────────────────

VISUAL
Três itens de checklist interativo:
☐ Coluna de nomes normalizados com capitalização consistente (Ana Silva, Bruno Santos, Carlos Lima)
☐ Coluna F sinalizando as linhas com ID 202 como "DUPLICADO" e demais como "OK"
☐ Capacidade de descrever o problema que cada fórmula resolve
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 5".

NARRAÇÃO
Confirme os três critérios. [PAUSA]
Se a fórmula de sinalização de duplicatas não funcionou, verifique se a condição de comparação está usando CONT.SE para contar ocorrências do ID — e se o critério de "mais de uma ocorrência" está corretamente codificado.

INTERAÇÃO
Checkboxes 1 a 3 — clicáveis individualmente.
Ao marcar os três: camada de parabéns + botão "Avançar para o Módulo 5".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com os três checkboxes marcados.

---

## MÓDULO 5 — SÍNTESE E APLICAÇÃO INTEGRADA

---


────────────────────────────────

SLIDE 32 — ABERTURA DO MÓDULO 5
Tipo: Título de módulo
Duração estimada: 15s

────────────────────────────────

VISUAL
Banner com ícone de bandeira de chegada, número e título do módulo. Subtítulo: "Duração estimada: 10 minutos de planejamento + execução conforme disponibilidade". Animação: slide-in da esquerda.

NARRAÇÃO
Módulo 5 — Síntese e Aplicação Integrada. [PAUSA]
Este módulo não introduz conteúdo novo. Sua função é consolidar, por meio de uma atividade integradora, todas as competências desenvolvidas ao longo do curso.

INTERAÇÃO
Botão "Começar" — avança para Slide 33.

NAVEGAÇÃO
Restrita — apenas o botão "Começar".


────────────────────────────────

SLIDE 33 — O FLUXO COMPLETO DE CONSULTORIA EM 5 ETAPAS
Tipo: Conteúdo — linha do tempo animada
Duração estimada: 40s

────────────────────────────────

VISUAL
Linha do tempo horizontal com as 5 etapas do ciclo de consultoria (retomada do Slide 07), agora mapeadas para as atividades do exercício integrador. Cada etapa conectada ao módulo de origem entre parênteses:
1. Diagnóstico (Módulo 4)
2. Exploração (Módulo 2 — prompt estruturado)
3. Implementação (Módulos 3 e 4 — fórmulas)
4. Validação (Módulos 1 e 3)
5. Escalação (documentação do processo)
Animação: etapas surgem em sequência com delay de 0,4s.

NARRAÇÃO
O fluxo completo de consultoria que você vai executar neste módulo articula todas as competências anteriores. [PAUSA]
Diagnóstico: identificar os problemas da base e enviar um prompt estruturado ao Claude. Exploração: solicitar múltiplas abordagens e selecionar a mais adequada. Implementação: aplicar fórmulas em um subconjunto controlado. Validação: testar com casos extremos antes de expandir. E escalação: aplicar à base completa e documentar o processo. [PAUSA]
A qualidade do resultado final depende diretamente da qualidade dos prompts formulados em cada etapa — e da acuidade com que você avalia o que o Claude sugere.

INTERAÇÃO
Nenhuma — slide expositivo.

NAVEGAÇÃO
Livre após conclusão da narração.


────────────────────────────────

SLIDE 34 — A ATIVIDADE INTEGRADORA: CENÁRIO
Tipo: Conteúdo — apresentação do cenário
Duração estimada: 35s

────────────────────────────────

VISUAL
Tabela de dados do cenário (Matrícula, Nome, Curso, Nota_Final, Frequência, Data_Matrícula — 6 registros com problemas intencionais: capitalização inconsistente, formatos de data diferentes, duplicata, campo vazio) exibida em caixa de destaque com scroll se necessário. Legenda: "Base de desempenho de alunos — coordenação acadêmica fictícia."

NARRAÇÃO
O cenário da atividade integradora é o seguinte: uma coordenação acadêmica possui uma planilha de desempenho de alunos com seis registros — e vários problemas de qualidade. [PAUSA]
Observe a tabela na tela: há capitalização inconsistente nos nomes, dois formatos de data diferentes na mesma coluna, uma matrícula duplicada com variações e um campo de Nota_Final vazio. [PAUSA]
Reproduza esta tabela em uma planilha Excel antes de avançar para as etapas.

INTERAÇÃO
Botão "Ver tabela completa" — abre layer com a tabela do cenário em tamanho completo.
Botão "Reproduzi a tabela no Excel" — libera avanço para Slide 35.

NAVEGAÇÃO
Restrita — avanço via botão "Reproduzi a tabela no Excel".


────────────────────────────────

SLIDE 35 — ATIVIDADE INTEGRADORA: ETAPAS 1 A 5
Tipo: Instrução prática guiada (stepper)
Duração estimada: 50s

────────────────────────────────

VISUAL
Stepper vertical com 5 etapas numeradas, cada uma expansível ao clicar:
Etapa 1 — Diagnóstico (Módulo 4): prompt de diagnóstico de qualidade
Etapa 2 — Normalização (Módulo 4): fórmulas para normalizar Nome e sinalizar duplicata
Etapa 3 — Classificação por IFS (Módulo 3): coluna "Situação" com 5 regras
Etapa 4 — Busca cruzada (Módulo 3): coluna "Coordenador" via ÍNDICE/CORRESP ou PROCV
Etapa 5 — Validação: testes com casos extremos (nota vazia e duplicata)
Cada etapa expandida mostra instrução detalhada e botão de acesso ao prompt correspondente. Barra de progresso: "Exercício 5 de 5".

[PRINT]
Nome: Planilha final com todas as colunas preenchidas — Situação, Coordenador, nomes normalizados e duplicata sinalizada
Caminho: Microsoft Excel > planilha principal com todas as colunas do exercício integrador preenchidas: Nome normalizado, sinalização de duplicata, Situação (IFS), Coordenador (PROCV/ÍNDICE+CORRESP)
Destaque: destacar a coluna Situação com os cinco resultados corretos (incluindo "Sem Registro" para Pedro Alves) e a coluna Coordenador com os três nomes corretos
Modo: Estática

[PRINT]
Nome: Trecho do chat com o Claude utilizado em alguma das etapas da atividade integradora
Caminho: claude.ai (navegador) > conversa com prompt estruturado utilizado em uma das cinco etapas + resposta do Claude correspondente
Destaque: destacar o prompt (com as seções Contexto, Dados, Objetivo, Restrições, Exemplo e Pergunta) e a resposta técnica recebida
Modo: Estática

NARRAÇÃO
Agora execute as cinco etapas da atividade integradora. [PAUSA]
Clique em cada etapa para ver as instruções detalhadas e acessar os prompts correspondentes. Etapa 1: diagnóstico da qualidade da base. Etapa 2: normalização do campo Nome e sinalização da duplicata. Etapa 3: coluna Situação com lógica IFS de cinco regras. Etapa 4: coluna Coordenador com busca cruzada na segunda aba. Etapa 5: validação com Pedro Alves e Carlos Souza como casos de teste. [PAUSA]
Documente o processo — capturas de tela dos prompts e respostas — para reutilização futura.

INTERAÇÃO
Etapa 1 — expande com: instrução de diagnóstico + botão "Ver prompt de diagnóstico".
Etapa 2 — expande com: instrução de normalização + botão "Ver prompts de normalização".
Etapa 3 — expande com: regras IFS completas (5 condições incluindo nota vazia) + botão "Ver prompt IFS".
Etapa 4 — expande com: instrução de criação da segunda aba com tabela de coordenadores + botão "Ver prompt de busca cruzada".
Etapa 5 — expande com: casos de teste obrigatórios (Pedro Alves com nota vazia; Carlos Souza duplicado) e instrução de registro.
Botão "Concluí todas as etapas" — avança para Slide 36.

NAVEGAÇÃO
Restrita — avanço via botão "Concluí todas as etapas".


────────────────────────────────

SLIDE 36 — CHECKLIST DE AVALIAÇÃO FINAL
Tipo: Avaliação de conclusão
Duração estimada: 35s

────────────────────────────────

VISUAL
Tabela de 7 critérios com checkbox interativo:
☐ Diagnóstico identificou pelo menos 3 problemas de qualidade distintos
☐ Campo Nome normalizado com capitalização consistente
☐ Duplicata da Matrícula 2021002 sinalizada corretamente
☐ Coluna "Situação" classifica corretamente os 6 registros, incluindo nota vazia
☐ Coluna "Coordenador" traz o nome correto para os 3 cursos distintos
☐ Ao menos um prompt estruturado (com Contexto, Dados, Objetivo, Exemplo e Pergunta) foi utilizado
☐ Resultado foi validado com ao menos um caso de teste extremo antes da aplicação completa
Ao marcar os sete: mensagem de conclusão + botão "Avançar para o encerramento".

NARRAÇÃO
Confirme os sete critérios de avaliação. [PAUSA]
O atendimento a todos eles evidencia que você internalizou não apenas as técnicas individuais, mas a lógica de uso do Claude como parceiro analítico — do diagnóstico à validação. [PAUSA]
Se algum critério não puder ser marcado, retorne à etapa correspondente e complete a atividade.

INTERAÇÃO
Checkboxes 1 a 7 — clicáveis individualmente.
Ao marcar todos os 7: camada de parabéns + botão "Avançar para o encerramento".

NAVEGAÇÃO
Restrita — botão de avanço aparece apenas com todos os sete checkboxes marcados.


────────────────────────────────

SLIDE 37 — MODELO DE REGISTRO DE CONSULTORIA
Tipo: Recurso de referência
Duração estimada: 25s

────────────────────────────────

VISUAL
Modelo de registro em caixa de código monoespaçada com as seções: Data, Base de dados, Problema original, Etapas Realizadas (5 subseções), Prompts Mais Eficazes, Limitações Identificadas, Próximos Passos. Botão de cópia. Nota explicativa: "Mantenha este registro para cada análise — ele permite a replicação futura e a revisão crítica do fluxo."

NARRAÇÃO
Antes de encerrar, guarde este modelo de registro de consultoria. [PAUSA]
Documentar o processo cumpre duas funções: permite a replicação futura do procedimento em contextos similares, e possibilita identificar etapas que poderiam ter sido mais eficientes. No ambiente acadêmico e administrativo, em que análises tendem a ser repetidas periodicamente — relatórios mensais, consolidações anuais —, essa documentação tem valor permanente.

INTERAÇÃO
Botão "Copiar modelo de registro" — copia o template para a área de transferência.
Botão "Avançar para o encerramento" — avança para Slide 38.

NAVEGAÇÃO
Livre — slide de referência.

---

## SLIDE DE ENCERRAMENTO

---


────────────────────────────────

SLIDE 38 — ENCERRAMENTO DO CURSO
Tipo: Encerramento
Duração estimada: 55s

────────────────────────────────

VISUAL
Fundo com identidade visual do Slide 01. Título: "Parabéns — você concluiu a Trilha Essentials." Ícone de conquista animado. Síntese em destaque tipográfico: "A IA não substitui o julgamento analítico do profissional — ela o amplifica. A competência de formular perguntas precisas é tão importante quanto a de interpretar respostas." Abaixo: três blocos de aprofundamento:
1. Fórmulas matriciais modernas — FILTRO, CLASSIFICAR, ÚNICA
2. Power BI e Power Query — visualizações e transformações em escala
3. VBA e Python (Pandas) — automação avançada
Animação: título e síntese surgem primeiro; blocos de aprofundamento em sequência com delay.

NARRAÇÃO
Você concluiu o curso Claude para Excel — Trilha Essentials. [PAUSA]
Ao longo dos cinco módulos, você aprendeu a tratar o Claude como consultor técnico, a estruturar prompts analíticos de seis seções, a aplicar funções de busca e lógica condicional, e a diagnosticar e tratar problemas de qualidade em bases de dados. [PAUSA]
Recomenda-se manter o hábito de aplicar o fluxo de consultoria — diagnóstico, exploração, implementação, validação e escalação — em situações reais da sua prática. É pela repetição contextualizada que as competências introduzidas aqui se consolidam em autonomia analítica duradoura. [PAUSA]
Para o aprofundamento, há três frentes na tela: fórmulas matriciais modernas como FILTRO e ÚNICA; Power BI e Power Query para análises em escala; e automação com VBA e Python para quem quiser ir mais longe. [PAUSA]
Bom trabalho.

INTERAÇÃO
Botão "Reiniciar o curso" — retorna ao Slide 01 (opcional).
Botão "Sair" — encerra o módulo e registra conclusão no LMS (trigger: Complete Course / passed).

NAVEGAÇÃO
Livre — slide final.

---

---

# TABELA GERAL DE ASSETS

| Tipo | Descrição | Slide de uso |
|------|-----------|:------------:|
| Diagrama animado | Planilha com problema → ponto de interrogação → especialista distante / Claude disponível | 04 |
| Diagrama animado | Cruzamento de tabelas por função de busca (Tabela A + Tabela B → resultado) | 19 |
| Diagrama animado | Ambiente de trabalho lado a lado: Excel (esquerda) + claude.ai (direita) com ciclo iterativo | 06 |
| Diagrama animado | Equação negativa (prompt impreciso → suposições → resposta superficial) vs. positiva | 12 |
| Diagrama animado | Garbage in / garbage out: base suja → fórmulas → resultado incorreto | 26 |
| Diagrama animado | Fluxo de 5 etapas do ciclo de consultoria (linha do tempo) | 07, 33 |
| Ícone | Bússola (Módulo 1) | 03 |
| Ícone | Engrenagem de prompt (Módulo 2) | 11 |
| Ícone | Grade de fórmulas (Módulo 3) | 18 |
| Ícone | Lupa sobre dados (Módulo 4) | 25 |
| Ícone | Bandeira de chegada (Módulo 5) | 32 |
| Ícone | Alvo (objetivo do prompt) | 13 |
| Ícone | Barreira (restrições) | 13 |
| Ícone | Célula em branco (campos vazios) | 27 |
| Ícone | Data com dois padrões (inconsistência de formato) | 27 |
| Ícone | Duas linhas idênticas (duplicação) | 27 |
| Ícone | Valor fora da escala (anomalia/outlier) | 27 |
| Ícone | Conquista/medalha | 36, 38 |
| Fonte monoespaçada | Exibição de prompts estruturados, fórmulas e modelo de registro | 13, 16, 23, 30, 37 |
| Áudio | Narração completa (38 slides) — locutor ou TTS | Todos |

---

# TABELA DE CAPTURAS DE TELA

| Tipo | Descrição da tela | Caminho no sistema | Modo de exibição | Slide | Responsável |
|------|-------------------|--------------------|:----------------:|:-----:|-------------|
| Captura de tela | Ambiente de trabalho com Excel e claude.ai abertos lado a lado | Tela do computador: Excel aberto à esquerda + claude.ai no navegador à direita | Estática | 06 | Equipe de conteúdo |
| Captura de tela | Janela do Claude com resposta ao prompt de classificação + planilha Excel com coluna D preenchida | claude.ai (resposta visível) + Microsoft Excel (coluna D com Acima/Abaixo da Média) | Estática | 09 | Equipe de conteúdo |
| Captura de tela | Duas respostas do Claude lado a lado: prompt vago vs. prompt estruturado | claude.ai — dois prints ou abas com as respostas das duas consultas para comparação | Estática (dois prints ou montagem lado a lado) | 16 | Equipe de conteúdo |
| Captura de tela | Planilha Excel com colunas I (busca por PROCV/ÍNDICE+CORRESP) e J (IFS) preenchidas | Microsoft Excel > aba Tabela Notas > colunas I e J com resultados e tratamento de erro | Estática | 23 | Equipe de conteúdo |
| Captura de tela | Trecho do chat com Claude que gerou as fórmulas de busca e IFS | claude.ai > prompt estruturado enviado + resposta com fórmulas e explicação dos argumentos | Estática | 23 | Equipe de conteúdo |
| Captura de tela | Planilha com coluna de nomes normalizados e coluna F de sinalização de duplicatas | Microsoft Excel > aba Dados_Brutos > coluna de nomes normalizados + coluna F com DUPLICADO/OK | Estática | 30 | Equipe de conteúdo |
| Captura de tela | Prompt de diagnóstico enviado ao Claude e resposta com fórmulas por ordem de prioridade | claude.ai > prompt de diagnóstico com problemas descritos + resposta com sequência de limpeza | Estática | 30 | Equipe de conteúdo |
| Captura de tela | Planilha final da atividade integradora com todas as colunas preenchidas | Microsoft Excel > planilha principal com Nome normalizado, duplicata sinalizada, Situação (IFS) e Coordenador (PROCV/ÍNDICE+CORRESP) | Estática | 35 | Participante (autogerado durante atividade) |
| Captura de tela | Trecho do chat com Claude utilizado em etapa da atividade integradora | claude.ai > prompt estruturado (6 seções) + resposta técnica usada em uma das 5 etapas | Estática | 35 | Participante (autogerado durante atividade) |
