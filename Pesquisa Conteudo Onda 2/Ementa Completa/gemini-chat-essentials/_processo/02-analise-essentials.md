# 02 — Análise crítica 360: Gemini Chat Essentials v1.0

Objeto base: Gemini Chat · Público: iniciantes (T1, posição 3), juristas (J1) e demais áreas · Trilha: Essentials.

## 1. Sumário Executivo

**Nota: 3,5/10.** A v1.0 cobre a tarefa observável no papel, mas tem um erro estrutural e um
risco crítico:

- **Ensina um recurso em extinção.** O produto final é um Gem; as notas de versão (30/09/2026)
  anunciam que habilidades substituem os Gems, e a descontinuação em contas pessoais ocorre em
  novembro de 2026. O curso nasceria desatualizado.
- **Privacidade ausente, com conexão ao Gmail no Módulo 4.** O aluno conecta e-mail pessoal ao
  Gemini sem saber que isso exige o Histórico ativado, que há revisão humana (conversas revisadas
  ficam até 3 anos) e que o próprio Google pede para não inserir informação confidencial.
- Nenhum Módulo 0: idade mínima (13 anos; 18 para habilidades), conta pessoal × Workspace e
  limites do gratuito não aparecem.
- Exercícios sem gabarito ("pergunte algo do seu interesse"; "resposta recebida").
- Alucinação e verificação de respostas não aparecem; a busca é tratada como confiável.
- Não há comparação com ChatGPT e Claude, embora o curso venha logo depois deles na T1/J1.

## 2. Pontos Positivos

- Usa o guia oficial de prompts do Google (persona, tarefa, contexto, formato) — ancoragem em
  fonte oficial, e diferente do quadro usado no curso do ChatGPT, o que enriquece a trilha.
- Identifica o diferencial do Gemini: integração com Gmail, Drive e Agenda.
- Inclui Canvas e exportação para o Documentos Google.

## 3. Pontos Negativos e Gargalos

**Clareza pedagógica:** Módulo 1 tem um parágrafo; o aluno não aprende o que é o app Gemini em
relação aos modelos Gemini, ao Gemini no Workspace e ao antigo Bard. Módulo 4 junta apps
conectados e Gems sem explicar nenhum dos dois.

**Rigor técnico:**
- Gems → habilidades (criar com o Gemini ou manualmente; acionar com "/" ou "@"; migração dos Gems
  como rascunhos inativos em "Personalizar").
- "Personalizar" (13/10/2026) é o novo ponto central de instruções, apps e habilidades.
- Memória: "conversas anteriores" renomeada para "memórias" (26/03/2026); gestão em
  `gemini.google.com/personalization-settings`; informações salvas em `gemini.google.com/saved-info`.
- Arquivos: até 10 por comando, 100 MB, vídeo 5 min e áudio 10 min no gratuito.
- Chat temporário ao lado de "Novo chat"; fica cerca de 2 meses; não treina modelos.
- Limites do gratuito "renovados de 5 em 5 horas até o teto semanal".

**Segurança (crítico):** sem módulo de dados; sem semáforo; sem LGPD e sigilo para o jurista; sem
a diferença entre conta pessoal e conta Workspace (que não treina modelos).

**Engajamento:** registro formal correto, mas textos curtos e exercícios sem desafio.

**Potencial oculto:** importação de memória de outros assistentes (útil a quem vem do ChatGPT e do
Claude, mas exige cuidado de dados); app de desktop no Windows (atalho Alt + Espaço); verificação
de resposta com a Pesquisa Google; Gemini Live; Deep Research como "onde fica".

**Aderência:** o PDF "de órgão público" sem link fixo e "resuma meus e-mails de hoje" expõem dados
reais e não têm gabarito.

## 4. Matriz de Soluções e Melhorias

| # | Gargalo | Onde | Correção concreta | Prioridade |
|---|---|---|---|---|
| G1 | Gems em extinção | M4, Síntese | Substituir por **habilidades**; Gems só como nome antigo; rota alternativa "instruções no início da conversa" para quem não tem habilidades | Alta |
| G2 | Sem Módulo 0 | Antes do M1 | Conta pessoal, idade, planos com preço em reais (17/11/2026), limites do gratuito, mapa da tela | Alta |
| G3 | Privacidade ausente | Antes de apps e arquivos | **Módulo 2 — Dados, privacidade e sigilo**: Histórico do Gemini, revisão humana (até 3 anos), ~2 meses com histórico desativado, chat temporário, exclusão automática, pessoal × Workspace, semáforo | Alta |
| G4 | Conexão de apps sem decisão | M5 | Explicitar a troca: apps do Google exigem Histórico ativado; decidir antes de conectar; desconectar depois | Alta |
| G5 | Identidade confusa | M1 | Tabela app Gemini × modelos × Gemini no Workspace × Google Assistente | Média |
| G6 | Verificação ausente | M1 → M4 | Plantar alucinação no M1, retomar no M4 com verificação na Pesquisa Google e conferência na fonte | Alta |
| G7 | Personalização desatualizada | Novo M3 | Personalizar, memória, informações salvas, chat temporário, habilidades | Alta |
| G8 | Exercícios sem gabarito | Todos | Dados embutidos e critério observável em cada pílula | Alta |
| G9 | Sem comparação | Síntese | Tabela ChatGPT × Claude × Gemini e atividade nas três ferramentas (ou duas, à escolha) | Média |
| G10 | Arquivos sem limites | M5 | Limites oficiais e rota para quando a cota acabar | Média |
| G11 | Faltam "Mão na massa" e 100–130 min | Todos | Prompt-base por módulo; carga redistribuída | Alta |

## 5. Roadmap de Expansão

**Cabem:** importação de memória (como cuidado de dados), app Windows/Mac, Gemini Live (menção
com limite), Deep Research (onde fica), YouTube como fonte (menção).
**Ficam fora:** Gemini no Workspace (curso próprio), NotebookLM, Spark, Antigravity, Veo/Flow.
**Não verificado:** rótulos atuais de "Personalizar", "Habilidades", "Ferramentas" e do botão de
verificação com a Pesquisa Google na tela (não houve acesso a conta).
