"""F3: casa o "Curso" do checklist com a pasta em Cursos/. Automático, sem mapa manual (D5): só aceita casamento exato por slug."""
import json
from pathlib import Path

from ..texto import slug


def carregar_registro(caminho):
    return json.loads(Path(caminho).read_text(encoding="utf-8"))


def indice(registro):
    """Uma entrada por curso do registro, com as chaves pelas quais ele pode ser achado."""
    saida = []
    for c in registro.get("cursos", []):
        s = slug(c["curso"])
        chaves = {s, s.removeprefix(slug(c["empresa"]) + "-")}
        titulo = ((c.get("ficha") or {}).get("curso") or {}).get("titulo")
        if titulo:
            chaves.add(slug(titulo))
        saida.append({"empresa": c["empresa"], "curso": c["curso"], "versao": c["versao"], "chaves": chaves})
    return saida


def casar(nomes, cursos):
    """Devolve (casados {nome: curso}, ambiguos {nome: [cursos]}, sem_pasta [nomes], pastas_sem_linha [cursos])."""
    casados, ambiguos, sem_pasta, usados = {}, {}, [], set()
    for nome in dict.fromkeys(nomes):
        achados = [c for c in cursos if slug(nome) in c["chaves"]]
        if len(achados) == 1:
            casados[nome] = achados[0]
            usados.add((achados[0]["empresa"], achados[0]["curso"]))
        elif achados:
            ambiguos[nome] = achados
        else:
            sem_pasta.append(nome)
    sobras = [c for c in cursos if (c["empresa"], c["curso"]) not in usados]
    return casados, ambiguos, sem_pasta, sobras
