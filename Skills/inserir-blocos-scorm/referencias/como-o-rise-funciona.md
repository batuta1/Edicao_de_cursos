# Como o pacote SCORM do Rise 360 funciona por dentro

O que foi descoberto lendo os pacotes e o código do player (out/2026). Leia quando precisar ir além
dos modelos prontos ou entender um comportamento.

## Sumário
1. Anatomia do pacote
2. O curso (runtime-data.js)
3. IDs
4. O esquema de todos os blocos, dentro do player
5. Conclusão de blocos e o Continue
6. Progresso do aluno e retomada
7. Abrir fora da LMS
8. Tipo de bloco novo (que não está em modelos/)

---

## 1. Anatomia do pacote

```
imsmanifest.xml            lista TODO arquivo de conteúdo (<file href>); identifier = courseId + versão
scormdriver/indexAPI.html  ponto de entrada da LMS; __DRIVER_CONFIG__ com coursePackageVersion
scormcontent/index.html    o player; comentário "course package version: XXXXXXXX"
scormcontent/runtime-data.js   o curso (Base64)
scormcontent/lib/rise/*.js     o player completo do Rise (todos os tipos de bloco, usados ou não)
scormcontent/lib/sandbox/      renderizador dos blocos HTML
scormcontent/assets/           imagens e mídias do curso (citadas no JSON só pelo nome do arquivo)
```

- A **versão do pacote** (8 caracteres, também no nome do .zip) aparece em 3 lugares e precisa ser
  igual nos 3 — o `verificar_scorm.py` confere.
- Os nomes dos arquivos em `lib/` mudam de uma exportação para outra (são hashes); procure pelo
  conteúdo, não pelo nome.
- Todo pacote traz o **player completo**: o código de abas, linha do tempo, galeria etc. está lá mesmo
  que o curso não use. O risco de um tipo novo não está no player, está no JSON.

## 2. O curso (`runtime-data.js`)

`__jsonp("runtime-data.js","<Base64 de JSON UTF-8>");` — JSON compacto, sem escapar acentos.
O `empacotar.py` reproduz a serialização do Rise **byte a byte** (ida e volta sem edição sai idêntica).

`course.lessons[]` (cada lição: `id`, `type` "blocks" ou "quiz", `position`, `items[]` = blocos).
Cada bloco: `id`, `type`, `family`, `variant`, `settings`, `items[]`, `metadata`, `globalBlockId`.
A aparência (cores, fontes, navegação) está em `course.theme`, não nos blocos.

## 3. IDs

- Aleatórios; o player **não valida formato**. Exigência real: **unicidade** e referências coerentes.
- Dois formatos, conforme o tipo: **UUID v4** (accordion, tabs, process, impact, continue, questões,
  HTML) e **cuid2** — 24 caracteres `a-z0-9`, começando com letra (texto, lista, flashcard). Os modelos
  registram o formato de cada nível; `ids.py` gera e confere colisão.
- Referências cruzadas: lição de quiz `id` == `course.exportSettings.quizId`;
  `lessons[].courseId` == `course.id` == `exportAggregate.courseId`; em questões do **quiz final**,
  `correct`/`corrects` = ids de `answers`.

## 4. O esquema de todos os blocos, dentro do player

Um dos arquivos de `scormcontent/lib/rise/` contém o **esquema JSON de todos os tipos de bloco do Rise**
(biblioteca TypeBox). Para achá-lo, procure o arquivo que contém `$id:"BlockHTML"` ou
`$id:"BlockItemContinue"`. Trechos úteis encontrados:

- `BlockBase`: `id`, `settings`, `metadata?` (`createdVia`, `contentValidation`), `globalBlockId?`.
- `BlockHTML`: `type/family "html"`, `variant "inline" | "cdn"`, settings `autoResize`,
  `hasCustomCompletion`, `height`, `width` (`MediaWidth`: `"0"|"1"|"2"`); item `srcdoc` ou
  `media.sandbox {src, srcName}`.
- `BlockItemContinue`: `type` = `"" | "completeBlock" | "completeAll"`, `buttonColor`
  `"brand"|"gray"|"black"`, `completeHint`.
- Há também `BlockCustomVideo`, `BlockItemImage…`, `BlockItemStep` etc. — base para tipos novos.

Para ler, use um script que imprima o texto em volta de um padrão (o arquivo é minificado, uma linha).

## 5. Conclusão de blocos e o Continue

No player há uma tabela `"family/variant": modo` (procure `"html/inline":`). Modos:

| Modo | Significado | Exemplos |
|---|---|---|
| `view` | concluído ao ser visto | texto, lista, impact, accordion |
| `step` | cada item precisa de interação | checkboxes, survey |
| `step-if` | `step` só se a condição valer | `html/inline` e `html/cdn`: só com `hasCustomCompletion: true` |

O Continue com `type`:
- `""` — sempre liberado (todos os Continues dos nossos cursos);
- `"completeBlock"` — libera quando o **último bloco acima** estiver concluído no progresso;
- `"completeAll"` — quando **todos** os blocos acima estiverem.

O `verificar_scorm.py` usa a mesma tabela para conferir que todo `family/variant` do curso existe no
player do pacote.

## 6. Progresso do aluno e retomada

- Em memória o player indexa o progresso por ID, mas o que **grava na LMS** (`cmi.suspend_data`) é
  indexado pela **posição** das lições e dos blocos (`decodeCourseProgress` lê `lessons[String(index)]`).
  → Trocar IDs quase não afeta progresso salvo; **inserir no meio desloca** as posições seguintes.
  Por isso: curso com alunos → inserir só no fim das lições, ou publicar como versão nova.
- Bookmark = `index.html#/lessons/<lessonId>` (`cmi.core.lesson_location`).
- O progresso guarda `cpv` (versão do pacote). Com `resetLearnerData: false` (o padrão dos nossos
  pacotes), versão diferente só gera aviso — o progresso antigo é mantido, **sem** proteção contra
  deslocamento.
- Não são restaurados na retomada: resposta de questões de verificação e estado interno de blocos HTML
  (só a conclusão). Abrir itens de accordion não é gravado.

## 7. Abrir fora da LMS

`index.html` tem `"loadOnlyInLms": true`, mas o código só bloqueia quando o protocolo **não** é `file:`:
duplo clique no `scormcontent/index.html` abre o curso; via `http://` sem LMS aparece "Content launched
outside of a supported LMS environment." — por isso o `teste/lms_mock.html` (LMS SCORM 1.2 simulada que
abre `scormdriver/indexAPI.html` num iframe, como uma LMS real faria).

## 8. Tipo de bloco novo (que não está em `modelos/`)

Nunca escreva um bloco "de cabeça". Em ordem de preferência:

1. **Exemplar real em outro curso nosso.** Extraia aquele curso só para leitura e catalogue apenas o
   tipo desejado (não sobrescreve modelos existentes):
   ```bash
   python <skill>/scripts/extrair.py OUTRO_CURSO.zip --saida trabalho/fonte_outro.json
   python <skill>/scripts/catalogar_modelos.py trabalho/fonte_outro.json --saida <skill>/modelos/ --somente "nome do variant"
   ```
   Foi assim que as abas vieram do curso de Word e funcionaram no de PowerPoint.
2. **Esquema do player** (seção 4): monte o modelo à mão seguindo `html-html-inline.json` como
   referência de formato (`chave`, `origem` dizendo que veio do esquema, `formato_id`,
   `campos_texto_item`, `campos_obrigatorios`, `settings_ajustaveis` se houver, `bloco`, `item_exemplo`).
3. **Curso-catálogo:** se nada acima resolver, peça à equipe um curso montado uma vez no Rise com o tipo
   desejado, exportado em SCORM, e use a opção 1.

Depois: fluxo completo **com teste no navegador**, relato claro de que é a primeira inserção do tipo,
e — se der certo — acrescente as regras do tipo em `padroes-por-tipo.md` (levante o padrão nos cursos
que o usam) e, se houver regra verificável, no `validar.py`.
