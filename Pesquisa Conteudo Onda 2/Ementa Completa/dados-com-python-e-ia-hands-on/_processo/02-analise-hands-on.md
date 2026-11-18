# Análise Crítica 360 — Dados com Python e IA, Hands-on v1.0

Objeto base: análise reprodutível em Python com Claude Code ou Codex · Público: quem fez o Essentials
deste assunto · Trilha: Hands-on · Tarefa observável: conduzir uma análise reprodutível em Python com
agente de código e validar resultados.

## 1. Sumário Executivo

**Nota: 2,5/10.** Tom adequado, mas a regra de ouro ("deixe o agente trabalhar") é o contrário do
que o curso precisa ensinar, nenhuma oficina tem base real nem gabarito, e a instalação é frágil
(npm, Python global). Nada é reprodutível nem validado.

- Regra de ouro perigosa para iniciante (agente age no computador).
- "Um CSV qualquer": sem problema real, sem número oficial.
- Sem pasta de projeto, sem dados brutos protegidos, sem uv.lock, sem "rodar do zero".
- Sem asserts, sem revisão independente.
- Projeto Final = repetir as oficinas.

## 2. Pontos Positivos

- Sequência ler → gráfico → relatório é natural.
- A Parte dos Dez acerta em "não apague dados", "use Git", "leia o código".

## 3. Pontos Negativos e Gargalos

1. **Regra de ouro errada** — trocar por "o agente faz; você aprova e confere".
2. **Instalação** com npm e Python global; sem verificação; sem rotas sem terminal.
3. **Sem permissões** — o agente vai pedir aprovação para comandos e o aluno não sabe o que aprovar.
4. **Sem bases reais** — perde as armadilhas que justificam código (vários arquivos, latin-1, escala,
   chave repetida, linhas de metadado).
5. **Sem reprodutibilidade** — nenhum passo de "apague resultados e rode de novo".
6. **Sem validação** — nenhum assert, nenhuma comparação com fonte oficial.
7. **Erro silencioso** não aparece — é o risco número 1 documentado em agentes de dados.
8. **Projeto Final sem missão própria nem checklist objetiva.**

## 4. Matriz de Soluções e Melhorias

| ID | Gargalo | Onde | Correção concreta | Prioridade |
|---|---|---|---|---|
| H1 | Regra de ouro | Antes de arregaçar | "O agente faz; você aprova, lê e confere. Dado bruto ninguém toca." | Alta |
| H2 | Instalação | Preparação | Rota A/B (apps de desktop) + uv pelo instalador oficial; verificação `uv --version`; pasta com `dados/brutos` | Alta |
| H3 | Sem permissões | O1 | Começar em modo plano/read-only; aprovar comandos lendo o que fazem; nunca `bypassPermissions` | Alta |
| H4 | O1 sem caso | O1 | "Primeiro projeto reprodutível": IPCA, CLAUDE.md/AGENTS.md, script, gráfico, assert 4,83%/4,26%, rodar do zero | Alta |
| H5 | O2 sem caso | O2 | "O ranking que mentia, em código": DFP da CVM lida direto do ZIP, latin-1, escala MIL/UNIDADE, linhas duplicadas; asserts | Alta |
| H6 | Sem cruzamento | O3 | "Cruzar duas tabelas": DRE × cadastro; chave repetida no cadastro; 4 sem cadastro; lucro por setor | Alta |
| H7 | Sem revisão | O4 | "Peça uma segunda opinião": `/code-review` (Claude Code) ou nova sessão revisando como auditor; teste do erro silencioso (top 5 lado a lado) | Alta |
| H8 | Projeto Final fraco | PF | "Clima do DF em 2024": 5 CSVs do INMET, 8 linhas de metadados, vazios, médias e máximas, README e asserts | Alta |
| H9 | Se travar genérico | todas | Problemas reais: comando pedindo aprovação, latin-1, pacote desconhecido, ZIP grande, `uv` não encontrado | Média |
| H10 | Quer ir além com 1 item | todas | Três desafios com validação | Baixa |
| H11 | Carga horária | geral | ~105 min | Média |

## 5. Roadmap de Expansão

Cabe como desafio: notebook gerado a partir do script; Git com commit por oficina; Portal da
Transparência (quatro tabelas, 148 MB) como alternativa do Projeto Final para o público de setor
público, sem gabarito oficial. Fica fora: CI, nuvem, painéis publicados.

Não verificado: tempo para baixar o ZIP do INMET (103 MB) em conexões lentas; Codex Free.
