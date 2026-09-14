# Roteiro Final — ChatGPT no PowerPoint (Hands-on)

**Público-Alvo:** professores universitários, de qualquer área, inteiramente novatos no uso de
inteligência artificial generativa.

**Objetivo Geral:** levar o docente a instalar o suplemento ChatGPT para PowerPoint e executar, com
as próprias mãos, o ciclo completo de produção de uma apresentação acadêmica — do material de origem
ao arquivo pronto, com o tema institucional aplicado e todos os dados conferidos.

**Pré-requisitos:** uso básico do PowerPoint; conta ativa no ChatGPT; permissão para adicionar
suplementos do Office (verificada na Oficina 0); um material de origem real e uma apresentação
própria, das quais será feita cópia.

**Carga horária:** 113 minutos (detalhamento em `../carga-horaria/carga-horaria-hands-on.md`).

---

## Estrutura do Curso

| Nível | Unidades | Finalidade |
|---|---|---|
| Nível 0 — Decisão | Oficina 0 | Descobrir quem lê os arquivos, se é possível instalar, e preparar as cópias |
| Nível 1 — Acesso | Oficina 1 | Instalar e testar em apresentação vazia |
| Nível 2 — Produção | Oficinas 2 a 4 | Criar a partir de material, editar sem estragar, trocar de público |
| Nível 3 — Integração | Projeto Final | Duas versões da mesma aula, a partir do mesmo material |
| Apêndice | A Parte dos Dez | Repertório de instruções para consulta rápida |

**Anexos:** não há anexos. Os assuntos deslocados constam do Roadmap de Expansão em
`../_processo/02-analise-hands-on.md`.

> **Nota sobre a auditoria.** Os onze gargalos da matriz de soluções de
> `../_processo/02-analise-hands-on.md` foram endereçados. Duas decisões declaradas: (a) a Oficina 0
> pode concluir que o curso não se aplica ao ambiente do participante, e essa saída está escrita no
> roteiro; (b) o primeiro contato com a ferramenta, na Oficina 1, ocorre em uma apresentação vazia de
> teste, e nunca em material institucional real — invertendo a ordem da versão 1.0.

---

# ChatGPT no PowerPoint Para Leigos — Curso Hands-on

*No fim deste curso você vai ter uma aula inteira montada a partir de material que já existia — em duas versões, para dois públicos.*

## Antes de Arregaçar as Mangas

Este curso é mão na massa. Você vai instalar o ChatGPT dentro do PowerPoint e passar as próximas
duas horas transformando material que já está no seu computador em slides. Cada oficina termina com
uma apresentação — ou um pedaço dela — pronta.

**O que você precisa ter aberto agora:**

- O Microsoft PowerPoint.
- Um documento seu que possa virar apresentação: um artigo, um capítulo, um plano de ensino.
- Uma apresentação sua que já use o tema institucional.
- Uma conta do ChatGPT.

> 🔑 **Regra de ouro:** o ChatGPT pode editar e apagar coisas nos seus slides — quem diz isso é a
> própria OpenAI. Você trabalha em cópia. Sempre. A Oficina 0 faz isso com você.

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 0 | "Antes de instalar: eu posso? Quem vai ler isso?" | 7 min |
| 1 | "Como eu coloco o ChatGPT dentro do PowerPoint?" | 20 min |
| 2 | "Tenho um artigo de trinta páginas e preciso de uma aula" | 20 min |
| 3 | "Preciso mexer nesses slides sem estragar o resto" | 20 min |
| 4 | "Essa apresentação é de congresso e a banca é outra coisa" | 20 min |
| Projeto Final | A mesma aula em dois tamanhos | 26 min |

Faça a Oficina 0 primeiro — ela não é opcional, e pode te poupar o curso inteiro se a instalação
estiver bloqueada na sua instituição.

---

# Oficina 0 — Cinco minutos antes de instalar

## Descrição

- **Objetivos da Aula:** mostrar quem tem acesso ao conteúdo dos arquivos; apresentar o consumo por
  plano; conduzir o teste de permissão de instalação com seus três desfechos; e criar a apresentação
  de teste e a cópia de trabalho.
- **Habilidades Esperadas:** ao final, você sabe quem lê os seus arquivos, sabe se pode instalar o
  suplemento, tem os arquivos de trabalho prontos, e sabe quais perguntas responder na sua
  instituição.

### 🎯 O Problema

Você está prestes a instalar um programa dentro do PowerPoint da sua universidade e a mandar para
ele o conteúdo dos seus slides. Vale cinco minutos para descobrir três coisas: se você tem permissão
de instalar, quem consegue ler esse conteúdo, e quanto isso consome do seu plano.

### 🧰 O que você vai usar

- PowerPoint aberto.
- Navegador com a sua conta do ChatGPT conectada.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** o painel de suplementos do Office aberto sobre o PowerPoint, no momento
  do teste de permissão — mostrando o campo de pesquisa e o resultado (ou o aviso de bloqueio).
  E, ao lado, o explorador de arquivos com os três arquivos: original, cópia e apresentação de teste.

1. **Saiba quem lê.** O ChatGPT para PowerPoint roda **dentro** do PowerPoint da Microsoft. Pelos
   Termos de Serviço do Marketplace de Suplementos, a Microsoft pode ler o conteúdo dos seus arquivos
   do PowerPoint. Somando o processamento da OpenAI, o arquivo passa por duas empresas.

2. **Decida o que não vai entrar.** Nada disto deve estar numa apresentação que você submete ao
   suplemento:

   - Nome de aluno associado a nota, frequência ou ocorrência.
   - Resultado de pesquisa ainda não publicado.
   - Conteúdo de parecer sigiloso.
   - Qualquer coisa coberta por acordo de confidencialidade.
   - Dado pessoal de terceiro coletado em pesquisa.

3. **Descubra o que custa.** Veja o seu plano em `ChatGPT > Menu de perfil > Configurações > Conta`:

   | Seu plano | Como é o acesso |
   |---|---|
   | Free e Go | Uso limitado |
   | Plus, Pro, Business | Sujeito ao limite de uso com agentes de IA do plano |
   | Business, Enterprise, Edu | Debitado do saldo de créditos compartilhado do espaço de trabalho |

   Uma mensagem típica consome de 10 a 50 créditos. Apresentação grande e edição em várias etapas
   consomem mais. Não planeje a aula de amanhã contando com uma cota que pode acabar hoje.

4. **Teste a permissão.** Vá em `PowerPoint > Página Inicial > Suplementos` e pesquise por `ChatGPT`.
   Três coisas podem acontecer:

   | O que aconteceu | O que significa | O que fazer |
   |---|---|---|
   | A loja abriu e dá para adicionar | Você pode instalar | Siga para a Oficina 1 |
   | Abriu, mas a adição está bloqueada ou pede autorização | Precisa do administrador | Peça a implantação pelo arquivo XML de manifesto e volte quando estiver feita |
   | A loja não abre ou o recurso não existe | A instituição bloqueou | **Este curso não vai funcionar no seu computador.** Veja o box abaixo |

5. **Crie a apresentação de teste.** Uma apresentação nova, vazia, salva como `teste-chatgpt.pptx`.
   É nela que você vai dar o primeiro comando na Oficina 1 — nunca num arquivo real.

6. **Crie a cópia de trabalho.** Abra a apresentação sua que usa o tema institucional,
   `PowerPoint > Arquivo > Salvar como`, acrescente `-copia-curso` ao nome, salve e feche a original.

7. **Responda para si**, antes de usar isso em material oficial: a sua universidade tem norma sobre
   uso de IA em material didático? Se você usar, precisa declarar — e uma banca, um congresso e um
   relatório de fomento podem exigir coisas diferentes? O que você vai dizer aos alunos, que têm a
   mesma ferramenta para os seminários deles?

> 📌 **Se a instalação estiver bloqueada.** Sem o suplemento, não há como fazer este curso — ele
> depende inteiramente da barra lateral dentro do PowerPoint. A alternativa honesta é o curso irmão
> **ChatGPT no Word**, cujo fluxo principal é copiar e colar entre o navegador e o documento, e
> funciona em qualquer ambiente, sem instalar nada. As habilidades de formular instruções são as
> mesmas, e você pode aplicá-las depois em slides feitos à mão.

### ✅ Deu certo?

🏁 **Ponto de controle:** em `Explorador de Arquivos > sua pasta` há três arquivos — a apresentação
original, a cópia com sufixo `-copia-curso`, e `teste-chatgpt.pptx`. E você sabe dizer qual dos três
desfechos do passo 4 você obteve.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não encontro `Suplementos` em `Página Inicial` | Sua versão do PowerPoint pode ser antiga demais para suportar suplementos do Office. Confira em `PowerPoint > Arquivo > Conta`. |
| Não sei qual é o meu plano | Você pode ter duas contas — a institucional e a pessoal. Confira com qual e-mail está conectado. |
| A loja abre mas não acha o ChatGPT | Pode ser bloqueio por política, ou indisponibilidade regional. Trate como o terceiro desfecho do passo 4. |

> ⚠️ **Cuidado:** não pule os passos 5 e 6. As oficinas seguintes editam arquivos de verdade, e o
> sistema pode apagar conteúdo. A cópia é o que separa "experimentei" de "perdi a aula".

### 🚀 Quer ir além?

1. **Descubra a norma.** Procure no site da sua instituição por "inteligência artificial" e
   "integridade acadêmica". *Deu certo se:* você achou a norma, ou confirmou que ela não existe.
2. **Veja a sua cota.** Localize o painel de uso da sua conta e anote a data de redefinição.
   *Deu certo se:* você sabe quanto tem e quando renova.
3. **Monte a sua lista pessoal.** Acrescente à lista do passo 2 dois itens específicos da sua área.
   *Deu certo se:* você consegue justificar cada um em uma frase.

---

# Oficina 1 — Botar o ChatGPT dentro do PowerPoint

## Descrição

- **Objetivos da Aula:** conduzir a instalação pelo Marketplace; apresentar a barra lateral; e fazer
  o primeiro comando em ambiente sem risco.
- **Habilidades Esperadas:** ao final, você tem o suplemento instalado e conectado, sabe onde ficam
  as Skills, e distinguiu uma falha de instalação de uma falha de login.

### 🎯 O Problema

Você ouviu falar que dá para usar o ChatGPT dentro do PowerPoint, mas não faz ideia de onde isso
fica. Nesta oficina você instala, conecta a conta, e dá o primeiro comando — numa apresentação vazia,
onde não há nada a perder.

### 🧰 O que você vai usar

- PowerPoint aberto.
- A apresentação `teste-chatgpt.pptx`, criada na Oficina 0.
- Conta do ChatGPT.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** o PowerPoint com a barra lateral do ChatGPT aberta à direita, ao lado da
  apresentação de teste com o slide de título recém-criado. As duas coisas na mesma captura.

1. Abra a apresentação `teste-chatgpt.pptx`. **Não abra material real ainda.**
2. Vá em `PowerPoint > Página Inicial > Suplementos`.
3. Pesquise por `ChatGPT` e clique em adicionar.
4. Abra o ChatGPT pela faixa de opções: `PowerPoint > faixa de opções > ChatGPT`. Ele aparece como
   uma barra lateral, do lado direito.
5. Entre com a sua conta do ChatGPT — aquela que tem o plano que você identificou na Oficina 0.
6. Dê o primeiro comando, na apresentação de teste:

   > Crie um slide de título com o texto "Teste" e um subtítulo com a data de hoje.

7. Veja se o slide apareceu.
8. Clique no símbolo de adição na barra lateral e veja quais Skills estão disponíveis na sua conta.
   Você vai voltar a elas depois; por ora, só localize onde ficam.

### ✅ Deu certo?

🏁 **Ponto de controle:** a barra lateral está visível em `PowerPoint > faixa de opções > ChatGPT`, a
apresentação de teste tem o slide que você pediu, e você sabe onde fica o acesso às Skills. Tudo isso
aconteceu num arquivo de teste, não no seu material.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Aparece "Não foi possível iniciar este suplemento" | Erro conhecido de login unificado. Feche a caixa e tente entrar pelo navegador. Se persistir, a correção depende do administrador da instituição, que precisa atualizar o endereço de retorno no provedor de identidade. |
| Instalou mas não aceita a minha conta | Confira se você está entrando com a conta ChatGPT certa. É comum ter uma pessoal e uma institucional abertas ao mesmo tempo. |
| A barra lateral abre em branco | Feche e reabra o PowerPoint. Se continuar, confira a conexão de internet — o suplemento não funciona offline. |
| Não achei as Skills | Nem toda conta tem Skills disponíveis. Depende do plano, do espaço de trabalho e das permissões. Não é falha sua. |

> ⚠️ **Cuidado:** repare que você só usou a apresentação de teste. Foi de propósito. Da Oficina 2 em
> diante você trabalha nas cópias, nunca nos originais.

### 🚀 Quer ir além?

1. **Explore os apps.** No símbolo de adição, veja quais apps aparecem na sua conta dentro do
   PowerPoint. *Deu certo se:* você sabe dizer se tem algum, e qual.
2. **Teste o limite.** Faça cinco pedidos seguidos na apresentação de teste e veja se algum aviso de
   consumo aparece. *Deu certo se:* você viu como o sistema avisa (ou confirmou que não avisa).
3. **Desinstale e reinstale.** Em `PowerPoint > Página Inicial > Suplementos > Meus Suplementos`,
   remova e adicione de novo. *Deu certo se:* você sabe refazer sozinho se algo quebrar.

---

# Oficina 2 — De um texto longo para uma aula

## Descrição

- **Objetivos da Aula:** produzir um rascunho a partir de material de origem, declarando os quatro
  elementos; e aplicar o procedimento do tema institucional, que a ferramenta nem sempre preserva.
- **Habilidades Esperadas:** ao final, você produz sozinho um deck com o número de slides e a
  estrutura que pediu, com o tema da sua instituição aplicado, e com os dados conferidos.

### 🎯 O Problema

Você tem um artigo de trinta páginas e precisa dar aula sobre ele na quinta-feira. Nesta oficina você
transforma o texto em slides — e resolve o problema que ninguém avisa: o resultado nem sempre respeita
o modelo visual da sua universidade.

### 🧰 O que você vai usar

- A cópia de trabalho (que já tem o tema institucional), esvaziada de conteúdo.
- Um documento de origem — daqueles que você decidiu, na Oficina 0, que pode submeter.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** o PowerPoint em `Exibir > Modo de Exibição de Estrutura de Tópicos`,
  mostrando a hierarquia de títulos dos slides gerados, com a barra lateral do ChatGPT ao lado.

1. **Não comece de uma apresentação em branco.** Abra a cópia de trabalho, que já tem o tema
   institucional, e apague os slides de conteúdo, deixando o arquivo vazio mas com o tema aplicado.
   Salve como `aula-nova.pptx`.

2. Abra a barra lateral: `PowerPoint > faixa de opções > ChatGPT`.

3. Peça o rascunho declarando os **quatro elementos** — origem, estrutura, extensão e público:

   > Crie uma apresentação a partir do material anexado. Doze slides: um de abertura, três seções de
   > conteúdo com três slides cada, um de discussão e um de fechamento. Público: alunos de
   > graduação, primeiro contato com o tema. Mantenha o modelo e o estilo desta apresentação.

4. Espere e percorra os slides gerados no painel de miniaturas.

5. **Confira o tema.** Se os slides não seguiram o modelo institucional — o que é uma limitação
   declarada pelo fabricante — reaplique em `PowerPoint > Design > Temas` e ajuste os layouts
   divergentes em `PowerPoint > Página Inicial > Layout`.

6. **Confira os dados.** Cada número, data e citação que aparecer nos slides precisa estar no
   material de origem. Percorra um por um.

7. Corrija à mão o que estiver errado. Não peça ao sistema para corrigir o que ele inventou — ele
   pode inventar de novo.

### ✅ Deu certo?

🏁 **Ponto de controle:** abra `PowerPoint > Exibir > Modo de Exibição de Estrutura de Tópicos`. Você
deve ver doze slides com a estrutura que pediu. E em modo de classificação de slides
(`PowerPoint > Exibir > Classificação de Slides`), todos devem estar com o tema institucional.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Veio com mais ou menos slides do que pedi | Peça de novo com o número exato e diga o que cortar ou desdobrar. |
| Os slides não seguiram o meu modelo | Limitação conhecida e declarada. Aplique o passo 5. |
| Ele inventou um dado que não está no artigo | Acontece e é previsível. Por isso o passo 6 existe. Remova à mão. |
| Consumiu muito da minha cota | Divida em duas solicitações menores: primeiro a estrutura, depois o conteúdo de cada seção. |

> 💡 **Dica:** declarar a estrutura ("um de abertura, três seções com três slides cada") funciona
> muito melhor do que só dizer o assunto. É a diferença entre um deck utilizável e uma pilha de
> tópicos.

### 🚀 Quer ir além?

1. **Dois públicos, dois decks.** Peça a mesma apresentação para alunos e para colegas da área.
   *Deu certo se:* você aponta três slides que existem numa e não na outra.
2. **Sem material de origem.** Peça a mesma aula só descrevendo o assunto, sem anexar nada. Compare.
   *Deu certo se:* você consegue dizer, concretamente, o que a fonte acrescentou.
3. **A aula de cinco minutos.** Peça a versão de cinco slides do mesmo material. *Deu certo se:* os
   cinco slides ainda contam a história inteira.

---

# Oficina 3 — Mexer sem estragar

## Descrição

- **Objetivos da Aula:** ensinar a delimitação de escopo em três elementos; e ensinar a pedir o plano
  antes de autorizar uma edição extensa.
- **Habilidades Esperadas:** ao final, você insere um slide no meio de uma apresentação pronta sem
  que nenhum outro slide mude, e sabe conferir isso.

### 🎯 O Problema

A apresentação já existe e está boa. Você só precisa acrescentar um slide no meio — e não quer que o
resto mude. Nesta oficina você aprende a delimitar a edição, que é o que separa uma correção de um
estrago.

### 🧰 O que você vai usar

- A cópia de trabalho, com conteúdo, criada na Oficina 0.
- A barra lateral do ChatGPT.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** painel de miniaturas do PowerPoint com o slide recém-inserido destacado
  no meio da sequência, e os slides imediatamente anterior e posterior visíveis e claramente
  inalterados.

1. Confirme que você está na cópia, e não no original. Olhe o nome do arquivo na barra de título.

2. **Peça o plano antes de autorizar qualquer coisa:**

   > Antes de editar, descreva quais slides você mudaria e por quê. Não altere nada ainda.

3. Leia o plano. Se não for o que você quer, corrija agora — antes que a apresentação seja
   modificada. Custa uma mensagem e evita refazer tudo.

4. Peça a edição declarando os **três elementos** — o que alterar, o que preservar, e onde:

   > Adicione um slide de limitações metodológicas logo após o slide de resultados. Mantenha o
   > estilo desta apresentação e não altere nenhum outro slide.

5. **Confira os vizinhos.** Olhe o slide imediatamente anterior e o imediatamente posterior ao novo.
   Eles devem estar exatamente como estavam.

6. Se o slide novo ficou com aparência diferente, reaplique em
   `PowerPoint > Página Inicial > Layout`.

### ✅ Deu certo?

🏁 **Ponto de controle:** no painel de miniaturas, o slide novo está na posição que você pediu, e os
slides vizinhos estão idênticos. Se quiser certeza, abra o arquivo original em paralelo e compare —
ele continua intacto porque você nunca o abriu para edição.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Ele mexeu em slides que eu não pedi | Desfaça com `Ctrl + Z`. Refaça declarando "não altere nenhum outro slide". |
| Ele apagou conteúdo | Volte para o arquivo original. É exatamente para isso que a cópia da Oficina 0 existe. |
| O slide novo ficou com outro visual | `PowerPoint > Página Inicial > Layout` e escolha o layout dos demais. |
| Pedi para mexer num gráfico e não funcionou | Limitação declarada: recursos avançados de gráficos, formas e formatação podem ser limitados. Faça à mão. |

> 📌 **Não esqueça:** pedir o plano antes custa uma mensagem e evita refazer a apresentação inteira.
> É o hábito mais barato deste curso.

### 🚀 Quer ir além?

1. **A narrativa.** Pergunte: "qual é a narrativa desta apresentação?". *Deu certo se:* o que ele
   descreve é o argumento que você achava ter construído — ou você descobriu que não é.
2. **As lacunas.** Pergunte: "onde estão as lacunas desta apresentação?". *Deu certo se:* pelo menos
   uma lacuna apontada era real e virou slide.
3. **A arguição.** Pergunte: "que perguntas o público provavelmente fará?". *Deu certo se:* você tem
   resposta para todas — ou anotou as que não tem.

---

# Oficina 4 — Trocar de público

## Descrição

- **Objetivos da Aula:** ensinar o refinamento de uma apresentação para um público diferente; e usar
  a consulta de narrativa e lacunas para validar o resultado.
- **Habilidades Esperadas:** ao final, você produz uma segunda versão de uma apresentação para outro
  público e sabe apontar o que cada versão sacrificou.

### 🎯 O Problema

A apresentação foi feita para um congresso da área. Agora é uma banca de qualificação — ou uma
reunião de colegiado, ou uma palestra para o público geral. Mesmo conteúdo, outro leitor, outro
tempo, outro nível de detalhe. Nesta oficina você faz a segunda versão.

### 🧰 O que você vai usar

- A apresentação da Oficina 2 ou 3 (uma cópia dela).
- A barra lateral do ChatGPT.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** duas janelas do PowerPoint lado a lado, em modo de classificação de
  slides, mostrando as duas versões da mesma apresentação com contagens de slides diferentes.

1. Duplique de novo: `PowerPoint > Arquivo > Salvar como`, com um nome que diga o público de destino
   — por exemplo `aula-banca.pptx`.

2. Peça o ajuste declarando **quem é o novo público e o que muda por causa dele**:

   > Ajuste esta apresentação para uma banca de qualificação de mestrado. Reduza para quinze slides.
   > Aumente o detalhe metodológico, diminua a contextualização histórica e mantenha todos os
   > números exatamente como estão. Mantenha o estilo desta apresentação.

3. Percorra o resultado no painel de miniaturas.

4. Valide com a consulta:

   > Qual é a narrativa desta apresentação e onde estão as lacunas para uma banca de qualificação?

5. Peça a antecipação da arguição:

   > Que perguntas uma banca de qualificação provavelmente fará sobre esta apresentação?

6. Corrija o que fizer sentido e confira que os números continuam iguais aos da versão original.

### ✅ Deu certo?

🏁 **Ponto de controle:** você tem dois arquivos, com contagens de slides diferentes, e todos os
números coincidem entre eles. Confira abrindo as duas em
`PowerPoint > Exibir > Classificação de Slides`, lado a lado.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Ficou genérico | Você não disse o suficiente sobre o público. Diga quem é a banca, o que ela vai cobrar e quanto tempo você tem. |
| Cortou o que era essencial | Diga qual slide precisa voltar e o que cortar no lugar. |
| Um número mudou entre as versões | Corrija à mão e reforce: "mantenha todos os números exatamente como estão". |
| O tema se perdeu na versão nova | Reaplique em `PowerPoint > Design > Temas`. |

> 💡 **Dica:** ao trocar de público, o risco não é o corte — é o número que se desloca junto com o
> texto. Confira sempre os dois arquivos lado a lado.

### 🚀 Quer ir além?

1. **Três públicos.** Faça a terceira versão, para o público leigo. *Deu certo se:* você consegue
   dizer o que a versão leiga não pode assumir como sabido.
2. **A versão de emergência.** Peça a versão de cinco minutos, com cinco slides. *Deu certo se:* ela
   ainda sustenta o argumento principal.
3. **O sanity check reverso.** Peça: "se você fosse contra esta apresentação, qual seria a sua
   objeção mais forte?". *Deu certo se:* você tem uma resposta preparada.

---

# Projeto Final — A mesma aula em dois tamanhos

## Descrição

- **Objetivos da Aula:** exigir a produção de duas versões da mesma aula, a partir do mesmo material,
  mantendo tema e dados idênticos — competência que nenhuma oficina cobre isoladamente.
- **Habilidades Esperadas:** ao final, você produz duas apresentações consistentes entre si, com o
  tema institucional aplicado, dados conferidos e cruzados, e a arguição antecipada.

### 🎯 A missão

Não é montar mais um deck. É montar **dois**, do mesmo material, para situações diferentes — e
garantir que eles não se contradigam.

Escolha um material de origem real e produza:

- **Versão longa:** uma aula de cinquenta minutos para a graduação. Mais contexto, mais exemplos,
  ritmo de quem está vendo pela primeira vez.
- **Versão curta:** um seminário de vinte minutos para colegas da área. Sem contexto básico, direto
  ao argumento e ao método.

As duas usam o tema institucional. As duas têm os mesmos números. Nenhuma das duas contradiz a outra.
É aqui que as oficinas isoladas não bastam: você precisa criar, editar, refinar e verificar em duas
frentes ao mesmo tempo.

### 🧰 O que você vai usar

- Um material de origem real, dos que você pode submeter.
- Um arquivo com o tema institucional aplicado, para servir de base às duas versões.
- A barra lateral do ChatGPT.

### 👐 Mão na massa

- **📸 Sugestão de Prints:** três janelas — a versão longa em classificação de slides, a versão curta
  em classificação de slides, e a barra lateral do ChatGPT. A comparação entre as duas contagens é o
  que a captura precisa mostrar.

1. **Prepare a base.** Duplique o arquivo com o tema institucional duas vezes:
   `aula-longa.pptx` e `aula-curta.pptx`.

2. **Produza a versão longa** (Oficina 2): declare material de origem, estrutura, extensão e público.
   Para cinquenta minutos, calcule entre vinte e vinte e cinco slides.

3. **Confira o tema e os dados** da versão longa. Liste os números que aparecem — você vai precisar
   dessa lista no passo 6.

4. **Produza a versão curta** a partir do **mesmo material de origem**, não a partir da versão longa.
   Isso é importante: derivar da longa propaga qualquer erro que tenha entrado nela.

5. **Refine a versão curta** para o público de pares (Oficina 4): mais método, menos contexto.

6. **Cruze os números.** Abra as duas lado a lado e confira que cada dado que aparece nas duas está
   idêntico. Onde divergir, volte ao material de origem e corrija as duas.

7. **Consulte as duas:** peça a narrativa e as lacunas de cada uma, separadamente.

8. **Antecipe a arguição da versão curta:** que perguntas os pares vão fazer?

9. **Confira o tema** nas duas, em `PowerPoint > Exibir > Classificação de Slides`.

10. **Anote** as três instruções que funcionaram melhor.

### 🏁 Como saber que terminou

- [ ] Existem dois arquivos, com contagens de slides diferentes e compatíveis com o tempo de cada
      situação.
- [ ] As duas versões partiram do mesmo material de origem, e não uma da outra.
- [ ] O tema institucional está aplicado em todos os slides das duas.
- [ ] Todo número que aparece nas duas versões é idêntico entre elas e confere com a origem.
- [ ] Nenhuma afirmação de uma versão contradiz a outra.
- [ ] Você consultou narrativa e lacunas das duas.
- [ ] Você tem resposta para as perguntas prováveis do público de pares.
- [ ] Nenhum conteúdo das categorias vedadas na Oficina 0 foi submetido.
- [ ] Você respondeu, para si, se este material precisa declarar o uso de IA.
- [ ] Você tem três instruções anotadas para reusar.

---

# A Parte dos Dez — Coisas que Funcionam no ChatGPT para PowerPoint

1. **Comece de um arquivo com o tema aplicado.** Nunca de uma apresentação em branco. Metade dos
   problemas de modelo desaparece só com isso.
2. **Diga a estrutura, não só o assunto.** "Doze slides: abertura, três seções de três, discussão,
   fechamento."
3. **Dê material de origem.** Resultado com fonte é sempre melhor que resultado sem.
4. **Peça o plano antes de editar.** "Antes de editar, diga o que mudaria e por quê. Não altere nada
   ainda."
5. **Delimite o escopo.** "Não altere nenhum outro slide."
6. **Declare o que preservar.** "Mantenha o estilo desta apresentação e todos os números."
7. **Pergunte pela narrativa.** "Qual é a narrativa desta apresentação?"
8. **Pergunte pelas perguntas.** "Que perguntas o público provavelmente fará?" — o melhor uso da
   ferramenta para quem vai a banca.
9. **Duplique antes.** `PowerPoint > Arquivo > Salvar como`. Sempre, sem exceção.
10. **Confira todo número.** O sistema não garante nenhum, e quem apresenta é você.

## Conseguiu! E agora?

Você montou duas apresentações a partir do mesmo material, com o tema da sua instituição, dados
conferidos e cruzados, e a arguição antecipada. Isso é mais do que "usar uma ferramenta de IA" — é um
processo de produção que você pode repetir toda semana.

O próximo passo é justamente repetir. Escolha o material da próxima aula e faça o ciclo inteiro. A
partir da terceira vez você vai perceber que o tempo economizado não está na geração dos slides, mas
em nunca mais começar de uma tela em branco. E vai perceber também quais aulas não valem a pena
passar por aqui — que é uma descoberta tão útil quanto a outra.
