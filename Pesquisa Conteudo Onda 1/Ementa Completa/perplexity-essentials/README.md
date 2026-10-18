# perplexity-essentials

Curso **Perplexity - Essentials** (catálogo `novos-cursos-iaclube-priorizacao-v6.json`, Onda 1,
ranking 3), gerado com a skill `criar-ementa-curso` a partir do conteúdo bruto em
`Pesquisa Conteudo Onda 1/conteudo-bruto/perplexity-essentials/`. Duas trilhas: Essentials (129 min)
e Hands-on (115 min).

## Produtos

| Arquivo | O que é |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada: identificação, objetivo, competências, trilhas, carga horária, avaliação, pendências |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Roteiro final Essentials (Módulos 0–6), com sugestões de print, objetivos e habilidades por aula, Anexos A–C |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Roteiro final Hands-on (preparação, 4 oficinas, Projeto Final, Parte dos Dez, anexos) |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Versão Rise 360 do Essentials: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲, "Mão na massa" por módulo |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Versão Rise 360 do Hands-on: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲ |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | Tabela MET usada no cálculo (cópia da skill) |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | Breakdown por módulo: 18 atividades, 129 min, 34% teoria / 66% prática |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | Breakdown por oficina: 18 atividades, 115 min, 10% teoria / 90% prática |

## Processo (não é entregável)

| Arquivo | O que é |
|---|---|
| [_processo/00-contornos.md](_processo/00-contornos.md) | Objeto base, público, pré-requisitos, carga alvo, escopo e fronteiras, material-fonte, decisão sobre rótulos |
| [_processo/01-v1-essentials.md](_processo/01-v1-essentials.md) | Versão 1.0 do Essentials (modelo base) |
| [_processo/01-v1-hands-on.md](_processo/01-v1-hands-on.md) | Versão 1.0 do Hands-on (modelo base) |
| [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md) | Auditoria 360 do Essentials v1.0 (nota 4/10) e matriz E1–E21 |
| [_processo/02-analise-hands-on.md](_processo/02-analise-hands-on.md) | Auditoria 360 do Hands-on v1.0 (nota 4,5/10) e matriz H1–H16 |

Cada achado das matrizes tem destino declarado na seção de rastreabilidade ao fim de cada roteiro final.

## Decisões de design

- **Citação é trilha, não prova:** fio condutor do "resumo com post-its" (Essentials) e regra de ouro
  do Hands-on, sustentados pelo dado do Tow Center (37% de erro de citação, a menor taxa entre oito
  ferramentas).
- **Tema-âncora LGPD, art. 20 (decisões automatizadas):** fontes oficiais públicas (Planalto, ANPD),
  serve aos dois públicos e dá continuidade ao curso seguinte da trilha, *NotebookLM - Essentials*, que
  também usa um corpus LGPD.
- **Referência de controle:** acórdão TJPR 0033052-89.2025.8.16.0001, com valores oficiais conhecidos,
  para a prova de existência. O exercício funciona acerte ou erre a IA.
- **Segurança antes da primeira pesquisa real:** Módulo 2 (Essentials) e setup de privacidade + semáforo
  (Hands-on), com os casos TJPR/STJ/TSE, a Recomendação CFOAB 001/2024 e a CNJ 615/2025 com escopo
  correto; prompt injection (STF) separado de alucinação.
- **Plano gratuito basta:** nenhuma Research; no máximo duas Pesquisas Pro, com plano B para quem não vê
  a opção ou esgotou a cota.
- **Rótulos:** três níveis de busca ensinados pela função, com tabela de equivalência pt-BR/inglês
  datada de 18/10/2026. **Pages não é ensinado** (só existe em ajuda legada); Spaces aparece apenas como
  nome antigo de Projetos.
- **Fora do escopo, só como fronteira:** Research auditado, Scite, Comet, Computer, Create files and apps,
  API, Model Council e escolha de modelos.

## O que não foi verificado (pendente de validação humana)

Nada foi testado numa conta real. A tela da Perplexity foi observada pela pesquisa **sem login**, em
18/10/2026. Antes de gravar ou publicar:

1. **Tela logada no plano gratuito:** onde ficam "Pesquisa Pro" e Research; se existe rótulo para a
   busca padrão (*Best*); posição do "seletor junto à caixa de pergunta" citado nos passos.
2. **Rótulos marcados [conferir]** nos roteiros: menu da conta e "Configurações", "Retenção de Dados de
   IA", "Memória", "Aplicativos e mais" (Acadêmico, Finanças, Saúde, Patentes), opções de visibilidade de
   "Compartilhar", mover pesquisa de "Recentes" para um Projeto, caminho para mudar o idioma.
3. **Plano gratuito:** se o opt-out de uso de dados para treinamento existe no gratuito (a ajuda cita
   Pro, Education Pro e Max) e se "Criar projeto" com instrução está disponível.
4. **Cotas e limites:** 3 Pesquisas Pro/dia e 1 Research/mês (ajuda de 02/09/2026); limites de upload
   (25 MB, quatro arquivos, 30 dias são legados); contradição da ajuda sobre Education Pro ("ilimitado"
   × "limites semanais").
5. **Links do kit:** reabrir os nove endereços dos anexos, em especial o acórdão do TJPR e os valores de
   controle (7ª Câmara Cível, Fabian Schweitzer, 01/06/2026). O texto compilado da LGPD
   (`l13709compilado.htm`) é o mesmo usado no curso NotebookLM; a pesquisa testou a forma `l13709.htm`.
6. **Conhecimento de controle sobre o art. 20 da LGPD** (direito de solicitar revisão de decisões tomadas
   unicamente com base em tratamento automatizado) e a menção à alteração da LGPD em 2019: vêm de
   conhecimento jurídico consolidado, não do conteúdo bruto — conferir no texto compilado.
7. **Preços:** valores em dólar das páginas oficiais (set.–out. 2026); preço em reais não publicado; a
   oferta B2C da Vivo da primeira pesquisa veio de ambiente de teste e **não** foi usada. Nenhuma oferta de
   operadora é citada como vigente.
8. **Requisitos mínimos:** iOS/iPadOS 18.0 (App Store Brasil, 18/10/2026); Android, Windows e macOS não
   localizados — o curso não os cita.
9. **Voz em português:** sem avaliação independente; aparece só como desafio opcional.
10. **Materiais de referência não reproduzidos:** `guia-oficial-perplexity-at-work.pdf` (licença não
    informada) e `relatorio-oficial-draco-deep-research.pdf` (estudo do próprio fabricante, tema de outro
    curso) foram usados só como contexto, pelas sínteses do conteúdo bruto; não foram relidos na íntegra.

## Próximos passos (fora desta skill)

Carregar no Articulate o `promptArticulate.md` do projeto + `roteiros/roteiro-articulate-<trilha>.md`
→ gerar o curso → verificação visual → exportar SCORM → revisar com a skill `revisar-curso-scorm`.
