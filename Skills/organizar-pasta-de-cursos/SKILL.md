---
name: organizar-pasta-de-cursos
description: Regras de onde guardar e como nomear tudo o que é de curso na pasta `Cursos/` do repositório Edicao_de_cursos — empresa, pasta do curso, versões do SCORM (`scorm/vN`), cópias idênticas, material de apoio (`base/`) e o README de cada curso. Use sempre que for salvar, mover, renomear ou procurar um arquivo de curso (pacote SCORM .zip ou pasta extraída, ementa, plano de aula, roteiro, carga horária, conteúdo bruto, pesquisa, análise crítica), criar a pasta de um curso novo, decidir se um SCORM novo é uma versão nova ou cópia de uma que já existe, ou reorganizar pastas — mesmo que o usuário só diga "guarda esse zip", "onde coloco esse roteiro?", "isso é a v2 ou a v3?". As skills criar-ementa-curso, revisar-curso-scorm e inserir-blocos-scorm usam esta para decidir onde entregar.
---

# Organização da pasta `Cursos/`

O repositório guarda o **processo de desenvolvimento** dos cursos: os pacotes SCORM e o apoio que serviu para construí-los. Os cursos publicados vivem na plataforma. Tudo o que é trabalho intermediário (JSONs do Rise, etapas, scripts, prompts) fica **fora** da principal: está na branch `joao`.

## O desenho

```
Cursos/
└── <Empresa>/
    └── <curso>/
        ├── README.md              id do curso na plataforma e para que serve cada pasta
        ├── scorm/
        │   ├── README.md          tabela de versões e «versão publicada na plataforma» (a preencher)
        │   └── vN/                v1 = a mais antiga
        │       ├── <pacote>.zip
        │       ├── <pacote>/      pasta extraída do mesmo zip (se houver)
        │       ├── autor.json     quem fez esta versão: {"autor": "Nome"} (ou {"autor": null} se ainda não se sabe)
        │       └── copias/        pacotes de conteúdo idêntico (outros zips, pastas em outros lugares)
        └── base/                  material de apoio, uma pasta por tipo (abaixo)
```

Exceção: `Cursos/OpenAI/OPENAI (ChatGPT)/LAB-SCORM-sem-Articulate/` é um laboratório de terceiros. **Nunca mova, renomeie nem apague nada dali.**

Sem pastas vazias. Sem arquivo solto na raiz de `Cursos/`.

## 1. Empresa (primeiro nível)

Quem é dono da **ferramenta** ensinada, não quem fez o curso.

| Assunto | Pasta |
|---|---|
| Claude (Chat, Desktop, Code, Cowork, Design, Excel, Word, PowerPoint, Skills, Legal…) | `Anthropic` |
| ChatGPT, Codex | `OpenAI` |
| NotebookLM, Gemini | `Google` |
| Perplexity | `Perplexity` |
| Conceito sem marca (MCP, agentes de IA, vibe coding…) | `iaclube` |
| Curso do programa ARCTEL (título «Módulo N - …») | `ARCTEL` |
| Ferramenta de terceiros (Glau, Bolt, v0, Cursor, n8n, Replit…) | a própria marca, com a grafia dela |

Empresa nova: crie a pasta com o nome da marca e avise o usuário.

## 2. Curso (segundo nível)

**Curso = ferramenta + modalidade**, não o título do pacote. Títulos mudam entre versões («Guia Essencial…», «Primeiros Passos…», «Fundamentos…») e continuam sendo o mesmo curso.

- Formato: `<ferramenta>-<modalidade>`, minúsculas, hífens, sem acento: `claude-chat-essentials`, `claude-power-point-hands-on`, `chatgpt-word-essentials`, `mcp-hands-on`.
- Modalidade: só `essentials` ou `hands-on`.
- O que já existe é a lista de referência: **olhe `ls Cursos/*/`** antes de criar. Se o assunto já tem pasta, o pacote entra nela.
- Nome de pasta novo = assunto novo. Confira com o catálogo (`novos-cursos-iaclube-priorizacao-v6.json`, só na branch `joao`: `git show joao:novos-cursos-iaclube-priorizacao-v6.json`) e **peça confirmação ao usuário** se não estiver lá.
- ARCTEL: `modulo-<N>-parte-<M>-<tema>` (ex.: `modulo-1-parte-1-impactos-do-ecossistema-digital`), uma pasta por parte.
- O id do curso na plataforma (ex.: `curso_ClaudeChatESS`) **não** é o nome da pasta: vai escrito no `README.md` do curso.

## 3. Versões do SCORM (`scorm/vN/`)

**Versão = conteúdo.** Dois pacotes com o mesmo conteúdo são a mesma versão, mesmo que um seja zip, outro pasta extraída, ou estejam em lugares diferentes. Quem decide isso é a impressão digital do conteúdo, não o nome do arquivo.

```bash
python Skills/organizar-pasta-de-cursos/scripts/versao_do_pacote.py PACOTE --curso Cursos/<Empresa>/<curso>
```

O script só lê. Ele diz uma de três coisas:
- **Mesmo conteúdo que a vN** → o pacote vai em `scorm/vN/copias/`. Não crie versão.
- **Conteúdo novo e mais recente** → crie `scorm/v(N+1)/`.
- **Conteúdo novo, mas mais antigo que uma versão existente** → ele ocupa essa posição: renumere de trás para frente com `git mv` e atualize o `scorm/README.md`.

Regras de ordem:
1. **Pela data de publicação** (`lastPublishedAt`, gravada dentro do curso, em UTC). No empate, pelo estágio indicado no nome: original → revisado/editado → V2/v3.
2. **Pipeline da Onda 1** (MCP, NotebookLM, Perplexity): as datas são todas iguais, então a ordem é a das etapas: original do Articulate → revisão de texto (`REVISADO`, `-v2`, `-r2`) → blocos inseridos (`FINAL-com-blocos-vN`).
3. Rascunhos antigos entram como versões antigas pela data, não como `v0`.

Dentro de `vN/`: o zip é o pacote principal; a pasta extraída fica ao lado, com o mesmo nome do zip sem `.zip`. Cópias idênticas com o mesmo nome ganham o sufixo `_copia1`, `_copia2`.

**Autor da versão (`autor.json`).** Cada pasta `vN/` tem um `autor.json` com o autor **daquela versão** (um nome por versão; a v3 pode ser de outra pessoa que a v1):

```json
{ "autor": "Ana Souza" }
```

Ao criar uma versão nova, crie também o `autor.json` (com `{ "autor": null }` se não souber o nome; quem souber troca `null` pelo nome). Um arquivo que já existe **não** se sobrescreve. O extrator de SCORM (`scorm_data_extractor`) lê esse arquivo e mostra o autor no resumo dos cursos; o `autor.json` não é um pacote SCORM e não atrapalha a leitura dos zips e das pastas.

Depois de guardar qualquer pacote, **atualize a tabela do `scorm/README.md`** (versão, data, título, pacote principal, quantas cópias).

## 4. Material de apoio (`base/<tipo>/`)

Só o que serviu para **construir** o curso, e só estes tipos de pasta:

| Pasta | O que vai |
|---|---|
| `ementa/` | Ementa consolidada |
| `plano-de-aula/` | Plano de aula |
| `roteiros/` | Roteiros (Essentials, Hands-on, Articulate, Rise) |
| `carga-horaria/` | Carga horária e tabela MET |
| `conteudo-bruto/` | Texto-fonte que alimentou o curso |
| `pesquisa/` | Pesquisa sobre o assunto |
| `analise/` | Análise crítica |

Mantenha o nome original do arquivo. Material comum a Essentials e Hands-on do mesmo assunto (ementa, análise, conteúdo bruto) é **copiado para os dois cursos**: cada pasta de curso fica completa sozinha. Arquivo idêntico dentro do mesmo curso: guarde **uma** cópia.

**Não entra na principal** (fica na branch `joao`): JSONs de lição, etapas intermediárias, scripts, HTML dos blocos, prompts, versões antigas de plano e roteiro, relatórios de edição, cursos sem SCORM. Se uma skill gerar isso, deixe na pasta de trabalho fora de `Cursos/` e **não** faça commit na principal.

## 5. README

- `<curso>/README.md`: id e título na plataforma, e o que há em `scorm/` e `base/`.
- `<curso>/scorm/README.md`: tabela de versões e o bloco «Versão publicada na plataforma» (versão e data). Quem publica na plataforma preenche; não invente.

## Como proceder

1. Descubra a empresa e o curso (seções 1 e 2). Na dúvida, pergunte.
2. SCORM novo? Rode o script e siga a resposta (seção 3). Documento de apoio? Escolha o tipo (seção 4).
3. Mova com `git mv` quando o arquivo já for do repositório, para preservar o histórico.
4. Atualize os README, confira que não ficou pasta vazia e **commite só o que você tocou**. Não faça `push` sem o usuário pedir.

## Antes de reorganizar em massa

Nunca mova várias pastas sem plano escrito e aprovado. Gere primeiro uma lista origem → destino, confira que todo arquivo tem destino e que nenhum destino se repete, e só então mova, **um commit por empresa**, comparando o conteúdo (hash do blob ou da árvore) antes e depois.
