"""Edicoes de texto do curso ChatGPT PowerPoint - Essentials.

Fonte: roteiros/roteiro-articulate-essentials.md (Modulos 0 a 5 + Encerramento).
Mapeamento: L1 = Modulos 0+1 | L2 = Modulos 2+3 | L3 = Modulos 4+5+Encerramento | L4 = Quiz.
"""
CURSO_ORIGINAL = 'cursoChatGPTPPTEssentials.json'
PASTA = 'licoes_extraidas_ChatGPTPPTEssentials'

L1 = 'licao_01_Decidindo_e_Instalando_o_ChatGPT_no_PowerPoint.json'
L2 = 'licao_02_Produzindo_e_Editando_Apresentacoes_com_ChatGPT.json'
L3 = 'licao_03_Automatizando_Fluxos_e_Aplicacao_Integrada.json'

FORMULA_OBJETIVOS = '<p>Ao final desta lição, você será capaz de:</p>'

EDICOES = {
    # ------------------------------------------------------------------ LICAO 1
    L1: [
        ('items[0].items[0].heading', 'Antes de instalar: o arquivo passa por duas empresas'),
        ('items[0].items[0].paragraph',
         '<p>O ChatGPT para PowerPoint é executado dentro do Microsoft PowerPoint, e disso decorrem duas '
         'consequências. A primeira é jurídica: o uso do PowerPoint continua regido pelos seus contratos com a '
         'Microsoft. A segunda é prática e mais relevante: pelos Termos de Serviço do Marketplace de Suplementos, '
         'a Microsoft pode ter a capacidade de ler o conteúdo dos arquivos do PowerPoint. Somado ao processamento '
         'que a OpenAI faz para responder às instruções, o arquivo passa por duas empresas antes de voltar a você.</p>'
         '<p>Esta lição parte desse fato para decidir se o suplemento pode ser adotado no seu ambiente e, se puder, '
         'instalá-lo com segurança. Concluir que o curso não se aplica ao seu ambiente é um resultado legítimo, '
         'não uma falha.</p>'),
        ('items[1].items[0].paragraph', FORMULA_OBJETIVOS),
        ('items[2].items[0].paragraph',
         '<p>Identificar quem tem acesso ao conteúdo dos arquivos do PowerPoint quando o suplemento está instalado, '
         'e o que é processado a cada solicitação.</p>'),
        ('items[2].items[1].paragraph',
         '<p>Enumerar as categorias de informação que não devem constar de apresentação submetida ao suplemento.</p>'),
        ('items[2].items[2].paragraph',
         '<p>Situar o consumo de uso do seu plano e a consequência prática do esgotamento da cota.</p>'),
        ('items[2].items[3].paragraph',
         '<p>Distinguir a administração do Microsoft 365 da administração do espaço de trabalho do ChatGPT, e saber '
         'a qual delas encaminhar uma falha de instalação, de autenticação ou de habilitação da conta.</p>'),
        ('items[4].items[0].heading', 'O que colocar no arquivo vem antes de usar a ferramenta'),
        ('items[4].items[0].paragraph',
         '<p>Nada disso torna a ferramenta imprópria ao trabalho acadêmico. Significa que a decisão sobre o que '
         'colocar dentro do arquivo precede a decisão de usar o suplemento. Registre-se também que o sistema pode '
         'editar ou excluir conteúdo da apresentação: duplicar o arquivo antes de trabalhos importantes é '
         'recomendação do próprio fabricante e, neste curso, requisito, não sugestão.</p>'
         '<p>Antes do uso em material institucional, três perguntas precisam de resposta, e quem responde é a sua '
         'instituição, não este curso: o que a norma interna estabelece sobre IA na produção de material didático e '
         'de apresentações acadêmicas; se o uso precisa ser declarado (uma banca de qualificação, uma comunicação em '
         'congresso e um relatório a agência de fomento podem exigir coisas diferentes); e que orientação será dada '
         'aos alunos, que dispõem da mesma ferramenta para os próprios seminários.</p>'),
        ('items[5].items[0].paragraph',
         '<p>Vire cada cartão para revisar os cinco conceitos que sustentam a decisão de adoção:</p>'),
        ('items[6].items[0].back.description',
         '<p>A Microsoft, que pode ter a capacidade de ler o conteúdo dos arquivos pelos termos do Marketplace, e a '
         'OpenAI, que processa o conteúdo para responder às suas instruções.</p>'),
        ('items[6].items[1].back.description',
         '<p>A instrução digitada, o conteúdo da apresentação disponibilizado ao sistema, os anexos enviados como '
         'material de origem e o contexto de conexões autorizadas, quando houver.</p>'),
        ('items[6].items[2].back.description',
         '<p>Dado identificável de aluno, pesquisa ainda não publicada, parecer sigiloso, informação sob acordo de '
         'confidencialidade e dado pessoal de terceiros obtido em pesquisa ficam fora do arquivo.</p>'),
        ('items[6].items[3].back.description',
         '<p>Free, Go, Plus, Pro, Business, Enterprise e Edu têm acesso, mas não nas mesmas condições: Free e Go com '
         'uso limitado; Plus, Pro e Business sujeitos ao limite de uso com agentes; Business, Enterprise e Edu '
         'debitados do saldo de créditos do espaço de trabalho, quando a cobrança flexível estiver em vigor.</p>'),
        ('items[6].items[4].back.description',
         '<p>A administração do Microsoft 365 controla a instalação do suplemento; a do espaço de trabalho do '
         'ChatGPT controla a habilitação do recurso para a conta. São pedidos diferentes, a pessoas diferentes.</p>'),
        ('items[7].items[0].paragraph',
         '<p>Abra cada item para ver o que isso significa na prática antes do primeiro uso:</p>'),
        ('items[8].items[0].description',
         '<p>O suplemento roda dentro do PowerPoint: a Microsoft pode ter a capacidade de ler o conteúdo dos '
         'arquivos, e a OpenAI processa esse conteúdo para gerar as respostas.</p><p></p><p>Na prática, todo '
         'arquivo aberto com o suplemento passa por dois ambientes distintos antes de voltar a você. Essa é a '
         'base de todas as decisões seguintes.</p>'),
        ('items[8].items[3].description',
         '<p>Uma tarefa típica com o modelo GPT-5.5 pode consumir de dez a cinquenta créditos por mensagem. '
         'Apresentações maiores, edições em várias etapas e solicitações fundamentadas em fontes consomem mais, e a '
         'cota é compartilhada com outros recursos de agente do plano, inclusive o ChatGPT para Excel.</p><p></p>'
         '<p>Não planeje a preparação de uma aula em torno de uma cota que pode se esgotar na véspera: produza o '
         'rascunho com antecedência e reserve saldo para a revisão. Valores conferidos na documentação oficial em '
         '7 de outubro de 2026; confira a situação vigente na sua conta.</p>'),
        ('items[8].items[4].description',
         '<p>Uma conta pessoal gratuita e uma conta institucional Edu não oferecem as mesmas garantias quanto ao '
         'tratamento dos dados.</p><p></p><p>Em contexto institucional, confirme antes do primeiro uso real as '
         'políticas internas sobre informações confidenciais, permissões de aplicativos conectados, retenção, '
         'conformidade e compartilhamento de arquivos.</p>'),
        ('items[9].items[0].title', 'Verificação de prontidão'),
        ('items[9].items[0].description',
         '<p>Quatro verificações rápidas, feitas antes de instalar, dizem se o curso se aplica ao seu ambiente e '
         'deixam prontos os dois arquivos que protegem o seu material.</p>'),
        ('items[9].items[1].title', 'Critério de êxito'),
        ('items[9].items[1].description',
         '<p>Você consegue afirmar qual é o seu plano, qual desfecho obteve no teste de instalação e a qual das '
         'duas administrações recorreria em caso de bloqueio, e tem na pasta a apresentação de teste e a cópia de '
         'trabalho.</p>'),
        ('items[9].items[3].description',
         '<p>No PowerPoint, vá em Página Inicial (Home) &gt; Suplementos (Add-ins) e pesquise por ChatGPT. Três '
         'desfechos são possíveis agora: a loja abre e permite adicionar (instalação livre: siga em frente); a loja '
         'abre, mas a adição é bloqueada ou pede autorização (solicite a quem administra o Microsoft 365 a '
         'implantação pelo arquivo XML de manifesto); ou a loja não abre ou o recurso está indisponível (instalação '
         'negada pela política institucional).</p><p>No último caso, este curso não se aplica ao seu ambiente. A '
         'alternativa é o curso irmão ChatGPT no Word, cujo fluxo de copiar e colar não depende de suplemento.</p>'),
        ('items[9].items[4].description',
         '<p>Crie uma apresentação nova, vazia, e salve como teste-chatgpt.pptx. O primeiro contato com o suplemento '
         'será feito nela, nunca em material real.</p>'),
        ('items[10].items[0].paragraph',
         'O sistema pode editar ou excluir conteúdo da apresentação. Nunca use material real no primeiro contato '
         'com o suplemento, e duplique o arquivo antes de qualquer trabalho importante.'),
        ('items[11].items[0].paragraph',
         '<p>O aparecimento do suplemento na loja não garante que toda conta possa usá-lo. A disponibilidade final '
         'resulta da combinação dos direitos do plano, das configurações do administrador, das permissões do '
         'usuário, das autorizações das fontes de dados conectadas e da liberação gradual feita pela OpenAI.</p>'
         '<p>Em ambiente institucional, duas administrações distintas intervêm, e confundi-las é a causa mais comum '
         'de pedido de suporte mal encaminhado.</p>'),
        ('items[12].items[0].heading', 'Quem controla o quê, e quando recorrer a cada um'),
        ('items[12].items[0].paragraph',
         '<p><strong>Microsoft 365</strong> (em geral, a área de TI): controla a instalação do suplemento no '
         'PowerPoint, inclusive a implantação interna pelo arquivo XML de manifesto. Recorra a ela quando a loja de '
         'suplementos estiver bloqueada ou exigir autorização.</p><p><strong>Espaço de trabalho do ChatGPT</strong> '
         '(conta Edu, Enterprise ou Business): controla a habilitação do ChatGPT para PowerPoint nas configurações '
         'do espaço de trabalho e o acesso a apps. Recorra a ela quando o suplemento já estiver instalado, mas a '
         'conta institucional não tiver acesso ao recurso.</p><p>A implantação pelo Microsoft 365 resolve apenas a '
         'primeira etapa. São pedidos diferentes, frequentemente dirigidos a pessoas diferentes.</p>'),
        ('items[13].items[0].title', 'Instalar pelo Marketplace'),
        ('items[13].items[0].description',
         '<p>A instalação é feita na apresentação teste-chatgpt.pptx, nunca em material real. Os rótulos entre '
         'parênteses correspondem à interface do Office em inglês, comum em computadores institucionais.</p>'),
        ('items[13].items[1].title', 'Ponto de controle'),
        ('items[13].items[1].description',
         '<p>A barra lateral está visível em PowerPoint &gt; faixa de opções &gt; ChatGPT, a apresentação de teste '
         'contém o slide solicitado e o acesso às Skills foi localizado. Tudo em arquivo de teste, não em material '
         'real.</p>'),
        ('items[13].items[3].description',
         '<p>Em PowerPoint &gt; faixa de opções &gt; ChatGPT, abra a barra lateral do suplemento. É nela que a '
         'conversa acontece; o símbolo de adição dá acesso às Skills e aos apps, tratados na última lição.</p>'),
        ('items[13].items[4].description',
         '<p>Entre com a conta do ChatGPT identificada na verificação de prontidão. Em seguida, envie: "Crie um '
         'slide de título com o texto \'Teste\' e um subtítulo com a data de hoje." Confira se o slide foi criado e '
         'localize o acesso às Skills em PowerPoint &gt; barra lateral do ChatGPT &gt; símbolo de adição.</p>'),
        ('items[14].items[0].paragraph',
         '<p>Uma falha de instalação, uma falha de autenticação e uma falha de habilitação da conta têm '
         'destinatários diferentes. Abra cada situação para saber o que fazer e a quem encaminhar:</p>'),
        ('items[15].items[1].description',
         '<p>A mensagem "Não foi possível iniciar este suplemento. Feche esta caixa de diálogo para ignorar o '
         'problema ou clique em Reiniciar para tentar novamente." indica um erro conhecido de login unificado: um '
         'endereço de retorno antigo redireciona para o endereço atual da OpenAI, e o suplemento do Office no '
         'Windows pode não concluir o redirecionamento.</p><p></p><p>A correção depende do administrador global do '
         'ambiente Microsoft da instituição, que deve obter o endereço ACS atual em Portal de administração da '
         'OpenAI &gt; Identidade &gt; SSO &gt; Gerenciar SSO, atualizar o aplicativo empresarial da OpenAI no '
         'provedor de identidade e definir esse endereço como padrão. Ao abrir o chamado, transcreva exatamente '
         'essa orientação.</p>'),
        ('items[15].items[2].description',
         '<p>Retorne ao teste de permissão e siga o desfecho correspondente. Se a adição estiver bloqueada ou pedir '
         'autorização, o pedido vai a quem administra o Microsoft 365, para implantação pelo arquivo XML de '
         'manifesto.</p><p></p><p>Prossiga somente depois que a implantação estiver concluída.</p>'),
        ('items[15].items[3].description',
         '<p>Primeiro, verifique se o acesso está sendo feito com a conta ChatGPT que possui o plano, e não com outra '
         'conta conectada no navegador. Se a conta estiver correta, o recurso pode não estar habilitado no espaço de '
         'trabalho do ChatGPT ou ainda não ter sido liberado para ela.</p><p></p><p>Encaminhe o pedido de '
         'habilitação a quem administra o espaço de trabalho do ChatGPT e, como a liberação é gradual, repita o '
         'teste mais tarde.</p>'),
        # Knowledge check: o gabarito original (alternativa 0) contradizia a propria licao para "loja
        # bloqueada". O enunciado foi reescrito para o 4o desfecho do roteiro, no qual a alternativa 0 e'
        # de fato a correta. Gabarito NAO alterado. Ver relatorio.
        ('items[16].items[0].title',
         'O suplemento foi instalado no PowerPoint, mas a sua conta institucional do ChatGPT não obtém acesso ao '
         'recurso. A quem você deve encaminhar o pedido?'),
        ('items[16].items[0].answers[0].feedback',
         'Correto. Com o suplemento já instalado, falta a habilitação do ChatGPT para PowerPoint no espaço de '
         'trabalho, e essa configuração cabe a quem administra a conta institucional do ChatGPT.'),
        ('items[16].items[0].answers[1].feedback',
         'Incorreto. Em conta institucional, a habilitação do recurso é decidida por quem administra o espaço de '
         'trabalho do ChatGPT, não pelo suporte.'),
        ('items[16].items[0].answers[2].feedback',
         'Incorreto. O administrador do Microsoft 365 controla a instalação, e a instalação já ocorreu. Ele seria o '
         'destinatário certo se a loja de suplementos estivesse bloqueada ou exigisse autorização.'),
        ('items[16].items[0].answers[3].feedback',
         'Incorreto. O PowerPoint funciona e o suplemento está instalado; o que falta é a habilitação do recurso para '
         'a sua conta, que não depende do suporte do PowerPoint.'),
        ('items[18].items[0].paragraph',
         '<p>Na próxima lição, a ferramenta passa a trabalhar sobre material de verdade: você vai produzir um '
         'rascunho a partir de material de origem declarando quatro elementos, preservar o tema institucional, '
         'intervir numa apresentação existente sem alterar o que não foi pedido e revisar o resultado em seis '
         'pontos. Tenha à mão um material de origem que você decidiu poder submeter e a cópia de trabalho criada '
         'nesta lição.</p>'),
    ],

    # ------------------------------------------------------------------ LICAO 2
    L2: [
        ('items[0].items[0].heading', 'Do material que já existe à apresentação revisada'),
        ('items[0].items[0].paragraph',
         '<p>O uso mais produtivo da ferramenta é produzir um primeiro rascunho a partir de material que já existe: '
         'um artigo, um capítulo, um plano de ensino, um conjunto de anotações, uma planilha de resultados. Quando a '
         'apresentação já está pronta, o cuidado muda: há trabalho anterior a preservar, e cada pedido precisa dizer '
         'o que pode e o que não pode mudar.</p><p>Esta lição percorre as duas situações, criar e intervir, e '
         'termina na revisão que todo resultado exige antes de ir para a sala de aula ou para a banca.</p>'),
        ('items[1].items[0].paragraph', FORMULA_OBJETIVOS),
        ('items[2].items[0].paragraph',
         '<p>Declarar os quatro elementos de uma instrução de criação: material de origem, estrutura, extensão e '
         'público.</p>'),
        ('items[2].items[1].paragraph', '<p>Aplicar o procedimento que preserva o tema institucional.</p>'),
        ('items[2].items[2].paragraph',
         '<p>Conferir os dados da apresentação gerada contra o material de origem.</p>'),
        ('items[2].items[3].paragraph',
         '<p>Delimitar uma edição em três elementos: o que alterar, o que preservar e onde.</p>'),
        ('items[2].items[4].paragraph',
         '<p>Solicitar um plano prévio antes de autorizar uma alteração extensa.</p>'),
        ('items[2].items[5].paragraph',
         '<p>Consultar a apresentação quanto à narrativa, às lacunas e às perguntas prováveis do público.</p>'),
        ('items[2].items[6].paragraph',
         '<p>Refinar uma apresentação (condensar, trocar de público, converter formato) e revisar o resultado nos '
         'seis pontos indicados pelo fabricante.</p>'),
        ('items[4].items[0].paragraph',
         '<p>Quatro elementos elevam a qualidade do rascunho: material de origem, estrutura, extensão e público. A '
         'ausência de qualquer um deles produz uma apresentação genérica.</p><p>Vale lembrar o ponto de partida do '
         'curso: o material de origem fornecido à ferramenta passa pelas duas empresas. O documento submetido deve '
         'ser um dos que você decidiu, na lição anterior, poder submeter. Convém ainda declarar o que deve '
         'permanecer inalterado (o estilo da apresentação, a ordem dos slides, a estrutura das tabelas): a instrução '
         'que diz o que preservar produz menos retrabalho do que a que apenas descreve o que se quer.</p>'),
        ('items[5].items[0].heading', 'O que declarar em cada elemento'),
        ('items[5].items[0].paragraph',
         '<p>Vire cada cartão para ver o que declarar e um exemplo de como escrever na instrução.</p>'),
        ('items[6].items[0].back.description',
         '<p>O documento que fundamenta a apresentação: um artigo, um capítulo, anotações, uma planilha de '
         'resultados.</p><p><em>Exemplo:</em> "Crie uma apresentação a partir do artigo anexado."</p>'),
        ('items[6].items[1].back.description',
         '<p>As seções e os tipos de slide esperados.</p><p><em>Exemplo:</em> "Um slide de abertura, três seções de '
         'conteúdo com três slides cada, um de discussão e um de fechamento."</p>'),
        ('items[6].items[2].back.description',
         '<p>O número exato de slides, e não "uma apresentação curta".</p><p><em>Exemplo:</em> "Doze slides."</p>'),
        ('items[6].items[3].back.description',
         '<p>Para quem se apresenta e qual a familiaridade dessa pessoa com o tema.</p><p><em>Exemplo:</em> '
         '"Público: alunos de graduação, primeiro contato com o tema."</p>'),
        ('items[7].items[0].title', 'Procedimento do tema institucional'),
        ('items[7].items[0].description',
         '<p>O fabricante declara que o produto trabalha com modelos existentes sempre que possível, mas que os '
         'slides gerados nem sempre correspondem ao estilo preferido. Para quem tem identidade visual obrigatória, '
         'essa é a limitação de maior impacto prático, e este procedimento a contorna.</p>'),
        ('items[7].items[1].title', 'Ponto de controle'),
        ('items[7].items[1].description',
         '<p>A apresentação tem o número de slides solicitado e a estrutura pedida; confira em PowerPoint &gt; '
         'Exibir &gt; Modo de Exibição de Estrutura de Tópicos, que mostra a hierarquia de títulos sem a '
         'formatação. Confira também ao menos três dados numéricos contra o material de origem.</p>'),
        ('items[7].items[2].description',
         '<p>Não parta de apresentação em branco. Abra um arquivo que já tenha o tema institucional aplicado: o '
         'modelo da instituição ou uma apresentação anterior salva como cópia e esvaziada de conteúdo.</p>'),
        ('items[7].items[3].description',
         '<p>Declare a preservação na própria instrução, junto com os quatro elementos: "Mantenha o modelo e o '
         'estilo desta apresentação, e preserve todos os números exatamente como aparecem no material de origem. '
         'Não acrescente informação que não esteja no material anexado."</p>'),
        ('items[8].items[0].heading', 'Solução de problemas na criação'),
        ('items[8].items[0].paragraph',
         '<p>Quatro situações aparecem com frequência no primeiro rascunho. Abra cada uma para ver o '
         'procedimento:</p>'),
        ('items[9].items[0].title', 'Vieram mais ou menos slides do que o pedido'),
        ('items[9].items[0].description',
         '<p>Solicite novamente com o número exato e declare o que deve ser cortado ou desdobrado.</p><p></p>'
         '<p>Exemplo: "Refaça com exatamente doze slides: funda os dois slides de contexto em um e desdobre o de '
         'resultados em dois."</p>'),
        ('items[9].items[1].description',
         '<p>É uma limitação declarada pelo fabricante. Aplique o procedimento do tema institucional: reaplique o '
         'layout em PowerPoint &gt; Página Inicial &gt; Layout ou o tema em PowerPoint &gt; Design &gt; Temas.</p>'
         '<p></p><p>Partir de um arquivo que já tenha o tema evita boa parte do problema.</p>'),
        ('items[9].items[2].description',
         '<p>Ocorre e é previsível. Remova a afirmação à mão; não solicite que o sistema corrija o que ele próprio '
         'inventou.</p><p></p><p>Pedir a correção abre espaço para uma nova invenção, e a conferência contra o '
         'material de origem continua sendo sua.</p>'),
        ('items[9].items[3].description',
         '<p>Apresentações maiores e solicitações fundamentadas em fontes consomem mais da cota. Divida o pedido em '
         'dois: primeiro a estrutura, depois o conteúdo de cada seção.</p><p></p><p>Assim você confere a estrutura '
         'antes de gastar créditos com o conteúdo.</p>'),
        ('items[10].items[0].paragraph',
         'O resultado é rascunho, não produto: a revisão das afirmações, dos números e das citações é '
         'responsabilidade de quem apresenta.'),
        ('items[11].items[0].heading', 'Intervir em apresentação existente'),
        ('items[11].items[0].paragraph',
         '<p>A edição de uma apresentação pronta exige mais cuidado do que a criação, porque há trabalho anterior a '
         'preservar. A recomendação do fabricante é ser específico sobre três coisas: o que se quer alterar, o que se '
         'quer preservar e onde a edição deve acontecer. Uma formulação de referência: "Adicione um slide de riscos '
         'após a visão geral do mercado. Mantenha o estilo desta apresentação e não altere os slides ao redor."</p>'
         '<p>Para edições maiores, peça um plano antes da execução: "Antes de editar, descreva quais slides você '
         'mudaria e por quê." Isso permite aprovar ou recusar o escopo antes que a apresentação seja modificada, ao '
         'custo de uma única troca de mensagens.</p>'),
        ('items[12].items[0].heading', 'As seis informações de um pedido completo'),
        ('items[12].items[0].paragraph',
         'Os quatro elementos da criação e os três da edição não são listas independentes. A documentação oficial '
         'reúne em seis informações o que um bom pedido declara: o que deve ser alterado; o que precisa permanecer '
         'intacto; em que ponto da apresentação; o público-alvo; os arquivos, notas ou dados de base; e o estilo '
         'visual ou a estrutura a preservar.<br><br>A instrução de criação recorta dessa lista o público, o material '
         'de origem e a estrutura, e declara à parte o que preservar ("mantenha o modelo").<br><br>A instrução de '
         'edição recorta o que alterar, o que preservar, onde e o estilo ("mantenha o estilo desta apresentação"). O '
         'público entra quando a edição muda o público; os dados de base, quando a edição acrescenta conteúdo.'
         '<br><br>As fórmulas curtas servem para o caso comum. Para o pedido de maior risco, uma instrução que '
         'declare as seis informações não é excessiva: é o pedido completo.'),
        ('items[13].items[0].title', 'Edição delimitada'),
        ('items[13].items[0].description',
         '<p>Este procedimento acrescenta ou altera um slide sem mexer no restante. Ele é feito na cópia de trabalho, '
         'nunca no original.</p>'),
        ('items[13].items[1].title', 'Ponto de controle'),
        ('items[13].items[1].description',
         '<p>Em PowerPoint &gt; Exibir &gt; Classificação de Slides, o slide novo está na posição pedida e os slides '
         'vizinhos estão idênticos ao que eram. O arquivo original permanece fechado e intacto.</p>'),
        ('items[13].items[2].description',
         '<p>Abra a cópia de trabalho criada na lição anterior e confirme pelo nome do arquivo na barra de título que '
         'não está no original.</p>'),
        ('items[13].items[4].description',
         '<p>Leia o plano sugerido e ajuste-o antes de autorizar qualquer alteração. Exemplo: "Aprovado com uma '
         'alteração: [ajuste ao plano]. Execute agora."</p>'),
        ('items[13].items[5].description',
         '<p>Envie a instrução declarando os três elementos: o que alterar, o que preservar e onde. Exemplo: '
         '"[O que alterar] em [onde exatamente]. Mantenha o estilo desta apresentação e não altere nenhum outro '
         'slide."</p>'),
        ('items[13].items[8].description',
         '<p>Aplique ao slide alterado os seis pontos de revisão descritos a seguir.</p>'),
        # Knowledge check de resposta multipla: o original empilhava tres perguntas em uma so',
        # com cabecalhos "Pergunta 1/2/3" como alternativas. Reescrito como uma pergunta coerente cujas
        # duas afirmacoes corretas sao exatamente as alternativas ja marcadas (indices 4 e 8). Gabarito,
        # ids, ordem e quantidade de alternativas preservados. Ver relatorio (campo `corrects`).
        ('items[14].items[0].title',
         'Sobre edição delimitada e revisão de apresentações, selecione as duas afirmações corretas.'),
        ('items[14].items[0].answers[0].title',
         'Em edições extensas, o plano prévio é dispensável: basta enviar a alteração e conferir o resultado depois.'),
        ('items[14].items[0].answers[1].title',
         'Os três elementos de uma edição delimitada são material de origem, estrutura e extensão.'),
        ('items[14].items[0].answers[2].title',
         'Os três elementos de uma edição delimitada são público, extensão e estrutura.'),
        ('items[14].items[0].answers[3].title',
         'Os três elementos de uma edição delimitada são layout, tema e conteúdo.'),
        ('items[14].items[0].answers[4].title',
         'Se slides não solicitados forem alterados, desfaça com Ctrl + Z ou retome a partir do arquivo original, e '
         'refaça o pedido declarando "não altere nenhum outro slide".'),
        ('items[14].items[0].answers[5].title',
         'Se slides não solicitados forem alterados, basta seguir adiante, desde que o slide pedido esteja correto.'),
        ('items[14].items[0].answers[6].title',
         'Se slides não solicitados forem alterados, o melhor é pedir ao sistema que corrija as alterações que ele '
         'mesmo fez.'),
        ('items[14].items[0].answers[7].title',
         'Se slides não solicitados forem alterados, é preciso apagar todos os slides e recomeçar do zero.'),
        ('items[14].items[0].answers[8].title',
         'Conferir as permissões de instalação do suplemento não faz parte da revisão em seis pontos.'),
        ('items[14].items[0].answers[9].title',
         'Conferir as afirmações factuais não faz parte da revisão em seis pontos.'),
        ('items[14].items[0].answers[10].title',
         'Conferir números e indicadores não faz parte da revisão em seis pontos.'),
        ('items[14].items[0].answers[11].title',
         'Conferir se algum slide foi removido ou deslocado não faz parte da revisão em seis pontos.'),
        ('items[15].items[0].heading', 'Refinar e revisar: os seis pontos'),
        ('items[15].items[0].paragraph',
         '<p>O refinamento (condensar, trocar de público, converter formato) é a operação de maior risco do curso, e '
         'o risco não está onde se costuma procurar. Ao reescrever para outro público ou para menos slides, o sistema '
         'pode preservar todos os números e, ainda assim, alterar o sentido de uma afirmação: um "sugere" que vira '
         '"demonstra", uma ressalva metodológica que desaparece na condensação.</p><p>Por isso, todo resultado '
         'reescrito passa pelos seis pontos que a documentação oficial manda conferir. Abra cada um para ver o que '
         'procurar:</p>'),
        ('items[16].items[0].description',
         '<p>Toda afirmação está no material de origem?</p><p></p><p>Percorra a apresentação com a fonte aberta ao '
         'lado. O que não estiver lá sai do slide.</p>'),
        ('items[16].items[1].description',
         '<p>Cada número confere com a origem e é o mesmo nas duas versões, quando houver uma original e uma '
         'reescrita?</p><p></p><p>Na instrução de refinamento, peça explicitamente: "mantenha todos os números '
         'exatamente como estão".</p>'),
        ('items[16].items[2].description',
         '<p>A citação existe, está correta e atribuída a quem a disse?</p><p></p><p>Citação que você não reconhece '
         'precisa ser localizada na fonte antes de permanecer no slide.</p>'),
        ('items[16].items[3].description',
         '<p>A afirmação reescrita diz o mesmo que a original, com a mesma força e as mesmas ressalvas?</p><p></p>'
         '<p>Se não disser, restaure a formulação a partir do material de origem e reforce na instrução: "não altere '
         'o sentido nem as ressalvas das afirmações".</p>'),
        ('items[16].items[4].description',
         '<p>Saiu algum slide que deveria ficar? A ordem do argumento mudou?</p><p></p><p>Se faltar um slide '
         'essencial, diga qual precisa voltar e o que pode ser cortado no lugar.</p>'),
        ('items[16].items[5].description',
         '<p>O tema institucional continua aplicado a todos os slides? Confira em PowerPoint &gt; Exibir &gt; '
         'Classificação de Slides.</p><p></p><p>Onde o tema se perdeu, reaplique em PowerPoint &gt; Design &gt; '
         'Temas; onde só o layout divergiu, em PowerPoint &gt; Página Inicial &gt; Layout.</p>'),
        ('items[19].items[0].paragraph',
         '<p>Na próxima lição, o foco passa da tarefa isolada para o trabalho que retorna a cada semestre: você vai '
         'decidir, pelo critério de previsibilidade de calendário, quando compensa transformar uma apresentação '
         'recorrente em fluxo reutilizável com Skills, apps ou modelos. Em seguida, vai encadear criar, editar, '
         'entender e refinar numa atividade integradora sobre material próprio.</p>'),
    ],

    # ------------------------------------------------------------------ LICAO 3
    L3: [
        ('items[0].items[0].heading', 'O trabalho que retorna a cada semestre'),
        ('items[0].items[0].paragraph',
         '<p>O docente refaz, a cada semestre, apresentações da mesma família: a aula inaugural da disciplina, a '
         'apresentação de resultados ao departamento, o seminário de acompanhamento de projeto, a defesa de '
         'orientandos. A estrutura é a mesma; muda o conteúdo.</p><p>Esta lição examina o que a ferramenta oferece '
         'para esse trabalho que se repete e, em seguida, articula tudo o que foi visto no curso em um único ciclo '
         'de produção, aplicado a uma apresentação sua.</p>'),
        ('items[1].items[0].paragraph', FORMULA_OBJETIVOS),
        ('items[2].items[0].paragraph',
         '<p>Distinguir Skills de apps quanto ao que cada um codifica, e situar plugins e modelos de '
         'apresentação.</p>'),
        ('items[2].items[1].paragraph',
         '<p>Aplicar o critério de previsibilidade de calendário para decidir se compensa configurar um fluxo.</p>'),
        ('items[2].items[2].paragraph',
         '<p>Reconhecer que a disponibilidade de Skills e apps depende de plano, espaço de trabalho e '
         'permissões.</p>'),
        ('items[2].items[3].paragraph',
         '<p>Encadear as quatro operações (criar, editar, entender e refinar) em um ciclo único, com a verificação em '
         'seis pontos como disposição permanente.</p>'),
        ('items[2].items[4].paragraph',
         '<p>Relacionar as quatro condições de bom uso indicadas pelo fabricante ao que foi praticado no curso.</p>'),
        ('items[4].items[0].paragraph',
         '<p>Skills são playbooks reutilizáveis para o trabalho com apresentações: codificam fluxos de trabalho, '
         'regras de estilo, expectativas de formatação e estruturas de saída, de modo que a mesma instrução não '
         'precise ser recriada a cada vez. Apps conectam o sistema a fontes de dados e ações aprovadas da sua conta, '
         'produzindo resultados mais contextuais.</p><p>Dois termos completam o quadro. Plugin, na terminologia do '
         'fabricante, é um pacote que pode reunir Skills, apps e outros recursos, distribuído pela instituição onde '
         'houver suporte. E os modelos de apresentação, listados ao lado das Skills e dos apps como meio de repetir '
         'um fluxo, são para o docente o mecanismo mais acessível: um arquivo com o tema institucional e a estrutura '
         'padrão da aula, que não depende de plano nem de administrador.</p>'),
        ('items[5].items[0].heading', 'Quatro termos para não confundir'),
        ('items[5].items[0].paragraph', '<p>Vire cada cartão para revisar o que cada recurso é e quando ele serve.</p>'),
        ('items[6].items[0].back.description',
         '<span>Playbook reutilizável que codifica fluxos de trabalho, regras de estilo, formatação e estrutura de '
         'saída. Acessada pelo símbolo de adição da barra lateral ou pelo símbolo @ na própria instrução.</span>'),
        ('items[6].items[1].back.description',
         '<span>Conexão a fontes de dados e ações aprovadas da sua conta, para resultados fundamentados nas fontes da '
         'instituição. Nem todo app do ChatGPT aparece dentro do PowerPoint.</span>'),
        ('items[6].items[2].back.description',
         '<span>Pacote que pode reunir Skills, apps e outros recursos de fluxo de trabalho, distribuído pela '
         'instituição onde houver suporte.</span>'),
        ('items[6].items[3].back.description',
         '<span>Arquivo com o tema institucional e a estrutura padrão da aula. O mecanismo mais acessível dos três: '
         'não depende de plano nem de administrador.</span>'),
        ('items[7].items[0].paragraph',
         '<p>Configurar um fluxo custa tempo, e esse custo só se paga quando o trabalho volta. Abra cada item para ver '
         'o critério de decisão e as limitações de cada recurso:</p>'),
        ('items[8].items[0].description',
         '<p>Se a apresentação se repete em calendário previsível, vale configurar; se é evento isolado, não vale.'
         '</p><p></p><p>Uma aula inaugural que se refaz todo semestre amortiza a configuração; uma palestra única '
         'não. O mesmo vale para o relatório trimestral à agência de fomento (vale) e para a aula substituta '
         'preparada às pressas (não vale).</p>'),
        ('items[8].items[1].description',
         '<p>Uma Skill evita recriar a mesma instrução a cada vez: o fluxo, as regras de estilo e a estrutura de '
         'saída ficam codificados. A disponibilidade, porém, depende do plano, das configurações do espaço de '
         'trabalho, da função atribuída e das permissões.</p><p></p><p>Confirme que a sua conta tem acesso a Skills '
         'antes de planejar a automação em torno delas.</p>'),
        ('items[8].items[2].description',
         '<p>Apps trazem para a apresentação dados e ações aprovadas da sua conta. Só aparecem quando estão '
         'disponíveis na interface do PowerPoint e permitidos pelo espaço de trabalho e pelas permissões das fontes '
         'de dados; nem todo app do ChatGPT está disponível dentro do PowerPoint.</p><p></p><p>Para ver os '
         'disponíveis, use PowerPoint &gt; barra lateral do ChatGPT &gt; símbolo de adição &gt; apps.</p>'),
        ('items[8].items[3].description',
         '<p>O modelo de apresentação, com tema institucional e estrutura padrão, não exige plano específico nem '
         'autorização de administrador. Quem não dispõe de Skills pode complementá-lo com um modelo de instrução '
         'repetível: um arquivo de texto com a parte fixa (disciplina, público, duração da aula, estrutura padrão e '
         'estilo) e um campo para o conteúdo que muda a cada semestre.</p><p></p><p>A cada uso, substitua apenas os '
         'campos variáveis e anexe o material de origem daquela vez.</p>'),
        ('items[8].items[4].description',
         '<p>O acesso a Skills e apps é condicionado ao plano, ao espaço de trabalho, à função atribuída e às '
         'permissões exigidas. Em espaços de trabalho corporativos e educacionais, quem administra controla tanto a '
         'instalação quanto o acesso a cada app.</p><p></p><p>Se um recurso não aparecer, o encaminhamento é o '
         'administrador do espaço de trabalho, não o suporte.</p>'),
        ('items[9].items[0].title', 'Fluxo de uso de uma Skill'),
        ('items[9].items[0].description',
         '<p>Onde o recurso estiver disponível, uma Skill é usada em quatro passos, sempre com o material de origem '
         'daquela vez.</p>'),
        ('items[9].items[1].title', 'Sem Skills na conta?'),
        ('items[9].items[1].description',
         '<p>Use o modelo de apresentação com o tema institucional e o modelo de instrução repetível salvo em '
         'arquivo de texto. O ganho é o mesmo: não recriar a cada semestre o que não muda.</p>'),
        ('items[9].items[2].description',
         '<p>Em PowerPoint &gt; faixa de opções &gt; ChatGPT, abra a barra lateral do suplemento.</p>'),
        ('items[9].items[3].description',
         '<p>Em PowerPoint &gt; barra lateral do ChatGPT &gt; símbolo de adição, navegue pelas Skills e pelos apps '
         'disponíveis na sua conta.</p>'),
        ('items[9].items[4].title', 'Selecionar ou invocar a Skill'),
        ('items[9].items[4].description',
         '<p>Selecione uma Skill na lista ou invoque-a diretamente na instrução com o símbolo @ seguido do nome.</p>'),
        ('items[9].items[5].title', 'Descrever a tarefa desta vez'),
        ('items[9].items[5].description',
         '<p>Descreva a tarefa específica e forneça o material de origem daquela vez. A Skill cuida do que se repete; '
         'a revisão do resultado continua sendo sua.</p>'),
        ('items[10].items[0].title',
         'A apresentação de abertura da mesma disciplina é refeita a cada semestre, com dados novos. Vale a pena '
         'configurar um fluxo reutilizável (Skill, app ou modelo) para ela?'),
        ('items[10].items[0].answers[0].feedback',
         'Correto. A apresentação retorna em calendário previsível e no mesmo formato, então a configuração se '
         'amortiza a cada semestre.'),
        ('items[10].items[0].answers[1].feedback',
         'Incorreto. Não valeria configurar para um evento isolado, como uma palestra única. Esta apresentação '
         'retorna todo semestre.'),
        ('items[10].items[0].answers[2].feedback',
         'Incorreto. O critério não é a obrigatoriedade, e sim a previsibilidade do calendário: a tarefa se repete em '
         'intervalo conhecido.'),
        ('items[10].items[0].answers[3].feedback',
         'Incorreto. O critério não é o tempo disponível agora, e sim a repetição previsível, que faz a configuração '
         'compensar ao longo dos semestres.'),
        ('items[11].items[0].heading', 'Um ciclo, não procedimentos isolados'),
        ('items[11].items[0].paragraph',
         '<p>As quatro operações anunciadas pelo fabricante são etapas de um ciclo: cria-se o rascunho a partir do '
         'material de origem; edita-se, de forma delimitada, o que não corresponde ao pretendido; consulta-se a '
         'apresentação quanto à narrativa e às lacunas; e refina-se para o público específico.</p><p>A verificação '
         'não é uma quinta operação acrescentada ao fim: é uma disposição que acompanha todas as demais, porque cada '
         'afirmação, número e citação da apresentação é responsabilidade de quem a apresenta. E, como o arquivo passa '
         'por duas empresas, a decisão sobre o que colocar dentro dele precede tudo o mais.</p>'),
        ('items[12].items[0].title', 'O ciclo de produção'),
        ('items[12].items[0].description',
         '<p>Cada etapa entrega algo concreto à seguinte. A revisão em seis pontos acompanha todas elas.</p>'),
        ('items[12].items[1].description',
         '<p>Criar, editar, entender e refinar, com a verificação em seis pontos (afirmações, números, citações, '
         'sentido, slides removidos ou deslocados e modelo visual) acompanhando cada etapa.</p>'),
        ('items[12].items[4].description',
         '<p>Pergunte, sem alterar nenhum slide: qual é a narrativa desta apresentação, onde estão as lacunas do '
         'raciocínio e que perguntas o público provavelmente fará.</p>'),
        ('items[12].items[5].description',
         '<p>Ajuste ao público específico (condensar, trocar de público ou dar acabamento) e aplique a revisão em seis '
         'pontos, com atenção especial ao sentido das afirmações reescritas.</p>'),
        ('items[13].items[0].heading', 'As quatro condições de bom uso'),
        ('items[13].items[0].paragraph',
         '<p>A documentação oficial resume o bom uso da ferramenta em quatro condições, que este curso desdobrou '
         'lição a lição. Abra cada uma para ver onde ela foi praticada:</p>'),
        ('items[14].items[0].description',
         '<p>Declarar com precisão o que se espera em cada solicitação. Instruções vagas produzem apresentações '
         'genéricas.</p><p></p><p>Praticada na lição anterior: os quatro elementos da criação e os três da edição, '
         'recortes das seis informações recomendadas pelo fabricante.</p>'),
        ('items[14].items[1].description',
         '<p>Fornecer material de origem que você conhece e pode submeter. O sistema não valida dados por conta '
         'própria, e uma fonte frágil gera slides frágeis.</p><p></p><p>Praticada na lição anterior, na criação a '
         'partir de material de origem, sempre dentro do que se decidiu, na primeira lição, poder submeter.</p>'),
        ('items[14].items[2].description',
         '<p>Declarar o que não deve mudar: o tema institucional, os slides ao redor, os números e o sentido das '
         'afirmações.</p><p></p><p>Praticada na lição anterior, no procedimento do tema institucional e na edição '
         'delimitada.</p>'),
        ('items[14].items[3].description',
         '<p>Conferir afirmações, números e citações antes de apresentar. O sistema não oferece garantia sobre nenhum '
         'deles.</p><p></p><p>Praticada na revisão em seis pontos da lição anterior e retomada nesta lição como '
         'disposição permanente, não como etapa final.</p>'),
        ('items[16].items[0].title', 'Atividade integradora: uma apresentação completa'),
        ('items[16].items[0].description',
         '<p>Aplique o ciclo inteiro a uma apresentação sua. A execução assistida leva cerca de seis minutos; a '
         'apresentação pode ser concluída depois.</p>'),
        ('items[16].items[1].title', 'Critérios de avaliação'),
        ('items[16].items[1].description',
         '<p>Confira: o rascunho foi pedido com os quatro elementos; a apresentação partiu de arquivo com o tema '
         'institucional; a edição declarou o que preservar e onde, e os slides vizinhos ficaram inalterados; a '
         'consulta sobre lacunas e perguntas foi feita; todo número e citação foi conferido contra a origem; nenhuma '
         'afirmação reescrita mudou de sentido; nada das categorias vedadas foi submetido; e você decidiu se o uso '
         'precisa ser declarado.</p>'),
        ('items[16].items[2].description',
         '<p>Escolha um material de origem próprio, entre os que você decidiu poder submeter ao suplemento.</p>'),
        ('items[16].items[3].description',
         '<p>Parta de um arquivo com o tema institucional já aplicado, nunca de uma apresentação em branco.</p>'),
        ('items[16].items[5].description',
         '<p>Escolha um slide para editar, peça o plano prévio, ajuste-o e solicite a alteração declarando o que '
         'alterar, o que preservar e onde.</p>'),
        ('items[16].items[6].description',
         '<p>Sem alterar nenhum slide, pergunte qual é a narrativa da apresentação em três frases, onde estão as '
         'lacunas do raciocínio e que cinco perguntas o seu público provavelmente fará.</p>'),
        ('items[16].items[7].description',
         '<p>Revise afirmações, números, citações, sentido, slides removidos ou deslocados e aderência ao modelo '
         'visual. Reaplique o tema onde necessário, em PowerPoint &gt; Design &gt; Temas.</p>'),
        ('items[18].items[0].paragraph',
         '<p>Você concluiu o curso. A competência tratada aqui se consolida pelo uso, não pela leitura: pratique '
         'sobre material real, começando pelas apresentações de menor exposição antes de levar o procedimento a uma '
         'banca ou a um relatório de fomento.</p><p>Como aprofundamento, configure fluxos reutilizáveis com Skills '
         'quando a disponibilidade estiver confirmada na sua conta, conecte apps a fontes de dados institucionais '
         'aprovadas e compare o suplemento com as demais ferramentas de apresentação assistida contratadas pela '
         'instituição. Reconsulte periodicamente a documentação oficial: planos, créditos, modelos e recursos mudam '
         'com frequência, e as informações deste curso correspondem à consulta de 7 de outubro de 2026.</p>'
         '<p><strong>Síntese:</strong> o sistema monta os slides; a apresentação continua sendo de quem sobe ao '
         'palco.</p>'),
    ],
}
