# Análise Crítica 360 — Agentes de IA - Hands-on (v1.0)

Entrada: `_processo/01-v1-hands-on.md` + `_processo/00-contornos.md`. Trilha: Hands-on.
Leitura feita como se o texto fosse de outra pessoa.

## 1. Sumário Executivo

**Nota: 3/10.** O tom está certo e o mapa das oficinas segue a tarefa observável, mas quase nenhum
passo é executável por um iniciante sozinho, e dois são perigosos.

Principais constatações:

- **Passo quebrado:** Oficina 2 manda ativar o modo agente do ChatGPT "pelo menu de ferramentas ou
  `/agent`" — recurso descontinuado. O aluno não acha nada.
- **Passos perigosos:** "O agente pediu login → Faça login" (sem dizer onde, nem que senha nunca vai
  no chat) e "Organize meus arquivos" delegado sem pasta isolada.
- **Sem caminho gratuito** e sem material: "alguns arquivos para testar" e "um tema do seu trabalho"
  deixam o aluno inventar insumo — provavelmente com dado real.
- **"Deu certo?" não verificável:** "o agente concluiu a tarefa", "você achou um erro" (e "Não achei
  erro nenhum → Ótimo!", que ensina exatamente o contrário do curso).
- **Oficina 3 depende de o agente errar sozinho** ("quando o agente sair do escopo") — pode não
  acontecer; a oficina precisa provocar a intervenção.
- Sem segurança antes do primeiro uso, sem injeção de prompt, sem créditos; 80 min (alvo 90–120);
  "Quer ir além?" com um desafio (prompt-mestre pede três).

## 2. Pontos Positivos (Fortalezas)

| Acerto | Por que manter |
|---|---|
| Regra de ouro "o agente trabalha, a responsabilidade é sua" | Curta, memorável e verdadeira; base para o tom do curso. |
| Oficina 1 sem ferramenta (só reescrever pedido) | Primeira vitória sem custo nem conta; reduz ansiedade. |
| Progressão pedido → executar → corrigir rumo → conferir | Cobre as quatro ações observáveis do catálogo. |
| Parte dos Dez com dicas reais e independentes | Os dez itens têm base na pesquisa; nenhum é enchimento. |
| 2ª pessoa, frases curtas | Registro correto para Hands-on. |

## 3. Pontos Negativos e Gargalos (Debilidades)

**Clareza pedagógica / acionabilidade**
- Sem preparação: conta, plano, pasta, material — nada é montado antes da Oficina 2.
- Oficina 1 trabalha sobre "Organize meus arquivos", que não é a tarefa executada depois (Oficina 3
  usa "pesquisa sobre um tema do seu trabalho"): não há fio de material entre as oficinas.
- Oficina 3 sem gatilho garantido para intervir.
- Oficina 4 confere "números e nomes" sem fonte para comparar.
- Projeto Final = repetição das oficinas com tarefa real; não é missão nova e expõe dados reais.

**Rigor técnico / segurança**
- `/agent` descontinuado; nenhuma rota Work/Cowork/Manus com breadcrumb.
- Login sem orientação (formulário seguro, assumir o controle, nunca senha no chat).
- Nenhuma menção a modo Manual antes de executar; nenhuma pasta dedicada.
- Créditos do Manus ignorados: um aluno Free pode esgotar os 300 créditos diários na primeira tarefa
  ampla ("pesquisa sobre um tema").
- Injeção de prompt só aparece na Parte dos Dez.

**Engajamento**
- Problemas genéricos; não falam com o escritório nem com o jurídico.
- "Se travar" com uma linha por oficina, às vezes inútil ("Procure no menu").

**Potencial oculto**
- Não usa o diferencial que tornaria o curso memorável: ver o plano antes de deixar executar,
  redirecionar no meio sem recomeçar, pegar uma instrução escondida num documento.

**Não verificado:** consumo real de créditos do Manus por tarefa e posição exata de botões (painel de
progresso, assumir o controle, seletor de modelo) — marcar [conferir].

## 4. Matriz de Soluções e Melhorias

| ID | Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|---|
| H1 | `/agent` descontinuado | Of. 2 | Caminho principal `manus.im > Modo Agent > Manus 2.0 Lite`; alternativos `ChatGPT > Work` e `Claude > Cowork`; "modo agente" só como nome antigo | Crítica |
| H2 | Sem preparação | Antes da Of. 1 | Seção "Preparação" com conta Manus Free, pasta `Treino_Agente`, download dos PDFs do TCU e da CGU, criação do arquivo-isca | Crítica |
| H3 | Login sem orientação | Of. 2 | Substituir por: tarefas do curso não exigem login; se pedir, negar; nunca senha no chat; "assumir o controle" só em site próprio | Crítica |
| H4 | Escrita em arquivos reais | Of. 1–2 | Todas as oficinas sobre documento público, somente leitura; escrita apenas na pasta de treino | Crítica |
| H5 | Sem caminho gratuito | Antes | Tabela "qual ferramenta você tem" com plano mínimo; Manus Free como principal | Crítica |
| H6 | "Deu certo?" não verificável | Of. 2–4 | Critérios observáveis: plano antes da execução; tabela com página em todas as linhas; três linhas conferidas; registro do erro corrigido | Alta |
| H7 | "Não achei erro → Ótimo!" | Of. 4 | Trocar por: "conferir mais três linhas; zero divergência em seis linhas é o critério" | Alta |
| H8 | Intervenção depende de o agente errar | Of. 3 | Provocar: no meio da execução, o aluno acrescenta uma restrição nova (limitar a duas seções, proibir fontes externas) e verifica se o plano muda | Alta |
| H9 | Créditos ignorados | Of. 2–PF | Box ⚠️ sobre 300 créditos/dia; tarefas pequenas (PDF de 7 páginas); conferir saldo antes/depois; se acabar, continuar no dia seguinte | Alta |
| H10 | Injeção de prompt ausente | — | Oficina 4 nova: arquivo-isca com instrução escondida; o agente deve sinalizá-la e não executar; caso STJ como contexto | Alta |
| H11 | Projeto Final = repetição com dado real | PF | Missão nova por perfil (CGU para escritório; OAB 001/2024 para jurídico) com ficha de delegação, registro de intervenção e ficha de revisão | Alta |
| H12 | Carga horária 80 min | Todos | Recalcular pela MET para 90–120 min; oficinas com tempo semelhante | Alta |
| H13 | "Se travar" raso | Todas | 2–3 linhas reais por oficina (créditos, seletor ausente, agente navega sem permissão, PDF não abre) | Média |
| H14 | Um desafio em "Quer ir além?" | Todas | Três desafios por oficina, com forma de validação, incluindo as rotas Work/Cowork | Média |
| H15 | Modo de aprovação não configurado | Of. 2 | Passo explícito: Manual (Cowork), "Sempre perguntar" (Work); no Manus, pedir no prompt "pare antes de qualquer ação externa" | Média |
| H16 | Sem escolha consciente de ferramenta | PF | Desafio opcional de comparar duas ferramentas com rubrica | Baixa |

## 5. Roadmap de Expansão

| Tópico | Destino |
|---|---|
| Plano antes da execução e parada combinada | **Neste curso** (Of. 1) |
| Redirecionar sem recomeçar | **Neste curso** (Of. 2) |
| Revisão por amostragem de página | **Neste curso** (Of. 3) |
| Arquivo-isca de injeção de prompt | **Neste curso** (Of. 4) |
| Pasta local com escrita (Cowork, Meu Computador) | Desafio opcional; profundidade em *Claude Cowork - Hands On* |
| Tarefas agendadas e automações do Manus | Fora; *N8N: Agentes de IA* e cursos de ferramenta |
| Navegação autenticada pelo agente | Fora; *Agentes Web - Hands On* |
