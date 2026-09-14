# Relatório de alterações — Curso "Claude Desktop Hands-on"

## Arquivos editados

- licao_01_Instalando_e_Configurando_o_Claude_Desktop_com_Segurança.json
- licao_02_Explorando_Funcionalidades_Abas,_Projetos_e_Proteção_de_Dados.json
- licao_03_Prompts_Eficazes,_Revisão_de_Alterações_e_Fluxo_Completo_com_Claude.json

(`indice_licoes.json` foi apenas lido, não alterado.)

Não foi encontrado um roteiro-fonte separado para este curso em `Editar Cursos\` (diferente de outros cursos do projeto, como o de ChatGPT no Excel). Na ausência dele, o próprio conteúdo original dos JSONs foi usado como referência de intenção pedagógica, conforme a regra de fallback do prompt de edição.

## Alterações realizadas

### Lição 01 — Instalando e Configurando o Claude Desktop com Segurança

- Parágrafo de abertura reescrito: trocou a explicação genérica/motivacional ("primeiro passo para transformar teoria em prática", "ferramenta poderosa ao alcance das mãos") por um diferencial concreto — o app interage com arquivos locais, o navegador não — que já justifica o cuidado extra com segurança anunciado no título da lição.
- Bloco de destaque "Regra de ouro do curso" corrigido: o texto original mandava o aluno consultar a "seção 'Se travar' da oficina", mas essa seção não existe com esse nome na lição (o bloco de solução de problemas se chama "Solucionando Problemas Comuns de Instalação", e o curso chama suas unidades de "lições", não "oficina"). Ajustado para referenciar o nome real da seção.
- Introdução do processo guiado (`interactive-fullscreen`) tornada mais concreta: agora antecipa o número de etapas e avisa que o e-mail da conta Anthropic será pedido no meio do processo, em vez de uma frase genérica sobre "seguir cada etapa com atenção".
- Resumo do processo guiado reescrito para apontar diretamente para a seção de solução de problemas, em vez de uma frase de encerramento genérica.
- Passo "Baixar o instalador correto" aprofundado: conecta com a informação levantada no passo anterior (x64/ARM64/Apple Silicon/Intel) e nomeia a causa mais comum de erro nessa etapa (baixar o instalador incompatível com o processador).

### Lição 02 — Explorando Funcionalidades: Abas, Projetos e Proteção de Dados

- Parágrafo de abertura reescrito para encadear diretamente com a Lição 01 (a capacidade do Claude de acessar arquivos locais) e transformar o tema "proteção de dados" numa pergunta prática, em vez de afirmações genéricas sobre "produtividade e segurança".
- Descrição da aba Cowork aprofundada com dois exemplos concretos de uso (organizar uma pasta inteira, reunir informações de várias fontes), mantendo a estrutura de parágrafos original (incluindo o espaçador `<p></p>` já existente).
- As 4 alternativas de feedback do quiz (aba Code) reescritas para explicar o porquê de cada opção estar certa ou errada, em vez de apenas reafirmar a resposta — inclusive a opção sobre "configurações do app", que agora orienta o aluno a procurar um menu separado das três abas.
- Introdução da prática guiada (Chat/Code) ligada explicitamente à "regra de ouro" apresentada na Lição 01, reforçando a identidade do curso.
- Introdução e resumo do processo guiado de estruturação de projeto seguro reescritos: a introdução não presume mais que o aluno "já domina as abas" (afirmação forte demais após um único exercício) e o resumo agora nomeia concretamente o que README.md e .gitignore fizeram no exercício, propondo o padrão como hábito replicável em outros projetos.

### Lição 03 — Prompts Eficazes, Revisão de Alterações e Fluxo Completo com Claude

- Parágrafo de abertura reescrito: em vez de afirmações genéricas ("separa usuários frustrados de quem aproveita o poder da IA"), usa o par de prompts fraco/forte que a própria lição já ensina mais adiante (nos flashcards) como gancho concreto logo na abertura.
- Introdução do processo guiado de prompts reescrita para descrever especificamente as 4 etapas daquele bloco (em vez de repetir pela terceira vez o mesmo resumo geral da lição, já dito na abertura e na lista de tópicos).
- Resumo desse mesmo processo reescrito para reforçar a fórmula (contexto, tarefa, limite, formato) e conectar com o bloco seguinte, de revisão de alterações.
- As 3 alternativas incorretas do quiz reescritas para citar o trecho exato do prompt correspondente a cada elemento (contexto/tarefa/limite/formato) que falta em cada opção, no mesmo padrão de profundidade que a alternativa correta já tinha.
- Resumo do processo guiado de revisão/diff view reescrito para nomear o ciclo de trabalho (revisar → interromper → redirecionar) de forma mais concreta que "trabalha a seu favor, com segurança e eficiência".

## Campos textuais alterados

`paragraph`, `description` e `feedback` dentro de blocos `text`, `interactive` (incluindo `interactive-fullscreen` do tipo `intro`/`summary`/`step`) e `knowledgeCheck`. Nenhum `title` de lição, pergunta de quiz, alternativa, item de lista ou heading foi alterado.

## Validação estrutural

- Todos os 3 arquivos validados com `ConvertFrom-Json` (PowerShell) — JSON válido em UTF-8.
- `numero_da_licao`, `position_original`, `id` da lição, `position` e `type` conferidos e idênticos aos originais nos 3 arquivos.
- Contagem de blocos (`lesson.items`) idêntica à original: Lição 01 = 12, Lição 02 = 17, Lição 03 = 13.
- Contagem de `globalBlockId` idêntica à contagem de blocos em cada arquivo, todos únicos (nenhum bloco duplicado, adicionado ou removido).
- Os 8 valores `correct` (4 por quiz, um quiz por lição nas Lições 02 e 03) conferidos: mesma alternativa marcada como `true` em cada quiz, na mesma ordem e com o mesmo texto de alternativa — nenhuma resposta correta foi alterada.
- Nenhuma lição foi adicionada ou removida (3 lições antes e depois, mesmos IDs).
- Edições feitas por substituição pontual de string (Edit tool), não reescrita de arquivo — indentação e formatação original preservadas integralmente.

## Pontos de atenção

1. **Sem roteiro-fonte disponível**: diferente de outros cursos do projeto, não existe um roteiro/script original registrado para este curso em `Editar Cursos\`. As melhorias foram baseadas no próprio conteúdo e na coerência interna entre as 3 lições. Se existir um roteiro-fonte fora dessa pasta, vale revisar os textos reescritos contra ele.
2. **Lição 02 — exercício do `.gitignore`/`.env` (não alterado, apenas observação)**: o exercício cria um arquivo `.env` "sensível" e pede para o aluno perguntar ao Claude se ele consegue ver esse arquivo, implicitamente testando se o `.gitignore` "protege" o arquivo. Tecnicamente, `.gitignore` é uma convenção do Git (evita que o arquivo seja versionado/commitado) e não garante, por si só, que uma ferramenta de IA rodando localmente deixe de ler o arquivo — isso depende do Claude Desktop respeitar `.gitignore` como sinal de exclusão de acesso, o que não pude confirmar com certeza. O texto original já é cauteloso nesse ponto (pede para "observar a resposta" em vez de afirmar que o arquivo ficará invisível), então não alterei a mecânica do exercício — mas recomendo confirmar o comportamento real do produto antes de publicar, para garantir que a conclusão pedagógica do exercício continue correta.
3. Nenhuma resposta correta de `knowledgeCheck` estava incorreta — as 2 questões (Lições 02 e 03) foram conferidas e ambas têm a alternativa correta coerente com o conteúdo da lição.
4. Textos de comando/prompt entre aspas que o aluno deve reproduzir literalmente (ex.: os prompts de exemplo nos passos e nos flashcards da Lição 03) foram mantidos verbatim, sem alteração.

## Confirmação

A estrutura técnica dos 3 arquivos JSON foi integralmente preservada. Apenas campos textuais pedagógicos permitidos foram alterados, conforme as regras do prompt de edição.
