"""Gera os roteiros de insercao da fase B (Perplexity Hands-on), na ordem de aplicacao.
Dentro de cada licao, as posicoes vao da maior para a menor, para uma insercao nao deslocar a seguinte.
Posicoes = indices do curso revisado (curso_original.json). Uso: python -I gerar_roteiros.py
Plano aprovado: 02_RELATORIOS/perplexity/Plano_Insercoes_HandsOn.md
Fonte dos textos: Ementa Completa/perplexity-essentials/roteiros/roteiro-articulate-hands-on.md
"""
import json, pathlib

AQUI = pathlib.Path(__file__).resolve().parent
(AQUI / "roteiros").mkdir(exist_ok=True)


def html(arq, trava=False, largura="1"):
    b = {"modelo": "html-html-inline.json", "settings": {"width": largura}, "itens": [{"srcdoc": f"@arquivo:../html/{arq}"}]}
    if trava:
        b["settings"]["hasCustomCompletion"] = True
    return b


def cont(tipo=""):
    item = {"title": "Continue"}
    if tipo:
        item["type"] = tipo
    return {"modelo": "divider-continue-continue.json", "itens": [item]}


def titulo(heading, paragraph):
    return {"modelo": "text-text-heading-paragraph.json", "itens": [{"heading": heading, "paragraph": paragraph}]}


def paragrafo(p):
    return {"modelo": "text-text-paragraph.json", "itens": [{"paragraph": p}]}


def lista(*itens):
    return {"modelo": "list-list-numbered.json", "itens": [{"paragraph": p} for p in itens]}


def acordeao(itens):
    return {"modelo": "interactive-interactive-accordion.json", "itens": [{"title": t, "description": d} for t, d in itens]}


def abas(itens):
    return {"modelo": "interactive-interactive-tabs.json", "itens": [{"title": t, "description": d} for t, d in itens]}


def desafios(itens):
    return [titulo("Quer ir além? (opcional)", INTRO), acordeao(
        [(t, f"<p>{d}</p><p></p><p><strong>Validação:</strong> {v}</p>") for t, d, v in itens])]


def se_travar(oficina, itens):
    return [titulo(f"Se travar na Oficina {oficina}", "<p>Abra o problema que apareceu para você e veja o que fazer:</p>"),
            acordeao([(t, f"<p>{d}</p>") for t, d in itens])]


def modelo(*linhas):
    return '<p>"""<br>' + "<br>".join(linhas) + '<br>"""</p>'


INTRO = "<p>Três desafios para quem terminou a oficina. Cada um diz como saber se deu certo:</p>"
URL_STJ = ("https://www.stj.jus.br/sites/portalp/paginas/comunicacao/noticias/2026/"
           "19052026-relator-identifica-habeas-corpus-com-erros-e-alucinacoes-criadas-por-ia.aspx")

ROTEIROS = [
    # ---- Licao 1 (licao 0)
    ("l0_desafios", 0, 19, desafios([
        ("Resposta em tabela", 'Troque o formato para "tabela afirmação | fonte | data | trecho".',
         "a resposta vem em tabela com as quatro colunas preenchidas."),
        ("A pergunta por voz", "Faça a mesma pergunta pesquisável no app do celular, por voz.",
         "compare se a transcrição da sua fala ficou fiel antes de enviar."),
        ("Termos para bases jurídicas",
         'Pergunte "Que termos técnicos eu deveria usar para pesquisar este tema em bases jurídicas?".',
         "você anota três termos para usar no Projeto Final.")])),
    ("l0_pergunta", 0, 11, [html("l1-pergunta.html")]),
    ("l0_semaforo", 0, 6, [html("l1-semaforo.html", trava=True), cont("completeBlock")]),
    # ---- Licao 2 (licao 1)
    ("l1_desafios3", 1, 19, desafios([
        ("Um processo que não existe",
         "Peça à Perplexity os dados de um número de processo inventado por você (troque dois dígitos do número do TJPR).",
         'anote se ela admitiu NÃO ENCONTRADO ou "achou" algo — e confira no portal.'),
        ("A notícia do STJ",
         f"Abra a notícia do STJ sobre o HC 1.094.270 ({URL_STJ}) e peça uma síntese de cinco linhas em que cada "
         "linha aponte o trecho da notícia.",
         'a síntese diz "16 julgados com erros e trechos inexistentes", e não "16 precedentes inexistentes".'),
        ("Prova de existência no STJ",
         "Repita a prova de existência no STJ, em <strong>scon.stj.jus.br &gt; Por número do processo</strong>, com "
         "um julgado que a Perplexity indicar.",
         "ficha com quatro campos conferidos no portal do STJ.")])),
    ("l1_decida_travar3", 1, 16, [html("l2-decida.html")] + se_travar(3, [
        ("A página citada não tem a frase",
         "Peça no Thread uma fonte primária para aquela frase. Se não vier, retire a frase."),
        ("O link do TJPR não abre",
         "Busque o número 0033052-89.2025.8.16.0001 em <strong>portal.tjpr.jus.br &gt; Jurisprudência</strong>."),
        ("A Perplexity trouxe os dados de uma notícia, não do portal",
         "Isso é fonte secundária. Exija o domínio oficial e confira você mesmo.")])),
    ("l1_desafios2", 1, 14, desafios([
        ("Foco acadêmico",
         "Em <strong>perplexity.ai &gt; + (Adicionar arquivos ou ferramentas) &gt; Aplicativos e mais &gt; "
         "Acadêmico</strong> [conferir], pergunte sobre decisões automatizadas em pesquisa científica.",
         "pelo menos uma fonte é artigo acadêmico."),
        ("A lei e a reportagem",
         "Compare a página da lei no Planalto com uma reportagem sobre o art. 20, pedindo \"coincidências, "
         "divergências, data e escopo; não trate silêncio como contradição\".",
         "a resposta lista pelo menos uma coincidência e aponta o que só uma das fontes diz."),
        ("A mesma pergunta amanhã",
         "Rode a pergunta de novo amanhã, com a cota renovada, e veja se as fontes mudam.",
         "você registra quantas fontes se repetiram.")])),
    # ---- Licao 3 (licao 2)
    ("l2_projeto_final", 2, 16, [
        cont(),
        titulo("Projeto Final — O dossiê citado do seu tema",
               "<p>Escolha um tema real da sua área — um conceito para o TCC, uma afirmação para checar, um mercado "
               "para comparar, uma tese jurídica — e entregue, sem roteiro, um dossiê de pesquisa: pergunta "
               "pesquisável, fontes conferidas e uma síntese curta que você assinaria.</p>"),
        paragrafo("<p>Desta vez, sem passo a passo detalhado. Siga os seis passos:</p>"),
        lista("<p>Passe o tema no semáforo. Se não for verde, minimize (rótulos no lugar de nomes, só a tese).</p>",
              "<p>Escreva a pergunta pesquisável com as cinco partes e as três exigências. Use, se quiser, um dos "
              "pontos de partida abaixo.</p>",
              "<p>Escolha o nível de busca e escreva por quê, numa linha.</p>",
              "<p>Audite duas citações com a ficha da Oficina 3. No perfil jurídico, prove a existência de pelo "
              "menos uma decisão no portal do tribunal (o TJ do seu estado está em "
              "<strong>cnj.jus.br/poder-judiciario/tribunais</strong>).</p>",
              "<p>Escreva uma síntese de 100 a 150 palavras com \"Limites desta síntese\".</p>",
              "<p>Decida se compartilha, e anote o motivo.</p>"),
        titulo("Pontos de partida por perfil",
               "<p>Abra a aba do seu perfil, copie o modelo e troque o que está entre colchetes:</p>"),
        abas([
            ("Estudante ou pesquisador", modelo(
                "Compare três explicações publicadas desde [ano] sobre [tema].",
                "Priorize revisões e artigos de acesso aberto. Para cada conclusão, autor, data, URL e",
                "uma frase sobre como a fonte a sustenta. Separe fatos, divergências e lacunas.")),
            ("Jornalista", modelo(
                "Compare a fonte oficial [URL A] com a reportagem [URL B]. Liste",
                "coincidências, divergências, data e escopo. Termine com duas perguntas que ainda",
                "precisam de apuração.")),
            ("Analista", modelo(
                "Compare [tema] em [organização A] e [organização B] usando só relatórios",
                "públicos oficiais desde [ano]. Mesmos critérios para as duas. Tabela afirmação |",
                "fonte | data | trecho.")),
            ("Jurídico", modelo(
                "Localize decisões públicas do [tribunal] sobre [tese], entre [datas]. Use",
                "apenas [domínio oficial]. Para cada decisão: número, órgão julgador, relator, data,",
                "URL do inteiro teor e trecho curto. Campo ausente na página oficial: NÃO ENCONTRADO.")),
        ]),
        html("l3-dossie.html", trava=True, largura="0"),
        cont("completeBlock"),
    ]),
    ("l2_travar4", 2, 7, se_travar(4, [
        ('"Criar projeto" não aparece no seu plano',
         "Faça tudo num Thread normal e cole a instrução do Projeto no começo da pergunta. [conferir "
         "disponibilidade no gratuito]"),
        ("O rascunho passou de 200 palavras",
         'Peça "reduza para 180 palavras mantendo as citações" ou corte você mesmo.'),
        ("O rascunho citou um site não oficial",
         "Retire a frase ou troque por fonte oficial conferida.")])),
]

for n, (nome, licao, pos, blocos) in enumerate(ROTEIROS, start=1):
    arq = AQUI / "roteiros" / f"r{n:02d}_{nome}.json"
    arq.write_text(json.dumps({"licao": licao, "posicao": pos, "blocos": blocos}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(arq.name)
