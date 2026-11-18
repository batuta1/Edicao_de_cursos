# Plano de Aula - Replit Agent (Essentials)

## Identificação

| Campo | Definição |
|---|---|
| Curso | Replit Agent - Essentials |
| Natureza | Curto, introdutório, conceitual e autoinstrucional |
| Carga horária | 75 minutos |
| Público-alvo | Iniciantes sem experiência em programação |
| Pré-requisitos | Conta Replit e acesso à internet |
| Recursos | Navegador atualizado e dados fictícios |

### Objetivo Geral

Compreender o ciclo de criação assistida pelo Replit Agent e avaliar, com critérios de custo, segurança e qualidade, quando planejar, testar, publicar ou reverter um aplicativo.

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Explicar o papel do Agent, do Project, do Preview, do banco e da publicação.
2. Diferenciar desenvolvimento e produção, bem como banco e App Storage.
3. Avaliar riscos de dados, permissões, custos e resultados probabilísticos.
4. Selecionar uma sequência segura de criação, teste, publicação e recuperação.

### Estrutura e Sequência dos Módulos

| Módulo | Título | Referência | Tempo |
|---|---|---|---:|
| 1 | Do pedido ao aplicativo | Visão geral do Agent | 15 min |
| 2 | Planos, modos e custos | Billing, Starter e gastos | 14 min |
| 3 | Dados, identidade e segurança | Database, Auth, Secrets e Security Center | 16 min |
| 4 | Testar, publicar e recuperar | Preview, Publishing e Rollback | 14 min |
| 5 | Síntese e aplicação integrada | Pesquisa consolidada | 16 min |

---

# Módulo 1 - Do pedido ao aplicativo

## Descrição

- **Objetivos da Aula:** ensinar o vocabulário básico e o fluxo do pedido à publicação.
- **Habilidades Esperadas:** classificar elementos da Replit e ordenar um ciclo seguro de criação.
- **📸 Sugestão de Prints:** tela inicial do Project Editor com a caixa do Agent, o seletor de tipo de artefato e a área de Preview identificados por contornos, sem dados de conta.

> Ponto de partida: apresenta o vocabulário e o ciclo que sustentam os demais módulos.

### Objetivos de Aprendizagem

- Identificar Agent, Project, Artifact e Preview.
- Ordenar as etapas do fluxo de criação.
- Reconhecer por que o resultado precisa de revisão humana.

### Texto Descritivo

O Replit Agent transforma descrições em linguagem comum em artefatos digitais. O Agent não apenas responde: atua no Project, propõe ou executa tarefas, cria arquivos, configura infraestrutura, testa e registra checkpoints.

O Project reúne conversa, arquivos, configurações e dados. Artifact é o resultado criado. Preview é a prévia privada de desenvolvimento; não corresponde à versão pública. O fluxo básico é descrever, planejar quando disponível, construir, testar, revisar, publicar e monitorar.

Como o sistema é probabilístico, a primeira saída não deve ser tratada como produto acabado. Um pedido claro, com público, campos, regras e critério de êxito, reduz ambiguidade, mas não elimina a necessidade de teste.

### Verificação Formativa

**Questão:** qual sequência é mais segura? A) publicar e depois definir requisitos; B) descrever, construir, testar no Preview, revisar e publicar; C) inserir dados reais para acelerar o teste.

**Gabarito:** B. **Feedback:** a publicação deve ocorrer somente após teste e revisão com dados fictícios.

### Aplicação Conceitual

Uma equipe precisa de um cadastro simples. Classifique como requisito, teste ou risco: campos obrigatórios; atualizar a página e conferir persistência; usar nomes reais de clientes. **Resposta:** requisito; teste; risco.

---

# Módulo 2 - Planos, modos e custos

## Descrição

- **Objetivos da Aula:** explicar a diferença entre assinatura, modo do Agent, consumo e publicação.
- **Habilidades Esperadas:** escolher escopo e controle de gasto adequados a um cenário.
- **📸 Sugestão de Prints:** `Settings > Usage` com os painéis de consumo e limite visíveis, valores pessoais ocultos; segunda imagem com o seletor de modo do Agent e a confirmação de custo.

> Retoma o fluxo e desloca o foco para decisões de capacidade e gasto antes da construção.

### Objetivos de Aprendizagem

- Diferenciar plano de assinatura, modo do Agent e consumo variável.
- Reconhecer que Plan Mode e Full build podem depender do plano.
- Selecionar controles de escopo e gasto.

### Texto Descritivo

Plano, modo e consumo representam dimensões distintas. O plano define franquias e recursos; o modo do Agent define capacidade e custo de uma ação; o consumo decorre do esforço, da infraestrutura e do uso publicado.

Na data da pesquisa, os modos documentados eram Free, Power e Max, enquanto Plan Mode exigia Core ou Pro. A interface solicitava confirmação antes de ações pagas. Esses rótulos e valores são instáveis e precisam ser revistos antes da publicação do curso.

O controle começa pelo escopo: construir um MVP, dividir mudanças, observar a estimativa antes de confirmar e acompanhar Settings > Usage. MVP é a menor versão que prova a utilidade principal.

### Verificação Formativa

**Cenário:** o orçamento é limitado e a proposta ainda está vaga. A melhor decisão é: A) usar Max imediatamente; B) reduzir o MVP e revisar a estimativa; C) ignorar Usage. **Gabarito:** B.

### Aplicação Conceitual

Relacione: assinatura, modo e publicação, respectivamente, a Core; Power; Autoscale. **Resposta:** plano; modo do Agent; tipo de publicação.

---

# Módulo 3 - Dados, identidade e segurança

## Descrição

- **Objetivos da Aula:** apresentar armazenamento, autenticação, Secrets, segregação de ambientes e responsabilidade sobre dados pessoais.
- **Habilidades Esperadas:** indicar onde guardar cada tipo de dado e reconhecer condições que impedem a publicação.
- **📸 Sugestão de Prints:** `Tools > Database`, `Tools > Secrets` e `Project Security Center` em três recortes, com valores de credenciais ocultos e apenas dados fictícios.

> Com o fluxo e o custo compreendidos, introduz os controles que antecedem qualquer uso real.

### Objetivos de Aprendizagem

- Diferenciar banco, App Storage, desenvolvimento e produção.
- Explicar o papel de Auth, Secrets e Security Center.
- Reconhecer dados inadequados para um exercício.

### Texto Descritivo

O banco PostgreSQL integrado guarda dados estruturados em tabelas; App Storage guarda arquivos grandes e não estruturados. O ambiente de desenvolvimento serve a testes. O ambiente de produção sustenta o aplicativo publicado e usa banco separado.

O Agent pode modificar o banco de desenvolvimento, mas a arquitetura documentada impede escrita direta no banco de produção. Essa separação foi reforçada após o incidente público de 2025, no qual registros de produção foram apagados durante um code freeze.

Replit Auth autentica com conta Replit; Clerk permite identidade independente. Secrets guarda credenciais fora do código. Nenhum segredo deve aparecer em prompt, página, log ou captura. O Security Center auxilia a localizar riscos, mas não substitui teste e revisão humana.

Quem publica um aplicativo que coleta dados pessoais permanece responsável por avisos, base legal ou consentimento e atendimento aos direitos dos titulares. No Brasil, essa responsabilidade deve ser analisada à luz da LGPD. O curso, por isso, usa somente dados fictícios.

### Solução de Problemas

| Sinal | Decisão segura |
|---|---|
| Chave aparece no código ou no prompt | Remover, invalidar a chave exposta e recriá-la em Secrets. |
| Usuários veem dados uns dos outros | Interromper a publicação, corrigir autorização e testar com duas contas. |
| Security Center não está disponível | Manter revisão manual e registrar a dependência de plano ou interface. |

### Verificação Formativa

**Questão:** onde guardar uma chave de API? A) no prompt; B) no código; C) em Secrets. **Gabarito:** C. **Feedback:** Secrets reduz exposição acidental e disponibiliza a credencial por variável de ambiente.

### Aplicação Conceitual

Classifique: lista de livros = banco; capas em imagem = App Storage; chave de API = Secret; nomes reais de alunos = não usar no exercício.

---

# Módulo 4 - Testar, publicar e recuperar

## Descrição

- **Objetivos da Aula:** distinguir validação em Preview, publicação, monitoramento e recuperação.
- **Habilidades Esperadas:** selecionar testes, diagnosticar divergências e indicar o mecanismo de retorno apropriado.
- **📸 Sugestão de Prints:** Preview com dados fictícios, menu `Agent > History` com um checkpoint selecionado e `Tools > Publishing` com a URL pública destacada.

> Aplica os controles anteriores ao ciclo de qualidade e operação.

### Objetivos de Aprendizagem

- Diferenciar Preview e publicação.
- Selecionar testes de persistência, autenticação e isolamento.
- Explicar checkpoint, rollback e restauração de produção.

### Texto Descritivo

Preview é uma prévia temporária. Publishing cria uma versão estável em URL própria. Antes de publicar, convém testar criação, edição, exclusão, atualização de página, saída e novo login, erros e comportamento em telas diferentes.

Checkpoint registra um estado do projeto. Rollback retorna arquivos e, quando selecionado, dados de desenvolvimento a um checkpoint. O banco de produção requer procedimento separado de restauração; não se deve presumir que um rollback comum o alcance.

Após publicar, o percurso principal deve ser repetido na URL pública. Monitoring, logs e Usage apoiam a observação de falhas e custos. Se dois usuários visualizarem os mesmos dados quando não deveriam, a publicação deve ser interrompida.

### Solução de Problemas

| Sinal | Decisão segura |
|---|---|
| Funciona no Preview, mas não em produção | Comparar logs, Secrets e configurações dos ambientes. |
| Mudança quebrou o app | Voltar ao checkpoint estável e repetir o teste. |
| É necessário recuperar dados de produção | Usar o procedimento específico de restauração; rollback comum não basta. |

### Verificação Formativa

**Questão:** o app funciona no Preview, mas não na URL pública. O primeiro passo é: A) apagar o projeto; B) comparar logs, Secrets e configuração de publicação; C) divulgar mesmo assim. **Gabarito:** B.

### Aplicação Conceitual

Ordene: checkpoint; mudança; teste; falha; rollback; novo teste. **Resposta:** essa ordem permite recuperar e verificar o estado estável.

---

# Módulo 5 - Síntese e Aplicação Integrada

## Descrição

- **Objetivos da Aula:** integrar escopo, custo, dados, teste, publicação e recuperação.
- **Habilidades Esperadas:** justificar publicar, adiar ou reverter com base em evidências.
- **📸 Sugestão de Prints:** quadro de decisão com colunas Escopo, Custo, Dados, Testes, Checkpoint e Publicação, preenchido com o cenário do módulo.

> Integra critérios de escopo, custo, segurança, teste, publicação e recuperação.

### Objetivos de Aprendizagem

- Avaliar um plano de construção de ponta a ponta.
- Priorizar correções antes da publicação.
- Justificar uma decisão de publicar, adiar ou reverter.

### Texto Descritivo

Uma criação responsável começa por um problema pequeno e verificável, usa dados fictícios, declara autenticação e persistência e define critérios de êxito. Em seguida, controla gasto, testa a prévia, revisa mudanças e cria um ponto seguro de retorno.

Publicar não encerra o trabalho. A versão pública deve ser testada, monitorada e, se necessário, revertida ou restaurada. A responsabilidade permanece humana, ainda que a ferramenta automatize código, infraestrutura e testes.

### Verificação Formativa

**Cenário:** o app persiste dados, mas uma segunda conta vê registros da primeira. Publicar ou interromper? **Gabarito:** interromper, corrigir isolamento, testar com duas contas e executar a verificação de segurança.

### Aplicação Conceitual

**Atividade integradora:** uma equipe concluiu o MVP, mas a estimativa de custo aumentou, uma chave apareceu em um log e o teste com duas contas falhou. A decisão correta é: A) publicar e corrigir depois; B) remover e rotacionar a chave, corrigir isolamento, rever custo, repetir testes e só então decidir; C) executar rollback de produção sem análise. **Gabarito:** B. **Feedback:** custo não autorizado, segredo exposto e falha de isolamento são três bloqueios independentes de publicação.

---

# Encerramento

O curso estabeleceu critérios para compreender a atuação do Replit Agent sem confundir automação com garantia. A prática regular deve preservar escopo pequeno, dados fictícios e teste observável.

Como aprofundamento, recomendam-se publicação avançada, aplicativos móveis, domínios, integrações e governança de ambientes.

> **Síntese:** criar com agentes exige especificar, testar, proteger, observar e saber voltar.

