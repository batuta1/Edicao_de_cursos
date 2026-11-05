# Relatório de edição — NotebookLM - Essentials (fase A: revisão de texto)

Data: 17/10/2026 · Pacote de entrada: `notebooklm-essentials-scorm12-eKTseo8Q.zip` (não modificado)
Saída: `notebooklm-essentials-scorm12-eKTseo8Q-REVISADO.zip` (hoje em `03_VERSOES_ANTIGAS/notebooklm/fase-A-so-texto/`; versão intermediária, sem os blocos novos da fase B)

## Material-fonte e mapeamento

Fonte principal: `Pesquisa Conteudo Onda 1/Ementa Completa/notebooklm-essentials/roteiros/roteiro-articulate-essentials.md`.

| Lição no Rise | Módulo do roteiro |
|---|---|
| 01 Preparação e Verificação Inicial | Módulo 0 |
| 02 Respostas Ancoradas e Princípios de Verificação | Módulo 1 |
| 03 Segurança, Privacidade e Uso Responsável | Módulo 2 |
| 04 Montagem e Gerenciamento de Fontes no Notebook | Módulo 3 |
| 05 Consultas, Citações e Auditoria de Respostas | Módulo 4 |
| 06 Produção de Artefatos no Estúdio | Módulo 5 |
| 07 Síntese e Aplicação Integrada | Módulo 6 + Encerramento |
| 08 Quiz | avaliação final (gerada pelo Articulate; sem correspondente direto no roteiro) |

## Critério aplicado

`promptRevisaoPorClaude.md` + skill `revisar-curso-scorm`. Só campos textuais; nenhum id, tipo, posição,
setting, item ou gabarito alterado. Edições feitas por script campo a campo (`aplicar.py` + `edicoes.py`,
no scratchpad da sessão), que confere que cada caminho existe e é texto antes de trocar.

## Arquivos editados

Todos os 8 `licao_*.json`. Nenhum arquivo foi lido sem alteração.

## Alterações por lição

Padrões aplicados em todas as lições: fórmula única de objetivos ("Ao final desta lição, você será capaz de:");
aberturas genéricas trocadas pelo conteúdo do roteiro (analogia da prova com consulta, decisão antes do upload
etc.); fechamentos trocados por "Próximo passo: …" concreto; convites de flashcard corrigidos ("passe o mouse"
→ "clique em cada cartão"); de abas ("expanda cada aba" → "clique em cada aba"); feedbacks de questão
padronizados ("Correto." / "Não." + porquê); breadcrumbs 🧭 e critérios 🏁 do roteiro restaurados onde tinham
sumido; process: intro com tempo da atividade, summary com fechamento ou critério de êxito.

- **Lição 01** — datas exatas (16/07/2026, 02/09/2026) e versão mínima do Android restauradas; tabela de
  problemas de acesso reorganizada em situação/causa/o que fazer; questão virou cenário ("e-mail da escola").
- **Lição 02** — "respostas produzidas *exclusivamente*" corrigido para "o notebook *privilegia*" (como no
  roteiro); acrescentados os riscos concretos da citação (trecho real que não sustenta a frase, ressalva
  omitida, fontes divergentes conciliadas), os três painéis com nomes em inglês e o objetivo 4 (quando o
  notebook é preferível), que estava ausente; prompt-base ganhou os cinco elementos do pedido ancorado.
- **Lição 03** — restaurado o alerta da ANPD (dados no ciclo da IA, reidentificação) e a recomendação do CFOAB;
  removida a menção a "médicos" (não está no roteiro); abas verde/amarelo/vermelho com exemplo e conduta;
  breadcrumb de compartilhamento restaurado.
- **Lição 04** — **o kit de fontes tinha perdido os quatro endereços**; foram restaurados como links (bloco 11).
  Corrigido "PDFs podem conter até 500.000 palavras" → "cada fonte pode ter até 500.000 palavras" (o limite
  vale para qualquer fonte). Acrescentada a situação "o PDF baixado abre como página da web", que o Articulate
  omitiu (dentro do item "PDF com problema"). Prompt de conferência do corpus voltou ao formato copiável.
- **Lição 05** — **o bloco "Mão na massa" (bloco 14) trazia a *resposta* do prompt (definições da LGPD) em vez
  do prompt-base**; o passo 1 da auditoria mandava enviar um prompt que não existia na tela. Restaurado o prompt
  comparativo do roteiro. Acrescentado um exemplo de correspondência ausente (ver pontos de atenção).
  Feedback da alternativa "usar apenas uma fonte" corrigido: a lição recomenda reduzir fontes para precisão.
- **Lição 06** — **mesmo problema da lição 05 no bloco 14** (resumo da LGPD no lugar do prompt de orientação);
  restaurado o prompt. Removidas afirmações sem fonte (Documento de resumo "ideal para sínteses rápidas",
  "personalize o foco do relatório"). Restaurados: ambiguidade da palavra "resumo", linha do tempo via relatório
  personalizado, duração Longer e modo interativo só em inglês.
- **Lição 07** — descrições da linha do tempo amarradas às lições; restaurados os quatro cenários (a)–(d) do
  roteiro; "projetos RAG e Bases de Conhecimento" corrigido para "projetos de assistentes gerais, tema do curso
  RAG e Bases de Conhecimento"; definição de ancoragem no flashcard corrigida; process ganhou critérios de
  avaliação em lista e a extensão opcional; parágrafo final motivacional trocado por próximo passo concreto.
- **Lição 08 (Quiz)** — alternativas "True/False" traduzidas para "Verdadeiro/Falso" (blocos 10, 16, 17);
  feedbacks reescritos sem metalinguagem ("A alternativa é convincente porque…"); "500.000 … palavras em
  PDFs" corrigido para "por fonte". Respostas aceitas dos FILL_IN_THE_BLANK e matchTitle dos MATCHING intactos.

## Contagem e validação

- Campos alterados: **362** (aplicados pelo script = contados pelo validador). Por campo: description 145,
  feedback 86, paragraph 71, title 44, heading 16.
- `validar_estrutura.py`: **ESTRUTURA OK** nas 8 lições.
- `scorm_reempacotar.py`: round-trip do Base64 conferido; 84 arquivos, 0 alterados fora de `runtime-data.js`.
- `verificar_scorm.py` (skill de inserção): **APROVADO**, 0 erros, 0 avisos.

## Pontos de atenção (revisão humana)

1. **Textos em inglês que a revisão não pode tocar** (campos não textuais para o validador):
   `date` da linha do tempo da lição 07 ("Step 1: Decidir"…) e `completeHint` dos Continue ("Complete the
   content above before moving on."). Corrigir no Rise ou autorizar edição desses campos.
2. **Rótulos marcados [conferir] no roteiro** foram mantidos sem a marca no texto do aluno: "adicionar fonte",
   "site/link", renomear pelo título, `Configure Chat`, `Save to note`, "visualização da conversa",
   "Gerar mais tarde". Conferir numa conta real antes de publicar.
3. **Exemplo novo na lição 05** (accordion "Classificação da correspondência"): "a LGPD proíbe o tratamento de
   dados sensíveis" × trecho que lista as hipóteses de tratamento (art. 11). É ilustrativo; conferir a redação.
4. Os textos dos prompts-base perderam as aspas triplas do roteiro (no Rise, aparecem como bloco destacado).
5. Gabaritos: nenhum parece errado. Nenhum foi alterado.

## Não verificado

O curso revisado **ainda não foi aberto no navegador** — isso fica para a fase B (mock de LMS), junto com os
blocos novos. Em especial: renderização dos links do kit (lição 04) e das alternativas "Verdadeiro/Falso".
