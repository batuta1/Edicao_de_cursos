# Análise Crítica 360 — Vibe Coding - Hands-on (v1.0)

Entrada: `_processo/01-v1-hands-on.md` + `_processo/00-contornos.md`. Trilha: Hands-on.
Leitura feita como se o texto fosse de outra pessoa.

## 1. Sumário Executivo

**Nota: 2,5/10.** O tom é leve e a promessa ("um app de verdade, no ar") é a certa, mas o roteiro
ensina exatamente os hábitos que a documentação e a pesquisa apontam como causa de apps quebrados e
inseguros.

Principais constatações:

- **Prompt-monstro na Oficina 1:** login, banco, categorias, prazos, notificações e modo escuro num
  único pedido. Contraria a recomendação oficial (uma mudança por vez), gasta os 5 créditos diários do
  gratuito e produz um app que o aluno não consegue depurar.
- **Supabase separado** na Oficina 2, quando o padrão é o Lovable Cloud.
- **"Mande para os amigos testarem"** um app com login e banco, sem teste de isolamento nem dados
  fictícios; o Projeto Final sugere "lista de alunos com notas" e "cadastro de clientes".
- **"Conserte o erro. Repita até funcionar."** — o anti-padrão clássico do vibe coding: gasta crédito,
  empilha mudanças e não usa History/Revert nem descrição de erro.
- **Nenhuma menção a `Publish changes`:** a Oficina 4 conserta o app na prévia e o site público
  continua quebrado.
- "Coloque um domínio próprio" e "login com Google" como desafios: o primeiro é pago, o segundo
  amplia escopo sem critério.
- Regra de ouro "se não gostou, peça de novo" incentiva a tentativa cega; 80 min (alvo 90–120).

## 2. Pontos Positivos (Fortalezas)

| Acerto | Por que manter |
|---|---|
| Promessa concreta no subtítulo | Motiva o público não técnico. |
| Mapa por problemas reais (esquece ao recarregar; só eu vejo; quebrou) | Formulação PBL boa; manter o espírito dos problemas. |
| Parte dos Dez com dicas certas (uma mudança por vez, histórico, republicar, dados fictícios) | Base correta — o problema é que as oficinas não as praticam. |
| Tom em 2ª pessoa, frases curtas | Registro correto para Hands-on. |

## 3. Pontos Negativos e Gargalos (Debilidades)

**Acionabilidade**
- Sem preparação: conta, créditos, `More > Usage`, interface em inglês, contas de teste.
- Nenhum ponto de controle verificável além de "aparece na tela".
- Oficina 4 depende de algo quebrar sozinho; não há gatilho.

**Rigor técnico / segurança**
- Supabase separado; nenhuma menção a Lovable Cloud, Database, Users.
- Sem RLS, sem teste com duas contas, sem varredura, sem Secrets.
- Sem opt-out de treinamento (Free e Pro, desde 09/09/2026).
- Sem History/Revert; sem aviso de que Revert não recupera dados.
- Domínio próprio indicado sem dizer que é pago.

**Engajamento**
- "Se travar" com uma linha genérica por oficina ("Tente de novo", "Espere um pouco").
- Um desafio por oficina (o prompt-mestre pede três, com validação).

**Potencial oculto**
- Não usa Plan (pensar antes de gastar), Preview toolbar (editar texto sem crédito), Mobile view,
  browser testing, Bookmarks — o que torna o Lovable bom para iniciantes.

**Não verificado:** custo real em créditos de cada oficina; se "Add user" cria contas sem confirmação
de e-mail; posição exata dos botões — marcar [conferir].

## 4. Matriz de Soluções e Melhorias

| ID | Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|---|
| H1 | Prompt-monstro | Of. 1 | Ficha de requisitos + interface sem backend no primeiro Build; funcionalidades extras viram "fora do escopo" | Crítica |
| H2 | Supabase separado | Of. 2 | Plan do backend → aprovar → Build; Lovable Cloud ativado pelo pedido; conferir `More > Cloud > Database` e `Users` | Crítica |
| H3 | Divulgar app sem teste de isolamento; dados reais | Of. 3, PF | Oficina própria de teste com duas contas fictícias antes de publicar; dados fictícios obrigatórios; Projeto Final por perfil sem dados pessoais | Crítica |
| H4 | "Conserte até funcionar" | Of. 4 | Descrever erro (onde, esperado, observado), investigar em Plan/Chat, mudança mínima; Revert pelo History | Crítica |
| H5 | Sem `Publish changes` | Of. 3–4 | Oficina de publicar → mudar → republicar, com teste em janela anônima | Crítica |
| H6 | Sem preparação | Antes da Of. 1 | Seção de preparação: conta, opt-out de treinamento, `More > Usage`, rótulos em inglês, plano de dias | Alta |
| H7 | Créditos ignorados | Todas | Box 📌 com 5/dia e 30/mês; Plan custa 1; Preview toolbar para textos; dividir em três dias | Alta |
| H8 | Regra de ouro incentiva tentativa cega | Intro | Trocar por "uma mudança por pedido, um teste depois de cada mudança" | Alta |
| H9 | Sem segurança mínima | — | Antes de publicar: varredura revisada, nada de segredo no prompt, RLS por usuário | Alta |
| H10 | Domínio próprio e Google login como desafios | Of. 2–3 | Remover domínio (pago); desafios com validação dentro do gratuito | Média |
| H11 | "Se travar" genérico | Todas | Três linhas reais por oficina (créditos, Cloud pedindo aprovação, login falha, Publish changes) | Média |
| H12 | Um desafio por oficina | Todas | Três desafios com validação | Média |
| H13 | Carga 80 min | Todos | Recalcular pela MET para 90–120 min | Alta |
| H14 | Sem Revert ensinado | Of. 4 | Passo de History + Bookmark antes de mudança arriscada; aviso de que Revert não restaura dados | Alta |
| H15 | Projeto Final = repetição | PF | Novo app do perfil na rota de baixo consumo, mesma checklist de segurança | Média |

## 5. Roadmap de Expansão

| Tópico | Destino |
|---|---|
| Ficha de requisitos e Plan | **Neste curso** (Of. 1–2) |
| Teste de isolamento com duas contas | **Neste curso** (Of. 3) |
| Publicar, mudar, republicar; History/Revert | **Neste curso** (Of. 4) |
| Browser testing pelo Lovable | Desafio opcional |
| Knowledge do projeto | Desafio opcional |
| GitHub sync | Menção |
| Integrações, pagamentos, e-mail | *Lovable - Hands On* |
| Outras ferramentas (Replit, Bolt, v0, Cursor) | Cursos próprios |
