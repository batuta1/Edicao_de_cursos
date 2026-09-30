# Relatório de Edição — ChatGPT Word (Essentials), trilha SCORM

## Pacote

- Original: `chatgpt-word-essentials-scorm12-bMZw5g3l.zip`
- Revisado: `chatgpt-word-essentials-scorm12-bMZw5g3l-REVISADO.zip`
- Formato: default (`scormcontent/runtime-data.js`)
- Título no pacote: `ChatGPT Word - Essentials` (confere com o título esperado; usado como trava na extração)
- 4 lições: `Preparação e Segurança no Uso do ChatGPT com Word`, `Caminhos de Integração e Formulação de
  Instruções Eficazes`, `Modelos, Automatização e Responsabilidade na Produção de Documentos`, `Quiz`.

## Material-fonte e mapeamento lição ↔ roteiro

- `roteiro-essentials.md` (roteiro final da trilha Essentials, 6 módulos) foi a referência principal.
- `ementa.md` foi usada para conferir fatos sensíveis a planos/limites, em especial a seção
  "Pendências de Validação".
- O curso SCORM condensa os 6 módulos do roteiro em 3 lições de conteúdo + 1 quiz final:
  - Lição 0 ≈ Módulo 0 (Antes de colar qualquer coisa)
  - Lição 1 ≈ Módulos 1 + 2 + 3 (caminhos de integração, anatomia da instrução, quatro operações)
  - Lição 2 ≈ Módulos 4 + 5 (modelo reutilizável, síntese e aplicação integrada)
  - Lição 3 = quiz final (8 questões, sem correspondência direta a um módulo)

## Critério aplicado

Compilação de cada bloco de texto (`paragraph`, `heading`, `title`, `description`, feedbacks de
questão) de cada lição, comparado frase a frase com o módulo correspondente do roteiro-fonte.
Buscados os sintomas típicos: abertura genérica, fechamento motivacional vazio, perda de
especificidade herdada da fonte, e afirmações não respaldadas pelo material-fonte ou pela ementa.

**Conclusão geral:** o texto do curso já estava bem alinhado ao roteiro-fonte — específico, sem
aberturas ou fechamentos genéricos de IA, com breadcrumbs de interface e prompts entre aspas triplas
preservados fielmente. Não havia sinal de revisão superficial pendente; as poucas alterações feitas
foram pontuais.

## Alterações lição a lição

### Lição 0 — Preparação e Segurança no Uso do ChatGPT com Word

1. **Campo `title`** (bloco de comparação de planos, id `c77aa2df-dff7-4176-8a24-fdfefc172c5c`):
   `"Free, Go, Plus e Pro"` → `"Plus e Pro"`.
   O roteiro-fonte lista, na tabela de tratamento de dados, apenas as linhas "Plus e Pro" e
   "Business, Enterprise e Edu" — não há "Free" nem "Go" no material-fonte. A ementa também
   registra esse dado, na seção "Pendências de Validação", item 3, como fato que precisa ser
   conferido antes da publicação. Ampliar a afirmação para incluir Free e Go, sem respaldo na
   fonte, arrisca declarar algo não verificado como fato. Corrigido para reproduzir exatamente o
   que o roteiro-fonte afirma.

2. **Campo `paragraph`** (item de lista, id `dlulw50hai5e83kdt199k7ch`):
   `"O uso precisa ser declarado no documento e em que forma?"` →
   `"O uso precisa ser declarado no documento? Em que forma — nota de rodapé, seção de métodos, declaração de autoria?"`
   O roteiro-fonte formula duas perguntas distintas e dá três exemplos concretos de forma de
   declaração (nota de rodapé, seção de métodos, declaração de autoria). A versão do curso havia
   fundido as duas perguntas em uma e descartado os exemplos — perda de especificidade que o
   critério da skill pede para restaurar.

### Lição 1 — Caminhos de Integração e Formulação de Instruções Eficazes

Nenhuma alteração. Texto fiel ao roteiro (Módulos 1, 2 e 3), com os três caminhos, os limites de
envio, os cinco elementos da instrução e as cinco operações corretamente descritos.

### Lição 2 — Modelos, Automatização e Responsabilidade na Produção de Documentos

Nenhuma alteração. Texto fiel ao roteiro (Módulos 4 e 5), incluindo o critério de frequência, as
quatro etapas do fluxo de modelo e a síntese final ("a ferramenta escreve; a responsabilidade pelo
que está escrito permanece de quem assina"), preservada verbatim.

### Lição 3 — Quiz

Nenhuma alteração de texto. Todos os gabaritos foram conferidos individualmente contra o
roteiro-fonte (ver seção seguinte) e estão corretos.

## Conferência de gabaritos

Todas as 11 questões de múltipla escolha/resposta do curso (3 *knowledge checks* na Lição 0, 3 na
Lição 1, 2 na Lição 2, 8 na Lição 3 — quatro tipos: `MULTIPLE_CHOICE`, `MULTIPLE_RESPONSE`,
`FILL_IN_THE_BLANK`, `MATCHING`) foram extraídas com um script auxiliar (`checar_gabaritos.py`) que
lista a alternativa marcada como `correct: true` ao lado do feedback de cada alternativa. Todas as
marcações de "correta" são consistentes com o texto do próprio feedback e com o roteiro-fonte,
incluindo o gabarito de arquivo de referência vs. modelo reutilizável (1–R, 2–M, 3–M, 4–R), idêntico
ao gabarito do Módulo 4 do roteiro. **Nenhum gabarito foi alterado.**

## Contagem de campos alterados

Confirmada pelo script `validar_estrutura.py`: **2 campos de texto alterados no total**
(`paragraph`=1, `title`=1), todos na Lição 0. Nenhuma divergência estrutural em nenhuma lição.

## Pontos de atenção

- A troca "Free, Go, Plus e Pro" → "Plus e Pro" segue estritamente o roteiro-fonte, mas a própria
  ementa marca esse dado como pendência de validação (planos e políticas de dados mudam com
  frequência). Antes de publicar, vale conferir a tabela de uso de conteúdo por plano diretamente na
  Central de Ajuda da OpenAI.
- Não foi feita alteração nos blocos de "Arquivo de referência" / "Modelo reutilizável" (Lição 2) e
  nos três cartões de caminho (Lição 1), que usam parágrafos HTML vazios (`<p></p>`) como separador
  visual entre os campos rotulados (ex.: "O que é" / "Quando convém" / "Custo de preparação" /
  "Ganho"). O padrão se repete de forma consistente em todos os cartões, o que sugere escolha de
  formatação deliberada (espaçamento visual dentro do card), não erro de geração — por isso não foi
  tratado como defeito de texto e não foi mexido.
- Não verificado neste ciclo: renderização visual do curso em navegador (Fase 8 da skill, opcional).
  A revisão foi inteiramente textual, cruzada contra o roteiro-fonte e a ementa.

## O que foi gerado

- `cursoChatGPTWord.json` — payload desserializado original.
- `licoes_extraidas_ChatGPTWord/licao_00…03…json` — lições separadas (2 editadas campos na 00; 01,
  02 e 03 lidas sem alteração).
- `cursoChatGPTWord_editado.json` — JSON fundido com as edições.
- `cursoChatGPTWord_editado_base64.txt` — Base64 serializado, com verificação de round-trip
  bem-sucedida (decodifica de volta ao mesmo objeto).
- `../chatgpt-word-essentials-scorm12-bMZw5g3l-REVISADO.zip` — pacote SCORM reempacotado; apenas
  `scormcontent/runtime-data.js` foi substituído, as demais 76 entradas do `.zip` permaneceram
  idênticas em tamanho. **O `.zip` original não foi alterado.**
