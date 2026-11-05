# Codex no VS Code Para Leigos — Curso Hands-on

*No fim deste curso você vai ter organizado uma pasta de verdade e feito o computador responder perguntas sobre os seus próprios arquivos — sem escrever uma linha de código.*

## Antes de Arregaçar as Mangas

Este curso é mão na massa. Você vai instalar dois programas e passar as próximas duas horas mandando
um assistente mexer nos seus arquivos — renomear, organizar, procurar coisa, montar gráfico. Você não
vai programar nada. Vai só dizer o que quer, em português.

**O que você precisa ter aberto agora:**

- Um computador onde você possa instalar programas.
- Uma pasta sua com arquivos de verdade — material de aula, dados de pesquisa, textos.
- Uma conta do ChatGPT (o plano gratuito serve).

> 🔑 **Regra de ouro:** o Codex mexe nos arquivos de verdade. Faça uma cópia da pasta antes de
> começar.

## O Mapa da Mão na Massa

| Oficina | O problema que você vai resolver | Tempo |
|---|---|---|
| 1 | "Como eu instalo isso?" | 20 min |
| 2 | "Tenho trinta arquivos com nomes impossíveis" | 20 min |
| 3 | "Em qual desses arquivos eu falei sobre aquilo?" | 20 min |
| 4 | "Tenho os dados numa planilha e queria um gráfico" | 20 min |
| Projeto Final | Organizar o material de uma disciplina inteira | 25 min |

As oficinas fazem mais sentido em sequência: cada uma entrega uma pequena vitória, e o Projeto Final
junta todas.

---

# Oficina 1 — Instalar e dar o primeiro comando

### 🎯 O Problema

Você nunca abriu um editor de código na vida e está prestes a instalar dois programas. Nesta oficina
você faz isso e dá o primeiro comando.

### 🧰 O que você vai usar

- Um navegador.
- Permissão de instalar programas no seu computador.

### 👐 Mão na massa

1. Baixe o Visual Studio Code no site oficial e instale.
2. Abra o VS Code.
3. Vá no painel de extensões, na barra lateral esquerda.
4. Pesquise por `Codex` e instale a extensão.
5. Abra o painel do Codex e entre com a sua conta do ChatGPT.
6. Abra uma pasta em `Arquivo > Abrir Pasta`.
7. No painel do Codex, escreva:

   > Descreva o que tem nesta pasta.

### ✅ Deu certo?

O painel do Codex respondeu descrevendo os seus arquivos.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Não consigo instalar | Sua instituição pode bloquear instalações. Fale com a TI. |
| Não achei a extensão | Confira se pesquisou por "Codex" e se a extensão é da OpenAI. |
| Não entra na conta | Confira se você está usando a conta certa do ChatGPT. |

> ⚠️ **Cuidado:** o Codex consegue alterar arquivos. Antes de mandar ele mexer em qualquer coisa, faça
> uma cópia da pasta.

### 🚀 Quer ir além?

Rode `codex doctor` no terminal para ver se está tudo funcionando.

---

# Oficina 2 — Arrumar uma pasta bagunçada

### 🎯 O Problema

Você tem trinta arquivos chamados `aula1.pdf`, `AULA 2 final.pdf`, `aula2-CORRIGIDA(1).pdf`. Nesta
oficina você padroniza tudo.

### 🧰 O que você vai usar

- Uma cópia de uma pasta bagunçada sua.
- O VS Code com o Codex.

### 👐 Mão na massa

1. Copie a pasta antes de qualquer coisa.
2. Abra a cópia no VS Code.
3. Peça:

   > Renomeie todos os arquivos desta pasta no padrão `aula-NN-tema.pdf`, mantendo o conteúdo
   > intacto. Antes de renomear, mostre a lista do que vai virar o quê.

4. Leia a lista proposta.
5. Aprove ou corrija.
6. Confira a pasta.

### ✅ Deu certo?

Os arquivos estão com nomes padronizados e nenhum sumiu.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Ele renomeou errado | Volte para a cópia original e refaça com instrução mais específica. |
| Ele pediu permissão e eu não sei o que responder | Leia o que ele quer fazer. Se não entendeu, recuse. |
| Ele não achou os arquivos | Confira se você abriu a pasta certa. |

> 💡 **Dica:** peça sempre a lista antes de executar. É a diferença entre corrigir uma lista e
> desfazer trinta renomeações.

### 🚀 Quer ir além?

Peça para ele organizar os arquivos em subpastas por assunto.

---

# Oficina 3 — Perguntar aos seus arquivos

### 🎯 O Problema

Você sabe que escreveu sobre determinado assunto em algum lugar, mas não lembra em qual arquivo.
Nesta oficina você para de procurar à mão.

### 🧰 O que você vai usar

- Uma pasta com vários documentos de texto.
- O VS Code com o Codex.

### 👐 Mão na massa

1. Abra a pasta no VS Code.
2. Pergunte:

   > Em quais arquivos desta pasta eu menciono [assunto]? Liste o arquivo e o trecho.

3. Confira os resultados.
4. Peça um resumo:

   > Faça um resumo de uma frase de cada arquivo desta pasta.

5. Peça um índice:

   > Crie um arquivo `indice.md` com a lista de todos os arquivos e um resumo de cada um.

### ✅ Deu certo?

Você tem um arquivo `indice.md` na pasta, com a lista e os resumos.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Ele não leu os PDFs | Nem todo formato é lido diretamente. Converta para texto se precisar. |
| O resumo está errado | Confira contra o arquivo. Ele pode errar. |
| Ele não criou o arquivo | Confira o nível de permissão. Em modo somente leitura ele não escreve. |

### 🚀 Quer ir além?

Peça um índice organizado por tema em vez de por nome de arquivo.

---

# Oficina 4 — Um gráfico sem programar

### 🎯 O Problema

Você tem as notas da turma numa planilha e queria um gráfico. Nesta oficina você pede e recebe.

### 🧰 O que você vai usar

- Um arquivo de dados exportado em formato CSV.
- O VS Code com o Codex.

### 👐 Mão na massa

1. Exporte a planilha em CSV e coloque numa pasta.
2. Abra a pasta no VS Code.
3. Peça:

   > Faça um gráfico de barras das médias por turma a partir do arquivo `notas.csv` e salve como
   > imagem.

4. Autorize a execução quando ele pedir.
5. Abra a imagem gerada.
6. Confira os números contra a planilha.

### ✅ Deu certo?

Existe uma imagem de gráfico na pasta e os valores batem com a planilha.

### 🚑 Se travar

| Problema | O que fazer |
|---|---|
| Ele disse que precisa instalar coisas | Ele precisa de acesso à rede. Autorize se você confiar na tarefa. |
| O gráfico está feio | Peça ajustes: cores, rótulos, título. |
| Os números não batem | Confira o CSV. Pode ser problema de separador decimal. |

> ⚠️ **Cuidado:** não coloque nome de aluno no arquivo que você vai processar. Use identificadores.

### 🚀 Quer ir além?

Peça três gráficos diferentes dos mesmos dados e escolha o melhor.

---

# Projeto Final — Organizar uma disciplina inteira

### 🎯 A missão

Pegue a pasta de uma disciplina sua e deixe tudo organizado, nomeado e indexado.

### 👐 Mão na massa

1. Copie a pasta.
2. Peça o diagnóstico do que tem lá dentro.
3. Peça a padronização dos nomes, com lista prévia.
4. Peça a organização em subpastas.
5. Peça um índice em Markdown.
6. Confira tudo.

### 🏁 Como saber que terminou

- [ ] Todos os arquivos estão com nomes padronizados.
- [ ] A pasta está organizada em subpastas.
- [ ] Existe um índice.
- [ ] Nenhum arquivo sumiu.
- [ ] A pasta original continua intacta.

---

# A Parte dos Dez — Coisas que Funcionam no Codex

1. **Peça a lista antes de executar.** "Mostre o que você vai fazer antes de fazer."
2. **Comece em modo somente leitura.** Você aprende sem risco.
3. **Copie a pasta antes.** Sempre.
4. **Abra a pasta certa.** Ele só vê o que está aberto.
5. **Seja específico sobre o padrão.** "aula-NN-tema.pdf" é melhor que "organize isso".
6. **Leia o que ele pede permissão para fazer.** Se não entendeu, recuse.
7. **Confira o resultado.** Ele erra.
8. **Não coloque dado de aluno na pasta.** Use identificadores.
9. **Use `codex doctor` quando algo não funcionar.**
10. **Peça em português.** Não precisa de comando nem sintaxe.

## Conseguiu! E agora?

Você organizou uma pasta inteira e fez o computador responder perguntas sobre os seus arquivos, sem
escrever código. O próximo passo é aplicar isso ao material da próxima disciplina.
