"""
Geracao e reconhecimento de IDs no formato do Rise 360.

O Rise usa dois formatos, conforme o tipo de bloco (ver ESTRATEGIA.md):
  - uuid  : UUID v4, ex. 0c024a65-a077-483b-9e37-e5a757bda639
  - cuid2 : 24 caracteres a-z0-9 comecando com letra, ex. phn3ltqr3ggvvqz5h0tdn6gw
O player nao valida formato, mas seguimos o mesmo padrao do Rise por seguranca.
"""
import re
import secrets
import string
import uuid

RE_UUID = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$')
RE_CUID2 = re.compile(r'^[a-z][a-z0-9]{23}$')
CHAVES_ID = ('id', 'globalBlockId')


def formato_de(valor):
    if isinstance(valor, str) and RE_UUID.match(valor):
        return 'uuid'
    if isinstance(valor, str) and RE_CUID2.match(valor):
        return 'cuid2'
    return 'outro'


def coletar_ids(obj, acc=None):
    """Todos os valores de 'id' e 'globalBlockId' em qualquer profundidade."""
    acc = set() if acc is None else acc
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in CHAVES_ID and isinstance(v, str) and v:
                acc.add(v)
            coletar_ids(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            coletar_ids(v, acc)
    return acc


def novo_id(formato, existentes):
    """Gera um ID inedito no formato pedido e ja o registra em `existentes`."""
    while True:
        if formato == 'uuid':
            novo = str(uuid.uuid4())
        elif formato == 'cuid2':
            novo = secrets.choice(string.ascii_lowercase) + ''.join(
                secrets.choice(string.ascii_lowercase + string.digits) for _ in range(23))
        else:
            raise ValueError(f'formato de ID desconhecido: {formato}')
        if novo not in existentes:
            existentes.add(novo)
            return novo
