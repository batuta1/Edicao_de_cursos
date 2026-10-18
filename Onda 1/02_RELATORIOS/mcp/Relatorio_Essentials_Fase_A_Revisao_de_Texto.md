# Relatório — Fase A (revisão de texto) — MCP Essentials

Data: 18/10/2026 · Skill: `revisar-curso-scorm` · Regras: `promptRevisaoPorClaude.md` + `promptRevisaoComInsercaoDeBlocos.md`

## 1. Material

| Item | Caminho |
|---|---|
| Pacote original (não modificado) | `Onda 1/03_VERSOES_ANTIGAS/mcp/original-articulate/model-context-protocol-mcp-essentials-scorm12-MYCD1EGZ.zip` (chegou em `04_NAO_REVISADO/mcp/`) |
| Título conferido na extração | `Model Context Protocol (MCP) - Essentials` (course.id `A6GxuiVLrHaIYJQ0N2rtL7ZCDLnK5DG_`) |
| Roteiro-fonte | `Pesquisa Conteudo Onda 1/Ementa Completa/mcp-essentials/roteiros/roteiro-articulate-essentials.md` |
| Pasta de trabalho | `Onda 1/05_ARQUIVOS_DE_TRABALHO/mcp/essentials/` |
| Mapas de substituição (o que foi escrito, por caminho do campo) | `…/essentials/revisao_textos/L01.json` a `L08.json` |
| Pacote revisado | `Onda 1/03_VERSOES_ANTIGAS/mcp/fase-A-so-texto/model-context-protocol-mcp-essentials-scorm12-MYCD1EGZ-REVISADO.zip` |

### Mapeamento lição ↔ módulo (1:1)

| Lição (arquivo) | position | Módulo do roteiro |
|---|---|---|
| licao_01 | 0 | Módulo 0 — Preparação e Verificação Inicial |
| licao_02 | 1 | Módulo 1 — O que é o MCP |
| licao_03 | 2 | Módulo 2 — Segurança, Permissões e Uso Responsável |
| licao_04 | 3 | Módulo 3 — Primeira conexão: consultar um serviço |
| licao_05 | 4 | Módulo 4 — Ler arquivos: pasta local e nuvem |
| licao_06 | 5 | Módulo 5 — Executar ações com aprovação e desfazer |
| licao_07 | 6 | Módulo 6 — Síntese e Aplicação Integrada (+ Encerramento) |
| licao_08 | 7 | Quiz (22 questões geradas pelo Articulate) |

## 2. Diagnóstico do que veio do Articulate

- **Idioma:** o curso saiu quase todo **em inglês** (títulos de lições, accordions, abas, flashcards, questões,
  quiz). Só os blocos que o roteiro mandava copiar verbatim vieram em português. A revisão foi, na prática,
  tradução + reescrita fiel ao roteiro em PT-BR. Rótulos de interface ficaram em inglês, como o roteiro
  determina (`Always allow`, `Needs approval`, `Blocked`, `Allow`, `Deny`, `Add custom connector`, `Settings`…).
- **Textos genéricos:** aberturas do tipo "Welcome to the hands-on turning point of your MCP journey!" e
  fechamento motivacional ("Congratulations on completing the course!") — trocados pelo conteúdo do roteiro.
- **Conteúdo perdido ou trocado pelo Articulate (corrigido no texto existente):**
  - Lição 2: o bloco "Mão na massa" trazia só "Não há conectores ativos nesta conversa." — a *resposta
    esperada*, não o prompt-base. Restaurado o prompt-base completo.
  - Lição 1: o requisito técnico perdeu o emoji 📌 que o roteiro manda preservar.
  - Todas as lições: os 🏁 Pontos de controle e critérios de êxito não apareciam nos Process; foram para o item
    de resumo de cada Process (que estava com texto genérico).
  - Objetivos: listas com títulos curtos em inglês, desalinhados do plano. Agora seguem o roteiro, na ordem;
    quando a lista do Articulate tinha mais itens que o roteiro, o item extra recebeu um objetivo real da lição.
  - Lição 7: a tabela "síntese da decisão" foi condensada numa aba; o Encerramento do roteiro (2 parágrafos)
    substituiu o fechamento motivacional.
- **Estrutura:** só 1 Continue em todo o curso (o NotebookLM Essentials tinha 7) — as lições são corridas,
  sem seções. Não dá para corrigir na fase A; vai para o plano de inserções.

## 3. Alterações (resumo por lição)

| Lição | Campos | O que mudou |
|---|---|---|
| 1 | 52 | Título; abertura com a justificativa documental (todos os planos, 1 conector no Free); objetivos; accordion com requisitos completos (macOS 13 [conferir], x64/arm64, Microsoft 365 fora); Process com passos do roteiro e ponto de controle; flashcards e questão em PT; registro de verificação com rótulo "Mão na massa" |
| 2 | 64 | N × M, histórico (25/11/2024, AAIF 09/12/2025), "não é app nem modelo", tomada e crachá, tabela de conceitos em abas, host/client/servidor e tools/resources/prompts, local × remoto, três verbos; prompt-base restaurado |
| 3 | 61 | Crachá e consentimento (especificação), os 5 riscos com controle, caminho de Tool permissions, as 3 opções (incl. Microsoft 365 nunca aceita Always allow), ficha do conector e sinais de alerta, semáforo e LGPD/ANPD/Governo Digital, prompt de proteção |
| 4 | 83 | OpenAI Docs MCP e erro 405, caminhos no Claude e no ChatGPT ("modo de desenvolvedor" obsoleto), Process com o pedido verbatim, bloco de chamada de ferramenta e URL, tabela de problemas em accordion, critério de êxito (a)–(d) |
| 5 | 76 | Filesystem e Google Drive (ferramentas de leitura e escrita), uma pasta só, "Quais diretórios…", Deny, arquivos fictícios com quebras de linha, prompt-base, problemas, critério de êxito |
| 6 | 92 | Método preparar–revisar–conferir–desfazer, Google Calendar, convite sem volta, Gmail só rascunho, desconectar/revogar, Process verbatim, problemas, flashcards, questão, critério de êxito |
| 7 | 74 | Quatro perguntas, semáforo × permissões, síntese da decisão, plano de conexão, devolução dos acessos, critérios de avaliação, Encerramento do roteiro |
| 8 (Quiz) | 157 | Descrição, 22 enunciados, alternativas e feedbacks em PT; True/False → Verdadeiro/Falso; respostas aceitas das lacunas traduzidas (ver ponto de atenção 3) |
| **Total** | **659** | por campo: description 191, feedback 90, heading 35, paragraph 100, title 243 |

Nenhum gabarito foi alterado. Feedbacks seguem "Correto." / "Não." + porquê (no quiz, "Correto." / "Incorreto.").

## 4. Validações

- `validar_estrutura.py`: **estrutura preservada em todas as lições**; 659 campos de texto alterados, igual ao
  número de edições aplicadas pelo script de substituição (677 planejadas − 18 pendentes, ver abaixo).
- Primeira rodada **reprovada** (18 divergências): `matchTitle` e `feedbackCorrect`/`feedbackIncorrect` do quiz
  não constam da lista de campos textuais do validador. A lição 8 foi restaurada do original e reaplicada sem
  esses campos — mesmo procedimento usado no NotebookLM Hands-on.
- `scorm_reempacotar.py`: round-trip do Base64 OK; só `scormcontent/runtime-data.js` mudou.
- Ponte `verificar_scorm.py REVISADO.zip --original …`: **APROVADO**, 0 erros, 0 avisos.
- Navegador: conferido junto com a fase B (ver `Relatorio_Essentials_Revisao_e_Insercao.md`).

## 5. Pontos de atenção (decisão humana)

1. **Gabarito suspeito — Lição 7, questão da agenda pessoal.** A correta marcada é "Verde; acesso somente
   leitura à agenda". O roteiro classifica "Consultar a própria agenda" como **Amarelo** (conta pessoal; tabela
   da síntese) e reserva Verde para fonte pública ou dados fictícios. Não foi alterado. Proposta: tornar
   correta uma alternativa "Amarelo; leitura liberada e escrita em Needs approval" (exige mudar alternativa e
   gabarito — no Rise, ou com autorização para editar o campo `correct`).
2. **18 campos do quiz continuam em inglês** (associações e feedbacks das questões de associação e lacuna:
   itens 2, 4, 18, 20 e 21). A tradução está pronta em `revisao_textos/L08_pendente_autorizacao.json`;
   aplicar exige autorizar esses três campos no validador.
3. **Descrição do curso (capa) em inglês.** Fica em `course.description`, fora das lições, e o fluxo da skill
   não a cobre. Texto proposto: "Conectar assistentes de IA a ferramentas e dados, com segurança. Entenda o que
   o Model Context Protocol (MCP) padroniza e o que ele não garante, ligue um conector remoto público, autorize
   a leitura de uma pasta de arquivos fictícios, consulte e altere a própria agenda de forma reversível e monte
   um plano de conexão segura para um caso do seu trabalho."
4. **Lacunas do quiz:** as respostas aceitas agora são "preparar–revisar–conferir–desfazer" (com travessão e
   com hífen), "Windows 10+" e "login" (a frase foi reescrita para "pela tela de ____ do próprio serviço", para
   que a resposta seja uma palavra só). Conferir no navegador se a comparação ignora maiúsculas.
5. **Critérios de êxito sem questões suficientes:** a Lição 2 diz "duas respostas corretas" e a Lição 3
   "quatro classificações corretas", mas o Articulate gerou só a 1ª questão de cada. As faltantes estão no
   plano de inserções; se não forem inseridas, os critérios precisam mudar.
6. **[conferir] do roteiro mantidos:** macOS 13, `Add custom connector`, rótulos em português de Settings >
   Extensions, rótulo para desativar a Filesystem, caminho de revogação na Conta Google.
7. **Rótulos de navegação do Rise em inglês** (`labelSet` "en": "Continue", "Start course", "Lesson x of y"):
   igual ao NotebookLM; não é campo de lição.

## Atualização — v2 (18/10/2026)

Os pontos 2 (18 campos do quiz) e 3 (descrição da capa) foram resolvidos com autorização do usuário: 677 campos alterados no total, validados com `validar_estrutura_autorizado.py` (que acrescenta só `matchTitle`, `feedbackCorrect` e `feedbackIncorrect` à lista de texto), e pacote `…-REVISADO-v2.zip` APROVADO na ponte. Detalhes em `Relatorio_Essentials_Revisao_e_Insercao.md`.

## Atualização — v3 (18/10/2026)

Ponto 1 (gabarito da Lição 7) corrigido com autorização; lacunas 19 e 21 simplificadas; ponto 7 (rótulos) resolvido com o `labelSet` em PT-BR e `iso639Code` `pt-BR`. 680 campos, validados com `validar_estrutura_autorizado_v3.py`; pacote `…-REVISADO-v3.zip` APROVADO na ponte. Detalhes em `Relatorio_Essentials_Revisao_e_Insercao.md`.
