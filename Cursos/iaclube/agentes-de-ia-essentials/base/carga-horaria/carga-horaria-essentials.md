# Carga Horária — Agentes de IA - Essentials

Base: `roteiros/roteiro-essentials.md` + `carga-horaria/met-tabela.md` (valores fixos para cálculo).
Carga horária alvo: 100–130 min (`_processo/00-contornos.md`).

## 1. Resumo Executivo

| Duração Total do Curso | Nº de Aulas/Módulos | Nº Total de Atividades | Proporção Teoria:Prática | Status | Recomendação de distribuição |
|---|---|---|---|---|---|
| **129 min** (2 h 09 min) | 7 (Módulo 0 + 5 de conteúdo + síntese) | 18 | 39% : 61% | Dentro da faixa alvo (1 min de folga) | 2 sessões em dias distintos (por causa dos créditos diários do Manus gratuito): Módulos 0–3 (69 min) e Módulos 4–6 (60 min) |

## 2. Breakdown por Aula

### Módulo 0 — Preparação e Verificação Inicial

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 0.1 Escolha do caminho pela tabela de planos, conta, localização dos seletores, pasta `Treino_Agente`, download do Guia do TCU e registro de verificação | Setup / Navegação | 7 min |
| **TOTAL MÓDULO 0** | | **7 min** |

### Módulo 1 — O que é um agente de IA

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 1.1 Texto descritivo: definições (Anthropic, OpenAI, Google Cloud), ciclo planejar-agir-observar-ajustar, ferramentas leitura × escrita (NIST), analogia do assistente recém-contratado, linha do tempo dos produtos, escada de autonomia | Exposição Teórica | 15 min |
| 1.2 Tabela chat × automação × agente com exemplos de escritório e jurídico; caso CAIXA com ressalva | Exemplo Aplicado | 6 min |
| Pílula: classificação com caso limítrofe (questão de múltipla escolha com gabarito e fundamentação) | Avaliação / Feedback | 4 min |
| **TOTAL MÓDULO 1** | | **25 min** |

### Módulo 2 — Segurança, Permissões e Responsabilidade Profissional

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 2.1–2.3 Texto descritivo: fórmula de risco, menor privilégio, modos de aprovação, ação consequencial, injeção de prompt (caso STJ, estudo UW), Recomendação 001/2024/CFOAB, dados proibidos, tratamento de dados por ferramenta | Exposição Teórica | 15 min |
| Pílula: avaliação de risco de quatro delegações com decisão e ajuste | Pílula Hands-on | 6 min |
| **TOTAL MÓDULO 2** | | **21 min** |

### Módulo 3 — Definir a tarefa: a ordem de serviço

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 3.1 Tabela O-F-L-C-P aplicada ao Guia do TCU; ponto de parada; um assunto por tarefa | Exemplo Aplicado | 6 min |
| Pílula: redação da `ordem_servico_tcu.txt` a partir do prompt-base | Pílula Hands-on | 6 min |
| Avaliação: autoverificação da ordem de serviço (checklist de cinco itens) | Avaliação / Feedback | 4 min |
| **TOTAL MÓDULO 3** | | **16 min** |

### Módulo 4 — Acompanhar a execução e intervir

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 4.1–4.2 O que a tela mostra (plano, ação atual, evidência, aprovação, produto), sinais de intervenção, assumir o controle, créditos e cotas; rotas nas três ferramentas | Demonstração Técnica | 10 min |
| Pílula: delegação com plano antes da execução | Pílula Hands-on | 6 min |
| Pílula: intervenção durante a execução (prompt-base de mudança de escopo) | Pílula Hands-on | 6 min |
| **TOTAL MÓDULO 4** | | **22 min** |

### Módulo 5 — Revisar o resultado e reconhecer limites

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 5.1–5.2 "Terminou ≠ correto" (HAL Princeton, AI Agent Index, ausência de *system card*), roteiro de revisão, critérios de escolha entre ferramentas | Discussão Orientada | 8 min |
| Pílula: conferência por amostragem de três linhas e pedido de correção | Pílula Hands-on | 6 min |
| Avaliação: ficha de revisão | Avaliação / Feedback | 4 min |
| **TOTAL MÓDULO 5** | | **18 min** |

### Módulo 6 — Síntese e Aplicação Integrada

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Atividade integradora: ciclo completo por perfil (CGU ou OAB) com arquivo-isca — risco, ordem de serviço, aprovação do plano, acompanhamento | Automação/Workflow | 10 min |
| Pílula: revisão do produto integrador e verificação da seção "Instruções suspeitas encontradas" | Pílula Hands-on | 6 min |
| Avaliação: critérios de avaliação (tabela de sete itens) | Avaliação / Feedback | 4 min |
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

O curso está equilibrado para iniciantes (alvo 40/60). A teoria concentra-se nos Módulos 1 e 2
(36 de 50 minutos), o que é intencional: conceito e segurança precedem o primeiro uso real. A partir
do Módulo 3, todos os módulos têm maioria de prática.

## 5. Aderência à carga horária alvo

Total de 129 min, dentro da faixa de 100–130 min, sem estouro. Os desafios opcionais e os anexos não
entram no cálculo.

Observação operacional: o tempo de espera pela execução do agente (alguns minutos por tarefa,
variável) está contido nas Pílulas dos Módulos 4 e 6 e na Atividade Integradora, mas pode exceder o
valor fixo em contas com fila ou em tarefas longas. Não se ajustou a tabela; recomenda-se, em vez
disso, a divisão em duas sessões indicada no Resumo Executivo, que também respeita a cota diária de
créditos do Manus gratuito.
