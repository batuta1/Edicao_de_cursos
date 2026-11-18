# 00 — Contornos do curso IA para Análise de Dados

Documento de partida compartilhado pelas duas trilhas. Tudo o que vem depois (v1.0, auditoria,
roteiros, carga horária, ementa) se apoia nestes campos.

## Origem do pedido

| Campo | Valor |
|---|---|
| Registro no catálogo | `novos-cursos-iaclube-priorizacao-v6.json` → `"id": "ia-para-analise-de-dados-essentials"` |
| Nome no catálogo | IA para Análise de Dados - Essentials (o par Hands On é produzido na mesma rodada) |
| Onda / ranking / score | Onda 2 · ranking 18 · 84 pontos (demanda 30, ferramenta 20, base 15, lacuna 12, esforço 7) |
| Tema / linha prioritária | Dados com IA / IA aplicada ao trabalho |
| Ferramentas do catálogo | ChatGPT (recurso "Análise de dados") e Julius AI |
| Competência | Analisar e visualizar dados com IA |
| Tarefa observável | Carregar uma base, explorar, gerar gráficos e interpretar resultados com verificação. |
| Base confiável | Docs da OpenAI e da Julius |

## Objeto base

**Análise de dados sem programar, conversando com um assistente de IA que escreve e executa código
por trás** — o ciclo **carregar → entender → limpar → explorar → visualizar → interpretar →
verificar → comunicar**, feito "fora da planilha": o participante envia a base ao assistente e
analisa na conversa.

- **Ferramenta principal: ChatGPT, recurso "Análise de dados"** (ex-Code Interpreter, ex-Advanced
  Data Analysis). Não é um modo a ligar: é acionado ao enviar um arquivo e pedir a análise; o
  ChatGPT escreve e executa Python num "ambiente de notebook Jupyter com estado".
- **Ferramenta secundária: Julius AI** — espaço de trabalho especializado, com o código à vista
  ("Generating code → Generated code") e o Data Explorer. Usado como comparação e segunda opinião,
  nunca como obrigação, por causa da política de dados e dos créditos.
- **Eixo do curso: verificação.** A própria OpenAI manda "revisar o código gerado, as saídas e as
  suposições antes de confiar no resultado". Todo exercício tem gabarito em número oficial
  publicado.

## Público-alvo

O curso aparece em oito trilhas (`trilhas.json`):

| Trilha | Posição | Antes | Depois | Público |
|---|---|---|---|---|
| T8 — IA aplicada ao trabalho: planilhas e dados | 5 de 6 | ChatGPT Excel - Hands On (e os demais cursos de Excel) | Dados com Python e IA - Hands On | Analistas, financeiro e planejamento, pesquisadores |
| J4 — Dados, jurimetria e automação do escritório | 2 de 6 | Claude Excel - Essentials | Jurimetria com IA - Essentials | Escritórios médios e grandes, departamentos jurídicos, compliance |
| F2, R4, S4, TE3, E6, C2 (trilhas de dados das áreas) | 3 a 6 | ao menos um curso de Excel | — | Finanças e negócios; servidores e regulação; gestores de saúde; engenheiros e técnicos; gestores escolares; comunicação e marketing |

Consequência de design: o curso precisa funcionar para quem fez **só Claude Excel - Essentials**.
Nada de PROCV, fórmula ou complemento de planilha (é assunto dos cursos de Excel). Os exemplos
cobrem finanças (IPCA, DRE da CVM), setor público (Censo), jurídico (CNJ) e são neutros para as
demais áreas.

## Pré-requisitos

- Excel básico (abrir arquivo, ler uma tabela, saber o que é coluna e linha).
- Nenhuma programação. Nenhuma estatística além de média e porcentagem.
- Para o Hands-on: ter feito o Essentials deste assunto.

## Recursos necessários

- Computador com navegador e internet (o celular serve para ler, não para os exercícios).
- Conta ChatGPT. **O plano Free funciona, com limite**: "Usuários do plano gratuito têm um limite de
  3 uploads de arquivos por dia" e "Análise de dados: Limitado" na página de preços. Go (R$ 39,99)
  ou Plus (R$ 99,90) removem o aperto.
- Conta Julius AI gratuita, **opcional** (75 créditos de boas-vindas + 25 diários; arquivos
  apagados após 1 hora de inatividade; interface em inglês).
- Pasta no computador com as bases do curso (todas públicas, sem login, baixadas e conferidas em
  17/11/2026 — ver "Bases e gabaritos").

## Natureza e carga horária

- **Autoinstrucional.** Ninguém explica ao vivo; todo passo e todo gabarito estão no texto.
- **Essentials:** 100 a 130 min, 4 a 6 módulos de conteúdo + síntese (prompt-mestre Articulate).
- **Hands-on:** 90 a 120 min, 4 oficinas + Projeto Final (prompt-mestre Articulate).
- Uploads: o Hands-on usa **no máximo um upload por oficina** e dois no Projeto Final, para caber no
  Free em dois ou três dias de estudo. Isso é declarado ao aluno.

## Escopo — o que NÃO é deste curso

| Fica fora | Onde está |
|---|---|
| IA dentro da planilha (ChatGPT/Claude no Excel e Sheets, fórmulas, PROCV) | Cursos Claude Excel e ChatGPT Excel |
| Uso geral do ChatGPT (planos, projetos, memória, busca) | ChatGPT Chat - Essentials e Hands On |
| Escrever e manter código Python próprio, agentes de código | Dados com Python e IA (próximo da T8) |
| Estatística inferencial, modelos preditivos, machine learning | Fora do par; só "o que é e quando procurar um especialista" |
| Painéis de BI (Power BI, Looker Studio, Tableau) | Só como alternativa citada |
| Automação de relatórios recorrentes | Cursos de N8N e Zapier |
| Achar dados na web | Deep Research |

## Material-fonte

`Pesquisa Conteudo Onda 2/conteudo-bruto/ia-para-analise-de-dados-essentials/` —
`ConteudoBruto_ia-para-analise-de-dados-essentials.txt` (duas rodadas, 17/11/2026) + 31 arquivos
(PDFs, bases, dicionários). Pontos usados como fato no curso:

| Fato | Fonte |
|---|---|
| Tipos de arquivo; Jupyter com estado; "revise o código gerado, as saídas e as suposições"; sem web no Python; PDF digitalizado não confiável | Ajuda OpenAI "Análise de dados com o ChatGPT" (pt-BR, ≈19/10/2026) |
| "Alternar para gráfico interativo"/"Alternar para gráfico estático"; interativos: barras, linhas, pizza, dispersão | Idem |
| Planilhas ~50 MB; 80 arquivos a cada 3 h; Free 3 uploads/dia; `+ > Adicionar fotos e arquivos`; `Configurações > Armazenamento` | Ajuda "Envio de arquivos e áudios" (≈14/11/2026) |
| Tabela expansível (duas setas), seleção com Ctrl/Command, download CSV/PNG, cores por hexadecimal, 12 tipos de gráfico estático | Ajuda "Extraindo insights com a análise de dados" |
| `Configurações > Controles de dados > Melhorar o modelo para todo mundo`; chat temporário; Business/Enterprise não treinam | Ajudas 7730893 e 5722486 (16/11/2026) |
| Prompts e boas práticas oficiais ("Estou tentando decidir ___, com base em ___"; EDA + hipóteses; não tratar correlação como causa) | OpenAI Academy "Analisando dados com o ChatGPT" (10/04/2026) |
| Julius: `+` ou arrastar; Generated code; Data Explorer (Expand, 49 linhas); gear > Customize Julius (responder em português); créditos; arquivos 1 h/7 dias; compartilhamento com provedores de IA e opt-out por e-mail | Docs Julius e Política de Privacidade (21/10/2026) |
| 32,5% / 81,3% / 92,5% de acerto em estatística inferencial conforme o detalhe do prompt | JMIR 2025 (Ruta et al.), texto integral |
| 8 táticas de gráfico enganoso; GPT-4o enganado por eixo invertido | "The Perils of Chart Deception" (IEEE VIS 2025) |
| Falhas de gráficos gerados por IA (inválido, coluna/legenda errada, ilegível) | VisEval (IEEE VIS 2024) |
| ANPD: só estudo preliminar de anonimização (2023/2024) | ANPD |
| OAB: Recomendação 001/2024 (supervisão, sigilo, informar o cliente) | Notícia OAB; artigo IAB 2025 |

## Bases e gabaritos (conferidos por script em 17/11/2026)

| Base | Link (testado, sem login) | Formato | Gabarito oficial |
|---|---|---|---|
| B1 IPCA mensal (BCB SGS 433) | `https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2020&dataFinal=31/12/2025` | CSV UTF-8, `;`, vírgula decimal, 72 linhas | 2024 = 4,83%; 2025 = 4,26% (IBGE). Soma simples errada de 2024 = 4,73% |
| B2 População por UF (SIDRA 4709) | `https://apisidra.ibge.gov.br/values/t/4709/n3/all/v/93/p/2022?formato=csv` | CSV UTF-8, `;`, cabeçalho em 2 linhas | Brasil = 203.080.756 |
| B3 Cadastro de companhias (CVM) | `https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv` | CSV latin-1, 2.680 linhas, códigos repetidos | 756 ATIVO; 1.917 CANCELADA |
| B4 DRE consolidada 2024 (CVM DFP) | `https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2024.zip` → `dfp_cia_aberta_DRE_con_2024.csv` (6,8 MB) | CSV latin-1; escala MIL ou UNIDADE | Petrobras: receita R$ 490,8 bi; lucro atribuído aos controladores R$ 36,6 bi (consolidado R$ 37,0 bi). Ranking correto: Petrobras, Vale (31,6), BB (26,4), Bradesco (17,3), Itaúsa (14,8). Armadilha: 8 empresas em UNIDADE — sem converter, a Vivara (R$ 653 mi) sobe para 1º lugar |
| B5 Justiça em Números (CNJ) | `https://www.cnj.jus.br/wp-content/uploads/2026/09/17-set-2026.zip` → `JN_23-Jun-2026.csv` (11,6 MB) | CSV latin-1, 1.314 colunas, com linhas de total por ramo | Casos novos 2025 = 40,9 mi (coluna `cn`, sem as linhas TJ/TRF/TRT/TRE e com os superiores: 40.940.966). Soma direta = 81 mi (o dobro). TJs 2025 = 28.288.316 |

Gabarito derivado para o Projeto Final do Hands-on (casos novos 2025 nos TJs ÷ população do Censo
2022 × 100 mil): maior taxa TJRO (20.421), depois TJRS (19.986) e TJDFT (19.691); menores TJPA
(6.745), TJCE (7.893), TJPE (8.037); média Brasil (TJs) 13.930. Maiores em número absoluto: TJSP
(6.828.558), TJRJ (2.238.416), TJRS (2.175.107).

## Pendências de validação herdadas da pesquisa

1. Nome do controle que mostra o código no ChatGPT ("View analysis"/"Ver análise"?) — não está na
   ajuda oficial.
2. Tempo de vida do ambiente Python e o que acontece com os arquivos quando ele reinicia (conta
   pessoal).
3. Significado dos ícones da tabela de planos para "Tabelas e gráficos interativos" no Free.
4. Julius: botão de anexar (`+` ou clipe), preço mensal × anual, RAM do Free.
5. Nenhum exercício foi executado numa conta Free real nesta rodada.
