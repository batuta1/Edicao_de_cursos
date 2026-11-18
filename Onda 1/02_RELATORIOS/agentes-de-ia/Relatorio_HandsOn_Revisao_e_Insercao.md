# Relatório de revisão e inserção — Agentes de IA - Hands On

Data: 02/11/2026 · Curso **presumido não publicado** (veio de `04_NAO_REVISADO/`; não foi confirmado).

**Pacote final para a LMS (v1):**
`01_FINALIZADO_subir-na-LMS/agentes-de-ia/agentes-de-ia-hands-on-scorm12-XMoaZLjF-FINAL-com-blocos-v1.zip`
(cópia idêntica, por hash, de `05_ARQUIVOS_DE_TRABALHO/agentes-de-ia/hands-on/agentes-hands-on-blocos/saidas/…-REVISADO-v1.zip`).
Histórico em `03_VERSOES_ANTIGAS/agentes-de-ia/` (original e só-texto).

---

## 1. Material-fonte e mapeamento

Roteiro: `Pesquisa Conteudo Onda 1/Ementa Completa/agentes-de-ia-essentials/roteiros/roteiro-articulate-hands-on.md`.
O Articulate condensou 6 partes do roteiro em 3 lições:

| Lição no Rise | Roteiro |
|---|---|
| 1 Preparando o Terreno | Antes de Arregaçar as Mangas + Mapa da Mão na Massa |
| 2 Delegando e Monitorando | Oficina 1 + Oficina 2 (separadas por um Continue) |
| 3 Revisão, Riscos e Práticas Seguras | Oficina 3 + Oficina 4 + Parte dos Dez + Projeto Final + "Conseguiu! E agora?" |

## 2. Fase A — revisão de texto (200 campos)

Por lição: L1 48 · L2 65 · L3 87. Por campo: description 90, title 53, paragraph 40, heading 17.

**Correções de conteúdo (as mais importantes):**
- **Prompts ausentes:** a ordem de serviço da Oficina 1, a mensagem de mudança de escopo da Oficina 2, o pedido de correção da Oficina 3, o texto do arquivo-isca e o pedido da Oficina 4 **não existiam** no curso — os passos diziam "cole a ordem de serviço" sem trazê-la. Todos restaurados verbatim dentro dos passos dos blocos Process.
- **Kit de documentos sem links:** a lista dos três documentos não tinha nenhum link. Links do roteiro incluídos.
- **Aviso do ChatGPT invertido:** "Este é um tutorial antigo que menciona…" → texto do roteiro (tutorial antigo falando em modo agente? o recurso foi aposentado).
- **"Agente de IA multitarefa":** termo inventado, trocado por "agente de IA".
- **Accordion "Outros problemas frequentes"** (texto vazio) virou "Os créditos do Manus acabaram", com a nota de créditos do roteiro (300/dia, 1.000 iniciais, dica de dividir as oficinas em dois dias).
- Pontos de controle 🏁, aviso de senha ⚠️, dica do "L" 💡, curiosidade 🤓, alerta de dado real ⚠️, perfis do Projeto Final (CGU/OAB e o que pedir) e o checklist "Como saber que terminou" levados para os blocos existentes; Mapa das oficinas com tempos no fechamento da lição 1; aberturas de oficina com o texto "🎯 O Problema" do roteiro; fechamento "Conseguiu! E agora?" com os cursos seguintes.
- Os dez hábitos (abas) ganharam a frase verbatim do roteiro em cada aba.
- Questão da lição 3: a alternativa correta (mesma posição) passou a dizer "pedir a correção da linha errada **e** conferir todas as restantes". Gabaritos intactos.

`validar_estrutura.py`: ESTRUTURA OK nas 3 lições; 200 campos = 200 entradas dos mapas.

## 3. Fase B — inserções (10 blocos)

| Lição | Posição final | Tipo | Por quê |
|---|---|---|---|
| 2 | 8–9 | Título + accordion "Quer ir além? Oficina 1 (opcional)" (3 desafios com validação) | Os desafios do roteiro não existiam no curso |
| 2 | 19–20 | Idem, Oficina 2 | idem |
| 3 | 9–10 | Idem, Oficina 3 | idem |
| 3 | 16–17 | Idem, Oficina 4 | idem |
| 3 | 21–22 | HTML "🏁 Como saber que terminou" (8 itens do Projeto Final) + Continue travado (`completeBlock`) | O checklist marcável do roteiro; o restante da lição só abre depois dele |

Fonte do HTML: `…/agentes-hands-on-blocos/trabalho/html/src/l3-projeto.body.html`. Edições pós-inserção (`pos_edicoes.py`): capa reescrita a partir do subtítulo do roteiro e `completeHint` dos 3 Continues em português.

## 4. Validações

| Etapa | Ferramenta | Resultado |
|---|---|---|
| Original | `verificar_scorm.py` | APROVADO, 0 erros, 0 avisos |
| Fase A | `validar_estrutura.py` | ESTRUTURA OK, 200 campos |
| Fase B | `validar.py` | APROVADO: só inserção, 10 blocos, 291 IDs únicos |
| Pós-edições | `pos_edicoes.py` | APROVADO: 4 folhas (capa + 3 completeHint) |
| Pacote v1 | `verificar_scorm.py --original` | APROVADO, 0 erros, 0 avisos; só `runtime-data.js` alterado |

## 5. Teste no navegador (mock de LMS)

**Visto:** lição 3 carrega; os blocos novos estão nas posições 9, 16 e 21–22 (pelos IDs); o Continue novo aparece travado com "Conclua o conteúdo acima para continuar." e o resto da lição não carrega; o texto do arquivo-isca e o Desafio do STJ estão na página. HTML sozinho: os 8 itens marcados liberam e enviam `{type:'complete'}`; sem rolagem horizontal a 375 px. Console sem erros.

**Não verificado:** o HTML dentro do player e a liberação real do Continue (painel do navegador oculto); lição 2 na tela; retomada; `file://`; LMS real; interface real das ferramentas (exige conta).

## 6. Pontos de atenção

1. Rótulos `[conferir]` do roteiro (cadastro do Manus, seletores, botão de anexo, painel do computador do agente, aceitação de `.txt` pelo Manus) não foram validados numa conta.
2. Link da CGU responde HTML, não PDF — confirme no navegador.
3. O roteiro manda a Oficina 3 sortear mais três linhas se a primeira amostra conferir; isso está no passo 3 do Process.
4. O checklist do Projeto Final é autodeclarativo.
