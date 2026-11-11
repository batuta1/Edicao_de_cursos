"""v2: troca os marcadores [conferir] por texto verificado (pesquisa de 11/11/2026) nas fontes dos mapas,
dos roteiros e dos HTMLs. Cada troca precisa achar o trecho exatamente uma vez ou mais (senao aborta).

Verificado em 11/11/2026:
- artigo UFF 6885: estudo retrospectivo, Campo Grande (MS), 113 medicos / 229 pacientes, desfecho =
  encaminhamentos presenciais a cardiologia; NAO mede pressao arterial (objnursing.uff.br, html_en).
- Consensus Free: help center diz 10 mensagens Pro/mes; arquivo de precos do site diz 15 -> "10 a 15".
- PRISMA 2020: fluxograma oficial em portugues (Brasil) em prisma-statement.org > Translations (.docx).
- Rotulos de interface nao verificaveis sem conta (Filter > Country, Has PDF, upload, busca avancada da BVS,
  Settings > Subscription) foram reescritos de forma que nao dependa do rotulo exato.
"""
import pathlib

AQUI = pathlib.Path(__file__).resolve().parent
PRISMA_ORIGEM = ' O modelo oficial em português fica em prisma-statement.org &gt; Translations &gt; Portuguese (Brazilian): baixe o fluxograma (.docx) e salve como prisma-2020-fluxograma-ptbr.docx.'

TROCAS = {
    'essentials/gerar_mapas.py': [
        ('10 mensagens Pro por mês [conferir: uma página de ajuda ainda indica 15]', 'de 10 a 15 mensagens Pro por mês (as páginas da própria Consensus divergem)'),
        (' e em <strong>Consensus &gt; Settings &gt; Subscription</strong> [conferir caminho].', ' e em <strong>consensus.app/pricing</strong>.'),
        (' A política de privacidade pública ainda indicava atualização de 2023 [conferir a versão vigente].', ' Antes de enviar qualquer material amarelo, leia a versão vigente da política de privacidade.'),
        ('política institucional [conferir caso a caso].', 'política institucional; confira caso a caso.'),
        ('registrar o descritor DeCS exibido [conferir].', 'anote o descritor que o DeCS exibir.'),
        ('<strong>Filter &gt; Country &gt; Brazil</strong> [conferir rótulo]', 'o filtro de país no botão <strong>Filter</strong> (Brazil)'),
        ('<strong>bvsalud.org &gt; Pesquisa avançada</strong> [conferir rótulo]', '<strong>bvsalud.org</strong> (caixa de busca ou busca avançada)'),
        ('<p>Ative <strong>Research Agent &gt; Has PDF</strong> [conferir rótulo] para priorizar trabalhos com texto completo.</p>', '<p>Se o Research Agent oferecer o filtro de artigos com PDF (<strong>Has PDF</strong>), ative-o para priorizar trabalhos com texto completo.</p>'),
        ('não foi confirmado como fluxo vigente [conferir].', 'não aparece como fluxo atual.'),
        ('Ele trata de capacitação em telessaúde e pode não medir pressão arterial [conferir]. Decida e registre na aba Triagem — registrar essa decisão também é parte do exercício.',
         'É um estudo retrospectivo de Campo Grande (MS) que mede encaminhamentos presenciais à cardiologia, não a pressão arterial dos pacientes: pelos critérios do caso-guia, ele seria excluído ("sem desfecho de pressão"). Registre essa decisão na aba Triagem — ela também é parte do exercício.'),
        ('estão visíveis na primeira página.</p>\',', 'estão visíveis na primeira página.' + PRISMA_ORIGEM + '</p>\','),
    ],
    'hands-on/gerar_mapas.py': [
        ('Repita com "telessaúde" [conferir os descritores exibidos].', 'Repita com "telessaúde" e anote o descritor exibido — ele pode ter nome diferente do termo que você digitou.'),
        ('10 mensagens Pro por mês [conferir: uma página de ajuda fala em 15].', 'de 10 a 15 mensagens Pro por mês (as páginas da própria Consensus divergem).'),
        ('os filtros, como Filter &gt; Country &gt; Brazil [conferir rótulo].', 'os filtros, como o de país (Brazil) no botão Filter.'),
        ('<strong>Filter &gt; Country &gt; Brazil</strong> [conferir rótulo]', 'o filtro de país no botão <strong>Filter</strong> (Brazil)'),
        ('ligue <strong>Research Agent &gt; Has PDF</strong> [conferir rótulo].</p>', 'ligue o filtro de artigos com PDF (<strong>Has PDF</strong>), se ele aparecer.</p>'),
        ('Se aparecer, ligue <strong>Research Agent &gt; Has PDF</strong> [conferir rótulo] para priorizar', 'Se aparecer o filtro <strong>Has PDF</strong>, ligue-o para priorizar'),
        ('Os números saem das abas Log e Triagem.</p>\',', 'Os números saem das abas Log e Triagem.' + PRISMA_ORIGEM + '</p>\','),
    ],
    'gerar_roteiros.py': [
        ('(<strong>Research Agent &gt; upload</strong> [conferir o botão no Basic])', '(opção de upload de PDF)'),
        ('esse artigo trata de capacitação em telessaúde e talvez não meça pressão arterial [conferir] — se for o caso, ele seria excluído do caso-guia.',
         'esse artigo mede encaminhamentos presenciais à cardiologia, não a pressão arterial — pelos critérios do caso-guia, ele seria excluído ("sem desfecho de pressão").'),
        ('aplique <strong>Filter &gt; Study design</strong> [conferir rótulo] e veja', 'aplique o filtro de desenho do estudo (Study design, no botão Filter) e veja'),
    ],
    'html/src/h2-preparacao.body.html': [
        ('10 mensagens Pro por mês [conferir: uma página de ajuda fala em 15]', 'de 10 a 15 mensagens Pro por mês (as páginas da própria Consensus divergem)'),
    ],
}

for rel, trocas in TROCAS.items():
    p = AQUI / rel
    t = p.read_text(encoding='utf-8')
    for velho, novo in trocas:
        n = t.count(velho)
        if n == 0:
            raise SystemExit(f'{rel}: trecho nao encontrado: {velho[:70]}')
        t = t.replace(velho, novo)
    p.write_text(t, encoding='utf-8')
    print(rel, len(trocas), 'trocas')
for rel in TROCAS:
    if '[conferir' in (AQUI / rel).read_text(encoding='utf-8'):
        raise SystemExit(f'{rel}: ainda tem [conferir]')
print('sem [conferir] restante')
