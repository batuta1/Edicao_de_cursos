<link rel="stylesheet" href="../../.css/style.css">

# Prompt-Modelo — Geração de Curso Hands-on ("Para Leigos")

> **Como usar:** preencha os campos entre colchetes `[ ]` na seção OBJETO BASE e envie o bloco inteiro ao Claude. O único campo obrigatório é o **OBJETO BASE**; os demais têm valores-padrão e podem ficar como estão.

---

```md
# CONTEXTO
Você atuará como autor de um curso prático no estilo da famosa coleção de livros
"Para Leigos" (For Dummies). Sua tarefa é produzir um curso completo, em português,
no formato de arquivo Markdown (.md), do tipo HANDS-ON: baseado em exercícios,
experimentação e resolução de problemas reais. O curso integra a trilha "Hands-on".

# OBJETO BASE (preencher)
- Tema/ferramenta do curso: `claude-Get_Started.md`
- Público-alvo: docentes ensino superior iniciantes em IA; analistas administrativos; alunos do ensino superior.

# CONFIGURAÇÃO (ajustar se desejar; caso contrário, manter o padrão)
- Carga horária: 60 a 120 minutos.
- Número de oficinas práticas: 4 oficinas + 1 projeto final
- Material-fonte de referência: `claude-Get_Started.md`

# TAREFA
Produza o curso completo (AUTOINSTRUCIONAL) respeitando a ESTRUTURA e o ESTILO definidos a seguir.
O princípio condutor é PBL (aprendizagem baseada em problemas): cada oficina
começa com um problema concreto e o aluno aprende RESOLVENDO-O com as próprias mãos.

## ESTRUTURA OBRIGATÓRIA (nesta ordem)

1. TÍTULO
   - Formato: `# Claude: Comece a usar o aplicativo para desktop — Curso Hands-on`
   - SUBTÍTULO sem TRADUÇÃO: "Claude: Get Started with the Desktop App — Curso Hands-on"
   - Logo abaixo, um subtítulo curto e encorajador (itálico) prometendo que,
     ao final, o aluno terá feito algo de verdade.

2. SEÇÃO "Antes de Arregaçar as Mangas"
   - Parágrafo curto, leve, dizendo o que o curso é (mão na massa, sem enrolação).
   - Uma lista "O que você precisa ter aberto agora:" com os itens essenciais.
   - Um box ">" no estilo da coleção, com o ícone 🔑, explicando em 1-2 frases
     a "regra de ouro" do curso (ex.: "errar faz parte; é assim que se aprende").

3. SEÇÃO "O Mapa da Mão na Massa"
   - Tabela: Oficina | O problema que você vai resolver | Tempo.
   - Uma frase dizendo que as oficinas podem ser feitas em sequência, cada uma
     entregando uma pequena vitória.

4. OFICINAS PRÁTICAS (uma por bloco, na quantidade definida em CONFIGURAÇÃO)
   Cada oficina deve conter, NESTA ORDEM:
   a. Cabeçalho: "# Oficina N — [Nome curto e direto, orientado à ação]"
   b. "### 🎯 O Problema" — 1 parágrafo curto apresentando uma situação real e
      reconhecível em que o aluno se veria, e o que ele vai conseguir resolver.
   c. "### 🧰 O que você vai usar" — lista enxuta do necessário para esta oficina.
   d. "### 👐 Mão na massa" — passo a passo NUMERADO, com instruções diretas,
      curtas e acionáveis (verbo no início: "Abra...", "Clique...", "Digite...").
      Inclua, quando útil, o texto exato a ser digitado em bloco de citação.
   e. "### ✅ Deu certo?" — como o aluno confirma que a tarefa funcionou
      (o resultado esperado descrito em 1-2 linhas).
   f. "### 🚑 Se travar" — mini-tabela (Problema | O que fazer) com 2 a 3 dos
      tropeços mais comuns daquela oficina.
   g. "### 🚀 Quer ir além?" — Três desafios extras opcionais, de 1 frase.
   - Distribua ao longo das oficinas, com moderação, os boxes de margem ">" da
     coleção, usando os ícones: 💡 (Dica), ⚠️ (Cuidado), 📌 (Não esqueça),
     🤓 (Curiosidade técnica — pode pular sem prejuízo).

5. PROJETO FINAL
   - Título: "# Projeto Final — [Nome do entregável]"
   - "### 🎯 A missão" — um problema maior que reúne o que foi praticado nas oficinas.
   - "### 👐 Mão na massa" — passos numerados que encadeiam as habilidades anteriores.
   - "### 🏁 Como saber que terminou" — uma checklist marcável "[ ]" com os
     critérios do entregável pronto.

6. SEÇÃO "A Parte dos Dez" (homenagem ao formato clássico da coleção)
   - Título: "# A Parte dos Dez — [tema, ex.: 'Atalhos que Salvam seu Dia']"
   - Uma lista de 10 dicas práticas, rápidas e independentes sobre o OBJETO BASE.
   - Caso 10 itens não se sustentem sem encher linguiça, reduza para um número
     honesto (ex.: "A Parte dos Sete") em vez de inventar conteúdo.

7. SEÇÃO "Conseguiu! E agora?"
   - 1-2 parágrafos comemorando o progresso e sugerindo como continuar praticando.

## ESTILO OBRIGATÓRIO (a "alma" do curso)

- Tom da coleção "Para Leigos": leve, encorajador, bem-humorado na medida certa,
  e SEMPRE respeitoso — o leitor é inteligente, apenas novato. Nunca condescendente.
- Sugerir a inserção de "Captura de Tela" para ilustrar instruções   
  complexas, pontos de controle ou páginas/janelas/objetos eu o aluno precise interagir.
- Fale diretamente com o aluno em 2ª pessoa ("você"). Linguagem simples e cotidiana.
- Zero jargão sem explicação. Se um termo técnico for inevitável, explique-o na hora,
  com uma comparação do dia a dia.
- Frases curtas. Parágrafos curtos. Priorize o FAZER sobre o explicar: o aluno
  aprende a teoria mínima necessária para executar o próximo passo, e nada além.
- Cada oficina deve entregar uma "pequena vitória" concreta e visível.
- Use os boxes de margem com parcimônia (1 a 2 por oficina), para não poluir.
- Humor é tempero, não prato principal: no máximo uma piada leve por seção.
- Markdown limpo: cabeçalhos, listas numeradas, tabelas curtas e citações para os
  boxes. Separe oficinas com uma quebra de página (`<div style="page-break-after: always;"></div>`). Use emojis SOMENTE nos cabeçalhos e boxes previstos acima, não no corpo do texto.

# RESTRIÇÕES
- Cada passo do "Mão na massa" deve ser executável de verdade, na ordem dada,
  sem etapas implícitas omitidas.
- Não invente recursos, botões ou menus que o OBJETO BASE não possua; se houver
  incerteza, descreva a ação de forma genérica e sinalize a necessidade de conferir.
- Some os tempos das oficinas dentro da carga horária definida.
- Mantenha o tom leve, mas a informação correta: diversão não justifica erro técnico.
- Produza o documento inteiro em um único arquivo Markdown, pronto para uso.

# FORMATO DE SAÍDA
Um único documento Markdown completo, do título à seção final, seguindo
exatamente a ordem e os elementos descritos em ESTRUTURA OBRIGATÓRIA.
```
