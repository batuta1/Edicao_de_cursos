# Relatório — ChatGPT Chat - Hands On (revisão de texto + inserção de blocos)

**Data:** 17/11/2026 (v1) · **Pacote final:** `Onda 2/01_FINALIZADO_subir-na-LMS/chatgpt-chat/chatgpt-chat-hands-on-scorm12-kvqOIjeU-FINAL-com-blocos-v1.zip`

## 1. Material-fonte e mapeamento

Fonte: `Pesquisa Conteudo Onda 2/Ementa Completa/chatgpt-chat-essentials/roteiros/roteiro-articulate-hands-on.md`.
Mapeamento 1:1: L1–L4 = Oficinas 1–4; L5 = Projeto Final. A preparação ("Antes de arregaçar as mangas") ficou no início da L1.

Ficaram de fora no Articulate: **o conteúdo dos dois arquivos do caso** (o curso tinha só um resumo e dois links para arquivos que não existem no pacote — sem eles nenhuma oficina pode ser feita), o mapa das oficinas, o gabarito da Oficina 4, o título "Quer ir além?" da Oficina 3 e A Parte dos Dez. Tudo recuperado na fase B.

## 2. Revisão de texto (fase A)

Trabalho em `05_ARQUIVOS_DE_TRABALHO/chatgpt-chat/hands-on/`. **209 campos alterados** (L1 49 · L2 46 · L3 37 · L4 36 · L5 41). Validação com `validar_texto.py`: estrutura preservada, 209 = 209.

**Erros de conteúdo corrigidos**
- **L1 — links quebrados:** o bloco dos arquivos apontava para `reclamacoes-loja-aurora.csv` e `politica-de-trocas-loja-aurora.txt`, que não existem no pacote. O texto virou a descrição dos arquivos, e o conteúdo completo entrou no kit HTML (fase B).
- **L1 — lista de recursos:** o terceiro item era a frase "Tenha esses itens em mãos…"; virou o terceiro recurso real (o texto das instruções do projeto).
- **L1:** o rótulo do 🏁 trazia o caminho incompleto; voltou o ponto de controle verbatim.
- **L2 e L4:** os prompts apareciam com as aspas triplas do roteiro dentro do texto (`""" … """`); limpos.
- **L3:** o passo 1 trazia "[conferir rótulo]" visível para o aluno; reescrito pela função.
- **L5:** os três desafios "Quer ir além?" eram genéricos (apresentar oralmente, adaptar para imprensa) e sem validação verificável; reescritos com validação concreta (números e artigos se mantêm, perguntas difíceis da diretoria, versão para clientes sem número interno).

**Demais melhorias**
- Aberturas genéricas ("Transformar dados brutos em informações claras é uma habilidade essencial…") trocadas pelo "🎯 O problema" de cada oficina; seções com os rótulos do roteiro (🧰 O que você vai usar, 🚑 Se travar, 🚀 Quer ir além?).
- Objetivos padronizados e alinhados ao que cada oficina faz.
- Processos com título e número de passos do roteiro; breadcrumbs em negrito.
- "A missão" do Projeto Final e "Conseguiu! E agora?" verbatim; o checklist "Como saber que terminou" com 🏁.
- Feedbacks das questões no padrão "Correto./Não."; nenhum gabarito alterado (os quatro estavam certos).

## 3. Inserções (fase B) — 13 blocos em 6 pontos

| # | Lição | Onde | Blocos | Por quê |
|---|---|---|---|---|
| h06 | L1 | após a descrição dos arquivos | **HTML "Kit do caso"** (CSV e política verbatim, com botões de copiar + checklist de 4 itens) que **trava o Continue** + Continue | sem os arquivos o curso não funciona |
| h05 | L1 | antes de "Mão na massa" | Título + lista "O mapa da mão na massa" (5 etapas e tempos) + frase de sequência + Continue | mapa do roteiro ausente |
| h04 | L3 | antes do 🏁 | **HTML "Política × CDC, item por item"** (5 itens; conflita ou não) | consolida os dois conflitos que vão para o relatório |
| h03 | L3 | antes dos desafios | Título "🚀 Quer ir além? (opcional)" | o accordion de desafios aparecia sem título |
| h02 | L4 | antes do 🏁 | **HTML "Os números do ChatGPT batem?"** (5 campos conferidos contra o gabarito) que **trava o Continue** + Continue + **gabarito** (5 valores) | o 🏁 citava "os cinco valores da tabela", que não existia |
| h01 | L5 | antes do Continue final | Título + lista **"A Parte dos Dez"** (10 atalhos) | seção do roteiro ausente |

Gabarito da Oficina 4 recalculado a partir do CSV (`conferir_csv.py`): 609 reclamações, 501 resolvidas (82,3%), troca/devolução 158/102 (64,6%), mai–ago 54 × set–out 104, pior mês outubro (132), depois setembro (122) — confere com o roteiro.

## 4. Validações

- Fase A: `validar_texto.py` sem divergência estrutural (209 campos); `scorm_reempacotar.py` com round-trip e 0 arquivos alterados fora do `runtime-data.js`; `verificar_scorm.py`: **APROVADO**, 0 erros, 0 avisos.
- Fase B: `validar.py` **APROVADO** (13 blocos novos; 373 IDs, todos distintos); `verificar_scorm.py` do pacote final contra o revisado: **APROVADO**, 0 erros, 0 avisos. Nenhum "[conferir]" no curso final.

## 5. Navegador (mock de LMS da skill)

Visto: as 5 lições percorridas até o fim; o Continue da L1 fica travado ("Complete the content above") até o checklist do kit ser marcado e libera depois; o mesmo com a conferência de números da L4 (609/501/82,3/104/outubro → mensagem final); o classificador Política × CDC completa 5/5; mapa, gabarito, título "Quer ir além?" e A Parte dos Dez aparecem na posição certa; os 3 HTMLs a 360 px sem rolagem horizontal.
**Não testado:** as quatro questões clicadas no navegador (texto e gabarito conferidos no JSON); LMS real; abertura por `file://`; cópia com área de transferência real (o teste caiu no fallback "texto selecionado, use Ctrl+C", previsto).

## 6. Decisões tomadas

- **[conferir] do roteiro:** "Ramificar em novo chat" confirmado em Mais ações (⋯); o rótulo da busca no botão "+" varia entre versões e foi escrito pela função ("ative a busca na web pelo botão +, ou escreva 'pesquise na web'").
- Na atividade Política × CDC, os itens 3, 4 e 5 aparecem como "não é conflito do caso": o item 3 está de acordo com o art. 18 (sem exceção para promoção); os itens 4 e 5 tratam de horário e prazo de resposta, que os artigos conferidos na oficina não regulam. A atividade não afirma que eles estão de acordo com toda a legislação.
- A conferência de números da L4 trava o Continue; quem esbarrar no limite do Free tem a rota do "Se travar" (colar o CSV na conversa) e as dicas de cálculo em cada campo.
