# Dúvidas · Automação checklist → Notion

Origem: [`_plan/detalhes/readme.md`](../detalhes/readme.md). Plano em [`_plan/fases/`](../fases/00-visao-geral.md). Estado geral: D1 a D8 respondidas; resta só a 1.2 (colunas e tipos do Notion), que a fase F4 descobre sozinha com o token.

<a id="indice"></a>
## Índice

| Nº | Estado | Resumo |
|---|---|---|
| [1](#d1) | 🟡📢 | Como atualizar o Notion: pyautogui ou API |
| ↳ [1.1](#d1) | ✅ | Se pyautogui: como achar a linha do curso |
| ↳ [1.2](#d1) | 🟡 | ID do banco e nomes exatos das colunas |
| [2](#d2) | ✅ | Nome da pasta de automação e de `referencias` |
| [3](#d3) | ✅ | Novo nome da pasta do extrator |
| [4](#d4) | ✅ | Quais abas do `xlsx` viram `csv` |
| [5](#d5) | ✅ | Casar "Curso" do `xlsx` com a pasta em `Cursos/` |
| [6](#d6) | ✅ | De onde vem o autor do `autor.json` |
| ↳ [6.1](#d6) | ✅ | Nome completo ou só primeiro nome |
| ↳ [6.2](#d6) | ✅ | João e Marina marcados juntos |
| [7](#d7) | ✅ | Como calcular Status e Progresso |
| [8](#d8) | ✅ | Como trazer o `xlsx` da `joao` e commitar |

🔴 aberta · 🟡 respondida com pendência · ✅ fechada · 🚨 urgente · 📢 subdúvida aberta · ⏸️ stand-by · ⛔🧐 fora do escopo por ora

---

<a id="d1"></a>
## 1 · 🟡📢 Como atualizar o Notion: pyautogui ou API

**Contexto:** o readme pede pyautogui. Ele clica na tela: quebra com zoom, tema, resolução, janela em segundo plano ou mudança de layout do Notion, e o PC fica preso durante a execução. A API oficial do Notion edita as mesmas colunas (título, status, pessoa/seleção, número) sem tela.

| Opção | 👍 Prós | 👎 Contras |
|---|---|---|
| A ⭐ API oficial do Notion (`NOTION_TOKEN` em variável de ambiente) | Estável, roda em segundo plano, sem mexer no mouse, dá para testar com `--dry-run` | Precisa criar uma integração no Notion e compartilhar o banco com ela (ação sua, uma vez) |
| B pyautogui puro | É o que o readme descreve; não precisa de token | Frágil, lento, ocupa mouse e teclado, difícil de testar, precisa calibrar por tela |
| C Híbrido: API como padrão e módulo pyautogui como plano B | Cobre o caso de a API não ser liberada na sua conta | Dobra o código e a manutenção |

⚠️ Se a coluna "Responsável" for do tipo *Pessoa*, a API precisa do ID do usuário no Notion; se for *Seleção*, basta o nome.

❓ **Pergunta:** A, B ou C?

- [USER] vamos tentar A;

📢 **Pendências:**

| Nº | Estado | Pendência |
|---|---|---|
| 1.1 | ✅ | Só se B ou C: achar a linha por busca do Notion (`Ctrl+F`), por reconhecimento de imagem ou por posição fixa (⭐ busca) |
| 1.2 | 🟡 | 👉 Informar o link do banco do Notion e os nomes exatos das 4 colunas e dos tipos (texto, status, pessoa/seleção, número) |

- [USER]:
link Notion: 
- https://app.notion.com/p/Produ-o-de-cursos-40d4a1ed76b480b18f67febbce8ade93?source=copy_link

📝 **Decisão:** link recebido; **faltam** nomes e tipos das colunas. A fase F4 lê isso pela API (`inspecionar.py`), então não precisa responder. 1.1 não se aplica (escolheu A).

[⬆️ Voltar ao índice](#indice)

---

<a id="d2"></a>
## 2 · ✅ Nome da pasta de automação e de `referencias`

**Contexto:** o readme usa `<AutomacaoUpdate>\<referencias>` como nome provisório. Essa pasta recebe o `xlsx` copiado da `joao`, o `csv` e o código da automação, e fica na raiz do repositório.

| Opção | 👍 Prós | 👎 Contras |
|---|---|---|
| A ⭐ `AutomacaoUpdate/referencias/` | É o nome do seu readme, sem retrabalho | Mistura PascalCase com os outros nomes da raiz (`Cursos`, `Skills`, `bagunca`) |
| B `automacao/referencias/` | Minúsculo, comum em código | Diverge do que você escreveu |
| C `Automacao/entrada/` | "entrada" diz o papel da pasta | Troca os dois nomes do readme |

❓ **Pergunta:** A, B ou C?

- [USER] B;

[⬆️ Voltar ao índice](#indice)

---

<a id="d3"></a>
## 3 · ✅ Novo nome da pasta do extrator

**Contexto:** `_plan/extrator` vai para a raiz. Como é pacote Python (`from ..servico import ...`), o nome precisa ser identificador válido (sem hífen). Exemplo: `python -m extrator_scorm Cursos`. O arquivo de saída vira `Cursos/registro-de-cursos.json` (nome sugerido por você, mantido).

| Opção | 👍 Prós | 👎 Contras |
|---|---|---|
| A ⭐ `extrator_scorm` | Diz o que lê (SCORM) e não colide com outros nomes | Mais longo |
| B `registro_cursos` | Combina com `registro-de-cursos.json` | Esconde que o foco é SCORM |
| C manter `extrator` | Zero troca nos textos e imports | Genérico demais na raiz |

❓ **Pergunta:** A, B ou C?

- [USER] vamos de A;

[⬆️ Voltar ao índice](#indice)

---

<a id="d4"></a>
## 4 · ✅ Quais abas do `xlsx` viram `csv`

**Contexto:** `checklist-producao-de-cursos-60-dias-v0-4.xlsx` tem 8 abas. Só **"Checklist 60 dias"** (104 linhas) tem o status por etapa de cada curso. "Cadastro dos 29" também tem João/Marina/Responsável. As demais são tabelas de apoio. Um `csv` guarda só uma tabela.

| Opção | 👍 Prós | 👎 Contras |
|---|---|---|
| A ⭐ Só "Checklist 60 dias" → um `csv` | Simples; é o que Notion e `autor.json` precisam | Perde "Cadastro dos 29" |
| B Uma aba = um `csv` (`<arquivo>__<aba>.csv`, 8 arquivos) | Nada se perde | Mais arquivos no commit |
| C "Checklist 60 dias" + "Cadastro dos 29" | Cobre os cursos antigos já publicados | Precisa definir qual vale quando há conflito |

❓ **Pergunta:** A, B ou C?

- [USER] A;

[⬆️ Voltar ao índice](#indice)

---

<a id="d5"></a>
## 5 · ✅ Casar "Curso" do `xlsx` com a pasta em `Cursos/`

**Contexto:** o `xlsx` diz `MCP - Essentials`; a pasta é `Cursos/<Empresa>/<slug>/scorm/vN`, por exemplo `Cursos/Google/notebooklm-essentials`. Não há chave comum. Hoje existem 39 pastas de curso e 104 linhas no `xlsx` (muitas ainda não produzidas, então sem pasta).

| Opção | 👍 Prós | 👎 Contras |
|---|---|---|
| A Automático por slug do nome (`MCP - Essentials` → `mcp-essentials`) | Zero manutenção | Erra em nomes diferentes (`ChatGPT Chat` × `openai-chatgpt-chat`) |
| B Tabela manual `mapa-cursos.json` | Exata | Alguém precisa preencher e manter |
| C ⭐ Híbrido: slug propõe, `mapa-cursos.json` confirma/corrige; o que não casa vai para o relatório | Quase tudo sai pronto; só os ambíguos pedem olhar | Um arquivo extra |

📦 O mesmo mapa serve ao `autor.json` e ao Notion.

❓ **Pergunta:** A, B ou C?

- [USER] A;

[⬆️ Voltar ao índice](#indice)

---

<a id="d6"></a>
## 6 · ✅ De onde vem o autor do `autor.json`

**Contexto:** `autor.json` é `{"autor": "Nome"}` ou `{"autor": null}`, um por `vN`. No `xlsx` a coluna "Responsável" está **vazia em todas as 104 linhas**; as colunas "João" e "Marina" têm `x`.

| Opção | 👍 Prós | 👎 Contras |
|---|---|---|
| A ⭐ "Responsável" se preenchido; senão o `x` de João/Marina | Usa o que existe hoje e já funciona quando "Responsável" for preenchida | Regra com duas fontes |
| B Só "Responsável" | Regra única | Hoje não preenche nenhum autor |
| C Só colunas João/Marina | Preenche já | Ignora "Responsável" quando ela existir |

⚠️ Premissa: só **sobrescreve `null`** e só na **última versão** (maior `vN`); autor já escrito à mão nunca é alterado.

❓ **Pergunta:** A, B ou C?

- [USER] A, ``Responsável" se preenchido; senão o `x` de João/Marina``; se não tiver a informação deixa vazio ou null;

📢 **Pendências:**

| Nº | Estado | Pendência |
|---|---|---|
| 6.1 | ✅ | Gravar "João Vitor" / "Marina Moreno" ou só "João" / "Marina" (⭐ nome completo, como no "Como usar" do `xlsx`) |
| | | deixa só a forma curta |
| 6.2 | ✅ | Se as duas colunas têm `x`: gravar `João Vitor; Marina Moreno` ou deixar `null` e avisar no relatório (⭐ relatório) |
| | | deixar `null` |

[⬆️ Voltar ao índice](#indice)

---

<a id="d7"></a>
## 7 · ✅ Como calcular Status e Progresso

**Contexto:** o `xlsx` não tem coluna de progresso pronta e "Status" está vazia. Tem 5 etapas com `x` (E1–2, E3, E4, E5, E6) e "Meta até 12 dez" = `publicado` (97 linhas). Notion pede Status ∈ {Aguardando, Em produção, Concluído} e Progresso em %.

| Opção | 👍 Prós | 👎 Contras |
|---|---|---|
| A ⭐ Progresso = etapas com `x` ÷ 5. Status: `publicado` ou 5/5 → Concluído; 1 a 4 → Em produção; 0 → Aguardando | Regra simples e explicável (ex.: 3 `x` = 60%) | Todas as etapas pesam igual |
| B Progresso por pesos (E4 e E6 valem mais) | Reflete melhor o esforço | Pesos arbitrários, decisão sua |
| C Usar só a coluna "Status" do `xlsx` quando preenchida, A como reserva | Respeita o que a pessoa digitou | A coluna está vazia hoje, então vira A |

⚠️ Conflito possível: `publicado` na Meta com etapas vazias. Na regra A, `publicado` ganha (100%).

❓ **Pergunta:** A, B ou C?

- [USER] A;

[⬆️ Voltar ao índice](#indice)

---

<a id="d8"></a>
## 8 · ✅ Como trazer o `xlsx` da `joao` e commitar

**Contexto:** o `xlsx` só existe na branch `joao` (hoje `v0-3` e `v0-4`); o código nasce na `structuring`, que depois vira `main`. "Mais recente" é o maior número de versão no nome (`v0-4` > `v0-3`). O commit leva só os arquivos do processo e nunca faz push.

| Opção | 👍 Prós | 👎 Contras |
|---|---|---|
| A ⭐ `git fetch` + `git show origin/joao:<arquivo>` e commit na branch atual | Não troca de branch nem mexe nos seus arquivos abertos; fácil de testar | O commit nasce na `structuring`; vai para a `main` junto com o merge |
| B Worktree temporária de `main` | Commit já cai na `main` | Mais lento e complexo; main ainda não tem o código |
| C `git checkout` entre branches | Simples de entender | Perigoso com alterações abertas; derruba o editor |

❓ **Pergunta:** A, B ou C?

- [USER] A;

[⬆️ Voltar ao índice](#indice)
