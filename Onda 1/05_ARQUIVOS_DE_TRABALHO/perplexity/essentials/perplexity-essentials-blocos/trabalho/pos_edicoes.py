"""Edições de texto em campos que validar_estrutura.py e validar.py não cobrem (autorizadas pelo usuário):
course.description (capa), matchTitle da associação de rótulos do quiz, date da linha do tempo da lição 7
("Step N" -> "Etapa N") e completeHint de todos os Continues (aviso em inglês -> português).

Uso: python -I pos_edicoes.py ENTRADA.json SAIDA.json
Depois de editar, compara ENTRADA x SAIDA folha a folha e falha se mudou qualquer coisa fora desses campos.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ent, sai = Path(sys.argv[1]), Path(sys.argv[2])
if sai.exists():
    raise SystemExit(f"{sai} já existe; escolha outro nome.")

antes = json.loads(ent.read_text(encoding="utf-8"))
dados = json.loads(ent.read_text(encoding="utf-8"))
curso = dados["course"]

CAPA = ("Como saber se uma resposta de IA diz mesmo o que a fonte diz? Neste curso, você aprende a pesquisar com a "
        "Perplexity — um motor de respostas que pesquisa a web e associa as afirmações a citações — e a tratar cada "
        "citação como ponto de partida da conferência. Pensado para estudantes, pesquisadores, jornalistas, analistas "
        "e profissionais do Direito, o curso percorre o fluxo completo: proteger o que entra na pergunta, formular "
        "perguntas delimitadas, escolher a profundidade da busca, conferir as citações no documento original e "
        "produzir uma síntese citada com limites declarados.")
PRO_ANTIGO = "Pro Search — opção de busca com modelo mais avançado e cota diária no plano gratuito."
PRO_NOVO = "Pro Search — busca que encadeia várias pesquisas e combina dezenas de fontes, com cota diária no plano gratuito."
HINT_ANTIGO = "Complete the content above before moving on."
HINT_NOVO = "Conclua o conteúdo acima para continuar."
TIMELINE_ID = "0a3802a7-dd81-4a9e-834c-d39a1c83944c"

contagem = {"description": 0, "matchTitle": 0, "date": 0, "completeHint": 0}

assert curso["description"].startswith("Você já se perguntou"), "capa inesperada"
curso["description"] = CAPA
contagem["description"] += 1

for licao in curso["lessons"]:
    for bloco in licao.get("items", []):
        if bloco.get("type") == "MATCHING":
            for a in bloco.get("answers", []):
                if a.get("matchTitle") == PRO_ANTIGO:
                    a["matchTitle"] = PRO_NOVO
                    contagem["matchTitle"] += 1
        if bloco.get("id") == TIMELINE_ID:
            for it in bloco["items"]:
                assert it["date"].startswith("Step "), it["date"]
                it["date"] = "Etapa " + it["date"][5:]
                contagem["date"] += 1
        if bloco.get("type") == "divider" and bloco.get("family") == "continue":
            for it in bloco["items"]:
                if it.get("completeHint") == HINT_ANTIGO:
                    it["completeHint"] = HINT_NOVO
                    contagem["completeHint"] += 1

# Checagem: só podem ter mudado folhas com estes nomes.
PERMITIDOS = set(contagem)
mudancas, proibidas = [], []


def comparar(a, b, caminho):
    if isinstance(a, dict):
        if not isinstance(b, dict) or a.keys() != b.keys():
            proibidas.append(f"CHAVES/TIPO em {caminho}")
            return
        for k in a:
            comparar(a[k], b[k], f"{caminho}.{k}")
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b):
            proibidas.append(f"ARRAY em {caminho}")
            return
        for i, (x, y) in enumerate(zip(a, b)):
            comparar(x, y, f"{caminho}[{i}]")
    elif a != b:
        campo = caminho.rsplit(".", 1)[-1]
        (mudancas if campo in PERMITIDOS else proibidas).append(caminho)


comparar(antes, dados, "")
if proibidas:
    print("\n".join(proibidas))
    raise SystemExit("REPROVADO: mudou algo fora dos campos permitidos. Nada gravado.")
if contagem["description"] != 1 or contagem["matchTitle"] != 1 or contagem["date"] != 5:
    raise SystemExit(f"REPROVADO: contagem inesperada {contagem}. Nada gravado.")
if len(mudancas) != sum(contagem.values()):
    raise SystemExit("REPROVADO: número de folhas alteradas não bate com as edições. Nada gravado.")

sai.write_text(json.dumps(dados, ensure_ascii=False), encoding="utf-8")
print("Edições:", contagem, "| folhas alteradas:", len(mudancas))
print("APROVADO: só mudaram description (capa), matchTitle, date e completeHint.")
