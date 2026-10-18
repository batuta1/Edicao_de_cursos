# Relatório — Fase A (revisão de texto) — Perplexity Hands-on

Data: 18/10/2026 · Skill: `revisar-curso-scorm` · Regras: `promptRevisaoPorClaude.md` + `promptRevisaoComInsercaoDeBlocos.md`

## 1. Material

| Item | Caminho |
|---|---|
| Pacote original (não modificado) | `Onda 1/04_NAO_REVISADO/perplexity/perplexity-hands-on-scorm12-Aht9E5t2.zip` |
| Título conferido na extração | `Perplexity - Hands On` (course.id `AzkC7V42Ip_mMssoNorO3gMmT4rzeMOO`) |
| Roteiro-fonte | `Pesquisa Conteudo Onda 1/Ementa Completa/perplexity-essentials/roteiros/roteiro-articulate-hands-on.md` |
| Pasta de trabalho | `Onda 1/05_ARQUIVOS_DE_TRABALHO/perplexity/hands-on/` |
| Mapas de substituição | `…/hands-on/revisao_textos/L01.json` a `L03.json`, gerados por `gerar_mapas.py` e aplicados por `aplicar_mapas.py` (mesmo método do MCP Hands-on) |
| Pacote revisado | `Onda 1/03_VERSOES_ANTIGAS/perplexity/fase-A-so-texto/perplexity-hands-on-scorm12-Aht9E5t2-REVISADO.zip` (cópia em `…/hands-on/perplexity-hands-on-blocos/original/`) |

### Mapeamento lição ↔ oficina (o Articulate condensou 7 partes do roteiro em 3 lições)

| Lição (arquivo) | position | Partes do roteiro |
|---|---|---|
| licao_01 (20 blocos) | 0 | Antes de Arregaçar as Mangas + O Mapa (blocos 0–7) · Oficina 1 (8–19) |
| licao_02 (20 blocos) | 1 | Oficina 2 (4–13) · Oficina 3 (15–18) |
| licao_03 (19 blocos) | 2 | Oficina 4 (0–15) · A Parte dos Dez (16–17) · Conseguiu! E agora? (18) |

**O Projeto Final não existe no curso** — o Articulate omitiu a parte inteira (missão, 6 passos, 4 modelos por perfil e checklist). Vai para o plano de inserções.

## 2. Diagnóstico do que veio do Articulate

- **Erros de conteúdo (corrigidos):**
  - Abas da Lição 2 diziam que a Pesquisa Pro "permite restringir buscas a domínios específicos" e que a busca padrão "não permite trancar domínios". O roteiro diz o contrário: em qualquer nível, a restrição é escrita na pergunta, e a Perplexity não garante obedecer a operadores (🤓 curiosidade técnica).
  - Destaque da Lição 3 (bloco 12) trazia uma "síntese de exemplo" genérica sobre a LGPD, com citações acadêmicas que não estão no roteiro (DONEDA, 2019; PINHEIRO, 2020), sem link e sem fonte conferível — o oposto do que a oficina ensina, e com "decisão de compartilhamento" já tomada. Trocado pelo 🏁 ponto de controle da Oficina 4.
  - Flashcards da Lição 2 diziam "passe o mouse"; o card do Rise vira com clique.
- **Conteúdo omitido restaurado em campos existentes:** os três prompts de cada oficina, verbatim; breadcrumbs (`perplexity.ai > …`) e marcas [conferir]; o 🏁 ponto de controle de cada oficina (o da Oficina 2 estava no lugar do da Oficina 3, e o da Oficina 3 — os dados do acórdão do TJPR — não existia); o problema da Oficina 3 (Tow Center, 37%) e o link do acórdão; o link do texto compilado da LGPD; a ficha de auditoria com as seis perguntas; o mapa das oficinas com tempos; o ⚠️ "navegação anônima não é invisibilidade"; o 📌 das multas por jurisprudência inventada; o ⚠️ do PDF anexado; o molde da pergunta pesquisável com as aspas triplas; o passo 7 da Oficina 1; o semáforo (num flashcard — a versão completa vai para o plano).
- **Emojis dos destaques restaurados:** 🔑 💡 🤓 🏁 ⚠️ 📌.
- **Textos genéricos trocados pelo roteiro:** aberturas ("Já percebeu como perguntas vagas…", "Nem toda resposta da IA é igual…"), fechamentos ("Prepare-se para… dominar o uso das melhores fontes!", "Parabéns! … Pesquisa responsável é um hábito"), e os parágrafos-enchimento dos accordions.
- **Objetivos:** padronizados em "Ao final desta lição, você será capaz de:" (Lição 1 vinha em `<strong>` sem `<p>`) e alinhados às oficinas de cada lição.
- **Atividade de classificar (Lição 1):** dois cartões estavam cortados no meio da palavra ("…a quem␣␣", "…para consum") — o Articulate cortou em 80 caracteres. Reescritos completos, com no máximo 80 caracteres. Pilha "Bem Estruturada" → "Pesquisável".
- **Questões:** enunciados em forma de cenário; feedbacks no padrão "Correto." / "Não." + porquê. A questão de múltipla resposta (Lição 2) teve só o enunciado reescrito (as alternativas ficaram iguais porque `correct`/`corrects` guardam o texto delas).

## 3. Alterações (resumo por lição)

| Lição | Campos | O que mudou |
|---|---|---|
| 1 | 72 | Abertura verbatim; objetivos; accordion de preparação (mapa das oficinas, o que ter aberto, regra de ouro + cota + multas, conta e privacidade com ponto de controle e cuidado); flashcards (citação, vaga, pesquisável, acompanhamento, semáforo); Process da Oficina 1 com os 7 passos e os prompts; abas das cinco partes com exemplos do art. 20 e o molde; questão em cenário; 💡 dica; classificar sem cartões cortados; 🏁; fechamento |
| 2 | 62 | Abertura das Oficinas 2 e 3; objetivos; abas busca padrão × Pesquisa Pro corrigidas, com plano B; Process da Oficina 2 com prompt e 🏁; 🤓 curiosidade; quadro comparativo nas 5 linhas do roteiro; flashcards; enunciado da múltipla resposta; Process da Oficina 3 (Tow Center, link TJPR, ficha de seis perguntas, autoauditoria, prova do acórdão); 💡 primária × secundária; 🏁 do TJPR; fechamento |
| 3 | 85 | Abertura da Oficina 4; objetivos; accordion (resumo × síntese citada, Projetos, ficha, ⚠️ PDF); Process da Oficina 4 com os 8 passos, prompts e link da LGPD; abas fato/inferência/lacuna, limites e compartilhamento; flashcards; questão em cenário; 🏁 no lugar da síntese inventada; desafios "Quer ir além?" verbatim com validação; Parte dos Dez verbatim (frente em negrito); "Conseguiu! E agora?" verbatim |
| **Total** | **219** | por campo: description 97, feedback 8, heading 18, paragraph 41, title 55 |

Nenhum gabarito foi alterado. Nenhuma alternativa mudou de posição. Títulos das lições mantidos.

## 4. Validações

- `aplicar_mapas.py`: cada caminho é campo de texto, o valor atual ainda era o original e o texto novo é diferente. 219 aplicados.
- `validar_estrutura.py`: **estrutura preservada nas 3 lições**; 219 campos de texto alterados — igual ao número aplicado.
- `scorm_reempacotar.py`: round-trip do Base64 OK; 84 arquivos; só `scormcontent/runtime-data.js` mudou.
- Ponte `verificar_scorm.py …-REVISADO.zip --original <Articulate>`: **APROVADO**, 0 erros, 2 avisos — os mesmos do original (múltipla resposta da Lição 2 com `correct`/`corrects` em texto; aviso conhecido do Rise).
- Navegador: **não testado nesta fase** (fica para a fase B, junto com os blocos novos).

## 5. Pontos de atenção (decisão humana)

1. **Rótulos de navegação em inglês** (`labelSet`, `iso639Code` `en`). O `labelSet` é idêntico ao do MCP Hands-on, então a tradução de 174 rótulos (`mcp/hands-on/revisao_textos/rotulos_ptbr.json`) serve sem ajuste. Exige autorização (fica fora das lições).
2. **Feedback geral da múltipla resposta (Lição 2, bloco 13)** começa com "Parabéns!". Os campos `feedbackCorrect`/`feedbackIncorrect` não estão na lista de campos textuais do validador; não foram mexidos.
3. **Dados "a confirmar" mantidos do roteiro:** nomes de menus marcados [conferir] (Configurações, Retenção de Dados de IA, seletor da Pesquisa Pro, Compartilhar, Projetos no plano gratuito, mover pesquisa para o Projeto). A Perplexity muda rótulos com frequência — vale uma checagem na ferramenta antes de publicar.
4. **Ponto de controle do TJPR** cita dados do acórdão consultados em 18/10/2026 (7ª Câmara Cível, relator Fabian Schweitzer, julgado em 01/06/2026), verbatim do roteiro; não reconferidos no portal nesta revisão.
5. **Projeto Final ausente** — ver plano de inserções.

## 6. Depois da aprovação (18/10/2026)

Com autorização do usuário, o ponto 1 (rótulos) foi resolvido com os 174 rótulos do MCP Hands-on e `iso639Code` `pt-BR` (`criar_base_v2.py` → `cursoPerplexityHandsOn_base_v2.json`); só o `labelSet` mudou. Estrutura preservada (219 campos); pacote `…-REVISADO-v2.zip` APROVADO na ponte e usado como base da fase B. O original do Articulate foi movido de `04_NAO_REVISADO/perplexity/` para `03_VERSOES_ANTIGAS/perplexity/original-articulate/`. Detalhes em `Relatorio_HandsOn_Revisao_e_Insercao.md`.
