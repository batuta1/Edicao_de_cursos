import json
from collections import Counter
from pathlib import Path

arquivo = Path(__file__).parent / "cursoVSCODEtest.json"

with open(arquivo, "r", encoding="utf-8") as f:
    dados = json.load(f)

tipos = Counter()

def percorrer(obj):
    if isinstance(obj, dict):
        if "type" in obj:
            tipos[obj["type"]] += 1
        for valor in obj.values():
            percorrer(valor)
    elif isinstance(obj, list):
        for item in obj:
            percorrer(item)

percorrer(dados)

for tipo, quantidade in tipos.most_common():
    print(f"{tipo}: {quantidade}")