# Relatório — Gemini Chat - Hands On (revisão de texto + inserção de blocos)

**Data:** 17/11/2026 (v1) · **Pacote final:** `Onda 2/01_FINALIZADO_subir-na-LMS/gemini-chat/gemini-chat-hands-on-scorm12-YkqQ0MtD-FINAL-com-blocos-v1.zip`

## 1. Material-fonte e mapeamento

Fonte: `Pesquisa Conteudo Onda 2/Ementa Completa/gemini-chat-essentials/roteiros/roteiro-articulate-hands-on.md`.
O Articulate **condensou 4 oficinas + Projeto Final em 3 lições**:
- L1 = Oficina 1 (habilidade do mutirão)
- L2 = Oficina 2 (planilha de inscrições)
- L3 = Oficina 3 (Gmail e Agenda) + Oficina 4 (Canvas) + Projeto Final

Ficaram de fora: **a preparação inteira** — inclusive o arquivo `inscricoes-mutirao.csv` e o e-mail de teste, sem os quais as Oficinas 2 e 3 não podem ser feitas —, a conferência do Histórico, o mapa das oficinas, a regra de ouro e A Parte dos Dez. Tudo recuperado na fase B.

## 2. Revisão de texto (fase A)

Trabalho em `05_ARQUIVOS_DE_TRABALHO/gemini-chat/hands-on/`. **170 campos alterados** (L1 43 · L2 46 · L3 81). Validação com `validar_texto.py`: estrutura preservada, 170 = 170.

**Erros de conteúdo corrigidos**
- **L2 — gabarito errado:** a questão sobre Previdência à tarde marcava **5** como correta, e o feedback repetia "5". O correto é **7** (I03, I09, I14, I19, I22, I28, I30 — conferido no CSV e na dica do próprio curso). Correção sem tocar na estrutura: a alternativa marcada como correta passou a dizer "7", e a que dizia "7" passou a "8" (total de Previdência nos dois turnos, um distrator plausível); feedbacks reescritos.
- **L1 — instruções da habilidade:** o bloco que devia trazer as instruções a colar trazia uma resposta inventada, com dados fictícios fora do caso ("I01: inscrição recebida por e-mail em 10/06…"). Voltaram as instruções verbatim.
- **L2:** o caminho de envio do CSV estava sem o "+".
- **L3:** as três partes (Oficina 3, Oficina 4, Projeto Final) agora têm títulos próprios; o ponto de controle completo da Oficina 3 (as três datas) entrou na alternativa correta da questão; a alternativa "o Gemini envia e-mails automaticamente" virou o cenário contrário, coerente com o desafio "o Gemini não envia nada sem você".

**Demais melhorias**
- Aberturas genéricas ("automatizar processos não só economiza tempo…") trocadas pelo "🎯 O problema" de cada oficina; seções com os rótulos do roteiro (🧰 O que você vai usar, 👐 Mão na massa, ✅ Deu certo?, 🚑 Se travar, 🚀 Quer ir além?).
- Objetivos padronizados e alinhados ao que cada oficina faz.
- Gabarito da Oficina 2 com a explicação de cada número (soma 30, tarde 60%, canal → comunicado).
- "Conseguiu! E agora?" verbatim no lugar do "Parabéns! … será ainda mais fácil!".

## 3. Inserções (fase B) — 14 blocos em 6 pontos

| # | Lição | Onde | Tipo | Por quê |
|---|---|---|---|---|
| h06 | L1 | início | Título "Antes de arregaçar as mangas" · título + **lista "O mapa da mão na massa"** · destaque 🔑 regra de ouro · **HTML "Kit do mutirão"** (CSV com botão copiar, assunto e corpo do e-mail de teste, checklist de 4 itens) + **Continue que trava** | sem o CSV e o e-mail o curso não podia ser feito; a conferência do Histórico é pré-requisito da Oficina 3 |
| h05 | L2 | após o gabarito | **HTML "Quantas mesas?"** (contagens tema × turno do CSV; muda os horários por mesa e recalcula; botão do desafio "tarde com 4 horários") | a decisão de mesas era só um número; agora o participante vê a conta e valida o desafio 3 |
| h04 | L3 | antes da questão da Oficina 3 | **HTML "Pedido delimitado ou amplo demais?"** (6 pedidos ao Gmail) | o ⚠️ "cite o assunto exato" virou prática |
| h03 | L3 | antes da Oficina 4 | Continue | separa a Oficina 4 como etapa própria |
| h02 | L3 | antes do Projeto Final | Continue | separa o Projeto Final |
| h01 | L3 | após "Como saber que terminou" | **HTML checklist final + Continue que trava** · título + **lista "A Parte dos Dez"** | fecha o projeto com critério objetivo; Parte dos Dez ausente |

## 4. Validações

- Fase A: `validar_texto.py` sem divergência (170 campos); reempacotamento com round-trip e 0 arquivos alterados fora do alvo; ponte `verificar_scorm.py`: **APROVADO**, 0 erros, 0 avisos.
- Fase B: `validar.py` **APROVADO** (14 blocos novos; 304 IDs, todos distintos); `verificar_scorm.py` do pacote final contra o revisado: **APROVADO**, 0 erros, 0 avisos. Nenhum "[conferir]" no curso final.

## 5. Navegador (mock de LMS da skill)

Visto: as três lições com os blocos novos na ordem certa; o Kit do mutirão mostra o cadeado ("Complete the content above…") e libera o Continue com os 4 itens marcados; botão copiar com alternativa (seleciona o texto quando a área de transferência é bloqueada); a calculadora mostra 9 mesas no caso e "Previdência à tarde" com 2 mesas no desafio; a questão corrigida aceita "7" como "Correct" com o feedback novo; o classificador do Gmail completa 6/6; o checklist final trava e libera, e A Parte dos Dez + "Conseguiu!" aparecem; **retomada** (recarregar sem reset) volta à lição salva; console sem erros; os quatro HTMLs a 360 px sem rolagem horizontal.
**Não testado:** LMS real; abertura por `file://`; o fluxo real no Gemini (habilidade, Gmail, Agenda, Canvas), que depende de conta.

## 6. Decisões tomadas

- **[conferir] do roteiro resolvidos:** habilidades em Personalizar > Habilidades (ajuda do Google, 17/11/2026); apps em "Personalizar > Apps conectados" e exportação pelo menu Compartilhar do Canvas, escritos pela função — o "Se travar" já orienta procurar no menu de compartilhar.
- O CSV e o e-mail de teste estão no HTML exatamente como no roteiro (o CSV foi recontado: 9/8/7/6, 12/18, 11/10/9, I03/I06/I07/I30 — bate com o gabarito).
- O Kit do mutirão inclui o aviso do roteiro sobre usar conta secundária se o Gmail recebe e-mails de clientes.
