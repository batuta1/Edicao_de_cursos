# Diário do laboratório

## E0 — Ida e volta sem mudança (2026-10-14) — ✅ PASSOU

**O que foi feito**

1. `ferramentas/extrair.py` → `trabalho/curso_E0.json`
   (4 lições: 19 + 20 + 19 blocos + quiz com 10 questões).
2. `ferramentas/empacotar.py` → `saidas/E0-ida-e-volta.zip`, sem nenhuma edição no JSON.
3. Pacote extraído em `teste/E0/` e aberto no navegador.

**Resultado da serialização**

| Verificação | Resultado |
|---|---|
| Ida e volta do Base64 (decodifica no mesmo JSON) | OK |
| Base64 gerado igual ao original | **SIM** |
| `runtime-data.js` idêntico byte a byte ao original | **SIM** |
| Outros 82 arquivos do pacote | idênticos ao original |

Conclusão: o Python reproduz exatamente a serialização do Rise (JSON compacto, UTF-8, sem escapar
acentos). O pipeline não perde nem altera nada.

**Resultado no navegador**

- Capa, título, descrição e Lição 1 renderizam normalmente.
- Console: **nenhum erro**.
- LMS simulada recebeu `LMSInitialize`, `lesson_status = incomplete`, `exit = suspend`,
  bookmark `index.html#/lessons/6e9c8e52-…` e `suspend_data`.
- Retomada: reabrindo sem `reset`, o curso voltou direto para a Lição 1.

**Como o teste no navegador funciona (descoberta)**

O `index.html` tem `"loadOnlyInLms": true`, mas o código só faz a checagem quando **não** é `file:`:

```js
if (e.loadOnlyInLms && "file:" !== window.location.protocol && !t.lmsPresent) throw ...
```

- Abrindo `scormcontent/index.html` com **duplo clique (`file://`)** o curso abre normalmente — é o
  teste mais simples, e é o que vale para conferência manual.
- O painel de navegador do Claude não executa scripts de `file://`, então ali o teste é feito com um
  servidor local (`python -m http.server`, configurado em `.claude/launch.json` como
  `lab-scorm-teste`) + `teste/lms_mock.html`, uma LMS SCORM 1.2 simulada que carrega o pacote pelo
  `scormdriver/indexAPI.html`. Nenhum arquivo do pacote é alterado para isso.
  - `http://localhost:8765/lms_mock.html?pkg=E0` → abre o pacote de `teste/E0/`
  - `&reset=1` → zera o progresso salvo do aluno simulado

**Próximo:** E1 — inserir um bloco text paragraph.

---

## E1 — Inserir um bloco text paragraph (2026-10-14) — ✅ PASSOU

**Ferramentas criadas**

| Script | Papel |
|---|---|
| `ids.py` | gera UUID v4 / cuid2, reconhece formato, coleta todos os IDs do curso |
| `catalogar_modelos.py` | gerou 10 modelos em `modelos/` a partir do próprio pacote |
| `listar_blocos.py` | lista os blocos de uma lição com índice, para escolher onde inserir |
| `inserir_bloco.py` | modelo + `conteudo_*.json` → bloco com IDs novos, inserido na posição pedida |
| `validar.py` | confere que só houve inserção e que o bloco novo segue o modelo |

**O que foi feito**

```
python inserir_bloco.py ../trabalho/curso_E0.json --modelo ../modelos/text-text-paragraph.json \
    --conteudo ../trabalho/conteudo_E1.json --licao 0 --posicao 1 --saida ../trabalho/curso_E1.json
python validar.py ../trabalho/curso_E1.json --original ../trabalho/curso_E0.json --modelos ../modelos/
python empacotar.py ../trabalho/curso_E1.json --pacote-original ../original/<zip> --pacote-saida ../saidas/E1-text-paragraph.zip
```

- Bloco inserido na Lição 1, entre o 1º heading paragraph e "Ao final desta lição…".
- IDs gerados: bloco `e2yvfmmmw0jrccxmus6jsffz` (cuid2), globalBlockId `bf872a64-…` (uuid),
  item `fnnowd7jb0g2t6cewt2xz8mx` (cuid2).
- HTML: `<p>`, `<strong>`, `<em>`.

**Validação**

- Sanidade: original × original → aprovado, 0 blocos novos.
- **Teste negativo:** cópia estragada de propósito (ID duplicado, `<p style>`, `<h1>`, bloco original
  alterado) → **reprovada com os 4 tipos de problema**. O validador pega o que deve pegar.
- E1 → aprovado: 1 bloco novo, 343 IDs, todos distintos.
- Pacote: 82 arquivos idênticos ao original; só `runtime-data.js` mudou.

**No navegador** (`lms_mock.html?pkg=E1&reset=1`)

- Bloco aparece na posição certa, com negrito e itálico, mesma tipografia e espaçamento dos vizinhos.
- Console: **nenhum erro**.
- Progresso registrado normalmente (`suspend_data` cresce ao rolar a página).
- Botão "Continue" logo abaixo libera a seção seguinte normalmente.
- **Busca interna: encontra o bloco novo** ("pergunta-guia" → 1 resultado na Lição 1). A busca é
  montada a partir do JSON em tempo de execução — ponto em aberto resolvido.

**Achado lateral (já existia no original, não foi causado por nós)**

O knowledgeCheck *multiple response* da Lição 2 (bloco 14, questão `0efc06d2-…`) tem em
`correct`/`corrects` **textos de pergunta** ("Pergunta 2: …", "Pergunta 3: …") em vez de IDs de
alternativa. As respostas certas de fato vêm do `correct: true` de cada alternativa (2 marcadas), e o
bloco tem 12 alternativas que juntam 3 perguntas diferentes — parece resíduo da geração por IA no
Rise. Vale revisar esse bloco pedagogicamente. O validador trata isso como **aviso**, não erro.

**Próximo:** E2 — inserir um bloco impact (ID UUID).

---

## E2 — Inserir um bloco impact / destaque (2026-10-14) — ✅ PASSOU

**Base cumulativa:** a partir de `curso_E1.json` (o curso vai acumulando blocos, como num curso real).
A validação continua sendo contra o original (`curso_E0.json`), então confere os 2 blocos novos juntos.

**Estética do bloco impact — levantada nos 42 impacts dos 5 cursos**

| Padrão do texto | Qtde |
|---|---|
| `<p>EMOJI <strong>Rótulo:</strong> texto</p>` | 23 |
| `<p>EMOJI texto</p>` | 12 |
| texto puro, sem `<p>` | 5 |
| outros | 2 |

Adotado o padrão dominante. Emojis usados nos cursos: 🔑 (regra de ouro), ⚠️ (cuidado),
🏁 (ponto de controle).

**O que foi feito**

```
python inserir_bloco.py ../trabalho/curso_E1.json --modelo ../modelos/text-impact-b.json \
    --conteudo ../trabalho/conteudo_E2.json --licao 0 --posicao 6 --saida ../trabalho/curso_E2.json
```

- Inserido na Lição 1, índice 6: logo após o heading "O que colocar no arquivo vem antes de usar a
  ferramenta" — ou seja, **depois do primeiro Continue** (testa bloco novo em seção bloqueada).
- IDs gerados no formato **UUID** (como manda o modelo): bloco `3190b51c-…`, item `a470c4b1-…`.
- Texto: `<p>🔑 <strong>Regra de ouro:</strong> na dúvida sobre um conteúdo, ele não entra no arquivo. …</p>`

**Validação:** aprovado — 2 blocos novos, 346 IDs, todos distintos. Pacote: só `runtime-data.js` mudou.

**No navegador** (`lms_mock.html?pkg=E2&reset=1`)

- Bloco aparece depois de clicar Continue, na posição certa, com a barra de acento, emoji e rótulo
  em negrito.
- Console: **nenhum erro**. Progresso registrado (`suspend_data` 632 → 858 ao avançar).
- **Comparação pelo DOM com o impact original da mesma lição** ("O sistema pode editar…"): mesmo
  componente (`block-statement`), mesma fonte do tema, 24px, centralizado, mesma cor. Renderização
  idêntica — a única diferença é o `<p>` envolvendo o texto, que é o padrão da maioria dos nossos
  impacts.
- Emoji em UTF-8 passou por todo o pipeline (JSON → Base64 → navegador) sem problema.

**Conclusão:** os dois formatos de ID (cuid2 no E1, UUID no E2) funcionam.

**Próximo:** E3 — inserir um accordion com 3 itens (IDs em dois níveis, `settings` complexo).

---

## E3 — Inserir um accordion com 3 itens (2026-10-14) — ✅ PASSOU

**Base cumulativa:** a partir de `curso_E2.json`.

**Estética do accordion — levantada nos 25 accordions dos 5 cursos**

| Aspecto | Padrão |
|---|---|
| Quantidade de itens | 3 a 6 (4 é o mais comum: 12 de 25) |
| `title` | **sempre texto puro**, sem HTML (100 de 100) |
| `description` | sempre `<p>…</p>`; às vezes com `<strong>` ou `<em>` (6 de 100) |

**O que foi feito**

```
python inserir_bloco.py ../trabalho/curso_E2.json --modelo ../modelos/interactive-interactive-accordion.json \
    --conteudo ../trabalho/conteudo_E3.json --licao 1 --posicao 12 --saida ../trabalho/curso_E3.json
```

- Inserido na **Lição 2** (lição diferente das anteriores), índice 12: logo após "Intervir em
  apresentação existente", cujo texto cita os três elementos de uma edição. O accordion desdobra
  esses três elementos ("O que alterar", "O que preservar", "Onde a edição deve acontecer"), usando
  os exemplos que a própria lição já dá.
- `settings` complexo (8 chaves) copiado do modelo, sem alteração.
- 5 IDs UUID gerados: bloco `b48ea489-…`, globalBlockId `5751bafa-…`, itens `73dbbf87-…`,
  `da842b04-…`, `0d0cb17f-…`.

**Validação:** aprovado — 3 blocos novos acumulados, 351 IDs, todos distintos.

**No navegador** (`lms_mock.html?pkg=E3&reset=1`)

- Navegação pela barra lateral até a Lição 2: OK; bookmark passou a apontar para o ID da Lição 2.
- Após o Continue da Lição 2, o accordion aparece na posição certa, com os 3 títulos.
- Os 3 itens abrem e mostram a descrição com o itálico dos exemplos; vários podem ficar abertos ao
  mesmo tempo; barra de destaque à esquerda do item aberto.
- Console: **nenhum erro**.
- **Comparação pelo DOM com um accordion original da mesma lição** ("Solução de problemas na
  criação"): mesma cadeia de componentes (`blocks-accordion__wrapper → __item → __header → __title`),
  mesma fonte, 18px, peso 700. Única diferença: a classe `--closed` do item original, que estava
  fechado.
- **`suspend_data` não muda ao abrir itens** — nem no accordion novo, nem no original (controle).
  O Rise não registra a abertura de cada item de accordion; só o avanço na lição. Comportamento
  idêntico.

**Conclusão:** IDs em dois níveis funcionam, e `settings` copiado do modelo produz a mesma
aparência do Rise.

**Próximo:** E4 — inserir um knowledgeCheck multiple choice (IDs de alternativas + gabarito).

---

## E4 — Inserir uma questão de verificação (knowledgeCheck multiple choice) (2026-10-14) — ✅ PASSOU

**Base cumulativa:** a partir de `curso_E3.json`.

**Padrão das questões — levantado nas 22 knowledgeCheck multiple choice dos 5 cursos (sem exceção)**

| Aspecto | Padrão |
|---|---|
| Questões por bloco | 1 |
| Alternativas | 4 |
| Corretas | exatamente 1 (`correct: true` na alternativa) |
| Posição da correta | 1ª: 8 · 2ª: 8 · 3ª: 5 · 4ª: 1 |
| `feedbackType` / `type` | `CHOICE` / `MULTIPLE_CHOICE` |
| HTML | **nenhum** — enunciado, alternativas e feedback em texto puro |
| Feedback | em todas as alternativas; começa com "Correto." ou "Não." |

**Ferramentas ajustadas**

- `validar.py`: regras da questão (1 questão, exatamente 1 correta, feedback em todas, texto puro → erro;
  ≠ 4 alternativas → aviso). Comparação de estrutura passou a checar **todos** os elementos de listas,
  não só o primeiro. Regressão: E3 continua aprovado.
- `inserir_bloco.py`: listas do item (`answers`) agora são obrigatórias no conteúdo — antes, se
  faltassem, o bloco herdaria em silêncio as alternativas da questão de exemplo.
- **Bug encontrado pelo validador:** na 1ª tentativa as 4 alternativas saíram **sem ID**, porque o
  gerador só criava ID onde já existia a chave `id`, e as alternativas vêm do conteúdo sem ela. O
  validador reprovou ("estrutura diferente do modelo", "id de alternativa fora do formato").
  Corrigido: todo nível que o modelo diz ter ID recebe ID, exista a chave ou não. `curso_E4.json`
  defeituoso apagado e gerado de novo.

**O que foi feito**

```
python inserir_bloco.py ../trabalho/curso_E3.json --modelo ../modelos/knowledgecheck-knowledgecheck-multiple-choice.json \
    --conteudo ../trabalho/conteudo_E4.json --licao 2 --posicao 15 --saida ../trabalho/curso_E4.json
```

- Inserida na **Lição 3**, índice 15: logo após o accordion "As quatro condições de bom uso".
  Cenário: docente usa planilha de procedência desconhecida → qual condição descumpriu?
  Correta: "Fonte confiável" (2ª posição). Feedbacks baseados no texto do próprio accordion.
- IDs UUID: bloco `c8be3645-…`, questão `7cac2592-…`, alternativas `f1364b96-…`, `54d88e8c-…` (correta),
  `e7ae3a8f-…`, `1e9f5529-…`.

**Validação:** aprovado — 4 blocos novos acumulados, 358 IDs, todos distintos.
**Teste negativo das regras novas:** cópia com 2 corretas, `<p>` no enunciado e feedback vazio →
reprovada com os 3 problemas.

**No navegador** (`lms_mock.html?pkg=E4&reset=1`)

- Navegação até a Lição 3 pela barra lateral; Continue; questão aparece na posição certa.
- **Resposta errada** ("Instrução específica") → "Incorrect" + feedback daquela alternativa, e o
  player marca com ✓ a "Fonte confiável" — leu o gabarito do nosso JSON corretamente.
- "Take again" limpa a questão (e o `suspend_data` muda: o estado da questão é registrado).
- **Resposta certa** → "Correct" + feedback correto.
- Console: **nenhum erro**.

**Retomada (recarregar sem `reset`)**

- O curso volta direto à Lição 3, com a seção após o Continue já liberada. ✅
- A questão nova volta **em branco**, sem a resposta dada.
- **Controle:** a questão **original** da mesma lição ("A apresentação de abertura…"), respondida e
  recarregada do mesmo jeito, também volta em branco. É comportamento do Rise (não restaura respostas
  de knowledgeCheck ao retomar), não efeito da inserção.

**Conclusão:** IDs em três níveis (bloco → questão → alternativas) e o gabarito funcionam. Todos os
4 tipos de bloco planejados para a fase 1 foram inseridos com sucesso.

**Próximo:** E5 — inserir uma sequência que reproduz o padrão de uma lição.

---

## E5 — Inserir uma sequência no padrão das nossas lições (2026-10-14) — ✅ PASSOU

**Base cumulativa:** a partir de `curso_E4.json`.

**Padrões levantados nos 5 cursos**

| Tipo | Padrão |
|---|---|
| heading paragraph | `heading` sempre texto puro (83/83); `paragraph` quase sempre `<p>` |
| list numbered | 3 a 5 itens na maioria; `number` = `"1"`, `"2"`… em sequência; `paragraph` em `<p>` |
| continue | item **idêntico nos 40**: `title "Continue"`, `buttonColor "brand"`, `type ""`, `completeHint` padrão em inglês |

Transições mais comuns entre blocos (como as nossas lições são compostas):
`continue → heading paragraph` (27) · `heading paragraph → accordion` (23) · `paragraph → numbered` (21) ·
`multiple choice → continue` (13) · `numbered → continue` (11). Accordion **sempre** vem depois de um
heading paragraph curto ("Abra cada item…") — por isso a sequência ganhou um 2º heading antes dele.

**Ferramentas**

- `inserir_bloco.py` refatorado: a montagem virou `construir_bloco()` e `localizar_licao()`,
  reutilizáveis. Lista numerada é **numerada automaticamente** se o conteúdo não trouxer `number`
  (senão todos os itens herdariam o "1" do exemplo).
- **Novo `inserir_sequencia.py`:** insere vários blocos em ordem a partir de um único roteiro
  (`trabalho/roteiro_E5.json`: lição, posição e lista de `{modelo, itens}`). Nada é gravado se
  qualquer bloco falhar.
- `validar.py`: regras por tipo — títulos de heading paragraph e de accordion em texto puro; lista
  com `number` em sequência; item do Continue idêntico ao padrão. Regressão: E4 continua aprovado.
  **Teste negativo:** numeração `1,2,7,4`, `<strong>` num heading, `<em>` num título de accordion e
  `completeHint` alterado → reprovado com os 4 problemas.

**O que foi feito**

```
python inserir_sequencia.py ../trabalho/curso_E4.json --roteiro ../trabalho/roteiro_E5.json \
    --modelos ../modelos/ --saida ../trabalho/curso_E5.json
```

Seção nova na **Lição 3**, logo após o primeiro Continue (índices 4–9), aplicando o critério da própria
lição ("o custo de configurar só se paga quando o trabalho volta"):

| Índice | Bloco | Conteúdo |
|---|---|---|
| 4 | heading paragraph | "Antes de configurar: mapeie o trabalho que volta" |
| 5 | list numbered (4) | inventário do semestre, numerado 1–4 automaticamente |
| 6 | heading paragraph | "Três casos para comparar" / "Abra cada item…" |
| 7 | accordion (3) | abertura de disciplina (compensa) · evento pontual (não compensa) · relatório anual (depende) |
| 8 | impact | 🔑 Regra de ouro: se o trabalho não volta, ele não precisa de fluxo… |
| 9 | continue | padrão |

IDs: cuid2 nos blocos de texto e lista, UUID no accordion, impact e continue — cada um no formato do
seu modelo.

**Validação:** aprovado — 10 blocos novos acumulados, 381 IDs, todos distintos.

**No navegador** (`lms_mock.html?pkg=E5&reset=1`)

- Após o primeiro Continue da Lição 3, a seção inteira aparece na ordem do roteiro, com a mesma
  aparência dos blocos originais (lista com círculos numerados, accordion, destaque com barra de acento).
- **O nosso Continue bloqueia o conteúdo original seguinte:** antes do clique, "Skills, Apps e
  Modelos…" não está na página; depois do clique, aparece — junto com a questão do E4 mais abaixo.
- Console: **nenhum erro**.
- **Retomada:** recarregando sem `reset`, o curso volta à Lição 3 com a seção nova **e** o conteúdo
  depois do nosso Continue já liberados — o estado dos dois Continues foi lembrado.

**Conclusão:** dá para compor uma seção inteira de lição, no nosso padrão, a partir de um roteiro em
JSON, sem a plataforma. O Continue inserido se integra ao controle de avanço do Rise como um original.

**Próximo (fase 2):** E6 — inserir `tabs` com modelo vindo de um curso de Word.

---

## E6 — Inserir abas (tabs) com modelo vindo do curso de Word (2026-10-14) — ✅ PASSOU

**Base cumulativa:** a partir de `curso_E5.json`.

**Risco 3 (modelo de outro pacote) — verificação antes de inserir**

Os 7 blocos tabs dos cursos (5 no Word Essentials, 1 no PowerPoint Hands-on, 1 no Word Hands-on —
**3 builds diferentes do player**) têm estrutura de item idêntica (`{id, title, description}`) e
`settings` idêntico — o mesmo `settings` do accordion. Padrões: 2 abas na maioria (comparação de dois
lados), `title` sempre texto puro (18/18), `description` em `<p>` com `<strong>` frequente; sempre
precedidas por um texto terminado em ":" que anuncia a comparação.

**Ferramentas**

- `catalogar_modelos.py`: opção `--somente <variant>` e **não sobrescreve** modelos existentes.
  `trabalho/fonte_word_essentials.json` (extraído só para leitura) → `modelos/interactive-interactive-tabs.json`.
- `validar.py`: título de aba em texto puro; **parágrafos de descrição de accordion/tabs precisam de
  `<p></p>` vazio entre eles** (regra nova, ver abaixo).
- **Novo `teste/servidor_sem_cache.py`** (substitui o `http.server` no `.claude/launch.json`), que manda
  o navegador não guardar cache (ver abaixo).

**O que foi feito**

```
python inserir_sequencia.py ../trabalho/curso_E5.json --roteiro ../trabalho/roteiro_E6.json \
    --modelos ../modelos/ --saida ../trabalho/curso_E6.json
```

Lição 2, índices 14–15, logo após "As seis informações de um pedido completo" (texto que compara a
instrução de criação com a de edição): parágrafo "Compare, nas abas, o que cada tipo de instrução
recorta das seis informações:" + tabs "Instrução de criação" / "Instrução de edição". Conteúdo só
reorganiza o que o texto anterior já afirma.

**Validação:** aprovado — 12 blocos novos acumulados, 388 IDs, todos distintos.

**Dois tropeços no caminho (e o que se aprendeu)**

1. **Parágrafos colados.** Na 1ª versão, cada aba tinha dois `<p>` seguidos e eles apareceram sem
   espaço entre si. Levantamento: em descrições de accordion e tabs com mais de um parágrafo, os
   nossos cursos **sempre** põem um `<p></p>` vazio entre eles (accordion 39/39, tabs 10/10; nenhum
   caso de parágrafos colados). Virou regra do validador — que reprovou a 1ª versão — e o roteiro foi
   corrigido. Arquivos da 1ª versão apagados e o E6 gerado de novo.
2. **Cache do navegador.** Depois de regerar, a tela continuou igual. Investigação: o servidor já
   entregava o arquivo novo (conferido com `fetch` sem cache), mas o navegador usava a cópia antiga
   (`transferSize: 0`; 180162 bytes no cache × 180178 no disco — a diferença são os dois `<p></p>`).
   Correção na raiz: `servidor_sem_cache.py`. Como a cópia antiga já estava guardada, o mesmo
   `E6-tabs.zip` foi extraído numa pasta nova, `teste/E6b/`. **Lição: sempre extrair um pacote
   regerado em pasta de nome novo, ou servir sem cache desde o início.**

**No navegador** (`lms_mock.html?pkg=E6b&reset=1`)

- Após o Continue da Lição 2, o parágrafo e as abas aparecem na posição certa, antes do bloco original
  "Edição delimitada".
- As duas abas alternam corretamente; rótulos em negrito; espaço entre os parágrafos (o `<p></p>`
  vira uma linha de 24px no DOM).
- Console: **nenhum erro** vindo do E6b (o único erro listado na aba é o antigo, do 1º acesso ao E0
  direto pelo `index.html`).
- **Comparação pelo DOM com abas originais do curso Word** (`teste/word_original/`, Lição 2, "Copiar e
  colar"): mesma cadeia de componentes (`blocks-tabs__header-item → __header → __header-wrap →
  block-card`; `blocks-tabs__description`), título 12px negrito em maiúsculas, corpo 16px, espaçador
  de 24px. Diferem só fonte e cor de destaque — que vêm do **tema de cada curso**. O bloco trazido do
  Word assumiu a aparência do curso de PowerPoint.

**Conclusão:** modelo vindo de outro pacote (outro build do player) funciona. A aparência vem do tema
do curso de destino, não do curso de onde o modelo saiu.

---

## E7a — Bloco HTML próprio: um infográfico (2026-10-14) — ✅ PASSOU

**Base cumulativa:** a partir de `curso_E6.json`.

**O que muda em relação aos anteriores:** é o primeiro bloco **sem exemplar** em nenhum curso nosso. O
modelo foi montado a partir do esquema do player (`lib/rise/f81f670e.js`, `BlockHTML`) — ver
ESTRATEGIA, "Investigação: bloco com HTML próprio".

- `modelos/html-html-inline.json` (escrito à mão): `type/family "html"`, `variant "inline"`,
  `settings {autoResize: true, hasCustomCompletion: false, height: 40, width: "1"}`, item `{id, srcdoc}`.
  `metadata` vazio (o esquema permite; não declara `createdVia: "ai"` num bloco que não veio de IA).
- O interruptor `htmlBlocksDisabled` do player só se aplica ao Quick Share em período de teste do Rise
  (mensagem no código: proteção contra phishing). Não afeta pacote exportado.

**Ferramentas**

- `inserir_sequencia.py`: campo pode vir de arquivo com `"@arquivo:<caminho>"` — o HTML fica em
  `trabalho/infografico_E7.html`, editável e abrível sozinho no navegador.
- `validar.py`: o `srcdoc` fica fora da regra de tags de texto rico; regras próprias — documento
  completo (`<html>` e `<body>`) e **autocontido** (sem `src`/`href` para http/https). Regressão: E6 OK.

**O infográfico** (`trabalho/infografico_E7.html`): "O ciclo de produção" — ponto de partida (decidir o
que entra no arquivo), 4 etapas em cards (criar, editar, entender, refinar) e faixa "Revisão em seis
pontos". Todo o conteúdo vem do texto da Lição 3. HTML + CSS + SVG embutidos, sem nenhum recurso
externo; azul do curso (`#152f4d`); grade responsiva; animação de entrada desligada para quem prefere
menos movimento. Inserido na Lição 3, índice 18, entre "Um ciclo, não procedimentos isolados" e o
process original "O ciclo de produção".

**Validação:** aprovado — 13 blocos novos acumulados, 391 IDs, todos distintos.

**No navegador** (`lms_mock.html?pkg=E7&reset=1`)

- O player reconheceu o bloco: criou o iframe do sandbox com as classes
  `block-code block-code--auto-resize block-code--width-medium` — leu `autoResize` e `width` do JSON.
- O HTML carregou dentro do iframe (`srcdoc` presente; título "O ciclo de produção") e a animação rodou.
- **Altura automática:** no celular (437px), bloco = 939px = altura do conteúdo, sem barra de rolagem
  interna. Na tela larga (1280px), recalculou sozinho para 580px = altura real do infográfico.
- **Responsivo:** 2 × 2 no celular, 4 etapas lado a lado na tela larga.
- Console: **nenhum erro** do bloco ou do sandbox.
- Observação: `width "1"` (médio) dá 1100px numa tela de 1280px — mais largo que a coluna de texto.
  Para alinhar ao texto, `width "0"`.

**Não verificado:** se o texto de dentro do bloco HTML entra na busca do curso (provavelmente não — o
conteúdo vive no `srcdoc`, renderizado em iframe). `hasCustomCompletion` (E7b) e variant `cdn` (E7c).

**Conclusão:** dá para inserir um bloco com estética HTML **totalmente livre** num SCORM do Rise, sem a
plataforma, e ele convive com os blocos nativos (Continue antes e depois funcionando).

---

## E7b — Bloco HTML interativo que trava o Continue até ser concluído (2026-10-14) — ✅ PASSOU

**Base cumulativa:** a partir de `curso_E7.json`.

**O que o código do player mostrou antes de montar**

- Item do Continue (esquema): `type` = `""` (não exige nada — o que os 40 Continues dos nossos cursos
  usam), `"completeBlock"` (exige o **bloco logo acima** concluído) ou `"completeAll"` (todos acima).
  `canContinue` com `completeBlock` = progresso do último bloco acima com `isComplete`.
- Modos de conclusão por tipo de bloco: `view` (concluído ao ser visto), `step` (cada item exige
  interação) e `step-if`. **`"html/inline"` e `"html/cdn"` usam `step-if`, que só vale quando
  `settings.hasCustomCompletion === true`.** Nesse caso o bloco só conclui quando o sandbox recebe
  `{type: "complete"}` do HTML e chama `onStep` com o id do item.

**Ferramentas**

- Modelo do bloco HTML ganhou `settings_ajustaveis` (`autoResize`, `hasCustomCompletion`, `height`,
  `width "0"|"1"|"2"`). No roteiro, um bloco pode trazer `"settings": {...}` — só essas chaves, com
  esses tipos; qualquer outra é **recusada na inserção**.
- `validar.py`: settings comparadas respeitando os ajustáveis; Continue aceita `type` `""`,
  `completeBlock` ou `completeAll` (o resto do item continua igual ao padrão).
- **Todas as ferramentas agora leem arquivos com ou sem BOM** (`utf-8-sig`). Descoberto no teste
  negativo: o PowerShell 5.1 grava UTF-8 com BOM e o roteiro foi recusado pelo motivo errado. O Bloco de
  Notas do Windows pode fazer o mesmo.
- **Testes negativos:** setting inexistente (`corDeFundo`) → recusado na inserção, nada gravado;
  `width "5"` e Continue `type "completeQualquer"` → validador reprova os dois.

**O que foi feito**

`trabalho/atividade_E7b.html` — atividade "Monte o ciclo": o aluno clica nas etapas na ordem
(criar → editar → entender → refinar); distrator "Revisar (5ª etapa)", porque a lição diz que a
verificação **não** é uma quinta operação; dicas de erro tiradas do texto da lição; ao completar, envia
`window.parent.postMessage({type: 'complete'}, '*')` uma única vez. Botões reais (teclado), feedback
com `aria-live`.

`trabalho/roteiro_E7b.json` — Lição 3, índices 19–20, logo após o infográfico do E7:
bloco HTML com `"settings": {"hasCustomCompletion": true}` + Continue com `"type": "completeBlock"`.

**Validação:** aprovado — 15 blocos novos acumulados, 397 IDs, todos distintos.

**No navegador** (`lms_mock.html?pkg=E7b&reset=1`, layout de computador)

- **Antes da atividade:** o Continue aparece **travado, com cadeado** e o aviso "Complete the content
  above before moving on."; o conteúdo seguinte ("Resumo do ciclo integrado") **não está na página**.
- Distrator → "A revisão não é uma quinta etapa…"; etapa fora de ordem → "Ainda não. O ciclo começa
  pelo rascunho…". Continue segue travado.
- **Ordem certa → "Ciclo completo…" e o Continue destrava sozinho** (cadeado some, vira o botão
  azul); `suspend_data` 1039 → 1047 (conclusão gravada).
- Clique no Continue → conteúdo original seguinte liberado. Console: **nenhum erro**.
- **Retomada** (recarregar sem `reset`): o curso lembra que o bloco foi concluído — conteúdo seguinte
  liberado, sem aviso de travado. **A atividade volta em branco**: o Rise guarda a conclusão, não o
  estado interno do HTML. Mesmo comportamento das knowledgeChecks nativas (E4). Se for importante
  mostrar a atividade já resolvida na volta, o próprio HTML teria de guardar o estado (ex.:
  `localStorage`, que vale só naquele navegador) — não implementado.

**Conclusão:** um bloco HTML próprio pode ser uma **atividade que participa do controle de avanço do
Rise**, como um bloco nativo interativo.

---

## E7c — Bloco HTML em pasta própria (variant cdn) + arquivos novos no manifest (2026-10-14) — ✅ PASSOU

**Base cumulativa:** a partir de `curso_E7b.json`.

**Do esquema do player:** `media: { sandbox: { src, srcName } }` (`MediaSandboxRecord`). O player
carrega `../../assets/<src>/index.html` a partir de `lib/sandbox/` — ou seja,
`scormcontent/assets/<src>/index.html`. Mesma convenção das imagens do curso, que o JSON referencia
pelo nome relativo a `assets/`. O significado exato de `srcName` não foi verificado (usado o nome da pasta).

**Ferramentas**

- `modelos/html-html-cdn.json` (do esquema), com `campos_obrigatorios: ["media"]` — sem isso o bloco
  herdaria a pasta-marcador do modelo. `inserir_bloco.py` passou a respeitar `campos_obrigatorios`.
- `validar.py`: `media.sandbox.src` = nome simples de pasta (letras, números, `-`, `_`); `srcName`
  preenchido e sem marcador.
- **`empacotar.py` reescrito com `--anexar PASTA=NOME`:**
  - copia a pasta para `scormcontent/assets/NOME/` e registra cada arquivo no `imsmanifest.xml`
    no formato exato do Rise (`<file href="…" />` + linha em branco, LF);
  - recusa: nome inválido, pasta sem `index.html`, arquivo que já exista no pacote, e qualquer
    referência externa (`src`/`href`/`url(`/`@import` para http/https) em .html/.css/.js/.svg;
  - recusa se algum bloco `html/cdn` do curso apontar para pasta que não estará no pacote;
  - grava primeiro um `.parcial`, confere tudo e só então renomeia — falha não deixa arquivo para trás;
  - confere: originais idênticos byte a byte (exceto `runtime-data.js` e manifest), manifest **só
    ganhou** as linhas dos anexos (removidas, volta a ser o original), anexos gravados byte a byte.
  - **Regressão:** ida e volta do E0 com o empacotar novo → continua idêntico byte a byte.
  - **Testes negativos:** bloco cdn sem `--anexar` → recusado; pasta com fonte do Google Fonts
    (`https://`) → recusado. Nos dois, nem zip nem `.parcial` gerados.

**O que foi feito**

`trabalho/checklist_E7c/` — "Checklist da revisão em seis pontos", em 4 arquivos separados com
referências relativas: `index.html`, `estilo.css`, `script.js`, `revisao.svg`. Perguntas tiradas do
accordion "Refinar e revisar: os seis pontos" (Lição 2). Barra de progresso, contagem, mensagem final e
botão "Recomeçar". **Não** trava o Continue (`hasCustomCompletion: false`), para isolar a novidade.

```
python inserir_sequencia.py ../trabalho/curso_E7b.json --roteiro ../trabalho/roteiro_E7c.json \
    --modelos ../modelos/ --saida ../trabalho/curso_E7c.json
python empacotar.py ../trabalho/curso_E7c.json --pacote-original ../original/<zip> \
    --pacote-saida ../saidas/E7c-html-pasta.zip --anexar ../trabalho/checklist_E7c=checklist-revisao
```

Lição 2, índice 21: depois do impact "Nenhuma conferência de números detecta mudanças de sentido…".

**Validação:** aprovado — 16 blocos novos acumulados, 400 IDs, todos distintos.
**Pacote:** 87 arquivos (83 originais + 4 anexados); manifest com as 4 linhas novas.

**No navegador** (`lms_mock.html?pkg=E7c&reset=1`, layout de computador)

- O player criou o bloco (`block-code--auto-resize block-code--width-medium`) e o iframe interno com
  `src="../../assets/checklist-revisao/index.html"`.
- **Os 3 arquivos referenciados pelo index.html carregaram da pasta anexada** (status 200):
  `estilo.css`, `revisao.svg`, `script.js`. Imagem visível, CSS aplicado, JS rodando.
- Marcando os 6 pontos: barra a 100% (medida: 870 de 870px), "6 de 6 pontos conferidos" e mensagem
  final. **A altura do bloco acompanhou o conteúdo**: 707px → 791px quando a mensagem final apareceu.
- Console: **nenhum erro**.

**Não verificado:** abrir este pacote por duplo clique (`file://`). O código do sandbox tem tratamento
específico para `file:` (não faz a checagem HEAD do arquivo), então deve funcionar — mas só foi testado
via servidor local.

**Conclusão:** dá para colocar uma mini-aplicação completa (HTML, CSS, JS e imagens em arquivos
separados) dentro do pacote, registrada no manifest, e exibi-la como bloco do curso — sem a plataforma.

---

## Skill `inserir-blocos-scorm` criada (2026-10-14)

Tudo o que funcionou foi organizado em `Skills/inserir-blocos-scorm/` (repositório da equipe), com
`.skill` e `.zip` para instalar. Contém: `SKILL.md` (fluxo em 10 passos, regras e por quê,
verificação), 9 scripts, 13 modelos, ferramentas de teste no navegador, 7 exemplos testados e 4
referências (padrões por tipo, bloco HTML, funcionamento do Rise, armadilhas).

**Nova ferramenta: `verificar_scorm.py`** — consistência do pacote .zip inteiro (zip íntegro,
manifest × arquivos, versão nos 3 lugares, curso decodifica, estrutura e IDs, tipos de bloco ×
player do pacote, regras de questões/Continue, arquivos citados, comparação com o original).
- Os 5 pacotes reais da equipe: 0 erros (só o aviso conhecido da múltipla resposta).
- Pacote quebrado de propósito com 6 defeitos: os 6 detectados (7 erros, 4 avisos).
- Dois falsos positivos corrigidos durante o teste: caminhos `rise/courses/...` não são arquivos
  exportados; aviso de gabarito duplicado.

**`inserir_bloco.py`:** campos do item que são lista **ou objeto** passaram a ser obrigatórios no
conteúdo (antes, só listas) — evita herdar em silêncio o `front`/`back` do flashcard de exemplo.

**Teste da skill seguindo só o SKILL.md, num curso que o laboratório nunca usou** (Word Hands-on,
outro build do player; pasta `teste-da-skill/`): seção nova no fim da Lição 1 (Continue → título →
accordion → questão). Validar, empacotar e verificar: aprovado sem avisos. No navegador: seção liberada
pelo Continue, tema do curso Word aplicado, parágrafos com espaçador, questão corrigindo ("Correct"),
console sem erros. Os modelos tirados do curso de PowerPoint servem para os outros cursos.
