"""Monta os HTMLs finais (documento completo + CSS comum) a partir de src/*.body.html.
Uso: python -I build.py   (rodar com o caminho; lê e grava ao lado deste arquivo)
Cada src começa com uma linha <!--titulo: ...-->.
"""
import pathlib, re

AQUI = pathlib.Path(__file__).resolve().parent
CSS = (AQUI / "src" / "comum.css").read_text(encoding="utf-8")

for src in sorted((AQUI / "src").glob("*.body.html")):
    corpo = src.read_text(encoding="utf-8")
    m = re.match(r"<!--titulo: (.*?)-->\s*", corpo)
    assert m, f"{src.name}: falta a linha de titulo"
    titulo, corpo = m.group(1), corpo[m.end():]
    doc = ("<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n<meta charset=\"utf-8\">\n"
           "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
           f"<title>{titulo}</title>\n<style>\n{CSS}\n</style>\n</head>\n<body>\n{corpo}\n</body>\n</html>\n")
    assert "http://" not in doc and "https://" not in doc, f"{src.name}: referencia externa"
    destino = AQUI / src.name.replace(".body.html", ".html")
    destino.write_text(doc, encoding="utf-8")
    print("gerado", destino.name, len(doc), "bytes")
