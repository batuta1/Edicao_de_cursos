"""MVP1.1, Fase E: o resumo estratégico. Um registro por curso, com as versões e a vigente; sem texto de conteúdo.

Entrada: uma lista de entradas, uma por pacote da lista de controle, cada uma com a `ficha` já lida (ou None se o pacote
deu erro) e, quando for o caso, `erro`. A versão vigente de um curso é a de maior número (D04-1, sugestão A).
"""
from collections import defaultdict

from .controle import COPIA
from .varredura import numero_da_versao as _numero

SCHEMA_DO_RESUMO = 1


def _metricas(ficha):
    curso, tamanho = ficha.get("curso") or {}, ficha.get("tamanho") or {}
    return {
        "titulo": curso.get("titulo"),
        "publicado": (curso.get("publicado") or "")[:10] or None,
        "capitulos": tamanho.get("capitulos"),
        "blocos": tamanho.get("blocos"),
        "palavras": tamanho.get("palavras"),
        "minutos_de_leitura_estimados": tamanho.get("minutos_de_leitura_estimados"),
        "questoes_do_quiz": tamanho.get("questoes_do_quiz"),
        "alertas": [a["codigo"] for a in ficha.get("alertas") or []],
    }


def _principal(entradas):
    """Uma versão = todos os pacotes de `<empresa>/<curso>/scorm/vN`. O principal é o primeiro que não é cópia e tem ficha."""
    ordem = sorted(entradas, key=lambda e: (bool(e.get("copia")), e["status"] == COPIA, e["tipo"] != "zip", e["caminho"]))
    com_ficha = [e for e in ordem if e.get("ficha")]
    return ordem, com_ficha, (com_ficha[0] if com_ficha else None)


def _registro_da_versao(entradas, autoria=None):
    ordem, com_ficha, principal = _principal(entradas)
    impressoes = {(e["ficha"].get("pacote") or {}).get("impressao_do_curso") for e in com_ficha}
    registro = {"versao": entradas[0].get("versao"),
                **(_metricas(principal["ficha"]) if principal else {"titulo": None}),
                "pacote_principal": (principal or ordem[0])["caminho"],
                "pacotes": len(entradas),
                "copias_identicas": sum(1 for e in entradas if e["status"] == COPIA),
                "conteudos_diferentes": len(impressoes),
                **(autoria(entradas, principal) if autoria else {})}
    if len(impressoes) > 1:
        registro["alertas"] = registro.get("alertas", []) + ["versao_com_mais_de_um_conteudo"]
    problemas = [{"caminho": e["caminho"], "mensagem": e["erro"]} for e in entradas if e.get("erro")]
    if problemas:
        registro["problemas"] = problemas
    elif principal is None:
        registro["nao_lida"] = True                              # só acontece com «só as últimas versões»: esta versão ficou fora
    return registro


def _duplicados(entradas):
    """Pacotes de conteúdo repetido, mesmo quando os bytes não batem (uma pasta e o zip dela, por exemplo).

    Compara a impressão do conteúdo do curso (`pacote.impressao_do_curso` da ficha). Uma cópia idêntica de outro pacote
    não entra: ela já é a mesma coisa byte a byte. `nao_comparados` são os pacotes lidos sem impressão (outro formato).
    """
    grupos, sem_impressao = defaultdict(list), []
    for e in entradas:
        if e["status"] == COPIA or not e.get("ficha"):
            continue
        impressao = (e["ficha"].get("pacote") or {}).get("impressao_do_curso")
        (grupos[impressao] if impressao else sem_impressao).append(e)
    lista = []
    for impressao, pacotes in sorted(grupos.items(), key=lambda kv: sorted(e["caminho"] for e in kv[1])):
        if len(pacotes) < 2:
            continue
        tipos = {e["tipo"] for e in pacotes}
        lista.append({"impressao": impressao, "titulo": _metricas(pacotes[0]["ficha"])["titulo"],
                      "tipos": "pasta_e_zip" if len(tipos) > 1 else f"so_{tipos.pop()}s",
                      "mesma_versao": len({(e["empresa"], e["curso"], e["versao"]) for e in pacotes}) == 1 and bool(pacotes[0].get("versao")),
                      "pacotes": [{"caminho": e["caminho"], "tipo": e["tipo"], "empresa": e["empresa"], "curso": e["curso"], "versao": e["versao"]}
                                  for e in sorted(pacotes, key=lambda e: e["caminho"])]})
    return {"grupos": lista, "nao_comparados": sorted(e["caminho"] for e in sem_impressao)}


def montar(entradas, gerado_em, nao_scorm=0, autoria=None):
    grupos, fora = defaultdict(lambda: defaultdict(list)), []
    for e in entradas:
        if e.get("curso") and e.get("versao"):
            grupos[(e["empresa"], e["curso"])][e["versao"]].append(e)
        else:
            fora.append(e)
    cursos = []
    for (empresa, curso), versoes in sorted(grupos.items()):
        registros = [_registro_da_versao(v, autoria) for _, v in sorted(versoes.items(), key=lambda kv: _numero(kv[0]))]
        cursos.append({"empresa": empresa, "curso": curso, "vigente": registros[-1]["versao"], "versoes": registros})
    resumo = {
        "schema": SCHEMA_DO_RESUMO,
        "gerado_em": gerado_em,
        "totais": {"cursos": len(cursos), "versoes": sum(len(c["versoes"]) for c in cursos), "pacotes": len(entradas),
                   "copias_identicas": sum(1 for e in entradas if e["status"] == COPIA),
                   "com_erro": sum(1 for e in entradas if e.get("erro")), "nao_scorm": nao_scorm},
        "duplicados": _duplicados(entradas),
        "cursos": cursos,
    }
    if fora:
        resumo["fora_do_padrao"] = [{"caminho": e["caminho"], **(_metricas(e["ficha"]) if e.get("ficha") else {"titulo": None}),
                                     **({"problemas": [e["erro"]]} if e.get("erro") else {})} for e in fora]
    return resumo


SCHEMA_DAS_ULTIMAS = 1


def montar_ultimas(entradas, gerado_em, autoria=None):
    """Um JSON só com a ficha completa da última versão (maior `vN`) de cada curso, para quem não quer abrir uma ficha por pacote.

    Entrada: as mesmas entradas do `montar`. Uma última versão sem ficha (erro, ou não lida) vai em `sem_ficha`, com o motivo.
    Pacotes fora do padrão (sem curso e versão) vão em `fora_do_padrao`, também com a ficha.
    """
    grupos, fora = defaultdict(lambda: defaultdict(list)), []
    for e in entradas:
        if e.get("curso") and e.get("versao"):
            grupos[(e["empresa"], e["curso"])][e["versao"]].append(e)
        else:
            fora.append(e)
    cursos, sem_ficha = [], []
    for (empresa, curso), versoes in sorted(grupos.items()):
        versao, pacotes = max(versoes.items(), key=lambda kv: _numero(kv[0]))
        _, _, principal = _principal(pacotes)
        autor = autoria(pacotes, principal) if autoria else {}
        if principal:
            cursos.append({"empresa": empresa, "curso": curso, "versao": versao, **autor, "pacote": principal["caminho"], "ficha": principal["ficha"]})
        else:
            erro = next((e["erro"] for e in pacotes if e.get("erro")), None)
            sem_ficha.append({"empresa": empresa, "curso": curso, "versao": versao, **autor,
                              "motivo": erro or "ainda não lida (rode sem «só as últimas versões» ou com --forcar)"})
    resultado = {"schema": SCHEMA_DAS_ULTIMAS, "gerado_em": gerado_em,
                 "totais": {"cursos": len(cursos), "sem_ficha": len(sem_ficha), "fora_do_padrao": sum(1 for e in fora if e.get("ficha"))},
                 "cursos": cursos}
    if sem_ficha:
        resultado["sem_ficha"] = sem_ficha
    if any(e.get("ficha") for e in fora):
        resultado["fora_do_padrao"] = [{"pacote": e["caminho"], "ficha": e["ficha"]} for e in fora if e.get("ficha")]
    return resultado
