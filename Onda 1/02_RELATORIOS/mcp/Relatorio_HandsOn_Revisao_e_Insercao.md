# Relatório — Revisão e Inserção de Blocos — MCP Hands-on

Data: 18/10/2026 · Prompt: `promptRevisaoComInsercaoDeBlocos.md` · Grau de liberdade: moderado · Curso não publicado.

**Pacote para a LMS:** `Onda 1/01_FINALIZADO_subir-na-LMS/mcp/model-context-protocol-mcp-hands-on-scorm12-lBHsLBqU-FINAL-com-blocos-v2.zip`
(SHA-256 começa com `79713f863b51744a`). Antes de publicar, veja a seção 6.

## 1. Material-fonte e mapeamento

- Roteiro: `Pesquisa Conteudo Onda 1/Ementa Completa/mcp-essentials/roteiros/roteiro-articulate-hands-on.md`.
- Original do Articulate: `03_VERSOES_ANTIGAS/mcp/original-articulate/model-context-protocol-mcp-hands-on-scorm12-lBHsLBqU.zip`.
- O Articulate condensou as 8 partes do roteiro em 3 lições: Lição 1 = Antes de Arregaçar as Mangas + Oficina 1;
  Lição 2 = Oficinas 2, 3 e 4; Lição 3 = Projeto Final + A Parte dos Dez + Conseguiu! E agora?

## 2. Fase A — revisão de texto

Detalhe em `Relatorio_HandsOn_Fase_A_Revisao_de_Texto.md`. Resumo:

- O curso veio em PT-BR, mas com textos genéricos, emojis e frases verbatim do roteiro perdidos e conteúdo omitido
  que quebrava a prática — **o principal: o texto dos dois arquivos de teste não existia no curso**, então a
  oficina da pasta e a pegadinha de prompt injection não tinham como acontecer. Restaurado verbatim. Também
  restaurados o passo de `Gmail > Tool permissions`, os 🏁 pontos de controle e o modelo do plano linha a linha.
- **v2 (autorizada pelo usuário):**
  - **Gabarito da Lição 1** (questão do semáforo): a alternativa marcada como correta dizia "Verde para leitura"
    da agenda pessoal; o roteiro diz amarelo. A alternativa A foi reescrita como "Amarelo para ver os seus
    eventos; vermelho para criar na agenda do chefe", com os 4 feedbacks. O campo `correct` não mudou (continua
    na A); por isso o validador da skill passou sem invólucro.
  - **Rótulos da interface em PT-BR**: os mesmos 174 rótulos traduzidos no Essentials v3 (o `labelSet` em inglês
    é idêntico nos dois cursos), `iso639Code` `pt-BR`. Feito por `criar_base_v2.py`, que confere que só o
    `labelSet` mudou.
- **254 campos alterados** (245 da v1 + 9 da questão). `validar_estrutura.py`: estrutura preservada.
- Pacote da fase A: `03_VERSOES_ANTIGAS/mcp/fase-A-so-texto/…-REVISADO-v2.zip`. Ponte `verificar_scorm.py`: **APROVADO**.

## 3. Fase B — inserções

20 blocos novos, conforme o plano aprovado (`Plano_Insercoes_HandsOn.md`), sem mudanças de conteúdo:
6 HTML, 4 seções "🚀 Quer ir além?" (título + accordion), 2 seções com lista numerada (título + lista),
2 Continues `completeBlock`. Índices abaixo são os **finais**.

| Lição | Posição final | Tipo | Justificativa didática |
|---|---|---|---|
| 1 | 3 | HTML "O mapa da mão na massa" (7 partes, problema, tempo, lição; total 117 min) | O mapa do roteiro tinha sumido; mostra a escada consultar → ler → agir |
| 1 | 11–12 | HTML "Dê a cor" (6 usos para classificar, correção imediata) + Continue travado | O semáforo é o critério do curso inteiro e só tinha uma questão |
| 1 | 18–19 | Título + lista "Variação no ChatGPT (opcional)", 4 passos | Omitida pelo Articulate |
| 1 | 23–24 | "🚀 Quer ir além?" — 3 desafios com validação | Omitido |
| 2 | 6–7 | Título + lista "Sem Claude Desktop? Caminho pelo Google Drive", 4 passos | O curso prometia esse caminho e não o trazia |
| 2 | 12–13 | "🚀 Quer ir além?" (pasta) | Omitido |
| 2 | 17 | HTML "Configure as Tool permissions" (simulação, 5 ferramentas genéricas) | Treina a decisão leitura × escrita, avisa quando a escrita fica em Always allow |
| 2 | 21–22 | "🚀 Quer ir além?" (agenda) | Omitido |
| 2 | 26–27 | "🚀 Quer ir além?" (ação), com "faça antes da Parte C" | Omitido |
| 2 | 30–31 | HTML checklist "Preparar, revisar, conferir, desfazer" (8 itens) + Continue travado | A oficina mais arriscada passa a exigir a conferência e o desligamento |
| 3 | 6 | HTML "Monte seu plano de conexão segura" (15 campos → plano no formato do modelo, alertas do semáforo, botão copiar) | O modelo vira texto pronto e o semáforo é conferido na hora |
| 3 | 10 | HTML checklist "Faxina final" (5 itens, sem trava) | A faxina era só um parágrafo |

**Mudança em relação ao plano aprovado:** nenhuma de conteúdo. Ajustes de forma: (a) o HTML de permissões
fica depois do Process da agenda, então o texto dele diz "compare com o que você deixou na tela real" em vez de
"ensaie antes"; (b) a v2 da fase B corrige o layout do mapa (as etiquetas "PREPARAR" e "CONSULTAR" estouravam a
coluna de 74 px; agora 92 px e fonte 10,5 px).

**Arquivos:** HTML embutidos (variante inline; nenhuma pasta anexada). Fontes em
`05_ARQUIVOS_DE_TRABALHO/mcp/hands-on/mcp-hands-on-blocos/trabalho/html/src/` (CSS comum = o mesmo do Essentials;
montagem por `build.py`); roteiros gerados por `trabalho/gerar_roteiros.py`, aplicados em cadeia
(`trabalho/etapas_v2/`) até `trabalho/curso_v2.json`.

## 4. Validações

| Etapa | Resultado |
|---|---|
| Fase A v2 — `validar_estrutura.py` | Estrutura preservada; 254 campos de texto |
| Ponte — `verificar_scorm.py REVISADO-v2.zip --original <Articulate>` | APROVADO, 0 erros, 0 avisos |
| Fase B v2 — `validar.py curso_v2.json --original curso_original.json` | APROVADO: só inserção, 20 blocos novos dentro dos modelos, 361 IDs únicos |
| Fase B v2 — `verificar_scorm.py FINAL-v2.zip --original REVISADO-v2.zip` | APROVADO, 0 erros, 0 avisos; só `runtime-data.js` mudou |
| Final — `verificar_scorm.py FINAL-v2.zip --original <Articulate>` | APROVADO, 0 erros, 0 avisos |

(A v1 da fase B passou pelas mesmas três validações, todas APROVADAS.)

## 5. Navegador (mock de LMS da skill, `http://localhost`)

**Visto (na v1, que tem os mesmos blocos e textos; a v2 só muda o CSS do mapa):**
- Capa com "INICIAR CURSO"; página do curso com `lang="pt-BR"`.
- As 3 lições abertas até o fim, com a lista de blocos conferida: Lição 1 com 27 blocos, Lição 2 com 32, Lição 3
  com 16 — todos os novos na posição planejada.
- "Dê a cor": uma resposta errada mostra "Ainda não…"; com as seis certas, aparece a mensagem final e o Continue
  passa de "Complete the content above before moving on." para "Continue".
- Questão corrigida da Lição 1: a alternativa "Amarelo… vermelho…" é corrigida como certa, com o feedback novo.
- Simulador de permissões: escrita em Always allow é apontada como erro; leitura em Blocked dá aviso; a
  configuração segura dá a mensagem de acerto.
- Checklist do ritual (8 itens) libera o Continue travado da Lição 2.
- Gerador do plano: os campos montam o plano no formato do modelo; conta do trabalho/dados de terceiros com cor
  amarelo dispara o alerta de vermelho.
- Faxina: os 5 itens marcados mostram a mensagem final.
- Accordion de desafios abre.
- Retomada: recarregando sem `reset`, o curso volta à Lição 3 (bookmark) e a Lição 1 reabre inteira, sem trava.
- Console sem erros.
- Capturas de tela: mapa, "Dê a cor", simulador de permissões e faxina, no computador.
- Os 6 HTML abertos sozinhos em 375 px: nenhum tem rolagem horizontal; mapa (v2), plano e permissões vistos em captura.

**v2:** conferido no curso que o mapa usa a coluna de 92 px e nenhuma etiqueta estoura; console sem erros.

**Não verificado:**
- Curso inteiro em largura de celular dentro do player (o mock de LMS não se adapta à emulação de celular; só os
  HTML foram testados sozinhos).
- Botão "Copiar o plano" no iframe do Rise: a área de transferência pode ser bloqueada pela sandbox; nesse caso o
  HTML seleciona o texto e pede Ctrl+C. Nenhum dos dois caminhos foi conferido no navegador.
- Questões da Lição 2 e 3 não foram respondidas no navegador (só vistas na posição); flashcards e Process não
  foram percorridos.
- Envio de nota ao LMS (o curso não tem quiz final) e LMS real (só o mock).

## 6. Pontos de atenção para revisão humana

1. **HTML são rascunho para revisão:** o simulador de permissões usa nomes de ferramenta genéricos e diz isso na
   tela; os 6 usos de "Dê a cor" vêm do roteiro (os 3 do treino + OpenAI Docs, pasta fictícia e e-mail de
   clientes, que seguem a tabela do semáforo).
2. **Classificação "conta do trabalho, com autorização"** no gerador do plano: o HTML trata como vermelho (o
   roteiro diz que conta do trabalho não liga sem autorização — a autorização muda a decisão, não a cor). Vale
   confirmar se é essa a leitura da equipe.
3. **[conferir] do roteiro continuam no texto:** macOS 13, `Add custom connector`, rótulos de Settings >
   Extensions, tela da pasta, rótulo para desativar a Filesystem e caminho de revogação na Conta Google. Os
   checklists repetem esses avisos ("a conferir").
4. **Botão Continue em inglês** ("Continue" e "Complete the content above before moving on."): esses textos estão
   em cada bloco Continue, e a skill exige o padrão nos blocos novos. Igual ao Essentials e ao NotebookLM.
5. **Tradução dos rótulos é nossa**, não a oficial do Articulate (a mesma do Essentials v3).
6. **Títulos das lições** foram mantidos como o Articulate gerou (não seguem os nomes das oficinas).

## 7. Onde está cada coisa

| O quê | Onde |
|---|---|
| `.zip` para a LMS | `01_FINALIZADO_subir-na-LMS/mcp/…-hands-on-…-FINAL-com-blocos-v2.zip` |
| Original do Articulate | `03_VERSOES_ANTIGAS/mcp/original-articulate/` |
| Só texto (fase A, v1 e v2) | `03_VERSOES_ANTIGAS/mcp/fase-A-so-texto/` |
| Versão anterior com blocos | `03_VERSOES_ANTIGAS/mcp/fase-B-v1/` |
| Relatórios e plano | `02_RELATORIOS/mcp/` (`Relatorio_HandsOn_…`, `Plano_Insercoes_HandsOn.md`) |
| Material de trabalho (JSONs, lições, mapas de texto, HTML, roteiros, teste) | `05_ARQUIVOS_DE_TRABALHO/mcp/hands-on/` |
