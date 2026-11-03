# NotebookLM Para Leigos — Curso Hands-on

> *» IA: Bloco Cover — título verbatim e subtítulo em itálico logo abaixo. Não traduzir "NotebookLM".*

*Em menos de duas horas, você vai transformar quatro documentos oficiais num caderno de estudo que responde perguntas, mostra de onde tirou cada resposta, monta guia e teste e ainda fala com você em português.*

## Antes de Arregaçar as Mangas

> *» IA: Bloco Text — parágrafo verbatim.*

Este curso é mão na massa. Você vai abrir o NotebookLM, colocar documentos dentro dele e fazer a ferramenta trabalhar para você — conferindo tudo, porque a IA resume, mas quem assina é você. Basta o plano gratuito e uma Conta Google.

> *» IA: Bloco Checklist — itens verbatim.*

O que você precisa ter aberto agora:

- Um computador com internet (o celular serve só para ouvir o áudio no fim).
- O navegador em `notebook.google.com`, já com sua Conta Google.
- Uma pasta no computador para baixar dois PDFs.
- Os quatro endereços do Kit LGPD, logo abaixo.

> *» IA: Bloco Table — Kit LGPD verbatim; manter os endereços sem nenhuma alteração.*

| # | Fonte | Como entra | Endereço |
|---|---|---|---|
| 1 | Lei nº 13.709/2018 — LGPD (Planalto) | Link | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm |
| 2 | Guia ANPD — Segurança da Informação para Agentes de Pequeno Porte (21 p.) | Baixar PDF e enviar | https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-vf.pdf/@@download/file |
| 3 | Guia ANPD — Tratamento de dados pessoais para fins acadêmicos (58 p.) | Baixar PDF e enviar | https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/web-guia-anpd-tratamento-de-dados-para-fins-academicos.pdf/@@display-file/file |
| 4 | ANPD — Titular de Dados | Link | https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados |

> *» IA: Bloco Statement — regra de ouro, preservar o emoji.*

> 🔑 **Regra de ouro:** a citação mostra de onde a resposta veio, não prova que ela está certa. Clicou, leu, comparou — só então use.

> *» IA: Bloco Statement — aviso de marca, preservar o emoji.*

> 📌 **Não esqueça:** em julho de 2026, o NotebookLM passou a se chamar **Gemini Notebook**. A tela pode mostrar um nome ou outro. É o mesmo produto, no mesmo endereço.

> *» IA: Bloco Process — passos de verificação verbatim; preservar os breadcrumbs.*

Confira sua conta:

1. Abra o navegador no computador e acesse `notebook.google.com`.
2. Confira qual conta está ativa em `notebook.google.com > avatar (canto superior direito)`.
3. Veja se aparece o botão "Criar novo notebook". Não clique ainda.

> *» IA: Bloco Statement — ponto de controle, preservar o emoji e o breadcrumb.*

> 🏁 Ponto de controle: em `notebook.google.com`, aparece o botão "Criar novo notebook". Se a tela disser que o serviço não está disponível e você usa conta da escola ou da empresa, é o administrador que precisa liberar. Enquanto isso, use uma conta pessoal — o curso só usa documentos públicos.

> *» IA: Bloco Text para a frase; Bloco Table para o semáforo, verbatim.*

Tudo o que você sobe vai para os servidores do Google. Então a pergunta vem **antes** do upload: posso subir isto? Use o semáforo:

| Cor | O que é | Pode subir? |
|---|---|---|
| Verde | Lei, guia de órgão público, artigo de acesso aberto, material que você mesmo publicou | Sim, em qualquer conta |
| Amarelo | Documento interno sem dado pessoal (ata, procedimento, plano de ensino) | Só na conta da instituição, se ela autorizou |
| Vermelho | Nome e nota de aluno, peça de cliente, prontuário, fonte jornalística, qualquer coisa sob sigilo | Não, sem base legal, ambiente aprovado e dados removidos antes |

> *» IA: Bloco Statement — aviso, preservar o emoji.*

> ⚠️ **Cuidado:** em conta pessoal, se você clicar no "joinha" (positivo ou negativo) de uma resposta, o pacote enviado pode incluir suas fontes e ser lido por pessoas do Google, ficando guardado por até três anos. Em notebook com material sensível, não dê feedback. Em conta Workspace/Education, o Google diz que nada disso é revisado nem usado para treinar modelos — mas a regra da LGPD continua valendo. Neste curso, tudo é verde.

## O Mapa da Mão na Massa

> *» IA: Bloco Table — mapa verbatim; frase seguinte em Bloco Text.*

| Oficina | Problema que vai resolver | Tempo |
|---|---|---|
| Antes de Arregaçar as Mangas | "Posso subir qualquer documento?" | 13 min |
| Oficina 1 — Junte tudo num notebook | Tenho documentos demais e nenhum lugar para juntá-los | 20 min |
| Oficina 2 — Pergunte e confira a citação | Preciso de resposta rápida, mas que eu consiga conferir | 20 min |
| Oficina 3 — Gere guia de estudo, resumo e teste | Quero estudar (ou dar aula) sem reler tudo | 20 min |
| Oficina 4 — Ouça suas fontes e mostre para alguém | Quero ouvir o conteúdo e mostrar para outra pessoa | 20 min |
| Projeto Final — O kit de estudo do seu tema | Repetir tudo sozinho, num tema seu | 16 min |
| A Parte dos Dez | Hábitos para levar | 6 min |
| **Total** | | **115 min** |

As oficinas usam o mesmo notebook, em sequência: cada uma entrega uma pequena vitória, e o Projeto Final junta todas num tema seu.

---

# Oficina 1 — Junte tudo num notebook

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 1" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Bloco Text — verbatim.*

Você é estudante e a prova de amanhã é sobre LGPD. O material está espalhado: uma lei no site do Planalto, dois guias em PDF da ANPD, uma página sobre direitos do titular. Nesta oficina, você junta tudo num lugar só — e confere se a ferramenta leu direito.

### 🧰 O que você vai usar

> *» IA: Bloco List — verbatim.*

- `notebook.google.com`
- Os dois PDFs da ANPD (você vai baixar agora) e os dois links do Kit LGPD

### 👐 Mão na massa

> *» IA: Bloco Process — um passo por etapa, verbatim; preservar os breadcrumbs; não traduzir termos de interface; o texto a digitar fica em citação, verbatim.*

1. Baixe os PDFs 2 e 3 do Kit LGPD. Abra cada um: o guia de segurança tem 21 páginas; o de fins acadêmicos, 58. Se abrir uma página de site, o download falhou — use o link de novo.
2. Vá a `notebook.google.com > Criar novo notebook`.
3. Na janela que abre ("Fazer upload de uma fonte"), escolha enviar arquivo do computador e selecione o guia de segurança.
4. Adicione um link em `Fontes > adicionar fonte [conferir rótulo] > site/link [conferir rótulo]` e cole o endereço da LGPD.
5. Espere as duas fontes aparecerem no painel Fontes, cada uma com uma caixinha marcada.
6. Agora sozinho: adicione o PDF 3 (fins acadêmicos) e o link da página "Titular de Dados", pelo mesmo caminho.
7. Clique no título do notebook, no topo, e renomeie para "LGPD — revisão" [conferir].
8. Em `Conversa`, cole e envie:

> Liste as fontes deste notebook. Para cada uma, informe título, tipo de documento, órgão responsável e, em uma frase, o tema central. Inclua uma citação por fonte.

> *» IA: Bloco Statement — curiosidade técnica, preservar o emoji.*

> 🤓 **Curiosidade técnica:** quando você cola o link de um site, a ferramenta copia só o texto daquela página. Imagens, vídeos e páginas ligadas a ela ficam de fora — e conteúdo de assinatura (paywall) não entra.

### ✅ Deu certo?

> *» IA: Bloco Statement — verbatim, preservar o emoji e o breadcrumb.*

> 🏁 Ponto de controle: em `notebook.google.com > LGPD — revisão > Fontes`, quatro fontes aparecem com caixas marcadas, e a resposta da Conversa lista as quatro, cada uma com um número de citação que abre o documento certo.

### 🚑 Se travar

> *» IA: Bloco Accordion — um item por linha da tabela, verbatim.*

| Problema | O que fazer |
|---|---|
| O "PDF" baixado abre como site | Era a página do portal, não o arquivo. Use o link direto do Kit LGPD e confira o número de páginas. |
| O PDF não sobe | Veja se passa de 200 MB ou é protegido contra cópia. Se for escaneado (só imagem), passe por OCR autorizado ou procure outra versão. |
| O link entrou pela metade | É normal: só o texto da página entra. Importe as outras páginas separadamente. |

### 🚀 Quer ir além?

> *» IA: Bloco Accordion — três desafios, marcados como OPCIONAL, verbatim.*

1. Adicione um vídeo público do YouTube **com legenda** sobre LGPD. Validação: ele aparece em Fontes; se for recusado, confira a legenda e se tem mais de 72 horas.
2. Teste a busca interna de fontes ("Pesquisa Rápida") descrevendo "direitos do titular LGPD". Validação: aparecem sugestões — e você **não** importa nenhuma sem checar autoria e data.
3. Abra uma fonte e leia o resumo automático que a ferramenta fez dela. Validação: você aponta uma informação do resumo e acha a mesma no documento.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 1" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 2 — Pergunte e confira a citação

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 2" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Bloco Text — verbatim.*

Agora você é advogada e um cliente perguntou, por mensagem, qual a diferença entre dado pessoal, dado sensível e dado anonimizado. Você quer responder rápido — mas não pode errar. Nesta oficina, você pergunta à ferramenta e **confere** a resposta trecho por trecho.

### 🧰 O que você vai usar

> *» IA: Bloco List — verbatim.*

- O notebook "LGPD — revisão"
- Um bloco de notas (papel ou arquivo) para a ficha de conferência

### 👐 Mão na massa

> *» IA: Bloco Process — verbatim; preservar os breadcrumbs; textos a digitar e a ficha ficam em citação, verbatim.*

1. Em `notebook.google.com > LGPD — revisão > Conversa`, com as quatro fontes marcadas, cole e envie:

> Compare dado pessoal, dado pessoal sensível e dado anonimizado. Para cada conceito, apresente a definição legal, um exemplo e a citação do trecho da lei. Explique para iniciantes. Se as fontes divergirem, mostre as versões separadamente.

2. Passe o cursor sobre o primeiro número de citação. Leia o trecho que aparece.
3. Clique no número. A fonte abre no ponto exato.
4. Compare: a frase da resposta diz **o mesmo** que o trecho? Diz mais? Diz menos?
5. Agora sozinho: abra mais duas citações e preencha a ficha:

> Citação nº | Frase gerada | Trecho original | Bate? (total / parcial / não)

6. Em `Fontes`, desmarque tudo menos a LGPD e reenvie a mesma pergunta. Anote uma diferença entre as duas respostas.
7. Salve a melhor resposta em `Conversa > [resposta] > Save to note` [conferir rótulo].

> *» IA: Bloco Statement — dica, preservar o emoji.*

> 💡 **Dica:** peça sempre "se não estiver nas fontes, escreva 'não encontrado nas fontes'". Assim a ferramenta não tapa buraco com conhecimento geral.

### ✅ Deu certo?

> *» IA: Bloco Statement — verbatim, preservar o emoji e o breadcrumb.*

> 🏁 Ponto de controle: você tem uma ficha com três citações conferidas e uma diferença anotada; em `notebook.google.com > LGPD — revisão`, a nota salva aparece com as citações clicáveis.

### 🚑 Se travar

> *» IA: Bloco Accordion — um item por linha, verbatim.*

| Problema | O que fazer |
|---|---|
| "Não consigo responder" | Diga qual fonte, qual recorte e qual formato você quer. Se a informação não existe nas fontes, falta fonte. |
| A resposta está errada, mas a fonte está certa | Marque menos fontes, peça uma citação por frase e reformule de forma mais específica. |
| Não aparece citação específica | Pergunta ampla demais ou trecho curto demais. Faça uma pergunta mais precisa. |

### 🚀 Quer ir além?

> *» IA: Bloco Accordion — três desafios, marcados como OPCIONAL, verbatim; preservar os breadcrumbs.*

1. Em `Conversa > Configure Chat [conferir rótulo] > Learning Guide`, peça para ser testado sobre o assunto. Validação: a ferramenta faz uma pergunta por vez e dá pista antes do gabarito.
2. Peça uma resposta "Shorter" e outra "Longer" na mesma configuração. Validação: você aponta o que a curta cortou.
3. Use sua nota salva como fonte e pergunte algo sobre ela. Validação: a nova resposta cita a nota.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 2" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 3 — Gere guia de estudo, resumo e teste

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 3" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Bloco Text — verbatim.*

Você é professor e precisa, para amanhã, de um material de revisão sobre LGPD para a turma: um resumo, um guia de estudo e um teste rápido. Sem reler 80 páginas. Nesta oficina, o painel Estúdio faz o rascunho — e você revisa.

### 🧰 O que você vai usar

> *» IA: Bloco List — verbatim.*

- O notebook "LGPD — revisão"
- O painel Estúdio

### 👐 Mão na massa

> *» IA: Bloco Process — verbatim; preservar os breadcrumbs; não traduzir termos de interface.*

1. Abra `notebook.google.com > LGPD — revisão > Estúdio > Relatórios`. Repare nos modelos prontos: Documento de resumo, Guia de estudo, Perguntas frequentes.
2. Em `Estúdio > Relatórios > Guia de estudo`, gere o guia.
3. Em `Estúdio > Relatórios > Documento de resumo`, gere o documento. Esse é o "resumo" do material.
4. Abra o guia, escolha uma afirmação e clique na citação dela para conferir na fonte.
5. Agora sozinho: em `Estúdio > Teste > Personalizar`, escolha 5 questões e dificuldade média, e gere.
6. Responda o teste. Em uma questão, confira o gabarito na fonte citada.

> *» IA: Bloco Statement — aviso, preservar o emoji.*

> ⚠️ **Cuidado:** artefato também é síntese de IA. Antes de entregar para a turma, revise contra as fontes.

### ✅ Deu certo?

> *» IA: Bloco Statement — verbatim, preservar o emoji e o breadcrumb.*

> 🏁 Ponto de controle: em `notebook.google.com > LGPD — revisão > Estúdio`, aparecem o guia de estudo, o documento de resumo e o teste; você conferiu uma afirmação do guia e um gabarito do teste.

### 🚑 Se travar

> *» IA: Bloco Accordion — um item por linha, verbatim.*

| Problema | O que fazer |
|---|---|
| Não acho "Guia de estudo" | Ele fica dentro de Relatórios: `Estúdio > Relatórios > Guia de estudo`. |
| Procurei "Linha do tempo" e não existe | Não é botão fixo. Peça em Relatórios com formato personalizado ou na Conversa. |
| Apareceu aviso de limite | No gratuito são 10 relatórios e 10 testes por dia (consulta de 17/10/2026). Espere a renovação; não regenere à toa. |

### 🚀 Quer ir além?

> *» IA: Bloco Accordion — três desafios, marcados como OPCIONAL, verbatim; preservar os breadcrumbs.*

1. Em `Estúdio > Cartões de estudo`, gere 10 cartões e exporte em CSV. Validação: o arquivo CSV abre numa planilha.
2. Em `Estúdio > Relatórios`, descreva um formato próprio: "quadro com artigo, obrigação e exemplo". Validação: o relatório sai em tabela, com citações.
3. Em `Estúdio > Relatórios > Perguntas frequentes`, gere e marque uma resposta que você reescreveria. Validação: você justifica com o trecho da fonte.

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 3" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Oficina 4 — Ouça suas fontes e mostre para alguém

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Oficina 4" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 O Problema

> *» IA: Bloco Text — verbatim.*

Você é jornalista, passa uma hora por dia no trânsito e precisa que uma colega da redação consulte o mesmo material sem bagunçar suas fontes. Nesta oficina, você gera um áudio em português, monta um mapa mental e compartilha do jeito seguro.

### 🧰 O que você vai usar

> *» IA: Bloco List — verbatim.*

- O notebook "LGPD — revisão"
- Fones de ouvido
- O e-mail de alguém com quem você pode compartilhar (ou só a decisão de não compartilhar)

### 👐 Mão na massa

> *» IA: Bloco Process — verbatim; preservar os breadcrumbs; o texto a digitar fica em citação, verbatim.*

1. Abra `notebook.google.com > LGPD — revisão > Estúdio > Resumo em Áudio > Personalizar`.
2. Escolha o formato Resumo (*The Brief*, um apresentador, menos de dois minutos), idioma Português (Brasil), e cole na orientação:

> Produza um resumo curto em português do Brasil para iniciantes. Enfatize os direitos do titular de dados. Não apresente aconselhamento jurídico.

3. Clique em `Gerar`. Não fique esperando: a geração leva alguns minutos.
4. Enquanto isso, gere o mapa em `Estúdio > Mapa mental`. Clique num nó para abrir os ramos e depois para fazer uma pergunta sobre ele.
5. Volte ao áudio e ouça os primeiros trinta segundos.
6. Agora sozinho: em `Compartilhar`, digite o e-mail de quem vai consultar e escolha **Leitor** (lê e pergunta, mas não mexe nas fontes). Se não tiver com quem compartilhar, abra a janela, observe as opções e feche sem enviar.
7. Anote sua decisão: com quem, em qual papel e por quê.

> *» IA: Bloco Statement — aviso, preservar o emoji.*

> ⚠️ **Cuidado:** o áudio é uma conversa gerada por IA, não uma leitura das fontes. Pode errar. E no gratuito são só 3 áudios por dia.

> *» IA: Bloco Statement — dica, preservar o emoji.*

> 💡 **Dica:** a opção de compartilhar que mostra só a conversa [conferir rótulo] esconde as fontes da tela, mas não tira o acesso a elas. Para documento protegido, ela não protege nada.

### ✅ Deu certo?

> *» IA: Bloco Statement — verbatim, preservar o emoji e o breadcrumb.*

> 🏁 Ponto de controle: em `notebook.google.com > LGPD — revisão > Estúdio`, o player do áudio toca em português e o mapa mental abre com ramos; sua decisão de compartilhamento (Leitor, para quem e por quê — ou "não compartilhar") está anotada.

### 🚑 Se travar

> *» IA: Bloco Accordion — um item por linha, verbatim.*

| Problema | O que fazer |
|---|---|
| O áudio está demorando ou deu erro | Espere, reduza a orientação e tente de novo mais tarde. Se aparecer "Gerar mais tarde", use [conferir]. |
| Saiu em inglês | O idioma não foi escolhido em Personalizar. Gere de novo com Português (Brasil). |
| Não acho o mapa mental no celular | Mapa mental, relatórios e configuração do chat só existem completos no navegador do computador. |

### 🚀 Quer ir além?

> *» IA: Bloco Accordion — três desafios, marcados como OPCIONAL, verbatim.*

1. Gere um áudio no formato Debate. Validação: você identifica as duas posições e confere uma delas na fonte.
2. Instale o aplicativo no celular e baixe o áudio para ouvir offline. Validação: o áudio toca com o modo avião ligado.
3. Gere um Resumo em Vídeo no formato Explicador ou Curto, em português. Validação: o vídeo aparece no Estúdio (o formato Cinematic é pago, 18+ e em inglês — não é para este curso).

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Oficina 4" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# Projeto Final — O kit de estudo do seu tema

> *» IA: ▼▼▼ INÍCIO DA LIÇÃO — "Projeto Final" — todo o conteúdo até o ▲▲▲ FIM correspondente é UMA única lição no Rise; não dividir nem fundir, mesmo que haja blocos de código no meio. ▼▼▼*

### 🎯 A missão

> *» IA: Bloco Text para o parágrafo; Bloco List para as sugestões por perfil, verbatim.*

Chega de LGPD. Escolha um tema real do seu trabalho ou estudo e monte, do zero e sem roteiro passo a passo, um kit de estudo verificado: notebook com fontes verdes, uma pergunta-chave conferida e um artefato pronto para usar ou compartilhar.

Sugestões por perfil (sempre material público):

- **Estudante:** um capítulo ou artigo de acesso aberto + a página oficial do assunto.
- **Educador:** o documento curricular oficial do tema + dois textos públicos que você usa em aula.
- **Direito:** uma lei no portal do Planalto + um guia de órgão público sobre ela.
- **Jornalismo/Análise:** três comunicados oficiais públicos sobre o mesmo fato.

Sem tempo para achar fontes? Use o Kit LGPD com um recorte novo do seu perfil.

### 👐 Mão na massa

> *» IA: Bloco Process — verbatim; preservar os breadcrumbs.*

1. Passe cada fonte pelo semáforo. Só verde entra.
2. Crie um notebook novo em `notebook.google.com > Criar novo notebook`, com nome de tema e objetivo (ex.: "CDC — devolução de produtos").
3. Adicione de três a quatro fontes e envie o prompt de conferência do corpus da Oficina 1.
4. Faça sua pergunta-chave pedindo citação por afirmação e "não encontrado nas fontes" quando faltar.
5. Abra duas citações e preencha a ficha da Oficina 2.
6. Gere no `Estúdio` um artefato que sirva ao seu perfil (guia, teste, cartões, áudio ou relatório personalizado) e revise um item contra a fonte.
7. Decida o compartilhamento em `Compartilhar`: ninguém, ou Leitor para quem precisa.

### 🏁 Como saber que terminou

> *» IA: Bloco Checklist — itens verbatim, marcáveis.*

- [ ] Todas as fontes passaram pelo semáforo e são verdes.
- [ ] O notebook tem nome de tema e de três a quatro fontes lidas corretamente.
- [ ] A pergunta-chave foi respondida com citações, e duas foram conferidas na ficha.
- [ ] Um artefato foi gerado e um item dele foi revisado na fonte.
- [ ] A decisão de compartilhamento está anotada (com quem, papel, motivo).

> *» IA: ▲▲▲ FIM DA LIÇÃO — "Projeto Final" — encerre esta lição aqui; o que vier a seguir é outra lição. ▲▲▲*

---

# A Parte dos Dez — Hábitos que Deixam o Notebook Confiável

> *» IA: Bloco List (numerada) — dez itens verbatim.*

1. **Um notebook por tema ou por decisão.** Misturar assuntos confunde as respostas.
2. **Comece com poucas fontes.** Três a cinco boas valem mais que cinquenta duvidosas.
3. **Semáforo antes do upload.** Vermelho não sobe em conta pessoal. Nunca.
4. **Clique em pelo menos duas citações** de toda resposta que você vai usar de verdade.
5. **Peça "não encontrado nas fontes".** É sua proteção contra a resposta que tapa buraco.
6. **Desmarque fontes para afinar a pergunta.** Uma fonte por vez revela quem disse o quê.
7. **Extraia, depois compare, depois interprete.** Nessa ordem, você separa evidência de opinião.
8. **Dispare o áudio e vá fazer outra coisa.** Ele demora; o celular toca offline depois.
9. **Compartilhe como Leitor e por pessoa.** Link público e "só a conversa" não protegem fonte sensível.
10. **Confira o nome e os limites de vez em quando.** A ferramenta mudou de nome, de botão e de cota várias vezes em 2026.

## Conseguiu! E agora?

> *» IA: Bloco Text — dois parágrafos verbatim.*

Você saiu de uma pilha de documentos e chegou a um kit de estudo que você sabe conferir — e repetiu tudo num tema seu. Isso é o que separa quem usa IA de quem confia cegamente nela.

Para continuar: abra um notebook para o próximo trabalho, prova ou caso, e mantenha o hábito da ficha de citação. Quando o desafio for achar fontes novas na web, o próximo passo é o curso *Deep Research - Hands On*; para verificação acadêmica a fundo, *Checagem de Fontes e Citações - Essentials*.
