"""Linha de comando. Sem argumentos, abre a tela (modo pasta); com um pacote (.zip ou pasta SCORM), extrai um só; com uma pasta de cursos, roda o lote."""
import argparse
import sys
from pathlib import Path

from .. import servico
from ..erros import ErroExtracao
from ..leitura import inventario
from ..lote import lote


def _eh_pacote_em_pasta(caminho):
    return caminho.is_dir() and any(f.name.lower() == inventario.MANIFESTO for f in caminho.iterdir())


def main(argv=None, saida=print):
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        from . import tela
        return tela.abrir()
    p = argparse.ArgumentParser(prog="python -m extrator_scorm", description="Extrai as informações de SCORM. Com um .zip (ou a pasta de um pacote), grava a ficha "
                                "dele em extrator_scorm/fichas/_individuais/. Com uma pasta de cursos, lê todos os pacotes (lote) e grava também o resumo estratégico. "
                                "Sem argumentos, abre a tela.")
    p.add_argument("caminho", help="um .zip de SCORM, a pasta de um pacote SCORM ou a pasta de cursos (lote)")
    p.add_argument("--forcar", action="store_true", help="só no lote: extrair tudo de novo, ignorando a lista de controle")
    p.add_argument("--ignorar", action="append", default=[], metavar="CAMINHO", help="só no lote: caminho relativo a ignorar, além do laboratório")
    p.add_argument("--so-ultimas", action="store_true", help="só no lote: extrair só a última versão (maior vN) de cada curso")
    args = p.parse_args(argv)
    if not args.caminho.strip():
        saida("Erro: o caminho está vazio.")
        return 1
    alvo = Path(args.caminho)
    if alvo.is_dir() and not _eh_pacote_em_pasta(alvo):
        return lote.main([str(alvo)] + (["--forcar"] if args.forcar else []) + (["--so-ultimas"] if args.so_ultimas else []) + [x for i in args.ignorar for x in ("--ignorar", i)], saida=saida)
    try:
        resultado = servico.extrair(alvo)
        destino = servico.gravar(resultado, alvo)
    except ErroExtracao as e:
        saida(f"Erro: {e}")
        return 1
    for a in resultado["avisos"]:
        saida(f"Aviso ({a['fase']}): {a['mensagem']}")
    saida(str(destino))
    return 0
