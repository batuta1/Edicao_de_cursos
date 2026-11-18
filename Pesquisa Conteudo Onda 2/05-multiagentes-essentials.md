# Pesquisa de conteúdo bruto — Multiagentes

| Campo | Valor |
|---|---|
| Assunto | Multiagentes |
| Registros no catálogo | `multiagentes-essentials` e `multiagentes-hands-on` |
| Produtos que sairão desta pesquisa | Ementa completa, curso Essentials e curso Hands On |
| Onda | 2 (ranking #24, 86 pontos) |
| Ferramentas-âncora | Claude Code e n8n |
| Tema | Coordenação de múltiplos agentes de IA |
| Trilhas | T3 — Agentes e MCP (posição 9; depois de Agentes Web e antes de Segurança em MCP)<br>T6 — Construindo com MCP, posição 6 (último curso)<br>TE5 — Integração, MCP e automação de TI, posição 8 (último curso) |
| Pesquisa feita por | ChatGPT Work |
| Versão do prompt | 7 (18 de novembro de 2026): versão 6 ampliada para pares Essentials/Hands On e alinhada à planilha v0.4 |
| Arquivo que o ChatGPT deve entregar | `ConteudoBruto_multiagentes.txt` |

## Como usar

1. Cole todo o bloco **Prompt** no ChatGPT Work.
2. Salve o TXT em `Pesquisa Conteudo Onda 2/conteudo-bruto/multiagentes/`.
3. Baixe os materiais e salve as páginas indicadas na mesma pasta.
4. Revise as lacunas antes de criar a ementa.

## Prompt

```text
# PAPEL
Você pesquisa conteúdo para a equipe brasileira de design instrucional da
IAClube.com. Reúna CONTEÚDO BRUTO verificável para a ementa completa e para os
cursos Essentials e Hands On. Não escreva a ementa, o curso ou o plano de aula.

Data de hoje: 18 de novembro de 2026. Confirme nesta data nomes, versões, planos,
limites, interfaces e disponibilidade.

# OS CURSOS QUE SERÃO CRIADOS COM ESTA PESQUISA
- Assunto: Multiagentes.
- Produtos: ementa integral; Essentials autoinstrucional de 100–130 minutos;
  Hands On autoinstrucional de 60–90 minutos, com 4 oficinas e 1 projeto final.
- Ferramentas-âncora: Claude Code e n8n. Inclua outras implementações apenas para
  explicar padrões ou comparar, sem perder o foco no que o público pode executar.
- Competência: projetar e supervisionar uma equipe de agentes com papéis definidos.
- Tarefa observável: decompor um objetivo, atribuir papéis a agentes, definir
  entradas/saídas e critérios de parada, coordenar a execução e avaliar o resultado.
- Público: usuários avançados de IA, analistas, automadores e profissionais de
  tecnologia; o Essentials deve continuar acessível a quem não programa.
- Pré-requisitos: Agentes de IA - Essentials; noções de MCP e de workflows ajudam.
  Para o Hands On, o aluno terá feito o Essentials deste assunto.
- Encaixe: T3 posição 9, entre Agentes Web e Segurança em MCP; T6 posição 6,
  último curso; TE5 posição 8, último curso.
- Fora do escopo: fundamentos gerais de um agente; criação de servidor MCP;
  segurança de MCP em profundidade; automação simples de um fluxo linear;
  engenharia de sistemas distribuídos e desenvolvimento de frameworks do zero.

# POR QUE A EQUIPE PRECISA DE CADA COISA
Defina termos para leigos; traga menus exatos em pt-BR/inglês e sua origem; para
cada ação, informe passo a passo, plano, dependências, erros, recuperação e sinal
de êxito. Para oficinas, localize arquivos públicos e gratuitos com gabarito ou
resultado verificável. Separe evidência oficial, independente e [SUGESTÃO].

# REGRA DE PROFUNDIDADE
Priorize desenho, montagem, acompanhamento e avaliação que o aluno consegue ver
e fazer. Detalhes de APIs, SDKs e arquitetura vão ao APÊNDICE TÉCNICO. Pelo menos
dois terços do arquivo devem ser práticos.

# O QUE PESQUISAR — PARTE GERAL
1. Identidade, histórico, terminologia e mudanças recentes.
2. Acesso, contas, planos, preços, limites, plataformas e requisitos.
3. Primeiros passos com nomes exatos da interface.
4. Glossário para leigos.
5. Funcionalidades, localização, plano, limites e dependências.
6. Casos reais publicados; NÃO ENCONTRADO quando não houver.
7. Boas práticas e exemplos oficiais.
8. Segurança, privacidade, dados, credenciais e LGPD.
9. Limitações, erros, observabilidade, recuperação e custos.
10. Comparação imparcial com alternativas.
11. Mudanças dos últimos 12 meses e recursos instáveis.
12. Material didático oficial.
13. Exercícios para cada ação, oficinas e dois projetos finais.

# O QUE PESQUISAR — FOCO ESPECÍFICO
1. Defina sistema multiagente e diferencie: agente único com ferramentas,
   subagentes, handoff, supervisor/worker, roteador, pipeline e swarm.
2. Quando vários agentes ajudam e quando só aumentam custo, latência, erros e
   dificuldade de depuração; traga estudos e avaliações independentes.
3. Claude Code: recursos atuais de subagentes/equipes, configuração, papéis,
   contexto, ferramentas, permissões, execução paralela, limites e interface.
4. n8n: padrões atuais para vários agentes, AI Agent, ferramentas, memória,
   subworkflows, roteamento, handoffs, human review e avaliação.
5. Padrões de coordenação: sequencial, paralelo, supervisor, debate/revisão,
   roteamento por especialidade e escalonamento humano; quando usar cada um.
6. Contratos de entrada e saída, contexto compartilhado, memória, artefatos,
   estado, critérios de conclusão e prevenção de loops.
7. Observabilidade: logs, rastreamento, custo/token, latência, versões de prompts,
   reprodução, avaliação por etapa e diagnóstico de falha.
8. Segurança: menor privilégio, segredos, isolamento, prompt injection, agente
   comprometido, propagação de erro e aprovação humana para ações sensíveis.
9. Como testar: conjunto de casos, resultado esperado, rubricas, métricas por
   etapa e ponta a ponta, testes de regressão e comparação com agente único.
10. Casos reais em pesquisa, desenvolvimento de software, suporte, conteúdo e
    operações; diferencie demonstração de produção.
11. Limites dos planos gratuitos e custo previsível de cada exercício.
12. Materiais de prática: repositório pequeno, brief, conjunto de tickets e
    documentos públicos que permitam dividir trabalho e verificar a integração.

# FONTES E MATERIAIS
Priorize documentação oficial de Claude Code/Anthropic e n8n, preços, políticas,
release notes, templates oficiais e guias de segurança; depois artigos acadêmicos,
benchmarks e imprensa confiável. Prefira pt-BR e depois inglês. Para PDFs, vídeos,
JSONs, workflows e repositórios, crie MATERIAIS PARA BAIXAR com link, tipo,
idioma, utilidade, licença e nome sugerido. Procure especialmente templates n8n,
exemplos de subagentes do Claude Code, estudos comparando agente único e equipes,
guias de avaliação/observabilidade e materiais de exercício.

# REGRAS
1. Não invente; use NÃO ENCONTRADO e diga onde procurou.
2. Use [CONFIRMADO] apenas para afirmação literal da fonte, [VERIFICAR] para
   evidência fraca/contraditória e [SUGESTÃO] para elaboração sua.
3. Dê data a preços, limites, nomes e menus; atribua cada número à fonte correta.
4. Marque a origem de menus: (interface), (ajuda pt-BR) ou (ajuda en).
5. Diferencie gratuito, pago e corporativo e teste links de exercício.
6. Liste cada página oficial essencial em PÁGINAS PARA SALVAR, uma por item.
7. Não escreva módulos, objetivos ou plano de aula. Tudo deve ser autoinstrucional.
8. Detalhes além do público vão ao APÊNDICE TÉCNICO.

# FORMATO DE ENTREGA
Entregue `ConteudoBruto_multiagentes.txt`, TXT UTF-8, com as seções:
0 Resumo executivo; 1 Identidade; 2 Acesso/planos; 3 Primeiros passos;
4 Glossário; 5 Funcionalidades; 6 Casos reais; 7 Boas práticas;
8 Segurança/privacidade; 9 Limitações/erros; 10 Comparação; 11 Novidades;
12 Material didático; 13 Exercícios (13a curtos, 13b oficinas, 13c projetos);
14 Respostas ao foco; 15 Trechos oficiais; 16 Materiais para baixar;
17 Páginas para salvar; 18 Lacunas; 19 Apêndice técnico; 20 Fontes.
Cite cada informação com o número da fonte da seção 20.

# ANTES DE ENTREGAR, CONFIRA
[ ] Sustenta ementa, Essentials e Hands On.
[ ] Todos os itens do foco têm resposta ou NÃO ENCONTRADO.
[ ] Cada ação da tarefa observável tem passo a passo e prática.
[ ] Padrões, custos, avaliação, falhas e segurança foram cobertos.
[ ] Menus têm origem; planos e região estão distinguidos.
[ ] Nenhuma elaboração própria está [CONFIRMADO].
[ ] Materiais e páginas estão listados individualmente e links foram testados.
[ ] Pelo menos dois terços tratam do que o aluno vê e faz.
```
