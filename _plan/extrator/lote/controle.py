"""MVP1.1, Fase C: a lista de controle. Guarda o que foi achado a cada execução e compara com a anterior.

Status de cada pacote nesta execução:
  novo           o caminho não estava na execução anterior
  alterado       o caminho já existia, mas o sha256 mudou
  sem_mudanca    o caminho e o sha256 são os mesmos
  copia_identica outro pacote desta execução tem o mesmo sha256 (o principal é o que não está em `copias/`, depois o que
                 já estava na execução anterior, depois o de caminho menor); a cópia não é extraída de novo
Um pacote que existia e não existe mais vai para `sumidos`.
"""
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path

from ..erros import ErroExtracao
from ..leitura import fonte, inventario

SCHEMA_DO_CONTROLE = 1
NOME = "controle.json"
NOME_ANTERIOR = "controle.anterior.json"
NOVO, ALTERADO, SEM_MUDANCA, COPIA = "novo", "alterado", "sem_mudanca", "copia_identica"


def calcular_sha256(raiz, pacote):
    """sha256 do arquivo (zip) ou do conteúdo da pasta, arquivo por arquivo. Levanta ErroExtracao se não der para ler."""
    caminho = Path(raiz) / pacote["caminho"]
    try:
        if pacote["tipo"] == "zip":
            return inventario.sha256_arquivo(caminho)
        with fonte.FontePasta(caminho) as f:
            return fonte.impressao_do_conteudo(f)
    except OSError as e:
        raise ErroExtracao(f"Não consegui ler {caminho}: {e}")


def agora():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def classificar(pacotes, anterior=None):
    """`pacotes`: lista da varredura, cada um já com `sha256` (ou `sha256` None se não deu para ler).

    Devolve (pacotes com `status` e `copia_de`, sumidos). Não altera a lista de entrada.
    """
    antes = {p["caminho"]: p for p in (anterior or {}).get("pacotes", [])}
    principais = {}
    conhecido = lambda p: antes.get(p["caminho"], {}).get("sha256") == p.get("sha256")      # noqa: E731 (já estava lá, com este conteúdo)
    for p in sorted(pacotes, key=lambda p: (bool(p.get("copia")), not conhecido(p), p["caminho"])):
        if p.get("sha256"):
            principais.setdefault(p["sha256"], p["caminho"])
    resultado = []
    for p in sorted(pacotes, key=lambda p: p["caminho"]):
        novo = {**p, "copia_de": None}
        principal = principais.get(p.get("sha256"))
        if principal and principal != p["caminho"]:
            novo["status"], novo["copia_de"] = COPIA, principal
        elif p["caminho"] not in antes:
            novo["status"] = NOVO
        elif antes[p["caminho"]].get("sha256") != p.get("sha256"):
            novo["status"] = ALTERADO
        else:
            novo["status"] = SEM_MUDANCA
        resultado.append(novo)
    atuais = {p["caminho"] for p in pacotes}
    sumidos = [{k: v for k, v in p.items() if k in ("caminho", "tipo", "sha256", "empresa", "curso", "versao")}
               for c, p in sorted(antes.items()) if c not in atuais]
    return resultado, sumidos


def carregar(pasta_saida):
    """O controle da execução anterior, ou None se não houver (ou se estiver ilegível)."""
    caminho = Path(pasta_saida) / NOME
    try:
        dados = json.loads(caminho.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return dados if isinstance(dados, dict) and isinstance(dados.get("pacotes"), list) else None


def gravar(pasta_saida, controle):
    """Guarda o controle atual como `controle.anterior.json` e grava o novo, trocando o arquivo de uma vez."""
    pasta = Path(pasta_saida)
    pasta.mkdir(parents=True, exist_ok=True)
    destino, anterior = pasta / NOME, pasta / NOME_ANTERIOR
    temporario = pasta / (NOME + ".tmp")
    try:
        temporario.write_text(json.dumps(controle, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        if destino.exists():
            shutil.copyfile(destino, anterior)
        os.replace(temporario, destino)
    except OSError as e:
        raise ErroExtracao(f"Não consegui gravar o controle em {destino}: {e}")
    return destino
