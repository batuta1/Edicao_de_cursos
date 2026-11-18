# ChatGPT (Codex) no VS Code — pacote de curso

Curso curto, introdutório e autoinstrucional sobre o uso do Codex no Visual Studio Code para trabalho
com pastas de arquivos, destinado a professores universitários **que não programam**. Duas trilhas,
238 minutos no total.

Gerado pela skill `criar-ementa-curso`, Fases 0 a 7.

## Índice da pasta

### Produtos

| Arquivo | O que é |
|---|---|
| [ementa.md](ementa.md) | Ementa consolidada — identificação, objetivo, competências, mapa das trilhas, carga horária e pendências. É o documento de decisão. |
| [roteiros/roteiro-essentials.md](roteiros/roteiro-essentials.md) | Plano de aula completo da trilha Essentials, com objetivos, habilidades, sugestões de print e solução de problemas por módulo. |
| [roteiros/roteiro-hands-on.md](roteiros/roteiro-hands-on.md) | Curso completo da trilha Hands-on, com as cinco oficinas, o Projeto Final e A Parte dos Dez. |
| [roteiros/roteiro-articulate-essentials.md](roteiros/roteiro-articulate-essentials.md) | Versão da trilha Essentials pronta para o Articulate Rise 360: breadcrumbs no lugar de prints, cues `» IA:` e marcadores de lição. |
| [roteiros/roteiro-articulate-hands-on.md](roteiros/roteiro-articulate-hands-on.md) | Versão da trilha Hands-on pronta para o Rise 360, com os mesmos recursos de montagem. |
| [carga-horaria/met-tabela.md](carga-horaria/met-tabela.md) | A tabela MET aplicada neste curso, com as regras de contagem adotadas. |
| [carga-horaria/carga-horaria-essentials.md](carga-horaria/carga-horaria-essentials.md) | Breakdown atividade a atividade da trilha Essentials: 125 min, 17 atividades, 32,8 % teoria. |
| [carga-horaria/carga-horaria-hands-on.md](carga-horaria/carga-horaria-hands-on.md) | Breakdown atividade a atividade da trilha Hands-on: 113 min, 17 atividades, 26,5 % teoria. |

### Processo (não é entregável)

| Arquivo | O que é |
|---|---|
| [_processo/00-contornos.md](_processo/00-contornos.md) | Fase 0 — objeto base, o recorte acadêmico não-programador, público, carga horária alvo e os três fatos centrais do curso. |
| [_processo/01-v1-essentials.md](_processo/01-v1-essentials.md) | Fase 1 — primeira versão da trilha Essentials, antes da auditoria. |
| [_processo/01-v1-hands-on.md](_processo/01-v1-hands-on.md) | Fase 1 — primeira versão da trilha Hands-on, antes da auditoria. |
| [_processo/02-analise-essentials.md](_processo/02-analise-essentials.md) | Fase 2 — auditoria crítica da Essentials, com matriz de doze soluções. Nota 4,5/10: o documento mais reprovado do lote, e a análise explica por quê. |
| [_processo/02-analise-hands-on.md](_processo/02-analise-hands-on.md) | Fase 2 — auditoria crítica da Hands-on, com matriz de onze soluções. |

## Números do curso

| | Essentials | Hands-on | Total |
|---|---|---|---|
| Unidades | 6 módulos | 5 oficinas + Projeto Final | — |
| Atividades | 17 | 17 | 34 |
| Duração | 125 min | 113 min | 238 min |
| Teoria : Prática | 32,8 % : 67,2 % | 26,5 % : 73,5 % | 29,8 % : 70,2 % |

## O recorte que distingue este curso

O material-fonte descreve o Codex como "o agente de programação da OpenAI". Este curso adota
deliberadamente **outro recorte**: o público não programa, e o valor do Codex para ele não está em
escrever software, mas em operar sobre uma pasta de arquivos a partir de instruções em português —
padronizar nomes de material de aula, localizar um assunto dentro de dezenas de textos, gerar um
gráfico a partir de dados exportados, montar um índice do próprio acervo.

A auditoria da Fase 2 reprovou a primeira versão justamente por não ter feito essa tradução
(`_processo/02-analise-essentials.md`, gargalo 1). O roteiro final abre por quatro casos acadêmicos
concretos, e a definição oficial da OpenAI aparece **depois** deles, como nota.

## Relação com o curso `../Codex/`

Já existe na pasta [../Codex/](../Codex/) um curso anterior sobre o Codex, de recorte generalista.
Este trata do mesmo objeto com público e recorte distintos. **Antes de publicar os dois, convém
decidir se coexistem ou se um substitui o outro.**

## O que NÃO foi verificado

A lista completa, com o local de cada afirmação, está na seção "Pendências de Validação" de
[ementa.md](ementa.md). A primeira é de outra ordem que as demais:

1. **Comportamento do Codex em pastas que não são repositórios de código.** O recorte acadêmico deste
   curso — renomear material de aula, consultar textos, gerar gráfico a partir de CSV — **não foi
   testado na prática**. Todo o curso repousa sobre esse pressuposto, e as quatro oficinas da trilha
   Hands-on dependem dele. **Valide isto antes de qualquer outra coisa e antes de investir na
   produção.** Se o comportamento divergir, o cálculo de carga horária também precisa ser refeito.
2. **Nome exato e editor da extensão Codex** na loja do VS Code, e o caminho de instalação.
3. **Se o modo somente leitura é ajustável a partir da extensão** ou apenas pela linha de comando e
   pelo arquivo de configuração. Essa instrução sustenta toda a estratégia de segurança das duas
   trilhas.
4. **Aparência atual do painel do Codex** e nomes dos controles em português.
5. **Disponibilidade do comando de inicialização do arquivo de instruções a partir da extensão.** O
   Módulo 4 da Essentials já está redigido de forma condicional, com alternativa manual.
6. **Limites de uso por plano** e quanto rende o plano gratuito, dado que a cota é compartilhada com
   o ChatGPT Work, o ChatGPT para Excel e os agentes do espaço de trabalho.
7. **Comando de diagnóstico** (`codex doctor`) e se a saída descrita corresponde à versão vigente.

## Decisões editoriais registradas

- **Nenhum número de benchmark foi usado.** Os resultados comparativos do anúncio do GPT-5-Codex são
  irrelevantes para o público e envelhecem rápido.
- **Nenhum nome de modelo é citado nos roteiros.** O material-fonte registra uma migração de modelos
  com data marcada; nomes de modelo envelhecem entre a redação e a publicação.
- **O parágrafo sobre distribuições do WSL foi removido** da versão final: é irrelevante ao público e
  sugere um pré-requisito que não existe.

## Próximo passo da esteira

1. **Validar a pendência 1** — testar o Codex em uma pasta real de material de aula. Sem isso, não
   vale produzir o curso.
2. Conferir as demais pendências.
3. Carregar no Articulate Rise 360 o `promptArticulate.md` do projeto junto com o roteiro Articulate
   da trilha desejada.
4. Gerar o curso e fazer a verificação visual.
5. Exportar o SCORM.
6. Revisar os textos com a skill `revisar-curso-scorm`.
