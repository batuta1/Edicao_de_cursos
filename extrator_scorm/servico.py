"""O trabalho de verdade, sem tela e sem linha de comando (a CLI e a tela só chamam isto)."""
import io
import json
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

from .erros import ErroExtracao
from .estrutura import ficha
from .leitura import fonte as fonte_, formato, inventario, manifesto
from .path import caminhos

SCHEMA = 2
PASTA_SAIDA = caminhos.PASTA_SAIDA
PASTA_INDIVIDUAIS = caminhos.INDIVIDUAIS


def _analisar(fonte, avisos):
    """Lê manifesto e conteúdo de uma fonte já aberta (zip, pasta, ou um zip de dentro de outro)."""
    nomes = fonte.nomes()
    caminho_manifesto, prefixo = inventario.achar_manifesto(nomes)
    dados_manifesto = None
    if caminho_manifesto is None:
        fundos = [n for n in nomes if n.lower().endswith("imsmanifest.xml")]
        if fundos:
            avisos.append({"fase": "manifesto", "mensagem": f"O pacote parece um contêiner: tem {len(fundos)} manifesto(s) em subpastas, "
                                                            "não na raiz. Passe um pacote de cada curso."})
        else:
            avisos.append({"fase": "manifesto", "mensagem": "Não achei o imsmanifest.xml na raiz do pacote nem numa pasta de topo."})
    else:
        try:
            dados_manifesto = manifesto.ler(fonte.ler(caminho_manifesto), nomes, prefixo)
        except ET.ParseError as e:
            avisos.append({"fase": "manifesto", "mensagem": f"Manifesto ilegível: {e}"})
    organizacao = dados_manifesto["organizacao"] if dados_manifesto else None
    descricao_formato, conteudo = formato.reconhecer(fonte, prefixo, set(nomes), organizacao, avisos)
    return conteudo, dados_manifesto, descricao_formato


def _dados_da_pasta(caminho, fonte):
    return {"nome": Path(caminho).name, "tamanho": sum(fonte.tamanho(n) for n in fonte.nomes()),
            "sha256": fonte_.impressao_do_conteudo(fonte)}


def extrair(caminho):
    """Lê um pacote SCORM (um .zip ou uma pasta) e devolve a ficha do curso. Nada é extraído no disco nem gravado aqui.

    "Duplo zip": se o zip não tem manifesto mas tem exatamente um .zip dentro, lê esse de dentro, em memória.
    Para uma pasta, `pacote.sha256` é o sha256 do conteúdo (arquivo por arquivo), já que não há um arquivo só.
    """
    avisos, zip_interno = [], None
    with fonte_.abrir(caminho) as fonte:
        if isinstance(fonte, fonte_.FontePasta):
            arquivo = _dados_da_pasta(caminho, fonte)
            conteudo, dados_manifesto, descricao_formato = _analisar(fonte, avisos)
        else:
            arquivo = inventario.dados_do_zip(caminho)
            nomes = fonte.nomes()
            internos = [n for n in nomes if n.lower().endswith(".zip")]
            if inventario.achar_manifesto(nomes)[0] is None and internos:
                if len(internos) == 1:
                    bruto = fonte.ler(internos[0])
                    zip_interno = inventario.dados_de_bytes(internos[0], bruto)
                    avisos.append({"fase": "zip", "mensagem": f"O zip tem outro zip dentro ({internos[0]}); li o de dentro."})
                    try:
                        with fonte_.FonteZip(zipfile.ZipFile(io.BytesIO(bruto))) as interno:
                            conteudo, dados_manifesto, descricao_formato = _analisar(interno, avisos)
                    except zipfile.BadZipFile:
                        raise ErroExtracao(f"O zip de dentro ({internos[0]}) está corrompido.")
                else:
                    avisos.append({"fase": "zip", "mensagem": f"O zip tem {len(internos)} zips dentro e nenhum manifesto na raiz; "
                                                              "extraia um de cada vez."})
                    conteudo, dados_manifesto, descricao_formato = _analisar(fonte, avisos)
            else:
                conteudo, dados_manifesto, descricao_formato = _analisar(fonte, avisos)
    resultado = {"schema": SCHEMA, **ficha.montar(conteudo, dados_manifesto, descricao_formato, arquivo, zip_interno)}
    resultado["avisos"] = avisos
    return resultado


def para_texto(resultado):
    return json.dumps(resultado, ensure_ascii=False, indent=2) + "\n"


def nome_da_saida(caminho):
    caminho = Path(caminho)
    return (caminho.name if caminho.is_dir() else caminho.stem) + ".json"


def gravar(resultado, caminho_zip, pasta=None):
    """Grava em extrator_scorm/fichas/_individuais/<nome-do-pacote>.json (sem perguntar onde). Rodar de novo regrava o mesmo arquivo."""
    pasta = Path(pasta) if pasta else PASTA_INDIVIDUAIS
    pasta.mkdir(parents=True, exist_ok=True)
    destino = pasta / nome_da_saida(caminho_zip)
    try:
        destino.write_text(para_texto(resultado), encoding="utf-8", newline="\n")
    except OSError as e:
        raise ErroExtracao(f"Não consegui gravar {destino}: {e}")
    return destino
