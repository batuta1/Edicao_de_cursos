# Integração do compilado — ChatGPT no PowerPoint

Documento da revisão de 7 de outubro de 2026. Registra a integração do novo material-fonte
`../compilado-chatgpt-powerpoint.txt` ao curso já construído, **sem descartar** o que as Fases 0 a 7
produziram.

## 1. Método adaptado

A skill `criar-ementa-curso` foi aplicada em modo de revisão, e não de criação. O curso existente é
tratado como a "versão 1.0" desta rodada, e o compilado como material-fonte novo.

| Fase da skill | O que se fez nesta rodada |
|---|---|
| 0 — Contornos | Mantidos objeto base, público, pré-requisitos, natureza e carga horária alvo. Atualizado apenas o material-fonte e a lista de pendências (seção acrescentada ao fim de `00-contornos.md`). |
| 1 — Versão 1.0 | **Não refeita.** Os arquivos `01-v1-*.md` permanecem como rastro histórico. O ponto de partida desta rodada são os roteiros finais vigentes. |
| 2 — Auditoria | Refeita em forma de **auditoria de integração**: cada tema do compilado foi confrontado com o que os roteiros já dizem (seções 2 a 4 deste arquivo). As análises `02-analise-*.md` continuam válidas e não foram alteradas. |
| 3 — Roteiro final | Matriz de integração aplicada aos dois roteiros finais. |
| 4 — Carga horária | Recalculada. Essentials ganhou uma atividade; Hands-on manteve as atividades. |
| 5 — Ementa | Reescrita a partir dos roteiros e da carga horária revisados. |
| 6 — Marcos | Checklist reaplicado (seção 7). |
| 7 — Articulate | Os dois roteiros Articulate receberam as mesmas mudanças, com breadcrumbs e cues. |

## 2. Comparação das fontes

As duas fontes descrevem **o mesmo artigo** da Central de Ajuda da OpenAI. A fonte antiga
(`../../ConteudoBruto/ConteudoBrutoPowerPointCHATGPT_OpenAI.txt`) é uma tradução quase literal; o
compilado é uma síntese em palavras próprias, datada, reorganizada em quinze seções e com a
terminologia de interface em inglês preservada.

| Tema | Fonte antiga | Compilado (07/10/2026) | Situação no curso antes desta rodada |
|---|---|---|---|
| O que é, para quem | Criar, editar, entender, refinar | Idem, mais "melhorar clareza, concisão e acabamento" e "reduzir um material longo" | Criar, editar e entender bem cobertos; **refinar só aparece como linha de tabela na Essentials** |
| Instalação | `Página Inicial > Suplementos` | Idem, com os rótulos em inglês `Home` e `Add-ins` | Só rótulos em português, marcados como pendência |
| Acesso efetivo | Implícito | **Explícito**: aparecer na loja não garante uso; depende de plano, regras do espaço de trabalho, **liberação gradual** e configurações administrativas | Teste de permissão cobre só a loja da Microsoft |
| Implantação por administrador | Rótulos em português | Rótulos em inglês: `Integrated apps > Deploy Add-in > Upload custom apps` | Rótulos em português apenas |
| Habilitação no espaço de trabalho ChatGPT | "Os administradores podem habilitar o ChatGPT para PowerPoint nas configurações do workspace" | Idem, seção própria de controles para administradores | **Ausente.** O curso só fala do administrador do Microsoft 365 |
| Como pedir bem | Três elementos (alterar, preservar, onde) + usar material de origem | **Seis itens**: alterar, preservar, onde, público, fontes, estilo visual ou estrutura a preservar | Três elementos na edição, quatro na criação; a lista unificada não aparece |
| Revisão humana | Afirmações, números, citações, alterações em slides | **Seis pontos**: afirmações factuais, números, citações, **mudanças de sentido na reescrita**, slides removidos/deslocados/alterados, aderência ao modelo visual | Números, citações, vizinhos e tema cobertos; **mudança de sentido e slides deslocados não nomeados** |
| Limitações | Três | Três, mesma substância | Cobertas |
| Plugins, Skills, apps | Plugin agrupa Skills, apps e outros recursos | Idem; "modelos de apresentação" listados entre os recursos de repetição | Skills e apps cobertos; **plugin e modelos não nomeados** |
| Dados processados | Prompt, conteúdo da apresentação, anexos, contexto conectado | Idem, mais a recomendação de confirmar políticas internas (confidencialidade, permissões de apps, retenção, conformidade, compartilhamento) | "Processamento da OpenAI" genérico; **o que é processado não é enumerado** |
| Preços | 10–50 créditos/mensagem com GPT-5.5; tarifas iguais às do Excel/Sheets | Idem, **com data de consulta** | Sem data; sem a relação com o suplemento do Excel |
| SSO | Administrador global; `Portal de administração da OpenAI > Identidade > SSO > Gerenciar SSO` | Idem; registra que a pergunta cita o Excel nominalmente | "Administrador atualiza o endereço de retorno" — **sem o perfil exato nem o caminho** |
| Conclusão | — | Quatro pilares do bom uso: instruções específicas, fontes confiáveis, preservação explícita, revisão humana | Os quatro estão no curso, dispersos; **não há fórmula de síntese** |

## 3. Auditoria do curso vigente contra o compilado

### 3.1 O que se mantém, e por quê

- **Módulo 0 / Oficina 0 como portão de decisão.** O compilado reforça a decisão: dedica três seções
  (9, 11 e 12) a disponibilidade, administração e dados. O curso já estava certo em pôr isso antes
  da instalação.
- **Saída para o curso irmão quando a instalação é negada.** Nada no compilado contradiz.
- **Tema institucional como procedimento.** A limitação 7.1 do compilado é a mesma da fonte antiga.
- **Plano prévio e delimitação de escopo.** Idênticos nas duas fontes.
- **Consulta à narrativa, lacunas e perguntas prováveis.** Mantida; o compilado só funde narrativa e
  lacunas em um exemplo.
- **Projeto Final de duas versões.** Já exercita refinar e verificar; ganha apenas critério novo.

### 3.2 Gargalos revelados pelo compilado

1. **Uma camada de administração inteira está ausente.** Para o público deste curso, que usa conta
   institucional (Edu ou Enterprise), o suplemento pode estar instalado e ainda assim não funcionar,
   porque o recurso não foi habilitado no espaço de trabalho do ChatGPT. O curso manda o docente ao
   administrador do Microsoft 365, que não tem como resolver. É o gargalo de maior impacto prático
   desta rodada.
2. **O teste de permissão tem um quarto desfecho que o curso não prevê**: a loja funciona, o
   suplemento instala, mas a conta não tem acesso (plano, espaço de trabalho ou liberação gradual).
   Hoje esse caso aparece só como "conta errada" no troubleshooting.
3. **Refinar não é ensinado na trilha Essentials.** É uma das quatro operações anunciadas e figura no
   ciclo do Módulo 5, mas nenhum módulo a desenvolve. O participante é avaliado em algo que não
   estudou.
4. **A revisão é incompleta no ponto mais perigoso para o público.** A reescrita para outro público
   ou para menos slides é exatamente onde o sentido de uma afirmação muda sem que nenhum número mude.
   O curso confere números, mas não sentido.
5. **A lista unificada do que declarar não aparece.** O participante aprende quatro elementos em um
   módulo e três em outro, sem saber que são partes de uma lista só do fabricante.
6. **O que a OpenAI processa não está enumerado.** "Processamento da OpenAI" é vago para quem precisa
   decidir o que submeter; anexos e contexto conectado também entram, não só os slides.
7. **O troubleshooting de SSO não serve para encaminhar o pedido.** Sem o perfil exato
   (administrador global) e o caminho no portal, a mensagem do docente à TI fica imprecisa.
8. **Rótulos de interface só em português**, quando a fonte agora dá os rótulos em inglês — útil para
   quem usa o Office em inglês, comum em universidades.
9. **Informação de preço sem data.** O compilado permite datar ("conforme consulta de 7 de outubro de
   2026"), o que é mais honesto do que "sujeito a alteração" sem referência.
10. **Plugins e modelos de apresentação não nomeados** no módulo de fluxos repetidos.

### 3.3 Não verificável com o compilado

- Os rótulos em português da interface continuam não confirmados; o compilado dá apenas os ingleses.
- A pergunta sobre SSO cita nominalmente o suplemento do Excel. Não é possível confirmar, só com a
  fonte, que o erro ocorre do mesmo modo no PowerPoint.
- A versão mínima do PowerPoint continua ausente.
- Os nomes exatos das Skills disponíveis continuam desconhecidos.

## 4. Matriz de integração

| # | Achado | Onde | Correção concreta | Trilha | Prioridade | Destino |
|---|---|---|---|---|---|---|
| I1 | Camada de administração do espaço de trabalho ChatGPT ausente | Módulo 0 / Oficina 0; Módulo 1 / Oficina 1 | Nomear as **duas administrações**: quem administra o Microsoft 365 (instala o suplemento) e quem administra o espaço de trabalho do ChatGPT (habilita o recurso e os apps). Incluir no troubleshooting e no modelo de pedido. | Ambas | Crítica | Corrigido — Módulo 0 (tabela de desfechos e nota), Módulo 1 (seção de implantação e troubleshooting), Oficinas 0 e 1; modelo de mensagem no Articulate Essentials |
| I2 | Quarto desfecho do teste de permissão | Módulo 0 / Oficina 0 | Acrescentar à tabela de desfechos: "instala, mas a conta não tem acesso" → verificar plano, pedir habilitação no espaço de trabalho, considerar liberação gradual. | Ambas | Alta | Corrigido — linha nova nas duas tabelas de desfecho |
| I3 | Refinar não ensinado na Essentials | Módulo 3 | Nova subseção "Refinar e revisar o que mudou" (Exemplo Aplicado, 6 min): condensar, trocar de público, melhorar acabamento — com exemplos de instrução. | Essentials | Alta | Corrigido — Módulo 3 ganha atividade; objetivo e habilidade atualizados |
| I4 | Revisão sem conferência de sentido | Módulos 3 e 5; Oficina 4; Projeto Final; Parte dos Dez | Adotar a **revisão em seis pontos** do fabricante, com destaque para a mudança de sentido na reescrita. | Ambas | Alta | Corrigido — tabela no Módulo 3; ciclo e critérios do Módulo 5; passo 6 da Oficina 4; item novo na checklist do Projeto Final; item 10 da Parte dos Dez |
| I5 | Lista unificada do que declarar ausente | Módulo 3 | Tabela "as seis informações que o fabricante recomenda declarar", mostrando que a instrução de criação (Módulo 2) e a de edição (Módulo 3) são recortes dela. Manter os nomes "quatro elementos" e "três elementos". | Essentials | Média | Corrigido — Módulo 3 |
| I6 | Dados processados não enumerados | Módulo 0 / Oficina 0 | Enumerar: a instrução digitada, o conteúdo da apresentação disponibilizado, os anexos e o contexto de conexões autorizadas; o tratamento segue o plano e o espaço de trabalho. Acrescentar as políticas internas a confirmar. | Ambas | Alta | Corrigido — "Quem lê o seu arquivo" e passo 1 da Oficina 0 |
| I7 | SSO impreciso | Módulo 1 / Oficina 1 | Nomear o administrador global e o caminho `Portal de administração da OpenAI > Identidade > SSO > Gerenciar SSO`; registrar que a fonte cita o Excel. | Ambas | Média | Corrigido — troubleshooting; pendência atualizada |
| I8 | Rótulos só em português | Todos os breadcrumbs de instalação | Acrescentar o rótulo em inglês entre parênteses na primeira ocorrência de cada caminho de instalação e de implantação. | Ambas | Média | Corrigido — Módulos 0 e 1, Oficinas 0 e 1 |
| I9 | Preço sem data | Módulo 0 / Oficina 0 | Datar a informação e registrar que a tarifa é a mesma do ChatGPT para Excel/Sheets e que a cota é compartilhada entre os recursos de agente. | Ambas | Média | Corrigido |
| I10 | Plugins e modelos não nomeados | Módulo 4 | Um parágrafo: plugin como pacote de Skills, apps e outros recursos; modelos de apresentação como terceiro mecanismo de repetição. | Essentials | Baixa | Corrigido |
| I11 | Sem fórmula de síntese | Módulo 5; Encerramento; "Conseguiu! E agora?" | Adotar os quatro pilares do compilado: instrução específica, fonte confiável, preservação explícita, revisão humana. | Ambas | Baixa | Corrigido |

### Decisões declaradas

- **Não se criou oficina nova na Hands-on.** As mudanças entram em passos existentes; a trilha
  continua com 113 min. Criar uma oficina de refinamento duplicaria a Oficina 4, que já é isso.
- **Não se renomearam os "quatro elementos" da criação nem os "três elementos" da edição.** São
  fórmulas já fixadas nos dois roteiros, nos dois Articulate e na ementa. A lista de seis entra como
  mapa que as reúne, não como substituição.
- **Administração do Microsoft 365, conformidade e residência de dados continuam fora do escopo**,
  conforme o Roadmap de `02-analise-essentials.md`. O curso apenas diz ao docente **a quem** pedir e
  **o quê**.
- **A trilha Essentials passa a ocupar o teto da carga horária alvo (130 min).** A folga de 6 min
  apontada em `carga-horaria-essentials.md` foi usada no Módulo 3, e não no Módulo 5 como lá se
  sugeria: o refinamento é lacuna de conteúdo; a conferência cruzada era melhoria opcional.

## 5. O que não mudou

Objeto base, público-alvo, pré-requisitos, natureza autoinstrucional, estrutura de módulos e
oficinas, os três fatos centrais de `00-contornos.md`, a saída para o curso irmão, o Projeto Final, a
tabela MET e as regras de contagem.

## 6. Impacto na carga horária

| Trilha | Antes | Depois | Mudança |
|---|---|---|---|
| Essentials | 124 min, 17 atividades, 37,9 % teoria | 130 min, 18 atividades, 40,8 % teoria | +1 Exemplo Aplicado (6 min) no Módulo 3 |
| Hands-on | 113 min, 17 atividades, 26,5 % teoria | 113 min, 17 atividades, 26,5 % teoria | Nenhuma atividade nova |
| Total | 237 min | 243 min | +6 min |

## 7. Marcos reaplicados

| Marco | Situação |
|---|---|
| 1 — Contornos | Verde. Material-fonte atualizado; nenhum campo "a definir". |
| 3 — Diagnóstico | Verde. Este arquivo cobre clareza (I3, I5), rigor técnico (I1, I2, I6, I7, I8, I9), engajamento (I11) e potencial (I10); declara o não verificável. |
| 4 — Roteiros | Verde. Todo achado de I1 a I11 tem destino visível. |
| 5 — Carga horária | Verde. Recalculada; Essentials no teto, sem estouro. |
| 6 — Ementa | Verde. Reescrita depois dos roteiros e da carga. |
| 7 — Pasta | Verde. README atualizado; pendências revistas. |
| 8 — Articulate | Verde. Mesmas mudanças, com cues e breadcrumbs; nenhuma "captura de tela". |
