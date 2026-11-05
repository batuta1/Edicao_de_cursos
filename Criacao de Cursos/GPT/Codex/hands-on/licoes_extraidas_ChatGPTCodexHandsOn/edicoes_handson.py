"""Edicoes de texto do curso ChatGPT CODEX - Hands On.

Curso gerado em ingles a partir de um roteiro em portugues. As edicoes traduzem para PT-BR e
alinham cada campo ao roteiro-fonte Codex-Para-Leigos-Hands-on.md.

Mapeamento: L1 = Abertura + Oficina 1; L2 = Oficinas 2 e 3; L3 = Oficina 4 + Projeto Final.
Nao editados de proposito: botoes "Continue" dos divisores (padrao dos cursos irmaos) e as frentes
de flashcard "ChatGPT", "Codex" e "Prompt" (iguais em portugues).

Uso (a partir da pasta hands-on):
    python licoes_extraidas_ChatGPTCodexHandsOn/aplicar_edicoes.py edicoes_handson
"""

PASTA = "licoes_extraidas_ChatGPTCodexHandsOn"
CURSO_ORIGINAL = "cursoChatGPTCodexHandsOn.json"

L1 = "licao_01_Getting_Started_with_Codex_and_ChatGPT.json"
L2 = "licao_02_Connecting_Codex_to_GitHub_and_Delegating_Tasks.json"
L3 = "licao_03_Reviewing,_Approving,_and_Delivering_AI-Completed_Tasks.json"

EDICOES = {
    # ------------------------------------------------------------------------------------------
    # Licao 1 — Abertura ("Antes de Arregacar as Mangas") + Oficina 1
    # ------------------------------------------------------------------------------------------
    L1: [
        ("title", "Descobrindo o Que o Codex Faz por Você"),

        ("items[0].items[0].heading", "Antes de Arregaçar as Mangas"),
        ("items[0].items[0].paragraph",
         "<p>Esqueça a ideia de curso em que você passa a primeira hora só ouvindo teoria antes de "
         "encostar em qualquer coisa. Aqui a lógica é inversa: você abre o Codex já nesta primeira "
         "lição e sai do curso com pelo menos uma tarefa de verdade, feita por um agente de IA e "
         "revisada por você. Não é preciso saber programar como profissional para acompanhar; é "
         "preciso, sim, topar clicar, testar e errar um pouco pelo caminho.</p>"
         "<p>São quatro oficinas e um Projeto Final, em cerca de 85 minutos. Cada oficina entrega uma "
         "pequena vitória concreta e deixa o terreno pronto para a próxima, por isso faça tudo na "
         "ordem.</p>"),

        ("items[1].items[0].paragraph", "<p>Ao final desta lição, você será capaz de:</p>"),
        ("items[2].items[0].paragraph",
         "<p>Acessar o ChatGPT em chatgpt.com e localizar o Codex no menu lateral.</p>"),
        ("items[2].items[1].paragraph",
         "<p>Deixar prontas as duas contas que o curso usa: ChatGPT e GitHub, ambas gratuitas.</p>"),
        ("items[2].items[2].paragraph",
         "<p>Diferenciar <em>perguntar</em> a uma IA de <em>delegar</em> uma tarefa a ela, e escolher "
         "o modo certo do Codex para cada situação.</p>"),
        ("items[2].items[3].paragraph",
         "<p>Usar o modo de pergunta para tirar uma dúvida sem alterar nenhum arquivo ou "
         "projeto.</p>"),

        # Process: "O que voce precisa ter aberto agora" + passos 1 a 3 da Oficina 1
        ("items[4].items[0].title", "O que você precisa ter aberto agora"),
        ("items[4].items[0].description",
         "<p>Antes da primeira oficina, deixe três coisas à mão: um navegador (Chrome, Edge ou "
         "similar), uma conta no ChatGPT e uma conta gratuita no GitHub. São poucos minutos de "
         "preparação que evitam interromper a prática no meio.</p>"),
        ("items[4].items[1].title", "Tudo pronto para a prática"),
        ("items[4].items[1].description",
         "<p>Você está logado no ChatGPT, já sabe onde fica o Codex e tem (ou sabe como criar) a "
         "conta no GitHub que será usada na próxima lição. Falta experimentar o Codex na prática, "
         "que é o que vem a seguir.</p>"),
        ("items[4].items[2].title", "Abra o ChatGPT no navegador"),
        ("items[4].items[2].description",
         "<p>Abra o navegador de sua preferência (Chrome, Edge ou similar) e acesse "
         "<strong>chatgpt.com</strong>.</p>"),
        ("items[4].items[3].title", "Entre na sua conta ou crie uma gratuita"),
        ("items[4].items[3].description",
         "<p>Se já tem conta no ChatGPT, faça login. Se ainda não tem, crie uma gratuitamente: o "
         "plano gratuito já é suficiente para acompanhar o curso.</p>"),
        ("items[4].items[4].title", "Adiante: crie sua conta gratuita no GitHub"),
        ("items[4].items[4].description",
         "<p>O GitHub só entra em cena na Oficina 2, na próxima lição, mas vale deixar a conta "
         "pronta. Se ainda não tiver uma, crie gratuitamente em <strong>github.com</strong>; leva "
         "poucos minutos.</p>"),
        ("items[4].items[5].title", "Localize o Codex no ChatGPT"),
        ("items[4].items[5].description",
         "<p>Já logado, localize o Codex no menu lateral do ChatGPT. Repare nas opções de interação: "
         "uma para conversar/perguntar e outra para gerar/executar código. Os nomes exatos podem "
         "variar conforme a versão da interface; procure algo como “Perguntar” e “Gerar código”, ou "
         "equivalentes.</p>"),

        # Flashcards
        ("items[5].items[0].heading", "Termos que você vai ver no curso"),
        ("items[5].items[0].paragraph",
         "<p>Três palavras aparecem o tempo todo daqui em diante. Vire cada cartão para conferir o "
         "significado antes de começar a prática.</p>"),
        ("items[6].items[0].back.description",
         "<p>O assistente de IA da OpenAI, acessado em chatgpt.com. Você conversa com ele em "
         "linguagem natural e recebe respostas. É dentro dele que fica o Codex.</p>"),
        ("items[6].items[1].back.description",
         "<p>O agente de IA que fica dentro do ChatGPT. Além de responder perguntas, ele "
         "<em>faz</em> o trabalho: cria e altera arquivos de um projeto conectado e mostra o que "
         "mudou para você revisar.</p>"),
        ("items[6].items[2].back.description",
         "<p>O pedido que você escreve para o ChatGPT ou para o Codex. Quanto mais claro o pedido, "
         "mais previsível o resultado; você vai praticar isso na Oficina 3.</p>"),

        # "O Problema" da Oficina 1 + accordion dos dois modos
        ("items[7].items[0].heading", "Perguntar ou delegar: qual é a diferença?"),
        ("items[7].items[0].paragraph",
         "<p>Você abre o ChatGPT para resolver alguma coisa chata: arrumar um trecho do seu projeto "
         "ou montar um relatório. Só que um chat comum te dá uma <em>resposta</em>, e quem faz o "
         "trabalho continua sendo você. Com o Codex, você pode perguntar ou delegar, e saber quando "
         "usar cada um é o primeiro passo. Abra cada item abaixo.</p>"),
        ("items[8].items[0].title", "Quando usar o modo de pergunta"),
        ("items[8].items[0].description",
         "<p>Para dúvidas rápidas, explicações e orientações. Nesse modo, o Codex responde em texto "
         "e <strong>não altera nenhum arquivo ou projeto</strong>. Exemplo: “em que tipo de tarefa "
         "eu deveria usar o Codex?”.</p>"),
        ("items[8].items[1].title", "Quando usar o modo de tarefa"),
        ("items[8].items[1].description",
         "<p>Quando você quer que o Codex <em>faça</em> o trabalho: criar ou editar arquivos, gerar "
         "código, ajustar um documento em um projeto conectado. É a opção de gerar/executar. Você "
         "vai usá-la a partir da Oficina 3, quando já houver um repositório conectado.</p>"),
        ("items[8].items[2].title", "Por que isso importa"),
        ("items[8].items[2].description",
         "<p>Escolher o modo certo evita surpresas. Se você só precisa de uma informação, o modo de "
         "pergunta é mais rápido e não mexe em nada. Se precisa de uma entrega, abra uma tarefa. Na "
         "dúvida sobre o projeto, comece sempre perguntando, antes de pedir qualquer "
         "alteração.</p>"),

        # Knowledge check 1 (gabarito inalterado: modo de tarefa)
        ("items[9].items[0].title",
         "Você quer que o Codex crie ou altere de fato um arquivo do seu projeto. Qual modo você "
         "deve usar?"),
        ("items[9].items[0].answers[0].title", "Modo de pergunta"),
        ("items[9].items[0].answers[0].feedback",
         "Não. No modo de pergunta o Codex só conversa: explica e orienta, mas não cria nem altera "
         "arquivos."),
        ("items[9].items[0].answers[1].title", "Modo de tarefa"),
        ("items[9].items[0].answers[1].feedback",
         "Correto. Criar ou alterar arquivos é executar trabalho no projeto, e isso se faz no modo "
         "de tarefa (gerar/executar)."),
        ("items[9].items[0].answers[2].title", "Apenas chat"),
        ("items[9].items[0].answers[2].feedback",
         "Não. Um chat comum devolve uma resposta, e quem faz a alteração continua sendo você. Para "
         "o Codex agir no projeto, é preciso abrir uma tarefa."),
        ("items[9].items[0].answers[3].title", "Nenhuma das anteriores"),
        ("items[9].items[0].answers[3].feedback",
         "Não. Existe uma opção certa na lista: o modo de tarefa, que é o que executa alterações no "
         "projeto."),

        ("items[10].items[0].paragraph",
         "<p>🔑 <strong>Regra de ouro:</strong> o primeiro prompt quase nunca sai perfeito, e tudo "
         "bem. Ajustar o pedido faz parte do processo, não é sinal de que você fez algo "
         "errado.</p>"),

        # Process: mao na massa da Oficina 1
        ("items[11].items[0].title", "Mão na massa: sua primeira pergunta ao Codex"),
        ("items[11].items[0].description",
         "<p>Agora você vai ver na prática como o Codex responde no modo de pergunta. Leva poucos "
         "minutos, e nenhum arquivo ou projeto é alterado.</p>"),
        ("items[11].items[1].title", "Deu certo?"),
        ("items[11].items[1].description",
         "<p>Você recebeu uma explicação em texto, e nenhum arquivo, projeto ou tarefa foi alterado. "
         "É exatamente o comportamento esperado: no modo de pergunta, o Codex só conversa, nunca "
         "executa nada.</p>"),
        ("items[11].items[2].title", "Abra o Codex no modo de pergunta"),
        ("items[11].items[2].description",
         "<p>No menu lateral do ChatGPT, abra o Codex e escolha a opção de perguntar (algo como "
         "“Perguntar”, ou o equivalente na sua versão da interface).</p>"),
        ("items[11].items[3].title", "Digite a pergunta"),
        ("items[11].items[3].description",
         "<p>Digite exatamente:</p>"
         "<p><em>“O que é o Codex e em que tipo de tarefa eu deveria usá-lo?”</em></p>"),
        ("items[11].items[4].title", "Leia a resposta com calma"),
        ("items[11].items[4].description",
         "<p>Leia a resposta com calma. Repare que o Codex explica, mas não altera nenhum arquivo "
         "nem projeto.</p>"),
        ("items[11].items[5].title", "Quer ir além? Compare com um chat comum"),
        ("items[11].items[5].description",
         "<p>Pergunte ao Codex: <em>“Quais são as principais diferenças entre você e um chat de IA "
         "comum?”</em> Compare a resposta com o que você acabou de descobrir na prática.</p>"),

        # Se travar
        ("items[12].items[0].heading", "Se travar"),
        ("items[12].items[0].paragraph",
         "<p>Travar no começo é normal. Abra o item que corresponde ao seu caso.</p>"),
        ("items[13].items[0].title", "Não encontro o Codex no menu"),
        ("items[13].items[0].description",
         "<p>Confira se você está logado e procure por “Codex” no menu principal do ChatGPT. A "
         "disponibilidade pode variar conforme o plano e a região.</p>"),
        ("items[13].items[1].title", "A resposta veio muito genérica"),
        ("items[13].items[1].description",
         "<p>Refaça a pergunta acrescentando contexto. Por exemplo: <em>“Para que tipo de tarefa de "
         "programação ou de organização de documentos eu usaria o Codex?”</em></p>"),
        ("items[13].items[2].title", "Dica: quando ficar no modo de pergunta"),
        ("items[13].items[2].description",
         "<p>💡 Sempre que tiver uma dúvida rápida e não precisar que nada seja alterado de verdade, "
         "use o modo de pergunta. É mais rápido do que abrir uma tarefa completa.</p>"),

        # Knowledge check 2 (gabarito inalterado: refazer com mais contexto)
        ("items[14].items[0].title",
         "Você fez uma pergunta ao Codex no modo de pergunta e recebeu uma resposta muito genérica. "
         "O que fazer?"),
        ("items[14].items[0].answers[0].title", "Refazer a pergunta com mais contexto"),
        ("items[14].items[0].answers[0].feedback",
         "Correto. Dizer para que tipo de tarefa você quer usar o Codex (programação, organização de "
         "documentos etc.) ajuda a ferramenta a dar uma resposta específica e útil."),
        ("items[14].items[0].answers[1].title", "Esperar uma resposta melhor"),
        ("items[14].items[0].answers[1].feedback",
         "Não. Esperar não muda a resposta. Quem melhora o resultado é o pedido: acrescente contexto "
         "e pergunte de novo."),
        ("items[14].items[0].answers[2].title", "Mudar para o modo de tarefa"),
        ("items[14].items[0].answers[2].feedback",
         "Não. O problema está na pergunta, não no modo. Abrir uma tarefa serve para alterar o "
         "projeto, e aqui você só precisa de uma explicação melhor."),
        ("items[14].items[0].answers[3].title", "Desistir"),
        ("items[14].items[0].answers[3].feedback",
         "Não. Lembre a regra de ouro: o primeiro prompt quase nunca sai perfeito. Reformule com "
         "mais detalhes e tente de novo."),

        # Fechamento
        ("items[16].items[0].paragraph",
         "<p>Você já sabe onde fica o Codex e sentiu a diferença entre perguntar e delegar. Só que, "
         "para delegar de verdade, o Codex precisa de um lugar onde trabalhar. Na próxima lição, "
         "você cria um repositório de teste no GitHub e o conecta ao Codex (Oficina 2), e depois "
         "pede sua primeira tarefa (Oficina 3). Deixe à mão o login do GitHub.</p>"),
    ],

    # ------------------------------------------------------------------------------------------
    # Licao 2 — Oficina 2 (sala de trabalho) + Oficina 3 (primeira tarefa)
    # ------------------------------------------------------------------------------------------
    L2: [
        ("title", "Conectando o Codex ao GitHub e Pedindo Sua Primeira Tarefa"),

        ("items[0].items[0].heading", "Preparando sua sala de trabalho"),
        ("items[0].items[0].paragraph",
         "<p>Um agente de trabalho precisa de um lugar para trabalhar. Sem um projeto conectado, o "
         "Codex simplesmente não tem onde colocar a mão. Nesta lição, você dá a ele essa “sala”, um "
         "repositório de teste no GitHub (Oficina 2), e depois pede a primeira tarefa de verdade "
         "(Oficina 3). Tenha à mão a conta no GitHub e reserve uns 15 minutos de atenção, sem "
         "pressa, para a parte do pedido.</p>"),

        ("items[1].items[0].paragraph", "<p>Ao final desta lição, você será capaz de:</p>"),
        ("items[2].items[0].paragraph",
         "<p>Criar um repositório de teste no GitHub e conectá-lo ao Codex.</p>"),
        ("items[2].items[1].paragraph",
         "<p>Revisar as permissões concedidas ao Codex ao autorizar o acesso ao GitHub.</p>"),
        ("items[2].items[2].paragraph",
         "<p>Escrever um pedido com objetivo, contexto, restrições e critério de sucesso.</p>"),
        ("items[2].items[3].paragraph",
         "<p>Delegar uma tarefa real ao Codex e acompanhar a execução até o comparativo (diff) "
         "final.</p>"),

        # Process: Oficina 2
        ("items[3].items[0].title", "Oficina 2: mão na massa"),
        ("items[3].items[0].description",
         "<p>Você vai criar um repositório só para praticar e conectá-lo ao Codex. É nele que o "
         "agente vai trabalhar até o fim do curso.</p>"),
        ("items[3].items[1].title", "Deu certo?"),
        ("items[3].items[1].description",
         "<p>O repositório de teste aparece disponível dentro do Codex, pronto para receber uma "
         "tarefa. Era exatamente esse o objetivo da Oficina 2. Quer ir além? Antes de seguir, "
         "explore a lista de arquivos do repositório diretamente de dentro do Codex.</p>"),
        ("items[3].items[2].title", "Crie sua conta no GitHub"),
        ("items[3].items[2].description",
         "<p>Se ainda não tiver conta no GitHub, crie uma gratuitamente em "
         "<strong>github.com</strong>. Se já criou na lição anterior, apenas faça login.</p>"),
        ("items[3].items[3].title", "Crie um repositório de teste"),
        ("items[3].items[3].description",
         "<p>Dentro do GitHub, crie um repositório novo, só para praticar. Sugestão de nome: "
         "<strong>meu-teste-codex</strong>. Na tela de criação, marque a opção de adicionar um "
         "arquivo README (“Add a README file”): é nele que o Codex vai trabalhar na Oficina 3.</p>"),
        ("items[3].items[4].title", "Conecte o repositório no Codex"),
        ("items[3].items[4].description",
         "<p>Volte ao Codex e procure a opção para conectar ou adicionar um repositório. Siga o "
         "fluxo que aparecer na tela.</p>"),
        ("items[3].items[5].title", "Autorize revisando as permissões"),
        ("items[3].items[5].description",
         "<p>O fluxo vai pedir que você autorize o Codex a acessar sua conta do GitHub. Leia com "
         "atenção quais permissões estão sendo concedidas antes de confirmar.</p>"),
        ("items[3].items[6].title", "Confirme a conexão"),
        ("items[3].items[6].description",
         "<p>Confira se o repositório <strong>meu-teste-codex</strong> aparece listado dentro do "
         "Codex. Se aparecer, o agente já tem onde trabalhar.</p>"),

        # Se travar na Oficina 2
        ("items[4].items[0].heading", "Se travar na Oficina 2"),
        ("items[4].items[0].paragraph",
         "<p>Abra o item que corresponde ao seu caso.</p>"),
        ("items[5].items[0].title", "Não aparece a opção para conectar o GitHub"),
        ("items[5].items[0].description",
         "<p>A sessão do ChatGPT pode ter expirado. Saia da conta e entre novamente.</p><p></p>"
         "<p>Esse passo simples costuma trazer de volta as opções que tinham sumido do menu.</p>"),
        ("items[5].items[1].title", "O repositório não aparece depois de autorizado"),
        ("items[5].items[1].description",
         "<p>Verifique, nas configurações da sua conta ou organização no GitHub, se o acesso ao "
         "repositório foi realmente concedido ao Codex.</p><p></p>"
         "<p>Se você autorizou só alguns repositórios, confira se o <strong>meu-teste-codex</strong> "
         "está entre os selecionados.</p>"),
        ("items[5].items[2].title", "Cuidado com as permissões"),
        ("items[5].items[2].description",
         "<p>⚠️ Revise sempre quais permissões está concedendo ao autorizar o acesso ao GitHub. Para "
         "praticar, prefira repositórios de teste em vez de projetos importantes.</p><p></p>"
         "<p>Assim, se algo sair diferente do esperado, nada que importa é afetado.</p>"),

        ("items[6].items[0].paragraph",
         "<p><strong>Regra para todo o curso:</strong> pratique sempre no repositório de teste. "
         "Conecte projetos importantes só depois de dominar o ciclo de pedir, conferir e "
         "aceitar.</p>"),

        # Flashcards: as quatro partes de um bom pedido (Oficina 3)
        ("items[8].items[0].heading", "Oficina 3: as quatro partes de um bom pedido"),
        ("items[8].items[0].paragraph",
         "<p>Pedir algo de forma vaga para um agente de IA é como pedir para alguém “resolver isso "
         "aí” sem dizer o quê, onde, nem como saber que terminou. Um bom pedido sempre tem quatro "
         "partes. Vire cada cartão.</p>"),
        ("items[9].items[0].back.description",
         "<p><strong>O quê.</strong> A tarefa que você quer que o Codex faça. Exemplo: adicionar uma "
         "seção chamada “Sobre o projeto”.</p>"),
        ("items[9].items[0].front.description", "<strong>Objetivo</strong>"),
        ("items[9].items[1].back.description",
         "<p><strong>Onde.</strong> O arquivo, a pasta ou a parte do projeto em que a tarefa "
         "acontece. Exemplo: no arquivo README.md.</p>"),
        ("items[9].items[1].front.description", "<strong>Contexto</strong>"),
        ("items[9].items[2].back.description",
         "<p><strong>O que não mexer.</strong> O que o Codex deve deixar intacto. Exemplo: “Não "
         "altere mais nada além disso.”</p>"),
        ("items[9].items[2].front.description", "<strong>Restrições</strong>"),
        ("items[9].items[3].back.description",
         "<p><strong>Como saber que terminou.</strong> O resultado que você espera ver. Exemplo: o "
         "README passa a ter a nova seção, sem perder o conteúdo que já existia.</p>"),
        ("items[9].items[3].front.description", "<strong>Critério de sucesso</strong>"),

        ("items[10].items[0].paragraph",
         "<p>Com as quatro partes, o Codex sabe o que fazer, onde agir e o que não tocar. Sem elas, "
         "ele precisa adivinhar, e o resultado fica imprevisível: pode alterar arquivos que você "
         "não queria ou parar antes do que você esperava.</p>"
         "<p>No exercício a seguir, você envia os dois tipos de pedido e compara o resultado.</p>"),

        # Process: mao na massa da Oficina 3
        ("items[11].items[0].title", "Mão na massa: do pedido vago ao pedido bem-feito"),
        ("items[11].items[0].description",
         "<p>Você vai enviar dois pedidos ao Codex no repositório de teste: um propositalmente vago, "
         "só para observar, e outro bem estruturado. No fim, terá uma alteração real no seu "
         "README.</p>"),
        ("items[11].items[1].title", "Deu certo?"),
        ("items[11].items[1].description",
         "<p>O Codex mostra um comparativo (diff) com a nova seção “Sobre o projeto” adicionada ao "
         "README, sem apagar nada que já estava lá. Quer ir além? Na mesma tarefa ou em uma nova, "
         "peça também uma seção “Como usar”, seguindo a mesma estrutura de pedido.</p>"),
        ("items[11].items[2].title", "Teste um pedido vago"),
        ("items[11].items[2].description",
         "<p>Abra o repositório de teste dentro do Codex e escolha a opção de gerar/executar uma "
         "tarefa (não apenas perguntar). Digite, de propósito:</p>"
         "<p><em>“Melhora esse projeto.”</em></p>"
         "<p>Repare como o pedido deixa muita coisa em aberto: o Codex pode até tentar, mas vai ter "
         "que adivinhar o que você realmente quer.</p>"),
        ("items[11].items[3].title", "Envie um pedido bem estruturado"),
        ("items[11].items[3].description",
         "<p>Abra uma nova tarefa e envie:</p>"
         "<p><em>“No arquivo README.md, adicione uma seção chamada ‘Sobre o projeto’ com uma frase "
         "explicando que este é um repositório de testes para aprender a usar o Codex. Não altere "
         "mais nada além disso. Critério de sucesso: o README passa a ter essa nova seção, sem "
         "perder o conteúdo que já existia.”</em></p>"),
        ("items[11].items[4].title", "Acompanhe o Codex trabalhando"),
        ("items[11].items[4].description",
         "<p>Acompanhe a execução em tempo real, observando a lista de arquivos sendo alterados e o "
         "registro (log) da tarefa. Tarefas simples costumam terminar em poucos minutos; aguarde a "
         "conclusão.</p>"),

        # Knowledge check (gabarito inalterado: as quatro partes)
        ("items[12].items[0].title",
         "Qual das opções descreve melhor um pedido bem estruturado para o Codex?"),
        ("items[12].items[0].answers[0].title", "Escrever apenas “melhora o projeto”"),
        ("items[12].items[0].answers[0].feedback",
         "Não. É o pedido vago da Oficina 3: não diz o quê, onde nem como saber que terminou, e o "
         "Codex fica obrigado a adivinhar."),
        ("items[12].items[0].answers[1].title",
         "Dizer o que fazer, onde, o que não alterar e como saber que terminou"),
        ("items[12].items[0].answers[1].feedback",
         "Correto. São as quatro partes de um bom pedido: objetivo, contexto, restrições e critério "
         "de sucesso."),
        ("items[12].items[0].answers[2].title", "Deixar o Codex decidir tudo sozinho"),
        ("items[12].items[0].answers[2].feedback",
         "Não. Sem orientação, o resultado fica imprevisível, e o Codex pode alterar mais do que "
         "você queria."),
        ("items[12].items[0].answers[3].title", "Informar só o objetivo"),
        ("items[12].items[0].answers[3].feedback",
         "Não. O objetivo é só uma das quatro partes. Sem contexto, restrições e critério de "
         "sucesso, o Codex não sabe onde agir, o que preservar nem quando parar."),

        # Se travar na Oficina 3
        ("items[13].items[0].heading", "Se travar na Oficina 3"),
        ("items[13].items[0].paragraph",
         "<p>Abra o item que corresponde ao seu caso.</p>"),
        ("items[14].items[0].title", "A tarefa parece travada"),
        ("items[14].items[0].description",
         "<p>Tarefas mais complexas podem levar até 30 minutos. Aguarde e acompanhe o log: passar "
         "alguns minutos sem novidade é normal.</p><p></p>"
         "<p>A tarefa do README, por ser simples, costuma terminar em poucos minutos.</p>"),
        ("items[14].items[1].title", "O resultado alterou mais do que o esperado"),
        ("items[14].items[1].description",
         "<p>O pedido provavelmente não deixou as restrições claras. Da próxima vez, diga "
         "explicitamente o que <strong>não</strong> deve ser alterado.</p><p></p>"
         "<p>Uma frase como “Não altere mais nada além disso” já evita a maior parte das alterações "
         "indesejadas.</p>"),
        ("items[14].items[2].title", "Dica: confira as quatro partes antes de enviar"),
        ("items[14].items[2].description",
         "<p>💡 Antes de enviar qualquer pedido, confira se ele tem objetivo (o quê), contexto "
         "(onde), restrições (o que não mexer) e critério de sucesso (como saber que "
         "terminou).</p><p></p>"
         "<p>Se faltar uma das quatro, complete antes de enviar. Sai mais rápido do que corrigir "
         "depois.</p>"),

        ("items[15].items[0].paragraph",
         "<p>📌 <strong>Não esqueça:</strong> pedido vago não é necessariamente “errado”, mas é "
         "imprevisível. Quanto mais claro o pedido, menos rodadas de correção você vai precisar "
         "depois.</p>"),

        # Fechamento
        ("items[17].items[0].paragraph",
         "<p>Seu repositório de teste está conectado e o Codex já entregou a primeira alteração. "
         "Mas “terminou” não é sinônimo de “está certo”. Na próxima lição, você confere esse "
         "trabalho antes de aceitar (Oficina 4) e depois faz o Projeto Final, do pedido à entrega. "
         "Mantenha à mão a tarefa do README: ela é o ponto de partida da Oficina 4.</p>"),
    ],

    # ------------------------------------------------------------------------------------------
    # Licao 3 — Oficina 4 (conferencia) + Projeto Final + "Conseguiu! E agora?"
    # ------------------------------------------------------------------------------------------
    L3: [
        ("title", "Conferindo o Trabalho do Agente e Entregando o Projeto Final"),

        ("items[0].items[0].heading", "“Pronto” não é o mesmo que “certo”"),
        ("items[0].items[0].paragraph",
         "<p>O Codex avisou que a tarefa terminou. Ótimo, mas “terminou” não é sinônimo de “está "
         "certo”. Nesta lição, você aprende a conferir o trabalho do agente antes de aceitar "
         "qualquer coisa, do jeito que um profissional experiente faria (Oficina 4). Depois, junta "
         "tudo no Projeto Final: escolhe um problema real e pequeno no repositório de teste e o leva "
         "do pedido à entrega.</p>"),

        ("items[1].items[0].paragraph", "<p>Ao final desta lição, você será capaz de:</p>"),
        ("items[2].items[0].paragraph",
         "<p>Ler o comparativo (diff) de uma tarefa e confirmar que nada além do combinado foi "
         "alterado.</p>"),
        ("items[2].items[1].paragraph",
         "<p>Conferir o registro (log) de execução em busca de erros ou avisos.</p>"),
        ("items[2].items[2].paragraph",
         "<p>Decidir entre aceitar o resultado, pedir um ajuste ou pedir uma nova execução, e "
         "explicar o porquê.</p>"),
        ("items[2].items[3].paragraph",
         "<p>Entregar uma tarefa completa, do pedido à aceitação ou à Pull Request.</p>"),

        # Process: mao na massa da Oficina 4
        ("items[4].items[0].title", "Oficina 4: mão na massa"),
        ("items[4].items[0].description",
         "<p>Abra a tarefa concluída na Oficina 3, a da seção “Sobre o projeto” no README. É nela "
         "que você vai praticar a conferência.</p>"),
        ("items[4].items[1].title", "Deu certo?"),
        ("items[4].items[1].description",
         "<p>Você consegue explicar, com suas próprias palavras, exatamente o que mudou no projeto e "
         "por que decidiu aceitar (ou não) o resultado. Quer ir além? Aplique o mesmo roteiro de "
         "conferência (diff → log → decisão) a uma tarefa antiga sua, ou à de um colega, se tiver "
         "uma disponível.</p>"),
        ("items[4].items[2].title", "Leia o diff linha por linha"),
        ("items[4].items[2].description",
         "<p>Localize o comparativo (diff) com as linhas alteradas. Leia linha por linha o que foi "
         "modificado e confirme que nada além do combinado foi tocado.</p>"),
        ("items[4].items[3].title", "Confira o log"),
        ("items[4].items[3].description",
         "<p>Confira o registro (log) de execução em busca de erros ou avisos. Ele mostra o que o "
         "Codex realmente fez, inclusive problemas que não aparecem no diff.</p>"),
        ("items[4].items[4].title", "Decida"),
        ("items[4].items[4].description",
         "<p>Escolha entre três caminhos: aceitar o resultado, pedir um ajuste ou pedir para o Codex "
         "testar de novo. Só siga em frente se entendeu completamente a alteração.</p>"),
        ("items[4].items[5].title", "Aceite ou abra uma Pull Request"),
        ("items[4].items[5].description",
         "<p>Se estiver tudo certo, aceite a alteração, ou abra uma Pull Request, caso essa opção "
         "esteja disponível para o seu repositório no GitHub.</p>"),

        # Flashcards
        ("items[5].items[0].heading", "Conceitos-chave da conferência"),
        ("items[5].items[0].paragraph",
         "<p>Três ideias sustentam a revisão de qualquer tarefa do Codex. Vire cada cartão.</p>"),
        ("items[6].items[0].back.description",
         "<p>Mostra exatamente quais linhas o Codex adicionou, removeu ou alterou nos arquivos do "
         "projeto. É a primeira coisa a ler antes de aceitar.</p>"),
        ("items[6].items[0].front.description", "<p>Diff (comparativo)</p>"),
        ("items[6].items[1].back.description",
         "<p>Registra as ações, os erros, os avisos e os resultados de teste da execução. É a prova "
         "do que o Codex realmente fez.</p>"),
        ("items[6].items[1].front.description", "<p>Log (registro)</p>"),
        ("items[6].items[2].back.description",
         "<p>Antes de aceitar, confira se o resultado cumpre o pedido original e o critério de "
         "sucesso que você definiu, sem nada além do combinado.</p>"),
        ("items[6].items[2].front.description", "<p>Critério para aceitar</p>"),

        # Se travar na Oficina 4
        ("items[7].items[0].heading", "Se travar na Oficina 4"),
        ("items[7].items[0].paragraph",
         "<p>Abra o item que corresponde ao seu caso.</p>"),
        ("items[8].items[0].title", "Não entendo por que uma linha foi alterada"),
        ("items[8].items[0].description",
         "<p>Pergunte diretamente ao Codex: <em>“Explique por que você alterou esta linha.”</em> "
         "Entender cada modificação é condição para aprovar.</p>"),
        ("items[8].items[1].title", "O log mostra um teste que falhou"),
        ("items[8].items[1].description",
         "<p>Não aceite a alteração ainda. Peça uma nova execução explicando o que falhou e o que se "
         "espera como correção.</p>"),
        ("items[8].items[2].title", "Cuidado: aceitar para ganhar tempo"),
        ("items[8].items[2].description",
         "<p>⚠️ Nunca aceite uma alteração só para ganhar tempo se você não entendeu completamente o "
         "que ela faz. Esse é o erro mais comum de quem começa a trabalhar com agentes de IA.</p>"),

        # Knowledge check (gabarito inalterado: pedir explicacao e conferir o log)
        ("items[9].items[0].title",
         "Ao revisar uma tarefa, você nota uma alteração que não esperava. O que fazer antes de "
         "aceitar?"),
        ("items[9].items[0].answers[0].title", "Aceitar a alteração para ganhar tempo"),
        ("items[9].items[0].answers[0].feedback",
         "Não. Aceitar sem entender é o erro mais comum de quem começa a trabalhar com agentes de "
         "IA, e o problema aparece depois, no projeto."),
        ("items[9].items[0].answers[1].title",
         "Pedir ao Codex que explique a alteração e conferir o log"),
        ("items[9].items[0].answers[1].feedback",
         "Correto. A explicação do Codex e o log mostram por que a linha mudou. Com isso, você "
         "decide com segurança entre aceitar, pedir um ajuste ou pedir nova execução."),
        ("items[9].items[0].answers[2].title", "Ignorar e seguir em frente"),
        ("items[9].items[0].answers[2].feedback",
         "Não. Uma alteração inesperada é justamente o que a conferência existe para pegar. "
         "Ignorá-la pode levar erros para o projeto."),
        ("items[9].items[0].answers[3].title", "Rodar o projeto inteiro de novo"),
        ("items[9].items[0].answers[3].feedback",
         "Não. Antes de refazer qualquer coisa, entenda o que mudou. Se for preciso corrigir, peça "
         "um ajuste ou uma nova execução explicando o que está errado."),

        ("items[10].items[0].paragraph",
         "<p><strong>Revisão humana nunca é opcional</strong>, nem quando o resultado parece "
         "perfeito à primeira vista. O Codex produz alterações no estilo de um profissional "
         "revisando o próprio código, mas quem responde pelo que entra no projeto é você.</p>"),

        # Process: Projeto Final
        ("items[11].items[0].title", "Projeto Final: do pedido à entrega completa"),
        ("items[11].items[0].description",
         "<p>Chegou a hora de juntar tudo: escolher um problema real e pequeno no seu repositório de "
         "teste, pedir a tarefa do jeito certo, acompanhar a execução, revisar com cuidado e "
         "entregar formalmente o resultado, como se fosse seu primeiro dia trabalhando ao lado de "
         "um agente de IA.</p>"),
        ("items[11].items[1].title", "Como saber que terminou"),
        ("items[11].items[1].description",
         "<p>Confira se você: escreveu um pedido com objetivo, contexto e critério de sucesso "
         "claros; acompanhou a execução até o fim; revisou o diff e o log completos antes de "
         "decidir; aceitou a alteração ou abriu uma Pull Request de forma consciente; e consegue "
         "explicar, em uma frase, o que foi entregue e por quê.</p>"),
        ("items[11].items[2].title", "Escolha uma melhoria real"),
        ("items[11].items[2].description",
         "<p>Escolha uma pequena melhoria real para o repositório. Por exemplo: corrigir um erro de "
         "digitação, atualizar o README ou adicionar um comentário explicativo.</p>"),
        ("items[11].items[3].title", "Escreva o pedido"),
        ("items[11].items[3].description",
         "<p>Escreva o pedido com objetivo, contexto e critério de sucesso, do jeito praticado na "
         "Oficina 3. Se houver algo que não deve ser tocado, inclua também a restrição.</p>"),
        ("items[11].items[4].title", "Envie e acompanhe"),
        ("items[11].items[4].description",
         "<p>Envie a tarefa e acompanhe a execução até o fim, como na Oficina 3: a lista de "
         "arquivos sendo alterados e o log.</p>"),
        ("items[11].items[5].title", "Revise o resultado"),
        ("items[11].items[5].description",
         "<p>Quando terminar, revise completamente o diff e o log, como praticado na Oficina 4. "
         "Confira se o resultado cumpre o critério de sucesso que você definiu.</p>"),
        ("items[11].items[6].title", "Aceite ou abra uma Pull Request"),
        ("items[11].items[6].description",
         "<p>Se estiver tudo certo, aceite a alteração ou abra uma Pull Request com o resultado. Se "
         "não estiver, peça um ajuste antes de aceitar.</p>"),
        ("items[11].items[7].title", "Resuma em uma frase"),
        ("items[11].items[7].description",
         "<p>Escreva, em uma frase só, o que você entregou e o que aprendeu fazendo esse "
         "projeto.</p>"),

        # Fechamento ("Conseguiu! E agora?" + itens da Parte dos Dez)
        ("items[13].items[0].paragraph",
         "<p>Se você chegou até aqui, já abriu o Codex, escreveu pedidos de verdade, acompanhou uma "
         "execução real e revisou um resultado antes de aceitá-lo. É exatamente o ciclo que "
         "profissionais experientes repetem todos os dias.</p>"
         "<p>O próximo passo é praticar com projetos reais, cada vez um pouco mais ambiciosos, "
         "dividindo tarefas grandes em pedidos menores e mais claros. Quando o básico estiver "
         "confortável, explore recursos mais avançados: um arquivo AGENTS.md na raiz do projeto "
         "(que pode ser criado com o comando <strong>/init</strong>) para o Codex seguir os padrões "
         "do seu time, várias tarefas rodando em paralelo e automações recorrentes. Uma tarefa de "
         "cada vez: a confiança no agente se constrói aos poucos.</p>"),
    ],
}
