# Relatório — IA para Análise de Dados - Hands On (revisão de texto + inserção de blocos)

**Data:** 17/11/2026 (v1) · **Pacote final:** `Onda 2/01_FINALIZADO_subir-na-LMS/ia-para-analise-de-dados/ia-para-analise-de-dados-hands-on-scorm12-UxxMjnun-FINAL-com-blocos-v1.zip`

## 1. Material-fonte e mapeamento

Fonte: `Pesquisa Conteudo Onda 2/Ementa Completa/ia-para-analise-de-dados-essentials/roteiros/roteiro-articulate-hands-on.md`.
O Articulate condensou tudo em 3 lições: L1 = Antes de arregaçar as mangas · L2 = Oficinas 1 a 4 · L3 = Projeto Final + Parte dos Dez.
Ficaram de fora: os 4 blocos "🚀 Quer ir além?", o checklist de preparação e o "Conseguiu! E agora?" — recuperados na fase B.

## 2. Revisão de texto (fase A)

**190 campos alterados** (L1 35 · L2 113 · L3 42). `validar_texto.py`: estrutura preservada, 190 = 190.

- **Títulos e textos em inglês**: as três lições vieram com título, cabeçalho e abertura em inglês ("Getting Started…", "Welcome to Your Hands-On Data Journey"). Tudo traduzido/reescrito a partir do roteiro.
- **L3 — questão com gabarito quebrado**: perguntava "o que NÃO deve faltar" e marcava como correta "opinião pessoal sobre as causas". O enunciado passou a "o que NÃO deve entrar num resumo confiável" — a alternativa marcada continua a mesma e agora está certa; feedbacks reescritos.
- Cada oficina ganhou o "🎯 O problema / 🧰 Você vai usar" no process, os passos com os textos a digitar verbatim e o "✅ Deu certo?" com os números do gabarito (Petrobras R$ 36,6 bi, 40.940.966 casos, 203.080.756 habitantes etc.), que o Articulate tinha cortado nas Oficinas 2, 3 e 4.
- Questões com feedbacks que explicam o porquê; a questão do CNJ virou cenário com o número de 81 milhões.
- "Se travar" separado por oficina; o modelo de resumo do Projeto Final e a checklist do gabarito restaurados.

## 3. Inserções (fase B) — 14 blocos

| Lição | Posição | Tipo | Por quê |
|---|---|---|---|
| L1 | antes da questão | **HTML checklist de preparação (6 itens) + Continue que trava** | sem as bases e o plano de envios, as oficinas não funcionam |
| L2 | fim de cada oficina (4×) | título + **accordion "Quer ir além? Desafios opcionais"** (3 desafios com validação cada) | os desafios do roteiro tinham sido omitidos |
| L3 | antes da questão | **HTML checklist do Projeto Final (6 itens) + Continue que trava** | fecha o projeto com os números do gabarito |
| L3 | fim | Continue + título **"Conseguiu! E agora?"** | o fechamento do roteiro tinha sido omitido |

## 4. Validações

- Fase A: `validar_texto.py` sem divergência; ponte `verificar_scorm.py` **APROVADO** (0 erros, 0 avisos).
- Fase B: `validar.py` **APROVADO** (14 blocos novos; 296 IDs distintos); `verificar_scorm.py` final **APROVADO** (0 erros, 0 avisos).

## 5. Navegador (mock de LMS)

Visto: as duas travas mostram o cadeado e liberam com os itens marcados; os 4 accordions de desafios aparecem depois de cada "Se travar"; "Conseguiu! E agora?" aparece no fim; console sem erros; HTMLs a 360 px sem rolagem horizontal.
**Não testado:** LMS real; `file://`; as análises reais no ChatGPT.

## 6. Decisões tomadas

- Tabela de bases mantida como tabela HTML no parágrafo (já vinha assim do Articulate e renderiza).
- O próximo curso citado no fechamento usa o título real: *Análise de Dados em Python com IA*.
