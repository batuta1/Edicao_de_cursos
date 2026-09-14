<link rel="stylesheet" href="../../.css/style.css">

# Prompt-Modelo — Geração de Plano de Aula (Trilha Essentials)

> **Como usar:** preencha os campos entre colchetes `[ ]` na seção CONFIGURAÇÃO e envie o bloco inteiro ao Claude. O único campo obrigatório é o **OBJETO BASE**; os demais possuem valores-padrão e podem ser deixados como estão.

---

```md
# CONTEXTO
Você atuará como designer instrucional. Sua tarefa é produzir um Plano de Aula
completo, em português, no formato de arquivo Markdown (.md), seguindo
RIGOROSAMENTE o modelo estrutural e o estilo descritos abaixo. O plano integra
uma trilha de cursos curtos chamada "Essentials".

Inspire-se na clareza didática da famosa coleção de livros "Para Leigos"
(For Dummies): pressuponha que o participante é inteligente, porém inteiramente
novato no tema. Em consequência, explique cada conceito a partir do zero,
descomplique todo termo técnico no momento em que ele surgir e não dê nenhum
conhecimento prévio como adquirido.
IMPORTANTE: esta inspiração refere-se EXCLUSIVAMENTE à acessibilidade do
conteúdo — ou seja, a tornar o assunto compreensível a quem nunca o viu. Ela NÃO
altera o registro do texto, que permanece formal, impessoal e de tom acadêmico,
conforme detalhado em ESTILO OBRIGATÓRIO. Não adote o tom descontraído, o humor
nem o tratamento em 2ª pessoa característicos daquela coleção: a marca "Para
Leigos" aqui é a de descomplicar, não a de informalizar.

# OBJETO BASE (preencher)
- Tema/ferramenta do curso: `claude-Get_Started.md`
- Público-alvo: docentes ensino superior iniciantes em IA; analistas administrativos; alunos do ensino superior.

# CONFIGURAÇÃO (ajustar se desejar; caso contrário, manter o padrão)
- Carga horária: 60 a 120 minutos.
- Número de módulos de conteúdo: padrão: 4 módulos de conteúdo + 1 de síntese
- Material-fonte de referência: `claude-Get_Started.md`

# TAREFA
Produza o Plano de Aula (AUTOINSTRUCIONAL) completo respeitando a ESTRUTURA e o ESTILO definidos a seguir.

## ESTRUTURA OBRIGATÓRIA (nesta ordem)

1. TÍTULO
   - Formato: `# (Plano de Aula) Claude: Comece a usar o aplicativo para desktop — Curso Essentials`
   - SUBTÍTULO sem TRADUÇÃO: "Claude: Get Started with the Desktop App — Curso Essentials"

2. SEÇÃO "Identificação"
   - Uma tabela de duas colunas (Campo | Definição) contendo, no mínimo:
     Curso, Natureza, Carga horária, Público-alvo, Pré-requisitos, Recursos necessários.

3. SUBSEÇÃO "Objetivo Geral"
   - Um parágrafo único, impessoal, que enuncie a finalidade do curso e o produto
     final esperado do participante.

4. SUBSEÇÃO "Competências a Desenvolver"
   - Frase introdutória ("Concluído o curso, o participante deverá demonstrar
     capacidade de:") seguida de lista numerada com 4 competências.

5. SUBSEÇÃO "Estrutura e Sequência dos Módulos"
   - Um parágrafo curto declarando a progressão cumulativa entre módulos.
   - Uma tabela: Módulo | Título | Referência (material-fonte) | Tempo.

6. MÓDULOS DE CONTEÚDO (um por bloco, na quantidade definida em CONFIGURAÇÃO)
   Cada módulo deve conter, nesta ordem:
   a. Cabeçalho: "# Módulo N — [Título do módulo]"
   b. Nota de encadeamento (uma única linha, em citação ">"), indicando o
      pré-requisito e o deslocamento de foco em relação ao módulo anterior.
      No primeiro módulo, indicar que é o ponto de partida.
   c. "### Objetivos de Aprendizagem" — frase introdutória ("Ao final deste
      módulo, o participante deverá ser capaz de:") + lista de 3 a 4 objetivos.
   d. "### Texto Descritivo" — de 3 a 5 parágrafos em prosa corrida, impessoal
      e de registro formal/acadêmico (ver ESTILO).
   e. "### Exercício Prático" — título da atividade com tempo estimado entre
      parênteses; procedimento em passos numerados OU questão de múltipla escolha;
      e um "Critério de êxito" / "Gabarito" / "Fundamentação" explícito.
   f. "### Mão na massa" - Um prompt base, editável, para o aluno preencher com 
      um assunto de interesse dele.

7. MÓDULO FINAL DE SÍNTESE
   - Título: "# Módulo [N] — Síntese e Aplicação Integrada"
   - Mesma estrutura dos demais, com Exercício Prático na forma de ATIVIDADE
     INTEGRADORA que articule as competências de todos os módulos anteriores,
     acompanhada de uma tabela de "Critérios de avaliação" (Critério | Atendido?).

8. SEÇÃO "Encerramento"
   - 2 parágrafos: o primeiro reafirma a finalidade cumprida e recomenda prática
     regular; o segundo aponta caminhos de aprofundamento.
   - Encerrar com uma citação ">" iniciada por "**Síntese:**", contendo a frase
     que resume a filosofia do curso.

## ESTILO OBRIGATÓRIO

- Registro: formal, impessoal e de tom acadêmico. Evite a 2ª pessoa ("você") e
  construções coloquiais; prefira voz impessoal ("recomenda-se", "observa-se",
  "cumpre registrar", "depreende-se", "convém").
- Acessibilidade ("Para Leigos") DENTRO do registro formal: explique cada conceito
  desde a base, sem pressupor conhecimento prévio, e descomplique todo termo técnico
  ao introduzi-lo — quando útil, por meio de uma analogia simples redigida em tom
  igualmente formal. Descomplicar não é informalizar: a clareza deve ser obtida sem
  recorrer a gírias, humor ou tratamento direto ao leitor.
- Sugerir a inserção de "Captura de Tela" para ilustrar instruções   
  complexas, pontos de controle ou páginas/janelas/objetos eu o aluno precise interagir.
- Terminologia técnica e precisa; evite gírias, metáforas informais e expressões
  de oralidade.
- Objetivos de aprendizagem redigidos de forma mensurável ("deverá ser capaz de...").
- Progressão pedagógica visível, porém enxuta: a nota de encadeamento de cada
  módulo deve ser breve (uma linha), sem repetições cansativas.
- Sempre que houver um conceito relevante a ser retomado adiante, plante-o em um
  módulo inicial e retome-o no módulo pertinente (fio condutor).
- Markdown limpo: cabeçalhos, listas numeradas, tabelas curtas e citações para os
  boxes. Separe oficinas com uma quebra de página (`<div style="page-break-after: always;"></div>`). Use emojis SOMENTE nos cabeçalhos e boxes previstos acima, não no corpo do texto.
- Cada exercício deve ser simples, executável no tempo indicado, e conter critério
  de êxito objetivo.

# RESTRIÇÕES
- Mantenha a coerência entre objetivos, texto descritivo e exercício de cada módulo.
- Não invente dados factuais sobre o OBJETO BASE; se a informação não estiver no
  material-fonte nem for de conhecimento consolidado, mantenha-se em formulações
  genéricas e indique a necessidade de validação.
- Não exceda a carga horária definida na soma dos tempos dos módulos.
- Produza o documento inteiro em um único arquivo Markdown, pronto para uso.

# FORMATO DE SAÍDA
Um único documento Markdown completo, do título ao encerramento, seguindo
exatamente a ordem e os elementos descritos em ESTRUTURA OBRIGATÓRIA.
```
