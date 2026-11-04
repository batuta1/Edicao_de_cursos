# Plano de Aula — Checagem de Fontes e Citações (Essentials)

## Identificação

| Campo | Definição |
|---|---|
| Curso | Checagem de Fontes e Citações - Essentials |
| Natureza | Curto, introdutório e prático |
| Carga horária | 90 minutos |
| Público-alvo | Estudantes, pesquisadores, jornalistas, analistas e profissionais do Direito |
| Pré-requisitos | Uso básico de assistentes de IA |
| Recursos necessários | Computador com internet; contas na Scite e na Perplexity |

### Objetivo Geral

O curso tem por finalidade capacitar o participante a verificar afirmações acompanhadas de citação, determinando se a obra citada existe, o que efetivamente afirma e se apoia ou contesta a alegação, com apoio da Scite e da Perplexity. Como produto final, o participante entrega a auditoria documentada de um conjunto de pares afirmação-citação.

### Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Reconhecer os tipos de erro de citação produzidos por ferramentas de IA.
2. Confirmar a existência de uma obra por meio de DOI e metadados.
3. Verificar o que a fonte afirma, com apoio da Perplexity.
4. Interpretar Smart Citations da Scite para avaliar apoio e contestação.

### Estrutura e Sequência dos Módulos

Os módulos seguem progressão cumulativa: do problema ao método, e do método às ferramentas.

| Módulo | Título | Referência | Tempo |
|---|---|---|---|
| 1 | Por que citações geradas por IA falham | Walters e Wilder (2023); Tow Center (2025) | 15 min |
| 2 | Existência: DOI e metadados | DOI Foundation; Crossref | 15 min |
| 3 | Fidelidade: o que a fonte diz | Ajuda Perplexity (Pro Search) | 20 min |
| 4 | Apoio e contestação com a Scite | Scite Features; Nicholson et al. (2021) | 20 min |
| 5 | Síntese e Aplicação Integrada | Módulos 1 a 4 | 20 min |

---

# Módulo 1 — Por que citações geradas por IA falham

> Ponto de partida: apresenta o problema que justifica o método.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Distinguir referência fabricada de referência real com erro.
2. Reconhecer que citação visível não garante atribuição correta.
3. Explicar as consequências de citações inventadas em contextos profissionais.

### Texto Descritivo

Os modelos de linguagem produzem texto plausível, e não necessariamente verdadeiro. Ao serem solicitados a fornecer referências, podem gerar obras inexistentes ou atribuir dados incorretos a obras reais. Estudos mostram que uma parcela relevante das referências geradas é fabricada.

Os motores de resposta com busca na web, como a Perplexity, reduzem o problema ao apresentar links, mas não o eliminam. Testes independentes identificaram erros frequentes de atribuição mesmo em respostas com citações.

No Brasil, tribunais já registraram petições com precedentes inexistentes, o que levou a multas e comunicações à OAB. Em pesquisa acadêmica, o uso de referências inventadas compromete a integridade do trabalho.

### Exercício Prático

Classificação de erros (5 min)

Uma referência indica autor, título e periódico reais, mas o ano e as páginas estão errados. Trata-se de:

a) referência fabricada;
b) referência real com erro de metadados;
c) referência correta;
d) referência retratada.

**Gabarito:** b. **Fundamentação:** a obra existe; o erro está nos metadados.

---

# Módulo 2 — Existência: DOI e metadados

> Pré-requisito: Módulo 1. Foco: confirmar que a obra existe.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Resolver um DOI.
2. Conferir metadados no Crossref.
3. Registrar a busca quando a obra não é localizada.

### Texto Descritivo

O DOI (Digital Object Identifier) é um identificador persistente de um objeto digital. Ao ser digitado após `https://doi.org/`, o resolvedor encaminha ao endereço registrado. O Crossref permite buscar metadados por título, autor ou DOI.

Recomenda-se comparar título, autores, periódico, ano, volume e páginas. Um campo divergente pode indicar erro de transcrição, e não inexistência.

Quando a obra não é localizada, convém registrar as bases consultadas e a data, sem concluir além do que foi pesquisado.

### Exercício Prático

Verificação de DOI (10 min)

1. Acessar `https://doi.org/10.1162/qss_a_00146`.
2. Conferir título, autores e ano.
3. Pesquisar o DOI 10.9999/ia-clube.2026.001 no DOI.org e no Crossref.

**Critério de êxito:** o primeiro DOI resolve para o artigo de Nicholson et al. (2021); o segundo não é localizado.

---

# Módulo 3 — Fidelidade: o que a fonte diz

> Pré-requisito: Módulo 2. Foco: do registro ao conteúdo.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Usar a Perplexity para localizar a fonte original de uma afirmação.
2. Abrir o original e localizar o trecho pertinente.
3. Classificar a relação entre afirmação e fonte.

### Texto Descritivo

A Perplexity é um mecanismo de respostas que pesquisa a web e devolve uma síntese com citações. O Pro Search realiza buscas sucessivas; o modo Academic restringe as fontes à literatura acadêmica. A própria ajuda da ferramenta recomenda validar os links.

Verificar a fidelidade consiste em abrir a fonte, localizar o trecho com a função Localizar do navegador e ler o contexto: método, população, limitações. Uma fonte pode existir e não sustentar a afirmação.

### Exercício Prático

Afirmação que não se sustenta (15 min)

1. Na Perplexity, em modo Academic, perguntar sobre a acurácia do classificador da Scite.
2. Abrir o artigo de Nicholson et al. (2021).
3. Verificar se o artigo sustenta a afirmação "99% de acurácia em todas as classes".

**Critério de êxito:** concluir que o artigo existe, mas não sustenta a afirmação.

---

# Módulo 4 — Apoio e contestação com a Scite

> Pré-requisito: Módulo 3. Foco: o que a literatura posterior diz.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Explicar o que é uma Smart Citation.
2. Interpretar os rótulos Supporting, Contrasting e Mentioning.
3. Usar o Reference Check para avaliar uma bibliografia.

### Texto Descritivo

A Scite é uma plataforma de pesquisa acadêmica que extrai o trecho em que um artigo cita outro e classifica a relação como Supporting (apoia), Contrasting (contesta) ou Mentioning (menciona). Essa unidade é chamada Smart Citation.

O Report de um artigo reúne as citações recebidas e permite filtrá-las por classificação. O Reference Check recebe um manuscrito em PDF e sinaliza referências retratadas ou com evidência contrastante.

### Exercício Prático

Leitura de Smart Citations (15 min)

1. Acessar scite.ai e buscar o DOI 10.1177/0956797610383437.
2. Abrir o Report e filtrar por Contrasting.
3. Ler duas citações contrastantes.

**Critério de êxito:** identificar ao menos uma citação que contesta o efeito hormonal do power posing.

---

# Módulo 5 — Síntese e Aplicação Integrada

> Pré-requisito: Módulos 1 a 4. Foco: aplicar o fluxo completo.

### Objetivos de Aprendizagem

Ao final deste módulo, o participante deverá ser capaz de:

1. Aplicar o fluxo existência–fidelidade–apoio a um conjunto de citações.
2. Documentar cada decisão.

### Texto Descritivo

O fluxo completo integra as etapas anteriores: confirmar a existência, abrir o original, verificar o trecho, consultar a literatura posterior e registrar a decisão.

### Exercício Prático

Atividade integradora (20 min)

Auditar cinco pares afirmação-citação fornecidos, preenchendo uma ficha com existência, trecho e decisão.

| Critério | Atendido? |
|---|---|
| Existência verificada em cada par | |
| Trecho localizado | |
| Decisão registrada | |

---

# Encerramento

O curso apresentou um método para verificar citações com apoio de IA. Recomenda-se aplicá-lo regularmente.

Para aprofundamento, sugere-se o curso de revisão bibliográfica com IA.

> **Síntese:** a IA ajuda a encontrar, mas quem verifica é o pesquisador.
