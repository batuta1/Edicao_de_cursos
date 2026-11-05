# 02 — Análise crítica 360 · Perplexity - Essentials (Hands-on, v1.0)

Entrada: `_processo/01-v1-hands-on.md` + `_processo/00-contornos.md`.
Contexto: objeto base Perplexity (Search); público duplo (T2 pesquisa; J2 jurídico); pré-requisito uso
básico de assistente de IA; trilha Hands-on; autoinstrucional; alvo 90–120 min; plano gratuito.

## 1. Sumário Executivo

**Nota: 4,5 / 10.** O tom em 2ª pessoa e a sequência de oficinas estão certos, mas quase todos os
passos esbarram na interface real ou no plano gratuito, e o curso ensina o aluno a **confiar** onde
deveria ensiná-lo a **conferir**. A "vitória" de cada oficina é ver algo aparecer na tela, não
produzir uma evidência.

Principais constatações:

- Rótulos que não existem na interface pt-BR atual ("Seletor de modos (Best, Pro, Research)",
  "Spaces > Create Space", Pages).
- Oficina 2 consome a única Research mensal do plano gratuito e a cota diária de Pro; "Research
  demora — espere" não informa quanto nem o que fazer enquanto isso.
- Oficina 3 manda "ver se o site é confiável" sem critério e sem abrir o trecho que sustenta a frase.
- `site:gov.br` ensinado como se funcionasse — sem suporte documentado.
- Projeto Final terceiriza a síntese à IA e manda compartilhar sem revisão; Thread público é
  publicação.
- Nenhuma segurança (o que não entra na pergunta, Retenção de Dados de IA, navegação anônima).
- O público jurídico não tem uma única tarefa; não há prova de existência em repositório oficial.
- "A Parte dos Dez" enche linguiça ("Assine o Pro", "Compartilhe Pages", itens repetidos).
- Carga declarada de 80 min, abaixo da faixa 90–120.

## 2. Pontos Positivos (Fortalezas)

| Fortaleza | Por que é um acerto |
|---|---|
| 2ª pessoa, frases curtas, verbos no início | Registro correto da trilha Hands-on. |
| Um problema por oficina | Estrutura PBL presente; falta tornar os problemas reais e encadeados. |
| Tema LGPD já nas Oficinas 1 e 2 | Tema público e útil aos dois públicos; vale virar tema-âncora de todo o curso. |
| Oficina 3 dedicada às fontes | O lugar certo existe; o conteúdo precisa de método. |
| Projeto Final em tema próprio | Transfere a habilidade para o contexto do aluno. |

## 3. Pontos Negativos e Gargalos (Debilidades)

### 3.1 Clareza e executabilidade

- **Oficina 1:** "Crie sua conta" sem opções (e-mail, Google) nem aviso de que dá para testar sem
  login. A pergunta "O que é a LGPD?" é justamente a pergunta vaga que o curso deveria ensinar a
  reformular.
- **Oficina 2:** "Clique no seletor de modos" — não há seletor com esses três nomes na tela pública
  pt-BR (18/10/2026). Sem rota para quem não vê Pesquisa Pro ou já usou a cota.
- **Oficina 3:** "veja se o site é confiável" não é ação verificável. Falta abrir a página, achar o
  trecho e compará-lo com a frase.
- **Oficina 4:** caminho `Spaces > Create Space` desatualizado (Projetos, `Criar projeto`, desde
  04/08/2026). "Share e copie o link" sem revisar o que fica exposto.
- **"Deu certo?"** mede presença de elementos ("apareceu", "você abriu"), não acerto.

### 3.2 Rigor técnico

- Focos legados; atuais em "Aplicativos e mais": Finanças, Saúde, Acadêmico, Patentes [conferir com
  login].
- `site:`/booleanos sem garantia; a alternativa é instruir os domínios e conferir link a link.
- Pages sem confirmação atual — não pode ser passo nem desafio.
- Contexto herdado no follow-up: sem orientação de quando começar nova pesquisa.

### 3.3 Segurança e riscos

- Nada sobre dados pessoais, sigilo, segredo profissional, peça de cliente ou fonte jornalística na
  pergunta ou no upload.
- Nada sobre Retenção de Dados de IA, Memória e navegação anônima (que não é anonimato total).
- Compartilhamento público como meta de sucesso do Projeto Final.
- Jurídico: sem os casos de sanção (TJPR, STJ, TSE) nem a regra "IA dá pistas; o tribunal confirma".

### 3.4 Engajamento

- Regra de ouro genérica ("errar faz parte"). A regra que este curso precisa é: **citação é trilha,
  não prova**.
- Problemas abstratos ("entender um assunto rápido"); faltam situações reconhecíveis por perfil
  (crédito negado por sistema automático, pauta de reportagem, parecer, trabalho de faculdade).
- "Quer ir além?" com um desafio só e sem forma de validação (o prompt-mestre pede três).

## 4. Matriz de Soluções e Melhorias

| # | Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|---|
| H1 | Segurança ausente | Todo o curso | Na abertura, "semáforo da pergunta" (verde/amarelo/vermelho) e conferência de `Configurações` (Retenção de Dados de IA, Memória, navegação anônima) **antes** da Oficina 1 | Crítica |
| H2 | Setup incompleto | Oficina 1 | Mover para "Antes de Arregaçar as Mangas": login opcional e o que ele libera; conta por e-mail/Google; registro de rótulos vistos | Alta |
| H3 | Rótulos inexistentes | Oficinas 2 e 4 | Breadcrumbs a partir da tela pt-BR de 18/10/2026; tabela de equivalência; **[conferir]** onde o rótulo não foi visto | Crítica |
| H4 | Dependência de Research e cota Pro | Oficina 2 | Comparar busca padrão × Pesquisa Pro; plano B: mesma pergunta com domínios oficiais; Research fora dos passos | Crítica |
| H5 | Não ensina a formular | Oficina 1 | Oficina 1 vira "Da pergunta vaga à pergunta pesquisável" com a estrutura oficial em cinco partes | Crítica |
| H6 | Conferência sem método | Oficina 3 | Ficha de auditoria (existe? quem publicou? data? trecho? escopo? primária?) para duas citações + prova de existência do acórdão TJPR | Crítica |
| H7 | `site:` como certeza | Oficina 3 | Trocar por instrução de domínios e contagem de citações que obedeceram | Alta |
| H8 | Pages e link público | Oficina 4 e Projeto | Remover Pages; compartilhar vira decisão (sim/não + motivo), com revisão prévia do Thread | Alta |
| H9 | Síntese terceirizada | Projeto Final | O aluno pede rascunho, audita cada parágrafo, reescreve frases sem apoio e escreve "Limites desta síntese" | Crítica |
| H10 | Jurídico ausente | Todo o curso | Prova de existência TJPR na Oficina 3; perfil jurídico no Projeto Final com repositório oficial | Alta |
| H11 | Parte dos Dez com enchimento | Fecho | Dez hábitos reais de pesquisa verificável, sem venda de plano e sem itens repetidos | Média |
| H12 | Um desafio só | Todas as oficinas | Três desafios por oficina, cada um com validação | Média |
| H13 | Carga horária fora da faixa | Mapa | Recalcular pela MET; alvo 90–120 | Alta |
| H14 | Regra de ouro genérica | Abertura | "A citação mostra onde conferir, não prova que está certo" | Alta |
| H15 | Problemas abstratos | Todas as oficinas | Problema encadeado: crédito negado por sistema automático (LGPD, art. 20) do começo ao fim | Média |
| H16 | Tema que não se acumula | Oficinas 1–4 | O mesmo Thread/Projeto atravessa as quatro oficinas; o Projeto Final repete o fluxo em tema próprio | Média |

## 5. Roadmap de Expansão

| Tópico | Cabe neste curso? | Destino |
|---|---|---|
| Upload de PDF com pergunta por páginas | Sim, como desafio opcional | Oficina 4 |
| Prompt de autoauditoria | Sim | Oficina 3 |
| Teste de referência inexistente (número de processo inventado) | Sim, como desafio | Oficina 3 |
| Comparação oficial × reportagem | Sim, como desafio | Oficina 2 |
| Research auditado | Não | *Deep Research - Hands On* |
| Comet, Computer, Create files and apps | Não | Fronteira (uma frase) |

## 6. O que não pôde ser verificado

- Posição exata de "Pesquisa Pro" e de Research na tela **logada** do plano gratuito.
- Se `Criar projeto` e a instrução do Projeto estão disponíveis no gratuito (a ajuda é ambígua).
- Rótulo pt-BR atual de "Retenção de Dados de IA" dentro de Configurações e se o opt-out vale no
  gratuito.
Esses pontos foram tratados como **[conferir]** nos roteiros e listados no `README.md`.
