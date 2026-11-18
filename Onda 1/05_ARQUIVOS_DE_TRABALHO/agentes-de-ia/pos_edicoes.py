"""Edições de texto em campos que validar_estrutura.py e validar.py não cobrem:
course.description (capa) e completeHint de todos os Continues (aviso em inglês -> português).

Uso: python -I pos_edicoes.py essentials|hands-on ENTRADA.json SAIDA.json
Depois de editar, compara ENTRADA x SAIDA folha a folha e falha se mudou qualquer coisa fora desses campos.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
qual, ent, sai = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
if sai.exists():
    raise SystemExit(f"{sai} já existe; escolha outro nome.")

CAPAS = {
    "essentials": ("Já pensou em aumentar sua eficiência",
        "Como passar a um agente de IA uma tarefa de várias etapas — e saber se ele fez direito? Pensado para "
        "profissionais de escritório e equipes jurídicas, este curso ensina a delegar com método: avaliar o risco "
        "antes de começar, redigir a ordem de serviço com objetivo, fontes, limites, critérios e produto, acompanhar "
        "a execução e intervir sem recomeçar, conferir o resultado contra a fonte e reconhecer os limites do agente. "
        "A prática usa o Manus no plano gratuito, com rotas para o ChatGPT Work e o Claude Cowork, sobre documentos "
        "públicos como o Guia de uso de IA generativa do TCU."),
    "hands-on": ("Você já imaginou entregar tarefas complexas",
        "Em menos de duas horas, você vai mandar um agente de IA fazer um trabalho de várias etapas, corrigir o rumo "
        "no meio do caminho, pegar o agente num erro — e flagrar uma instrução escondida antes que ela faça estrago. "
        "São quatro oficinas e um projeto final com documentos públicos (o Guia de IA generativa do TCU, o guia da "
        "CGU ou a Recomendação 001/2024 da OAB), para quem trabalha em escritório ou no jurídico. Basta o plano "
        "gratuito do Manus; quem assina ChatGPT Plus ou Claude Pro pode usar o Work ou o Cowork."),
}
HINT_ANTIGO = "Complete the content above before moving on."
HINT_NOVO = "Conclua o conteúdo acima para continuar."

antes = json.loads(ent.read_text(encoding="utf-8"))
dados = json.loads(ent.read_text(encoding="utf-8"))
curso = dados["course"]
contagem = {"description": 0, "completeHint": 0}

inicio, capa = CAPAS[qual]
assert curso["description"].startswith(inicio), "capa inesperada"
curso["description"] = capa
contagem["description"] += 1

for licao in curso["lessons"]:
    for bloco in licao.get("items", []):
        if bloco.get("type") == "divider" and bloco.get("family") == "continue":
            for it in bloco["items"]:
                if it.get("completeHint") == HINT_ANTIGO:
                    it["completeHint"] = HINT_NOVO
                    contagem["completeHint"] += 1

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
if contagem["description"] != 1 or contagem["completeHint"] < 1:
    raise SystemExit(f"REPROVADO: contagem inesperada {contagem}. Nada gravado.")
if len(mudancas) != sum(contagem.values()):
    raise SystemExit("REPROVADO: número de folhas alteradas não bate com as edições. Nada gravado.")

sai.write_text(json.dumps(dados, ensure_ascii=False), encoding="utf-8")
print("Edições:", contagem, "| folhas alteradas:", len(mudancas))
print("APROVADO: só mudaram description (capa) e completeHint.")
