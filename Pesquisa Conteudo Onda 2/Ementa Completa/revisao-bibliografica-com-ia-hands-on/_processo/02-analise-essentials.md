# 02 — Análise crítica 360 da v1.0 (Essentials)

Contexto: objeto base *Revisão bibliográfica assistida por IA* (Elicit, Consensus, Semantic
Scholar); público T2 (estudantes, pesquisadores, jornalistas, analistas), posição 5 de 5;
pré-requisito: uso básico de assistente de IA; trilha Essentials; autoinstrucional; plano gratuito.
Fonte de verificação: `00-contornos.md` e conteúdo bruto de 04/11/2026.

## 1. Sumário Executivo

**Nota: 4/10.** A v1.0 tem a espinha certa (conceito → busca → extração → síntese) e um bom
exercício no Módulo 1, mas falha na própria tarefa observável do catálogo e contém dois erros
técnicos que travariam o aluno.

- **Erro técnico crítico:** o Módulo 2 manda usar AND/OR no Semantic Scholar, que não suporta
  operadores booleanos nem curingas (FAQ oficial).
- **Exercício inexecutável no plano gratuito:** o Módulo 3 exige Systematic Review (Pro, US$ 39/mês)
  e exportação CSV (Plus). O curso é desenhado para conta gratuita.
- **Duas etapas da tarefa observável faltam:** triagem (com critérios e motivos) e rastreabilidade
  (log de busca, PRISMA preenchido). Sem elas o curso não entrega "revisão com rastreabilidade".
- **Segurança e declaração de IA** aparecem numa frase no Módulo 4 — depois do primeiro upload.
- **Ferramentas tratadas como confiáveis:** supporting quote e Consensus Meter apresentados sem os
  limites que a própria documentação e os estudos independentes registram.

## 2. Pontos Positivos (Fortalezas)

- **Sequência das etapas** segue a lógica real de uma revisão; o aluno vê o mapa antes do detalhe.
- **Quatro tipos de revisão** com definições corretas e curtas — base suficiente para iniciante.
- **Exercício do Módulo 1** (escolher a revisão de escopo para mapear lacunas) é objetivo, tem
  gabarito e testa compreensão, não memória.
- **Papéis complementares das ferramentas** (descoberta, panorama, extração) aparecem na síntese —
  é o diferencial correto e deve virar fio condutor.
- **Encerramento** com responsabilidade humana está alinhado ao CNPq.

## 3. Pontos Negativos e Gargalos (Debilidades)

**Clareza pedagógica**
- Não há Módulo 0: o aluno chega ao Módulo 2 sem saber que precisa de três contas, quais são
  gratuitas e o que cada plano libera.
- A pergunta de pesquisa é tratada como "escolher um tema". Faltam PICO/PICo/PCC, critérios de
  inclusão/exclusão definidos antes da busca e descritores DeCS/MeSH.
- Triagem desaparece entre busca e extração; deduplicação também.
- Textos descritivos têm 1 a 3 parágrafos (o modelo pede 3 a 5) e o Módulo 5 tem objetivo único.
- Critérios de êxito fracos: "obter resultados nas duas ferramentas" e "cinco frases com
  referência" não verificam nada que importe.

**Rigor técnico**
- Boolean no Semantic Scholar (erro factual).
- Systematic Review e CSV do Elicit fora do plano gratuito; o v1 também ignora que, sem PDF, o
  Elicit extrai só do resumo.
- Não menciona que Find Papers, Extract Data e Chat with Papers foram fundidos no Research Agent
  em 30/09/2026 — o aluno que procurar vídeo vai ver telas que não existem.
- Consensus Meter descrito como "grau de concordância", sem dizer que só vale para perguntas
  sim/não, pode não aparecer e não é medida de certeza; tipo de estudo automático não é qualidade.
- PRISMA chamado de "principal referência" sem distinguir relato de método.

**Segurança e dados**
- Nenhuma palavra sobre onde os dados são processados (Elicit: EUA, AWS, provedores de modelo;
  Consensus: OpenAI, Anthropic, Google, Baseten), sobre manuscrito inédito ou sobre a orientação
  da UFRB. Declaração de IA citada sem modelo e sem o que o CNPq exige (ferramenta e finalidade).

**Engajamento**
- Registro formal está correto. Mas o curso não tem caso-guia: cada módulo usa um exemplo solto, e
  o aluno não vê a revisão crescer.

**Potencial oculto**
- Ficam de fora: Has PDF e supporting quote como trilha de auditoria; filtros do Consensus por
  desenho, país e ano; Library e exportação BibTeX do Semantic Scholar; Zotero para deduplicar;
  bases brasileiras; evidência independente sobre a precisão (51,40%; 82%; 77%/10%).

**Aderência ao público**
- Exigir conta paga contradiz o público (estudantes). Nenhum módulo é avançado demais, mas o
  Systematic Review como exercício é.

## 4. Matriz de Soluções e Melhorias

| # | Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|---|
| E1 | Sem pré-requisitos e planos | Antes do Módulo 1 | Criar Módulo 0 com tabela de planos gratuitos, criação de contas e planilha de quatro abas | Alta |
| E2 | Boolean no Semantic Scholar | Módulo 2 | Substituir por: consultas curtas sem Boolean, frase exata entre aspas, uma consulta por sinônimo, todas registradas; Boolean só em BVS/SciELO | Alta |
| E3 | Systematic Review/CSV no gratuito | Módulo 3 | Trocar por Research Agent com "Add a column" e conferência manual em planilha; Systematic Review como texto descritivo e caminho opcional | Alta |
| E4 | Segurança tardia | Módulo 4 | Criar Módulo 2 "Responsabilidade, dados e declaração de uso de IA" antes de qualquer busca, com cenários e modelo de declaração CNPq | Alta |
| E5 | Pergunta sem framework e critérios | Módulo 2 | Novo módulo "Pergunta, critérios e termos" com PICO/PICo/PCC, critérios antes da busca e DeCS | Alta |
| E6 | Triagem e deduplicação ausentes | Entre busca e extração | Incluir triagem (título/resumo → texto completo, motivo de exclusão, "incerto") no módulo de triagem e extração | Alta |
| E7 | Supporting quote como garantia | Módulo 3 | Apresentar como pista de auditoria; citar Meliante et al. 2025 e estudo de 2026 com amostra e data | Alta |
| E8 | Consensus Meter e tipo de estudo sem limites | Módulo 2 | Box sobre Meter (sim/não, não é certeza) e "tipo ≠ qualidade" | Média |
| E9 | PRISMA ambíguo | Módulos 1 e 4 | Definir PRISMA como diretriz de relato; mostrar as caixas do fluxograma pt-BR | Média |
| E10 | Sem log de busca | Todo o curso | Fio condutor: planilha com abas Log, Triagem, Extração, Síntese, plantada no Módulo 0 e preenchida em cada módulo | Alta |
| E11 | Sem bases brasileiras | Módulo 2 | Incluir SciELO, BVS/LILACS, BDTD, CAPES e Google Acadêmico como complemento obrigatório de cobertura | Média |
| E12 | Fusão de 30/09/2026 no Elicit omitida | Módulo 3 | Nota sobre telas antigas e Notebooks [conferir] | Média |
| E13 | Textos curtos, objetivos insuficientes | Todos | 3–5 parágrafos e 3–4 objetivos mensuráveis por módulo | Média |
| E14 | Carga de 90 min fora do prompt-mestre | Estrutura | Recalcular para 100–130 min com MET | Média |
| E15 | Critérios de êxito fracos | Módulos 2 e 4 | Critério com evidência verificável: contagem registrada, célula com página/trecho, frase com trecho | Alta |
| E16 | Sem caso-guia | Todo o curso | Caso fixo "telessaúde e hipertensão na atenção primária brasileira" do Módulo 0 à síntese | Média |

## 5. Roadmap de Expansão

**Cabe neste curso:** filtros do Consensus (desenho, país, ano) e Study Snapshot; Library e
exportação BibTeX do Semantic Scholar; Zotero (File > Import) para deduplicar; Research Feeds como
alerta; leitura crítica de "contagem ≠ relevância".

**Fica para curso seguinte ou anexo:** Systematic Review completo do Elicit (Pro), Routines,
Consensus Deep além de uma demonstração, avaliação de risco de viés e GRADE, meta-análise, protocolo
PROSPERO, ResearchRabbit e Connected Papers (redes visuais), APIs.

**Não verificado:** menus e rótulos em conta autenticada (o conteúdo bruto testou só Semantic
Scholar e uma busca pública do Consensus); cota Free do Consensus (10 ou 15); se exportação RIS/BIB
do Elicit está no Basic.
