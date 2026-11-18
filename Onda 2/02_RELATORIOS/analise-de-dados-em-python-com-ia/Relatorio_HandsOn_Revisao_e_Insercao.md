# Relatório — Análise de Dados em Python com IA - Hands On (revisão de texto + inserção de blocos)

**Data:** 17/11/2026 (v1) · **Pacote final:** `Onda 2/01_FINALIZADO_subir-na-LMS/analise-de-dados-em-python-com-ia/analise-de-dados-em-python-com-ia-hands-on-scorm12-1P2wjd00-FINAL-com-blocos-v1.zip`

## 1. Material-fonte e mapeamento

Fonte: `Pesquisa Conteudo Onda 2/Ementa Completa/dados-com-python-e-ia-hands-on/roteiros/roteiro-articulate-hands-on.md`.
3 lições: L1 = Antes de arregaçar as mangas + Parte dos Dez · L2 = Oficinas 1 a 3 · L3 = Oficina 4 + Projeto Final + Parte dos Dez com exemplos.

## 2. Revisão de texto (fase A)

**227 campos alterados** (L1 46 · L2 94 · L3 87). `validar_texto.py`: estrutura preservada, 227 = 227.

**Erros de conteúdo corrigidos**
- **L1 — endereços truncados**: as quatro bases apontavam só para o domínio (api.bcb.gov.br, dados.cvm.gov.br…), sem o caminho do arquivo. Endereços completos restaurados.
- **L2 — "plano" inventado no lugar do brief da Oficina 1**: voltou o brief verbatim.
- **L3 — critério do Projeto Final errado**: "valores ausentes nas posições 26, 235, 453, 66 e 416" — são **contagens** de vazios por estação, não posições. Corrigido.
- **L3 — brief do INMET**: "arquivos com DF no nome" → "_DF_" (como no roteiro; "DF" casaria outros nomes).
- Títulos das lições alinhados às oficinas; cada oficina com 🎯 problema, 🧰 materiais, passos verbatim, ✅ ponto de controle, 🚑 Se travar e 🚀 Quer ir além em itens separados (antes vinham em parágrafos com hífens).
- A Parte dos Dez da L3 ganhou o exemplo de onde cada hábito foi usado; "Parabéns!" trocado pelo "Conseguiu! E agora?" do roteiro.

## 3. Inserções (fase B) — 7 blocos

| Lição | Posição | Tipo | Por quê |
|---|---|---|---|
| L1 | antes da questão | **HTML checklist de preparação (6 itens) + Continue que trava** | 4 downloads (um de 103 MB), uv e modo seguro antes da Oficina 1 |
| L2 | após os objetivos | título + **lista "O mapa da mão na massa"** | o mapa das oficinas tinha sido omitido |
| L2 | fim da Oficina 2 | **Questão em cenário** (460 linhas, 458 empresas, Vivara no topo) | a Oficina 2 não tinha verificação |
| L3 | após os critérios do Projeto Final | **HTML checklist do Projeto Final + Continue que trava** | fecha com os números do gabarito do INMET |

## 4. Validações

- Fase A: `validar_texto.py` sem divergência; ponte **APROVADO** (0 erros, 0 avisos).
- Fase B: `validar.py` **APROVADO** (7 blocos; 305 IDs distintos); `verificar_scorm.py` final **APROVADO** (0 erros, 0 avisos).

## 5. Navegador (mock de LMS)

Visto: mapa e questão nova na L2; as duas travas mostram o cadeado e liberam; o fechamento aparece depois da trava da L3; console sem erros; HTMLs a 360 px sem rolagem horizontal.
**Não testado:** LMS real; `file://`; execução real dos scripts com o agente.

## 6. Decisões tomadas

- Process "Resumo" de cada oficina descreve o que fica na pasta, para não repetir o ponto de controle do accordion logo abaixo.
