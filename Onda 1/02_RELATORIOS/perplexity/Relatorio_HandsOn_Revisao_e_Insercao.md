# Relatório — Revisão e Inserção — Perplexity Hands-on

Data: 18/10/2026 · Skills: `revisar-curso-scorm` (fase A) e `inserir-blocos-scorm` (fase B) · Regras: `promptRevisaoComInsercaoDeBlocos.md` + `promptRevisaoPorClaude.md`
Grau de liberdade: **moderado** · Curso **não publicado** (confirmado pelo usuário) · Plano aprovado sem cortes, com rótulos em PT-BR.

**`.zip` para subir na LMS:** `Onda 1/01_FINALIZADO_subir-na-LMS/perplexity/perplexity-hands-on-scorm12-Aht9E5t2-FINAL-com-blocos-v1.zip`

## 1. Material-fonte e mapeamento

- Roteiro: `Pesquisa Conteudo Onda 1/Ementa Completa/perplexity-essentials/roteiros/roteiro-articulate-hands-on.md`
- Original do Articulate (não modificado): `Onda 1/03_VERSOES_ANTIGAS/perplexity/original-articulate/perplexity-hands-on-scorm12-Aht9E5t2.zip` (estava em `04_NAO_REVISADO/perplexity/`)
- Título: `Perplexity - Hands On` · course.id `AzkC7V42Ip_mMssoNorO3gMmT4rzeMOO`

| Lição | position | Partes do roteiro (depois da fase B) |
|---|---|---|
| 1 — Da Dúvida Vaga à Pergunta Pesquisável | 0 | Antes de Arregaçar as Mangas + Mapa · Oficina 1 |
| 2 — Comparando e Validando Níveis de Busca e Fontes | 1 | Oficina 2 · Oficina 3 |
| 3 — Construindo e Documentando Sínteses Fundamentadas | 2 | Oficina 4 · **Projeto Final (novo)** · A Parte dos Dez · Conseguiu! E agora? |

## 2. Revisão de texto (fase A)

Detalhe completo em `Relatorio_HandsOn_Fase_A_Revisao_de_Texto.md`. Resumo:

- 219 campos de texto em 3 lições (L1: 72, L2: 62, L3: 85), aplicados por mapas (`05_ARQUIVOS_DE_TRABALHO/perplexity/hands-on/revisao_textos/`).
- Corrigidos dois erros de conteúdo: as abas que diziam que só a Pesquisa Pro "restringe domínios" e uma "síntese de exemplo" inventada (com citações DONEDA/PINHEIRO que não estão no roteiro).
- Restaurados verbatim: prompts, breadcrumbs, pontos de controle (o da Oficina 3 não existia), Tow Center 37%, links do TJPR e da LGPD, ficha de auditoria, molde da pergunta, avisos ⚠️ e 📌, Parte dos Dez e fechamento.
- **Rótulos de navegação em PT-BR** (autorizado): 174 rótulos do MCP Hands-on, `iso639Code` `pt-BR` (`criar_base_v2.py` → `cursoPerplexityHandsOn_base_v2.json`). Confere que só o `labelSet` mudou. Pacote `…-REVISADO-v2.zip`.
- `validar_estrutura.py`: estrutura preservada, 219 campos — igual ao aplicado. Nenhum gabarito alterado.

## 3. Inserções (fase B)

Base: `…-REVISADO-v2.zip`. 8 roteiros (`trabalho/roteiros/r01…r08`), gerados por `trabalho/gerar_roteiros.py`, aplicados em cadeia (`trabalho/etapas/`). **22 blocos novos.** O índice abaixo é a posição final na lição (0 = primeiro).

| # | Lição | Posição final | Tipo | Justificativa didática |
|---|---|---|---|---|
| 1 | 1 | 6–7 | HTML "Posso digitar isto?" (semáforo, 6 itens) + Continue travado | O semáforo é o critério do curso (passo 1 do Projeto Final) e só aparecia num flashcard |
| 2 | 1 | 13 | HTML "Monte sua pergunta pesquisável" | Transforma o molde em ferramenta para o passo 6 ("reescreva sozinho") |
| 3 | 1 | 22–23 | Título + accordion "Quer ir além? (opcional)" | Desafios da Oficina 1 omitidos pelo Articulate |
| 4 | 2 | 14–15 | Título + accordion "Quer ir além? (opcional)" | Desafios da Oficina 2 omitidos |
| 5 | 2 | 18 | HTML "Manter, trocar ou retirar?" (4 citações) | A ficha termina numa decisão que o curso não praticava |
| 6 | 2 | 19–20 | Título + accordion "Se travar na Oficina 3" | Omitido; a Oficina 2 tinha o seu |
| 7 | 2 | 24–25 | Título + accordion "Quer ir além? (opcional)" | Desafios da Oficina 3 omitidos |
| 8 | 3 | 7–8 | Título + accordion "Se travar na Oficina 4" | Omitido |
| 9 | 3 | 18–25 | Seção **Projeto Final**: Continue → título + missão → parágrafo + lista numerada (6 passos) → título + abas (4 perfis) → HTML checklist "Como saber que terminou" → Continue travado | A parte que junta tudo num tema do aluno não existia no curso |

**Em relação ao plano aprovado:** nada mudou de lugar ou de tipo. Detalhes de execução: o HTML #5 ficou **sem** trava (a atividade de classificar logo abaixo já pede interação); o checklist do Projeto Final usa largura "pequena", como a faxina do MCP.

**HTMLs** (embutidos via `srcdoc`, nenhuma pasta anexada): `trabalho/html/l1-semaforo.html`, `l1-pergunta.html`, `l2-decida.html`, `l3-dossie.html`, montados por `html/build.py` a partir de `html/src/` com o CSS comum do MCP (mesmas cores do tema, `#152f4d`). Autocontidos, sem referência externa.

Totais por lição: L1 20 → 25 blocos · L2 20 → 27 · L3 19 → 29.

## 4. Validações

| Etapa | Resultado |
|---|---|
| `verificar_scorm.py` no original do Articulate | APROVADO, 0 erros, 2 avisos |
| Fase A `validar_estrutura.py` (v1 e base v2) | Estrutura preservada; 219 campos |
| Ponte `verificar_scorm.py …-REVISADO-v2.zip --original <Articulate>` | APROVADO, 0 erros, 2 avisos; só `runtime-data.js` mudou |
| Fase B `validar.py curso_v1.json` | APROVADO — só inserção; 22 blocos novos seguem os modelos; 374 IDs únicos |
| `verificar_scorm.py …-FINAL-com-blocos-v1.zip --original …-REVISADO-v2.zip` | APROVADO, 0 erros, 2 avisos |

Os 2 avisos são sempre os mesmos e já vinham do Articulate: a questão de múltipla resposta da Lição 2 grava `correct`/`corrects` como texto (comportamento conhecido do Rise; a correção usa `answers[].correct`).

## 5. Navegador (mock de LMS, `teste/v1`)

Visto e funcionando:
- Rótulos em PT-BR na interface ("Continuado", "Clique para virar", "Lição 3 de 3").
- **Lição 1:** todos os 25 blocos na ordem planejada. Semáforo: resposta errada mostra o aviso; com as 6 certas, a mensagem final aparece e o Continue (antes com cadeado) libera. "Monte sua pergunta": o molde se forma, as 8 etiquetas acendem, o exemplo do art. 20 preenche tudo.
- **Lição 2:** 27 blocos na ordem. "Manter, trocar ou retirar?": erro com feedback, 4 de 4 com mensagem final. Accordion dos desafios da Oficina 3 abre. Texto revisado do Process da Oficina 3 (Tow Center, link do TJPR) conferido na tela.
- **Lição 3:** 29 blocos na ordem. Projeto Final com missão, lista de 6 passos, abas dos 4 perfis (aba Jurídico conferida, aspas triplas visíveis), checklist que, marcado por cliques reais, libera o Continue; depois dele, Parte dos Dez e fechamento.
- Console sem erros.
- Retomada: recarregando sem `reset`, o curso voltou à Lição 3 com todos os blocos liberados.

**Não verificado:**
- Botão "Copiar pergunta": no mock, a cópia automática foi bloqueada pelo iframe e entrou o plano B (texto selecionado + aviso "use Ctrl+C"). Não sei se a LMS real permite a cópia direta; o plano B funciona de qualquer jeito.
- Visual no celular (testei só em 800 px de largura) e em LMS real.
- Questões nativas (corrigir/enviar), flashcards e sorting não foram respondidos um a um; foram vistos carregando.
- Lições 1 e 3 não chegaram a "concluída" no mock (não respondi as questões de todas); não testei o status final `completed` do curso.

## 6. Pontos de atenção para revisão humana

1. **Textos dos HTML são rascunho** a partir do roteiro: os 6 itens do semáforo, os 4 casos de citação, o exemplo do art. 20 na ferramenta (o contexto "entender que direito eu tenho" e o recorte "Brasil, lei em vigor" são meus).
2. **Aviso do Continue travado em inglês** ("Complete the content above before moving on."): o `completeHint` do modelo é o padrão em inglês e o validador exige o item idêntico — não traduzível sem mudar o modelo. Vale como pendência da skill.
3. **Nomes de menus marcados [conferir]** (vêm do roteiro): Configurações, Retenção de Dados de IA, seletor da Pesquisa Pro, Acadêmico, Compartilhar, Projetos no gratuito, mover pesquisa para o Projeto.
4. **Dados do acórdão do TJPR e da notícia do STJ** (verbatim do roteiro, consultados em 18/10/2026 pela ementa) não foram reconferidos nos portais nesta revisão.
5. **Múltipla resposta da Lição 2:** feedback geral começa com "Parabéns!" (campos `feedbackCorrect`/`feedbackIncorrect` fora da lista de campos de texto; não alterados). Alternativas mantidas como "Pergunta 1: A) …" porque `correct`/`corrects` guardam esse texto.
6. A Lição 2 passou a ter 4 inserções (concentra duas oficinas).

## 7. Arquivos

| O quê | Onde |
|---|---|
| **Pacote final** | `01_FINALIZADO_subir-na-LMS/perplexity/perplexity-hands-on-scorm12-Aht9E5t2-FINAL-com-blocos-v1.zip` |
| Pacotes da fase A | `03_VERSOES_ANTIGAS/perplexity/fase-A-so-texto/` (`-REVISADO.zip` sem rótulos; `-REVISADO-v2.zip` com rótulos) |
| Trabalho da fase A | `05_ARQUIVOS_DE_TRABALHO/perplexity/hands-on/` (mapas, lições, scripts) |
| Trabalho da fase B | `05_ARQUIVOS_DE_TRABALHO/perplexity/hands-on/perplexity-hands-on-blocos/` (roteiros, HTMLs, etapas, `saidas/`, `teste/v1`) |
| Plano aprovado | `02_RELATORIOS/perplexity/Plano_Insercoes_HandsOn.md` |
