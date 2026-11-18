# Roteiro de produção - Replit Agent Hands-on

## Análise essencial do material-fonte

- O participante produz o app Minha Estante com dados fictícios.
- Segurança e limite de gasto antecedem a construção.
- Persistência, isolamento, checkpoint e recuperação são critérios de êxito.
- Publicação pode ser substituída por simulação documentada quando faltar crédito ou autorização.
- A carga MET é 128 minutos em quatro oficinas e um Projeto Final.

## Identificação

- Curso: Replit Agent - Hands-on.
- Lições: 4 oficinas e 1 Projeto Final.
- Formato: autoinstrucional e assíncrono.
- Público: iniciantes sem experiência em programação.
- Pré-requisitos: conta Replit, navegador, internet e revisão prévia de gastos.
- Tempo estimado: 128 minutos.
- Recursos: dados fictícios e, opcionalmente, segunda conta para teste.

## Objetivo geral

Criar, testar e preparar para publicação um aplicativo simples com autenticação e persistência, aplicando controles de custo e segurança.

## Objetivos de aprendizagem

- Delimitar um MVP seguro e testável.
- Criar e revisar um aplicativo no Agent.
- Testar persistência e isolamento por usuário.
- Corrigir falhas e identificar recuperação.
- Publicar e monitorar ou justificar o adiamento.

# Oficina 1 - Prepare o terreno

## Ficha de produção da lição

- Objetivo: produzir um brief seguro e compatível com o orçamento.
- Resultado observável: brief sem dados reais e decisão explícita de gasto.

| Etapa | Conteúdo | Bloco Rise 360 |
|---|---|---|
| Problema | Pedido vago gera custo e risco | Cover + Text |
| Execução | Usage, limite e brief | Process |
| Validação | Critérios e decisão | Knowledge Check + Checklist |

> A ficha orienta a produção e não deve aparecer no curso publicado.

> » IA: ▼▼▼ INÍCIO DA LIÇÃO - "Oficina 1 - Prepare o terreno" - todo o conteúdo até o marcador de fim corresponde a UMA única lição no Rise 360; não dividir, duplicar, fundir ou criar sublições. Não publicar este marcador. ▼▼▼

> » IA: BLOCO RISE 360 - Cover. Usar fundo sólido e alto contraste. Não publicar esta linha.

BLOCO RISE 360
Cover

- Título visível: Prepare o terreno
- Configuração: fundo sólido, sem imagem.
- Conteúdo visível: Defina escopo, gasto e dados antes do primeiro Build.

> » IA: BLOCO RISE 360 - Text. Apresentar o problema em dois parágrafos curtos. Não publicar esta linha.

BLOCO RISE 360
Text

- Título visível: O problema
- Configuração: texto simples.
- Conteúdo visível: Um pedido vago pode gerar recursos extras, custo e retrabalho. Dados reais também podem parar em prompts, telas e logs.

  Você vai definir um MVP de cadastro de leituras, revisar Usage e remover qualquer informação real antes da construção.

> » IA: BLOCO RISE 360 - Process. Preservar o prompt verbatim e os breadcrumbs. Não publicar esta linha.

BLOCO RISE 360
Process

- Título visível: Prepare o brief
- Configuração: cinco etapas.
- Conteúdo visível:
  1. **Entre na conta:** acesse a Replit e confirme que está na conta destinada ao exercício.
  2. **Revise o consumo:** siga `Replit > Settings > Usage` e observe consumo e limites. Se o caminho variar, localize a área de uso sem confirmar ação paga. 🏁 Ponto de controle: o limite ou a decisão de não gastar está registrado.
  3. **Defina o teto:** use a opção de limite quando disponível ou adote a regra de não confirmar ação paga.
  4. **Copie o brief:** """Crie um aplicativo web chamado Minha Estante. Cada usuário vê apenas seus próprios livros. Cada livro tem título obrigatório, autor, status, nota e observações. Use dados fictícios."""
  5. **Faça a revisão:** remova nomes, e-mails, documentos, chaves e dados institucionais reais. 🏁 Ponto de controle: o brief contém somente regras e dados fictícios.

> » IA: BLOCO RISE 360 - Knowledge Check - Multiple Choice. Habilitar nova tentativa. Não publicar esta linha.

BLOCO RISE 360
Knowledge Check - Multiple Choice

- Título visível: Antes de confirmar
- Configuração: uma resposta correta; nova tentativa habilitada.
- Conteúdo visível: A estimativa supera o teto definido. O que fazer primeiro?
  - A. Confirmar e reduzir depois.
  - B. Reduzir o escopo ou não confirmar.
  - C. Trocar de modo sem rever a estimativa.
- Gabarito e feedback: B. Acerto: limite e escopo precisam concordar antes da ação. Erro: confirmar ou apenas mudar de modo não controla o compromisso financeiro.

> » IA: BLOCO RISE 360 - Accordion. Incluir dois bloqueios reais. Não publicar esta linha.

BLOCO RISE 360
Accordion

- Título visível: Se travar
- Configuração: dois itens.
- Conteúdo visível:
  - **Usage não aparece:** não confirme ação paga e registre a interface para validação posterior.
  - **O brief ficou grande:** preserve público, campos, regra por usuário e critério de êxito; retire recursos adicionais.

> » IA: BLOCO RISE 360 - Checklist. Confirmar o resultado observável. Não publicar esta linha.

BLOCO RISE 360
Checklist

- Título visível: Deu certo?
- Configuração: três itens.
- Conteúdo visível:
  - O brief descreve somente o MVP.
  - Não há dado nem chave real.
  - O teto de gasto ou a decisão de não gastar está explícito.

> » IA: ▲▲▲ FIM DA LIÇÃO - "Oficina 1 - Prepare o terreno" - encerrar esta lição aqui. Não publicar este marcador. ▲▲▲

# Oficina 2 - Construa o MVP

## Ficha de produção da lição

- Objetivo: iniciar o Project, revisar o escopo e validar o primeiro Preview.
- Resultado observável: formulário e lista visíveis, com checkpoint identificável.

| Etapa | Conteúdo | Bloco Rise 360 |
|---|---|---|
| Problema | Primeiro resultado testável | Cover + Text |
| Execução | Project, Plan/Build e Preview | Process |
| Validação | Escopo e checkpoint | Knowledge Check + Checklist |

> A ficha orienta a produção e não deve aparecer no curso publicado.

> » IA: ▼▼▼ INÍCIO DA LIÇÃO - "Oficina 2 - Construa o MVP" - todo o conteúdo até o marcador de fim corresponde a UMA única lição no Rise 360; não dividir, duplicar, fundir ou criar sublições. Não publicar este marcador. ▼▼▼

> » IA: BLOCO RISE 360 - Cover. Usar fundo sólido. Não publicar esta linha.

BLOCO RISE 360
Cover

- Título visível: Construa o MVP
- Configuração: fundo sólido, sem imagem.
- Conteúdo visível: Gere pouco, revise cedo e teste antes de ampliar.

> » IA: BLOCO RISE 360 - Text. Apresentar o problema. Não publicar esta linha.

BLOCO RISE 360
Text

- Título visível: O problema
- Configuração: um parágrafo.
- Conteúdo visível: O primeiro resultado precisa provar o cadastro, não impressionar com recursos extras. Você vai iniciar um Project, revisar a proposta e conferir o Preview.

> » IA: BLOCO RISE 360 - Process. Uma ação principal por etapa e breadcrumbs preservados. Não publicar esta linha.

BLOCO RISE 360
Process

- Título visível: Do brief ao Preview
- Configuração: sete etapas.
- Conteúdo visível:
  1. **Inicie o projeto:** siga `Replit > Create Project` e selecione Web app quando a opção estiver disponível.
  2. **Envie o brief:** cole o texto validado na caixa do Agent.
  3. **Revise o plano:** se houver Plan Mode, use `Agent > Plan`, revise tarefas e escolha `Revise plan` até o escopo corresponder ao MVP. Sem Plan Mode, escreva que a construção deve ser pequena e sem recursos extras.
  4. **Revise o custo:** confirme somente depois de comparar a estimativa com o teto.
  5. **Construa:** use Build e aguarde a conclusão dos testes do Agent.
  6. **Abra a prévia:** siga `Project Editor > Preview` e confira formulário e lista. 🏁 Ponto de controle: ambos aparecem sem erro de inicialização.
  7. **Leia o resumo:** localize o resumo de mudanças e o checkpoint. 🏁 Ponto de controle: o estado de retorno está identificável.

> » IA: BLOCO RISE 360 - Knowledge Check - Multiple Choice. Habilitar nova tentativa. Não publicar esta linha.

BLOCO RISE 360
Knowledge Check - Multiple Choice

- Título visível: Proteja o escopo
- Configuração: uma resposta correta; nova tentativa habilitada.
- Conteúdo visível: O Agent adicionou chat e pagamentos fora do brief. O que fazer?
  - A. Manter porque já foi criado.
  - B. Pedir a remoção dos extras e preservar o MVP.
  - C. Publicar para decidir depois.
- Gabarito e feedback: B. Acerto: remover extras reduz custo e superfície de risco. Erro: recurso gerado não se torna requisito automaticamente.

> » IA: BLOCO RISE 360 - Accordion. Incluir dois sintomas e soluções. Não publicar esta linha.

BLOCO RISE 360
Accordion

- Título visível: Se travar
- Configuração: dois itens.
- Conteúdo visível:
  - **O Preview não abre:** peça ao Agent que teste a inicialização e faça somente o menor ajuste necessário.
  - **O resultado divergiu do brief:** cite a regra descumprida e peça correção sem novas funcionalidades.

> » IA: BLOCO RISE 360 - Checklist. Confirmar pequena vitória. Não publicar esta linha.

BLOCO RISE 360
Checklist

- Título visível: Deu certo?
- Configuração: três itens.
- Conteúdo visível:
  - Formulário e lista aparecem no Preview.
  - Não há recurso funcional fora do MVP.
  - Resumo e checkpoint foram localizados.

> » IA: ▲▲▲ FIM DA LIÇÃO - "Oficina 2 - Construa o MVP" - encerrar esta lição aqui. Não publicar este marcador. ▲▲▲

# Oficina 3 - Guarde dados por usuário

## Ficha de produção da lição

- Objetivo: configurar persistência e autenticação e testar isolamento.
- Resultado observável: registros persistem e não aparecem para outro usuário.

| Etapa | Conteúdo | Bloco Rise 360 |
|---|---|---|
| Problema | Dados que somem ou vazam | Cover + Text |
| Execução | Auth, banco e testes | Process |
| Validação | Decisão de bloqueio | Knowledge Check + Checklist |

> A ficha orienta a produção e não deve aparecer no curso publicado.

> » IA: ▼▼▼ INÍCIO DA LIÇÃO - "Oficina 3 - Guarde dados por usuário" - todo o conteúdo até o marcador de fim corresponde a UMA única lição no Rise 360; não dividir, duplicar, fundir ou criar sublições. Não publicar este marcador. ▼▼▼

> » IA: BLOCO RISE 360 - Cover. Usar fundo sólido. Não publicar esta linha.

BLOCO RISE 360
Cover

- Título visível: Guarde dados por usuário
- Configuração: fundo sólido, sem imagem.
- Conteúdo visível: Persistir não basta: é preciso autorizar corretamente.

> » IA: BLOCO RISE 360 - Text. Reforçar dados fictícios. Não publicar esta linha.

BLOCO RISE 360
Text

- Título visível: O problema
- Configuração: dois parágrafos.
- Conteúdo visível: Um registro que desaparece após atualizar não está persistindo. Um registro que aparece para a pessoa errada representa falha de autorização.

  Use somente títulos, autores e observações fictícios. Não use dados pessoais ou institucionais reais.

> » IA: BLOCO RISE 360 - Process. Preservar os prompts verbatim. Não publicar esta linha.

BLOCO RISE 360
Process

- Título visível: Persistência e isolamento
- Configuração: sete etapas.
- Conteúdo visível:
  1. **Peça os recursos:** """Adicione Replit Auth e banco PostgreSQL integrado. Cada usuário deve acessar somente os próprios livros."""
  2. **Crie registros:** no Preview, cadastre dois livros fictícios.
  3. **Teste o refresh:** atualize a página. 🏁 Ponto de controle: os dois registros permanecem.
  4. **Teste a sessão:** saia e entre novamente. 🏁 Ponto de controle: os registros permanecem associados ao mesmo usuário.
  5. **Teste outra conta:** em sessão separada, confirme que a segunda conta não vê os registros da primeira.
  6. **Use alternativa parcial:** sem segunda conta, peça teste automatizado de autorização e marque o teste humano como pendente.
  7. **Pare diante de vazamento:** se outra conta vir os registros, não continue para publicação.

> » IA: BLOCO RISE 360 - Knowledge Check - Multiple Choice. Habilitar nova tentativa. Não publicar esta linha.

BLOCO RISE 360
Knowledge Check - Multiple Choice

- Título visível: Decisão de segurança
- Configuração: uma resposta correta; nova tentativa habilitada.
- Conteúdo visível: Os dados persistem, mas outra conta os vê. O que fazer?
  - A. Publicar e avisar os usuários.
  - B. Interromper, corrigir autorização e repetir o teste.
  - C. Ocultar o botão de login.
- Gabarito e feedback: B. Acerto: vazamento entre usuários bloqueia a publicação. Erro: aviso ou ocultação de interface não corrige a autorização.

> » IA: BLOCO RISE 360 - Accordion. Incluir três bloqueios. Não publicar esta linha.

BLOCO RISE 360
Accordion

- Título visível: Se travar
- Configuração: três itens.
- Conteúdo visível:
  - **Dados somem no refresh:** peça para verificar se o app usa o banco, não apenas armazenamento do navegador.
  - **Outra conta vê os dados:** interrompa o fluxo, corrija a consulta por usuário e repita o teste.
  - **Login não abre:** confirme se Replit Auth foi habilitado e peça o menor ajuste necessário.

> » IA: BLOCO RISE 360 - Checklist. Confirmar o resultado. Não publicar esta linha.

BLOCO RISE 360
Checklist

- Título visível: Deu certo?
- Configuração: três itens.
- Conteúdo visível:
  - Os registros permanecem após atualizar e entrar novamente.
  - Uma segunda conta não acessa os registros da primeira, ou o teste humano está marcado como pendente.
  - Nenhum dado real foi inserido.

> » IA: ▲▲▲ FIM DA LIÇÃO - "Oficina 3 - Guarde dados por usuário" - encerrar esta lição aqui. Não publicar este marcador. ▲▲▲

# Oficina 4 - Teste, corrija e saiba voltar

## Ficha de produção da lição

- Objetivo: executar teste regressivo, correção mínima e análise de recuperação.
- Resultado observável: percurso principal validado e mecanismo de retorno identificado.

| Etapa | Conteúdo | Bloco Rise 360 |
|---|---|---|
| Problema | Correção pode criar regressão | Cover + Text |
| Execução | Teste, correção, History e Security | Process |
| Validação | Desenvolvimento versus produção | Knowledge Check + Checklist |

> A ficha orienta a produção e não deve aparecer no curso publicado.

> » IA: ▼▼▼ INÍCIO DA LIÇÃO - "Oficina 4 - Teste, corrija e saiba voltar" - todo o conteúdo até o marcador de fim corresponde a UMA única lição no Rise 360; não dividir, duplicar, fundir ou criar sublições. Não publicar este marcador. ▼▼▼

> » IA: BLOCO RISE 360 - Cover. Usar fundo sólido. Não publicar esta linha.

BLOCO RISE 360
Cover

- Título visível: Teste, corrija e saiba voltar
- Configuração: fundo sólido, sem imagem.
- Conteúdo visível: Uma correção só termina depois do novo teste.

> » IA: BLOCO RISE 360 - Process. Um passo por ação. Não publicar esta linha.

BLOCO RISE 360
Process

- Título visível: Valide e recupere
- Configuração: sete etapas.
- Conteúdo visível:
  1. **Execute o percurso:** crie, edite, exclua, atualize, saia e entre.
  2. **Registre o sintoma:** descreva ação, resultado esperado e resultado obtido.
  3. **Peça correção mínima:** """Não adicione funcionalidades. Corrija somente a falha descrita e diga como confirmar o resultado."""
  4. **Repita o teste:** valide primeiro a falha e depois o percurso completo. 🏁 Ponto de controle: não surgiu regressão visível.
  5. **Localize o retorno:** siga `Project Editor > Agent > History > checkpoint > Rollback to here`, mas não confirme sem decidir o escopo.
  6. **Revise o banco:** observe `Additional rollback options > Database`; essa opção se refere ao desenvolvimento.
  7. **Revise segurança:** abra o Security Center quando disponível e trate achados críticos antes de publicar.

> » IA: BLOCO RISE 360 - Statement. Uma frase curta. Não publicar esta linha.

BLOCO RISE 360
Statement

- Título visível: sem título
- Configuração: alerta.
- Conteúdo visível: Rollback comum não substitui restauração do banco de produção.

> » IA: BLOCO RISE 360 - Knowledge Check - Multiple Choice. Habilitar nova tentativa. Não publicar esta linha.

BLOCO RISE 360
Knowledge Check - Multiple Choice

- Título visível: Escolha a recuperação
- Configuração: uma resposta correta; nova tentativa habilitada.
- Conteúdo visível: O banco publicado precisa voltar a um estado anterior. O rollback comum basta?
  - A. Sim, sempre inclui produção.
  - B. Não; produção exige procedimento específico de restauração.
  - C. Sim, desde que o Preview esteja aberto.
- Gabarito e feedback: B. Acerto: desenvolvimento e produção têm recuperações distintas. Erro: Preview e rollback comum não restauram automaticamente produção.

> » IA: BLOCO RISE 360 - Accordion. Incluir dois bloqueios. Não publicar esta linha.

BLOCO RISE 360
Accordion

- Título visível: Se travar
- Configuração: dois itens.
- Conteúdo visível:
  - **A correção criou outro defeito:** retorne ao checkpoint estável e reduza o pedido.
  - **Security Center não aparece:** registre a dependência de plano ou interface e mantenha testes manuais.

> » IA: BLOCO RISE 360 - Checklist. Confirmar resultado. Não publicar esta linha.

BLOCO RISE 360
Checklist

- Título visível: Deu certo?
- Configuração: três itens.
- Conteúdo visível:
  - O percurso principal passa.
  - O checkpoint estável está identificado.
  - A diferença entre rollback de desenvolvimento e restauração de produção está clara.

> » IA: ▲▲▲ FIM DA LIÇÃO - "Oficina 4 - Teste, corrija e saiba voltar" - encerrar esta lição aqui. Não publicar este marcador. ▲▲▲

# Projeto Final - Publique e valide a Minha Estante

## Ficha de produção da lição

- Objetivo: integrar custo, segurança, teste, publicação e monitoramento.
- Resultado observável: URL pública validada ou adiamento justificado por evidências.

| Etapa | Conteúdo | Bloco Rise 360 |
|---|---|---|
| Missão | Decisão responsável de publicação | Cover + Text |
| Execução | Checklist, Publish e teste público | Process |
| Fecho | Critérios do entregável | Checklist |

> A ficha orienta a produção e não deve aparecer no curso publicado.

> » IA: ▼▼▼ INÍCIO DA LIÇÃO - "Projeto Final - Publique e valide a Minha Estante" - todo o conteúdo até o marcador de fim corresponde a UMA única lição no Rise 360; não dividir, duplicar, fundir ou criar sublições. Não publicar este marcador. ▼▼▼

> » IA: BLOCO RISE 360 - Cover. Usar fundo sólido. Não publicar esta linha.

BLOCO RISE 360
Cover

- Título visível: Publique e valide a Minha Estante
- Configuração: fundo sólido, sem imagem.
- Conteúdo visível: A missão final é decidir com evidências, não apenas clicar em Publish.

> » IA: BLOCO RISE 360 - Text. Explicar a alternativa sem gasto. Não publicar esta linha.

BLOCO RISE 360
Text

- Título visível: A missão
- Configuração: dois parágrafos.
- Conteúdo visível: Você vai revisar o projeto, publicar quando houver crédito e autorização e repetir o teste na URL pública.

  Se não puder publicar, conclua com uma simulação documentada das configurações, decisões e testes prévios. O curso não exige gasto.

> » IA: BLOCO RISE 360 - Process. Preservar breadcrumbs e pontos de controle. Não publicar esta linha.

BLOCO RISE 360
Process

- Título visível: Da revisão ao monitoramento
- Configuração: oito etapas.
- Conteúdo visível:
  1. **Revise dados:** confirme que só existem dados fictícios e nenhum Secret aparece em tela, código ou log.
  2. **Revise evidências:** confira custo, isolamento, testes e checkpoint.
  3. **Abra publicação:** siga `Project Editor > Publish` ou `Tools > Publishing`.
  4. **Revise configuração:** confira URL `.replit.app`, acesso, tipo sugerido e custo.
  5. **Decida:** confirme somente com crédito e autorização pessoal; caso contrário, registre o adiamento.
  6. **Teste a URL:** crie, atualize, saia e entre na versão pública. 🏁 Ponto de controle: o percurso principal funciona fora do Preview.
  7. **Observe operação:** confira `Tools > Publishing/Monitoring`, logs e `Settings > Usage`.
  8. **Registre o retorno:** anote o checkpoint estável e o procedimento de restauração aplicável.

> » IA: BLOCO RISE 360 - Knowledge Check - Multiple Choice. Habilitar nova tentativa. Não publicar esta linha.

BLOCO RISE 360
Knowledge Check - Multiple Choice

- Título visível: Decisão final
- Configuração: uma resposta correta; nova tentativa habilitada.
- Conteúdo visível: Os testes passam, mas não há crédito nem autorização para gasto. O que fazer?
  - A. Publicar mesmo assim.
  - B. Documentar a simulação e adiar a publicação.
  - C. Inserir um cartão sem revisar condições.
- Gabarito e feedback: B. Acerto: o objetivo é uma decisão responsável, não gasto obrigatório. Erro: autorização financeira é um requisito do projeto.

> » IA: BLOCO RISE 360 - Checklist. Usar como critérios finais. Não publicar esta linha.

BLOCO RISE 360
Checklist

- Título visível: Como saber que terminou
- Configuração: seis itens marcáveis.
- Conteúdo visível:
  - Brief e escopo do MVP estão registrados.
  - Dados fictícios persistem e permanecem isolados.
  - Testes passam no Preview.
  - Checkpoint e recuperação estão identificados.
  - URL pública foi testada ou o adiamento foi justificado.
  - Custos, logs e monitoramento foram conferidos.

> » IA: ▲▲▲ FIM DA LIÇÃO - "Projeto Final - Publique e valide a Minha Estante" - encerrar esta lição aqui. Não publicar este marcador. ▲▲▲

# A Parte dos Dez - Atalhos que Salvam seu Projeto

> » IA: BLOCO RISE 360 - List. Publicar fora das lições como seção final. Não publicar esta linha.

BLOCO RISE 360
List

- Título visível: Dez atalhos
- Configuração: lista numerada.
- Conteúdo visível:
  1. Comece pelo menor MVP útil.
  2. Declare campos e regras no primeiro pedido.
  3. Use dados fictícios.
  4. Nunca coloque chave no prompt ou no código.
  5. Teste após cada checkpoint.
  6. Descreva o sintoma e o resultado esperado.
  7. Peça a menor correção possível.
  8. Diferencie Preview de publicação.
  9. Confira Usage antes e depois de ações grandes.
  10. Saiba onde está o último estado estável.

# Conseguiu! E agora?

> » IA: BLOCO RISE 360 - Text. Encerrar com dois parágrafos curtos. Não publicar esta linha.

BLOCO RISE 360
Text

- Título visível: Próximo projeto
- Configuração: texto simples.
- Conteúdo visível: Você construiu um fluxo completo e aprendeu a não confundir geração rápida com produto confiável.

  Continue praticando com projetos fictícios e escopo pequeno. Aprofunde depois em domínio próprio, aplicativos móveis, integrações e operação de produção.

# Orientações gerais de produção no Rise 360

- Manter exatamente quatro oficinas e um Projeto Final.
- Usar títulos internos como seções e remover fichas, marcadores e linhas dirigidas à IA.
- Não adicionar mídia ou dependências externas.
- Preservar breadcrumbs e nomes de interface; validar todos antes da publicação.
- Configurar Knowledge Checks como formativos e permitir novas tentativas.
- Manter contraste, hierarquia de títulos e controles com nomes descritivos.
- Não comunicar informação apenas por cor.
- Testar os passos em computador e celular e conferir ortografia, gabaritos, feedbacks e acessibilidade.

# Pendências de validação

- Confirmar breadcrumbs e rótulos na interface vigente de uma conta brasileira.
- Confirmar disponibilidade por plano de Usage, Plan Mode, Security Center e restauração.
- Confirmar custos e limites atuais; o Starter não é garantia de conclusão gratuita.

