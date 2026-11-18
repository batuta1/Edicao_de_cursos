# 00 — Contornos do curso Vibe Coding - Essentials

Documento de partida compartilhado pelas duas trilhas. Tudo o que vem depois (v1.0, auditoria,
roteiros, carga horária, ementa) se apoia nestes campos.

## Origem do pedido

| Campo | Valor |
|---|---|
| Registro no catálogo | `novos-cursos-iaclube-priorizacao-v6.json` → `"id": "vibe-coding-essentials"` |
| Nome no catálogo | Vibe Coding - Essentials |
| Onda / ranking / score | Onda 1 · ranking 5 · 92 pontos (demanda 30, ferramenta 20, base 15, lacuna 20, esforço 7) |
| Tema / linha prioritária | Vibe Coding / App Building · Vibe Coding |
| Ferramenta-âncora | Lovable |
| Competência | Construir aplicações por linguagem natural |
| Tarefa observável | Criar, publicar e iterar um aplicativo web simples com banco de dados e autenticação. |
| Base confiável | Documentação e tutoriais oficiais da Lovable |
| Observação do catálogo | Maior demanda potencial; público sem experiência em código. |

## Objeto base

**Vibe coding com o Lovable** — criar um aplicativo web descrevendo o resultado em linguagem
natural e deixando a IA escrever o código (termo popularizado por Andrej Karpathy em fevereiro de
2025; *Word of the Year* 2025 da Collins). A ferramenta-âncora é o **Lovable** (`lovable.dev`),
plataforma que gera, a partir de conversa, um app web completo — interface, lógica, banco de dados,
login e hospedagem — e o publica num endereço `lovable.app`.

Elementos do Lovable que o curso usa (rótulos da ajuda em inglês, 18/10/2026):

| Elemento | Função |
|---|---|
| Modos **Chat / Plan / Build** | Chat conversa sem alterar código; Plan propõe um plano e espera aprovação (1 crédito por mensagem); Build executa (custo variável). Build era chamado "Agent mode". |
| Prévia e **Preview toolbar** | Testar o app; Select elements, edição de texto, Draw annotation, Add comment; Mobile view |
| **Lovable Cloud** (`More > Cloud`) | Backend padrão (baseado no Supabase open source): Database, Users, Secrets, Usage, etc. |
| **History / Revert / Bookmarks** | Versões do código; Revert restaura só o código, não os dados |
| **Publish / Publish changes** | Publica um snapshot em `[subdominio].lovable.app`, com varredura rápida de segurança; mudanças exigem republicar |
| **Knowledge** | Instruções persistentes do projeto |

## Público-alvo

| Trilha | Posição | Público |
|---|---|---|
| T5 — Vibe Coding: do zero ao app | 1 de 6 (primeiro curso; depois: Replit Agent - Essentials) | Não programadores com ideias de produto, empreendedores e professores |

Consequências de design:

1. **App-âncora comum: "Minhas Tarefas"** — lista pessoal de tarefas com login e banco, usando só
   dados fictícios. É o menor app que exercita as cinco ações da tarefa observável (criar, banco,
   login, publicar, iterar) e não exige conhecimento de domínio.
2. **Atividade final por perfil**, mesma estrutura técnica (uma tabela, login, regra "cada um vê o
   seu"): professor → *Diário de Leituras* pessoal (sem dados de alunos); empreendedor → *Banco de
   Ideias de Produto*.
3. **Zero dado real:** nada de nomes, CPF, notas, dados de alunos ou clientes. Contas de teste
   controladas pelo próprio aluno.

## Pré-requisitos

- Uso básico de um assistente de IA (ChatGPT, Claude ou Gemini).
- **Não** exige saber programar.

## Recursos necessários

- Computador com navegador atualizado e internet (o Lovable roda no navegador; não exige instalação).
- Conta gratuita no Lovable (e-mail/senha, Google, GitHub ou Apple); 18 anos ou autorização de
  responsável.
- Um e-mail próprio para a conta e a possibilidade de criar **duas contas de teste** do app (via
  "Add user" em `More > Cloud > Users` ou endereços de e-mail que o aluno controla).

## Configuração

| Campo | Valor |
|---|---|
| Autoinstrucional | **Sim.** Nenhum passo pode depender de instrutor. |
| Trilhas | Essentials (compreensão) e Hands-on (execução), ambas a partir deste objeto base. |
| Carga horária alvo — Essentials | 100–130 min (prompt-mestre `articulate-essentials.md`) |
| Carga horária alvo — Hands-on | 90–120 min (prompt-mestre `articulate-hands-on.md`) |
| Módulos/oficinas | Essentials: 4–6 módulos de conteúdo + síntese. Hands-on: 4 oficinas + Projeto Final. |
| Idioma | Português do Brasil; prompts em português; rótulos do Lovable em inglês (a ajuda está em inglês e não há confirmação de interface traduzida). |
| Plano exigido | **Gratuito**, com rota de baixo consumo. Free: 5 *build credits* por dia (teto de 30/mês), 20 Cloud credits/mês, 4 AI credits/mês, 1 connector credit/mês. O fabricante **não garante** que o exercício completo caiba no gratuito; o curso distribui as etapas em dias diferentes. |

## Fora do escopo (outro curso cobre)

- Evoluir um app existente com integrações (pagamentos, e-mail, APIs externas) → *Lovable - Hands On*.
- Replit Agent → *Replit Agent - Essentials* (próximo da trilha).
- Bolt e v0 → curso próprio.
- Programação em editor de código (Cursor, Claude Code) → cursos próprios, mais adiante na trilha.
- Supabase próprio, domínio próprio (pago), download de código (pago), Edge Functions, MCP, migração
  para hospedagem externa.

Esses temas aparecem apenas para delimitar a fronteira (uma frase, nunca um passo a passo).

## Material-fonte

Pasta `Pesquisa Conteudo Onda 1/conteudo-bruto/vibe-coding-essentials/`:

| Arquivo | Uso no curso |
|---|---|
| `ConteudoBruto_vibe-coding-essentials.txt` (18/10/2026) | Fonte principal: origem do termo, Lovable, planos e créditos, passo a passo oficial (Build, prévia, Cloud, auth, RLS, History, Publish), glossário com analogias, segurança (Secrets, RLS, scans, incidente de abril de 2026, opt-out de treinamento), LGPD, erros comuns, casos (Plinq, Elora), prompts sugeridos, exercício integrado; 53 referências. |
| `guia-anpd-seguranca-pequeno-porte.pdf` | Guia ANPD de segurança da informação para agentes de pequeno porte (21 p., pt-BR) — base do aviso LGPD. |
| `vibe-coding-in-practice-icse-2026.pdf` | Estudo acadêmico (ICSE 2026, CC BY 4.0) — benefícios e desafios relatados. |
| `vibe-coding-state-of-the-art-review-2026.pdf` | Revisão acadêmica (arXiv, 2026) — riscos de qualidade, segurança e manutenção. |

**Não houve pesquisa complementar** (diferente de Agentes de IA). Lacunas que pesam: interface só
documentada em inglês; nenhum caso independente de professor; custo real do exercício no gratuito.

Regra para dado factual: o que no conteúdo bruto está [CONFIRMADO] entra no curso com a data de
consulta; o que está [VERIFICAR] ou NÃO ENCONTRADO entra no máximo como formulação genérica e vai
para as pendências do `README.md`. Elaborações [SUGESTÃO] (analogias, modelo de requisitos,
prompts, app "Minhas Tarefas") podem ser usadas como proposta didática, nunca como fato.

## Decisões sobre rótulos de interface

Rótulos ficam **em inglês, como na ajuda oficial**, marcados **[conferir]** quando forem caminhos de
menu: `Chat`, `Plan`, `Build`, `Preview toolbar > Select elements`, `More > Cloud > Database`,
`More > Cloud > Users`, `Add user`, `Auth settings`, `More > Cloud > Secrets`, `More > Usage`,
`History`, `Revert`, `Bookmarks`, `Publish`, `Publish changes`, `Account settings > Preferences >
AI model training`, `Project settings > Knowledge`. "Agent mode" aparece só como nome antigo do Build.

## Alertas herdados do conteúdo bruto

1. **Prévia não é publicação:** depois de mudar o projeto, é preciso `Publish > Publish changes`.
2. **O navegador é inspecionável:** chave secreta nunca no prompt nem na tela; segredos em `Secrets`.
3. **RLS é o que impede um usuário de ver dados de outro;** a tela "esconder" não basta. Teste com
   duas contas é obrigatório.
4. **A varredura do Lovable não substitui revisão** ("do not replace a thorough security review").
5. **Incidente oficial:** entre 03/02 e 20/04/2026, usuários autenticados com o link de certos
   projetos públicos podiam ver histórico de chat e código; corrigido. Projetos privados e Lovable
   Cloud não foram afetados.
6. **Treinamento:** desde 09/09/2026, dados de clientes Free e Pro podem treinar modelos da Lovable,
   com opt-out em `Account settings > Preferences > AI model training`. Dados de usuários finais no
   banco do app não são usados.
7. **Revert não recupera dados apagados do banco;** `Delete rows` é irreversível.
8. **Casos de sucesso (Plinq, Elora) são da fabricante**, não auditorias; números são alegações.
9. Reportagem RedAccess (maio/2026) reúne várias plataformas; não atribuir o total à Lovable.
10. Oferta de Chat gratuito até 31/10/2026 é temporária: **não** citar como vigente.
