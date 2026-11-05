# Plano de Aula — Gemini no Google Workspace (Essentials)

**Público-Alvo:** profissionais administrativos, analistas, educadores, estudantes e servidores públicos iniciantes em IA aplicada ao trabalho.

**Objetivo Geral:** compreender o funcionamento do Gemini incorporado ao Google Workspace e aplicar, com segurança e verificação humana, recursos de redação, síntese e análise no Gmail, Docs e Sheets. Ao final, o participante terá produzido e auditado um mini fluxo de atualização executiva com dados fictícios.

**Pré-requisitos:** uso básico de Gmail, Docs e Sheets; nenhuma experiência prévia com IA. Para executar todas as práticas, requer-se edição Business Standard/Plus ou Enterprise qualificada, recursos inteligentes ativos e liberação administrativa.

> Nota de vigência: planos, preços, idiomas, limites, rótulos e recursos beta foram pesquisados em 05/11/2026. Itens marcados **[conferir]** dependem de teste na conta brasileira de produção.

## Estrutura do Curso

| Nível | Módulo | Título | Tempo MET |
|---|---:|---|---:|
| Pré-filtro | 0 | Ambiente, conta e disponibilidade | 7 min |
| Fundamentos | 1 | O que é o Gemini no Workspace | 21 min |
| Fundamentos | 2 | Segurança, privacidade e verificação | 19 min |
| Aplicação | 3 | Gmail e Docs: redigir e resumir | 21 min |
| Aplicação | 4 | Sheets, Drive e Meet: analisar e acompanhar | 21 min |
| Integração | 5 | Prompts e fluxo entre aplicativos | 20 min |
| Síntese | 6 | Síntese e Aplicação Integrada | 20 min |
| **Total** |  |  | **129 min** |

**Fio condutor:** a ideia de **copiloto com checklist** é plantada no Módulo 1 e retomada na seleção de dados, na redação, na análise e na síntese. O copiloto prepara; o checklist impede que rascunho seja confundido com decisão.

**Fronteira:** Slides, Chat, Gems e Vids são citados; Workspace Studio, agentes entre aplicativos, DLP, Vault e administração avançada ficam para cursos posteriores.

---

## Módulo 0 — Ambiente, conta e disponibilidade

### 0.1 Pré-filtro antes do uso

- **📸 Sugestão de Prints:** navegador com Gmail aberto; avatar da Conta Google destacado; canto superior direito com `Peça ao Gemini` destacado; segunda imagem com a ausência do painel e um quadro apontando plano, idioma, recursos inteligentes e administrador como itens de verificação.

O curso utiliza a versão web no computador. O conjunto de recursos varia conforme edição, idioma, região, implantação e controles do administrador. Business Starter concentra IA no Gmail e Vids; Standard e Plus liberam, em regra, os painéis de Docs, Sheets, Slides, Drive, Chat e Meet. Conta pessoal gratuita não equivale a Workspace Standard.

### 0.2 Registro de ambiente

"""
Conta: [corporativa | educacional | pessoal]
Edição/plano: [nome]
Idioma: [pt-BR | outro]
Recursos inteligentes: [ativos | não confirmado]
Peça ao Gemini aparece em: [Gmail | Docs | Sheets | Drive | outros]
Administrador liberou o recurso: [sim | não | não se aplica]
Rota de contingência: [executar | acompanhar demonstração]
"""

### Pílula Hands-on — Diagnóstico (7 min)

1. Entrar na conta correta e registrar o tipo e a edição.
2. Abrir Gmail, Docs e Sheets no computador.
3. Localizar `Peça ao Gemini` no canto superior direito.
4. Se não aparecer, conferir plano, idioma, recursos inteligentes e administrador, nessa ordem.
5. Preencher o registro de ambiente.

**Critério de êxito:** o registro informa onde o recurso está disponível e define uma rota de contingência sem prometer paridade entre contas.

### Solução de Problemas

| Situação | Causa provável | Procedimento |
|---|---|---|
| Painel aparece apenas no Gmail | edição Starter ou implantação parcial | executar Gmail e acompanhar as demais práticas por demonstração |
| Painel não aparece em nenhum app | conta, idioma, recursos inteligentes ou administrador | validar os quatro itens e acionar o suporte institucional |
| Interface difere do roteiro | atualização contínua | procurar a ação equivalente e marcar o rótulo para conferência |

## Descrição

- **Objetivos da Aula:** apresentar os requisitos técnicos e diagnosticar a disponibilidade real.
- **Habilidades Esperadas:** o participante identifica sozinho conta, plano, aplicativos disponíveis e rota de contingência.

---

## Módulo 1 — O que é o Gemini no Workspace

> Pré-requisito: Módulo 0. Desloca-se o foco da disponibilidade para o modelo mental do serviço.

### 1.1 App separado, painel incorporado e contexto

- **📸 Sugestão de Prints:** montagem em duas colunas: `gemini.google.com` à esquerda e painel `Peça ao Gemini` aberto no Gmail à direita; destacar que o painel permanece dentro do aplicativo e utiliza o contexto permitido.

O **app Gemini** é um assistente separado, acessado pelo site ou aplicativo móvel. O **Gemini no Workspace** é o conjunto de recursos incorporados a Gmail, Docs, Sheets, Slides, Drive, Meet e Chat. No painel lateral, o pedido e a resposta permanecem no fluxo de trabalho do aplicativo aberto.

IA generativa é um sistema capaz de produzir texto, imagem ou estrutura a partir de um pedido e de contexto. Ela não funciona como base de dados infalível. A analogia adotada neste curso é a de um **copiloto com checklist**: o copiloto acelera a preparação; o responsável continua verificando rota, dados e decisão.

O contexto pode vir da mensagem aberta, do documento, da planilha ou de arquivos adicionados como fonte. Menções `@` e a opção `Fontes` permitem selecionar materiais aos quais a conta já tem acesso. Permissão de acesso continua valendo: a IA não deveria ser tratada como atalho para contornar controles.

### 1.2 Mapa de recursos e planos

- **📸 Sugestão de Prints:** tabela de comparação com a linha Starter destacando Gmail/Vids e a linha Standard/Plus destacando Gmail, Docs, Sheets, Slides, Drive, Meet e Chat.

| Contexto | Núcleo disponível para este curso |
|---|---|
| Business Starter | sobretudo Gmail e Vids; não prometer painel em Docs/Sheets/Drive |
| Business Standard/Plus | núcleo completo das práticas, sujeito a administração e idioma |
| Enterprise elegível | núcleo e controles avançados |
| Conta pessoal/Google AI | disponibilidade própria por país, idioma e experimento |

### 1.3 Prompt-base — inventário de contexto

"""
Tarefa: [o que precisa ser produzido]
Contexto autorizado: [mensagem, documento, planilha ou arquivos]
Dados que não devem ser usados: [listar]
Formato da saída: [tópicos, tabela, e-mail]
Verificação obrigatória: [fonte, cálculo ou aprovação humana]
"""

### Pílula Hands-on — Escolha do ambiente (6 min)

Analisar três cenários — resposta a e-mail, resumo de documento e análise de despesas — e indicar o aplicativo, o contexto necessário e a verificação humana.

**Critério de êxito:** cada cenário associa tarefa, aplicativo, contexto e verificação, sem supor acesso a dados não autorizados.

## Descrição

- **Objetivos da Aula:** diferenciar app e integração, explicar contexto, permissões e variação por plano.
- **Habilidades Esperadas:** o participante escolhe o ambiente adequado e descreve o Gemini como apoio, não como autoridade final.

---

## Módulo 2 — Segurança, privacidade e verificação

> Pré-requisito: Módulo 1. Antes do primeiro uso real, decide-se o que pode integrar o contexto do copiloto.

### 2.1 Proteção empresarial não é autorização irrestrita

- **📸 Sugestão de Prints:** tela institucional de privacidade/segurança do Workspace ao lado de um checklist com Finalidade, Minimização, Permissão, Revisão e Retenção destacados.

Para contas corporativas e educacionais qualificadas, o Google declara que dados do Workspace não são usados para treinar ou melhorar modelos generativos fora do Workspace sem permissão. Conteúdo e interações permanecem sujeitos às proteções do domínio. Essa declaração não autoriza inserir qualquer dado: finalidade, base legal, política institucional, minimização e controle de acesso continuam necessários.

Em conta pessoal, termos e controles são diferentes. Não se deve prometer proteção empresarial a um endereço `@gmail.com` sem verificar o plano e a tela de privacidade. O envio voluntário de feedback pode incluir prompt, contexto e saída; por isso, informações pessoais, sensíveis ou confidenciais não devem acompanhar feedback.

### 2.2 Checklist antes do prompt

| Pergunta | Evidência esperada |
|---|---|
| Há finalidade legítima? | tarefa e destinatário definidos |
| O dado é necessário? | identificadores removidos quando dispensáveis |
| A conta e o plano foram aprovados? | política ou orientação institucional |
| As permissões estão corretas? | acesso aos arquivos revisado |
| Quem revisará a saída? | responsável humano identificado |

### 2.3 Prompt-base — regra de lacunas

"""
Use apenas o contexto fornecido. Não complete lacunas com suposições.
Quando uma informação não estiver nas fontes, escreva "não consta".
Separe fatos, inferências e recomendações. Indique o que precisa de revisão humana.
"""

### Pílula Hands-on — Semáforo de dados (6 min)

Classificar como verde, amarelo ou vermelho: comunicado público; relatório interno sem dados pessoais; planilha com CPF e avaliação individual. Para cada um, indicar conta adequada e ação de minimização.

**Gabarito:** público = verde; interno autorizado = amarelo; dado pessoal/sigiloso sem base e controles = vermelho.

## Descrição

- **Objetivos da Aula:** explicar proteções, limites, minimização, permissões e revisão.
- **Habilidades Esperadas:** o participante decide se um dado pode ser usado, em qual ambiente e com quais controles.

---

## Módulo 3 — Gmail e Docs: redigir e resumir

> Pré-requisito: Módulo 2. Passa-se do contexto autorizado à produção de texto verificável.

### 3.1 Gmail — rascunho sob controle

- **📸 Sugestão de Prints:** `Gmail > Escrever` com `Me ajude a escrever` destacado; segunda tela com opções `Deixar mais formal`, `Usar tom simpático` e `Encurtar`; destinatário, fatos e anexos destacados para revisão final.

No Gmail, o Gemini pode redigir, refinar e resumir mensagens. O pedido deve declarar destinatário, objetivo, informações permitidas, tom, extensão e fatos que não podem ser inventados. Antes do envio, revisam-se destinatários, datas, compromissos e anexos.

### 3.2 Docs — síntese com rastreabilidade

- **📸 Sugestão de Prints:** painel `Peça ao Gemini` no Docs com um pedido de resumo; botão `Fontes` ou menção `@` destacado; saída separada em fatos, decisões e pendências; opção de inserir somente após revisão.

No Docs, o painel cria, resume e reescreve texto. Arquivos do Drive podem ser adicionados como fontes. Um resumo útil separa categorias e declara `não consta` quando o documento não contém a informação. Atualizar a página pode apagar histórico recente não inserido; a versão conferida deve ser registrada no documento.

### 3.3 Prompt-base — atualização de projeto

"""
Você é analista administrativo. Use somente o documento aberto e as fontes adicionadas.
Produza: (1) contexto em duas frases; (2) três entregas; (3) riscos;
(4) decisões; (5) pendências com responsável e prazo, se constarem.
Quando algo não estiver no material, escreva "não consta".
Separe fatos de recomendações e limite a saída a 250 palavras.
"""

### Pílula Hands-on — Redigir e resumir (6 min)

1. Gerar um rascunho de resposta a uma solicitação fictícia.
2. Resumir um relatório fictício no Docs.
3. Preencher uma ficha: item gerado, trecho-fonte, confere?, decisão humana.

**Critério de êxito:** nenhum fato ou prazo foi inventado e cada item do resumo tem apoio no documento.

### Solução de Problemas

| Situação | Procedimento |
|---|---|
| Rascunho inventa prazo | exigir `não invente datas; escreva a confirmar` |
| Resumo mistura fato e sugestão | separar categorias e exigir marcação de inferências |
| Fonte não aparece com `@` | confirmar acesso ao arquivo e usar `Fontes > Adicionar` **[conferir]** |

## Descrição

- **Objetivos da Aula:** ensinar redação e síntese com contexto, limites e revisão.
- **Habilidades Esperadas:** o participante produz rascunho e resumo auditáveis sem criar fatos.

---

## Módulo 4 — Sheets, Drive e Meet: analisar e acompanhar

> Pré-requisito: Módulo 3. Amplia-se a verificação textual para números, arquivos e reunião.

### 4.1 Sheets — análise que precisa ser recalculada

- **📸 Sugestão de Prints:** painel no Sheets com pedido de totais e variações; prévia de gráfico com `Etapas da análise`; células com fórmulas `SOMA` usadas para conferência; exemplo de `=AI()` com o botão `Gerar e inserir`.

O painel no Sheets pode criar tabelas, fórmulas, análises e gráficos. O gráfico gerado pode ser colocado em nova guia e não permanecer ligado à origem. A função `=AI()` ou `=Gemini()` produz texto, resumo e classificação; não acessa automaticamente toda a planilha, não pode ser aninhada e não substitui fórmula determinística.

### 4.2 Drive e Meet — fontes e consentimento

- **📸 Sugestão de Prints:** arquivo ou pasta selecionada no Drive com `Resumir` destacado; painel com uma fonte `@`; no Meet, controle `Tome notas por mim` **[conferir]** e aviso de consentimento/idioma.

No Drive, o Gemini pode resumir arquivos e uma pasta por vez, mas a resposta pode não incluir todos os arquivos. Convém mencionar arquivos-chave com `@` e conferir a origem. No Meet, `Tome notas por mim` produz notas em Docs; a reunião deve usar um idioma por vez e pode exigir consentimento explícito e liberação administrativa.

### 4.3 Prompt-base — análise de despesas

"""
Você é analista de controle. Analise somente a tabela aberta.
Calcule total previsto, total realizado, variação absoluta e percentual.
Aponte as três maiores diferenças e possíveis duplicidades como hipóteses.
Mostre as etapas e não altere nem exclua dados.
Entregue em tabela e liste o que precisa ser conferido com fórmula convencional.
"""

### Pílula Hands-on — Cálculo conferido (6 min)

Executar a análise em tabela fictícia e conferir totais com `SOMA`, subtração e filtro. Registrar uma limitação do recurso.

**Critério de êxito:** os totais conferem; duplicidade permanece hipótese; nenhuma linha é apagada automaticamente.

### Solução de Problemas

| Situação | Procedimento |
|---|---|
| Arquivo é Excel | usar `Arquivo > Salvar como Planilha Google` |
| Gráfico não acompanha alterações | recriar ou vincular manualmente; não assumir atualização automática |
| `=AI()` não funciona | conferir plano, idioma, administrador, arquivo nativo e limite de uso |
| Resumo de pasta omite arquivos | reduzir escopo e citar arquivos-chave com `@` |

## Descrição

- **Objetivos da Aula:** explicar análise, função de IA, fontes no Drive e notas no Meet.
- **Habilidades Esperadas:** o participante confere números, reconhece limites e usa fontes/reuniões de forma controlada.

---

## Módulo 5 — Prompts e fluxo entre aplicativos

> Pré-requisito: Módulos 3 e 4. Organizam-se as tarefas em um briefing reutilizável.

### 5.1 Persona, tarefa, contexto e formato

- **📸 Sugestão de Prints:** diagrama de quatro campos — Persona, Tarefa, Contexto e Formato — preenchido com o exemplo de atualização executiva; abaixo, bloco `Verificação` como quinto campo operacional.

O guia oficial recomenda quatro elementos: persona, tarefa, contexto e formato. Para uso responsável, acrescenta-se a verificação. Clareza e especificidade reduzem respostas genéricas, mas não eliminam erro. Iterar significa ajustar o briefing e conferir novamente, não pedir versões até que uma pareça convincente.

### 5.2 Workflow de atualização executiva

- **📸 Sugestão de Prints:** fluxo horizontal `Sheets: conferir números > Docs: sintetizar > Gmail: comunicar`, com um losango `revisão humana` antes de cada seta.

O fluxo deste curso começa pela evidência numérica no Sheets, transforma evidências em resumo no Docs e só depois redige a comunicação no Gmail. Cada transferência conserva a fonte e registra o que foi verificado. Recursos agentivos beta não são necessários e não compõem o exercício.

### Pílula Hands-on — Briefing completo (6 min)

Reescrever `faça uma atualização` com persona, tarefa, contexto, formato, proibição de inventar e critério de verificação.

**Critério de êxito:** outra pessoa consegue executar o pedido e identificar o que deve conferir.

## Descrição

- **Objetivos da Aula:** estruturar comandos e organizar um fluxo rastreável entre aplicativos.
- **Habilidades Esperadas:** o participante redige briefings completos e preserva evidências ao transferir resultados.

---

## Módulo 6 — Síntese e Aplicação Integrada

> Pré-requisito: todos os módulos. O participante executa o fluxo completo com autonomia.

### 6.1 Atividade integradora — atualização executiva conferida

- **📸 Sugestão de Prints:** três telas lado a lado: totais conferidos no Sheets, resumo inserido no Docs e rascunho não enviado no Gmail; uma ficha de auditoria preenchida abaixo.

1. Confirmar conta, plano e dados fictícios.
2. Analisar a planilha de despesas e conferir totais com fórmulas.
3. Resumir o relatório no Docs e marcar `não consta` para lacunas.
4. Redigir e-mail no Gmail com os fatos conferidos, sem inventar prazo ou anexo.
5. Preencher a ficha de auditoria.

"""
Entregável: [Sheets | Docs | Gmail]
Fonte usada: [arquivo/mensagem]
Verificação realizada: [fórmula, comparação, permissão]
Limitação observada: [qual]
Decisão humana: [aceitar, corrigir, não usar]
"""

| Critério de avaliação | Atendido? |
|---|---|
| Conta e plano diagnosticados | [ ] |
| Dados fictícios e minimizados | [ ] |
| Comandos com persona, tarefa, contexto e formato | [ ] |
| Totais recalculados | [ ] |
| Resumo sustentado pelo documento | [ ] |
| Rascunho revisado e não enviado | [ ] |
| Limitações registradas | [ ] |

### Solução de Problemas

| Situação | Procedimento |
|---|---|
| Um recurso não está disponível | usar a rota de demonstração do Módulo 0 e documentar a limitação |
| Resultados divergem entre apps | voltar à fonte, reduzir o escopo e refazer a transferência |
| O fluxo ficou longo | preservar verificação; remover extensões, não etapas de controle |

## Descrição

- **Objetivos da Aula:** integrar diagnóstico, segurança, prompting, execução e auditoria.
- **Habilidades Esperadas:** o participante conduz sozinho um fluxo entre três aplicativos e justifica cada decisão humana.

---

# Encerramento

O curso demonstrou que o ganho de produtividade depende da adequação do ambiente, da qualidade do briefing e da verificação. Recomenda-se repetir o fluxo com tarefas de baixo risco e dados fictícios antes de adotar documentos reais.

Como aprofundamento, poderão ser estudados Slides, Chat, Gems, Vids, notas de reunião, administração e Workspace Studio. Recursos beta devem ser revalidados antes de uso institucional.

> **Síntese:** o Gemini acelera o trabalho quando contexto, permissão e verificação permanecem sob responsabilidade humana.

## Rastreabilidade da auditoria

| Achado | Destino |
|---|---|
| Pré-filtro ausente | Módulo 0 |
| Planos vagos | Módulo 1, quadro de recursos |
| Segurança genérica | Módulo 2, checklist antes do prompt |
| Navegação e falhas | sugestões de prints e troubleshooting nos módulos 0, 3 e 4 |
| Verificação sem evidência | ficha de auditoria nos módulos 3 e 6 |
| Limites técnicos | Módulo 4 |
| Meet sem consentimento | Módulo 4.2 |
| Beta misturado ao núcleo | Fronteira e encerramento |

