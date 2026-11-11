"""Fase B do Deep Search (Essentials e Hands On): grava os roteiros de insercao e os aplica em cadeia.

Uso: python roteiros_insercao.py essentials|hands-on
- Cada roteiro vai para <curso>/deep-<curso>-blocos/trabalho/roteiros/rNN_*.json
- Antes de cada insercao, confere o tipo do bloco-ancora (o bloco logo antes da posicao) no curso atual.
- Dentro de cada licao, as insercoes vao da maior posicao para a menor, para os indices do plano
  (plano_insercoes.md) continuarem valendo.
- Saidas: trabalho/etapas/eNN.json (intermediarias) e trabalho/curso_v1.json (final). Nada e' sobrescrito.
"""
import json
import pathlib
import shutil
import subprocess
import sys

AQUI = pathlib.Path(__file__).resolve().parent
SKILL = pathlib.Path.home() / '.claude' / 'skills' / 'inserir-blocos-scorm'
HTML = '@arquivo:../../../../html/'

T = 'text-text-heading-paragraph.json'
P = 'text-text-paragraph.json'
L = 'list-list-numbered.json'
I = 'text-impact-b.json'
A = 'interactive-interactive-accordion.json'
TABS = 'interactive-interactive-tabs.json'
C = 'divider-continue-continue.json'
H = 'html-html-inline.json'


def b(modelo, *itens, settings=None):
    d = {'modelo': modelo, 'itens': list(itens)}
    if settings:
        d['settings'] = settings
    return d


def cont(tipo=''):
    return b(C, {'title': 'Continue', 'type': tipo}) if tipo else b(C, {'title': 'Continue'})


def lista(*ps):
    return b(L, *[{'paragraph': f'<p>{p}</p>'} for p in ps])


# (nome, licao=position, posicao, ancora=(type, variant) do bloco em posicao-1, blocos)
ESSENTIALS = [
    # L2 / Módulo 1
    ('e1_m1_agente', 1, 4, ('text', 'paragraph'), [
        b(H, {'srcdoc': HTML + 'e1-agente.html'}, settings={'width': '1'}),
    ]),
    # L3 / Módulo 2 (maior posição primeiro)
    ('e3_m2_checklist_base', 2, 16, ('interactive', 'flashcard'), [
        b(I, {'paragraph': '<p>📋 <strong>Checklist-base</strong> (copie para a aba Registro e adapte):<br>Finalidade documentada: [ ]<br>O material é público? [sim | não] — se não: há base legal e autorização interna? [ ]<br>Mínimo necessário: [quais arquivos ou pasta, e não a caixa inteira]<br>Dados pessoais ou sigilosos removidos ou anonimizados de fato? [ ]<br>Conta: [pessoal | empresarial contratada] · Treinamento desligado? [ ]<br>Conectores ativos: [nenhum | quais] · Revisão de sigilo profissional feita? [ ]</p>'}),
    ]),
    ('e2_m2_semaforo', 2, 11, ('text', 'b'), [
        b(T, {'heading': 'Agora, casos novos', 'paragraph': '<p>Aplique o mesmo critério a seis situações que não estavam no exercício:</p>'}),
        b(H, {'srcdoc': HTML + 'e2-semaforo.html'}, settings={'width': '1'}),
    ]),
    # L4 / Módulo 3
    ('e5_m3_ponto_controle', 3, 9, ('interactive', 'process'), [
        b(I, {'paragraph': '<p>🏁 <strong>Ponto de controle:</strong> no Gemini, <em>Deep Research &gt; plano</em> exibe a etapa acrescentada antes de Start research; no ChatGPT, o plano confirmado aparece no início da atividade da pesquisa.</p>'}),
    ]),
    ('e4_m3_antes_depois', 3, 5, ('interactive', 'flashcard'), [
        b(P, {'paragraph': '<p>Veja os seis componentes funcionando no caso-guia. Compare o pedido vago com o brief reescrito:</p>'}),
        b(TABS,
          {'title': 'Pedido vago', 'description': '<p>"Pesquise envelhecimento no Brasil."</p><p></p><p><strong>O que fica em aberto:</strong> corte etário, período, fonte e formato. O agente preenche cada lacuna por conta própria.</p>'},
          {'title': 'Brief reescrito', 'description': '<p><strong>Exige:</strong> os cortes 60+ e 65+, o período 2010–2022 e o Censo do IBGE como fonte obrigatória.</p><p></p><p><strong>Pede como saída:</strong> uma tabela com número, fonte e data para cada dado, e a separação entre fatos, inferências e lacunas.</p>'}),
    ]),
    # L5 / Módulo 4
    ('e6_m4_pilula_ibge', 4, 10, ('text', 'b'), [
        b(T, {'heading': 'Pílula Hands-on: confira no IBGE', 'paragraph': '<p>Em 6 minutos, confira no IBGE os dados de 65+ em 2010 e 2022. Registre valores, URL e data da consulta, sem misturar os cortes 60+ e 65+. Depois compare com o gabarito e responda à questão:</p>'}),
        b(I, {'paragraph': '<p>📌 <strong>Gabarito do IBGE:</strong> 65+ = 7,4% e 14 milhões em 2010; 10,9% e 22,2 milhões em 2022. 60+ = 15,8% em 2022, crescimento de 46,6% sobre 2010. Caso jurídico: comunicação à ANPD e aos titulares em três dias úteis (art. 6º da Resolução 15/2024); registro do incidente por pelo menos cinco anos (art. 10).</p>'}),
    ]),
    # L6 / Módulo 5
    ('e8_m5_escolha_por_tarefa', 5, 10, ('text', 'b'), [
        b(T, {'heading': 'Escolha por tarefa', 'paragraph': '<p>Como nenhum placar decide por você, escolha pela tarefa — e valide na sua própria pergunta:</p><ul><li><strong>ChatGPT</strong>, quando restrição de sites e exportação editável importam.</li><li><strong>Gemini</strong>, quando o corpus está no Gmail ou no Drive, ou quando Docs e áudio são o destino.</li><li><strong>Perplexity</strong>, quando o fluxo centrado em citação e a rapidez são prioritários.</li></ul><p>Registre na aba Registro a ferramenta que você usou no Módulo 3 e a justificativa da escolha (6 minutos).</p>'}),
    ]),
    ('e7_m5_benchmarks', 5, 9, ('interactive', 'flashcard'), [
        b(P, {'paragraph': '<p>Três estudos circulam com frequência. Antes de citar qualquer placar, veja quem fez, o que mede e a ressalva de cada um:</p>'}),
        b(TABS,
          {'title': 'BrowseComp', 'description': '<p><strong>Quem fez:</strong> OpenAI. <strong>O que mede:</strong> localização de fatos difíceis, em 1.266 problemas.</p><p></p><p><strong>Resultado:</strong> o deep research da OpenAI obteve 51,5%. <strong>Ressalva:</strong> a própria OpenAI informa treinamento em dados específicos para essas tarefas, e o resultado agrega até 64 tentativas.</p>'},
          {'title': 'DRACO (2026)', 'description': '<p><strong>O que mede:</strong> 100 tarefas em 10 domínios, avaliadas por um modelo como juiz.</p><p></p><p><strong>Resultado:</strong> a Perplexity liderou com 67,15%. <strong>Ressalva:</strong> os autores incluem pesquisadores da Perplexity, e as tarefas vieram de consultas da própria Perplexity.</p>'},
          {'title': 'DeepResearch Bench (2025)', 'description': '<p><strong>Quem fez:</strong> pesquisa acadêmica e aberta. <strong>O que mede:</strong> separa a qualidade do relatório da precisão de citação.</p><p></p><p><strong>Resultado:</strong> o Gemini produziu mais citações efetivas (111,21 em média), e a Perplexity teve maior precisão de citação. <strong>Ressalva:</strong> versões de 2025, já superadas.</p>'}),
    ]),
    # L7 / Módulo 6 — depois do Continue existente, antes do encerramento
    ('e9_m6_checklist_dossie', 6, 12, ('divider', 'continue'), [
        b(H, {'srcdoc': HTML + 'e9-checklist-dossie.html'}, settings={'width': '1', 'hasCustomCompletion': True}),
        cont('completeBlock'),
    ]),
]

HANDS_ON = [
    # L1 / Preparação + Oficina 1 (maior posição primeiro)
    ('h3_o1_injection_controle', 0, 17, ('interactive', 'sorting'), [
        b(I, {'paragraph': '<p>⚠️ <strong>Cuidado:</strong> página e arquivo podem trazer instrução escondida para o agente (prompt injection). Mais um motivo para não conectar o que você não precisa.</p>'}),
        b(I, {'paragraph': '<p>🏁 <strong>Ponto de controle:</strong> no menu + (ou de ferramentas) da ferramenta escolhida, a opção Deep research aparece — e você não clicou em "Create files and apps", que é outro modo da Perplexity, com outra cota.</p>'}),
    ]),
    ('h4_o1_ir_alem', 0, 11, ('interactive', 'accordion'), [
        b(T, {'heading': 'Quer ir além? (opcional)', 'paragraph': '<p>Três desafios para quem quer praticar mais. Abra cada um — o critério de validação está no fim:</p>'}),
        b(A,
          {'title': 'Briefar o caso jurídico antes da hora', 'description': '<p>Escreva o brief do caso jurídico (comunicação de incidente sob a LGPD, na última lição) antes de chegar a ele.</p><p></p><p><strong>Valida se:</strong> ele distingue lei, regulamento e orientação.</p>'},
          {'title': 'Pedir a leitura de um colega', 'description': '<p>Peça a um colega para ler seu brief e dizer o que faria diferente.</p><p></p><p><strong>Valida se:</strong> ele entendeu o recorte sem perguntar.</p>'},
          {'title': 'Reescrever um pedido antigo', 'description': '<p>Reescreva com as seis linhas um pedido de pesquisa que você fez a uma IA na semana passada.</p><p></p><p><strong>Valida se:</strong> você achou pelo menos uma linha que faltava.</p>'}),
    ]),
    ('h1h2_o1_dossies_brief', 0, 7, ('interactive', 'process'), [
        b(P, {'paragraph': '<p>Escolha agora o dossiê do seu Projeto Final. Compare as três opções:</p>'}),
        b(TABS,
          {'title': 'A — Selic', 'description': '<p><strong>Pergunta:</strong> reconstrua as decisões do Copom de janeiro de 2025 a setembro de 2026; identifique pico e reversão.</p><p></p><p><strong>Fonte obrigatória:</strong> Banco Central (histórico de taxas).</p>'},
          {'title': 'B — Renda', 'description': '<p><strong>Pergunta:</strong> o que a PNAD Contínua/Ipea mostra sobre crescimento da renda por gênero no 2º trimestre de 2025?</p><p></p><p><strong>Fonte obrigatória:</strong> nota do Ipea.</p>'},
          {'title': 'C — Licitações', 'description': '<p><strong>Pergunta:</strong> quais valores de dispensa da Lei 14.133 estão vigentes em 2026 e qual ato os atualizou?</p><p></p><p><strong>Fonte obrigatória:</strong> Lei 14.133 consolidada no Planalto e o decreto nela referido.</p>'}),
        b(H, {'srcdoc': HTML + 'h2-monte-brief.html'}, settings={'width': '1'}),
    ]),
    # L2 / Oficina 2
    ('h5_o2_ir_alem', 1, 15, ('interactive', 'flashcard'), [
        b(T, {'heading': 'Quer ir além? (opcional)', 'paragraph': '<p>Três desafios para quem quer praticar mais. Abra cada um — o critério de validação está no fim:</p>'}),
        b(A,
          {'title': 'Ouvir o relatório no Gemini', 'description': '<p>Gere o Audio Overview do relatório: <strong>relatório aberto &gt; More &gt; Generate Audio Overview</strong>.</p><p></p><p><strong>Valida se:</strong> o áudio repete algum número que você ainda não conferiu — anote.</p>'},
          {'title': 'Interromper e mudar o foco no ChatGPT', 'description': '<p>Interrompa uma pesquisa em andamento e mude o foco ("concentre-se em 65+").</p><p></p><p><strong>Valida se:</strong> o Registro anota a interrupção.</p>'},
          {'title': 'Rodar o mesmo brief em outra data', 'description': '<p>Rode o mesmo brief em outra data e compare dois números.</p><p></p><p><strong>Valida se:</strong> você anotou se mudaram.</p>'}),
    ]),
    # L3 / Oficina 3 + Projeto Final (maior posição primeiro)
    ('h11h12_pf_checklist_dez', 2, 16, ('divider', 'continue'), [
        b(H, {'srcdoc': HTML + 'h11-checklist-projeto.html'}, settings={'width': '1', 'hasCustomCompletion': True}),
        cont('completeBlock'),
        b(T, {'heading': 'A Parte dos Dez', 'paragraph': '<p>Dez hábitos de quem usa deep research sem passar vergonha:</p>'}),
        lista('<strong>Brief antes do clique.</strong> Seis linhas economizam uma pesquisa.',
              '<strong>Leia o plano.</strong> É ali que você corrige o rumo de graça.',
              '<strong>Desligue o treino antes.</strong> Data Controls, Keep Activity ou Temporary chat.',
              '<strong>Pasta mínima, nunca a caixa inteira.</strong> Conector é porta aberta.',
              '<strong>Link não é prova.</strong> Abra, ache o trecho, anote.',
              '<strong>Cinco fontes iguais são uma.</strong> Conte famílias de evidência, não links.',
              '<strong>Número sem corte, unidade e período não é número.</strong> 60+ não é 65+.',
              '<strong>Norma se confere no texto consolidado.</strong> Com artigo, vigência e data.',
              '<strong>Benchmark tem dono.</strong> Pergunte quem fez antes de acreditar no placar.',
              '<strong>Escolha por tarefa e teste na sua pergunta.</strong> Não existe "a melhor" para tudo.'),
    ]),
    ('h9h10_pf_gabaritos_modelo', 2, 13, ('interactive', 'process'), [
        b(I, {'paragraph': '<p>📌 <strong>Gabaritos de referência</strong> (reconfira no dia):<br><strong>A</strong> — 13,25% em 29/01/2025; 15,00% de 18/06/2025 a 28/01/2026; cortes até 13,75% em 16/09/2026.<br><strong>B</strong> — crescimento interanual de 3,4% (homens) e 3,3% (mulheres); é taxa de crescimento, não igualdade de salário.<br><strong>C</strong> — os valores mudam em 1º de janeiro: o acerto é achar o decreto vigente na lei consolidada e rejeitar o revogado, não decorar valor.</p>'}),
        b(I, {'paragraph': '<p>📝 <strong>Modelo do relatório auditado</strong> (copie e preencha):<br>RELATÓRIO AUDITADO — [pergunta] · [data]<br>Fatos verificados: [afirmação] — [fonte primária, data] (Auditoria nº __)<br>Inferências: [o que se deduz, marcado como inferência]<br>Lacunas: [o que o brief pedia e não foi encontrado]<br>Método: [ferramenta, modo, data e hora, brief, plano e edições, configuração de dados]</p>'}),
    ]),
    ('h8_o4_fonte_oficial', 2, 11, ('text', 'b'), [
        cont(),
        b(T, {'heading': 'Pesquisa com fonte oficial: a regra que vale', 'paragraph': '<p>Uma empresa sofreu um vazamento de dados. Quando e para quem ela precisa comunicar? Pergunta assim não aceita "segundo um blog": a resposta mora na LGPD e na Resolução CD/ANPD 15/2024. Aqui você prende o agente às fontes oficiais e confere artigo por artigo — serve para quem é do Direito e para qualquer pessoa que precise de regra, não de opinião.</p><p>Você vai usar o ChatGPT, pela restrição de sites (<strong>1 pesquisa</strong>), ou a Perplexity, se for a sua do mês; o PDF da Resolução CD/ANPD 15/2024 e a página da ANPD sobre comunicação de incidente. Parte guiada:</p>'}),
        lista('No ChatGPT, vá a <strong>caixa do prompt &gt; Sites &gt; Manage sites</strong>, inclua planalto.gov.br e gov.br/anpd e escolha <strong>restringir</strong> a esses sites (não "priorizar").',
              'Ative <strong>+ &gt; Deep research</strong> e cole o prompt do destaque abaixo.',
              'Registre a execução na aba Registro, com os sites restringidos.',
              'Abra o PDF da Resolução. Ele traz outros atos do Diário Oficial antes: procure pelo título dentro do arquivo (<strong>Localizar &gt; "Resolução CD/ANPD nº 15"</strong>).',
              'Confira três afirmações do relatório: prazo, destinatários e tempo de guarda do registro. 🏁 Em Sites &gt; Manage sites, os dois domínios aparecem com a opção de restringir marcada; no PDF, o art. 6º está localizado.'),
        b(I, {'paragraph': '<p>💬 <strong>Prompt:</strong> Pesquise a obrigação de comunicar incidente de segurança sob a LGPD e a Resolução CD/ANPD 15/2024. Use apenas planalto.gov.br, gov.br/anpd e o repositório do Ministério da Justiça para a conclusão normativa. Distinga lei, regulamento e orientação; informe vigência e artigo; não dê parecer para caso concreto; transcreva no máximo o trecho necessário; liste qualquer conflito ou mudança posterior.</p>'}),
        b(I, {'paragraph': '<p>⚠️ <strong>Na Perplexity,</strong> escrever os domínios no prompt não bloqueia o resto da web (não há garantia documentada). Se usar a Perplexity, confira no painel de fontes quais escaparam do domínio.</p>'}),
        b(P, {'paragraph': '<p>Sua vez:</p>'}),
        lista('Para cada afirmação do relatório, marque o tipo: lei (LGPD), regulamento (Resolução) ou orientação (página da ANPD).',
              'Verifique se o relatório trata a regra geral como parecer para um caso concreto. Se sim, marque "corrigir".',
              '<strong>Sem saldo?</strong> Rode o mesmo pedido na busca comum da Perplexity (ilimitada) e audite do mesmo jeito — anotando que não foi pesquisa profunda.'),
        b(I, {'paragraph': '<p>✅ <strong>Deu certo?</strong> Sua auditoria confirma: comunicação à ANPD e aos titulares, em três dias úteis (art. 6º); conteúdo da comunicação nos arts. 6º e 9º; registro do incidente por pelo menos cinco anos (art. 10). Cada linha diz se a fonte é lei, regulamento ou orientação, e nenhuma frase do relatório corrigido virou parecer.</p>'}),
        b(T, {'heading': 'Se travar', 'paragraph': '<p>Abra o item do seu problema:</p>'}),
        b(A,
          {'title': 'Não acho Manage sites', 'description': '<p>Pode depender de plano ou região [conferir]. Escreva os domínios no brief e audite as fontes uma a uma.</p>'},
          {'title': 'O relatório cita blog de escritório', 'description': '<p>É fonte secundária: troque pelo artigo da norma ou remova.</p>'},
          {'title': 'Dúvida se a norma mudou', 'description': '<p>Abra o texto consolidado no Planalto e procure atos alteradores; anote a data.</p>'}),
        cont(),
    ]),
    ('h6c_o3_deu_certo', 2, 8, ('knowledgeCheck', 'multiple choice'), [
        b(I, {'paragraph': '<p>✅ <strong>Deu certo?</strong> As três frases: integral; parcial (mistura cortes — 46,6% é de 60+, 10,9% é de 65+); não suporta (7,4% → 10,9% não é dobrar). Sua aba Auditoria tem cinco linhas com trecho, tipo de fonte e decisão, e você listou duas lacunas.</p>'}),
    ]),
    ('h6h7_o3_gabarito_sua_vez', 2, 7, ('divider', 'continue'), [
        b(I, {'paragraph': '<p>📌 <strong>Gabarito do IBGE:</strong> 65+ = 7,4% e 14 milhões em 2010; 10,9% e 22,2 milhões em 2022. 60+ = 15,8% em 2022, com crescimento de 46,6% sobre 2010.</p>'}),
        b(P, {'paragraph': '<p>Sua vez, usando o gabarito acima:</p>'}),
        lista('Classifique estas três frases: "Em 2022, pessoas com 65 anos ou mais eram 10,9% da população, cerca de 22,2 milhões."; "A população idosa cresceu 46,6% entre 2010 e 2022 e chegou a 10,9% do total."; "A parcela de pessoas com 65 anos ou mais dobrou entre 2010 e 2022."',
              'Procure <strong>famílias de evidência</strong>: duas ou mais fontes do relatório repetem a mesma notícia? Conte como uma.',
              'Compare com o brief: o que você pediu e o relatório não trouxe (diferenças regionais? contraponto?). Escreva duas lacunas.'),
    ]),
]


def main():
    curso_nome = sys.argv[1]
    roteiros = {'essentials': ESSENTIALS, 'hands-on': HANDS_ON}[curso_nome]
    trab = AQUI / curso_nome / f'deep-{curso_nome}-blocos' / 'trabalho'
    (trab / 'roteiros').mkdir(exist_ok=True)
    (trab / 'etapas').mkdir(exist_ok=False)
    atual = trab / 'curso_original.json'
    for n, (nome, licao, pos, ancora, blocos) in enumerate(roteiros, 1):
        curso = json.loads(atual.read_text(encoding='utf-8'))
        lic = sorted(curso['course']['lessons'], key=lambda x: x['position'])[licao]
        anterior = lic['items'][pos - 1]
        achado = (anterior.get('type'), anterior.get('variant'))
        if achado[0] != ancora[0] or (ancora[1] not in (achado[1] or '')):
            raise SystemExit(f'{nome}: ancora esperada {ancora}, encontrada {achado} em licao {licao} pos {pos - 1}')
        rot = trab / 'roteiros' / f'r{n:02d}_{nome}.json'
        rot.write_text(json.dumps({'licao': licao, 'posicao': pos, 'blocos': blocos}, ensure_ascii=False, indent=1), encoding='utf-8')
        saida = trab / 'etapas' / f'e{n:02d}.json'
        r = subprocess.run([sys.executable, str(SKILL / 'scripts' / 'inserir_sequencia.py'), str(atual),
                            '--roteiro', str(rot), '--modelos', str(SKILL / 'modelos'), '--saida', str(saida)],
                           capture_output=True, text=True, encoding='utf-8')
        print(f'[{n:02d}] {nome}: licao {licao} pos {pos} -> {len(blocos)} bloco(s) | rc={r.returncode}')
        if r.returncode != 0:
            print(r.stdout[-2000:], r.stderr[-2000:])
            raise SystemExit('falhou')
        atual = saida
    final = trab / 'curso_v1.json'
    if final.exists():
        raise SystemExit('curso_v1.json ja existe')
    shutil.copyfile(atual, final)
    print('gravado', final)


if __name__ == '__main__':
    main()
