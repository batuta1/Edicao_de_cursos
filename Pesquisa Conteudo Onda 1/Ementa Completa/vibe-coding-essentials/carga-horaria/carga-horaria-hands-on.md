# Carga Horária — Vibe Coding - Hands-on

Base: `roteiros/roteiro-hands-on.md` + `carga-horaria/met-tabela.md` (valores fixos para cálculo).
Carga horária alvo: 90–120 min (`_processo/00-contornos.md`).

## 1. Resumo Executivo

| Duração Total do Curso | Nº de Aulas/Oficinas | Nº Total de Atividades | Proporção Teoria:Prática | Status | Recomendação de distribuição |
|---|---|---|---|---|---|
| **115 min** (1 h 55 min) | 6 (Preparação + 4 oficinas + Projeto Final) | 19 | 17% : 83% | Dentro da faixa alvo (5 min de folga) | 3 sessões em dias distintos (5 créditos diários no gratuito): Preparação + Oficinas 1–2 (49 min), Oficinas 3–4 (38 min), Projeto Final (28 min) |

## 2. Breakdown por Aula

### Preparação — Monte sua bancada

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Conta, seletor de modo, `More > Usage`, decisão sobre treinamento, rótulos em inglês | Setup / Navegação | 7 min |
| **TOTAL PREPARAÇÃO** | | **7 min** |

### Oficina 1 — Da ideia à tela

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 1.1 A planta antes da obra: quatro perguntas e ficha de requisitos | Exemplo Aplicado | 6 min |
| Mão na massa, passos 1–4: ajustar a ficha e enviar o primeiro Build (só interface) | Pílula Hands-on | 6 min |
| Mão na massa, passos 5–8: testar a prévia, Mobile view, editar texto pela Preview toolbar, anotar créditos | Pílula Hands-on | 6 min |
| Deu certo? — tela sem login, legível no celular | Avaliação / Feedback | 4 min |
| **TOTAL OFICINA 1** | | **22 min** |

### Oficina 2 — Login e banco de dados

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 2.1 Planejar antes de construir: Plan, leitura e aprovação do plano, Lovable Cloud | Demonstração Técnica | 10 min |
| Mão na massa, passos 4–7: Build do plano, ativar Cloud, conferir Database e Users | Pílula Hands-on | 6 min |
| Deu certo? — tela de login e tabela `tasks` visível | Avaliação / Feedback | 4 min |
| **TOTAL OFICINA 2** | | **20 min** |

### Oficina 3 — Quem vê o quê

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 3.1 Catraca e crachá: autenticação × autorização, RLS, falhas recorrentes | Exemplo Aplicado | 6 min |
| Mão na massa, passos 1–5: duas contas fictícias, tarefas, recarregar, conferir o banco | Pílula Hands-on | 6 min |
| Deu certo? — conta B vê só a própria tarefa | Avaliação / Feedback | 4 min |
| **TOTAL OFICINA 3** | | **16 min** |

### Oficina 4 — Publicar, mudar, republicar

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Mão na massa, passos 1–4: Publish, varredura, endereço, teste em janela anônima | Pílula Hands-on | 6 min |
| Mão na massa, passos 5–7: Bookmark e mudança única (filtro) testada na prévia | Pílula Hands-on | 6 min |
| Mão na massa, passo 8: `Publish changes` e conferência pública | Pílula Hands-on | 6 min |
| Deu certo? — login, isolamento e filtro no endereço público | Avaliação / Feedback | 4 min |
| **TOTAL OFICINA 4** | | **22 min** |

### Projeto Final — Seu app, do seu jeito

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 5.1 Escolha do perfil, triagem de dados reais e limites de um protótipo | Discussão Orientada | 8 min |
| Mão na massa, passos 1–5: ficha, Plan, Build, duas contas, varredura e publicação | Automação/Workflow | 10 min |
| Mão na massa, passos 6–7: Bookmark, mudança final, `Publish changes` | Pílula Hands-on | 6 min |
| Como saber que terminou — checklist de sete itens | Avaliação / Feedback | 4 min |
| **TOTAL PROJETO FINAL** | | **28 min** |

## 3. Resumo Matemático do Curso

$$T_{total} = \sum_{i=1}^{n} t_i$$

com $n = 19$ atividades.

| Tipo de Elemento | Qtde | Valor unitário | Subtotal |
|---|---|---|---|
| Exposição Teórica | 0 | 15 | 0 |
| Demonstração Técnica | 1 | 10 | 10 |
| Exemplo Aplicado | 2 | 6 | 12 |
| Discussão Orientada | 1 | 8 | 8 |
| Setup / Navegação | 1 | 7 | 7 |
| Pílula Hands-on | 8 | 6 | 48 |
| Automação/Workflow | 1 | 10 | 10 |
| Avaliação / Feedback | 5 | 4 | 20 |
| **Total** | **19** | | **115 min** |

Conferência por aula: 7 + 22 + 20 + 16 + 22 + 28 = **115 min**.

## 4. Análise de Densidade

| Bloco | Tipos | Minutos | % |
|---|---|---|---|
| Teoria | Exemplo Aplicado, Discussão Orientada | 20 | 17,4% |
| Prática | Demonstração, Setup, Pílula, Automação/Workflow, Avaliação | 95 | 82,6% |

Abaixo do alvo de 40% de teoria, como é próprio da trilha Hands-on: os conceitos (loja, RLS, prévia ×
publicação) aparecem em boxes e Exemplos Aplicados curtos imediatamente antes da prática; o
tratamento conceitual completo está no Essentials.

Equilíbrio entre oficinas: 22, 20, 16 e 22 min. O Projeto Final (28 min) não ultrapassa o dobro da
oficina mais longa (44 min).

## 5. Aderência à carga horária alvo

Total de 115 min, dentro da faixa de 90–120 min, sem estouro. Os desafios de "Quer ir além?" são
opcionais e não entram no cálculo.

Observação operacional: o tempo de geração do Lovable está contido nas Pílulas e na atividade de
Automação/Workflow, mas varia com o tamanho do pedido. A divisão em três dias também preserva a cota
de 5 créditos diários do plano gratuito.
