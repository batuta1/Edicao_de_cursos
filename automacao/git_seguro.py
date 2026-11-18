"""Git só para o que a automação precisa: ler de outra branch e commitar SOMENTE os caminhos do processo. Nunca faz push."""
import subprocess
from pathlib import Path

from . import caminhos


class ErroGit(RuntimeError):
    pass


def git(*args, binario=False):
    r = subprocess.run(["git", "-c", "core.quotepath=false", *args], cwd=str(caminhos.RAIZ), capture_output=True)
    if r.returncode != 0:
        raise ErroGit(f"git {' '.join(args)}: {r.stderr.decode('utf-8', 'replace').strip()}")
    return r.stdout if binario else r.stdout.decode("utf-8", "replace")


def relativo(caminho):
    return Path(caminho).resolve().relative_to(caminhos.RAIZ.resolve()).as_posix()


def validar_caminho(caminho):
    """Erro se o caminho (arquivo ou pasta) estiver fora da lista permitida ou dentro de bagunca/ ou Skills/."""
    try:
        rel = relativo(caminho)
    except ValueError:
        raise ErroGit(f"caminho fora do repositório: {caminho}")
    if any(rel == p.rstrip("/") or rel.startswith(p) for p in caminhos.PROIBIDOS):
        raise ErroGit(f"a automação não mexe em {rel}")
    if not any(rel == p.rstrip("/") or rel.startswith(p) for p in caminhos.PERMITIDOS):
        raise ErroGit(f"caminho fora da lista permitida: {rel}")
    return rel


def commitar_somente(caminhos_, mensagem):
    """Commit só destes caminhos (arquivos ou pastas; inclui remoções). Devolve o hash curto, ou None se não havia mudança."""
    rels = [validar_caminho(c) for c in caminhos_]
    git("add", "-A", "--", *rels)
    if not git("diff", "--cached", "--name-only", "--", *rels).strip():
        return None
    git("commit", "-m", mensagem, "--", *rels)
    return git("rev-parse", "--short", "HEAD").strip()
