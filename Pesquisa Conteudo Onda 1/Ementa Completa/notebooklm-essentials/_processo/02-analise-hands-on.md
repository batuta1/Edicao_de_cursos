# 02 — Análise crítica 360 · NotebookLM - Hands-on (v1.0)

Entrada: `_processo/01-v1-hands-on.md` + `_processo/00-contornos.md`.
Contexto: objeto base NotebookLM (Gemini Notebook desde 16/07/2026); público triplo; trilha
Hands-on; autoinstrucional; alvo 90–120 min; plano gratuito.

## 1. Sumário Executivo

**Nota: 5 / 10.** O tom está acertado — leve, em 2ª pessoa, com problemas reconhecíveis — e a
regra de ouro ("sempre clique na citação") é exatamente a lição certa. O problema é que a v1.0
promete execução sem fornecer o que executar: não há fontes definidas, um passo leva a um botão
que não existe, o "Se travar" não resolve nada e nenhum aviso de privacidade aparece antes de o
aluno subir o primeiro documento.

Principais constatações:

- Oficina 1 manda subir "um PDF do seu computador": sem corpus definido e sem aviso, o aluno sobe
  o que tiver à mão — inclusive documento de cliente ou planilha de alunos.
- Oficina 3, passo 2, "Clique em Guia de estudo": o caminho real é `Estúdio > Relatórios > Guia de
  estudo`. O aluno trava no segundo passo.
- Oficina 4 não diz onde se escolhe o idioma (`Personalizar`) nem que a geração leva minutos — o
  aluno fica olhando para a tela.
- "Se travar" com respostas vazias ("tente outro arquivo", "atualize a página").
- Soma de 80 min, abaixo da faixa de 90–120 min; "Quer ir além?" com um desafio só (o prompt-mestre
  pede três).
- Mudança de marca para Gemini Notebook ignorada.

## 2. Pontos Positivos (Fortalezas)

| Fortaleza | Por que é um acerto |
|---|---|
| Problemas de abertura concretos ("a prova é amanhã", "uma hora no trânsito") | PBL legítimo: o aluno se vê na situação e sabe por que está fazendo a oficina. |
| Regra de ouro 🔑 sobre conferir a citação | É a principal lição de segurança epistêmica do produto e está no lugar mais visível. |
| Um único notebook atravessando as oficinas | Cada vitória se acumula; o Projeto Final reaproveita o hábito. |
| Aviso ⚠️ de que o áudio pode errar | Correto e alinhado à documentação. |
| Tom leve sem condescendência, humor ausente ou mínimo | Respeita o estilo; nada a cortar. |

## 3. Pontos Negativos e Gargalos (Debilidades)

### 3.1 Clareza pedagógica

- **Fontes não fornecidas:** "três documentos ou links sobre um tema" é etapa implícita. O aluno
  precisa decidir o tema, achar fontes, avaliar se servem. Em curso autoinstrucional, isso é o
  maior ponto de abandono.
- **Passos que não dizem onde clicar:** "Escolha português" (onde?), "Vá até o painel Conversa"
  (em que parte da tela?). Faltam breadcrumbs.
- **"Deu certo?" mede a ferramenta, não o aluno:** "a resposta tem números de citação" não prova
  que o aluno conferiu algo.
- **Seleção de fontes ausente:** o aluno não aprende que pode perguntar só a uma fonte.

### 3.2 Rigor técnico

- **Botão inexistente:** guia de estudo está em `Estúdio > Relatórios`, não solto no Estúdio.
- **Áudio:** formatos (Deep Dive, The Brief, Critique, Debate), idioma e duração ficam em
  `Personalizar`; `Longer` é documentado só para inglês; geração assíncrona e sujeita a falha; cota
  de 3 áudios/dia no gratuito.
- **"Se travar" sem diagnóstico:** PDF não carrega por excesso de 200 MB/500.000 palavras,
  proteção contra cópia ou por ser imagem escaneada; link não funciona por paywall ou porque a URL
  importa só o HTML daquela página; YouTube precisa ser público e com legenda.
- **Quer ir além da Oficina 1** (YouTube) sem a ressalva da legenda e das 72 horas.
- **Marca e rótulos:** Gemini Notebook × NotebookLM; rótulos pt-BR irregulares (parte da interface
  em inglês, como `Configure Chat`, `Learning Guide`).

### 3.3 Segurança e permissões (risco crítico)

- Nenhuma orientação antes do primeiro upload: conta pessoal × Workspace, feedback revisado por
  humanos, LGPD, sigilo profissional.
- Item 10 da Parte dos Dez — "Compartilhe notebooks com colegas" — sem ressalva de papéis
  (Leitor/Editor), link público e do fato de a "visualização da conversa" não esconder de verdade
  as fontes. É um conselho que, seguido à risca, vaza documento.

### 3.4 Engajamento

- Tom adequado. Mas os problemas de abertura são todos de estudante; educador, advogado e
  jornalista não aparecem.
- "Quer ir além?" com um único desafio genérico e sem forma de validação.

### 3.5 Potencial oculto

- A citação clicável — o grande diferencial — é tratada como detalhe (passo 4 da Oficina 2).
- Ausentes: configurar o chat para modo tutor (`Learning Guide`), salvar resposta como nota e usar
  como fonte, cartões/testes com dificuldade, mapa mental com perguntas por nó, compartilhamento
  com Leitor/Editor.

### 3.6 Aderência ao público

- Sem conteúdo avançado indevido. Recursos pagos/18+ não são cobrados — correto —, mas também não
  são sinalizados, então o aluno que vê "Cinematic" na tela não sabe que não é para ele.

### 3.7 Não verificado

Rótulos pt-BR exatos de: opções de tipo de fonte na janela de upload, botão "salvar como nota",
menu de configuração do chat, item "Compartilhar > visualização da conversa". Ficam como formulação
genérica com marcação de conferência.

## 4. Matriz de Soluções e Melhorias

| # | Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|---|
| H1 | Sem aviso de privacidade antes do upload | Antes da Oficina 1 | Acrescentar em "Antes de Arregaçar as Mangas" o **semáforo do upload** (verde: público; amarelo: interno sem dado pessoal, só em conta da instituição; vermelho: dado pessoal, cliente, aluno, sigilo) + box ⚠️ sobre feedback | Crítica |
| H2 | Fontes não definidas | Oficina 1 | Entregar o **kit LGPD**: quatro fontes públicas com links, passo de download dos dois PDFs e upload; a página HTML entra por link | Crítica |
| H3 | Botão inexistente "Guia de estudo" | Oficina 3 | Trocar por `Estúdio > Relatórios > Guia de estudo` | Crítica |
| H4 | Idioma/duração do áudio sem caminho; espera não prevista | Oficina 4 | `Estúdio > Resumo em Áudio > Personalizar > formato · idioma · duração > Gerar`; instruir a disparar o áudio **antes** e fazer o mapa mental enquanto espera | Alta |
| H5 | "Se travar" inútil | Todas | Reescrever com causa + ação (200 MB/500.000 palavras, PDF escaneado → OCR autorizado, paywall, URL só HTML, YouTube sem legenda/72 h, cota diária) | Alta |
| H6 | "Deu certo?" passivo | Oficina 2 | Exigir **ficha de 3 citações** (frase, trecho, bate/parcial/não bate) | Alta |
| H7 | Seleção de fontes ausente | Oficina 2 | Passo de desmarcar fontes no painel Fontes e repetir a pergunta | Alta |
| H8 | Compartilhamento sem ressalva | Parte dos Dez, item 10 | Reescrever: compartilhar como Leitor, nunca link público para notebook com documento protegido; levar o tema para a Oficina 4 | Alta |
| H9 | Marca em transição | Antes de Arregaçar | Box 📌: "pode aparecer NotebookLM ou Gemini Notebook; é o mesmo produto em `notebook.google.com`" | Média |
| H10 | Breadcrumbs ausentes | Todas | Acrescentar caminho `notebook.google.com > painel > opção` nos passos de navegação | Média |
| H11 | Problemas só de estudante | Oficinas | Variar o problema de abertura (estudante, professor, advogado, jornalista) mantendo o mesmo kit LGPD | Média |
| H12 | "Quer ir além?" com 1 desafio | Todas | Três desafios por oficina, cada um com validação | Média |
| H13 | Diferenciais omitidos | Oficinas 2–4 | `Learning Guide` (Oficina 2), salvar como nota (Oficina 2), cartões/teste (Oficina 3), mapa mental + compartilhamento (Oficina 4) | Média |
| H14 | Carga horária curta | Mapa | Recalcular pela MET na Fase 4; mirar 90–120 min | Média |
| H15 | Projeto Final é cópia das oficinas | Projeto Final | Missão autônoma: tema do **seu** perfil, fontes escolhidas por você com o semáforo, entrega de um "kit de estudo" compartilhado como Leitor | Média |

## 5. Roadmap de Expansão

| Tópico | Destino |
|---|---|
| Ficha de auditoria de citação | **Neste curso** (Oficina 2 e Projeto Final) |
| Learning Guide como tutor | **Neste curso** (Oficina 2, desafio) |
| Cartões e teste | **Neste curso** (Oficina 3) |
| Mapa mental e compartilhamento | **Neste curso** (Oficina 4) |
| Uso no celular (ouvir áudio offline) | **Neste curso**, como dica na Parte dos Dez |
| Pesquisa Rápida / descoberta de fontes | Desafio opcional; prática completa fica para Deep Research - Hands On |
| Tabela de dados, Apresentações, Infográficos | Desafio opcional "Quer ir além?" |
| Deep Research, Video Cinematic | **Fora** (curso seguinte / plano pago) |
