# 00 — Contornos do curso NotebookLM - Essentials

Documento de partida compartilhado pelas duas trilhas. Tudo o que vem depois (v1.0, auditoria,
roteiros, carga horária, ementa) se apoia nestes campos.

## Origem do pedido

| Campo | Valor |
|---|---|
| Registro no catálogo | `novos-cursos-iaclube-priorizacao-v6.json` → `"id": "notebooklm-essentials"` |
| Nome no catálogo | NotebookLM - Essentials |
| Onda / ranking / score | Onda 1 · ranking 1 · 98 pontos (demanda 30, ferramenta 20, base 18, lacuna 20, esforço 10) |
| Tema / linha prioritária | Pesquisa com IA |
| Competência | Pesquisa e estudo sobre fontes próprias |
| Tarefa observável | Montar um caderno com fontes, gerar resumo, guia de estudo e Audio Overview e responder perguntas com citações. |
| Base confiável | Central de ajuda e guias oficiais do Google |
| Observação do catálogo | Nenhum curso atual cobre pesquisa; aderência forte ao público educacional. |

## Objeto base

**NotebookLM** — o caderno de pesquisa com IA do Google, renomeado **Gemini Notebook** em
16/07/2026. O curso mantém o nome do catálogo ("NotebookLM") e explica a mudança de marca já no
primeiro módulo. A navegação é ancorada no endereço `notebook.google.com`, que não depende da marca.

## Público-alvo

Três públicos, vindos das trilhas em que o curso está posicionado:

| Trilha | Posição | Público |
|---|---|---|
| T2 — Pesquisa com IA | 2 de 5 (antes: Perplexity - Essentials; depois: Deep Research - Hands On) | Estudantes, pesquisadores, jornalistas e analistas |
| T12 — IA para educadores | 1 de 6 (primeiro curso; depois: Educação com IA: Planejamento e Avaliação - Essentials) | Professores, coordenadores pedagógicos e designers instrucionais |
| J2 — Pesquisa e fundamentação jurídica | 2 de 5 (antes: Perplexity - Essentials; depois: Pesquisa jurídica com IA - Hands On) | Advogados, assessores jurídicos, estudantes e professores de Direito |

Consequência de design: o exercício-âncora precisa servir aos três públicos ao mesmo tempo (tema
LGPD, fontes oficiais públicas), e a atividade integradora final deixa o aluno escolher o recorte do
seu perfil.

## Pré-requisitos

- Uso básico de um assistente de IA (ChatGPT, Claude ou Gemini).
- Uma Conta Google (pessoal, de trabalho ou escolar). Conta Workspace/Education depende de o
  administrador ter habilitado o serviço.
- Nenhum conhecimento técnico.

## Recursos necessários

- Computador com navegador atualizado e internet. O fluxo principal é o **web**; o aplicativo
  móvel (Android 10+ e iOS/iPadOS) não tem paridade de recursos e fica como complemento.
- Plano **gratuito (Standard)** basta para todo o curso: 100 notebooks, 50 fontes por notebook,
  50 chats/dia, 3 Resumos em Áudio/dia, 10 relatórios/dia, 10 conjuntos de cartões, 10 testes e
  10 mapas mentais/dia (ajuda oficial consultada em 17/10/2026).
- Quatro fontes públicas sobre LGPD (dois PDFs da ANPD baixados e duas páginas HTML oficiais).

## Configuração

| Campo | Valor |
|---|---|
| Autoinstrucional | **Sim.** Nenhum passo pode depender de professor. |
| Trilhas | Essentials (compreensão) e Hands-on (execução), ambas a partir deste objeto base. |
| Carga horária alvo — Essentials | 100–130 min (prompt-mestre `articulate-essentials.md`) |
| Carga horária alvo — Hands-on | 90–120 min (prompt-mestre `articulate-hands-on.md`) |
| Módulos/oficinas | Essentials: 4–6 módulos de conteúdo + síntese. Hands-on: 4 oficinas + Projeto Final. |
| Idioma | Português do Brasil; nomes de recurso que só existem em inglês ficam em inglês. |
| Plano exigido | Gratuito. Recursos pagos ou 18+ (Video Overview Cinematic, cotas ampliadas) só são citados. |

## Fora do escopo (outro curso cobre)

- Pesquisa profunda automatizada na web (Deep Research) → *Deep Research - Hands On*.
- Verificação sistemática de citações acadêmicas → *Checagem de Fontes e Citações - Essentials*.
- Bases de conhecimento comparando ferramentas (Projetos do Claude e do ChatGPT) →
  *RAG e Bases de Conhecimento - Essentials*.

Esses temas aparecem apenas para delimitar a fronteira (uma frase, nunca um passo a passo).

## Material-fonte

Pasta `Pesquisa Conteudo Onda 1/conteudo-bruto/notebooklm-essentials/`:

| Arquivo | Uso no curso |
|---|---|
| `ConteudoBruto_notebooklm-essentials.txt` | Fonte principal: fatos marcados [CONFIRMADO]/[VERIFICAR], com 47 referências datadas de 17/10/2026. |
| `anpd-guia-seguranca-informacao-pequeno-porte.pdf` | Fonte 2 do exercício-âncora; base do módulo de segurança. |
| `anpd-guia-dados-pessoais-pesquisa-academica.pdf` | Fonte 3 do exercício-âncora; base da discussão de minimização e anonimização. |
| `guia-ia-aplicada-profissoes.pdf` (LabTeC/UFSC) | Referência de exemplos profissionais; não reproduzido. |
| `guia-educador-notebooklm-*.xlsx` (Google for Education) | Referência de sequência para educadores; licença de redistribuição não encontrada, não reproduzido. |

Regra para dado factual: o que no conteúdo bruto está [CONFIRMADO] entra no curso com a data de
consulta; o que está [VERIFICAR] ou NÃO ENCONTRADO entra no máximo como formulação genérica e vai
para as pendências do `README.md`.

## Alertas herdados do conteúdo bruto

1. "Com base nas fontes" reduz, mas não elimina, respostas erradas: abrir a citação é parte do fluxo.
2. Conta pessoal: conteúdo pode ser revisado por humanos **se o usuário enviar feedback**;
   documentos pessoais, sigilosos ou protegidos por segredo profissional não entram sem base legal
   e ambiente adequado.
3. Limites, preços e menus mudaram várias vezes em 2026; revisão humana obrigatória na semana de
   publicação. Marca em transição (NotebookLM × Gemini Notebook) e rótulos pt-BR traduzidos de
   forma irregular.
