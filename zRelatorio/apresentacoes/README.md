# Apresentações

Roteiros e slides das apresentações do projeto. Cada apresentação tem um **roteiro** (Markdown) e os **slides** (LaTeX Beamer) feitos a partir dele.

## Apresentações

| Apresentação | Roteiro | Slides | PDF |
|---|---|---|---|
| Da planilha ao Notion (registro de atividade) | [roteiro-automacao-notion.md](roteiro-automacao-notion.md) | [automacao-notion.tex](automacao-notion.tex) | `out/automacao-notion.pdf` (ainda não gerado) |

Base: [registro de atividade](../registros/2026-11-automacao-notion-e-extrator.md). A fala de cada slide está nas **notas do apresentador** (`\note`) do `.tex`; ela não aparece na tela.

## Compilar

> Estes arquivos **ainda não foram compilados nem conferidos visualmente**. A primeira compilação pode mostrar ajustes de espaçamento.

Precisa do `xelatex` (MiKTeX ou TeX Live). Rode **da raiz do repositório** (os caminhos de fontes e imagens são relativos a ela), **duas vezes** (a numeração dos slides sai na segunda):

```bash
xelatex -output-directory="zRelatorio/apresentacoes/out" -interaction=nonstopmode -halt-on-error "zRelatorio/apresentacoes/automacao-notion.tex"
```

O PDF fica em `out/`. Os arquivos auxiliares (`.aux`, `.log`...) também ficam lá e o git os ignora.

Para ver as notas do apresentador junto com os slides, acrescente `\setbeameroption{show notes}` antes de `\begin{document}`.

## Arquivos

| Caminho | O que é |
|---|---|
| `roteiro-*.md` | Narrativa: para cada slide, o **Roteiro** (o que se fala) e a **Descrição do slide** (o que se vê) |
| `*.tex` | Slides (Beamer 16:9, malha de 160 × 90 mm, Manual de Marca do IAclube) |
| `fonts/` | `Ubuntu-Bold.ttf` e `Montserrat-Regular.ttf` (fontes da marca) com as licenças `UFL-Ubuntu.txt` e `OFL-Montserrat.txt` |
| `images/` | `provisoria.png` (logo da capa) e `provisoria-simbolo.png` (símbolo no canto dos slides): **logo provisória** |
| `out/` | Saída da compilação |

## Observações

- A logo é a **provisória**: o Manual de Marca não traz os arquivos oficiais. Troque os dois PNGs quando houver a versão final (mesmos nomes de arquivo).
- Se uma fonte ou imagem faltar, o `.tex` segue com a Liberation Sans (no lugar de Ubuntu e Montserrat) e sem logo. Isso aparece no PDF, não é avisado na compilação.
- Referência de marca: `Manual de Marca.pdf` e `manual-de-marca.md`, no repositório `scorm_data_extractor`, pasta `zApresentacao/`.
- Os modelos de macros (malha, cartões, painéis) vêm de `zApresentacao/projeto-organizacao.tex`, do mesmo repositório.
