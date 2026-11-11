# Relatório — Deep Search com IA - Essentials (revisão de texto + inserção de blocos)

**Data:** 07/11/2026 · **Pacote final:** `Onda 2/01_FINALIZADO_subir-na-LMS/deep-research/deep-search-com-ia-essentials-scorm12-xEZQDi0v-FINAL-com-blocos-v1.zip`
**Curso publicado com alunos?** Não (informado pelo usuário) — inserções em qualquer posição.

## 1. Material-fonte e mapeamento

Fonte: `Pesquisa Conteudo Onda 2/Ementa Completa/deep-research-hands-on/roteiros/roteiro-articulate-essentials.md`.
Mapeamento 1:1: L1 = Módulo 0 · L2 = Módulo 1 · L3 = Módulo 2 · L4 = Módulo 3 · L5 = Módulo 4 · L6 = Módulo 5 · L7 = Módulo 6 + Encerramento · L8 = Quiz.

## 2. Revisão de texto (fase A)

Trabalho em `05_ARQUIVOS_DE_TRABALHO/deep-research/essentials/` (mapas em `gerar_mapas.py` → `revisao_textos/`, aplicados por `aplicar_mapas.py`).
**152 campos alterados** (L1 25 · L2 22 · L3 30 · L4 20 · L5 18 · L6 21 · L7 16 · Quiz 0). `validar_estrutura.py`: estrutura preservada em todas as lições; contagem bate com os mapas.

Principais correções:
- **Aberturas genéricas** trocadas pelos exemplos do roteiro (Selic × panorama da população idosa; "pesquise envelhecimento no Brasil"; "a melhor ferramenta é a pergunta errada").
- **Objetivos** padronizados em "Ao final desta lição, você será capaz de:".
- **L2:** os cartões da atividade de classificação estavam **cortados no meio da frase** (limite de 80 caracteres do Rise: "…entre 2010 e 2022,  <"). Reescritos para caber.
- **L5:** a questão pedia para classificar "as afirmações abaixo", que **não apareciam em lugar nenhum**. As três frases do roteiro foram postas no enunciado; feedbacks reescritos com os números.
- **L5:** o fechamento anunciava o "dossiê final" como próximo módulo; o próximo é o de ferramentas e benchmarks. Corrigido.
- **L6:** feedback da questão DRACO dizia "Perplexity e BrowseComp podem medir…" (confundia ferramenta com benchmark). Corrigido com os dados do roteiro.
- **L7:** a atividade integradora falava em "documentos jurídicos"; o caso-guia é o do IBGE. Corrigido.
- **L4:** removida a afirmação inventada de que o modo Thinking/Pro "influencia o acesso a fontes"; ChatGPT "opção de bloqueio" → "restringir".
- Detalhes restaurados: rota sem cota (relatório do MIT), números de 2025 como históricos, Sources do Gemini, princípios completos da LGPD, item "fonte de baixa autoridade", 🏁 nos pontos de controle, rótulos nos modelos copiáveis, linha de síntese verbatim.
- **Quiz:** lido; sem alterações.

## 3. Inserções (fase B) — 14 blocos em 9 pontos

| # | Lição | Onde | Tipo | Por quê |
|---|---|---|---|---|
| E1 | L2 | após a definição de pesquisa profunda | HTML infográfico "O que acontece entre o pedido e o relatório" | o ciclo brief → plano → buscas → relatório → auditoria, com o que é seu e o que é do agente |
| E2 | L3 | após o gabarito dos cenários | Título + **HTML semáforo** (6 situações novas, correção imediata) | o processo original mostra a resposta junto do cenário; aqui o aluno decide |
| E3 | L3 | após os flashcards do checklist | Destaque com o checklist-base copiável | modelo do roteiro que o Articulate omitiu |
| E4 | L4 | após os 6 componentes | Parágrafo + abas "Pedido vago × Brief reescrito" | exemplo de antes/depois omitido |
| E5 | L4 | após a demonstração | Destaque 🏁 ponto de controle | único módulo sem ponto de controle |
| E6 | L5 | antes da questão de classificação | Título "Pílula Hands-on" + destaque 📌 gabarito do IBGE | a questão usava números que o aluno nunca via |
| E7 | L6 | após os flashcards de benchmark | Parágrafo + abas BrowseComp / DRACO / DeepResearch Bench | os três estudos e seus conflitos de interesse estavam ausentes |
| E8 | L6 | após o destaque "nenhum desses números" | Título + texto "Escolha por tarefa" | recomendação final do módulo (objetivo 3) ausente |
| E9 | L7 | após o Continue, antes do encerramento | **HTML checklist dos 6 critérios + Continue que trava** | autoavaliação ativa; o encerramento só abre com os 6 marcados |

**Mudanças em relação ao plano aprovado:** E2 passou a usar **seis situações novas** e foi para depois do gabarito (prática de transferência), em vez de repetir os cinco cenários do exercício. E9 entrou depois do Continue existente (e não antes) para não deixar dois Continues seguidos.
HTML: `05_ARQUIVOS_DE_TRABALHO/deep-research/html/` (fontes em `src/`, montados por `build.py`). Roteiros: `essentials/deep-essentials-blocos/trabalho/roteiros/` (gerados por `deep-research/roteiros_insercao.py`). Nenhuma pasta anexada (todos os HTML são embutidos).

## 4. Validações

- Fase A: `validar_estrutura.py` sem divergência; ponte `verificar_scorm.py` do `-REVISADO.zip`: **APROVADO**, 0 avisos.
- Fase B: `validar.py`: **APROVADO** (só inserção; 646 IDs, todos distintos). `verificar_scorm.py` do pacote final contra o revisado: **APROVADO**, 0 erros, 0 avisos.

## 5. Navegador (mock de LMS da skill, servidor local)

Visto: texto revisado da L2; infográfico E1 renderizado com a estética do curso; abas E4 e E7 presentes (o Rise mostra os títulos em maiúsculas); E3, E5, E6, E8 presentes na posição certa; semáforo E2 corrige na hora (erro e acerto) e chega a 6 de 6; checklist E9 mostra o cadeado ("Complete the content above…") e libera o Continue com os 6 marcados; console sem erros.
**Não verificado:** retomada de progresso neste curso (verificada no Hands On, mesmo mecanismo); largura de celular (~400 px); abertura por `file://`; comportamento na LMS real.

## 6. Pontos de atenção

- Marcadores **[conferir]** mantidos do roteiro (rótulos de interface, saldo, Perplexity gratuita, exportação da Perplexity). Precisam de conferência humana antes de publicar.
- Situações do semáforo E2 são **exemplos de aplicação** escritos para o curso (não estão no roteiro); as regras aplicadas são as do Módulo 2. Vale uma leitura.
- Números e datas (IBGE, benchmarks, datas de lançamento) foram copiados do roteiro, sem nova conferência na fonte.
- Gabaritos das questões existentes não foram alterados; nenhum pareceu errado.

## 7. Pacote a subir

`Onda 2/01_FINALIZADO_subir-na-LMS/deep-research/deep-search-com-ia-essentials-scorm12-xEZQDi0v-FINAL-com-blocos-v1.zip`
