# Relatório — IA para Análise de Dados - Essentials (revisão de texto + inserção de blocos)

**Data:** 17/11/2026 (v1) · **Pacote final:** `Onda 2/01_FINALIZADO_subir-na-LMS/ia-para-analise-de-dados/ia-para-analise-de-dados-essentials-scorm12-leCGQBuW-FINAL-com-blocos-v1.zip`

## 1. Material-fonte e mapeamento

Fonte: `Pesquisa Conteudo Onda 2/Ementa Completa/ia-para-analise-de-dados-essentials/roteiros/roteiro-articulate-essentials.md`.
Mapeamento 1:1 — L1 = Módulo 0 … L8 = Módulo 7; L9 = Quiz gerado pelo Articulate.

## 2. Revisão de texto (fase A)

Trabalho em `05_ARQUIVOS_DE_TRABALHO/ia-para-analise-de-dados/essentials/` (mapas em `revisao_textos/L01–L09.json`). **445 campos alterados** (L1 45 · L2 65 · L3 40 · L4 50 · L5 41 · L6 65 · L7 59 · L8 44 · Quiz 36). `validar_texto.py`: estrutura preservada, 445 = 445.

**Erros de conteúdo corrigidos**
- **"Mão na massa" com respostas inventadas** (L1, L2, L3, L5, L7): o Articulate escreveu uma "resposta do ChatGPT" no lugar do prompt — numa delas, um limite de "20 MB por arquivo no plano Plus" que não está na fonte. Voltaram os prompts do roteiro.
- **L1 — questão do Módulo 1 duplicada no Módulo 0**: reescrita como questão do próprio Módulo 0 (planejar os envios no plano Free), mantendo a alternativa correta na mesma posição.
- **L2 — "sete etapas" erradas**: process e accordion listavam "carregar e entender, limpar, …, conferir, resumir". Corrigido para as sete do roteiro (carregar, entender, limpar, explorar, visualizar, interpretar, comunicar), com a conferência atravessando todas.
- **L3 e L5** — objetivos que não batiam com o plano de aula; alinhados.
- **L8** — dica errada ("ativar o chat temporário para dados sensíveis"): dado sensível não vai para conta pessoal, com ou sem chat temporário. Reescrita.
- **Quiz**: alternativas "True/False" em inglês → "Verdadeiro/Falso"; associação correlação × causa com quatro pares quase iguais (ambígua) → quatro conceitos × exemplo das bases; lacuna "a etapa conferir" (não é etapa) → "o número só vale depois da conferência"; alternativa com o "20 MB" inventado substituída.
- Cabeçalhos genéricos, fórmulas variadas de objetivos e fechamentos "Prepare-se…/Parabéns!" trocados pelo conteúdo concreto do roteiro (gabaritos, analogias, números das bases, próximos cursos).
- Nome do curso seguinte padronizado com o título real: *Análise de Dados em Python com IA*.

## 3. Inserções (fase B) — 8 blocos

| Lição | Posição | Tipo | Por quê |
|---|---|---|---|
| L3 Privacidade | antes da questão | **HTML "Semáforo de dados"** (6 bases novas para classificar) | prática do semáforo antes da verificação, sem entregar o gabarito da questão |
| L4 Carregar | antes do exercício | **HTML "O mesmo arquivo, lido de três jeitos"** (separador e decimal alternáveis sobre as linhas reais do ipca.csv) | o erro de leitura era só descrito; agora se vê |
| L5 Explorar | após o ponto de controle | **HTML calculadora "Somar ou compor?"** | o 2,01% × 2% e o 4,83% × 4,73% viram conta que o participante faz |
| L5 Explorar | antes do Mão na massa | **Questão em cenário** (SP × RR: taxa por 100 mil) | a lição não verificava taxas |
| L6 Gráficos | após as 8 táticas | **HTML simulador de eixo truncado** (valores ilustrativos, rotulados como tal) | mostra a distorção em vez de descrevê-la |
| L7 Verificar | após a rotina de 5 conferências | **HTML "Qual premissa falhou?"** (5 casos das bases × escala, linha de total, fórmula, leitura parcial, codificação) | aplica a rotina aos erros documentados |
| L8 Síntese | antes da questão | **HTML checklist dos 5 critérios + Continue que trava** | fecha a atividade integradora com critério objetivo |

HTMLs em `05_ARQUIVOS_DE_TRABALHO/ia-para-analise-de-dados/html/` (fontes em `src/`, `build.py`); roteiros gerados por `gerar_roteiros.py`.

## 4. Validações

- Fase A: `validar_texto.py` sem divergência; reempacotamento com round-trip, 0 arquivos alterados fora do alvo; ponte `verificar_scorm.py` **APROVADO** (0 erros, 0 avisos).
- Fase B: `validar.py` **APROVADO** (8 blocos novos; 785 IDs distintos); `verificar_scorm.py` do pacote final contra o revisado **APROVADO** (0 erros, 0 avisos).

## 5. Navegador (mock de LMS)

Visto: os 6 HTMLs renderizam nas lições certas; o checklist da L8 mostra o cadeado e libera o Continue com os 5 itens; retomada volta à lição salva; console sem erros; os HTMLs a 360 px sem rolagem horizontal.
**Não testado:** LMS real; abertura por `file://`; o fluxo real no ChatGPT/Julius.

## 6. Decisões tomadas

- Gabaritos numéricos (4,83%, 4,26%, 4,73%, 72 linhas, 2.680 linhas, 7,52/3,94 mi, R$ 653 mi, 40,9 mi) vêm do roteiro, que já foi recalculado por script nas bases públicas.
- Simulador de eixo usa valores ilustrativos (40 e 36 mi), declarados no próprio bloco, para não inventar dado oficial.
- A descrição da capa do curso (gerada pelo Articulate) não foi alterada: não é campo de lição.
