# notebooklm-essentials

Curso **NotebookLM - Essentials** (catálogo `novos-cursos-iaclube-priorizacao-v6.json`, Onda 1,
ranking 1), gerado com a skill `criar-ementa-curso` a partir do conteúdo bruto em
`Pesquisa Conteudo Onda 1/conteudo-bruto/notebooklm-essentials/`. Duas trilhas: Essentials (129 min)
e Hands-on (115 min).

## Produtos

| Arquivo | O que é |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada: identificação, objetivo, competências, trilhas, carga horária, avaliação, pendências |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Roteiro final Essentials (Módulos 0–6), com sugestões de print, objetivos e habilidades por aula |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Roteiro final Hands-on (preparação, 4 oficinas, Projeto Final, Parte dos Dez) |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Versão Rise 360 do Essentials: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲, "Mão na massa" por módulo |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Versão Rise 360 do Hands-on: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲ |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | Tabela MET usada no cálculo (cópia da skill) |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | Breakdown por módulo: 18 atividades, 129 min, 34% teoria / 66% prática |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | Breakdown por oficina: 18 atividades, 115 min, 10% teoria / 90% prática |

## Processo (não é entregável)

| Arquivo | O que é |
|---|---|
| [_processo/00-contornos.md](_processo/00-contornos.md) | Objeto base, público, pré-requisitos, carga alvo, escopo e fronteiras, material-fonte |
| [_processo/01-v1-essentials.md](_processo/01-v1-essentials.md) | Versão 1.0 do Essentials (modelo base) |
| [_processo/01-v1-hands-on.md](_processo/01-v1-hands-on.md) | Versão 1.0 do Hands-on (modelo base) |
| [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md) | Auditoria 360 do Essentials v1.0 (nota 4,5/10) e matriz E1–E17 |
| [_processo/02-analise-hands-on.md](_processo/02-analise-hands-on.md) | Auditoria 360 do Hands-on v1.0 (nota 5/10) e matriz H1–H15 |

Cada achado das matrizes tem destino declarado na seção de rastreabilidade ao fim de cada roteiro final.

## Decisões de design

- **Nome do produto:** o catálogo diz NotebookLM; o produto chama-se Gemini Notebook desde 16/07/2026.
  O curso mantém "NotebookLM", explica a mudança no início e ancora toda a navegação em
  `notebook.google.com`.
- **Corpus único para os três públicos:** Caderno/Kit LGPD (lei no Planalto, dois guias PDF da ANPD,
  página Titular de Dados) — público, oficial, em português, sem dado pessoal do aluno.
- **Segurança antes do primeiro upload:** Módulo 2 (Essentials) e semáforo do upload (Hands-on).
- **Plano gratuito basta:** recursos pagos/18+ (Video Overview Cinematic, Deep Research) só aparecem
  como fronteira.
- **"Resumo" da tarefa observável** = modelo `Estúdio > Relatórios > Documento de resumo`.

## O que não foi verificado (pendente de validação humana)

Nada foi testado numa conta real; os dados vêm do conteúdo bruto de 17/10/2026. Antes de gravar ou
publicar:

1. **Rótulos pt-BR marcados [conferir]** nos roteiros: opção de adicionar fonte e de site/link,
   renomear notebook pelo título, `Configure Chat`, `Save to note`, "visualização da conversa",
   "Gerar mais tarde". A ajuda em português é parcialmente traduzida por máquina.
2. **Marca na interface:** qual nome aparece de fato (NotebookLM, Gemini Notebook ou ambos).
3. **Limites:** cotas do plano gratuito (100 notebooks, 50 fontes, 50 chats, 3 áudios, 10
   relatórios/testes/mapas por dia) e como se combinam com o consumo computacional (janelas de 5 h,
   teto semanal).
4. **Links do Kit LGPD:** testar os quatro; conferir que os PDFs baixados são os guias (21 e 58 páginas),
   e não a página HTML do portal gov.br.
5. **Linha do tempo:** confirmar que não existe como botão fixo do Estúdio.
6. **Resumo em Áudio em português:** disponibilidade do formato *The Brief* em pt-BR, opções de duração
   e tempo real de geração.
7. **Teste e Cartões:** nomes exatos ("Teste", "Cartões de estudo") e opções em Personalizar.
8. **Compartilhamento:** papéis Leitor/Editor e o comportamento da "visualização da conversa" em conta
   pessoal e em Workspace/Education.
9. **Requisito mínimo do iOS/iPadOS** (não encontrado na pesquisa) — citado apenas genericamente.
10. **Casos de uso:** os cenários de advogada, professor e jornalista são ilustrativos, não depoimentos
    reais (a pesquisa não encontrou casos brasileiros documentados).
11. **Materiais de referência não reproduzidos:** guias de educador do Google for Education (.xlsx) e
    guia da UFSC não têm licença de redistribuição clara; não foram usados como texto do curso.

## Próximos passos (fora desta skill)

Carregar no Articulate o `promptArticulate.md` do projeto + `roteiros/roteiro-articulate-<trilha>.md`
→ gerar o curso → verificação visual → exportar SCORM → revisar com a skill `revisar-curso-scorm`.
