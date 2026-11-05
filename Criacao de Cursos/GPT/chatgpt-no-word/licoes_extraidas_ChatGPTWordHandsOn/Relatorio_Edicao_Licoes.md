# Relatório de alterações — ChatGPT Word - Hands On

Revisão integral do pacote `chatgpt-word-hands-on-scorm12-jqAulfnT.zip` (formato default,
`scormcontent/runtime-data.js`; `course.id` `0n2O0LOkRyck9XkXloJ-i_ojH-evJ30A`; 3 lições).

## Arquivos editados

- `licao_01_Ambiente_Seguro_e_Preparação_de_Documentos_no_Word_e_ChatGPT.json`
- `licao_02_Redação,_Revisão_e_Diagnóstico_de_Documentos_com_ChatGPT.json`
- `licao_03_Redução,_Transformação_e_Adaptação_de_Conteúdo_para_Novos_Públicos.json`

Nenhum arquivo de lição foi lido sem ser alterado: as três foram editadas.

## Material-fonte e mapeamento

Fonte principal: `roteiros/roteiro-articulate-hands-on.md`. Fontes de apoio: `ementa.md` (objetivos,
pontos de controle, pendências de validação) e `promptRevisaoPorClaude.md` (regras de edição).

| Lição no Rise | Oficinas do roteiro |
|---|---|
| 1 — Ambiente Seguro e Preparação… | Oficina 0 — Cinco minutos antes de começar |
| 2 — Redação, Revisão e Diagnóstico… | Oficina 1 (página em branco) + Oficina 2 (parágrafo) + Oficina 3 (documento inteiro) |
| 3 — Redução, Transformação e Adaptação… | Oficina 4 (encolher) + Projeto Final + "Conseguiu! E agora?" |

## Critério aplicado

- Aberturas genéricas trocadas pelo "🎯 O Problema" de cada oficina, que traz a situação concreta
  do roteiro (o cursor piscando há quarenta minutos, o relatório de dezoito páginas que precisa
  virar duas).
- Fórmula única para objetivos: "Ao final desta lição, você será capaz de:", com itens alinhados,
  na ordem, ao que cada oficina realmente faz.
- O bloco "summary" de cada Process, que antes só repetia o processo, passou a trazer o
  **Ponto de controle** do roteiro, ou seja, um estado verificável na interface. A ementa define
  esse ponto de controle como o instrumento de avaliação da trilha Hands-on.
- Recuperada a especificidade perdida: caminho do Word na web, limites de envio, breadcrumbs,
  frase final do prompt do Projeto Final e prompt da revisão de diagnóstico.
- Cabeçalhos de seção renomeados com o nome da oficina ("Oficina N — …"), para que o participante
  saiba onde está dentro das lições que juntam mais de uma oficina.
- Mantidos sem alteração: prompts entre aspas triplas, a maior parte dos accordions de "Se travar",
  o statement "Regra de ouro", as dicas 💡/📌 e todos os gabaritos.

## Alterações por lição

### Lição 01 — Oficina 0 (35 campos)

- **Abertura:** o título "Preparando um Ambiente Seguro e Eficiente" e o parágrafo genérico deram
  lugar a "Oficina 0 — Cinco minutos antes de começar", com o problema do roteiro: o texto vai para
  servidores de outra empresa, e o original precisa continuar intacto.
- **Objetivos:** os 5 itens vagos ("Configurar Word e ChatGPT corretamente") foram reescritos de
  acordo com os passos reais: identificar o plano, desativar o uso do conteúdo, reconhecer o que
  nunca entra, criar a cópia de trabalho e verificar a norma institucional.
- **Process:**
  - O resumo virou Ponto de controle (dois arquivos na pasta + saber o plano).
  - O passo "Entenda os controles de dados" virou ação ("Desative o uso do seu conteúdo, se
    quiser") e recuperou o "não é falha sua".
  - O passo da norma institucional recuperou a pergunta sobre os alunos.
- **Erro corrigido em "O que nunca entra":** o item de dado pessoal de terceiros dizia "não podem
  ser compartilhados **sem consentimento explícito**", o que sugere que com consentimento pode. O
  roteiro diz "nada aqui entra no ChatGPT, em nenhum plano". O texto agora segue o roteiro. O item
  de pesquisa não publicada dizia "Evite" e passou a ser uma proibição.
- **Abas de planos:** a frase de enchimento ("revisar regularmente as configurações…") foi
  removida. As duas abas agora deixam claro que a lista do que nunca entra vale também nos planos
  que não treinam com o conteúdo.
- **Quiz:** os 4 feedbacks agora explicam o motivo e remetem à lista. O gabarito não mudou.
- **Erro corrigido no "⚠️ Cuidado":** o texto dizia "não pule o passo 5", mas no Process do Rise a
  cópia de trabalho é o **passo 3** (o 5 do roteiro contava passos que, no curso, viraram blocos
  separados). Agora diz "não pule o passo 3, a cópia de trabalho".

### Lição 02 — Oficinas 1, 2 e 3 (52 campos)

- **Abertura e objetivos:** a abertura genérica ("transformar cada uma dessas etapas, tornando o
  processo mais ágil e menos solitário") deu lugar aos três problemas concretos das oficinas. Os 4
  objetivos telegráficos ("Superar bloqueios de escrita") viraram resultados verificáveis.
- **Oficina 1:**
  - Cabeçalho e problema retirados do roteiro.
  - O resumo do Process virou Ponto de controle (Painel de Navegação).
  - O passo "Cole no Word" recuperou o caminho do Word na web e o motivo (fundo cinza, fonte do
    navegador).
  - O feedback da alternativa correta do quiz agora detalha o que dar de contexto.
- **Oficina 2:**
  - Cabeçalho e problema retirados do roteiro.
  - Intro do Process reescrita, e o resumo virou Ponto de controle.
  - O passo "Avalie e Dê Feedback" virou "Diga o que está errado", que é o ponto central da
    oficina.
  - O passo de conferência recuperou "reescrever é justamente onde número troca de lugar".
- **Erro corrigido no "⚠️ Cuidado":** o texto dizia "O passo 6 não é opcional", mas no Process do
  Rise a conferência de números e citações é o **passo 5** (o passo 6 é colar no Word). Corrigido.
- **Oficina 3:**
  - Cabeçalho e problema retirados do roteiro.
  - O passo de limites recuperou os números (512 MB por arquivo; 2 milhões de tokens).
  - O breadcrumb do anexo foi restaurado.
  - O último passo, "Compare com o Documento no Word", virou "Confira o que ele não viu", com o
    caminho `Revisão > Mostrar Comentários` do roteiro.
  - O resumo virou Ponto de controle.
- **Quiz da Oficina 3:** o enunciado "O ChatGPT pode analisar **quais** destes elementos…" sugeria
  resposta múltipla numa questão de escolha única. Agora diz "qual destes elementos o ChatGPT
  efetivamente lê?". Os feedbacks foram reescritos, e o trecho em inglês "(control track changes)"
  foi removido. O gabarito não mudou.

### Lição 03 — Oficina 4 + Projeto Final (41 campos)

- **Abertura e objetivos:** a abertura genérica deu lugar ao problema do roteiro (dezoito páginas
  → duas; nove mil palavras → seis mil). Os objetivos foram alinhados à Oficina 4 e ao Projeto
  Final.
- **Oficina 4:**
  - Cabeçalho e problema retirados do roteiro.
  - O resumo do Process virou Ponto de controle (Contagem de Palavras).
  - Os passos foram ajustados à redação do roteiro ("'Metade' é interpretado com folga").
  - Os accordions tinham uma frase final de enchimento ("Assim, você garante…"). Ela foi trocada
    por informação útil.
- **Projeto Final:**
  - O parágrafo genérico deu lugar à missão do roteiro e aos 4 pares de documentos (antes
    ausentes).
  - Os passos agora remetem à oficina de origem e à numeração correta (lista de dados no passo 2,
    conferida no passo 9).
  - O prompt do passo 3 recuperou a frase final do roteiro: "O leitor não acompanhou o projeto e
    precisa decidir se aprova a continuidade".
  - O passo de revisão de diagnóstico recebeu o prompt do roteiro.
- **Erro corrigido no checklist:** o item 7 dizia "Não há dados identificáveis ou sigilosos
  presentes **no documento**". O critério do roteiro é outro: "Nenhum dado identificável de aluno
  ou informação sigilosa **entrou no ChatGPT**". Os 10 itens foram realinhados ao roteiro, que pede
  "verbatim". O item "símbolos desnecessários" voltou a ser "símbolo de Markdown".
- **Fechamento:**
  - O statement "Você saiu **desta oficina**" passou a "Você sai **deste curso**".
  - O parágrafo final motivacional ("Parabéns… você se tornará cada vez mais autônomo e
    estratégico") deu lugar ao próximo passo concreto do roteiro: um documento por semana, durante
    um mês.

## Contagem e validação

`validar_estrutura.py`: **128 campos de texto alterados** (description=58, paragraph=37, title=16,
feedback=10, heading=7), **0 divergências estruturais**, saída 0. A contagem bate com as edições
intencionais. O detalhamento caminho a caminho foi conferido para a Lição 2.

- Nenhum `id`, `type`, `family`, `variant`, `position`, `settings`, `metadata` ou `globalBlockId`
  foi alterado.
- Nenhum bloco, item de lista, etapa de Process ou alternativa de quiz foi adicionado, removido ou
  reordenado.
- Nenhum campo `correct` foi alterado. Os 4 gabaritos foram conferidos e estão corretos.
- Quantidade de lições: 3 → 3.

Remontagem (`scorm_reempacotar.py`):

- O Base64 passou na verificação de round-trip (129.216 caracteres).
- O pacote novo tem 83 arquivos, e só `scormcontent/runtime-data.js` mudou.
- O título no pacote novo continua "ChatGPT Word - Hands On" (3 lições).

## Gerado

- `cursoChatGPTWordHandsOn.json`: o curso original desserializado.
- `cursoChatGPTWordHandsOn_editado.json`: o curso remontado.
- `cursoChatGPTWordHandsOn_editado_base64.txt`: o payload, para colagem manual se preferir.
- `chatgpt-word-hands-on-scorm12-jqAulfnT-REVISADO.zip`: o pacote SCORM revisado. O `.zip` original
  não foi modificado.

## Teste em navegador

O pacote revisado foi servido em `localhost` com um mock da API SCORM 1.2 (`lms_mock.html`).

**Verificado:**

- O curso carrega, e a capa e as 3 lições aparecem na navegação.
- A abertura da Lição 1 renderiza com acentos e travessões corretos.
- Na Lição 3, avancei pelo primeiro "Continue", respondi o quiz (o Submit foi aceito) e passei o
  segundo "Continue". O bloco do Projeto Final renderiza a lista com setas, e o Process mostra o
  texto novo.
- No payload carregado pelo navegador, estão presentes 7 trechos novos e ausentes 4 trechos
  antigos que foram corrigidos.

**Não verificado visualmente:** accordions, abas e feedbacks de quiz das Lições 1 e 2, e as etapas
internas de cada Process. Também não houve teste em uma LMS real.

## Pontos de atenção (exigem decisão ou olho humano)

1. **Descrição da capa do curso não foi revisada.** O texto ("Já imaginou transformar o jeito que
   você escreve…") fica em `course.description`, fora das lições e fora do que o validador cobre. É
   genérico e não segue o roteiro. Proposta, a partir do bloco Cover do roteiro: *"Um curso mão na
   massa para professores universitários: em duas horas de oficinas você usa o ChatGPT no
   navegador para estruturar, reescrever, encolher e transformar um documento seu, de verdade — e
   sai com ele pronto para enviar e com um caderninho de instruções que funcionam."* Aplicar no
   Rise ou pedir uma edição específica do JSON do curso.
2. **Conteúdo do roteiro ausente no curso.** Não foi possível incluí-lo sem criar blocos, o que as
   regras proíbem:
   - Os blocos "🚀 Quer ir além?" (15 desafios opcionais).
   - O apêndice "A Parte dos Dez — Instruções que Salvam seu Dia".
   - A tabela-mapa das oficinas com os tempos.

   A ementa diz que os dois primeiros não integram a carga horária, mas eles fazem parte da trilha
   Hands-on. Se forem desejados, precisam ser criados no Rise.
3. **Pendências de validação da ementa agora explícitas no texto.** Os números e caminhos abaixo
   já constavam como pendentes de conferência na ementa. Ao restaurá-los, eles ficaram mais
   visíveis no curso e precisam ser conferidos antes da publicação:
   - limites de envio (3 por dia no gratuito; 80 a cada 3 h; 512 MB; 2 milhões de tokens);
   - política de treinamento por plano;
   - rótulos dos menus do Word (incluindo "Manter somente texto" na web e
     `Revisão > Mostrar Comentários`).
4. **Inconsistência herdada da fonte.** O passo de desativar o uso do conteúdo fala em "Plus ou
   Pro" (como no roteiro), mas a aba de planos agrupa "Free, Go, Plus, Pro" como planos que podem
   desativar. O texto foi mantido fiel ao roteiro. Vale conferir na Central de Ajuda da OpenAI se
   Free e Go também têm a opção.
5. **Títulos das lições (navegação) mantidos.** Os títulos ("Ambiente Seguro e Preparação…", etc.)
   são descritivos e funcionam. Agora as oficinas aparecem nos cabeçalhos internos. Se a
   preferência for ver "Oficina N" também no menu lateral, é uma mudança simples de `title`.
6. **Formatação do "⚠️ Cuidado" da Lição 1.** Diferente dos outros statements, ele não tem
   `<strong>` no rótulo. Isso foi mantido como estava.
