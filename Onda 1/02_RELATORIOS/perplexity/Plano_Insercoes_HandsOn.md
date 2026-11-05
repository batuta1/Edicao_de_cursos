# Plano de inserções — Perplexity Hands-on (fase B, aguardando aprovação)

Base: `…-REVISADO.zip` (fase A). Grau: **moderado**. Supõe curso **não publicado** (inserção em qualquer ponto).
"Depois do bloco" = índice do bloco existente na lição revisada (0 = primeiro). `--licao` da skill = position (0, 1, 2).

| # | Lição | Depois do bloco | Tipo | Por que melhora a aprendizagem | Conteúdo vem de |
|---|---|---|---|---|---|
| 1 | 1 (pos 0) | 5 — accordion de preparação | **HTML** "Posso digitar isto?": 6 itens para pôr no semáforo (artigo da LGPD no Planalto, acórdão público do TJPR, rascunho seu sem dado pessoal, número agregado de atendimentos, nome e CPF de um cliente, estratégia de um processo), com correção imediata + **Continue travado** | O semáforo é o critério do curso inteiro (é o passo 1 do Projeto Final) e hoje só aparece num flashcard | Tabela do semáforo + "troque nomes por rótulos" |
| 2 | 1 | 10 — abas das cinco partes | **HTML** "Monte sua pergunta pesquisável": campos para instrução, tema, público, contexto, recorte, fontes e formato; a pergunta se forma no molde, com indicador das 5 partes + 3 exigências e botão de copiar | O passo 6 ("reescreva sozinho") é o momento de prática da oficina; o molde vira ferramenta em vez de texto | Molde da pergunta pesquisável + passos 3 e 6 |
| 3 | 1 | 18 — 🏁 ponto de controle | Título + **accordion** "Quer ir além? (opcional)" — 3 desafios com validação | Omitido pelo Articulate | Oficina 1 |
| 4 | 2 (pos 1) | 13 — múltipla resposta | Título + **accordion** "Quer ir além? (opcional)" — 3 desafios | Omitido | Oficina 2 |
| 5 | 2 | 15 — Process da Oficina 3 | **HTML** "Manter, trocar ou retirar?": 4 citações-caso (lei no Planalto com o trecho achado no Ctrl+F; blog que comenta o art. 20; página que abre mas não tem o trecho; notícia com os dados de um acórdão) — o aluno decide e recebe o porquê | A ficha termina numa decisão que o curso nunca pratica; o caso treina o critério antes da ficha real | Ficha de auditoria, 💡 primária × secundária, "Se travar" da Oficina 3 |
| 6 | 2 | 15 (logo após o #5) | Título + **accordion** "Se travar na Oficina 3" — 3 problemas | Omitido; a Oficina 2 tem o seu, a 3 não | "Se travar" da Oficina 3 |
| 7 | 2 | 18 — 🏁 do TJPR | Título + **accordion** "Quer ir além? (opcional)" — 3 desafios (processo inventado, notícia do STJ, prova no `scon.stj.jus.br`) | Omitido | Oficina 3 |
| 8 | 3 (pos 2) | 6 — Process da Oficina 4 | Título + **accordion** "Se travar na Oficina 4" — 3 problemas (inclui o caminho sem Projetos) | Omitido | "Se travar" da Oficina 4 |
| 9 | 3 | 15 — desafios da Oficina 4 | **Seção nova "Projeto Final — O dossiê citado do seu tema"**: Continue → título + missão (verbatim) → parágrafo + **lista numerada** (6 passos) → título + **abas** (4 perfis: estudante, jornalista, analista, jurídico, modelos com aspas triplas) → **HTML checklist** "Como saber que terminou" (6 itens) + **Continue travado** | A parte que junta tudo num tema do aluno sumiu do curso. O checklist trava até ele confirmar os 6 critérios de entrega | Projeto Final inteiro |

**Totais:** 9 inserções · 4 HTML (2 na Lição 1, 1 na 2, 1 na 3) · 3 Continues travados novos · só tipos já testados (texto, lista, accordion, abas, HTML, Continue). Nenhum Process novo (tipo ainda não testado em inserção — os passos do Projeto Final vão em lista numerada).
A Lição 2 recebe 4 inserções porque concentra duas oficinas.

**Estética dos HTML:** cores do tema do curso (extraídas de `course.theme`), texto real, sem nada da internet, legível no celular. Os textos dos HTML são rascunho a partir do roteiro, para revisão humana.

## Decisões pendentes

1. **Rótulos em PT-BR** (`labelSet` + `iso639Code`), reaproveitando os 174 rótulos traduzidos no MCP (o `labelSet` em inglês é idêntico)? Se sim, gero uma base v2 da fase A antes de inserir, como no MCP Hands-on.
2. **Curso publicado com alunos?** Suponho que não (está em `04_NAO_REVISADO`). Se estiver, tudo teria de ir para o fim das lições ou o curso sobe como versão nova.
3. **Dosagem:** cortar algum item? Os #3, #4 e #7 (desafios opcionais) e #6 e #8 ("Se travar") são os mais simples de tirar.
