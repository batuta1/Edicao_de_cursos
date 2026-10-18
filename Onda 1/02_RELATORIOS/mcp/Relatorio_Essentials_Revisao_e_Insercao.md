# Relatório — Revisão e Inserção de Blocos — MCP Essentials

Data: 18/10/2026 · Prompt: `promptRevisaoComInsercaoDeBlocos.md` · Grau de liberdade: moderado · Curso não publicado.

**Pacote para a LMS:** `Onda 1/01_FINALIZADO_subir-na-LMS/mcp/model-context-protocol-mcp-essentials-scorm12-MYCD1EGZ-FINAL-com-blocos-v3.zip`
(SHA-256 começa com `f8dcc4109ba80541`). Antes de publicar, veja a seção 6.

## v3 (18/10/2026) — pendências resolvidas

Pedido do usuário: "faça os pendentes". A v3 parte da v2 e muda três coisas:

1. **Gabarito da Lição 7 (questão da agenda pessoal)**: a correta passou de "Verde; acesso somente leitura à
   agenda" (1ª) para a 4ª alternativa, reescrita como "Amarelo; leitura liberada e escrita em Needs approval" —
   coerente com o roteiro e com o HTML "Síntese da decisão". Feedbacks da 1ª e da 4ª reescritos. Feito por
   `corrigir_gabarito_l7.py`, que confere o estado anterior antes de trocar.
2. **Lacunas do quiz mais robustas.** No código do player, a correção apara espaços e ignora maiúsculas, mas
   exige o texto exato (acentos, travessão). Por isso: questão 19 virou "preparar, revisar, ____ e desfazer"
   (aceita "conferir" e "verificar"); questão 21 virou "Windows ____ ou posterior" (aceita "10"); questão 22
   ("login") ficou como estava.
3. **Rótulos da interface em PT-BR**: 174 dos 456 rótulos do `labelSet` — todos os que este curso exibe (capa,
   navegação, lições, quiz, process, flashcards, verificações, progresso, busca, carregamento e acessibilidade).
   Os demais são de recursos que o curso não usa (Tutor de IA, vídeo, cenários de IA, pesquisas) e ficaram em
   inglês. `iso639Code` passou de `en` para `pt-BR`: o player usa esse código no `lang` da página, então leitores
   de tela agora leem o curso em português. Feito por `criar_base_v3.py`, que confere mesmas chaves, `%`
   preservado e nenhuma mudança fora do `labelSet`.

**Validações:** `validar_estrutura_autorizado_v3.py` (invólucro que, além dos 3 campos da v2, aceita só a troca
de `correct` em `lesson.items[13].items[0].answers[0|3]`): estrutura preservada, 680 campos. Ponte: APROVADO.
`validar.py` (30 blocos novos, 773 IDs únicos): APROVADO. `verificar_scorm.py` contra a fase A v3 e contra o
original do Articulate: APROVADO, 0 erros, 0 avisos.

**Navegador (v3):** capa com "INICIAR CURSO" e `lang="pt-BR"`; na Lição 7, "Verde" agora é corrigida como
incorreta e a 4ª alternativa como correta, com os feedbacks novos; **quiz inteiro respondido** (22 questões):
associações 3 e 5 corrigidas como certas com os textos traduzidos; lacunas aceitas digitadas como "Conferir",
" 10 " e "Login" (maiúscula e espaços); tela de resultado em PT ("Resultado do quiz", "NOTA MÍNIMA",
"Reprovado", "REFAZER" — a nota de 32% é proposital: respondi a 1ª alternativa das demais); console sem erros.

**Limite que fica:** o botão Continue continua "Continue" e o aviso de trava "Complete the content above before
moving on.": esses textos estão gravados em cada bloco Continue (não nos rótulos), e a skill de inserção exige
os valores padrão nos blocos novos. Igual ao NotebookLM.

## v2 (18/10/2026) — o que mudou em relação à v1

Com autorização do usuário, a v2 traduz os **18 campos do quiz** que tinham ficado em inglês (`matchTitle` das
associações 3 e 5; `feedbackCorrect`/`feedbackIncorrect` das associações e das lacunas 19, 21 e 22) e a
**descrição da capa** (`course.description`).

- Fase A refeita: os 18 campos aplicados a partir de `revisao_textos/L08_pendente_autorizacao.json`; a capa
  entrou numa base nova (`cursoMCPEssentials_base_v2.json`, gerada por `criar_base_capa.py`, que confere que a
  única diferença para o original é `course.description`).
- Validação com `validar_estrutura_autorizado.py`: um invólucro do validador da skill que acrescenta **só**
  esses três campos à lista de texto (a skill não foi alterada). Estrutura preservada; **677 campos** (659 + 18).
- Ponte `verificar_scorm.py REVISADO-v2.zip`: APROVADO, 0 erros, 0 avisos.
- Fase B: as mesmas 21 inserções reaplicadas sobre a nova base (`trabalho/etapas_v2/` → `curso_v2.json`).
  `validar.py`: APROVADO, 30 blocos novos, 773 IDs únicos. `verificar_scorm.py` contra a fase A v2 e contra o
  original do Articulate: APROVADO, 0 erros, 0 avisos.
- Navegador (v2): capa em PT-BR; as 8 opções das associações em PT, sem texto em inglês no quiz; Lição 3 com
  o HTML e a trava no mesmo ponto; console sem erros. Os demais testes da seção 5 foram feitos na v1, que tem os
  mesmos blocos.
- A v1 foi para `03_VERSOES_ANTIGAS/mcp/fase-B-v1/`.

## 1. Material-fonte e mapeamento

- Roteiro: `Pesquisa Conteudo Onda 1/Ementa Completa/mcp-essentials/roteiros/roteiro-articulate-essentials.md`.
- Original do Articulate: `03_VERSOES_ANTIGAS/mcp/original-articulate/model-context-protocol-mcp-essentials-scorm12-MYCD1EGZ.zip`.
- Mapeamento 1:1: lição 1 = Módulo 0 … lição 7 = Módulo 6 (+ Encerramento); lição 8 = Quiz.

## 2. Fase A — revisão de texto

Detalhe completo em `Relatorio_Essentials_Fase_A_Revisao_de_Texto.md`. Resumo:

- O curso veio **quase todo em inglês**; foi traduzido e reescrito em PT-BR a partir do roteiro, com os
  rótulos de interface em inglês, como o roteiro manda.
- Conteúdo restaurado: prompt-base da Lição 2 (o Articulate pôs a resposta esperada no lugar), pontos de
  controle 🏁 e critérios de êxito nos Process, objetivos alinhados ao plano e Encerramento do roteiro no
  lugar do fechamento motivacional.
- **659 campos alterados** em 8 lições. `validar_estrutura.py`: estrutura preservada. A primeira rodada
  reprovou 18 campos do quiz (ver 6.2), que foram desfeitos.
- Pacote da fase A: `03_VERSOES_ANTIGAS/mcp/fase-A-so-texto/…-REVISADO.zip`. Ponte `verificar_scorm.py`: **APROVADO**.

## 3. Fase B — inserções

30 blocos novos: 8 HTML, 4 questões nativas, 1 seção nativa (título + lista), 3 parágrafos/títulos, 1 bloco de
abas, 9 Continues livres e 4 Continues `completeBlock`. Índices abaixo são os **finais**, na v1.

| Lição | Posição final | Tipo | Justificativa didática |
|---|---|---|---|
| 1 | 0–2 | Seção "Sobre este curso": título + parágrafo (objetivo geral, 129 min, público), lista das 5 competências, Continue | Objetivo geral e competências do roteiro não apareciam |
| 1 | 8 | Continue | Separa a abertura da verificação (o curso tinha 1 Continue no total) |
| 1 | 17 | HTML "Monte o seu registro de verificação" | O modelo estático vira ação; cada escolha gera o aviso do que fazer (vaga ocupada, sem Desktop, ChatGPT sem opção) |
| 2 | 3 | Continue | Abre a lição em seções |
| 2 | 5 | HTML infográfico "N × M" (sem padrão × com o MCP) | O problema que o MCP resolve estava só em texto |
| 2 | 17 | Parágrafo "Exemplos no Brasil" (Senior, Econodata, conectores interativos) | Exemplos do roteiro omitidos pelo Articulate |
| 2 | 20 | Questão: servidor local (correta na 2ª) | O critério "duas respostas corretas" tinha uma questão só |
| 3 | 3 | Continue | Abre a lição em seções |
| 3 | 12–13 | HTML "Avalie a ficha antes de instalar" (3 conectores fictícios) + Continue travado | O objetivo "avaliar a ficha" não tinha prática |
| 3 | 19–21 | Questões: Cenários B (vermelho), C (amarelo), D (vermelho) | O critério "quatro classificações" tinha só o Cenário A |
| 4 | 4 e 9 | 2 Continues | Separam preparação, prática e conferência |
| 4 | 12 | HTML "Dá para confiar nesta resposta?" (4 respostas simuladas) | Pratica a conferência pela chamada de ferramenta e pelo domínio |
| 5 | 3 | Continue | Abre a lição em seções |
| 5 | 6–7 | Parágrafo "Compare os dois caminhos, lado a lado:" + abas Local × Remoto | O roteiro pedia comparação em duas colunas |
| 5 | 11–12 | HTML "Arquivo ou ordem?" (achar a instrução maliciosa e responder Allow/Deny) + Continue travado | Ensaia a recusa antes do exercício real |
| 6 | 3 | Continue | Abre a lição em seções |
| 6 | 12–13 | HTML "Revise antes do Allow" (4 solicitações simuladas, 3 com erro) + Continue travado | Pratica o tempo "Revisar" |
| 7 | 3 | Continue | Abre a lição em seções |
| 7 | 8 | HTML "Síntese da decisão" (necessidade → caminho, permissões, semáforo) | A tabela do roteiro estava espremida numa aba |
| 7 | 15–16 | HTML checklist "Devolva os acessos do curso" (6 itens) + Continue travado | Devolver o crachá vira ação conferida |

**O que mudou em relação ao plano aprovado**

- Lição 5, abas: antes delas entrou um parágrafo curto de anúncio ("Compare os dois caminhos, lado a lado:"),
  porque nos nossos cursos abas vêm sempre precedidas de um texto terminado em dois-pontos.
- Lição 4, HTML "Dá para confiar…": sem Continue travado, como no plano (só avisa a conclusão).
- Nenhum tipo de bloco não testado foi usado.

**Arquivos:** HTML embutidos (variante inline; nenhuma pasta anexada). Fontes em
`05_ARQUIVOS_DE_TRABALHO/mcp/essentials/mcp-essentials-blocos/trabalho/html/src/` (CSS comum = o mesmo do
NotebookLM; montagem por `build.py`); roteiros gerados por `trabalho/gerar_roteiros.py`, aplicados em cadeia
(`trabalho/etapas/`) até `trabalho/curso_v1.json`.

## 4. Validações

| Etapa | Resultado |
|---|---|
| Fase A — `validar_estrutura.py` | Estrutura preservada; 659 campos de texto |
| Ponte — `verificar_scorm.py REVISADO.zip --original <Articulate>` | APROVADO, 0 erros, 0 avisos |
| Fase B — `validar.py curso_v1.json --original curso_original.json` | APROVADO: só inserção, 30 blocos novos dentro dos modelos, 773 IDs únicos, 0 avisos |
| Fase B — `verificar_scorm.py FINAL-v1.zip --original REVISADO.zip` | APROVADO, 0 erros, 0 avisos; só `runtime-data.js` mudou |
| Final — `verificar_scorm.py FINAL-v1.zip --original <Articulate>` | APROVADO, 0 erros, 0 avisos |

## 5. Navegador (mock de LMS da skill, `http://localhost`)

**Visto:**
- As 7 lições abertas até o fim: todos os blocos novos na posição planejada, com títulos e textos revisados
  em PT-BR (incluindo a barra lateral).
- Os 8 HTML carregam e respondem: registro monta o texto e os avisos; N × M alterna as vistas; ficha, confiança,
  arquivo ou ordem e revise dão feedback de erro e de acerto; síntese mostra o caso escolhido; checklist marca.
- As 4 travas: o Continue aparece com "Complete the content above before moving on." e libera depois da
  atividade (lições 3, 5, 6 e 7).
- Questão nova da Lição 2: resposta correta marcada como correta, com o feedback em PT.
- Console sem erros.
- Retomada: recarregando sem `reset`, o curso volta à última lição (bookmark) e a Lição 3 reabre inteira, sem
  trava, com a atividade já concluída.
- Aparência dos HTML conferida por captura de tela no registro, no N × M e na ficha.

**Não verificado:**
- ~~Quiz e lacunas~~ — testados na v3 (ver acima).
- Envio de nota ao LMS: o mock mostrou "nota: -" depois de uma tentativa reprovada; uma tentativa aprovada não foi testada.
- As 3 questões de cenário da Lição 3 não foram respondidas no navegador (só vistas na posição).
- Aparência em celular e captura de tela dos HTML das lições 4 a 7.
- LMS real (só o mock).

## 6. Pontos de atenção para revisão humana

1. ~~Gabarito suspeito da Lição 7~~ — **corrigido na v3** (correta: "Amarelo; leitura liberada e escrita em Needs approval").
2. ~~18 campos do quiz em inglês~~ — **resolvido na v2.**
3. ~~Descrição da capa em inglês~~ — **resolvido na v2.**
4. ~~Rótulos de navegação em inglês~~ — **traduzidos na v3**, exceto o botão "Continue" e o aviso de trava
   (ver "Limite que fica").
5. **HTML são rascunho para revisão:** conectores e respostas da Lição 3 e da Lição 4 são fictícios e estão
   marcados como tal; a solicitação de aprovação da Lição 6 é simulada e avisa que a tela real é outra. Nenhum
   nome de menu foi inventado além dos do roteiro.
6. **[conferir] do roteiro continuam no texto:** macOS 13, `Add custom connector`, rótulos de Settings >
   Extensions, rótulo para desativar a Filesystem e caminho de revogação na Conta Google. O HTML do registro e o
   checklist repetem esses avisos ("a conferir").
7. ~~Lacunas do quiz~~ — **simplificadas e testadas na v3.**
8. **Tradução dos rótulos é nossa**, não a oficial do Articulate: se a equipe tiver o conjunto PT-BR oficial do
   Rise, vale comparar.

## 7. Onde está cada coisa

| O quê | Onde |
|---|---|
| `.zip` para a LMS | `01_FINALIZADO_subir-na-LMS/mcp/…-FINAL-com-blocos-v3.zip` |
| Original do Articulate | `03_VERSOES_ANTIGAS/mcp/original-articulate/` |
| Só texto (fase A, v1 a v3) | `03_VERSOES_ANTIGAS/mcp/fase-A-so-texto/` |
| Versões anteriores com blocos | `03_VERSOES_ANTIGAS/mcp/fase-B-v1/` e `fase-B-v2/` |
| Relatórios e plano | `02_RELATORIOS/mcp/` |
| Material de trabalho (JSONs, lições, mapas de texto, HTML, roteiros, teste) | `05_ARQUIVOS_DE_TRABALHO/mcp/essentials/` |
