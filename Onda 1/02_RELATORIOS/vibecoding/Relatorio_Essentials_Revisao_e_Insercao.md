# Relatório de revisão, tradução e inserção — Vibe Coding - Essentials

Data: 04/11/2026 · Curso **presumido não publicado** (veio de `04_NAO_REVISADO/`; não confirmado) — por isso houve inserções no meio das lições.

**Pacote final para a LMS (v1):**
`01_FINALIZADO_subir-na-LMS/vibecoding/vibe-coding-essentials-scorm12-knPCm1GR-FINAL-com-blocos-v1.zip`
(cópia idêntica, por hash, de `05_ARQUIVOS_DE_TRABALHO/vibecoding/essentials/vibe-essentials-blocos/saidas/…-REVISADO-v1.zip`).

Histórico em `03_VERSOES_ANTIGAS/vibecoding/`: `original-articulate/` (exportação original, não modificada) e `fase-A-so-texto/` (`…-REVISADO.zip`, só texto). O original continua também em `04_NAO_REVISADO/vibecoding/`.

---

## 1. Situação de partida

O curso veio **inteiro em inglês** (títulos de lição, textos, questões, feedbacks, capa), com só os prompts e a ficha do "Minhas Tarefas" em português. Foi **traduzido integralmente** e, ao mesmo tempo, revisado contra o roteiro.

## 2. Material-fonte e mapeamento

Roteiro: `Pesquisa Conteudo Onda 1/Ementa Completa/vibe-coding-essentials/roteiros/roteiro-articulate-essentials.md`.
Mapeamento 1:1: lição N do Rise = Módulo N−1 do roteiro (lição 1 = Módulo 0 … lição 7 = Módulo 6 + Encerramento); lição 8 = quiz gerado pelo Articulate. No texto do aluno, as referências cruzadas usam "lição N", não "Módulo".

## 3. Fase A — tradução e revisão de texto (795 campos)

Método: mapas `revisao_textos/L01..L08.json` (caminho → texto novo) aplicados por `aplicar_mapas.py`, que recusa campo não textual ou já alterado. Termos idênticos ao original (Chat, Plan, Build, Front-end, History…) foram retirados dos mapas por `limpar_iguais.py`.
Por lição: L1 91 · L2 105 · L3 97 · L4 107 · L5 87 · L6 59 · L7 71 · L8 (quiz) 178. Por campo: title 290, description 241, paragraph 112, feedback 87, heading 43, matchTitle 8, feedbackCorrect 7, feedbackIncorrect 7.

`matchTitle`, `feedbackCorrect` e `feedbackIncorrect` (questões de associação, de lacuna e verificações com feedback único) não estão na lista de texto do `validar_estrutura.py` da skill; foram validados por `vibecoding/validar_texto.py`, que só acrescenta essas três chaves à lista e chama o validador da skill.

**Correções de conteúdo (além da tradução):**
- **Dados do "Minhas Tarefas" errados:** a aba de banco de dados dizia que cada tarefa tem "due date"; o roteiro define título, concluída, dono e data de criação (colunas `title`, `completed`, `user_id`, `created_at`). Corrigido.
- **"A autorização é gerida automaticamente pelo Lovable":** falso pelo roteiro — as regras RLS precisam ser pedidas e comprovadas com duas contas. Reescrito.
- **Rótulos com posição inventada** ("fica no centro da tela", "no topo do workspace") e funções não documentadas no roteiro (Auth settings "escolhe login social", Users "redefine senhas") foram retirados.
- **Conteúdo do roteiro que faltava:** tabela de planos (Free/Pro/Business com preços e cotas), custo por alteração (0,50 / 1,20 / Plan = 1), rota de baixo consumo, apps para desktop/celular como complemento, data e local de lançamento do Lovable, casos Plinq e Elora com a ressalva de não auditados, datas exatas do incidente (3/2 a 20/4/2026), artigos acadêmicos de 2026, LGPD/ANPD, treinamento desde 09/09/2026 e exclusão dos dados dos usuários finais, Supabase ("Do I need Supabase? No."), dependência de plataforma (GitHub), Replit Agent/Bolt/v0, encerramento com os próximos cursos.
- **Pontos de controle 🏁 e critérios de êxito** do roteiro passaram para os itens "resumo" dos blocos *process*.
- **Gabarito da triagem de ideias:** as abas vinham depois da atividade e eram o gabarito; agora estão rotuladas como "Gabarito da triagem" (a atividade interativa entrou antes — Fase B).
- **Quiz:** "True/False" → "Verdadeiro/Falso"; Q10 passou a perguntar o público do curso (mesma alternativa correta); Q16 (lacuna) dizia a ordem errada do ciclo (construir antes de proteger) — enunciado reescrito na ordem do curso, resposta "publicação"; Q14 (lacuna) aceita "créditos de construção" e "build credits" (as duas respostas já existiam, só traduzidas).
- Objetivos padronizados em "Ao final desta lição, você será capaz de:" e alinhados ao roteiro. Aberturas genéricas ("Get ready to unlock…", "This is your moment to shine!") trocadas pela analogia da loja; fechamentos motivacionais trocados pelo próximo passo concreto.
- Marcadores `[conferir]` do roteiro **não** foram levados para o texto do aluno (ver pontos de atenção).

`validar_texto.py`: ESTRUTURA OK nas 8 lições; 795 campos = 795 entradas dos mapas.

## 4. Fase B — inserções (8 blocos)

| Lição | Posição final | Tipo | Por quê |
|---|---|---|---|
| 1 | 0–2 | Seção nativa "Sobre este curso": título + parágrafo (objetivo geral, 129 min em três sessões, estrutura em sete lições), lista das 5 competências, Continue | Objetivo geral, competências e estrutura do roteiro não estavam no curso |
| 2 | 21 | HTML "Descreva sua ideia como uma loja" (gera o texto para copiar) | O "Mão na massa" do Módulo 1 (modelo com o vocabulário da loja) não existia no curso |
| 3 | 12 | HTML "Triagem de ideias de aplicativo" (5 ideias, correção imediata) | O exercício do roteiro era só lido (gabarito à vista); a 5ª ideia exercita "adequada com ajuste", que o gabarito do roteiro não usa |
| 4 | 9 | HTML "Monte sua ficha de requisitos" (exemplos Minhas Tarefas / Diário de Leituras / Banco de Ideias; confere fora do escopo, dados reais, teste com outra conta, campos sensíveis) | A ficha do roteiro vira ferramenta, reutilizável na lição 7 |
| 5 | 9 | HTML "Resultado do teste de isolamento" (4 perguntas → aprovado / falha de segurança, com o pedido em Plan pronto) | Transforma o critério de êxito e a solução de problemas do Módulo 4 em verificação |
| 6 | 11 | HTML "Descreva o erro antes de pedir a correção" (gera o pedido do roteiro; alerta se houver senha/CPF/chave) | O "Mão na massa" do Módulo 5 não existia no curso |

Nenhum HTML trava Continue. Fontes: `…/vibe-essentials-blocos/trabalho/html/src/` (CSS/JS comuns herdados de Agentes de IA, cor `#152f4d` do tema; montagem por `build.py`); roteiros em `trabalho/roteiros/`; cadeia de inserção em `trabalho/etapas/`.

Fase C (`05_ARQUIVOS_DE_TRABALHO/vibecoding/pos_edicoes.py`, com checagem folha a folha): descrição da capa traduzida e reescrita, e `completeHint` dos 8 Continues → "Conclua o conteúdo acima para continuar.".

## 5. Validações

| Etapa | Ferramenta | Resultado |
|---|---|---|
| Fase A | `validar_texto.py` (wrapper do `validar_estrutura.py`) | ESTRUTURA OK, 795 campos |
| Fase A, pacote | `scorm_reempacotar.py` | round-trip OK; só `runtime-data.js` alterado |
| Original da Fase B | `verificar_scorm.py` | APROVADO, 0 erros, 0 avisos |
| Fase B | `validar.py` | APROVADO: só inserção, 8 blocos seguindo os modelos, 811 IDs únicos |
| Fase C | `pos_edicoes.py` | APROVADO: 9 folhas (capa + 8 completeHint) |
| Pacote v1 | `verificar_scorm.py --original` (contra o original do Articulate) | APROVADO, 0 erros, 0 avisos; só `runtime-data.js` alterado |

## 6. Teste no navegador (mock de LMS da skill, servidor sem cache)

**Visto:** o pacote carrega; lição 1 mostra "Sobre este curso" e para no Continue; os 5 HTMLs aparecem dentro do player nas posições previstas (vizinhos conferidos — ex.: triagem entre o *process* e a questão da lição 3, com altura ajustada); o quiz abre em português (enunciado e Verdadeiro/Falso). Os 6 HTMLs, abertos sozinhos: triagem 5/5 com mensagem final; teste de isolamento (B vê A → falha + pedido; tudo certo → aprovado); ficha com exemplos e conferência; gerador de erro e de "loja" com exemplo. Console sem erros.

**Não verificado:** retomada sem `reset`; abertura por `file://`; LMS real; largura de celular dentro do player; **interface real do Lovable** (exige conta; não entro em contas).

## 7. Pontos de atenção para revisão humana

1. **Rótulos da interface do player continuam em inglês** ("START COURSE", "Lesson 1 of 8", "START QUIZ", "SUBMIT", "TAKE AGAIN", "Your score", "Continue"). Vêm do `labelSet` "English" do curso — o mesmo de todos os cursos da equipe já finalizados. Não foi alterado por ser decisão de padrão da equipe; dá para traduzir (são ~460 rótulos, a maioria de acessibilidade) se for desejado.
2. **Rótulos `[conferir]` do roteiro** não foram validados: `More > Usage`, seletor `Chat/Plan/Build`, `Account settings > Preferences > AI model training`, `Preview toolbar > Mobile view` e `Select elements`, `History`, `More > Cloud > Database/Users > Add user`, `Publish`. Confira numa conta antes de publicar.
3. **Listas de objetivos com itens a mais:** como não se pode remover itens, as lições 3, 4, 5, 6 e 7 têm 5–6 objetivos onde o roteiro tem 3–4; os itens extras desdobram objetivos do roteiro (ex.: "gerar a interface" / "conferir no celular").
4. **Prompts escritos por mim** (não verbatim do roteiro): o de Build e o da iteração final nas abas da lição 7 (o roteiro só traz o de Plan e manda "executar em Build").
5. **Questões de associação** (Q6 e Q12 do quiz): os pares foram traduzidos; não testei a interação de arrastar no player.
6. Gabaritos: nenhum foi mudado.
