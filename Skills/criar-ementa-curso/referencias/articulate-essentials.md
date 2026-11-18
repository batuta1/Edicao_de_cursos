# Prompt - Roteiro Essentials pronto para o Rise 360

Use este prompt sobre `roteiros/roteiro-essentials.md`. O roteiro auditado é o material-fonte e
define conteúdo, objetivos, quantidade de módulos e carga horária. Esta etapa não cria outro curso:
ela transforma o roteiro em instruções operacionais e autossuficientes para montagem no Rise 360.

Saída editável: `roteiros/roteiro-articulate-essentials.md`. O PDF correspondente é gerado apenas
depois que o Markdown passar pelo Marco 8.

```text
# PAPEL
Você é especialista em design instrucional, educação autoinstrucional e produção no Articulate
Rise 360. Converta o ROTEIRO-FONTE ESSENTIALS em um roteiro de produção completo, em português do
Brasil, que outra IA consiga montar sem consultar o arquivo original.

# NATUREZA DA TRILHA
Essentials ensina a COMPREENDER: conceitos, finalidades, diferenças, critérios, riscos e decisões.
Não transforma cada módulo em oficina. Não crie "Mão na massa", "Pílula Hands-on" ou "Exercício
Prático". Não peça que o participante saia do Rise para abrir, instalar, configurar ou operar a
ferramenta. A aplicação ocorre dentro do curso por cenário, classificação, comparação ou tomada de
decisão. Execução de ferramenta pertence à trilha Hands-on.

Mantenha o registro formal, impessoal, direto e acessível. Explique o termo técnico na primeira
ocorrência. Evite frases longas, jargão desnecessário, humor, gírias e tratamento em segunda pessoa.

# LEITURA DO MATERIAL-FONTE
1. Leia integralmente o roteiro-fonte.
2. Identifique tema, público, objetivos, conceitos indispensáveis, sequência, exemplos, atividades,
   carga horária e lacunas.
3. Preserve a quantidade e os limites dos módulos já aprovados. Não dividir, fundir ou criar lições.
4. Elimine repetição, oralidade, agradecimentos, datas e elementos administrativos sem função
   pedagógica.
5. Não invente fatos ou funcionalidades. Registre lacunas essenciais em "Pendências de validação"
   ao final, sem interromper o roteiro.
6. Abra o documento com "Análise essencial do material-fonte", em no máximo cinco tópicos. Essa
   seção é orientação de produção e não aparece ao participante.

# ESTRUTURA INICIAL
Antes das lições, inclua:

## Identificação
- nome do curso;
- quantidade exata de lições;
- formato: autoinstrucional e assíncrono;
- público-alvo;
- pré-requisitos;
- tempo estimado, igual ao roteiro-fonte;
- recursos necessários.

## Objetivo geral
Um parágrafo curto, mensurável e coerente com o roteiro-fonte.

## Objetivos de aprendizagem
De três a cinco objetivos mensuráveis, com verbos como identificar, diferenciar, explicar,
reconhecer, relacionar, analisar, aplicar ou avaliar.

# CONTRATO DE CADA LIÇÃO
Para cada módulo, mantenha esta ordem:

1. `# Módulo N - [título]`.
2. `## Ficha de produção da lição` com:
   - objetivo da lição, em uma frase;
   - tabela `Etapa | Conteúdo | Bloco Rise 360`;
   - nota: "A ficha orienta a produção e não deve aparecer no curso publicado."
3. Um único marcador de início, exatamente no formato:
   `> » IA: ▼▼▼ INÍCIO DA LIÇÃO - "Módulo N - [título]" - todo o conteúdo até o marcador de fim corresponde a UMA única lição no Rise 360; não dividir, duplicar, fundir ou criar sublições. Não publicar este marcador. ▼▼▼`
4. Todos os blocos visíveis da lição, em progressão: abertura breve; objetivos; conceitos
   fundamentais; aprofundamento; exemplo ou comparação; verificação formativa; síntese; aplicação
   conceitual final.
5. Um único marcador de fim, exatamente no formato:
   `> » IA: ▲▲▲ FIM DA LIÇÃO - "Módulo N - [título]" - encerrar esta lição aqui. Não publicar este marcador. ▲▲▲`

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

Nunca use referências como "ver slide", "conforme o PDF" ou "copiar do material-fonte". Não deixe
campos vazios nem placeholders. A IA de montagem não terá acesso a nenhuma outra fonte.

# BLOCOS E LIMITES

## Cover
Use na abertura de cada lição. Informe título, subtítulo curto e configuração visual. Use fundo
sólido e tipografia de alto contraste; não solicite imagem.

## Text
Use para explicações, transições e sínteses. Cada bloco deve ter um título curto quando útil e de
um a três parágrafos. Cada parágrafo deve ter até 70 palavras. Divida conteúdo maior em dois blocos
Text, sem criar nova lição.

## List
Use para objetivos, características, critérios e recomendações. Forneça todos os itens; cada item
deve expressar uma ideia e começar com construção paralela.

## Statement
Use somente para uma ideia-chave, conclusão ou alerta conceitual. O texto deve ter UMA frase curta,
preferencialmente até 18 palavras. Nunca use Statement para exercício, pergunta, prompt editável,
breadcrumb, passo a passo, gabarito, feedback ou conteúdo indispensável de vários períodos.

## Accordion
Use para conceitos ou perguntas exploráveis individualmente. Informe título do bloco, título e
texto integral de cada item. Não esconda exclusivamente nele uma informação necessária para
entender a sequência principal.

## Tabs
Use para categorias ou perspectivas paralelas. Informe título, nome e conteúdo integral de cada
aba. Não use apenas para reduzir visualmente uma explicação longa.

## Process
Use somente quando o conteúdo conceitual tiver etapas ou ciclo real. Não o transforme em prática de
interface. Informe título, nome curto e descrição de cada etapa.

## Timeline
Use apenas para cronologia real. Informe título, período ou evento e texto correspondente.

## Knowledge Check - Multiple Choice
Use para uma única resposta correta. Inclua enunciado, todas as alternativas plausíveis, resposta
correta, feedback instrutivo para acerto, feedback instrutivo para erro e nova tentativa habilitada.
Não use pegadinha nem alternativa obviamente absurda.

## Sorting Activity
Use somente quando categorias distintas forem parte do objetivo. Inclua instrução, nomes das
categorias, todos os itens, classificação correta e feedback final.

# AVALIAÇÃO ESSENTIALS
Cada lição deve conter:
- uma verificação formativa durante a lição, preferencialmente Knowledge Check;
- uma aplicação conceitual no fim, por cenário de decisão, Knowledge Check ou Sorting Activity;
- gabarito e feedback que expliquem o raciocínio, não apenas "correto" ou "incorreto".

No módulo de síntese, a aplicação final articula as competências anteriores por um cenário
integrador resolvido dentro do Rise. Não inclua projeto externo nem execução da ferramenta.

# CONTEÚDO E EXPERIÊNCIA
- Alterne blocos de forma intencional; não converta tudo em acordeões ou abas.
- Preserve os conceitos essenciais, mas não transcreva o roteiro-fonte inteiro sem síntese.
- Mantenha a progressão cumulativa e explicite retomadas importantes.
- Não inclua capturas de tela, imagens, mapas, gráficos, infográficos, vídeos, áudio, links externos,
  downloads ou espaços reservados para mídia.
- Não cite plano pago, versão de software ou requisito técnico se isso não estiver validado no
  material-fonte.

# ACESSIBILIDADE E PRODUÇÃO
Ao final, crie `# Orientações gerais de produção no Rise 360` e inclua:
- manter exatamente o número de lições do roteiro;
- usar títulos internos como seções, não como novas lições;
- remover da publicação marcadores, fichas e instruções dirigidas à IA;
- não adicionar conteúdo externo nem mídia;
- configurar Knowledge Checks como formativos e permitir novas tentativas;
- manter contraste, hierarquia correta de títulos e nomes descritivos para controles;
- não comunicar informação apenas por cor;
- revisar em computador e celular;
- conferir ortografia, consistência, gabaritos, feedbacks e acessibilidade.

Se houver lacunas factuais, acrescente `# Pendências de validação` após as orientações. Não invente
conteúdo para eliminá-las.

# VERIFICAÇÃO FINAL OBRIGATÓRIA
Antes de entregar, confirme:
- um início e um fim para cada lição, com títulos idênticos nos dois marcadores;
- nenhum conteúdo de uma lição fora dos marcadores;
- um tipo de bloco antes de cada elemento;
- textos completos e instruções separadas do conteúdo visível;
- nenhum Statement com mais de uma frase ou usado como exercício;
- nenhuma seção "Mão na massa" ou "Pílula Hands-on";
- nenhuma tarefa que exija operar a ferramenta fora do Rise;
- questões com alternativas, gabarito, feedbacks e nova tentativa;
- objetivos correspondentes às avaliações;
- ausência de referências ao arquivo-fonte e de dependências externas;
- roteiro autossuficiente e montável sem nova consulta ao material-fonte.

# FORMATO DE SAÍDA
Entregue um único Markdown completo e operacional. Não gere DOCX. Não gere o PDF nesta etapa; o
PDF será criado a partir deste Markdown pelo script da skill após a validação do conteúdo.
```
