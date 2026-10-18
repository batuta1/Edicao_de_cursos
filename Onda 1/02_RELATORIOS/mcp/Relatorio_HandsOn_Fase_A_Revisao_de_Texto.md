# Relatório — Fase A (revisão de texto) — MCP Hands-on

Data: 18/10/2026 · Skill: `revisar-curso-scorm` · Regras: `promptRevisaoPorClaude.md` + `promptRevisaoComInsercaoDeBlocos.md`

## 1. Material

| Item | Caminho |
|---|---|
| Pacote original (não modificado) | `Onda 1/04_NAO_REVISADO/mcp/model-context-protocol-mcp-hands-on-scorm12-lBHsLBqU.zip` |
| Título conferido na extração | `Model Context Protocol (MCP) - Hands On` (course.id `9pUgk_ePl9Hcs6jPzZ36jjE2dZc5U0SO`) |
| Roteiro-fonte | `Pesquisa Conteudo Onda 1/Ementa Completa/mcp-essentials/roteiros/roteiro-articulate-hands-on.md` |
| Pasta de trabalho | `Onda 1/05_ARQUIVOS_DE_TRABALHO/mcp/hands-on/` |
| Mapas de substituição (texto novo por caminho do campo) | `…/hands-on/revisao_textos/L01.json` a `L03.json`, aplicados por `…/hands-on/aplicar_mapas.py` |
| Pacote revisado | `Onda 1/03_VERSOES_ANTIGAS/mcp/fase-A-so-texto/model-context-protocol-mcp-hands-on-scorm12-lBHsLBqU-REVISADO.zip` (cópia em `…/hands-on/mcp-hands-on-blocos/original/`) |

### Mapeamento lição ↔ oficina (o Articulate condensou 8 partes do roteiro em 3 lições)

| Lição (arquivo) | position | Partes do roteiro |
|---|---|---|
| licao_01 (20 blocos) | 0 | Antes de Arregaçar as Mangas + Oficina 1 — Ligue seu primeiro conector |
| licao_02 (23 blocos) | 1 | Oficina 2 — Pasta (blocos 3–9) · Oficina 3 — Agenda (11–15) · Oficina 4 — Crie, confira e apague (17–21) |
| licao_03 (14 blocos) | 2 | Projeto Final (0–8) + A Parte dos Dez (10–11) + Conseguiu! E agora? (12–13) |

## 2. Diagnóstico do que veio do Articulate

- **Idioma:** desta vez o curso veio em PT-BR. Os rótulos de navegação do Rise (`labelSet`) estão em inglês (`iso639Code` `en`), como vinha no Essentials antes da v3.
- **Conteúdo omitido que quebrava a prática (restaurado em campos existentes):**
  - **O conteúdo dos dois arquivos de teste não aparecia em lugar nenhum** — o passo só dizia "adicione os arquivos de teste conforme instruções futuras". Sem ele a oficina da pasta (e a pegadinha de prompt injection) não acontece. Restaurado verbatim, com as aspas triplas e a última linha de `politica-ficticia.txt`, no passo "A pasta com os arquivos de teste" (Lição 1).
  - Oficina 4: faltava o passo de `Gmail > Tool permissions` (enviar/responder/encaminhar em Needs approval ou Blocked) e a conferência "criar rascunho, não enviar". Restaurados no passo da Parte B.
  - Os 🏁 pontos de controle de cada oficina não apareciam; foram para o item de resumo de cada Process (que tinha texto genérico, inclusive "Parabéns! Seu plano de integração está pronto").
  - O modelo do plano (Lição 3) estava num parágrafo corrido só; agora uma linha por campo, entre aspas triplas.
  - Os 📌 "Não esqueça" das Oficinas 2 e 3 (desligar a Filesystem; manter o Calendar para a Oficina 4) foram para o resumo dos respectivos Process.
- **Emojis e textos verbatim do roteiro perdidos nos destaques:** 🤓 curiosidade, 🔑 regra de ouro, ⚠️ cuidado (×3), 💡 dica, 📌 não esqueça — restaurados com o texto do roteiro.
- **Textos genéricos:** aberturas ("Integrar assistentes de IA… pode trazer praticidade e agilidade"), fechamentos ("Parabéns por concluir este curso — sua prática segura começa agora!") e introduções de flashcard trocados pelo texto do roteiro.
- **Objetivos:** padronizados em "Ao final desta lição, você será capaz de:" e alinhados às oficinas de cada lição.
- **Não restaurável na fase A (vai para o plano de inserções):** mapa das oficinas com tempos, variação no ChatGPT da Oficina 1, caminho sem Desktop (Google Drive) da Oficina 2, os 12 desafios "🚀 Quer ir além?" e o checklist marcável do Projeto Final.

## 3. Alterações (resumo por lição)

| Lição | Campos | O que mudou |
|---|---|---|
| 1 | 80 | Abertura verbatim; objetivos; flashcards (MCP, conector, plugin/app, permissão, ficha do conector); Process de preparação com os arquivos de teste completos; regra de ouro; semáforo com a frase de anúncio; Process do treino com ponto de controle "amarelo, amarelo, vermelho" e o porquê; Process da Oficina 1 com problema, URL e ponto de controle; questão da Oficina 1 reescrita (feedback "Correto."/"Não." + porquê); "Se travar" com títulos do roteiro; fechamento que anuncia a Lição 2 |
| 2 | 111 | Abertura das três oficinas; objetivos; flashcards; Process da Oficina 2 (Filesystem, pegadinha, Deny, conferência da pasta); Process da Oficina 3 (Tool permissions, consulta verbatim); Process da Oficina 4 (Partes A, B e C, com Gmail Tool permissions e revogação na Conta Google); três "Se travar"; três questões reescritas; fechamento |
| 3 | 54 | Missão verbatim; objetivos; flashcards dos critérios (com o semáforo completo); Process do plano com o modelo linha a linha e a faxina final; questão do dado de cliente; flashcards da Parte dos Dez com a frente em negrito (verbatim do roteiro); "Conseguiu! E agora?" verbatim |
| **Total** | **245** | por campo: description 89, feedback 18, heading 12, paragraph 40, title 86 |

Nenhum gabarito foi alterado. Nenhuma alternativa mudou de posição.

## 4. Validações

- `aplicar_mapas.py`: confere que cada caminho é campo de texto, que o valor atual ainda é o original e que o texto novo é diferente; 3 entradas iguais ao original foram retiradas dos mapas antes de aplicar. 245 aplicados.
- `validar_estrutura.py`: **estrutura preservada nas 3 lições**; 245 campos de texto alterados — igual ao número aplicado.
- `scorm_reempacotar.py`: round-trip do Base64 OK; 84 arquivos; só `scormcontent/runtime-data.js` mudou.
- Ponte `verificar_scorm.py …-REVISADO.zip --original <Articulate>`: **APROVADO**, 0 erros, 0 avisos.
- Navegador: não testado ainda nesta fase (fica para a fase B, junto com os blocos novos).

## 5. Pontos de atenção (decisão humana)

1. **Gabarito errado — Lição 1, questão do semáforo (bloco 10).** A correta marcada é "A. Verde para leitura, vermelho para criar na agenda do chefe". O roteiro dá **amarelo** para "ver meus eventos" (conta pessoal) — é o próprio ponto de controle do treino, que agora aparece logo acima da questão. Nenhuma alternativa diz "amarelo e vermelho". A questão **não foi alterada** (nem texto). Proposta: reescrever a alternativa A para "Amarelo para ler; vermelho para criar na agenda do chefe" e ajustar os quatro feedbacks — o campo `correct` não muda, mas o sentido da correta muda, por isso pede autorização.
2. **Rótulos de navegação em inglês** (`labelSet`, `iso639Code` `en`): no Essentials foram traduzidos na v3 (174 rótulos, `pt-BR`). Dá para reaproveitar a mesma tradução aqui; exige autorização (é fora das lições).
3. **[conferir] do roteiro mantidos:** macOS 13, `Add custom connector`, rótulos em português de Settings > Extensions, tela de escolha da pasta, rótulo para desativar a Filesystem, caminho de revogação na Conta Google.
4. **Referências a oficinas:** como as oficinas não viraram lições, os textos falam em "Lição 2", "próxima oficina" e "projeto final, na Lição 3" no lugar de "Oficina 2" etc.

## Atualização — v2 (18/10/2026)

Com autorização do usuário: ponto 1 (gabarito da Lição 1) corrigido reescrevendo a alternativa A e os 4 feedbacks, sem mexer no campo `correct`; ponto 2 (rótulos) resolvido com o `labelSet` do Essentials v3 e `iso639Code` `pt-BR` (`criar_base_v2.py` → `cursoMCPHandsOn_base_v2.json`). 254 campos, estrutura preservada; pacote `…-REVISADO-v2.zip` APROVADO na ponte. A v1 das lições ficou em `03_VERSOES_ANTIGAS/mcp/fase-A-so-texto/licoes_extraidas_MCPHandsOn_v1/`. Detalhes em `Relatorio_HandsOn_Revisao_e_Insercao.md`.
