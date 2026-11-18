# Ementa — ChatGPT (Codex) no VS Code

## Identificação

| Campo | Definição |
|---|---|
| Curso | ChatGPT (Codex) no VS Code — trabalho com pastas de arquivos para quem não programa |
| Natureza | Curto, introdutório, prático e autoinstrucional |
| Trilhas | Essentials e Hands-on |
| Carga horária total | 238 minutos (3 h 58 min) — Essentials 125 min; Hands-on 113 min |
| Público-alvo | Professores universitários, de qualquer área, que não programam e não pretendem programar |
| Pré-requisitos | Saber criar pastas, mover arquivos e localizar uma pasta no computador; conta ativa no ChatGPT, ainda que gratuita; permissão para instalar programas; nenhum conhecimento de programação |
| Recursos necessários | Computador com Windows, macOS ou Linux, com permissão de instalação; Visual Studio Code; extensão Codex; internet ativa; conta ChatGPT; uma pasta de trabalho real, da qual se fará cópia no início do curso |
| Material-fonte | Central de Ajuda da OpenAI ("Usando o Codex com seu plano ChatGPT") e anúncio do GPT-5-Codex. Ver pendências de validação ao final. |

## Objetivo Geral

O curso destina-se a habilitar o docente do ensino superior, ainda que sem qualquer conhecimento de
programação, a empregar o Codex no Visual Studio Code como assistente para o trabalho com pastas de
arquivos — organizar material, consultar conjuntos de documentos, converter formatos e produzir
análises simples —, compreendendo o modelo de permissões que governa o que o agente pode fazer e
mantendo controle sobre os próprios arquivos em todas as etapas. Ao término, espera-se que o
participante tenha entregue, na trilha Hands-on, a pasta de uma disciplina padronizada, indexada e
acompanhada de um arquivo de instruções que faz o padrão se repetir sem redigitação.

## Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Distinguir um sistema que responde de um agente que executa, e estabelecer os limites do agente —
   nível de aprovação, cópia de segurança e o que fica fora da pasta de trabalho — antes do primeiro
   uso.
2. Reconhecer, na própria rotina, quais tarefas cabem no agente e quais não cabem, aplicando as três
   condições de adequação e as três razões de recusa.
3. Formular um pedido contendo padrão, restrição de preservação e exigência de proposta prévia, e
   revisar a proposta pelas três verificações antes de aprovar.
4. Registrar em arquivo de instruções, em português, as regras permanentes de uma pasta, de modo que
   o agente as observe sem que precisem ser repetidas a cada pedido.

## Estrutura das Trilhas

As trilhas são complementares e podem ser cursadas em sequência ou isoladamente. A trilha Essentials
constrói o entendimento — o que muda quando um sistema executa em vez de responder, o que os níveis
de aprovação controlam, para que isto serve a um docente, e como se formula um pedido conferível. A
trilha Hands-on exercita a execução, levando o participante da instalação à entrega de uma pasta de
disciplina organizada. Recomenda-se a ordem Essentials → Hands-on; quem optar por começar pela
Hands-on **não deve, em nenhuma hipótese, pular a Oficina 0**.

> **Nota de posicionamento.** Já existe na pasta `../Codex/` um curso anterior sobre o Codex, de
> recorte generalista. Este curso trata do mesmo objeto com público e recorte distintos: docentes que
> não programam, aplicando o agente a material de aula e dados de pesquisa. Antes de publicar os
> dois, convém decidir se coexistem ou se um substitui o outro.

### Trilha Essentials — 125 min

| Módulo | Título | Tempo |
|---|---|---|
| 0 | Antes de deixar um agente perto dos seus arquivos | 22 min |
| 1 | O que o Codex faz com uma pasta sua | 18 min |
| 2 | Instalar o editor e a extensão | 21 min |
| 3 | Pedir, revisar, aprovar | 22 min |
| 4 | Ensinar ao Codex as regras da sua pasta | 22 min |
| 5 | Síntese e Aplicação Integrada | 20 min |

### Trilha Hands-on — 113 min

| Oficina | Título | Tempo |
|---|---|---|
| 0 | Antes de soltar um assistente na sua pasta | 7 min |
| 1 | Instalar e experimentar sem risco | 20 min |
| 2 | Arrumar uma pasta bagunçada | 20 min |
| 3 | Perguntar aos seus arquivos | 20 min |
| 4 | Um gráfico sem programar | 20 min |
| — | Projeto Final — Uma disciplina que se organiza sozinha no semestre que vem | 26 min |

A trilha Hands-on inclui ainda o apêndice "A Parte dos Dez — Coisas que Funcionam no Codex", de
consulta rápida, e quinze desafios opcionais de extensão. Nenhum dos dois integra a carga horária
nominal.

## Distribuição da Carga Horária

| Trilha | Atividades | Teoria | Prática | Total |
|---|---|---|---|---|
| Essentials | 17 | 41 min (32,8 %) | 84 min (67,2 %) | 125 min |
| Hands-on | 17 | 30 min (26,5 %) | 83 min (73,5 %) | 113 min |
| **Total geral** | **34** | **71 min (29,8 %)** | **167 min (70,2 %)** | **238 min** |

Proporção alvo para iniciantes: 40 % teoria / 60 % prática. O curso combinado apura 29,8 % / 70,2 %,
desviando no sentido de mais prática — o maior desvio dos três cursos deste lote. A explicação é o
público: docentes que não programam precisam de mais execução acompanhada, e não de mais exposição,
para vencer a barreira de um editor de código. Não se recomenda correção. O detalhamento atividade a
atividade consta de `carga-horaria/`.

## Avaliação

Não há prova nem nota. A verificação da aprendizagem é feita pelo próprio participante, por critérios
objetivos, como convém a um curso autoinstrucional:

| Instrumento | Onde | Como se verifica |
|---|---|---|
| Critérios de êxito dos exercícios | Cada módulo da trilha Essentials | Resultado observável descrito no próprio exercício (ex.: a contagem de arquivos permaneceu a mesma após a renomeação) |
| Tabela de critérios de avaliação | Módulo 5 da trilha Essentials | Sete critérios de marcação sobre a Atividade Integradora |
| Pontos de controle | Cada oficina da trilha Hands-on | Estado verificável na interface (ex.: três pastas no explorador de arquivos; os nomes no padrão pedido na barra lateral; a imagem do gráfico abrindo no editor) |
| Checklist do Projeto Final | Trilha Hands-on | Dez itens de marcação sobre a pasta entregue |

O curso adota três critérios transversais, presentes em ambas as trilhas: o trabalho ocorre sempre na
cópia, permanecendo a pasta original intacta; toda proposta do agente é revisada por amostragem —
cinco itens, não um — antes da aprovação; e a contagem de arquivos após qualquer operação é conferida
contra a original.

## Pendências de Validação

Os pontos abaixo devem ser conferidos antes da publicação. O primeiro é de outra ordem que os
demais.

1. **Comportamento do Codex em pastas que não são repositórios de código.** O material-fonte descreve
   fluxos de desenvolvimento de software; o recorte acadêmico deste curso — renomear material de
   aula, consultar textos, gerar gráfico a partir de dados exportados — **não foi testado na
   prática**. Todo o curso repousa sobre esse pressuposto, e as quatro oficinas da trilha Hands-on
   dependem dele. **Esta é a pendência de primeira ordem: valide-a antes de qualquer outra, e antes
   de investir na produção do curso.** Se o comportamento divergir, o cálculo de carga horária também
   precisa ser refeito.
2. **Nome exato e editor da extensão Codex** na loja de extensões do Visual Studio Code, e o caminho
   de interface para instalá-la. Usado no Módulo 2 da Essentials e na Oficina 1 da Hands-on.
3. **Se o modo somente leitura é ajustável a partir da extensão do VS Code**, ou apenas pela linha de
   comando e pelo arquivo de configuração. O curso instrui a configurá-lo na extensão, e essa
   instrução sustenta toda a estratégia de segurança de ambas as trilhas.
4. **Aparência atual do painel do Codex** no VS Code e nomes dos controles em português.
5. **Disponibilidade do comando de inicialização do arquivo de instruções a partir da extensão.** O
   material-fonte o documenta para o aplicativo de desktop e para a linha de comando. O Módulo 4 da
   Essentials já está redigido de forma condicional, com a alternativa de criar o arquivo à mão.
6. **Limites de uso por plano** e quanto rende, na prática, o plano gratuito — dado que a cota é
   compartilhada com o ChatGPT Work, o ChatGPT para Excel e os agentes do espaço de trabalho.
7. **Comando de diagnóstico** (`codex doctor`) e se a saída descrita corresponde à versão vigente.
8. **Decisão editorial registrada:** os números de desempenho comparativo constantes do anúncio do
   GPT-5-Codex (resultados de benchmark, percentuais de tokens, taxas de comentários de revisão) não
   foram usados em nenhum ponto do curso. São irrelevantes para o público e envelhecem rápido. Pelo
   mesmo motivo, **nenhum nome de modelo é citado nos roteiros** — o material-fonte registra uma
   migração de modelos com data marcada, e nomes de modelo envelhecem entre a redação e a publicação.
   A justificativa consta de `_processo/00-contornos.md`.
