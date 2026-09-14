Aqui está um mini manual focado na **sequência e anatomia dos parâmetros de entrada** do Pandoc.

O Pandoc funciona seguindo uma lógica posicional e de declaração de flags (sinalizadores). Entender essa ordem evita que o terminal confunda o que é arquivo de texto, o que é estilo e o que é o e-book final.

---

## 📖 A Anatomia Espacial do Comando Pandoc

A estrutura ideal e mais segura para organizar o seu comando no terminal segue esta sequência exata:

```powershell
pandoc [ARQUIVOS_DE_ENTRADA] -o [ARQUIVO_DE_SAÍDA] [FLAGS_DE_ESTRUTURA] [FLAGS_DE_ESTILO] [METADADOS]

```

---

## 🛠️ Guia Passo a Passo da Sequência de Entradas

Ao montar o seu comando em uma única linha no PowerShell, adicione os elementos nesta ordem:

### 1. O Motor e as Fontes (`pandoc ...`)

Logo após o comando `pandoc`, você deve colocar os arquivos que contêm o texto do livro. O Pandoc aceita mais de um arquivo de entrada e vai juntá-los na ordem em que aparecem.

* **Exemplo com arquivo único:** `pandoc meu_livro.md`
* **Exemplo com múltiplos arquivos:** `pandoc intro.md capitulo1.md capitulo2.md`
* **Exemplo com arquivo de metadados:** `pandoc metadata.yaml meu_livro.md` *(O arquivo YAML sempre vem primeiro)*.

### 2. O Destino (`-o seu_livro.epub`)

A flag `-o` significa *output* (saída). O arquivo com a extensão `.epub` deve vir imediatamente após essa flag.

* **Exemplo:** `-o curso_claude.epub`

### 3. Divisores de Estrutura (Capítulos e Sumário)

Aqui você diz ao Pandoc como ele deve quebrar o Markdown para criar as páginas do e-book e o menu lateral.

* `--epub-chapter-level=1`: Diz que cada título `#` vira um capítulo/página nova.
* `--toc`: Gera a tabela de conteúdos (sumário) digitalizada.

### 4. Identidade Visual (Capa e CSS)

Agora entram os arquivos de mídia e estilização que vão dar a cara do e-book.

* `--epub-cover-image=capa.jpg`: Aponta para a imagem da capa (JPG ou PNG).
* `--css=estilo.css`: Aplica a sua folha de estilo customizada para fontes, recuos e breadcrumbs.

### 5. Metadados Rápidos (Se não usou o arquivo YAML)

Por fim, as informações que aparecem nos detalhes do arquivo dentro do e-reader.

* `--metadata title="Título"` `--metadata author="Autor"` `--metadata language="pt-BR"`
* `--metadata metadata.yaml`


```YAML
---
title: "Meu Incrível Livro"
author: "Seu Nome"
language: pt-BR
publisher: "Sua Editora"
rights: "© 2026 Todos os direitos reservados"
---
```

---

## 🚀 O Comando Pronto e Sequenciado (Linha Única)

Juntando toda a sequência lógica explicada acima, o seu comando definitivo para o terminal fica assim:

```powershell
pandoc ebook_claude_ppt.md -o curso_claude.epub --split-level=1 --toc --epub-cover-image=capa.png --css=style.css --metadata metadata.yaml

```

> 💡 **Nota de execução:** Lembre-se de que todos os arquivos citados (`meu_livro.md`, `capa.jpg`, `estilo.css`) precisam estar guardados **dentro da mesma pasta** onde o seu PowerShell está aberto.