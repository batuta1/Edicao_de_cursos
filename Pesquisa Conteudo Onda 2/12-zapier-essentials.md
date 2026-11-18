# Pesquisa de conteúdo bruto — Zapier

| Campo | Valor |
|---|---|
| Assunto | Zapier |
| Registros | `zapier-essentials` e `zapier-hands-on` |
| Produtos | Ementa completa, curso Essentials e curso Hands On |
| Onda | 2 (ranking #50, 84 pontos) |
| Ferramenta-âncora | Zapier |
| Trilhas | T10 — Automação e agentes com n8n, pos. 8; C6 — Automação e assistentes de conteúdo, pos. 3; F4 — Automação, atendimento e agentes no negócio, pos. 8 |
| Versão | 7 (18 de novembro de 2026), alinhada à planilha v0.4 |
| Arquivo de saída | `ConteudoBruto_zapier.txt` |

## Como usar

Cole o prompt no ChatGPT Work. Salve o TXT, materiais e páginas em
`Pesquisa Conteudo Onda 2/conteudo-bruto/zapier/`.

## Prompt

```text
# PAPEL
Reúna CONTEÚDO BRUTO verificável para a IAClube.com criar ementa, Essentials e
Hands On. Não escreva o curso. Data: 18 de novembro de 2026. Confirme interface,
produtos, planos, tarefas/créditos, limites, IA, segurança e Brasil nesta data.

# OS CURSOS
- Assunto: Zapier.
- Produtos: ementa; Essentials 100–130 min; Hands On 60–90 min, 4 oficinas e projeto.
- Competência: projetar, construir, testar e operar automações no-code confiáveis.
- Tarefa observável: mapear um processo, criar um Zap com gatilho e ações,
  transformar/filtrar dados, testar, publicar, monitorar e corrigir falhas.
- Público: comunicação/marketing, operações, atendimento, finanças e pequenos negócios.
- Pré-requisito: uso básico de apps web; Hands On após Essentials.
- Encaixe: T10 pos. 8; C6 pos. 3; F4 pos. 8.
- Fora do escopo: série completa de n8n; APIs/código avançado; agentes de IA em
  profundidade; RPA de desktop; automação de TI; decisões financeiras automáticas.

# NECESSIDADES E PROFUNDIDADE
Defina automação para leigos. Traga menus exatos/origem, plano, consumo de tarefas,
passos, erros, recuperação e critério de êxito. Priorize interface e operação;
webhooks/APIs avançados vão ao apêndice. Use contas de teste e dados fictícios.

# PARTE GERAL
Identidade/histórico; acesso/planos/preços/limites; primeiros passos; glossário;
funcionalidades; casos reais; boas práticas; segurança/LGPD; erros; comparação;
novidades; material oficial; exercícios curtos, oficinas e projetos.

# FOCO ESPECÍFICO
1. Mapa atual de produtos: Zaps, Tables, Interfaces/Forms, Chatbots, Agents,
   Canvas e outros; confirme nomes e fronteiras.
2. Conceitos: trigger, action, task, run, step, field mapping, sample/test data,
   connection, polling, instant trigger e webhook.
3. Fluxo completo: mapear processo, escolher apps/eventos, conectar contas,
   testar gatilho, mapear, testar ações, publicar e monitorar.
4. Filtros, Paths, Formatter, Delay, Schedule, Looping, Storage/Tables e tratamento
   de datas/texto/números; plano exigido e exemplos.
5. Teste seguro, dados de amostra, replay/reprocessamento, duplicidade,
   idempotência, ordem, rate limits e prevenção de loops.
6. Histórico, alertas, diagnóstico, versionamento, desligamento e recuperação.
7. Planos, tarefas, limites, cobrança excedente, usuários, pastas e governança.
8. Segurança: OAuth, credenciais, menor privilégio, segredos, contas compartilhadas,
   dados pessoais, DPA, retenção e LGPD.
9. Zapier AI/Agents/Copilot: capacidades atuais, limites, revisão humana e fronteira
   com curso de agentes.
10. Comparação com n8n, Make e Power Automate por critérios verificáveis, sem slogan.
11. Casos reais em marketing, conteúdo, atendimento e finanças; riscos e métricas.
12. Práticas com apps gratuitos e dados fictícios: captura de lead, calendário,
    conteúdo, notificação e registro, com modo de testar sem afetar pessoas reais.

# FONTES, MATERIAIS E REGRAS
Priorize Zapier Help, Learn, preços, limites de tarefas, segurança, privacidade,
status e templates oficiais; depois avaliações independentes. Liste guias, vídeos,
templates, CSVs e checklists em MATERIAIS PARA BAIXAR. Procure matriz de planos,
documentação de cada recurso, guias de teste/erros, segurança e templates práticos.

Não invente; use NÃO ENCONTRADO. [CONFIRMADO] literal; [VERIFICAR] incerteza;
[SUGESTÃO] elaboração. Dê data/fonte a números, marque origem de menus, diferencie
planos, teste links e liste uma página por item. Tudo autoinstrucional.

# ENTREGA
Entregue `ConteudoBruto_zapier.txt` UTF-8 com seções 0–20: Resumo; Identidade;
Acesso; Primeiros passos; Glossário; Funcionalidades; Casos; Boas práticas;
Segurança; Limitações/erros; Comparação; Novidades; Material didático; Exercícios
13a/13b/13c; Foco; Trechos; Materiais; Páginas; Lacunas; Apêndice; Fontes.

# CHECKLIST
[ ] Sustenta ementa, Essentials e Hands On.
[ ] Consumo de tarefas, planos e limites estão atuais e com fonte.
[ ] Cada etapa tem passos, teste seguro e critério de êxito.
[ ] Falhas, duplicidade, loops, segurança e LGPD foram cobertos.
[ ] Todos os focos têm resposta ou NÃO ENCONTRADO.
[ ] Sugestões não estão [CONFIRMADO]; links e templates foram testados.
```
