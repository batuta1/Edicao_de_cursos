# Relatório — ChatGPT Chat - Essentials (revisão de texto + inserção de blocos)

**Data:** 17/11/2026 (v1) · **Pacote final:** `Onda 2/01_FINALIZADO_subir-na-LMS/chatgpt-chat/chatgpt-chat-essentials-scorm12-OxgDcR0G-FINAL-com-blocos-v1.zip`

## 1. Material-fonte e mapeamento

Fonte: `Pesquisa Conteudo Onda 2/Ementa Completa/chatgpt-chat-essentials/roteiros/roteiro-articulate-essentials.md`.
Mapeamento 1:1: L1–L7 = Módulos 0–6. O Articulate não gerou lição de Quiz (cada lição tem sua questão). O encerramento do roteiro está no fim da L7.

## 2. Revisão de texto (fase A)

Trabalho em `05_ARQUIVOS_DE_TRABALHO/chatgpt-chat/essentials/` (mapas em `revisao_textos/L01..L07.json`, aplicados por `aplicar_mapas.py`). **288 campos alterados** (L1 40 · L2 40 · L3 35 · L4 32 · L5 51 · L6 49 · L7 41).

**Erros de conteúdo corrigidos**
- **L1 — "Mão na massa":** o Articulate executou o prompt-base e gravou uma *resposta* no lugar dele, com informação errada (GPT-4 só em planos pagos, link para chat.openai.com, "sem atualização em tempo real"). Voltou o prompt-base verbatim, com a orientação de comparar a resposta com a página oficial.
- **L2 — exemplo vago × estruturado:** o bloco trazia um e-mail e uma explicação jurídica "prontos" (respostas inventadas). Voltaram o pedido vago, o pedido estruturado e a variação jurídica do roteiro.
- **L2 — ponto de controle:** tinha virado um texto sobre "comunicação eficaz no ambiente de trabalho", sem relação com o exercício. Voltou o 🏁 do roteiro.
- **L3 — "Mão na massa":** o bloco classificava como **amarelo** uma planilha com nome e telefone de clientes. Pelo semáforo do próprio curso é **vermelho** (dados pessoais de terceiros). Voltou o prompt-base, com a classificação esperada.
- **L7 — quadro comparativo:** afirmava que o ChatGPT tem "preferências pessoais do perfil" e "modo incógnito" (são nomes do Claude). Refeito com a simetria do roteiro.
- **L7 — "Mão na massa":** o prompt de comparação tinha virado uma tabela HTML para preencher. Voltou o prompt verbatim.
- **L6:** a lista de objetivos estava abreviada ("Anexar arquivos e gerar gráficos") e o mapa dizia que tarefas agendadas tinham "cursos avançados". Ambos alinhados ao roteiro (tarefas agendadas: do Go em diante, sem curso específico).
- **L4:** o accordion de Projetos dizia que "todos os participantes compartilham as mesmas instruções" e omitia os limites de arquivos (5/25/40) e a regra dos projetos compartilhados. Corrigido.

**Demais melhorias**
- Aberturas genéricas ("é fundamental para aproveitar todo o seu potencial") trocadas pelo problema concreto de cada módulo e pela nota de encadeamento do roteiro.
- Fórmula de objetivos padronizada ("Ao final desta lição, você será capaz de:") nas 7 lições.
- Informação restaurada da fonte: tabela de planos com fonte e data (L1), caminhos com breadcrumbs dos seis elementos da interface (L1), janela de contexto de ~12 páginas no Free (L2), Exportar dados (L3), LGPD com número e semáforo com condutas (L3).
- Processos com título e tempo do roteiro ("Verificação inicial (4 min)", "Do vago ao estruturado (6 min)" etc.) e pontos de controle 🏁.
- Feedbacks das questões no padrão "Correto./Não." com o porquê; nenhum gabarito alterado.
- Fechamentos "Agora que você domina…" trocados pelo próximo passo concreto.

Validação com `validar_texto.py`: estrutura preservada, 288 = 288.

## 3. Inserções (fase B) — 7 blocos

| # | Lição | Onde | Tipo | Por quê |
|---|---|---|---|---|
| e01 | L1 | após o quadro-resumo dos planos | **HTML "Disponível não é ilimitado"** (6 recursos: incluído, limitado por cota ou fora do Free) | a distinção central do módulo era só texto |
| e02 | L2 | antes do exercício "Do vago ao estruturado" | **HTML "Monte o seu pedido"** (tarefa, contexto, público, formato; copia o pedido) | os 4 elementos não tinham prática guiada |
| e03 | L3 | após os flashcards do semáforo | **HTML "Pode ir para o ChatGPT?"** (6 conteúdos no semáforo, correção imediata) | o roteiro pede discussão de classificação; o curso só tinha flashcards |
| e04 | L4 | antes do Continue | **HTML "Instruções, memória ou projeto?"** (6 situações) | os três recursos "costumam ser confundidos" e não havia prática |
| e05 | L5 | antes do Continue | **HTML "A fonte sustenta a frase?"** (frase × trecho real do CDC, 5 casos) | o passo "localizar o trecho" era só afirmado |
| e06 | L6 | após os flashcards | Questão em cenário (planilha com nome e CPF de clientes) | aplica o semáforo a arquivos ("arquivo enviado é dado tratado") |
| e07 | L7 | após o checklist | **HTML "Seu quadro comparativo"** (ChatGPT × Claude, com os dois perfis; copia o quadro) | o produto final do curso não tinha onde ser montado |

HTMLs em `05_ARQUIVOS_DE_TRABALHO/chatgpt-chat/html/` (fontes em `src/`, montados por `build.py`; mesma base visual e cor `#152f4d` dos cursos anteriores). Roteiros gerados por `gerar_roteiros.py` e aplicados por `aplicar_roteiros.sh`.

## 4. Validações

- Fase A: `validar_texto.py` sem divergência estrutural (288 campos); `scorm_reempacotar.py` com round-trip e 0 arquivos alterados fora do `runtime-data.js`; `verificar_scorm.py`: **APROVADO**, 0 erros, 0 avisos.
- Fase B: `validar.py` **APROVADO** (7 blocos novos; 550 IDs, todos distintos); `verificar_scorm.py` do pacote final contra o revisado: **APROVADO**, 0 erros, 0 avisos. Nenhum "[conferir]" no curso final.

## 5. Navegador (mock de LMS da skill)

Visto: as 7 lições percorridas até o fim com todos os Continues; os 6 HTMLs carregam e funcionam (classificadores completam com a mensagem final; montador de pedido e quadro comparativo geram o texto); a questão nova (L6) e a questão da L2 corrigem como "Correct" com o feedback revisado; os 6 HTMLs a 360 px sem rolagem horizontal.
**Não testado:** as outras 5 questões de lição clicadas no navegador (texto e gabarito conferidos no JSON); LMS real; abertura por `file://`; botão copiar com área de transferência real (no teste automatizado caiu no modo "texto selecionado, use Ctrl+C", que é o fallback previsto).

## 6. Decisões tomadas

- **[conferir] do roteiro resolvidos por pesquisa** (17/11/2026): "Ramificar em novo chat" fica em Mais ações (⋯) abaixo da resposta (help.openai.com e imprensa especializada); Canvas e Modo Estudo estão disponíveis no Free (ajuda da OpenAI), mas o rótulo do Modo Estudo e o da busca no botão "+" variam entre versões — foram escritos pela função ("no botão +, a opção de busca na web / de estudo"), sem depender do rótulo. Claude: "Preferências pessoais" em Configurações > Perfil e "Chat incógnito" (mesma pesquisa do Gemini Chat).
- Os cenários das atividades e da questão nova são ilustrativos, construídos só com regras do próprio curso; os trechos do CDC citados na atividade e05 seguem o texto do Planalto (arts. 18, § 1º, e 49).
