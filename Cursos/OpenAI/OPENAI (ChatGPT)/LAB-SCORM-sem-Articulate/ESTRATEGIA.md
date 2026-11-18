# Laboratório — inserir blocos novos em SCORM do Rise 360 sem a plataforma Articulate

**Status:** só planejamento. Nada foi modificado ainda.
**Pacote de teste:** `original/chatgpt-powerpoint-essentials-scorm12-1FExiyZi-REVISADO.zip`
(cópia idêntica — SHA-256 `93E96163…C3DF215C` — do arquivo em `ChatGPT PowerPoint/essentials/`).

## Escopo

- **Meta:** inserir **blocos novos**, com a estética dos nossos cursos, num SCORM exportado do Rise,
  sem precisar editar nada na plataforma online da Articulate.
- **Teste:** só no navegador, por enquanto. Critério: **o curso abre e o bloco novo aparece e funciona**.
  (A equipe tem LMS própria; teste em LMS fica para depois.)
- **Fora do escopo agora:** editar/mover/remover blocos existentes, mexer em quiz final, criar lições,
  mudar tema.
- **A skill `revisar-curso-scorm` não é tocada.** Todas as ferramentas deste laboratório são arquivos
  novos dentro de `ferramentas/`. Uma skill nova só será criada **no final**, quando soubermos que
  conseguimos montar um curso.

## Por que este pacote

Tem a maior variedade de blocos entre os 5 cursos revisados e os dois formatos de ID:

| Tipo de bloco | Qtde | Formato do `id` |
|---|---|---|
| text (heading paragraph / paragraph), list numbered, flashcard | 32 | cuid2 (24 chars `a-z0-9`, começa com letra) |
| impact, continue, accordion, process, knowledgeCheck (choice/response) | 36 | UUID v4 |
| Questões do quiz final | 10 | UUID v4 |

## O que já sabemos

1. O curso inteiro é um JSON em Base64 dentro de `scormcontent/runtime-data.js`.
2. **IDs são aleatórios**, não derivados de conteúdo, posição ou data. O player não valida formato.
   Requisito real: **unicidade** + **referências coerentes** (`correct`/`corrects` → `answers[].id`).
3. **Correção da investigação anterior:** em memória o player indexa o progresso por ID, mas o que ele
   **grava no LMS** (`suspend_data`) é indexado pela **posição** da lição e do bloco
   (`decodeCourseProgress` lê `lessons[String(index)]`). Ver risco 2.
4. Bookmark no LMS = `index.html#/lessons/<lessonId>`.
5. O `imsmanifest.xml` lista todo arquivo de conteúdo. Bloco novo **sem imagem** não exige mexer no
   manifest — só o `runtime-data.js` muda.

---

## Riscos verificados e como resolver

### Risco 1 — Estrutura de cada bloco (`settings`, `metadata`, HTML)

**Verificação:** comparei os 346 blocos dos 5 cursos, tipo por tipo.

**Resultado — muito mais regular do que parecia:**

- Todos os blocos de conteúdo têm exatamente as mesmas 8 chaves:
  `id, type, family, variant, settings, items, metadata, globalBlockId`.
  (Questões do quiz final têm outro formato, mas estão fora do escopo.)
- **Cada tipo tem um único formato de item** (ex.: text paragraph → `{id, paragraph}`; accordion →
  `{id, title, description}`; process → `{id, type, title, description, isHidden}`).
- **`settings` é constante dentro de cada tipo** — mesmo valor em todos os blocos de todos os cursos:

  | Tipo | `settings` |
  |---|---|
  | text (paragraph, heading paragraph), impact, knowledgeCheck | `{}` |
  | list numbered, flashcard | `{"paddingTop": 0}` |
  | continue | `{"v": 2}` |
  | accordion, tabs, process | `{"v":2, "paddingTop":0, "paddingBottom":3, "paddingLinked":true, "zoomOnClick":true, "audioPosition":"bottom", "markerColorContrast":"AUTO", "snippetColorContrast":"AUTO"}` |

- **`metadata`** só varia em uma coisa: às vezes tem `contentValidation: {pass: true, version: "1.14x.0"}`,
  às vezes não (110 blocos não têm, e funcionam). Ou seja, é opcional.
- **HTML usado nos textos:** apenas `<p> <strong> <em> <br> <ul> <li> <span>`, **sem nenhum atributo**
  (sem `class`, sem `style`).
- **A estética não está no bloco, está no curso:** cores, fontes, navegação e cantos arredondados vêm de
  `course.theme` (ex.: acento `#152f4d`, `blockCorners: ROUNDED`, `navigationType`). Um bloco novo
  herda automaticamente a aparência do curso onde é inserido.

**Como resolver:**

1. **Catálogo de modelos** extraído dos nossos próprios cursos: um JSON por tipo, com `settings`
   e `metadata` exatamente como o Rise gera, e os IDs trocados por marcadores. Inserir bloco =
   copiar o modelo + preencher texto + gerar IDs.
2. Para novos blocos, usar `metadata: {"createdVia": "ai"}` (forma mínima já comprovada em 110 blocos).
3. **Regra de HTML:** só as 7 tags acima, sem atributos. O validador recusa qualquer outra coisa.
4. **"Nossa estética"** = (a) inserir em curso que já tem nosso tema e (b) usar só os tipos de bloco e
   os padrões de composição que já usamos. Se a equipe quiser estilos por bloco que nunca usamos
   (fundo colorido, espaçamento diferente), os valores dessas opções **não existem nos nossos dados** —
   ver "Curso-catálogo" abaixo.

### Risco 2 — Mudar IDs / progresso de alunos

**Verificação:** li no código do player como o progresso é salvo e restaurado
(`encodeCourseProgress` / `decodeCourseProgress` em `scormcontent/lib/rise/53ad29dd.js`).

**Resultado:**

- O progresso gravado no LMS é **por posição, não por ID**. Ao abrir o curso, o player monta o
  progresso a partir das lições atuais e encaixa o que estava salvo **pelo índice**.
- Consequência 1: **trocar IDs** de blocos existentes praticamente não afeta o progresso salvo
  (ainda assim, não faremos isso — não há motivo).
- Consequência 2, a que importa: **inserir um bloco no meio de uma lição desloca os índices** dos
  blocos seguintes. Um aluno que já tinha progresso naquela lição pode ter o progresso "encaixado" no
  bloco errado.
- A versão do pacote (`cpv`) muda a cada exportação; com `resetLearnerData: false` (nosso caso) o
  player só registra aviso e mantém o progresso antigo — ou seja, **não protege** contra o
  deslocamento.

**Como resolver:**

1. **Nunca alterar IDs existentes.** Blocos novos sempre com IDs novos, gerados e conferidos contra
   todos os IDs do curso (unicidade).
2. **Curso ainda não publicado (caso principal):** risco zero — não há aluno com progresso. Inserir
   onde quiser.
3. **Curso já publicado com alunos:** subir como **curso/versão nova no LMS** (matrícula nova), ou
   inserir blocos **apenas no fim** das lições. Fica registrado como regra, não precisa de teste agora.

### Risco 3 — Player diferente em cada pacote

**Verificação:** procurei, no JavaScript do player de cada um dos 5 pacotes, os nomes dos tipos de
bloco do Rise — inclusive os que **nenhum** dos nossos cursos usa (timeline, labeled graphic, sorting,
scenario, gallery, quote, chart, etc.).

**Resultado:**

- **Todo pacote traz o player completo do Rise** (~8,2 MB de JS em todos), com o código de **todos** os
  tipos de bloco, usados ou não. Ex.: o pacote PowerPoint Essentials não tem nenhum bloco `tabs`, mas
  o código de `tabs`, `timeline`, `sorting` etc. está lá, em contagem idêntica aos outros pacotes.
- As diferenças entre builds são mínimas (o de Word Essentials varia em poucas ocorrências).
- **O risco real não é o player, é o JSON:** para tipos que não temos em nenhum curso não temos
  exemplo do formato, e adivinhar campos é o que quebra.

**Como resolver:**

1. **Fase 1 (agora):** só inserir tipos que já existem **no próprio pacote de teste**, usando modelos
   **dele mesmo**.
2. **Fase 2:** tipos que existem em outros cursos (ex.: `tabs`, dos cursos de Word) — modelo vindo de
   outro pacote, testado no navegador antes de usar.
3. **Tipos que não temos em lugar nenhum / estilos por bloco que nunca usamos → "Curso-catálogo":**
   montar **uma única vez** no Rise um curso com um bloco de cada tipo desejado, já com a estética da
   equipe, e exportá-lo em SCORM. Ele vira a biblioteca de modelos permanente. A plataforma é usada uma
   vez para gerar modelos, e nunca mais para montar curso.

---

## Princípios

- **O `.zip` em `original/` nunca é alterado.** Cada experimento gera um `.zip` novo em `saidas/`.
- **Um experimento = um tipo de inserção.** Se quebrar, sabemos exatamente o quê.
- **Nunca escrever bloco do zero** — sempre a partir de modelo do catálogo.
- **Validar antes de empacotar; abrir no navegador antes de considerar pronto.**

## Estrutura da pasta (criada conforme os passos avançam)

```
LAB-SCORM-sem-Articulate/
├── ESTRATEGIA.md       ← este documento
├── original/           ← .zip intocado
├── trabalho/           ← curso.json desserializado + versões com blocos inseridos
├── modelos/            ← catálogo: 1 bloco real de cada tipo (JSON com marcadores no lugar dos IDs)
├── ferramentas/        ← scripts .py novos (a skill existente não é usada nem alterada)
├── teste/              ← LMS simulada + pacote extraído para abrir no navegador
├── saidas/             ← .zip gerados, um por experimento
└── DIARIO.md           ← o que foi tentado, resultado, prints
```

## Ferramentas a construir (todas novas, em `ferramentas/`)

| Script | Função |
|---|---|
| `extrair.py` | `.zip` → `trabalho/curso.json` formatado e legível |
| `catalogar_modelos.py` | Salva em `modelos/` um bloco real de cada tipo, com `{{ID}}`, `{{TEXTO}}` etc. no lugar de IDs e textos |
| `ids.py` | Gera UUID v4 e ID estilo cuid2 (1 letra + 23 `a-z0-9`), escolhe o formato pelo tipo e garante que não colide com nenhum ID do curso |
| `inserir_bloco.py` | Pega um modelo, preenche os textos, gera **todos** os IDs (`id`, `globalBlockId`, `items[].id`, `answers[].id`) e insere na lição/posição indicada |
| `validar.py` | IDs únicos; formato do ID compatível com o tipo; chaves do bloco = chaves do modelo; `settings` = do modelo; HTML só com as 7 tags permitidas e sem atributos; gabarito de knowledgeCheck aponta para alternativa existente. Sai com código 1 se falhar |
| `empacotar.py` | Serializa em Base64 (com conferência de ida e volta), troca só o `runtime-data.js` e gera `.zip` novo em `saidas/` |
| `teste/servidor_sem_cache.py` | Servidor local de teste que impede o navegador de reaproveitar versões antigas dos arquivos (ver DIARIO, E6). Mesmo assim, extrair cada pacote regerado em pasta de nome novo |
| `teste/lms_mock.html` | LMS SCORM 1.2 simulada (`window.API`) que abre o `scormdriver/indexAPI.html` num iframe. Usado no painel de navegador do Claude (que não executa `file://`). Para conferência manual, basta abrir `scormcontent/index.html` com duplo clique — via `file://` o pacote pula a checagem de LMS (ver DIARIO, E0) |

## Sequência de experimentos

Critério de cada um: `validar.py` OK → curso abre no mock → bloco novo aparece na posição certa → sem
erro no console do navegador → dá para chegar ao fim da lição.

| # | Experimento | O que prova |
|---|---|---|
| **E0 ✅** | **Ida e volta sem mudança:** extrair e reempacotar sem inserir nada. JSON idêntico e curso abrindo no mock | Pipeline e mock funcionam. Sem isso, nada adiante vale |
| E1 ✅ | Inserir 1 bloco **text paragraph** (ID cuid2, 1 item) | O caso mais simples |
| E2 ✅ | Inserir 1 **impact** (ID UUID) | Formato UUID |
| E3 ✅ | Inserir 1 **accordion** com 3 itens | IDs em dois níveis (bloco + itens), `settings` complexo |
| E4 ✅ | Inserir 1 **knowledgeCheck** multiple choice | IDs de alternativas + coerência do gabarito; checar que corrige certo |
| E5 ✅ | Inserir uma **sequência** que reproduz nosso padrão de lição (ex.: heading paragraph → list → accordion → impact → continue) | "Nossa estética" na prática, e o `continue` bloqueando até completar o conteúdo acima |
| E6 ✅ | Inserir **tabs** com modelo vindo de um curso de Word | Modelo de outro pacote (risco 3, fase 2) |

## Investigação: bloco com HTML próprio (E7a ✅, E7b ✅ e E7c ✅ testados — ver DIARIO)

Pergunta: dá para inserir um bloco com estética HTML qualquer, fora dos tipos prontos?

**O que o código do player mostra (2026-10-14, só leitura):**

- O Rise tem um tipo de bloco oficial para isso — o **bloco de código/HTML** (`block-code` no player).
  Nenhum dos nossos cursos usa, mas o renderizador está em todo pacote.
- `scormcontent/lib/rise/f81f670e.js` contém o **esquema JSON de todos os blocos do Rise** (inclusive
  os que nunca usamos). O do bloco HTML:
  ```
  type "html", family "html", variant "inline" | "cdn"
  settings: { autoResize: bool, hasCustomCompletion: bool, height: número, width }
  items: [ { id, srcdoc: "<!doctype html>…" } ]                       ← variant inline
  items: [ { id, media: { sandbox: { src: "<pasta>" } } } ]           ← variant cdn: assets/<pasta>/index.html
  ```
- Quem desenha o bloco é `lib/sandbox/sandbox.html`: um iframe que recebe o HTML (`srcDoc`) ou carrega
  `../../assets/<pasta>/index.html`. Com `autoResize`, a altura acompanha o conteúdo; sem ele, a altura
  vem de `settings.height` (em décimos de rem). Funciona também via `file://`.
- **Conclusão do bloco:** com `hasCustomCompletion`, o bloco só conta como concluído quando o HTML
  envia `window.parent.postMessage({type: "complete"}, "*")` — dá para fazer interações próprias que
  travam o Continue até o aluno terminar.
- Existe um interruptor `htmlBlocksDisabled` no player; ele **não aparece** nos dados deste curso.

**Consequências**

- O HTML roda **isolado num iframe**: não herda fonte nem cor do tema do curso. A estética é 100% a do
  HTML — o que é exatamente a liberdade pedida, mas significa trazer as próprias fontes/cores.
- Variant `inline`: HTML + CSS + JS num único texto, dentro do JSON — só muda o `runtime-data.js`.
  Variant `cdn`: uma pasta com `index.html`, imagens etc. em `assets/` — exige mexer no manifest.
- **O esquema resolve o risco 1 para qualquer tipo de bloco** sem precisar do "curso-catálogo": dá
  para montar o JSON de tipos que nunca usamos a partir dele (com teste no navegador, como sempre).
- Não verificado: se HTML com `style`/`class` dentro dos campos de texto comuns é preservado ou limpo
  pelo editor do Rise (`rise-tiptap`). O caminho certo para HTML livre é o bloco HTML.

**Plano do E7:** (a) bloco HTML `inline` simples, com `autoResize` → abre? altura certa? (b) mesmo bloco
com `hasCustomCompletion` → o Continue só libera após o `postMessage`? (c) variant `cdn` com uma pasta
em `assets/` + entrada no manifest.

## Pontos ainda em aberto (não verificados)

- ~~**Busca interna**~~ — **resolvido no E1:** a busca é montada do JSON em tempo de execução e
  encontra blocos novos.
- **knowledgeCheck multiple response:** o modelo catalogado veio de um bloco com `correct`/`corrects`
  preenchidos com texto de pergunta (resíduo do Rise; ver DIARIO, E1). Antes de inserir esse tipo,
  entender qual campo o player usa de fato. No E4 usaremos *multiple choice*, que não tem esse problema.
- **Retomada de knowledgeCheck (verificado no E4):** ao retomar o curso, o Rise não restaura a
  resposta dada nas questões de verificação — nem nas originais, nem nas inseridas. Comportamento do
  player, não da inserção.
- **Respostas de knowledgeCheck no relatório do LMS:** não verificado se o ID da questão vai para o
  relatório de interações do SCORM. Irrelevante para o teste no navegador.
- **Bloco com imagem:** exige arquivo em `assets/` + entrada no manifest + formato da referência no
  JSON. Fica para depois do E6.

## Decisão que fica com você

**Curso-catálogo:** vale a pena montar uma vez no Rise um curso com todos os tipos de bloco e estilos
que a equipe quer usar, para servir de biblioteca de modelos? Não é necessário para E0–E6, mas é o
caminho mais seguro para qualquer tipo/estilo que ainda não temos em nenhum curso.
