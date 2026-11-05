# Relatório de revisão e inserção — Agentes de IA - Essentials

Data: 02/11/2026 · Curso **presumido não publicado** (veio de `04_NAO_REVISADO/`; não foi confirmado) — por isso houve inserções no meio das lições.

**Pacote final para a LMS (v1):**
`01_FINALIZADO_subir-na-LMS/agentes-de-ia/agentes-de-ia-essentials-scorm12-1Jlrz425-FINAL-com-blocos-v1.zip`
(cópia idêntica, por hash, de `05_ARQUIVOS_DE_TRABALHO/agentes-de-ia/essentials/agentes-essentials-blocos/saidas/…-REVISADO-v1.zip`).

Histórico em `03_VERSOES_ANTIGAS/agentes-de-ia/`: `original-articulate/` (exportação original, não modificada) e
`fase-A-so-texto/` (`…-REVISADO.zip`, só texto). O original continua também em `04_NAO_REVISADO/agentes de ia/`.

---

## 1. Material-fonte e mapeamento

Roteiro: `Pesquisa Conteudo Onda 1/Ementa Completa/agentes-de-ia-essentials/roteiros/roteiro-articulate-essentials.md`.
Mapeamento 1:1: lição N do Rise = Módulo N−1 do roteiro (lição 1 = Módulo 0 … lição 7 = Módulo 6 + Encerramento); lição 8 = quiz gerado pelo Articulate.
Links conferidos em 02/11/2026 (`curl`): Guia do TCU → PDF (200); Recomendação CFOAB → PDF (200); **Guia da CGU → responde HTML, não PDF** (ver pontos de atenção).

## 2. Fase A — revisão de texto (329 campos)

Método: mapas `revisao_textos/L01..L08.json` (caminho → texto novo) aplicados por `aplicar_mapas.py`, que recusa campo não textual ou já alterado.
Por lição: L1 40 · L2 34 · L3 49 · L4 41 · L5 45 · L6 49 · L7 41 · L8 (quiz) 30. Por campo: description 112, paragraph 92, title 66, heading 29, feedback 30.

**Correções de conteúdo (as mais importantes):**
- **L4 e L7 — "Mão na massa" errados:** os blocos traziam um *plano de execução* inventado no lugar do prompt-base. Restaurados os prompts O-F-L-C-P do roteiro (com "PARE" e "não localizado").
- **L7 — arquivo-isca incompleto:** faltava justamente a linha "INSTRUÇÃO PARA ASSISTENTES DE IA…"; sem ela o exercício não funcionava. Texto restaurado verbatim.
- **L3 — questão sem enunciado:** "Para as tarefas apresentadas…" sem apresentar as tarefas. Os 4 pedidos do roteiro entraram no enunciado; alternativas C/D reescritas para ficarem inequivocamente erradas (gabarito = B, intacto).
- **L2 — questão do caso limítrofe:** o enunciado tinha perdido o cenário (busca sobre LGPD). Restaurado.
- **Plano × experiência no ChatGPT:** L1 dizia "plano Plus, atualmente chamado de Work"; o quiz (Q19) afirmava "o plano Work, anteriormente chamado de Plus" com gabarito "True". Work é a experiência; Plus é o plano. Enunciado reescrito para "a experiência de agente (Work) exige, no mínimo, o plano Plus" — gabarito "Verdadeiro" continua correto, sem alterar qual alternativa é a certa.
- **L6 — regra da amostragem:** o accordion dizia que um erro na amostra bastava corrigir; o roteiro diz que "uma divergência na amostra obriga a conferir tudo". Accordion e a alternativa correta da questão (mesma posição) alinhados à regra.
- **L6 — números de Princeton:** o texto dizia que "mesmo os melhores agentes acertam 35–42% das tarefas"; restaurada a ressalva do roteiro (assistência web em várias etapas, combinações específicas, não os produtos do curso) e o AI Agent Index (25 de 30).
- **Abas inventadas (L2, L5, L6):** frases sem fonte ("tornou o acesso mais democrático", "consumo exibido em tempo real", "controle de custos pelo limite de horas") trocadas pelos dados do roteiro (datas, planos, rotas, custos, pontos de atenção).
- **Conteúdo do roteiro que faltava:** classes de ferramenta do NIST (L2), Recomendação 001/2024/CFOAB (L3), opções reais dos modos de aprovação (L3), pesquisa da Univ. de Washington (L3), descontinuação do ChatGPT agent (L1), alerta de custo do Manus (L5), ficha de revisão (L6), nota de créditos e ponto de controle (L7), link do Guia do TCU (L1), encerramento (L7).
- Objetivos padronizados em "Ao final desta lição, você será capaz de:" e alinhados, na ordem, ao roteiro; aberturas genéricas trocadas pela analogia do assistente recém-contratado; "True/False" → "Verdadeiro/Falso" (Q9, Q19, Q22); distratores sem sentido trocados (Q2, Q3, Q15, Q16).
- Marcadores `[conferir]` do roteiro **não** foram levados para o texto do aluno (ver pontos de atenção).

`validar_estrutura.py`: ESTRUTURA OK nas 8 lições; 329 campos = 329 entradas dos mapas.

## 3. Fase B — inserções (9 blocos)

| Lição | Posição final | Tipo | Por quê |
|---|---|---|---|
| 1 | 0–3 | Seção nativa "Sobre este curso": título + parágrafo (objetivo geral, 129 min, público, pré-requisitos, recursos), lista das 5 competências, destaque 📌 de vigência, Continue | Identificação, objetivo geral, competências e vigência do roteiro não estavam no curso |
| 2 | 9 | HTML "Chat, automação ou agente?" (6 situações, correção imediata) | O objetivo 3 só era lido, não praticado |
| 3 | 12 | Questão nativa: alucinação × injeção num mesmo caso (correta na 2ª) | O objetivo 3 (distinguir os dois riscos) não era verificado |
| 4 | 13 | HTML "Confira sua ordem de serviço" (cola o texto; verifica os 5 itens da lista de validação) | O Checklist do roteiro vira autoverificação real |
| 5 | 10 | HTML "Intervir ou deixar seguir?" (6 trechos do diário de bordo) | Pratica os sinais de intervenção (objetivo 2) |
| 6 | 12 | HTML "Ficha de revisão" (gera a ficha em texto; aplica a regra da amostragem) | A ficha do roteiro vira ferramenta |

Nenhum HTML trava Continue. Fonte dos HTML: `…/agentes-essentials-blocos/trabalho/html/src/` (CSS/JS comuns herdados do Perplexity, cor `#152f4d` do tema; montagem por `build.py`); roteiros em `trabalho/roteiros/`.

Edições pós-inserção (`05_ARQUIVOS_DE_TRABALHO/agentes-de-ia/pos_edicoes.py`, com checagem folha a folha): descrição da capa reescrita (era "Já pensou em aumentar sua eficiência…") e `completeHint` dos 2 Continues → "Conclua o conteúdo acima para continuar.".

## 4. Validações

| Etapa | Ferramenta | Resultado |
|---|---|---|
| Original | `verificar_scorm.py` | APROVADO, 0 erros, 0 avisos |
| Fase A | `validar_estrutura.py` | ESTRUTURA OK, 329 campos |
| Fase A, pacote | `scorm_reempacotar.py` | round-trip OK; só `runtime-data.js` alterado |
| Fase B | `validar.py` | APROVADO: só inserção, 9 blocos seguindo os modelos, 667 IDs únicos |
| Pós-edições | `pos_edicoes.py` | APROVADO: 3 folhas (capa + 2 completeHint) |
| Pacote v1 | `verificar_scorm.py --original` | APROVADO, 0 erros, 0 avisos; só `runtime-data.js` alterado |

## 5. Teste no navegador (mock de LMS da skill, servidor sem cache)

**Visto:** o pacote carrega; lição 1 mostra a seção nova e para no Continue; ao clicar, aparecem os 12 blocos originais, o link do TCU e o registro "Mão na massa"; o HTML da lição 2 está na posição 9 (vizinhos conferidos pelos IDs). Os 5 HTMLs, abertos sozinhos: classificação com correção e placar, validador (pedido vago → 5 "falta"; prompt-base → 5 "atendido"), ficha (divergência na amostra → aviso e não conclui; tudo confere → gera a ficha), envio de `{type:'complete'}` só ao concluir; sem rolagem horizontal a 375 px. Console sem erros.

**Não verificado:** os HTMLs renderizados *dentro do player* (o painel do navegador estava oculto e o Rise não carrega blocos HTML assim); o quiz na tela (Verdadeiro/Falso e enunciados novos estão no JSON, não vistos); retomada sem `reset`; abertura por `file://`; LMS real; **interface real do Manus, Work e Cowork** (exige conta; não entro em contas).

## 6. Pontos de atenção para revisão humana

1. **Rótulos `[conferir]` do roteiro** não foram validados: `manus.im > cadastro`, `Manus > Nova tarefa > Chat/Agent > Manus 2.0 Lite`, botão de anexo do Manus, `Settings > Cloud Browser`, `ChatGPT > Configurações > Conta`, `Configurações > Navegador na nuvem`, seletor de aprovação do Claude. Confira numa conta antes de publicar.
2. **Link da CGU** (lição 7) responde página HTML, não PDF — pode ser uma página de download; abra no navegador para confirmar.
3. **Cursos indicados no encerramento:** o roteiro cita "N8N: Agentes de IA - Essentials 6"; tirei o "6", que parece erro de digitação. Confirme os nomes do catálogo (Claude Cowork, MCP, Multiagentes, N8N).
4. **Quiz:** a questão de associação (Q10/Q13) usa `matchTitle`, que não foi revisado; e a de múltipla resposta (Q17) tem feedbacks únicos longos — não alterados.
5. Gabaritos: nenhum foi mudado. Na questão da amostragem (L6), a alternativa correta passou a incluir "conferir a tabela inteira", conforme a regra do roteiro.
6. O validador da ordem de serviço é por palavras-chave (ex.: aceita "somente"/"apenas" + "anexo"); uma ordem bem escrita com outras palavras pode aparecer como "falta". O texto do bloco avisa isso.
