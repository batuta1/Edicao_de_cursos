# Carga Horária — Agentes de IA - Hands-on

Base: `roteiros/roteiro-hands-on.md` + `carga-horaria/met-tabela.md` (valores fixos para cálculo).
Carga horária alvo: 90–120 min (`_processo/00-contornos.md`).

## 1. Resumo Executivo

| Duração Total do Curso | Nº de Aulas/Oficinas | Nº Total de Atividades | Proporção Teoria:Prática | Status | Recomendação de distribuição |
|---|---|---|---|---|---|
| **115 min** (1 h 55 min) | 6 (Preparação + 4 oficinas + Projeto Final) | 19 | 23% : 77% | Dentro da faixa alvo (5 min de folga) | 2 sessões em dias distintos (créditos diários do Manus gratuito): Preparação + Oficinas 1–2 (49 min) e Oficinas 3–4 + Projeto Final (66 min) |

## 2. Breakdown por Aula

### Preparação — Monte sua bancada

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 0.1–0.2 Escolha da ferramenta pelo plano, conta, localização dos seletores, saldo de créditos, pasta `Treino_Agente` e download dos PDFs | Setup / Navegação | 7 min |
| **TOTAL PREPARAÇÃO** | | **7 min** |

### Oficina 1 — Do pedido vago à ordem de serviço

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 1.1 Fórmula O-F-L-C-P aplicada ao Guia do TCU; ponto de parada | Exemplo Aplicado | 6 min |
| Mão na massa, passos 1–2: redigir e salvar a `ordem_servico_tcu.txt` | Pílula Hands-on | 6 min |
| Mão na massa, passos 3–7: abrir o modo de agente, anexar, enviar e ler o plano | Pílula Hands-on | 6 min |
| Deu certo? — plano devolvido e agente parado | Avaliação / Feedback | 4 min |
| **TOTAL OFICINA 1** | | **22 min** |

### Oficina 2 — Acompanhe e corrija o rumo

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 2.1 Diário de bordo: cinco sinais, aprovação do plano e acompanhamento da execução | Demonstração Técnica | 10 min |
| Mão na massa, passos 2–6: correção de escopo no meio da execução, negativa de pedidos externos, saldo final | Pílula Hands-on | 6 min |
| Deu certo? — plano atualizado e tabela limitada às páginas 1–4 | Avaliação / Feedback | 4 min |
| **TOTAL OFICINA 2** | | **20 min** |

### Oficina 3 — Confira antes de confiar

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 3.1 Por que conferir: dados de Princeton com ressalva; amostragem | Exemplo Aplicado | 6 min |
| Mão na massa, passos 1–4: conferência por amostragem (três + três linhas) | Pílula Hands-on | 6 min |
| Mão na massa, passos 5–6: pedido de correção e reconferência | Pílula Hands-on | 6 min |
| Deu certo? — seis linhas conferidas, sem divergência | Avaliação / Feedback | 4 min |
| **TOTAL OFICINA 3** | | **22 min** |

### Oficina 4 — Pegue o bilhete do estranho

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 4.1 Injeção × alucinação; caso STJ | Exemplo Aplicado | 6 min |
| Mão na massa, passos 1–5: criar o arquivo-isca, delegar com os dois anexos, negar envio | Pílula Hands-on | 6 min |
| Deu certo? — instrução listada em "Instruções suspeitas encontradas", sem envio | Avaliação / Feedback | 4 min |
| **TOTAL OFICINA 4** | | **16 min** |

### Projeto Final — Uma delegação completa, do seu jeito

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 5.1 Escolha do perfil e avaliação de risco antes de delegar | Discussão Orientada | 8 min |
| Mão na massa, passos 1–7: ordem de serviço, envio com arquivo-isca, aprovação do plano, correção de escopo, negativas | Automação/Workflow | 10 min |
| Mão na massa, passos 8–9: conferência por amostragem, correção, frase sobre limites | Pílula Hands-on | 6 min |
| Como saber que terminou — checklist de oito itens | Avaliação / Feedback | 4 min |
| **TOTAL PROJETO FINAL** | | **28 min** |

## 3. Resumo Matemático do Curso

$$T_{total} = \sum_{i=1}^{n} t_i$$

com $n = 19$ atividades.

| Tipo de Elemento | Qtde | Valor unitário | Subtotal |
|---|---|---|---|
| Exposição Teórica | 0 | 15 | 0 |
| Demonstração Técnica | 1 | 10 | 10 |
| Exemplo Aplicado | 3 | 6 | 18 |
| Discussão Orientada | 1 | 8 | 8 |
| Setup / Navegação | 1 | 7 | 7 |
| Pílula Hands-on | 7 | 6 | 42 |
| Automação/Workflow | 1 | 10 | 10 |
| Avaliação / Feedback | 5 | 4 | 20 |
| **Total** | **19** | | **115 min** |

Conferência por aula: 7 + 22 + 20 + 22 + 16 + 28 = **115 min**.

## 4. Análise de Densidade

| Bloco | Tipos | Minutos | % |
|---|---|---|---|
| Teoria | Exemplo Aplicado, Discussão Orientada | 26 | 22,6% |
| Prática | Demonstração, Setup, Pílula, Automação/Workflow, Avaliação | 89 | 77,4% |

O curso fica abaixo do alvo de 40% de teoria, o que é coerente com a trilha Hands-on (teoria mínima
para o próximo passo). A compreensão conceitual completa está no Essentials; aqui, cada bloco teórico
é um Exemplo Aplicado curto que antecede a prática da mesma oficina.

Equilíbrio entre oficinas: 22, 20, 22 e 16 min. A Oficina 4 é a mais curta por ter uma única
execução do agente; o Projeto Final (28 min) não ultrapassa o dobro da oficina mais longa (44 min),
como exige o prompt-mestre.

## 5. Aderência à carga horária alvo

Total de 115 min, dentro da faixa de 90–120 min, sem estouro. Os desafios de "Quer ir além?" (três
por oficina) são opcionais e não entram no cálculo.

Observação operacional: o tempo de execução do agente está contido nas Pílulas e na atividade de
Automação/Workflow, mas varia com a fila e o tamanho da tarefa. Recomenda-se a divisão em duas
sessões indicada no Resumo Executivo, que também preserva a cota diária de créditos do Manus.
