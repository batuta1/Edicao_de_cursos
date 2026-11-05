# Análise Crítica 360 — Vibe Coding - Essentials (v1.0)

Entrada: `_processo/01-v1-essentials.md` + `_processo/00-contornos.md`. Trilha: Essentials.
Leitura feita como se o texto fosse de outra pessoa.

## 1. Sumário Executivo

**Nota: 3/10.** A sequência conceito → criar → banco/login → publicar segue a tarefa observável,
mas o texto ensina um fluxo desatualizado, ignora o custo do plano gratuito e — o mais grave —
convida o aluno a publicar um app com dados reais sem nenhuma noção de segurança.

Principais constatações:

- **Fluxo de backend errado:** manda criar conta no Supabase e conectá-lo. O padrão atual é o
  **Lovable Cloud**, ativado pelo próprio Lovable; a ajuda responde literalmente "Do I need Supabase?
  No." Supabase próprio é alternativa, sem migração de um clique — decidir errado cedo custa caro.
- **Nome de modo desatualizado:** "Agent mode" hoje é **Build**; os modos são Chat, Plan e Build.
- **Segurança ausente:** nada sobre RLS, segredos, navegador inspecionável, varredura, incidente de
  2026 ou opt-out de treinamento. A atividade integradora sugere "controle de notas dos alunos ou
  cadastro de clientes" — dados pessoais reais (e de menores) num app publicado.
- **Créditos ignorados:** o prompt do Módulo 2 pede tudo de uma vez ("app de tarefas com login e banco
  de dados"); com 5 *build credits* por dia no gratuito, o aluno pode esgotar a cota no primeiro dia e
  receber um app que não entende.
- **"Prévia ≠ publicação" ausente:** o Módulo 4 manda "pedir uma alteração de cor" e considera "o app
  está no ar" — sem `Publish changes`, a alteração nunca chega ao público.
- **Critérios fracos:** "o app aparece na prévia", "o app está no ar". Não há teste com duas contas,
  que é o único que prova que login + banco funcionam como deveriam.
- **Carga e densidade:** 85 min (alvo 100–130), textos de um ou dois parágrafos.

## 2. Pontos Positivos (Fortalezas)

| Acerto | Por que manter |
|---|---|
| Definição com origem (Karpathy, fev. 2025; Collins) | Ancora um termo da moda em fato verificável. |
| Distinção vibe coding × no-code | Responde a dúvida típica do público ("isso é Bubble?"). |
| Sequência criar → persistir → publicar → iterar | Espelha a tarefa observável do catálogo. |
| App de tarefas como exemplo | Domínio universal, sem pré-requisito de negócio. |
| Encerramento aponta o próximo curso da trilha | Continuidade com Replit Agent - Essentials. |

## 3. Pontos Negativos e Gargalos (Debilidades)

**Clareza pedagógica**
- Sem Módulo 0: conta, plano, créditos, idioma da interface (inglês) não são tratados.
- Nenhum glossário: front-end, back-end, banco, autenticação, autorização, deploy, domínio aparecem
  sem explicação — fatal para quem "não sabe programar".
- O aluno não aprende a **especificar** antes de pedir (quatro perguntas oficiais: o quê, para quem,
  por quê, ação principal), nem o modo **Plan**.
- Iteração reduzida a "alteração de cor"; nada sobre History/Revert, uma mudança por vez, como
  descrever um erro.

**Rigor técnico**
- Supabase em vez de Lovable Cloud; Agent mode em vez de Build (ver Sumário).
- Nada sobre `More > Cloud > Database/Users` para conferir o que foi criado.
- Nada sobre RLS: login sem RLS pode deixar qualquer usuário ler os dados de outro.
- Nada sobre Revert não recuperar dados do banco.

**Engajamento / aderência**
- Professores e empreendedores sem exemplo próprio; casos reais (Plinq, Elora) ausentes.
- Síntese otimista ("qualquer pessoa pode criar um app") sem limite: não diz quando vibe coding não
  basta (dados sensíveis, pagamento, produção).

**Potencial oculto**
- Não explora Plan (pensar antes de gastar), Preview toolbar, Knowledge, browser testing, varredura de
  segurança, GitHub sync — diferenciais reais do Lovable.

**Não verificado:** a interface logada não foi observada; rótulos vêm da ajuda em inglês e devem ser
marcados [conferir]. Custo real em créditos do exercício completo é desconhecido.

## 4. Matriz de Soluções e Melhorias

| ID | Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|---|
| E1 | Supabase como caminho padrão | Mód. 3 | Substituir por Lovable Cloud ativado pelo pedido de auth/tabela; Supabase próprio só como alternativa citada, com aviso "sem migração de um clique" | Crítica |
| E2 | "Agent mode" | Mód. 2 | Ensinar Chat / Plan / Build; "Agent mode" só como nome antigo | Crítica |
| E3 | Sem segurança antes de construir | Antes do Mód. 2 | Criar módulo de segurança, dados e custos antes do primeiro Build: navegador inspecionável, Secrets, RLS, scan não substitui revisão, incidente 2026, opt-out de treinamento, LGPD/ANPD | Crítica |
| E4 | Atividade integradora com dados reais (notas de alunos, clientes) | Mód. 5 | Trocar por app do perfil com dados fictícios (Diário de Leituras; Banco de Ideias); proibir dados pessoais | Crítica |
| E5 | Prompt "tudo de uma vez" | Mód. 2 | Construir em etapas: interface sem backend → Plan do backend → Build do plano aprovado | Crítica |
| E6 | Sem Módulo 0 | Antes do Mód. 1 | Criar: conta, plano gratuito e créditos (5/dia, 30/mês), `More > Usage`, interface em inglês, rota de baixo consumo, distribuição em dias | Alta |
| E7 | Prévia ≠ publicação ausente | Mód. 4 | Ensinar `Publish` → teste em janela anônima → mudança → `Publish changes` | Alta |
| E8 | Sem teste de isolamento | Mód. 3–4 | Teste com duas contas fictícias ("Add user") como critério de êxito obrigatório | Alta |
| E9 | Sem glossário | Mód. 1 | Glossário com analogia da loja (salão, estoque, fichários, catraca, crachá/gavetas, ensaio/portas abertas, cofre) como fio condutor | Alta |
| E10 | Sem especificação nem Plan | Mód. 2 | Modelo de requisitos (quatro perguntas oficiais + dados + regra de acesso + fora do escopo + critérios de pronto) e uso de Plan | Alta |
| E11 | Iteração rasa | Mód. 4 | Uma mudança por vez; descrever erro (onde, esperado, observado); History/Revert; Revert não restaura dados | Alta |
| E12 | Carga 85 min, textos curtos | Todos | 3–5 parágrafos por módulo; recalcular pela MET para 100–130 min | Alta |
| E13 | Sem limites do método | Síntese/Encerramento | Quando vibe coding não basta (dados sensíveis, pagamento, produção); estudos acadêmicos 2026; dependência e portabilidade | Média |
| E14 | Sem casos reais | Mód. 1 | Plinq (Brasil) e Elora, com ressalva de fonte da fabricante; registrar que não há caso independente de professor | Média |
| E15 | Conferência do backend ausente | Mód. 3 | `More > Cloud > Database` e `Users` como pontos de controle | Média |
| E16 | Exercício do Mód. 1 trivial | Mód. 1 | Questão com distratores plausíveis (no-code, IA assistida em editor) e fundamentação | Média |
| E17 | Alternativas sem fronteira | Encerramento | Situar Replit Agent, Bolt, v0, Cursor em uma frase cada, sem tutorial | Baixa |
| E18 | Rótulos sem aviso | Todos | Nota de vigência e anexo de rótulos em inglês com [conferir] | Média |

## 5. Roadmap de Expansão

| Tópico | Destino |
|---|---|
| Modos Chat/Plan/Build; Preview toolbar; Knowledge | **Neste curso** (Mód. 3) |
| Lovable Cloud, Database, Users, RLS, teste com duas contas | **Neste curso** (Mód. 4) |
| Publish, Publish changes, History/Revert, varredura | **Neste curso** (Mód. 5) |
| Browser testing pelo próprio Lovable | Menção no Mód. 5 |
| GitHub sync e portabilidade | Menção no Mód. 5 (limites) |
| Integrações, pagamentos, e-mail, APIs externas | *Lovable - Hands On* |
| Supabase próprio, Edge Functions, domínio próprio | Fora (menção de fronteira) |
| Replit Agent, Bolt, v0, Cursor, Claude Code | Cursos próprios da trilha T5 |
