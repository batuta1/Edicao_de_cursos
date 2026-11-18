"""Catálogo: que informações existem dentro de um SCORM do Rise 360 e ONDE ficam.

A ficha (ficha.py) usa só as marcadas como USADA. As demais ficam anotadas aqui, com o caminho exato, para quando
quisermos pegá-las: basta ler o caminho indicado (não é preciso descobrir de novo onde estão).

Onde procurar (a coluna "onde"):
  manifesto   -> imsmanifest.xml, na raiz do zip (ou numa pasta de topo)
  json        -> o JSON do curso, em base64 dentro de scormcontent/runtime-data.js (export novo) ou de
                 scormcontent/index.html (export antigo); ver leitura/formato.py
  zip         -> o próprio arquivo .zip e a lista dos arquivos dentro dele
Dentro do JSON, `course` é o curso, `course.lessons[]` são os capítulos e `course.lessons[].items[]` são os blocos
(no capítulo de quiz, as questões). As posições (`position`) do Rise começam em 0.

Texto do conteúdo (parágrafos, títulos de blocos, perguntas e respostas dos quizzes, imagens, vídeos) NÃO entra na
ficha por decisão do usuário (D01-3, D01-5); aqui só está dito onde ele fica.
"""

USADA, DISPONIVEL = "USADA", "disponível"

# (nome, onde, caminho, situação, observação)
INFORMACOES = [
    # --- Curso: o que aparece na capa
    ("título do curso", "json", "course.title", USADA, "Também está no manifesto (organizations/organization/title); os dois podem diferir."),
    ("descrição do curso", "json", "course.description", USADA, "HTML do editor do Rise; a ficha guarda em texto limpo. Preenchida nos 109 cursos."),
    ("autores", "json", "course.authors[].authorName", USADA, "Também há course.author (id) e course.authors[].avatar (imagem)."),
    ("imagem de capa", "json", "course.coverImage, course.cardImage", DISPONIVEL, "Imagens são ignoradas por decisão do usuário."),
    # --- Curso: identidade e datas
    ("identificador do curso", "json", "course.id", USADA, "Igual ao identifier do manifesto; os 32 primeiros caracteres identificam o curso e os 8 últimos, a exportação."),
    ("curso copiado de outro", "json", "course.copyOf, course.originalId", DISPONIVEL, "Ficam vazios na maioria dos cursos."),
    ("link de compartilhamento", "json", "course.shareId", DISPONIVEL, "Identificador do link de revisão do Rise."),
    ("datas do curso", "json", "course.createdAt, course.updatedAt, course.contentUpdatedAt, course.lastPublishedAt", USADA,
     "UTC. contentUpdatedAt é a última edição do CONTEÚDO; lastPublishedAt, a última exportação."),
    ("como foi criado", "json", "course.metadata.createdVia, course.settings.isAIConceptToCourse", USADA, "createdVia = 'ai' em 107 dos 109 cursos."),
    ("curso apagado / pronto", "json", "course.deleted, course.ready", DISPONIVEL, ""),
    ("conta (tenant)", "json", "course.tenantId", DISPONIVEL, "Identificador da conta do Rise; igual em todos."),
    # --- Curso: idioma
    ("idioma da interface do player", "json", "labelSet.iso639Code, labelSet.name", USADA,
     "É o idioma dos botões e avisos do player, NÃO o do conteúdo. 95 de 109 cursos estão em inglês."),
    ("rótulos do player", "json", "labelSet.labels", DISPONIVEL, "Dicionário de ~18 KB com os textos da interface (ex.: 'Continue')."),
    ("idioma do conteúdo", "json", "course.locale, course.defaultLocaleId, course.sourceCourseLocaleId", DISPONIVEL,
     "Só existem em 8 cursos; não dá para contar com eles."),
    # --- Curso: como reporta ao LMS
    ("padrão SCORM exportado", "json", "course.exportSettings.targetName, course.exportSettings.target", USADA, "'SCORM 1.2' ou 'SCORM 2004 - 4th Edition'."),
    ("regra de reporte ao LMS", "json", "course.exportSettings.reporting, course.exportSettings.completeWith, course.exportSettings.completionPercentage", USADA,
     "Quase todos: passed-incomplete / reporting."),
    ("outras opções de exportação", "json", "course.exportSettings (28 chaves: quizId, identifier, loadOnlyInLMS, resetLearnerData, activeLMS...)", DISPONIVEL,
     "exportSettings.quizId aponta para o capítulo de quiz; exportSettings.identifier é course.id + '_rise'."),
    ("opções do LMS", "json", "course.lmsOptions", DISPONIVEL, "enableTelemetryCollection, disableCoverPage, enableExitCourse."),
    # --- Curso: só no export novo (runtime-data.js)
    ("versão do pacote", "json", "settings.coursePackageVersion", USADA, "Só no export novo. O nome do zip termina com ela (ex.: ...-scorm12-JQ7lFMWa.zip)."),
    ("nome e origem do zip exportado", "json", "settings.filename, settings.cdnUri, settings.exporterAuthId, settings.exportedAt", DISPONIVEL, "Só no export novo."),
    ("estatísticas calculadas pelo Rise", "json", "exportAggregate (courseLessons.total/ai/blocks..., courseTheme, courseCreatedVia, exportId, subscriptionId)", DISPONIVEL,
     "Só no export novo. Conta capítulos e blocos 'ai' x manuais."),
    ("política de entrega", "json", "deliveryPolicy (access, protection, status, evaluatedAt)", DISPONIVEL, "Só no export novo."),
    ("conteúdo de parceiro", "json", "partnerContent", DISPONIVEL, "Só no export novo; vazio nos exemplos."),
    ("mídia do curso", "json", "media (raiz do JSON, só no export antigo)", DISPONIVEL, "Mídia é ignorada."),
    # --- Curso: aparência e recursos
    ("tema, cores e tipografia", "json", "course.theme, course.color, course.bodyTypeface, course.headingTypeface, course.uiTypeface, fonts", DISPONIVEL, "Aparência do player."),
    ("navegação e comportamento do player", "json",
     "course.navigationMode, sidebarMode, showLessonCount, showNavigationButtons, allowSearch, animateBlockEntrance, allowCopy, enableVideoPlaybackSpeed",
     DISPONIVEL, "Configurações; quase todas iguais entre os cursos."),
    ("recursos do Rise em uso", "json", "course.features", DISPONIVEL, "Mapa de recursos ligados (ex.: ai-learner-chatbot, rise-course-navigation)."),
    ("tutor de IA", "json", "course.aiTutorConfig, course.aiTutorImage", DISPONIVEL, "Em 100 e 19 cursos; vazio na maioria."),
    ("segredos", "json", "course.sharePassword, course.aiLearnerCourseApiKey", DISPONIVEL,
     "Vazios nos 109 cursos. Nunca copiar para a saída se vierem preenchidos."),
    # --- Capítulos
    ("lista e ordem dos capítulos", "json", "course.lessons[] ordenados por position (0, 1, 2...)", USADA, "A ficha numera a partir de 1, como na barra lateral do player."),
    ("título do capítulo", "json", "course.lessons[].title", USADA, ""),
    ("descrição do capítulo", "json", "course.lessons[].description", USADA, "Vazia em 597 de 602 capítulos de conteúdo."),
    ("tipo do capítulo", "json", "course.lessons[].type", USADA, "'blocks' (conteúdo) ou 'quiz'."),
    ("capítulo apagado / pronto", "json", "course.lessons[].deleted, course.lessons[].ready", USADA, "'deleted' vira alerta."),
    ("datas do capítulo", "json", "course.lessons[].createdAt, course.lessons[].updatedAt", USADA,
     "É o que mostra quais capítulos foram mexidos depois da criação (createdVia não mostra, é 'ai' em quase todos os blocos)."),
    ("capítulo obrigatório para concluir", "json", "course.lessons[].settings.isRequiredForCompletion", DISPONIVEL, ""),
    ("ícone do capítulo", "json", "course.lessons[].icon", DISPONIVEL, "'Article' ou 'Quiz'."),
    ("quem editou", "json", "course.lessons[].author, lastUpdatedBy, selectedAuthorId", DISPONIVEL, "Ids de autor, não nomes."),
    ("cópia de outro capítulo", "json", "course.lessons[].originalId, duplicatedFromId", DISPONIVEL, ""),
    ("imagem do cabeçalho", "json", "course.lessons[].headerImage, course.lessons[].media", DISPONIVEL, "Mídia é ignorada."),
    # --- Blocos
    ("quantidade e tipos de bloco", "json", "course.lessons[].items[].type, .family, .variant", USADA,
     "Ex.: family 'interactive' + variant 'accordion'. É o melhor descritor do que o capítulo tem, sem revelar o conteúdo."),
    ("tamanho do texto (palavras)", "json", "course.lessons[].items[] (todos os textos, menos mídia, srcdoc e configuração)", USADA,
     "Só se conta; o texto não é guardado. Serve de base para estimar o tempo de leitura."),
    ("bloco de HTML customizado", "json", "course.lessons[].items[] com family 'html' (o código fica em items[].srcdoc)", USADA, "Código próprio dentro do curso: ponto de atenção."),
    ("texto dos blocos", "json", "course.lessons[].items[].items[] (paragraph, heading, title...)", DISPONIVEL, "CONTEÚDO: fora por decisão do usuário."),
    ("origem do bloco", "json", "course.lessons[].items[].metadata.createdVia", DISPONIVEL, "'ai' em quase todos."),
    ("identificador global do bloco", "json", "course.lessons[].items[].globalBlockId", DISPONIVEL, ""),
    # --- Quiz
    ("nota mínima, tentativas e revelação das respostas", "json",
     "course.lessons[] (type 'quiz').settings.passingScore, .retryCount (-1 = ilimitadas), .revealAnswers, .shuffleAnswerChoices, .randomizeQuestionOrder", USADA,
     "Nota 80 e tentativas ilimitadas em todos os quizzes dos 109 cursos."),
    ("questões do quiz por tipo", "json", "course.lessons[] (type 'quiz').items[].type", USADA, "MULTIPLE_CHOICE, MULTIPLE_RESPONSE, MATCHING, FILL_IN_THE_BLANK."),
    ("número de respostas por questão", "json", "course.lessons[] (type 'quiz').items[].answers[]", DISPONIVEL, "Só contar; o texto é conteúdo."),
    ("resposta correta e feedback", "json", "items[].correct, .corrects, .feedbackType, .feedbackCorrect, .feedbackIncorrect", DISPONIVEL, "CONTEÚDO do quiz: fora por decisão do usuário."),
    # --- Manifesto
    ("identificador do manifesto", "manifesto", "manifest@identifier", USADA, "Igual a course.id."),
    ("esquema e versão do SCORM", "manifesto", "metadata/schema, metadata/schemaversion", USADA, "'ADL SCORM' 1.2 ou 2004 4th Edition."),
    ("título da organização", "manifesto", "organizations/organization/title", USADA, "Comparado com course.title (alerta se diferir)."),
    ("arquivos declarados e ausentes", "manifesto", "resources/resource/file@href contra a lista do zip", USADA, "Alerta se faltar algum."),
    ("itens da organização, recursos, metadados LOM, sequenciamento", "manifesto",
     "organizations/organization/item, resources/resource, metadata, sequencing", DISPONIVEL, "No Rise, um item e um recurso (scormdriver/indexAPI.html)."),
    # --- Zip
    ("nome, tamanho e SHA-256 do zip", "zip", "o arquivo .zip", USADA, "Identifica a versão do arquivo (dois zips com o mesmo SHA-256 são o mesmo pacote)."),
    ("lista de arquivos do zip", "zip", "entradas do zip (caminho, tamanho, SHA-256 de cada uma)", DISPONIVEL,
     "Não é útil para o relatório (decisão do usuário). Os nomes em scormcontent/lib/ têm hash e identificam o release do Rise."),
    ("variante do conteúdo", "zip", "scormcontent/runtime-data.js (export novo) ou scormcontent/index.html (export antigo)", USADA, "Mostra a geração do export."),
]
