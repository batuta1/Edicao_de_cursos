<!--
Catálogo das interfaces de usuário do projeto (sem dúvidas nem opções). Um H2 por interface, com Descrição + Funções esperadas.
Toda interface nova citada em qualquer conversa entra aqui. Padrão visual: skill `interface-tkinter`.
-->
# Lista de UIs

<a id="indice"></a>
## Índice

| Nº | Estado | Interface |
|---|---|---|
| [1](#u1) | ✅ existe | Extrator de SCORM (`scripts/extrator_scorm/interface/tela.py`) |
| [2](#u2) | ✅ existe | Automação checklist → Notion (`scripts/automacao/interface/`) |

---

<a id="u1"></a>
## 1 · Extrator de SCORM

**Descrição:** janela tkinter com 2 abas (`Pasta de cursos` e `Individual`) para varrer `Cursos/`, extrair as fichas dos pacotes e ver o JSON de um pacote só. Abrir: duplo clique em `scripts/extrator_scorm/abrir-interface.bat` ou `uv run python -m extrator_scorm`.

**Funções esperadas:**
- Escolher a pasta de cursos (já vem preenchida com `Cursos/`) e **Varrer** (só lista).
- **Extrair tudo** (lote, com `Parar`), opções "só as últimas versões" e "forçar".
- Mostrar o resultado numa tabela e o relatório em texto monoespaçado.
- Aba `Individual`: escolher um `.zip`, ver o JSON, gravar em `fichas/_individuais/`.

[⬆️ Voltar ao índice](#indice)

---

<a id="u2"></a>
## 2 · Automação checklist → Notion

**Descrição:** janela tkinter com 2 abas (`Executar` e `Notion`) para rodar as etapas da automação (`checklist`, `extrator`, `autores`, `notion`) com ensaio antes de gravar. Abrir: duplo clique em `scripts/automacao/abrir-interface.bat` ou `uv run python -m automacao.interface`. Decisões em [02-interface-automacao.md](02-interface-automacao.md).

**Funções esperadas:**
- **Aba Executar:** caixas das 4 etapas e "Fazer commit" (marcada); botões `Ensaio`, `Aplicar` (só depois de um ensaio da mesma seleção, com confirmação) e `Parar`; mensagem de estado; tabela por curso (curso, status, progresso, responsável, resultado); relatório em texto monoespaçado (somente leitura).
- **Aba Notion:** estado do token (ver sem digitar), botão `Testar conexão`, lista de colunas e tipos encontrados, estado da fonte de dados.
- Etapas indisponíveis ficam desativadas com o motivo escrito (ex.: sem `Cursos/`, sem `csv`, sem token).

[⬆️ Voltar ao índice](#indice)
