---
name: formatar-duvidas
description: Format every document in the `_plan/_duvidas/` folder of this repository. Use when creating, editing, updating, or reformatting any file in `_plan/_duvidas/` (planning and discussion documents with numbered questions/doubts). Enforces an index table at the top (number as link, state emoji, short summary), one anchored block per question, a back-to-index link at the end of each block, and a fixed emoji vocabulary for state and quick information.
---

# Skill: Formatar Dúvidas

## Objetivo

Padronizar os arquivos de `_plan/_duvidas/` para quem abre o arquivo ver o estado de tudo em segundos e navegar por links.

## Quando usar

Sempre que criar, editar, atualizar ou reorganizar qualquer arquivo de `_plan/_duvidas/`.

## Aviso obrigatório

Ao usar esta skill, **cite o uso** no início da resposta: `Usando a skill formatar-duvidas.`

## Estrutura do arquivo (ordem fixa)

1. Título (`# ...`) e uma linha de contexto (status geral, escopo).
2. **Índice**: uma **tabela**, não um sumário (nada de *table of contents*).
3. **Legenda** de emojis (uma linha).
4. Um bloco por dúvida, em ordem numérica.

## 1. Índice (tabela)

Âncora no título do índice: `<a id="indice"></a>`.

| Coluna | Conteúdo |
|---|---|
| `Nº` | número da dúvida, **sempre um link** para o bloco: `[3](#d3)` |
| `Estado` | emoji de estado (ver abaixo) |
| `Resumo` | até ~8 palavras, sem ponto final |

Exemplo:

```markdown
<a id="indice"></a>
## Índice

| Nº | Estado | Resumo |
|---|---|---|
| [1](#d1) | ✅ | Formato do `schema` |
| [2](#d2) | 🟡📢 | Versão nova ou atual |
| [3](#d3) | 🚨🔴 | Valores dos estados de migração |

🔴 aberta · 🟡 respondida com pendência · ✅ fechada · 🚨 urgente · 📢 subdúvida aberta · ⏸️ stand-by · ⛔🧐 fora do escopo por ora
```

**Subdúvidas no índice:** toda subdúvida (`N.k`), pequena ou grande, aparece numa **sub-linha** logo abaixo da dúvida de origem, com `↳` antes do número. Número = link: para o **próprio bloco** se a subdúvida é grande (`[4.5](#d4-5)`), ou para o **bloco da dúvida de origem** se é pequena (`[4.6](#d4)`). Mesmo estado e resumo curto da linha de Pendências.

```markdown
| [4](#d4)   | 🟡📢 | Nomes dos atributos |
| ↳ [4.5](#d4-5) | ✅ | Semântica das duas chaves |
| ↳ [4.6](#d4) | 🔴 | Sentido de "nota" |
```

## 2. Estados (emojis)

| Emoji | Significado |
|---|---|
| ✅ | Dúvida **terminada** |
| 🔴 | **Aberta** |
| 🟡 | **Respondida**, mas ficou algo em aberto |
| 🚨 | **Urgente**: precisa ser respondida logo |
| 📢 | **Subdúvida** ("dúvida da dúvida"): sobrou um elemento em aberto |
| ⏸️ | **Stand-by**: decidido deixar parada de propósito; voltar depois |
| ⛔🧐 | **Fora do escopo por ora**: pode nem ser desejado; **aguarda decisão** (ex.: do colegiado). **Não desenvolver** até lá |

Combinações:

* `🚨` vai **antes** do estado: `🚨🔴`, `🚨🟡`.
* `📢` vai **depois**: `🟡📢`, `🔴📢`.
* `✅` nunca combina com `🚨` nem `📢`. Se ainda há pendência, o estado é `🟡`.
* `⏸️` e `⚠️` podem acompanhar `✅`, quando a decisão está tomada mas a execução está **pausada de propósito** e merece atenção: escreva `✅⏸️⚠️` (stand-by **antes** do triângulo).
* `⛔🧐` é um estado **por si só** (não combina com `🔴`, `🟡`, `✅` nem `📢`); vale para a dúvida e para as suas subdúvidas.
* O mesmo emoji de estado aparece no índice **e** no título do bloco.

## 3. Bloco de cada dúvida

Âncora `<a id="dN"></a>` imediatamente antes do título. Título: `## N · <emoji de estado> Título curto`.

Campos, nesta ordem, **só os que se aplicam**:

| Campo | Uso |
|---|---|
| `**Contexto:**` | 1 a 2 linhas |
| tabela de opções | quando houver alternativas; marcar a recomendada com ⭐ |
| `⭐ **Recomendação:**` | 1 linha |
| `📝 **Decisão:**` | quando respondida; o que foi escolhido |
| `📢 **Pendências:**` | subdúvidas, numeradas `N.1`, `N.2`, cada uma com seu emoji de estado |

Último item do bloco, sempre: `[⬆️ Voltar ao índice](#indice)`.

### Subdúvidas: pequena × grande

A subdúvida **nunca ganha número novo** nem se afasta da dúvida de origem. Ela sempre se chama `N.k` (ex.: `B1.5`).

| Tamanho | Quando | Onde fica |
|---|---|---|
| **Pequena** | cabe em 1 a 3 linhas, sem opções | **linha da tabela de Pendências** da dúvida de origem |
| **Grande** | precisa de contexto, tabela de opções, recomendação ou impacto | **bloco completo**, logo **depois do bloco da dúvida de origem** (antes da próxima dúvida) |

Bloco de subdúvida grande:

* Título de nível 3: `### N.k · <emoji de estado> Título curto`, com âncora `<a id="dN-k"></a>` antes (ex.: `db1-5`, `d2-1`).
* Mesmos campos da dúvida normal: Contexto, tabela de opções (com ⭐), `⭐ Recomendação`, `📝 Decisão`, `❓ Pergunta`, `📦 Impacto`.
* Último item: `[⬆️ Voltar a N](#dN)` (volta para a dúvida de origem, não para o índice).
* A linha dela na tabela de Pendências da dúvida de origem **continua existindo** e aponta para o bloco: `[N.k](#dN-k)`, o emoji de estado e um resumo curto.
* O **índice lista também a subdúvida** (pequena ou grande), numa sub-linha logo abaixo da dúvida de origem (ver "Índice").
* Se ela crescer ou diminuir, pode mudar de forma (linha ↔ bloco) **mantendo o número `N.k`**.
* **Sub-subdúvida** (`N.k.m`, ex.: `A2.1.1`): mesma regra, um nível abaixo. Fica como linha na tabela de Pendências do bloco da subdúvida `N.k` e entra no índice numa sub-linha com `↳↳`, apontando para o bloco de `N.k`.

Modelo:

```markdown
<a id="d2"></a>
## 2 · 🟡📢 Versão nova ou atual

**Contexto:** adicionar `schema` altera a estrutura.

| Opção | Efeito |
|---|---|
| ⭐ Subir versão | `a0.7` → `a0.8` |
| Manter | muda a versão atual |

📝 **Decisão:** subir versão em cada estrutura.

📢 **Pendências:**

| Nº | Estado | Pendência |
|---|---|---|
| 2.1 | 🔴 | Subir também as de manutenção? |

[⬆️ Voltar ao índice](#indice)
```

## 4. Emojis de informação rápida

Usar em títulos, tabelas e frases curtas para a leitura ser imediata. Não encher o texto.

| Emoji | Uso |
|---|---|
| ⭐ | recomendada |
| 📝 | decisão registrada |
| ⚠️ | risco ou cuidado |
| 🔗 | depende de outro item/arquivo |
| 💡 | sugestão ou ideia |
| 👉 | próximo passo |
| 📦 | impacto em dados ou arquivos |
| 🧪 | precisa ser verificado ou testado |
| ❓ | pergunta direta ao usuário |

## Perguntas e opções (regra de conteúdo)

Toda pergunta que o usuário precisa responder segue estas regras, em **qualquer** formato (tabela, lista ou texto):

1. **Cada pergunta é uma seção própria** (`###` se for subdúvida, `##` se for dúvida), com título e estado. **Nunca** junte várias perguntas numa lista curta dentro de uma seção maior.
2. **Sempre apresente de 2 a 4 opções, de preferência 3** (A, B, C), com a recomendada marcada com ⭐ e uma frase de **prós (👍) e contras (👎)** para cada uma. As opções podem ir em **lista** ou em **tabela**; o que não pode faltar é a **escolha**.
3. Termine com `❓ **Pergunta:**` dizendo **exatamente o que se decide** ("A, B ou C?"). Se a pergunta não puder ser dita em uma frase, a seção está confusa: reescreva.
4. Explique antes, em poucas linhas, **o que acontece** (contexto) e **por que a pergunta existe**, com um **exemplo concreto**.
5. Use os emojis da seção de informação rápida (⭐ 👍 👎 ⚠️ 💡 📝 📌 🧪 🔗 👉 📦) para guiar o olho. **Não** reduza o texto a parágrafos secos.
6. Não amontoe tabelas coladas. Use tabela quando houver **vários itens com as mesmas colunas**; para o resto, prefira listas e frases curtas.
7. Quando o usuário **responder**, a seção fica com: as opções que estavam na mesa, o `📝 **Decisão:**` e a fala dele citada.

## Perguntas ficam no arquivo, não no chat

**Toda pergunta de decisão** (opções, ⭐, "como proceder") vai para `_plan/_duvidas/`, numa seção própria. No chat, diga **só em quais itens** a decisão é necessária (ex.: "decidir A5.2 e A5.3") e um resumo de uma linha de cada. Não repita as opções no chat: o usuário se perde entre o chat e o arquivo.

## Nomes de CAMPO × nomes de ED (regra de clareza)

Muitos **campos** têm o **mesmo nome** de uma **ED** (`tools`, `courses`, `trails`, `areas`, `profiles`, `policies`). Para o leitor não confundir:

1. **Campo (chave dentro de um objeto):** escreva **`CAMPO`** em caixa alta antes do nome. Ex.: "o CAMPO `tools` da ED `areas`", "os CAMPOS `courses` e `planned_courses`".
2. **ED (a estrutura inteira):** escreva **`ED`** antes do nome. Ex.: "a ED `areas`", "a ED `tools`".
3. Nunca escreva "lista `tools`", "a chave `trails`" ou só "`courses`" quando o nome puder ser lido das duas formas.
4. Vale também em **títulos, índice e tabelas**. Em coluna que já é só de campos (ex.: tabela "campo bruto → campo da ED") não precisa repetir `CAMPO`.

## Regras de manutenção

1. **Nunca renumere.** Dúvida fechada continua no arquivo, com ✅. Dúvida nova recebe o próximo número.
2. Mudou o estado? Atualize **os três lugares**: linha do índice, título do bloco e campo `📝 Decisão`/`📢 Pendências`. Subdúvida: linha da tabela de Pendências, **sub-linha do índice** e, se for grande, o título do seu bloco.
3. Índice e blocos devem sempre bater: mesmo número, mesmo estado, mesmo resumo. Subdúvida grande fica **colada** ao bloco de origem, nunca no fim do arquivo nem com número de dúvida nova.
4. Âncoras em minúsculas: `d1`, `d2`, `indice`. Subdúvida **pequena** não tem âncora; subdúvida **grande** tem `dN-k` (ex.: `db1-5`).
5. Se o arquivo agrupa dúvidas por parte (ex.: A e B), o número pode ter letra (`A1`, `B3`), com âncora `da1`, `db3`.
6. Sem tabela de conteúdo padrão do Markdown, em nenhuma parte do arquivo.
7. Tabelas antes de texto corrido; frases curtas (ver skill `fala-simples-objetiva`).
8. Não use "—" em tabela para dizer "ainda não existe"; escreva `(novo)` ou `n/a`.
9. **Assunto novo não entra em arquivo antigo.** "Arquivo antigo" é qualquer arquivo de `_plan/_duvidas/` que **não** seja o que está em trabalho (em geral, o de numeração menor). Assunto novo (dúvida, regra, chave, tabela, linha de anexo) vai para o **arquivo em trabalho**, numa **parte nova** (próxima letra: `D`, `E`…), com âncora. No arquivo antigo cabe, **no máximo, uma âncora**: uma linha que aponta para a parte nova. Só se acrescenta algo a um arquivo antigo quando o autor **pedir de forma expressa e clara** (ex.: "coloque isto no 1.2"); na dúvida, **pergunte** em vez de editar.
   * Exceção estreita: corrigir **o ponto exato** do arquivo antigo que ficou **errado** por causa de uma decisão nova (para não haver contradição) é permitido, com a menor edição possível e sem acrescentar assunto.
   * Ao fechar a resposta, **diga** o que ficou sem aplicar nos arquivos antigos, para o autor decidir se pede.

## Escopo

Vale para `_plan/_duvidas/`, **exceto `_plan/_duvidas/lista de UIs.md`**: é um catálogo de interfaces (um H2 por interface, agrupadas por funcionalidade) e **não tem dúvidas nem opções**. **Tem índice** em tabela, no mesmo formato dos outros arquivos, e cada interface, tela ou aba segue a estrutura **Descrição** + **Funções esperadas**. Ver as instruções no comentário do próprio arquivo. Toda interface de usuário nova citada em qualquer conversa entra nele.

Fora disso: a pasta `_retornos/` tem formato próprio (o quê, como, por quê, impacto) e não é coberta por esta skill.
