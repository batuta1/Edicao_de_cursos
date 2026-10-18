# Relatório de edição — NotebookLM - Hands On (fase A: revisão de texto)

Data: 18/10/2026 · Entrada: `03_VERSOES_ANTIGAS/original-articulate/notebooklm-hands-on-scorm12-Iwwx9t04.zip` (não modificado)
Saída: `notebooklm-hands-on-scorm12-Iwwx9t04-REVISADO-faseA.zip` (cópias em `03_VERSOES_ANTIGAS/fase-A-so-texto/` e `05_ARQUIVOS_DE_TRABALHO/hands-on/`)
(versão intermediária, sem blocos novos; a fase B está em `Relatorio_HandsOn_Revisao_e_Insercao.md`)

## Material-fonte e mapeamento

Fonte: `Pesquisa Conteudo Onda 1/Ementa Completa/notebooklm-essentials/roteiros/roteiro-articulate-hands-on.md`.
O roteiro tem 7 partes; o Articulate gerou 3 lições.

| Lição no Rise (licao = position) | Partes do roteiro |
|---|---|
| 1 Selecionando e Organizando Documentos Públicos (0) | Antes de Arregaçar as Mangas + Oficina 1 |
| 2 Conferindo Respostas e Criando Conteúdos com IA (1) | Oficina 2 + Oficina 3 |
| 3 Compartilhando e Aplicando o Notebook Inteligente (2) | Oficina 4 (só o compartilhamento) + A Parte dos Dez + Conseguiu! |

**Omitidos pelo Articulate (não há bloco onde revisar; vão para o plano da fase B):** o Mapa da Mão na
Massa (tabela de oficinas e tempos), os passos práticos da Oficina 4 (Resumo em Áudio, mapa mental,
compartilhar), a tabela "Se travar" da Oficina 4, o **Projeto Final** inteiro e todos os desafios
"Quer ir além?" das quatro oficinas.

## Critério

`promptRevisaoPorClaude.md` + skill `revisar-curso-scorm`; tom do roteiro Hands-on ("Para Leigos": direto,
segunda pessoa). Edições por script campo a campo (`aplicar.py` + `edicoes_ho.py`, no scratchpad da sessão).

## Alterações por lição

Padrões em todas: objetivos com a fórmula "Ao final desta lição, você será capaz de:" e itens concretos;
aberturas genéricas trocadas pelo "🎯 problema" do roteiro (estudante, advogada, professor, jornalista);
process com tempo da oficina na intro e "Pequena vitória"/🏁 no resumo; destaques com o emoji fora do
negrito (padrão da equipe); feedbacks de múltipla escolha com "Correto." / "Não." + porquê.

- **Lição 1** — **Kit LGPD restaurado** (não existia no curso): o bloco 7 passou a listar as quatro fontes,
  com links e como cada uma entra. Restaurados: aviso de troca de nome (Gemini Notebook), verificação da conta
  e do botão "Criar novo notebook", aviso do "joinha" de feedback (dentro do item Vermelho do semáforo), 🤓 e 🏁.
  Process reescrito com os 8 passos do roteiro, incluindo o "Agora sozinho" e o prompt de conferência do corpus.
- **Lição 2** — divisão explícita em Oficina 2 e Oficina 3; flashcards viraram "o que pedir na pergunta";
  process da Oficina 2 com o prompt completo e a ficha total/parcial/não; o passo 5 do process da Oficina 3
  ganhou o "Se travar" (Guia dentro de Relatórios, linha do tempo, limite de 10/dia), que o Articulate omitiu.
- **Lição 3** — "Opções de compartilhamento" alinhado ao roteiro (por pessoa / link / só a conversa); removida a
  afirmação sem fonte "feedbacks e comentários podem ser visíveis para todos com acesso"; os dez hábitos
  restaurados com o texto completo do roteiro (antes eram só títulos); fechamento "Conseguiu! E agora?" do roteiro.

## Contagem e validação

- Campos alterados: **176** (aplicados = contados). description 46, paragraph 61, title 37, heading 16, feedback 16.
- `validar_estrutura.py`: **ESTRUTURA OK** nas 3 lições.
  Na primeira tentativa, 6 edições em `feedbackCorrect`/`feedbackIncorrect` das questões de múltipla resposta
  foram **reprovadas** (não são campos textuais permitidos). Foram desfeitas; as lições foram regeradas a partir
  do curso original e as demais edições reaplicadas.
- `scorm_reempacotar.py`: round-trip OK; 84 arquivos; nenhum alterado fora de `runtime-data.js`.
- `verificar_scorm.py` (ponte): **APROVADO**, 0 erros, 10 avisos — os mesmos 10 do pacote original
  (`correct/corrects` com texto de alternativa nas 3 questões de múltipla resposta; comportamento conhecido do Rise).

## Pontos de atenção

1. **Questão de múltipla resposta da lição 1 (bloco 6)**: o original pedia "classifique cada situação", mas as
   alternativas são só as cores e as três estão corretas — o formato não permite classificar. Sem mexer no
   gabarito, o enunciado virou "Quais cores do semáforo aparecem nesse conjunto? Marque todas", que combina com ele.
   Proposta: na fase B, uma atividade HTML de classificação de verdade.
2. **Feedbacks das 3 questões de múltipla resposta continuam como o Articulate gerou** ("Parabéns! Você…"),
   porque `feedbackCorrect`/`feedbackIncorrect` não podem ser editados por esta skill. Ajustar no Rise ou autorizar.
3. Títulos das alternativas das múltiplas respostas também não foram tocados (os campos `correct/corrects`
   guardam esses textos).
4. Rótulos [conferir] do roteiro mantidos sem a marca para o aluno (adicionar fonte, site/link, Save to note,
   Configure Chat, "só a conversa", Gerar mais tarde).
5. "Complete the content above before moving on." dos Continues segue em inglês.

## Não verificado

O curso ainda não foi aberto no navegador; fica para a fase B.
