# Análise Crítica 360 — Cursor Essentials v1.0

## 1. Sumário Executivo

**Nota: 8,3/10.** A versão apresenta progressão clara e coloca segurança e revisão no centro. Ainda precisa transformar algumas formulações gerais em caminhos de interface verificáveis, distinguir com mais precisão checkpoint e Git e tornar explícita a volatilidade de planos, modelos e menus.

## 2. Pontos Positivos (Fortalezas)

- O Módulo 0 impede que o primeiro uso ocorra antes da preparação de dados, permissões e reversibilidade.
- A sequência modo → prompt → plano → revisão reduz a carga cognitiva de iniciantes.
- O fio condutor “IA propõe; pessoa valida” reaparece nos exercícios e na síntese.
- A exclusão da antiga edição inline evita ensinar um fluxo aposentado.
- O uso do Gilded Rose cria uma aplicação reproduzível com requisitos e testes.

## 3. Pontos Negativos e Gargalos (Debilidades)

- Os caminhos de instalação e configurações ainda não diferenciam sistemas operacionais.
- A contradição oficial sobre aprovação padrão de terminal não aparece no texto.
- `.cursorignore` pode ser interpretado como barreira absoluta, embora terminal e MCP possam contorná-lo.
- Ask, Plan, Debug e Agent são apresentados corretamente, mas faltam sinais de escolha em cenários ambíguos.
- O exercício de revisão precisa exigir evidência concreta: comando, resultado e justificativa.
- Preços e modelos são voláteis e não devem integrar objetivos avaliados.

## 4. Matriz de Soluções e Melhorias

| Gargalo | Onde ocorre | Correção concreta | Prioridade |
|---|---|---|---|
| Setup genérico | Módulo 0 | Acrescentar passos separados para Windows, macOS e Linux e ponto de controle de login | Alta |
| Padrão de aprovação contraditório | Módulo 0 | Declarar a contradição e orientar conferência manual do modo atual | Alta |
| Limite de ignore pouco visível | Módulo 0 | Inserir aviso de que comandos e MCP podem ler arquivos ignorados | Alta |
| Modos sem heurística | Módulo 1 | Incluir tabela “intenção → modo → risco” | Média |
| Prompt sem molde reutilizável | Módulo 2 | Fornecer estrutura editável objetivo/contexto/restrições/validação | Média |
| Revisão sem registro padronizado | Módulo 4 | Exigir tabela arquivo/efeito/evidência/decisão | Alta |
| Conteúdo volátil | Identificação e README | Datar a fonte e listar itens a reconferir antes da publicação | Alta |

## 5. Roadmap de Expansão

Cabem neste curso: Rules e `AGENTS.md` como extensão opcional; seleção consciente de modelo sem listar preços fixos. Ficam para cursos seguintes: Cloud Agents, Bugbot, CLI, MCP, automações, Origin, segurança corporativa e agentes paralelos.

