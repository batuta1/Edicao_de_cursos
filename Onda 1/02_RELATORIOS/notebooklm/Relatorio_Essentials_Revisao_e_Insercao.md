# Relatório de revisão e inserção — NotebookLM - Essentials

Data: 17–18/10/2026 · Grau de liberdade: moderado (plano completo aprovado, incluindo a seção opcional da lição 1)
Curso **não publicado** com alunos: inserções em qualquer posição.

**Pacote final para a LMS:**
`01_FINALIZADO_subir-na-LMS/notebooklm/notebooklm-essentials-scorm12-eKTseo8Q-FINAL-com-blocos-v2.zip` (cópia idêntica de `05_ARQUIVOS_DE_TRABALHO/notebooklm/essentials/notebooklm-essentials-blocos/saidas/notebooklm-essentials-scorm12-eKTseo8Q-REVISADO-v2.zip`). Atenção: o `-REVISADO.zip` em `03_VERSOES_ANTIGAS/notebooklm/fase-A-so-texto/` é só a fase A, sem os blocos novos.

O `.zip` original do Articulate (`03_VERSOES_ANTIGAS/notebooklm/original-articulate/notebooklm-essentials-scorm12-eKTseo8Q.zip`) não foi modificado.

---

## 1. Material-fonte e mapeamento

Roteiro: `Pesquisa Conteudo Onda 1/Ementa Completa/notebooklm-essentials/roteiros/roteiro-articulate-essentials.md`.

| Lição no Rise (licao = position) | Módulo do roteiro |
|---|---|
| 1 Preparação e Verificação Inicial (0) | Identificação/Objetivo/Competências + Módulo 0 |
| 2 Respostas Ancoradas e Princípios de Verificação (1) | Módulo 1 |
| 3 Segurança, Privacidade e Uso Responsável (2) | Módulo 2 |
| 4 Montagem e Gerenciamento de Fontes no Notebook (3) | Módulo 3 |
| 5 Consultas, Citações e Auditoria de Respostas (4) | Módulo 4 |
| 6 Produção de Artefatos no Estúdio (5) | Módulo 5 |
| 7 Síntese e Aplicação Integrada (6) | Módulo 6 + Encerramento |
| 8 Quiz (7) | avaliação final gerada pelo Articulate |

## 2. Fase A — revisão de texto

Detalhes em `02_RELATORIOS/notebooklm/Relatorio_Essentials_Fase_A_Revisao_de_Texto.md`. Resumo:

- 8 lições editadas, **362 campos de texto** (description 145, feedback 86, paragraph 71, title 44, heading 16).
- Correções de conteúdo importantes: endereços do Kit LGPD restaurados (lição 4); prompts "Mão na massa" das
  lições 5 e 6 restaurados (o Articulate tinha posto a *resposta* no lugar do prompt); "True/False" → "Verdadeiro/Falso"
  no quiz; limite de 500.000 palavras corrigido para "por fonte"; "exclusivamente" → "privilegia" (ancoragem).
- `validar_estrutura.py`: ESTRUTURA OK nas 8 lições; contagem = edições aplicadas.

## 3. Fase B — inserções

20 blocos novos (2 questões nativas, 4 blocos nativos de seção, 9 HTML, 5 Continues `completeBlock`).
Índices abaixo são os finais, na v2.

| Lição | Posição final | Tipo | Justificativa didática |
|---|---|---|---|
| 1 | 0–3 | Seção nativa "Sobre este curso": título + parágrafo (objetivo geral, carga, recursos), lista das 5 competências, destaque ⚠️ de vigência, Continue | Objetivo, competências e nota de vigência do roteiro não apareciam no curso |
| 1 | 19–20 | HTML "Monte o seu registro de verificação" + Continue travado | O Mão na massa virou ação: escolhas montam o registro para copiar; dicas por tipo de conta e idioma |
| 2 | 10 | HTML "Os três painéis e a citação" (esquema clicável) | Painéis e mecânica da citação estavam só em texto |
| 3 | 12–13 | HTML "Semáforo" (7 fontes, correção imediata) + Continue travado | Pratica a classificação verde/amarelo/vermelho antes da questão |
| 3 | 17 | Questão nativa: Leitor × Editor, pessoa × link (correta na 2ª) | Compartilhamento era ensinado e não verificado |
| 4 | 16–17 | HTML checklist do Caderno LGPD (7 itens) + Continue travado | Critério de êxito vira verificação antes de seguir |
| 5 | 4 | HTML "Monte seu pedido ancorado" (5 elementos, mostra o que falta) | Estrutura do pedido saía da regra abstrata |
| 5 | 7–8 | HTML "Audite esta citação" (3 casos total/parcial/ausente, LGPD art. 5º e 11) + Continue travado | A habilidade central do curso passa a ser praticada |
| 6 | 8 | HTML "O que fica onde no Estúdio" (mapa clicável) | Desfaz a confusão "resumo"/Guia de estudo dentro de Relatórios |
| 6 | 14 | Questão nativa: configurar Resumo em Áudio curto em pt-BR (correta na 4ª) | Primeira verificação operacional da lição |
| 7 | 7 | HTML "Qual ferramenta serve melhor?" (6 situações, inclui os cenários a–d) | Os cenários deixam de ser só reflexão |
| 7 | 14–15 | HTML checklist dos 6 critérios de avaliação + Continue travado | O roteiro pedia checklist; o Articulate escondeu os critérios |

**O que mudou em relação ao plano aprovado**

- Lição 1, gerador do registro: entrou **depois** do Continue existente (como etapa própria), e não antes,
  para evitar dois Continues seguidos. O mesmo critério valeu para todos os HTML que travam: cada um tem o seu
  Continue `completeBlock` novo logo abaixo.
- v1 → v2: na seção "Sobre este curso", os `<p></p>` vazios abriam espaços grandes no bloco de texto (o padrão
  só vale dentro de accordion e abas). Removidos na v2; nenhum outro bloco de texto do curso tinha o problema.

**Arquivos HTML** (embutidos no JSON, variante inline; nenhuma pasta anexada):
fonte em `05_ARQUIVOS_DE_TRABALHO/notebooklm/essentials/notebooklm-essentials-blocos/trabalho/html/src/` (CSS comum em `comum.css`, montagem por `build.py`),
roteiros em `trabalho/roteiros/` (gerados por `gerar_roteiros.py`). Todos autocontidos, sem recursos externos,
cor do tema `#152f4d`, fontes do sistema, `aria-live` nos feedbacks.

## 4. Validações

| Etapa | Ferramenta | Resultado |
|---|---|---|
| Fase A | `validar_estrutura.py` | ESTRUTURA OK, 362 campos de texto |
| Ponte | `verificar_scorm.py` no `-REVISADO.zip` | APROVADO, 0 erros, 0 avisos |
| Fase B v1 | `validar.py` / `verificar_scorm.py --original` | APROVADO / APROVADO, 0 erros, 0 avisos |
| Fase B v2 | `validar.py` / `verificar_scorm.py --original` | APROVADO (20 blocos novos, 739 IDs únicos) / APROVADO, 0 erros, 0 avisos; só `runtime-data.js` alterado |

## 5. Teste no navegador (mock de LMS da skill, servidor sem cache)

**Visto e funcionando** (v1; a v2 difere só no parágrafo corrigido, que foi conferido):
- Posição de todos os 20 blocos novos, nas lições 1 a 7, conferida pelos IDs renderizados.
- Seção "Sobre este curso" e seu Continue; espaçamento corrigido na v2.
- Os 5 HTML que travam: Continue aparece com cadeado e "Complete the content above…" e o resto da lição não
  carrega; ao concluir a atividade, libera (registro, semáforo, checklist do Caderno, auditoria, critérios).
- Interações: painéis e citação, mapa do Estúdio, monte seu pedido (inclusive aviso de elemento faltando),
  qual ferramenta, feedback de erro no semáforo e na auditoria.
- Questão nova da lição 3: feedback da alternativa errada e da correta.
- Links do Kit LGPD (fase A): quatro links presentes, abrem em nova aba.
- Retomada: ao recarregar sem `reset`, o curso voltou à última lição e o Continue liberado da lição 1 continuou liberado.
- Celular (375 px): bloco "Monte seu pedido" cabe na largura e fica legível.
- Console sem erros.

**Não verificado:**
- Alternativas **"Verdadeiro/Falso" no quiz final** renderizadas na tela (estão corretas no JSON; não consegui
  avançar o quiz até a questão 11 pela automação).
- Questão nova da lição 6 respondida no navegador (só a posição foi conferida).
- Botões "Copiar" dos HTML (a área de transferência pode ser bloqueada pela LMS; há alternativa de seleção do texto).
- Os outros HTML na largura de celular (só um foi testado); abertura por `file://` (duplo clique); comportamento
  numa LMS real.
- Se o console capturou também os iframes internos.

## 6. Pontos de atenção para revisão humana

1. **Trechos da LGPD no "Audite esta citação"** (art. 5º, I e II; art. 11, caput): transcritos de memória do texto
   compilado — **conferir no Planalto**. As frases "geradas" são exemplos criados para o exercício. O mesmo vale
   para o exemplo do art. 11 no accordion da lição 5.
2. **Esquemas de tela** (painéis na lição 2, mapa do Estúdio na lição 6): ilustrativos, com aviso de que a
   tela real pode variar. Conferir numa conta real se a lista do Estúdio e os nomes batem.
3. **Rótulos [conferir] do roteiro** (adicionar fonte, site/link, Configure Chat, Save to note, visualização da
   conversa, Gerar mais tarde) seguem sem confirmação numa conta real.
4. **Inglês remanescente** que as regras não deixam editar: "Step 1:"… na linha do tempo da lição 7 e o
   aviso "Complete the content above before moving on." dos Continues (inclusive nos 5 novos travados).
5. **Checklists são autodeclarativos**: o participante marca o que diz ter feito; não há verificação real.
6. Nenhum gabarito existente parece errado; nenhum foi alterado.

## 7. Entregável

`Onda 1/NotebookLM/01_FINALIZADO_subir-na-LMS/notebooklm/notebooklm-essentials-scorm12-eKTseo8Q-FINAL-com-blocos-v2.zip`
