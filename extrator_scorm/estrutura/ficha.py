"""A ficha do curso: só as informações úteis, sem o conteúdo (D01-2, D01-3, D01-5).

O que mais existe dentro do SCORM, e onde, está anotado em disponiveis.py.
"""
import html
import re
from collections import Counter

PALAVRAS_POR_MINUTO = 200                       # estimativa de leitura; não conta o tempo das interações
# Textos que NÃO são lidos pelo aluno como texto de bloco: ids, configuração, mídia e código HTML customizado.
CHAVES_FORA_DA_CONTAGEM = frozenset({"id", "type", "family", "variant", "globalBlockId", "media", "srcdoc", "settings", "metadata"})
FAMILIAS_INTERATIVAS = ("interactive", "flashcard")       # interactive, interactive-fullscreen e flashcard
IDIOMA_ESPERADO = "pt"


def texto_limpo(valor):
    """HTML do editor -> texto simples, com espaços normalizados."""
    if not isinstance(valor, str):
        return None
    sem_marcas = re.sub(r"<[^>]+>", " ", valor)
    return " ".join(html.unescape(sem_marcas).split())


def _textos(x):
    if isinstance(x, dict):
        for k, v in x.items():
            if k not in CHAVES_FORA_DA_CONTAGEM:
                yield from _textos(v)
    elif isinstance(x, list):
        for i in x:
            yield from _textos(i)
    elif isinstance(x, str):
        yield x


def contar_palavras(itens):
    return len(texto_limpo(" ".join(_textos(itens))).split())


def _rotulo(bloco):
    familia, variante = bloco.get("family"), bloco.get("variant")
    return f"{familia}/{variante}" if familia and variante else (familia or bloco.get("type") or "desconhecido")


def _capitulo(numero, lic):
    itens = [b for b in lic.get("items") or [] if isinstance(b, dict)]
    quiz = lic.get("type") == "quiz"
    cap = {
        "numero": numero,
        "titulo": lic.get("title"),
        "descricao": texto_limpo(lic.get("description")) or None,
        "tipo": lic.get("type"),
        "apagado": bool(lic.get("deleted")),
        "criado": lic.get("createdAt"),
        "atualizado": lic.get("updatedAt"),
        "blocos": len(itens),
        "palavras": contar_palavras(itens),
    }
    if quiz:
        cfg = lic.get("settings") or {}
        cap.update({
            "nota_minima": cfg.get("passingScore"),
            "tentativas": cfg.get("retryCount"),                  # -1 = ilimitadas
            "questoes": dict(sorted(Counter(b.get("type") for b in itens).items(), key=lambda kv: str(kv[0]))),
        })
    else:
        familias = [b.get("family") or "" for b in itens]
        cap.update({
            "interativos": sum(1 for f in familias if f.startswith(FAMILIAS_INTERATIVAS)),
            "verificacoes_de_conhecimento": sum(1 for f in familias if f == "knowledgeCheck"),
            "html_customizado": sum(1 for f in familias if f == "html"),
            "tipos_de_bloco": dict(sorted(Counter(_rotulo(b) for b in itens).items())),
        })
    return cap


def _alertas(curso, capitulos, idioma, manifesto):
    alertas = []
    conteudo = [c for c in capitulos if c["tipo"] != "quiz"]
    if idioma and not idioma.lower().startswith(IDIOMA_ESPERADO):
        alertas.append({"codigo": "interface_em_outro_idioma",
                        "mensagem": f"Os botões e avisos do player estão em '{idioma}', não em português."})
    sem_descricao = [c["numero"] for c in conteudo if not c["descricao"]]
    if sem_descricao:
        alertas.append({"codigo": "capitulos_sem_descricao", "capitulos": sem_descricao,
                        "mensagem": f"{len(sem_descricao)} de {len(conteudo)} capítulo(s) de conteúdo sem descrição."})
    com_html = [c["numero"] for c in conteudo if c["html_customizado"]]
    if com_html:
        alertas.append({"codigo": "html_customizado", "capitulos": com_html,
                        "mensagem": f"{sum(c['html_customizado'] for c in conteudo)} bloco(s) de HTML customizado em {len(com_html)} capítulo(s)."})
    if not any(c["tipo"] == "quiz" for c in capitulos):
        alertas.append({"codigo": "sem_quiz", "mensagem": "O curso não tem capítulo de quiz."})
    apagados = [c["numero"] for c in capitulos if c["apagado"]]
    if apagados:
        alertas.append({"codigo": "capitulo_apagado", "capitulos": apagados, "mensagem": f"{len(apagados)} capítulo(s) marcado(s) como apagado(s)."})
    if manifesto:
        titulo_json, titulo_manifesto = curso.get("title"), manifesto.get("titulo")
        if titulo_json and titulo_manifesto and titulo_json.strip() != titulo_manifesto.strip():
            alertas.append({"codigo": "titulo_do_manifesto_diferente",
                            "mensagem": f"Título do curso '{titulo_json}' x título do manifesto '{titulo_manifesto}'."})
        if manifesto.get("declarados_ausentes_no_zip"):
            alertas.append({"codigo": "arquivos_declarados_ausentes",
                            "mensagem": f"{len(manifesto['declarados_ausentes_no_zip'])} arquivo(s) do manifesto não estão no zip."})
    return alertas


def montar(conteudo, manifesto, formato, arquivo_zip, zip_interno=None):
    """Monta a ficha. `conteudo` é o JSON do curso (ou None); campo ausente vira None, nunca erro."""
    conteudo = conteudo or {}
    curso = conteudo.get("course") or {}
    export = curso.get("exportSettings") or {}
    configuracoes = conteudo.get("settings") or {}
    lista = sorted((c for c in curso.get("lessons") or [] if isinstance(c, dict)),
                   key=lambda c: (c.get("position") is None, c.get("position") or 0))
    capitulos = [_capitulo(i, c) for i, c in enumerate(lista, 1)]
    idioma = (conteudo.get("labelSet") or {}).get("iso639Code")
    publicado, editado = curso.get("lastPublishedAt"), curso.get("contentUpdatedAt")
    palavras = sum(c["palavras"] for c in capitulos if c["tipo"] != "quiz")
    pacote = {**arquivo_zip, "scorm": None, "ferramenta": formato.get("ferramenta"), "variante_do_conteudo": formato.get("variante"),
              "versao_do_pacote": configuracoes.get("coursePackageVersion"),
              "impressao_do_curso": formato.get("impressao")}
    if zip_interno:
        pacote["zip_interno"] = zip_interno
    if manifesto:
        pacote["identificador_do_manifesto"] = manifesto.get("identificador")
        pacote["scorm"] = {"esquema": manifesto.get("esquema"), "versao": manifesto.get("versao_do_esquema")}
    return {
        "curso": {
            "id": curso.get("id"),
            "titulo": curso.get("title"),
            "descricao": texto_limpo(curso.get("description")) or None,
            "autores": [a.get("authorName") for a in curso.get("authors") or [] if isinstance(a, dict) and a.get("authorName")],
            "idioma_da_interface": idioma,               # idioma dos botões do player, NÃO do conteúdo
            "criado_por_ia": (curso.get("metadata") or {}).get("createdVia") == "ai" if curso else None,
            "criado": curso.get("createdAt"),
            "atualizado": curso.get("updatedAt"),
            "conteudo_atualizado": editado,
            "publicado": publicado,
            "publicado_depois_da_ultima_edicao": (publicado >= editado) if publicado and editado else None,
        },
        "capitulos": capitulos,
        "tamanho": {
            "capitulos": len(capitulos),
            "blocos": sum(c["blocos"] for c in capitulos if c["tipo"] != "quiz"),
            "palavras": palavras,
            "minutos_de_leitura_estimados": round(palavras / PALAVRAS_POR_MINUTO),
            "questoes_do_quiz": sum(c["blocos"] for c in capitulos if c["tipo"] == "quiz"),
        },
        "lms": {
            "padrao": export.get("targetName"),
            "reporte": export.get("reporting"),
            "conclusao": export.get("completeWith"),
            "porcentagem_de_conclusao": export.get("completionPercentage", configuracoes.get("completionPercentage")),
        },
        "pacote": pacote,
        "alertas": _alertas(curso, capitulos, idioma, manifesto) if curso else [],
    }
