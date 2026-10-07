"""Edicoes de texto do curso ChatGPT PowerPoint - Hands On.

Fonte: roteiros/roteiro-articulate-hands-on.md (Oficinas 0 a 4, Projeto Final, Parte dos Dez).
Mapeamento: L1 = Oficinas 0+1 | L2 = Oficina 2 | L3 = Oficinas 3+4 (Projeto Final ausente no SCORM).
Tom: o do roteiro (segunda pessoa, direto, "Para Leigos").
"""
CURSO_ORIGINAL = 'cursoChatGPTPPTHandsOn.json'
PASTA = 'licoes_extraidas_ChatGPTPPTHandsOn'

L1 = 'licao_01_Preparando_o_Ambiente_e_Instalando_o_ChatGPT_no_PowerPoint.json'
L2 = 'licao_02_Transformando_Textos_em_Apresentacoes_Estruturadas.json'
L3 = 'licao_03_Ajustando_Revisando_e_Comparando_Versoes_de_Apresentacoes.json'

FORMULA_OBJETIVOS = '<p>Ao final desta lição, você será capaz de:</p>'

EDICOES = {
    # ------------------------------------------------------------------ LICAO 1
    L1: [
        ('items[0].items[0].heading', 'Antes de arregaçar as mangas'),
        ('items[0].items[0].paragraph',
         '<p>Este curso é mão na massa. Você vai instalar o ChatGPT dentro do PowerPoint e passar as próximas duas '
         'horas transformando material que já está no seu computador em slides. No fim, vai ter uma aula inteira '
         'montada a partir de material que já existia, em duas versões, para dois públicos.</p><p>Esta lição reúne '
         'as duas primeiras oficinas. A Oficina 0 leva cinco minutos e descobre se você pode instalar, quem consegue '
         'ler o conteúdo dos seus slides e quanto isso consome do seu plano. A Oficina 1 instala o suplemento e dá o '
         'primeiro comando numa apresentação vazia. Faça a Oficina 0 primeiro: ela pode te poupar o curso inteiro se '
         'a instalação estiver bloqueada na sua instituição.</p>'),
        ('items[1].items[0].paragraph', '<p>O que você precisa ter aberto agora:</p>'),
        ('items[2].items[0].paragraph', '<p>O Microsoft PowerPoint.</p>'),
        ('items[2].items[1].paragraph',
         '<p>Um documento seu que possa virar apresentação: um artigo, um capítulo, um plano de ensino.</p>'),
        ('items[2].items[2].paragraph', '<p>Uma apresentação sua que já use o tema institucional.</p>'),
        ('items[2].items[3].paragraph', '<p>Uma conta do ChatGPT, conectada no navegador.</p>'),
        ('items[4].items[0].title', 'Oficina 0 — Cinco minutos antes de instalar'),
        ('items[4].items[0].description',
         '<p>Você está prestes a instalar um programa dentro do PowerPoint da sua universidade e a mandar para ele o '
         'conteúdo dos seus slides. Vale cinco minutos para descobrir três coisas: se você tem permissão de instalar, '
         'quem consegue ler esse conteúdo, e quanto isso consome do seu plano.</p>'),
        ('items[4].items[1].title', 'O que você resolveu'),
        ('items[4].items[1].description',
         '<p>Você sabe quem lê o que você envia, o que não entra na apresentação, quanto custa cada pedido e se a '
         'instalação é possível no seu computador. E tem na pasta os dois arquivos que protegem o seu material: a '
         'apresentação de teste e a cópia de trabalho.</p>'),
        ('items[4].items[2].title', 'Saiba quem lê'),
        ('items[4].items[2].description',
         '<p>O ChatGPT para PowerPoint roda dentro do PowerPoint da Microsoft. Pelos Termos de Serviço do Marketplace '
         'de Suplementos, a Microsoft pode ler o conteúdo dos seus arquivos. Somando o processamento da OpenAI, o '
         'arquivo passa por duas empresas. E não vai só o slide: a cada pedido, a OpenAI processa o que você digitou, '
         'o conteúdo da apresentação, os anexos que você mandou e o contexto de apps conectados, se houver. Uma conta '
         'pessoal gratuita e uma conta institucional não tratam esses dados da mesma forma.</p>'),
        ('items[4].items[3].description',
         '<p>Antes de qualquer pedido, decida o que fica de fora. A lista do que nunca entra está logo abaixo desta '
         'sequência e vale para todo arquivo que você abrir com o suplemento.</p>'),
        ('items[4].items[4].description',
         '<p>Veja o seu plano em ChatGPT &gt; Menu de perfil &gt; Configurações &gt; Conta e encontre a sua linha na '
         'tabela de planos, logo abaixo. Uma mensagem típica consome de 10 a 50 créditos; apresentação grande e '
         'edição em várias etapas consomem mais. A cota é a mesma do ChatGPT para Excel e de outros recursos de '
         'agente: se você usa os dois suplementos, tudo sai do mesmo saldo. Não planeje a aula de amanhã contando com '
         'uma cota que pode acabar hoje.</p>'),
        ('items[4].items[5].description',
         '<p>Vá em PowerPoint &gt; Página Inicial (Home) &gt; Suplementos (Add-ins) e pesquise por ChatGPT. Se o seu '
         'Office estiver em inglês, os nomes são os que estão entre parênteses. Três coisas podem acontecer agora, e '
         'uma quarta só aparece na Oficina 1. Os desfechos e o que fazer em cada um estão logo abaixo desta '
         'sequência.</p>'),
        ('items[4].items[6].description',
         '<p>Crie uma apresentação nova, vazia, e salve como teste-chatgpt.pptx. É nela que você vai dar o primeiro '
         'comando na Oficina 1, nunca num arquivo real.</p>'),
        ('items[4].items[7].description',
         '<p>Abra a apresentação sua que usa o tema institucional, vá em PowerPoint &gt; Arquivo &gt; Salvar como, '
         'acrescente -copia-curso ao nome, salve e feche a original. Daqui em diante você trabalha na cópia; o '
         'original fica intacto, como garantia.</p>'),
        ('items[4].items[8].title', 'Responda para si'),
        ('items[4].items[8].description',
         '<p>Antes de usar isso em material oficial: a sua universidade tem norma sobre uso de IA em material '
         'didático? Se você usar, precisa declarar, e uma banca, um congresso e um relatório de fomento podem exigir '
         'coisas diferentes? O que você vai dizer aos alunos, que têm a mesma ferramenta para os seminários deles?</p>'),
        ('items[5].items[0].paragraph',
         '<p>Nada disto entra numa apresentação que você submete ao suplemento:</p>'),
        ('items[7].items[0].heading', 'Quanto custa: a sua linha na tabela de planos'),
        ('items[7].items[0].paragraph',
         '<p>O acesso existe em todos os planos, mas não nas mesmas condições:</p><ul><li><strong>Free</strong> e '
         '<strong>Go</strong>: uso limitado.</li><li><strong>Plus</strong>, <strong>Pro</strong> e '
         '<strong>Business</strong>: sujeito ao limite de uso com agentes de IA do plano.</li><li><strong>Business'
         '</strong>, <strong>Enterprise</strong> e <strong>Edu</strong>: debitado do saldo de créditos compartilhado '
         'do espaço de trabalho.</li></ul><p>Valores conferidos na documentação oficial em 7 de outubro de 2026. Isso '
         'muda com frequência: confira na sua conta.</p>'),
        ('items[8].items[0].heading', 'O que aconteceu no passo 4'),
        ('items[8].items[0].paragraph',
         '<p><strong>A loja abriu e dá para adicionar:</strong> você pode instalar. Siga para a Oficina 1.</p>'
         '<p><strong>Abriu, mas a adição está bloqueada ou pede autorização:</strong> você precisa do administrador do '
         'Microsoft 365. Peça a ele a implantação do suplemento pelo arquivo XML de manifesto e volte quando estiver '
         'feita.</p><p><strong>A loja não abre ou o recurso não existe:</strong> a instituição bloqueou. Este curso '
         'não vai funcionar no seu computador; veja o aviso abaixo.</p><p><strong>(Na Oficina 1) Instalou, mas a sua '
         'conta não tem acesso:</strong> o recurso não está liberado para a sua conta. Confira o plano; se a conta for '
         'institucional, peça a habilitação a quem administra o espaço de trabalho do ChatGPT; se nada resolver, pode '
         'ser liberação gradual, e vale tentar de novo depois.</p>'),
        ('items[13].items[0].heading', 'Se travar na Oficina 0'),
        ('items[13].items[0].paragraph', '<p>Abra o problema que apareceu para ver o que fazer:</p>'),
        ('items[16].items[0].heading', 'Oficina 1 — Botar o ChatGPT dentro do PowerPoint'),
        ('items[16].items[0].paragraph',
         'Você ouviu falar que dá para usar o ChatGPT dentro do PowerPoint, mas não faz ideia de onde isso fica. '
         'Nesta oficina você instala, conecta a conta e dá o primeiro comando, numa apresentação vazia, onde não há '
         'nada a perder. Vai precisar do PowerPoint aberto, da apresentação teste-chatgpt.pptx criada na Oficina 0 e '
         'da sua conta do ChatGPT.'),
        ('items[17].items[0].title', 'Instalar, conectar e dar o primeiro comando'),
        ('items[17].items[0].description',
         '<p>Oito passos, todos na apresentação de teste. Ao final, a barra lateral do ChatGPT vai estar aberta e '
         'você vai saber onde ficam as Skills.</p>'),
        ('items[17].items[1].title', 'O que você resolveu'),
        ('items[17].items[1].description',
         '<p>O suplemento está instalado e conectado à conta certa, o primeiro comando funcionou e você sabe onde '
         'ficam as Skills. Tudo isso sem arriscar nenhum arquivo real.</p>'),
        ('items[17].items[2].description',
         '<p>Abra o arquivo <strong>teste-chatgpt.pptx</strong>. Não abra material real ainda.</p>'),
        ('items[17].items[6].description',
         '<p>Entre com a sua conta do ChatGPT: aquela que tem o plano que você identificou na Oficina 0.</p>'),
        ('items[17].items[9].description',
         '<p>Vá em PowerPoint &gt; barra lateral do ChatGPT &gt; <strong>símbolo de adição</strong> e veja quais '
         'Skills estão disponíveis na sua conta. Você vai voltar a elas depois; por ora, só localize onde ficam.</p>'),
        ('items[20].items[0].heading', 'Se travar na Oficina 1'),
        ('items[20].items[0].paragraph',
         '<p>Cada problema abaixo tem um destinatário diferente. Abra o que apareceu para você:</p>'),
        ('items[22].items[0].answers[1].feedback',
         'Incorreto. O suplemento funciona normalmente com arquivos originais, e é justamente por isso que o risco '
         'existe: ele pode editar ou apagar conteúdo.'),
        ('items[22].items[0].answers[2].feedback',
         'Incorreto. A velocidade de abertura não tem relação com o uso de cópias. O motivo é proteger o original de '
         'edições e exclusões feitas pelo sistema.'),
        ('items[22].items[0].answers[3].feedback',
         'Incorreto. O PowerPoint não exige duplicar arquivos. Trabalhar em cópia é uma regra deste curso, baseada no '
         'aviso da própria OpenAI de que o sistema pode editar e apagar conteúdo.'),
        ('items[23].items[0].paragraph',
         '<p>Ambiente pronto, suplemento instalado e primeiro comando dado, tudo sem tocar em material real. Na '
         'Oficina 2 você pega um texto longo, como aquele artigo de trinta páginas, e transforma numa aula de doze '
         'slides com o tema da sua universidade. Deixe à mão a cópia de trabalho e um documento de origem que você '
         'decidiu, na Oficina 0, que pode submeter.</p>'),
    ],

    # ------------------------------------------------------------------ LICAO 2
    L2: [
        ('items[0].items[0].heading', 'Oficina 2 — De um texto longo para uma aula'),
        ('items[0].items[0].paragraph',
         '<p>Você tem um artigo de trinta páginas e precisa dar aula sobre ele na quinta-feira. Nesta oficina você '
         'transforma o texto em slides e resolve o problema que ninguém avisa: o resultado nem sempre respeita o '
         'modelo visual da sua universidade.</p><p>Vai precisar da cópia de trabalho criada na Oficina 0, que já tem '
         'o tema institucional, e de um documento de origem, daqueles que você decidiu, na Oficina 0, que pode '
         'submeter.</p>'),
        ('items[1].items[0].paragraph', FORMULA_OBJETIVOS),
        ('items[2].items[0].paragraph',
         '<p>Pedir um rascunho declarando os quatro elementos: origem, estrutura, extensão e público.</p>'),
        ('items[2].items[1].paragraph',
         '<p>Partir de um arquivo com o tema institucional e reaplicar tema e layout quando o resultado sair do '
         'modelo.</p>'),
        ('items[2].items[2].paragraph',
         '<p>Conferir cada número, data e citação contra o material de origem e corrigir à mão o que estiver '
         'errado.</p>'),
        ('items[2].items[3].paragraph',
         '<p>Resolver os problemas mais comuns do primeiro rascunho: número de slides errado, tema perdido, dado '
         'inventado e cota consumida.</p>'),
        ('items[3].items[0].title', 'Do artigo ao rascunho de doze slides'),
        ('items[3].items[0].description',
         '<p>Sete passos, da cópia de trabalho esvaziada até a conferência dos dados. Você vai pedir, conferir e '
         'corrigir, nessa ordem.</p>'),
        ('items[3].items[1].title', 'Ponto de controle'),
        ('items[3].items[1].description',
         '<p>Em PowerPoint &gt; Exibir &gt; Modo de Exibição de Estrutura de Tópicos você vê doze slides com a '
         'estrutura que pediu. Em PowerPoint &gt; Exibir &gt; Classificação de Slides, todos estão com o tema '
         'institucional.</p>'),
        ('items[3].items[2].title', 'Não comece de uma apresentação em branco'),
        ('items[3].items[2].description',
         '<p>Abra a cópia de trabalho, que já tem o tema institucional, apague os slides de conteúdo e salve como '
         'aula-nova.pptx. O arquivo fica vazio, mas com o tema aplicado.</p>'),
        ('items[3].items[3].description',
         '<p>Abra a barra lateral em PowerPoint &gt; faixa de opções &gt; ChatGPT.</p>'),
        ('items[3].items[4].description',
         '<p>Peça o rascunho declarando os quatro elementos: origem, estrutura, extensão e público. Anexe o documento '
         'e envie:</p><p>Crie uma apresentação a partir do material anexado. Doze slides: um de abertura, três seções '
         'de conteúdo com três slides cada, um de discussão e um de fechamento. Público: alunos de graduação, '
         'primeiro contato com o tema. Mantenha o modelo e o estilo desta apresentação.</p>'),
        ('items[3].items[5].description',
         '<p>Espere a geração e percorra os slides no painel de miniaturas. Veja se a estrutura que você pediu foi '
         'respeitada.</p>'),
        ('items[3].items[6].description',
         '<p>Se os slides não seguiram o modelo institucional, o que é uma limitação declarada pelo fabricante, '
         'reaplique o tema em PowerPoint &gt; Design &gt; Temas e ajuste os layouts divergentes em PowerPoint &gt; '
         'Página Inicial &gt; Layout.</p>'),
        ('items[3].items[7].description',
         '<p>Cada número, data e citação que aparecer nos slides precisa estar no material de origem. Percorra um por '
         'um, com o documento aberto ao lado.</p>'),
        ('items[3].items[8].description',
         '<p>Corrija à mão o que estiver errado. Não peça ao sistema para corrigir o que ele inventou: ele pode '
         'inventar de novo.</p>'),
        ('items[5].items[0].heading', 'Se travar'),
        ('items[5].items[0].paragraph', '<p>Abra o problema que apareceu para ver o que fazer:</p>'),
        ('items[6].items[1].description',
         '<p>Limitação conhecida e declarada pelo fabricante. Reaplique o tema como no passo 5: PowerPoint &gt; Design '
         '&gt; Temas, e ajuste os layouts em PowerPoint &gt; Página Inicial &gt; Layout.</p>'),
        ('items[6].items[2].description',
         '<p>Acontece e é previsível; é por isso que o passo de conferência dos dados existe. Remova ou corrija à '
         'mão, com base no artigo.</p>'),
        ('items[7].items[0].paragraph',
         '<p>Quer ir além? Os três desafios abaixo são opcionais e usam o mesmo material de origem:</p>'),
        ('items[8].items[0].paragraph',
         '<p><strong>Dois públicos, dois decks</strong><br>Peça a mesma apresentação para alunos e para colegas da '
         'área. Deu certo se: você aponta três slides que existem numa e não na outra.</p>'),
        ('items[8].items[1].paragraph',
         '<p><strong>Sem material de origem</strong><br>Peça a mesma aula só descrevendo o assunto, sem anexar nada, '
         'e compare. Deu certo se: você consegue dizer, concretamente, o que a fonte acrescentou.</p>'),
        ('items[8].items[2].paragraph',
         '<p><strong>A aula de cinco minutos</strong><br>Peça a versão de cinco slides do mesmo material. Deu certo '
         'se: os cinco slides ainda contam a história inteira.</p>'),
        ('items[9].items[0].heading', 'Antes de mexer no rascunho'),
        ('items[9].items[0].paragraph',
         '<p>Os doze slides são ponto de partida, não aula pronta. A partir da próxima oficina você vai editar esse '
         'material, e cada edição precisa proteger o que já foi conferido. Por isso, antes de seguir, garanta duas '
         'coisas: os números e as citações já passaram pela conferência contra o artigo, e a aula-nova.pptx está '
         'salva, separada da cópia de trabalho.</p>'),
        ('items[10].items[0].answers[0].feedback',
         'Incorreto. Pedir ao sistema que corrija o que ele inventou abre espaço para uma nova invenção. A correção é '
         'feita à mão, com base no material de origem.'),
        ('items[10].items[0].answers[1].feedback',
         'Incorreto. Inventar dados é um comportamento previsível do sistema. Todo número, data e citação precisa ser '
         'conferido contra a origem.'),
        ('items[10].items[0].answers[2].feedback',
         'Correto. Conferir slide por slide contra o artigo e corrigir à mão garante que a aula diga o que a fonte '
         'diz.'),
        ('items[10].items[0].answers[3].feedback',
         'Incorreto. Recomeçar desperdiça o que está certo e pode gerar novos erros. Basta corrigir à mão os dados '
         'divergentes.'),
        ('items[12].items[0].paragraph',
         '<p>Você tem uma aula de doze slides, com o tema da sua universidade e os dados conferidos contra o artigo. '
         'Na Oficina 3, a apresentação já existe e está boa: você vai acrescentar um slide no meio sem mexer no resto, '
         'pedindo o plano antes, delimitando a edição em três elementos e conferindo os slides vizinhos. Em seguida, '
         'na Oficina 4, vai fazer a segunda versão da mesma apresentação, para outro público.</p>'),
    ],

    # ------------------------------------------------------------------ LICAO 3
    L3: [
        ('items[0].items[0].heading', 'Oficinas 3 e 4 — Mexer sem estragar e trocar de público'),
        ('items[0].items[0].paragraph',
         '<p>A apresentação já existe e está boa. Você só precisa acrescentar um slide no meio, e não quer que o '
         'resto mude. Na Oficina 3 você aprende a delimitar a edição, que é o que separa uma correção de um '
         'estrago.</p><p>Depois, a mesma apresentação vai para outro público: uma banca de qualificação, uma reunião '
         'de colegiado, uma palestra para o público geral. Mesmo conteúdo, outro leitor, outro tempo, outro nível de '
         'detalhe. Na Oficina 4 você faz essa segunda versão, sem perder nenhum número nem o sentido de nenhuma '
         'afirmação.</p>'),
        ('items[1].items[0].paragraph', FORMULA_OBJETIVOS),
        ('items[2].items[0].paragraph',
         '<p>Pedir o plano antes e delimitar a edição em três elementos: o que alterar, o que preservar e onde.</p>'),
        ('items[2].items[1].paragraph',
         '<p>Ajustar a apresentação para outro público, dizendo quem ele é e o que muda por causa dele.</p>'),
        ('items[2].items[2].paragraph',
         '<p>Comparar as duas versões lado a lado com a revisão em seis pontos, incluindo números, citações e sentido '
         'das afirmações.</p>'),
        ('items[2].items[3].paragraph',
         '<p>Consultar a narrativa e as lacunas da apresentação e antecipar as perguntas do novo público.</p>'),
        ('items[3].items[0].title', 'Oficina 3 — Mexer sem estragar'),
        ('items[3].items[0].description',
         '<p>Você vai usar a cópia de trabalho com conteúdo, criada na Oficina 0, e a barra lateral do ChatGPT. Seis '
         'passos, e o mais importante é o segundo: pedir o plano antes de autorizar qualquer coisa.</p>'),
        ('items[3].items[1].title', 'Ponto de controle'),
        ('items[3].items[1].description',
         '<p>Em PowerPoint &gt; Exibir &gt; Classificação de Slides, o slide novo está na posição que você pediu, e os '
         'slides vizinhos estão idênticos. Se quiser certeza, abra o arquivo original em paralelo e compare: ele '
         'continua intacto porque você nunca o abriu para edição.</p>'),
        ('items[3].items[2].description',
         '<p>Confirme que você está na cópia, e não no original. Olhe o nome do arquivo na barra de título.</p>'),
        ('items[3].items[4].description',
         '<p>Leia o plano. Se não for o que você quer, corrija agora, antes que a apresentação seja modificada. Custa '
         'uma mensagem e evita refazer tudo.</p>'),
        ('items[3].items[5].description',
         '<p>Peça a edição declarando os três elementos: o que alterar, o que preservar, e onde. Por exemplo: """ '
         'Adicione um slide de limitações metodológicas logo após o slide de resultados. Mantenha o estilo desta '
         'apresentação e não altere nenhum outro slide. """</p>'),
        ('items[3].items[6].title', 'Confira os vizinhos'),
        ('items[3].items[6].description',
         '<p>Olhe o slide imediatamente anterior e o imediatamente posterior ao novo. Eles devem estar exatamente como '
         'estavam.</p>'),
        ('items[5].items[0].heading', 'Se travar na Oficina 3'),
        ('items[5].items[0].paragraph', '<p>Abra o problema que apareceu para ver o que fazer:</p>'),
        ('items[6].items[0].description',
         '<p>Desfaça com Ctrl + Z. Refaça o pedido declarando explicitamente: "não altere nenhum outro slide".</p>'),
        ('items[6].items[1].description',
         '<p>Volte para o arquivo original, que continua intacto. É exatamente para isso que você trabalha na cópia '
         'criada na Oficina 0.</p>'),
        ('items[6].items[2].description',
         '<p>Vá em PowerPoint &gt; Página Inicial &gt; Layout e escolha o layout dos demais slides.</p>'),
        ('items[6].items[3].title', 'Pedi para mexer num gráfico e não funcionou'),
        ('items[6].items[3].description',
         '<p>Limitação declarada pelo fabricante: recursos avançados de gráficos, formas e formatação podem ser '
         'limitados ou ainda estar em desenvolvimento. Faça à mão.</p>'),
        ('items[7].items[0].heading', 'Oficina 4 — Trocar de público'),
        ('items[7].items[0].paragraph',
         '<p>Parta de uma cópia da apresentação da Oficina 2 ou 3. Duplique de novo em PowerPoint &gt; Arquivo &gt; '
         'Salvar como, com um nome que diga o público de destino, por exemplo aula-banca.pptx, e peça o ajuste '
         'declarando quem é o novo público e o que muda por causa dele. Veja nas abas dois destinos comuns:</p>'),
        ('items[8].items[0].description',
         '<p>Peça: """ Ajuste esta apresentação para uma banca de qualificação de mestrado. Reduza para quinze slides. '
         'Aumente o detalhe metodológico, diminua a contextualização histórica e mantenha todos os números exatamente '
         'como estão. Não altere o sentido nem as ressalvas das afirmações. Mantenha o estilo desta apresentação. """'
         '</p><p></p><p>Percorra o resultado no painel de miniaturas e repare quais slides saíram e se a ordem do '
         'argumento mudou. Depois valide com """ Qual é a narrativa desta apresentação e onde estão as lacunas para '
         'uma banca de qualificação? """ e antecipe a arguição com """ Que perguntas uma banca de qualificação '
         'provavelmente fará sobre esta apresentação? """</p>'),
        ('items[8].items[1].description',
         '<p>Para o público leigo, o pedido muda de direção: menos jargão, mais exemplos, mesmo argumento. Diga quem '
         'vai assistir e quanto tempo você tem, e mantenha a exigência de preservar todos os números e as ressalvas '
         'das afirmações.</p><p></p><p>Ao conferir, procure o que a versão leiga não pode assumir como sabido: todo '
         'termo técnico precisa ser explicado ou sair. O argumento principal tem que continuar de pé para quem não é '
         'da área.</p>'),
        ('items[9].items[0].paragraph',
         '<ul><li><strong>Afirmações:</strong> tudo o que está escrito está no material de origem?</li><li><strong>'
         'Números:</strong> são os mesmos da versão original?</li><li><strong>Citações:</strong> existem e estão '
         'atribuídas a quem disse?</li><li><strong>Sentido:</strong> alguma frase ficou mais forte, mais fraca ou '
         'perdeu a ressalva? Um "sugere" que virou "demonstra" passa batido se você só olhar os números.</li><li>'
         '<strong>Slides:</strong> algum slide importante sumiu ou mudou de lugar?</li><li><strong>Visual:</strong> o '
         'tema institucional continua em todos?</li></ul><p>É a lista da própria OpenAI para conferir antes de usar. '
         'Ponto de controle: você tem dois arquivos, com contagens de slides diferentes, todos os números coincidem '
         'entre eles, e você escolheu três afirmações da versão nova e confirmou que dizem o mesmo que na original.</p>'),
        ('items[10].items[0].heading', 'Se travar na Oficina 4'),
        ('items[10].items[0].paragraph', '<p>Abra o problema que apareceu para ver o que fazer:</p>'),
        ('items[11].items[0].description',
         '<p>Você não disse o suficiente sobre o público. Diga quem é a banca, o que ela vai cobrar e quanto tempo você '
         'tem.</p>'),
        ('items[11].items[1].description',
         '<p>Diga qual slide precisa voltar e o que cortar no lugar.</p>'),
        ('items[11].items[2].description',
         '<p>Corrija à mão e reforce no pedido: "mantenha todos os números exatamente como estão".</p>'),
        ('items[11].items[3].description',
         '<p>Reaplique em PowerPoint &gt; Design &gt; Temas.</p>'),
        ('items[11].items[4].description',
         '<p>É mudança de sentido na reescrita. Volte à frase original, corrija à mão e reforce: "não altere o sentido '
         'nem as ressalvas das afirmações".</p>'),
        ('items[13].items[0].paragraph',
         '<p>Quer ir além? Os três desafios abaixo são opcionais:</p>'),
        ('items[14].items[0].paragraph',
         '<p><strong>Três públicos</strong><br>Faça a terceira versão, para o público leigo. Deu certo se: você '
         'consegue dizer o que a versão leiga não pode assumir como sabido.</p>'),
        ('items[14].items[1].paragraph',
         '<p><strong>A versão de emergência</strong><br>Peça a versão de cinco minutos, com cinco slides. Deu certo '
         'se: ela ainda sustenta o argumento principal.</p>'),
        ('items[14].items[2].paragraph',
         '<p><strong>A objeção mais forte</strong><br>Peça: "se você fosse contra esta apresentação, qual seria a sua '
         'objeção mais forte?". Deu certo se: você tem uma resposta preparada.</p>'),
        ('items[15].items[0].answers[0].feedback',
         'Incorreto. Número que muda entre versões é exatamente o erro que a revisão em seis pontos existe para pegar. '
         'Pequena diferença em dado compromete a credibilidade.'),
        ('items[15].items[0].answers[1].feedback',
         'Correto. Corrija à mão com base na origem e reforce no pedido: "mantenha todos os números exatamente como '
         'estão".'),
        ('items[15].items[0].answers[3].feedback',
         'Incorreto. Recomeçar descarta o que já foi conferido. Basta corrigir à mão o número divergente e reforçar a '
         'instrução.'),
        ('items[17].items[0].paragraph',
         '<p>Você agora tem duas versões da mesma apresentação, com números conferidos, sentido preservado e a '
         'arguição antecipada. O próximo passo é o ciclo completo: escolha um material de origem real e produza, a '
         'partir dele, uma aula de cinquenta minutos para a graduação e um seminário de vinte minutos para colegas da '
         'área. As duas versões saem do material de origem, nunca uma da outra, porque derivar da longa propaga '
         'qualquer erro que tenha entrado nela.</p><p>A própria OpenAI resume o bom uso em quatro coisas, e você '
         'praticou as quatro: pedido específico, fonte confiável, dizer o que não pode mudar e revisão humana. Se um '
         'dia o resultado vier ruim, uma delas faltou.</p>'),
    ],
}
