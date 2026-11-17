# Pesquisa Conteudo Onda 2

Prompts de pesquisa para o **ChatGPT Work** levantar o conteúdo bruto dos cursos da Onda 2. O fluxo é o mesmo da `Pesquisa Conteudo Onda 1/README.md`. Cada prompt (versão 6) cobre o assunto inteiro: ementa completa, Essentials e Hands On.

A Onda 2 é feita **trilha por trilha**. Primeiro entram os cursos que faltam para fechar uma trilha (fonte: `trilhas.json` e a aba "Trilhas × Cursos" da checklist).

| # | Prompt | Curso (par) | Trilha que fecha | Situação |
|---|---|---|---|---|
| 1 | [01-checagem-de-fontes-e-citacoes-essentials.md](01-checagem-de-fontes-e-citacoes-essentials.md) | Checagem de Fontes e Citações | T2 — Pesquisa com IA | ✅ publicado |
| 2 | [02-revisao-bibliografica-com-ia-hands-on.md](02-revisao-bibliografica-com-ia-hands-on.md) | Revisão Bibliográfica com IA | T2 — Pesquisa com IA | ✅ publicado |
| 3 | [03-deep-research-hands-on.md](03-deep-research-hands-on.md) | Deep Research | T2 — Pesquisa com IA | ✅ publicado |
| 4 | [04-chatgpt-chat-essentials.md](04-chatgpt-chat-essentials.md) | ChatGPT Chat | T1 — Começando com assistentes de IA | ✅ publicado |
| 5 | [05-gemini-chat-essentials.md](05-gemini-chat-essentials.md) | Gemini Chat | T1 — Começando com assistentes de IA | ✅ publicado |
| 6 | [06-ia-para-analise-de-dados-essentials.md](06-ia-para-analise-de-dados-essentials.md) | IA para Análise de Dados | T8 — Planilhas e dados | ⏳ rodar a pesquisa |
| 7 | [07-dados-com-python-e-ia-hands-on.md](07-dados-com-python-e-ia-hands-on.md) | Dados com Python e IA (Onda 3, trazido para fechar a T8) | T8 — Planilhas e dados | ⏳ rodar a pesquisa |

## Por que a T8 é a próxima

- **T1 e T2 já estão completas** (a T1 fechou em 17/11 com ChatGPT Chat e Gemini Chat).
- **A T8 é a trilha da área Geral mais perto do fim:** os quatro cursos de Excel (Claude e ChatGPT, Essentials e Hands On) já existem. Faltam só IA para Análise de Dados e Dados com Python e IA, cada um com seu par da D12.
- **IA para Análise de Dados é o curso que mais trilhas destrava entre os que faltam:** entra em 8 (T8, J4, F2, R4, S4, TE3, E6 e C2). Dados com Python e IA é o último curso de T8, F2 e R4.
- **J1 e J2 continuam paradas:** cada uma depende de um único curso contextual jurídico (IA no Direito e Pesquisa jurídica com IA). A Pesquisa jurídica não pode ser feita pelo João.

Os prompts 06 e 07 usam a versão 6 sem mudanças na parte comum. O 07 acrescenta uma linha à regra de profundidade: nesse assunto, o código Python que o aluno lê e confere faz parte do curso e não vai para o apêndice técnico.

## Restante da Onda 2, por trilha (cursos ainda não feitos)

- **T3 Agentes e MCP:**
  - MCP com ChatGPT
  - Agentes Web
  - Multiagentes
  - Segurança em MCP
- **T6 Construindo com MCP:**
  - Construindo Servidores MCP
  - Multiagentes e Segurança em MCP (também estão na T3)
  - MCP com Claude (Onda 3)
- **T7 Documentos:**
  - Microsoft 365 Copilot
  - DeepL (Onda 3)
  - Gemini Workspace (Onda 1, da Marina)
- **T9 Apresentações e reuniões:**
  - IA para Reuniões
  - Canva Magic Studio
  - Gamma (Onda 3)
- **T10 Automação com N8N:**
  - Zapier
  - N8N Essentials 6 (Onda 1, da Marina)
  - N8N Hands On (Onda 3)
- **T11 Criação visual:**
  - Imagem com IA
  - Vídeo com IA
  - Canva Magic Studio
  - Midjourney, HeyGen e Voz e Áudio (Onda 3)
- **T13 Personalização:**
  - GPTs e Ferramentas do ChatGPT
  - ChatGPT Atlas, Perplexity Comet e Claude Chrome (Onda 3)
