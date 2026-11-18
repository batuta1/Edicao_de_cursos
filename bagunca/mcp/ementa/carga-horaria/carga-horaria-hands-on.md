# Carga Horária — MCP - Hands-on

Base: `roteiros/roteiro-hands-on.md` + `carga-horaria/met-tabela.md` (valores fixos para cálculo).
Carga horária alvo: 90–120 min (`_processo/00-contornos.md`).

## 1. Resumo Executivo

| Duração Total do Curso | Nº de Aulas/Oficinas | Nº Total de Atividades | Proporção Teoria:Prática | Status | Recomendação de distribuição |
|---|---|---|---|---|---|
| **117 min** (1 h 57 min) | 7 (preparação + 4 oficinas + Projeto Final + Parte dos Dez) | 18 | 12% : 88% | Dentro da faixa alvo (3 min de folga) | 1 semana × 2 sessões: preparação + Oficinas 1–2 (53 min) e Oficinas 3–4 + Projeto Final + Parte dos Dez (64 min) |

## 2. Breakdown por Aula

Regra de classificação: nas oficinas, a parte guiada que instala ou conecta (passos com caminho de
menu ditado) é Demonstração Técnica; a parte em que o aluno formula pedidos e confere resultados é
Pílula Hands-on; "Deu certo?" é Avaliação / Feedback. "Se travar", "Quer ir além?" (opcional) e
"Desligue ao sair" são material de apoio e não entram no cálculo; a Parte C da Oficina 4
(desconexão) integra a Pílula dessa oficina.

### Antes de Arregaçar as Mangas

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Conferência de conta, vaga do Free, Claude Desktop, Conta Google pessoal, criação da pasta de teste, ChatGPT opcional | Setup / Navegação | 7 min |
| Pílula do semáforo: ler a ficha do Google Calendar, separar leitura × escrita, classificar três usos | Pílula Hands-on | 6 min |
| **TOTAL PREPARAÇÃO** | | **13 min** |

### Oficina 1 — Ligue seu primeiro conector

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Passos 1–5: liberar a vaga, adicionar o OpenAI Docs por URL, ligar na conversa (e variação no ChatGPT) | Demonstração Técnica | 10 min |
| Passos 6–9: listar ferramentas, consulta restrita ao conector, abrir a chamada e a URL | Pílula Hands-on | 6 min |
| Deu certo? (chamada visível, URL oficial, nenhuma escrita) | Avaliação / Feedback | 4 min |
| **TOTAL OFICINA 1** | | **20 min** |

### Oficina 2 — Deixe o Claude ler uma pasta — só uma

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Passos 1–4: instalar a extensão Filesystem e autorizar só a pasta de teste (ou conectar o Google Drive) | Demonstração Técnica | 10 min |
| Passos 5–9: perguntar diretórios, pedir leitura, identificar a instrução maliciosa, negar gravação, conferir a pasta | Pílula Hands-on | 6 min |
| Deu certo? (pasta única, resumos corretos, injeção não executada, dois arquivos) | Avaliação / Feedback | 4 min |
| **TOTAL OFICINA 2** | | **20 min** |

### Oficina 3 — Consulte sua agenda sem mexer em nada

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Passos 1–5: conectar o Google Calendar com login e configurar Tool permissions | Demonstração Técnica | 10 min |
| Passos 6–7: consulta somente leitura e conferência no Google Calendar | Pílula Hands-on | 6 min |
| Deu certo? (eventos coincidentes, nenhuma aprovação de escrita) | Avaliação / Feedback | 4 min |
| **TOTAL OFICINA 3** | | **20 min** |

### Oficina 4 — Crie, confira e apague

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Parte A: criar o evento de teste com aprovação, conferir, excluir e confirmar | Demonstração Técnica | 10 min |
| Partes B e C: rascunho no Gmail sem envio, conferência em Rascunhos e Enviados, desconexão e revogação | Pílula Hands-on | 6 min |
| Deu certo? (evento criado e removido, rascunho sem envio, conectores desconectados) | Avaliação / Feedback | 4 min |
| **TOTAL OFICINA 4** | | **20 min** |

### Projeto Final — Seu plano de conexão segura

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Passos 1–3: escolher a tarefa, ler a ficha sem instalar e preencher o plano (decisão pelo semáforo) | Discussão Orientada | 8 min |
| Passos 4–6: teste com dado fictício ou encaminhamento do pedido; faxina final | Pílula Hands-on | 6 min |
| Como saber que terminou (checklist de seis itens) | Avaliação / Feedback | 4 min |
| **TOTAL PROJETO FINAL** | | **18 min** |

### A Parte dos Dez — Hábitos que Salvam seu Dia com Conectores

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| Leitura dos dez hábitos práticos | Exemplo Aplicado | 6 min |
| **TOTAL PARTE DOS DEZ** | | **6 min** |

## 3. Resumo Matemático do Curso

$$T_{total} = \sum_{i=1}^{n} t_i$$

com $n = 18$ atividades.

| Tipo de Elemento | Ocorrências | Valor unitário | Subtotal |
|---|---|---|---|
| Exposição Teórica | 0 | 15 | 0 |
| Demonstração Técnica | 4 | 10 | 40 |
| Exemplo Aplicado | 1 | 6 | 6 |
| Discussão Orientada | 1 | 8 | 8 |
| Setup / Navegação | 1 | 7 | 7 |
| Pílula Hands-on | 6 | 6 | 36 |
| Automação/Workflow | 0 | 10 | 0 |
| Avaliação / Feedback | 5 | 4 | 20 |
| **Total** | **18** | | **117 min** |

Conferência por etapa: 13 + 20 + 20 + 20 + 20 + 18 + 6 = **117 min**.

## 4. Análise de Densidade

| Classe | Tipos | Tempo | Percentual |
|---|---|---|---|
| Teoria | Exemplo Aplicado (6) + Discussão Orientada (8) | 14 min | 12,0% |
| Prática | Demonstração (40) + Setup (7) + Pílula (36) + Avaliação (20) | 103 min | 88,0% |

O curso fica abaixo da referência de 40% de teoria, **por desenho**: a trilha Hands-on prioriza o
fazer, e a teoria mínima (o que é MCP, leitura × escrita, semáforo) está embutida no box 🤓 e na pílula
do semáforo, que a MET classifica como prática. O risco correspondente — o aluno executar sem entender
o que concede — é mitigado pela pílula do semáforo antes da primeira conexão e pela recomendação de
cursar o *MCP - Essentials* antes ou em paralelo. Nenhuma oficina carece de prática.

## 5. Aderência à carga horária alvo

Total de 117 min, dentro da faixa de 90–120 min, com 3 min de folga. As quatro oficinas têm o mesmo
tempo (20 min) e o Projeto Final (18 min) não ultrapassa o dobro de uma oficina, como exige o
prompt-mestre. Não há estouro.
