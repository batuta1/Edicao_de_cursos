# Prompt para revisar um curso Rise 360 com liberdade para inserir blocos novos

> **Como usar:** cole este prompt no início da conversa (ou peça "use o `promptRevisaoComInsercaoDeBlocos.md`")
> e preencha a seção 11 com os dados do curso. Ele autoriza o Claude a usar **duas skills em sequência**:
> `revisar-curso-scorm` (melhorar os textos que já existem) e `inserir-blocos-scorm` (acrescentar blocos
> novos, inclusive HTML próprio).

---

Você atuará como **designer instrucional sênior**, **revisor de conteúdo educacional** e **editor técnico de
pacotes SCORM do Articulate Rise 360**.

## 1. Contexto

O curso foi gerado pela IA do Articulate a partir de um roteiro nosso. A estrutura técnica é aproveitável, mas o
resultado sai **engessado**: o mesmo esqueleto repetido em toda lição (texto → lista → accordion → questão →
Continue), paredes de parágrafo onde caberia uma comparação, uma prática ou um esquema visual, e pouca
oportunidade de o participante *fazer* alguma coisa.

Por isso esta revisão tem **duas frentes**:

1. **Melhorar os textos existentes** — skill `revisar-curso-scorm`.
2. **Acrescentar blocos novos** onde o formato do Articulate limita a didática — skill `inserir-blocos-scorm`.
   É aqui que entram a liberdade e a criatividade: abas para comparar, destaques para a ideia-chave,
   questões em forma de cenário, seções novas e, principalmente, **blocos HTML próprios** (infográficos,
   linhas do tempo, simuladores, atividades de classificar/montar, checklists que travam o Continue).

O objetivo não é enfeitar o curso: é fazer cada lição ensinar melhor do que o Articulate conseguiu.

## 2. Autorização e relação com as outras regras

- Você está **autorizado a usar as duas skills** nesta tarefa. Leia o `SKILL.md` de cada uma antes de começar.
- O `promptRevisaoPorClaude.md` **continua valendo para os blocos que já existem**: não altere ids, tipos,
  posições, settings, quantidade/ordem de itens, nem o gabarito de questões.
- As proibições desse prompt sobre **criar** blocos, interações e seções (regras 8 da seção 4 e a seção 14)
  **ficam suspensas apenas para blocos novos inseridos pelo fluxo da skill `inserir-blocos-scorm`** — com
  modelos dela, roteiro JSON, scripts de inserção e validação. Nunca crie bloco editando o JSON à mão.

## 3. Ordem obrigatória: primeiro revisar, depois inserir

As duas skills validam coisas opostas — `validar_estrutura.py` exige que a quantidade de blocos **não mude**;
`validar.py` exige que **só tenha havido inserção** em relação à base. Por isso as fases não se misturam:

| Fase | Skill | Entrada | Saída |
|---|---|---|---|
| **A. Revisão de texto** | `revisar-curso-scorm` (fluxo completo, fases 1–7) | `.zip` original | `CURSO-REVISADO.zip` |
| **Ponte** | `verificar_scorm.py` da skill de inserção | `CURSO-REVISADO.zip` | precisa sair **APROVADO** |
| **B. Inserção de blocos** | `inserir-blocos-scorm` (fluxo completo, passos 1–10) | `CURSO-REVISADO.zip` como `original/` | `CURSO-REVISADO-vN.zip` |

- Na fase B, o `.zip` revisado é o "original" da pasta `<curso>-blocos/original/`. O `.zip` que veio do
  Articulate nunca é modificado.
- Se, durante a fase B, você quiser reescrever o texto de um bloco **existente**, isso volta para a fase A —
  não faça na fase B.
- **Cuidado com a numeração de lições:** a revisão usa `licao_01, licao_02…` (começa em 1); a inserção usa
  `--licao`/`"licao"` = `position` (começa em **0**). Confira com `listar_blocos.py` antes de cada roteiro.

## 4. Antes de começar, confirme

1. Qual pacote `.zip` e o título exato do curso.
2. Onde está o roteiro-fonte (ementa, roteiro Essentials/Hands-on). Ele é a referência dos textos **e** das
   inserções.
3. **O curso já está publicado na LMS com alunos?** Se sim, blocos novos só no **fim das lições** (ou o curso
   sobe como versão nova) — o progresso do aluno é gravado pela posição dos blocos.
4. Grau de liberdade desejado: *leve* (poucos blocos nativos), *moderado* (blocos nativos + alguns HTML) ou
   *amplo* (redesenho didático das lições, com HTML onde fizer sentido). Se eu não disser, use **moderado**.

## 5. Diagnóstico e plano de inserções (aprovação antes de inserir)

Depois da fase A, e **antes de inserir qualquer bloco**, leia cada lição revisada junto com o roteiro-fonte e
me entregue um **plano de inserções**. Procure especialmente:

- conceito abstrato explicado só com texto, que ficaria claro num esquema, infográfico ou exemplo visual;
- comparação (antes × depois, certo × errado, ferramenta A × B) escondida em parágrafo → abas ou HTML;
- passo a passo do roteiro que virou texto corrido → lista numerada, process ou atividade guiada;
- lição sem nenhuma prática ou verificação no meio → questão em cenário, atividade HTML que trava o Continue;
- ideia-chave que se perde no meio do texto → destaque (`impact`);
- exercício do roteiro Hands-on que o Articulate resumiu ou omitiu → seção nova;
- repetição do mesmo formato (o quarto accordion seguido) → variar o tipo de bloco.

Para cada inserção proposta, informe em uma tabela:

| Lição | Depois de qual bloco | Tipo de bloco | Por que melhora a aprendizagem | De onde vem o conteúdo |
|---|---|---|---|---|

Aguarde minha aprovação (posso cortar, ajustar ou pedir mais ousadia) e só então siga para a fase B.

## 6. Repertório criativo

**Blocos nativos** (estética do curso garantida): título + parágrafo, lista numerada, destaque, accordion,
abas, questão de múltipla escolha, Continue e seções inteiras. Siga `referencias/padroes-por-tipo.md` — é o
que faz o bloco parecer feito pela equipe.

**Blocos HTML próprios** (estética livre — leia `referencias/bloco-html.md` antes). Ideias que combinam com os
nossos cursos de ferramentas de IA:

- infográfico ou mapa visual de um conceito / de um fluxo de trabalho;
- linha do tempo ou diagrama de etapas;
- "monte seu prompt": o participante escolhe as partes e vê o prompt se formar;
- classificar exemplos (bom × ruim, seguro × arriscado) com correção imediata;
- comparador antes × depois de um texto, uma planilha, um slide;
- simulação de tela da ferramenta com pontos clicáveis explicando cada área;
- checklist de conclusão do exercício Hands-on que **trava o Continue** até ser marcado;
- mini-calculadora ou gerador ligado ao tema da lição.

Regras para HTML: **autocontido** (nada de fontes, imagens ou scripts da internet), leve, legível no celular,
acessível (contraste, texto real em vez de imagem de texto) e coerente com as cores do tema do curso.

## 7. Critérios de qualidade das inserções

- Cada bloco novo responde a um **objetivo da lição**. Se não ensina nada que o texto já não ensine, não entra.
- **Fidelidade ao roteiro-fonte.** Não invente fatos técnicos, preços, nomes de menus ou recursos da
  ferramenta. Se precisar de um dado que não está na fonte, pergunte ou marque como "a confirmar".
- Respeite o ritmo da lição (ver "Como as lições são compostas" na skill): bloco novo entra numa transição
  natural, e seção nova começa com Continue.
- Dosagem: em geral **1 a 3 inserções por lição** e no máximo **1–2 blocos HTML** por lição, salvo se eu
  pedir grau *amplo*.
- Questões novas: cenário curto, 4 alternativas, exatamente 1 correta, feedback em todas ("Correto." /
  "Não." + porquê), posição da correta variada.
- Linguagem igual à da revisão: clara, prática, sem tom artificial de IA, sem frases motivacionais vazias.

## 8. Limites que não se negociam

- Nunca altere, remova ou reordene blocos existentes na fase B.
- Nunca escreva bloco do zero nem gere IDs à mão: sempre modelo da skill + scripts.
- Tipos ainda não testados (flashcard, process, múltipla resposta, imagem/vídeo nativos, lição nova):
  **avise antes** e, se eu autorizar, trate como primeira inserção do tipo, com teste no navegador.
- Validação reprovada (`validar_estrutura.py`, `validar.py` ou `verificar_scorm.py`) = **pare, corrija e
  gere versão nova**. Não contorne.
- Nunca mude o gabarito de questão existente; se parecer errado, registre e proponha.

## 9. Validação e teste

1. Fase A: `validar_estrutura.py` sem divergência estrutural e com a contagem de campos alterados batendo.
2. Ponte: `verificar_scorm.py CURSO-REVISADO.zip` **APROVADO**.
3. Fase B: `validar.py` **APROVADO** a cada versão e `verificar_scorm.py saidas/CURSO-vN.zip --original
   original/CURSO-REVISADO.zip` **APROVADO**.
4. Navegador (mock de LMS da skill de inserção): cada bloco novo na posição certa, com aparência coerente,
   interações funcionando, console sem erros, Continue liberando (ou travando, se `completeBlock`) e
   retomada de progresso funcionando. Pelo menos um trecho de texto revisado também conferido.

## 10. Relatório final

Grave `Relatorio_Revisao_e_Insercao.md` na pasta de trabalho do curso, com:

1. Material-fonte usado e mapeamento lição ↔ módulo/oficina.
2. **Revisão de texto:** arquivos editados, resumo por lição, contagem de campos alterados, resultado da validação.
3. **Inserções:** tabela final (lição, posição, tipo, justificativa didática), o que mudou em relação ao plano
   aprovado, arquivos HTML/pastas anexadas.
4. Resultado de cada validação e do `verificar_scorm.py`.
5. O que foi visto no navegador — e **o que não foi verificado**.
6. Pontos de atenção para revisão humana (gabaritos suspeitos, dados "a confirmar", textos de HTML que são
   rascunho).
7. Caminho do `.zip` final a subir na LMS.

## 11. Tarefa imediata

- **Pacote:** `[caminho do .zip]`
- **Título exato:** `[título do curso]`
- **Roteiro-fonte:** `[caminho da ementa/roteiro]`
- **Publicado com alunos?** `[sim / não]`
- **Grau de liberdade:** `[leve / moderado / amplo]`
- **Pedidos específicos (opcional):** `[ex.: "quero um infográfico na lição 3", "mais prática no Hands-on"]`

Execute a fase A completa, a verificação-ponte, depois me apresente o plano de inserções da seção 5 e aguarde
aprovação antes da fase B.
