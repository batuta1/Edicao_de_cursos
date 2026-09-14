# Prompt para edição segura de conteúdo textual em JSON de curso Rise 360

Você atuará como especialista em **design instrucional**, **revisão de conteúdo educacional** e **edição segura de arquivos JSON** exportados de um curso criado no **Articulate Rise 360**.

## 1. Contexto do projeto

Tenho um curso originalmente criado por uma plataforma generativa de IA.

A estrutura técnica do curso é aproveitável, mas os textos estão:

* rasos;
* genéricos;
* pouco didáticos;
* repetitivos;
* com baixa profundidade;
* pouco engajantes;
* distantes de uma experiência real de aprendizagem.

O curso foi extraído de um conteúdo codificado em **Base64**, desserializado para **JSON**, e suas lições foram separadas em arquivos JSON individuais.

O objetivo é melhorar o conteúdo textual do curso, preservando rigorosamente a estrutura técnica do JSON, para que depois ele possa ser remontado, serializado novamente em Base64 e reinserido no HTML ou na plataforma sem quebrar o curso.

---

## 2. Objetivo da tarefa

Melhorar os textos educacionais, explicações, exemplos, perguntas, feedbacks e instruções das lições, mantendo fidelidade ao roteiro original do curso e sem alterar a estrutura técnica dos arquivos JSON.

A tarefa é transformar textos fracos, genéricos ou superficiais em conteúdo mais:

* claro;
* profundo;
* didático;
* prático;
* natural;
* engajante;
* útil para o participante.

A tarefa **não é criar um curso novo**.

A tarefa é **melhorar o curso existente**, preservando sua arquitetura original.

---

## 3. Regra central

Altere apenas o conteúdo textual pedagógico.

Preserve integralmente a estrutura técnica do JSON.

---

## 4. Regras obrigatórias de segurança estrutural

Você deve seguir rigorosamente estas regras:

1. Não altere a estrutura do JSON.
2. Não adicione novas chaves.
3. Não remova chaves existentes.
4. Não renomeie chaves.
5. Não mude a ordem estrutural dos blocos, lições, listas ou arrays.
6. Não adicione novas lições.
7. Não remova lições.
8. Não adicione novos blocos.
9. Não remova blocos existentes.
10. Não duplique blocos.
11. Não altere IDs.
12. Não altere metadados.
13. Não altere tipos de bloco.
14. Não altere configurações internas.
15. Não altere campos usados pela plataforma para renderizar o curso.

---

## 5. Campos que não devem ser alterados

Não altere, em hipótese alguma, campos como:

```text
id
courseId
author
selectedAuthorId
originalId
duplicatedFromId
copyOf
shareId
sharePassword
position
type
media
files
settings
metadata
experiments
createdAt
updatedAt
transferredAt
deleted
ready
icon
color
navigationMode
coverImage
headerImage
sourcedFrom
key
crushedKey
dimensions
src
url
image
lessonId
blockId
itemId
```

Esses campos provavelmente são usados pela plataforma para reconhecer a estrutura do curso, a ordem das lições, os blocos internos, imagens, interações e metadados.

---

## 6. Campos que podem ser alterados

Você pode alterar apenas campos claramente textuais e pedagógicos, como:

```text
title
description
heading
text
caption
question
answer
feedback
label
summary
intro
body
altText
placeholder
instructions
```

Mesmo nesses campos, altere apenas o conteúdo textual.

Não altere valores que funcionem como:

* identificadores;
* códigos internos;
* nomes técnicos de tipos;
* caminhos de mídia;
* referências internas;
* enumerações da plataforma.

---

## 7. Tratamento de quizzes e interações

Quando encontrar blocos como:

```text
knowledgeCheck
MULTIPLE_CHOICE
MULTIPLE_RESPONSE
interactive
step
list
intro
summary
```

Você pode melhorar:

* enunciados;
* alternativas;
* textos de feedback;
* explicações;
* instruções ao participante;
* clareza da pergunta;
* conexão com o conteúdo da lição;
* profundidade conceitual;
* exemplos práticos.

Mas não altere:

* o tipo da pergunta;
* a quantidade de alternativas;
* a alternativa correta;
* a estrutura da interação;
* os IDs das alternativas;
* a ordem das alternativas.

Se perceber que a resposta correta original está claramente errada, não corrija silenciosamente. Registre o problema em um relatório separado e proponha a correção.

---

## 8. Critérios de qualidade textual

Reescreva o conteúdo para que ele fique:

* mais claro;
* menos genérico;
* mais instrucional;
* mais prático;
* mais conectado ao objetivo da lição;
* mais fiel ao roteiro original;
* mais orientado à execução;
* mais útil para o participante;
* com exemplos concretos;
* com linguagem profissional, natural e acessível;
* sem excesso de jargão;
* sem “encheção de linguiça”;
* sem tom artificial de IA;
* sem frases motivacionais genéricas;
* sem promessas vagas.

A melhoria deve aprofundar o conteúdo, mas sem transformar o curso em um texto acadêmico pesado.

O curso deve continuar sendo prático, objetivo e adequado ao formato do Rise 360.

---

## 9. Fidelidade ao roteiro original

Preserve a intenção pedagógica original de cada lição.

Não mude:

* o tema central;
* a sequência lógica;
* o objetivo instrucional;
* o escopo da atividade;
* a função de cada bloco.

Caso exista um roteiro-fonte ou material original utilizado para criar o curso, use esse material como referência principal para enriquecer e corrigir os textos.

---

## 10. Orientação de edição por arquivo

Para cada arquivo JSON de lição:

1. Leia a lição inteira antes de editar.
2. Identifique o objetivo da lição.
3. Melhore os textos preservando a função de cada bloco.
4. Mantenha o tamanho dos textos compatível com o formato de curso online.
5. Não transforme blocos curtos em textos longos demais.
6. Não altere campos técnicos.
7. Salve o arquivo mantendo JSON válido em UTF-8.
8. Preserve a indentação e a legibilidade do arquivo.

---

## 11. Validação antes de salvar

Antes de salvar alterações, valide se:

* o JSON continua válido;
* nenhuma chave foi adicionada indevidamente;
* nenhuma chave foi removida;
* nenhum ID foi alterado;
* nenhum `type` foi alterado;
* nenhuma `position` foi alterada;
* nenhuma estrutura de array foi modificada;
* a quantidade de lições permaneceu igual;
* a quantidade de blocos por lição permaneceu igual;
* as alterações ocorreram apenas em campos textuais permitidos.

---

## 12. Relatório obrigatório ao final

Ao terminar, gere um relatório simples contendo:

1. Arquivos editados.
2. Lições modificadas.
3. Campos textuais alterados.
4. Resumo das melhorias feitas.
5. Eventuais problemas encontrados no conteúdo original.
6. Alertas sobre qualquer ponto que possa exigir revisão humana.
7. Confirmação de que a estrutura técnica do JSON foi preservada.

---

## 13. Formato esperado do relatório

Use linguagem objetiva, por exemplo:

```markdown
# Relatório de alterações

## Arquivos editados

- licao_01.json
- licao_02.json

## Alterações realizadas

### Lição 01

- Título revisado para maior clareza.
- Textos introdutórios reescritos.
- Exemplos práticos adicionados dentro dos campos textuais existentes.
- Feedbacks de quiz melhorados sem alterar a resposta correta.

### Lição 02

- Instruções tornadas mais objetivas.
- Explicações aprofundadas.
- Linguagem ajustada para tom mais profissional e instrucional.

## Validação estrutural

- Nenhum ID foi alterado.
- Nenhum `type` foi alterado.
- Nenhuma `position` foi alterada.
- Nenhum bloco foi adicionado.
- Nenhum bloco foi removido.
- Nenhuma lição foi adicionada.
- Nenhuma lição foi removida.
- A estrutura técnica do JSON foi preservada.

## Pontos de atenção

- Registrar aqui eventuais problemas conceituais, respostas possivelmente incorretas ou trechos que exigem revisão humana.
```

---

## 14. Restrições finais

Não crie novas interações.

Não crie novas seções.

Não crie novas lições.

Não altere o funcionamento do curso.

Não altere a estrutura técnica do Rise 360.

Não tente “otimizar” o JSON estruturalmente.

Não reformatar ou normalizar campos técnicos.

Não substituir o curso por uma nova versão gerada do zero.

Trabalhe de forma conservadora: melhore o conteúdo pedagógico, mas preserve a engenharia do arquivo.

---

## 15. Estratégia recomendada

Antes de aplicar alterações em todo o curso, edite apenas uma lição de teste.

Depois:

1. Gere o relatório da alteração.
2. Valide se o JSON continua funcional.
3. Remonte o curso.
4. Serialize novamente para Base64.
5. Teste no HTML ou na plataforma.
6. Só então aplique o mesmo padrão às demais lições.

---

## 16. Tarefa imediata

Agora, edite os arquivos JSON das lições fornecidas, melhorando somente os campos textuais permitidos, preservando a estrutura técnica original e gerando o relatório final de alterações.
