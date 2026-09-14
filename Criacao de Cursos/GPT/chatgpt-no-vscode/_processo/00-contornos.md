# Contornos — ChatGPT (Codex) no VS Code

Documento da Fase 0. Define os limites do curso antes de qualquer aula ser escrita. Se algo aqui
mudar, as fases seguintes precisam ser refeitas, não remendadas.

## Objeto base

**Codex no Visual Studio Code — o agente de IA da OpenAI aplicado ao trabalho acadêmico com
arquivos de texto e dados.**

O Codex é apresentado no material-fonte como "o agente de programação da OpenAI". Este curso adota
um recorte deliberadamente diferente do óbvio: o público não programa, e o valor do Codex para ele
não está em escrever software, mas em **operar sobre uma pasta de arquivos com instruções em
português**.

O que isso significa na prática para um docente:

- Uma pasta com trinta arquivos de aula, e uma instrução: "renomeie tudo no padrão
  `AAAA-MM-DD-tema`".
- Uma tese em LaTeX que não compila, e uma instrução: "descubra por que e conserte".
- Uma planilha exportada em CSV, e uma instrução: "faça um gráfico das médias por turma".
- Um conjunto de arquivos de texto e uma instrução: "gere um índice em Markdown com links".

O curso **não** ensina a programar, não pressupõe conhecimento de linguagem alguma, e não é curso de
VS Code. O VS Code entra como a janela onde o Codex trabalha.

> **Nota de posicionamento.** Já existe na pasta `../Codex/` um curso anterior sobre o Codex, de
> recorte generalista. Este curso é diferente: mesmo objeto, público e recorte distintos. Antes de
> publicar os dois, convém decidir se coexistem ou se um substitui o outro.

## Público-alvo

Professores universitários (docentes do ensino superior), **de qualquer área**, que não programam e
não pretendem programar.

Consequências assumidas — este é o público mais distante do objeto base dos três cursos do lote, e a
distância governa todas as decisões:

- O curso precisa justificar sua própria existência nos primeiros cinco minutos, com um exemplo que
  o docente reconheça como problema seu. Um exemplo de código na abertura perde o participante.
- Todo termo de programação (terminal, repositório, extensão, sandbox, diretório, versionamento)
  precisa ser explicado na hora, com comparação do cotidiano.
- Instalar VS Code e uma extensão é, para esse público, uma barreira real. O Módulo 0 é sobre isso e
  precisa ser paciente.
- O modelo de aprovações e a caixa de areia (*sandbox*) não são detalhe técnico: são o que impede o
  agente de apagar a pasta da tese. Entram cedo e como assunto central.
- Docentes de exatas e computação que já programam continuam atendidos, mas o curso não pressupõe
  esse perfil.

## Pré-requisitos

- Nenhum conhecimento de programação.
- Nenhum conhecimento prévio de inteligência artificial.
- Saber criar pastas, mover arquivos e localizar uma pasta no próprio computador.
- Conta no ChatGPT. O Codex está incluído nos planos do ChatGPT, **inclusive Free e Go**, com
  limites de uso variáveis por plano.

## Recursos necessários

- Computador com Windows, macOS ou Linux, com permissão para instalar programas.
- Visual Studio Code instalado.
- Extensão Codex para VS Code instalada.
- Internet ativa.
- Conta ChatGPT ativa.
- Uma pasta de trabalho real do participante — material de aula, dados de pesquisa, capítulos de
  texto — com **cópia de segurança feita antes** de qualquer exercício.

## Natureza

Curso curto, introdutório, prático e **autoinstrucional**. Nenhum passo pode depender de explicação
ao vivo; todo exercício precisa de critério de êxito verificável pelo próprio participante.

## Carga horária alvo

| Trilha | Alvo |
|---|---|
| Essentials | 100 a 130 minutos |
| Hands-on | 90 a 120 minutos |

> **Decisão declarada.** Adotou-se desde a Fase 0 a carga horária dos prompts-mestre do Articulate
> (Fase 7), em vez dos 60–90 min dos modelos base, para que roteiro, cálculo da MET e versão do
> Rise 360 descrevam o mesmo curso.

## Estrutura definida

| Trilha | Unidades |
|---|---|
| Essentials | Módulo 0 (instalação e segurança) + Módulos 1 a 4 (conteúdo) + Módulo 5 (síntese) |
| Hands-on | Preparação + Oficinas 1 a 4 + Projeto Final + A Parte dos Dez |

## Material-fonte

`../../ConteudoBruto/ConteudoBrutoVSCODE_CHATGPT_OpenAI.txt`

Dois blocos:

| Bloco | Origem | Tratamento |
|---|---|---|
| "Usando o Codex com seu plano ChatGPT" | Central de Ajuda da OpenAI | Fonte primária. Base dos módulos de acesso, limites, configuração e dados. |
| Anúncio do GPT-5-Codex (setembro de 2025) | Blog da OpenAI | Contexto e capacidades. Os números de *benchmark* **não entram no curso**: são irrelevantes para o público e envelhecem rápido. |

O que o material-fonte sustenta:

- O Codex está incluído nos planos do ChatGPT, inclusive Free e Go; limites variam por plano.
- Quatro clientes: app ChatGPT para desktop (modo Codex), CLI, extensão para IDE, Codex para a web.
- A extensão Codex para VS Code é compatível com a maioria das variações do VS Code.
- Por padrão o Codex roda em ambiente isolado, **com acesso à rede desabilitado**, local ou na
  nuvem. Pede permissão antes de ações potencialmente perigosas.
- Três níveis de aprovação no CLI: somente leitura com aprovações explícitas; automático com acesso
  ao espaço de trabalho e aprovação fora dele; acesso total.
- `codex doctor` diagnostica problemas de inicialização, conectividade e desempenho.
- `/init` gera uma estrutura inicial de `AGENTS.md` para o projeto atual.
- `/status` mostra a situação de uso em uma sessão ativa do CLI.
- Configuração em `~/.codex/config.toml` (macOS/Linux) ou `%USERPROFILE%\.codex\config.toml`
  (Windows).
- No Windows: seleção da distribuição WSL quando há mais de uma instalada.
- Codex, ChatGPT Work, ChatGPT para Excel e Agentes usam cota e saldo de créditos compartilhados.
- Controles de dados de treinamento do ChatGPT se aplicam ao Codex; fluxos locais rodam no
  dispositivo, tarefas na nuvem em ambientes da OpenAI.
- O Codex pode anexar imagens no CLI e usar busca na web e MCP.

## Fatos centrais que o curso precisa deixar explícitos

1. **O Codex modifica arquivos de verdade no computador do participante.** É a diferença que separa
   este curso dos outros dois do lote, e é onde mora o risco. Cópia de segurança antes de tudo, e o
   modo somente leitura como padrão de quem está aprendendo.
2. **Os três níveis de aprovação são o controle de segurança principal.** Precisam ser ensinados
   antes do primeiro uso real, não depois.
3. **O Codex está incluído no plano gratuito**, o que remove a objeção de custo — mas os limites de
   uso são compartilhados com outros recursos e se esgotam.

## Pendências de validação humana

1. Nome exato e editor da extensão Codex na loja do VS Code, e o caminho da interface para
   instalá-la.
2. Aparência atual do painel do Codex no VS Code e nomes dos controles em português.
3. Se o modo somente leitura é ajustável pela extensão do VS Code ou apenas pelo CLI e pelo arquivo
   de configuração.
4. Comportamento do Codex em pastas que não são repositórios de código — o material-fonte descreve
   fluxos de programação, e o recorte acadêmico deste curso precisa ser testado na prática antes da
   publicação. **Esta é a pendência mais importante do curso.**
5. Limites de uso por plano e quanto rende, na prática, o plano gratuito.
6. Nomes dos modelos disponíveis. O material-fonte cita uma migração de GPT-5.4 para GPT-5.6 em
   31 de agosto de 2026; nomes de modelo **não** são citados no roteiro final, justamente por
   envelhecerem entre a redação e a publicação.
7. Disponibilidade de "Gravar e reproduzir" (apenas macOS, usuários qualificados, indisponível na
   União Europeia, Suíça e Reino Unido) — fora do escopo deste curso, registrado apenas como limite.
