# vibe-coding-essentials

Curso **Vibe Coding - Essentials** (catálogo `novos-cursos-iaclube-priorizacao-v6.json`, Onda 1,
ranking 5), ferramenta-âncora **Lovable**, gerado com a skill `criar-ementa-curso` a partir do
conteúdo bruto em `Pesquisa Conteudo Onda 1/conteudo-bruto/vibe-coding-essentials/`. Duas trilhas:
Essentials (129 min) e Hands-on (115 min).

## Produtos

| Arquivo | O que é |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada: identificação, objetivo, competências, trilhas, carga horária, avaliação, pendências |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Roteiro final Essentials (Módulos 0–6), com sugestões de print, objetivos e habilidades por aula, Anexos A–D |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Roteiro final Hands-on (preparação, 4 oficinas, Projeto Final, Parte dos Dez, anexos) |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Versão Rise 360 do Essentials: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲, "Mão na massa" por módulo |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Versão Rise 360 do Hands-on: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲ |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | Tabela MET usada no cálculo (cópia da skill) |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | Breakdown por módulo: 18 atividades, 129 min, 39% teoria / 61% prática |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | Breakdown por oficina: 19 atividades, 115 min, 17% teoria / 83% prática |

## Processo (não é entregável)

| Arquivo | O que é |
|---|---|
| [_processo/00-contornos.md](_processo/00-contornos.md) | Objeto base, público, pré-requisitos, carga alvo, fronteiras, material-fonte, rótulos, alertas |
| [_processo/01-v1-essentials.md](_processo/01-v1-essentials.md) | Versão 1.0 do Essentials (modelo base) |
| [_processo/01-v1-hands-on.md](_processo/01-v1-hands-on.md) | Versão 1.0 do Hands-on (modelo base) |
| [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md) | Auditoria 360 do Essentials v1.0 (nota 3/10) e matriz E1–E18 |
| [_processo/02-analise-hands-on.md](_processo/02-analise-hands-on.md) | Auditoria 360 do Hands-on v1.0 (nota 2,5/10) e matriz H1–H15 |

Cada achado das matrizes tem destino declarado na seção de rastreabilidade ao fim de cada roteiro final.

## Decisões de design

- **Aplicativo-âncora "Minhas Tarefas"** com dados fictícios: o menor app que exercita as cinco ações
  da tarefa observável (criar, banco, login, publicar, iterar).
- **Construção em camadas:** interface sem back-end → Plan do back-end → Build do plano aprovado. A
  v1.0 pedia tudo num prompt só; isso gasta a cota diária e gera app impossível de depurar.
- **Lovable Cloud, não Supabase separado:** a ajuda diz "Do I need Supabase? No."; não há migração de
  um clique entre as opções.
- **Modos Chat / Plan / Build;** "Agent mode" só como nome antigo do Build.
- **Segurança antes do primeiro Build:** front-end inspecionável, Secrets, RLS, limite da varredura,
  incidente oficial de fev.–abr. 2026, LGPD/ANPD, opt-out de treinamento (Free/Pro desde 09/09/2026).
- **Teste de isolamento com duas contas** como critério obrigatório antes de publicar.
- **Prévia ≠ publicação:** `Publish changes` ensinado na prática (mudança visível só depois de
  republicar).
- **Fio condutor:** a loja (salão = front-end; fichários = banco; catraca = login; crachá e gavetas =
  RLS; ensaio × portas abertas = prévia × publicação).
- **Rota de baixo consumo e três dias** por causa dos 5 créditos de construção diários do gratuito.
- **Atividade final por perfil** com dados fictícios: Diário de Leituras (professor, sem dados de
  alunos) e Banco de Ideias de Produto (empreendedor).
- **Fora do escopo, só como fronteira:** integrações, pagamentos, Supabase próprio, domínio próprio,
  Edge Functions, Replit Agent, Bolt, v0, Cursor, Claude Code.

## O que não foi verificado (pendente de validação humana)

Nada foi testado numa conta real, e **não houve pesquisa complementar** (diferente de Agentes de IA).
Antes de gravar ou publicar:

1. **Idioma e rótulos da interface:** a ajuda está em inglês e não há confirmação de interface em
   português. Conferir todos os caminhos marcados [conferir]: `More > Usage`, `More > Cloud >
   Database`, `More > Cloud > Users > Add user`, `Preview toolbar > Select elements`, `Mobile view`,
   `History`/`Bookmarks`/`Revert`, `Publish > Publish changes`, `Account settings > Preferences > AI
   model training`, `Project settings > Knowledge`.
2. **Consumo real de créditos** de cada etapa (primeiro Build, Plan + Build do back-end, filtro,
   Projeto Final) no plano gratuito. O fabricante não garante que o exercício completo caiba; a
   divisão em três dias e a estimativa de 3–5 créditos no Projeto Final são hipóteses.
3. **"Add user":** se cria contas sem confirmação de e-mail e aceita endereços fictícios
   (`teste.a@exemplo.com`). O roteiro tem alternativa (cadastro pela tela do app com e-mails do aluno).
4. **Se a publicação consome créditos** e se a varredura bloqueia publicação no workspace gratuito.
5. **Visibilidade do projeto:** onde se define privado/público no plano gratuito (relevante pelo
   incidente de 2026).
6. **Comportamento do Lovable Cloud** ao pedir autenticação: ativação automática ou pedido de
   aprovação; formas de login geradas além de e-mail e senha.
7. **Preços e limites:** valores em dólar (página oficial, 18/10/2026); créditos, franquia de edições
   inline e "free fixes" mudam com frequência. A oferta de Chat gratuito até 31/10/2026 **não** foi
   citada.
8. **Casos de uso:** Plinq e Elora são histórias da fabricante; não há caso independente de professor
   brasileiro.
9. **Estudos acadêmicos** (ICSE 2026; revisão arXiv 2026): usados só como síntese de riscos; licença de
   redistribuição dos PDFs a confirmar antes de anexá-los ao curso.
10. **Lojas de aplicativos no Brasil:** o curso não depende dos apps móveis/desktop; não verificado.

## Próximos passos (fora desta skill)

Carregar no Articulate o `promptArticulate.md` do projeto + `roteiros/roteiro-articulate-<trilha>.md`
→ gerar o curso → verificação visual → exportar SCORM → revisar com a skill `revisar-curso-scorm`.
