"""
Diz a que versão de um curso pertence um pacote SCORM do Rise 360 (zip ou pasta extraída).

Lê o JSON do curso (sem descompactar o zip), calcula a impressão digital do conteúdo e a data de
publicação, e, se receber a pasta do curso, compara com as versões que já estão em scorm/vN/.

Uso:
    python versao_do_pacote.py PACOTE                          # só a ficha do pacote
    python versao_do_pacote.py PACOTE --curso Cursos/Anthropic/claude-chat-essentials

Só lê; não move nem grava nada.
"""
import argparse
import base64
import hashlib
import json
import pathlib
import re
import sys
import zipfile

VARIANTES = (
    ("scormcontent/runtime-data.js", re.compile(r'__jsonp\(\s*"runtime-data\.js"\s*,\s*"([A-Za-z0-9+/=]+)"')),
    ("scormcontent/index.html", re.compile(r'deserialize\(\s*"([A-Za-z0-9+/=]+)"')),
)


def _base64_do_texto(nome, texto):
    for sufixo, padrao in VARIANTES:
        if nome.endswith(sufixo):
            m = padrao.search(texto)
            if m:
                return m.group(1)
    return None


def ler_base64(caminho):
    """Devolve o base64 do curso, ou None se o pacote não for um Rise reconhecido."""
    p = pathlib.Path(caminho)
    if p.is_dir():
        for sufixo, _ in VARIANTES:
            for f in sorted(p.rglob(sufixo.split("/")[-1])):
                if f.as_posix().endswith(sufixo):
                    b = _base64_do_texto(f.as_posix(), f.read_text(encoding="utf-8", errors="replace"))
                    if b:
                        return b
        return None
    if not zipfile.is_zipfile(p):
        return None
    with zipfile.ZipFile(p) as z:
        nomes = z.namelist()
        for sufixo, _ in VARIANTES:
            for n in sorted(x for x in nomes if x.endswith(sufixo)):
                b = _base64_do_texto(n, z.read(n).decode("utf-8", errors="replace"))
                if b:
                    return b
    return None


def ficha(caminho):
    b64 = ler_base64(caminho)
    if not b64:
        return None
    curso = json.loads(base64.b64decode(b64).decode("utf-8-sig"))["course"]
    return {
        "caminho": str(caminho),
        "id": curso.get("id"),
        "titulo": curso.get("title"),
        "publicado": curso.get("lastPublishedAt") or "",
        "impressao": hashlib.sha256(b64.encode()).hexdigest()[:10],
    }


def versoes_do_curso(pasta_do_curso):
    """{n: [fichas]} das pastas scorm/vN (pacotes principais e cópias)."""
    saida = {}
    base = pathlib.Path(pasta_do_curso) / "scorm"
    for v in sorted(base.glob("v[0-9]*"), key=lambda x: int(x.name[1:])):
        fichas = []
        itens = [i for i in v.iterdir() if i.name != "copias"]
        if (v / "copias").is_dir():
            itens += list((v / "copias").iterdir())
        for i in itens:
            f = ficha(i)
            if f:
                fichas.append(f)
        saida[int(v.name[1:])] = fichas
    return saida


def main():
    ap = argparse.ArgumentParser(description="Versão de um pacote SCORM do Rise 360.")
    ap.add_argument("pacote")
    ap.add_argument("--curso", help="pasta do curso (Cursos/<Empresa>/<curso>) para comparar com scorm/vN")
    a = ap.parse_args()

    f = ficha(a.pacote)
    if not f:
        print("Não reconheci o pacote como Rise 360 (sem scormcontent/runtime-data.js nem index.html com o curso).")
        return 2
    print(f"Pacote     : {f['caminho']}")
    print(f"Título     : {f['titulo']}")
    print(f"Projeto Rise: {f['id']}   (identifica o curso no Rise; muda só se o curso for recriado)")
    print(f"Publicado  : {f['publicado'] or '(sem data)'}")
    print(f"Impressão  : {f['impressao']}   (mesma impressão = mesmo conteúdo = mesma versão)")
    if not a.curso:
        return 0

    versoes = versoes_do_curso(a.curso)
    print(f"\nVersões já em {a.curso}/scorm:")
    for n, fs in versoes.items():
        pubs = sorted(x["publicado"] for x in fs if x["publicado"])
        print(f"  v{n}: {len(fs)} pacote(s), publicada em {pubs[0][:10] if pubs else '?'}, impressão {', '.join(sorted({x['impressao'] for x in fs}))}")
    for n, fs in versoes.items():
        if any(x["impressao"] == f["impressao"] for x in fs):
            print(f"\n=> MESMO CONTEÚDO que a v{n}: guarde em scorm/v{n}/copias/ (não crie versão nova).")
            return 0
    ultimas = [max((x["publicado"] for x in fs if x["publicado"]), default="") for fs in versoes.values()]
    posicao = 1 + sum(1 for u in ultimas if u <= f["publicado"])
    if posicao == len(versoes) + 1:
        print(f"\n=> CONTEÚDO NOVO e mais recente: crie scorm/v{posicao}/.")
    else:
        print(f"\n=> CONTEÚDO NOVO, mas mais antigo que a v{posicao}: ele seria a v{posicao}; "
              f"renumere (git mv) da v{posicao} em diante e atualize o scorm/LEIAME.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
