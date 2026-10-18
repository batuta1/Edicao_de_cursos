"""Gera os roteiros de insercao da fase B (um por ponto de insercao), na ordem de aplicacao.
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

def questao(titulo, alternativas):
    return {"modelo": "knowledgecheck-knowledgecheck-multiple-choice.json",
            "itens": [{"title": titulo, "answers": [{"title": t, "correct": c, "feedback": f} for t, c, f in alternativas]}]}

ROTEIROS = [
    # ---- Licao 1 (licao 0)
    ("l0_registro", 0, 15, [html("l1-registro.html", trava=True, largura="0"), cont("completeBlock")]),
    ("l0_sobre", 0, 0, [
        {"modelo": "text-text-heading-paragraph.json", "itens": [{
            "heading": "Sobre este curso",
            "paragraph": "<p>Este curso prepara você para usar o NotebookLM — chamado Gemini Notebook desde 16/07/2026 — para estudar e sintetizar um conjunto delimitado de fontes próprias, com segurança e conferindo sistematicamente as citações. Ao final, você terá montado um notebook com quatro fontes públicas, obtido respostas auditadas pelas citações e gerado, no painel Estúdio, documento de resumo, guia de estudo e Resumo em Áudio.</p><p>São 129 minutos, com um mesmo notebook — o Caderno LGPD — acompanhando as lições de fontes, consultas, Estúdio e aplicação. Você precisa de um computador com navegador atualizado, uma Conta Google e acesso a notebook.google.com; o plano gratuito basta para todas as atividades.</p><p>Concluído o curso, você deverá ser capaz de:</p>"}]},
        {"modelo": "list-list-numbered.json", "itens": [
            {"paragraph": "<p>Explicar o princípio da ancoragem nas fontes e o papel das citações na conferência das respostas.</p>"},
            {"paragraph": "<p>Decidir, antes de qualquer upload, se uma fonte pode ser importada, em qual conta e com qual compartilhamento.</p>"},
            {"paragraph": "<p>Montar um notebook com fontes de tipos diferentes e diagnosticar importações malsucedidas.</p>"},
            {"paragraph": "<p>Formular perguntas ancoradas e auditar as respostas por meio das citações.</p>"},
            {"paragraph": "<p>Gerar e revisar artefatos de estudo no painel Estúdio, aplicando o fluxo completo ao próprio perfil profissional.</p>"}]},
        {"modelo": "text-impact-b.json", "itens": [{
            "paragraph": "<p>⚠️ <strong>Vigência:</strong> planos, limites e rótulos de interface foram extraídos da Central de Ajuda oficial consultada em 17/10/2026. A ferramenta muda com frequência; se um botão tiver outro nome na sua tela, siga o caminho a partir de notebook.google.com.</p>"}]},
        cont(),
    ]),
    # ---- Licao 2 (licao 1)
    ("l1_paineis", 1, 10, [html("l2-paineis.html")]),
    # ---- Licao 3 (licao 2)
    ("l2_questao_compart", 2, 15, [questao(
        "Você quer que um colega leia as fontes do seu Caderno LGPD e faça perguntas na conversa, mas sem poder adicionar ou remover fontes. Qual compartilhamento escolher?",
        [("Editor, com acesso por link para qualquer pessoa com Conta Google.", False,
          "Não. Editor pode adicionar e remover fontes e compartilhar, e o link abre o acesso a qualquer pessoa com Conta Google."),
         ("Leitor, compartilhado com o e-mail do colega.", True,
          "Correto. Leitor lê fontes e notas e usa a conversa; compartilhar com a pessoa específica segue o princípio do menor privilégio."),
         ("Editor, compartilhado com o e-mail do colega.", False,
          "Não. A pessoa está certa, mas o papel não: Editor também pode adicionar e remover fontes e compartilhar."),
         ("Visualização da conversa, para que ele não veja as fontes.", False,
          "Não. O colega precisa ler as fontes, e a visualização da conversa só as oculta na apresentação, sem revogar o acesso a elas.")])]),
    ("l2_semaforo", 2, 12, [html("l3-semaforo.html", trava=True), cont("completeBlock")]),
    # ---- Licao 4 (licao 3)
    ("l3_checklist", 3, 16, [html("l4-checklist.html", trava=True, largura="0"), cont("completeBlock")]),
    # ---- Licao 5 (licao 4)
    ("l4_audite", 4, 6, [html("l5-audite.html", trava=True), cont("completeBlock")]),
    ("l4_pedido", 4, 4, [html("l5-pedido.html", largura="0")]),
    # ---- Licao 6 (licao 5)
    ("l5_questao_audio", 5, 13, [questao(
        "Você quer um Resumo em Áudio curto, com um apresentador, em português, para ouvir antes de uma aula. Como configurar em Personalizar?",
        [("Formato Conversa aprofundada (Deep Dive), duração Longer e idioma padrão.", False,
          "Não. A Conversa aprofundada não é o formato curto, a duração Longer é documentada só para inglês e, sem escolher o idioma, o áudio pode sair em inglês."),
         ("Formato Debate, idioma Português (Brasil) e modo interativo.", False,
          "Não. Debate não é o formato curto com um apresentador, e o modo interativo é documentado só para inglês."),
         ("Formato Crítica (Critique), sem escolher idioma nem orientação.", False,
          "Não. Crítica não é o formato curto com um apresentador, e sem escolher Português (Brasil) o áudio pode sair em inglês."),
         ("Formato Resumo (The Brief), idioma Português (Brasil) e uma orientação de foco.", True,
          "Correto. O Resumo (The Brief) tem um apresentador e menos de dois minutos; escolher Português (Brasil) evita o áudio em inglês, e a orientação define o foco.")])]),
    ("l5_estudio", 5, 8, [html("l6-estudio.html")]),
    # ---- Licao 7 (licao 6)
    ("l6_criterios", 6, 13, [html("l7-criterios.html", trava=True, largura="0"), cont("completeBlock")]),
    ("l6_ferramenta", 6, 7, [html("l7-ferramenta.html")]),
]

for n, (nome, licao, pos, blocos) in enumerate(ROTEIROS, start=1):
    arq = AQUI / "roteiros" / f"r{n:02d}_{nome}.json"
    arq.write_text(json.dumps({"licao": licao, "posicao": pos, "blocos": blocos}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(arq.name)
