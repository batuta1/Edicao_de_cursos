# Marcos de Desenvolvimento

Cada fase tem um portão. Sinal vermelho aponta para a fase a refazer — não para um remendo local no
arquivo atual. Os marcos 2 a 5 valem **por trilha**.

## 🚩 Marco 1 — Contornos definidos (`_processo/00-contornos.md`)
- [ ] Objeto base, público-alvo, pré-requisitos e recursos estão escritos, não subentendidos.
- [ ] Está definido se o curso é autoinstrucional.
- [ ] A carga horária alvo está definida.
- [ ] Está registrado se há material-fonte — e, não havendo, que dados factuais precisarão de
      validação humana.
- [ ] A pasta do tema foi criada, em kebab-case e sem acento, com `roteiros/`, `carga-horaria/` e
      `_processo/`.

**Verde:** outra pessoa conseguiria escrever a v1.0 só com este arquivo.
**Vermelho:** algum campo está "a definir" — pergunte ao usuário antes de escrever qualquer aula.

## 🚩 Marco 2 — Versão 1.0 consolidada (`_processo/01-v1-<trilha>.md`)
- [ ] Todas as seções obrigatórias do modelo estão presentes, na ordem exigida.
- [ ] O documento vai do título ao encerramento sem trecho truncado nem módulo faltando.
- [ ] Cada módulo/oficina tem exercício com critério de êxito explícito.
- [ ] O tom corresponde à trilha (formal impessoal em Essentials; 2ª pessoa em Hands-on).
- [ ] Nada do prompt-modelo vazou para o conteúdo (o curso fala do objeto base, não de design
      instrucional).

**Verde:** dá para ler a v1.0 do início ao fim com continuidade.
**Vermelho:** estrutura incompleta ou tom trocado — refaça a Fase 1 com o modelo aberto ao lado.

## 🚩 Marco 3 — Diagnóstico crítico concluído (`_processo/02-analise-<trilha>.md`)
- [ ] Os quatro eixos foram cobertos: clareza, rigor técnico, engajamento, potencial oculto.
- [ ] A matriz de soluções existe e cada correção é executável, não genérica.
- [ ] Os riscos críticos para iniciantes (instalação, segurança, permissões) estão nomeados.
- [ ] O que não pôde ser verificado está declarado como não verificado.

**Verde:** os achados já são ações objetivas de melhoria.
**Vermelho:** relatório opinativo, sem plano de ação — refaça a auditoria.

## 🚩 Marco 4 — Roteiro final entregue (`roteiros/roteiro-<trilha>.md`)
- [ ] Cada gargalo da auditoria tem destino visível (corrigido, ou decisão declarada).
- [ ] Toda aula tem **Objetivos da Aula** e **Habilidades Esperadas**, distintos entre si.
- [ ] Sugestões de print descrevem a tela ao ponto de alguém conseguir capturá-la.
- [ ] Troubleshooting está nos pontos que a auditoria marcou como críticos.
- [ ] Pré-requisitos e segurança aparecem antes do primeiro uso real da ferramenta.

**Verde:** há ganho real de clareza e aplicabilidade em relação à v1.0.
**Vermelho:** os problemas críticos persistem — volte à matriz de soluções.

## 🚩 Marco 5 — Carga horária fechada (`carga-horaria/`)
- [ ] `met-tabela.md` está na pasta, para os números poderem ser conferidos sem a skill.
- [ ] Toda atividade do roteiro aparece classificada em um dos oito tipos da MET.
- [ ] Nenhuma categoria nova foi inventada.
- [ ] Há tempo por aula, total do curso e a lógica de cálculo declarada.
- [ ] A proporção teoria/prática foi calculada e comparada ao alvo 40/60.
- [ ] O total foi comparado à carga horária alvo; estouro, se houver, está declarado.

**Verde:** outra pessoa soma as tabelas e chega ao mesmo total.
**Vermelho:** os números não se reproduzem — refaça o breakdown atividade a atividade.

## 🚩 Marco 6 — Ementa consolidada (`ementa.md`)
- [ ] Foi escrita **depois** dos roteiros e da carga horária.
- [ ] Identificação, Objetivo Geral, Competências, Estrutura das Trilhas, Distribuição da Carga
      Horária, Avaliação e Pendências de validação estão todos presentes.
- [ ] Todo tempo declarado bate com `carga-horaria/`.
- [ ] Nenhuma competência prometida sem aula que a desenvolva.
- [ ] Registro formal e impessoal, sem emoji, mesmo havendo trilha Hands-on.

**Verde:** alguém decide sobre o curso lendo só a ementa.
**Vermelho:** a ementa promete o que os roteiros não entregam — corrija a ementa, não o número.

## 🚩 Marco 7 — Pasta organizada e entregue
- [ ] Produtos no nível de cima: `ementa.md`, `roteiros/`, `carga-horaria/`.
- [ ] `_processo/` contém contornos, v1.0 e análises — presente, mas fora da entrega.
- [ ] `README.md` lista cada arquivo em uma linha.
- [ ] O `README.md` declara o que **não** foi verificado e o que depende de validação humana.
- [ ] Nenhum nome de arquivo ou pasta com acento.

**Verde:** a pasta é autoexplicativa para quem a receber sem contexto.
**Vermelho:** falta índice ou os produtos estão misturados ao processo — reorganize antes de
entregar.

## 🚩 Marco 8 — Roteiros Articulate (`roteiros/roteiro-articulate-<trilha>.md`)
- [ ] Cada trilha usou **o seu** prompt-mestre (`articulate-essentials.md` /
      `articulate-hands-on.md`), não o da outra.
- [ ] O roteiro final da Fase 3 foi passado como material-fonte — a versão Rise não é um curso
      novo gerado do zero, e continua batendo com a carga horária da Fase 4.
- [ ] Nenhuma menção a "captura de tela" sobrou; navegação está em breadcrumbs
      `App > Menu > Opção`, com pontos de controle 🏁 onde há resultado a conferir.
- [ ] Cada bloco tem cue `» IA:` com o tipo de bloco do Rise, e as travas ("verbatim", "não
      traduzir termos de interface", "preservar os breadcrumbs") onde cabem.
- [ ] Marcadores `▼▼▼`/`▲▲▲` cercam cada módulo (Essentials) ou cada oficina + Projeto Final
      (Hands-on). Identificação, Parte dos Dez e Encerramento **não** recebem marcador.
- [ ] Modelos editáveis estão em aspas triplas, não crases triplas.
- [ ] Essentials: cada módulo tem a subseção "Mão na massa" com prompt-base editável.
- [ ] Essentials: requisitos técnicos citados quando aplicável (versão do Office; plano pago do
      Claude — o gratuito não habilita o recurso).
- [ ] O curso não virou um curso sobre Rise 360, fidelidade ou conversão de roteiros.

**Verde:** o arquivo pode ir para o Articulate junto com o `promptArticulate.md`.
**Vermelho:** falta camada de montagem ou o conteúdo divergiu — reprocesse a Fase 7 sobre o
roteiro final daquela trilha.
