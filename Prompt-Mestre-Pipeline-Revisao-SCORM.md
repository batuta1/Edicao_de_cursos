# Prompt-Mestre — Pipeline de Revisão de Curso Publicado (SCORM)
### (SCORM → Desserialização → Revisão por Lição → Serialização → SCORM Revisado)

> **Arquivo-irmão de `Prompt-Mestre-Pipeline-Completo-Curso.md`.** Aquele cobre a *criação* do
> conteúdo (roteiro → auditoria → reconstrução → trilhas → material pronto para o Rise 360) e
> termina no arquivo `.md` que é montado manualmente no Rise. **Este aqui começa depois:** pega o
> pacote SCORM já exportado do Rise e faz o ciclo de revisão textual sem quebrar o curso.

---

## Visão Geral do Pipeline

| Fase | O que faz | Ferramenta | Saída |
|---|---|---|---|
| 0 | Recebe o pacote e define nomes | — | plano de trabalho |
| 1 | Acha o payload do curso dentro do `.zip` | Python inline | string Base64 |
| 2 | Desserializa **e confere a identidade do curso** | Python inline | `curso[Nome].json` |
| 3 | Quebra o curso em arquivos de lição | `lessonExtracter.py` | `licoes_extraidas_[Nome]/` |
| 4 | Revisa o texto pedagógico das lições | `promptRevisaoPorClaude.md` | lições editadas |
| 5 | Valida que só o texto mudou | Python inline | relatório de divergências |
| 6 | Remonta o curso e serializa | `lessonExtracterTester.py` / `serialize.py` | `curso[Nome]_editado_base64.txt` |
| 7 | Reinsere o Base64 no pacote SCORM | Python inline | `[Pacote]-REVISADO.zip` |
| 8 | Testa o pacote em navegador | mock de LMS | confirmação visual |
| 9 | Gera o relatório de alterações | — | `Relatorio_Edicao_Licoes.md` |

**Regra de ouro deste pipeline:** o valor está em **melhorar o texto sem quebrar a engenharia do
arquivo**. Toda fase tem uma verificação; nenhuma fase avança com a verificação falhando.

---

## OBJETO BASE (preencher uma única vez)

```text
- Pacote SCORM de entrada: [ex.: EssentialsClaudeDesign.zip]
- Nome curto do curso:     [ex.: ClaudeDesign  — vira "Essentials" ou "HandsOn" no sufixo]
- Trilha:                  [Essentials | HandsOn]
- Título esperado:         [ex.: "Claude Design - Essentials" — usado na conferência da Fase 2]
- Material-fonte:          [caminho do roteiro/plano de aula que originou o curso]
```

**Onde ficam as coisas (estrutura real deste projeto):**

```
Edicao_de_cursos/
├── [Pacote].zip                                  ← entrada (pacote SCORM exportado do Rise)
├── [Pacote]-REVISADO.zip                         ← saída da Fase 7
├── promptRevisaoPorClaude.md                     ← regras de edição (Fase 4)
├── Criacao de Cursos/
│   └── [Ferramenta]/[Curso]/                     ← MATERIAL-FONTE (roteiro + planos de aula)
│       ├── roteiro-curso-[slug].md
│       ├── essentials/plano-de-aula-...-rise360.md
│       └── hands-on/...-hands-on-articulate-rise360.md
└── cursos_desserializados/                       ← diretório de trabalho; rode os scripts DAQUI
    ├── desserialize.py          (template, base64 hardcoded)
    ├── lessonExtracter.py       (caminhos hardcoded)
    ├── lessonExtracterTester.py (caminhos hardcoded)
    ├── serialize.py             ✅ genérico, aceita argumentos
    ├── naousar/                 ⛔ scripts abandonados — NÃO USAR
    ├── curso[Nome].json                          ← saída da Fase 2
    ├── licoes_extraidas_[Nome]/                  ← saída da Fase 3
    │   ├── licao_01_....json
    │   ├── indice_licoes.json
    │   └── Relatorio_Edicao_Licoes.md            ← saída da Fase 9
    ├── curso[Nome]_editado.json                  ← saída da Fase 6
    └── curso[Nome]_editado_base64.txt            ← saída da Fase 6
```

---

## Modo de Execução

- Rode **sempre a partir de `cursos_desserializados/`** — os scripts usam `Path(__file__).parent`,
  e os scripts auxiliares abaixo assumem esse diretório como raiz.
- **Nunca sobrescreva o `.zip` original.** A saída é sempre um arquivo novo, com sufixo `-REVISADO`.
- **Nunca edite os scripts em `naousar/`.** Estão marcados como abandonados de propósito.
- Antes de sobrescrever qualquer arquivo já existente (`curso[Nome].json`, `_editado_base64.txt`),
  **olhe o que tem nele** — pode ser uma revisão anterior legítima.
- Python está disponível (3.14+). Node **não** está.

> 🚨 **REGRA DE OURO DO AMBIENTE — não use `python -c "..."` neste projeto.**
> O shell é **PowerShell 5.1**, que tenta interpretar o conteúdo de strings com aspas duplas e
> **quebra** em qualquer regex com colchetes: `[A-Za-z0-9+/=]` vira erro de parser
> (`] ausente no final do atributo`). Isso foi testado e confirmado.
> **Sempre grave o código em um arquivo `.py` temporário** (com a ferramenta Write, que não sofre
> escaping de shell) e rode `python arquivo.py`. Todos os blocos deste documento já estão nesse
> formato. Guarde os auxiliares no diretório de scratchpad da sessão, não na pasta do projeto.

---
---

# FASE 1 — Localizar o payload dentro do SCORM

O curso inteiro vive **codificado em Base64** dentro do pacote. Existem **dois formatos**, e o
primeiro passo é descobrir qual você tem em mãos.

| Formato | Arquivo que carrega o payload | Padrão no arquivo |
|---|---|---|
| **Default** (atual) | `scormcontent/runtime-data.js` | `__jsonp("runtime-data.js","BASE64...")` |
| **Legacy** (antigo) | `scormcontent/index.html` | `Promise.resolve(deserialize("BASE64..."))` |

Nos dois casos o payload é **Base64 simples de JSON em UTF-8** — `atob` + `JSON.parse`, nada além
disso.

Grave como `_fase1_formato.py` e rode com `python _fase1_formato.py`:

```python
import zipfile

PACOTE = r'../[Pacote].zip'

nomes = zipfile.ZipFile(PACOTE).namelist()
if 'scormcontent/runtime-data.js' in nomes:
    print('FORMATO: Default -> payload em scormcontent/runtime-data.js')
elif 'scormcontent/index.html' in nomes:
    print('FORMATO: Legacy  -> payload embutido em scormcontent/index.html')
else:
    print('FORMATO DESCONHECIDO — inspecione manualmente:')
    print(nomes[:40])
print('Total de arquivos no pacote:', len(nomes))
```

*(Testado: retorna `Default` para `HandsOnClaudeDesign-Default.zip` — 74 arquivos — e `Legacy` para
`EssentialsClaudeDesign.zip` — 73 arquivos.)*

> ⚠️ **`lzwcompress.js` é uma pista falsa.** O pacote inclui essa biblioteca de compressão LZW, mas
> ela **não** é usada no conteúdo do curso — serve para os dados de bookmark/progresso da LMS. Não
> tente descomprimir o payload com LZW; ele é Base64 puro.

---

# FASE 2 — Desserializar e **conferir a identidade do curso**

Esta é a fase onde já houve um acidente real neste projeto: um arquivo `cursoXHandsOn.json` foi
gravado com o conteúdo do curso **Essentials** (mesmo hash, mesmo título), e o erro só apareceu
muito depois. **A conferência de identidade abaixo não é opcional.**

Grave como `_fase2_desserializar.py` e rode com `python _fase2_desserializar.py`:

```python
import zipfile, re, base64, json, pathlib

PACOTE = r'../[Pacote].zip'
FORMATO = 'default'                    # 'default' ou 'legacy'
SAIDA = 'curso[Nome].json'
TITULO_ESPERADO = '[Título esperado]'

z = zipfile.ZipFile(PACOTE)
if FORMATO == 'default':
    texto = z.read('scormcontent/runtime-data.js').decode('utf-8')
    padrao = r'__jsonp\("runtime-data\.js","([A-Za-z0-9+/=]+)"\)'
else:
    texto = z.read('scormcontent/index.html').decode('utf-8')
    padrao = r'deserialize\("([A-Za-z0-9+/=]+)"\)'

m = re.search(padrao, texto)
assert m, 'PAYLOAD NAO ENCONTRADO — confira o formato'
b64 = m.group(1)
dados = json.loads(base64.b64decode(b64 + '=' * (-len(b64) % 4)).decode('utf-8'))

titulo = dados['course']['title']
print('Titulo :', titulo)
print('ID     :', dados['course']['id'])
print('Licoes :', len(dados['course']['lessons']))
for l in sorted(dados['course']['lessons'], key=lambda x: x.get('position', 0)):
    print('  ', l['position'], l['title'], l['id'])

# --- TRAVA DE SEGURANCA: nao prossiga se o curso nao for o esperado ---
assert titulo == TITULO_ESPERADO, f'TITULO DIVERGENTE! esperado={TITULO_ESPERADO!r} obtido={titulo!r}'

destino = pathlib.Path(SAIDA)
if destino.exists():
    antigo = json.loads(destino.read_text(encoding='utf-8'))
    print()
    print('ATENCAO: arquivo ja existe. Titulo atual no disco:', antigo['course']['title'])
    print('Confira se sobrescrever e mesmo o desejado antes de prosseguir.')

destino.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding='utf-8')
print()
print('Gravado:', SAIDA)
```

*(Testado nos dois formatos. A trava foi verificada também no caso negativo: com um título esperado
propositalmente errado, o `assert` bloqueia a execução antes de gravar qualquer coisa.)*

**Critério de êxito:** título e quantidade de lições batem com o curso esperado, e os títulos das
lições listadas são de fato os daquele curso (não os de outro).

> 📌 **Sobre `desserialize.py`:** ele existe, mas é um **template**, não uma ferramenta. O Base64
> fica *hardcoded* na linha 4 e o nome do arquivo de saída está fixo no código (e frequentemente
> desatualizado — a mensagem de sucesso chega a citar outro curso). Prefira o comando acima, que lê
> direto do `.zip` e confere a identidade. Se for usar o script, reescreva as duas coisas antes.

---

# FASE 3 — Quebrar o curso em arquivos de lição

Use **`lessonExtracter.py`**. Ele tem dois caminhos hardcoded no topo, que precisam apontar para o
curso da vez:

```python
# linha ~6
arquivo_entrada = Path(__file__).parent / "curso[Nome].json"
# linha ~9
pasta_saida = Path(__file__).parent / "licoes_extraidas_[Nome]"
```

Edite essas duas linhas e rode:

```bash
python lessonExtracter.py
```

O script ordena as lições por `position`, gera `licao_NN_[Título].json` (um arquivo por lição, cada
um com `numero_da_licao`, `position_original`, `title` e o objeto `lesson` inteiro) e um
`indice_licoes.json`.

**Critério de êxito:** a pasta tem exatamente o mesmo número de arquivos `licao_*.json` que o curso
tem lições, e o `indice_licoes.json` lista todas na ordem correta.

---

# FASE 4 — Revisão editorial das lições

**Esta é a única fase em que o conteúdo muda.** As regras completas estão em
**`promptRevisaoPorClaude.md`** — leia esse arquivo e siga-o integralmente. O resumo operacional:

### 4.1 — Ache o material-fonte primeiro (não pule)

O curso foi gerado por IA a partir de um roteiro/plano de aula humano. **Esse roteiro é a
referência principal da revisão** (seção 9 do prompt de revisão). Ele fica em:

```
Criacao de Cursos/[Ferramenta]/[Curso]/
├── roteiro-curso-[slug].md                                    ← analogias e exemplos concretos
├── essentials/plano-de-aula-[slug]-essentials-...rise360.md   ← objetivos verbatim, trilha Essentials
└── hands-on/[slug]-hands-on-articulate-rise360.md             ← prompts verbatim, trilha Hands-on
```

Monte o **mapeamento lição ↔ módulo/oficina** antes de editar (às vezes é 1:1, às vezes uma lição
condensa duas oficinas). Registre esse mapeamento no relatório final.

### 4.2 — O que costuma estar ruim (padrões recorrentes já observados)

| Padrão | Sintoma | Correção |
|---|---|---|
| Abertura genérica | "surge como uma solução inovadora", "representa um diferencial" | Trocar pela analogia concreta do roteiro-fonte |
| Lead-in inconsistente | Cada lição parafraseia a lista de objetivos de um jeito | Padronizar: "Ao final desta lição, você será capaz de:" |
| Objetivo trocado | Item da lista não corresponde ao objetivo real do módulo | Alinhar, em ordem, ao plano de aula |
| Fechamento motivacional | "Parabéns! Continue explorando..." | Trocar pelos próximos passos concretos do roteiro |
| Especificidade perdida | "uma conta ativa no serviço necessário" | Restaurar o detalhe do roteiro (qual serviço, qual plano) |

**Não mexa** no que já reproduz bem o roteiro — accordions, flashcards, exercícios guiados com
breadcrumbs e prompts entre aspas triplas costumam estar corretos e devem ser preservados.

### 4.3 — Limites rígidos

- Altere **apenas** campos textuais pedagógicos: `paragraph`, `description`, `heading`, `title` (só
  de conteúdo), `feedback`. Na prática, a esmagadora maioria das edições cai em **`paragraph`**.
- **Nunca** altere `id`, `type`, `family`, `variant`, `position`, `settings`, `metadata`,
  `globalBlockId`, nem a quantidade/ordem de blocos, itens de lista ou alternativas de quiz.
- **Nunca** mude qual alternativa de quiz é a correta. Se achar que o gabarito está errado, **não
  corrija em silêncio** — registre em "Pontos de atenção" no relatório e proponha a correção.
- Edite por **substituição pontual de string** (ferramenta Edit), nunca reescrevendo o arquivo
  inteiro — isso preserva indentação e evita alteração acidental de estrutura.

> ⚠️ **Aspas dentro do JSON.** Ao inserir texto com aspas (`"não gostei"`), elas precisam sair
> escapadas no arquivo (`\"não gostei\"`). Depois de qualquer edição com aspas, valide o arquivo
> (`json.load`) antes de seguir.

---

# FASE 5 — Validação estrutural (antes de remontar)

Compara cada lição editada, nó a nó, contra o curso original. Só campos de texto podem divergir.

Grave como `_fase5_validar.py` e rode com `python _fase5_validar.py`:

```python
import json, pathlib

ORIGINAL = 'curso[Nome].json'
PASTA = 'licoes_extraidas_[Nome]'
CAMPOS_TEXTO = {'paragraph', 'description', 'heading', 'title', 'feedback'}

curso = json.loads(pathlib.Path(ORIGINAL).read_text(encoding='utf-8'))
por_id = {l['id']: l for l in curso['course']['lessons']}

estruturais, textuais = [], []


def comparar(a, b, caminho):
    if isinstance(a, dict) and isinstance(b, dict):
        if a.keys() != b.keys():
            estruturais.append(f'CHAVES {caminho}: {set(a) ^ set(b)}')
        for k in a.keys() & b.keys():
            comparar(a[k], b[k], f'{caminho}.{k}')
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            estruturais.append(f'TAMANHO {caminho}: {len(a)} -> {len(b)}')
        for i in range(min(len(a), len(b))):
            comparar(a[i], b[i], f'{caminho}[{i}]')
    elif type(a) is not type(b):
        estruturais.append(f'TIPO {caminho}')
    elif a != b:
        campo = caminho.split('.')[-1].split('[')[0]
        (textuais if campo in CAMPOS_TEXTO else estruturais).append(f'{campo} em {caminho}')


total = 0
for arq in sorted(pathlib.Path(PASTA).glob('licao_*.json')):
    editada = json.loads(arq.read_text(encoding='utf-8'))['lesson']
    assert editada['id'] in por_id, f'{arq.name}: lesson.id nao existe no curso original!'
    estruturais.clear()
    textuais.clear()
    comparar(por_id[editada['id']], editada, 'lesson')
    total += len(textuais)
    status = 'OK' if not estruturais else f'{len(estruturais)} PROBLEMAS'
    print(f'{arq.name}')
    print(f'   texto alterado : {len(textuais)}')
    for t in textuais:
        print(f'      - {t}')
    print(f'   ESTRUTURA      : {status}')
    for e in estruturais:
        print(f'      !! {e}')
print()
print('TOTAL de campos de texto alterados:', total)
```

*(Testado contra a revisão real do Claude Design Essentials: reportou `ESTRUTURA: OK` nas 6 lições e
18 campos de texto alterados — exatamente o que havia sido editado de propósito.)*

**Critério de êxito:** `ESTRUTURA: OK` em **todas** as lições, e a lista de campos de texto alterados
bate exatamente com o que você editou de propósito. Qualquer `!!` interrompe o pipeline.

---

# FASE 6 — Remontar o curso e serializar

### Opção A — trilha com script pronto (`lessonExtracterTester.py`)

Tem caminhos hardcoded no topo (linhas ~11-15). Ajuste-os e rode:

```bash
python lessonExtracterTester.py
```

Gera `curso[Nome]_editado.json` **e** `curso[Nome]_editado_base64.txt` de uma vez.

> 🟡 **Falso alarme esperado:** o script tem uma sentinela de teste `frase_teste = "XXXX"` e imprime
> `ERRO: a frase de teste NÃO está dentro do objeto final` quando não a encontra. **Isso é normal e
> inofensivo** em uso real — a frase só existe quando alguém está testando o script de propósito.
> Outra mensagem cita `cursoChatGPTExcel_editado.json` (texto antigo, hardcoded). Ignore ambas; o
> que importa são os dois arquivos gerados.

### Opção B — fusão inline + `serialize.py` (recomendada para cursos novos)

`serialize.py` é o **único script genérico** do conjunto: aceita argumentos, confere o round-trip
sozinho antes de gravar e faz backup `.bak` da versão anterior.

Grave como `_fase6_fundir.py`, rode, e em seguida chame o `serialize.py`:

```python
import json, pathlib

ORIGINAL = 'curso[Nome].json'
PASTA = 'licoes_extraidas_[Nome]'
SAIDA = 'curso[Nome]_editado.json'

curso = json.loads(pathlib.Path(ORIGINAL).read_text(encoding='utf-8'))
por_id = {l['id']: l for l in curso['course']['lessons']}

editadas = []
for arq in sorted(pathlib.Path(PASTA).glob('licao_*.json')):
    c = json.loads(arq.read_text(encoding='utf-8'))
    assert c['lesson']['id'] in por_id, f'{arq.name}: lesson.id fora do curso!'
    editadas.append((c['numero_da_licao'], c['lesson']))
editadas.sort(key=lambda x: x[0])

assert len(editadas) == len(curso['course']['lessons']), 'QUANTIDADE DE LICOES MUDOU!'
curso['course']['lessons'] = [l for _, l in editadas]
pathlib.Path(SAIDA).write_text(json.dumps(curso, ensure_ascii=False, indent=2), encoding='utf-8')
print('Gerado:', SAIDA, '| licoes:', len(editadas))
```

```bash
python serialize.py curso[Nome]_editado.json curso[Nome]_editado_base64.txt
```

> ⚠️ **Sempre passe os dois argumentos.** Sem eles, `serialize.py` usa defaults hardcoded que
> apontam para o curso **Cowork** e você sobrescreve o arquivo errado.

**Critério de êxito:** `serialize.py` imprime "Arquivo Base64 gerado com sucesso" (ele só grava se o
round-trip Base64→JSON bater exatamente) e o título/quantidade de lições no resumo estão corretos.

---

# FASE 7 — Reinserir o Base64 no pacote SCORM

Copia o `.zip` original e troca **apenas** o arquivo que carrega o payload. Todo o resto do pacote
(fontes, JS, CSS, imagens, manifest) fica intocado.

Grave como `_fase7_reempacotar.py` e rode com `python _fase7_reempacotar.py`:

```python
import zipfile, re, pathlib, base64, json

PACOTE_IN = r'../[Pacote].zip'
PACOTE_OUT = r'../[Pacote]-REVISADO.zip'
FORMATO = 'default'                    # 'default' ou 'legacy'
B64 = pathlib.Path('curso[Nome]_editado_base64.txt').read_text(encoding='utf-8').strip()

alvo = 'scormcontent/runtime-data.js' if FORMATO == 'default' else 'scormcontent/index.html'

zin = zipfile.ZipFile(PACOTE_IN)
original = zin.read(alvo).decode('utf-8')
if FORMATO == 'default':
    novo = re.sub(r'(__jsonp\("runtime-data\.js",")[A-Za-z0-9+/=]+("\))',
                  lambda m: m.group(1) + B64 + m.group(2), original, count=1)
else:
    novo = re.sub(r'(deserialize\(")[A-Za-z0-9+/=]+("\))',
                  lambda m: m.group(1) + B64 + m.group(2), original, count=1)
assert novo != original, 'SUBSTITUICAO NAO OCORREU — confira o padrao/formato'

# zipfile nao substitui entradas in-place: reescreve o pacote trocando so o alvo
with zipfile.ZipFile(PACOTE_OUT, 'w', zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        dados = novo.encode('utf-8') if item.filename == alvo else zin.read(item.filename)
        zout.writestr(item, dados)

# --- VERIFICACAO ---
za, zb = zipfile.ZipFile(PACOTE_IN), zipfile.ZipFile(PACOTE_OUT)
assert len(za.namelist()) == len(zb.namelist()), 'QUANTIDADE DE ARQUIVOS MUDOU!'
difs = [n for n in za.namelist()
        if n != alvo and za.getinfo(n).file_size != zb.getinfo(n).file_size]
print('Arquivos no pacote     :', len(zb.namelist()))
print('Alterados fora do alvo :', len(difs), difs[:5])

conteudo = zb.read(alvo).decode('utf-8')
m = re.search(r'"([A-Za-z0-9+/=]{500,})"', conteudo)
d = json.loads(base64.b64decode(m.group(1) + '=' * (-len(m.group(1)) % 4)).decode('utf-8'))
print('Titulo no pacote novo  :', d['course']['title'], '| licoes:', len(d['course']['lessons']))
print('OK ->', PACOTE_OUT)
```

*(Testado de ponta a ponta: gerou `Alterados fora do alvo: 0` e um payload **byte a byte idêntico**
ao pacote revisado que havia sido produzido antes por outro caminho — validação cruzada de duas
implementações independentes.)*

**Critério de êxito:** `Alterados fora do alvo: 0`, mesma contagem de arquivos, e o título/lições
decodificados do pacote novo conferem.

---

# FASE 8 — Testar o pacote em navegador

> ⚠️ **O pacote se recusa a renderizar fora de uma LMS.** Abrir `index.html` direto mostra
> *"Error: Content launched outside of a supported LMS enviroment."* **Isso é comportamento
> original, não regressão da sua edição** — confirme abrindo o `.zip` original do mesmo jeito antes
> de suspeitar do seu trabalho.

Para ver o curso de verdade, extraia o pacote e sirva por HTTP com um mock mínimo da API de LMS.
Crie `lms_mock.html` **na raiz da pasta extraída** (irmão de `scormcontent/`):

```html
<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>LMS Mock</title></head>
<body style="margin:0">
<script>
  window.IsLmsPresent = function () { return true; };
  window.getCourseTitle = function () { return "Preview"; };
  window.INTERACTION_RESULT_CORRECT = "correct";
  window.INTERACTION_RESULT_WRONG = "wrong";
  window.LESSON_STATUS_PASSED = "passed";
  ['CommitData','ConcedeControl','CreateResponseIdentifier','Finish','GetDataChunk','GetStatus',
   'GetStudentID','MatchingResponse','RecordFillInInteraction','RecordMatchingInteraction',
   'RecordMultipleChoiceInteraction','ResetStatus','SetBookmark','SetDataChunk','SetFailed',
   'SetLanguagePreference','SetPassed','SetReachedEnd','SetScore','WriteToDebug']
  .forEach(function (n) { window[n] = function () {
      if (n === 'GetDataChunk') return '';
      if (n === 'GetStatus') return 'incomplete';
      if (n === 'GetStudentID') return 'preview-user';
      return true; }; });
</script>
<iframe src="scormcontent/index.html" style="width:100%;height:100vh;border:0;display:block"></iframe>
</body></html>
```

```bash
python -m http.server 8743 --directory "[pasta extraída]"
```

Abra `http://localhost:8743/lms_mock.html`, entre no curso e **confirme visualmente pelo menos um
trecho que você editou**. Ao terminar, pare o servidor e apague a pasta extraída e o mock.

---

# FASE 9 — Relatório de alterações

Grave `Relatorio_Edicao_Licoes.md` **dentro da pasta `licoes_extraidas_[Nome]/`**, seguindo o padrão
já usado nas outras pastas do projeto. Seções obrigatórias:

1. **Arquivos editados** (e os lidos sem alteração, explicitamente).
2. **Roteiro-fonte utilizado** + tabela de mapeamento lição ↔ módulo/oficina.
3. **Critério aplicado** — o que você decidiu mexer e o que preservou, e por quê.
4. **Alterações realizadas**, lição a lição, dizendo *o que estava ruim* e *o que a fonte dizia*.
5. **Campos textuais alterados** — contagem por campo e por lição.
6. **Validação estrutural** — resultado da Fase 5 e da Fase 7.
7. **Pontos de atenção** — gabaritos suspeitos, conteúdo faltante, o que exige revisão humana.
8. **Remontagem, serialização e teste** — formato do pacote, arquivos gerados, resultado da Fase 8.

Linguagem objetiva, sem autoelogio. Se algo não foi verificado, **diga que não foi**.

---
---

## Armadilhas Conhecidas (aprendidas errando)

| # | Armadilha | Como evitar |
|---|---|---|
| 1 | **Arquivo de curso com conteúdo de outro curso.** Já aconteceu: `cursoXHandsOn.json` era cópia byte a byte do Essentials, e o erro passou despercebido por dias. | Trava de identidade da Fase 2 (`assert titulo == esperado`) + conferir os títulos das lições listadas. |
| 2 | **`serialize.py` sem argumentos** grava por cima do curso Cowork. | Sempre passar entrada e saída explicitamente. |
| 3 | **`lessonExtracterTester.py` grita `ERRO: frase de teste`** — é sentinela `"XXXX"`, inofensiva. | Ignorar; conferir os arquivos gerados. |
| 4 | **`desserialize.py` é template**, com Base64 e nome de saída hardcoded (e mensagem citando outro curso). | Usar o comando da Fase 2, ou reescrever as duas linhas antes de rodar. |
| 5 | **Pasta `naousar/`** tem uma versão mais completa (com patch de HTML) que foi abandonada. | Não usar. Se precisar da lógica, ela está replicada e corrigida neste documento. |
| 6 | **`lzwcompress.js` sugere compressão LZW** no payload — não é. | Payload é Base64 puro. |
| 7 | **Aspas não escapadas** em texto editado quebram o JSON silenciosamente até o próximo parse. | Validar `json.load` após cada edição com aspas. |
| 8 | **`python -c "..."` quebra no PowerShell 5.1.** Qualquer regex com colchetes (`[A-Za-z0-9+/=]`) vira erro de parser antes de o Python rodar. Confirmado na prática. | Gravar o código em `.py` com a ferramenta Write e rodar `python arquivo.py`. Nunca inline. |
| 9 | **PowerShell 5.1 + UTF-8 sem BOM:** `Get-Content` sem `-Encoding UTF8` mostra `lição` como `liÃ§Ã£o` — parece corrupção, mas o arquivo está certo. | Ler bytes e decodificar como UTF-8 explicitamente antes de concluir que algo corrompeu. |
| 10 | **Script `.ps1` sem BOM com acentos/travessões** dá erro de parser no PowerShell 5.1 (o erro aparece em linha/coluna que não tem nada de errado). | Manter auxiliares em ASCII puro — ou, melhor, usar Python. |
| 11 | **Erro de LMS ao abrir o curso** parece regressão, mas é o comportamento normal do pacote. | Comparar com o `.zip` original antes de investigar. |
| 12 | **Caminhos com acento/espaço** (`João Victor`, `Editar Cursos`) quebram scripts que embutem o caminho no código-fonte. | Passar caminhos como parâmetro na invocação, não hardcoded no `.ps1`. |

---

## Checklist Final

- [ ] Formato do pacote identificado (Default ou Legacy).
- [ ] `curso[Nome].json` gerado **com título e lições conferidos**.
- [ ] `licoes_extraidas_[Nome]/` com o número correto de lições.
- [ ] Material-fonte localizado e mapeamento lição ↔ módulo registrado.
- [ ] Revisão feita apenas em campos textuais permitidos, por substituição pontual.
- [ ] Fase 5: `ESTRUTURA: OK` em todas as lições.
- [ ] Nenhum gabarito de quiz alterado (divergências registradas, não corrigidas em silêncio).
- [ ] `curso[Nome]_editado_base64.txt` gerado com round-trip aprovado.
- [ ] `[Pacote]-REVISADO.zip` gerado; `0` arquivos alterados fora do alvo.
- [ ] Curso aberto em navegador e trecho editado conferido visualmente.
- [ ] `Relatorio_Edicao_Licoes.md` escrito, incluindo o que **não** foi verificado.
- [ ] Pastas temporárias de preview e servidores removidos.
- [ ] `.zip` original **não** foi modificado.

---

## Resultado Final Esperado

```
Edicao_de_cursos/
├── [Pacote].zip                                   ← intocado
├── [Pacote]-REVISADO.zip                          ← ✅ entregável: pronto para a plataforma
└── cursos_desserializados/
    ├── curso[Nome].json                           ← curso original desserializado
    ├── curso[Nome]_editado.json                   ← curso com as lições revisadas
    ├── curso[Nome]_editado_base64.txt             ← ✅ entregável: para colagem manual, se preferir
    └── licoes_extraidas_[Nome]/
        ├── licao_01_....json ... licao_NN_....json
        ├── indice_licoes.json
        └── Relatorio_Edicao_Licoes.md             ← ✅ entregável: o que mudou e por quê
```

**Dois caminhos de entrega, ambos válidos:** o `-REVISADO.zip` (importar direto na plataforma) ou o
`_editado_base64.txt` (colar manualmente no HTML, fluxo original do projeto). O `.txt` é gerado de
qualquer forma — a Fase 7 é um extra, não substitui o fluxo manual.
