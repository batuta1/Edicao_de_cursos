# Relatório de Edição — ChatGPT PowerPoint (Hands On), trilha SCORM

Revisão feita em 7 de outubro de 2026 com a skill `revisar-curso-scorm`.

## Pacote

- Original: `chatgpt-powerpoint-hands-on-scorm12-IKtiWXi5.zip` (não foi modificado)
- Revisado: `chatgpt-powerpoint-hands-on-scorm12-IKtiWXi5-REVISADO.zip`
- Formato: default (`scormcontent/runtime-data.js`)
- Título no pacote: `ChatGPT PowerPoint - Hands On` (bate com o título esperado, usado como trava na extração)
- `course.id`: `ItiYDmh_KQwh6hwIbBpyTUHRIblB_QaI`
- 3 lições: `Preparando o Ambiente e Instalando o ChatGPT no PowerPoint`,
  `Transformando Textos em Apresentações Estruturadas`,
  `Ajustando, Revisando e Comparando Versões de Apresentações`.

## Material-fonte e mapeamento lição ↔ oficina

- Referência principal: `roteiros/roteiro-articulate-hands-on.md` (Oficinas 0 a 4, Projeto Final,
  A Parte dos Dez, Conseguiu! E agora?).
- Apoio: `roteiros/roteiro-hands-on.md` e `ementa.md`.

| Lição do SCORM | Oficinas do roteiro |
|---|---|
| 1 — Preparando o Ambiente e Instalando o ChatGPT no PowerPoint | Abertura ("Antes de Arregaçar as Mangas") + Oficina 0 + Oficina 1 |
| 2 — Transformando Textos em Apresentações Estruturadas | Oficina 2 |
| 3 — Ajustando, Revisando e Comparando Versões de Apresentações | Oficina 3 + Oficina 4 |
| — (ausente) | Projeto Final, A Parte dos Dez, Conseguiu! E agora? |

## Critério aplicado

O mesmo da trilha Essentials (comparação campo a campo com a oficina correspondente), mais uma regra:
**manter o tom do roteiro Hands-on**, que fala em segunda pessoa, é direto e segue o estilo "Para
Leigos". As aberturas genéricas ("O Primeiro Passo para o Sucesso", "aproveitando todo o potencial da
inteligência artificial para criar slides claros e personalizados") foram trocadas pelos blocos
"🎯 O Problema" de cada oficina. Os fechamentos com "Parabéns!" foram trocados por próximos passos
concretos. Os objetivos foram padronizados com "Ao final desta lição, você será capaz de:".
Accordions "Se travar", knowledge checks e prompts entre aspas triplas já estavam fiéis ao roteiro e
receberam só ajustes pontuais.

Método de edição: igual ao da Essentials (`aplicar_edicoes.py` + `edicoes_handson.py`, guardados
nesta pasta), com aplicação por caminho JSON e trava sobre o valor original.

## Alterações lição a lição

### Lição 1 — Preparando o Ambiente e Instalando o ChatGPT no PowerPoint (42 campos)

- **Abertura**: o texto genérico foi trocado pelo "Antes de Arregaçar as Mangas" do roteiro, com a
  promessa concreta do curso (uma aula inteira em duas versões, para dois públicos) e o aviso de fazer
  a Oficina 0 primeiro.
- **"O que você precisa ter aberto"**: itens restaurados do roteiro. "Documento seu que possa virar
  apresentação" voltou a ter os exemplos: artigo, capítulo, plano de ensino.
- **Oficina 0** (process): a introdução virou o "🎯 O Problema" da oficina. Os passos ganharam o que
  havia se perdido: "o arquivo passa por duas empresas", "não planeje a aula de amanhã contando com uma
  cota que pode acabar hoje", os rótulos em inglês entre parênteses e "uma quarta [situação] só aparece
  na Oficina 1". O resumo virou um balanço do que foi resolvido.
- **Erro corrigido, cópia de trabalho**: "Assim, você trabalha sempre em uma cópia de segurança"
  invertia a lógica. Agora diz que você trabalha na cópia e o original fica intacto, como garantia.
- **Erro corrigido, desfechos do passo 4**: o texto dizia que "a adição pede um arquivo XML de
  manifesto". Quem usa o XML é o administrador do Microsoft 365, na implantação. O bloco foi
  reescrito como a tabela de decisão do roteiro: os 4 desfechos, com o que significa e o que fazer em
  cada um.
- **Planos**: incluída a data de conferência (7/10/2026) e o aviso de que muda com frequência.
- **Oficina 1**: a abertura virou o "🎯 O Problema" da oficina, com o material necessário. A
  introdução e o resumo do process foram refeitos. O passo das Skills voltou a ter o breadcrumb e o
  "por ora, só localize onde ficam".
- **Títulos dos accordions**: "Soluções para Problemas Comuns" / "Resolvendo Dificuldades na
  Instalação" viraram "Se travar na Oficina 0" / "Se travar na Oficina 1", seguindo o roteiro.
- **Knowledge check**: os feedbacks das alternativas erradas agora explicam o motivo (o aviso da
  própria OpenAI de que o sistema pode editar e apagar). Gabarito inalterado.
- **Fechamento**: o "Parabéns!..." genérico foi trocado pelo que a Oficina 2 faz e pelo que ter à mão.

### Lição 2 — Transformando Textos em Apresentações Estruturadas (34 campos)

- **Abertura**: o texto genérico foi trocado pelo "🎯 O Problema" da Oficina 2 (artigo de trinta
  páginas, aula na quinta-feira, modelo visual que ninguém avisa) e pelo material necessário.
- **Objetivos**: lead-in padronizado. O item "Adaptar apresentações para diferentes públicos
  acadêmicos" não corresponde à Oficina 2 (é da Oficina 4) e foi trocado por "resolver os problemas
  mais comuns do primeiro rascunho". Os demais itens foram alinhados aos passos da oficina.
- **Process**: o primeiro passo voltou a ser "Não comece de uma apresentação em branco". O resumo
  virou o ponto de controle do roteiro (Estrutura de Tópicos com doze slides; Classificação de Slides
  com o tema).
- **"Quer ir além?"**: lead-in e desafios no formato do roteiro ("Deu certo se: ...").
- **Bloco de transição** ("Editando e Adaptando com Segurança", que antecipava a próxima lição no
  meio desta): virou "Antes de mexer no rascunho", com o que garantir antes da Oficina 3.
- **Knowledge check**: os feedbacks foram refeitos com o motivo de cada resposta, por exemplo que
  pedir ao sistema para corrigir o que inventou abre espaço para nova invenção. Gabarito inalterado.
- **Fechamento**: próximos passos concretos (Oficinas 3 e 4).

### Lição 3 — Ajustando, Revisando e Comparando Versões de Apresentações (43 campos)

- **Abertura**: une os dois "🎯 O Problema" das Oficinas 3 e 4.
- **Objetivos**: lead-in padronizado. "Antecipar perguntas e garantir práticas éticas", vago, virou
  "consultar a narrativa e as lacunas e antecipar as perguntas do novo público". Os demais foram
  alinhados aos três elementos da edição e à revisão em seis pontos.
- **Oficina 3** (process): a introdução diz qual é o passo mais importante (pedir o plano). O resumo
  virou o ponto de controle do roteiro, com a comparação com o original intacto.
- **Erro corrigido, "Conteúdo apagado indevidamente"**: o texto dizia que "a cópia de trabalho
  existe justamente para recuperar informações perdidas", também com a lógica invertida. Corrigido:
  você volta ao original, que ficou intacto porque se trabalha na cópia.
- **Gráficos**: incluído "limitação declarada pelo fabricante" e "ou ainda estar em desenvolvimento".
- **Oficina 4**: o bloco introdutório agora traz o procedimento real (duplicar com o nome do público,
  por exemplo `aula-banca.pptx`). A aba "Banca de Qualificação" ganhou os três prompts do roteiro
  (ajuste, validação da narrativa e antecipação da arguição), que estavam ausentes. A aba "Público
  Geral" ganhou o critério do roteiro (o que a versão leiga não pode assumir como sabido).
- **Revisão em seis pontos**: voltaram os rótulos (Afirmações, Números, Citações, Sentido, Slides,
  Visual) e o exemplo "sugere" → "demonstra". O ponto de controle da Oficina 4, que não tinha bloco
  próprio, foi incluído no mesmo campo.
- **"Quer ir além?"**: os desafios agora dizem o que fazer, não só o critério de êxito. O "Objeção
  mais forte" voltou a ter o prompt.
- **Knowledge check**: feedbacks refeitos. Gabarito inalterado.
- **Fechamento**: o "Parabéns! Agora você domina..." foi trocado pelo próximo passo do roteiro (o
  Projeto Final, ver "Pontos de atenção", item 1) e pelas quatro condições de bom uso.

## Contagem de campos alterados

Confirmada por `validar_estrutura.py`: **119 campos de texto** (L1 = 42, L2 = 34, L3 = 43). Por
campo: description = 42, paragraph = 41, title = 13, heading = 13, feedback = 10. A contagem do
validador bate exatamente com a do script de edição.

## Validações

- `validar_estrutura.py`: **estrutura preservada em todas as lições**, sem nenhuma divergência estrutural.
- `checar_html.py`: tags HTML balanceadas em todos os campos (0 problemas).
- `checar_gabaritos.py`: 3 knowledge checks, todos com gabarito coerente com o roteiro e com os
  feedbacks.
- `scorm_reempacotar.py`: round-trip do Base64 conferido. 83 arquivos no pacote, apenas
  `scormcontent/runtime-data.js` substituído e 0 arquivos alterados fora do alvo.
- **Teste em navegador** (LMS simulada com API SCORM 1.2): o curso carrega; na Lição 3 foram
  conferidos a abertura, os objetivos, a revisão em seis pontos e o fechamento com o texto novo.
- **Não verificado visualmente**: as Lições 1 e 2. Foram validadas só de forma estrutural e de HTML.

## Pontos de atenção (exigem olho humano)

1. **O Projeto Final não existe no SCORM.** O roteiro termina com o "Projeto Final — A mesma aula em
   dois tamanhos" (26 min da carga horária), "A Parte dos Dez" e "Conseguiu! E agora?". O curso gerado
   para na Oficina 4. O fechamento da Lição 3 agora aponta o Projeto Final como próximo passo e
   resume as quatro condições de bom uso, mas **a atividade em si (10 passos + checklist de 10 itens)
   precisa ser acrescentada no Rise como nova lição**. Isso é mudança estrutural, fora do escopo desta
   revisão. Sem ela, a carga horária declarada na ementa não corresponde ao conteúdo do pacote.
2. **"Quer ir além?" das Oficinas 0, 1 e 3 ausentes.** Os desafios da Oficina 3 (narrativa, lacunas,
   arguição) aparecem em parte nos prompts da aba "Banca de Qualificação". Os das Oficinas 0 e 1 não
   têm bloco.
3. **Dados datados.** Créditos (10 a 50 por mensagem), planos e cota compartilhada com o Excel
   correspondem à documentação consultada em 7/10/2026. Confira antes de publicar.

## O que foi gerado

- `cursoChatGPTPPTHandsOn.json`: payload desserializado original.
- `licoes_extraidas_ChatGPTPPTHandsOn/licao_01…03_*.json`: lições separadas (todas editadas) +
  `indice_licoes.json`.
- `licoes_extraidas_ChatGPTPPTHandsOn/edicoes_handson.py`: registro de cada campo alterado.
- `cursoChatGPTPPTHandsOn_editado.json`: curso fundido com as edições.
- `cursoChatGPTPPTHandsOn_editado_base64.txt`: Base64 final (120.728 caracteres), com round-trip
  verificado.
- `chatgpt-powerpoint-hands-on-scorm12-IKtiWXi5-REVISADO.zip`: pacote reempacotado, entregue em
  `OpenAI/OPENAI (ChatGPT)/ChatGPT PowerPoint/hands-on/` junto com a versão extraída
  `HandsOnChatGPT_PowerPointRevisado/`.
