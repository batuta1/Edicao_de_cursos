# Relatório de revisão, tradução e inserção — Vibe Coding - Hands On

Data: 04/11/2026 · Curso **presumido não publicado** (veio de `04_NAO_REVISADO/`; não confirmado) — por isso houve inserções no meio das lições.

**Pacote final para a LMS (v1):**
`01_FINALIZADO_subir-na-LMS/vibecoding/vibe-coding-hands-on-scorm12-8IfQh11n-FINAL-com-blocos-v1.zip`
(cópia idêntica, por hash, de `05_ARQUIVOS_DE_TRABALHO/vibecoding/hands-on/vibe-hands-on-blocos/saidas/…-REVISADO-v1.zip`).

Histórico em `03_VERSOES_ANTIGAS/vibecoding/`: `original-articulate/` e `fase-A-so-texto/`. O original continua também em `04_NAO_REVISADO/vibecoding/`.

---

## 1. Situação de partida

Curso **misto**: estrutura, títulos, passos e questões em inglês; alguns destaques, os prompts e a ficha em português — e vários accordions com a primeira frase em português e a segunda em inglês. Foi **traduzido integralmente** e revisado contra o roteiro.

## 2. Material-fonte e mapeamento

Roteiro: `Pesquisa Conteudo Onda 1/Ementa Completa/vibe-coding-essentials/roteiros/roteiro-articulate-hands-on.md`.
O curso tem 3 lições para 7 partes do roteiro: lição 1 = "Antes de Arregaçar as Mangas" + a planta (início da Oficina 1); lição 2 = Oficinas 1 (construção), 2 e 3; lição 3 = Oficina 4 + Projeto Final + "A Parte dos Dez" + "Conseguiu! E agora?". Os títulos das lições foram reescritos para refletir isso.

## 3. Fase A — tradução e revisão de texto (298 campos)

Mesmo método do Essentials (mapas `revisao_textos/L01..L03.json`, `aplicar_mapas.py`, `validar_texto.py`).
Por lição: L1 70 · L2 126 · L3 102. Por campo: title 110, description 99, paragraph 52, heading 19, feedback 16, feedbackCorrect 1, feedbackIncorrect 1.

**Correções de conteúdo (além da tradução):**
- **Tom do roteiro** (curso "para leigos", direto, em segunda pessoa) restaurado: "O Problema", "Deu certo?", "Se travar", "Regra de ouro" — a versão do Articulate tinha trocado por inglês formal genérico.
- **Pontos de controle 🏁** de cada oficina, que faltavam, entraram nos itens "resumo" dos *process* ("Deu certo?").
- **Curiosidades técnicas** do roteiro (modos Chat/Plan/Build com o nome antigo "Agent"; Lovable Cloud sobre Supabase, sem conta própria e sem troca de um clique) entraram nos flashcards.
- **Accordions bilíngues** (frase em português + explicação em inglês) reescritos em português, mantendo a frase do roteiro.
- **"A Parte dos Dez":** títulos numerados de 1 a 10; a explicação em inglês que repetia a frase foi retirada (cada hábito ficou com a frase do roteiro).
- O passo "Review the Security Scan… return to the previous workshop" agora diz "volte à Oficina 3", como no roteiro; o perfil "Professor" mantém "suas leituras, não as dos alunos".
- Questões de verificação reescritas como cenário curto, com feedback "Correto./Não." explicando o porquê.

`validar_texto.py`: ESTRUTURA OK nas 3 lições; 298 campos = 298 entradas dos mapas.

## 4. Fase B — inserções (12 blocos)

| Lição | Posição final | Tipo | Por quê |
|---|---|---|---|
| 1 | 3–5 | Título + parágrafo, lista numerada, parágrafo: "O mapa da mão na massa" (4 oficinas + Projeto Final, problema e tempo de cada uma; 115 min) | O mapa do roteiro não estava no curso |
| 2 | 8–9 | Título + accordion "🚀 Quer ir além? Oficina 1 (opcional)" — 3 desafios com validação | Os desafios opcionais do roteiro não estavam no curso |
| 2 | 19–20 | Idem, Oficina 2 | Idem |
| 2 | 28–29 | Idem, Oficina 3 | Idem |
| 3 | 11–12 | Idem, Oficina 4 | Idem |
| 3 | 18 | HTML "Ficha de requisitos e pedido em Plan" (exemplos dos dois perfis; confere a ficha e gera o pedido em Plan do Projeto Final) | O passo 1–2 do Projeto Final vira ferramenta |

Nenhum HTML trava Continue. O HTML é a mesma ferramenta da lição 4 do Essentials, com o bloco do pedido em Plan ligado (`data-plano="sim"`); a fonte está em `vibecoding/essentials/vibe-essentials-blocos/trabalho/html/src/ho-ficha.body.html` e o HTML montado em `…/vibe-hands-on-blocos/trabalho/html/`.

Fase C (`pos_edicoes.py`): descrição da capa traduzida (a partir do subtítulo do roteiro) e `completeHint` dos 4 Continues → "Conclua o conteúdo acima para continuar.".

## 5. Validações

| Etapa | Ferramenta | Resultado |
|---|---|---|
| Fase A | `validar_texto.py` | ESTRUTURA OK, 298 campos |
| Fase A, pacote | `scorm_reempacotar.py` | round-trip OK; só `runtime-data.js` alterado |
| Original da Fase B | `verificar_scorm.py` | APROVADO, 0 erros, 0 avisos |
| Fase B | `validar.py` | APROVADO: só inserção, 12 blocos seguindo os modelos, 353 IDs únicos |
| Fase C | `pos_edicoes.py` | APROVADO: 5 folhas (capa + 4 completeHint) |
| Pacote v1 | `verificar_scorm.py --original` (contra o original do Articulate) | APROVADO, 0 erros, 0 avisos; só `runtime-data.js` alterado |

## 6. Teste no navegador (mock de LMS da skill)

**Visto:** o pacote carrega; lição 1 mostra "O mapa da mão na massa" depois dos objetivos; na lição 3, depois dos Continues, aparecem o "Quer ir além? Oficina 4" e a ferramenta da ficha, entre o aviso ⚠️ e o *process* do Projeto Final, com altura ajustada. A ferramenta, aberta sozinha, gera a ficha e o pedido em Plan com os exemplos. Console sem erros.

**Não verificado:** os três "Quer ir além?" da lição 2 vistos na tela (estão no JSON e passaram no `validar.py`); retomada sem `reset`; LMS real; **interface real do Lovable**.

## 7. Pontos de atenção para revisão humana

1. **Rótulos do player em inglês** ("START COURSE", "Lesson 1 of 3", "Continue") — mesmo caso do Essentials (`labelSet` padrão da equipe).
2. **Rótulos `[conferir]` do roteiro** não validados, incluindo os dos desafios opcionais: `Project settings > Knowledge` e a conexão com o GitHub.
3. O desafio da Oficina 4 mantém em inglês o prompt "Review my app's security. Check the authentication flow.", como no roteiro (exemplo da biblioteca oficial).
4. Listas de objetivos têm 4–5 itens escritos a partir das oficinas (o roteiro do Hands On não tem objetivos formais por oficina).
5. Gabaritos: nenhum foi mudado.
