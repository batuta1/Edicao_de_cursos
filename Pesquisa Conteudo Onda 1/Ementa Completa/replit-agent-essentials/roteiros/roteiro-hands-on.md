# Replit Agent Para Leigos - Curso Hands-on

*Ao final, você terá criado, testado e preparado para publicação o app Minha Estante.*

## Antes de Arregaçar as Mangas

Este curso é mão na massa: você vai construir um cadastro de leituras com dados fictícios, login e persistência.

**O que você precisa ter aberto agora:**

- Conta Replit, navegador atualizado e internet.
- Limite de gasto revisado em Settings > Usage.
- Nenhum dado real ou chave real.

> 🔑 Regra de ouro: teste cada pequena vitória antes de pedir a próxima mudança.

## O Mapa da Mão na Massa

| Oficina | Problema que você vai resolver | Tempo |
|---|---|---:|
| 1 | Preparar escopo, custos e segurança | 15 min |
| 2 | Criar o MVP no Agent | 20 min |
| 3 | Adicionar dados e autenticação | 20 min |
| 4 | Testar, corrigir e recuperar | 20 min |
| Projeto Final | Publicar e validar a Minha Estante | 15 min |

---

# Oficina 1 - Prepare o terreno

## Descrição

- **Objetivos da Aula:** ensinar a delimitar MVP, verificar gasto e eliminar dados reais antes da construção.
- **Habilidades Esperadas:** produzir um brief seguro, testável e compatível com o orçamento.
- **📸 Sugestão de Prints:** `Replit > Settings > Usage` com consumo e limite destacados e valores pessoais ocultos; caixa do Agent com o brief, antes de enviar.

### 🎯 O Problema

Um pedido vago pode gerar custo, retrabalho e exposição de dados. Você vai transformar a ideia em um brief seguro.

### 🧰 O que você vai usar

- Replit, Settings > Usage e o prompt do curso.

### 👐 Mão na massa

1. Entre na conta Replit.
2. Abra Settings > Usage e confira o consumo e os limites disponíveis.
3. Defina um teto pessoal de gasto; se a conta não oferecer essa opção, anote que nenhuma ação paga será confirmada.
4. Copie o brief: "Crie um aplicativo web chamado Minha Estante. Cada usuário vê apenas seus próprios livros. Cada livro tem título obrigatório, autor, status, nota e observações. Use dados fictícios."
5. Revise e remova qualquer dado real.

### ✅ Deu certo?

Você tem um brief sem dados reais e sabe qual ação exigirá confirmação de custo.

**Verificação formativa:** se a estimativa ultrapassar o teto, qual ação vem primeiro? **Resposta:** reduzir o escopo ou não confirmar; trocar de modo sem revisar não resolve o limite.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Usage não aparece | Não confirme ações pagas e registre a interface para validação. |
| O brief ficou grande | Preserve público, campos, regra por usuário e critério de êxito. |

### 🚀 Quer ir além?

Escreva uma frase com o que não fará parte do MVP.

---

# Oficina 2 - Construa o MVP

## Descrição

- **Objetivos da Aula:** ensinar a iniciar um Project, revisar um plano e validar o primeiro Preview.
- **Habilidades Esperadas:** obter um MVP pequeno, localizar o resumo e identificar o checkpoint.
- **📸 Sugestão de Prints:** `Replit > Project Editor > Agent` com Plan/Build, lista de tarefas e botão de aprovação; Preview com formulário e lista.

### 🎯 O Problema

Você precisa transformar o brief em um primeiro resultado testável, sem adicionar recursos extras.

### 🧰 O que você vai usar

- Project, Agent, Plan ou Build e Preview.

### 👐 Mão na massa

1. Inicie um Project e escolha Web app quando essa opção estiver disponível.
2. Cole o brief da oficina anterior.
3. Se tiver Plan Mode, revise as tarefas e use Revise plan até o escopo corresponder ao MVP; caso contrário, peça explicitamente uma construção pequena.
4. Confirme a ação somente depois de revisar a estimativa de custo.
5. Aguarde o Agent construir e testar.
6. Abra Preview e confira se existem formulário e lista.
7. Leia o resumo de mudanças e localize o checkpoint.

### ✅ Deu certo?

O Preview mostra o formulário e a lista, e o checkpoint está identificável.

**Verificação formativa:** o Agent adicionou chat e pagamentos fora do brief. O que fazer? **Resposta:** pedir a remoção desses recursos e preservar apenas o MVP.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Agent adicionou recursos extras | Peça para remover apenas o que ficou fora do MVP. |
| Preview não abre | Peça ao Agent que teste a inicialização e relate o menor ajuste. |

### 🚀 Quer ir além?

Peça uma revisão de acessibilidade sem alterar o escopo funcional.

---

# Oficina 3 - Guarde dados por usuário

## Descrição

- **Objetivos da Aula:** ensinar persistência, autenticação e isolamento com dados fictícios.
- **Habilidades Esperadas:** testar refresh, novo login e separação entre usuários, interrompendo o fluxo quando houver vazamento.
- **📸 Sugestão de Prints:** `Replit > Tools > Database` com tabelas fictícias; tela de login; duas sessões lado a lado mostrando listas diferentes e sem identificação real.

### 🎯 O Problema

Dados que somem após atualizar ou aparecem para a pessoa errada tornam o aplicativo inadequado.

### 🧰 O que você vai usar

- Agent, banco PostgreSQL integrado, Replit Auth e Preview.

### 👐 Mão na massa

1. Peça Replit Auth e banco PostgreSQL integrado.
2. Declare que cada usuário deve acessar somente os próprios livros.
3. Crie dois registros fictícios no Preview.
4. Atualize a página e confirme que os registros permanecem.
5. Saia e entre novamente; confirme a persistência.
6. Quando houver segunda conta segura, teste que ela não vê os registros da primeira.
7. Se não houver segunda conta, peça ao Agent um teste automatizado de autorização e marque o teste humano como pendente.
8. Interrompa o fluxo se houver vazamento entre usuários.

### ✅ Deu certo?

Os registros persistem e permanecem isolados por usuário.

**Verificação formativa:** os dados persistem, mas outra conta os vê. Publicar ou interromper? **Resposta:** interromper e corrigir autorização antes de qualquer publicação.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Dados somem no refresh | Peça para verificar armazenamento no banco, não apenas no navegador. |
| Outra conta vê os dados | Não publique; peça isolamento por usuário e repita o teste. |
| Login não abre | Confirme se Replit Auth foi realmente habilitado. |

### 🚀 Quer ir além?

Adicione um filtro por status e valide que ele não altera o isolamento.

---

# Oficina 4 - Teste, corrija e saiba voltar

## Descrição

- **Objetivos da Aula:** ensinar teste regressivo, correção mínima, checkpoint e limites do rollback.
- **Habilidades Esperadas:** diagnosticar uma falha, validar a correção e escolher entre rollback de desenvolvimento e restauração de produção.
- **📸 Sugestão de Prints:** `Replit > Agent > History` com checkpoint e `Rollback to here`; janela `Additional rollback options` com Database destacado, sem confirmar a ação.

### 🎯 O Problema

Uma correção pode quebrar o que já funcionava. Você vai testar, limitar a correção e praticar recuperação.

### 🧰 O que você vai usar

- Preview, Agent, histórico, checkpoint e Security Center.

### 👐 Mão na massa

1. Teste criar, editar, excluir, atualizar, sair e entrar.
2. Descreva qualquer falha com sintoma e resultado esperado.
3. Peça a menor correção possível, sem novas funcionalidades.
4. Repita somente o teste que falhou e depois o percurso completo.
5. Abra o histórico e identifique Rollback to here, sem confirmar se não quiser alterar o projeto.
6. Revise Additional rollback options e observe que Database se refere ao desenvolvimento.
7. Execute o Security Center quando disponível e trate achados críticos antes de publicar.

### ✅ Deu certo?

O percurso principal passa e você sabe localizar o checkpoint e o escopo do rollback.

**Verificação formativa:** o banco publicado precisa voltar a um estado anterior. O rollback comum basta? **Resposta:** não; produção exige procedimento específico de restauração.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| A correção criou outro defeito | Volte ao checkpoint estável e reduza o pedido. |
| Não há Security Center | Registre a dependência de plano/interface e mantenha os testes manuais. |

### 🚀 Quer ir além?

Crie uma tabela simples de teste com ação, resultado esperado e resultado obtido.

---

# Projeto Final - Publique e valide a Minha Estante

## Descrição

- **Objetivos da Aula:** integrar controles técnicos, financeiros e de segurança na decisão de publicação.
- **Habilidades Esperadas:** publicar e validar uma URL ou justificar com evidências por que a publicação foi adiada.
- **📸 Sugestão de Prints:** `Replit > Tools > Publishing` com URL, acesso e custo; página pública com dados fictícios; Monitoring e Usage após o teste.

### 🎯 A missão

Publicar a versão validada, repetir o teste na URL pública e registrar como monitorar ou recuar.

### 👐 Mão na massa

1. Confirme que só há dados fictícios e nenhum Secret exposto.
2. Revise custo, acesso, checkpoint e resultado dos testes.
3. Use Publish ou Tools > Publishing.
4. Revise a URL `.replit.app`, a opção de acesso e o tipo sugerido.
5. Confirme a publicação apenas se houver créditos e autorização pessoal para o gasto.
6. Abra a URL pública e repita criar, atualizar, sair e entrar.
7. Verifique Monitoring, logs e Usage.
8. Se não puder publicar, conclua com uma simulação documentada das decisões e dos testes prévios.

### 🏁 Como saber que terminou

- [ ] Brief e escopo do MVP registrados.
- [ ] Dados fictícios persistem e ficam isolados.
- [ ] Testes passam no Preview.
- [ ] Checkpoint e caminho de rollback identificados.
- [ ] URL pública testada ou decisão de não publicar justificada.
- [ ] Custos e monitoramento conferidos.

# A Parte dos Dez - Atalhos que Salvam seu Projeto

1. Comece pelo menor MVP útil.
2. Declare campos e regras no primeiro pedido.
3. Use dados fictícios.
4. Nunca coloque chave no prompt ou no código.
5. Teste após cada checkpoint.
6. Descreva o sintoma, não apenas "não funciona".
7. Peça a menor correção possível.
8. Diferencie Preview de publicação.
9. Confira Usage antes e depois de ações grandes.
10. Saiba onde está o último estado estável.

# Conseguiu! E agora?

Você construiu um fluxo completo e, principalmente, aprendeu a não confundir geração rápida com produto confiável. Continue praticando com projetos fictícios e escopo pequeno.

