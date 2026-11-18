# Análise Crítica 360 — IA para Análise de Dados, Hands-on v1.0

Objeto base: análise de dados sem programar com o ChatGPT e o Julius AI · Público: quem concluiu o
Essentials deste assunto · Trilha: Hands-on · Tarefa observável do Hands-on: conduzir a análise
completa de uma base pública real, do carregamento ao resumo dos achados com gráficos, conferindo
os números contra a fonte oficial.

## 1. Sumário Executivo

**Nota: 3/10.** O tom está certo e a estrutura do modelo está completa, mas nenhuma oficina tem
problema real nem resultado conferível: "uma planilha qualquer" não tem gabarito, e o "Deu certo?"
se cumpre com qualquer resposta. A tarefa observável exige conferir contra a fonte oficial — a v1.0
nunca faz isso.

- Sem bases definidas, sem links testados, sem números oficiais.
- Nenhuma armadilha real de dados brasileiros (latin-1, escala, linhas de total).
- Controles de dados e limite de 3 uploads/dia do Free ignorados.
- "Se travar" genérico ("tente outro formato").
- Projeto Final é "repita as oficinas", não uma missão nova.
- 75 min: abaixo do padrão Articulate (90–120 min).

## 2. Pontos Positivos

- Regra de ouro ("quem confere é você") é exatamente a mensagem do curso; manter.
- Progressão entender → padrões → gráfico → conclusões é boa.
- A Parte dos Dez já tem itens úteis (pedir código, conferir totais, não enviar dados pessoais).

## 3. Pontos Negativos e Gargalos

1. **Sem preparação**: não manda configurar dados nem baixar as bases; o aluno descobre o limite de
   upload no meio da Oficina 3.
2. **Oficinas sem problema real**: "você recebeu uma planilha" não é situação reconhecível nem
   conferível.
3. **Passos implícitos**: "Anexe a planilha" sem dizer onde fica o botão; "Baixe o gráfico" sem
   dizer como.
4. **Sem verificação contra fonte oficial** em nenhuma oficina.
5. **Armadilhas reais ausentes**: escala MIL/UNIDADE (Vivara sobe para 1º lugar se não converter),
   linhas de total no CNJ (soma dá o dobro), soma de taxas × composição no IPCA.
6. **Gráfico sem honestidade**: "peça para mudar as cores" não ensina eixo zero nem rótulo.
7. **Julius ausente**, embora seja ferramenta-âncora.
8. **Projeto Final sem gabarito nem critério objetivo.**
9. **"Quer ir além?"** com um desafio só; o prompt-mestre pede três, com validação.

## 4. Matriz de Soluções e Melhorias

| ID | Gargalo | Onde | Correção concreta | Prioridade |
|---|---|---|---|---|
| H1 | Sem preparação | Antes de arregaçar | Passo de controles de dados + download das bases (links testados) + plano de uploads em dois dias | Alta |
| H2 | Oficina 1 sem caso | O1 | "Quanto vale meu reajuste?": IPCA (B1), acumulado composto, gráfico; gabarito 4,83%/4,26%; armadilha 4,73% | Alta |
| H3 | Oficina 2 sem caso | O2 | "O ranking que mentia": DRE da CVM (B4), filtro ÚLTIMO + 3.11.01, conversão MIL/UNIDADE; gabarito Petrobras R$ 36,6 bi, Vivara R$ 653 mi | Alta |
| H4 | Sem armadilha de agregação | nova O3 | "O número que dobrou": CNJ (B5), linhas TJ/TRF/TRT/TRE; gabarito 40,9 mi | Alta |
| H5 | Gráfico sem honestidade | O4 | "Três gráficos, uma verdade": população por UF (B2), barras ordenadas com eixo zero × eixo truncado × pizza de 27 fatias | Alta |
| H6 | Passos implícitos | todas | Breadcrumbs para anexar (`+ > Adicionar fotos e arquivos`), expandir e baixar tabela, alternar gráfico, baixar PNG | Alta |
| H7 | Se travar genérico | todas | Problemas reais: limite de upload, acentos quebrados, "não analisou o arquivo inteiro", gráfico estático | Média |
| H8 | Julius ausente | O1 (opcional) | "Quer ir além": refazer O1 no Julius, abrir Generated code e Data Explorer, conferir o mesmo 4,83% | Média |
| H9 | Projeto Final fraco | PF | "Litigiosidade por 100 mil habitantes": juntar B5 + B2; gabarito TJRO 20.421, TJPA 6.745, TJSP maior absoluto; resumo executivo com premissas | Alta |
| H10 | Quer ir além com 1 item | todas | Três desafios por oficina, cada um com validação | Baixa |
| H11 | Carga horária | geral | 100–110 min, oficinas ~16–22 min, PF ≤ 2× oficina | Média |
| H12 | Parte dos Dez genérica | final | Itens ancorados nos erros reais vistos nas oficinas | Baixa |

## 5. Roadmap de Expansão

Cabe: comparação ChatGPT × Julius (opcional), conferência de PDF de tabela (citar limitação),
slides do resumo (desafio). Fica fora: Python próprio, BI, automação.

Não verificado: oficinas não foram executadas numa conta Free real; o tempo de processamento do
CSV de 11,6 MB do CNJ no ChatGPT Free não foi medido.
