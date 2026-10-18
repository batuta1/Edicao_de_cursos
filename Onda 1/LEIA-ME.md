# Onda 1 — organização da pasta

A pasta é organizada **primeiro por etapa, depois por tema**. Cada curso novo ganha uma subpasta com o nome do tema (`notebooklm/`, `mcp/`, …) dentro da etapa em que está; não é preciso recriar a estrutura por tema.

| Pasta | O que tem | Situação |
|---|---|---|
| `01_FINALIZADO_subir-na-LMS/<tema>/` | Os `.zip` finais (textos revisados + blocos novos). Pastas `extraido-…` são só para conferência | ✅ Terminado: são estes `.zip` que vão para a LMS |
| `02_RELATORIOS/<tema>/` | Para cada curso, o relatório completo (`…_Revisao_e_Insercao.md`) e o detalhe da revisão de texto (`…_Fase_A_Revisao_de_Texto.md`) | 📄 Relatórios |
| `03_VERSOES_ANTIGAS/<tema>/` | `original-articulate/` (exportações originais), `fase-A-so-texto/`, versões intermediárias | 🗄️ Não usar. Guardadas como histórico |
| `04_NAO_REVISADO/<tema>/` | `.zip` recém-chegados do Articulate, aguardando revisão | ⏳ Fila de revisão |
| `05_ARQUIVOS_DE_TRABALHO/<tema>/` | Por curso (`essentials/`, `hands-on/`): JSONs extraídos, lições separadas, Base64, HTMLs dos blocos, pacotes de teste | 🔧 Material de trabalho. Necessário só para refazer ou ajustar os cursos |

## Situação atual

| Tema | Etapa |
|---|---|
| `notebooklm` (Essentials e Hands-on) | ✅ Finalizado — `01_FINALIZADO_subir-na-LMS/notebooklm/` |
| `mcp` (Essentials) | ✅ Finalizado — `01_FINALIZADO_subir-na-LMS/mcp/` (v3; veja os pontos de atenção no relatório) |
| `mcp` (Hands-on) | ✅ Finalizado — `01_FINALIZADO_subir-na-LMS/mcp/` (v2; veja os pontos de atenção no relatório) |

Quando um curso muda de etapa, mova só a subpasta do tema. Antes de publicar, veja a seção "Pontos de atenção" de cada relatório completo.
