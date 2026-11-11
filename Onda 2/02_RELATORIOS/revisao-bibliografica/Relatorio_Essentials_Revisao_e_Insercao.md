# Relatório — Revisão Bibliográfica com IA - Essentials (revisão de texto + inserção de blocos)

**Data:** 11/11/2026 (v2) · **Pacote final:** `Onda 2/01_FINALIZADO_subir-na-LMS/revisao-bibliografica/revisao-bibliografica-com-ia-essentials-scorm12-3jzmScz3-FINAL-com-blocos-v2.zip`

## 1. Material-fonte e mapeamento

Fonte: `Pesquisa Conteudo Onda 2/Ementa Completa/revisao-bibliografica-com-ia-hands-on/roteiros/roteiro-articulate-essentials.md`.
Mapeamento **1:1**: L1–L7 = Módulos 0–6 (o encerramento está no fim da L7); L8 = Quiz final (20 questões, geradas pelo Articulate).
O Articulate seguiu o roteiro de perto; faltavam a 2ª questão do Módulo 1 (PRISMA), a pílula Hands-on do Módulo 3 com gabarito e a discussão dos totais do Módulo 4 com os números reais.

## 2. Revisão de texto (fase A)

Trabalho em `05_ARQUIVOS_DE_TRABALHO/revisao-bibliografica/essentials/` (mapas em `gerar_mapas.py` → `revisao_textos/`). **323 campos alterados** (L1 49 · L2 40 · L3 39 · L4 55 · L5 49 · L6 45 · L7 36 · Quiz 10) + o `matchTitle` da questão 17. `validar_estrutura.py`: estrutura preservada; contagem bate com os mapas.

Erros de conteúdo corrigidos:
- **L1:** o accordion do Consensus listava "exportação de tabela CSV/Excel" como recurso pago — isso é do **Elicit** (Plus). O flashcard do Consensus repetia o erro.
- **L5:** a base brasileira recomendava "AND, OR, NOT"; o roteiro manda **evitar NOT** quando ele puder excluir estudos relevantes. O flashcard do Consensus dizia "exige cadastro" — a primeira busca funciona sem conta.
- **L5:** o prompt-base do Consensus tinha perdido os colchetes ("…sobre intervenção ou conceito em população no contexto de contexto"). Restaurado o modelo do roteiro.
- **L6:** as instruções de coluna do Research Agent tinham sido **traduzidas para o português**; o roteiro manda manter em inglês (é o que se cola no Elicit). Restaurado.
- **L6:** "não disponível em texto completo" aparecia como motivo de exclusão; no PRISMA é "não recuperado". Aba "Motivo de exclusão mais comum" (afirmação sem fonte) virou "Motivo vago × motivo específico"; a orientação inventada de anotar "data da decisão e responsável" foi trocada pelas colunas reais da aba Triagem.
- **L7:** exemplos com autores e números fictícios ("Silva et al., 2022…") não avisavam que eram fictícios, e o modelo de síntese vinha preenchido com eles. O modelo voltou a ser o template com colchetes do roteiro; os exemplos ganharam o aviso "fictícios — não cite". O exemplo do Log ("Consensus, 10/06/2024, total 45") virou a busca real do caso-guia (04/11/2026, cerca de 8.230); a lacuna "junho de 2024" virou 04/11/2026.
- **Quiz:** alternativas "True"/"False" em inglês → "Verdadeiro"/"Falso" (questões 16 e 20; gabarito inalterado).

Melhorias didáticas: aberturas genéricas trocadas pelo texto do roteiro (cota esgotada confundida com erro, visita guiada × mapa do território × auditoria, "depois que um prontuário foi colado num chat…"); objetivos verbatim; analogias e dados que tinham sido resumidos (214 milhões, Paper/Pro/Deep, TLDR, BDTD, Google Acadêmico, SOC 2, política de 2023 [conferir], CNPq 13/03/2026, Cochrane, CAPES, Notebooks [conferir], Research Report); "mini-revisão rastreável, não sistemática"; flashcards que repetiam o accordion ao lado viraram teste ("qual aba guarda o quê?", "inclusão ou exclusão?"); processos com breadcrumbs e títulos "Demonstração (10 min)", "Pílula Hands-on (6 min)", "Critério de êxito"; cenários do semáforo com a resposta separada do enunciado; questão do Módulo 4 reescrita com os números 8.230 × 433,1 mil e alternativas "Sim/Não" (gabarito inalterado).

## 3. Inserções (fase B) — 8 blocos em 7 pontos

| # | Lição | Onde | Tipo | Por quê |
|---|---|---|---|---|
| e02 | L2 | após o accordion das modalidades | **HTML "Qual modalidade de revisão?"** (5 objetivos × 5 modalidades) | o objetivo 1 da lição só tinha leitura; agora o participante decide |
| e01 | L2 | após a 1ª questão | **Questão** "O que o PRISMA 2020 é, de fato?" (correta na 2ª posição) | 2ª questão do Módulo 1, omitida pelo Articulate |
| e03 | L3 | fim da lição | **HTML "Monte sua declaração de uso de IA"** (gera o texto do roteiro, avisa o que falta, botão copiar) | objetivo 4 ("redigir uma declaração") não tinha prática |
| e04 | L4 | antes da questão | Título + accordion "Pílula Hands-on (6 min): agora em PCC" com o gabarito | pílula e gabarito do Módulo 3 ausentes |
| e05 | L5 | após o ⚠️ do Semantic Scholar | **HTML "Onde esta consulta funciona?"** (5 consultas: Semantic Scholar × BVS/SciELO) | a regra booleano × semântica era só texto |
| e06 | L6 | após os estudos independentes | **HTML "Confira a célula"** (5 células fictícias: conferido / corrigido / só resumo) | treina a conferência que o módulo exige |
| e07 | L7 | após o ponto de controle do PRISMA | **HTML "Do Log ao fluxograma PRISMA"** (calculadora das caixas, com exemplo e avisos) | preencher o fluxograma era só descrito |

Nenhum bloco trava o Continue no Essentials. HTMLs em `05_ARQUIVOS_DE_TRABALHO/revisao-bibliografica/html/`.

## 4. Validações

- Fase A (v2): `validar_estrutura.py` sem divergência (323 campos); ponte `verificar_scorm.py`: **APROVADO**, 0 erros, 0 avisos (o original também: 0/0). A troca do `matchTitle` da questão 17 (ver seção 6) é feita depois dessa validação por `v2_quiz_associacao.py`, que confere que só aquele campo muda.
- Fase B (v2): `validar.py` **APROVADO** (8 blocos novos, todos os IDs distintos); `verificar_scorm.py` do pacote final contra o revisado: **APROVADO**, 0 erros, 0 avisos. Nenhum "[conferir]" no curso final.

## 5. Navegador (mock de LMS da skill)

Visto: todas as lições (L1–L7 e o Quiz) com os blocos novos na posição planejada; as cinco atividades HTML funcionando (modalidade 5/5, onde buscar 5/5, confira a célula 5/5, declaração gerada com aviso "atende ao CNPq", calculadora PRISMA 20 → 3 → 17 → 8 → 7 → 5); Quiz percorrido até a questão 17: a questão 8 nova aceita "Vermelho" (com maiúscula) como correta, a 17 mostra o texto corrigido e a 16 mostra Verdadeiro/Falso; os nove blocos HTML a 360 px de largura sem rolagem horizontal; console sem erros do curso.
Não testado: LMS real e abertura por `file://` (o mock simula a LMS SCORM 1.2).

## 6. Decisões tomadas (v2, 11/11/2026)

- **Quiz, questão 8 (preencher lacuna):** a resposta "políticas específicas de processamento e privacidade de dados" era impossível de acertar digitando. Trocada por "No semáforo do curso, enviar … uma planilha com dados de prontuário de pacientes é classificado como ____." → "vermelho".
- **Quiz, questão 17 (associação):** "aceita AND, OR e NOT" → "aceita expressões booleanas com AND e OR (evitando NOT)".
- **Marcadores [conferir] resolvidos** por pesquisa (11/11/2026): o artigo da UFF é um estudo retrospectivo de Campo Grande (MS) que mede encaminhamentos à cardiologia, **não** pressão arterial — o curso agora diz que ele seria excluído do caso-guia; o Consensus informa 10 Pro/mês na central de ajuda e 15 no arquivo de preços — o curso diz "de 10 a 15 (as páginas da própria Consensus divergem)"; rótulos de interface que exigem conta para conferir (Filter > Country, Has PDF, Settings > Subscription, busca avançada da BVS, Notebooks, data da política do Elicit) foram reescritos sem depender do rótulo exato.
- **Fluxograma PRISMA:** o curso agora indica a origem do modelo oficial em português (prisma-statement.org > Translations > Portuguese (Brazilian), .docx).
- Atividades "Confira a célula" e os exemplos de síntese usam **dados fictícios**, avisados no próprio bloco.
- Curso não publicado na LMS (confirmado): inserções no meio das lições sem risco para progresso de alunos. Plano de inserções aprovado.

## 7. Pacote a subir

`Onda 2/01_FINALIZADO_subir-na-LMS/revisao-bibliografica/revisao-bibliografica-com-ia-essentials-scorm12-3jzmScz3-FINAL-com-blocos-v2.zip`
