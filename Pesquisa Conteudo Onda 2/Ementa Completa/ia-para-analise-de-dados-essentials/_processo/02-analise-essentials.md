# Análise Crítica 360 — IA para Análise de Dados, Essentials v1.0

Objeto base: análise de dados sem programar com o ChatGPT (Análise de dados) e o Julius AI ·
Público: T8, J4 e trilhas de dados das áreas (pré-requisito: Excel básico; pode ter feito só Claude
Excel - Essentials) · Trilha: Essentials · Material-fonte: conteúdo bruto de 17/11/2026 (duas
rodadas).

## 1. Sumário Executivo

**Nota: 3/10.** A v1.0 tem a estrutura do modelo, mas ensina o oposto do que a tarefa observável
pede: o verbo "com verificação" não aparece em nenhum exercício, e o curso trata o número que a IA
devolve como resposta final. Há erro factual (recurso para "ativar nas configurações", nome
"Advanced Data Analysis" como atual) e nenhum exercício é executável sem decisões que o aluno não
sabe tomar ("baixar uma planilha pública de interesse").

- Verificação ausente: nenhum gabarito numérico, nenhuma base com número oficial publicado.
- Privacidade ausente: o aluno envia arquivos ao ChatGPT antes de saber que, no plano pessoal, o
  conteúdo pode treinar modelos.
- Formatos brasileiros ignorados: separador `;`, vírgula decimal, latin-1 — o primeiro tropeço real
  de quem baixa dado público no Brasil.
- Limite do plano Free (3 uploads/dia) não declarado; exercícios podem travar no meio.
- Julius citado sem papel; sua política de dados (compartilhamento com provedores de IA) não aparece.
- 90 min e 4 módulos: abaixo do prompt-mestre Articulate (100–130 min, 4–6 módulos).

## 2. Pontos Positivos

- Sequência carregar → explorar → visualizar → interpretar é a ordem natural do trabalho e deve
  ser mantida como espinha do curso.
- A questão "correlação × causalidade" no Módulo 4 é o embrião certo da interpretação crítica.
- Registro formal e impessoal está correto para a trilha.

## 3. Pontos Negativos e Gargalos

1. **Fato errado sobre a ferramenta.** "Advanced Data Analysis" é nome antigo; o recurso hoje se
   chama "Análise de dados" e não é ligado em configurações — é acionado ao enviar arquivo e pedir
   análise (ajuda OpenAI, out/2026). O aluno vai procurar uma chave que não existe.
2. **Sem Módulo 0.** Não se verifica conta, plano, limite de upload nem se baixam as bases antes de
   começar.
3. **Segurança depois do uso.** O primeiro envio de arquivo acontece no Módulo 2 sem que o aluno
   saiba de controles de dados, chat temporário, LGPD, sigilo (OAB) ou da política do Julius.
4. **Exercícios sem gabarito.** "Valores obtidos", "gráfico baixado": critérios que qualquer
   resposta errada cumpre.
5. **Base indefinida.** "Uma planilha pública de interesse" gera fricção (qual? onde? em que
   formato?) e torna o gabarito impossível.
6. **"Código por trás" ausente.** O aluno não sabe que o número vem de um programa que ele pode ler;
   sem isso, "verificar" vira fé.
7. **Estatística mínima rasa.** Média e mediana citadas sem analogia; faltam taxa/per capita,
   nominal × real, porcentagem × ponto percentual — exatamente os erros dos públicos financeiro,
   jurídico e público.
8. **Gráficos sem crítica.** Não há gráfico enganoso, nem acessibilidade, nem os botões reais
   ("Alternar para gráfico interativo", cores por hexadecimal, download PNG).
9. **Erros documentados da IA ausentes.** O estudo JMIR 2025 (32,5% de acerto com prompt básico ×
   92,5% com prompt detalhado) e as armadilhas reais das bases (escala MIL/UNIDADE na CVM, linhas de
   total no CNJ) são o melhor material do assunto e não aparecem.
10. **Comunicar resultados** fica em uma frase; faltam premissas e limitações, que a própria OpenAI
    recomenda pedir.
11. **Encadeamento fraco:** notas de encadeamento genéricas; nenhum fio condutor.
12. **Carga horária** abaixo do padrão Articulate e módulo de síntese sem tempo coerente.

## 4. Matriz de Soluções e Melhorias

| ID | Gargalo | Onde | Correção concreta | Prioridade |
|---|---|---|---|---|
| E1 | Nome e acionamento errados | M1 | Substituir por "Análise de dados" (ex-Code Interpreter/ADA), acionada ao anexar arquivo; remover "ativar nas configurações" | Alta |
| E2 | Sem verificação inicial | antes de M1 | Criar Módulo 0: conta, plano (Free = 3 uploads/dia), pasta com as cinco bases baixadas por link testado | Alta |
| E3 | Segurança tardia | M2 | Criar módulo de dados e sigilo ANTES do primeiro envio: controles de dados, chat temporário, Julius (compartilhamento + opt-out), semáforo LGPD/sigilo com 5 casos | Alta |
| E4 | Exercícios sem gabarito | todos | Trocar por bases fixas com número oficial: IPCA 2024 4,83%; Censo 203.080.756; Petrobras R$ 36,6 bi; CNJ 40,9 mi | Alta |
| E5 | Base indefinida | M2, M5 | Fixar B1–B5 com link testado e formato descrito | Alta |
| E6 | Código invisível | M1, M6 | Explicar Jupyter com estado e "revisar código, saídas e suposições"; exercício de ler o cálculo (4,83% composto × 4,73% somado) | Alta |
| E7 | Formatos BR | M2 | Módulo de carregar/entender/limpar com `;`, vírgula decimal, latin-1, cabeçalho de 2 linhas (SIDRA) e "Raio X" | Alta |
| E8 | Estatística rasa | M4 | Média × mediana, outlier, taxa por 100 mil, nominal × real, % × p.p., correlação × causa — cada um com analogia formal e exemplo nas bases | Média |
| E9 | Gráficos sem crítica | M3 | Botões reais, tipos interativos, oito táticas enganosas (IEEE VIS 2025), acessibilidade | Alta |
| E10 | Erros da IA ausentes | M4 | Módulo de verificação: JMIR 2025, VisEval, armadilhas CVM/CNJ, rotina de cinco conferências | Alta |
| E11 | Comunicação rasa | M4 | Resumo executivo com premissas, limitações e fonte; prompts oficiais da OpenAI | Média |
| E12 | Julius sem papel | M1 | Julius como segunda opinião (Generated code, Data Explorer, resposta em português), opcional | Média |
| E13 | Sem fio condutor | todos | Plantar "o número só vale com a conferência" no M1 e retomar em M3, M5, M6; caso IPCA atravessando os módulos | Média |
| E14 | Carga horária | geral | Recalcular para 100–130 min com 6 módulos + síntese | Média |
| E15 | Quando parar | M4 | Bloco "quando procurar um especialista" (inferência, previsão) e ponte para Dados com Python e IA | Baixa |

## 5. Roadmap de Expansão

Cabe neste curso: conectores Google Drive/OneDrive (citação, sem exercício), "Tabelas e gráficos
interativos", Julius como comparação, plugin Data apenas citado.
Fica para cursos seguintes: Python próprio e reprodutibilidade (Dados com Python e IA); jurimetria
(Jurimetria com IA); painéis de BI; automação de relatórios (N8N, Zapier); estatística inferencial.

Não verificado: nome do botão que exibe o código no ChatGPT; comportamento da conta Free nos
exercícios (nenhum teste em conta real nesta rodada).
