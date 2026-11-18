# Análise Crítica 360 — Cursor Hands-on v1.0

## 1. Sumário Executivo

**Nota: 8,5/10.** O curso entrega um fluxo real e verificável. A maior fragilidade é depender de caminhos de interface que mudam rapidamente e pressupor que o kata escolhido já executa testes sem preparação adicional.

## 2. Pontos Positivos (Fortalezas)

- Cada oficina resolve um problema reconhecível e entrega uma vitória observável.
- O projeto final não é mera repetição: exige registrar decisão e evidência.
- O tom é direto sem tratar o iniciante como incapaz.
- As oficinas impedem edição precoce e proíbem alteração oportunista dos testes.
- O troubleshooting cobre contexto, escopo, permissões e timeout.

## 3. Pontos Negativos e Gargalos (Debilidades)

- O curso não escolhe uma linguagem específica do Gilded Rose, o que pode tornar comandos de teste ambíguos.
- O commit inicial é sugerido, mas faltam critérios para repositório já sujo.
- “Clique em Build” pode mudar de nome ou posição.
- O aluno pode aceitar comandos destrutivos sem compreender seus efeitos.
- A Oficina 4 precisa separar teste automatizado de inspeção manual.
- Os desafios “Quer ir além?” ainda têm apenas um item, enquanto o roteiro Articulate exige três.

## 4. Matriz de Soluções e Melhorias

| Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|
| Linguagem não definida | Antes de começar | Orientar escolha de uma implementação cujo teste local já tenha sido executado | Alta |
| Repositório sujo | Oficina 1 | Acrescentar decisão: guardar, commitar ou usar cópia limpa antes do Agent | Alta |
| Interface volátil | Oficinas 2 e 3 | Manter breadcrumb e nota para procurar o nome atual do modo | Média |
| Comando destrutivo | Oficinas 1 e 3 | Inserir checagem de comando, diretório, efeitos e reversão antes da aprovação | Alta |
| Validação pouco separada | Oficina 4 | Criar checklist com testes, lint/build e inspeção do comportamento | Alta |
| Extensões insuficientes | Todas | Expandir para três desafios com instrução e validação | Média |

## 5. Roadmap de Expansão

Cabem como opcionais: regras do projeto, TDD estrito e autorrevisão. Ficam fora: Cloud Agents, Bugbot, CLI, MCP, múltiplos agentes e integrações corporativas.

