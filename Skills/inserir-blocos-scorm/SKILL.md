---
name: inserir-blocos-scorm
description: Insere blocos novos em cursos Articulate Rise 360 exportados como SCORM (.zip), sem a plataforma Articulate — parágrafos, títulos, listas, destaques, accordions, abas, questões, Continue, seções inteiras e blocos com HTML próprio (infográficos, atividades que travam o Continue, mini-aplicações com CSS/JS/imagens) — na estética dos cursos da equipe, e verifica a consistência do pacote para garantir que o SCORM não está quebrado antes da LMS. Use sempre que o usuário quiser acrescentar ou criar conteúdo num curso do Rise já exportado, montar uma seção nova, pôr um HTML/infográfico/atividade no curso, ou verificar se um SCORM do Rise está íntegro ou pronto para subir — mesmo sem dizer "bloco" ou "SCORM", por exemplo "coloca um accordion depois daquele texto", "dá pra pôr esse HTML no curso?", "acrescenta uma questão na lição 2", "esse zip tá quebrado?". Para só melhorar textos existentes, use revisar-curso-scorm.
---

# Inserir blocos novos em SCORM do Rise 360 — sem a plataforma Articulate

O curso inteiro de um pacote do Rise vive num JSON codificado em Base64 dentro de
`scormcontent/runtime-data.js`. Esta skill abre esse JSON, **insere** blocos novos montados a partir
de modelos reais do Rise, valida, reempacota e **verifica o pacote inteiro** antes da entrega.

Tudo aqui foi testado num laboratório (2026-10), com um curso real, no navegador. O que funciona:

| Pode inserir | Observação |
|---|---|
| parágrafo, título + parágrafo, lista numerada, destaque (impact) | estética dos nossos cursos já mapeada |
| accordion, abas (tabs) | abas vieram de outro curso e funcionaram |
| questão de verificação de múltipla escolha | gabarito e feedback funcionando |
| Continue (livre, ou travado até concluir o bloco acima) | |
| seção inteira de lição, a partir de um único roteiro | |
| bloco HTML próprio, embutido ou em pasta com CSS/JS/imagens | estética livre; pode travar o Continue |

**Ainda não testado — avise o usuário antes de tentar:** criar lições novas, remover/mover blocos
existentes, bloco nativo de imagem/vídeo, flashcard, process e knowledgeCheck de múltipla resposta
(os modelos existem, mas nunca foram inseridos e conferidos no navegador).

Esta skill **não altera** textos de blocos que já existem — isso é da skill `revisar-curso-scorm`.

---

## Antes de começar

Confirme com o usuário (ou deduza do pedido, se estiver claro):

1. **Qual pacote `.zip`.** Só pacotes SCORM do Rise 360 com `scormcontent/runtime-data.js`.
2. **O curso já está publicado na LMS com alunos?** Isso muda onde se pode inserir — ver "Regras".
3. **O que inserir e onde.** Lição e posição (você vai listar os blocos para escolher junto).
4. **De onde vem o texto.** Se o usuário não der o texto, escreva a partir do conteúdo do próprio
   curso (sem inventar fatos técnicos) e diga claramente que é rascunho para ele revisar.

## Ambiente

- `<skill>` abaixo = a pasta desta skill. Os scripts estão em `<skill>/scripts/` e importam uns aos
  outros: rode-os pelo caminho (`python <skill>/scripts/x.py`), nunca copie um só.
- Python 3.10+. Sem bibliotecas externas.
- No Windows o shell costuma ser **PowerShell 5.1**: não use `python -c` com regex (quebra o parser);
  escreva `.py` em arquivo. Para imprimir acentos/emoji, `$env:PYTHONIOENCODING='utf-8'`.
- Os scripts leem arquivos **com ou sem BOM** (o Bloco de Notas e o `Set-Content` do PowerShell 5.1
  gravam BOM). Grave JSON sempre em UTF-8.
- Todo script que grava algo **recusa sobrescrever** arquivo existente. Isso é proposital: escolha um
  nome novo para cada versão.

## Pasta de trabalho

Crie uma pasta por curso (perto do `.zip` do curso, ou onde o usuário preferir):

```
<curso>-blocos/
├── original/   ← cópia do .zip. Nunca é alterado.
├── trabalho/   ← curso_original.json (nunca editar) + curso_v1.json, curso_v2.json... + roteiros
├── saidas/     ← .zip gerados
└── teste/      ← pacotes extraídos para abrir no navegador (uma pasta nova por versão)
```

Copie o `.zip` para `original/` (copiar, não mover) e confira o hash se quiser certeza.

---

## Fluxo

### 1. Verificar o pacote original

```bash
python <skill>/scripts/verificar_scorm.py original/CURSO.zip
```

Assim você sabe quais **avisos já existiam** antes de você mexer (ver "Avisos conhecidos").
Se o original já tiver **ERRO**, pare e mostre ao usuário — não construa em cima de pacote quebrado.

### 2. Extrair o curso

```bash
python <skill>/scripts/extrair.py original/CURSO.zip --saida trabalho/curso_original.json
```

`curso_original.json` é a referência de tudo que vem depois. Nunca o edite.

### 3. Escolher onde inserir

```bash
python <skill>/scripts/listar_blocos.py trabalho/curso_original.json --licao 0
```

Mostra os blocos da lição (`--licao` é a `position`: 0 = primeira) com índice, tipo e início do texto.
A `posicao` do roteiro é o índice que o **primeiro** bloco novo vai ocupar; os seguintes deslocam.

Antes de escrever, leia **`referencias/padroes-por-tipo.md`**: ele diz como cada tipo de bloco é
escrito nos nossos cursos (HTML permitido, quantidade de itens, emoji do destaque, que bloco vem antes
de um accordion etc.). É isso que faz o bloco novo parecer feito pela equipe.

### 4. Escrever o roteiro

Um roteiro é um JSON com a lição, a posição e a lista de blocos, cada um com o **modelo** e os
**itens** (só os textos; IDs e configurações vêm do modelo):

```json
{
  "licao": 2,
  "posicao": 4,
  "blocos": [
    {"modelo": "text-text-heading-paragraph.json",
     "itens": [{"heading": "Título em texto puro", "paragraph": "<p>Parágrafo terminando em dois-pontos:</p>"}]},
    {"modelo": "list-list-numbered.json",
     "itens": [{"paragraph": "<p>Primeiro passo.</p>"}, {"paragraph": "<p>Segundo passo.</p>"}]},
    {"modelo": "divider-continue-continue.json", "itens": [{"title": "Continue"}]}
  ]
}
```

- Modelos disponíveis em `<skill>/modelos/` (tabela em `referencias/padroes-por-tipo.md`).
- `"settings": {...}` num bloco ajusta **só** o que o modelo declara em `settings_ajustaveis`
  (hoje, apenas os blocos HTML). Qualquer outra chave é recusada.
- Um campo pode vir de arquivo: `"srcdoc": "@arquivo:infografico.html"` (relativo ao roteiro).
- Lista numerada é numerada sozinha. Alternativas de questão e itens não precisam de `id`.
- Exemplos completos e testados em `<skill>/exemplos/` (seção de lição, abas, HTML embutido,
  atividade que trava o Continue, HTML em pasta). Os números de lição/posição deles são do curso de
  teste — ajuste para o seu.

Para blocos HTML (infográfico, atividade, mini-aplicação), leia antes **`referencias/bloco-html.md`**.

### 5. Inserir

```bash
python <skill>/scripts/inserir_sequencia.py trabalho/curso_original.json \
    --roteiro trabalho/roteiro_v1.json --modelos <skill>/modelos/ --saida trabalho/curso_v1.json
```

Para várias inserções, encadeie: a entrada da próxima é a saída da anterior (`curso_v1.json` →
`curso_v2.json`). Se qualquer bloco falhar, nada é gravado.
(`inserir_bloco.py` faz o mesmo para um bloco só, com `--modelo` e `--conteudo`.)

### 6. Validar o curso

```bash
python <skill>/scripts/validar.py trabalho/curso_v1.json --original trabalho/curso_original.json \
    --modelos <skill>/modelos/
```

Confere que **só houve inserção** (nada fora dos blocos mudou; blocos originais intactos e na mesma
ordem), que cada bloco novo bate com seu modelo (chaves, settings, formato dos IDs, estrutura dos
itens), que os IDs são únicos e que as regras estéticas e de questões foram seguidas.
**REPROVADO = pare, corrija o roteiro e gere uma versão nova.** Não contorne.

### 7. Empacotar

```bash
python <skill>/scripts/empacotar.py trabalho/curso_v1.json --pacote-original original/CURSO.zip \
    --pacote-saida saidas/CURSO-v1.zip
```

Troca só o `runtime-data.js`. Para blocos HTML em pasta, acrescente `--anexar PASTA=NOME` (copia a
pasta para `scormcontent/assets/NOME/` e registra no manifest). O script confere tudo antes de gravar
e não deixa arquivo pela metade se falhar.

### 8. Verificar o pacote final

```bash
python <skill>/scripts/verificar_scorm.py saidas/CURSO-v1.zip --original original/CURSO.zip
```

Ver a seção "Verificação de consistência". **Só entregue pacote APROVADO.**

### 9. Testar no navegador

O pacote se recusa a abrir fora de uma LMS quando servido por `http://` — mas **abre normalmente
por `file://`** (o código do Rise pula a checagem nesse caso).

- **Para a pessoa conferir:** extraia o `.zip` numa pasta **nova** em `teste/` e abra
  `scormcontent/index.html` com duplo clique.
- **Para você (Claude) conferir no navegador embutido**, que não executa scripts de `file://`:
  copie `<skill>/teste/lms_mock.html` e `<skill>/teste/servidor_sem_cache.py` para `teste/`, rode
  `python teste/servidor_sem_cache.py 8765` (ou configure em `.claude/launch.json` e use
  `preview_start`) e abra `http://localhost:8765/lms_mock.html?pkg=<pasta-extraída>&reset=1`.
  O mock é uma LMS SCORM 1.2 simulada; mostra status, bookmark e `suspend_data` no topo.

O que conferir, no mínimo:
1. O bloco novo aparece na posição certa, com a aparência dos vizinhos.
2. Console sem erros (abra uma aba nova para cada teste — o console acumula mensagens antigas).
3. Interações funcionam (abas alternam, accordion abre, questão corrige, HTML responde).
4. O Continue logo abaixo libera o conteúdo seguinte (e, se for `completeBlock`, fica travado antes).
5. Retomada: recarregue **sem** `reset` e veja se o curso volta à lição e ao progresso.

**Cada versão nova vai para uma pasta de teste nova** (`v1`, `v2`…): o navegador guarda cópia dos
arquivos e pode mostrar a versão anterior com o mesmo endereço.

### 10. Entregar e relatar

Entregue o `.zip` de `saidas/` e um relato curto: o que foi inserido (lição, posição, tipo), o
resultado do `validar.py` e do `verificar_scorm.py`, o que foi visto no navegador e **o que não foi
verificado**. Um relato que afirma mais do que se checou é pior que nenhum.

---

## Regras (e por quê)

- **Nunca altere, remova ou reordene blocos existentes.** O progresso do aluno é gravado na LMS
  **pela posição** dos blocos e lições, não pelo ID. Inserir desloca as posições seguintes.
  - Curso **ainda não publicado**: insira onde quiser.
  - Curso **já publicado com alunos**: insira só **no fim das lições**, ou publique como curso/versão
    nova na LMS. Do contrário, o progresso salvo de quem já começou pode "cair" no bloco errado.
- **Nunca escreva um bloco do zero.** Use sempre um modelo de `<skill>/modelos/`. Campos que parecem
  opcionais podem ser obrigatórios para o player; os modelos vêm de blocos reais do Rise.
- **Nunca gere ou edite IDs à mão.** Os scripts geram no formato certo (UUID ou cuid2, conforme o
  tipo) e garantem que não colidem com nenhum ID do curso.
- **Não invente configurações.** Só o que o modelo declara ajustável. Um tipo de bloco que não está em
  `modelos/` segue o roteiro de `referencias/como-o-rise-funciona.md` ("Tipo de bloco novo").
- **HTML próprio é autocontido.** Nada de fontes, imagens ou scripts da internet: a LMS pode bloquear
  e o curso pode abrir sem internet. Os scripts recusam.
- **O original nunca muda; cada saída é um arquivo novo.**

---

## Verificação de consistência (`verificar_scorm.py`)

Funciona com qualquer pacote do Rise — use também em pacotes que vieram de outra ferramenta ou da
skill `revisar-curso-scorm`. Cada linha é OK, AVISO ou ERRO; com qualquer ERRO o pacote **não** deve
ir para a LMS.

| Checagem | O que um ERRO significa | O que fazer |
|---|---|---|
| 1. Pacote | `.zip` corrompido ou sem arquivo essencial | Gere o pacote de novo a partir do JSON |
| 2. Manifest | Manifest cita arquivo que não existe (a LMS pode recusar o pacote) | Ver se uma pasta HTML faltou no `--anexar` |
| 3. Versão | `coursePackageVersion` diferente entre manifest, `index.html` e `indexAPI.html` | Algo editou esses arquivos à mão; volte ao original |
| 4. Curso | `runtime-data.js` não decodifica | O Base64 foi corrompido; reempacote com `empacotar.py` |
| 5. Estrutura | Lições fora de ordem, `courseId`/`quizId` incoerentes, ID repetido, bloco sem id/type | Corrija o JSON (normalmente edição manual indevida) |
| 6. Tipos | Tipo de bloco que o player deste pacote não conhece — **não será exibido** | Use um tipo existente ou siga "Tipo de bloco novo" |
| 7. Regras | Múltipla escolha sem exatamente 1 correta; Continue com `type` inválido | Corrija o roteiro |
| 8. Arquivos | Bloco HTML sem pasta/`srcdoc`; mídia citada ausente (aviso) | Anexe a pasta / inclua a mídia |
| 9. Comparação | Arquivo do original removido ou alterado fora do previsto | Refaça a partir do original |

**Avisos conhecidos que não indicam quebra:**
- *"correct/corrects … não é id de alternativa"*: o próprio Rise às vezes grava texto de pergunta
  nesses campos em questões de **múltipla resposta**; a correção usa `answers[].correct`. Aparece já
  no pacote original. Vale avisar o usuário para revisar a questão pedagogicamente.
- *"arquivos novos fora de scormcontent/assets/"* só é esperado se alguém acrescentou arquivo
  deliberadamente fora de `assets/` — investigue.

---

## Referências — quando ler cada uma

| Arquivo | Leia quando |
|---|---|
| `referencias/padroes-por-tipo.md` | Sempre, antes de escrever um roteiro (estética e campos de cada tipo) |
| `referencias/bloco-html.md` | Precisar inserir infográfico, atividade ou qualquer HTML próprio |
| `referencias/como-o-rise-funciona.md` | Precisar de um tipo de bloco que não está em `modelos/`, entender IDs, progresso, Continue, conclusão de blocos ou o esquema do player |
| `referencias/armadilhas.md` | Algo der errado ou parecer estranho (cache, BOM, retomada, prints, PowerShell) |
