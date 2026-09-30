"""Extrai todo texto pedagogico legivel de uma licao, em ordem, com os ids dos blocos."""
import json
import sys

CAMPOS_TEXTO = ("paragraph", "heading", "text", "title", "caption", "label", "prompt", "feedback", "description", "body", "subtitle", "altText")


def dump(obj, prefixo="", caminho=""):
    if isinstance(obj, dict):
        tipo = obj.get("type") or obj.get("family") or obj.get("variant")
        oid = obj.get("id")
        cabeca = f"{prefixo}-- id={oid} type={tipo}" if oid else None
        impresso_cabeca = False
        for campo in CAMPOS_TEXTO:
            v = obj.get(campo)
            if isinstance(v, str) and v.strip():
                if not impresso_cabeca and cabeca:
                    print(cabeca)
                    impresso_cabeca = True
                print(f"{prefixo}   {campo}: {v}")
        for k, v in obj.items():
            if isinstance(v, (list, dict)):
                dump(v, prefixo + "  ", caminho + "/" + k)
    elif isinstance(obj, list):
        for v in obj:
            dump(v, prefixo, caminho)


def main(caminho):
    with open(caminho, encoding="utf-8") as f:
        data = json.load(f)
    lesson = data["lesson"]
    print(f"=== Licao {data['numero_da_licao']}: {data['title']} ===\n")
    dump(lesson.get("items", []))


if __name__ == "__main__":
    main(sys.argv[1])
