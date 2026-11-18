"""Fase C: reconhecer o formato e achar o JSON do curso (codificado em base64)."""
import base64
import hashlib
import json
import posixpath
import re

# As duas variantes que a biblioteca tem (D01-1): o conteúdo fora do HTML ou dentro dele.
VARIANTES = (
    ("runtime-data.js", "scormcontent/runtime-data.js", re.compile(r'__jsonp\(\s*"runtime-data\.js"\s*,\s*"([A-Za-z0-9+/=]+)"')),
    ("index.html", "scormcontent/index.html", re.compile(r'deserialize\(\s*"([A-Za-z0-9+/=]+)"')),
)


def impressao_do_curso(base64_texto):
    """10 primeiros caracteres do sha256 do conteúdo codificado: o mesmo valor, em pacotes diferentes, é a mesma versão do curso."""
    return hashlib.sha256(base64_texto.encode("ascii")).hexdigest()[:10]


def decodificar(base64_texto):
    """base64 -> bytes -> UTF-8 (utf-8-sig tira o BOM) -> JSON."""
    return json.loads(base64.b64decode(base64_texto).decode("utf-8-sig"))


# Reserva (D01-1, cuidado com variantes novas): qualquer .js/.html de scormcontent/ com um base64 grande
# que decodifique para o JSON de um curso Rise (course.lessons).
GENERICO = re.compile(r'"([A-Za-z0-9+/=]{2000,})"')
LIMITE_ARQUIVO = 100 * 1024 * 1024


def _procurar_em_outros_arquivos(z, prefixo, nomes, conhecidos, avisos):
    """Plano B: procura o JSON do curso em qualquer `.js` ou `.html` de `scormcontent/` e avisa que o formato era desconhecido."""
    for nome in sorted(nomes):
        if nome in conhecidos or not nome.startswith(prefixo + "scormcontent/") or not nome.lower().endswith((".js", ".html", ".htm")):
            continue
        if z.tamanho(nome) > LIMITE_ARQUIVO:
            continue
        texto = z.ler(nome).decode("utf-8", errors="replace")
        for achado in GENERICO.finditer(texto):
            try:
                conteudo = decodificar(achado.group(1))
            except (ValueError, UnicodeDecodeError):
                continue
            if isinstance(conteudo, dict) and isinstance((conteudo.get("course") or {}).get("lessons"), list):
                avisos.append({"fase": "formato", "mensagem": f"O conteúdo estava num arquivo fora das duas variantes conhecidas: {nome}."})
                return {"variante": f"outro ({posixpath.basename(nome)})", "arquivo": nome, "tamanho_do_base64": len(achado.group(1)),
                        "impressao": impressao_do_curso(achado.group(1))}, conteudo
    return None, None


def reconhecer(z, prefixo, nomes, identificador_da_organizacao, avisos):
    """Devolve (descrição do formato, json do curso ou None). Formato desconhecido não é erro."""
    pistas, conteudo, usada = [], None, None
    conhecidos = {prefixo + c for _, c, _ in VARIANTES}
    for variante, caminho, padrao in VARIANTES:
        nome = prefixo + caminho
        if nome not in nomes:
            continue
        texto = z.ler(nome).decode("utf-8", errors="replace")
        achado = padrao.search(texto)
        if not achado:
            continue
        try:
            conteudo = decodificar(achado.group(1))
        except (ValueError, UnicodeDecodeError) as e:
            avisos.append({"fase": "formato", "mensagem": f"{nome}: não consegui decodificar o conteúdo: {e}"})
            continue
        usada = {"variante": variante, "arquivo": nome, "tamanho_do_base64": len(achado.group(1)),
                 "impressao": impressao_do_curso(achado.group(1))}
        break
    if usada is None:
        usada, conteudo = _procurar_em_outros_arquivos(z, prefixo, nomes, conhecidos, avisos)
    if identificador_da_organizacao == "articulate_rise":
        pistas.append("organização do manifesto é articulate_rise")
    if isinstance(conteudo, dict) and isinstance((conteudo.get("course") or {}).get("lessons"), list):
        pistas.append("o JSON tem course.lessons")
    ferramenta = "Articulate Rise 360" if pistas else "desconhecida"
    if usada is None:
        avisos.append({"fase": "formato", "mensagem": "Não achei o conteúdo codificado em nenhuma das duas variantes conhecidas "
                                                        "(scormcontent/runtime-data.js ou scormcontent/index.html)."})
    return {"ferramenta": ferramenta, "reconhecida_por": pistas, **(usada or {"variante": None})}, conteudo
