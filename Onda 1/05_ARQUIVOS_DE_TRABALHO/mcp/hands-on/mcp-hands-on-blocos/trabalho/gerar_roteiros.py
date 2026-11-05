"""Gera os roteiros de insercao da fase B (MCP Hands-on), na ordem de aplicacao.
Dentro de cada licao, as posicoes vao da maior para a menor, para uma insercao nao deslocar a seguinte.
Posicoes = indices do curso revisado (curso_original.json). Uso: python -I gerar_roteiros.py
Plano aprovado: 02_RELATORIOS/mcp/Plano_Insercoes_HandsOn.md
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

def lista(*itens):
    return {"modelo": "list-list-numbered.json", "itens": [{"paragraph": p} for p in itens]}

def desafios(intro, itens):
    acc = {"modelo": "interactive-interactive-accordion.json", "itens": [
        {"title": t, "description": f"<p>{d}</p><p></p><p><strong>Validação:</strong> {v}</p>"} for t, d, v in itens]}
    return [titulo("🚀 Quer ir além?", intro), acc]

INTRO = "<p>Três desafios opcionais para quem terminou. Abra cada um para ver o desafio e como validar:</p>"
BC = "<strong>Claude &gt; Personalizar &gt; Conectores"

ROTEIROS = [
    # ---- Licao 1 (licao 0)
    ("l0_desafios", 0, 18, desafios(INTRO, [
        ("Uma segunda pergunta", "Faça uma segunda pergunta sobre outro tema da documentação e confira se a URL também é oficial.",
         "a URL abre num dos três domínios oficiais."),
        ("A mesma pergunta no ChatGPT", "Repita a mesma pergunta no ChatGPT com o plugin e compare as duas respostas: o servidor é o mesmo.",
         "as duas respostas mostram chamada de ferramenta e URL oficial."),
        ("Com e sem o conector", "Peça ao Claude \"Responda a mesma pergunta sem usar o conector\" e compare.",
         "você aponta qual das duas respostas traz fonte conferível.")])),
    ("l0_chatgpt", 0, 15, [
        titulo("Variação no ChatGPT (opcional)", "<p>Só se a sua conta tiver a opção. O servidor é o mesmo; muda o caminho:</p>"),
        lista("<p>Abra <strong>ChatGPT &gt; Plugins</strong> (ou Apps) <strong>&gt; + &gt; Add custom MCP server</strong>.</p>",
              "<p>Dê o nome <strong>OpenAI Docs</strong>, cole a mesma URL em Server URL e deixe sem autenticação.</p>",
              "<p>Leia o aviso e clique em <strong>I understand and want to continue</strong>; depois, em <strong>Create as a plugin</strong>, e instale.</p>",
              "<p>Abra um chat novo, digite @, escolha o plugin e mande a mesma pergunta do passo \"Faça a pergunta de verdade\".</p>")]),
    ("l0_semaforo", 0, 10, [html("l1-semaforo.html", trava=True), cont("completeBlock")]),
    ("l0_mapa", 0, 3, [html("l1-mapa.html")]),
    # ---- Licao 2 (licao 1)
    ("l1_ritual", 1, 21, [html("l2-ritual.html", trava=True, largura="0"), cont("completeBlock")]),
    ("l1_desafios4", 1, 19, desafios(
        "<p>Faça estes desafios antes da Parte C, com os conectores ainda ligados. Abra cada um para ver o desafio e como validar:</p>", [
        ("Mova o evento de teste", "Peça ao Claude para mover o evento de teste para outro horário, revise a aprovação e depois apague.",
         "o evento aparece no novo horário e depois some."),
        ("A Parte B no ChatGPT", "Se o seu ChatGPT tiver o plugin do Gmail, faça a Parte B por lá (@Gmail) e compare como cada um pede confirmação.",
         "o rascunho existe e Enviados continua sem nada novo."),
        ("O relatório da conversa", "Peça ao Claude um relatório do que foi feito na conversa: conector, ferramenta, argumentos e se houve escrita.",
         "o relatório bate com os blocos de chamada de ferramenta.")])),
    ("l1_desafios3", 1, 16, desafios(INTRO, [
        ("Horas livres na semana", "Peça \"Em quais dias desta semana eu tenho pelo menos duas horas livres entre 9h e 18h?\".",
         "os dias batem com a agenda."),
        ("Escrita bloqueada", "Coloque as ferramentas de escrita em Blocked e peça para criar um evento.",
         "o Claude avisa que não pode e nada aparece na agenda."),
        ("Resumo da semana", "Peça um resumo da semana em tabela, com uma coluna \"o que preparar\", sem alterar nenhum evento.",
         "nenhum pedido de aprovação aparece.")])),
    ("l1_permissoes", 1, 13, [html("l2-permissoes.html")]),
    ("l1_desafios2", 1, 10, desafios(INTRO, [
        ("Prazo em dias", "Peça \"Quais arquivos desta pasta mencionam prazo em dias?\".",
         "a resposta aponta só politica-ficticia.txt, e você confere abrindo os arquivos."),
        ("Um terceiro arquivo", "Crie um terceiro arquivo fictício e peça uma comparação entre os três, sem alterar nenhum.",
         "a pasta continua com três arquivos, sem nenhum novo."),
        ("As ferramentas que gravam", "Pergunte ao Claude quais ferramentas da extensão gravam ou movem arquivos.",
         "a lista bate com a ficha da extensão.")])),
    ("l1_drive", 1, 6, [
        titulo("Sem Claude Desktop? Caminho pelo Google Drive",
               "<p>Sem o app, a oficina funciona no navegador, com uma pasta nova e não compartilhada no seu Drive:</p>"),
        lista(f"<p>Em {BC} &gt; + &gt; Google Drive</strong>, clique em <strong>Connect</strong> e faça login com a Conta Google pessoal.</p>",
              "<p>No Drive, crie a pasta teste-mcp-arquivos (não compartilhada) com dois documentos com o texto dos arquivos de teste.</p>",
              f"<p>Em {BC} &gt; Google Drive &gt; Tool permissions</strong>, deixe em <strong>Needs approval</strong> (requer aprovação) tudo o que compartilha, move, envia para a lixeira ou faz upload.</p>",
              f"<p>Siga os passos \"Peça a leitura\" e \"Confira a pegadinha e a pasta\", trocando \"pasta\" por \"pasta do Drive\". Ao terminar: {BC} &gt; Google Drive &gt; Disconnect</strong>.</p>")]),
    # ---- Licao 3 (licao 2)
    ("l2_faxina", 2, 9, [html("l3-faxina.html", largura="0")]),
    ("l2_plano", 2, 6, [html("l3-plano.html")]),
]

for n, (nome, licao, pos, blocos) in enumerate(ROTEIROS, start=1):
    arq = AQUI / "roteiros" / f"r{n:02d}_{nome}.json"
    arq.write_text(json.dumps({"licao": licao, "posicao": pos, "blocos": blocos}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(arq.name)
