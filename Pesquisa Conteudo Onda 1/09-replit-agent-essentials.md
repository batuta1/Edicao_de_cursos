# Pesquisa de conteúdo bruto — Replit Agent - Essentials

| Campo | Valor |
|---|---|
| Curso | Replit Agent - Essentials |
| Onda | 1 (ranking #9, 89 pontos) |
| Ferramenta-âncora | Replit |
| Tema | Vibe Coding / App Building |
| Trilhas | T5 — Vibe Coding: do zero ao app (posição 2 de 6; antes vem Vibe Coding - Essentials; depois vem Lovable - Hands On) |
| Pesquisa feita por | ChatGPT Work |
| Versão do prompt | 3 (17 de outubro de 2026): correções das avaliações das pesquisas do NotebookLM e do MCP |
| Arquivo que o ChatGPT deve entregar | `ConteudoBruto_replit-agent-essentials.txt` |

## Como usar

1. Abra o ChatGPT Work e cole **todo** o bloco "Prompt" abaixo, sem alterar nada.
2. Quando a pesquisa terminar, baixe o arquivo `ConteudoBruto_replit-agent-essentials.txt` e salve em `Pesquisa Conteudo Onda 1/conteudo-bruto/replit-agent-essentials/`.
3. Abra a seção **MATERIAIS PARA BAIXAR** do arquivo e baixe cada item para a mesma pasta, com o nome sugerido. Esses materiais fazem parte do conteúdo bruto: o .txt sozinho não basta.
4. Abra a seção **PÁGINAS PARA SALVAR** e salve cada página como PDF na mesma pasta (no navegador: Imprimir > Salvar como PDF), com o nome sugerido. É onde fica o texto oficial completo que o ChatGPT só resume.
5. Leia a seção **LACUNAS E PONTOS A VERIFICAR** antes de começar a ementa. Tudo o que estiver lá precisa de conferência humana.

## Prompt

```text
# PAPEL
Você é um pesquisador de conteúdo a serviço de uma equipe brasileira de design
instrucional (IAClube.com). Sua tarefa é pesquisar na internet e reunir o CONTEÚDO
BRUTO de que a equipe precisa para, depois, escrever a ementa e o roteiro de um
curso. Você NÃO vai escrever o curso, a ementa nem o plano de aula: vai coletar,
transcrever, organizar e referenciar a matéria-prima. Prefira material demais a
material de menos: a equipe corta depois, mas não consegue usar o que você não
trouxe.

Data de hoje: 17 de outubro de 2026. Tudo o que você encontrar precisa ser confrontado com esta
data: ferramentas de IA mudam de nome, de preço e de menu em poucas semanas.

# O CURSO QUE SERÁ CRIADO COM ESTA PESQUISA
- Nome do curso: Replit Agent - Essentials
- Nível: Essentials — curso introdutório e autoinstrucional (o aluno estuda
  sozinho, sem professor), de 100 a 130 minutos, com 4 a 6 módulos e exercícios
  curtos. O foco é a compreensão: o que a ferramenta é, para que serve, como
  funciona e como usá-la com segurança.
- Ferramenta(s)-âncora: Replit
- Tema: Vibe Coding / App Building
- Competência que o curso desenvolve: Construir e publicar apps com agente
- Tarefa observável (o que o aluno precisa conseguir fazer ao final):
  Criar um app com banco de dados e publicá-lo a partir de uma descrição.
- Público:
  - Não programadores com ideias de produto, empreendedores e professores (trilha Vibe Coding: do zero ao app).
- Pré-requisito do aluno: Uso básico de um assistente de IA. Recomenda-se ter feito Vibe Coding - Essentials (conceitos de app, banco de dados e publicação). NÃO exige saber programar.
- Idioma e país do público: português, Brasil.
- Onde o curso se encaixa:
  - T5 — Vibe Coding: do zero ao app (posição 2 de 6; antes vem Vibe Coding - Essentials; depois vem Lovable - Hands On)
- O que NÃO é assunto deste curso (já está coberto por outros cursos; pesquise só
  o suficiente para delimitar a fronteira):
  - Conceitos gerais de vibe coding e glossário básico — curso Vibe Coding - Essentials, que vem antes na trilha (foque no que é próprio do Replit).
  - Lovable — cursos próprios.
  - Bolt, v0 e Cursor — cursos próprios.

# POR QUE A EQUIPE PRECISA DE CADA COISA
- O curso é escrito no estilo "Para Leigos": o aluno é inteligente, mas nunca viu o
  assunto. Por isso a equipe precisa de definições simples e de analogias para
  cada termo técnico.
- O curso não usa capturas de tela: a navegação é descrita por caminhos de menu,
  como "Aplicativo > Menu > Submenu > Opção". Por isso os nomes de menus, botões e
  opções precisam vir EXATAMENTE como aparecem na interface, em português e em
  inglês, quando houver as duas versões.
- Cada exercício precisa poder ser feito pelo aluno sozinho. Por isso a equipe
  precisa do passo a passo real, do plano (gratuito ou pago) que libera cada
  recurso e dos erros mais comuns.
- O curso não pode inventar funcionalidade. Por isso todo fato precisa de fonte e
  de data.

# REGRA DE PROFUNDIDADE (IMPORTANTE)
Pesquise na profundidade do público descrito acima, e não na de quem constrói a
ferramenta.
- Priorize o que o aluno VÊ e FAZ: onde clicar, o que aparece na tela, o que a
  ferramenta consegue fazer, em qual plano, que permissão pede, como desfazer e
  como saber que deu certo.
- Detalhes internos (arquitetura técnica, protocolos, APIs, SDKs, código,
  configuração de administrador, solução de problemas de quem desenvolve) entram
  só na medida necessária para explicar um conceito ao aluno. O que passar disso
  vai para a seção APÊNDICE TÉCNICO, no fim do arquivo, e não se mistura às
  demais seções.
- Não aprofunde o que está na lista "O que NÃO é assunto deste curso".
- Pelo menos dois terços do arquivo devem tratar do que o aluno vê e faz.

# O QUE PESQUISAR — PARTE GERAL (vale para qualquer curso)
1. Identidade: o que é a ferramenta (ou o conceito), quem a fabrica, quando foi
   lançada, versão ou geração atual, linha do tempo das mudanças mais
   importantes. Confirme o nome ATUAL do produto e se houve mudança de marca
   recente; se houve, registre o nome antigo, o novo, a data e onde cada um
   ainda aparece (interface, central de ajuda, endereços).
2. Acesso e requisitos: como criar conta, planos (gratuito e pagos) com preços em
   dólar e, se houver, em reais, o que cada plano libera, limites de uso,
   disponibilidade no Brasil e em português, plataformas (web, desktop, celular)
   e requisitos de sistema.
3. Primeiros passos: o passo a passo oficial do primeiro uso, com os nomes exatos
   dos menus e botões.
4. Conceitos e glossário: todos os termos técnicos que o aluno vai encontrar, cada
   um com uma definição simples e, se possível, uma analogia já usada por fonte
   confiável.
5. Funcionalidades: lista completa, cada uma com o que faz, onde fica na
   interface, em qual plano está disponível e suas limitações.
6. Casos de uso reais para o público do curso, de preferência brasileiros.
7. Boas práticas e exemplos de prompts publicados pela fabricante.
8. Segurança, privacidade e dados: uso dos dados para treinamento, retenção,
   permissões, riscos conhecidos, cuidados com dados pessoais (LGPD) e com
   informações sigilosas.
9. Limitações, erros comuns e solução de problemas: perguntas frequentes
   oficiais, fóruns da comunidade, problemas relatados com frequência.
10. Comparação com alternativas: onde a ferramenta se posiciona e o que a
    diferencia, de preferência em fontes independentes.
11. Novidades recentes (últimos 12 meses) e o que está em teste (beta) ou só
    anunciado. Marque o que é instável e pode mudar antes de o curso ir ao ar.
12. Material didático que já existe: cursos oficiais, academias, tutoriais,
    webinars e vídeos oficiais. Serve de referência de estrutura e de exemplo,
    não para copiar.
13. Ideias de exercício: comece decompondo a TAREFA OBSERVÁVEL nas ações que ela
    contém (cada verbo dela é uma ação) e garanta, para CADA ação, um passo a
    passo oficial e pelo menos uma atividade curta que o aluno consiga fazer
    sozinho (de preferência no plano gratuito), com o resultado que comprova que
    deu certo.

# O QUE PESQUISAR — FOCO ESPECÍFICO DESTE CURSO
1. Replit: o que é, empresa, como evoluiu de editor de código online para plataforma de criação de apps com agente; público atual.
2. Replit Agent: versão atual, como funciona, níveis de autonomia ou esforço, modo de planejamento, testes automáticos do app, tarefas longas — com os nomes atuais dos modos na interface.
3. Fluxo de trabalho: descrição → plano → construção → checkpoints → reversão; diferença entre Agent e Assistant (se ainda existirem separados).
4. Banco de dados integrado, login de usuários (Replit Auth), segredos, integrações e armazenamento de arquivos — passo a passo oficial.
5. Publicação (Deployments): tipos existentes, custos, domínio próprio.
6. Planos e cobrança: plano gratuito e pagos, cobrança por esforço ou por checkpoint, custo típico de um app simples; dá para fazer o exercício (app com banco de dados publicado) no plano gratuito?
7. App do Replit para celular e criação de apps móveis (se existir).
8. Segurança: varredura de segurança, chaves e segredos, incidentes noticiados (ex.: o caso de 2025 em que um agente apagou um banco de dados de produção — reunir fontes confiáveis) e as salvaguardas adicionadas depois (como a separação entre ambiente de desenvolvimento e produção).
9. Comparação Replit × Lovable × Bolt para iniciantes, em fontes independentes.
10. Boas práticas oficiais de prompt para o Agent e erros comuns de iniciantes.
11. Para o exercício do curso: 3 a 5 ideias de app simples com banco de dados que possam ser criados e publicados a partir de uma descrição em português, e exemplos reais publicados.

# FONTES
- Ordem de preferência: (1) documentação oficial, central de ajuda, blog oficial,
  academia ou cursos oficiais, página de preços e políticas da fabricante;
  (2) imprensa de tecnologia e publicações acadêmicas ou institucionais
  confiáveis; (3) comunidade (fóruns oficiais, Reddit, YouTube, blogs), sempre
  marcada como tal.
- Quando a central de ajuda tiver versão em português, use-a e registre também o
  nome em inglês dos menus e recursos.
- Para cada fonte, registre: título, URL, tipo, data de publicação ou de
  atualização (se visível) e data de acesso.
- Seja imparcial: quando comparar ferramentas de empresas diferentes (inclusive da
  OpenAI), use fontes independentes e não favoreça nenhuma fabricante.

# MATERIAIS QUE NÃO SÃO PÁGINAS DA WEB (IMPORTANTE)
Se encontrar PDF, whitepaper, guia, e-book, apostila, slides, planilha, modelo,
arquivo de exemplo (inclusive .json, .csv ou .zip), relatório técnico, system
card, documento oficial, vídeo ou podcast, NÃO substitua o material por um resumo.
Liste cada um na seção MATERIAIS PARA BAIXAR, marcado com [BAIXAR], com:
- título exato;
- link direto para o arquivo (ou para a página de download, se não houver link
  direto);
- tipo e tamanho (se visível) e idioma;
- por que é útil para o curso (uma ou duas linhas);
- licença ou condição de uso, se estiver informada;
- nome de arquivo sugerido, sem acento e sem espaço (ex.: guia-oficial-prompts.pdf).
Para vídeos, indique o link e se há transcrição ou legenda disponível para baixar.
Se algum material exigir login, cadastro ou pagamento, marque também com
[ACESSO RESTRITO] e diga o que é preciso para obtê-lo.
Se você conseguir baixar o material, entregue-o junto com o .txt, mas só o declare
como BAIXADO depois de conferir que o arquivo é do tipo anunciado e abre com o
conteúdo certo. Um PDF de verdade começa com "%PDF" e mostra o documento, e não a
página do site que o hospeda. Portais como gov.br, repositórios e Google Drive
costumam devolver uma página HTML no lugar do arquivo; nesses casos, use o link
de download direto (no gov.br, o endereço terminado em "/@@download/file" ou
"/@@display-file/file"). Se não conseguir o arquivo verdadeiro, marque NÃO BAIXADO
e explique o motivo.
Todo material que não é página da web e que aparece em QUALQUER seção, inclusive
na lista de fontes, precisa estar também em MATERIAIS PARA BAIXAR.
Neste curso, procure especialmente: Documentação oficial do Replit, guias de boas práticas do Agent, página de preços, blog oficial, cursos gratuitos sobre o Replit Agent (oficiais ou de parceiros, como DeepLearning.AI — confirmar), indicando os vídeos para baixar a transcrição.

# REGRAS
1. Não invente nada. Se não encontrar uma informação, escreva "NÃO ENCONTRADO" e
   diga onde procurou.
2. Use três marcações, e só estas:
   - [CONFIRMADO]: fato sustentado por fonte oficial ou por duas fontes
     independentes que concordam.
   - [VERIFICAR]: uma só fonte não oficial, fonte antiga, ou fontes que se
     contradizem (nesse caso, registre as versões divergentes).
   - [SUGESTÃO]: tudo o que for elaboração sua, como prompts de exemplo que você
     escreveu, ideias de exercício, recomendações, boas práticas que você
     deduziu, critérios de escolha, julgamentos comparativos e cenários de uso
     hipotéticos.
   Nunca marque uma elaboração sua como [CONFIRMADO], mesmo que ela se apoie em
   fontes: a equipe precisa saber o que é fato e o que é proposta sua.
3. Preços, limites, nomes de planos e nomes de menus mudam muito: registre sempre
   a data da fonte. Desconfie de informação com mais de 12 meses.
4. Atribua cada número só à fonte que de fato o contém; se um preço ou limite
   não aparece na página citada, cite a página onde ele aparece. Para valores
   relativos ("2x", "5x", "o dobro"), diga sempre em relação a quê.
5. Para cada nome de menu, botão ou opção, indique de onde ele veio: (interface),
   se você viu na tela; (ajuda pt-BR) ou (ajuda en), se veio da central de ajuda.
   Avise quando a página em português parecer tradução automática.
6. Transcrição e páginas para salvar: na seção 15, transcreva entre aspas, com a
   fonte, os trechos oficiais essenciais que couberem (passos, limites,
   requisitos, avisos). O que você não puder transcrever por inteiro, resuma
   fielmente e liste a página na seção PÁGINAS PARA SALVAR: a equipe vai salvá-la
   como PDF. Nessa seção entram, no mínimo, as páginas oficiais com: (a) o
   procedimento de cada tarefa que pode virar exercício; (b) planos e limites;
   (c) requisitos de conta e de sistema; (d) limitações, segurança e
   privacidade. Para cada página: título, URL, o trecho que importa, prioridade
   (alta ou média) e nome de arquivo sugerido, sem acento e sem espaço (ex.:
   ajuda-planos-e-limites.pdf).
7. Links que o aluno vai abrir ou importar nos exercícios precisam levar direto
   ao conteúdo, ser públicos e não exigir login. Teste cada um e diga o que ele
   devolve (página HTML, PDF, vídeo).
8. Diferencie sempre o que vale para o plano gratuito e o que exige plano pago.
9. Não escreva ementa, plano de aula, módulos nem objetivos de aprendizagem: isso
   é trabalho da equipe.
10. Escreva em português do Brasil. Mantenha em inglês os nomes de recursos e
    menus que só existem em inglês, sem traduzir.

# FORMATO DE ENTREGA
Entregue UM arquivo de texto puro (.txt), em UTF-8, chamado
ConteudoBruto_replit-agent-essentials.txt, para download. Não use Markdown nem tabelas complexas: use
os separadores e a estrutura abaixo.

================================================================
CONTEÚDO BRUTO — Replit Agent - Essentials
Pesquisa realizada em: [data]
Ferramenta(s): [nome e versão atual de cada uma]
================================================================

0. RESUMO EXECUTIVO
   Em até 15 linhas: o que é, para quem serve, o que mudou recentemente e os 3
   alertas mais importantes para quem vai criar o curso.

1. IDENTIDADE E HISTÓRICO
2. ACESSO, PLANOS E REQUISITOS
3. PRIMEIROS PASSOS (passo a passo oficial)
4. CONCEITOS E GLOSSÁRIO
5. FUNCIONALIDADES
6. CASOS DE USO PARA O PÚBLICO DO CURSO
7. BOAS PRÁTICAS E EXEMPLOS DE PROMPTS
   (separe os exemplos publicados pela fabricante, com fonte, dos que você
   escreveu, marcados [SUGESTÃO])
8. SEGURANÇA, PRIVACIDADE E DADOS
9. LIMITAÇÕES, ERROS COMUNS E SOLUÇÃO DE PROBLEMAS
10. COMPARAÇÃO COM ALTERNATIVAS
    (fatos com fonte; conclusões suas marcadas [SUGESTÃO])
11. NOVIDADES RECENTES E RECURSOS INSTÁVEIS
12. MATERIAL DIDÁTICO EXISTENTE
13. IDEIAS DE EXERCÍCIO
    (comece pela decomposição da tarefa observável em ações; depois, as
    atividades, todas marcadas [SUGESTÃO], cada uma com a ação que cobre, os
    links testados e o resultado que comprova que deu certo)
14. RESPOSTAS AO FOCO ESPECÍFICO DESTE CURSO
    (um item para cada ponto da lista "FOCO ESPECÍFICO", na mesma numeração)
15. TRECHOS TRANSCRITOS DA DOCUMENTAÇÃO OFICIAL
    (cada trecho com: título da página, URL, data de atualização e o texto
    transcrito entre aspas)
16. MATERIAIS PARA BAIXAR
    (um item por material, no formato pedido acima, começando com [BAIXAR])
17. PÁGINAS PARA SALVAR
    (uma página oficial por item, no formato pedido na regra 6)
18. LACUNAS E PONTOS A VERIFICAR
    (tudo o que ficou [VERIFICAR] ou NÃO ENCONTRADO, e as contradições entre
    fontes)
19. APÊNDICE TÉCNICO
    (detalhes técnicos além da profundidade do público, conforme a REGRA DE
    PROFUNDIDADE; se não houver, escreva "sem conteúdo")
20. FONTES CONSULTADAS
    (lista numerada: título, URL, tipo, data da fonte, data de acesso)

Em todas as seções, cite a fonte de cada informação com o número dela na lista da
seção 20, entre colchetes (ex.: [12]).

# ANTES DE ENTREGAR, CONFIRA
[ ] Cada ação da tarefa observável tem passo a passo e pelo menos um exercício.
[ ] Pelo menos dois terços do arquivo tratam do que o aluno vê e faz; o que é
    técnico demais está no APÊNDICE TÉCNICO.
[ ] Nenhuma elaboração sua (prompt, exercício, recomendação, comparação) está
    marcada [CONFIRMADO].
[ ] Todo material não-web citado nas seções 1 a 20 está na seção 16.
[ ] Cada arquivo declarado BAIXADO abre e é do tipo anunciado (nenhuma página
    HTML salva como .pdf).
[ ] Os links dos exercícios foram testados e levam direto ao conteúdo.
[ ] A seção 17 lista páginas dos quatro tipos pedidos na regra 6.
[ ] Cada número está atribuído à fonte que de fato o contém.
[ ] Nomes de menus e botões indicam a origem: (interface), (ajuda pt-BR) ou
    (ajuda en).
```
