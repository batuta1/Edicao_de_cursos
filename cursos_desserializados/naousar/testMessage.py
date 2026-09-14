import json
from pathlib import Path

pasta_base = Path(__file__).parent
pasta_licoes = pasta_base / "licoes_extraidas"

frase_teste = "OI EU EDITEI AQUI"

def procurar_texto(obj, texto):
    if isinstance(obj, dict):
        return any(procurar_texto(v, texto) for v in obj.values())
    elif isinstance(obj, list):
        return any(procurar_texto(item, texto) for item in obj)
    elif isinstance(obj, str):
        return texto in obj
    return False

encontrou = False

for arquivo in sorted(pasta_licoes.glob("licao_*.json")):
    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = json.load(f)

    if procurar_texto(conteudo, frase_teste):
        print(f"Frase encontrada no arquivo: {arquivo.name}")

        if procurar_texto(conteudo.get("lesson", {}), frase_teste):
            print("A frase está DENTRO de 'lesson'. Ela deve entrar no curso editado.")
        else:
            print("A frase está FORA de 'lesson'. Ela NÃO será reinserida no curso.")

        encontrou = True

if not encontrou:
    print("A frase não foi encontrada em nenhum arquivo da pasta licoes_extraidas.")