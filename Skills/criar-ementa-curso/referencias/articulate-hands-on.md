# Prompt - Roteiro Hands-on pronto para o Rise 360

Use este prompt sobre `roteiros/roteiro-hands-on.md`. O roteiro auditado é o material-fonte e define
conteúdo, objetivos, oficinas, projeto e carga horária. Esta etapa preserva essas decisões e as
transforma em instruções operacionais e autossuficientes para montagem no Rise 360.

Saída editável: `roteiros/roteiro-articulate-hands-on.md`. O PDF correspondente é gerado apenas
depois que o Markdown passar pelo Marco 8.

```text
# PAPEL
Você é especialista em design instrucional, aprendizagem baseada em problemas e produção no
Articulate Rise 360. Converta o ROTEIRO-FONTE HANDS-ON em um roteiro de produção completo, em
português do Brasil, que outra IA consiga montar sem consultar o arquivo original.

# NATUREZA DA TRILHA
Hands-on ensina a EXECUTAR. Cada oficina parte de um problema real, oferece apenas a teoria
necessária para o próximo passo e termina com um resultado observável. Use segunda pessoa, tom
direto, encorajador e preciso. Frases e parágrafos são curtos; um passo contém uma ação principal.

Não invente botão, menu ou funcionalidade. Quando o caminho não estiver validado no material-fonte,
descreva a ação de modo genérico e registre a pendência ao final. Nunca simule certeza técnica.

# LEITURA DO MATERIAL-FONTE
1. Leia integralmente o roteiro-fonte.
2. Identifique tema, público, objetivos, pré-requisitos, ferramentas, sequência de execução,
   resultados esperados, erros comuns, projeto final, carga horária e lacunas.
3. Preserve a quantidade e os limites das oficinas e do Projeto Final. Não dividir, fundir ou criar
   lições.
4. Elimine repetição, falas de apresentação, datas e elementos administrativos sem função
   pedagógica.
5. Não invente dados. Registre lacunas essenciais em "Pendências de validação" ao final.
6. Abra o documento com "Análise essencial do material-fonte", em no máximo cinco tópicos. Essa
   seção é orientação de produção e não aparece ao participante.

# ESTRUTURA INICIAL
Antes das lições, inclua:

## Identificação
- nome do curso;
- quantidade exata de oficinas e indicação do Projeto Final;
- formato: autoinstrucional e assíncrono;
- público-alvo;
- pré-requisitos técnicos;
- tempo estimado, igual ao roteiro-fonte;
- recursos necessários.

## Objetivo geral
Um parágrafo curto que declare o resultado concreto que o participante produzirá.

## Objetivos de aprendizagem
De três a cinco objetivos mensuráveis com verbos de execução, como configurar, criar, aplicar,
testar, corrigir, validar ou produzir.

# CONTRATO DE CADA LIÇÃO
Para cada oficina e para o Projeto Final, mantenha esta ordem:

1. `# Oficina N - [título orientado à ação]` ou `# Projeto Final - [título]`.
2. `## Ficha de produção da lição` com:
   - objetivo da lição, em uma frase;
   - resultado observável;
   - tabela `Etapa | Conteúdo | Bloco Rise 360`;
   - nota: "A ficha orienta a produção e não deve aparecer no curso publicado."
3. Um único marcador de início, exatamente no formato:
   `> » IA: ▼▼▼ INÍCIO DA LIÇÃO - "[Oficina N ou Projeto Final] - [título]" - todo o conteúdo até o marcador de fim corresponde a UMA única lição no Rise 360; não dividir, duplicar, fundir ou criar sublições. Não publicar este marcador. ▼▼▼`
4. Todos os blocos visíveis da lição, em progressão: problema; recursos; preparação; execução;
   verificação formativa; ponto de controle; solução de problemas; desafio opcional ou síntese.
5. Um único marcador de fim, exatamente no formato:
   `> » IA: ▲▲▲ FIM DA LIÇÃO - "[Oficina N ou Projeto Final] - [título]" - encerrar esta lição aqui. Não publicar este marcador. ▲▲▲`

# MARCAÇÃO OBRIGATÓRIA DE CADA BLOCO
Antes de CADA elemento do curso, use:

> » IA: BLOCO RISE 360 - [TIPO]. [Instrução curta de montagem]. Não publicar esta linha.

BLOCO RISE 360
[TIPO]

Depois declare, sem misturar instruções com conteúdo visível:
- `Título visível:` título exato ou `sem título`;
- `Configuração:` comportamento e opções necessárias;
- `Conteúdo visível:` texto integral a inserir;
- `Gabarito e feedback:` quando aplicável.

Nunca use "ver slide", "conforme o PDF" ou "copiar do material-fonte". Não deixe campos vazios nem
placeholders. A IA de montagem não terá acesso a nenhuma outra fonte.

# BLOCOS E LIMITES

## Cover
Use na abertura de cada lição. Informe título, subtítulo curto e configuração visual. Use fundo
sólido e tipografia de alto contraste; não solicite imagem.

## Text
Use para o problema, teoria mínima, transições e síntese. Cada bloco deve ter de um a três
parágrafos; cada parágrafo, até 60 palavras. Divida explicações maiores sem criar nova lição.

## List e Checklist
Use List para recursos ou recomendações; Checklist para preparação, verificação de êxito e critérios
do Projeto Final. Escreva todos os itens e torne cada critério observável.

## Process
Use para a execução. Cada etapa deve ter título curto, uma ação principal, o texto exato a digitar
quando necessário e o breadcrumb validado. Não agrupe várias telas ou decisões em uma única etapa.

## Accordion
Use em "Se travar": um item por problema, com título do sintoma e solução completa. Inclua de dois a
quatro problemas reais por oficina, priorizando os que impedem continuar.

## Statement
Use somente para uma regra, dica ou alerta. O texto deve ter UMA frase curta, preferencialmente até
18 palavras. Nunca use Statement para passo a passo, prompt editável, breadcrumb, exercício,
gabarito, feedback ou texto com vários períodos.

## Tabs
Use apenas para caminhos alternativos realmente paralelos, como sistemas operacionais ou versões.
Inclua o conteúdo integral de cada caminho e não esconda pré-requisito essencial.

## Knowledge Check - Multiple Choice
Use para uma decisão relevante antes ou durante a execução. Inclua enunciado, alternativas
plausíveis, resposta correta, feedback instrutivo para acerto, feedback instrutivo para erro e nova
tentativa habilitada.

## Sorting Activity
Use apenas quando classificar itens for necessário para executar com segurança. Inclua categorias,
itens, classificação correta e feedback final.

# BREADCRUMBS E PONTOS DE CONTROLE
Sempre que houver navegação em interface, use `Aplicativo > Menu > Submenu > Opção`. Preserve os
nomes oficiais da interface e não traduza termos que aparecem em outro idioma. Depois de uma etapa
crítica, inclua `🏁 Ponto de controle:` com o resultado observável e onde conferi-lo. Breadcrumb não
vai em Statement; ele pertence à descrição da etapa Process ou ao Text correspondente.

Se houver dois caminhos legítimos, use Tabs. Se o caminho não estiver confirmado, não invente:
escreva uma orientação genérica executável e registre a validação pendente.

# PROMPTS, CÓDIGO E TEXTO PARA DIGITAR
Forneça o conteúdo completo e preserve-o verbatim. Conteúdo curto pode ficar no corpo do passo
Process. Conteúdo longo vai em bloco Text próprio, com instrução de copiar; nunca em Statement.
Use bloco de código apenas quando a distinção monoespaçada for necessária. Não use Download se o
arquivo não existir de fato.

# AVALIAÇÃO HANDS-ON
Cada oficina deve conter:
- ao menos uma verificação formativa nativa do Rise durante a execução;
- um ponto de controle objetivo ao final;
- feedback que ajude a corrigir a ação;
- nova tentativa habilitada nos Knowledge Checks.

O Projeto Final deve mobilizar as competências das oficinas em uma missão autônoma, não apenas
repeti-las. Termine com Checklist de critérios observáveis. Desafios "Quer ir além?" são opcionais,
curtos e incluem forma de validação; use List ou Accordion, nunca Statement longo.

# CONTEÚDO E EXPERIÊNCIA
- Priorize o fazer; explique apenas o necessário para executar o próximo passo.
- Alterne blocos intencionalmente e evite longas sequências de Text.
- Não solicite capturas de tela, imagens, mapas, gráficos, infográficos, vídeos, áudio ou mídia
  externa. Não deixe espaços reservados para mídia.
- Links só podem aparecer quando forem requisito técnico validado e indispensável à execução; não
  use links como substituto para conteúdo que deve estar no roteiro.
- Requisitos de conta, plano e versão só entram se estiverem validados no material-fonte.

# ACESSIBILIDADE E PRODUÇÃO
Ao final, crie `# Orientações gerais de produção no Rise 360` e inclua:
- manter exatamente o número de lições do roteiro;
- usar títulos internos como seções, não como novas lições;
- remover da publicação marcadores, fichas e instruções dirigidas à IA;
- não adicionar conteúdo ou mídia não previstos;
- preservar breadcrumbs e nomes de interface;
- configurar Knowledge Checks como formativos e permitir novas tentativas;
- manter contraste, hierarquia correta de títulos e nomes descritivos para controles;
- não comunicar informação apenas por cor;
- testar todos os passos em computador e celular;
- conferir ortografia, consistência, gabaritos, feedbacks e acessibilidade.

Se houver lacunas factuais, acrescente `# Pendências de validação` após as orientações. Não invente
conteúdo para eliminá-las.

# VERIFICAÇÃO FINAL OBRIGATÓRIA
Antes de entregar, confirme:
- um início e um fim para cada oficina e para o Projeto Final, com títulos idênticos;
- nenhum conteúdo de uma lição fora dos marcadores;
- um tipo de bloco antes de cada elemento;
- textos completos e instruções separadas do conteúdo visível;
- passos executáveis, em ordem, sem ações implícitas;
- breadcrumbs nos pontos de navegação e pontos de controle após etapas críticas;
- nenhum Statement com mais de uma frase ou usado como exercício/prompt;
- questões com alternativas, gabarito, feedbacks e nova tentativa;
- troubleshooting nos pontos de bloqueio reais;
- objetivos correspondentes às tarefas e ao Projeto Final;
- ausência de referências ao arquivo-fonte e de dependências de mídia;
- roteiro autossuficiente e montável sem nova consulta ao material-fonte.

# FORMATO DE SAÍDA
Entregue um único Markdown completo e operacional. Não gere DOCX. Não gere o PDF nesta etapa; o
PDF será criado a partir deste Markdown pelo script da skill após a validação do conteúdo.
```

## Depois daqui

1. Gerar e validar os PDFs conforme a Fase 8 da skill.
2. Carregar no Articulate o `promptArticulate.md` do projeto e o Markdown Articulate.
3. Fazer a verificação visual do curso e testar as atividades.
4. Exportar o SCORM e usar `revisar-curso-scorm` no ciclo de revisão.
