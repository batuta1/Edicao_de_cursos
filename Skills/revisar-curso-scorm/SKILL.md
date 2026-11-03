---
name: revisar-curso-scorm
description: Revisa o conteúdo textual de cursos Articulate Rise 360 exportados como pacote SCORM (.zip), sem quebrar a estrutura técnica do curso. Cobre o ciclo completo — desserializar o curso de dentro do .zip, separar em arquivos de lição, melhorar os textos pedagógicos com base no roteiro-fonte, validar que nada estrutural mudou, serializar de volta para Base64 e reempacotar o SCORM. Use esta skill sempre que o usuário mencionar revisar/editar/melhorar um curso, um pacote SCORM, um .zip de curso, lições em JSON, Articulate Rise 360, desserializar ou serializar curso, arquivos licao_*.json ou pastas licoes_extraidas_*, mesmo que ele não cite explicitamente "SCORM" ou "pipeline" — por exemplo "melhora os textos do curso X", "revisa esse zip aí", "os textos dessas lições estão fracos".
---

# Revisão de curso Rise 360 empacotado em SCORM

O curso inteiro vive **codificado em Base64 dentro do pacote `.zip`**. O trabalho aqui é abrir esse
payload, melhorar apenas o texto pedagógico e devolver tudo no lugar — sem tocar em nada que a
plataforma use para renderizar o curso (ids, tipos, posições, settings, quantidade de blocos).

Um erro estrutural aqui não aparece como erro: aparece como um curso que quebra na plataforma, ou
pior, um curso que carrega com o conteúdo trocado. Por isso cada fase tem uma verificação, e os
scripts saem com código de erro quando algo não bate. **Se uma verificação falhar, pare e investigue
— não contorne.**

## Antes de começar

Confirme com o usuário (ou infira do pedido, se estiver claro):

- **Qual pacote `.zip`** revisar.
- **Qual o título esperado** do curso — usado como trava de segurança na extração.
- **Onde está o material-fonte** (roteiro/plano de aula que originou o curso). Ele é a referência
  principal da revisão; sem ele você só consegue melhorar o texto "no vácuo".

Se o projeto tiver um documento de regras de edição (neste projeto:
`promptRevisaoPorClaude.md`), **leia-o antes de editar** — ele manda em caso de conflito com esta skill.

## Ambiente

- O shell aqui costuma ser **PowerShell 5.1**, que quebra em `python -c "..."` com regex contendo
  colchetes (`[A-Za-z0-9+/=]` vira erro de parser). **Escreva scripts em arquivo `.py` e rode
  `python arquivo.py`** — nunca inline.
- Rode os comandos a partir da pasta de trabalho do projeto (onde ficam os `curso*.json` e as
  pastas `licoes_extraidas_*`).

---

## Fase 1 e 2 — Extrair e desserializar

```bash
python <skill>/scripts/scorm_extrair.py PACOTE.zip --so-inspecionar
```

Mostra o formato do pacote, o título, o `course.id` e a lista de lições. Confira que é mesmo o curso
certo, e então grave:

```bash
python <skill>/scripts/scorm_extrair.py PACOTE.zip --saida curso[Nome].json --titulo-esperado "Título Exato"
```

O `--titulo-esperado` é uma trava deliberada: se o título divergir, o script aborta **sem gravar
nada**. Isso já evitou um caso real em que um arquivo de curso foi sobrescrito com o conteúdo de
outro curso e o erro passou dias despercebido.

Existem dois formatos de pacote e o script detecta sozinho:

| Formato | Payload em | Envelope |
|---|---|---|
| Default | `scormcontent/runtime-data.js` | `__jsonp("runtime-data.js","BASE64")` |
| Legacy | `scormcontent/index.html` | `Promise.resolve(deserialize("BASE64"))` |

O payload é **Base64 puro de JSON UTF-8**. Se o pacote tiver `lzwcompress.js`, ignore: essa
biblioteca serve para dados de progresso da LMS, não para o conteúdo do curso.

## Fase 3 — Separar em lições

Use o `lessonExtracter.py` do projeto, se existir (ele tem os caminhos no topo do arquivo, que
precisam apontar para o curso da vez). Ele gera `licoes_extraidas_[Nome]/licao_NN_[Título].json` —
um arquivo por lição, cada um com o objeto `lesson` inteiro — mais um `indice_licoes.json`.

Não havendo script no projeto, gere a mesma estrutura: um arquivo por lição, ordenados por
`position`, cada um no formato `{numero_da_licao, position_original, title, lesson}`.

## Fase 4 — Revisar os textos

**Esta é a única fase em que o conteúdo muda.** Antes de escrever qualquer coisa, localize o
material-fonte e monte o mapeamento lição ↔ módulo/oficina — às vezes é 1:1, às vezes uma lição
condensa duas oficinas do roteiro.

O que costuma estar ruim em curso gerado por IA, e o que fazer:

| Sintoma | Correção |
|---|---|
| Abertura genérica ("surge como solução inovadora", "representa um diferencial") | Trocar pela analogia concreta que existe no roteiro-fonte |
| Cada lição introduz a lista de objetivos de um jeito diferente | Padronizar a fórmula ("Ao final desta lição, você será capaz de:") |
| Item da lista de objetivos não corresponde ao objetivo real do módulo | Alinhar, na ordem, ao plano de aula |
| Fechamento motivacional vazio ("Parabéns! Continue explorando...") | Trocar pelos próximos passos concretos do roteiro |
| Especificidade perdida ("uma conta no serviço necessário") | Restaurar o detalhe da fonte (qual serviço, qual plano) |

Preserve o que já está bom. Accordions, flashcards, exercícios guiados com breadcrumbs e prompts
entre aspas triplas costumam reproduzir o roteiro fielmente — mexer neles é risco sem ganho.

Limites que não se negociam:

- Altere **apenas** campos textuais pedagógicos. Na prática a quase totalidade das edições cai em
  `paragraph`.
- Nunca altere `id`, `type`, `family`, `variant`, `position`, `settings`, `metadata`,
  `globalBlockId`, nem a quantidade ou ordem de blocos, itens de lista e alternativas de quiz.
- Nunca mude qual alternativa de quiz é a correta. Se o gabarito parecer errado, **registre no
  relatório e proponha** — corrigir em silêncio esconde um problema pedagógico real de quem
  precisa decidir sobre ele.
- Edite por substituição pontual de string (ferramenta Edit), não reescrevendo o arquivo inteiro —
  preserva indentação e evita estrago acidental.
- Texto com aspas precisa sair escapado no JSON (`\"assim\"`). Depois de editar algo com aspas,
  valide o arquivo antes de seguir.

## Fase 5 — Validar que só o texto mudou

```bash
python <skill>/scripts/validar_estrutura.py curso[Nome].json licoes_extraidas_[Nome]/
```

Compara cada lição nó a nó contra o original e separa o que mudou em "texto" (esperado) e
"estrutura" (proibido). Sai com código 1 se achar divergência estrutural, se a quantidade de lições
não bater, ou se algum `lesson.id` não existir no curso — o que denuncia pasta e curso trocados.

Confira também se a contagem de campos alterados bate com o que você editou de propósito. Um número
maior que o esperado significa edição acidental.

## Fase 6 e 7 — Remontar, serializar e reempacotar

```bash
python <skill>/scripts/scorm_reempacotar.py curso[Nome].json licoes_extraidas_[Nome]/ \
    --base64-saida curso[Nome]_editado_base64.txt \
    --json-saida curso[Nome]_editado.json \
    --pacote-original PACOTE.zip \
    --pacote-saida PACOTE-REVISADO.zip
```

Funde as lições por `numero_da_licao`, serializa com verificação de round-trip (não grava se o
Base64 não voltar a ser exatamente o mesmo objeto), e reescreve o `.zip` trocando **apenas** o
arquivo do payload — conferindo no final que nenhuma outra entrada mudou de tamanho.

**O `.zip` original nunca é modificado.** A saída é sempre um arquivo novo.

Se o projeto usa colagem manual do Base64 no HTML, omita `--pacote-original`/`--pacote-saida`: o
`.txt` é gerado do mesmo jeito e é o entregável suficiente. Pergunte ao usuário qual entrega ele
quer antes de assumir.

## Fase 8 — Testar em navegador (opcional, mas revela o que a validação não pega)

O pacote **se recusa a renderizar fora de uma LMS** — abrir o `index.html` direto mostra
*"Content launched outside of a supported LMS enviroment"*. Isso é comportamento original do
pacote, não regressão da edição; confirme abrindo o `.zip` original do mesmo jeito antes de
suspeitar do próprio trabalho.

Para ver o curso de verdade, extraia o pacote, crie um `lms_mock.html` irmão de `scormcontent/` com
stubs da API de LMS (`IsLmsPresent`, `GetStatus`, `SetScore`, etc.) carregando o curso num iframe,
sirva com `python -m http.server` e abra o mock. Confira visualmente pelo menos um trecho editado.
Depois limpe a pasta extraída.

## Fase 9 — Relatório

Grave `Relatorio_Edicao_Licoes.md` dentro da pasta `licoes_extraidas_[Nome]/`, com: arquivos
editados (e os lidos sem alteração), material-fonte e mapeamento lição↔módulo, critério aplicado,
alterações lição a lição (o que estava ruim e o que a fonte dizia), contagem de campos alterados,
resultado das validações, pontos de atenção (gabaritos suspeitos, o que exige olho humano) e o que
foi gerado/testado.

Linguagem objetiva. **Se algo não foi verificado, diga que não foi** — um relatório que afirma mais
do que se checou é pior que relatório nenhum, porque cria confiança injustificada.

---

## Armadilhas conhecidas deste tipo de projeto

- **Scripts do projeto com caminhos hardcoded**: `lessonExtracter.py` e similares costumam apontar
  para o curso anterior. Ajuste antes de rodar e confira a saída.
- **Sentinelas de teste**: alguns scripts têm frases de teste (ex.: `"XXXX"`) e imprimem `ERRO:
  frase de teste não encontrada` em uso normal. É inofensivo; olhe os arquivos gerados.
- **Scripts genéricos com defaults perigosos**: `serialize.py` aceita argumentos, mas sem eles usa
  caminhos padrão de outro curso. Sempre passe entrada e saída explicitamente.
- **Pasta `naousar/`** (ou similar): versões abandonadas de propósito. Não use.
- **PowerShell 5.1 + UTF-8 sem BOM**: `Get-Content` sem `-Encoding UTF8` mostra `lição` como
  `liÃ§Ã£o`. Parece corrupção, mas o arquivo está certo — decodifique explicitamente antes de
  concluir que algo quebrou.
- **`.ps1` sem BOM com acentos** dá erro de parser em linha que aparenta estar correta. Prefira
  Python, ou mantenha auxiliares em ASCII.
