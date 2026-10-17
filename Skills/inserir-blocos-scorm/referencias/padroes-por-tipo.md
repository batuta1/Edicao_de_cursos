# Padrões por tipo de bloco — a estética dos cursos da equipe

Levantados em 5 cursos da equipe exportados do Rise (ChatGPT Codex, PowerPoint e Word; Essentials e
Hands-on), 346 blocos. "Nossa estética" = **o tema do curso** (cores, fontes, navegação, que vêm de
`course.theme` e valem para todo bloco nativo inserido) **+ estes padrões de escrita e composição**.
O `validar.py` reprova o que está marcado como regra.

## Sumário

1. Tabela de modelos
2. Regras por tipo (com exemplos de itens)
3. Como as lições são compostas
4. HTML permitido em textos

---

## 1. Tabela de modelos (`<skill>/modelos/`)

| Modelo | Bloco | ID | Campos de cada item no roteiro | Testado no navegador |
|---|---|---|---|---|
| `text-text-paragraph.json` | Parágrafo | cuid2 | `paragraph` | ✅ |
| `text-text-heading-paragraph.json` | Título + parágrafo | cuid2 | `heading`, `paragraph` | ✅ |
| `list-list-numbered.json` | Lista numerada | cuid2 | `paragraph` (o `number` é automático) | ✅ |
| `text-impact-b.json` | Destaque (impact) | UUID | `paragraph` | ✅ |
| `interactive-interactive-accordion.json` | Accordion | UUID | `title`, `description` | ✅ |
| `interactive-interactive-tabs.json` | Abas | UUID | `title`, `description` | ✅ (modelo veio do curso Word) |
| `knowledgecheck-knowledgecheck-multiple-choice.json` | Questão de múltipla escolha | UUID | `title`, `answers` [`title`, `correct`, `feedback`] | ✅ |
| `divider-continue-continue.json` | Continue | UUID | `title` ("Continue") e, opcional, `type` | ✅ |
| `html-html-inline.json` | HTML embutido | UUID | `srcdoc` (documento HTML inteiro) | ✅ |
| `html-html-cdn.json` | HTML em pasta | UUID | `media` → `{"sandbox": {"src": PASTA, "srcName": NOME}}` | ✅ |
| `interactive-flashcard-flashcard.json` | Flashcards | cuid2 | `front`, `back` (ver o item_exemplo) | ⚠️ não testado |
| `interactive-interactive-fullscreen-process.json` | Process (passo a passo) | UUID | `title`, `description` e **sempre** `type` (`intro`, `step` ou `summary` — se faltar, herda o do exemplo) e `isHidden` | ⚠️ não testado |
| `knowledgecheck-knowledgecheck-multiple-response.json` | Múltipla resposta | UUID | — | ⚠️ não testado; o exemplar tem `correct`/`corrects` anômalos (ver armadilhas) |

Os tipos não testados devem passar pelo fluxo completo, **com teste no navegador**, e o resultado
precisa ser relatado como primeira inserção desse tipo.

---

## 2. Regras por tipo

### Parágrafo (`text/paragraph`)
- Texto em `<p>…</p>`. Pode ter `<strong>`, `<em>`, `<br>`, `<ul><li>`.
- Usos típicos: "Ao final desta lição, você será capaz de:" antes de uma lista; fechamento da lição;
  frase curta anunciando um bloco interativo ("Compare, nas abas, …:").

```json
{"paragraph": "<p>Uma <strong>pergunta-guia</strong> acompanha toda esta lição: <em>…?</em></p>"}
```

### Título + parágrafo (`text/heading paragraph`)
- **Regra:** `heading` em texto puro, sem HTML (83 de 83).
- `paragraph` em `<p>`. Quando anuncia um accordion, abas ou process, termina com dois-pontos e um
  convite: "Abra cada item para ver…:", "Vire cada cartão…:".

### Lista numerada (`list/numbered`)
- 3 a 5 itens na maioria (até 9 aparece). Cada `paragraph` em `<p>`.
- **Regra:** `number` em sequência "1", "2", "3"… — o script numera sozinho.
- Quase sempre precedida por um parágrafo terminado em ":" (21 vezes) e seguida de Continue (11).

### Destaque (`impact`, variante `b`)
- Padrão dominante (23 de 42): `<p>EMOJI <strong>Rótulo:</strong> texto</p>`.
- Emojis em uso: 🔑 regra de ouro · ⚠️ cuidado · 🏁 ponto de controle.
- Aparece em fonte maior, centralizado, com barra de acento — use para **uma** ideia-chave, curta.

```json
{"paragraph": "<p>🔑 <strong>Regra de ouro:</strong> na dúvida sobre um conteúdo, ele não entra no arquivo.</p>"}
```

### Accordion (`interactive/accordion`)
- 3 a 6 itens (4 é o mais comum).
- **Regra:** `title` em texto puro (100 de 100).
- `description` em `<p>`; `<strong>`/`<em>` ocasionais.
- **Regra:** dois ou mais parágrafos numa `description` são separados por um `<p></p>` vazio
  (39 de 39). Sem ele, o Rise mostra os parágrafos colados.
- **Sempre** precedido por um título + parágrafo curto ("Abra cada item para ver…:") — 23 de 23.

```json
{"title": "O que preservar",
 "description": "<p>Declare o que não pode mudar.</p><p></p><p>Exemplo: <em>\"Mantenha o estilo…\"</em>.</p>"}
```

### Abas (`interactive/tabs`)
- Na maioria **2 abas** — comparação de dois lados ("criação × edição", "plano A × plano B").
- **Regra:** `title` em texto puro (18 de 18). `description` em `<p>`, `<strong>` frequente como rótulo.
- **Regra:** o mesmo `<p></p>` entre parágrafos (10 de 10).
- Precedidas por um texto terminado em ":" anunciando a comparação.

### Questão de verificação (`knowledgeCheck/multiple choice`)
- **Regras** (22 de 22, sem exceção): 1 questão por bloco; **exatamente 1** alternativa
  `"correct": true`; `feedback` em **todas** as alternativas; **texto puro** em enunciado, alternativas
  e feedbacks (sem HTML).
- 4 alternativas (o validador avisa se for diferente).
- Enunciado em forma de **cenário** curto ("Um docente faz X… Qual …?").
- Feedback começa com **"Correto."** ou **"Não."** e explica o porquê com base no conteúdo da lição.
- Varie a posição da correta (nos cursos: 1ª 8×, 2ª 8×, 3ª 5×, 4ª 1×).
- Costuma vir no fim de uma seção, logo antes de um Continue.

```json
{"title": "Cenário… Qual das quatro condições ele deixou de cumprir?",
 "answers": [
   {"title": "Instrução específica", "correct": false, "feedback": "Não. …"},
   {"title": "Fonte confiável", "correct": true, "feedback": "Correto. …"},
   {"title": "…", "correct": false, "feedback": "Não. …"},
   {"title": "…", "correct": false, "feedback": "Não. …"}]}
```

### Continue (`divider/continue`)
- **Regra:** item idêntico ao dos 40 Continues dos cursos — `title "Continue"`, `buttonColor "brand"`,
  `completeHint` padrão em inglês. Só o `type` pode variar:
  - `""` (padrão de todos os nossos cursos) — não exige nada;
  - `"completeBlock"` — trava até o **bloco logo acima** estar concluído (use com bloco HTML que tenha
    `hasCustomCompletion`, ou com interativos que exigem interação);
  - `"completeAll"` — trava até **todos os blocos acima** estarem concluídos (não testado).
- Separa as seções de uma lição. Transição mais comum depois dele: título + parágrafo (27 vezes).

---

## 3. Como as lições são compostas

Esqueleto típico de uma lição nos nossos cursos:

```
título + parágrafo (abertura)
parágrafo "Ao final desta lição, você será capaz de:"
lista numerada (objetivos)
Continue
── seção ──
título + parágrafo ("Abra cada item…:")  →  accordion / abas / process / flashcards
destaque (ideia-chave)
questão de verificação
Continue
── … ──
parágrafo de fechamento ("Na próxima lição…")
```

Transições mais comuns (bloco → próximo): Continue → título (27) · título → accordion (23) ·
parágrafo → lista (21) · título → parágrafo (16) · título → process (14) · questão → Continue (13) ·
process → destaque (12) · destaque → título (12) · lista → Continue (11).

Ao inserir uma seção, siga esse ritmo. Ao inserir um bloco solto, encaixe-o numa transição natural
(ex.: um destaque logo depois do título cujo conteúdo ele resume).

Seção nova **no fim de uma lição** que não termina com Continue: comece a seção com um Continue
(`type ""`), para ela abrir como etapa própria — como as seções originais. Testado no curso Word
Hands-on: Continue → título + "Abra cada um…:" → accordion → questão de verificação.

---

## 4. HTML permitido em textos de blocos nativos

Só `<p> <strong> <em> <br> <ul> <li> <span>`, **sem atributos** (sem `class`, sem `style`). É o que
existe nos cursos; o validador recusa o resto. Para estética livre, use o bloco HTML
(`referencias/bloco-html.md`) — ele é o caminho certo, não estilos dentro dos textos.
