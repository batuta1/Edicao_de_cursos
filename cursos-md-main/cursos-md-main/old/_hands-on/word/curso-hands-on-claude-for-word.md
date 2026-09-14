<link rel="stylesheet" href="../../.css/style.css">

# Use Claude for Word: Estruturar, Editar e Finalizar Documentos Profissionais — Curso Hands-on

> **Use Claude for Word — Structuring, Editing, and Finalizing Professional Documents**

*Ao final deste curso, você vai sair com um documento real, estruturado, revisado e formatado — feito por você, com a IA como parceira.*

---

## Antes de Arregaçar as Mangas

Sem enrolação: este curso é puro fazer. Cada oficina começa com um problema do dia a dia — aquele tipo de situação que você já viveu — e termina com algo concreto na sua tela. A teoria aparece só na dose mínima necessária para você dar o próximo passo. O resto você aprende errando, tentando e vendo o resultado aparecer.

**O que você precisa ter aberto agora:**

- Microsoft Word 2019 ou Office 365 (versão 2109 ou mais recente)
- O suplemento Claude for Word instalado e o painel visível à direita do documento — se ainda não instalou, vá em **Inserir → Obter Suplementos**, pesquise "Claude" e clique em Adicionar
- Uma conta Anthropic ativa (gratuita já funciona para começar)
- Conexão com a internet
- Um documento em branco aberto no Word — pode ser o que você criou ontem ou um novo mesmo

> 🔑 **Regra de ouro:** se o Claude devolveu algo que não era o que você queria, não é erro seu nem dele — é só o prompt pedindo ajuste. Reformule, tente de novo e siga em frente. É assim que se aprende.

---

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1 | Tenho notas soltas sobre um tema e não sei por onde começar o documento | 15 min |
| 2 | Escrevi no Claude mas perco toda a formatação quando colo no Word | 15 min |
| 3 | Meu texto ficou confuso, repetitivo e sem fluidez | 20 min |
| 4 | Alguém apontou contradições no meu relatório e não sei como encontrá-las | 20 min |
| Projeto Final | Preciso entregar um documento profissional completo até o fim do dia | 30 min |

As oficinas foram desenhadas para funcionar em sequência — cada uma entrega uma pequena vitória que faz sentido por si só e serve de degrau para a próxima.

---

<div style="page-break-after: always;"></div>

# Oficina 1 — Transforme Notas Soltas num Esqueleto de Documento

### 🎯 O Problema

Você tem um prazo chegando e, na sua cabeça — ou numa folha de papel, ou num bloco de notas —, há uma lista de assuntos que precisam entrar no relatório. Mas tudo parece solto, sem ordem, e você não sabe qual seção vem antes da outra. Em vez de sentar e estruturar manualmente por meia hora, você vai pedir ao Claude que faça isso em dois minutos — e depois você decide o que muda.

### 🧰 O que você vai usar

- Word com o painel Claude aberto à direita
- Suas notas soltas (pode ser qualquer tema; usaremos um exemplo para guiar)

### 👐 Mão na massa

1. Abra um documento em branco no Word.
2. No painel Claude (lado direito), clique no campo de texto — o cursor vai piscar lá.
3. Digite ou cole o prompt abaixo, **substituindo os itens da lista pelos seus próprios tópicos**:

> Sou professor do ensino superior e preciso criar um relatório sobre a adoção de IA em universidades públicas brasileiras. Tenho estes tópicos soltos:
> — resistência docente
> — benefícios para pesquisa
> — custo de infraestrutura
> — conformidade com a LGPD
> — exemplos de sucesso no exterior
> — risco de plágio acadêmico
>
> Crie um outline profissional e hierarquizado, com Introdução, três seções de desenvolvimento e Conclusão. Cada seção deve ter dois subtópicos. Use numeração (1., 1.1, 1.2...).

4. Pressione Enter ou clique em Enviar.
5. Aguarde a resposta — leva alguns segundos.
6. Leia o outline que o Claude devolveu. Anote mentalmente: *faz sentido a ordem? Falta algo importante?*
7. Se quiser ajustar, envie uma resposta de acompanhamento diretamente no painel, por exemplo:

> Troque a seção 2 de lugar com a seção 3. E adicione um subtópico sobre "impacto nas avaliações discentes" na seção de benefícios.

8. Copie o outline final (selecione o texto no painel e use Ctrl+C).
9. Cole no documento Word (Ctrl+V) — apenas para guardar enquanto você avança.

📸 *Sugestão de captura de tela: o painel Claude à direita exibindo o outline numerado, com o documento Word vazio à esquerda.*

> 💡 **Dica:** Quanto mais contexto você der no prompt — público-alvo, tamanho do documento, tom desejado —, melhor o Claude vai estruturar. "Crie um outline sobre IA" é como pedir uma pizza sem dizer o tamanho nem os ingredientes.

### ✅ Deu certo?

Você tem um outline com pelo menos três seções numeradas, cada uma com dois subtópicos, colado no seu documento Word. Se olhar para ele e conseguir imaginar o que vai escrever em cada parte, a oficina foi um sucesso.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O painel Claude não aparece no Word | Vá em **Inserir → Meus Suplementos** e verifique se Claude for Word está listado. Se não estiver, reinstale pelo Obter Suplementos. |
| O Claude devolveu texto corrido, sem numeração | Adicione no final do prompt: "Formate em lista numerada hierárquica (1., 1.1, 1.2, 2., 2.1...)". |
| O outline ficou genérico demais | Inclua no prompt mais contexto específico: institução, público que vai ler, objetivo do documento. |

### 🚀 Quer ir além?

- Peça ao Claude para estimar quantas páginas cada seção do outline vai ter, dado o total desejado.
- Solicite que ele aponte qual seção é a mais crítica para o argumento central do documento.
- Experimente pedir outlines para dois ângulos diferentes do mesmo tema e compare qual faz mais sentido.

---

<div style="page-break-after: always;"></div>

# Oficina 2 — Escreva no Claude, Cole no Word Sem Perder a Formatação

### 🎯 O Problema

Você pediu ao Claude que redigisse uma seção do relatório, a resposta ficou ótima — e aí você colou no Word e... virou um bloco de texto sem título, sem lista, sem nada. Parece um parágrafo gigante sem forma. Isso acontece porque o Claude escreve usando uma linguagem chamada Markdown (explicação em 10 segundos logo abaixo) e o Word às vezes não sabe o que fazer com ela. Nesta oficina você vai aprender o caminho certo para que a estrutura apareça direitinho.

### 🧰 O que você vai usar

- Word com o painel Claude aberto
- O outline que você criou na Oficina 1 (ou qualquer tema de sua escolha)

> 🤓 **O que é Markdown?** É uma forma de escrever formatação usando símbolos simples. `#` na frente de uma linha vira título grande. `##` vira título médio. `-` vira um item de lista. `**texto**` vira negrito. O Claude usa Markdown automaticamente quando produz textos estruturados — e o Word consegue interpretar isso, desde que você cole do jeito certo.

### 👐 Mão na massa

1. No painel Claude, envie este prompt (adapte o tema se quiser):

> Escreva a seção de Introdução de um relatório sobre adoção de IA em universidades públicas brasileiras. Use Markdown puro. Inclua:
> - Um título principal com #
> - Dois subtítulos com ##
> - Pelo menos uma lista com marcadores (-)
> - Aproximadamente 300 palavras
>
> Escreva apenas o conteúdo em Markdown. Nada de explicações antes ou depois.

2. Quando a resposta aparecer, selecione TODO o texto da resposta no painel.
3. Copie com Ctrl+C.
4. No documento Word, clique numa área em branco abaixo do outline da Oficina 1 (ou num documento novo).
5. **Antes de colar**: vá em **Página Inicial → Colar → Colar Especial → Texto Unicode** — isso garante que os símbolos Markdown cheguem inteiros.

   📸 *Sugestão de captura de tela: o menu "Colar Especial" aberto, com a opção "Texto Unicode" destacada.*

6. Após colar, selecione a linha que começa com `#` (o título principal).
7. Vá em **Página Inicial → Estilos** e clique em **Título 1**.
8. Selecione as linhas que começam com `##` e aplique **Título 2**.
9. Selecione os itens de lista que começam com `-` e aplique **Lista com Marcadores** (ou apenas veja se o Word já converteu automaticamente).

> ⚠️ **Cuidado:** Se você simplesmente pressionar Ctrl+V sem usar Colar Especial, o Word pode converter o Markdown de formas inesperadas — às vezes bem, às vezes mal. Usar Colar Especial → Texto Unicode garante consistência.

10. Volte ao painel Claude e envie:

> Agora escreva também a seção "1.1 Contexto Brasileiro" em Markdown puro, com ## no título, dois parágrafos de texto corrido e uma lista numerada com três itens.

11. Repita os passos 2 a 9 para esta nova seção.

### ✅ Deu certo?

No seu documento Word, você vê pelo menos um título formatado em negrito e tamanho maior (Título 1) e um subtítulo levemente menor (Título 2). O texto de corpo aparece em parágrafo normal, e a lista tem marcadores ou números visíveis — não traços e hífens soltos.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O Word não reconheceu os títulos `#` automaticamente | Aplique os estilos manualmente: selecione a linha → Página Inicial → Estilos → Título 1. |
| A lista com `-` virou texto corrido | Selecione as linhas → Página Inicial → clique no ícone de Lista com Marcadores. |
| O texto colado está em fonte diferente do resto do documento | Selecione tudo (Ctrl+A) → Página Inicial → Limpar Toda a Formatação → reaplique os estilos desejados. |

### 🚀 Quer ir além?

- Peça ao Claude para gerar uma tabela em Markdown com três colunas e veja como ela aparece ao ser colada no Word.
- Solicite que ele produza o documento inteiro de uma vez em Markdown e experimente colar tudo junto.
- Ative a conversão automática de Markdown no Word: **Arquivo → Opções → Verificação → AutoCorreção → Formatação Automática** e procure a opção de substituição de Markdown.

---

<div style="page-break-after: always;"></div>

# Oficina 3 — Faça seu Texto Fluir: Clareza, Tom e Coesão

### 🎯 O Problema

Você releu o que escreveu e sentiu aquele desconforto: repetição de palavras, frases longas demais que cansam antes de terminar, tom ora muito formal ora muito casual, e parágrafos que parecem não ter conversa entre si. Você sabe que o texto precisa melhorar, mas não sabe exatamente onde mexer. O Claude vai funcionar como um editor de texto experiente — e você decide o que aceita ou não das sugestões.

### 🧰 O que você vai usar

- Um trecho de texto com pelo menos três parágrafos — pode ser algo que você já escreveu ou o texto gerado na Oficina 2
- Word com o painel Claude aberto

### 👐 Mão na massa

**Parte A — Edição de clareza (frases longas e repetição)**

1. Selecione um parágrafo do seu documento que pareça confuso ou longo demais.
2. Copie-o (Ctrl+C).
3. No painel Claude, cole o trecho e envie este prompt:

> Revise este parágrafo para melhorar a clareza. Faça o seguinte:
> 1. Quebre frases com mais de 25 palavras em frases menores
> 2. Elimine adjetivos redundantes (como "muito importante" → "essencial")
> 3. Use voz ativa sempre que possível
> 4. O público é formado por gestores sem formação técnica em IA
>
> Mostre primeiro a lista de mudanças que você faria e por quê. Depois apresente a versão revisada.
>
> TRECHO:
> [cole o seu parágrafo aqui]

4. Leia a análise do Claude. Veja se as razões fazem sentido para você.
5. Copie a versão revisada e substitua o trecho original no Word.

📸 *Sugestão de captura de tela: o painel Claude exibindo a lista "Mudanças sugeridas" e abaixo a versão revisada do parágrafo.*

**Parte B — Edição de tom**

6. Escolha um segundo parágrafo — de preferência um que pareça excessivamente formal ou, ao contrário, informal demais.
7. No painel Claude, envie:

> Reescreva este trecho com tom profissional mas acessível — sem jargão excessivo, sem ser coloquial. O leitor é um coordenador pedagógico de escola pública que não tem familiaridade com tecnologia. O objetivo é persuadi-lo de que a mudança proposta é viável.
>
> Mostre: versão "Antes" e versão "Depois", com uma linha explicando cada mudança principal.
>
> TRECHO:
> [cole o seu parágrafo aqui]

8. Compare Antes e Depois. Aceite as mudanças que fazem sentido, ignore as que distorcem sua intenção.

**Parte C — Coesão entre parágrafos**

9. Selecione dois parágrafos consecutivos do seu documento que pareçam desconectados.
10. Envie ao Claude:

> Estes dois parágrafos estão soltos. Adicione uma transição que os conecte logicamente — uma frase de fechamento no primeiro ou de abertura no segundo, usando conectores como "No entanto", "Em decorrência disso", "Apesar disso" ou similares. Não reescreva os parágrafos inteiros.
>
> PARÁGRAFO 1:
> [cole aqui]
>
> PARÁGRAFO 2:
> [cole aqui]

11. Aplique a sugestão ao documento.

> 💡 **Dica:** Se você não gostou de nenhuma das transições sugeridas, responda ao Claude: "Não gostei dessas opções. Me dê três alternativas usando conectores diferentes." Ele vai gerar novas possibilidades.

### ✅ Deu certo?

Você tem pelo menos um parágrafo mais curto e mais direto que a versão original, um trecho com tom ajustado ao público e dois parágrafos que agora se encadeiam com naturalidade. Leia os três em voz alta — se não travar, funcionou.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O Claude reescreveu tudo e perdeu a ideia original | Adicione no prompt: "Não mude o conteúdo nem a argumentação — apenas o estilo." |
| As sugestões soam artificiais ou robóticas | Peça: "Reescreva de forma mais natural, como se fosse um professor experiente explicando para um colega." |
| A versão revisada ficou maior que o original | Inclua: "A versão revisada deve ter no máximo o mesmo número de palavras que o original." |

### 🚀 Quer ir além?

- Peça ao Claude para revisar uma seção inteira de uma vez, passando contexto sobre o público e o objetivo do documento.
- Solicite que ele classifique cada parágrafo do trecho com uma nota de 1 a 5 em clareza, e comece pelos de nota mais baixa.
- Experimente pedir dois estilos diferentes para o mesmo parágrafo (ex.: "versão mais formal" e "versão mais direta") e escolha a que mais combina com seu documento.

---

<div style="page-break-after: always;"></div>

# Oficina 4 — Encontre as Contradições Antes que os Outros Encontrem

### 🎯 O Problema

Você finalizou o relatório, mandou para um colega revisar — e ele voltou dizendo que a seção 2 fala uma coisa e a seção 4 fala outra. Ou pior: o documento foi publicado e alguém apontou a inconsistência numa reunião. Esta oficina ensina você a usar o Claude como um crítico editorial que lê seu texto com olhos de detetive, antes que mais ninguém faça isso.

### 🧰 O que você vai usar

- Um trecho com pelo menos duas seções ou três parágrafos — pode ser o que você produziu nas oficinas anteriores
- Word com o painel Claude aberto

### 👐 Mão na massa

**Parte A — Encontrando contradições**

1. Separe dois trechos do seu documento que estejam em seções diferentes — por exemplo, a Introdução e a Conclusão, ou duas seções de desenvolvimento.
2. No painel Claude, envie:

> Leia estes dois trechos do meu documento. Verifique se há contradições entre eles — afirmações que se contradizem, dados inconsistentes ou posições diferentes sobre o mesmo ponto.
>
> Para cada contradição encontrada, informe:
> - Qual é a contradição exata (cite os trechos)
> - Qual seção está mais alinhada com o argumento central
> - Como resolver (reescrever A, reescrever B, ou reconhecer as duas perspectivas)
>
> TRECHO A (Seção de Introdução):
> [cole aqui]
>
> TRECHO B (Seção de Conclusão):
> [cole aqui]

3. Se o Claude não encontrar contradições reais, ótimo — documente isso como um ponto positivo. Se encontrar, anote cada uma.

**Parte B — Caçando generalizações sem evidência**

4. Escolha três afirmações do seu texto que soem absolutas — frases com "todos", "sempre", "nenhum", "comprovadamente", "certamente".
5. Envie ao Claude:

> Analise estas três afirmações do meu documento. Para cada uma, me diga:
> - É uma afirmação de fato verificável, ou uma generalização sem evidência?
> - Como eu poderia reformulá-la de forma mais precisa e defensável?
>
> AFIRMAÇÃO 1: [cole aqui]
> AFIRMAÇÃO 2: [cole aqui]
> AFIRMAÇÃO 3: [cole aqui]

6. Para cada generalização apontada, revise o texto no Word antes de continuar.

**Parte C — Verificando consistência de tom**

7. Cole três trechos de seções diferentes do documento e envie:

> Leia estes três trechos e me diga: o tom é consistente entre eles, ou há mudanças de postura, formalidade ou otimismo que podem confundir o leitor? Me dê um diagnóstico de uma frase por trecho.
>
> TRECHO 1: [cole aqui]
> TRECHO 2: [cole aqui]
> TRECHO 3: [cole aqui]

8. Se o diagnóstico apontar inconsistência, volte à Oficina 3 e aplique o ajuste de tom no trecho problemático.

> ⚠️ **Cuidado:** Nem toda crítica do Claude vai proceder. Ele pode apontar uma "contradição" que, na verdade, é uma distinção intencional que você fez entre contextos diferentes. Leia com atenção e decida — você é o autor, não ele.

📸 *Sugestão de captura de tela: o painel Claude exibindo a análise com as contradições identificadas em formato de lista, com os trechos citados.*

### ✅ Deu certo?

Você passou pelo seu documento com olhos de crítico e chegou a uma das duas conclusões possíveis: (a) encontrou e corrigiu ao menos um problema real, ou (b) confirmou que o texto está consistente. Qualquer um dos dois resultados é uma vitória — você agora sabe que o documento foi testado.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O Claude disse "não encontrei contradições" mas você sabe que há | Seja mais específico: cite exatamente as duas afirmações que parecem conflitar e peça uma análise direta. |
| A análise veio muito genérica, sem citar trechos | Adicione no prompt: "Cite os trechos exatos que evidenciam cada problema que você apontar." |
| O Claude apontou muitos problemas e você não sabe por onde começar | Peça: "Ordene os problemas encontrados do mais crítico para o menos crítico, considerando o impacto na credibilidade do documento." |

### 🚀 Quer ir além?

- Peça ao Claude que simule a reação de um leitor cético ao seu argumento central e liste as três objeções que ele levantaria.
- Solicite que ele verifique se todas as recomendações do documento têm uma justificativa explícita — ou se alguma "aparece do nada".
- Peça uma leitura focada em bias: "Há suposições não questionadas sobre o comportamento de professores, estudantes ou gestores neste texto?"

---

<div style="page-break-after: always;"></div>

# Projeto Final — Documento Profissional do Zero ao Entregável

### 🎯 A missão

Você vai produzir, do início ao fim, um documento profissional real — um relatório, uma proposta ou um manual de pelo menos cinco páginas — usando tudo o que praticou nas quatro oficinas. O Claude vai ajudar em cada etapa, mas quem decide, revisa e assina é você. No final, você terá um arquivo Word com índice automático, estilos aplicados, texto revisado e checklist de qualidade preenchido.

Escolha um dos tipos de documento abaixo — de preferência algo que você realmente precise produzir:

- **Tipo A — Relatório:** sobre uma iniciativa, resultado ou diagnóstico da sua área
- **Tipo B — Proposta:** justificando uma mudança, adoção de ferramenta ou nova metodologia
- **Tipo C — Manual ou guia:** orientações práticas para uma equipe ou turma

### 👐 Mão na massa

**Etapa 1: Estrutura (aplica o que você fez na Oficina 1)**

1. Abra um documento novo no Word.
2. No painel Claude, envie um prompt de outline com: tipo de documento, tema, público-alvo, objetivo, tamanho estimado e os tópicos que você já tem em mente.
3. Revise o outline recebido, faça os ajustes necessários e cole no documento Word como ponto de partida.

**Etapa 2: Redação colaborativa (aplica o que você fez na Oficina 2)**

4. Para cada seção do outline, envie ao Claude um prompt de redação com: título da seção, contexto do documento inteiro, público, tom e tamanho esperado.
5. Peça sempre o resultado em Markdown puro.
6. Cole cada seção no Word usando Colar Especial → Texto Unicode.
7. Aplique os estilos (Título 1, Título 2, Normal) logo após colar cada seção — não deixe para o final.

> 📌 **Não esqueça:** ao pedir a redação de cada seção, inclua um resumo de uma linha do que as seções anteriores disseram. Isso ajuda o Claude a manter a coesão sem que você precise mandar o documento inteiro toda vez.

**Etapa 3: Revisão de estilo (aplica o que você fez na Oficina 3)**

8. Depois que todas as seções estiverem redigidas, releia o documento inteiro uma vez.
9. Marque os trechos que parecerem confusos, formais demais ou desconexos.
10. Envie cada trecho marcado ao Claude com o prompt de revisão da Oficina 3 — especificando o nível (clareza, tom ou coesão).
11. Aplique as mudanças que fizerem sentido para você.

**Etapa 4: Revisão crítica (aplica o que você fez na Oficina 4)**

12. Envie ao Claude a Introdução e a Conclusão juntas e peça verificação de contradições.
13. Escolha três afirmações fortes do documento e peça análise de generalização.
14. Corrija o que for necessário.

**Etapa 5: Formatação e índice**

15. Confirme que todos os títulos estão com os estilos corretos (Título 1, Título 2, Título 3).
16. Posicione o cursor logo após o título do documento.
17. Vá em **Referências → Índice → Índice Automático 1**.
18. Verifique se todas as seções aparecem no índice.
19. Faça qualquer ajuste final de formatação (margens, espaçamento, fonte do corpo).

📸 *Sugestão de captura de tela: o documento Word com o índice automático gerado na primeira página, mostrando os títulos e números de página.*

**Etapa 6: Checklist de validação**

20. Preencha o checklist da próxima seção. Só publique ou envie o documento depois que todos os itens estiverem marcados.

### 🏁 Como saber que terminou

- [ ] O documento tem pelo menos cinco páginas de conteúdo
- [ ] O outline foi revisado e aprovado por você antes da redação
- [ ] Todas as seções do outline têm conteúdo redigido
- [ ] Os estilos Título 1, Título 2 e Normal estão aplicados corretamente
- [ ] O índice automático foi gerado e está atualizado
- [ ] Pelo menos dois trechos passaram pela revisão de estilo (clareza, tom ou coesão)
- [ ] A Introdução e a Conclusão foram verificadas quanto a contradições
- [ ] Nenhuma generalização sem evidência ficou no texto sem qualificação
- [ ] Não há dados pessoais identificáveis de terceiros sem anonimização
- [ ] Você releu o documento inteiro ao menos uma vez do início ao fim
- [ ] O arquivo está salvo com nome final, sem "rascunho" ou "v0.3" no nome

---

<div style="page-break-after: always;"></div>

# A Parte dos Dez — Dez Prompts que Você Vai Usar Toda Semana

A coleção Para Leigos tem uma tradição: a "Parte dos Dez". Aqui você encontra dez prompts prontos, testados e imediatamente úteis para o seu dia a dia com o Claude for Word. Copie, adapte e use à vontade.

**1. Outline rápido**

> Crie um outline para um [tipo de documento] sobre [tema], com introdução, três seções e conclusão. Público: [quem vai ler]. Tamanho: [número] páginas. Use numeração hierárquica (1., 1.1, 1.2...).

**2. Redação de seção com contexto**

> Redija a seção "[título da seção]" em Markdown puro. Contexto: este é um [tipo de documento] sobre [tema], destinado a [público]. As seções anteriores abordaram [resumo em uma frase]. Esta seção deve ter aproximadamente [número] palavras.

**3. Revisão de clareza**

> Revise este parágrafo para melhorar a clareza. Quebre frases longas, elimine adjetivos redundantes e use voz ativa. Mostre primeiro as mudanças propostas e depois a versão revisada. TRECHO: [cole aqui]

**4. Ajuste de tom**

> Reescreva este trecho com tom [profissional e acessível / mais formal / mais direto]. Público: [quem vai ler]. Objetivo: [o que você quer que o leitor faça ou sinta]. Mostre Antes e Depois. TRECHO: [cole aqui]

**5. Transição entre parágrafos**

> Estes dois parágrafos estão desconectados. Adicione uma frase de transição — no final do primeiro ou no início do segundo — que os conecte logicamente, sem reescrever o restante. P1: [cole aqui] P2: [cole aqui]

**6. Verificação de contradições**

> Estes dois trechos do meu documento se contradizem? Se sim, qual é a contradição e como eu resolvo? TRECHO A: [cole aqui] TRECHO B: [cole aqui]

**7. Caça a generalizações**

> Analise estas afirmações. Alguma é uma generalização sem evidência? Se sim, sugira uma reformulação mais defensável. AFIRMAÇÕES: [liste aqui]

**8. Resumo executivo**

> Leia o trecho abaixo e escreva um resumo executivo de [número] palavras, destacando o problema, a solução proposta e o próximo passo recomendado. TEXTO: [cole aqui]

**9. Checklist de formatação ABNT**

> Quais são os requisitos de formatação ABNT para um [tipo de documento] com [número] páginas, incluindo tabelas e citações diretas? Liste em ordem de prioridade, com um exemplo concreto para cada item.

**10. Crítica editorial completa**

> Faça uma análise crítica severa deste trecho. Para cada problema, informe o tipo (contradição, generalização, lacuna lógica, promessa sem evidência), a localização e uma sugestão de correção. Formato: ❌ Problema | 📍 Onde | 💡 Sugestão. TRECHO: [cole aqui]

---

## Conseguiu! E agora?

Se você chegou até aqui — e especialmente se completou o Projeto Final —, você acabou de fazer algo que muita gente acha complicado: usou IA de verdade, para um documento real, mantendo você no comando de cada decisão. O Claude sugeriu, você julgou. O Claude redigiu, você revisou. Esse é o jeito certo de trabalhar com inteligência artificial — e você já sabe fazer isso.

O próximo passo é simples: use o mesmo fluxo no próximo documento que você precisar produzir. Pode ser um ofício, um relatório de pesquisa, uma proposta de projeto, um plano de aula, um artigo. Cada vez que você repetir o processo — outline, redação, revisão de estilo, revisão crítica, formatação —, ele vai ficar mais rápido e mais natural. E quando você se pegar ajustando os prompts instintivamente para conseguir exatamente o que quer, é sinal de que a habilidade virou sua — não da IA.

Se quiser ir além, explore o Claude Desktop (uma versão que funciona no seu computador sem precisar do painel no Word, e que permite carregar arquivos localmente) e o uso do Claude para documentos mais sensíveis, com dados que você não quer enviar para a nuvem. Mas isso é história para o próximo curso. Por enquanto: salva esse arquivo, abre seu próximo documento em branco e vai.
