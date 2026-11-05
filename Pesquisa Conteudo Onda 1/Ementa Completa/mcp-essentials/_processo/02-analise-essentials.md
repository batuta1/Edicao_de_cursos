# 02 — Análise crítica 360 · MCP - Essentials (v1.0)

Entrada: `_processo/01-v1-essentials.md` + `_processo/00-contornos.md`.
Contexto: objeto base MCP (revisão 2026-07-28), ferramentas-âncora Claude e ChatGPT; público duplo
(profissionais não programadores da T3; desenvolvedores e TI da T6); pré-requisito uso básico de
Claude ou ChatGPT, sem programação; trilha Essentials; autoinstrucional; alvo 100–130 min.

## 1. Sumário Executivo

**Nota: 4 / 10.** A v1.0 acerta a definição do protocolo e o registro formal, mas é um plano que
**explica o MCP para desenvolvedores e deixa o não programador sem conseguir usá-lo**. O módulo mais
longo é sobre a arquitetura interna do protocolo; o único exercício prático não diz qual conector
ligar; a segurança chega depois da instalação; e a tarefa observável do catálogo (ler arquivos,
consultar serviços, executar ações com segurança) não aparece decomposta em lugar nenhum.

Principais constatações:

- **Segurança depois do primeiro uso.** O Módulo 3 manda instalar "um conector de interesse" e só o
  Módulo 4 fala de risco. O aluno típico vai ligar o Drive ou o e-mail do trabalho antes de saber o
  que é uma permissão.
- **Exercício do Módulo 3 não é executável:** não informa URL, conector, plano necessário nem o que
  perguntar; o critério ("aparece como instalado") mede a ferramenta, não o aluno.
- **Módulo 2 fora do público:** JSON-RPC, `initialize`, `Mcp-Session-Id`, MRTR e depreciações não
  servem a quem não programa e consomem o maior bloco de tempo.
- **ChatGPT apresentado como universal.** O conteúdo bruto registra que a disponibilidade de MCP
  personalizado por plano (Free, Go, Plus, Pro) **não foi confirmada**, e que algumas contas mostram
  "Apps" em vez de "Plugins".
- **Faltam três das quatro ações da tarefa observável:** não há leitura de arquivos (extensão
  Filesystem), não há ação reversível com aprovação, não há desconexão/revogação.
- **Permissões ausentes:** os controles reais do Claude (Always allow / Needs approval / Blocked;
  Allow / Deny) não são citados.
- Textos Descritivos abaixo do mínimo (1 a 4 parágrafos); carga declarada de 90 min, abaixo da faixa
  do prompt-mestre (100–130) e sem cálculo; não há subseção "Mão na massa".

## 2. Pontos Positivos (Fortalezas)

| Fortaleza | Por que é um acerto |
|---|---|
| Definição de MCP como protocolo, não produto | É a confusão nº 1 do público ("MCP é um app?"). A questão do Módulo 1 a testa bem. |
| Analogia USB-C | É a analogia oficial e funciona para leigos — deve virar fio condutor, completada por uma analogia que explique permissões. |
| Datas e governança corretas | 25/11/2024, 09/12/2025 e AAIF batem com o material-fonte [CONFIRMADO]. |
| Caminhos de menu do Claude e do ChatGPT corretos | `Customize > Connectors` e `Plugins > + > Add custom MCP server` são os fluxos vigentes; a v1.0 não caiu no tutorial antigo de "Developer Mode". |
| Registro formal e impessoal | Nenhum "você", nenhum humor: o tom da trilha está correto. |
| Recomendação de somente leitura e de evitar "permitir sempre" | Coincide com Anthropic, OpenAI e especificação. |

## 3. Pontos Negativos e Gargalos (Debilidades)

### 3.1 Clareza pedagógica

- **Etapa implícita no Módulo 3:** "escolher um conector de interesse" pressupõe que o aluno saiba
  avaliar conectores, tenha conta no serviço, saiba que o Free comporta só **um** conector
  personalizado e saiba onde ligar o conector na conversa. Em curso autoinstrucional, trava.
- **Sem Módulo 0:** não se verifica conta, plano, sistema operacional nem a instalação do Claude
  Desktop, que é necessária para ler arquivos locais.
- **Progressão invertida:** arquitetura detalhada (Módulo 2) antes de qualquer experiência concreta.
  Para o leigo, host/client/server só ganha sentido depois de ver uma chamada de ferramenta.
- **Critérios de êxito fracos:** "aparece como instalado" e "uma ação foi realizada" não verificam
  se o aluno **conferiu** a ação, identificou a ferramenta chamada ou desfez o teste.
- **Sem fio condutor:** a analogia USB-C é plantada no Módulo 1 e abandonada. Ela explica a
  padronização, mas não explica que cada serviço decide o que liberar — exatamente o que o módulo de
  segurança precisaria retomar.
- **Atividade integradora vaga:** "uma consulta e uma ação" em serviço profissional, sem roteiro.

### 3.2 Rigor técnico

- **ChatGPT:** a v1.0 afirma o fluxo como disponível. O material-fonte diz: tabela pública de planos
  ilegível para Plugins/MCP, Free e Go ausentes da tabela, rollout por conta. Precisa virar caminho
  condicional, com instrução do que fazer se a opção não existir.
- **Plano do Claude:** não diz que Free tem **um** conector personalizado; o aluno que já usou a vaga
  falha sem saber por quê.
- **Local × remoto ausente:** conector remoto do Claude é chamado da nuvem da Anthropic e não alcança
  `localhost`, VPN ou rede corporativa; extensão local roda na máquina e não aparece no web. Sem isso,
  o aluno não entende por que o conector "do Desktop" some no navegador.
- **Ações destrutivas:** nenhum aviso de que Drive, Gmail e Calendar podem mover para a lixeira,
  enviar e excluir; nem de que algumas ações do Microsoft 365 exigem conta corporativa Entra e nunca
  aceitam "Always allow".
- **Troubleshooting inexistente:** URL sem `/mcp`, erro 405 ao abrir o endpoint no navegador (normal),
  conector não habilitado na conversa, vaga do Free ocupada.
- **Rótulos pt-BR:** a v1.0 usa só os nomes em inglês, sem dizer quais foram confirmados em português
  (`Personalizar > Conectores` foi; os demais não).

### 3.3 Segurança e dados (risco para iniciantes)

- Segurança no Módulo 4, após o uso. Inverte a ordem obrigatória.
- Nenhuma menção a LGPD, ANPD ou Governo Digital, embora conectar e-mail e arquivos seja tratamento
  de dados pessoais.
- Prompt injection é "reconhecida" por questão de múltipla escolha, sem exemplo concreto.
- A atividade integradora manda ligar serviço do cotidiano profissional: convite direto a conectar
  conta corporativa sem autorização.
- Diretório tratado implicitamente como garantia; não ensina a ler a ficha do conector (publicador,
  selo, leitura/escrita, login, revogação).

### 3.4 Engajamento

- Tom correto, mas o curso não mostra **nenhum** ganho concreto para o profissional não programador.
  Faltam exemplos de uso (pesquisa documental, agenda, contratos) e um caso brasileiro.

### 3.5 Potencial oculto

- Ficam de fora os diferenciais que o público mais precisa: permissões por ferramenta, modos de
  aprovação, diretório unificado do Claude, distinção MCP × API × plugin × skill × Zapier/n8n,
  conectores interativos, e a ideia de que o MCP padroniza a conexão, **não** a qualidade da resposta.

### 3.6 Aderência ao público

- Módulo 2 serve à T6 (desenvolvedores) e afasta a T3. Deve virar anexo opcional.
- Encerramento recomenda Anthropic Academy como gratuita — o conteúdo bruto marca a gratuidade como
  [VERIFICAR].

## 4. Matriz de Soluções e Melhorias

| ID | Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|---|
| E1 | Segurança depois do primeiro uso | Módulos 3 e 4 | Mover segurança para o Módulo 2, antes de qualquer conexão; conectar só a partir do Módulo 3 | Crítica |
| E2 | Sem verificação de acesso | Início | Criar Módulo 0: conta Claude, plano, vaga do conector personalizado, Desktop e SO, conta Google pessoal, ChatGPT opcional | Crítica |
| E3 | Exercício de instalação inexecutável | Módulo 3 | Fixar conector OpenAI Docs MCP (`https://developers.openai.com/mcp`, público, somente leitura, sem login); passos completos; critério: chamada visível + URL oficial + nenhuma escrita | Crítica |
| E4 | Arquitetura técnica para não programador | Módulo 2 | Reduzir a host/client/server, tools/resources/prompts e local/remoto em linguagem leiga no Módulo 1; mover versão, transporte, JSON-RPC e Inspector para Anexo técnico opcional | Alta |
| E5 | ChatGPT como universal | Módulo 3 | Caminho condicional: "se a conta exibir `Plugins > + > Add custom MCP server`"; nomenclatura Plugins/Apps; instrução "registrar indisponível e seguir no Claude" | Alta |
| E6 | Plano e limite do Free omitidos | Módulos 0 e 3 | Citar: Free = um conector personalizado; conectores Google e extensões para todos; nenhum exercício exige pagamento | Alta |
| E7 | Tarefa observável não decomposta | Curso todo | Um módulo por ação: consultar (M3), ler arquivos (M4), executar ação reversível (M5), com desfazer e revogação em cada um | Crítica |
| E8 | Permissões e aprovações ausentes | Módulo 4 | Ensinar `Tool permissions` (Always allow / Needs approval / Blocked) e Allow / Deny no Módulo 2 e aplicá-las nos Módulos 4 e 5 | Crítica |
| E9 | Dados reais na atividade integradora | Módulo 5 | Substituir por cenário fictício e plano de conexão no papel + execução só com conta pessoal e dados de teste | Crítica |
| E10 | Local × remoto ausente | Módulo 2 | Explicar no Módulo 1 e retomar no Módulo 4 (Filesystem local × Drive remoto) | Alta |
| E11 | Diretório como garantia | Módulo 3 | Ficha de avaliação do conector (publicador, selo, leitura/escrita, login, privacidade, revogação) no Módulo 2; aplicá-la no Módulo 6 | Alta |
| E12 | MCP confundido com plugin/API/automação | Módulo 1 | Tabela comparativa MCP × API × plugin × skill × Zapier/n8n no Módulo 1 | Média |
| E13 | Textos curtos | Módulos 3, 4, 5 | Textos com 4–5 parágrafos | Média |
| E14 | Sem fio condutor | Curso todo | Plantar no Módulo 1 a dupla **tomada USB-C + crachá** (o padrão liga; o crachá define o que abre) e retomá-la nos Módulos 2, 4, 5 e 6 | Média |
| E15 | Carga horária sem base; sem "Mão na massa" | Estrutura | Recalcular pela MET; alvo 100–130 min; prompt-base editável por módulo | Média |
| E16 | Sem solução de problemas | Módulos 3–5 | Tabelas de Solução de Problemas: URL `/mcp`, 405 no navegador, conector desligado na conversa, vaga do Free, pasta não autorizada, aprovação negada | Alta |
| E17 | Sem LGPD nem prompt injection concreta | Módulo 4 | Princípios de finalidade e necessidade (LGPD), orientação do Governo Digital sobre dados fictícios; exercício com arquivo fictício contendo instrução maliciosa | Alta |
| E18 | Recomendação não verificada | Encerramento | Citar cursos externos sem afirmar gratuidade; apontar os cursos seguintes da trilha | Baixa |

## 5. Roadmap de Expansão

| Tópico | Cabe neste curso? | Destino |
|---|---|---|
| Ficha de avaliação de conector e permissões por ferramenta | Sim | Módulo 2 e Módulo 6 |
| Leitura de arquivos locais (Filesystem) × nuvem (Drive) | Sim | Módulo 4 |
| Ação reversível com aprovação manual e desfazer | Sim | Módulo 5 |
| Prompt injection simulada com arquivo fictício | Sim, em versão curta | Módulo 4 (pílula) |
| Exemplos brasileiros (Senior, Econodata) | Sim, como ilustração | Módulo 1 |
| Conectores interativos (Canva, Figma, Asana) | Só citação | Módulo 1 |
| Versão do protocolo, transporte, Inspector | Não no corpo | Anexo técnico opcional (T6) |
| Microsoft 365 corporativo (Entra, consentimento de admin) | Só citação | Módulo 4; prática fica para *Claude Desktop - Hands On* |
| Construir servidor; análise aprofundada de riscos; fluxos longos | Não | *Construindo Servidores MCP*, *Segurança em MCP*, *MCP com ChatGPT* |

**Não verificado nesta auditoria:** rótulos pt-BR da interface (só `Personalizar > Conectores` está
confirmado), elegibilidade do ChatGPT por plano, tela de escolha de pastas do Filesystem e
comportamento atual do OpenAI Docs MCP em conta brasileira. Nada foi testado em conta real.
