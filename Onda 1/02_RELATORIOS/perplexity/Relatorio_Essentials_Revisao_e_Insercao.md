# Relatório de revisão e inserção — Perplexity - Essentials

Data: 18/10/2026 · Grau de liberdade: moderado · Curso **não publicado** com alunos (confirmado): inserções em qualquer posição.

**Pacote final para a LMS (v2):**
`01_FINALIZADO_subir-na-LMS/perplexity/perplexity-essentials-scorm12-PHjV4LCQ-FINAL-com-blocos-v2.zip` (cópia idêntica, por hash, de
`05_ARQUIVOS_DE_TRABALHO/perplexity/essentials/perplexity-essentials-blocos/saidas/perplexity-essentials-scorm12-PHjV4LCQ-REVISADO-v2.zip`).

Histórico em `03_VERSOES_ANTIGAS/perplexity/`: `original-articulate/` (exportação do Articulate, não modificada),
`fase-A-so-texto/` (`-REVISADO.zip` = r1 e `-REVISADO-r2.zip`, só texto) e `fase-B-v1/` (primeira versão com blocos,
substituída pela v2).

---

## 1. Material-fonte e mapeamento

Roteiro: `Pesquisa Conteudo Onda 1/Ementa Completa/perplexity-essentials/roteiros/roteiro-articulate-essentials.md`.
Conferências externas feitas em 18/10/2026: texto da LGPD no portal do Planalto (compilado e original) e a interface
pública de perplexity.ai, **sem login**.

| Lição no Rise (licao = position) | Módulo do roteiro |
|---|---|
| 1 Preparação e Verificação Inicial (0) | Identificação/Objetivo/Competências + Módulo 0 |
| 2 Entendendo o Motor de Respostas com Citações (1) | Módulo 1 |
| 3 Segurança, Privacidade e Responsabilidade Profissional (2) | Módulo 2 |
| 4 Formulando Perguntas e Escolhendo a Profundidade da Busca (3) | Módulo 3 |
| 5 Conferindo Citações e Comparando Fontes (4) | Módulo 4 |
| 6 Organizando a Pesquisa e Produzindo a Síntese Citada (5) | Módulo 5 |
| 7 Síntese e Aplicação Integrada (6) | Módulo 6 + Encerramento |
| 8 Quiz (7) | avaliação final gerada pelo Articulate |

## 2. Fase A — revisão de texto

Detalhes em `02_RELATORIOS/perplexity/Relatorio_Essentials_Fase_A_Revisao_de_Texto.md`. Resumo:

- 8 lições editadas, **423 campos de texto** (description 163, paragraph 88, feedback 78, title 64, heading 30).
- Correções de conteúdo mais importantes: prompts "Mão na massa" restaurados nas lições 2, 4 e 5 (na 4 havia uma
  *resposta* inventada no lugar do prompt; na 5, "Sem apoio suficiente." e uma resposta com quatro links quebrados
  `href="NÃO ENCONTRADO"`); objetivos das lições 6 e 7 alinhados ao roteiro; afirmações sem fonte retiradas;
  alternativa correta do quiz "citações *auditadas*" → "números de citação" (gabarito intacto); "True/False" →
  "Verdadeiro/Falso".
- **r2** (depois da conferência da interface): rótulos atualizados nas lições 1 e 4 — Research aparece no seletor
  como **"Pesquisa profunda"** (não "Pesquisa aprofundada"); o menu "+" mostra **"Conectores"** (Web, Acadêmico),
  não "Aplicativos e mais"; a caixa de pergunta fica sob o título "O que você quer saber?" com o texto "Pergunte
  qualquer coisa…"; aviso de que a Pesquisa Pro não aparece sem login. Mesmos 423 campos, outro texto em 7 deles.
- Scripts: `05_ARQUIVOS_DE_TRABALHO/perplexity/essentials/scripts_fase_A/` (lições r2 em `licoes_extraidas_PerplexityEssentials_r2/`).
- `validar_estrutura.py`: ESTRUTURA OK nas 8 lições; contagem = edições aplicadas.

## 3. Fase B — inserções

23 blocos novos: 10 HTML, 3 questões nativas, 3 blocos nativos de texto da seção "Sobre este curso" e 7 Continues
(1 livre, na seção nova, + 6 `completeBlock` abaixo dos HTML que travam). Índices abaixo são os finais.

| Lição | Posição final | Tipo | Justificativa didática |
|---|---|---|---|
| 1 | 0–3 | Seção nativa "Sobre este curso": título + parágrafo (objetivo geral, produtos, 129 min, público, pré-requisitos, recursos), lista das 5 competências, destaque 📌 de vigência, Continue | Identificação, objetivo, competências e vigência do roteiro não estavam no curso |
| 1 | 24–25 | HTML "Monte o seu registro de verificação" + Continue travado | O Mão na massa vira ação: escolhas montam o registro (com a data) para copiar; dicas para "sem conta", interface em inglês ou mista |
| 2 | 9 | HTML "Como o motor de respostas monta a resposta" (4 etapas clicáveis + modo "chatbot sem busca") | As quatro etapas e onde a citação falha estavam só em texto |
| 2 | 16 | HTML "Monte sua pergunta pesquisável" (6 elementos, da pergunta vaga à pesquisável, com aviso do que falta) | Pratica a anatomia da pergunta antes das questões |
| 3 | 11–12 | HTML "Semáforo" (8 casos, correção imediata) + Continue travado | Classificar é o objetivo 1 da lição |
| 3 | 16 | Questão nativa: comando oculto numa petição → prompt injection (correta na 2ª) | O objetivo 4 (alucinação × prompt injection) não era verificado |
| 4 | 9 | HTML "Qual nível de busca?" (6 situações) | Pratica a escolha entre busca padrão, Pesquisa Pro e Research, com as cotas |
| 4 | 14 | Questão nativa: restrição de domínios ignorada (correta na 3ª) | O objetivo 3 (verificar se a restrição foi obedecida) não era verificado |
| 5 | 7–8 | HTML "Audite esta citação" (5 casos com o art. 20 da LGPD: sustenta, não sustenta ×2, desatualizada, escopo) + Continue travado | A habilidade central do curso passa a ser praticada |
| 5 | 19–20 | HTML "Ficha de prova de existência" (prompt já preenchido para copiar, campos IA × portal, situação, ponto de controle sob demanda) + Continue travado | A ficha do roteiro vira ferramenta |
| 6 | 13 | Questão nativa: compartilhar Thread com anexo interno (correta na 1ª) | O objetivo 4 (decidir sobre o compartilhamento) não era verificado |
| 6 | 26–27 | HTML "Confira sua síntese citada" (contador de palavras, parágrafos com citação, seção de limites + checklist de 6 critérios) + Continue travado | O critério de êxito vira verificação |
| 7 | 9 | HTML "Qual ferramenta serve melhor?" (6 situações) | A tabela de escolha da ferramenta vira prática |
| 7 | 17–18 | HTML checklist dos 6 critérios da atividade integradora + Continue travado | O roteiro pedia checklist; cada critério aponta a etapa do fluxo |

**O que mudou em relação ao plano**

- O plano não chegou a ser exibido na conversa antes da aprovação (falha minha); foi mostrado em seguida, no início
  da fase B, com a execução já em andamento.
- **Lição 5, ficha**: passou a **trazer o prompt de prova de existência já preenchido**, porque o prompt original fica
  depois de um Continue e o aluno ficaria travado sem acesso a ele.
- **Lição 6, síntese** e **lição 7, critérios**: entraram **depois do último Continue** da lição, e não logo após as
  regras/critérios, porque o exercício e os prompts vêm depois — travar ali impediria o aluno de fazer a atividade.
- Lição 1, registro: entrou depois do Continue existente, para não ficarem dois Continues seguidos.

**Arquivos HTML** (embutidos no JSON, variante inline; nenhuma pasta anexada):
fonte em `05_ARQUIVOS_DE_TRABALHO/perplexity/essentials/perplexity-essentials-blocos/trabalho/html/src/` (CSS em
`comum.css` e funções comuns em `comum.js`, montagem por `build.py`); roteiros em `trabalho/roteiros/` (gerados por
`gerar_roteiros.py`). Todos autocontidos, sem recursos externos, cor do tema `#152f4d`, fontes do sistema,
`aria-live` nos feedbacks, `prefers-reduced-motion`.

## 4. Pendências resolvidas na v2 (a pedido do usuário)

| Pendência da v1 | O que foi feito |
|---|---|
| Trechos da LGPD no "Audite esta citação" | Conferidos no Planalto em 18/10/2026. Caput em vigor e § 1º **idênticos**. A redação de 2018 tinha um erro ("a solicitar *a* revisão, por pessoa natural") → corrigida para "a solicitar revisão, por pessoa natural". Nota do bloco passou a citar a consulta. |
| Descrição da capa ("citações auditadas") | Reescrita: a Perplexity associa as afirmações a citações, e o aluno trata cada citação como ponto de partida da conferência. |
| `matchTitle` do quiz ("Pro Search — modelo mais avançado") | → "Pro Search — busca que encadeia várias pesquisas e combina dezenas de fontes, com cota diária no plano gratuito." |
| "Step 1…5" na linha do tempo da lição 7 | → "Etapa 1…5". |
| "Complete the content above before moving on." | → "Conclua o conteúdo acima para continuar." nos 26 Continues (19 originais + 7 novos). **Confirmado na tela**: o player usa esse texto. |
| Rótulos [conferir] da interface | Conferidos na interface pública, sem login — ver seção 2 (r2) e o ponto 2 da seção 7. |

Como `validar_estrutura.py` e `validar.py` não aceitam mudança nesses campos (capa, `matchTitle`, `date`,
`completeHint`), as edições foram feitas **depois** das inserções por `trabalho/pos_edicoes.py`, que compara o curso
antes e depois folha a folha e só grava se mudaram exclusivamente esses campos (33 folhas: 1 + 1 + 5 + 26).

## 5. Validações

| Etapa | Ferramenta | Resultado |
|---|---|---|
| Fase A r2 | `validar_estrutura.py` | ESTRUTURA OK, 423 campos de texto |
| Ponte r2 | `verificar_scorm.py` no `-REVISADO-r2.zip` | APROVADO, 0 erros, 0 avisos |
| Fase B (inserções sobre r2) | `validar.py` | APROVADO: só inserção, 23 blocos novos seguindo os modelos, 827 IDs únicos |
| Edições extras | `pos_edicoes.py` (checagem própria) | APROVADO: 33 folhas, só nos 4 campos autorizados |
| Pacote v2 | `verificar_scorm.py --original` | APROVADO, 0 erros, 0 avisos; só `runtime-data.js` alterado, nenhum arquivo novo |

## 6. Teste no navegador (mock de LMS da skill, servidor sem cache)

**Visto e funcionando** (v1, e repetido na v2 onde houve mudança):
- Posição dos 23 blocos novos nas lições 1 a 7, conferida pelos IDs renderizados (vizinho anterior e posterior).
- Os 6 HTML que travam (registro, semáforo, auditoria, ficha, síntese, critérios): o Continue abaixo fica travado e o
  resto da lição não carrega; ao concluir a atividade, libera.
- Interações de todos os 10 HTML; questões novas das lições 3, 4 e 6 com feedback.
- **v2:** capa nova; aviso em português no Continue travado; aba de rótulos atualizada (lição 1); a correção da
  LGPD está no pacote (conferida no JSON).
- Quiz: questões 1 (lacuna) e 2 ("Verdadeiro", com o feedback novo) respondidas na v1 e na v2.
- Retomada (v1): ao recarregar sem `reset`, voltou ao quiz e manteve os Continues travados liberados.
- **Celular dentro do player (v2):** com uma cópia do mock com `meta viewport`, a 375 px as lições 1, 5 e 6 não têm
  rolagem horizontal. Os 10 HTML abertos sozinhos a 375 px também não.
- Botões "Copiar": o caminho alternativo funciona (sem permissão da área de transferência, o texto fica selecionado
  com a instrução "use Ctrl+C").
- Console sem erros.

**Não verificado:**
- O quiz **a partir da questão 3** — é uma associação por arrastar, e com a janela do navegador oculta não foi possível
  arrastar. As questões 6 e 17 ("Verdadeiro/Falso") e o novo texto do Pro Search (questão 6) estão no JSON, mas não
  foram vistos na tela.
- O botão "Copiar" com a área de transferência liberada (precisa de clique real com a janela visível).
- Os blocos HTML renderizados **dentro do player** a 375 px (com a janela oculta eles não carregam).
- Abertura por `file://` e comportamento numa LMS real.
- **Pesquisa Pro, Retenção de Dados de IA, Memória, Projetos com conta, limites de arquivos e opções de
  compartilhamento**: exigem login numa conta da Perplexity, e eu não entro em contas.

## 7. Pontos de atenção para revisão humana

1. As frases "geradas" e as páginas do "Audite esta citação" (blog de 2018, artigo sobre a União Europeia) são
   exemplos criados para o exercício; os trechos da lei estão conferidos.
2. **Interface com login**: confira numa conta se a Pesquisa Pro aparece no seletor "Pesquisar", se "Conectores"
   mostra também Finanças/Saúde/Patentes e os caminhos de Configurações (Retenção de Dados de IA, Memória). Sem login,
   o seletor mostra "Pesquisar", "Pesquisa profunda", "Conselho de modelos" (Max) e "Aprender passo a passo"; a
   barra lateral tem também "Automações", "Artefatos" e "Personalizar", que o curso não usa.
3. **Checklists são autodeclarativos** (registro, síntese, critérios). O contador da síntese é aproximado e só
   reconhece citações no formato [1] ou com link.
4. Nenhum gabarito existente parece errado; nenhum foi alterado.

## 8. Entregável

`Onda 1/01_FINALIZADO_subir-na-LMS/perplexity/perplexity-essentials-scorm12-PHjV4LCQ-FINAL-com-blocos-v2.zip`
