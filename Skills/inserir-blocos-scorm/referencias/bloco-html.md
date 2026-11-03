# Bloco HTML próprio — estética livre dentro do curso

O Rise tem um tipo de bloco oficial para HTML personalizado (no player, `block-code`). Nenhum curso
nosso foi criado com ele na plataforma, mas o renderizador vem em todo pacote (`lib/sandbox/`).
Testado e funcionando: infográfico, atividade que trava o Continue e mini-aplicação em pasta.

## Sumário
1. Duas variantes: embutido (inline) e em pasta (cdn)
2. Configurações
3. Fazer o bloco travar o Continue até o aluno concluir
4. Como escrever o HTML
5. Limitações conhecidas

---

## 1. Duas variantes

| | `html-html-inline.json` | `html-html-cdn.json` |
|---|---|---|
| Onde fica o HTML | dentro do JSON do curso (`srcdoc`) | pasta em `scormcontent/assets/<PASTA>/` |
| Arquivos | um documento só (CSS e JS dentro dele; imagens em SVG embutido ou data URI) | `index.html` + CSS, JS, imagens separados, com caminhos relativos |
| Roteiro | `{"srcdoc": "@arquivo:meu.html"}` | `{"media": {"sandbox": {"src": "PASTA", "srcName": "PASTA"}}}` |
| Empacotar | normal | `--anexar caminho/da/pasta=PASTA` (registra cada arquivo no manifest) |
| Use quando | infográfico, card, atividade pequena | algo maior, com imagens próprias ou vários arquivos |

O nome `PASTA` só pode ter letras, números, `-` e `_`, e não pode já existir no pacote.

## 2. Configurações (`"settings"` no bloco do roteiro)

| Chave | Valores | Padrão no modelo | Efeito |
|---|---|---|---|
| `autoResize` | true/false | true | A altura do bloco acompanha o conteúdo (inclusive quando ele cresce, ex.: mensagem que aparece). Deixe ligado. |
| `height` | número | 40 | Altura fixa em décimos de rem, usada só com `autoResize: false` |
| `width` | `"0"`, `"1"`, `"2"` | `"1"` | pequeno / médio / largura total. Em tela de 1280px, médio ≈ 1100px (mais largo que a coluna de texto); `"0"` alinha melhor com o texto. |
| `hasCustomCompletion` | true/false | false | true = o bloco só conta como concluído quando o HTML avisar (seção 3) |

## 3. Travar o Continue até o aluno concluir

Três peças, testadas juntas:

1. No roteiro, o bloco HTML com `"settings": {"hasCustomCompletion": true}`.
2. Logo abaixo, um Continue com `"type": "completeBlock"`:
   `{"modelo": "divider-continue-continue.json", "itens": [{"title": "Continue", "type": "completeBlock"}]}`
3. No HTML, quando o aluno terminar a atividade, **uma vez**:
   ```js
   window.parent.postMessage({ type: 'complete' }, '*');
   ```

Resultado no navegador: antes, o Continue aparece com cadeado e "Complete the content above before
moving on." e o resto da lição não é carregado; depois do `postMessage`, o cadeado some e o Continue
libera. A conclusão é gravada no progresso do aluno (retomada mantém o Continue liberado).

Exemplo completo: `exemplos/roteiro-html-com-conclusao.json` + `exemplos/atividade.html`.

## 4. Como escrever o HTML

O HTML roda **isolado num iframe**: não herda fonte, cor nem nada do tema do curso. Isso é a liberdade
de estética — e significa que tudo precisa vir no próprio HTML.

- **Documento completo:** `<!doctype html>`, `<html lang="pt-BR">`, `<meta charset="utf-8">`,
  `<meta name="viewport" …>`, `<head>`, `<body>`. O validador exige `<html>` e `<body>`.
- **Autocontido:** nada de `src`/`href`/`url(`/`@import` para `http(s)://` — sem Google Fonts, CDN de
  bibliotecas ou imagens da web. A LMS pode bloquear e o curso pode abrir offline. Os scripts recusam.
  Use fontes do sistema (`"Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`), SVG embutido ou
  arquivos dentro da pasta (variante cdn).
- **Combine com o curso:** leia a cor de destaque do curso em `course.theme.colorAccent` no
  `curso_original.json` (ex.: `#152f4d`) e use-a como cor principal.
- **Fundo transparente** em `html, body` e `margin: 0`, para o bloco se encaixar na página; desenhe um
  cartão com borda/raio próprios se quiser moldura.
- **Responsivo:** a mesma página aparece no celular (~400px) e no computador (~1100px). Use grid com
  `repeat(auto-fit, minmax(…, 1fr))` ou flex-wrap. Teste as duas larguras.
- **Acessível:** botões de verdade (`<button>`), `aria-live="polite"` em feedbacks, foco visível,
  `prefers-reduced-motion` para desligar animações.
- **Conteúdo:** venha do texto do próprio curso; não invente dados técnicos.
- Abra o arquivo HTML sozinho no navegador para ajustar o visual antes de inserir.

Exemplos testados: `exemplos/infografico.html` (inline), `exemplos/atividade.html` (inline com
conclusão), `exemplos/checklist/` (cdn, 4 arquivos).

## 5. Limitações conhecidas

- **Estado interno não é salvo.** Ao retomar o curso, o HTML recarrega do zero (a atividade aparece em
  branco), embora a conclusão fique registrada. O Rise faz o mesmo com as questões nativas. Se for
  importante, o HTML pode guardar o próprio estado em `localStorage` (vale só naquele navegador).
- **Busca do curso:** o texto de dentro do bloco HTML provavelmente não entra na busca (não verificado).
- **Quick Share:** o Rise desliga blocos de código no compartilhamento Quick Share em período de teste.
  Não afeta pacote SCORM exportado.
- **`file://`:** testado via servidor local. O sandbox tem tratamento específico para `file://`, mas o
  duplo clique com bloco cdn não foi conferido — confira na primeira vez.
