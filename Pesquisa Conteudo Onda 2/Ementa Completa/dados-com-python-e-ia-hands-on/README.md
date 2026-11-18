# dados-com-python-e-ia-hands-on

Curso **Dados com Python e IA** (catálogo `novos-cursos-iaclube-priorizacao-v6.json`, Onda 3,
ranking 47, antecipado para fechar a T8; par Essentials produzido na mesma rodada), gerado com a
skill `criar-ementa-curso` a partir do conteúdo bruto em
`Pesquisa Conteudo Onda 2/conteudo-bruto/dados-com-python-e-ia-hands-on/`. Duas trilhas: Essentials
(111 min) e Hands-on (105 min).

## Produtos

| Arquivo | O que é |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada: identificação, objetivo, competências, trilhas, carga horária, avaliação, pendências |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Roteiro final Essentials (Módulos 0–6), com sugestões de print, objetivos e habilidades por aula |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Roteiro final Hands-on (preparação, 4 oficinas, Projeto Final, Parte dos Dez) |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Versão Rise 360 do Essentials: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲, "Mão na massa" por módulo |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Versão Rise 360 do Hands-on: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲ |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | Tabela MET usada no cálculo (cópia da skill) |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | Breakdown por módulo: 16 atividades, 111 min, 32% teoria / 68% prática |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | Breakdown por oficina: 19 atividades, 105 min, 11% teoria / 89% prática |

## Processo (não é entregável)

| Arquivo | O que é |
|---|---|
| [_processo/00-contornos.md](_processo/00-contornos.md) | Objeto base, público (T8, F2, R4, TE3), rotas e custos, escopo, material-fonte, bases e gabaritos |
| [_processo/01-v1-essentials.md](_processo/01-v1-essentials.md) | Versão 1.0 do Essentials (modelo base) |
| [_processo/01-v1-hands-on.md](_processo/01-v1-hands-on.md) | Versão 1.0 do Hands-on (modelo base) |
| [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md) | Auditoria 360 do Essentials v1.0 (nota 2,5/10) e matriz E1–E12 |
| [_processo/02-analise-hands-on.md](_processo/02-analise-hands-on.md) | Auditoria 360 do Hands-on v1.0 (nota 2,5/10) e matriz H1–H11 |

Cada achado das matrizes tem destino declarado na seção de rastreabilidade ao fim de cada roteiro final.

## Decisões de design

- **O aluno não programa:** pede, aprova, lê por blocos e confere. Nenhuma aula de sintaxe de
  pandas; vocabulário mínimo com analogias.
- **Sem terminal para o agente:** rotas recomendadas são o app Claude Desktop (aba Code) e o app de
  desktop do ChatGPT (modo Codex); o terminal aparece só para o uv. O curso declara que não há rota
  gratuita garantida (Claude Code fora do Free; Codex Free em liberação gradual).
- **uv no lugar de pip global:** instala Python e bibliotecas por projeto e gera `uv.lock`
  (reprodutibilidade).
- **Script como formato principal:** notebooks ficam como desafio, pelas limitações documentadas de
  edição (UTF-8, saídas apagadas) e pelo dado de Pimentel et al. (24,11% rodam).
- **Segurança antes do primeiro uso:** modos de permissão, rede desligada no Codex, limite do
  `/rewind` com comandos Bash, incidentes de 2025, pacotes inexistentes (19,7% → 3,6–5,0%).
- **Armadilhas reais medidas por script:** escala MIL/UNIDADE e duplicatas na DFP da CVM; 107 códigos
  repetidos no cadastro; pareamento posicional em tabela "lado a lado"; 8 linhas de metadados e vazios
  no INMET.
- **Validação em quatro defesas:** assert, contagem de controle, número oficial, revisão independente
  (`/code-review` ou nova sessão).

## O que não foi verificado (pendente de validação humana)

1. **Execução com agente real:** nenhum roteiro foi executado no Claude Code ou no Codex; os
   gabaritos vêm de script independente sobre as mesmas bases (17/11/2026).
2. **Rótulos dos apps de desktop** em português: aba Code, seleção de pasta, modos de permissão;
   menu de modos do ChatGPT, "Work in > This computer", `/permissions` no app.
3. **Codex no Free** no Brasil: disponibilidade e limites.
4. **uv:** comandos `uv init`, `uv add`, `uv run` e instalação de Python (só a página de instalação
   foi lida).
5. **`/code-review`** no app de desktop do Claude (documentado no terminal).
6. **Caminho da opção de treino** nas configurações da conta Claude.
7. **Preços** em reais (17/11/2026) — reconferir antes da gravação.
8. **Leitura direta de ZIP:** o roteiro pede que o agente leia os CSVs de dentro do ZIP; confirmar
   que o agente não extrai para `dados/brutos` por conta própria.

## Próximos passos (fora desta skill)

Carregar no Articulate o `promptArticulate.md` do projeto + `roteiros/roteiro-articulate-<trilha>.md`
→ gerar o curso → verificação visual → exportar SCORM → revisar com a skill `revisar-curso-scorm`.
