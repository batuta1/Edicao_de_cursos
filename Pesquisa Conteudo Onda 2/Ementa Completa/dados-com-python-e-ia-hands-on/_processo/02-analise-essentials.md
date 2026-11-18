# Análise Crítica 360 — Dados com Python e IA, Essentials v1.0

Objeto base: análise de dados reprodutível em Python com Claude Code ou Codex, para quem não programa ·
Público: T8, F2, R4, TE3 · Trilha: Essentials · Material-fonte: conteúdo bruto de 17/11/2026 (duas
rodadas, 27 PDFs).

## 1. Sumário Executivo

**Nota: 2,5/10.** A v1.0 é um curso de instalação de Python com agente acoplado, escrito para quem
já programa. Ignora as duas palavras centrais da tarefa observável — **reprodutível** e **validar** —
e contém instruções técnicas erradas ou perigosas para iniciante.

- Instalação errada/desatualizada: Claude Code e Codex têm instaladores próprios (e apps de desktop);
  "instalar pelo npm" não é o caminho recomendado; `pip install` global gera conflito de versões.
- Nenhuma palavra sobre o que o agente pode fazer no computador (apagar, alterar, executar) nem sobre
  permissões, sandbox, checkpoints e seus limites.
- Plano pago não declarado: o Claude Code não existe no plano Free.
- Reprodutibilidade ausente: pastas, versões, rodar do zero, Git.
- Validação reduzida a "o agente pode errar? sim".
- Público "não programa" contrariado: o Módulo 3 ensina `read_csv` e `groupby` como aula de pandas.

## 2. Pontos Positivos

- A ordem ambiente → agente → análise → validação é razoável e pode ser preservada como esqueleto.
- A síntese "o agente escreve, o analista decide" é a mensagem certa.

## 3. Pontos Negativos e Gargalos

1. **Requisitos e custos ocultos:** plano necessário, sistema operacional mínimo, Git for Windows.
2. **Instalação vaga e frágil:** "baixar e instalar o Python" sem dizer qual, sem verificação; npm
   exige Node.js, que o aluno não tem.
3. **Segurança ausente:** modos de permissão do Claude Code; sandbox e aprovação do Codex (rede
   desligada por padrão); trabalhar em cópia; incidentes reais (Replit, Gemini CLI, 2025); pacotes
   inexistentes sugeridos pela IA (19,7% em 2025; 3,6–5,0% em 2026).
4. **Privacidade ausente:** treino e retenção (5 anos se o usuário permitir, no Claude consumidor;
   transcrições locais por 30 dias), Codex "Incluir ambientes", LGPD.
5. **Pedido e plano ausentes:** brief, modo plano, CLAUDE.md/AGENTS.md.
6. **Reprodutibilidade ausente:** dados brutos intocados, `uv.lock`, rodar do zero; dado de Pimentel
   (24,11% dos notebooks rodam) é o argumento perfeito e não aparece.
7. **Validação rasa:** sem `assert`, sem soma de controle, sem número oficial, sem revisão
   independente; benchmarks (DA-Code 30,5%, KramaBench 55%) e erros silenciosos (69,8%) ausentes.
8. **Dados brasileiros:** latin-1 e vírgula decimal; NotebookEdit recusa arquivo não UTF-8.
9. **"Quando passar para código"** não explicado (a fronteira com o curso anterior).
10. **Exercícios sem gabarito** ("script criado", "gráfico gerado").

## 4. Matriz de Soluções e Melhorias

| ID | Gargalo | Onde | Correção concreta | Prioridade |
|---|---|---|---|---|
| E1 | Requisitos ocultos | antes de M1 | Módulo 0 com três rotas (Claude Desktop aba Code; ChatGPT desktop modo Codex; terminal), custos, requisitos e verificação (`uv --version`) | Alta |
| E2 | Instalação frágil | M1 | Trocar Python/pip global por uv (instalador oficial) + ambiente por projeto; agente pelo app de desktop | Alta |
| E3 | Segurança ausente | novo M2 | Módulo de segurança antes do primeiro uso: modos de permissão, sandbox/aprovação, cópia dos dados, checkpoints e limite com Bash, pacotes inexistentes, incidentes | Alta |
| E4 | Privacidade ausente | M2 | Treino e retenção de cada agente; Codex "Incluir ambientes"; semáforo LGPD | Alta |
| E5 | Pedido e plano ausentes | novo M3 | Brief em seis itens, modo plano/read-only, CLAUDE.md/AGENTS.md com premissas, leitura de código como leigo | Alta |
| E6 | Reprodutibilidade ausente | novo M4 | Pastas (Wilson et al.), versões (uv.lock), rodar do zero, Git mínimo, 10 regras de Sandve, dado de Pimentel | Alta |
| E7 | Validação rasa | M4 → M5 | Asserts, somas de controle, número oficial, `/code-review`/segunda sessão; benchmarks e erros silenciosos | Alta |
| E8 | Dados BR | M3 | Declarar latin-1, `;`, vírgula decimal no brief; trabalhar com script, não notebook, para arquivos não UTF-8 | Média |
| E9 | Quando passar para código | M1 | Critérios: vários arquivos, mais de 50 MB, repetir todo mês, auditoria | Média |
| E10 | Aula de pandas | M3 | Remover sintaxe; trocar por "ler o código como leigo" com glossário mínimo (pandas, Matplotlib, uv) | Alta |
| E11 | Sem gabarito | todos | Caso-guia IPCA (4,83%/4,26%) com assert | Alta |
| E12 | Carga horária | geral | 100–130 min com 5 módulos + M0 + síntese | Média |

## 5. Roadmap de Expansão

Cabe: notebooks como alternativa (com limitações), caso real da Anthropic (finanças em texto simples),
estudo METR como alerta de percepção × medição. Fica para depois: CI, empacotamento, SDKs, MCP,
machine learning, painéis publicados.

Não verificado: comportamento real do Codex Free no Brasil; rótulos em português dos apps de desktop.
