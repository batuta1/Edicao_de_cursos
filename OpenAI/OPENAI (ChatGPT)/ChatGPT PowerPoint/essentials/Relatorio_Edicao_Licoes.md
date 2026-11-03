# Relatório de Edição — ChatGPT PowerPoint (Essentials), trilha SCORM

Revisão feita em 7 de outubro de 2026 com a skill `revisar-curso-scorm`.

## Pacote

- Original: `chatgpt-powerpoint-essentials-scorm12-1FExiyZi.zip` (não foi modificado)
- Revisado: `chatgpt-powerpoint-essentials-scorm12-1FExiyZi-REVISADO.zip`
- Formato: default (`scormcontent/runtime-data.js`)
- Título no pacote: `ChatGPT PowerPoint - Essentials` (bate com o título esperado, usado como trava na extração)
- `course.id`: `IC7M1AupmWY_XkpWEa9_SyDSt6B12Ocv`
- 4 lições: `Decidindo e Instalando o ChatGPT no PowerPoint`, `Produzindo e Editando Apresentações com ChatGPT`,
  `Automatizando Fluxos e Aplicação Integrada`, `Quiz`.

## Material-fonte e mapeamento lição ↔ módulo

- Referência principal: `roteiros/roteiro-articulate-essentials.md` (Módulos 0 a 5 + Encerramento).
- Apoio: `roteiros/roteiro-essentials.md` e `ementa.md` (pasta `chatgpt-no-powerpoint`).
- O SCORM condensa os 6 módulos do roteiro em 3 lições de conteúdo + 1 quiz:

| Lição do SCORM | Módulos do roteiro |
|---|---|
| 1 — Decidindo e Instalando o ChatGPT no PowerPoint | Módulo 0 (Antes de instalar) + Módulo 1 (Instalar e reconhecer a ferramenta) |
| 2 — Produzindo e Editando Apresentações com ChatGPT | Módulo 2 (Criar a partir de material de origem) + Módulo 3 (Intervir em apresentação existente) |
| 3 — Automatizando Fluxos e Aplicação Integrada | Módulo 4 (Fluxos que se repetem) + Módulo 5 (Síntese) + Encerramento |
| 4 — Quiz | Avaliação final, sem correspondência direta a um módulo |

## Critério aplicado

Cada campo de texto foi comparado com o módulo correspondente do roteiro. Foram corrigidos os sintomas
típicos de curso gerado por IA: abertura genérica ("pode transformar o fluxo de trabalho"),
lead-in de objetivos diferente em cada lição, objetivos que não batiam com os do roteiro,
fechamentos motivacionais vazios, frases de enchimento no segundo parágrafo dos accordions
("Isso ajuda a ajustar o resultado sem perder informações importantes") e especificidade perdida
(créditos por mensagem, cota compartilhada com o Excel, desfechos do teste de permissão, caminho do
erro de SSO, exemplo de formulação de edição). Onde o roteiro tinha conteúdo sem bloco
correspondente no SCORM, o conteúdo foi trazido para dentro de um campo de texto já existente do
mesmo assunto. Nenhum bloco foi criado.

Fórmula de objetivos padronizada nas 3 lições: **"Ao final desta lição, você será capaz de:"**, com
os itens alinhados, na ordem, aos objetivos de aprendizagem do roteiro.

Método de edição: em vez da ferramenta Edit, as alterações foram aplicadas por caminho JSON com o
script `aplicar_edicoes.py` + `edicoes_essentials.py` (guardados nesta pasta como registro). O
script só aceita campos textuais, recusa mudar o tipo de valor ou criar chave, confere que o valor
atual ainda é o original e regrava o arquivo com a mesma formatação.

## Alterações lição a lição

### Lição 1 — Decidindo e Instalando o ChatGPT no PowerPoint (45 campos)

- **Abertura**: o parágrafo genérico ("é fundamental compreender os critérios de adoção...") foi
  trocado pelo fato central do Módulo 0: o suplemento roda dentro do PowerPoint, a Microsoft pode ter
  a capacidade de ler os arquivos e a OpenAI os processa, então o arquivo passa por duas empresas.
  Incluída a frase do roteiro de que concluir que o curso não se aplica é resultado legítimo.
- **Objetivos**: lead-in padronizado. Os 4 itens (antes telegráficos, como "Compreender consumo e
  limites do plano") passaram a reproduzir os objetivos do Módulo 0. O item 4 também cobre o objetivo
  do Módulo 1 de distinguir falha de instalação, de autenticação e de habilitação.
- **"Critérios de adoção"**: reescrito com o que faltava do roteiro: o sistema pode editar ou excluir
  conteúdo (duplicar é requisito), e as três perguntas institucionais (norma, declaração de uso,
  orientação aos alunos).
- **Flashcards**: versos com os dados completos (as 5 categorias vedadas, as condições de cada plano,
  instalação × habilitação).
- **Accordion de privacidade**: o item de consumo agora traz os 10 a 50 créditos por mensagem com
  GPT-5.5, a cota compartilhada com o ChatGPT para Excel, a recomendação de produzir o rascunho com
  antecedência e a data de consulta (7/10/2026).
- **Verificação de prontidão** (process): o passo "Testar permissão" agora traz os três desfechos e o
  que fazer em cada um, inclusive a saída do curso (curso irmão ChatGPT no Word), que estava
  ausente. O card de resumo virou o critério de êxito do roteiro.
- **Administração**: o primeiro bloco ganhou a explicação de que estar na loja não garante acesso
  (plano, administrador, permissões, liberação gradual). O segundo virou um quadro "quem controla o
  quê / quando recorrer".
- **Instalação** (process): o primeiro comando de teste ("Crie um slide de título com o texto
  'Teste'...") e a localização das Skills, que faltavam, foram incluídos no último passo. O resumo
  virou o ponto de controle do roteiro.
- **Solução de problemas**: o erro de SSO agora traz o caminho completo
  (`Portal de administração da OpenAI > Identidade > SSO > Gerenciar SSO`) e a orientação de transcrevê-lo
  no chamado. O item "não aceita a conta" ganhou a verificação da conta conectada no navegador.
- **Knowledge check**: ver "Pontos de atenção", item 1.
- **Fechamento**: o "Continue para descobrir como potencializar..." foi trocado pelo que a próxima
  lição faz e pelo que o participante deve ter à mão.

### Lição 2 — Produzindo e Editando Apresentações com ChatGPT (65 campos)

- **Abertura**: o parágrafo genérico foi trocado pelo do roteiro (rascunho a partir de material que
  já existe: artigo, capítulo, plano de ensino, anotações, planilha), com a virada para a
  intervenção em material pronto.
- **Objetivos**: lead-in padronizado e os 7 itens alinhados aos objetivos dos Módulos 2 e 3.
- **Quatro elementos**: retomado o conceito de que o material passa pelas duas empresas e de que a
  instrução deve declarar o que preservar. Os flashcards usam os exemplos do roteiro ("Doze slides",
  "Público: alunos de graduação, primeiro contato com o tema"). Antes, um exemplo era inventado, outro
  repetia a definição, e o texto dizia "Expanda cada cartão" para flashcards.
- **Tema institucional** (process): a introdução traz a limitação declarada pelo fabricante. O passo
  2 traz a frase de preservação completa do modelo de instrução. O resumo virou o ponto de controle,
  com o Modo de Exibição de Estrutura de Tópicos e a conferência de 3 dados.
- **Problemas na criação**: o título em inglês "Slide count diferente do pedido" foi corrigido. Os
  segundos parágrafos de enchimento viraram exemplos e procedimentos concretos.
- **Intervir em apresentação existente**: incluídas a formulação de referência do fabricante
  ("Adicione um slide de riscos após a visão geral do mercado...") e a recomendação de pedir um
  plano antes de edições extensas.
- **Seis informações**: o parágrafo prolixo sobre "comparação da aplicação das informações" foi
  reescrito, de forma objetiva, pela tabela do roteiro: quais das seis informações entram na criação
  e quais na edição.
- **Edição delimitada** (process): os exemplos das duas mensagens do modelo de edição foram incluídos
  nos passos, e o resumo virou o ponto de controle.
- **Knowledge check de resposta múltipla**: ver "Pontos de atenção", item 2.
- **Checklist de seis pontos**: a introdução agora traz o conteúdo de refinamento, que faltava:
  condensar, trocar de público e converter formato, e o risco de mudança de sentido ("sugere" que vira
  "demonstra"). Cada item do accordion abre com a pergunta do roteiro e termina com o procedimento de
  correção, no lugar das frases de enchimento.
- **Fechamento**: próximos passos concretos (critério de previsibilidade e atividade integradora).

### Lição 3 — Automatizando Fluxos e Aplicação Integrada (59 campos)

- **Abertura**: trocada pela família de apresentações que o docente refaz a cada semestre (aula
  inaugural, resultados ao departamento, seminário de projeto, defesa de orientandos).
- **Objetivos**: lead-in padronizado e os 5 itens alinhados aos Módulos 4 e 5.
- **Skills, apps, plugin e modelos**: definições conforme o roteiro. O modelo de apresentação aparece
  como o mecanismo mais acessível, que não depende de plano nem de administrador. Os flashcards
  incluem o acesso pelo símbolo @ e o aviso de que nem todo app aparece no PowerPoint.
- **Critérios e limitações**: a promessa vazia ("com poucos cliques, economizando tempo e evitando
  erros") foi removida. Incluídos os exemplos do gabarito do roteiro (relatório trimestral: vale; aula
  substituta: não vale) e o modelo de instrução repetível, que é o "Mão na massa" do Módulo 4 e não
  tinha bloco próprio.
- **Fluxo de uso de uma Skill** (process): os passos foram alinhados aos 4 passos do roteiro. O
  passo 4 misturava modelo de apresentação com modelo de instrução. O resumo virou "Sem Skills na
  conta?".
- **Knowledge check**: o enunciado dizia "Para cada situação abaixo" com uma situação só e foi
  reescrito. Os feedbacks foram refeitos; antes, um deles era "A tarefa é recorrente, então não
  escolher esta opção". Gabarito inalterado.
- **Ciclo integrado**: o texto genérico ("melhoria constante e revisão permanente") foi trocado pelo
  do Módulo 5: verificação como disposição permanente e decisão sobre o que submeter antes de tudo.
- **Quatro condições de bom uso**: os itens remetiam a "Módulos 2 e 3", "Módulo 5", que **não existem
  no SCORM** (o curso tem lições, não módulos). Foram trocados por referências às lições. A condição
  "preservação explícita" também falava, sem base no roteiro, em "proteger informações sensíveis".
- **Atividade integradora** (process): o resumo agora traz os critérios de avaliação do roteiro (os
  9 itens condensados) e o passo de consulta traz a pergunta das 5 perguntas prováveis.
- **Encerramento**: reescrito pelo Encerramento do roteiro (prática começando pelas apresentações de
  menor exposição, caminhos de aprofundamento, data de consulta). A síntese foi preservada sem
  alteração: "o sistema monta os slides; a apresentação continua sendo de quem sobe ao palco".

### Lição 4 — Quiz (0 campos)

Lido sem alteração. As 10 questões estão bem escritas e coerentes com o roteiro. Os gabaritos foram
conferidos um a um com `checar_gabaritos.py`: os campos `correct`/`corrects` apontam para ids
existentes e batem com os booleanos das alternativas.

## Contagem de campos alterados

Confirmada por `validar_estrutura.py`: **169 campos de texto** (L1 = 45, L2 = 65, L3 = 59, L4 = 0).
Por campo: description = 73, paragraph = 44, title = 31, heading = 13, feedback = 8. A contagem do
validador bate exatamente com a do script de edição, sem nenhuma alteração acidental.

## Validações

- `validar_estrutura.py`: **estrutura preservada em todas as lições**, sem nenhuma divergência estrutural.
  Mesmos ids, types, positions, settings, quantidade e ordem de blocos, itens e alternativas.
- `checar_html.py`: tags HTML balanceadas em todos os campos editados (0 problemas).
- `scorm_reempacotar.py`: round-trip do Base64 conferido. 83 arquivos no pacote, apenas
  `scormcontent/runtime-data.js` substituído e 0 arquivos alterados fora do alvo.
- **Teste em navegador** (LMS simulada com API SCORM 1.2): o curso carrega; a abertura e os objetivos
  da Lição 1 aparecem com o texto novo; o knowledge check de resposta múltipla da Lição 2 foi
  respondido de verdade: marcando as alternativas 5 e 9 (índices 4 e 8) → **Correct**; marcando 5 e
  6 → **Incorrect**.
- **Não verificado visualmente**: os demais blocos da Lição 1, a Lição 3 e o Quiz. Foram validados só
  de forma estrutural e de HTML.

## Pontos de atenção (exigem olho humano)

1. **Gabarito errado no knowledge check da Lição 1 — resolvido pelo enunciado, não pelo gabarito.**
   O original perguntava "Quem deve ser contatado se a loja de suplementos estiver bloqueada?" e
   marcava como correta "O administrador do espaço de trabalho do ChatGPT". Pelo roteiro (e pelo
   próprio texto da lição, quatro blocos acima), loja bloqueada é com **o administrador do Microsoft
   365**. A alternativa correta não foi alterada. O enunciado foi reescrito para o 4º desfecho do
   roteiro ("instalado, mas a conta não obtém acesso"), cenário em que a alternativa marcada é de fato
   a certa, e os 4 feedbacks foram refeitos de acordo. **Se preferir manter a pergunta original**,
   no Rise basta marcar "O administrador do Microsoft 365" como correta e reescrever os feedbacks.
2. **Knowledge check de resposta múltipla da Lição 2 estava quebrado no original.** Eram três
   perguntas empilhadas num bloco só, com "Pergunta 1/2/3" ocupando o lugar de alternativas e duas
   dessas "perguntas" marcadas como corretas. Foi reescrito como uma pergunta coerente ("selecione as
   duas afirmações corretas"), em que as duas corretas são exatamente as alternativas já marcadas (4 e
   8). Ids, ordem, quantidade e booleanos foram preservados, e os feedbacks gerais, que já descreviam
   essas duas afirmações, não precisaram mudar. Observações:
   - Os campos `correct`/`corrects` desse bloco guardam **textos** das antigas alternativas no lugar de
     ids (defeito de geração). Não foram alterados, porque não são campos de texto. O teste no
     navegador mostrou que a pontuação funciona pelos booleanos.
   - Pedagogicamente, o ideal no Rise seria desmembrar em três knowledge checks. Isso exige mudança
     estrutural, fora do escopo desta revisão.
3. **Quiz, lacuna "Automatizar só compensa quando a tarefa se repete em ____".** A única resposta
   aceita é "intervalos previsíveis", mas o curso nomeia o critério como "previsibilidade de
   calendário". Quem digitar "calendário previsível" será marcado como errado. Sugestão: no Rise,
   acrescentar respostas aceitas ("calendário previsível", "intervalo previsível"). Não foi alterado,
   porque respostas aceitas são dado de correção.
4. **Conteúdo do roteiro sem bloco no SCORM.** O curso gerado não tem blocos para os "Mão na massa" do
   roteiro: os dois modelos de mensagem às administrações, o prompt-base de reconhecimento, os modelos
   de criação, de edição em duas mensagens e de refinamento, e o prompt-base de fechamento. Também
   faltam a tabela de perguntas de consulta, a solução de problemas da edição (Módulo 3) e o exercício
   de 4 situações do Módulo 4 (o SCORM tem só a primeira). Parte disso foi trazida para campos
   existentes (exemplos nos passos dos processes, modelo de instrução repetível no accordion,
   refinamento na introdução do checklist). O resto exigiria **novos blocos no Rise**.
5. **Dados datados.** Créditos (10 a 50 por mensagem), modelo GPT-5.5, planos e cota compartilhada
   com o Excel correspondem à documentação consultada em 7/10/2026, como diz o roteiro. Confira antes
   de publicar.

## O que foi gerado

- `cursoChatGPTPPTEssentials.json`: payload desserializado original.
- `licoes_extraidas_ChatGPTPPTEssentials/licao_01…04_*.json`: lições separadas (01 a 03 editadas;
  04 lida sem alteração) + `indice_licoes.json`.
- `licoes_extraidas_ChatGPTPPTEssentials/edicoes_essentials.py`: registro de cada campo alterado
  (caminho JSON + texto novo).
- `cursoChatGPTPPTEssentials_editado.json`: curso fundido com as edições.
- `cursoChatGPTPPTEssentials_editado_base64.txt`: Base64 final (168.320 caracteres), com round-trip
  verificado.
- `chatgpt-powerpoint-essentials-scorm12-1FExiyZi-REVISADO.zip`: pacote reempacotado, entregue em
  `OpenAI/OPENAI (ChatGPT)/ChatGPT PowerPoint/essentials/` junto com a versão extraída
  `EssentialsChatGPT_PowerPointRevisado/`.
