# ChatGPT no Excel e Google Sheets Para Leigos — Curso Hands-on

*Ao final deste curso, você vai ter uma planilha de verdade, criada e conferida por você, com a ajuda de um assistente de IA dentro dela.*

---

## Antes de Arregaçar as Mangas

Esse curso não é para ficar assistindo. É para você abrir sua planilha, digitar pedidos em português mesmo e ver as coisas acontecerem na tela. Nada de decorar menu por menu — você vai aprender fazendo, oficina por oficina, cada uma resolvendo um probleminha real de quem trabalha com planilha todo santo dia.

**O que você precisa ter aberto agora:**
- Excel (aplicativo ou versão web) ou Google Sheets — o que você usar no dia a dia
- Uma conta ativa no ChatGPT (qualquer plano já serve para começar)
- Internet
- Uma planilha em branco, só para experimentar sem medo

> 🔑 **Regra de ouro deste curso:** errar faz parte. Se o resultado sair torto, você não quebrou nada — é só pedir de novo, de um jeito mais claro. Ninguém aprende a andar de bicicleta lendo o manual.

---

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1 | Instalar o ChatGPT dentro da sua planilha, sem se perder no caminho | 15 min |
| 2 | Criar e atualizar uma planilha só de conversa, sem digitar fórmula nenhuma | 20 min |
| 3 | Escrever pedidos que a IA entende de primeira, sem ficar tentando de novo | 20 min |
| 4 | Conferir o que a IA fez antes de confiar cegamente no resultado | 15 min |
| **Projeto Final** | Montar um painel de tarefas do zero, usando tudo que você aprendeu | 15 min |

As oficinas foram pensadas para serem feitas em sequência — cada uma te entrega uma pequena vitória que vira ferramenta para a próxima. Bora?

---

# Oficina 1 — Coloque o Robô ao Lado da Sua Planilha

### 🎯 O Problema

Você já perdeu tempo copiando um pedaço da planilha, colando no ChatGPT em outra janela, esperando a resposta e trazendo tudo de volta na mão? Nesta oficina você resolve isso de vez: vai instalar o ChatGPT *dentro* do Excel ou do Google Sheets, como um painel de conversa que já enxerga suas células.

### 🧰 O que você vai usar

- Excel ou Google Sheets aberto
- Sua conta do ChatGPT
- Conexão com a internet

### 👐 Mão na massa

**Se você usa Excel:**

1. Abra o Excel e vá até a guia **Página Inicial**.
2. Clique em **Suplementos** (também pode aparecer como "Add-ins").
3. Abra o **Microsoft Marketplace**.
4. Digite "ChatGPT" na busca e confirme que é o suplemento oficial da OpenAI.
5. Clique em **Adicionar** (ou **Instalar**).
6. Faça login com sua conta do ChatGPT.
7. Confira se a barra lateral abriu do lado direito da tela.

**Se você usa Google Sheets:**

1. Abra o Google Sheets.
2. Vá ao menu **Extensões**.
3. Clique em **Complementos** e depois em **Google Workspace Marketplace**.
4. Busque "ChatGPT", encontre o complemento oficial e clique em **Instalar**.
5. Aceite as permissões pedidas (leitura e edição da planilha ativa).
6. Faça login com sua conta do ChatGPT.
7. Reabra o painel sempre que precisar, pelo menu **Extensões**.

8. Com a barra lateral aberta, digite exatamente este texto e envie:

   ```
   Olá, você consegue ver esta planilha? Descreva em poucas
   linhas quantas abas existem e qual é o nome de cada uma,
   sem alterar nada.
   ```

### ✅ Deu certo?

A barra lateral respondeu descrevendo as abas da sua planilha (mesmo que só exista a "Planilha1" ou "Página1"). Isso prova que o ChatGPT está "vendo" o seu arquivo, e não apenas conversando no vazio.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não encontro "ChatGPT" na busca do Marketplace | Sua conta pode ser corporativa e ter a loja bloqueada — pergunte ao time de TI |
| A barra lateral não abre depois de instalado | Feche e reabra o Excel, ou recarregue a página do Google Sheets |
| Instalei, mas continua bloqueado | Em contas de empresa, um administrador precisa liberar o uso — fale com ele |

> 💡 **Dica:** pense na barra lateral como um colega sentado do seu lado, olhando pra planilha. Você não precisa explicar onde estão os dados — só dizer o que quer.

### 🚀 Quer ir além?

Se você usa Excel e Google Sheets no trabalho, instale nos dois e repare: cada um guarda sua própria conversa, sem compartilhar histórico entre si.

---

# Oficina 2 — Crie e Atualize uma Planilha Só de Conversa

### 🎯 O Problema

Você precisa montar rapidamente uma lista de controle — de despesas, de tarefas, do que for — mas não quer perder tempo digitando cabeçalho, formatando coluna por coluna. Nesta oficina você faz isso apenas conversando com a barra lateral.

### 🧰 O que você vai usar

- A barra lateral instalada na Oficina 1
- Uma planilha em branco

### 👐 Mão na massa

1. Com a planilha aberta, digite na barra lateral:

   ```
   Crie uma lista de controle de despesas mensais com as
   colunas data, categoria e valor.
   ```

2. Confira o resultado direto na planilha: as três colunas devem ter aparecido, com algum exemplo preenchido.
3. Agora peça uma atualização, sem recriar tudo do zero:

   ```
   Adicione uma quarta coluna chamada observações, sem
   alterar os dados que já estão preenchidos.
   ```

4. Confira se os dados da etapa 1 continuam lá — só a coluna nova é que deve ter mudado.

### ✅ Deu certo?

Sua planilha agora tem quatro colunas (data, categoria, valor e observações), e os dados criados no passo 1 seguem intactos depois da atualização do passo 3.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| A IA respondeu, mas nada mudou na planilha | Confirme que a aba certa está selecionada e peça de novo, sendo mais direto: "aplique isso na planilha atual" |
| Os dados antigos sumiram depois do pedido de atualização | Peça para desfazer (Ctrl+Z) e refaça o pedido dizendo explicitamente "sem apagar o que já existe" |
| A planilha tem mais de uma aba e a IA mexeu na errada | Use o símbolo @ para apontar a aba certa, ex.: "@Despesas adicione..." — você vai praticar isso na Oficina 3 |

> 📌 **Não esqueça:** depois de qualquer alteração, vale pedir "resuma exatamente o que você mudou" — isso vira um hábito valioso e você vai usar de novo na Oficina 4.

### 🚀 Quer ir além?

Peça para a IA "limpar" a planilha: padronizar formato de data e remover linhas duplicadas, se houver alguma.

---

# Oficina 3 — Escreva Pedidos que a IA Entende de Primeira

### 🎯 O Problema

Você já pediu "organize isso pra mim" e recebeu de volta algo ainda mais bagunçado? O problema não foi a IA — foi o pedido. Nesta oficina você aprende a transformar um pedido vago em um pedido específico, que funciona de primeira.

### 🧰 O que você vai usar

- A planilha da Oficina 2
- A barra lateral aberta

### 👐 Mão na massa

1. Escreva na barra lateral este pedido vago (sim, de propósito):

   ```
   Organiza essa planilha pra mim.
   ```

2. Observe a resposta: ela provavelmente vai ser genérica, porque o pedido não disse *o quê* organizar.
3. Agora reescreva o pedido com três ingredientes: **o que fazer**, **em qual aba** (usando @) e **o formato esperado** do resultado:

   ```
   @Despesas: ordene os valores da coluna "valor" do maior
   para o menor, sem alterar a coluna de data. Apresente o
   resultado na própria planilha.
   ```

4. Compare os dois resultados. O segundo deve ter feito exatamente o que você queria.
5. Para uma mudança maior, peça primeiro um plano, antes de deixar a IA agir:

   ```
   Antes de aplicar qualquer coisa, me diga exatamente quais
   colunas você vai alterar.
   ```

### ✅ Deu certo?

O pedido específico do passo 3 produziu um resultado direto ao ponto — sem "sobras" que você não pediu. E no passo 5 a IA descreveu o plano antes de tocar na planilha.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Mesmo com o @ a resposta ainda saiu genérica | Confira se o nome da aba depois do @ está escrito exatamente igual ao nome real |
| A IA alterou uma aba diferente da que você queria | Repita o pedido citando o nome da aba entre aspas, além do @ |
| Não sei que formato pedir | Peça o mais simples: "apresente como tabela" ou "apresente como resumo em texto" |

> 💡 **Dica:** um pedido forte tem três partes — o quê, onde e em que formato. Faltando uma delas, a IA precisa "adivinhar", e é aí que as coisas saem torto.

### 🚀 Quer ir além?

Guarde o pedido específico que funcionou bem em um bloco de notas. Da próxima vez que precisar de algo parecido, é só reaproveitar e ajustar.

---

# Oficina 4 — Confira Antes de Confiar

### 🎯 O Problema

Você aceitou uma alteração da IA sem olhar direito, e só depois percebeu que um número mudou sem você ter pedido. Nesta oficina você aprende um checklist rápido para nunca mais passar por isso.

### 🧰 O que você vai usar

- A planilha das oficinas anteriores
- A barra lateral aberta

### 👐 Mão na massa

1. Antes de qualquer coisa, duplique o arquivo (Arquivo > Fazer uma cópia, ou salvar como outro nome). Essa cópia é o seu "seguro".
2. Peça uma alteração de porte médio, por exemplo:

   ```
   @Despesas: some o total de cada categoria e crie um
   resumo em uma nova aba chamada Resumo.
   ```

3. Antes de considerar a tarefa concluída, confira, um por um:
   - [ ] Os números fazem sentido? (faça uma contagem rápida de cabeça)
   - [ ] As colunas e linhas antigas continuam lá, do jeito que estavam?
   - [ ] O resumo que a IA deu bate com o que você realmente pediu?
4. Se algo não bater, use o histórico de versões do programa (no Excel, via OneDrive/SharePoint; no Google Sheets, em Arquivo > Histórico de versões) para voltar atrás.
5. Registre em uma frase: você aceitou o resultado, ajustou ou rejeitou? Por quê?

### ✅ Deu certo?

Você tem uma nova aba "Resumo" com os totais corretos, os dados antigos intactos, e uma frase escrita registrando sua decisão final sobre o resultado.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Esqueci de duplicar o arquivo antes de editar | Combine, a partir de agora, sempre duplicar antes de pedidos médios ou grandes |
| Não sei onde fica o histórico de versões | No Excel, é preciso estar salvo no OneDrive/SharePoint; no Sheets, está sempre em Arquivo > Histórico de versões |
| O resumo da IA não bateu com o que ela realmente fez na planilha | Não aceite — peça para refazer, sendo mais específico sobre o que preservar |

> ⚠️ **Cuidado:** o ChatGPT não é contador nem advogado. Se o resultado envolver decisão financeira ou jurídica importante, trate-o como rascunho — nunca como palavra final.

### 🚀 Quer ir além?

Escolha uma fórmula que você não escreveu (de um colega, por exemplo) e peça: "explique esta fórmula célula por célula."

---

# Projeto Final — Painel de Controle de Tarefas

### 🎯 A Missão

Chegou a hora de juntar tudo: instalação, criação por conversa, pedido bem escrito e checklist de conferência. Você vai montar, do zero, um painel de controle de tarefas — o tipo de planilha que qualquer time usa toda semana.

### 👐 Mão na massa

1. Confirme que a barra lateral está aberta e funcionando (Oficina 1).
2. Peça a criação da estrutura, já com pedido específico (Oficina 3):

   ```
   @Tarefas: crie uma planilha de controle de tarefas com as
   colunas tarefa, responsável e prazo. Apresente como tabela.
   ```

3. Peça uma atualização incremental, preservando o que já existe (Oficina 2):

   ```
   Adicione uma coluna de status, sem alterar os dados já
   preenchidos.
   ```

4. Antes de considerar pronto, aplique o checklist da Oficina 4: confira os dados, confirme que nada antigo sumiu, e peça um resumo final do que foi feito.
5. Registre, em uma frase, se você aceitou o resultado como está ou pediu algum ajuste.

### 🏁 Como saber que terminou

- [ ] Planilha com as quatro colunas (tarefa, responsável, prazo e status) visível
- [ ] Estrutura criada por linguagem natural, sem digitação manual de cabeçalhos
- [ ] Pedido de atualização usado sem apagar dados anteriores
- [ ] Checklist da Oficina 4 aplicado antes de considerar concluído
- [ ] Frase escrita registrando sua decisão final sobre o resultado

---

# A Parte dos Dez — Truques que Salvam seu Dia com o ChatGPT na Planilha

1. Use o símbolo **@** seguido do nome da aba para garantir que o pedido caia no lugar certo, principalmente em planilhas com várias abas.
2. Depois de qualquer edição, peça "resuma exatamente o que você alterou" — isso facilita conferir em segundos.
3. Antes de mudanças grandes, peça um plano antes de deixar a IA executar.
4. Duplique o arquivo antes de pedidos médios ou grandes — sua cópia de segurança leva 10 segundos para criar e pode salvar horas de retrabalho.
5. Diga explicitamente o que **preservar** ("sem alterar a coluna de data") — sem isso, a IA pode presumir errado.
6. Se pedir um dado da internet (cotação, índice), peça também a data da consulta, e confira a fonte antes de usar em algo importante.
7. Excel e Google Sheets não compartilham histórico de conversa entre si — trate cada um como uma conversa independente.
8. Em planilhas grandes (muitas abas), peça primeiro um "mapa geral" antes de pedir qualquer alteração.
9. Se o resultado vier torto, não desista no primeiro erro — refine o pedido dizendo o que manter e o que corrigir.
10. Trate qualquer saída sobre tema financeiro ou jurídico como rascunho a ser revisado por um profissional, nunca como resposta definitiva.

---

# Conseguiu! E agora?

Você instalou o ChatGPT na sua planilha, criou e atualizou dados só de conversa, aprendeu a escrever pedidos que funcionam de primeira e — o mais importante — aprendeu a conferir antes de confiar. Isso não é pouco: é o ciclo completo que qualquer uso responsável de IA em planilha exige.

Da próxima vez que precisar montar um controle, limpar uma base de dados ou entender uma fórmula esquisita, é só abrir a barra lateral e repetir o mesmo ciclo: pedir, conferir, ajustar. Quanto mais você praticar em planilhas reais do seu dia a dia, mais natural esse hábito vai ficar — até virar tão automático quanto salvar o arquivo antes de fechar.
