# ChatGPT no Excel e Google Sheets For Dummies — Versão 2.0
## Do Zero ao Modelo Automatizado

> **Nota de versão:** este roteiro é uma reconstrução completa da versão 1.0, incorporando todas as correções apontadas na auditoria crítica anterior: suporte visual em cada aula, troubleshooting sistemático, aprofundamento de engenharia de prompts, MCP, Codex avançado e Skills, checklist de validação de respostas da IA, comparação explícita Excel × Google Sheets, e um apêndice de governança corporativa (RBAC, EKM, residência de dados).

---

# Visão Geral do Curso

| Item | Descrição |
|---|---|
| **Título** | ChatGPT no Excel e Google Sheets For Dummies: Do Zero ao Modelo Automatizado — v2.0 |
| **Carga horária sugerida** | 9 a 11 horas |
| **Formato** | Curso prático, com pílulas Hands-on, checkpoints e projeto integrador |
| **Público-alvo** | Profissionais de negócios, analistas, contadores, servidores públicos, estudantes e qualquer pessoa que usa planilhas no dia a dia e quer eliminar tarefas repetitivas |
| **Pré-requisitos** | Conhecimento básico/intermediário de Excel ou Google Sheets. Nenhum conhecimento prévio em IA é necessário |
| **Fonte técnica de referência** | Documentação oficial da OpenAI para ChatGPT no Excel e Google Sheets (OpenAI Help Center) |

## Objetivos de Aprendizagem

Ao concluir este curso, o aluno será capaz de:

- Instalar e configurar corretamente o ChatGPT no Excel e no Google Sheets, inclusive em ambientes corporativos com restrições de TI.
- Usar linguagem natural para criar, atualizar, limpar e explicar planilhas.
- Escrever prompts eficientes, aplicando técnicas de engenharia de prompt específicas para dados tabulares.
- Automatizar tarefas recorrentes com Skills próprias e reaproveitar Skills padrão já inclusas.
- Conectar Apps e fontes de dados externas via MCP, entendendo os limites de segurança dessas conexões.
- Auditar e validar de forma estruturada qualquer alteração gerada por IA antes de confiar nela.
- Trabalhar com segurança, privacidade, governança e custos, inclusive em ambientes corporativos regulados.
- Diagnosticar e resolver os problemas mais comuns de instalação, permissão e uso.

## Estrutura Geral

| Módulo | Tema | Tempo estimado |
|---|---|---|
| 1 | Fundamentos | 90 min |
| 2 | Primeiros Usos | 80 min |
| 3 | Engenharia de Prompts | 90 min |
| 4 | Automação | 80 min |
| 5 | Auditoria | 70 min |
| 6 | Integrações | 80 min |
| 7 | Recursos Avançados e Governança | 90 min |
| 8 | Projeto Final | 60 min |
| Apêndices | Glossário e Troubleshooting de Referência Rápida | 20 min |

---

# Módulo 1 — Fundamentos

**Objetivo do módulo:** dar ao aluno uma base sólida sobre o que é a ferramenta, quem pode usá-la e como instalá-la corretamente em qualquer um dos dois ambientes, sem depender de tentativa e erro.

## Aula 1 — O que é o ChatGPT para Planilhas?

### 📸 Sugestão de Prints
- Captura da tela do Excel com a barra lateral do ChatGPT aberta à direita, com uma seta apontando para o ícone que a abre na faixa de opções (ribbon).
- Captura equivalente do Google Sheets, com o painel lateral aberto a partir do menu **Extensões**.
- Uma imagem lado a lado (split screen) comparando visualmente as duas barras laterais, destacando que a experiência é semelhante, mas não idêntica.
- Diagrama simples (caixa e seta) mostrando o fluxo: **Aluno digita um pedido → ChatGPT lê células/fórmulas/abas → ChatGPT responde ou propõe alteração → Aluno aprova**.

### Descrição

#### Objetivos da Aula
Explicar o que é o ChatGPT para Excel e Google Sheets, como ele se diferencia de simplesmente "copiar e colar dados no ChatGPT normal", e apresentar o conceito central: é um assistente que opera diretamente sobre a planilha aberta, lendo fórmulas, referências e abas.

#### Habilidades Esperadas
Ao final, o aluno deve conseguir explicar, com suas próprias palavras, a diferença entre usar o ChatGPT "por fora" (copiando e colando) e usar o suplemento nativo, e identificar visualmente a barra lateral em qualquer um dos dois programas.

### Conteúdo Programático
1. **O problema que a ferramenta resolve**: perda de tempo copiando dados para o ChatGPT e depois copiando o resultado de volta manualmente.
2. **O que é a barra lateral**: um painel de conversa que fica ao lado da planilha e enxerga o conteúdo das células, fórmulas e nomes das abas — sem que o aluno precise explicar o contexto a cada pergunta.
3. **Diferença entre Excel e Google Sheets**: são duas experiências separadas (não compartilham histórico de conversa), mas seguem os mesmos princípios de uso.
4. **Quando considerar o Codex com @Microsoft Excel** (introdução breve — aprofundado no Módulo 4): uma variante voltada a quem já usa o Codex e quer controlar diretamente uma pasta de trabalho aberta, com fluxo de permissões próprio.

> **💡 Dica profissional:** pense na barra lateral como um colega que já está olhando para a sua planilha — você não precisa descrever a estrutura dela, só precisa dizer o que quer.

### Pílula Hands-on
Abra uma planilha qualquer (pode ser em branco) no Excel ou no Google Sheets e, sem instalar nada ainda, localize onde a barra lateral do ChatGPT deveria aparecer (faixa de opções no Excel; menu Extensões no Sheets). Anote o caminho que você encontrou — você vai confirmar essa localização na Aula 3.

### Checkpoint
1. Qual é a principal diferença entre usar o ChatGPT "por fora" (copiando dados) e usar o suplemento nativo?
2. A barra lateral do Excel compartilha histórico de conversa com a barra lateral do Google Sheets?

---

## Aula 2 — Quem Pode Utilizar? Planos e Elegibilidade

### 📸 Sugestão de Prints
- Tabela oficial de planos renderizada como imagem (ou print da página de planos da OpenAI), com destaque em cores para os planos com acesso completo versus acesso limitado.
- Print da tela de configurações de uma conta ChatGPT Business/Enterprise mostrando onde o administrador habilita o recurso para usuários específicos.

### Descrição

#### Objetivos da Aula
Esclarecer, sem ambiguidade, quais planos dão acesso à ferramenta, quais têm uso limitado, e como funciona o controle administrativo em contas corporativas — evitando que o aluno tente instalar algo ao qual não tem direito.

#### Habilidades Esperadas
O aluno deve conseguir identificar, no seu próprio plano, se tem acesso completo, limitado, ou se depende de liberação de um administrador.

### Conteúdo Programático
1. **Planos com acesso**: Free, Go, Plus, Pro, Business, Enterprise, Edu e K-12 têm acesso global à ferramenta.
2. **Diferença de profundidade de uso**: Free e Go têm acesso limitado; Plus e Pro têm acesso sujeito ao limite de uso agêntico do plano; Business, Enterprise, Edu e K-12 seguem créditos e termos de uso próprios do plano corporativo.
3. **Controle administrativo**: em contas Enterprise, Edu e Teacher, o acesso vem **desligado por padrão** e precisa ser habilitado pelo administrador para usuários ou grupos específicos.
4. **Tabela comparativa de planos** (ver abaixo).

| Plano | Acesso ao suplemento | Nível de uso | Controle do administrador |
|---|---|---|---|
| Free / Go | Sim, limitado | Uso básico, sujeito a limites frequentes | Não aplicável |
| Plus / Pro | Sim | Sujeito ao limite de uso agêntico da conta | Não aplicável |
| Business / Enterprise / Edu / K-12 | Sim, via workspace | Créditos e termos do plano corporativo | Desligado por padrão; habilitado pelo admin por usuário/grupo |

> **⚠️ Cuidado com a Casca de Banana:** ter uma conta ChatGPT paga não significa automaticamente ter acesso ao suplemento em um ambiente corporativo. Se você não vê a opção de instalar, o primeiro passo é perguntar ao administrador de TI se o recurso está habilitado para o seu usuário.

### Pílula Hands-on
Verifique qual é o seu plano atual de ChatGPT e escreva uma frase resumindo se o seu acesso é completo, limitado, ou dependente de liberação administrativa — você vai precisar dessa informação nas próximas duas aulas.

### Checkpoint
1. Um usuário Enterprise, por padrão, já tem o suplemento habilitado?
2. Qual a diferença prática entre o acesso de um plano Free/Go e o de um plano Plus/Pro?

### Troubleshooting
| Erro comum | Causa provável | Solução |
|---|---|---|
| "Não encontro a opção de instalar o suplemento" | Conta corporativa com recurso desligado por padrão | Solicitar ao administrador de TI a habilitação via configurações do workspace |
| "Minhas respostas param no meio ou demoram muito" | Limite de uso agêntico do plano atingido | Aguardar renovação do limite ou verificar necessidade de upgrade de plano |

---

## Aula 3 — Instalando no Excel (Passo a Passo)

### 📸 Sugestão de Prints
- Print 1: tela inicial do Excel com o menu **Página Inicial** em destaque (círculo vermelho no botão "Suplementos"/"Add-ins").
- Print 2: janela do Microsoft Marketplace já aberta, com a barra de busca contendo o texto "ChatGPT" e o resultado oficial destacado com uma seta.
- Print 3: botão **Adicionar/Instalar** em destaque, com callout "clique aqui".
- Print 4: tela de login do ChatGPT dentro do Excel, mostrando o campo de e-mail preenchido (dado fictício) e o botão de continuar.
- Print 5: resultado final — barra lateral aberta e pronta para uso, com uma mensagem de boas-vindas do ChatGPT.
- Print extra (admin): tela do Microsoft 365 admin center em **Integrated apps → Deploy Add-in → Upload custom apps**, mostrando o upload do arquivo de manifesto XML.

### Descrição

#### Objetivos da Aula
Guiar o aluno, passo a passo e sem ambiguidade, pela instalação do suplemento no Excel — tanto no fluxo individual (Microsoft Marketplace) quanto no fluxo corporativo (implantação via administrador).

#### Habilidades Esperadas
Ao final, o aluno deve ser capaz de instalar o suplemento sozinho ou, caso esteja em ambiente corporativo restrito, saber exatamente o que pedir ao administrador de TI.

### Conteúdo Programático

**Fluxo individual:**
1. Abrir o Microsoft Excel (área de trabalho ou versão web).
2. Ir até **Página Inicial**.
3. Clicar em **Suplementos** (Add-ins).
4. Abrir o **Microsoft Marketplace**.
5. Buscar por "ChatGPT" e confirmar que é o suplemento oficial da OpenAI.
6. Clicar em **Adicionar/Instalar**.
7. Fazer login com a conta ChatGPT que possui o plano compatível (ver Aula 2).
8. Confirmar que a barra lateral abriu corretamente.

**Fluxo corporativo (para administradores):**
1. Baixar o arquivo de manifesto XML oficial (disponibilizado pela OpenAI).
2. No Microsoft 365 admin center, acessar **Integrated apps**.
3. Selecionar **Deploy Add-in**.
4. Escolher **Upload custom apps** e enviar o arquivo de manifesto.
5. Atribuir o suplemento aos usuários ou grupos apropriados.

> **🛡️ Boa prática:** se você é administrador, atribua o suplemento primeiro a um grupo piloto pequeno antes de liberar para toda a organização — isso permite validar políticas de segurança antes de uma adoção ampla.

### Pílula Hands-on
Instale o suplemento na sua própria conta seguindo os oito passos do fluxo individual. Ao final, abra a barra lateral e envie a mensagem "Olá, você consegue ver esta planilha?" e confira a resposta.

### Checkpoint
1. Em qual menu do Excel fica a opção "Suplementos"?
2. Qual é a diferença entre o fluxo de instalação individual e o fluxo de implantação corporativa via administrador?

### Troubleshooting
| Erro comum | Causa provável | Solução |
|---|---|---|
| O suplemento não aparece na busca do Marketplace | Conta Microsoft sem acesso à loja, ou restrição corporativa | Verificar com o administrador se a loja está bloqueada; usar o fluxo de manifesto XML |
| A barra lateral não abre após a instalação | Falha temporária de carregamento | Fechar e reabrir o Excel; verificar conexão de internet |
| Erro de login com a conta ChatGPT | Conta sem plano compatível, ou senha incorreta | Confirmar o plano na Aula 2; redefinir senha se necessário |
| "Suplemento instalado, mas administrador bloqueou o uso" | Política corporativa de RBAC ainda não habilitada para o usuário | Solicitar habilitação ao administrador (ver Aula 2) |

---

## Aula 4 — Instalando no Google Sheets (Passo a Passo)

### 📸 Sugestão de Prints
- Print 1: Google Sheets aberto, menu **Extensões** clicado, mostrando a opção **Complementos → Google Workspace Marketplace**.
- Print 2: página do Marketplace com "ChatGPT" buscado e o card oficial destacado.
- Print 3: botão **Instalar**, com a janela de permissões solicitadas pelo complemento visível.
- Print 4: complemento já instalado, acessado novamente pelo menu **Extensões**, com o painel lateral aberto.
- Print 5 (admin): tela de **Configurações do Workspace → Permissões e funções → ChatGPT for Excel and Google Sheets**, mostrando o botão de habilitação.

### Descrição

#### Objetivos da Aula
Replicar, para o Google Sheets, o mesmo nível de clareza da instalação no Excel, incluindo o fluxo de administrador via RBAC.

#### Habilidades Esperadas
O aluno deve conseguir instalar o complemento sozinho e entender o papel do RBAC (Controle de Acesso Baseado em Funções) na liberação do recurso em contas corporativas do Google Workspace.

### Conteúdo Programático
1. Abrir o Google Sheets.
2. Ir ao menu **Extensões**.
3. Acessar o **Google Workspace Marketplace**.
4. Buscar "ChatGPT" e instalar o complemento oficial.
5. Aceitar as permissões solicitadas (leitura e edição da planilha ativa).
6. Fazer login com a conta ChatGPT compatível.
7. Reabrir o painel pelo menu **Extensões** sempre que precisar.

**RBAC explicado em linguagem simples:** é o mecanismo que uma organização usa para decidir *quem*, dentro da empresa, pode usar determinado recurso. Mesmo que o complemento esteja instalado, um administrador pode restringir seu uso a certos cargos ou departamentos. Se estiver em uma conta corporativa, o caminho é **Configurações do Workspace → Permissões e funções → ChatGPT for Excel and Google Sheets → Habilitar**. Essa configuração vale tanto para o Excel quanto para o Google Sheets.

> **⚠️ Cuidado com a Casca de Banana:** aceitar as permissões do complemento não é o mesmo que ter uso liberado pela empresa. São duas camadas diferentes — a permissão técnica (você autoriza o complemento a ler a planilha) e a permissão administrativa (a empresa autoriza você a usar o complemento).

### Pílula Hands-on
Instale o complemento no Google Sheets seguindo os sete passos acima. Depois, compare mentalmente (ou por escrito) com o processo do Excel feito na Aula 3: quais passos foram parecidos? Quais foram diferentes?

### Checkpoint
1. Onde fica a opção para instalar complementos no Google Sheets?
2. O que é RBAC e por que ele pode impedir o uso do complemento mesmo depois de instalado?

### Troubleshooting
| Erro comum | Causa provável | Solução |
|---|---|---|
| Complemento não aparece após instalação | Sheets precisa ser recarregado | Atualizar a página do navegador |
| "Este complemento requer aprovação do administrador" | RBAC não habilitado para o usuário | Solicitar habilitação conforme processo descrito acima |
| Erro ao aceitar permissões | Conta Google gerenciada com políticas restritivas | Verificar com o administrador do Workspace se complementos de terceiros estão bloqueados |

---

## Aula 5 — Excel × Google Sheets: Entendendo as Diferenças

### 📸 Sugestão de Prints
- Imagem única em formato de tabela comparativa visual (duas colunas, ícones do Excel e do Sheets), destacando os pontos de divergência.

### Descrição

#### Objetivos da Aula
Consolidar, em um único ponto do curso, todas as diferenças relevantes entre as duas plataformas — evitando que o aluno precise juntar essa informação espalhada por várias aulas.

#### Habilidades Esperadas
O aluno deve conseguir decidir, diante de uma tarefa concreta, se há alguma limitação relevante de plataforma a considerar antes de começar.

### Conteúdo Programático

| Critério | Excel | Google Sheets |
|---|---|---|
| Canal de instalação | Microsoft Marketplace / manifesto XML corporativo | Google Workspace Marketplace |
| Controle corporativo | Microsoft 365 admin center (Integrated apps) | RBAC via Configurações do Workspace |
| Suporte a macros/VBA | Parcial — pode não funcionar completamente | Não aplicável (Google Apps Script segue lógica própria, também com suporte parcial) |
| Histórico de conversa | Próprio do suplemento, sem sincronizar com o ChatGPT principal | Próprio do complemento, sem sincronizar com o ChatGPT principal |
| Uso do Codex dedicado (@Microsoft Excel) | Disponível como modo avançado | Não aplicável |
| Trabalho com arquivos grandes/múltiplas abas | Suportado, com atenção a desempenho | Suportado, com atenção a desempenho |

> **💡 Dica profissional:** se a sua organização usa as duas ferramentas, trate cada uma como um ambiente de conversa independente — não espere que o ChatGPT "lembre" o que foi decidido no outro programa.

### Pílula Hands-on
Com base na tabela acima, escreva duas frases: uma descrevendo uma tarefa para a qual você usaria o Excel, e outra para a qual usaria o Google Sheets, justificando com pelo menos um critério da tabela.

### Checkpoint
1. O histórico de conversa é compartilhado entre Excel e Google Sheets?
2. Cite uma limitação que as duas plataformas têm em comum.

---

# Módulo 2 — Primeiros Usos

**Objetivo do módulo:** transformar o aluno de "instalador" em "usuário produtivo", ensinando o uso conversacional básico com exemplos completos, incluindo pesquisa na web.

## Aula 1 — Conversando com a Planilha pela Primeira Vez

### 📸 Sugestão de Prints
- Print de uma planilha vazia com o prompt "Crie uma lista de controle de despesas mensais com categorias e total" digitado na barra lateral.
- Print do resultado gerado, com uma seta indicando as células que foram preenchidas automaticamente.
- Print de um prompt de atualização ("Adicione uma coluna de data") e o resultado comparado lado a lado (antes/depois).

### Descrição

#### Objetivos da Aula
Demonstrar, com um exemplo completo do início ao fim, como pedir a criação e a atualização de uma planilha usando linguagem natural.

#### Habilidades Esperadas
O aluno deve ser capaz de criar uma planilha simples do zero e pedir uma alteração incremental sobre ela, observando exatamente o que mudou.

### Conteúdo Programático
1. **Criar planilhas do zero**: pedir estrutura, categorias e formatação em uma única instrução.
2. **Atualizar modelos existentes**: pedir alterações específicas sem reescrever tudo.
3. **Explicar fórmulas**: pedir que o ChatGPT descreva o que uma fórmula complexa faz, célula por célula.
4. **Resumir alterações**: pedir um resumo do que foi modificado após uma edição, para facilitar a revisão.

> **📌 Boa prática:** depois de qualquer edição, peça "resuma exatamente o que você alterou" antes de continuar — isso cria o hábito de revisão que será formalizado no Módulo 5 (Auditoria).

### Pílula Hands-on
Peça ao ChatGPT para criar uma lista de controle de despesas mensais com categorias, valores e total. Em seguida, peça para adicionar uma coluna de data. Observe e anote apenas o que mudou entre as duas versões.

### Checkpoint
1. Que tipo de instrução é mais eficaz para atualizar uma planilha sem afetar o que já existe?
2. Por que pedir um resumo das alterações é uma boa prática?

---

## Aula 2 — Limpeza e Organização de Dados com IA

### 📸 Sugestão de Prints
- Print de uma planilha "suja" (dados desalinhados, duplicados, formatos inconsistentes) antes da limpeza.
- Print da mesma planilha depois de um prompt de limpeza, com destaque nas linhas removidas (duplicatas) e nas células padronizadas.

### Descrição

#### Objetivos da Aula
Ensinar o uso do ChatGPT para tarefas de limpeza de dados — um dos casos de uso oficiais mais comuns da ferramenta.

#### Habilidades Esperadas
O aluno deve saber pedir padronização de formatação, correção de rótulos inconsistentes e remoção de duplicatas, sempre revisando o resultado antes de aceitar.

### Conteúdo Programático
1. Padronização de formatação (datas, moeda, texto).
2. Correção de rótulos inconsistentes (ex.: "SP", "São Paulo", "sao paulo" tratados como o mesmo valor).
3. Remoção de linhas duplicadas.
4. Correção de fórmulas quebradas.

> **⚠️ Cuidado com a Casca de Banana:** limpeza de dados pode remover informações que pareciam duplicadas mas não eram (ex.: dois clientes com o mesmo nome). Sempre peça para o ChatGPT explicar o critério usado antes de aceitar a remoção.

### Pílula Hands-on
Pegue uma planilha real com pelo menos uma inconsistência de formatação (ou baixe um exemplo simples) e peça: "Limpe esta planilha: padronize formatação, corrija rótulos inconsistentes e remova duplicatas. Antes de aplicar, me diga o que você vai fazer."

### Checkpoint
1. Por que é importante pedir o critério usado antes de aceitar uma remoção de duplicatas?
2. Cite dois tipos de inconsistência que a IA pode corrigir automaticamente.

---

## Aula 3 — Pesquisando na Internet sem Sair da Planilha

### 📸 Sugestão de Prints
- Print do prompt "Busque a cotação atual do dólar e insira na célula B2" sendo digitado na barra lateral.
- Print do resultado, com a célula B2 preenchida e uma citação/fonte indicada pelo ChatGPT.

### Descrição

#### Objetivos da Aula
Ensinar como e quando usar a pesquisa na web integrada, incluindo a responsabilidade de verificar a fonte antes de usar o dado em decisões importantes.

#### Habilidades Esperadas
O aluno deve saber formular um pedido de pesquisa web aplicado a uma célula específica e verificar a fonte citada.

### Conteúdo Programático
1. Como pedir uma pesquisa: ser específico sobre o dado desejado e onde ele deve ser inserido.
2. Exemplos de uso: cotações, indicadores públicos, dados de referência de mercado.
3. **Verificação de fonte**: sempre conferir a origem da informação antes de usá-la em um relatório ou decisão relevante.

**Exemplo de prompt:** *"Busque a cotação atual do dólar (USD/BRL) e insira o valor na célula B2, com a data da consulta na célula C2."*

> **⚠️ Cuidado com a Casca de Banana:** informação buscada na web pode estar desatualizada no momento em que você lê o resultado, especialmente para dados que mudam a cada minuto (cotações, índices). Para decisões financeiras críticas, confirme em uma fonte oficial antes de agir.

### Pílula Hands-on
Peça uma pesquisa de um dado público qualquer (por exemplo, a cotação do dólar) para ser inserido em uma célula específica, com a data da consulta em outra célula. Verifique a fonte citada pelo ChatGPT.

### Checkpoint
1. Por que é importante pedir a data da consulta junto com o dado pesquisado?
2. O que fazer antes de usar um dado buscado na web em uma decisão importante?

---

## Aula 4 — Explicando e Entendendo Planilhas Alheias

### 📸 Sugestão de Prints
- Print de uma planilha complexa (múltiplas abas) recebida de terceiros, com o prompt "Explique as premissas e a lógica desta pasta de trabalho" na barra lateral.
- Print da resposta do ChatGPT organizada por aba, destacando premissas-chave.

### Descrição

#### Objetivos da Aula
Ensinar o uso do ChatGPT para entender rapidamente uma planilha desconhecida — um dos casos de uso oficiais mais valiosos para quem herda modelos de outras pessoas.

#### Habilidades Esperadas
O aluno deve conseguir pedir uma explicação estruturada (premissas, direcionadores, fórmulas-chave) de uma planilha que nunca viu antes.

### Conteúdo Programático
1. Pedir um resumo geral da estrutura (quantas abas, o que cada uma representa).
2. Pedir a identificação de premissas e direcionadores (*drivers*) do modelo.
3. Pedir a explicação de fórmulas específicas suspeitas ou complexas.
4. Pedir um resumo de tendências ao comparar múltiplas abas.

### Pílula Hands-on
Abra uma planilha que você não construiu (de um colega, de um modelo público, ou uma das planilhas já usadas nas aulas anteriores) e peça: "Explique a estrutura desta planilha, as premissas usadas e aponte qualquer coisa que pareça incomum."

### Checkpoint
1. Que tipo de pergunta ajuda a entender rapidamente uma planilha desconhecida?
2. Por que pedir para a IA apontar "algo incomum" é uma boa prática ao herdar um modelo?

---

# Módulo 3 — Engenharia de Prompts

**Objetivo do módulo:** transformar o aluno em um usuário autônomo na escrita de prompts, saindo de instruções genéricas para instruções precisas e reutilizáveis.

## Aula 1 — Anatomia de um Prompt Eficaz

### 📸 Sugestão de Prints
- Imagem comparativa (antes/depois) de dois prompts lado a lado — um vago e um reescrito com critérios claros — com anotações coloridas explicando cada melhoria.

### Descrição

#### Objetivos da Aula
Ensinar, de forma acionável e não apenas conceitual, os elementos que compõem um prompt eficaz para planilhas.

#### Habilidades Esperadas
O aluno deve conseguir reescrever um prompt vago em um prompt específico, aplicando pelo menos três dos critérios ensinados.

### Conteúdo Programático

Um prompt eficaz em contexto de planilha normalmente define:
1. **O que preservar** (formatação, fórmulas existentes, abas não relacionadas).
2. **O que alterar** (o alvo exato da mudança).
3. **Onde** (uso do símbolo **@** para focar em uma aba ou intervalo específico).
4. **O formato de saída esperado** (uma tabela, um resumo, um novo aba).
5. **Se deve pedir um plano antes de agir**, quando a mudança for grande.

**Exemplo comentado — Prompt fraco:**
> "Arruma essa planilha pra mim."

**Por que é fraco:** não diz o que "arrumar" significa, não delimita o escopo, não define o que deve ser preservado.

**Exemplo comentado — Prompt reescrito:**
> "Na aba @Vendas, padronize o formato de data para DD/MM/AAAA e remova linhas duplicadas pela coluna 'ID do Pedido'. Não altere a formatação de cores nem as fórmulas da coluna Total. Antes de aplicar, me diga quantas linhas serão removidas."

**Por que é forte:** define escopo (aba específica via @), a ação exata, o que preservar, e pede confirmação antes de agir.

**Segundo exemplo — Prompt fraco:**
> "Faz um resumo dos dados."

**Prompt reescrito:**
> "Resuma, em até 5 marcadores, as principais tendências de vendas por região na aba @Q3, destacando qualquer região com queda superior a 10% em relação ao trimestre anterior."

> **💡 Dica profissional:** para mudanças grandes, sempre peça primeiro: *"Antes de editar, liste exatamente quais abas e intervalos você vai modificar."* Isso transforma a IA de "executora" em "planejadora que aguarda aprovação".

### Pílula Hands-on
Pegue um prompt vago que você mesmo escreveria naturalmente (ex.: "melhora essa tabela") e reescreva-o aplicando pelo menos três dos cinco critérios acima. Execute as duas versões e compare os resultados.

### Checkpoint
1. Quais são os cinco elementos de um prompt eficaz apresentados nesta aula?
2. Por que pedir "um plano antes de agir" é especialmente importante em planilhas grandes?

---

## Aula 2 — Biblioteca de Prompts por Caso de Uso

### 📸 Sugestão de Prints
- Print de um "cartão de prompt" visual, com o texto do prompt em destaque e o resultado esperado ilustrado ao lado.

### Descrição

#### Objetivos da Aula
Entregar ao aluno uma biblioteca de referência rápida de prompts testados, organizados por situação, para reduzir a fricção de "não saber o que perguntar".

#### Habilidades Esperadas
O aluno deve conseguir localizar rapidamente um prompt adequado à sua necessidade e adaptá-lo ao seu próprio contexto.

### Conteúdo Programático

| Situação | Prompt de referência |
|---|---|
| Criar orçamento mensal | "Crie um orçamento mensal formatado com categorias, totais e gráficos." |
| Localizar erro em uma célula | "Por que a célula B145 está retornando erro? Explique a cadeia de fórmulas e proponha uma correção." |
| Resumir múltiplas abas | "Resuma as tendências das abas @Jan, @Fev e @Mar e aponte qualquer coisa incomum." |
| Remover duplicatas | "Remova linhas duplicadas com base na coluna 'ID' e me diga quantas foram removidas." |
| Atualizar premissas | "Atualize as premissas da aba @Inputs para refletir a nova taxa de 5,5% e resuma exatamente o que mudou." |
| Criar cenários | "Crie uma nova aba comparando os cenários Base, Otimista e Pessimista com base nas premissas da aba @Inputs." |
| Auditar uma pasta de trabalho | "Explique todas as fórmulas importantes desta pasta de trabalho e mostre quais células seriam alteradas antes de qualquer edição." |
| Pesquisar dado externo | "Busque [dado específico] e insira na célula [X], com a data da consulta na célula [Y]." |

> **📌 Boa prática:** trate esta tabela como ponto de partida, não como fórmula fixa — sempre adapte com os critérios da Aula 1 (o que preservar, onde, formato de saída).

### Pílula Hands-on
Escolha três prompts da tabela, adapte-os para uma planilha real sua e execute-os. Anote qual adaptação foi necessária em cada caso.

### Checkpoint
1. Cite dois prompts da biblioteca que poderiam ser combinados em uma única tarefa.
2. Por que os prompts da tabela são chamados de "ponto de partida" e não de "fórmula fixa"?

---

## Aula 3 — Prompts Avançados: Iteração e Refinamento

### 📸 Sugestão de Prints
- Sequência de três prints mostrando a evolução de um mesmo pedido ao longo de três rodadas de refinamento (v1 → v2 → v3), com o resultado ficando mais próximo do desejado a cada rodada.

### Descrição

#### Objetivos da Aula
Ensinar que a interação ideal raramente é um único prompt perfeito, e sim um processo de refinamento iterativo.

#### Habilidades Esperadas
O aluno deve conseguir conduzir uma conversa de múltiplas rodadas, corrigindo o rumo sem precisar recomeçar do zero.

### Conteúdo Programático
1. **Primeira rodada**: pedido inicial, propositalmente mais simples.
2. **Avaliação do resultado**: o que está certo, o que falta, o que está errado.
3. **Refinamento**: instruções curtas e específicas sobre o que ajustar ("mantenha tudo, só troque a cor dos totais para verde").
4. **Quando recomeçar do zero**: se o resultado se afastou muito do objetivo, é mais eficiente reiniciar com um prompt mais completo do que insistir em pequenos ajustes.

> **💡 Dica profissional:** ao refinar, diga explicitamente o que **manter** — sem essa instrução, cada nova rodada corre o risco de desfazer acertos da rodada anterior.

### Pílula Hands-on
Peça a criação de um dashboard simples de vendas em uma única instrução ampla. Depois, refine em pelo menos duas rodadas, ajustando um aspecto por vez (ex.: cores, depois formato dos números).

### Checkpoint
1. Quando faz mais sentido recomeçar do zero em vez de continuar refinando?
2. Por que é importante dizer explicitamente o que deve ser mantido durante o refinamento?

---

# Módulo 4 — Automação

**Objetivo do módulo:** ensinar Skills, Skills padrão já inclusas, criação de Skills próprias e o uso avançado do Codex com @Microsoft Excel.

## Aula 1 — O que são Skills?

### 📸 Sugestão de Prints
- Print do botão **+** na barra lateral, com o menu de Skills aberto, mostrando as Skills padrão já disponíveis (modelagem financeira, formatação corporativa).
- Print de uma Skill sendo invocada com **@** dentro de um prompt.

### Descrição

#### Objetivos da Aula
Explicar o conceito de Skill como playbook reutilizável e apresentar as Skills padrão já inclusas na ferramenta — um ponto ausente na versão anterior do curso.

#### Habilidades Esperadas
O aluno deve saber abrir o menu de Skills, identificar as Skills padrão disponíveis e invocar uma Skill em um prompt usando @.

### Conteúdo Programático
1. **Definição simples**: uma Skill é como salvar uma receita pronta — você não precisa reescrever o mesmo prompt detalhado toda vez.
2. **Skills padrão inclusas**: a ferramenta já vem com Skills para modelagem financeira e formatação corporativa, prontas para uso imediato.
3. **Como acessar**: botão **+** na barra lateral, ou comando **@** dentro do prompt.
4. **Quando usar uma Skill em vez de escrever um prompt do zero**: quando a mesma tarefa se repete com frequência (ex.: sempre formatar relatórios no mesmo padrão da empresa).

### Pílula Hands-on
Abra o menu de Skills pelo botão + e identifique quais Skills padrão estão disponíveis na sua conta. Invoque uma delas com @ em um prompt relacionado a uma planilha sua.

### Checkpoint
1. O que diferencia uma Skill de um prompt comum?
2. Cite as duas categorias de Skills padrão mencionadas nesta aula.

---

## Aula 2 — Criando sua Própria Skill

### 📸 Sugestão de Prints
- Sequência de três prints mostrando o fluxo completo de criação de uma Skill: nomear, descrever o comportamento esperado, salvar.
- Print da Skill recém-criada aparecendo na lista, ao lado das Skills padrão.

### Descrição

#### Objetivos da Aula
Fechar a lacuna identificada na auditoria anterior: ensinar, passo a passo, como transformar uma tarefa repetitiva em uma Skill reutilizável.

#### Habilidades Esperadas
O aluno deve ser capaz de criar do zero uma Skill simples baseada em uma tarefa real do seu trabalho.

### Conteúdo Programático
1. Identificar uma tarefa que se repete (ex.: sempre formatar um relatório semanal do mesmo jeito).
2. Descrever o comportamento desejado de forma clara, como se estivesse treinando um novo colega de equipe.
3. Salvar a Skill com um nome claro e reutilizável.
4. Testar a Skill em um caso real e ajustar a descrição se o resultado não for o esperado.

> **📌 Boa prática:** comece com Skills simples e de escopo único. Skills que tentam fazer "tudo de uma vez" são mais difíceis de manter e de confiar.

### Pílula Hands-on
Escolha uma tarefa repetitiva do seu próprio trabalho (por exemplo, um relatório semanal) e crie uma Skill para ela, seguindo os quatro passos acima. Teste-a em uma planilha real.

### Checkpoint
1. Por que é recomendável começar com Skills de escopo único?
2. Que tipo de tarefa é um bom candidato a virar uma Skill?

---

## Aula 3 — Codex Avançado com @Microsoft Excel

### 📸 Sugestão de Prints
- Print mostrando a invocação do Codex com @Microsoft Excel dentro de uma conversa, com a pasta de trabalho ativa sendo referenciada.
- Diagrama comparando o fluxo padrão do suplemento com o fluxo do Codex (destacando as diferenças de permissão e controle).

### Descrição

#### Objetivos da Aula
Aprofundar um recurso que na versão anterior do curso era citado em uma única frase: quando e como usar o Codex para controlar diretamente uma pasta de trabalho aberta.

#### Habilidades Esperadas
O aluno avançado deve entender a diferença entre o suplemento padrão e o modo Codex, e saber decidir qual usar em cada situação.

### Conteúdo Programático
1. **O que é**: um modo que permite ao Codex operar diretamente sobre uma pasta de trabalho do Excel já aberta, útil para fluxos que combinam código e planilha.
2. **Diferenças de permissão**: o Codex pode exigir confirmações adicionais e opera sob um fluxo de controle próprio, distinto do suplemento padrão.
3. **Quando preferir o Codex**: cenários que já envolvem automação por código (scripts, pipelines) e que precisam interagir com a pasta de trabalho de forma mais programática.
4. **Quando preferir o suplemento padrão**: uso conversacional do dia a dia, sem necessidade de integração com código.

> **⚠️ Cuidado com a Casca de Banana:** o modo Codex é voltado a usuários avançados. Se você ainda não está confortável revisando alterações geradas pelo suplemento padrão, não é o momento de adotar o Codex.

### Pílula Hands-on
Se você tiver acesso ao Codex, abra uma pasta de trabalho simples e peça uma alteração pequena e reversível, comparando a experiência com o uso do suplemento padrão nas aulas anteriores. Caso não tenha acesso, escreva um parágrafo descrevendo em qual cenário do seu trabalho o Codex faria sentido.

### Checkpoint
1. Qual é a principal diferença entre o suplemento padrão e o modo Codex?
2. Em que tipo de cenário o Codex é preferível ao suplemento padrão?

---

# Módulo 5 — Auditoria

**Objetivo do módulo:** transformar "revisar sempre" em um processo estruturado e repetível de validação.

## Aula 1 — Rastreamento de Fórmulas e Transparência

### 📸 Sugestão de Prints
- Print de uma resposta do ChatGPT explicando uma fórmula célula por célula, com links de referência às células citadas destacados.
- Print de uma confirmação pedida antes de uma alteração ser aplicada ("Você quer que eu aplique esta mudança?").

### Descrição

#### Objetivos da Aula
Mostrar como o ChatGPT explica sua própria lógica e como usar isso para rastrear alterações antes de aceitá-las.

#### Habilidades Esperadas
O aluno deve saber pedir explicações de fórmulas e exigir confirmação antes de qualquer alteração relevante.

### Conteúdo Programático
1. Pedir a explicação da lógica de uma fórmula complexa.
2. Usar links/referências de célula citados na resposta para conferir a origem dos dados.
3. Exigir confirmação explícita antes de qualquer alteração ("não aplique ainda, apenas explique o que faria").

### Pílula Hands-on
Escolha uma fórmula complexa em uma planilha sua e peça: "Explique esta fórmula célula por célula e me diga quais outras células ela referencia."

### Checkpoint
1. Por que é útil pedir para a IA citar as células que ela está referenciando?
2. Que instrução você pode usar para garantir que uma alteração não seja aplicada sem sua aprovação?

---

## Aula 2 — Checklist de Validação de Respostas da IA

### 📸 Sugestão de Prints
- Imagem de um checklist visual (caixas de marcação) sobreposto a uma planilha, ilustrando cada etapa da verificação.

### Descrição

#### Objetivos da Aula
Fechar uma das lacunas mais importantes identificadas na auditoria anterior: transformar "revise sempre" em um processo concreto e repetível.

#### Habilidades Esperadas
O aluno deve aplicar um checklist estruturado sempre que receber uma alteração gerada por IA, antes de compartilhar ou tomar decisões com base nela.

### Conteúdo Programático

**Checklist de Validação (referência para uso em qualquer módulo):**
1. ☐ A fórmula faz sentido matematicamente? Confira com um cálculo manual de amostra.
2. ☐ As células de origem citadas realmente contêm os dados esperados?
3. ☐ As unidades estão corretas (ex.: valores em milhares vs. unidades, percentual vs. decimal)?
4. ☐ A formatação e as fórmulas que deveriam ser preservadas continuam intactas?
5. ☐ O resumo de alterações fornecido pela IA corresponde ao que você realmente pediu?
6. ☐ Em caso de dúvida, foi feita uma cópia do arquivo original antes da edição?

> **🛡️ Cuidado com a segurança:** o ChatGPT para Excel e Google Sheets não é um consultor financeiro, jurídico ou tributário — qualquer saída relacionada a esses temas deve ser tratada como rascunho a ser validado por um profissional habilitado, nunca como aconselhamento definitivo.

### Pílula Hands-on
Aplique o checklist completo a uma alteração gerada por IA em qualquer planilha das aulas anteriores. Marque cada item e registre se algum ponto falhou.

### Checkpoint
1. Quais dos seis itens do checklist você aplicaria primeiro, e por quê?
2. Por que verificar "unidades" é um item separado de verificar "a fórmula está certa"?

---

## Aula 3 — Revisão de Alterações e Controle de Versões

### 📸 Sugestão de Prints
- Print comparando duas versões de uma planilha lado a lado (antes/depois), com as células alteradas destacadas em amarelo.
- Print do histórico de versões do Excel/Sheets sendo usado para reverter uma alteração.

### Descrição

#### Objetivos da Aula
Ensinar boas práticas de controle de versão específicas para o contexto de edição assistida por IA.

#### Habilidades Esperadas
O aluno deve saber duplicar um arquivo antes de uma edição importante e usar o histórico de versões nativo do Excel/Sheets para reverter alterações indesejadas.

### Conteúdo Programático
1. **Duplicar antes de editar**: sempre que a alteração for grande ou o arquivo for crítico, criar uma cópia antes de pedir a edição.
2. **Nomear versões de forma clara** (ex.: "orcamento_v2_revisado_IA").
3. **Usar o histórico de versões nativo** do Excel (OneDrive/SharePoint) ou do Google Sheets para reverter, se necessário.
4. **Comunicar alterações geradas por IA à equipe**, especialmente em arquivos compartilhados.

### Pílula Hands-on
Duplique um arquivo importante, peça uma edição de médio porte na cópia, e pratique reverter a alteração usando o histórico de versões nativo do programa.

### Checkpoint
1. Por que duplicar o arquivo antes de uma edição importante é uma prática recomendada?
2. Onde fica o histórico de versões nativo do Excel/Google Sheets, e como ele complementa (mas não substitui) o checklist de validação?

---

# Módulo 6 — Integrações

**Objetivo do módulo:** aprofundar Apps, MCP e integrações de dados financeiros, incluindo as regras de segurança específicas de cada uma.

## Aula 1 — Apps: Conceito e Uso

### 📸 Sugestão de Prints
- Print do menu de Apps aberto na barra lateral, mostrando os Apps disponíveis na conta do usuário.
- Print de um App sendo usado dentro de um prompt para trazer dados de uma fonte conectada.

### Descrição

#### Objetivos da Aula
Explicar Apps como conexões autorizadas entre o ChatGPT e outras fontes de dados, e como sua disponibilidade depende de plano, permissões e configurações do administrador.

#### Habilidades Esperadas
O aluno deve saber abrir o menu de Apps, verificar quais estão disponíveis e entender por que um App específico pode não aparecer.

### Conteúdo Programático
1. **Definição**: um App conecta o ChatGPT a uma fonte de dados autorizada (arquivos, bancos de dados, sistemas internos).
2. **Disponibilidade condicional**: um App só aparece se (a) o plano do usuário permite, (b) o usuário tem permissão individual, e (c) o administrador do workspace habilitou aquele App especificamente.
3. **Como verificar**: se um App esperado não aparece, o primeiro passo é confirmar com o administrador se ele está habilitado.

> **⚠️ Cuidado com a Casca de Banana:** a ausência de um App na lista quase nunca é um bug — na grande maioria dos casos, é uma configuração de permissão que precisa ser ajustada por um administrador.

### Pílula Hands-on
Abra o menu de Apps e liste quais estão disponíveis na sua conta. Se algum App esperado não aparecer, escreva a pergunta exata que você faria ao administrador para investigar.

### Checkpoint
1. Quais três fatores determinam se um App aparece disponível para um usuário?
2. O que fazer se um App esperado não estiver na lista?

---

## Aula 2 — MCP na Prática

### 📸 Sugestão de Prints
- Diagrama simples mostrando o fluxo: **Planilha ↔ ChatGPT ↔ Servidor MCP ↔ Sistema/dado externo**, com um cadeado ilustrando o controle de permissão.
- Print de uma ferramenta MCP sendo listada como "somente leitura" na interface, com um selo ou ícone indicando essa característica.

### Descrição

#### Objetivos da Aula
Corrigir a principal lacuna identificada na auditoria anterior: sair da definição de dicionário e mostrar, na prática, como o MCP funciona e por que a anotação de segurança "somente leitura" importa.

#### Habilidades Esperadas
O aluno deve entender o que é uma conexão MCP, como identificá-la na interface e por que ferramentas MCP usadas em planilhas devem ser, preferencialmente, somente leitura e não destrutivas.

### Conteúdo Programático
1. **MCP (Model Context Protocol) em linguagem simples**: um padrão que permite ao ChatGPT acessar ferramentas e dados externos autorizados, mantendo controles de segurança e permissões — como um "conector universal" com regras claras de acesso.
2. **Exemplo de fluxo completo**: um usuário conecta uma ferramenta MCP de um sistema interno de estoque; ao pedir "atualize o preço do produto X na planilha com o valor do sistema", o ChatGPT usa o MCP para ler (não alterar) o sistema de origem e trazer o dado para a planilha.
3. **Regra de segurança oficial**: ferramentas MCP destinadas a uso em planilhas devem ser explicitamente anotadas como **somente leitura e não destrutivas**. Ferramentas sem essa anotação podem ser tratadas de forma mais conservadora pela plataforma e podem nem aparecer disponíveis nesse contexto.
4. **Papel do administrador**: assim como os Apps, o acesso a conexões MCP específicas pode depender de configuração administrativa.

> **🛡️ Cuidado com a segurança:** antes de conectar qualquer ferramenta MCP a uma planilha com dados sensíveis, confirme que ela está anotada como somente leitura. Isso reduz o risco de uma alteração indevida em um sistema externo a partir de um comando mal interpretado.

### Pílula Hands-on
Se você tiver acesso a uma conexão MCP, use-a para trazer um dado de um sistema externo para uma célula específica, e confirme na interface se a ferramenta está identificada como somente leitura. Caso não tenha acesso, descreva por escrito um cenário do seu trabalho em que uma conexão MCP somente leitura seria útil.

### Checkpoint
1. Por que ferramentas MCP usadas em planilhas devem ser preferencialmente "somente leitura e não destrutivas"?
2. Dê um exemplo de dado externo que você gostaria de trazer para uma planilha via MCP.

---

## Aula 3 — Integrações de Dados Financeiros

### 📸 Sugestão de Prints
- Print de um prompt solicitando dados de uma fonte financeira conectada (ex.: cotação de uma ação), com o resultado inserido na planilha e a fonte citada.

### Descrição

#### Objetivos da Aula
Dar um exemplo prático de uso das integrações financeiras, além da simples lista de fornecedores apresentada na versão anterior do curso.

#### Habilidades Esperadas
O aluno deve entender para que servem essas integrações e conseguir formular um pedido simples que as utilize.

### Conteúdo Programático
1. **Fornecedores disponíveis** (sujeitos a plano e configuração administrativa): FactSet, Moody's, Dow Jones Factiva, LSEG, Daloopa, S&P Global.
2. **Aplicações típicas**: valuation, due diligence, auditoria financeira, pesquisa de mercado.
3. **Exemplo guiado**: *"Usando a fonte de dados conectada, traga o histórico de receita dos últimos 4 trimestres da empresa X e insira na aba @Dados_Externos, citando a fonte."*
4. **Limite realista**: essas integrações dependem de habilitação administrativa e de contratos específicos — nem todo usuário terá acesso a todos os fornecedores.

### Pílula Hands-on
Se você tiver acesso a alguma integração financeira, execute o exemplo guiado acima adaptado à sua realidade. Caso não tenha acesso, escreva o prompt que você usaria e o resultado esperado.

### Checkpoint
1. Cite duas aplicações típicas das integrações de dados financeiros.
2. Por que nem todo usuário terá acesso a todos os fornecedores listados?

---

# Módulo 7 — Recursos Avançados e Governança

**Objetivo do módulo:** preparar o aluno para operar em ambientes corporativos regulados, cobrindo planilhas grandes, colaboração, governança avançada e custos.

## Aula 1 — Trabalhando com Grandes Pastas de Trabalho

### 📸 Sugestão de Prints
- Print de uma pasta de trabalho com muitas abas, com o uso de @ para focar em uma aba específica destacado.

### Descrição

#### Objetivos da Aula
Ensinar estratégias específicas para arquivos grandes e complexos, um tema ausente na versão anterior do curso.

#### Habilidades Esperadas
O aluno deve saber recortar o escopo de um pedido em arquivos grandes, evitando pedidos amplos demais que consomem mais tempo e créditos do que o necessário.

### Conteúdo Programático
1. **Recorte por aba/intervalo**: usar @ para limitar o foco da IA a uma parte específica do arquivo, em vez de pedir análises sobre a pasta inteira.
2. **Expectativa de desempenho**: arquivos maiores e pedidos mais complexos tendem a levar mais tempo e consumir mais créditos (ver Aula 4).
3. **Dividir tarefas grandes em etapas menores**: em vez de "reorganize toda a pasta de trabalho", pedir aba por aba.

> **📌 Boa prática:** para pastas de trabalho com mais de 10 abas, comece sempre pedindo um mapa geral ("liste as abas e o que cada uma parece representar") antes de pedir qualquer alteração.

### Pílula Hands-on
Em uma pasta de trabalho com múltiplas abas (ou simule uma), peça primeiro um mapa geral, depois um pedido de alteração recortado a uma única aba usando @.

### Checkpoint
1. Por que recortar o escopo do pedido é especialmente importante em arquivos grandes?
2. O que fazer antes de pedir uma alteração ampla em uma pasta de trabalho com muitas abas?

---

## Aula 2 — Colaboração em Ambientes Corporativos

### 📸 Sugestão de Prints
- Print ilustrativo de um arquivo compartilhado com múltiplos usuários, com um comentário indicando "alteração feita por IA em [data], revisado por [nome]".

### Descrição

#### Objetivos da Aula
Cobrir uma lacuna identificada na auditoria anterior: boas práticas quando várias pessoas trabalham na mesma planilha com apoio de IA.

#### Habilidades Esperadas
O aluno deve saber comunicar claramente à equipe quando uma alteração foi gerada por IA e evitar conflitos de edição simultânea.

### Conteúdo Programático
1. **Sinalizar alterações geradas por IA**: usar comentários ou uma aba de log para registrar o que foi alterado, quando e por quem foi revisado.
2. **Evitar sobreposição de edições**: combinar com a equipe horários ou blocos de trabalho quando uma edição assistida por IA de grande porte estiver em andamento.
3. **Nomeação de versões consistente** (retomando a Aula 3 do Módulo 5) para facilitar a colaboração.

> **💡 Dica profissional:** trate toda alteração gerada por IA em um arquivo compartilhado como um "pull request" informal — alguém revisa antes de considerar definitivo.

### Pílula Hands-on
Em um arquivo compartilhado (real ou simulado), pratique registrar uma alteração gerada por IA em um comentário ou aba de log, incluindo data e quem deve revisar.

### Checkpoint
1. Por que é importante sinalizar quando uma alteração foi gerada por IA em um arquivo compartilhado?
2. Que prática ajuda a evitar conflitos de edição simultânea?

---

## Aula 3 — Governança, Segurança e Privacidade Avançada

### 📸 Sugestão de Prints
- Print (ou diagrama) do painel administrativo mostrando as opções de Residência de Dados, Residência de Inferência e Enterprise Key Management (EKM).
- Print da Compliance API sendo referenciada em um painel de administração.

### Descrição

#### Objetivos da Aula
Fechar a lacuna mais relevante identificada na auditoria anterior para o público corporativo: apresentar recursos de governança avançada ausentes na versão 1.0 do curso.

#### Habilidades Esperadas
O aluno que atua em ambiente corporativo regulado deve reconhecer a existência desses controles e saber a quem perguntar sobre sua configuração.

### Conteúdo Programático
1. **Criptografia e retenção de dados**: prompts e respostas podem ficar disponíveis via Compliance API; alguns registros são retidos por até 30 dias para fins de segurança e integridade.
2. **Uso de dados para treinamento**: em contas Enterprise, os dados não são usados para treinar modelos por padrão.
3. **Residência de Dados e Residência de Inferência**: recursos que permitem a organizações controlarem em quais regiões geográficas os dados são armazenados e processados — relevante para conformidade regulatória, incluindo requisitos da União Europeia.
4. **Enterprise Key Management (EKM)**: permite que a organização gerencie suas próprias chaves de criptografia, em vez de depender exclusivamente das chaves padrão do provedor.
5. **RBAC revisitado**: controle de acesso por função, já apresentado no Módulo 1, mas reforçado aqui como parte de uma estratégia de governança mais ampla.

> **🛡️ Cuidado com a segurança:** esses controles avançados normalmente são configurados por administradores de TI e segurança, não pelo usuário final. Se sua organização exige conformidade regulatória específica, este é o momento de acionar esse time.

### Pílula Hands-on
Se você atua em um ambiente corporativo, verifique com o time de TI/segurança se Residência de Dados, Residência de Inferência e EKM estão habilitados e configurados de acordo com a política da sua organização. Caso não atue nesse contexto, escreva um parágrafo explicando por que uma empresa do setor público poderia se importar com residência de dados.

### Checkpoint
1. Qual é a diferença entre Residência de Dados e Enterprise Key Management (EKM)?
2. Por que uma organização pode precisar de controle sobre onde os dados são processados (residência de inferência)?

---

## Aula 4 — Créditos, Limites de Uso Agêntico e Custos

### 📸 Sugestão de Prints
- Print de um painel de consumo de créditos, com destaque para o indicador de uso agêntico.

### Descrição

#### Objetivos da Aula
Explicar, de forma concreta, como o consumo de créditos funciona e o que caracteriza uma ação "agêntica" — outra lacuna da versão anterior.

#### Habilidades Esperadas
O aluno deve entender por que tarefas maiores consomem mais créditos e o que significa, na prática, o limite de uso agêntico compartilhado entre recursos.

### Conteúdo Programático
1. **O que é uma ação agêntica**: qualquer ação em que o ChatGPT toma múltiplos passos de forma relativamente autônoma para cumprir um pedido (por exemplo, ler várias abas, propor e aplicar uma edição, gerar um resumo) — diferente de uma simples pergunta e resposta.
2. **O que o agente pode fazer sem confirmação explícita**: leituras e explicações. **O que normalmente exige confirmação**: alterações que modificam dados ou fórmulas existentes.
3. **Consumo de créditos**: varia conforme a complexidade da tarefa e o tamanho do arquivo; pastas de trabalho grandes e pedidos com múltiplas etapas consomem mais.
4. **Limite compartilhado**: em muitos planos, o limite de uso agêntico é compartilhado com outros recursos agênticos da mesma conta — não é exclusivo do suplemento de planilhas.
5. **Monitoramento (contas Business/Enterprise)**: administradores podem acompanhar o consumo e adquirir créditos adicionais quando necessário.

> **💡 Dica profissional:** para tarefas grandes, quebre o pedido em etapas menores (ver Módulo 7, Aula 1) — além de facilitar a revisão, isso também ajuda a controlar o consumo de créditos.

### Pílula Hands-on
Verifique, se disponível na sua conta, o painel de consumo de créditos, e identifique se o seu plano compartilha o limite de uso agêntico com outros recursos.

### Checkpoint
1. O que diferencia uma ação agêntica de uma simples pergunta e resposta?
2. Por que dividir uma tarefa grande em etapas menores pode ajudar a controlar o consumo de créditos?

---

# Módulo 8 — Projeto Final

## Projeto Integrador: Modelo Financeiro Automatizado

### 📸 Sugestão de Prints
- Print do resultado final esperado: uma pasta de trabalho completa, com abas de dados, cenários, e um resumo executivo gerado por IA.

### Descrição

#### Objetivo do Projeto
Consolidar, em um único artefato, todas as competências desenvolvidas ao longo do curso — não como um exercício novo e isolado, mas como uma continuação natural dos artefatos já produzidos nos módulos anteriores (recomenda-se reaproveitar a planilha de orçamento criada no Módulo 2).

#### Habilidades Avaliadas
Uso de linguagem natural, engenharia de prompts, Skills, Apps/MCP (quando disponíveis), auditoria e validação, e boas práticas de governança.

### Escopo do Projeto

O aluno deve construir uma pasta de trabalho que inclua:

1. **Criação/atualização de uma pasta de trabalho** (reaproveitando o orçamento do Módulo 2, se possível).
2. **Limpeza automática de dados**, com verificação do critério usado antes de aceitar qualquer remoção.
3. **Explicação das fórmulas principais**, com rastreamento de células de origem.
4. **Criação de cenários** (Base, Otimista, Pessimista).
5. **Uso de pelo menos uma Skill** (padrão ou própria, criada no Módulo 4).
6. **Uso de um App ou conexão MCP**, quando disponível, com verificação de que a ferramenta é somente leitura.
7. **Aplicação do checklist de validação completo** (Módulo 5, Aula 2) antes da entrega.
8. **Resumo executivo final**, gerado com apoio da IA, descrevendo o que foi construído e quais decisões foram tomadas.

### Critérios de Sucesso (Rubrica)

| Critério | O que observar |
|---|---|
| Clareza dos prompts utilizados | Os prompts seguem os critérios da Aula 1 do Módulo 3 (o que preservar, onde, formato de saída)? |
| Uso de pelo menos uma Skill | A Skill foi corretamente invocada com @ ou pelo menu +? |
| Checklist de validação aplicado | Todos os seis itens do checklist foram verificados e documentados? |
| Cenários corretamente construídos | Base, Otimista e Pessimista refletem premissas coerentes entre si? |
| Resumo executivo final | Descreve com precisão o que foi feito, sem omitir limitações ou dados pesquisados na web que precisem de verificação? |

> **🛡️ Cuidado com a segurança:** antes de compartilhar o projeto final com terceiros, confirme que nenhum dado sensível foi inserido sem necessidade, e que qualquer dado financeiro pesquisado na web foi verificado em uma fonte oficial.

### Checkpoint Final
1. Qual foi a etapa do projeto em que o checklist de validação mais ajudou a identificar um problema?
2. Se você tivesse que repetir este projeto do zero, qual prompt você reescreveria primeiro, e por quê?

---

# Apêndice A — Glossário

| Termo | Definição em linguagem simples |
|---|---|
| **Barra lateral** | Painel de conversa com o ChatGPT que fica ao lado da planilha e enxerga seu conteúdo. |
| **RBAC** | Controle de Acesso Baseado em Funções — mecanismo que define quem, na organização, pode usar determinado recurso. |
| **Skill** | Playbook reutilizável que evita reescrever o mesmo prompt detalhado repetidamente. |
| **App** | Conexão autorizada entre o ChatGPT e uma fonte de dados externa (arquivos, sistemas, bancos de dados). |
| **MCP (Model Context Protocol)** | Padrão que permite ao ChatGPT acessar ferramentas e dados externos autorizados, com controles de segurança específicos. |
| **Codex com @Microsoft Excel** | Modo avançado que permite ao Codex controlar diretamente uma pasta de trabalho aberta no Excel. |
| **Ação agêntica** | Ação em que o ChatGPT executa múltiplos passos de forma relativamente autônoma para cumprir um pedido. |
| **Compliance API** | Interface que disponibiliza prompts e respostas para fins de auditoria e conformidade corporativa. |
| **Residência de Dados/Inferência** | Controle sobre em quais regiões geográficas os dados são armazenados e processados. |
| **EKM (Enterprise Key Management)** | Recurso que permite à organização gerenciar suas próprias chaves de criptografia. |

---

# Apêndice B — Troubleshooting: Referência Rápida

| Sintoma | Onde ocorre normalmente | Solução resumida |
|---|---|---|
| Suplemento não aparece na loja | Instalação (Excel/Sheets) | Verificar bloqueio corporativo; usar fluxo de administrador |
| Login falha | Instalação | Confirmar plano compatível (Módulo 1, Aula 2); redefinir senha |
| "Aguardando aprovação do administrador" | Instalação corporativa | Solicitar habilitação via RBAC ou admin center |
| App esperado não aparece | Módulo 6 | Confirmar plano, permissão individual e habilitação administrativa |
| Resposta lenta ou interrompida | Uso geral | Verificar limite de uso agêntico (Módulo 7, Aula 4) |
| Alteração inesperada em célula não relacionada | Uso geral | Reforçar no prompt "o que preservar" (Módulo 3, Aula 1); reverter pelo histórico de versões |
| Dado da web desatualizado | Módulo 2, Aula 3 | Sempre pedir data da consulta e confirmar em fonte oficial para decisões críticas |

---

*Fim do roteiro — Versão 2.0.*
