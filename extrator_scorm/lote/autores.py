"""MVP1.1, Fase H: o autor de cada versão de curso. Um nome por versão (D04-10).

**Onde se declara:** em `Edicao_de_cursos`, junto de cada versão, num arquivo `autor.json`:
    Cursos/<Empresa>/<curso>/scorm/vN/autor.json      {"autor": "Nome da pessoa"}     (ou {"autor": null} enquanto não se sabe)
Quem escreve o arquivo é uma pessoa; o extrator só lê (a única exceção é `--criar`, que cria os arquivos vazios que faltam).

Quem vale, em ordem:
  1. o `autor.json` da versão (origem «autor.json»);
  2. o autor do Rise (`curso.autores` da ficha), mas só quando é uma pessoa: a conta compartilhada «Iaclube Help» não conta (origem «rise»);
  3. nada (`null`): o relatório lista as versões sem autor.
O autor do commit no git entra só como **sugestão** (`autor_sugerido.git`): ele diz quem subiu o arquivo, não quem criou o curso.
"""
import argparse
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

from ..erros import ErroExtracao
from . import varredura

NOME_DO_ARQUIVO = "autor.json"
CONTAS_COMPARTILHADAS = ("Iaclube Help",)


def pasta_da_versao(raiz, empresa, curso, versao):
    return Path(raiz) / empresa / curso / "scorm" / versao


def ler_declaracao(pasta):
    """(autor, existe, problema) do `autor.json` de uma pasta de versão. Arquivo estragado não derruba nada: vira `problema`."""
    arquivo = Path(pasta) / NOME_DO_ARQUIVO
    if not arquivo.is_file():
        return None, False, None
    try:
        dados = json.loads(arquivo.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return None, True, f"não consegui ler: {e}"
    if not isinstance(dados, dict) or "autor" not in dados:
        return None, True, 'o arquivo precisa ser {"autor": "Nome"} (ou {"autor": null})'
    autor = dados["autor"]
    if autor is None:
        return None, True, None
    if isinstance(autor, str) and autor.strip():
        return autor.strip(), True, None
    return None, True, "«autor» precisa ser um nome (texto) ou null"


def dono_dos_arquivos_no_git(pasta):
    """{caminho relativo a `pasta`: autor do commit que criou o arquivo}, seguindo as renomeações. Vazio se não for um repositório git.

    O histórico é lido do repositório inteiro (e não só da `pasta`): uma pasta de cursos reorganizada tem arquivos que vieram de fora dela.
    """
    git = ["git", "-c", "core.quotepath=false", "-C", str(pasta)]
    try:
        prefixo = subprocess.run(git + ["rev-parse", "--show-prefix"], capture_output=True, text=True, timeout=30, check=True).stdout.strip()
        r = subprocess.run(git + ["log", "--reverse", "--no-merges", "-M", "--name-status", "--diff-filter=ARD", "--format=@%an"],
                           capture_output=True, text=True, timeout=120, check=True)
    except (OSError, subprocess.SubprocessError):
        return {}
    dono, atual = {}, None
    for linha in r.stdout.splitlines():
        if linha.startswith("@"):
            atual = linha[1:]
            continue
        partes = linha.split("\t")
        if partes[0][:1] == "A" and len(partes) >= 2:
            dono[partes[1]] = atual
        elif partes[0][:1] == "R" and len(partes) >= 3:
            dono[partes[2]] = dono.pop(partes[1], atual)
        elif partes[0][:1] == "D" and len(partes) >= 2:
            dono.pop(partes[1], None)
    return {c[len(prefixo):]: a for c, a in dono.items() if c.startswith(prefixo)}


def autor_no_git(dono, caminho_do_pacote):
    """O autor do commit de um pacote: do próprio arquivo (zip) ou o mais comum entre os arquivos da pasta."""
    if caminho_do_pacote in dono:
        return dono[caminho_do_pacote]
    nomes = [a for c, a in dono.items() if c.startswith(caminho_do_pacote + "/")]
    return Counter(nomes).most_common(1)[0][0] if nomes else None


def decidir(declarado, nomes_do_rise, do_git):
    """(autor, origem, sugerido). A origem é «autor.json», «rise» ou None."""
    pessoas = [n for n in nomes_do_rise if n not in CONTAS_COMPARTILHADAS]
    sugerido = {"rise": list(nomes_do_rise), "git": do_git}
    if declarado:
        return declarado, NOME_DO_ARQUIVO, sugerido
    if len(pessoas) == 1:
        return pessoas[0], "rise", sugerido
    return None, None, sugerido


class Autoria:
    """O que o resumo chama para saber o autor de uma versão: `autoria(entradas_da_versao, pacote_principal_ou_None)`.

    Guarda o que viu: `sem_arquivo` (versões sem `autor.json`) e `problemas` (`autor.json` estragado), para o relatório.
    """

    def __init__(self, raiz, dono_no_git):
        self.raiz, self.dono_no_git = Path(raiz), dono_no_git
        self.sem_arquivo, self.problemas, self._feitos = [], [], {}

    def __call__(self, entradas, principal):
        e = entradas[0]
        chave = (e["empresa"], e["curso"], e["versao"])
        if chave not in self._feitos:
            pasta = pasta_da_versao(self.raiz, *chave)
            declarado, existe, problema = ler_declaracao(pasta)
            nome = "/".join(chave)
            if not existe:
                self.sem_arquivo.append(nome)
            if problema:
                self.problemas.append({"versao": nome, "mensagem": f"{NOME_DO_ARQUIVO}: {problema}"})
            self._feitos[chave] = declarado
        nomes = ((principal or {}).get("ficha") or {}).get("curso", {}).get("autores") or []
        git = autor_no_git(self.dono_no_git, (principal or sorted(entradas, key=lambda x: x["caminho"])[0])["caminho"])
        autor, origem, sugerido = decidir(self._feitos[chave], nomes, git)
        return {"autor": autor, "autor_origem": origem, "autor_sugerido": sugerido}


def criar_vazios(pasta, ignorar=varredura.IGNORAR_PADRAO):
    """Cria `autor.json` com {"autor": null} em cada pasta de versão que ainda não tem um. Nunca sobrescreve. Devolve os caminhos criados."""
    achados = varredura.varrer(pasta, ignorar)
    versoes = sorted({(p["empresa"], p["curso"], p["versao"]) for p in achados["pacotes"] if p["versao"]})
    criados = []
    for chave in versoes:
        destino = pasta_da_versao(pasta, *chave) / NOME_DO_ARQUIVO
        if destino.exists():
            continue
        try:
            destino.write_text('{\n  "autor": null\n}\n', encoding="utf-8", newline="\n")
        except OSError as e:
            raise ErroExtracao(f"Não consegui criar {destino}: {e}")
        criados.append(destino)
    return criados


def main(argv=None, saida=print):
    p = argparse.ArgumentParser(prog="python -m extrator_scorm.lote.autores",
                                description=f"Cria o {NOME_DO_ARQUIVO} (com autor vazio) em cada versão de curso que ainda não tem um. Nunca sobrescreve.")
    p.add_argument("--criar", action="store_true", help="cria os arquivos que faltam (sem isso, só mostra quantos faltam)")
    p.add_argument("pasta", help="pasta de cursos (por exemplo Cursos)")
    args = p.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        if args.criar:
            criados = criar_vazios(args.pasta)
            saida(f"{len(criados)} arquivo(s) {NOME_DO_ARQUIVO} criado(s) em {args.pasta}; os que já existiam não foram tocados.")
            return 0
        achados = varredura.varrer(args.pasta)
        versoes = {(p["empresa"], p["curso"], p["versao"]) for p in achados["pacotes"] if p["versao"]}
        faltam = [v for v in versoes if not (pasta_da_versao(args.pasta, *v) / NOME_DO_ARQUIVO).exists()]
        saida(f"{len(faltam)} de {len(versoes)} versões ainda sem {NOME_DO_ARQUIVO}. Use --criar para criá-los (vazios).")
        return 0
    except ErroExtracao as e:
        saida(f"Erro: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
