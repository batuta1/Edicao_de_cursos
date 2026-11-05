# Relatório de edição — Perplexity - Essentials (fase A: revisão de texto)

Data: 18/10/2026 · Pacote de entrada: `perplexity-essentials-scorm12-PHjV4LCQ.zip` (não modificado; hoje em `03_VERSOES_ANTIGAS/perplexity/original-articulate/`)
Saída: `perplexity-essentials-scorm12-PHjV4LCQ-REVISADO.zip` (hoje em `03_VERSOES_ANTIGAS/perplexity/fase-A-so-texto/`; versão intermediária, sem os blocos novos da fase B)

> **Atualização (r2, 18/10/2026):** depois de conferir a interface pública de perplexity.ai (sem login), 7 textos das
> lições 1 e 4 foram atualizados no próprio `edicoes.py` e a fase A foi refeita do zero
> (`licoes_extraidas_PerplexityEssentials_r2/`, `-REVISADO-r2.zip`): Research = "Pesquisa profunda" no seletor; menu
> "+" com "Conectores" (Web, Acadêmico) em vez de "Aplicativos e mais"; caixa de pergunta sob o título "O que você
> quer saber?", com "Pergunte qualquer coisa…"; aviso de que a Pesquisa Pro não aparece sem login. Mesmos 423 campos;
> ESTRUTURA OK; ponte APROVADA. Os pontos de atenção 1 e 2 abaixo foram resolvidos na v2 do pacote final — ver o
> relatório completo.

## Material-fonte e mapeamento

Fonte principal: `Pesquisa Conteudo Onda 1/Ementa Completa/perplexity-essentials/roteiros/roteiro-articulate-essentials.md`.

| Lição no Rise (position) | Módulo do roteiro |
|---|---|
| 01 Preparação e Verificação Inicial (0) | Módulo 0 |
| 02 Entendendo o Motor de Respostas com Citações (1) | Módulo 1 |
| 03 Segurança, Privacidade e Responsabilidade Profissional (2) | Módulo 2 |
| 04 Formulando Perguntas e Escolhendo a Profundidade da Busca (3) | Módulo 3 |
| 05 Conferindo Citações e Comparando Fontes (4) | Módulo 4 |
| 06 Organizando a Pesquisa e Produzindo a Síntese Citada (5) | Módulo 5 |
| 07 Síntese e Aplicação Integrada (6) | Módulo 6 + Encerramento |
| 08 Quiz (7) | avaliação final gerada pelo Articulate (sem correspondente direto no roteiro) |

Identificação, Objetivo Geral, Competências e a nota de vigência 📌 do roteiro **não aparecem no curso** — não há
bloco onde caibam; ficam como candidatas da fase B.

## Critério aplicado

`promptRevisaoPorClaude.md` + `promptRevisaoComInsercaoDeBlocos.md` + skill `revisar-curso-scorm`. Só campos
textuais; nenhum id, tipo, posição, setting, item ou gabarito alterado. Edições feitas por script campo a campo
(`05_ARQUIVOS_DE_TRABALHO/perplexity/essentials/scripts_fase_A/edicoes.py` + `aplicar.py`), que confere que cada
caminho existe e já é texto antes de trocar.

## Arquivos editados

Todos os 8 `licao_*.json` de `licoes_extraidas_PerplexityEssentials/`.

## Problemas encontrados no original

1. **Lição 04, bloco 18 ("Mão na massa")**: no lugar do prompt-base havia uma *resposta* gerada pelo Articulate, com
   citação de uma página da ANPD "publicada em 23/08/2022" e trecho entre aspas que não estão no roteiro (não
   verificados). O exercício mandava enviar um prompt que não existia na tela. **Restaurado o prompt do roteiro.**
2. **Lição 05, blocos 19 e 20**: o bloco 19 continha só "Sem apoio suficiente." (o prompt de autoauditoria tinha
   sumido) e o bloco 20 trazia uma resposta com quatro links `href="NÃO ENCONTRADO"` (quebrados) no lugar do prompt
   de prova de existência. **Restaurados os dois prompts.**
3. **Lição 02, bloco 18**: anunciava "o modelo apresentado a seguir", mas o prompt-base não existia em lugar nenhum.
   **Restaurado.**
4. **Objetivos desalinhados**: lição 06 (lista não correspondia ao roteiro) e lição 07 (quatro itens genéricos).
   Alinhados ao roteiro; na 07, o objetivo 3 do roteiro foi dividido em dois itens para manter a quantidade.
5. **Afirmações sem fonte ou erradas**, corrigidas: Pesquisa Pro "usa modelos mais avançados" (lição 01; o roteiro
   diz que encadeia buscas e combina dezenas de fontes); "use navegadores diferentes e horários distintos" (lição
   05); retenção "excluídos automaticamente, sem garantia de recuperação" (lição 06); limitações inventadas de
   base especializada ("exige assinatura") e Deep Research ("exige conhecimento avançado") (lição 07); "Para a
   maioria dos usuários iniciantes, o limite não é um obstáculo" (lição 01).
6. **Quiz**: a alternativa correta da questão 5 dizia "citações *auditadas* vinculadas à resposta" — a ferramenta
   não audita citações; virou "números de citação vinculados às afirmações" (mesmo id, gabarito intacto). A
   alternativa "Nova pesquisa no mesmo Thread" (contraditória) virou "Iniciar uma nova pesquisa".

## Alterações por lição

Padrões em todas as lições: fórmula única de objetivos ("Ao final desta lição, você será capaz de:"); aberturas
genéricas trocadas pelo conteúdo do roteiro (pré-filtro, analogia do resumo com post-its, tema-âncora art. 20);
fechamentos "Próximo passo: …" concretos; convites "Clique em cada cartão / aba / item"; feedbacks padronizados
"Correto." / "Não." + porquê; breadcrumbs 🧭 e pontos de controle 🏁 restaurados; process com título e tempo da
atividade no início e critério de êxito no resumo; accordions de solução de problemas em "Causa provável / O que
fazer"; referências a "Módulo N" trocadas pelo nome da lição (o aluno não vê a numeração dos módulos).

- **01** — tabela de planos pagos restaurada no accordion (preços em US$, ressalva de reais/lojas/operadoras);
  rótulos de 18/10/2026 (Pesquisar, Computer, +, Projetos, Recentes); tabela de equivalência completada (Best,
  Aplicativos e mais, Sua Biblioteca, Spaces, Computer fora do escopo); "Histórico" → "Recentes"; process
  "Verificação de acesso (7 min)" com breadcrumbs e critério de êxito.
- **02** — fundadores, as quatro etapas com geração aumentada por recuperação, Tow Center/El País (25/04/2025, menor
  taxa entre oito ferramentas, 37%), JMLA 2026 e o fluxo "pistas → confirma → conclui"; accordion comparativo no
  formato ferramenta a ferramenta; abas vaga × pesquisável comentando os elementos; questões com fundamentação.
- **03** — política de privacidade (17/10/2026) detalhada; controles com breadcrumbs e o caso Enterprise; riscos
  de conteúdo e de compartilhamento (teste em janela privada); semáforo em "Exemplos / Pode entrar?"; casos TJPR,
  STJ, TSE e Mata v. Avianca com números, datas e sanções; OAB item 3.7; escopo da Resolução CNJ 615/2025;
  prompt injection com ARE 1.608.713 e AP 2.822; questão 1 voltou ao cenário do roteiro (assessora jurídica).
- **04** — tabela dos três níveis no accordion (rótulo, uso, cota); Aplicativos e mais + seletor "Modelo";
  operadores site:/AND/OR sem suporte; process "Mesma pergunta, dois níveis (6 min)" com variação sem Pesquisa
  Pro, critério de êxito e conhecimento de controle (art. 20, caput).
- **05** — as seis perguntas da conferência; tipos de fonte; quatro falhas com "Como agir"; checklist de 7 pontos
  para decisões; caminhos STF/STJ/CNJ com links (nova aba); process com o link oficial do acórdão TJPR e o ponto
  de controle (7ª Câmara Cível, rel. Fabian Schweitzer, 01/06/2026).
- **06** — Projetos/Recentes/Spaces com breadcrumbs; anexos (25 MB/4 arquivos/30 dias marcados como "ajuda antiga,
  não reconfirmado"); compartilhamento e Pages; quatro regras da síntese; ficha de auditoria com a coluna "Existe?"
  que faltava; process com link do texto compilado e ponto de controle; prompts sem aspas simples trocadas.
- **07** — linha do tempo ligada às lições; ferramentas sem as limitações inventadas; os quatro cenários (a)–(d)
  em "a Perplexity ajuda / a fonte primária entra"; critérios de avaliação verbatim; dicas dos prompts por perfil
  trocadas por orientação de conferência; encerramento sem fecho motivacional.
- **08 (Quiz)** — "True/False" → "Verdadeiro/Falso" (blocos 1, 6, 17); feedbacks reescritos sem metalinguagem
  ("Essa alternativa é convincente porque…", "testa se o aluno…"); descrição do quiz; enunciados dos MATCHING.
  Respostas aceitas dos FILL_IN_THE_BLANK e `matchTitle` intactos.

## Contagem e validação

- Campos alterados: **423** (aplicados pelo script = contados pelo validador). Por campo: description 163,
  paragraph 88, feedback 78, title 64, heading 30. Por lição: 50, 41, 47, 46, 57, 65, 50, 67.
- `validar_estrutura.py`: **ESTRUTURA OK** nas 8 lições.
- `scorm_reempacotar.py`: round-trip do Base64 conferido; 84 arquivos, 0 alterados fora de `runtime-data.js`.
- `verificar_scorm.py` (skill de inserção): **APROVADO**, 0 erros, 0 avisos (8 lições, 172 blocos, 742 IDs únicos).

## Pontos de atenção (revisão humana)

1. **Texto que as regras não deixam editar** (campos não textuais para o validador):
   - `matchTitle` da questão de associação de rótulos (quiz, bloco 5): "Pro Search — opção de busca com **modelo
     mais avançado**…" — impreciso; pelo roteiro, a Pesquisa Pro encadeia várias buscas e combina dezenas de fontes.
   - `date` da linha do tempo da lição 07 ("Step 1"… "Step 5") e `completeHint` dos Continues ("Complete the
     content above before moving on.").
2. **Rótulos marcados [conferir] no roteiro**, mantidos sem a marca no texto do aluno: "Pesquisa Pro" na tela e o
   seletor junto à caixa; "Research"/"Pesquisa aprofundada"; caminho e disponibilidade da Retenção de Dados de IA no
   plano gratuito; caminho da Memória; Projetos/Recentes na barra lateral; "Aplicativos e mais" com login; criação
   e limites de Projeto no gratuito; limites de arquivos; opções de visibilidade de "Compartilhar"; caminho para
   trocar o idioma. Conferir numa conta real antes de publicar.
3. Dados factuais vindos só do roteiro e não reconferidos por mim (processos, datas, preços, estudo JMLA, teste do
   Tow Center): estão como no roteiro.
4. Gabaritos: nenhum parece errado. Nenhum foi alterado.

## Não verificado

O curso revisado **ainda não foi aberto no navegador** — fica para a fase B (mock de LMS), junto com os blocos
novos. Em especial: renderização dos prompts com `<br>` (lição 02), da lista numerada dentro do parágrafo (lição
05, bloco 12) e dos links novos (lições 05 e 06).
