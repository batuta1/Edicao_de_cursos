"""
Serializa um JSON de curso Rise de volta para o formato Base64
(operacao inversa do desserialize.py).

Formato de saida, identico ao de cursoClaudeCoworkEssentials_editado_base64.txt:
  - JSON compacto, sem espacos: separators=(",", ":")
  - acentos crus em UTF-8 (ensure_ascii=False), sem escapes \\uXXXX
  - Base64 padrao com padding "="
  - uma unica linha, sem quebra de linha no final

Uso:
    python serialize.py
    python serialize.py entrada.json saida.txt
"""

import base64
import json
import shutil
import sys
from pathlib import Path

ENTRADA_PADRAO = "cursoClaudeCoworkEssentials_editado.json"
SAIDA_PADRAO = "cursoClaudeCoworkEssentials_editado_base64.txt"


def serializar(dados) -> str:
    """Converte o dicionario do curso para a string Base64 no formato do Rise."""
    json_texto = json.dumps(dados, ensure_ascii=False, separators=(",", ":"))
    return base64.b64encode(json_texto.encode("utf-8")).decode("ascii")


def main() -> int:
    entrada = Path(sys.argv[1] if len(sys.argv) > 1 else ENTRADA_PADRAO)
    saida = Path(sys.argv[2] if len(sys.argv) > 2 else SAIDA_PADRAO)

    if not entrada.is_file():
        print(f"ERRO: arquivo de entrada nao encontrado: {entrada}")
        return 1

    with entrada.open("r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    texto_base64 = serializar(dados)

    # Confere que o Base64 gerado volta a ser exatamente o mesmo JSON
    conferencia = json.loads(base64.b64decode(texto_base64).decode("utf-8"))
    if conferencia != dados:
        print("ERRO: round-trip falhou, arquivo NAO foi gravado.")
        return 1

    # Preserva a versao anterior antes de sobrescrever
    if saida.exists():
        backup = saida.with_suffix(saida.suffix + ".bak")
        shutil.copy2(saida, backup)
        print(f"Backup da versao anterior: {backup}")

    # newline="" evita que o Windows converta \n em \r\n; sem quebra de linha final
    with saida.open("w", encoding="utf-8", newline="") as arquivo:
        arquivo.write(texto_base64)

    print(f"Arquivo Base64 gerado com sucesso: {saida}")
    print(f"  JSON compacto : {len(json.dumps(dados, ensure_ascii=False, separators=(',', ':')).encode('utf-8')):,} bytes")
    print(f"  Base64        : {len(texto_base64):,} caracteres")
    print(f"  Titulo        : {dados['course'].get('title')}")
    print(f"  Cor           : {dados['course'].get('color')}")
    print(f"  Licoes        : {len(dados['course'].get('lessons', []))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
