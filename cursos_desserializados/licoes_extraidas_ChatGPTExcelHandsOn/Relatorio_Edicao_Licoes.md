# Relatório de alterações — Curso "ChatGPT no Excel e Google Sheets Para Leigos"

## Arquivos editados

- licao_01_Instalando_o_ChatGPT_Primeiros_Passos_no_Excel_e_Sheets.json
- licao_02_Criando_e_Atualizando_Planilhas_por_Conversa.json
- licao_03_Como_Escrever_Pedidos_Claros_e_Específicos_para_a_IA.json
- licao_04_Validando_Resultados_Checklist_de_Conferência_e_Segurança.json
- licao_05_Projeto_Final_Montando_um_Painel_de_Controle_com_IA.json
- licao_06_Dicas_Essenciais_para_Produtividade_e_Segurança_com_ChatGPT_em_Planilhas.json

(`indice_licoes.json` foi apenas lido, não alterado.)

## Alterações realizadas

### Lição 01 — Instalando o ChatGPT
- Parágrafo de abertura reescrito: trocou explicação genérica ("economiza tempo, evita vai-e-vem") pelo cenário concreto do roteiro original — copiar/colar entre janelas — que justifica a instalação.
- Parágrafo introdutório da lição tornado mais objetivo e ligado à ação real do aluno.
- Feedbacks das 4 alternativas do quiz reescritos para explicar o *porquê* de cada opção, em vez de apenas reafirmar "está correto/incorreto".
- Parágrafo de transição para a Lição 02 ajustado para antecipar concretamente o que vem a seguir.

### Lição 02 — Criando e Atualizando Planilhas por Conversa
- Título/parágrafo de abertura reescrito com o problema real do roteiro (montar lista de controle sem digitar cabeçalho).
- **Correção de imprecisão conceitual**: o item 1 da lista de tópicos e o parágrafo introdutório diziam "criar listas por comando de **voz**" — a interação do curso é por **texto** na barra lateral, não por voz. Corrigido para refletir a mecânica real da ferramenta.
- Feedbacks do quiz aprofundados, ligando cada alternativa errada a uma ação prática (ex.: "desfaça com Ctrl+Z e refaça o pedido").
- Parágrafo de transição para a Lição 03 tornado mais específico.

### Lição 03 — Como Escrever Pedidos Claros e Específicos
- Abertura reescrita usando o exemplo "organiza essa planilha pra mim" do roteiro original, que ilustra melhor o problema do pedido vago.
- Parágrafo introdutório reformulado para adiantar os "três ingredientes" (o quê, onde, formato) que estruturam a lição.
- Feedbacks do quiz reescritos para explicar o critério de avaliação (presença ou ausência dos três ingredientes) em cada alternativa.
- Transição para a Lição 04 conectada ao limite da lição atual (pedido bem escrito reduz erro, mas não substitui conferência).

### Lição 04 — Validando Resultados: Checklist de Conferência e Segurança
- Abertura reescrita com o cenário concreto do roteiro (alteração aceita sem conferir, número mudou sem pedido).
- Parágrafo introdutório reformulado para citar as ações práticas da lição (duplicar, checar, registrar).
- Feedbacks do quiz aprofundados, com ênfase nas três perguntas do checklist.
- Transição para a Lição 05 explicitando os quatro elementos que serão combinados no projeto final.

### Lição 05 — Projeto Final: Painel de Controle
- Abertura alinhada ao texto original do roteiro ("chegou a hora de juntar tudo"), reforçando que o aluno decide sozinho a ordem dos pedidos.
- Parágrafo introdutório simplificado.
- Feedbacks do quiz reescritos, retomando os quatro critérios de conclusão do projeto.
- Parágrafo de encerramento reescrito para reforçar o ciclo "pedir, conferir, ajustar, registrar" e anunciar a lição final.

### Lição 06 — Dicas Essenciais para Produtividade e Segurança
- Abertura reescrita para amarrar a lição como síntese das lições 1 a 5, em vez de repetir o texto genérico de "kit de sobrevivência".
- Parágrafo introdutório tornado mais direto.
- Feedbacks do quiz reescritos com foco na função prática do resumo de alterações (não é backup, não é obrigatório tecnicamente, é hábito de conferência).
- Parágrafo final de encerramento do curso alinhado ao fechamento do roteiro original ("Conseguiu! E agora?").

## Validação estrutural

- Nenhum `id` foi alterado.
- Nenhum `type` foi alterado.
- Nenhuma `position` foi alterada.
- Nenhum `globalBlockId`, `family`, `variant` ou `correct` foi alterado.
- Nenhum bloco foi adicionado ou removido.
- Nenhuma lição foi adicionada ou removida (6 lições antes e depois).
- Todos os 6 arquivos JSON validados com `ConvertFrom-Json` — sintaxe válida em UTF-8.
- Indentação e formatação original preservadas (edições feitas por substituição pontual de string, não reescrita de arquivo).

## Pontos de atenção (revisão humana recomendada)

1. **Lição 02 — erro conceitual corrigido**: o conteúdo original (título da lição, item 1 da lista de tópicos e parágrafo introdutório do bloco) mencionava "comando de voz", mas a mecânica real do curso é digitar o pedido na barra lateral de texto. Corrigi diretamente por ser um erro descritivo, não uma resposta de quiz — mas vale uma checagem humana rápida para confirmar que não há, em algum lugar do curso publicado (fora dos arquivos revisados), outra menção a "voz" que precise do mesmo ajuste.
2. Nenhuma resposta correta de `knowledgeCheck` foi alterada ou parece incorreta — as 6 questões (uma por lição) foram conferidas e todas têm a alternativa correta coerente com o conteúdo da lição.
3. Os textos de processo (`interactive-fullscreen` / `step`) e os prompts entre aspas/negrito foram mantidos como no roteiro original (verbatim), conforme instrução de não alterar comandos-modelo que o aluno deve reproduzir.
