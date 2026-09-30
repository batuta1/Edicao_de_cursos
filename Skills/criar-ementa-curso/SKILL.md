---
name: criar-ementa-curso
description: Cria do zero o pacote completo de um curso, em Markdown, dentro de uma pasta própria do tema — a ementa consolidada, os roteiros nas trilhas Essentials e Hands-on, a tabela MET e a carga horária calculada por aula e total. Cobre o ciclo inteiro: definir contornos (objeto base, público, pré-requisitos), escrever a versão 1.0, auditar criticamente, reformular em roteiro final com objetivos e habilidades por aula, calcular a carga horária pela MET, consolidar a ementa e, opcionalmente, gerar o roteiro pronto para o Articulate Rise 360. Use esta skill sempre que o usuário quiser criar/planejar/estruturar um curso novo, uma ementa, um plano de aula, um roteiro de curso, oficinas hands-on, módulos Essentials, calcular carga horária de curso ou aplicar a tabela de tempo por atividade — mesmo que ele não cite "ementa", por exemplo "monta um curso de Excel para professores", "preciso de um plano de aula sobre Canva", "quanto tempo dura esse curso?", "faz o roteiro das oficinas".
---

# Criação de ementa de curso do zero

A entrega desta skill é **uma pasta com o nome do tema**, contendo o curso descrito por inteiro:
a ementa consolidada, os roteiros nas duas trilhas, a tabela MET e a carga horária. É a
matéria-prima do restante da esteira — vira curso no Articulate Rise 360, que vira SCORM, que
depois é revisado pela skill `revisar-curso-scorm`.

O pipeline tem fases separadas porque **texto de curso gerado de uma vez só sai plausível e raso**.
A versão 1.0 sempre parece boa: ela só revela os buracos (instalação vaga, pré-requisito não dito,
exercício que não dá para executar) quando alguém a lê procurando defeito. Por isso a auditoria é
uma fase própria, e não um "revisar antes de entregar".

**Na fase de auditoria, leia a versão 1.0 como se outra pessoa a tivesse escrito.** No fluxo
original cada fase rodava em uma IA diferente justamente para isso — se quiser preservar essa
separação, o usuário pode levar o arquivo a outro modelo; o importante é que a auditoria não seja
uma defesa do próprio texto.

## Antes de começar

Confirme com o usuário (ou infira, se o pedido já disser):

- **Objeto base** — tema/ferramenta do curso. É o único campo obrigatório; ele também nomeia a pasta.
- **Público-alvo** — muda tudo: exemplos, ritmo, o que pode ser pressuposto.
- **Pré-requisitos e recursos** — conta em alguma plataforma? software instalado? internet?
- **Carga horária alvo** — padrão 60–90 min por trilha.
- **Material-fonte** — documentação oficial, artigo, apostila, curso anterior. Sem ele o conteúdo
  sai de conhecimento geral, e aí **todo dado factual precisa ser marcado como "verificar"**.
- **Autoinstrucional?** — se o aluno faz sozinho, nada pode depender de "o professor explica na
  hora". Declare isso na TAREFA do modelo.

**As duas trilhas são o padrão.** Essentials entrega o entendimento, Hands-on entrega a execução, a
partir do *mesmo* objeto base, mesmo público e mesmo material-fonte — é assim que o projeto usa.
Só gere uma trilha se o usuário pedir explicitamente.

## Pasta de entrega

Crie a pasta no diretório de trabalho atual, nomeada a partir do tema em **kebab-case e sem
acento** (`Excel para professores` → `excel-para-professores/`). Se o projeto já tiver um lugar
canônico para cursos, use-o em vez de inventar um.

```
<tema>/
├── README.md                          índice da pasta: o que é cada arquivo
├── ementa.md                          ◀ PRODUTO — ementa consolidada do curso
├── roteiros/
│   ├── roteiro-essentials.md          ◀ PRODUTO — plano de aula completo, trilha Essentials
│   ├── roteiro-hands-on.md            ◀ PRODUTO — curso completo, trilha Hands-on
│   ├── roteiro-articulate-essentials.md   ◀ PRODUTO — versão Rise 360 (cues » IA:, ▼▼▼)
│   └── roteiro-articulate-hands-on.md     ◀ PRODUTO — versão Rise 360 (cues » IA:, ▼▼▼)
├── carga-horaria/
│   ├── met-tabela.md                  ◀ PRODUTO — a MET aplicada neste curso
│   ├── carga-horaria-essentials.md    ◀ PRODUTO — breakdown por aula + total
│   └── carga-horaria-hands-on.md      ◀ PRODUTO — breakdown por oficina + total
└── _processo/                         rastro de construção, não é entregável
    ├── 00-contornos.md
    ├── 01-v1-essentials.md
    ├── 01-v1-hands-on.md
    ├── 02-analise-essentials.md
    └── 02-analise-hands-on.md
```

Os produtos ficam no nível de cima, separados por natureza. O `_processo/` existe porque é o que
explica **por que** o roteiro ficou como ficou: quando alguém questionar uma decisão daqui a três
meses, a resposta está na análise crítica. Ele não entra na entrega, mas não se apaga.

O `README.md` da pasta lista os arquivos com uma linha cada e registra o que ficou pendente de
validação humana.

## As duas trilhas

| | **Essentials** | **Hands-on** |
|---|---|---|
| Objetivo do aluno | Compreender um assunto | Executar uma tarefa com a ferramenta |
| Unidade | Módulo | Oficina (parte de um problema real) |
| Registro | Formal, impessoal ("recomenda-se") | 2ª pessoa, leve ("você") |
| Corpo | Texto descritivo (3–5 parágrafos) + exercício | Passo a passo numerado + "Deu certo?" |
| Fecho | Módulo de Síntese integradora | Projeto Final + "A Parte dos Dez" |
| Modelo | `referencias/modelo-essentials.md` | `referencias/modelo-hands-on.md` |

As duas compartilham a acessibilidade "Para Leigos": o participante é inteligente, porém
inteiramente novato — explique cada conceito desde o zero e descomplique todo termo técnico no
momento em que ele aparece. **Em Essentials, descomplicar não é informalizar**: a clareza vem sem
gíria, sem humor e sem tratamento direto ao leitor.

Rode as Fases 1 a 4 **uma vez por trilha**. Elas compartilham apenas o `00-contornos.md` —
auditoria, reformulação e carga horária são independentes, porque os defeitos de um plano de aula
formal não são os mesmos de uma oficina prática.

Não funda as duas em um documento só: o registro é incompatível (impessoal × 2ª pessoa) e o
resultado sai com o tom trocado no meio.

---

## Fase 1 — Versão 1.0 de cada trilha

Leia o modelo da trilha em `referencias/` e produza o documento inteiro seguindo a ordem de seções
que ele exige. Grave em `_processo/01-v1-essentials.md` e `_processo/01-v1-hands-on.md`.

O modelo não é sugestão: a ordem das seções, os cabeçalhos e os elementos obrigatórios de cada
módulo/oficina são o contrato. Se um item não couber (ex.: não existem dez itens honestos para "A
Parte dos Dez"), **reduza declaradamente** em vez de encher linguiça.

Não invente funcionalidade, botão ou menu que a ferramenta não tenha. Onde houver incerteza,
descreva de forma genérica e sinalize que precisa ser conferido — um passo inventado só aparece
quando o aluno trava nele.

## Fase 2 — Auditoria crítica

Aplique `referencias/prompt-analise-critica.md` sobre cada v1.0. Grave em
`_processo/02-analise-<trilha>.md`.

A auditoria cobre quatro eixos — clareza pedagógica, rigor técnico, engajamento e potencial oculto
— e termina em **matriz de soluções**: cada ponto negativo com a correção concreta ao lado ("trocar
o texto X pelo caminho Y"), não com um lamento genérico.

Um relatório que só elogia falhou. Estes são os defeitos que a v1.0 costuma ter:

| Sintoma | O que corrigir no roteiro final |
|---|---|
| Instalação/setup vago ("baixe e instale") | Passos por sistema operacional, com o que verificar depois |
| Pré-requisito não declarado, cobrado no meio do curso | Puxar para o Módulo 0 / "O que você precisa ter aberto" |
| Exercício que não dá para executar sozinho | Reescrever com todos os passos explícitos e critério de êxito |
| Nada sobre segurança de dados / permissões | Módulo próprio, cedo, antes do primeiro uso real |
| Módulo avançado desconectado do público-alvo | Marcar como opcional ou reposicionar como anexo |
| Só o básico da ferramenta; o diferencial fica de fora | Roadmap de expansão no relatório, virando módulos no roteiro |

## Fase 3 — Roteiro final (produto)

Aplique `referencias/prompt-reformulacao.md` sobre v1.0 + análise. Grave em
`roteiros/roteiro-essentials.md` e `roteiros/roteiro-hands-on.md`.

O roteiro final é a v1.0 com a matriz de soluções executada, mais o que o modelo v1 não exigia:

- **Objetivos da aula** e **Habilidades esperadas** em cada módulo/oficina, separados — objetivo é
  o que se ensina; habilidade é o que o aluno faz sozinho depois.
- **Sugestão de prints** descrita ao ponto de alguém conseguir capturá-la (qual botão destacado,
  qual menu aberto).
- **Troubleshooting** exatamente nos pontos que a auditoria marcou como críticos.

Cada achado da auditoria precisa ter destino visível aqui. Achado não endereçado deve ser declarado
como decisão consciente, não simplesmente sumir.

## Fase 4 — Carga horária (produto)

Copie a tabela de `referencias/tabela-tempo-atividade.md` para `carga-horaria/met-tabela.md` — ela
viaja junto com o curso, porque sem ela os números não se conferem. Depois aplique
`referencias/prompt-carga-horaria.md` sobre cada roteiro final, gerando
`carga-horaria/carga-horaria-<trilha>.md`.

O método: classificar **cada atividade** em um dos oito tipos da MET, somar por aula, somar o
curso, e reportar a proporção teoria/prática.

Regras que sustentam o número:

- **Não crie categorias novas.** Se uma atividade não se encaixa em nenhum dos oito tipos, ou ela
  está mal descrita no roteiro, ou é duas atividades — resolva no roteiro, não na tabela.
- Use o valor fixo de cada tipo, não a faixa, para o cálculo ser reproduzível por terceiros.
- Alvo para iniciantes: **40% teoria / 60% prática**. Fora disso, diga onde falta prática.
- A soma tem que caber na carga horária combinada na Fase 0. Se estourar, **reporte o estouro** e
  proponha o que cortar — não encolha os tempos para fechar a conta.

O breakdown vai em tabela (Atividade | Tipo de Elemento | Duração), com linha de total por aula.

## Fase 5 — Ementa consolidada (produto)

Só agora, com roteiros e tempos fechados, escreva `ementa.md` seguindo
`referencias/modelo-ementa.md`. Ela é o documento de uma página que apresenta o curso: identificação,
objetivo geral, competências, mapa das trilhas e carga horária real.

**A ementa vem por último de propósito.** Escrita antes, ela promete o que o curso não entrega;
escrita no fim, cada número e cada competência sai de um arquivo que já existe. Não afirme nela
nada que não esteja num roteiro.

## Fase 6 — Verificação por marcos

Rode `referencias/checklist-marcos.md`. Cada fase tem sinal verde e sinal vermelho; sinal vermelho
aponta para qual fase refazer, e não para um remendo local.

Escreva o `README.md` da pasta e, nele, o que **não** foi verificado. Vale principalmente para dado
factual sobre a ferramenta quando não havia material-fonte: liste esses pontos como pendências de
validação humana.

---

## Fase 7 — Roteiros para o Articulate

Quando o curso vai virar curso no Rise 360, o roteiro da Fase 3 ainda não basta: falta a camada de
montagem. **Cada trilha tem o seu prompt-mestre, e eles não são intercambiáveis:**

| Trilha | Prompt | Saída |
|---|---|---|
| Essentials | `referencias/articulate-essentials.md` | `roteiros/roteiro-articulate-essentials.md` |
| Hands-on | `referencias/articulate-hands-on.md` | `roteiros/roteiro-articulate-hands-on.md` |

Os dois são prompts-mestre do projeto, reproduzidos verbatim. **Eles mandam em caso de conflito
com os modelos das Fases 1–3** — são mais recentes e já embutem decisões que os modelos base não
têm (a subseção "Mão na massa" de cada módulo Essentials, os requisitos técnicos de plano pago, a
carga horária de 100–130 min).

Passe o roteiro final da trilha como **material-fonte** do prompt. Sem isso o prompt gera um curso
novo do zero, que diverge do que você auditou na Fase 2 e cronometrou na Fase 4 — e aí a ementa
passa a descrever um curso que não é o entregue.

O que a camada de montagem acrescenta:

- **Breadcrumbs no lugar de prints** — `Aplicativo > Menu > Submenu > Opção`, mais os pontos de
  controle `🏁`. Isto **inverte** a Fase 3: a "sugestão de prints" serve à produção do material
  visual; no roteiro que vai para o Rise ela é substituída por caminho de navegação. Nenhuma
  menção a "captura de tela" pode sobrar.
- **Cues `» IA:`** antes de cada bloco, dizendo o tipo de bloco do Rise e o que preservar verbatim.
  Os mapas de tipo diferem entre as trilhas — Essentials tem `Knowledge Check` para múltipla
  escolha e `List` verbatim para objetivos; Hands-on tem `Process` para o passo a passo e
  `Accordion` para o "Se travar".
- **Marcadores `▼▼▼`/`▲▲▲`** cercando cada módulo (Essentials) ou cada oficina e o Projeto Final
  (Hands-on), para o Rise não dividir nem fundir lições. Identificação, Parte dos Dez e
  Encerramento não recebem marcador.

Daí em diante o fluxo sai desta skill: carregar no Articulate o `promptArticulate.md` do projeto +
o roteiro → gerar curso → verificação visual → exportar SCORM → `revisar-curso-scorm`.

## Armadilhas conhecidas

- **Nome de arquivo ou pasta com acento**: o fluxo original pedia `carga-horária.md` e o arquivo
  real ficou `carga-horaria.md`. Nomes sem acento; acento quebra link e atrapalha script.
- **Instruções vazando para o conteúdo**: ao usar os prompts-modelo, o tema do curso vem do OBJETO
  BASE, nunca das instruções. Se o curso começar a falar de "design instrucional", "Rise 360" ou
  "trilha Essentials", o prompt vazou — descarte e reescreva a partir do objeto base.
- **Tom trocado entre trilhas**: Essentials com "você" e piadinha, ou Hands-on em voz impessoal.
  São erros de trilha, não de gosto; confira o registro antes de entregar.
- **Emoji fora do lugar**: nos modelos, emoji só aparece em cabeçalho de subseção e nos boxes
  previstos (🔑 💡 ⚠️ 📌 🤓 🎯 🧰 👐 ✅ 🚑 🚀 🏁). Nunca no corpo do texto.
- **Modelo editável com crase tripla**: prompts e modelos que o aluno vai copiar são delimitados
  por **aspas triplas**, não crases — crase tripla dentro de Markdown que já está em bloco de
  código quebra a renderização.
- **PowerShell 5.1 + UTF-8 sem BOM**: `Get-Content` sem `-Encoding UTF8` mostra `lição` como
  `liÃ§Ã£o`. O arquivo está certo; a leitura é que não está.
- **Vault Obsidian**: nos documentos do projeto, `![[arquivo]]` é embed do Obsidian e
  `[texto](caminho.md)` é link comum. Ao editar `main.md` e similares, preserve a forma que já
  estiver ali — trocar uma pela outra quebra a renderização de quem lê no Obsidian.
