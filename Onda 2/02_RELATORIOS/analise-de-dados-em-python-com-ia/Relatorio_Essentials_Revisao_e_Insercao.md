# Relatório — Análise de Dados em Python com IA - Essentials (revisão de texto + inserção de blocos)

**Data:** 17/11/2026 (v1) · **Pacote final:** `Onda 2/01_FINALIZADO_subir-na-LMS/analise-de-dados-em-python-com-ia/analise-de-dados-em-python-com-ia-essentials-scorm12-hFEI5IWi-FINAL-com-blocos-v1.zip`

## 1. Material-fonte e mapeamento

Fonte: `Pesquisa Conteudo Onda 2/Ementa Completa/dados-com-python-e-ia-hands-on/roteiros/roteiro-articulate-essentials.md` (na ementa o curso se chama *Dados com Python e IA*; no Articulate, *Análise de Dados em Python com IA*).
Mapeamento 1:1 — L1 = Módulo 0 … L7 = Módulo 6; L8 = Quiz.

## 2. Revisão de texto (fase A)

**330 campos alterados**. `validar_texto.py`: estrutura preservada, 330 = 330.

**Erros de conteúdo corrigidos**
- **Respostas inventadas no lugar dos prompts** (L1, L2, L6, L7). A pior, na L7: um "README modelo" com `pip install -r requirements.txt`, `python main.py` e `git clone` — contradiz o curso, que usa uv e `uv run analise.py`. Na L2, uma estrutura de projeto `data/ src/ requirements.txt` diferente da do curso. Voltaram os prompts do roteiro.
- **L6 — dados das avaliações imprecisos** ("DA-Code e KramaBench acertam menos de 60%", "programadores superestimam"): substituídos pelos números da fonte (30,5% / 34,12% / 55%; METR: +19% de tempo × 20% de ganho percebido).
- **L3 — retenção de dados ausente**: os prazos (5 anos / 30 dias no Claude; transcrições locais de 30 dias; treino ativado no ChatGPT; "Incluir ambientes" no Codex) entraram no cartão de exposição de dados; números de pacotes inexistentes (19,7%; 3,6–5,0%) no cartão correspondente.
- **L2** — a definição de agente de código não aparecia; o accordion "vantagens × riscos" passou a "o que o agente faz × o que fica com você"; tabs com os números do estudo de notebooks (24,11% / 4,03%).
- **L5** — "scripts em scripts/" contradizia o projeto (analise.py na raiz); corrigido. Regras de Sandve com a origem citada.
- **Quiz**: "True/False" → "Verdadeiro/Falso"; associação com a pasta inexistente `scripts/` → `analise.py`; feedbacks com justificativa errada (questão de rotas) corrigidos.
- Aberturas genéricas, objetivos com fórmulas variadas e fechamentos "Agora que você domina…" trocados pelo conteúdo do roteiro; comandos em `<code>`.

## 3. Inserções (fase B) — 6 blocos

| Lição | Posição | Tipo | Por quê |
|---|---|---|---|
| L2 Por que código | após o process de decisão | **HTML "Conversa ou código?"** (5 casos) | aplica o critério repetição/volume/auditoria |
| L3 Segurança | antes da questão | **HTML "O agente pede permissão. E agora?"** (6 pedidos: aprovar / com cuidado / recusar) | treino com casos diferentes do gabarito do exercício |
| L4 Pedir e planejar | após os 6 cartões do brief | **HTML "Monte o seu brief"** (6 campos, copiar) | o brief vira ferramenta reutilizável |
| L5 Reprodutibilidade | após as abas | **HTML "O que há na pasta ipca-projeto"** (árvore clicável) | liga cada arquivo à prática de reprodutibilidade |
| L7 Síntese | antes da questão | **HTML checklist de entrega (5 critérios) + Continue que trava** | fecha o projeto com critério objetivo |

## 4. Validações

- Fase A: `validar_texto.py` sem divergência; ponte **APROVADO** (0 erros, 0 avisos).
- Fase B: `validar.py` **APROVADO** (6 blocos; 617 IDs distintos); `verificar_scorm.py` final **APROVADO** (0 erros, 0 avisos).

## 5. Navegador (mock de LMS)

Visto: os 5 HTMLs renderizam; o classificador de aprovações completa 6/6; o checklist da L7 trava e libera o Continue; console sem erros; HTMLs a 360 px sem rolagem horizontal.
**Não testado:** LMS real; `file://`; o fluxo real no Claude Code/Codex.

## 6. Decisões tomadas

- A questão "modo mais seguro para iniciar a sessão" foi mantida com o gabarito Manual (tabela do roteiro: "início de cada sessão"); o feedback do modo `plan` agora explica a diferença.
- Pacote do exemplo "pandas-brasil-utils" é fictício de propósito (caso de nome desconhecido a recusar).
