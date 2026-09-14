# Análise Crítica 360 — ChatGPT no Word (Essentials), versão 1.0

**Objeto base:** ChatGPT aplicado à produção de documentos no Microsoft Word
**Público-alvo:** professores universitários, novatos em IA generativa
**Pré-requisitos declarados:** uso básico do Word; conta ChatGPT; nenhum conhecimento prévio de IA
**Trilha:** Essentials
**Documento analisado:** `01-v1-essentials.md`

---

## 1. Sumário Executivo

**Nota: 6,0 / 10.** É um plano de aula bem escrito e mal sequenciado. O texto tem registro correto,
progressão legível e exercícios com critério de êxito — mas o conteúdo que protege o participante
está no lugar errado, e o conteúdo que o material-fonte oferece de mais específico não está em lugar
nenhum.

Principais constatações:

1. **Segurança de dados aparece no Módulo 5**, depois de o participante ter colado quatro documentos
   próprios no sistema ao longo de quatro módulos. É o defeito mais grave do documento.
2. **Não há Módulo 0.** O participante começa o Módulo 1 sem ter verificado se tem conta, qual é seu
   plano, se o plano trata seus dados de um jeito ou de outro, e sem ter feito cópia do documento
   com que vai trabalhar.
3. **Nenhum dado concreto do material-fonte foi aproveitado.** Limites de upload, retenção, política
   de treinamento por plano, limites por projeto — tudo isso está no material bruto e nada disso
   está no curso. O curso poderia ter sido escrito sem material-fonte algum.
4. **Integridade acadêmica não é mencionada uma vez.** Para o público declarado, esta é a pergunta
   que mais importa e a que mais gera constrangimento institucional. A omissão é indefensável.
5. **O maior diferencial para o público está fora do curso:** arquivos de referência e modelos
   reutilizáveis. O docente reescreve o mesmo tipo de documento a cada semestre; é exatamente o caso
   que o material-fonte descreve e o curso ignora.
6. Não há troubleshooting em nenhum ponto, embora a v1.0 mencione três situações previsíveis de
   falha (formatação perdida, símbolos de Markdown, arquivos longos).

---

## 2. Pontos Positivos (Fortalezas)

**A definição operacional de modelo de linguagem no Módulo 1.** "Produz o texto mais plausível, e não
necessariamente o mais verdadeiro" é a formulação certa: dá ao participante um modelo mental do qual
todas as cautelas posteriores decorrem por dedução, em vez de precisarem ser memorizadas uma a uma.
Deve ser mantida literalmente e transformada em fio condutor explícito.

**A declaração de que não existe suplemento oficial da OpenAI para o Word.** É o tipo de informação
que evita quinze minutos de busca frustrada e uma conclusão errada ("então não dá"). Acerto de
expectativa, colocado cedo. Mantenha.

**Os quatro elementos da instrução no Módulo 2.** Tarefa, público, extensão, registro é um esquema
curto o bastante para ser lembrado e completo o bastante para funcionar. O acréscimo da restrição de
preservação ("o que não deve mudar") é o detalhe que separa este material dos guias genéricos de
prompt.

**A distinção entre "peça outra versão" e "diga o que está errado" no Módulo 3.** Pedagogicamente é o
ponto mais valioso do curso: transfere ao participante o papel de editor, que é o papel que ele já
sabe exercer.

**Os critérios de êxito dos exercícios são verificáveis sem instrutor.** Coerente com a natureza
autoinstrucional declarada nos contornos.

---

## 3. Pontos Negativos e Gargalos (Debilidades)

### 3.1 Sequência de risco invertida

O Módulo 5 informa que não se deve inserir dado de aluno, resultado não publicado ou parecer
sigiloso. Mas os exercícios dos Módulos 3, 4 e 5 mandam o participante colar trechos de documentos
próprios de trabalho. Um docente que siga o curso na ordem terá colado material institucional real
antes de ler a única advertência sobre isso. O curso **cria** o risco que depois adverte.

### 3.2 Ausência de verificação inicial

Não há nenhum momento em que o participante confirme que tem conta ativa, que sabe qual é seu plano,
que fez cópia do documento de trabalho e que o Word está acessível. O Módulo 1 pressupõe tudo isso.
Em um curso autoinstrucional, cada pressuposto não verificado é um ponto de abandono.

### 3.3 O material-fonte foi ignorado

O material bruto contém informação factual específica que não aparece no curso:

| Informação disponível na fonte | Onde deveria estar | Está? |
|---|---|---|
| Limite de 512 MB por arquivo | Módulo sobre envio de arquivos | Não |
| Limite de 2 milhões de tokens por arquivo de texto | Idem | Não |
| 80 arquivos a cada 3 horas; 3 por dia no plano gratuito | Idem | Não |
| Conversas e arquivos apagados em até 30 dias após exclusão | Módulo de segurança | Não |
| Business, Enterprise e Edu não treinam por padrão; Plus e Pro treinam salvo desativação | Módulo de segurança | Não |
| Onde desativar o treinamento (controles de dados do ChatGPT) | Idem | Não |
| Recuperação de imagens em PDF só no Enterprise; demais planos extraem só texto | Módulo sobre leitura de arquivos | Não |
| Arquivos de referência e modelos reutilizáveis (`@Template-Creator`, `@Documents`) | Módulo próprio | Não |
| Limite de arquivos por projeto (Plus 20; Pro, Team, Education, Business 40) | Módulo de segurança | Não |

Um curso que não usa o material-fonte disponível entrega ao participante menos do que ele acharia
sozinho na Central de Ajuda em dez minutos.

### 3.4 Integridade acadêmica ausente

Para um docente, "posso usar isso?" precede "como uso isso?". O curso não trata de: o que a
instituição do participante permite; como declarar uso de IA em um documento acadêmico; a diferença
entre usar como assistente de redação e usar como autor; o que dizer aos alunos que perguntarem se
eles podem fazer o mesmo. Nenhum desses pontos exige tomar partido — exigem apenas ser nomeados,
com a orientação de consultar a norma da própria instituição.

### 3.5 O Módulo 1 abre com teoria e fecha com múltipla escolha

Em um curso autoinstrucional, o primeiro módulo é o que decide se o participante continua. O atual
tem cinco parágrafos expositivos e um exercício de marcar alternativa. Não há nenhum momento em que o
participante toque a ferramenta antes do Módulo 3. É tarde demais.

### 3.6 Falhas previsíveis mencionadas e não resolvidas

O Módulo 4 informa que o Markdown não cola bem no Word e sugere localizar e substituir — em uma
frase, sem procedimento. O Módulo 1 informa que comentários e alterações controladas não sobrevivem
ao envio do arquivo — e não diz o que fazer no lugar. São dois casos de problema nomeado e
abandonado.

### 3.7 Word desktop e Word na web tratados como equivalentes

Os recursos necessários citam os dois. Os módulos não distinguem em nenhum momento. Como a colagem
especial e os estilos funcionam de modo diferente nos dois ambientes, o participante que estiver na
web vai procurar um menu que não existe daquela forma.

### 3.8 Não verificável

Não foi possível verificar de forma independente, a partir do material-fonte: (a) a inexistência
atual de suplemento oficial da OpenAI para o Word — a fonte fala de suplementos para Excel e
PowerPoint e de add-ins de terceiros para o Word, o que é indício forte mas não declaração; (b) a
disponibilidade do fluxo de modelos (`@Template-Creator`), que a própria fonte condiciona a plano e
configuração de espaço de trabalho. Ambos os pontos devem constar como pendência de validação e ser
formulados no roteiro final de modo condicional.

---

## 4. Matriz de Soluções e Melhorias

| # | Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|---|
| 1 | Segurança depois do uso | Módulo 5 | Criar **Módulo 0 — Antes de colar qualquer coisa**, com: verificação de conta e plano; tabela de tratamento de dados por plano (Plus/Pro treinam salvo desativação; Business/Enterprise/Edu não treinam por padrão); caminho para desativar o treinamento; lista do que nunca colar; passo obrigatório de duplicar o documento de trabalho. Remover a advertência do Módulo 5 e substituí-la por uma retomada de uma linha. | Crítica |
| 2 | Sem verificação inicial | Início do curso | O exercício do Módulo 0 é uma checagem de quatro itens: conta acessível, plano identificado, cópia do documento criada, Word aberto. Critério de êxito: os quatro confirmados. | Crítica |
| 3 | Integridade acadêmica ausente | Todo o curso | Subseção própria no Módulo 0: "Autoria e uso declarado", com três perguntas que o docente deve responder antes de usar (o que a instituição permite; se o uso precisa ser declarado; o que dizer aos alunos) e a orientação explícita de consultar a norma interna. Não prescrever conduta; nomear a decisão. | Crítica |
| 4 | Limites de arquivo ausentes | Módulo 1 | Acrescentar tabela de limites (512 MB por arquivo; 2 milhões de tokens por arquivo de texto; 80 arquivos a cada 3 horas; 3 por dia no gratuito; 20 ou 40 arquivos por projeto conforme plano), marcada como sujeita a alteração. | Alta |
| 5 | Modelos reutilizáveis fora do curso | — | Novo **Módulo 4 — Do documento avulso ao modelo reutilizável**: arquivo de referência (uma tarefa) versus modelo (fluxo repetido), com o caso do docente que refaz o mesmo plano de ensino a cada semestre. Formular de modo condicional: o recurso depende de plano e configuração. | Alta |
| 6 | Módulo 1 sem contato com a ferramenta | Módulo 1 | Substituir a múltipla escolha por uma pílula prática de três minutos: fazer a mesma pergunta de duas formas (vaga e específica) e comparar os resultados. A múltipla escolha migra, reduzida, para o Módulo 5. | Alta |
| 7 | Markdown e formatação abandonados | Módulo 4 | Transformar em subseção "Solução de Problemas" com procedimento: instrução preventiva ("texto puro, sem símbolos"); colagem especial pelo caminho de menu; limpeza em massa com localizar e substituir; reaplicação de estilos. | Alta |
| 8 | Comentários e revisões perdidos no envio | Módulo 1 | Acrescentar o que fazer no lugar: copiar o texto dos comentários manualmente para a conversa, ou trabalhar por trecho. Declarar que o sistema não vê a conversa de revisão. | Média |
| 9 | Desktop e web indistintos | Módulos 3 e 4 | Onde houver caminho de menu, apresentar as duas variantes ou declarar explicitamente a qual ambiente o caminho se refere. | Média |
| 10 | Sem troubleshooting sistemático | Todo o curso | Subseção "Solução de Problemas" nos Módulos 0, 1 e 4 — os três pontos que a auditoria marca como críticos (acesso, envio de arquivo, formatação). | Média |
| 11 | Nenhuma retomada explícita de conceito | Todo o curso | Tornar o fio condutor visível: plantar "plausível ≠ verdadeiro" no Módulo 0 e retomá-lo nominalmente no módulo de revisão e na síntese. | Média |
| 12 | Carga horária sem lastro | Tabela de módulos | Os tempos foram arredondados em 25 min por módulo, sem cálculo por atividade. Refazer na Fase 4 pela MET, atividade a atividade. | Média |

---

## 5. Roadmap de Expansão

**Cabe neste curso** (endereçado pela matriz acima):

- Módulo 0 de preparação, dados e autoria.
- Módulo de modelos reutilizáveis e arquivos de referência.
- Limites concretos de arquivo e de uso.
- Solução de problemas nos três pontos críticos.

**Fica para um curso seguinte:**

- **Suplementos de terceiros para o Word.** Existem na loja do Office e resolvem o incômodo do
  copiar e colar, mas veem apenas o texto selecionado, devolvem texto simples e não propõem
  alterações controladas. Merecem um critério de avaliação, não uma recomendação. Fora do escopo de
  um curso introdutório porque a decisão é institucional, não individual.
- **Leitura e análise de material de terceiros.** Comparar dois documentos, aplicar uma rubrica de
  avaliação de um documento ao conteúdo de outro, extrair citações. O material-fonte descreve essas
  operações de síntese, transformação e extração, e elas são diretamente úteis para orientação de
  trabalhos — mas constituem um curso próprio.
- **Fluxo institucional.** ChatGPT Trabalho, biblioteca, projetos com limite de arquivos,
  compartilhamento de modelos por plugin com aprovação de administrador. Depende de contrato
  institucional e é assunto de quem administra, não de quem escreve.
- **Comparação com o Microsoft Copilot.** Pergunta inevitável do público. Exige testar as duas
  ferramentas no ambiente da instituição, o que este curso não tem como fazer.
