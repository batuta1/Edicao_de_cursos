# Relatório — Revisão Bibliográfica com IA - Hands On (revisão de texto + inserção de blocos)

**Data:** 11/11/2026 (v2) · **Pacote final:** `Onda 2/01_FINALIZADO_subir-na-LMS/revisao-bibliografica/revisao-bibliografica-com-ia-hands-on-scorm12-mHAyKmaX-FINAL-com-blocos-v2.zip`

## 1. Material-fonte e mapeamento

Fonte: `Pesquisa Conteudo Onda 2/Ementa Completa/revisao-bibliografica-com-ia-hands-on/roteiros/roteiro-articulate-hands-on.md`.
O Articulate **condensou 4 oficinas + Projeto Final em 3 lições**:
- L1 = Oficina 1 (tema → pergunta)
- L2 = Oficina 2 (busca) + Oficina 3 (triagem)
- L3 = Oficina 4 (extração com Elicit) + Projeto Final

Ficaram de fora: **a preparação inteira** (abas a abrir, planilha com colunas, semáforo, avisos de privacidade e de plano pago, as cinco etapas), os quatro "Quer ir além?", o "Sua vez" da Oficina 4 (artigo da UFF), o 🤓 da mudança do Elicit em 30/09/2026, o checklist "Como saber que terminou", A Parte dos Dez e o "Conseguiu! E agora?". Tudo recuperado na fase B.

## 2. Revisão de texto (fase A)

Trabalho em `05_ARQUIVOS_DE_TRABALHO/revisao-bibliografica/hands-on/` (mapas em `gerar_mapas.py` → `revisao_textos/`). **203 campos alterados** (L1 54 · L2 77 · L3 72). `validar_estrutura.py`: estrutura preservada; contagem bate com os mapas.

- **Erro de conteúdo corrigido (L1):** o destaque dizia que "o tema não deve ser formulado como uma pergunta" e dava um exemplo de fotossíntese — o contrário do que o curso ensina. Virou "Tema não é pergunta", com o caso da telessaúde.
- **Erro de conteúdo corrigido (L2):** a aba do Elicit dizia que ele funciona "sem exigir conta"; o roteiro exige conta Basic. A aba agora explica que o Elicit fica para a extração (guardar a cota) e traz o aviso de privacidade.
- Aberturas genéricas trocadas pelo "O Problema" de cada oficina (o pedido do orientador, as chaves debaixo do poste, os 51,40% / 82% do Elicit).
- Objetivos padronizados ("Ao final desta lição, você será capaz de:") e alinhados ao que cada oficina faz.
- Processos: passos genéricos ganharam os breadcrumbs, consultas exatas, o prompt do Consensus verbatim, o comando "Add a column" e os pontos de controle 🏁; os resumos viraram "Deu certo?" com os critérios do roteiro (8.230 × 433,1 mil; 6 de 10 no teste de 04/11/2026).
- Critério de exclusão "estudos fora do Brasil" restaurado no caso-guia; exemplo do PCC trocado para o da pergunta de educação (era o de gestão pública, que no roteiro é PICo); abas de "Sua vez" alinhadas ao gabarito do roteiro.
- Questões: enunciados em forma de cenário e feedbacks "Correto./Não." com o porquê. A alternativa correta da L1 era uma frase sem ponto de interrogação ("Efeitos da telessaúde em…"): virou a pergunta completa — **continua sendo a mesma alternativa correta**. A questão da L3 virou o cenário recrutados × analisados (alternativa correta inalterada).
- Atividade de arrastar (L2): pilhas renomeadas para "Motivo válido de exclusão" / "Não é motivo de exclusão"; "Sem desfecho clínico" → "Sem desfecho de pressão arterial". Gabarito inalterado.
- Fechamentos motivacionais repetidos ("💡 receita…" no fim das três lições) trocados por próximos passos concretos; a receita ficou só no fim do curso.

## 3. Inserções (fase B) — 28 blocos em 8 pontos

| # | Lição | Onde | Tipo | Por quê |
|---|---|---|---|---|
| h08 | L1 | após os objetivos | Título "Antes de arregaçar as mangas" (+ 5 etapas) · título + **accordion das 4 abas da planilha** · título + **HTML Semáforo** (6 casos, correção imediata) · destaque ⚠️ plano pago · **HTML checklist "Quatro abas abertas" + Continue que trava** | a preparação inteira estava ausente; o curso pedia a planilha sem nunca mostrá-la |
| h07 | L1 | antes do fechamento | Título + accordion "Quer ir além? (opcional)" | 3 desafios da Oficina 1 |
| h06 | L2 | entre busca e triagem | Título + accordion "Quer ir além?" + **Continue** | desafios da Oficina 2; o Continue separa busca de triagem |
| h05 | L2 | após o 📌 "Não encontrei" | **HTML "Trie com regra"** (6 resumos fictícios: incluir/excluir/incerto) | a triagem só tinha texto; agora o participante decide com os critérios do caso-guia |
| h04 | L2 | antes do fechamento | Título + accordion "Quer ir além?" | desafios da Oficina 3 |
| h03 | L3 | após o processo do Elicit | Destaque 🤓 mudança de 30/09/2026 · título + **lista "Sua vez: você contra o Elicit"** (artigo da UFF) · destaque ✅ "Deu certo?" | o "Sua vez" da Oficina 4 tinha sumido |
| h02 | L3 | antes do Projeto Final | Título + accordion "Quer ir além?" + Continue | desafios da Oficina 4; abre o Projeto Final como etapa própria |
| h01 | L3 | antes do destaque final | **HTML checklist "Como saber que terminou" + Continue que trava** · título + **lista "A Parte dos Dez"** · título + parágrafo "Conseguiu! E agora?" | fecha o projeto com critério objetivo; Parte dos Dez e encerramento ausentes |

HTMLs em `05_ARQUIVOS_DE_TRABALHO/revisao-bibliografica/html/` (fontes em `src/`, montados por `build.py`; mesma base visual dos cursos de deep-research, cor `#152f4d`).

## 4. Validações

- Fase A (v2): `validar_estrutura.py` sem divergência (203 campos); ponte `verificar_scorm.py` do pacote revisado: **APROVADO**, 0 erros, 0 avisos (o original também: 0/0).
- Fase B (v2): `validar.py` **APROVADO** (28 blocos novos, todos os IDs distintos); `verificar_scorm.py` do pacote final contra o revisado: **APROVADO**, 0 erros, 0 avisos. Nenhum "[conferir]" no curso final.

## 5. Navegador (mock de LMS da skill)

Visto: as três lições com todos os blocos novos na ordem certa; textos revisados renderizando (abertura, processo com "Deu certo?" no fim, abas, questões); Semáforo corrige erro proposital e completa 6/6; checklist da preparação mostra o cadeado e libera o Continue com os 4 itens; "Trie com regra" corrige erro e completa 6/6; checklist final trava e libera, e A Parte dos Dez + "Conseguiu!" aparecem; **retomada** (recarregar sem reset) volta à L3 com o Continue liberado; console sem erros.
v2 conferida de novo no navegador (L3 com o texto novo do artigo da UFF e a origem do fluxograma PRISMA, sem "[conferir]"); os quatro blocos HTML a 360 px de largura sem rolagem horizontal.
Não testado: LMS real e abertura por `file://` (o mock simula a LMS SCORM 1.2).

## 6. Decisões tomadas (v2, 11/11/2026)

- **Marcadores [conferir] resolvidos** por pesquisa: o artigo da UFF mede encaminhamentos presenciais à cardiologia (estudo retrospectivo, Campo Grande/MS), **não** pressão arterial — o curso agora afirma que ele seria excluído do caso-guia; mensagens Pro do Consensus: "de 10 a 15 (as páginas da própria Consensus divergem)"; rótulos de interface que só se conferem com conta (Filter > Country, Has PDF, Filter > Study design, upload no Basic, descritor exibido pelo DeCS) foram reescritos sem depender do rótulo exato.
- **Fluxograma PRISMA:** o passo do Projeto Final agora indica a origem do modelo oficial em português (prisma-statement.org > Translations > Portuguese (Brazilian), .docx).
- Os resumos do "Trie com regra" são **fictícios** (avisado no próprio bloco); o cenário da questão da L3 (1.200 recrutados × 980 analisados) é ilustrativo.
- A atividade de arrastar da L2 classifica "Sem acesso ao texto completo" como "não é motivo de exclusão" — coerente com o PRISMA ("não recuperado" é caixa própria), e o texto da L2 explica isso.
- Curso não publicado na LMS (confirmado); plano de inserções aprovado.

## 7. Pacote a subir

`Onda 2/01_FINALIZADO_subir-na-LMS/revisao-bibliografica/revisao-bibliografica-com-ia-hands-on-scorm12-mHAyKmaX-FINAL-com-blocos-v2.zip`
