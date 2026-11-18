# Pesquisa de conteúdo bruto — Agentes Web

| Campo | Valor |
|---|---|
| Assunto | Agentes Web |
| Registros no catálogo | `agentes-web-hands-on` e `agentes-web-essentials` |
| Produtos que sairão desta pesquisa | Ementa completa, curso Essentials e curso Hands On |
| Onda | 2 (ranking #22, 86 pontos) |
| Ferramentas-âncora | Perplexity Comet e ChatGPT Atlas |
| Tema | Agentes de IA que navegam e executam tarefas na web |
| Trilhas | T3 — Agentes e MCP (posição 8; depois de Claude Cowork - Hands On e antes de Multiagentes - Essentials)<br>T13 — Navegadores e agentes web |
| Pesquisa feita por | ChatGPT Work |
| Versão do prompt | 7 (18 de novembro de 2026): versão 6 ampliada para pares Essentials/Hands On e alinhada à planilha de produção v0.4 |
| Arquivo que o ChatGPT deve entregar | `ConteudoBruto_agentes-web.txt` |

## Como usar

1. Abra o ChatGPT Work e cole todo o bloco **Prompt** abaixo.
2. Salve o arquivo entregue em `Pesquisa Conteudo Onda 2/conteudo-bruto/agentes-web/`.
3. Baixe os itens de **MATERIAIS PARA BAIXAR** e salve as páginas de **PÁGINAS PARA SALVAR** na mesma pasta.
4. Revise **LACUNAS E PONTOS A VERIFICAR** antes de criar a ementa.

## Prompt

```text
# PAPEL
Você é um pesquisador de conteúdo a serviço de uma equipe brasileira de design
instrucional (IAClube.com). Pesquise na internet e reúna o CONTEÚDO BRUTO para a
ementa completa e os roteiros Essentials e Hands On. Não escreva a ementa, o
curso nem o plano de aula. Colete, organize e referencie matéria-prima verificável.

Data de hoje: 18 de novembro de 2026. Confronte nomes, menus, planos, preços,
limites e disponibilidade com esta data.

# OS CURSOS QUE SERÃO CRIADOS COM ESTA PESQUISA
- Assunto: Agentes Web.
- Produtos: uma ementa integral; um Essentials autoinstrucional de 100 a 130
  minutos, com 4 a 6 módulos; e um Hands On autoinstrucional de 60 a 90 minutos,
  com 4 oficinas e 1 projeto final. A mesma pesquisa precisa sustentar os três.
- Ferramentas-âncora: Perplexity Comet e ChatGPT Atlas. Confirme os nomes,
  disponibilidade, plataformas e estado atual dos produtos; se algum mudou de
  nome, foi encerrado, está em beta ou não está disponível no Brasil, registre.
- Competência: delegar tarefas de navegação a agentes com controle e verificação.
- Tarefa observável: configurar um agente web, dar uma tarefa com limites,
  acompanhar a navegação, intervir quando necessário e validar o resultado e as ações.
- Público: profissionais de conhecimento, pesquisa, atendimento, operações,
  comunicação e tecnologia que já usam assistentes de IA, sem exigir programação.
- Pré-requisito: Agentes de IA - Essentials e uso básico de navegador. Para o
  Hands On, o aluno terá feito também o Essentials deste assunto.
- Idioma e país: português, Brasil.
- Encaixe: T3 — Agentes e MCP, posição 8, depois de Claude Cowork - Hands On e
  antes de Multiagentes - Essentials; e T13 — Navegadores e agentes web.
- Fora do escopo: fundamentos gerais de agentes (Agentes de IA); deep research
  sem ação na web (Deep Research); automações determinísticas no Zapier/n8n;
  coordenação de vários agentes (Multiagentes); uso completo de um navegador sem
  recursos agênticos; APIs e desenvolvimento de agentes próprios.

# POR QUE A EQUIPE PRECISA DE CADA COISA
- O texto será “Para Leigos”: defina termos e use analogias sem esconder riscos.
- O curso não usa capturas de tela: traga nomes exatos de menus em pt-BR e inglês,
  com origem (interface), (ajuda pt-BR) ou (ajuda en).
- Para cada ação, informe passo a passo, plano necessário, permissões, como
  interromper/desfazer e o sinal observável de êxito.
- Para o Hands On, encontre materiais públicos, gratuitos e sem login e indique
  o resultado esperado para autocorreção.
- Separe fatos da fabricante, evidência independente e sugestões didáticas.

# REGRA DE PROFUNDIDADE
Priorize o que o aluno vê e faz. Arquitetura, APIs e detalhes para desenvolvedores
vão ao APÊNDICE TÉCNICO. Pelo menos dois terços do conteúdo devem tratar da
experiência prática, do controle e da verificação pelo usuário.

# O QUE PESQUISAR — PARTE GERAL
1. Identidade, fabricante, lançamento, mudanças de nome e linha do tempo.
2. Acesso no Brasil, conta, plataformas, requisitos, planos, preços e limites.
3. Primeiros passos com menus e botões exatos.
4. Glossário para leigos.
5. Funcionalidades, localização, plano, limites e disponibilidade regional.
6. Casos reais publicados para os públicos do curso; marque NÃO ENCONTRADO quando faltar.
7. Boas práticas e prompts publicados pela fabricante.
8. Segurança, privacidade, retenção, treinamento, permissões e LGPD.
9. Limitações, falhas conhecidas, erros comuns, recuperação e suporte.
10. Comparação imparcial com alternativas.
11. Novidades dos últimos 12 meses, beta e anúncios ainda não disponíveis.
12. Materiais didáticos oficiais.
13. Exercícios: decomponha a tarefa observável e cubra cada ação com prática
    curta, oficina e pelo menos duas opções de projeto final.

# O QUE PESQUISAR — FOCO ESPECÍFICO
Responda todos os itens; use NÃO ENCONTRADO e diga onde procurou.
1. Definição operacional de agente web, navegador com IA, automação de navegador,
   deep research e copiloto; diferenças e fronteiras.
2. Comet: instalação, conta, Assistant, automações/agentes, contexto de abas,
   pesquisa, execução de ações, histórico, permissões e controles de segurança.
3. ChatGPT Atlas: existência e nome atuais, instalação, planos, modo agente,
   memória/contexto, execução de ações, confirmações e controles.
4. Para cada ferramenta: tarefa simples completa, da instrução ao resultado,
   com caminhos de menu e pontos em que o usuário precisa confirmar ou intervir.
5. Capacidades e limites para pesquisar, preencher formulários, comparar opções,
   fazer reservas/compras sem concluir pagamento, trabalhar em sistemas e baixar arquivos.
6. Tratamento de login, MFA, CAPTCHA, paywall, anexos, pop-ups, downloads,
   conteúdo malicioso e páginas que tentam instruir o agente.
7. Prompt injection indireta e outras ameaças específicas de navegação; estudos,
   system cards, red teaming e incidentes documentados.
8. Permissões, isolamento, dados de navegação, histórico, memória, treinamento,
   modo privado/incógnito e controles corporativos.
9. Como observar o plano, pausar, assumir o controle, cancelar, revisar ações,
   desfazer e auditar o que ocorreu.
10. Critérios para decidir o que pode ser delegado e o que exige ação humana;
    atenção especial a pagamentos, dados pessoais, saúde, jurídico e contas corporativas.
11. Comparação prática com agentes do Chrome/Edge/Opera, Claude no Chrome,
    ChatGPT agent e automação RPA, sem transformar o curso em catálogo.
12. Materiais de prática seguros: sites sandbox ou páginas públicas que permitam
    busca, comparação, preenchimento sem envio e organização de informação.

# FONTES
Priorize documentação, ajuda, preços, políticas, system cards e status oficiais;
depois pesquisa acadêmica/institucional e imprensa confiável; comunidade apenas
como evidência identificada. Prefira pt-BR, depois inglês. Use páginas públicas
do Brasil e nunca ambientes dev, hml, staging ou qa. Registre título, URL, tipo,
data da fonte e data de acesso.

# MATERIAIS QUE NÃO SÃO PÁGINAS DA WEB
Liste PDFs, relatórios, system cards, vídeos, transcrições, arquivos de exemplo e
guias em MATERIAIS PARA BAIXAR, com título, link, tipo, idioma, utilidade, licença
e nome sugerido. Marque [ACESSO RESTRITO] quando necessário e só declare BAIXADO
após conferir o tipo e o conteúdo. Procure especialmente: documentação e guias
oficiais de Comet e Atlas; system cards e relatórios de segurança; estudos sobre
prompt injection em agentes web; políticas de privacidade; materiais de prática.

# REGRAS
1. Não invente. Use NÃO ENCONTRADO e informe onde procurou.
2. Use apenas [CONFIRMADO] para o que a fonte diz literalmente, [VERIFICAR] para
   evidência insuficiente/contraditória e [SUGESTÃO] para elaboração sua.
3. Registre datas para preços, limites, planos, menus e recursos instáveis.
4. Atribua cada número à fonte que realmente o contém.
5. Indique a origem de cada nome de menu.
6. Transcreva apenas trechos essenciais permitidos e liste as páginas oficiais
   completas em PÁGINAS PARA SALVAR, um item por página.
7. Teste links de exercício; devem ser públicos e não exigir login.
8. Diferencie gratuito, teste, pago, individual, equipe e corporativo.
9. Não escreva módulos, objetivos, plano de aula ou divisão em tempo.
10. Escreva em português do Brasil e preserve nomes oficiais em inglês.
11. Tudo deve funcionar sem instrutor.

# FORMATO DE ENTREGA
Entregue um TXT UTF-8 chamado ConteudoBruto_agentes-web.txt, com:
0. RESUMO EXECUTIVO
1. IDENTIDADE E HISTÓRICO
2. ACESSO, PLANOS E REQUISITOS
3. PRIMEIROS PASSOS
4. CONCEITOS E GLOSSÁRIO
5. FUNCIONALIDADES
6. CASOS DE USO PARA O PÚBLICO
7. BOAS PRÁTICAS E PROMPTS
8. SEGURANÇA, PRIVACIDADE E DADOS
9. LIMITAÇÕES, ERROS E SOLUÇÃO DE PROBLEMAS
10. COMPARAÇÃO COM ALTERNATIVAS
11. NOVIDADES E RECURSOS INSTÁVEIS
12. MATERIAL DIDÁTICO EXISTENTE
13. IDEIAS DE EXERCÍCIO (13a curtos; 13b oficinas; 13c projetos finais)
14. RESPOSTAS AO FOCO ESPECÍFICO
15. TRECHOS DA DOCUMENTAÇÃO OFICIAL
16. MATERIAIS PARA BAIXAR
17. PÁGINAS PARA SALVAR
18. LACUNAS E PONTOS A VERIFICAR
19. APÊNDICE TÉCNICO
20. FONTES CONSULTADAS
Cite cada afirmação com o número da fonte da seção 20.

# ANTES DE ENTREGAR, CONFIRA
[ ] Estrutura, títulos e arquivo seguem o pedido.
[ ] A pesquisa sustenta ementa, Essentials e Hands On.
[ ] Cada ação da tarefa tem passo a passo e exercício.
[ ] Todos os itens do foco foram respondidos ou marcados NÃO ENCONTRADO.
[ ] Nenhuma elaboração foi marcada [CONFIRMADO].
[ ] Casos de uso são reais; hipóteses estão como [SUGESTÃO].
[ ] Menus têm origem e recursos distinguem planos e região.
[ ] Links de exercício foram testados.
[ ] Todo material não-web citado está na seção 16.
[ ] A seção 17 tem um item por página.
[ ] Riscos de prompt injection, permissões e ações sensíveis foram cobertos.
[ ] Pelo menos dois terços tratam do que o aluno vê e faz.
```
