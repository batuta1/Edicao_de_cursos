# Relatório de revisão e inserção — NotebookLM - Hands On

Data: 18/10/2026 · Grau de liberdade: moderado (plano completo aprovado) · Curso **não publicado** com alunos.

**Pacote final para a LMS:**
`01_FINALIZADO_subir-na-LMS/notebooklm/notebooklm-hands-on-scorm12-Iwwx9t04-FINAL-com-blocos-v1.zip`
(cópia idêntica de `05_ARQUIVOS_DE_TRABALHO/notebooklm/hands-on/blocos/saidas/notebooklm-hands-on-scorm12-Iwwx9t04-REVISADO-v1.zip`).
O `.zip` original do Articulate está em `03_VERSOES_ANTIGAS/notebooklm/original-articulate/` e não foi modificado.

---

## 1. Material-fonte e mapeamento

Roteiro: `Pesquisa Conteudo Onda 1/Ementa Completa/notebooklm-essentials/roteiros/roteiro-articulate-hands-on.md`.

| Lição (licao = position) | Partes do roteiro |
|---|---|
| 1 Selecionando e Organizando Documentos Públicos (0) | Antes de Arregaçar as Mangas + Oficina 1 |
| 2 Conferindo Respostas e Criando Conteúdos com IA (1) | Oficina 2 + Oficina 3 |
| 3 Compartilhando e Aplicando o Notebook Inteligente (2) | Oficina 4 + Projeto Final + A Parte dos Dez + Conseguiu! |

## 2. Fase A — revisão de texto

Detalhes em `02_RELATORIOS/notebooklm/Relatorio_HandsOn_Fase_A_Revisao_de_Texto.md`. Resumo: 3 lições, **176 campos**;
Kit LGPD restaurado com links (lição 1), dez hábitos com o texto completo, tom "mão na massa" do roteiro;
enunciado da múltipla resposta da lição 1 reescrito para combinar com o gabarito (que não foi alterado).
6 edições em `feedbackCorrect`/`feedbackIncorrect` foram reprovadas pelo validador e desfeitas.

## 3. Fase B — inserções (22 blocos novos)

Índices finais na v1:

| Lição | Posição final | Tipo | Justificativa didática |
|---|---|---|---|
| 1 | 3 | HTML "O mapa da mão na massa" (7 partes, tempos, lição de cada uma, o que se entrega) | A tabela do roteiro não existia no curso; mostra que as 7 partes estão comprimidas em 3 lições |
| 1 | 7 | HTML "Semáforo: posso subir isto?" (7 documentos, correção imediata) | A múltipla resposta original não permite classificar; aqui o participante classifica de verdade |
| 1 | 23–24 | Seção nativa "Quer ir além? (opcional)": título + accordion com 3 desafios | Desafios da Oficina 1, omitidos |
| 2 | 10–11 | HTML "Audite esta citação" (total / parcial / não) + Continue `completeBlock` | Pratica a ficha de conferência da Oficina 2 antes da questão |
| 2 | 18–19 | Seção nativa "Quer ir além?": accordion com 6 desafios (Oficinas 2 e 3) | Desafios omitidos |
| 3 | 8–14 | Passos da Oficina 4: parágrafo + lista dos 7 passos + 🏁 + "Se travar" (título + accordion) + "Quer ir além?" (título + accordion) | A Oficina 4 não tinha nenhum passo prático (áudio, mapa mental, compartilhar) |
| 3 | 18–24 | Seção Projeto Final: Continue + missão + sugestões por perfil + 7 passos + HTML checklist "Como saber que terminou" + Continue `completeBlock` | O Projeto Final estava ausente; agora entra antes da Parte dos Dez, como no roteiro |

**Mudanças em relação ao plano:** nenhuma de conteúdo. Detalhe de forma: os passos usam **lista numerada**
(e não process), porque o process ainda não foi testado como inserção.

**Arquivos:** HTML embutidos (inline), sem pastas anexadas. Fonte em
`05_ARQUIVOS_DE_TRABALHO/notebooklm/hands-on/blocos/trabalho/html/src/` (o semáforo, a auditoria e o checklist foram
adaptados dos HTML já testados no Essentials); roteiros em `.../trabalho/roteiros/`, gerados por `gerar_roteiros.py`.

## 4. Validações

| Etapa | Ferramenta | Resultado |
|---|---|---|
| Fase A | `validar_estrutura.py` | ESTRUTURA OK, 176 campos (após desfazer as 6 edições reprovadas) |
| Ponte | `verificar_scorm.py` no `-REVISADO-faseA.zip` | APROVADO, 0 erros, 10 avisos (os mesmos 10 do original) |
| Fase B | `validar.py` | APROVADO: só inserção, 22 blocos novos, 352 IDs únicos |
| Fase B | `verificar_scorm.py --original` | APROVADO, 0 erros, 10 avisos (os mesmos); só `runtime-data.js` alterado |

Os 10 avisos: `correct/corrects` com texto de alternativa nas 3 questões de múltipla resposta — vêm do próprio
Articulate e já estavam no pacote original; a correção usa `answers[].correct`.

## 5. Teste no navegador

**Visto e funcionando** (mock de LMS da skill, servidor sem cache):
- Posição de todos os blocos novos nas 3 lições, conferida pela ordem renderizada.
- Mapa: etapas abrem e mostram o que se entrega. Semáforo: feedback de erro e conclusão.
- Auditoria (lição 2) e checklist do Projeto Final (lição 3): Continue travado antes, liberado depois.
- Lista da Oficina 4 com a aparência dos blocos do curso.
- Retomada: ao recarregar sem `reset`, voltou à lição 3 e o Continue da auditoria seguiu liberado.
- Console sem erros.
- **Por `file://`** (Chrome headless, como no duplo clique): os HTML da lição 1 carregam com conteúdo.

**Não verificado:**
- As 3 questões de múltipla resposta respondidas no navegador (não foram alteradas na estrutura; só textos).
- Largura de celular nos HTML do Hands-on.
- Abertura por duplo clique no seu navegador e numa LMS real.
- Os links do Kit LGPD na lição 1 (só conferidos no JSON; no Essentials, os mesmos links foram vistos no navegador).

## 6. Pontos de atenção para revisão humana

1. **Feedbacks das 3 múltiplas respostas** seguem como o Articulate gerou ("Parabéns! Você…") — esses campos
   não podem ser editados pela skill. Ajustar no Rise, se quiser.
2. **Múltipla resposta da lição 1**: enunciado reescrito para combinar com o gabarito (todas as cores corretas);
   a classificação real agora é feita no HTML "Semáforo" logo antes.
3. **Rótulos [conferir] do roteiro** (adicionar fonte, site/link, Save to note, Configure Chat, "só a conversa",
   "Gerar mais tarde", "Pesquisa Rápida") sem confirmação numa conta real.
4. **Checklist do Projeto Final é autodeclarativo**: o participante marca o que diz ter feito.
5. "Complete the content above before moving on." dos Continues segue em inglês (também nos 2 novos travados).
6. Nenhum gabarito foi alterado.

## 7. Entregável

`Onda 1/NotebookLM/01_FINALIZADO_subir-na-LMS/notebooklm/notebooklm-hands-on-scorm12-Iwwx9t04-FINAL-com-blocos-v1.zip`
