# Onde estão os SCORMs

**Desde 18 nov 2026, os SCORMs, roteiros e ementas de todos os cursos ficam na pasta `bagunca/` da branch `main`** (commit `58d586d`). Saíram desta branch (`joao`) para não ficarem em dois lugares.

Em `bagunca/` há uma pasta por tema, cada uma com `scorm/`, `roteiros/` e `ementa/`. O `bagunca/README.md` diz de onde veio cada coisa e o que falta.

Para ver a pasta: abra a `main` no GitHub ou rode `git checkout main`. Para trazer um tema só para esta branch, sem trocar de branch:

```
git checkout origin/main -- "bagunca/<tema>"
```

## Onde cada tema estava antes

Só saíram os arquivos com cópia idêntica na `bagunca` (comparados pelo conteúdo). Versões antigas (`old/`, `03_VERSOES_ANTIGAS/`), relatórios, arquivos de trabalho, conteúdo bruto e as pastas `_processo` das ementas continuam aqui.

| Tema em `bagunca/` | Pastas de onde saíram os pacotes |
|---|---|
| `agentes-de-ia` | `Onda 1/01_FINALIZADO_subir-na-LMS/agentes-de-ia/` · `Onda 1/05_ARQUIVOS_DE_TRABALHO/agentes-de-ia/essentials/agentes-essentials-blocos/saidas/` · `Onda 1/05_ARQUIVOS_DE_TRABALHO/agentes-de-ia/hands-on/agentes-hands-on-blocos/saidas/` |
| `analise-de-dados-em-python-com-ia` | `Onda 2/01_FINALIZADO_subir-na-LMS/analise-de-dados-em-python-com-ia/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/analise-de-dados-em-python-com-ia/essentials/pythonia-essentials-blocos/saidas/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/analise-de-dados-em-python-com-ia/hands-on/pythonia-hands-on-blocos/saidas/` |
| `chatgpt-chat` | `Onda 2/01_FINALIZADO_subir-na-LMS/chatgpt-chat/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/chatgpt-chat/essentials/chatgpt-essentials-blocos/saidas/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/chatgpt-chat/hands-on/chatgpt-hands-on-blocos/saidas/` |
| `chatgpt-codex` | `Onda 3/01_FINALIZADO_subir-na-LMS/chatgpt-codex/` · `OpenAI/OPENAI (ChatGPT)/ChatGPT CODEX/essentials/` |
| `chatgpt-excel` | `OpenAI/OPENAI (ChatGPT)/ChatGPT Excel/essentials/` · `OpenAI/OPENAI (ChatGPT)/ChatGPT Excel/hands-on/` |
| `chatgpt-powerpoint` | `OpenAI/OPENAI (ChatGPT)/ChatGPT PowerPoint/essentials/` · `OpenAI/OPENAI (ChatGPT)/ChatGPT PowerPoint/hands-on/` |
| `chatgpt-word` | `Onda 3/01_FINALIZADO_subir-na-LMS/chatgpt-word/` · `OpenAI/OPENAI (ChatGPT)/ChatGPT Word/essentials/` |
| `checagem-de-fontes` | `Onda 2/01_FINALIZADO_subir-na-LMS/checagem-de-fontes/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/checagem-de-fontes/essentials/checagem-essentials-blocos/saidas/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/checagem-de-fontes/hands-on/checagem-hands-on-blocos/saidas/` |
| `claude-chat` | `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE CHAT/essentials/` · `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE CHAT/hands-on/` · `Cursos Revisados/Claude/` |
| `claude-code-no-vscode` | `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE VSCODE/essentials/` · `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE VSCODE/hands-on/` · `Cursos Revisados/Claude/` |
| `claude-cowork` | `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE COWORK/essentials/` · `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE COWORK/hands-on/` · `Cursos Revisados/Claude/` |
| `claude-design` | `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE DESIGN/Essentials/` · `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE DESIGN/Hands-On/` · `Cursos Revisados/Claude/` |
| `claude-desktop` | `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE DESKTOP/essentials/` · `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE DESKTOP/hands-on/` · `Cursos Revisados/Claude/` |
| `claude-desktop-para-engenharia` | `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE DESKTOP/old/` |
| `claude-excel` | `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE EXCEL/essentials/` · `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE EXCEL/hands-on/` · `Cursos Revisados/Claude/` |
| `claude-for-legal` | `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE FOR LEGAL/Essentials/` · `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE FOR LEGAL/Hands-On/` |
| `claude-power-point` | `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE POWER POINT/essentials/` · `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE POWER POINT/hands-on/` · `Cursos Revisados/Claude/` |
| `claude-skills` | `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE SKILLs/essentials/` · `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE SKILLs/hands-on/` · `Cursos Revisados/Claude/` |
| `claude-word` | `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE WORD/essentials/` · `Anthropic/ANTHROPIC (CLAUDE)/CLAUDE WORD/hands-on/` · `Cursos Revisados/Claude/` |
| `deep-research` | `Onda 2/01_FINALIZADO_subir-na-LMS/deep-research/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/deep-research/essentials/deep-essentials-blocos/saidas/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/deep-research/hands-on/deep-hands-on-blocos/saidas/` |
| `gemini-chat` | `Onda 2/01_FINALIZADO_subir-na-LMS/gemini-chat/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/gemini-chat/essentials/gemini-essentials-blocos/saidas/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/gemini-chat/hands-on/gemini-hands-on-blocos/saidas/` |
| `ia-para-analise-de-dados` | `Onda 2/01_FINALIZADO_subir-na-LMS/ia-para-analise-de-dados/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/ia-para-analise-de-dados/essentials/iadados-essentials-blocos/saidas/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/ia-para-analise-de-dados/hands-on/iadados-hands-on-blocos/saidas/` |
| `mcp` | `Onda 1/01_FINALIZADO_subir-na-LMS/mcp/` · `Onda 1/05_ARQUIVOS_DE_TRABALHO/mcp/essentials/mcp-essentials-blocos/saidas/` · `Onda 1/05_ARQUIVOS_DE_TRABALHO/mcp/hands-on/mcp-hands-on-blocos/saidas/` |
| `notebooklm` | `Onda 1/01_FINALIZADO_subir-na-LMS/notebooklm/` · `Onda 1/05_ARQUIVOS_DE_TRABALHO/notebooklm/essentials/notebooklm-essentials-blocos/saidas/` · `Onda 1/05_ARQUIVOS_DE_TRABALHO/notebooklm/hands-on/blocos/saidas/` |
| `perplexity` | `Onda 1/01_FINALIZADO_subir-na-LMS/perplexity/` · `Onda 1/05_ARQUIVOS_DE_TRABALHO/perplexity/essentials/perplexity-essentials-blocos/saidas/` · `Onda 1/05_ARQUIVOS_DE_TRABALHO/perplexity/hands-on/perplexity-hands-on-blocos/saidas/` |
| `revisao-bibliografica` | `Onda 2/01_FINALIZADO_subir-na-LMS/revisao-bibliografica/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/revisao-bibliografica/essentials/revbib-essentials-blocos/saidas/` · `Onda 2/05_ARQUIVOS_DE_TRABALHO/revisao-bibliografica/hands-on/revbib-hands-on-blocos/saidas/` |
| `vibe-coding` | `Onda 1/01_FINALIZADO_subir-na-LMS/vibecoding/` · `Onda 1/05_ARQUIVOS_DE_TRABALHO/vibecoding/essentials/vibe-essentials-blocos/saidas/` · `Onda 1/05_ARQUIVOS_DE_TRABALHO/vibecoding/hands-on/vibe-hands-on-blocos/saidas/` |

Também saíram os roteiros, planos de aula e ementas desses cursos: `Pesquisa Conteudo Onda 1/Ementa Completa/` e `Pesquisa Conteudo Onda 2/Ementa Completa/` (menos `_processo/`), `Criacao de Cursos/Claude/` e `Criacao de Cursos/GPT/`, e as pastas `ementa completa/` de `OpenAI/OPENAI (ChatGPT)/`.

**Regra para curso novo:** o pacote final vai para `bagunca/<tema>/scorm/` na `main`, com os roteiros em `roteiros/` e a ementa em `ementa/`.
