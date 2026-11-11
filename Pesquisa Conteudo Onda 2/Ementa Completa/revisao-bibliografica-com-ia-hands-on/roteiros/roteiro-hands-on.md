# Revisão Bibliográfica com IA Para Leigos — Roteiro Final (Hands-on)

*Ao final, você terá transformado um tema solto em pergunta, buscado em três lugares, triado,
extraído dados conferidos no artigo e entregado uma mini-revisão que qualquer pessoa consegue
refazer — com fluxograma PRISMA e tudo.*

**Público-Alvo:** estudantes, pesquisadores, jornalistas e analistas (trilha T2 — Pesquisa com IA,
último curso da trilha).

**Objetivo Geral:** você vai conduzir, com as próprias mãos, uma mini-revisão de literatura com
Semantic Scholar, Consensus e Elicit, completando com uma base brasileira, e vai deixar cada passo
anotado numa planilha que prova de onde veio cada dado.

**Pré-requisitos:** saber fazer uma pergunta a um assistente de IA; computador com navegador e
internet; contas gratuitas no Consensus e no Elicit (o Semantic Scholar funciona sem conta). Ajuda
muito ter feito *Checagem de Fontes e Citações - Essentials*.

> Dados e interfaces consultados em 04/11/2026. Onde aparece [conferir], o nome do botão ou o
> caminho ainda precisa ser validado na tela antes da gravação.

## Estrutura do Curso

| Nível | Parte | Tempo |
|---|---|---|
| Preparação | Antes de Arregaçar as Mangas | 7 min |
| Nível 1 — Planejar e buscar | Oficinas 1 e 2 | 40 min |
| Nível 2 — Selecionar e extrair | Oficinas 3 e 4 | 40 min |
| Integração | Projeto Final — Mini-revisão rastreável | 22 min |
| Anexo | A Parte dos Dez | 6 min |
| | **Total** | **115 min** |

Cada oficina tem três partes: **guiada** (você faz junto, no caso da telessaúde), **sua vez** (você
repete sozinho) e **Deu certo?** (você confere com o gabarito).

---

## Antes de Arregaçar as Mangas

### O que você precisa ter aberto agora

- **📸 Sugestão de Prints:** navegador com quatro abas — `semanticscholar.org`, `consensus.app`
  (logado, avatar visível no canto), `elicit.com` (logado, tela inicial do Research Agent) e a
  planilha com as quatro abas visíveis embaixo.

Revisão de literatura é trabalho de abas e de anotação. Deixe abertos:

1. `semanticscholar.org` — não precisa de conta para buscar.
2. `consensus.app`, com conta gratuita. Você tem Paper search à vontade, 10 mensagens Pro por mês
   [conferir: uma página de ajuda ainda fala em 15] e 3 Deep por mês. Este curso gasta no máximo
   duas mensagens Pro e nenhuma Deep.
3. `elicit.com`, com conta gratuita (Basic). O Research Agent tem uso limitado; o curso usa duas
   execuções.
4. Sua planilha, com quatro abas:

| Aba | Colunas |
|---|---|
| Log | Data · Onde buscou · Consulta exata · Filtros · Total exibido |
| Triagem | ID · Título · Onde achou · Decisão (incluir / excluir / incerto) · Motivo |
| Extração | ID · País · Desenho · Amostra · Resultado · Página e trecho · Texto completo ou só resumo? · Conferido? |
| Síntese | Frase · Tipo · Referência · Trecho |

> 💡 Revisão bem anotada é como receita bem escrita: outra pessoa segue e chega ao mesmo bolo. A
> planilha é a sua receita.

### Semáforo: o que pode ir para a ferramenta

| Cor | Exemplos | O que fazer |
|---|---|---|
| Verde | Sua pergunta; termos de busca; PDF de artigo de acesso aberto | Pode usar |
| Amarelo | PDF baixado pelo Portal CAPES; capítulo seu ainda não publicado | Confira a licença e combine com orientador ou coautores antes |
| Vermelho | Prontuários, dados de participantes, parecer sigiloso, manuscrito de outra pessoa | Não envie |

Por quê: o Elicit pode processar dados nos Estados Unidos com provedores de modelo; o Consensus
repassa consultas e uploads a OpenAI, Anthropic, Google e Baseten (sem usar para treino, segundo a
política). O Semantic Scholar busca sem conta.

> ⚠️ Systematic Review do Elicit e exportação de tabela em CSV são pagos. Você **não** precisa deles:
> a planilha faz esse papel.

### A regra das cinco etapas

Toda revisão passa por: **pergunta → busca → triagem → extração → síntese**. Cada uma deixa uma
pegada na planilha. Se a pegada não está lá, para quem lê a revisão a etapa não aconteceu.

> 🔑 **Regra de ouro:** a IA encontra e resume; você confere e anota. Dado sem página não entra.

### Solução de Problemas

| Problema | O que fazer |
|---|---|
| O Elicit não deixa buscar | Termine o Sign up; ele exige conta desde a primeira busca |
| O Consensus pede cadastro na segunda busca | Normal; crie a conta gratuita |
| Interface em inglês | O curso dá os nomes em inglês e explica cada um |

## Descrição

- **Objetivos da Aula:** preparar contas, planilha e semáforo de dados; apresentar as cinco etapas.
- **Habilidades Esperadas:** deixar o ambiente pronto e decidir sozinho se um material pode ir para
  uma ferramenta.
- **Pílula Hands-on:** abas abertas, planilha criada, data de hoje na primeira linha do Log.

---

## Oficina 1 — Transforme um tema em pergunta

### 🎯 O Problema

Seu orientador (ou editor, ou chefe) pediu "uma revisão sobre telessaúde e hipertensão". Isso é um
tema, não uma pergunta — e tema não diz o que buscar nem o que descartar. Você vai transformá-lo em
pergunta, critérios e termos antes de abrir qualquer buscador.

### 🧰 O que você vai usar

- `decs.bvsalud.org` (descritores em saúde, gratuito)
- Sua planilha (topo da aba Log)

### 👐 Mão na massa — parte guiada

- **📸 Sugestão de Prints:** página do DeCS com "hipertensão" na caixa de busca e o registro do
  descritor aberto, mostrando os nomes em português e inglês e a lista de sinônimos.

1. Escreva a pergunta numa frase:

   > Em adultos com hipertensão atendidos na atenção primária brasileira, intervenções de
   > telessaúde melhoram o controle da pressão arterial em comparação ao cuidado usual?

2. Separe em PICO (Paciente/População, Intervenção, Comparação, Desfecho — "Outcome"):
   P = adultos com hipertensão na atenção primária no Brasil; I = telessaúde; C = cuidado usual;
   O = controle da pressão arterial.
3. Escreva os critérios **antes** de buscar:

   > Incluir: estudos empíricos com adultos no Brasil, atenção primária, intervenção de telessaúde
   > e resultado de pressão arterial. Excluir: protocolos, editoriais, estudos sem resultado clínico
   > e estudos fora do Brasil.

4. Abra `decs.bvsalud.org`, busque "hipertensão" e depois "telessaúde". Anote o descritor em
   português e em inglês e dois sinônimos de cada [conferir os descritores exibidos].
5. Monte sua lista de termos em inglês: `hypertension`, `telehealth`, `telemedicine`,
   `primary health care`, `blood pressure`.

> 🤓 DeCS é um "índice remissivo" comum a milhares de artigos: autores escrevem "pressão alta" ou
> "hipertensão arterial", e o descritor junta tudo. Ele deriva do MeSH, o vocabulário do PubMed.

### 👐 Mão na massa — sua vez

Escolha **uma** destas perguntas (é ela que você vai levar até o Projeto Final) — ou use uma sua:

| Área | Pergunta | Use |
|---|---|---|
| Educação | Quais efeitos e barreiras das metodologias ativas no ensino superior brasileiro? | PCC |
| Comunicação | Quais fatores explicam crença em desinformação nas redes sociais no Brasil? | PICo |
| Direito | Quais riscos e salvaguardas são discutidos para IA em decisões judiciais brasileiras? | PCC |
| Gestão pública | Como o orçamento participativo afeta transparência e participação no Brasil? | PICo |

PCC = População, Conceito, Contexto (para mapear um campo). PICo = População, fenômeno de Interesse,
Contexto (para entender experiências e fatores). Separe os componentes, escreva dois critérios de
inclusão e um de exclusão e liste os termos em inglês.

### ✅ Deu certo?

Sua pergunta tem os três (ou quatro) componentes com nome, e cada critério sai de um componente.
Exemplo para educação: P = estudantes e docentes do ensino superior; C = metodologias ativas
(efeitos e barreiras); C = instituições brasileiras; incluir estudos no Brasil que relatem efeitos
ou barreiras; excluir textos de opinião sem dados.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não sei se é PICO, PICo ou PCC | Tem intervenção e comparação? PICO. Quer entender experiência ou fator? PICo. Quer mapear o que existe? PCC |
| O DeCS não acha o termo | Tente sinônimo ou termo mais amplo; fora da saúde, pule o DeCS e use sinônimos |
| Critério ficou vago ("estudos bons") | Reescreva com algo que dá para ver no resumo: país, população, tipo de estudo |

### 🚀 Quer ir além?

1. Monte a expressão para a BVS: (termos de I unidos por OR) AND (termos de P unidos por OR). Valida
   se cada conceito está entre parênteses.
2. Reescreva sua pergunta com recorte de tempo (ex.: 2015–2026). Valida se o critério de inclusão
   ganhou o período.
3. Procure seus termos no MeSH (`meshb.nlm.nih.gov`) e compare com o DeCS. Valida se você anotou
   uma diferença.

## Descrição

- **Objetivos da Aula:** praticar PICO/PICo/PCC, critérios antes da busca e conversão em termos.
- **Habilidades Esperadas:** transformar sozinho um tema em pergunta com critérios e termos.

---

## Oficina 2 — Busque em três lugares e anote tudo

### 🎯 O Problema

Cada ferramenta enxerga um pedaço da literatura. Buscar num lugar só é como procurar as chaves só
debaixo do poste porque lá tem luz. Você vai buscar em três lugares — e deixar o caminho anotado.

### 🧰 O que você vai usar

- Semantic Scholar (sem conta)
- Consensus (1 mensagem Pro)
- BVS (`bvsalud.org`) ou SciELO (`scielo.org`)
- Aba Log

### 👐 Mão na massa — parte guiada

- **📸 Sugestão de Prints:** Semantic Scholar com `telehealth hypertension Brazil`, o total "About"
  visível e o painel de filtros aberto em Date Range; Consensus com a pergunta digitada, o seletor
  mostrando Pro e o menu Filter aberto; aba Log com três linhas.

1. No Semantic Scholar, digite `telehealth hypertension Brazil` (sem AND, sem OR) e tecle Enter.
2. Anote no Log: data, consulta exata, filtros (nenhum) e o total (em 04/11/2026 eram cerca de 8.230).
3. Aplique Date Range (últimos dez anos) e anote a nova linha.
4. No Consensus, cole:

   > Compare estudos brasileiros sobre telessaúde para hipertensão na atenção primária. Separe
   > ensaios, observacionais e implementação; cite cada afirmação e indique quando só o resumo foi
   > lido.

5. Escolha o modo Pro e, em Filter, restrinja o país ao Brasil se a opção aparecer [conferir].
   Anote no Log.
6. Abra dois estudos citados na resposta e leia o resumo de cada um no próprio artigo.
7. Na BVS, busque `hipertensão AND (telessaúde OR telemedicina)` (ou na SciELO, `telessaúde
   hipertensão`) e anote no Log.

> ⚠️ O Semantic Scholar **não** aceita AND, OR nem curingas. Colar uma estratégia booleana ali
> piora a busca. Lá, faça consultas curtas separadas, uma por sinônimo. Booleano é para BVS e SciELO.

> ⚠️ O Consensus Meter (aquela barrinha de "sim/não") só aparece para pergunta de sim ou não e
> resume a direção dos estudos. Não é certeza, e "tipo de estudo" classificado pela ferramenta não é
> qualidade.

### 👐 Mão na massa — sua vez

Repita os passos 1, 2, 4 e 7 com a pergunta que você escolheu na Oficina 1 (use os termos em
inglês no Semantic Scholar; termos em português na BVS ou SciELO). Fora da saúde, prefira SciELO ou
BDTD (`bdtd.ibict.br`) à BVS.

### ✅ Deu certo?

Seu Log tem pelo menos sete linhas (quatro do caso-guia, três da sua pergunta), cada uma com data,
consulta exata, filtros e total. E você sabe responder: os 8.230 do Semantic Scholar e os 433,1 mil
registros que o Consensus mostrou no painel (04/11/2026) **não** medem a mesma coisa — e nenhum diz
quantos estudos servem. Isso só a triagem diz.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O Meter não aparece | Normal em pergunta aberta; use a síntese em texto ou reformule como sim/não |
| Acabaram as mensagens Pro | Use Paper search (ilimitado) e abra os estudos você mesmo |
| Total muda de um dia para outro | Normal; é por isso que a data vai no Log |

### 🚀 Quer ir além?

1. Repita a busca do Semantic Scholar em português, entre aspas, e compare o total. Valida se o Log
   tem as duas linhas.
2. No Semantic Scholar, crie conta, salve 5 artigos com Save to Library e crie um Research Feed
   (marque 5 relevantes e 3 "less like this"). Valida se o feed sugeriu artigos novos.
3. Exporte a Library em BibTeX (`Account > Research > Library > Export`) e importe no Zotero
   (`File > Import… > A file`). Valida se as referências aparecem no Zotero.

## Descrição

- **Objetivos da Aula:** praticar busca semântica, busca booleana e registro no Log.
- **Habilidades Esperadas:** buscar sozinho em três fontes complementares e deixar o caminho
  anotado para outra pessoa repetir.

---

## Oficina 3 — Trie sem se enganar pelo título

### 🎯 O Problema

Você tem dezenas de resultados. O impulso é escolher os de título mais bonito. É assim que entram
estudos fora do critério e saem os bons de título sem graça. Você vai triar com regra — e anotar o
porquê de cada "não".

### 🧰 O que você vai usar

- Seus critérios da Oficina 1
- Os 10 primeiros resultados do caso-guia no Semantic Scholar
- Aba Triagem

### 👐 Mão na massa — parte guiada

- **📸 Sugestão de Prints:** aba Triagem com dez linhas, colunas Decisão e Motivo preenchidas, uma
  linha "incerto" destacada; ao lado, a página de um resultado do Semantic Scholar com o Abstract
  aberto.

1. Copie para a aba Triagem os 10 primeiros resultados da busca `telehealth hypertension Brazil`
   (ID, título, "Semantic Scholar").
2. Confira duplicatas: se algum título já veio da BVS ou do Consensus, marque "duplicata" e não
   conte de novo.
3. Para cada registro, abra o resumo (não o TLDR — ele é uma frase gerada, em versão beta).
4. Decida: **incluir**, **excluir** ou **incerto**. Toda exclusão leva o critério que falhou
   ("fora do Brasil", "protocolo", "sem desfecho de pressão").
5. Conte: quantos incluídos, excluídos, incertos e duplicatas. Anote embaixo da aba — esses números
   vão para o PRISMA.

### 👐 Mão na massa — sua vez

Pegue os dois "incertos" (ou dois incluídos, se não houver incerto) e abra o texto completo pelo
link de PDF do Semantic Scholar ou pelo Portal CAPES. Decida de novo, agora na etapa "texto
completo", e anote.

> 📌 "Não encontrei" não é "não existe". Escreva "não identificado nesta busca, nestas bases, nesta
> data".

### ✅ Deu certo?

Cada uma das 10 linhas tem decisão; cada exclusão tem motivo ligado a um critério; os totais da
triagem estão anotados. No teste de 04/11/2026, 6 dos 10 primeiros pareciam úteis pelo título e
resumo — o seu número pode ser outro, e tudo bem, desde que cada decisão tenha motivo.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| O resumo não diz o país | Marque "incerto" e confira no texto completo |
| Sem PDF disponível | Tente Portal CAPES (Acesso CAFe com login da sua instituição); se não der, "não recuperado" — também entra no PRISMA |
| Fiquei em dúvida entre dois critérios | Registre o primeiro que falha; consistência vale mais que perfeição |

### 🚀 Quer ir além?

1. Peça a um colega para triar os mesmos 10 com seus critérios e compare. Valida se você anotou
   quantas decisões divergiram.
2. Aplique a mesma triagem aos resultados da BVS. Valida se as duplicatas foram marcadas.
3. No Consensus, aplique Filter por desenho de estudo e veja quantos dos seus incluídos são ensaios.
   Valida se você não trocou "tipo de estudo" por "qualidade" na anotação.

## Descrição

- **Objetivos da Aula:** praticar deduplicação e triagem em duas etapas com motivo registrado.
- **Habilidades Esperadas:** triar sozinho um conjunto de registros com decisões que outra pessoa
  consegue auditar.

---

## Oficina 4 — Extraia com o Elicit e confira cada célula

### 🎯 O Problema

O Elicit monta uma tabela de dados de vários artigos em minutos. Lindo. Só que estudos
independentes acharam erros: num deles, só 51,40% das extrações estavam precisas; noutro, 82%. Você
vai usar a velocidade do Elicit sem herdar os erros.

### 🧰 O que você vai usar

- Elicit (Research Agent; 1 execução)
- Artigo aberto "Efeitos da capacitação em telessaúde..."
  (`objnursing.uff.br/nursing/article/download/6885/pdf_pt`)
- Aba Extração

### 👐 Mão na massa — parte guiada

- **📸 Sugestão de Prints:** Research Agent com a pergunta do caso-guia e a tabela; chat com "Add a
  column: Sample size" digitado; uma célula clicada com o supporting quote aberto; controle Has PDF
  ligado.

1. No Elicit, abra o Research Agent e cole a pergunta PICO da Oficina 1.
2. Se aparecer, ligue Has PDF [conferir rótulo] para priorizar artigos com texto completo.
3. No chat, peça uma coluna por vez:

   > Add a column: "Study design" — the type of study (trial, cohort, cross-sectional, qualitative).

   Repita para "Country and setting", "Sample size" e "Blood pressure outcome".

4. Clique numa célula e abra o supporting quote (o trecho de onde o Elicit diz ter tirado o dado).
5. Para dois artigos, abra o original e confira as quatro células. Copie para a aba Extração o dado
   **certo**, com página e trecho, e marque "conferido" ou "corrigido".

> 🤓 Mudou em 30/09/2026: Find Papers, Extract Data e Chat with Papers viraram parte do Research
> Agent. Se um vídeo mostrar esses botões, ele é anterior à mudança.

### 👐 Mão na massa — sua vez

1. Baixe o PDF do artigo da UFF (acesso aberto, sinal verde).
2. Preencha à mão, na aba Extração: país, desenho, população e resultado, cada um com página e
   trecho.
3. Envie o mesmo PDF ao Research Agent [conferir o botão de upload no Basic] e peça as mesmas
   quatro colunas.
4. Compare célula por célula e anote as divergências.

> ⚠️ Sem PDF, o Elicit extrai só do resumo. Marque "só resumo" na planilha sempre que for o caso.

### ✅ Deu certo?

Cada célula da aba Extração tem página e trecho do original, a coluna "texto completo ou só resumo"
está preenchida e as divergências entre você e o Elicit estão anotadas. Detalhe: esse artigo trata
de capacitação em telessaúde e talvez não meça pressão arterial [conferir] — se for o caso, ele
seria excluído do caso-guia. Notou? É a triagem conversando com a extração.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| A célula diz uma coisa e o artigo outra | Vale o artigo; anote "corrigido" |
| Acabou o uso do Research Agent | Faça a extração à mão; o método é o mesmo |
| Não acho o botão Export CSV | É do plano Plus; copie as células para a planilha |

### 🚀 Quer ir além?

1. Rode a mesma pergunta de novo no Research Agent e compare duas células com a primeira execução.
   Valida se você anotou se o resultado mudou (no estudo de 2026, só 77% se repetiram).
2. Gere um Research Report com a mesma pergunta e abra três citações. Valida se cada uma tem o
   supporting quote conferido.
3. Escreva uma coluna com instrução mais precisa ("Sample size: number of participants analyzed,
   not recruited") e compare. Valida se a coluna nova errou menos.

## Descrição

- **Objetivos da Aula:** praticar extração por colunas no Research Agent e conferência do
  supporting quote.
- **Habilidades Esperadas:** extrair dados com IA e conferir sozinho cada célula no original.

---

## Projeto Final — Mini-revisão rastreável

### 🎯 A missão

Agora a pergunta é sua: a que você escolheu na Oficina 1. Em 22 minutos você vai entregar uma
mini-revisão pequena, mas completa: busca registrada, 10 registros triados, 3 estudos extraídos,
cinco frases de síntese, fluxograma PRISMA e declaração de uso de IA. Pequena de propósito: o que
importa é que qualquer pessoa consiga refazer.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** fluxograma `prisma-2020-fluxograma-ptbr.docx` com as caixas
  preenchidas; ao lado, a aba Síntese com cinco frases e a coluna Trecho completa.

1. Confira o semáforo: nada vermelho vai para as ferramentas.
2. **Triagem:** use as buscas da sua pergunta (Oficina 2). Pegue 10 registros, marque duplicatas e
   trie com seus critérios, com motivo.
3. **Extração:** dos incluídos, escolha 3. Extraia país, desenho, amostra e resultado (com o
   Research Agent ou à mão) e confira cada célula no original.
4. **Síntese:** escreva cinco frases — duas concordâncias, uma divergência, uma limitação, uma
   lacuna. Cada frase com referência e trecho. Se ficou com menos de três incluídos, a lacuna é o
   achado: escreva isso.
5. **PRISMA:** abra `prisma-2020-fluxograma-ptbr.docx` e preencha identificados (por fonte),
   duplicatas removidas, triados, excluídos (com motivos), não recuperados e incluídos.
6. **Declaração:** cole e adapte:

   """
   Declaração de uso de IA: usei Semantic Scholar (busca), Consensus (panorama, modo Pro) e Elicit
   (Research Agent, extração assistida das colunas [quais]) em [datas]. Conferi cada dado extraído no
   artigo original e assumo a responsabilidade pelo conteúdo. Não enviei dados pessoais nem
   material inédito de terceiros.
   """

### 🏁 Como saber que terminou

- [ ] Pergunta com framework e critérios escritos antes da busca
- [ ] Log com pelo menos três buscas (incluindo uma base brasileira), cada uma com data, consulta,
      filtros e total
- [ ] 10 registros triados, cada exclusão com motivo
- [ ] 3 estudos extraídos, cada célula com página e trecho e marcação de texto completo ou só resumo
- [ ] Cinco frases de síntese com referência e trecho, sem citar o resumo da IA como se fosse o estudo
- [ ] Fluxograma PRISMA batendo com a planilha e declaração de uso de IA anexada

## Descrição

- **Objetivos da Aula:** integrar as cinco etapas numa mini-revisão da pergunta do aluno.
- **Habilidades Esperadas:** entregar sozinho uma mini-revisão rastreável, com PRISMA e declaração.

---

## A Parte dos Dez — Hábitos de Quem Revisa com IA

1. **Pergunta antes de buscador.** Tema não é pergunta.
2. **Critério antes de resultado.** Critério escrito depois da busca vira desculpa.
3. **Nenhuma ferramenta sozinha.** Pelo menos uma de IA e uma base brasileira.
4. **Semantic Scholar não fala booleano.** Consulta curta, uma por sinônimo.
5. **Anote a busca na hora.** Data, consulta exata, filtros, total. Amanhã o total muda.
6. **Total recuperado não é total relevante.** Quem diz o que serve é a triagem.
7. **TLDR e Meter são pistas.** Resumo e estudo são a prova.
8. **Supporting quote se abre.** E o dado se confere no artigo.
9. **"Só resumo" se anota.** Extração sem texto completo vale menos — e o leitor precisa saber.
10. **Declare a IA.** Ferramenta, finalidade e data, como pede o CNPq.

## Conseguiu! E agora?

Você fez o que muita revisão por aí não faz: deixou cada passo anotado. Pergunta estruturada,
busca em três lugares, triagem com motivo, dado conferido no artigo, síntese citada e PRISMA. Isso
é o que separa "a IA me deu uns artigos" de "eu revisei a literatura".

Para continuar: use a planilha na próxima revisão de verdade, com mais registros. Se a sua
instituição tiver Elicit Pro, experimente o Systematic Review — agora você sabe conferir o que ele
entrega. E para ir além da mini-revisão, os próximos degraus são o manual do JBI, o Cochrane
Handbook e a avaliação de risco de viés.

---

## Rastreabilidade da auditoria (H1–H13)

| Achado | Destino nesta versão |
|---|---|
| H1 Sem preparação | Antes de Arregaçar as Mangas (contas, cotas, planilha, semáforo) |
| H2 Sem pergunta, critérios e termos | Oficina 1 |
| H3 Sem log | Aba Log usada nas Oficinas 2 e 3 e no Projeto Final |
| H4 Meter como veredito | Oficina 2 (box ⚠️, abrir dois estudos); Parte dos Dez, item 7 |
| H5 CSV pago e conferência ausente | Oficina 4 (planilha no lugar do CSV, supporting quote, artigo UFF) |
| H6 Triagem ausente | Oficina 3 |
| H7 Síntese sem estrutura | Projeto Final, passo 4 (cinco frases tipadas com trecho) |
| H8 Projeto Final vago | Tamanho fixo (10/3/5), PRISMA, declaração, checklist de seis itens |
| H9 Segurança tardia e desafio que vaza texto | Semáforo na preparação; desafio de "revisar seu parágrafo" removido |
| H10 Um desafio sem validação | Três desafios com validação por oficina |
| H11 Bases brasileiras e Zotero | Oficina 2 (BVS/SciELO/BDTD obrigatória; Zotero no desafio 3) |
| H12 Carga | 115 min (ver `carga-horaria/carga-horaria-hands-on.md`) |
| H13 Parte dos Dez imprecisa | Itens reescritos (TLDR como pista; "só resumo" anotado em vez de "prefira PDF") |
