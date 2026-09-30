"""Percorre todas as licoes e imprime cada pergunta de multipla escolha com a
alternativa marcada como correta e o feedback de cada alternativa, para
conferencia cruzada."""
import json
import glob


def walk(obj, licao_titulo):
    if isinstance(obj, dict):
        if obj.get("type") in ("MULTIPLE_CHOICE", "MULTIPLE_RESPONSE", "TRUE_FALSE"):
            print(f"\n=== [{licao_titulo}] {obj.get('title')}")
            print(f"    corrects: {obj.get('corrects')}")
            for opt in obj.get("answers", []) or obj.get("items", []) or []:
                if isinstance(opt, dict):
                    marca = "CORRETA" if opt.get("correct") else "errada "
                    print(f"    [{marca}] {opt.get('title')}")
                    if opt.get("feedback"):
                        print(f"              -> {opt.get('feedback')}")
        for v in obj.values():
            if isinstance(v, (list, dict)):
                walk(v, licao_titulo)
    elif isinstance(obj, list):
        for v in obj:
            walk(v, licao_titulo)


for path in sorted(glob.glob("licoes_extraidas_ChatGPTWord/licao_*.json")):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    walk(data["lesson"].get("items", []), data["title"])
