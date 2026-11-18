# checagem-de-fontes-e-citacoes-essentials

Curso **Checagem de Fontes e Citações - Essentials** (catálogo `novos-cursos-iaclube-priorizacao-v6.json`,
Onda 2, ranking 10), gerado com a skill `criar-ementa-curso` a partir do conteúdo bruto em
`Pesquisa Conteudo Onda 2/conteudo-bruto/checagem-de-fontes-e-citacoes-essentials/`. Duas trilhas:
Essentials (130 min) e Hands-on (115 min).

## Produtos

| Arquivo | O que é |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada: identificação, objetivo, competências, trilhas, carga horária, avaliação, pendências |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Roteiro final Essentials (Módulos 0–6), com sugestões de print, objetivos e habilidades por aula |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Roteiro final Hands-on (preparação, 4 oficinas, Projeto Final, Parte dos Dez) |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Versão Rise 360 do Essentials: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲, "Mão na massa" por módulo |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Versão Rise 360 do Hands-on: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲ |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | Tabela MET usada no cálculo (cópia da skill) |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | Breakdown por módulo: 17 atividades, 130 min, 55% teoria / 45% prática |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | Breakdown por oficina: 18 atividades, 115 min, 5% teoria / 95% prática |

## Processo (não é entregável)

| Arquivo | O que é |
|---|---|
| [_processo/00-contornos.md](_processo/00-contornos.md) | Objeto base, público (T2 e J2), recursos, carga alvo, escopo, material-fonte, pares de exercício |
| [_processo/01-v1-essentials.md](_processo/01-v1-essentials.md) | Versão 1.0 do Essentials (modelo base) |
| [_processo/01-v1-hands-on.md](_processo/01-v1-hands-on.md) | Versão 1.0 do Hands-on (modelo base) |
| [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md) | Auditoria 360 do Essentials v1.0 (nota 4/10) e matriz E1–E15 |
| [_processo/02-analise-hands-on.md](_processo/02-analise-hands-on.md) | Auditoria 360 do Hands-on v1.0 (nota 4,5/10) e matriz H1–H12 |

Cada achado das matrizes tem destino declarado na seção de rastreabilidade ao fim de cada roteiro final.

## Decisões de design

- **Método antes da ferramenta:** o curso ensina três camadas (identidade, fidelidade, estado da
  evidência) e um fluxo de oito passos; Perplexity e Scite entram como apoio a cada camada, e as
  bases oficiais (DOI.org, Crossref, SciELO, PubMed, STJ, Planalto) como autoridade final.
- **Scite opcional:** é paga, o teste renova automaticamente e não há convênio CAPES conhecido.
  Toda atividade tem rota gratuita; as Smart Citations são ensinadas com o relatório de exemplo
  público da Scite e com o artigo técnico de 2021.
- **Cinco pares fixos + um caso jurídico** nas duas trilhas: correto, existe sem sustentar,
  contestado (power posing), inexistente (referência inventada de propósito, DOI 10.9999) e
  retratado (SciELO); caso real STJ HC 1.023.732.
- **Segurança antes da primeira consulta:** Módulo 2 (Essentials) e semáforo da preparação
  (Hands-on). Reference Check de manuscrito próprio não é ensinado; aparece só como desafio
  opcional com PDF público.
- **Perplexity gratuita:** o curso consome no máximo duas das três Pro Searches diárias.
- **Carga Essentials no teto (130 min) e com 55% de teoria:** desvio declarado e justificado em
  `carga-horaria/carga-horaria-essentials.md`, com proposta de ajuste.

## O que não foi verificado (pendente de validação humana)

Nada foi testado em conta real; os dados vêm do conteúdo bruto de 04/11/2026. Antes de gravar ou
publicar:

1. **Perplexity — rótulos marcados [conferir]:** seletor do modo Academic, botão Check Sources,
   painel Sources e posição da conta no menu lateral; se Academic e Check Sources estão
   disponíveis no plano gratuito.
2. **Perplexity — dados do plano gratuito:** se as consultas podem ser usadas para treinamento (a
   ajuda só descreve opt-out para Pro, Education Pro e Max).
3. **Scite — caminhos:** `Search > Report > filtros Supporting/Contrasting/Mentioning`,
   Reference Check e Collections/alertas (parte vem de tutoriais de 2021).
4. **Scite — teste:** se exige cartão no Brasil e com que antecedência cancelar; preço em reais.
5. **Scite — retenção** de PDFs enviados ao Reference Check (não encontrada em fonte pública).
6. **STJ:** se o HC 1.023.732 está indexado na pesquisa de jurisprudência ou só na consulta
   processual; rótulos atuais do menu `stj.jus.br > Jurisprudência`; o que exatamente a notícia de
   18/10/2026 diz sobre o texto atribuído ao art. 436, §1º, do CPP (o roteiro manda comparar, não
   reproduz o texto falso).
7. **Planalto:** caminho de menu até o CPP (o roteiro dá também o endereço direto `del3689.htm`).
8. **Links dos pares:** SciELO do artigo retratado, aviso DOI 10.5380/rinc.v11i1.94614, PDF público
   de Ranehill et al. na Universidade de Zurique (não baixado na pesquisa), DOIs dos pares 1 e 3.
9. **Par 2 (gabarito):** confirmar no PDF de Nicholson et al. os termos "precision", "recall", "F1"
   e "coverage" indicados para Localizar e a redação sobre desempenho por classe.
10. **Relatório de exemplo da Scite:** o arquivo `scite-reference-check-sample.pdf` é um relatório
    de busca por citation statements (tremelimumab, 12/8/2021), não um Reference Check de
    manuscrito; o curso o apresenta como "relatório de exemplo". Definir se ele será
    disponibilizado como download no Rise (verificar licença) ou só referenciado pelo link oficial.
11. **Questão do Módulo 1:** o número "REsp 1.765.432/SP" é ilustrativo; confirmar que não
    corresponde a processo real com conteúdo constrangedor, ou trocar por número claramente
    fictício.

## Próximos passos (fora desta skill)

Carregar no Articulate o `promptArticulate.md` do projeto + `roteiros/roteiro-articulate-<trilha>.md`
→ gerar o curso → verificação visual → exportar SCORM → revisar com a skill `revisar-curso-scorm`.
