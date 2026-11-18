# ia-para-analise-de-dados-essentials

Curso **IA para Análise de Dados** (catálogo `novos-cursos-iaclube-priorizacao-v6.json`, Onda 2,
ranking 18; par Hands On produzido na mesma rodada), gerado com a skill `criar-ementa-curso` a
partir do conteúdo bruto em `Pesquisa Conteudo Onda 2/conteudo-bruto/ia-para-analise-de-dados-essentials/`.
Duas trilhas: Essentials (127 min) e Hands-on (105 min).

## Produtos

| Arquivo | O que é |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada: identificação, objetivo, competências, trilhas, carga horária, avaliação, pendências |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Roteiro final Essentials (Módulos 0–7), com sugestões de print, objetivos e habilidades por aula |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Roteiro final Hands-on (preparação, 4 oficinas, Projeto Final, Parte dos Dez) |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Versão Rise 360 do Essentials: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲, "Mão na massa" por módulo |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Versão Rise 360 do Hands-on: breadcrumbs, cues `» IA:`, marcadores ▼▼▼/▲▲▲ |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | Tabela MET usada no cálculo (cópia da skill) |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | Breakdown por módulo: 19 atividades, 127 min, 32% teoria / 68% prática |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | Breakdown por oficina: 19 atividades, 105 min, 11% teoria / 89% prática |

## Processo (não é entregável)

| Arquivo | O que é |
|---|---|
| [_processo/00-contornos.md](_processo/00-contornos.md) | Objeto base, público (T8, J4 e seis trilhas de dados), escopo, material-fonte, bases e gabaritos |
| [_processo/01-v1-essentials.md](_processo/01-v1-essentials.md) | Versão 1.0 do Essentials (modelo base) |
| [_processo/01-v1-hands-on.md](_processo/01-v1-hands-on.md) | Versão 1.0 do Hands-on (modelo base) |
| [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md) | Auditoria 360 do Essentials v1.0 (nota 3/10) e matriz E1–E15 |
| [_processo/02-analise-hands-on.md](_processo/02-analise-hands-on.md) | Auditoria 360 do Hands-on v1.0 (nota 3/10) e matriz H1–H12 |

Cada achado das matrizes tem destino declarado na seção de rastreabilidade ao fim de cada roteiro final.

## Decisões de design

- **Verificação é o eixo:** a tarefa observável termina em "com verificação"; todo exercício tem
  número oficial a reproduzir (IBGE, Banco Central, CVM, CNJ), conferido por script em 17/11/2026.
- **Armadilhas reais, não inventadas:** soma × composição do IPCA (4,73% × 4,83%); escala MIL/UNIDADE
  na CVM (a Vivara sobe para 1º lugar sem conversão); linhas de total no CNJ (a soma direta dá o
  dobro dos 40,9 milhões); eixo truncado e pizza de 27 fatias no Censo.
- **Cabe no plano Free:** no máximo um envio por módulo/oficina; o Hands-on vem com plano de dois
  dias (3 envios por dia).
- **Julius como segunda opinião, nunca obrigatório:** a política declara compartilhamento de prompts,
  arquivos e saídas com provedores de IA; arquivos do Free somem após 1 hora de inatividade.
- **Dados antes do primeiro envio:** controles de dados, chat temporário, LGPD, estudo da ANPD e
  Recomendação 001/2024 da OAB no Módulo 2, antes do primeiro arquivo (Módulo 3).
- **Fronteira com os cursos vizinhos:** nada de fórmula ou planilha (cursos de Excel); nada de código
  próprio (Dados com Python e IA).

## O que não foi verificado (pendente de validação humana)

1. **Rótulo do comando que exibe o código** no ChatGPT ("Ver análise"/"View analysis"): não está na
   ajuda oficial; os roteiros oferecem a alternativa "Mostre o código Python que você executou".
2. **Execução em conta Free real:** nenhum exercício foi rodado numa conta; confirmar que o arquivo
   de 11,6 MB do CNJ e o de 6,8 MB da CVM são analisados por inteiro no Free.
3. **Ícones da tabela de planos** ("Tabelas e gráficos interativos" no Free).
4. **Julius:** ícone de anexar (`+` ou clipe), rótulos "Generated code" e "Data Explorer" na
   interface atual, preço mensal × anual.
5. **IPCA de 2022 publicado** (desafio da Oficina 1 supõe diferença de até 0,01 p.p.).
6. **Recomendação 001/2024 da OAB:** texto oficial não lido (citada por notícia oficial e artigo do
   IAB).
7. **Preços e limites** do ChatGPT em 17/11/2026 — reconferir antes da gravação.

## Próximos passos (fora desta skill)

Carregar no Articulate o `promptArticulate.md` do projeto + `roteiros/roteiro-articulate-<trilha>.md`
→ gerar o curso → verificação visual → exportar SCORM → revisar com a skill `revisar-curso-scorm`.
