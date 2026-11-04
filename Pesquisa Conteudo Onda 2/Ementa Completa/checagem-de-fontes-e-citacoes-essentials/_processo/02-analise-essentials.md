# 02 — Análise crítica 360: Essentials v1.0

Objeto base: checagem de fontes e citações com apoio de IA (Scite e Perplexity). Público: T2
(estudantes, pesquisadores, jornalistas, analistas) e J2 (advogados, assessores, estudantes e
professores de Direito). Trilha: Essentials. Entrada: `01-v1-essentials.md` + `00-contornos.md`.

## 1. Sumário Executivo

**Nota: 4/10.** A v1.0 acerta o esqueleto (problema → existência → fidelidade → apoio) e escolhe
bons pares de exercício, mas é rasa onde o curso precisa ser rigoroso e pressupõe acesso que o
público não tem.

- Exige "contas na Scite e na Perplexity" sem dizer que a Scite é paga (teste de sete dias com
  cartão e renovação automática) e que não há convênio CAPES. O Módulo 4 fica inexecutável para a
  maioria.
- Falta a terceira camada como conceito: **estado da evidência** (retratação, correção) não aparece;
  o par retratado (DOI 10.5380/rinc.v9i1.83825) foi esquecido.
- O público jurídico (J2) é citado na identificação e abandonado: nenhum exercício em base oficial
  (SCON, Planalto).
- Nenhuma palavra sobre o que **não** enviar a Perplexity e Scite (manuscrito sigiloso, peça sob
  segredo de justiça, dado de cliente) — e o Módulo 4 manda fazer upload de PDF.
- Números citados de forma vaga ("uma parcela relevante") quando o material-fonte tem os dados
  exatos, com amostra e data. O alerta "não misturar porcentagens" sumiu.
- Textos descritivos com 2–3 parágrafos, abaixo do mínimo (3–5); termos como "metadados",
  "Crossref", "citation statement" não são descomplicados.

## 2. Pontos Positivos (Fortalezas)

- **Progressão correta**: existência antes de fidelidade antes de apoio. É a ordem de custo
  crescente da checagem e evita ler um artigo que nem existe.
- **Pares de exercício bem escolhidos**: o artigo da própria Scite como par correto e como par
  "existe, mas não sustenta" ensina que a mesma fonte pode validar uma frase e não outra.
- **Referência inventada declarada como tal** (DOI 10.9999): exercício seguro, sem acusar obra real.
- **Critério "registrar bases e data sem concluir além do pesquisado"** no Módulo 2: é o núcleo da
  postura de verificação.
- Registro formal mantido em quase todo o texto.

## 3. Pontos Negativos e Gargalos (Debilidades)

1. **Acesso**: sem Módulo 0; nenhuma verificação de conta, plano, limite de três Pro Searches/dia na
   Perplexity gratuita, nem aviso de cobrança do teste Scite.
2. **Segurança e dados** ausentes, embora o Módulo 4 peça upload de PDF ao Reference Check. O
   material-fonte registra que a retenção de uploads atuais não foi confirmada.
3. **Terceira camada ausente**: retratação, Crossmark, banner SciELO, "Retraction in" no PubMed.
4. **Público jurídico sem exercício**: casos STJ (HC 1.023.732, HC 1.094.270, multa de 2026) e
   TJSC aparecem só como frase genérica no Módulo 1.
5. **Rigor dos números**: o Módulo 1 não traz os dados (Walters e Wilder: 636 referências, 55%
   GPT-3.5 e 18% GPT-4 fabricadas, abril/2023; Tow Center: 37% de erro da Perplexity em atribuição
   de notícias, 2025) nem o aviso de que valem para aquelas versões e tarefas.
6. **Exercício do Módulo 3 inexecutável como está**: "perguntar sobre a acurácia" não diz qual
   prompt, nem onde está o PDF, nem quais termos procurar com Localizar.
7. **Módulo 4 trata rótulo como veredito**: não explica que a classificação vale para o trecho
   citante, que o classificador tem desempenho desigual entre classes e que contagem não é placar.
8. **Check Sources e painel Sources** (Perplexity, julho/2026) — diferencial atual da ferramenta
   para checagem — não aparecem.
9. **Bases gratuitas** limitadas a DOI.org e Crossref; faltam Google Scholar (descoberta),
   SciELO e PubMed (estado editorial), CAPES/BDTD (acesso brasileiro), e a regra "ausência no
   Google não é inexistência".
10. **Sem ficha de auditoria** definida, embora a síntese a exija; sem "Mão na massa" com modelo
    editável.
11. **Atividade integradora** com três critérios vagos e sem os gabaritos dos pares; não dá para
    autoavaliar.
12. **Leitura lateral e SIFT**, métodos publicados de verificação, ausentes.

## 4. Matriz de Soluções e Melhorias

| # | Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|---|
| E1 | Acesso e planos não verificados | Identificação; antes do Módulo 1 | Criar Módulo 0 com verificação de acesso, tabela de planos (Perplexity Free: 3 Pro Searches/dia; Scite: teste 7 dias, cartão, renovação) e decisão "rota com ou sem Scite" | Alta |
| E2 | Scite tratada como obrigatória | Recursos; Módulo 4 | Declarar Scite opcional; ensinar Smart Citations com o relatório de exemplo público e com o artigo de 2021; uso ao vivo como caminho opcional | Alta |
| E3 | Segurança ausente | Antes do primeiro uso | Criar Módulo 2 "Responsabilidade, sigilo e dados" antes de qualquer pergunta à Perplexity: termos da Scite (responsabilidade final do usuário), opt-out da Perplexity, LGPD, segredo de justiça, retenção não confirmada | Alta |
| E4 | Estado da evidência ausente | Entre fidelidade e síntese | Reescrever Módulo 4 como "Estado da evidência": retratação (par 5 SciELO), Crossmark, PubMed, e Smart Citations | Alta |
| E5 | Público J2 sem exercício | Todos os módulos | Variante jurídica em cada exercício; caso STJ HC 1.023.732 no Módulo 1 e na síntese; rota SCON + Planalto | Alta |
| E6 | Números vagos | Módulo 1 | Substituir "parcela relevante" pelos dados com amostra, modelo e data; incluir box "não misturar porcentagens" | Alta |
| E7 | Exercício de fidelidade sem passos | Módulo 3 | Dar o prompt exato, o link do artigo, os termos para Localizar e o gabarito fundamentado | Alta |
| E8 | Rótulo como veredito | Módulo 4 | Texto e questão "contagem não é placar" usando os números do relatório de exemplo (1.095 citation statements: 7 supporting, 1.077 mentioning, 0 contrasting) | Alta |
| E9 | Check Sources ausente | Módulo 3 | Incluir Check Sources e Sources como apoio, com [conferir] sobre disponibilidade no plano gratuito | Média |
| E10 | Bases gratuitas incompletas | Módulo 2 | Tabela "qual base responde a qual pergunta" (DOI/Crossref, Scholar, SciELO, PubMed, CAPES, BDTD, Lattes, SCON, Planalto) | Média |
| E11 | Sem ficha de auditoria | Módulo 0 e "Mão na massa" | Modelo de ficha em aspas triplas no Módulo 0, reutilizado em todos os módulos | Alta |
| E12 | Integradora sem critério objetivo | Síntese | Tabela de seis critérios e gabarito dos pares; escolha de dossiê científico ou jurídico | Alta |
| E13 | SIFT e leitura lateral ausentes | Módulo 3 | Apresentar SIFT (Stop, Investigate, Find, Trace) e leitura lateral como método de fidelidade | Média |
| E14 | Textos descritivos curtos e termos não explicados | Todos | 3–5 parágrafos; descomplicar DOI, metadados, Crossref, citation statement, retratação na primeira ocorrência; analogia da encomenda (rastreio / abrir a caixa / recall) | Média |
| E15 | Carga horária e progressão | Estrutura | Passar a 6 módulos + síntese dentro de 100–130 min; "Mão na massa" por módulo | Média |

## 5. Roadmap de Expansão

Cabe neste curso:

- Fluxo fixo de oito passos (extrair afirmação → identificar citação → metadados → original →
  trecho → contexto e método → contestação/retratação → registro), apresentado no Módulo 1 e
  retomado como fio condutor.
- Afirmações atômicas: quebrar uma resposta de IA em alegações verificáveis.
- Extensão gratuita da Scite como entrada opcional ([conferir] o que aparece sem conta).

Fica para outro curso:

- Reference Check de manuscrito completo e Collections com alertas (uso contínuo de pesquisador) →
  menção no Essentials; prática no Hands-on apenas como opcional.
- Avaliação metodológica (desenho, risco de viés) → *Revisão Bibliográfica com IA - Hands On*.
- API/MCP da Scite → fora do público.

Não verificado: nenhuma interface foi aberta nesta análise; os caminhos de menu da Scite vêm em
parte de tutoriais de 2021 e a disponibilidade de Academic e Check Sources no plano gratuito da
Perplexity não está confirmada.
