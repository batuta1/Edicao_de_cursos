# Carga horária — Dados com Python e IA Essentials

Base: `roteiros/roteiro-essentials.md` + `carga-horaria/met-tabela.md` (valores fixos).

## 1. Resumo Executivo

| Duração Total | Nº de Módulos | Nº de Atividades | Teoria : Prática | Status | Distribuição sugerida |
|---|---|---|---|---|---|
| 111 min | 7 (M0 + 5 de conteúdo + síntese) | 16 | 32% : 68% | Dentro da faixa 100–130 min | 2 sessões: M0–M2 (41 min) e M3–M6 (70 min) |

## 2. Breakdown por Módulo

**Módulo 0 — Preparação e verificação inicial**

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Rotas, instalação do uv, pasta do projeto e verificação (0.1, 0.2 + pílula) | Setup / Navegação | 7 |
| **TOTAL MÓDULO 0** | | **7** |

**Módulo 1 — Por que código e o que é um agente**

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Quando passar para código, agente, vocabulário, dado de Pimentel, "rodou ≠ acertou" (1.1, 1.2) | Exposição Teórica | 15 |
| Questão sobre quando passar para código | Avaliação / Feedback | 4 |
| **TOTAL MÓDULO 1** | | **19** |

**Módulo 2 — O agente no seu computador: segurança e dados**

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Modo restrito e controle de treino configurados (2.1 + pílula) | Setup / Navegação | 7 |
| Riscos documentados e classificação de cinco pedidos de aprovação (2.2 + discussão) | Discussão Orientada | 8 |
| **TOTAL MÓDULO 2** | | **15** |

**Módulo 3 — Pedir e planejar**

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Brief, CLAUDE.md/AGENTS.md, plano, leitura por blocos, dados BR (3.1, 3.2) | Demonstração Técnica | 10 |
| Pílula "Plano do caso-guia" | Pílula Hands-on | 6 |
| **TOTAL MÓDULO 3** | | **16** |

**Módulo 4 — Reprodutibilidade**

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Wilson et al., regras de Sandve, tabela de práticas (4.1) | Exemplo Aplicado | 6 |
| Pílula "Executar e rodar do zero" | Pílula Hands-on | 6 |
| Questão sobre registro de versões | Avaliação / Feedback | 4 |
| **TOTAL MÓDULO 4** | | **16** |

**Módulo 5 — Validar resultados**

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Benchmarks, erro silencioso, METR (5.1) | Exemplo Aplicado | 6 |
| Quatro defesas: assert, controle, número oficial, revisão (5.2) | Demonstração Técnica | 10 |
| Pílula "O assert que falha" | Pílula Hands-on | 6 |
| **TOTAL MÓDULO 5** | | **22** |

**Módulo 6 — Síntese e aplicação integrada**

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Integradora, parte 1: modo, instruções, gráfico e rodar do zero (passos 1–3) | Pílula Hands-on | 6 |
| Integradora, parte 2: asserts, revisão e README (passos 4–5) | Pílula Hands-on | 6 |
| Autoavaliação pela tabela de critérios | Avaliação / Feedback | 4 |
| **TOTAL MÓDULO 6** | | **16** |

## 3. Resumo Matemático do Curso

$$T_{total} = \sum_{i=1}^{n} t_i = 7 + 19 + 15 + 16 + 16 + 22 + 16 = 111 \text{ min}$$

com $n = 16$ atividades.

## 4. Análise de Densidade

| Grupo | Tipos | Minutos | % |
|---|---|---|---|
| Teoria | Exposição (15), Exemplo Aplicado (2 × 6 = 12), Discussão (8) | 35 | 32% |
| Prática | Setup (2 × 7 = 14), Demonstração (2 × 10 = 20), Pílula (5 × 6 = 30), Avaliação (3 × 4 = 12) | 76 | 68% |

Acima do alvo de prática (60%); adequado para um curso cujo produto é um projeto executável.

## 5. Aderência à carga horária alvo

Alvo: 100–130 min. Total: **111 min**, sem estouro. A espera do agente (instalar bibliotecas,
executar) não está na MET e varia com a máquina e a conexão.
