# Relatório de revisão e inserção — Checagem de Fontes e Citações com IA - Essentials

Data: 05/11/2026 · Curso **presumido não publicado** (veio de `04_NAO_REVISADO/`; não confirmado) — por isso houve inserções no meio das lições.

**Pacote final para a LMS (v1):**
`01_FINALIZADO_subir-na-LMS/checagem-de-fontes/checagem-de-fontes-e-citacoes-com-ia-essentials-scorm12-Eq89phRI-FINAL-com-blocos-v1.zip`
(cópia idêntica, por hash, de `05_ARQUIVOS_DE_TRABALHO/checagem-de-fontes/essentials/checagem-essentials-blocos/saidas/…-REVISADO-v1.zip`).

Histórico em `03_VERSOES_ANTIGAS/checagem-de-fontes/`: `original-articulate/` (exportação original, não modificada) e `fase-A-so-texto/` (`…-REVISADO.zip`, só texto). O original continua também em `04_NAO_REVISADO/checagem de fontes e citacoes/`.

---

## 1. Material-fonte e mapeamento

Roteiro: `Pesquisa Conteudo Onda 2/Ementa Completa/checagem-de-fontes-e-citacoes-essentials/roteiros/roteiro-articulate-essentials.md`.
Mapeamento 1:1: lição N do Rise = Módulo N−1 do roteiro (lição 1 = Módulo 0 … lição 7 = Módulo 6 + Encerramento); lição 8 = quiz gerado pelo Articulate.

## 2. Fase A — revisão de texto (199 campos)

Método: mapas `revisao_textos/L01..L07.json` gerados por `gerar_mapas.py` e aplicados por `aplicar_mapas.py` (recusa campo não textual ou já alterado).
Por lição: L1 14 · L2 39 · L3 23 · L4 39 · L5 25 · L6 26 · L7 33 · L8 (quiz) 0. Por campo: description 72, paragraph 62, title 36, feedback 16, heading 13.

**Problemas graves corrigidos:**
- **Prompts "Mão na massa" executados pelo Articulate** em vez de exibidos. Os blocos traziam a *resposta* da IA: L2 virou uma lista de referências (Hattie, Mayer, Bandura — "DOI: não confirmado"); L4 e L5 viraram "Por favor, forneça a referência…"; L6 virou um texto em inglês sobre "structured approach". Os quatro voltaram a ser o prompt-base do roteiro, com instrução de uso. O prompt jurídico da L7 tinha sido reescrito em lista; voltou ao texto do roteiro.
- **A analogia da encomenda** (rastreio / abrir a caixa / recall), eixo do curso, não aparecia em lugar nenhum. Entrou no texto do método das três camadas (L2), nos itens das camadas e na abertura das L4, L5 e L6.
- **Erros de conteúdo:** "O Scite oferece citações inteligentes, com opções gratuitas e pagas" (a Scite é paga e opcional); "Obra retratada: … retratada ou desmentida"; Retraction Watch "útil para casos ainda não atualizados em outras bases" e PubMed "indica correções e expressões de preocupação" (afirmações sem fonte no roteiro); tab do HC 1.023.732 com "para apuração de responsabilidade" (não está no roteiro). Todos corrigidos para o que o roteiro diz.
- **Conteúdo do roteiro que faltava, reposto em campos existentes:** duas rotas equivalentes com e sem Scite e falta de convênio CAPES (L1); condições de cada estudo e alerta "citação visível ≠ atribuição correta" (L2); Enterprise da Perplexity e "nos exercícios só documentos públicos" (L3); ordem de autoridade numerada, leitura lateral, adaptação SIFT do Ceará (L4/L5); caminhos 🧭 da Perplexity (L5); cobertura da Scite (1,7 bi / 323 mi), Research Solutions, rótulos sem nome oficial em português (L6); caminho do STJ e endereço do CPP no Planalto, "segunda e última Pro Search" (L7); síntese final verbatim.
- **Pontos de controle e critérios de êxito** passaram para os itens de resumo dos *process* (L1, L5); o gabarito dos três cenários da L3 virou a última etapa ("Decida antes de avançar").
- Objetivos padronizados em "Ao final desta lição, você será capaz de:". Aberturas genéricas ("é fundamental", "Prepare-se para conhecer os riscos ocultos") trocadas por aberturas concretas; fechamentos com o próximo passo real. Accordion de bases da L4 virou "pergunta — base", como a tabela do roteiro. Listas "Se travar" no formato Situação/Causa/Procedimento. Feedbacks das questões em "Correto." / "Não." com o porquê.

Validação: `validar_estrutura.py` — **estrutura preservada nas 8 lições; 199 campos alterados = 199 entradas dos mapas.**

## 3. Fase B — inserções (12 blocos)

| Lição | Posição final | Tipo | Por quê | Fonte do conteúdo |
|---|---|---|---|---|
| 2 (M1) | 12–13 | HTML "Em qual camada está o erro?" (7 casos) + Continue que trava | Os sete erros × três camadas eram só uma lista; o objetivo 2 pede associação | Sete erros e casos do curso (pares 3, 4, 5, Tow Center, Walters e Wilder) |
| 3 (M2) | 12–13 | HTML "Semáforo de envio" (6 materiais novos) + Continue que trava | Objetivo 3 (classificar material) só tinha 3 cenários lidos | Tabela-semáforo e checklist de pré-envio do roteiro |
| 4 (M3) | 13 | Questão-cenário: ano divergente → "localizada com divergência" | A regra de divergência não era verificada | Texto do Módulo 3 |
| 5 (M4) | 7–8 | HTML "A fonte diz isso — nessas condições?" (6 afirmações sobre os estudos do M1, com o resumo da fonte ao lado) + Continue que trava | "Fora de contexto" só existia como definição | Números do Módulo 1, verbatim |
| 5 (M4) | 14 | Questão-cenário: painel Sources × abrir o original | Objetivo 4 (Perplexity como localizador, não prova) sem verificação | Texto do Módulo 4 |
| 6 (M5) | 10–11 | HTML "Qual é o estado da evidência?" (6 situações → vigente / corrigida / contestada / retratada / não verificado) + Continue que trava | Estados da ficha e cautelas sem prática | Pares 3 e 5, cautelas e "Se travar" do Módulo 5 |
| 6 (M5) | 12 | Título + parágrafo "Reference Check: por que não usar com manuscrito próprio" | Parágrafo do roteiro omitido pelo Articulate | Módulo 5, verbatim |
| 7 (M6) | 9 | Destaque 🏁 "Gabarito de referência" dos pares 1–5 e dos dossiês | Omitido pelo Articulate; sem ele a autoavaliação não fecha | Módulo 6, verbatim |

HTMLs em `…/checagem-essentials-blocos/trabalho/html/src/` (CSS/JS comuns herdados do vibecoding, cor `#152f4d` do tema; montagem por `build.py`). Roteiros em `trabalho/roteiros/`; cadeia em `trabalho/etapas/`.

## 4. Validações

| Etapa | Ferramenta | Resultado |
|---|---|---|
| Fase A | `validar_estrutura.py` | Estrutura preservada; 199 campos |
| Ponte | `verificar_scorm.py …-REVISADO.zip --original` | APROVADO, 0 erros, 0 avisos |
| Fase B | `validar.py curso_v1.json --original` | APROVADO; 12 blocos novos; 659 IDs distintos |
| Pacote final | `verificar_scorm.py …-v1.zip --original …-REVISADO.zip` | APROVADO, 0 erros, 0 avisos |

## 5. Navegador (mock de LMS da skill, servidor local)

Visto: texto revisado na abertura da L2; as 4 atividades HTML renderizam com a estética do curso, **travam o Continue** ("Complete the content above…") e **liberam** depois de todas as respostas certas; feedback de erro aparece; as questões novas, o texto do Reference Check e o gabarito do M6 aparecem após o Continue; ao voltar à lição, o Continue já estava liberado (conclusão registrada); console sem erros.

**Não verificado:** largura de celular (~400px); LMS real; abertura por duplo clique (`file://`); a lição 8 (quiz) no navegador; leitura integral de todos os blocos revisados na tela (conferidos por texto/validador, não visualmente um a um).

## 6. Pontos de atenção (revisão humana)

1. **Marcadores `[conferir]`** do roteiro foram mantidos no texto do aluno (cartão da Scite no Brasil, posição do menu da Perplexity, rótulo Academic, Check Sources no plano gratuito, treinamento no plano gratuito, controles da Scite, rótulos do STJ). O próprio curso avisa que devem ser validados antes da publicação: **validar e retirar antes de subir**.
2. **Questão da L3 (M2)**: a alternativa "Enviar apenas se remover os dados pessoais" é próxima da saída segura do roteiro (extrair só os números). O gabarito ("Não enviar") está correto, mas o feedback único da questão (`feedbackCorrect/feedbackIncorrect`) não pôde ser melhorado: esses campos não estão na lista de texto do `validar_estrutura.py`. Proposta para o feedback de erro: *"Incorreto. Remover os dados pessoais não tira a petição do sigilo profissional, e plano pago não afasta o sigilo. O documento não deve ser enviado: extraia só os números dos precedentes e confira-os na base oficial."* — aplicar no Rise ou com um validador estendido, como o `validar_texto.py` do vibecoding.
3. **Quiz (lição 8) não revisado.** Gabaritos conferidos, sem erro encontrado; o feedback da alternativa 1 da Q18 é longo e confuso.
4. **Rótulos do player em inglês** ("Complete the content above before moving on.", "START COURSE", "Lesson 2 of 8") — não alterados.
5. **Textos dos 4 HTMLs** são rascunho meu, montados só com dados do curso; vale uma leitura pedagógica.
6. Datas futuras do roteiro (decisões de 2026, anúncio de 27/07/2026) foram mantidas como estão na fonte.
