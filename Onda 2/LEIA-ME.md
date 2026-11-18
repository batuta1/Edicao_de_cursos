# Onda 2 — organização da pasta

A pasta é organizada **primeiro por etapa, depois por tema**, como a `Onda 1/`. Cada curso novo ganha uma subpasta com o nome do tema (`checagem-de-fontes/`, `revisao-bibliografica/`, …) dentro da etapa em que está; não é preciso recriar a estrutura por tema.

| Pasta | O que tem | Situação |
|---|---|---|
| `01_FINALIZADO_subir-na-LMS/<tema>/` | Os `.zip` finais (textos revisados + blocos novos). Pastas `extraido-…` são só para conferência | ✅ Terminado: são estes `.zip` que vão para a LMS |
| `02_RELATORIOS/<tema>/` | Para cada curso, o relatório completo (`…_Revisao_e_Insercao.md`) e o detalhe da revisão de texto (`…_Fase_A_Revisao_de_Texto.md`) | 📄 Relatórios |
| `03_VERSOES_ANTIGAS/<tema>/` | `original-articulate/` (exportações originais), `fase-A-so-texto/`, versões intermediárias | 🗄️ Não usar. Guardadas como histórico |
| `04_NAO_REVISADO/<tema>/` | `.zip` recém-chegados do Articulate, aguardando revisão | ⏳ Fila de revisão |
| `05_ARQUIVOS_DE_TRABALHO/<tema>/` | Por curso (`essentials/`, `hands-on/`): JSONs extraídos, lições separadas, Base64, HTMLs dos blocos, pacotes de teste | 🔧 Material de trabalho. Necessário só para refazer ou ajustar os cursos |

Antes desta pasta, cada curso passa por `Pesquisa Conteudo Onda 2/`: conteúdo bruto em `conteudo-bruto/<id>/` e ementa + roteiros em `Ementa Completa/<id>/`. Os roteiros `roteiro-articulate-*.md` de lá são o que vai para o Articulate; o `.zip` exportado entra aqui em `04_NAO_REVISADO/<tema>/`.

## Situação atual

| Tema | Etapa |
|---|---|
| `checagem-de-fontes` (Essentials e Hands-on) | ✅ Finalizado — `01_FINALIZADO_subir-na-LMS/checagem-de-fontes/` (v1; marcadores [conferir] e um gabarito discutível no Hands-on — veja os pontos de atenção dos relatórios) |
| `revisao-bibliografica` (Essentials e Hands-on) | ✅ Finalizado — `01_FINALIZADO_subir-na-LMS/revisao-bibliografica/` (v2, 11/11/2026; sem pendências: [conferir] resolvidos por pesquisa e questões do Quiz corrigidas — v1 em `03_VERSOES_ANTIGAS/revisao-bibliografica/v1-final/`). Os `.zip` do Articulate ainda estão em `04_NAO_REVISADO/revisao bibliografica com ia/` (cópia em `03_VERSOES_ANTIGAS/revisao-bibliografica/original-articulate/`) |
| `deep-research` (Essentials e Hands-on) | ✅ Finalizado — `01_FINALIZADO_subir-na-LMS/deep-research/` (v1; marcadores [conferir] e gabaritos "reconfira no dia" — veja os pontos de atenção dos relatórios). Os `.zip` do Articulate ainda estão em `04_NAO_REVISADO/deepsearch com IA/` (cópia em `03_VERSOES_ANTIGAS/deep-research/original-articulate/`) |
| `gemini-chat` (Essentials e Hands-on) | ✅ Finalizado — `01_FINALIZADO_subir-na-LMS/gemini-chat/` (v1, 17/11/2026; [conferir] resolvidos, gabarito errado do Hands-on corrigido, preparação com CSV e e-mail de teste recuperada). Os `.zip` do Articulate ainda estão em `04_NAO_REVISADO/gemini-chat/` (cópia em `03_VERSOES_ANTIGAS/gemini-chat/original-articulate/`) |
| `chatgpt-chat` (Essentials e Hands-on) | ✅ Finalizado — `01_FINALIZADO_subir-na-LMS/chatgpt-chat/` (v1, 17/11/2026; [conferir] resolvidos, respostas inventadas pelo Articulate trocadas pelos prompts do roteiro, arquivos do caso Loja Aurora recuperados no Hands-on). Os `.zip` do Articulate ainda estão em `04_NAO_REVISADO/chatgpt-chat/` (cópia em `03_VERSOES_ANTIGAS/chatgpt-chat/original-articulate/`) |
| `ia-para-analise-de-dados` (Essentials e Hands-on) | ✅ Finalizado — `01_FINALIZADO_subir-na-LMS/ia-para-analise-de-dados/` (v1, 17/11/2026; prompts no lugar de respostas inventadas, "sete etapas" corrigidas, Hands-on traduzido do inglês e com desafios e checklists recuperados, gabarito quebrado do Hands-on corrigido). Os `.zip` do Articulate ainda estão em `04_NAO_REVISADO/ia para analise de dados/` (cópia em `03_VERSOES_ANTIGAS/ia-para-analise-de-dados/original-articulate/`) |
| `analise-de-dados-em-python-com-ia` (Essentials e Hands-on) | ✅ Finalizado — `01_FINALIZADO_subir-na-LMS/analise-de-dados-em-python-com-ia/` (v1, 17/11/2026; README inventado com pip/requirements trocado pelo prompt do roteiro, endereços das bases restaurados no Hands-on, critério do INMET corrigido). Os `.zip` do Articulate ainda estão em `04_NAO_REVISADO/analise de dados em pyhton com ia/` (cópia em `03_VERSOES_ANTIGAS/analise-de-dados-em-python-com-ia/original-articulate/`) |

Quando um curso muda de etapa, mova só a subpasta do tema. Antes de publicar, veja a seção "Pontos de atenção" de cada relatório completo.

Os arquivos `.gitkeep` só existem para o Git guardar as pastas vazias; podem ser apagados quando a pasta receber o primeiro curso.
