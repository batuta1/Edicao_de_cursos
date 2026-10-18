# 02 — Análise crítica 360 · MCP - Hands-on (v1.0)

Entrada: `_processo/01-v1-hands-on.md` + `_processo/00-contornos.md`.
Contexto: objeto base MCP; ferramentas-âncora Claude e ChatGPT; público que não programa (T3) e
desenvolvedores/TI (T6); trilha Hands-on; autoinstrucional; alvo 90–120 min.

## 1. Sumário Executivo

**Nota: 3 / 10.** O tom está certo e as quatro oficinas têm o formato do modelo, mas a v1.0 é
**perigosa para iniciante**: manda o assistente responder e enviar e-mails reais, marcar reuniões na
agenda real, convidar colegas e ler o Drive pessoal — sem configurar aprovação, sem dados de teste e
sem desfazer nada. Ao mesmo tempo, a primeira oficina não é executável (não diz qual URL colar) e a
leitura de arquivos locais, parte da tarefa observável, não aparece.

Principais constatações:

- **Ação irreversível na Oficina 4:** "responda os que forem simples" + "aprove os envios" envia
  e-mail real a terceiros. Envio não se desfaz.
- **Oficina 1 inexecutável:** "cole a URL de um servidor MCP" — qual? O aluno trava no passo 3.
- **Dados reais em todas as oficinas** (Drive, agenda, caixa de entrada). Nenhuma pasta, evento ou
  e-mail de teste.
- **Zero teoria:** o aluno conecta coisas sem saber o que é MCP, conector, ferramenta de leitura ou de
  escrita. O mínimo para o próximo passo precisa estar lá.
- **Nenhuma revogação:** o curso termina com Drive, Calendar e Gmail ligados indefinidamente.
- **Tarefa observável incompleta:** sem leitura de arquivos locais (Filesystem); ChatGPT só aparece
  num "ir além" vago.
- "Deu certo?" mede a ferramenta; "Se travar" é genérico ("tente de novo"); um desafio por oficina
  (o prompt-mestre pede três); 80 min, abaixo da faixa de 90–120.

## 2. Pontos Positivos (Fortalezas)

| Fortaleza | Por que é um acerto |
|---|---|
| Problemas reconhecíveis (arquivo perdido, agenda cheia, e-mails repetitivos) | Ancoram o PBL na rotina do profissional não programador. |
| Tom leve e em 2ª pessoa | Corresponde à trilha; humor dosado ("um café"). |
| Regra de ouro "leia antes de clicar em permitir" | É a semente certa — falta transformá-la em prática real (Needs approval). |
| Caminho `Customize > Connectors` correto | Coincide com a ajuda oficial. |
| Sequência ler → consultar → agir | A ordem de risco crescente está implícita; precisa ficar explícita e com travas. |

## 3. Pontos Negativos e Gargalos (Debilidades)

### 3.1 Clareza pedagógica

- Oficina 1 sem URL, sem dizer onde ligar o conector na conversa, sem pergunta de teste.
- O aluno não sabe o que está fazendo: falta uma explicação de 3–4 frases sobre o que é um conector
  MCP e o que é ferramenta de leitura × escrita.
- "Conecte o Google Calendar como fez com o Drive" — passo implícito.
- "Deu certo?" mede a ferramenta ("o conector aparece na lista"), não o resultado conferido.
- Projeto Final é a soma das oficinas com dados reais, não uma missão autônoma.

### 3.2 Rigor técnico

- Não cita o limite do Free (um conector personalizado), nem que conectores Google são para todos.
- Não diz que a extensão local (Desktop) e o conector remoto (web) são mecanismos diferentes.
- Não configura `Tool permissions`; o aluno nunca vê `Needs approval` nem `Allow / Deny`.
- ChatGPT: caminho "menu de Plugins" vago; disponibilidade por plano não confirmada no material-fonte;
  algumas contas mostram "Apps".
- Parte dos Dez inclui Microsoft 365 sem dizer que exige conta corporativa Entra e consentimento de
  administrador; GitHub e Canva sem plano ou escopo verificados.

### 3.3 Segurança (risco para iniciantes)

- Envio de e-mail real (Oficina 4), convite a colega (Oficina 3, "ir além"), leitura do Drive pessoal
  inteiro (Oficina 2): três riscos graves sem nenhuma trava.
- Nada sobre LGPD, dado de terceiros, conta de trabalho.
- Nenhuma menção a prompt injection: o assistente lê e-mails de terceiros, que é exatamente o vetor.
- Nenhum passo de desconectar e revogar no provedor.

### 3.4 Engajamento

- Subtítulo promete que o assistente vai "trabalhar por você" — expectativa que o próprio material
  contradiz (aprovação humana é parte do método). Trocar por promessa concreta e honesta.

### 3.5 Potencial oculto

- Faltam: ler a ficha do conector antes de instalar, bloquear ferramentas de escrita, ver a chamada
  de ferramenta na conversa, pedir ao assistente que liste as ferramentas antes de usar, conector
  personalizado por URL (o que torna o MCP "universal").

### 3.6 Aderência ao público

- Adequado ao não programador no nível de tela; para a T6, falta só um ponteiro para o anexo técnico
  do Essentials.

## 4. Matriz de Soluções e Melhorias

| ID | Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|---|
| H1 | Oficina 1 inexecutável | Oficina 1 | Fixar OpenAI Docs MCP (`https://developers.openai.com/mcp`); passos completos até `+ > Conectores` na conversa; prompt de teste exato | Crítica |
| H2 | Envio de e-mail real | Oficina 4 | Substituir por **rascunho** com assunto "Teste MCP — excluir", endereço do próprio aluno, instrução "não envie"; conferir em Rascunhos e em Enviados | Crítica |
| H3 | Evento real e convite a terceiros | Oficina 3 | Separar: Oficina 3 = consulta somente leitura da agenda; Oficina 4 = criar e apagar evento de teste de 10 min sem convidados | Crítica |
| H4 | Drive pessoal real | Oficina 2 | Trocar por pasta `teste-mcp-arquivos` com dois `.txt` fictícios, lida pela extensão Filesystem; alternativa web: arquivo fictício no Drive | Crítica |
| H5 | Nenhum desfazer | Todas | Bloco "Desligue ao sair" no fim de cada oficina; revogação completa no Projeto Final | Crítica |
| H6 | Leitura de arquivos locais ausente | Estrutura | Oficina 2 com Filesystem (Claude Desktop), pasta única autorizada | Alta |
| H7 | ChatGPT vago | Oficina 1 | Variação condicional com caminho `Plugins > + > Add custom MCP server`, aviso Plugins/Apps, "se não aparecer, anote e siga" | Alta |
| H8 | Pré-requisitos implícitos | Antes de Arregaçar | Lista: Claude Free com vaga de conector, Desktop (SO mínimo), conta Google **pessoal**, pasta de teste, ChatGPT opcional | Alta |
| H9 | "Deu certo?" fraco | Todas | Critérios observáveis: chamada de ferramenta visível, URL oficial, resumo que bate com o arquivo, evento que aparece e depois some | Alta |
| H10 | "Se travar" genérico | Todas | Tabelas específicas: vaga do Free, 405 no navegador, conector desligado na conversa, pasta não autorizada, login pedido de novo, aprovação negada | Alta |
| H11 | Permissões nunca configuradas | Oficinas 3 e 4 | Passo explícito `Personalizar > Conectores > [conector] > Tool permissions`: leitura em Needs approval ou Always allow; escrita em Needs approval ou Blocked | Crítica |
| H12 | Parte dos Dez = lista de nomes | Parte dos Dez | Dez dicas práticas de uso seguro e eficaz (não nomes de produto) | Média |
| H13 | Projeto Final dependente e arriscado | Projeto Final | Missão autônoma: avaliar um conector do próprio perfil pela ficha, decidir, testar em modo leitura com dado fictício, uma ação reversível se aplicável, revogar | Alta |
| H14 | Tempo e desafios abaixo do prompt-mestre | Estrutura | Recalcular pela MET (alvo 90–120); três desafios em "Quer ir além?" | Média |
| H15 | Promessa exagerada | Título | Subtítulo concreto: ligar, consultar, agir com aprovação e desligar | Baixa |
| H16 | Zero teoria mínima | Antes de Arregaçar / Oficina 1 | Box 🤓 com a analogia tomada + crachá e "semáforo" leitura × escrita antes da primeira conexão | Alta |
| H17 | Prompt injection ausente | Oficina 2 | Um dos arquivos de teste contém instrução maliciosa; o aluno observa e confirma que nada foi executado | Média |

## 5. Roadmap de Expansão

| Tópico | Cabe neste curso? | Destino |
|---|---|---|
| Ficha de avaliação de conector | Sim | Projeto Final |
| Pedir ao assistente a lista de ferramentas antes de usar | Sim | Oficina 1 |
| Rascunho de e-mail sem envio | Sim | Oficina 4 |
| ChatGPT com plugin Gmail | Variação condicional | Oficina 4 (desafio) |
| Microsoft 365 corporativo | Não | *Claude Desktop - Hands On* |
| Fluxos longos (agenda + e-mail + arquivos encadeados) | Não | *MCP com ChatGPT - Hands On*, *Claude Desktop - Hands On* |
| Construir servidor próprio | Não | *Construindo Servidores MCP - Hands On* |

**Não verificado nesta auditoria:** rótulos pt-BR (exceto `Personalizar > Conectores`), tela de
pastas do Filesystem, botão de desinstalar extensão, elegibilidade do ChatGPT por plano, rótulos de
aprovação do ChatGPT. Nada foi testado em conta real.
