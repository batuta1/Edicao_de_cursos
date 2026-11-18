# Dúvidas · Interface da automação (tkinter)

Escopo: uma janela desktop para a automação do checklist → Notion, seguindo a skill [`interface-tkinter`](../../.claude/skill/interface-tkinter/SKILL.md). Catálogo das telas: [lista de UIs.md](lista%20de%20UIs.md). Estado geral: D1 e D2 fechadas (pasta comum; atalho executável por pasta). O resto está nas premissas abaixo e só vira pergunta se você discordar.

<a id="indice"></a>
## Índice

| Nº | Estado | Resumo |
|---|---|---|
| [1](#d1) | ✅ | Onde mora a base de UI (fontes e padrão) |
| [2](#d2) | ✅ | Como abrir a tela da automação |
| ↳ [2.1](#d2) | ⏸️ | Gerar `.exe` de verdade (PyInstaller) |

🔴 aberta · 🟡 respondida com pendência · ✅ fechada · 🚨 urgente · 📢 subdúvida aberta · ⏸️ stand-by · ⛔🧐 fora do escopo por ora

## Premissas (sem pergunta; diga se discordar)

| # | Premissa | Por quê |
|---|---|---|
| P1 | Janela **própria** em `scripts/automacao/interface/`, separada da tela do extrator | A skill diz "uma interface não importa de outra" e as duas partes já são independentes |
| P2 | **2 abas**: `Executar` (etapas, ensaio, resultados) e `Notion` (token, colunas) | Só as abas necessárias |
| P3 | Fluxo seguro: marcar etapas → **Ensaio** → conferir a tabela → **Aplicar** (só habilita depois de um ensaio do mesmo `csv`) | O Notion não tem desfazer |
| P4 | Token **não é digitado na tela**: a aba mostra "token encontrado ✔ / ausente" e o botão "Testar conexão" (roda o `inspecionar`); quem edita o `automacao/.env` é você | Evita segredo em campo de texto |
| P5 | Caixa "Fazer commit" marcada por padrão (igual à linha de comando); nunca faz `push` | Mesmo comportamento do CLI |
| P6 | Sem `Cursos/` (branch sem a pasta), as etapas `extrator` e `autores` ficam desativadas com o motivo escrito ao lado | Hoje a `structuring` não tem `Cursos/` |
| P7 | `Parar` vale entre um curso e outro (Notion) ou entre etapas; a tela avisa isso | Regra da skill: avisar quando a parada tem efeito |
| P8 | Mesma lógica do CLI: a janela só chama `automacao.atualizar` / `notion.sincronizar` em thread + fila + `after()`; **nada** de regra dentro dos widgets | Regra da skill: lógica separada dos widgets |
| P9 | Sem arrastar e soltar (não há arquivo para arrastar) | A skill só quer DnD se ajudar |

## Estrutura nova (decisão do usuário, detalhes por conta do plano)

Na `main` as pastas definitivas serão `Cursos/`, `Skills/` e `scripts/`; `bagunca/` é temporária (conteúdo a ser triado depois) e não é tocada.

```
Cursos/  Skills/  bagunca/            (já existem na main; bagunca é temporária)
scripts/
  automacao/        planilha → autores → Notion (+ interface/)
  extrator_scorm/   mapeamento dos SCORM (+ interface/)
  comum/            o que as duas partes usam
    ui/             fontes.py + .ttf + licenças (base da skill interface-tkinter)
    caminhos.py     raiz do repositório, Cursos/, EDICAO_RAIZ
    autor_json.py   ler/escrever autor.json (hoje o automacao importa isso do extrator)
  documentacao/     os guias
pyproject.toml  uv.lock  .gitignore    (na raiz: o uv exige)
```

| # | Premissa da estrutura | Por quê |
|---|---|---|
| P10 | Os comandos **não mudam** (`uv run python -m automacao`, `python -m extrator_scorm`): `automacao`, `extrator_scorm` e `comum` viram pacotes instalados em modo editável a partir de `scripts/` (basta rodar `uv sync` de novo) | Evita `scripts.automacao...` e reescrever toda a documentação |
| P11 | `comum/` não importa de `automacao` nem de `extrator_scorm`; as duas partes só importam de `comum/` | Uma parte funciona sem a outra; o extrator pode ser apagado sem quebrar a automação |
| P12 | Dados gerados vão junto do código que os gera: `scripts/automacao/referencias/`, `scripts/automacao/relatorios/`, `scripts/extrator_scorm/fichas/` etc. `Cursos/registro-de-cursos.json` continua em `Cursos/` | O registro é dado dos cursos, não do script |
| P13 | O `automacao/.env` (token) **muda de lugar junto**: vira `scripts/automacao/.env`; eu movo o arquivo sem ler nem imprimir o conteúdo | O token não pode ficar para trás nem ir para o git |
| P14 | A lista de caminhos permitidos da automação passa a ser `scripts/` e `Cursos/` (continua recusando `bagunca/` e `Skills/`) | Mesma proteção, nova estrutura |
| P15 | A única ligação que sobra entre as partes é o `atualizar.py` chamando o extrator como etapa opcional | Orquestração, não dependência |

---

<a id="d1"></a>
## 1 · ✅ Onde mora a base de UI (fontes e padrão)

**Contexto:** hoje o código de fontes (Ubuntu 11 / SUSE Mono 10, `.ttf`, licenças) está em `extrator_scorm/interface/fontes.py` e `extrator_scorm/fontes/arquivos/`. A automação precisa do mesmo. A skill manda "reutilize; não recrie", mas também que as duas partes do repositório sejam independentes (já separamos as documentações). Exemplo: se `automacao` importar `extrator_scorm`, apagar o extrator quebra a automação.

| Opção | 👍 Prós | 👎 Contras |
|---|---|---|
| A ⭐ Pasta nova `ui_base/` na raiz (`fontes.py` + `.ttf`), usada pelas duas telas | Nenhuma tela depende da outra; um só lugar para corrigir fontes (inclui o conserto para Windows) | Mexe no extrator: ele passa a importar de `ui_base/` |
| B `automacao` importa `extrator_scorm.interface.fontes` | Zero movimentação | Acopla as duas partes; a skill proíbe uma interface importar de outra |
| C Copiar `fontes.py` e os `.ttf` para `automacao/interface/` | Independência total, sem mexer no extrator | Código e fontes duplicados (arquivos pesados) |

⚠️ Achado: no Windows a tela do extrator **não carrega** Ubuntu nem SUSE Mono (o código só trata Linux) e cai em Segoe UI e Courier New. A correção fica no lugar escolhido aqui.

❓ **Pergunta:** A, B ou C?

📝 **Decisão:** a base vai para uma **pasta comum** (opção A, ampliada). Fala do usuário: "seria interessante a gente centralizar esses arquivos comuns [...] uma pasta separada", dentro de uma pasta `scripts/` que reúne automação, extrator, documentação e essa pasta comum. Nome escolhido: **`comum`** (curto, em português, identificador Python válido). Ver "Estrutura nova" abaixo.

[⬆️ Voltar ao índice](#indice)

---

<a id="d2"></a>
## 2 · ✅ Como abrir a tela da automação

**Contexto:** hoje `uv run python -m automacao` **roda tudo** (commit e escrita no Notion incluídos). No extrator, o mesmo gesto sem argumentos abre a tela. Exemplo: alguém digita o comando sem argumentos esperando "ver o que tem" e grava no Notion.

| Opção | 👍 Prós | 👎 Contras |
|---|---|---|
| A ⭐ Comando separado: `uv run python -m automacao.interface` | Não muda o CLI nem a documentação; sem risco de rodar tudo sem querer | Dois comandos diferentes para lembrar |
| B Sem argumentos abre a tela (como no extrator); `--tudo` roda tudo | Igual ao extrator | Muda o comportamento atual e a documentação; quem usava o comando antigo grava sem querer |
| C Flag `--tela` no comando atual | Um comando só | Mistura CLI e janela no mesmo parser |

❓ **Pergunta:** A, B ou C?

📝 **Decisão:** nenhuma das três como estava; o usuário escolheu um **atalho executável em cada pasta** que só abre a interface. Fala dele: "seria legal a gente ter um executável em cada uma das pastas [...] no máximo, algum comando que compila e cria esse executável [...] pode ficar no README da pasta, uma resumida, e fica só realmente o comando que chama a interface de usuário [...] a gente precisa disso logo".
- Por baixo, o comando da tela da automação é `uv run python -m automacao.interface` (opção A) e o do extrator já existe (`uv run python -m extrator_scorm`). O CLI da automação **não muda** (`uv run python -m automacao` continua rodando as etapas).
- O "executável" de agora é um **atalho de duplo clique** (`.bat`) que roda esse comando: `scripts/automacao/abrir-interface.bat` e `scripts/extrator_scorm/abrir-interface.bat`. Mais rápido, sem compilar nada.
- O README de cada pasta fica curto: o que é, o comando/atalho que abre a interface e um link para `scripts/documentacao/`.

📢 **Pendências:**

| Nº | Estado | Pendência |
|---|---|---|
| 2.1 | ⏸️ | Gerar `.exe` de verdade (PyInstaller) com um comando de compilar: fica em **stand-by**, só depois que as telas estiverem prontas e se ainda fizer falta |

[⬆️ Voltar ao índice](#indice)
