"""Gera os roteiros de insercao da fase B do NotebookLM - Hands On, na ordem de aplicacao.
Dentro de cada licao, as posicoes vao da maior para a menor, para uma insercao nao deslocar a seguinte.
Uso: python -I gerar_roteiros.py  (grava roteiros/rNN_*.json ao lado deste arquivo)
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

def titulo(h, p):
    return {"modelo": "text-text-heading-paragraph.json", "itens": [{"heading": h, "paragraph": p}]}

def paragrafo(p):
    return {"modelo": "text-text-paragraph.json", "itens": [{"paragraph": p}]}

def lista(itens):
    return {"modelo": "list-list-numbered.json", "itens": [{"paragraph": t} for t in itens]}

def destaque(p):
    return {"modelo": "text-impact-b.json", "itens": [{"paragraph": p}]}

def accordion(pares):
    return {"modelo": "interactive-interactive-accordion.json", "itens": [{"title": t, "description": d} for t, d in pares]}

def desafio(texto, validacao):
    return f"<p>{texto}</p><p></p><p><strong>Validação:</strong> {validacao}</p>"

ALEM = "<p>Desafios para quem terminou e quer mais. Nenhum é obrigatório. Abra cada um:</p>"

ROTEIROS = [
    # ---- Licao 1 (licao 0): Antes de Arregacar as Mangas + Oficina 1
    ("l0_alem", 0, 21, [
        titulo("Quer ir além? (opcional)", ALEM),
        accordion([
            ("Desafio 1 — Um vídeo do YouTube", desafio("Adicione um vídeo público do YouTube <strong>com legenda</strong> sobre LGPD.", "ele aparece em Fontes. Se for recusado, confira a legenda e se tem mais de 72 horas.")),
            ("Desafio 2 — A busca interna de fontes", desafio('Teste a busca interna de fontes ("Pesquisa Rápida") descrevendo "direitos do titular LGPD".', "aparecem sugestões — e você <strong>não</strong> importa nenhuma sem checar autoria e data.")),
            ("Desafio 3 — O resumo automático da fonte", desafio("Abra uma fonte e leia o resumo automático que a ferramenta fez dela.", "você aponta uma informação do resumo e acha a mesma no documento.")),
        ]),
    ]),
    ("l0_semaforo", 0, 6, [html("h1-semaforo.html")]),
    ("l0_mapa", 0, 3, [html("h1-mapa.html", largura="0")]),
    # ---- Licao 2 (licao 1): Oficinas 2 e 3
    ("l1_alem", 1, 16, [
        titulo("Quer ir além? (opcional)", ALEM),
        accordion([
            ("Oficina 2 — Seja testado pela ferramenta", desafio("Em <strong>Conversa &gt; Configure Chat &gt; Learning Guide</strong>, peça para ser testado sobre o assunto.", "a ferramenta faz uma pergunta por vez e dá pista antes do gabarito.")),
            ("Oficina 2 — Curta × longa", desafio('Peça uma resposta "Shorter" e outra "Longer" na mesma configuração.', "você aponta o que a curta cortou.")),
            ("Oficina 2 — A nota como fonte", desafio("Use sua nota salva como fonte e pergunte algo sobre ela.", "a nova resposta cita a nota.")),
            ("Oficina 3 — Cartões em CSV", desafio("Em <strong>Estúdio &gt; Cartões de estudo</strong>, gere 10 cartões e exporte em CSV.", "o arquivo CSV abre numa planilha.")),
            ("Oficina 3 — Um formato próprio", desafio('Em <strong>Estúdio &gt; Relatórios</strong>, descreva um formato próprio: "quadro com artigo, obrigação e exemplo".', "o relatório sai em tabela, com citações.")),
            ("Oficina 3 — Perguntas frequentes", desafio("Em <strong>Estúdio &gt; Relatórios &gt; Perguntas frequentes</strong>, gere e marque uma resposta que você reescreveria.", "você justifica com o trecho da fonte.")),
        ]),
    ]),
    ("l1_audite", 1, 10, [html("h2-audite.html", trava=True), cont("completeBlock")]),
    # ---- Licao 3 (licao 2): Oficina 4 + Projeto Final + Parte dos Dez
    ("l2_projeto", 2, 11, [
        cont(),
        titulo("Projeto Final — O kit de estudo do seu tema",
               "<p>Chega de LGPD. Escolha um tema real do seu trabalho ou estudo e monte, do zero e sem roteiro passo a passo, um kit de estudo verificado: notebook com fontes verdes, uma pergunta-chave conferida e um artefato pronto para usar ou compartilhar.</p><p>Sugestões por perfil (sempre material público):</p>"),
        lista([
            "<p><strong>Estudante:</strong> um capítulo ou artigo de acesso aberto + a página oficial do assunto.</p>",
            "<p><strong>Educador:</strong> o documento curricular oficial do tema + dois textos públicos que você usa em aula.</p>",
            "<p><strong>Direito:</strong> uma lei no portal do Planalto + um guia de órgão público sobre ela.</p>",
            "<p><strong>Jornalismo/Análise:</strong> três comunicados oficiais públicos sobre o mesmo fato.</p>",
        ]),
        paragrafo("<p>Sem tempo para achar fontes? Use o Kit LGPD com um recorte novo do seu perfil. Mão na massa (16 min):</p>"),
        lista([
            "<p>Passe cada fonte pelo semáforo. Só verde entra.</p>",
            '<p>Crie um notebook novo em <strong>notebook.google.com &gt; Criar novo notebook</strong>, com nome de tema e objetivo (ex.: "CDC — devolução de produtos").</p>',
            "<p>Adicione de três a quatro fontes e envie o prompt de conferência do corpus da Oficina 1.</p>",
            '<p>Faça sua pergunta-chave pedindo citação por afirmação e "não encontrado nas fontes" quando faltar.</p>',
            "<p>Abra duas citações e preencha a ficha da Oficina 2.</p>",
            "<p>Gere no <strong>Estúdio</strong> um artefato que sirva ao seu perfil (guia, teste, cartões, áudio ou relatório personalizado) e revise um item contra a fonte.</p>",
            "<p>Decida o compartilhamento em <strong>Compartilhar</strong>: ninguém, ou Leitor para quem precisa.</p>",
        ]),
        html("h3-projeto.html", trava=True, largura="0"),
        cont("completeBlock"),
    ]),
    ("l2_oficina4", 2, 8, [
        paragrafo("<p>Mão na massa (20 min):</p>"),
        lista([
            "<p>Abra <strong>notebook.google.com &gt; LGPD — revisão &gt; Estúdio &gt; Resumo em Áudio &gt; Personalizar</strong>.</p>",
            "<p>Escolha o formato Resumo (<em>The Brief</em>, um apresentador, menos de dois minutos), o idioma Português (Brasil), e cole na orientação: <em>Produza um resumo curto em português do Brasil para iniciantes. Enfatize os direitos do titular de dados. Não apresente aconselhamento jurídico.</em></p>",
            "<p>Clique em <strong>Gerar</strong>. Não fique esperando: a geração leva alguns minutos.</p>",
            "<p>Enquanto isso, gere o mapa em <strong>Estúdio &gt; Mapa mental</strong>. Clique num nó para abrir os ramos e depois para fazer uma pergunta sobre ele.</p>",
            "<p>Volte ao áudio e ouça os primeiros trinta segundos.</p>",
            "<p><strong>Agora sozinho:</strong> em <strong>Compartilhar</strong>, digite o e-mail de quem vai consultar e escolha <strong>Leitor</strong> (lê e pergunta, mas não mexe nas fontes). Se não tiver com quem compartilhar, abra a janela, observe as opções e feche sem enviar.</p>",
            "<p>Anote sua decisão: com quem, em qual papel e por quê.</p>",
        ]),
        destaque('<p>🏁 <strong>Ponto de controle:</strong> em notebook.google.com &gt; LGPD — revisão &gt; Estúdio, o player do áudio toca em português e o mapa mental abre com ramos; sua decisão de compartilhamento (Leitor, para quem e por quê — ou "não compartilhar") está anotada.</p>'),
        titulo("Se travar", "<p>Abra o problema que apareceu para você:</p>"),
        accordion([
            ("O áudio está demorando ou deu erro", '<p>Espere, reduza a orientação e tente de novo mais tarde.</p><p></p><p>Se aparecer a opção "Gerar mais tarde", use-a.</p>'),
            ("Saiu em inglês", "<p>O idioma não foi escolhido em Personalizar.</p><p></p><p>Gere de novo com Português (Brasil).</p>"),
            ("Não acho o mapa mental no celular", "<p>Mapa mental, relatórios e configuração do chat só existem completos no navegador do computador.</p><p></p><p>Use o celular para ouvir o áudio.</p>"),
        ]),
        titulo("Quer ir além? (opcional)", ALEM),
        accordion([
            ("Desafio 1 — Um áudio em Debate", desafio("Gere um áudio no formato Debate.", "você identifica as duas posições e confere uma delas na fonte.")),
            ("Desafio 2 — Ouvir offline", desafio("Instale o aplicativo no celular e baixe o áudio para ouvir offline.", "o áudio toca com o modo avião ligado.")),
            ("Desafio 3 — Um Resumo em Vídeo", desafio("Gere um Resumo em Vídeo no formato Explicador ou Curto, em português.", "o vídeo aparece no Estúdio. O formato Cinematic é pago, 18+ e em inglês — não é para este curso.")),
        ]),
    ]),
]

for n, (nome, licao, pos, blocos) in enumerate(ROTEIROS, start=1):
    arq = AQUI / "roteiros" / f"r{n:02d}_{nome}.json"
    arq.write_text(json.dumps({"licao": licao, "posicao": pos, "blocos": blocos}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(arq.name)
