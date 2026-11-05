# Carga Horária — MCP - Essentials

Base: `roteiros/roteiro-essentials.md` + `carga-horaria/met-tabela.md` (valores fixos para cálculo).
Carga horária alvo: 100–130 min (`_processo/00-contornos.md`).

## 1. Resumo Executivo

| Duração Total do Curso | Nº de Aulas/Módulos | Nº Total de Atividades | Proporção Teoria:Prática | Status | Recomendação de distribuição |
|---|---|---|---|---|---|
| **129 min** (2 h 09 min) | 7 (Módulo 0 + 5 de conteúdo + síntese) | 18 | 34% : 66% | Dentro da faixa alvo (1 min de folga) | 1 semana × 2 sessões: Módulos 0–3 (71 min) e Módulos 4–6 (58 min) |

## 2. Breakdown por Aula

Regra de classificação: os blocos "Prompt-base (Mão na massa)" e "Solução de Problemas" são material
de apoio consumido dentro da atividade em que aparecem e não constituem atividade própria. O Anexo B
(técnico, opcional) e os Anexos A e C não entram no cálculo.

### Módulo 0 — Preparação e Verificação Inicial

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 0.1 Verificação de conta, plano, vaga de conector, Desktop/SO, Conta Google e ChatGPT; preenchimento do registro | Setup / Navegação | 7 min |
| **TOTAL MÓDULO 0** | | **7 min** |

### Módulo 1 — O que é o MCP: um padrão comum entre assistentes e serviços

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 1.1 Texto descritivo: problema N × M, protocolo, governança, tomada e crachá, host/client/servidor, tools/resources/prompts, local × remoto, limites | Exposição Teórica | 15 min |
| 1.2 Tabela MCP × API × conector/plugin × skill × Zapier/n8n; três verbos (consultar, ler, agir); exemplos Senior e Econodata; prompt-base de listagem | Exemplo Aplicado | 6 min |
| 1.3 Verificação de compreensão (2 questões de múltipla escolha com gabarito fundamentado) | Avaliação / Feedback | 4 min |
| **TOTAL MÓDULO 1** | | **25 min** |

### Módulo 2 — Segurança, Permissões e Uso Responsável

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 2.1 Texto descritivo: cinco riscos, Tool permissions e Allow/Deny, diretório ≠ garantia, ficha do conector, LGPD/ANPD/Governo Digital, semáforo; prompt-base de proteção | Exposição Teórica | 15 min |
| 2.2 Análise de quatro cenários pelo semáforo (com gabarito) | Avaliação / Feedback | 4 min |
| **TOTAL MÓDULO 2** | | **19 min** |

### Módulo 3 — Primeira conexão: consultar um serviço

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 3.1 Demonstração: conector personalizado no Claude, ativação por conversa, bloco de chamada de ferramenta, fluxo `Plugins > + > Add custom MCP server` no ChatGPT | Demonstração Técnica | 10 min |
| 3.2 Primeira consulta com o OpenAI Docs MCP (adicionar, ligar, consultar, conferir ferramenta e URL) | Pílula Hands-on | 6 min |
| 3.3 Verificação do critério de êxito (quatro itens) | Avaliação / Feedback | 4 min |
| **TOTAL MÓDULO 3** | | **20 min** |

### Módulo 4 — Ler arquivos: pasta local e nuvem

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 4.1 Demonstração: extensão Filesystem no Claude Desktop (instalação, pasta única, leitura × escrita) e conector Google Drive | Demonstração Técnica | 10 min |
| 4.2 Leitura da pasta `teste-mcp-arquivos` com instrução maliciosa simulada | Pílula Hands-on | 6 min |
| 4.3 Verificação do critério de êxito e fundamentação sobre injeção indireta | Avaliação / Feedback | 4 min |
| **TOTAL MÓDULO 4** | | **20 min** |

### Módulo 5 — Executar ações com aprovação e desfazer

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 5.1 Demonstração: método preparar–revisar–conferir–desfazer, Google Calendar com Needs approval, Gmail em rascunho, desconexão e revogação | Demonstração Técnica | 10 min |
| 5.2 Consultar, criar, conferir e apagar um evento de teste | Pílula Hands-on | 6 min |
| 5.3 Verificação do critério de êxito (quatro itens) | Avaliação / Feedback | 4 min |
| **TOTAL MÓDULO 5** | | **20 min** |

### Módulo 6 — Síntese e Aplicação Integrada

| Atividade | Tipo de Elemento | Duração |
|---|---|---|
| 6.1 Discussão orientada: quatro perguntas de decisão e tabela de casos por semáforo; fronteira do curso | Discussão Orientada | 8 min |
| 6.2 Atividade integradora: plano de conexão segura para caso próprio e devolução dos acessos do curso | Pílula Hands-on | 6 min |
| 6.3 Autoavaliação pela tabela de seis critérios | Avaliação / Feedback | 4 min |
| **TOTAL MÓDULO 6** | | **18 min** |

## 3. Resumo Matemático do Curso

$$T_{total} = \sum_{i=1}^{n} t_i$$

com $n = 18$ atividades.

| Tipo de Elemento | Ocorrências | Valor unitário | Subtotal |
|---|---|---|---|
| Exposição Teórica | 2 | 15 | 30 |
| Demonstração Técnica | 3 | 10 | 30 |
| Exemplo Aplicado | 1 | 6 | 6 |
| Discussão Orientada | 1 | 8 | 8 |
| Setup / Navegação | 1 | 7 | 7 |
| Pílula Hands-on | 4 | 6 | 24 |
| Automação/Workflow | 0 | 10 | 0 |
| Avaliação / Feedback | 6 | 4 | 24 |
| **Total** | **18** | | **129 min** |

Conferência por módulo: 7 + 25 + 19 + 20 + 20 + 20 + 18 = **129 min**.

## 4. Análise de Densidade

| Classe | Tipos | Tempo | Percentual |
|---|---|---|---|
| Teoria | Exposição Teórica (30) + Exemplo Aplicado (6) + Discussão Orientada (8) | 44 min | 34,1% |
| Prática | Demonstração (30) + Setup (7) + Pílula (24) + Avaliação (24) | 85 min | 65,9% |

O curso está próximo do alvo de 40% de teoria e 60% de prática, com leve inclinação à prática. A
inclinação é deliberada: num curso sobre conectores, a compreensão se consolida ao ver a chamada de
ferramenta e a tela de aprovação. A teoria concentra-se nos Módulos 1 e 2, antes da primeira conexão,
como exige a regra de segurança antes do uso; nenhum módulo carece de prática, pois todos, exceto o
Módulo 2, contêm Pílula Hands-on ou Setup, e o Módulo 2 tem análise de cenários com gabarito.

## 5. Aderência à carga horária alvo

Total de 129 min, dentro da faixa de 100–130 min, com 1 min de folga. Não há estouro. Caso a revisão
humana acrescente conteúdo, recomenda-se mover para anexo, em vez de reduzir tempos unitários, a
tabela de conectores interativos (Módulo 1.2) ou a variação do ChatGPT (Módulo 3.1), que já são
opcionais na prática.
