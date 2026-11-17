# Relatório — Gemini Chat - Essentials (revisão de texto + inserção de blocos)

**Data:** 17/11/2026 (v1) · **Pacote final:** `Onda 2/01_FINALIZADO_subir-na-LMS/gemini-chat/gemini-chat-essentials-scorm12-Wt2012XL-FINAL-com-blocos-v1.zip`

## 1. Material-fonte e mapeamento

Fonte: `Pesquisa Conteudo Onda 2/Ementa Completa/gemini-chat-essentials/roteiros/roteiro-articulate-essentials.md`.
Mapeamento 1:1: L1–L7 = Módulos 0–6; L8 = Quiz gerado pelo Articulate (21 questões). O encerramento do roteiro está no fim da L7.

## 2. Revisão de texto (fase A)

Trabalho em `05_ARQUIVOS_DE_TRABALHO/gemini-chat/essentials/` (mapas em `revisao_textos/L01..L08.json`, aplicados por `aplicar_mapas.py`). **268 campos alterados** (L1 19 · L2 31 · L3 36 · L4 33 · L5 41 · L6 34 · L7 51 · L8 23).

**Erros de conteúdo corrigidos**
- **L1 — "Mão na massa":** o Articulate trocou o prompt-base por uma *resposta* inventada, que dizia que o Gemini exige 18 anos (o roteiro diz 13; 18 só para habilidades, Pro e Ultra). Voltou o prompt-base verbatim, com a orientação de comparar a resposta com a lição.
- **L3 — "Mão na massa":** o bloco classificava como **amarelo** conectar um Gmail pessoal que recebe e-mails de clientes; pelo roteiro é **vermelho**. Voltou o prompt-base, com a classificação esperada.
- **L7 — atividade de arrastar:** "Canvas" estava na pilha do Claude (Claude usa Artefatos; Canvas é do Gemini e do ChatGPT) e "Projetos" na do ChatGPT (existe nos dois). Itens renomeados para nomes únicos — "Artefatos" (Claude), "GPTs" e "Plugins e apps" (ChatGPT) —, sem mexer no gabarito das pilhas.
- **L7 — checklist de avaliação:** tinha virado uma "persona/tarefa/contexto" sem sentido; voltou o checklist de 5 critérios do roteiro. A aba do Gemini dizia que ele "envia e-mails pelo Gmail" (o roteiro só fala em consultar e criar eventos) — removido.
- **L5, L6, L7:** prompts-base parafraseados ou convertidos em tabela voltaram verbatim.
- **Quiz (L8):** rótulos "True/False" → "Verdadeiro/Falso" (3 questões); a afirmação vaga "O Gemini Chat foi projetado com atenção à privacidade…" virou uma afirmação verificável (Histórico desativado ainda guarda ~2 meses — Verdadeiro, mesma alternativa correta); a lacuna "pesquisar, redigir, ____" (resposta "analisar arquivos", ambígua) virou "chat ____" → **temporário**; a lacuna "O ____ registra…" (resposta de 3 palavras) virou "exclusão automática após ____ meses" → **18**; caminho de imagem alinhado a "Criar imagens".

**Demais melhorias**
- Aberturas genéricas ("é fundamental para aproveitar ao máximo…") trocadas pelo problema concreto de cada módulo e pela nota de encadeamento do roteiro.
- Fórmula de objetivos padronizada ("Ao final desta lição, você será capaz de:") nas 7 lições.
- Processos com título e tempo do roteiro ("Verificação inicial (4 min)", "Configurar o Histórico (7 min)" etc.), breadcrumbs e pontos de controle 🏁.
- Informação restaurada da fonte: seletor de modelo (rápido × raciocínio) na L2; Histórico desativado guarda ~2 meses e derruba apps na L3; "o que você sabe sobre mim?" e Gems → habilidades na L4; LGPD com número na L3.
- Feedbacks das questões no padrão "Correto./Não." com o porquê; nenhum gabarito alterado nas questões de lição.
- Fechamentos "Agora que você domina…" trocados pelo próximo passo concreto.

Os campos `feedbackCorrect/feedbackIncorrect` não estão na lista do `validar_estrutura.py`; a validação usou o `validar_texto.py` (mesmo wrapper do vibecoding, que só acrescenta `matchTitle`, `feedbackCorrect` e `feedbackIncorrect` como texto). Resultado: estrutura preservada, 268 = 268.

## 3. Inserções (fase B) — 7 blocos

| # | Lição | Onde | Tipo | Por quê |
|---|---|---|---|---|
| e01 | L1 | após o ponto de controle | Questão em cenário (estagiária de 16 anos sem "Habilidades") | o módulo não tinha nenhuma verificação; fixa a regra de idade, o erro mais comum |
| e02 | L2 | antes do modelo de pedido | **HTML "Monte o seu pedido"** (escolhe persona, tarefa, contexto e formato e vê o prompt se formar, com botão copiar) | o quadro de 4 elementos era só texto e flashcard |
| e03 | L3 | após os flashcards | **HTML "O que acontece com a sua conversa?"** (Histórico ativado × desativado × chat temporário, 5 critérios) | comparação de 3 modos escondida em accordion + flashcards |
| e04 | L4 | antes de "o que o Gemini sabe" | **HTML "Informação salva, memória ou habilidade?"** (6 situações, correção imediata) | distinção central do módulo sem prática |
| e05 | L5 | após o destaque | **HTML "Isso já é conferência?"** (6 situações sobre a definição de dado pessoal) | "marcação não é prova" só era afirmado |
| e06 | L6 | antes de "Outros recursos" | Questão em cenário (planilha com nome e telefone de clientes) | aplica o semáforo a arquivos, objetivo 1 do módulo |
| e07 | L7 | após o checklist | **HTML "Seu quadro comparativo"** (preenche Gemini × outro assistente e copia o quadro) | o produto final do curso não tinha onde ser montado |

HTMLs em `05_ARQUIVOS_DE_TRABALHO/gemini-chat/html/` (fontes em `src/`, montados por `build.py`; mesma base visual dos cursos anteriores, cor `#152f4d` do tema). Roteiros gerados por `gerar_roteiros.py` e aplicados por `aplicar_roteiros.sh`.

## 4. Validações

- Fase A: `validar_texto.py` sem divergência estrutural (268 campos); `scorm_reempacotar.py` com round-trip e 0 arquivos alterados fora do `runtime-data.js`; ponte `verificar_scorm.py`: **APROVADO**, 0 erros, 0 avisos.
- Fase B: `validar.py` **APROVADO** (7 blocos novos; 689 IDs, todos distintos); `verificar_scorm.py` do pacote final contra o revisado: **APROVADO**, 0 erros, 0 avisos. Nenhum "[conferir]" no curso final.

## 5. Navegador (mock de LMS da skill)

Visto: as 7 lições percorridas com todos os Continues; textos revisados renderizando; os 5 HTMLs carregam na posição certa e funcionam (pedido montado com as 4 partes; troca de modo no comparador do Histórico; os dois classificadores completam 6/6 com a mensagem final); as duas questões novas corrigem como "Correct" com o feedback certo; Quiz: questões 1 a 7 respondidas no navegador, todas corretas (inclui a lacuna "modelo de linguagem" e o Verdadeiro/Falso reescrito); console sem erros; os 5 HTMLs a 360 px sem rolagem horizontal.
**Não testado no navegador:** as questões 8 a 21 do Quiz (a 8 é de arrastar e travou a automação; as lacunas reescritas 19 e 20 usam o mesmo mecanismo da questão 2, que funcionou); LMS real; abertura por `file://`.

## 6. Decisões tomadas

- **[conferir] do roteiro resolvidos por pesquisa** (support.google.com/gemini e support.claude.com, 17/11/2026): Claude — "Preferências pessoais" em Configurações > Perfil e "Chat incógnito"; Gemini — "Verificar resposta" fica abaixo da resposta (em algumas versões, no menu de mais opções); habilidades em Personalizar > Habilidades, criadas com o Gemini ou manualmente e acionadas com "/". Rótulos sem confirmação exata (exportar do Canvas, criar imagens, apps conectados) foram escritos pela função, sem depender do rótulo.
- Gems: o texto diz que "passam a habilidades em novembro de 2026", coerente com a ajuda do Google (transição em 17/11/2026).
- Os cenários das duas questões novas e dos classificadores são ilustrativos, construídos só com regras do próprio curso.
