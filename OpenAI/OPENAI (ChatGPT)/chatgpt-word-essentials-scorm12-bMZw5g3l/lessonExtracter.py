"""Separa cursoChatGPTWord.json em um arquivo por licao, ordenados por position."""
import json
import os
import re

CURSO_JSON = "cursoChatGPTWord.json"
PASTA_SAIDA = "licoes_extraidas_ChatGPTWord"


def slug(title):
    s = re.sub(r"[^\w\s-]", "", title, flags=re.UNICODE)
    s = re.sub(r"\s+", "_", s.strip())
    return s[:60]


def main():
    with open(CURSO_JSON, encoding="utf-8") as f:
        data = json.load(f)

    lessons = data["course"]["lessons"]
    lessons_ord = sorted(lessons, key=lambda l: l.get("position", 0))

    os.makedirs(PASTA_SAIDA, exist_ok=True)

    indice = []
    for i, lesson in enumerate(lessons_ord):
        numero = i
        title = lesson.get("title", f"licao_{numero}")
        nome_arquivo = f"licao_{numero:02d}_{slug(title)}.json"
        caminho = os.path.join(PASTA_SAIDA, nome_arquivo)

        payload = {
            "numero_da_licao": numero,
            "position_original": lesson.get("position"),
            "title": title,
            "lesson": lesson,
        }
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

        indice.append({
            "numero_da_licao": numero,
            "arquivo": nome_arquivo,
            "title": title,
            "id": lesson.get("id"),
            "position_original": lesson.get("position"),
        })
        print(f"{numero:02d}: {title}  -> {nome_arquivo}")

    with open(os.path.join(PASTA_SAIDA, "indice_licoes.json"), "w", encoding="utf-8") as f:
        json.dump(indice, f, ensure_ascii=False, indent=2)

    print(f"\nTotal: {len(lessons_ord)} licoes gravadas em {PASTA_SAIDA}/")


if __name__ == "__main__":
    main()
