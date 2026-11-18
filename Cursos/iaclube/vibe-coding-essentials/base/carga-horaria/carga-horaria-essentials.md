# Carga Horária — Vibe Coding - Essentials

Base: `roteiros/roteiro-essentials.md` + `carga-horaria/met-tabela.md` (valores fixos para cálculo).
Carga horária alvo: 100–130 min (`_processo/00-contornos.md`).

## 1. Resumo Executivo

| Duração Total do Curso | Nº de Aulas/Módulos | Nº Total de Atividades | Proporção Teoria:Prática | Status | Recomendação de distribuição |
|---|---|---|---|---|---|
| **129 min** (2 h 09 min) | 7 (Módulo 0 + 5 de conteúdo + síntese) | 18 | 39% : 61% | Dentro da faixa alvo (1 min de folga) | 3 sessões em dias distintos, por causa dos 5 créditos diários do plano gratuito: Módulos 0–3 (69 min), Módulos 4–5 (40 min), Módulo 6 (20 min) |

## 2. Breakdown por Aula

### Módulo 0 — Preparação e Verificação Inicial

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 0.1 Conta, plano gratuito e créditos, rota de baixo consumo, rótulos em inglês, `More > Usage`, registro de verificação | Setup / Navegação | 7 min |
| **TOTAL MÓDULO 0** | | **7 min** |

### Módulo 1 — O que é vibe coding e como funciona um aplicativo web

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 1.1 Texto descritivo: origem e definição, fronteiras com no-code e programação assistida, Lovable e modos, analogia da loja | Exposição Teórica | 15 min |
| 1.2 Glossário aplicado (loja × "Minhas Tarefas") e casos Plinq e Elora com ressalva | Exemplo Aplicado | 6 min |
| Pílula: distinção entre métodos (múltipla escolha com gabarito e fundamentação) | Avaliação / Feedback | 4 min |
| **TOTAL MÓDULO 1** | | **25 min** |

### Módulo 2 — Segurança, Dados e Custos antes de Construir

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 2.1–2.2 Texto descritivo: front-end inspecionável, Secrets, RLS, limites da varredura, incidente de 2026, LGPD e dados fictícios, recusa ao treinamento, custo × segurança | Exposição Teórica | 15 min |
| Pílula: configuração do treinamento e triagem de quatro ideias de aplicativo | Pílula Hands-on | 6 min |
| **TOTAL MÓDULO 2** | | **21 min** |

### Módulo 3 — Especificar e gerar o primeiro protótipo

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 3.1 Quatro perguntas oficiais, ficha de requisitos, modos Chat/Plan/Build, Preview toolbar, construção em camadas | Exemplo Aplicado | 6 min |
| Pílula: ficha de requisitos e primeiro Build (só interface) | Pílula Hands-on | 6 min |
| Avaliação: conferência do protótipo (cinco critérios, incluindo Mobile view) | Avaliação / Feedback | 4 min |
| **TOTAL MÓDULO 3** | | **16 min** |

### Módulo 4 — Banco de dados, login e controle de acesso

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 4.1 Lovable Cloud, fluxo Plan → aprovação → Build, telas Database e Users, irreversibilidade da exclusão, teste de isolamento | Demonstração Técnica | 10 min |
| Pílula: plano, aprovação e construção do back-end | Pílula Hands-on | 6 min |
| Pílula: teste de isolamento com duas contas | Pílula Hands-on | 6 min |
| **TOTAL MÓDULO 4** | | **22 min** |

### Módulo 5 — Publicar, iterar e reconhecer limites

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 5.1 Publish × prévia, Publish changes, descrição de erro, History/Bookmarks/Revert e seu limite, quando vibe coding não basta, dependência e alternativas | Discussão Orientada | 8 min |
| Pílula: publicação após a varredura e teste em janela anônima | Pílula Hands-on | 6 min |
| Avaliação: checklist de prontidão para publicação (Anexo C) | Avaliação / Feedback | 4 min |
| **TOTAL MÓDULO 5** | | **18 min** |

### Módulo 6 — Síntese e Aplicação Integrada

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Atividade integradora: novo aplicativo do perfil — ficha, Plan, Build, duas contas, varredura, publicação | Automação/Workflow | 10 min |
| Pílula: Bookmark, iteração com filtro e `Publish changes` | Pílula Hands-on | 6 min |
| Avaliação: critérios de avaliação (sete itens) | Avaliação / Feedback | 4 min |
| **TOTAL MÓDULO 6** | | **20 min** |

## 3. Resumo Matemático do Curso

$$T_{total} = \sum_{i=1}^{n} t_i$$

com $n = 18$ atividades.

| Tipo de Elemento | Qtde | Valor unitário | Subtotal |
|---|---|---|---|
| Exposição Teórica | 2 | 15 | 30 |
| Demonstração Técnica | 1 | 10 | 10 |
| Exemplo Aplicado | 2 | 6 | 12 |
| Discussão Orientada | 1 | 8 | 8 |
| Setup / Navegação | 1 | 7 | 7 |
| Pílula Hands-on | 6 | 6 | 36 |
| Automação/Workflow | 1 | 10 | 10 |
| Avaliação / Feedback | 4 | 4 | 16 |
| **Total** | **18** | | **129 min** |

Conferência por módulo: 7 + 25 + 21 + 16 + 22 + 18 + 20 = **129 min**.

## 4. Análise de Densidade

| Bloco | Tipos | Minutos | % |
|---|---|---|---|
| Teoria | Exposição Teórica, Exemplo Aplicado, Discussão Orientada | 50 | 38,8% |
| Prática | Demonstração, Setup, Pílula, Automação/Workflow, Avaliação | 79 | 61,2% |

Equilibrado para iniciantes (alvo 40/60). A teoria concentra-se nos Módulos 1 e 2 (36 de 50 minutos):
vocabulário e segurança precedem o primeiro pedido de construção. Do Módulo 3 em diante, todos os
módulos têm maioria de prática.

## 5. Aderência à carga horária alvo

Total de 129 min, dentro da faixa de 100–130 min, sem estouro. Desafios opcionais e anexos não entram
no cálculo.

Observação operacional: o tempo de geração do Lovable (geralmente de segundos a poucos minutos por
pedido) está contido nas Pílulas e na Atividade Integradora, mas pode exceder o valor fixo em pedidos
maiores. A divisão em três dias acomoda também a cota de 5 créditos diários; o fabricante não garante
que o curso inteiro caiba no plano gratuito (ver `README.md`).
