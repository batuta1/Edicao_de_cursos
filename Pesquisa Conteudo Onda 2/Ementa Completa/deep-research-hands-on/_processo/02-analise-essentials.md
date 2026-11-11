# 02 — Análise crítica 360 da v1.0 (Essentials)

Contexto: objeto base *Deep research com auditoria do relatório* (ChatGPT, Gemini, Perplexity);
público T2 (posição 3) e J2 (posição 5); pré-requisito: Perplexity ou NotebookLM Essentials;
trilha Essentials; autoinstrucional; plano gratuito. Fonte de verificação: `00-contornos.md` e
conteúdo bruto de 04/11/2026.

## 1. Sumário Executivo

**Nota: 3,5/10.** A v1.0 descreve a ferramenta e esquece metade da tarefa observável: "auditar
fontes, lacunas e erros" vira um exercício de cinco minutos para ver se três links abrem. Pior, ela
ensina como atual o que a documentação de 2026 já desmentiu e tira conclusão de compra de benchmark
com conflito de interesse.

- **Dados desatualizados apresentados como atuais:** "usa o modelo o3" (a ajuda de 2026 fala em
  "latest models"); "cinco pesquisas por mês no gratuito" (número de 2025; hoje o saldo só aparece
  no produto).
- **Erro de exportação:** Google Docs não é formato direto do ChatGPT (só Markdown, Word, PDF); só o
  Gemini exporta para Docs.
- **Benchmark como veredito:** "recomenda-se a Perplexity" com base no DRACO, cujos autores são
  ligados à Perplexity; BrowseComp é da OpenAI e teve treino específico. O módulo ensina o contrário
  do que deveria.
- **Exercício inexecutável:** "executar nas três ferramentas" no plano gratuito — a Perplexity dá
  uma pesquisa por mês e o Gemini/ChatGPT não garantem saldo no mesmo dia.
- **Segurança numa frase, no Módulo 4,** depois do primeiro uso; nada sobre treino por padrão,
  Keep Activity, conectores Gmail/Drive.
- **Auditoria rasa:** "verificar se as fontes existem" — mas o problema central é fonte que existe
  e não sustenta a frase.

## 2. Pontos Positivos (Fortalezas)

- **Definição de deep research** correta e enxuta (tarefa ampla, buscas sucessivas, muitas fontes,
  relatório) — base do Módulo 1.
- **Linha do tempo** (Gemini 11/12/2024; ChatGPT 02/02/2025; Perplexity 14/02/2025) confirmada.
- **Questão do Módulo 1** (fato rápido × panorama com dados oficiais) é boa e deve ser ampliada.
- **Plano editável do Gemini** mencionado — é diferencial real.
- **SIFT** citado: é o método certo, só falta aplicá-lo.

## 3. Pontos Negativos e Gargalos (Debilidades)

**Clareza pedagógica**
- Sem Módulo 0: o aluno não sabe que precisa de uma ferramenta com saldo nem como ver o saldo.
- Brief não é ensinado: "escolher um tema" é exatamente o pedido vago que gera relatório raso.
- O plano do agente aparece só no Gemini; o ChatGPT também propõe plano editável e faz perguntas de
  esclarecimento.
- Textos descritivos de 1–2 parágrafos; Módulos 3–5 com objetivo único.
- Critérios de êxito fracos ("três relatórios exportados", "três fontes verificadas").

**Rigor técnico**
- o3 como modelo atual; 5/mês como cota atual; Docs como exportação do ChatGPT.
- Sem distinção entre Deep Research e "Create files and apps" (antigo Labs) na Perplexity.
- Nada sobre restrição de sites (Sites > Manage sites, só documentada no ChatGPT) nem sobre o fato
  de a Perplexity não garantir restrição exclusiva por domínio.
- "5 a 30 minutos" é do lançamento de 2025; a ajuda atual evita prometer tempo.

**Segurança e dados**
- ChatGPT pessoal usa conversas para treino por padrão (opt-out em Data Controls); Gemini com Keep
  Activity pode usar prompts e uploads para treino com revisão humana; conectores Gmail/Drive
  ampliam a superfície de dados; LGPD e sigilo profissional (público J2) ausentes; prompt injection
  (System Card) ausente.

**Engajamento**
- Registro formal correto; mas a síntese final ("transforma horas em minutos") é promessa de
  marketing e contradiz a responsabilidade humana.

**Potencial oculto**
- Ficam de fora: perguntas de esclarecimento, edição de plano e interrupção com novo foco no
  ChatGPT; desmarcar Google Search no Gemini para pesquisar só nos próprios arquivos; Audio Overview;
  "Sources used" e activity history; auditoria afirmação–fonte–trecho; contagem de famílias de
  evidência (fontes que repetem a mesma matéria); vigência de norma para o público J2.

**Aderência ao público**
- Nenhum caso jurídico, embora o curso feche a trilha J2. Nenhum gabarito com fonte primária
  brasileira.

## 4. Matriz de Soluções e Melhorias

| # | Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|---|
| E1 | Sem pré-requisitos e saldo | Antes do Módulo 1 | Módulo 0: contas, onde ver o saldo em cada ferramenta, rota sem cota (relatório MIT), planilha de auditoria | Alta |
| E2 | o3 e 5/mês como atuais | Módulos 1 e 2 | Substituir por "modelos mudam; a ajuda de 2026 diz 'latest models'" e "o saldo aparece no produto"; números de 2025 só como histórico | Alta |
| E3 | Docs como exportação do ChatGPT | Módulo 2 | ChatGPT: Markdown, Word, PDF (Docs indireto); Gemini: Export to Docs; Perplexity: testar [conferir] | Alta |
| E4 | Benchmark como veredito | Módulo 3 | Reescrever como leitura crítica: quem fez, o que mede, conflito de interesse; questão com gabarito "nenhum é comparação neutra"; escolha por tarefa | Alta |
| E5 | Exercício nas três ferramentas | Módulo 2 | Uma execução em uma ferramenta com saldo; comparação vira opcional | Alta |
| E6 | Segurança tardia | Módulo 4 | Módulo 2 próprio, antes do primeiro uso: configurações de treino de cada ferramenta, conectores, LGPD, sigilo, prompt injection | Alta |
| E7 | Brief não ensinado | Módulo 2 | Módulo "Brief e plano" com os seis componentes, prompt-base e edição do plano no ChatGPT e no Gemini | Alta |
| E8 | Auditoria rasa | Módulo 4 | Módulo de auditoria: afirmações numeradas, suporte integral/parcial/ausente/inacessível, fonte primária, data, famílias de evidência, lacunas; gabarito IBGE | Alta |
| E9 | Sem caso jurídico | Todo o curso | Caso LGPD/ANPD (Resolução 15/2024) com gabarito por artigo; restrição de sites a planalto.gov.br e gov.br/anpd | Alta |
| E10 | Deep Research × Create files and apps | Módulo 2 | Nota de distinção; idem Gemini app × Deep Research Max (API) | Média |
| E11 | Restrição de domínio | Módulo 3 novo | Explicar Sites > Manage sites (restrict/prioritize) no ChatGPT e a ausência de garantia na Perplexity | Média |
| E12 | Promessa de tempo | Módulos 1 e 5 | "5–30 min" como referência histórica; Encerramento sem promessa de "horas em minutos" | Média |
| E13 | Textos e objetivos insuficientes | Todos | 3–5 parágrafos e 3–4 objetivos por módulo | Média |
| E14 | Carga de 80 min | Estrutura | Recalcular para 100–130 min pela MET | Média |
| E15 | Critérios fracos | Módulos 2, 4 e 5 | Critérios com gabarito numérico (IBGE, ANPD) e tabela de seis critérios na síntese | Alta |

## 5. Roadmap de Expansão

**Cabe neste curso:** perguntas de esclarecimento e interrupção com novo foco (ChatGPT); Search
desligado e fontes próprias (Gemini); Audio Overview como desafio; leitura de DeepResearch Bench
(precisão × volume de citações); famílias de evidência; prompt de auditoria.

**Fica para curso seguinte:** conectores corporativos (SharePoint, Drive empresarial) e MCP;
Deep Research Max (API); avaliação interna com três execuções e rubrica (apêndice); Create files and
apps; pesquisa de jurisprudência (curso jurídico próprio).

**Não verificado:** rótulos pt-BR dos botões; formatos de exportação da Perplexity; local exato do
contador de saldo do ChatGPT e do Gemini; se o plano gratuito da Perplexity tem opt-out de treino.
