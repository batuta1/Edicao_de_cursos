> Note que estamos na banch `structuring`, quando a implementação ficar estável movemos para a main;

# Planejamneto

Precisamos de um .py (ou um conjunto deles muito bem organizado) organizados dentro dessa pasta para serem capazes de via pyautogui ou semelhantes interagirem com a interface do Notion para atualizar o que está sendo desenvolvido.

desafios da automação:
- Essa aplicação não meche nas pastas `bagunca` e `Skills` que está na main;
- Precisamos "ficar movimentando" arquivos como `checklist-producao-de-cursos-60-dias-*.xlsx` da branch "joao" para a branch "main" como por exemplo para a pasta `<AutomacaoUpdate>\<referencias>` (que nem existe ainda, então pode ser outro nome... tanto `<AutomacaoUpdate>` quanto `<referencias>`...)
  - Note que o ideal é que seja escolhido arquivo `checklist-producao-de-cursos-60-dias-*.xlsx` mais recente, o último seja removido e que haja um commit automatizado somente para os arquivo envolvidos nesse processo, com uma mensagem simplificada do tipo "update de producao dos cursos" ou algo semelhante...
  - Precisamos de um script python que transforme esses arquivos `xlsx` para `csv` (separado por "," e simultaneamente tomando o cuidado para substituir "," que existam no `xlsx` por ";" )
  - o `csv` será o arquivo utilizado por scripts para:
    - preencher a informação de `Cursos\*\*\scorm\v*\autor.json`;
    - fazer o update das informações no notion;
- Seria muito bom ter uma ED (arquivo `.json`) listando todos os cursos; ORA, isso já existe em outro repositório e parece ser o momento ideial para integrar ao repo; 
  - para isso já anexei `_plan\extrator` que precisa ser renomeado, movido para a raiz do projeto e seus "caminhos" precisam ser corrigidos, se possível criar pasta `path` na pasta do `extrator` (ou nome que este passar assumir quando estiver na raiz do repo) e nele concetrar eventuais navegações;
  - no `_plan\extrator` é preciso fazer as correções, quando ele for executado:
    - este deve passar a retornar o arquivo `saida_extrator\ultimas_versoes.json` diretamente em `Cursos/<nome-do-arquivo>`, mas com novo nome algo como "registro-de-cursos.json" (mas aceito outras sugestões)
    - já o arquivo `saida_extrator\controle.json` e `saida_extrator\resumo.json` devem ficar dentro da pasta raiz do `extrator` (ou nome que este passar assumir quando estiver na raiz do repo);
- Na interface do Notion existe uma planilha com vários colunas dentre elas:
1. "Nome do curso"
2. "Status"
3. "Responsável"
4. "Progresso"
  - Isto posto, precisamos 
    - identificar na tela "1";
    - clica em "2" para alternar entre os estados ["Aguardando","Em produção","Concluído"];
    - "3" seleciona o responsável ["João", "Marina"];
    - "4" coloca um valor de porcentagem;

comece pegando o arquivo mais recente que se encaixe em `checklist-producao-de-cursos-60-dias-*.xlsx` e que esteja na branch "joao"