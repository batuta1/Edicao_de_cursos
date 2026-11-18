# Ementa — Dados com Python e IA

## Identificação

| Campo | Definição |
|---|---|
| Curso | Dados com Python e IA - Essentials e Dados com Python e IA - Hands On (registro `dados-com-python-e-ia-hands-on`, Onda 3, ranking 47, antecipado para fechar a T8) |
| Natureza | Curto, introdutório, prático e autoinstrucional |
| Trilhas | Essentials (compreensão) e Hands-on (execução) |
| Carga horária total | 216 minutos (Essentials 111 min + Hands-on 105 min), sem contar a espera do agente e o download das bases |
| Público-alvo | Analistas, finanças e planejamento, pesquisadores (T8, posição 6 de 6); finanças e negócios (F2, 7 de 7); servidores públicos e equipes de regulação (R4, 6 de 6); engenheiros e técnicos (TE3, 4 de 6) |
| Pré-requisitos | *IA para Análise de Dados - Essentials* (recomendado) e Excel básico; nenhuma programação; para o Hands-on, o Essentials deste assunto |
| Recursos necessários | Computador com macOS 13+ ou Windows 10 1809+ e 4 GB de RAM; internet; Claude Code no app Claude Desktop (Claude Pro, R$ 110/mês, ou superior; o Free não inclui Claude Code) ou Codex no app de desktop do ChatGPT (acesso limitado no Free, sujeito a liberação gradual; Plus, R$ 99,90/mês, para uso pleno); gerenciador uv; cerca de 120 MB livres para as bases |
| Material-fonte | Pesquisa de conteúdo bruto de 17/11/2026 (duas rodadas): documentação oficial do Claude Code (permissões, checkpoints, memória, uso de dados, boas práticas) e do Codex (sandbox, aprovações, AGENTS.md, preços); página oficial do uv; estudos independentes em PDF (DA-Code, DSBench, KramaBench, "Fail Loudly", DSDBench, USENIX Security 2025, METR, Pimentel et al., Sandve et al., Wilson et al.); bases públicas com gabaritos conferidos por script |

## Objetivo Geral

O curso tem por finalidade capacitar o participante, que não programa, a conduzir análises de dados
reprodutíveis em Python com agentes de código — Claude Code ou Codex —, formulando o pedido em brief,
aprovando as ações com segurança, lendo o código no nível de leigo, organizando o projeto para que
rode do zero e validando os resultados com testes automáticos, contagens de controle, revisão
independente e número oficial. Como produto final, o participante entrega o projeto do IPCA validado
contra o IBGE (Essentials) e o projeto do clima do Distrito Federal em 2024, construído a partir de
cinco arquivos do INMET, com testes e README (Hands-on).

## Competências a Desenvolver

Concluído o curso, o participante deverá demonstrar capacidade de:

1. Decidir quando uma análise deve passar para código e operar o agente em modo restrito, avaliando
   cada pedido de aprovação à luz dos riscos documentados e das regras de dados.
2. Redigir um brief de análise com premissas registradas em arquivo de instruções e exigir o plano
   antes da execução.
3. Organizar um projeto reprodutível — dados brutos intocados, versões registradas, execução do zero
   — sobre bases públicas brasileiras com codificação, escala e chaves problemáticas.
4. Validar resultados com asserts, contagens de controle, número oficial e revisão independente,
   reconhecendo erros silenciosos de leitura, escala, junção e pareamento.

## Estrutura das Trilhas

O Essentials constrói o método (segurança, pedido, reprodutibilidade, validação) sobre um caso-guia
pequeno; o Hands-on aplica o método a bases maiores e com armadilhas reais (CVM e INMET). O Hands-on
pressupõe o Essentials.

**Essentials (111 min)**

| Módulo | Título | Tempo |
|---|---|---|
| 0 | Preparação e Verificação Inicial | 7 min |
| 1 | Por que Código e o que é um Agente | 19 min |
| 2 | O Agente no seu Computador: Segurança e Dados | 15 min |
| 3 | Pedir e Planejar | 16 min |
| 4 | Reprodutibilidade | 16 min |
| 5 | Validar Resultados | 22 min |
| 6 | Síntese e Aplicação Integrada | 16 min |

**Hands-on (105 min)**

| Oficina | Título | Tempo |
|---|---|---|
| Preparação | Antes de Arregaçar as Mangas | 7 min |
| 1 | Seu primeiro projeto reprodutível (IPCA) | 16 min |
| 2 | O ranking que mentia, agora em código (CVM) | 22 min |
| 3 | Cruze duas tabelas sem inflar a soma (CVM × cadastro) | 22 min |
| 4 | Peça uma segunda opinião (pareamento e revisão) | 16 min |
| Projeto Final | O clima do Distrito Federal em 2024 (INMET) | 22 min |

## Distribuição da Carga Horária

| Trilha | Atividades | Tempo | Teoria : Prática |
|---|---|---|---|
| Essentials | 16 | 111 min | 32% : 68% |
| Hands-on | 19 | 105 min | 11% : 89% |
| **Total** | **35** | **216 min** | — |

Cálculo pela Métrica de Estimativa de Tempo (valores fixos por tipo de atividade); detalhes em
`carga-horaria/`.

## Avaliação

- Essentials: duas questões de múltipla escolha com gabarito (Módulos 1 e 4), classificação de cinco
  pedidos de aprovação com gabarito (Módulo 2), exercícios com ponto de controle verificável (plano
  sem arquivos criados; `uv.lock`; `AssertionError` provocado e corrigido) e atividade integradora com
  cinco critérios (Módulo 6).
- Hands-on: cada oficina termina com asserts que passam e números oficiais reproduzidos (IBGE; CVM:
  Petrobras R$ 36,6 bi; setores; pareamento correto); o Projeto Final tem checklist de seis itens com
  gabarito por estação do INMET.

## Pendências de validação

1. Codex no plano Free do ChatGPT no Brasil ("sujeito a liberação gradual"): disponibilidade e
   limites reais.
2. Rótulos do app Claude Desktop (aba Code, seleção de pasta, modos) e do app de desktop do ChatGPT
   (menu de modos, "Work in", `/permissions`) na interface em português.
3. Comandos `uv init`, `uv add` e `uv run` e a instalação do Python pelo uv (documentação lida apenas
   na página de instalação).
4. Caminho da opção de treino de dados nas configurações da conta Claude.
5. Disponibilidade de `/code-review` no app de desktop (documentado para o terminal).
6. Nenhum exercício foi executado com agente real; os gabaritos foram calculados por script
   independente sobre as mesmas bases.
7. Preços (Claude Pro R$ 110; ChatGPT Plus R$ 99,90) vigentes em 17/11/2026 — reconferir antes da
   gravação.
