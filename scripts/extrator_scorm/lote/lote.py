"""MVP1.1, Fase D: o lote. Varre a pasta de cursos, compara com a execução anterior, extrai só o que precisa e grava o resumo.

Só lê a pasta de cursos. Grava na raiz do extrator `fichas/<caminho do pacote>.json`, `controle.json` e `resumo.json`; e `Cursos/registro-de-cursos.json`.
"""
import argparse
import json
import sys
from pathlib import Path

from .. import servico
from ..erros import ErroExtracao
from ..path import caminhos
from . import autores, controle, resumo, varredura

PASTA_FICHAS = "fichas"
NOME_RESUMO = "resumo.json"
NOME_ULTIMAS = "registro-de-cursos.json"


def caminho_da_ficha(pasta_saida, caminho_do_pacote):
    """A ficha de cada pacote mora no mesmo caminho do pacote, dentro de fichas/: nunca colide."""
    return Path(pasta_saida) / PASTA_FICHAS / (caminho_do_pacote + ".json")


def _gravar_json(destino, dados):
    """Grava `dados` como JSON legível em `destino`, criando as pastas. Erro claro se não der para gravar."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    try:
        destino.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    except OSError as e:
        raise ErroExtracao(f"Não consegui gravar {destino}: {e}")


def _ler_ficha(destino):
    """Lê uma ficha já gravada; devolve None se não existe ou está estragada."""
    try:
        return json.loads(destino.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def executar(pasta, pasta_saida=None, ignorar=varredura.IGNORAR_PADRAO, forcar=False, progresso=None, cancelar=None, agora=controle.agora,
             so_ultimas=False, pasta_registro=None):
    """Roda o lote e devolve o relatório (um dict). `progresso(texto, atual, total)` e `cancelar()` são opcionais.

    Um pacote com erro vira linha do relatório e não interrompe os demais. Se `cancelar()` devolver True, o lote para entre
    dois pacotes e NÃO grava o controle nem o resumo (as fichas já gravadas ficam).

    `so_ultimas`: só lê (extrai) os pacotes da maior `vN` de cada curso. A lista de controle e o resumo continuam completos: as versões
    antigas entram com a ficha que já existir (ou `nao_lida`). A leitura dos bytes (sha256) vale para todos.
    """
    raiz = Path(pasta)
    saida = Path(pasta_saida) if pasta_saida else servico.PASTA_SAIDA
    progresso = progresso or (lambda *_: None)
    cancelar = cancelar or (lambda: False)
    achados = varredura.varrer(raiz, ignorar)
    pacotes, erros, avisos = achados["pacotes"], {}, []
    if not pacotes:                                              # pasta errada ou vazia: não apaga o controle da execução anterior
        return {**_interrompido(raiz, saida, achados), "interrompido": False, "sem_pacotes": True}

    for i, p in enumerate(pacotes, 1):
        if cancelar():
            return _interrompido(raiz, saida, achados)
        progresso("Lendo", i, len(pacotes), p["caminho"])
        try:
            p["sha256"] = controle.calcular_sha256(raiz, p)
        except ErroExtracao as e:
            p["sha256"], erros[p["caminho"]] = None, str(e)
    anterior = controle.carregar(saida)
    entradas, sumidos = controle.classificar(pacotes, anterior)
    schema_mudou = bool(anterior) and anterior.get("schema_da_ficha") != servico.SCHEMA

    escopo = varredura.so_as_ultimas(pacotes) if so_ultimas else None
    if escopo is not None:                                       # uma cópia na seleção precisa da ficha do principal, onde ele estiver
        escopo |= {e["copia_de"] for e in entradas if e["caminho"] in escopo and e["copia_de"]}
    aextrair = [e for e in entradas if e["caminho"] not in erros and e["status"] != controle.COPIA
                and (escopo is None or e["caminho"] in escopo)
                and (forcar or schema_mudou or e["status"] in (controle.NOVO, controle.ALTERADO)
                     or not caminho_da_ficha(saida, e["caminho"]).exists())]
    marcados = {e["caminho"] for e in aextrair}
    for i, e in enumerate(aextrair, 1):
        if cancelar():
            return _interrompido(raiz, saida, achados)
        progresso("Extraindo", i, len(aextrair), e["caminho"])
        try:
            ficha = servico.extrair(raiz / e["caminho"])
            _gravar_json(caminho_da_ficha(saida, e["caminho"]), ficha)
            avisos += [{"caminho": e["caminho"], **a} for a in ficha["avisos"]]
        except ErroExtracao as ex:
            erros[e["caminho"]] = str(ex)
        except Exception as ex:                                  # um pacote estranho não derruba o lote
            erros[e["caminho"]] = f"erro inesperado ({type(ex).__name__}): {ex}"

    por_caminho = {e["caminho"]: e for e in entradas}
    registros = []
    for e in entradas:
        dono = por_caminho.get(e["copia_de"], e)                 # a cópia usa a ficha do principal
        ficha = None if e["caminho"] in erros else _ler_ficha(caminho_da_ficha(saida, dono["caminho"]))
        if ficha is None and e["caminho"] not in erros and dono["caminho"] in erros:
            erros[e["caminho"]] = f"a ficha do principal ({dono['caminho']}) não existe porque ele deu erro"
        registros.append({**e, "ficha": ficha, **({"erro": erros[e["caminho"]]} if e["caminho"] in erros else {})})

    gerado_em = agora()
    destino_resumo = saida / NOME_RESUMO
    autoria = autores.Autoria(raiz, autores.dono_dos_arquivos_no_git(raiz))
    dados_do_resumo = resumo.montar(registros, gerado_em, len(achados["nao_scorm"]), autoria)
    _gravar_json(destino_resumo, dados_do_resumo)
    destino_ultimas = Path(pasta_registro) if pasta_registro else (saida / NOME_ULTIMAS if pasta_saida else caminhos.REGISTRO)
    dados_das_ultimas = resumo.montar_ultimas(registros, gerado_em, autoria)
    _gravar_json(destino_ultimas, dados_das_ultimas)
    # fichas de versões antigas que não foram refeitas continuam no formato velho: o controle não pode dizer que já estão no novo
    schema_da_ficha = anterior["schema_da_ficha"] if schema_mudou and escopo is not None else servico.SCHEMA
    campos = ("caminho", "tipo", "tamanho", "sha256", "empresa", "curso", "versao", "copia", "status", "copia_de")
    destino_controle = controle.gravar(saida, {
        "schema": controle.SCHEMA_DO_CONTROLE, "schema_da_ficha": schema_da_ficha, "gerado_em": gerado_em, "pasta": str(raiz.resolve()),
        "pacotes": [{**{c: r.get(c) for c in campos}, **({"erro": r["erro"]} if r.get("erro") else {})} for r in registros],
        "sumidos": sumidos})

    com_erro = [r for r in registros if r.get("erro")]
    extraidos = [r for r in registros if r["caminho"] in marcados and not r.get("erro")]
    copiados = [r for r in registros if r["status"] == controle.COPIA and not r.get("erro")]
    fora = [r for r in registros if escopo is not None and r["caminho"] not in escopo and r["status"] != controle.COPIA and not r.get("erro")]
    caminhos_fora = {r["caminho"] for r in fora}
    pulados = [r for r in registros if r["caminho"] not in marcados and r["status"] != controle.COPIA and not r.get("erro")
               and r["caminho"] not in caminhos_fora]
    return {
        "pasta": str(raiz), "interrompido": False, "forcado": forcar, "so_ultimas": so_ultimas,
        "encontrados": len(registros), "extraidos": len(extraidos), "copiados": len(copiados), "pulados": len(pulados),
        "fora_da_selecao": len(fora), "com_erro": len(com_erro), "nao_scorm": len(achados["nao_scorm"]),
        "novos": [r["caminho"] for r in registros if r["status"] == controle.NOVO],
        "alterados": [r["caminho"] for r in registros if r["status"] == controle.ALTERADO],
        "sumidos": [s["caminho"] for s in sumidos],
        "erros": [{"caminho": r["caminho"], "mensagem": r["erro"]} for r in com_erro],
        "pacotes": [{"caminho": r["caminho"], "tipo": r["tipo"], "empresa": r["empresa"], "curso": r["curso"], "versao": r["versao"],
                     "status": r["status"], "resultado": _resultado(r, marcados, escopo)} for r in registros],
        "avisos": avisos, "avisos_da_varredura": achados["avisos"], "nao_scorm_lista": achados["nao_scorm"],
        "arquivos": {"controle": str(destino_controle), "resumo": str(destino_resumo), "ultimas": str(destino_ultimas),
                     "fichas": str(saida / PASTA_FICHAS)},
        "ultimas_sem_ficha": dados_das_ultimas.get("sem_ficha", []),
        "autores": _relatorio_de_autores(dados_do_resumo, autoria),
        "totais": {k: v for k, v in dados_do_resumo["totais"].items() if k in ("cursos", "versoes")},
        "duplicados": dados_do_resumo["duplicados"],
    }


def _relatorio_de_autores(dados_do_resumo, autoria):
    """Quantos autores foram definidos e por quê, o que ficou sem autor e o que falta nas pastas (`autor.json`)."""
    versoes = [(f"{c['empresa']}/{c['curso']}", v) for c in dados_do_resumo["cursos"] for v in c["versoes"]]
    return {"versoes": len(versoes),
            "pelo_arquivo": sum(1 for _, v in versoes if v["autor_origem"] == autores.NOME_DO_ARQUIVO),
            "pelo_rise": sum(1 for _, v in versoes if v["autor_origem"] == "rise"),
            "sem_autor": [f"{curso}/{v['versao']}" for curso, v in versoes if not v["autor"]],
            "sem_arquivo": sorted(autoria.sem_arquivo), "problemas": autoria.problemas}


def _resultado(registro, marcados, escopo=None):
    """O que aconteceu com um pacote neste lote: erro, copiado, fora da seleção, extraído ou pulado."""
    if registro.get("erro"):
        return "erro"
    if registro["status"] == controle.COPIA:
        return "copiado"
    if registro["caminho"] in marcados:
        return "extraido"
    return "fora" if escopo is not None and registro["caminho"] not in escopo else "pulado"


def _interrompido(raiz, saida, achados):
    """Relatório de um lote interrompido (nada foi gravado no controle nem no resumo)."""
    return {"pasta": str(raiz), "interrompido": True, "encontrados": len(achados["pacotes"]), "extraidos": 0, "copiados": 0, "pulados": 0,
            "com_erro": 0, "fora_da_selecao": 0, "so_ultimas": False, "duplicados": {"grupos": [], "nao_comparados": []},
            "pacotes": [], "novos": [], "alterados": [], "sumidos": [], "erros": [], "avisos": [], "avisos_da_varredura": [],
            "nao_scorm": len(achados["nao_scorm"]), "nao_scorm_lista": achados["nao_scorm"], "forcado": False,
            "arquivos": {}, "totais": {}, "ultimas_sem_ficha": [], "autores": None}


def texto_do_relatorio(r):
    """O relatório em linhas de texto (a linha de comando e a tela mostram o mesmo)."""
    if r.get("sem_pacotes"):
        return [f"Nenhum pacote SCORM em {r['pasta']}. Nada foi gravado (nem o controle, nem o resumo): confira se é a pasta certa."] \
            + [f"  não SCORM: {x['caminho']} ({x['motivo']})" for x in r["nao_scorm_lista"]]
    if r["interrompido"]:
        return ["Interrompido. O controle e o resumo NÃO foram gravados (as fichas já feitas ficam em extrator_scorm/fichas/)."]
    linhas = [f"{r['encontrados']} pacotes SCORM em {r['pasta']}"
              f" ({r['totais'].get('cursos', 0)} cursos, {r['totais'].get('versoes', 0)} versões)"
              f"{'; extração forçada' if r['forcado'] else ''}{'; só as últimas versões' if r.get('so_ultimas') else ''}.",
              f"  extraídos: {r['extraidos']} · cópias idênticas: {r['copiados']} · sem mudança: {r['pulados']} · com erro: {r['com_erro']}"
              f"{' · versões antigas, fora da seleção: ' + str(r['fora_da_selecao']) if r.get('so_ultimas') else ''}"
              f" · zips que não são SCORM: {r['nao_scorm']}",
              f"  novos: {len(r['novos'])} · alterados: {len(r['alterados'])} · sumidos: {len(r['sumidos'])}"]
    linhas += _linhas_dos_duplicados(r["duplicados"]) + _linhas_dos_autores(r["autores"])
    linhas += [f"  sumiu: {c}" for c in r["sumidos"]]
    linhas += [f"  ERRO {e['caminho']}: {e['mensagem']}" for e in r["erros"]]
    linhas += [f"  não SCORM: {x['caminho']} ({x['motivo']})" for x in r["nao_scorm_lista"]]
    linhas += [f"  aviso: {a['caminho']}: {a['mensagem']}" for a in r["avisos_da_varredura"]]
    linhas += [f"  última versão sem ficha: {u['empresa']}/{u['curso']}/{u['versao']}: {u['motivo']}" for u in r.get("ultimas_sem_ficha", [])]
    linhas += [f"Resumo estratégico: {r['arquivos']['resumo']}", f"Fichas das últimas versões, num JSON só: {r['arquivos']['ultimas']}",
               f"Lista de controle: {r['arquivos']['controle']}",
               f"Fichas: {r['arquivos']['fichas']}"]
    return linhas


MAXIMO_DE_DUPLICADOS_NO_TEXTO = 15
ROTULO_DO_GRUPO = {"pasta_e_zip": "pasta e zip", "so_zips": "zips", "so_pastas": "pastas"}


def _linhas_dos_duplicados(d):
    """Linhas de texto sobre conteúdo repetido (mesma versão em pasta e zip, etc.) para o relatório."""
    grupos = d["grupos"]
    if not grupos:
        return ["  conteúdo repetido (pasta × zip): nenhum"]
    pasta_e_zip = sum(1 for g in grupos if g["tipos"] == "pasta_e_zip")
    linhas = [f"  conteúdo repetido: {len(grupos)} grupo(s), {pasta_e_zip} com pasta e zip (a lista completa está no resumo.json)"]
    for g in grupos[:MAXIMO_DE_DUPLICADOS_NO_TEXTO]:
        onde = "mesma versão" if g["mesma_versao"] else "versões diferentes"
        linhas.append(f"    {ROTULO_DO_GRUPO[g['tipos']]}, {onde}: " + " = ".join(p["caminho"] for p in g["pacotes"]))
    if len(grupos) > MAXIMO_DE_DUPLICADOS_NO_TEXTO:
        linhas.append(f"    ... e mais {len(grupos) - MAXIMO_DE_DUPLICADOS_NO_TEXTO}")
    return linhas


def _linhas_dos_autores(a):
    """Linhas de texto sobre os autores das versões (declarados, do Rise, sem autor) para o relatório."""
    linhas = [f"  autores: {a['versoes']} versões: {a['pelo_arquivo']} declaradas em {autores.NOME_DO_ARQUIVO}, {a['pelo_rise']} pelo Rise, "
              f"{len(a['sem_autor'])} sem autor"]
    if a["sem_autor"]:
        linhas.append("    sem autor: " + ", ".join(a["sem_autor"][:MAXIMO_DE_DUPLICADOS_NO_TEXTO])
                      + (f" ... e mais {len(a['sem_autor']) - MAXIMO_DE_DUPLICADOS_NO_TEXTO}" if len(a["sem_autor"]) > MAXIMO_DE_DUPLICADOS_NO_TEXTO else ""))
    if a["sem_arquivo"]:
        linhas.append(f"    {len(a['sem_arquivo'])} versões ainda não têm o {autores.NOME_DO_ARQUIVO} (para criá-los vazios: "
                      "uv run python -m extrator_scorm.lote.autores --criar Cursos)")
    linhas += [f"    PROBLEMA em {x['versao']}: {x['mensagem']}" for x in a["problemas"]]
    return linhas


def codigo_de_saida(r):
    """Diferente de zero só se nenhum pacote pôde ser processado (inclusive se não havia nenhum)."""
    return 1 if r["extraidos"] + r["copiados"] + r["pulados"] == 0 and not r.get("interrompido") else 0


def main(argv=None, saida=print):
    """Linha de comando do lote: `python -m extrator_scorm PASTA [--forcar] [--so-ultimas] [--ignorar CAMINHO]`."""
    p = argparse.ArgumentParser(prog="extrair_lote.py", description="Lê todos os pacotes SCORM de uma pasta de cursos (só lê a pasta) "
                                "e grava as fichas, a lista de controle e o resumo estratégico na raiz do extrator, e o registro dos cursos em Cursos/.")
    p.add_argument("pasta", help="pasta de cursos (por exemplo Cursos)")
    p.add_argument("--forcar", action="store_true", help="extrair tudo de novo, ignorando a lista de controle")
    p.add_argument("--ignorar", action="append", default=[], metavar="CAMINHO", help="caminho relativo a ignorar, além do laboratório")
    p.add_argument("--so-ultimas", action="store_true", help="extrair só a última versão (maior vN) de cada curso; o resumo continua completo")
    args = p.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        r = executar(args.pasta, ignorar=varredura.IGNORAR_PADRAO + tuple(args.ignorar), forcar=args.forcar, so_ultimas=args.so_ultimas)
    except ErroExtracao as e:
        saida(f"Erro: {e}")
        return 1
    for linha in texto_do_relatorio(r):
        saida(linha)
    return codigo_de_saida(r)


if __name__ == "__main__":
    sys.exit(main())
