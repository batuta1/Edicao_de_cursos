# Pesquisa de conteúdo bruto — IA para Reuniões

| Campo | Valor |
|---|---|
| Assunto | IA para Reuniões |
| Registros no catálogo | `ia-para-reunioes-essentials` e `ia-para-reunioes-hands-on` |
| Produtos | Ementa completa, curso Essentials e curso Hands On |
| Onda | 2 (ranking #33, 86 pontos) |
| Ferramentas-âncora | Otter.ai, Fireflies.ai e Microsoft 365 Copilot |
| Trilhas | T9 — Apresentações e reuniões, posição 4<br>C5 — Apuração, checagem e pesquisa de audiência, posição 5<br>F3 — Documentos, propostas e apresentações de negócio, posição 6<br>S3 — Documentação clínica e comunicação, posição 5 |
| Versão do prompt | 7 (18 de novembro de 2026), alinhada à planilha v0.4 |
| Arquivo de saída | `ConteudoBruto_ia-para-reunioes.txt` |

## Como usar

Cole o prompt no ChatGPT Work. Salve o TXT, os materiais baixados e as páginas
convertidas em PDF em `Pesquisa Conteudo Onda 2/conteudo-bruto/ia-para-reunioes/`.
Revise as lacunas antes da ementa.

## Prompt

```text
# PAPEL
Reúna CONTEÚDO BRUTO verificável para a IAClube.com criar a ementa completa e os
cursos Essentials e Hands On. Não escreva o curso, a ementa ou o plano de aula.
Data de hoje: 18 de novembro de 2026. Confirme recursos, menus, planos, preços,
limites, integrações, idiomas e disponibilidade no Brasil nesta data.

# OS CURSOS
- Assunto: IA para Reuniões.
- Produtos: ementa integral; Essentials autoinstrucional de 100–130 min; Hands On
  autoinstrucional de 60–90 min, com 4 oficinas e projeto final.
- Âncoras: Otter.ai, Fireflies.ai e Microsoft 365 Copilot.
- Competência: preparar, registrar, resumir e transformar reuniões em ações com
  consentimento, revisão e rastreabilidade.
- Tarefa observável: configurar captura/transcrição, obter notas e resumo,
  conferir o registro, extrair decisões e tarefas e compartilhar com segurança.
- Público: profissionais de conhecimento e negócios; jornalistas/pesquisadores;
  equipes de saúde. Nenhum conhecimento técnico.
- Pré-requisito: uso básico de videoconferência e assistente de IA; Hands On após Essentials.
- Encaixe: T9 pos. 4; C5 pos. 5; F3 pos. 6; S3 pos. 5.
- Fora do escopo: apresentações; edição geral de áudio/podcast; documentação
  clínica automatizada sem validação; vigilância de empregados; Microsoft 365
  Copilot completo; gravação sem consentimento.

# NECESSIDADES E PROFUNDIDADE
Explique termos para leigos. Traga menus exatos e origem, passo a passo, plano,
limites, erros, como corrigir e sinal de êxito. Priorize a experiência do usuário;
APIs/admin vão ao apêndice. Para práticas, use reuniões simuladas ou gravações
públicas autorizadas, com transcrição/gabarito verificável.

# PARTE GERAL
Identidade/histórico; acesso/planos/preços; primeiros passos; glossário;
funcionalidades; casos reais; boas práticas; privacidade/LGPD; limitações/erros;
comparação; novidades; materiais oficiais; exercícios curtos, oficinas e projetos.

# FOCO ESPECÍFICO
1. Fluxo antes/durante/depois: pauta, convite, consentimento, captura, transcrição,
   resumo, decisões, tarefas, acompanhamento e descarte.
2. Otter.ai: bot/notetaker, gravação, transcrição, identificação de falantes,
   resumo, chat, clips, integrações, exportação, idiomas e planos.
3. Fireflies.ai: equivalentes atuais, integração com calendários/plataformas,
   canais, análise, busca, tarefas, exportação e planos.
4. Microsoft 365 Copilot em Teams: transcrição, recap, Intelligent Recap/Copilot,
   perguntas sobre reunião, tarefas, requisitos de licença e política do tenant.
5. Presencial, híbrida e online; Windows/macOS/mobile; upload de gravação versus bot.
6. Qualidade de transcrição em português do Brasil: sotaques, sobreposição,
   ruído, termos técnicos, nomes próprios e métricas/estudos independentes.
7. Método de conferência: voltar ao timestamp, distinguir fala de inferência,
   corrigir falantes, decisões e tarefas; preservar rastreabilidade.
8. Consentimento e legislação no Brasil: gravação, dados pessoais/sensíveis,
   relações de trabalho, atendimento, pesquisa jornalística e saúde; não dê
   aconselhamento jurídico, cite fontes oficiais e marque incertezas.
9. Saúde: riscos de usar resumo como prontuário, validação por profissional,
   sigilo, requisitos institucionais e proibição de inferir diagnóstico.
10. Controles: retenção, exclusão, treinamento, compartilhamento, convidados,
    conta corporativa, DPA e administração.
11. Casos reais e critérios de escolha; diferencie material da fabricante.
12. Práticas com áudio autorizado: pauta, transcrição imperfeita, revisão,
    ata, decisões e lista de tarefas com responsáveis/prazos.

# FONTES, MATERIAIS E REGRAS
Priorize ajuda, preços, políticas, trust centers e documentação oficial; depois
estudos independentes e fontes brasileiras oficiais. Prefira pt-BR e inglês.
Liste PDFs, vídeos/transcrições, modelos de pauta/ata, amostras de áudio e políticas
em MATERIAIS PARA BAIXAR. Procure guias de consentimento, privacidade, idiomas,
limites, Microsoft Teams/Copilot e estudos de acurácia.

Não invente: use NÃO ENCONTRADO. [CONFIRMADO] só para o que a fonte diz;
[VERIFICAR] para evidência fraca/contraditória; [SUGESTÃO] para elaboração.
Registre datas, atribua números à fonte correta, marque origem de menus, diferencie
planos e teste links. Liste uma página por item em PÁGINAS PARA SALVAR. Curso
autoinstrucional; não escreva módulos ou objetivos.

# ENTREGA
Entregue `ConteudoBruto_ia-para-reunioes.txt` em UTF-8 com seções 0 a 20:
Resumo; Identidade; Acesso; Primeiros passos; Glossário; Funcionalidades; Casos;
Boas práticas; Segurança/privacidade; Limitações; Comparação; Novidades; Material
didático; Exercícios (13a curtos, 13b oficinas, 13c projetos); Foco; Trechos;
Materiais; Páginas; Lacunas; Apêndice técnico; Fontes. Cite cada informação.

# CHECKLIST
[ ] Sustenta ementa, Essentials e Hands On.
[ ] Cobre consentimento, LGPD, retenção, saúde e rastreabilidade.
[ ] Todos os itens do foco têm resposta ou NÃO ENCONTRADO.
[ ] Cada ação tem passo a passo, material e critério de êxito.
[ ] Planos, idiomas, região, menus e datas estão claros.
[ ] Sugestões não estão [CONFIRMADO]; links foram testados.
```
