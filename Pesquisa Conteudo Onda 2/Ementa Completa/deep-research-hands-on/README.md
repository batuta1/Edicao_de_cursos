# deep-research-hands-on

Curso **Deep Research - Hands On** (catálogo `novos-cursos-iaclube-priorizacao-v6.json`, Onda 2,
ranking 17), gerado com a skill `criar-ementa-curso` a partir do conteúdo bruto em
`Pesquisa Conteudo Onda 2/conteudo-bruto/deep-research-hands-on/`. Duas trilhas: Essentials
(120 min) e Hands-on (115 min), sem contar a espera do agente durante as execuções.

## Produtos

| Arquivo | O que é |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada: identificação, objetivo, competências, trilhas, carga horária, avaliação, pendências |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Roteiro final Essentials (Módulos 0–6), com sugestões de print, objetivos e habilidades por aula |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Roteiro final Hands-on (preparação, 4 oficinas, Projeto Final, Parte dos Dez) |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Versão Rise 360 do Essentials: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲, "Mão na massa" por módulo |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Versão Rise 360 do Hands-on: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲ |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | Tabela MET usada no cálculo (cópia da skill) |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | Breakdown por módulo: 18 atividades, 120 min, 41% teoria / 59% prática |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | Breakdown por oficina: 18 atividades, 115 min, 5% teoria / 95% prática |

## Processo (não é entregável)

| Arquivo | O que é |
|---|---|
| [_processo/00-contornos.md](_processo/00-contornos.md) | Objeto base, público (T2 posição 3; J2 posição 5), cotas, carga alvo, escopo, material-fonte, casos e gabaritos |
| [_processo/01-v1-essentials.md](_processo/01-v1-essentials.md) | Versão 1.0 do Essentials (modelo base) |
| [_processo/01-v1-hands-on.md](_processo/01-v1-hands-on.md) | Versão 1.0 do Hands-on (modelo base) |
| [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md) | Auditoria 360 do Essentials v1.0 (nota 3,5/10) e matriz E1–E15 |
| [_processo/02-analise-hands-on.md](_processo/02-analise-hands-on.md) | Auditoria 360 do Hands-on v1.0 (nota 3,5/10) e matriz H1–H14 |

Cada achado das matrizes tem destino declarado na seção de rastreabilidade ao fim de cada roteiro final.

## Decisões de design

- **Produzir e auditar pesam igual:** a tarefa observável tem dois verbos; o curso dedica a mesma
  quantidade de oficinas/módulos à produção (brief, plano) e à auditoria (afirmação–fonte–trecho,
  lacunas, norma por artigo).
- **Uma ferramenta basta, e há rota sem cota:** a Perplexity gratuita dá 1 pesquisa por mês e as
  outras não publicam número. O curso gasta no máximo três execuções, distribuídas entre
  ferramentas, e oferece o relatório público do MIT (e a busca comum, anotada) quando não há saldo.
  A comparação das três ferramentas virou discussão/desafio, nunca obrigação.
- **Gabarito em fonte primária brasileira:** IBGE (caso-guia, com a armadilha 60+ × 65+),
  Resolução CD/ANPD 15/2024 (caso jurídico, por artigo), Banco Central, Ipea e Lei 14.133 (dossiês
  do Projeto Final).
- **Nada de "vencedor":** benchmarks ensinados como leitura crítica (BrowseComp é da OpenAI; DRACO
  tem autores da Perplexity; DeepResearch Bench é de 2025); escolha por tarefa.
- **Dados antes do primeiro clique:** Data Controls (ChatGPT), Keep Activity/Temporary chat
  (Gemini), conectores com pasta mínima, prompt injection, LGPD e sigilo para o público J2.
- **Sem modelo e sem cota "atuais":** o3 e 5/25/250 por mês aparecem só como histórico de 2025.
- **Espera do agente fora da MET:** declarada na ementa e nas cargas horárias.

## O que não foi verificado (pendente de validação humana)

Nenhuma ferramenta foi testada em conta autenticada para este roteiro; os dados vêm do conteúdo
bruto de 04/11/2026. Antes de gravar ou publicar:

1. **Rótulos em pt-BR e caminhos marcados [conferir]:** menu do Gemini para Deep Research (Add
   Files ou ferramentas), Edit plan e Start research, Sources; `Download/Export` do ChatGPT;
   Temporary chat e Keep Activity no Gemini.
2. **Saldo no gratuito:** onde ChatGPT (`Settings > Usage`?) e Gemini (`Settings > Usage Limits`?)
   mostram o saldo de pesquisa profunda.
3. **Manage sites:** se `Sites > Manage sites` (restringir/priorizar) está disponível no ChatGPT
   gratuito no Brasil.
4. **Perplexity:** formatos de exportação do Deep Research; opt-out de treinamento no plano
   gratuito; local do saldo mensal.
5. **Rota sem cota:** confirmar que `mit-case-study-deep-research.pdf` traz citações suficientes
   para auditar cinco afirmações (não foi possível extrair o texto do PDF nesta sessão) e verificar
   a licença antes de oferecê-lo como download no Rise.
6. **Gabaritos voláteis:** Selic (reconferir no Banco Central na data de gravação) e valores de
   dispensa da Lei 14.133 (identificar o decreto vigente em 2026).
7. **PDF da Resolução CD/ANPD 15/2024:** confirmar a busca pelo título dentro da edição do DOU e
   os artigos citados (6º, 9º, 10).
8. **Página IBGE Educa:** caminho `Jovens > Conheça o Brasil > População > Pirâmide etária`
   (derivado do endereço) e valores 7,4%/14 milhões e 10,9%/22,2 milhões; PDF do Censo para 60+
   (15,8%; +46,6%).
9. **Preços em reais** das três ferramentas (não fixados no curso; só em dólar no contornos).

## Próximos passos (fora desta skill)

Carregar no Articulate o `promptArticulate.md` do projeto + `roteiros/roteiro-articulate-<trilha>.md`
→ gerar o curso → verificação visual → exportar SCORM → revisar com a skill `revisar-curso-scorm`.
