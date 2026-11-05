"""Gera os roteiros de insercao da fase B (MCP Essentials), na ordem de aplicacao.
Dentro de cada licao, as posicoes vao da maior para a menor, para uma insercao nao deslocar a seguinte.
Posicoes = indices do curso revisado (curso_original.json). Uso: python -I gerar_roteiros.py
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

def questao(titulo, alternativas):
    return {"modelo": "knowledgecheck-knowledgecheck-multiple-choice.json",
            "itens": [{"title": titulo, "answers": [{"title": t, "correct": c, "feedback": f} for t, c, f in alternativas]}]}

def semaforo(cenario, correta, fbs):
    nomes = ["Verde", "Amarelo", "Vermelho", "Não se aplica"]
    return questao(f"Análise de cenários — {cenario} Qual é a cor do semáforo?",
                   [(n, n == correta, fbs[n]) for n in nomes])

ROTEIROS = [
    # ---- Licao 1 (licao 0)
    ("l0_registro", 0, 13, [html("l1-registro.html", largura="0")]),
    ("l0_continue", 0, 5, [cont()]),
    ("l0_sobre", 0, 0, [
        {"modelo": "text-text-heading-paragraph.json", "itens": [{
            "heading": "Sobre este curso",
            "paragraph": "<p>Este curso capacita você a compreender o Model Context Protocol (MCP) — padrão aberto que conecta assistentes de inteligência artificial a ferramentas e dados externos — e a instalar e usar conectores MCP no Claude e, quando a conta permitir, no ChatGPT: para consultar serviços, ler arquivos e executar ações com aprovação humana, sempre com a possibilidade de desfazer e de revogar o acesso concedido. Ao final, você terá ligado um conector remoto público, autorizado a leitura de uma pasta de arquivos fictícios, consultado e alterado a própria agenda de forma reversível e elaborado um plano de conexão segura para um caso do seu perfil profissional.</p><p>São 129 minutos, em ordem crescente de risco: verificar o acesso, entender o protocolo, definir os critérios de segurança e, então, consultar, ler e agir. O curso foi desenhado para quem não programa; basta o uso básico de Claude ou ChatGPT, uma conta Claude (o plano gratuito é suficiente) e uma Conta Google pessoal.</p><p>Concluído o curso, você deverá ser capaz de:</p>"}]},
        {"modelo": "list-list-numbered.json", "itens": [
            {"paragraph": "<p>Explicar o que o MCP padroniza e o que não garante, distinguindo-o de API, conector, plugin, skill e orquestradores de automação.</p>"},
            {"paragraph": "<p>Decidir, antes de instalar, se um conector pode ser ligado, com qual conta e com quais permissões.</p>"},
            {"paragraph": "<p>Instalar um conector remoto e consultar um serviço, conferindo a origem da resposta pela chamada de ferramenta.</p>"},
            {"paragraph": "<p>Ler arquivos com acesso restrito a uma única pasta, recusando instruções embutidas em conteúdo externo.</p>"},
            {"paragraph": "<p>Executar uma ação com aprovação manual, conferi-la no serviço de origem, desfazê-la e revogar os acessos concedidos.</p>"}]},
        cont(),
    ]),
    # ---- Licao 2 (licao 1)
    ("l1_questao_local", 1, 17, [questao(
        "Uma colega quer usar o MCP para que o Claude leia arquivos de uma pasta do computador dela. Qual das situações descreve um servidor local?",
        [("Um conector adicionado no Claude pelo navegador, informando uma URL pública.", False,
          "Não. Um conector adicionado por URL é um servidor remoto, acessado pela internet."),
         ("Uma extensão instalada no Claude Desktop que lê arquivos de uma pasta do computador.", True,
          "Correto. Extensões do Claude Desktop rodam na máquina do usuário; por isso existem apenas no Desktop."),
         ("Um plugin do diretório do ChatGPT.", False,
          "Não. Plugins do diretório do ChatGPT são servidores remotos, acessados pela internet."),
         ("O conector do Google Calendar.", False,
          "Não. O Google Calendar é um conector remoto: funciona no navegador, no aplicativo e no celular.")])]),
    ("l1_brasil", 1, 15, [{"modelo": "text-text-paragraph.json", "itens": [{
        "paragraph": "<p><strong>Exemplos no Brasil:</strong> a Senior Sistemas documenta servidores MCP que permitem a assistentes como ChatGPT e Claude consultar dados e, conforme permissões, executar ações no seu sistema de gestão; a Econodata oferece servidor MCP para consulta de dados empresariais, com chave de acesso somente leitura e revogável. Ambos exigem contratação e servem aqui apenas como ilustração. Os diretórios do Claude e do ChatGPT incluem ainda conectores interativos, que exibem interfaces dentro da conversa (Canva, Figma, Asana, entre outros), cuja disponibilidade depende do plano de cada serviço.</p>"}]}]),
    ("l1_nxm", 1, 4, [html("l2-nxm.html")]),
    ("l1_continue", 1, 3, [cont()]),
    # ---- Licao 3 (licao 2)
    ("l2_cenarios", 2, 16, [
        semaforo("Cenário B: conectar o e-mail institucional para “organizar a caixa de entrada”.", "Vermelho", {
            "Verde": "Não. E-mail institucional envolve dados de terceiros e da instituição; não é fonte pública nem fictícia.",
            "Amarelo": "Não. Amarelo é para conta pessoal própria. Conta de trabalho é Vermelho.",
            "Vermelho": "Correto. Conta de trabalho com dados de terceiros: não conectar sem autorização da instituição.",
            "Não se aplica": "Não. Todo uso de conector pode ser classificado pelo semáforo; este é Vermelho."}),
        semaforo("Cenário C: criar, na própria agenda pessoal, um evento de teste sem convidados, com aprovação manual.", "Amarelo", {
            "Verde": "Não. Há escrita numa conta pessoal real; Verde é só leitura de fonte pública ou dados fictícios.",
            "Amarelo": "Correto. Conta pessoal própria, com escrita: executar com Needs approval, conferir e apagar ao final.",
            "Vermelho": "Não. É a sua própria conta pessoal, sem dados de terceiros nem sigilo profissional.",
            "Não se aplica": "Não. Todo uso de conector pode ser classificado pelo semáforo; este é Amarelo."}),
        semaforo("Cenário D: instalar um conector cuja página pede que se cole a senha do serviço na conversa.", "Vermelho", {
            "Verde": "Não. Pedido de senha na conversa é sinal de alerta, qualquer que seja o serviço.",
            "Amarelo": "Não. Não é questão de aprovar a escrita: o conector nem deve ser instalado.",
            "Vermelho": "Correto. Não instalar: autenticação legítima ocorre por login no próprio serviço, nunca por senha na conversa.",
            "Não se aplica": "Não. O cenário é classificável, e é Vermelho: não instalar."}),
    ]),
    ("l2_ficha", 2, 11, [html("l3-ficha.html", trava=True), cont("completeBlock")]),
    ("l2_continue", 2, 3, [cont()]),
    # ---- Licao 4 (licao 3)
    ("l3_confianca", 3, 10, [html("l4-confianca.html")]),
    ("l3_continue2", 3, 8, [cont()]),
    ("l3_continue1", 3, 4, [cont()]),
    # ---- Licao 5 (licao 4)
    ("l4_arquivo_ordem", 4, 8, [html("l5-arquivo-ordem.html", trava=True, largura="0"), cont("completeBlock")]),
    ("l4_abas", 4, 5, [
        {"modelo": "text-text-paragraph.json", "itens": [{"paragraph": "<p>Compare os dois caminhos, lado a lado:</p>"}]},
        {"modelo": "interactive-interactive-tabs.json", "itens": [
            {"title": "Caminho local — Filesystem",
             "description": "<p><strong>Onde roda:</strong> no computador, pelo Claude Desktop. <strong>Onde está disponível:</strong> somente no Claude Desktop.</p><p></p><p><strong>O que lê:</strong> arquivos das pastas autorizadas. <strong>Ferramentas de escrita:</strong> criar pasta, gravar, editar, mover. <strong>Como restringir:</strong> autorizar uma única pasta.</p>"},
            {"title": "Caminho remoto — Google Drive",
             "description": "<p><strong>Onde roda:</strong> na nuvem, a partir da conta Claude. <strong>Onde está disponível:</strong> navegador, aplicativo e celular.</p><p></p><p><strong>O que lê:</strong> Docs, Sheets, Slides, PDFs e arquivos do Office do Drive. <strong>Ferramentas de escrita:</strong> compartilhar, mover, enviar para a lixeira, upload. <strong>Como restringir:</strong> Tool permissions em Needs approval ou Blocked; pasta não compartilhada.</p>"}]},
    ]),
    ("l4_continue", 4, 3, [cont()]),
    # ---- Licao 6 (licao 5)
    ("l5_revise", 5, 11, [html("l6-revise.html", trava=True), cont("completeBlock")]),
    ("l5_continue", 5, 3, [cont()]),
    # ---- Licao 7 (licao 6)
    ("l6_devolucao", 6, 13, [html("l7-devolucao.html", trava=True, largura="0"), cont("completeBlock")]),
    ("l6_sintese", 6, 7, [html("l7-sintese.html")]),
    ("l6_continue", 6, 3, [cont()]),
]

for n, (nome, licao, pos, blocos) in enumerate(ROTEIROS, start=1):
    arq = AQUI / "roteiros" / f"r{n:02d}_{nome}.json"
    arq.write_text(json.dumps({"licao": licao, "posicao": pos, "blocos": blocos}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(arq.name)
