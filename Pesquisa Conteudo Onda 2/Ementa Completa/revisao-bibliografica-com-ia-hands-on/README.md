# revisao-bibliografica-com-ia-hands-on

Curso **Revisão Bibliográfica com IA - Hands On** (catálogo `novos-cursos-iaclube-priorizacao-v6.json`,
Onda 2, ranking 11), gerado com a skill `criar-ementa-curso` a partir do conteúdo bruto em
`Pesquisa Conteudo Onda 2/conteudo-bruto/revisao-bibliografica-com-ia-hands-on/`. Duas trilhas:
Essentials (128 min) e Hands-on (115 min).

## Produtos

| Arquivo | O que é |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada: identificação, objetivo, competências, trilhas, carga horária, avaliação, pendências |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Roteiro final Essentials (Módulos 0–6), com sugestões de print, objetivos e habilidades por aula |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Roteiro final Hands-on (preparação, 4 oficinas, Projeto Final, Parte dos Dez) |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Versão Rise 360 do Essentials: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲, "Mão na massa" por módulo |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Versão Rise 360 do Hands-on: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲ |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | Tabela MET usada no cálculo (cópia da skill) |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | Breakdown por módulo: 18 atividades, 128 min, 38% teoria / 62% prática |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | Breakdown por oficina: 18 atividades, 115 min, 5% teoria / 95% prática |

## Processo (não é entregável)

| Arquivo | O que é |
|---|---|
| [_processo/00-contornos.md](_processo/00-contornos.md) | Objeto base, público (T2, posição 5), recursos e planos, carga alvo, escopo, material-fonte, caso-guia e perguntas |
| [_processo/01-v1-essentials.md](_processo/01-v1-essentials.md) | Versão 1.0 do Essentials (modelo base) |
| [_processo/01-v1-hands-on.md](_processo/01-v1-hands-on.md) | Versão 1.0 do Hands-on (modelo base) |
| [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md) | Auditoria 360 do Essentials v1.0 (nota 4/10) e matriz E1–E16 |
| [_processo/02-analise-hands-on.md](_processo/02-analise-hands-on.md) | Auditoria 360 do Hands-on v1.0 (nota 4/10) e matriz H1–H13 |

Cada achado das matrizes tem destino declarado na seção de rastreabilidade ao fim de cada roteiro final.

## Decisões de design

- **O registro é o produto, não a ferramenta:** uma planilha de quatro abas (Log, Triagem, Extração,
  Síntese) atravessa as duas trilhas e vira o dossiê/Projeto Final, com fluxograma PRISMA pt-BR e
  declaração de uso de IA (CNPq).
- **Uma ferramenta por etapa:** Semantic Scholar para descoberta e exportação; Consensus para
  panorama (Meter e tipo de estudo tratados como pista); Elicit para extração com supporting quote
  conferido no original. Base brasileira (BVS, SciELO ou BDTD) obrigatória em toda busca.
- **Tudo no plano gratuito:** Systematic Review (Pro) e exportação CSV (Plus) do Elicit não entram
  nos exercícios; a planilha substitui o CSV. O curso gasta no máximo 2 mensagens Pro do Consensus
  e 2 execuções do Research Agent.
- **Caso-guia fixo + pergunta do aluno:** telessaúde/hipertensão (PICO) nas partes guiadas; o aluno
  escolhe na Oficina 1 uma das quatro perguntas testadas (educação, comunicação, Direito, gestão
  pública) ou a própria e a leva até o Projeto Final.
- **Evidência independente sobre a IA, com amostra e data:** Meliante et al. 2025 (51,40%) e estudo
  de viabilidade 2026 (82%; 77% de reprodução; 10% de supporting quotes coincidentes).
- **Mini-revisão, não revisão sistemática:** declarado nos dois roteiros; meta-análise, risco de viés
  e GRADE ficam como fronteira.

## O que não foi verificado (pendente de validação humana)

Nada foi testado em conta autenticada; o conteúdo bruto (04/11/2026) testou só o Semantic Scholar e
uma busca pública do Consensus, sem login. Antes de gravar ou publicar:

1. **Elicit Basic — rótulos marcados [conferir]:** controle Has PDF, botão de upload de PDF no
   Research Agent, uso limitado do Research Agent (quantas execuções), e se a exportação RIS/BIB de
   referências está no Basic ou só no Plus.
2. **Elicit — "Notebooks":** se ainda existe na interface atual.
3. **Elicit — privacidade:** versão vigente da política (a pública indicava 12/09/2023).
4. **Consensus — cota Free:** 10 (página de planos) ou 15 (página de ajuda do Deep) mensagens Pro.
5. **Consensus — rótulos:** `Filter > Country` e `Filter > Study design`; caminho de planos
   (`Settings > Subscription`).
6. **Semantic Scholar:** caminho `Account > Research > Library > Export` em conta nova.
7. **DeCS:** descritores efetivamente exibidos para "hipertensão" e "telessaúde" (o roteiro manda
   anotar o que aparece, sem fixar o nome).
8. **BVS:** rótulo da pesquisa avançada.
9. **Artigo de extração** (`objnursing.uff.br/.../6885/pdf_pt`): conteúdo (população, desenho,
   desfecho) e se mede pressão arterial — o roteiro trata a exclusão provável como parte do
   exercício, mas é preciso confirmar.
10. **Contagens de busca** (8.230; 433,1 mil; 6 de 10): são de 04/11/2026; repetir no ambiente de
    gravação e atualizar ou apresentar como "em 04/11/2026".
11. **Checklist PRISMA pt-BR:** os links do checklist e do checklist expandido retornaram 404; o
    curso usa só a declaração e o fluxograma pt-BR (baixados) e o checklist em inglês.
12. **Licenças:** fluxograma PRISMA é CC BY 4.0; guias CAPES/BVS/JBI não tinham licença visível —
    decidir se viram download no Rise ou só link.

## Próximos passos (fora desta skill)

Carregar no Articulate o `promptArticulate.md` do projeto + `roteiros/roteiro-articulate-<trilha>.md`
→ gerar o curso → verificação visual → exportar SCORM → revisar com a skill `revisar-curso-scorm`.
