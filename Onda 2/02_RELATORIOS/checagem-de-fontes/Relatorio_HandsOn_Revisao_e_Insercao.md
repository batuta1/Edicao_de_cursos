# Relatório de revisão e inserção — Checagem de Fontes e Citações com IA - Hands On

Data: 05/11/2026 · Curso **presumido não publicado** (veio de `04_NAO_REVISADO/`; não confirmado) — por isso houve inserções no meio das lições.

**Pacote final para a LMS (v1):**
`01_FINALIZADO_subir-na-LMS/checagem-de-fontes/checagem-de-fontes-e-citacoes-com-ia-hands-on-scorm12-7E0iZEFj-FINAL-com-blocos-v1.zip`
(cópia idêntica, por hash, de `05_ARQUIVOS_DE_TRABALHO/checagem-de-fontes/hands-on/checagem-hands-on-blocos/saidas/…-REVISADO-v1.zip`).

Histórico em `03_VERSOES_ANTIGAS/checagem-de-fontes/` (`original-articulate/`, `fase-A-so-texto/`). O original continua também em `04_NAO_REVISADO/checagem de fontes e citacoes/`.

---

## 1. Material-fonte e mapeamento

Roteiro: `Pesquisa Conteudo Onda 2/Ementa Completa/checagem-de-fontes-e-citacoes-essentials/roteiros/roteiro-articulate-hands-on.md`.
O Articulate **condensou 5 partes em 3 lições**:

| Lição do Rise | Roteiro |
|---|---|
| 1 | Antes de Arregaçar as Mangas + Oficina 1 |
| 2 | Oficinas 2 e 3 |
| 3 | Oficina 4 + A Parte dos Dez + Conseguiu! (o **Projeto Final tinha sumido** — reposto na Fase B) |

## 2. Fase A — revisão de texto (146 campos)

Mapas `revisao_textos/L01..L03.json` (`gerar_mapas.py` + `aplicar_mapas.py`). Por lição: L1 33 · L2 59 · L3 54. Por campo: paragraph 50, description 38, title 30, heading 16, feedback 12.

**O que estava ruim e o que foi feito:**
- **Oficina 3 genérica:** os passos não citavam nenhum par, DOI ou artigo ("Acesse o artigo na SciELO e verifique se há banners"). Reescritos com os pares 5 e 3, os DOIs, o banner "ARTIGO RETRATADO", a curiosidade 🤓 sobre o motivo da retratação, a rota sem Scite (Ranehill et al., termos para Localizar) e a rota com Scite marcada como opcional.
- **Oficina 2:** o pedido à Perplexity (o comando entre aspas do roteiro) tinha sumido — voltou; o "Deu certo?" com o gabarito (a)/(b) "não apoia" e par 1 "apoia" passou a ser o resumo do process.
- **Abertura, encomenda e regra de ouro:** o subtítulo do curso, "Existe? Diz isso? Ainda vale?" e a analogia da encomenda não apareciam; entraram na abertura e no destaque da regra de ouro. Semáforo virou 🟢🟡🔴 com o aviso ⚠️ da Scite.
- **Oficina 4:** caminho do STJ, ponto de controle e "Deu certo?" repostos; objetivos alinhados.
- **Parte dos Dez:** os dez hábitos tinham sido parafraseados e perderam a graça ("É um boato com casas decimais"); voltaram ao texto do roteiro. "Parabéns! … mantenha o padrão elevado" trocado pelo "Conseguiu! E agora?" do roteiro.
- Tom "Para Leigos" (você, frases curtas, emojis 🎯🧰🚑✅) restaurado nos títulos; objetivos padronizados em "Ao final desta lição, você será capaz de:"; feedbacks "Isso." / "Não." com o porquê.

Validação: `validar_estrutura.py` — **estrutura preservada nas 3 lições; 146 campos = 146 entradas dos mapas.**

## 3. Fase B — inserções (16 blocos)

| Lição | Posição final | Tipo | Por quê |
|---|---|---|---|
| 1 | 9–10 | Título + parágrafo "O mapa da mão na massa" + lista numerada (5 oficinas, problema e tempo, e em que lição está cada uma) | Mapa do roteiro omitido; o aluno não sabia que o curso tem 4 oficinas + projeto |
| 1 | 17–18 | Título + accordion "🚀 Quer ir além? (opcional)" — 3 desafios da Oficina 1 | Desafios do roteiro omitidos |
| 2 | 8–9 | Idem, Oficina 2 | Idem |
| 2 | 15–16 | Idem, Oficina 3 | Idem |
| 3 | 10–11 | Idem, Oficina 4 | Idem |
| 3 | 17–22 | **Seção Projeto Final**: título + parágrafo (missão), abas Dossiê científico × jurídico, título + lista com os 6 passos, HTML "🏁 Como saber que terminou" (checklist de 6 itens) + Continue que trava | O Projeto Final do roteiro (22 min) não existia no curso |

Tudo em texto verbatim do roteiro, exceto a segunda frase de cada aba de dossiê e as frases de abertura dos blocos (minhas). HTML em `…/checagem-hands-on-blocos/trabalho/html/src/pf-checklist.body.html`.

## 4. Validações

| Etapa | Ferramenta | Resultado |
|---|---|---|
| Fase A | `validar_estrutura.py` | Estrutura preservada; 146 campos |
| Ponte | `verificar_scorm.py …-REVISADO.zip --original` | APROVADO, 0 erros, 0 avisos |
| Fase B | `validar.py curso_v1.json --original` | APROVADO; 16 blocos novos; 308 IDs distintos |
| Pacote final | `verificar_scorm.py …-v1.zip --original …-REVISADO.zip` | APROVADO, 0 erros, 0 avisos |

## 5. Navegador (mock de LMS da skill)

Visto: mapa, regra de ouro com a encomenda e os 4 "Quer ir além?" presentes após os Continues; seção do Projeto Final no lugar certo; com 5 de 6 itens marcados o Continue segue travado, com 6 libera e a Parte dos Dez aparece em seguida; Parte dos Dez revisada renderiza corretamente; retomada sem `reset` volta à lição 3 com o Continue liberado; console sem erros.

**Não verificado:** largura de celular; LMS real; duplo clique (`file://`); leitura visual de cada bloco revisado (conferidos por texto/validador).

## 6. Pontos de atenção (revisão humana)

1. **Gabarito discutível — questão da lição 3** ("Qual é a melhor fonte para conferir o texto vigente de um artigo de lei citado em uma petição?"; gabarito: Diário Oficial). O roteiro usa o Planalto para conferir o texto vigente e só diz que ele é informativo e não substitui o Diário Oficial. O feedback original do Planalto ("pode não refletir alterações mais recentes") não tem base no roteiro e foi reescrito. **Gabarito não alterado.** Proposta: reformular o enunciado para "Qual é a publicação oficial que prevalece sobre a base do Planalto?" ou aceitar o Planalto com a ressalva de anotar versão e data.
2. **Marcadores `[conferir]`** mantidos (posição do menu da Perplexity, rótulo Academic, Check Sources, cartão da Scite no Brasil, caminho da Scite, rótulos do STJ, alertas da Collection). Validar e retirar antes de subir.
3. A rota com Scite da Oficina 3 é uma etapa do *process* marcada "(Opcional)" — o bloco nativo não permite etapa opcional de verdade.
4. Rótulos do player em inglês, não alterados.
5. Texto do checklist HTML é verbatim do roteiro; a frase final é minha.
