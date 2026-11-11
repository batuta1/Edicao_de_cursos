# Relatório — Deep Search com IA - Hands On (revisão de texto + inserção de blocos)

**Data:** 07/11/2026 · **Pacote final:** `Onda 2/01_FINALIZADO_subir-na-LMS/deep-research/deep-search-com-ia-hands-on-scorm12-2jNiRx6A-FINAL-com-blocos-v1.zip`
**Curso publicado com alunos?** Não (informado pelo usuário).

## 1. Material-fonte e mapeamento

Fonte: `Pesquisa Conteudo Onda 2/Ementa Completa/deep-research-hands-on/roteiros/roteiro-articulate-hands-on.md`.
O Articulate **condensou 5 oficinas em 3 lições**:
- L1 = Preparação + Oficina 1 (brief)
- L2 = Oficina 2 (rodar, dirigir o plano, guardar a trilha)
- L3 = Oficina 3 (auditoria) + Projeto Final

Ficaram de fora: **Oficina 4 inteira** (fonte oficial / LGPD / ANPD), os três dossiês do Projeto Final, os gabaritos do IBGE e do Projeto Final, o modelo do relatório auditado, a checklist final, os "Quer ir além?", o aviso de prompt injection e A Parte dos Dez. Tudo isso foi recuperado na fase B.

## 2. Revisão de texto (fase A)

Trabalho em `05_ARQUIVOS_DE_TRABALHO/deep-research/hands-on/`. **101 campos alterados** (L1 39 · L2 35 · L3 27). `validar_estrutura.py`: estrutura preservada.

- Tom "Para Leigos" do roteiro restaurado nas aberturas (o pedido do chefe, "link não é prova").
- Objetivos reescritos para o que a oficina realmente faz; fórmula padronizada.
- Processos: os passos genéricos ganharam os breadcrumbs, o brief de seis linhas **verbatim**, a linha padrão e o refinamento sem nova cota; os resumos viraram "Deu certo?" com os critérios do roteiro.
- Planilha: a aba Registro listava "Resumo" no lugar de **"Brief"**. Corrigido.
- Abas de privacidade e de ferramentas: padrão × o que fazer, exigência de 18+ no Gemini, "Create files and apps" como outro modo.
- Fechamento motivacional vazio ("Parabéns! … continue explorando") trocado pelos próximos passos do roteiro.
- **Revertido:** o feedback de acerto/erro da questão da L3 (`feedbackCorrect`/`feedbackIncorrect`) foi reescrito, mas o `validar_estrutura.py` trata esses campos como não textuais. A edição foi desfeita (o feedback original está correto). Se quiserem liberar esses campos, o ajuste é no validador da skill.

## 3. Inserções (fase B) — 30 blocos em 9 pontos

| # | Lição | Onde | Tipo | Por quê |
|---|---|---|---|---|
| H1 | L1 | após o processo do brief | Parágrafo + abas dos 3 dossiês (A Selic, B Renda, C Licitações) | o passo "escolha o dossiê" não dizia quais eram |
| H2 | L1 | após H1 | **HTML "Monte o brief do seu dossiê"** (preenche pelo dossiê, avisa o que falta, gera texto copiável) | prática do passo central da oficina |
| H4 | L1 | após "Se travar" | Título + accordion "Quer ir além? (opcional)" | 3 desafios do roteiro |
| H3 | L1 | após o semáforo | Destaques ⚠️ prompt injection e 🏁 ponto de controle da preparação | aviso e controle omitidos |
| H5 | L2 | após os flashcards | Título + accordion "Quer ir além? (opcional)" | idem |
| H6/H7 | L3 | após o 1º Continue, antes da questão | Destaque 📌 gabarito do IBGE + "Sua vez" (lista de 3 passos) | a questão usava números nunca mostrados; a parte "sua vez" sumiu |
| H6c | L3 | após a questão | Destaque ✅ "Deu certo?" com as três classificações | gabarito das três frases |
| H8 | L3 | antes do Projeto Final | **Seção "Pesquisa com fonte oficial" (Oficina 4)**: Continue, título, passos, prompt, ⚠️ Perplexity, "Sua vez", ✅ gabarito (art. 6º, arts. 6º e 9º, art. 10), "Se travar", Continue — 11 blocos | oficina inteira ausente |
| H9/H10 | L3 | após o processo do Projeto Final | Destaques 📌 gabaritos A/B/C e 📝 modelo do relatório auditado | sem gabarito e sem modelo no curso |
| H11/H12 | L3 | após o Continue final | **HTML checklist "Como saber que terminou" + Continue que trava** + título e lista "A Parte dos Dez" | fecha o projeto com critério objetivo |

**Mudanças em relação ao plano aprovado:** acrescentado o destaque ✅ "Deu certo?" depois da questão (H6c), para dar o gabarito das três frases sem entregá-lo antes da questão. H11/H12 entraram depois do Continue existente, para não deixar dois Continues seguidos. A Oficina 4 entrou como **seção dentro da L3** (opção aprovada), não como lição nova.

## 4. Validações

- Fase A: `validar_estrutura.py` sem divergência (após reverter os 2 campos acima); ponte `verificar_scorm.py`: **APROVADO**, 0 avisos.
- Fase B: `validar.py` **APROVADO** (355 IDs, todos distintos); `verificar_scorm.py` do pacote final: **APROVADO**, 0 erros, 0 avisos.

## 5. Navegador (mock de LMS da skill)

Visto: todos os blocos novos das três lições presentes no texto da página, na ordem; "Monte seu brief" renderiza, preenche o dossiê A, avisa campos faltando e formato sem "fonte e data", e gera o brief; checklist da L3 mostra o cadeado, libera com os 6 itens marcados (cliques reais) e A Parte dos Dez + fechamento aparecem; **retomada** (recarregar sem reset) volta à L3 com o Continue liberado; console sem erros.
**Não verificado:** largura de celular; botão "Copiar" na LMS real (há alternativa de seleção manual se a LMS bloquear a área de transferência); abertura por `file://`; comportamento na LMS real.

## 6. Pontos de atenção

- O fechamento da L3 ("Você pediu direito, dirigiu o plano, pegou um número misturado…") não cita a conferência de norma, porque foi revisado antes da inserção da Oficina 4. Se quiserem, é uma frase a acrescentar numa nova rodada da fase A.
- Gabaritos A/B/C do Projeto Final têm a ressalva "reconfira no dia" — os valores da Selic, do Ipea e da Lei 14.133 mudam.
- Marcadores **[conferir]** mantidos (rótulos de interface, saldo, Manage sites por plano/região).
- A Oficina 4 não tem questão de verificação própria; a conferência fica no ✅ "Deu certo?".
- Lista "A Parte dos Dez" tem 10 itens (acima do habitual de 3 a 5, mas é o formato do roteiro); o validador não reclamou.

## 7. Pacote a subir

`Onda 2/01_FINALIZADO_subir-na-LMS/deep-research/deep-search-com-ia-hands-on-scorm12-2jNiRx6A-FINAL-com-blocos-v1.zip`
