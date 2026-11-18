"""xlsx → csv. Só a aba "Checklist 60 dias". Separador `,`; `,` dentro da célula vira `;`; quebra de linha na célula vira espaço."""
import csv
import datetime as dt
import re
from pathlib import Path

import openpyxl

ABA = "Checklist 60 dias"


def _celula(v):
    """Converte o valor de uma célula em texto de csv: vazio, número sem `.0`, data ISO, `,` vira `;` e quebra de linha vira espaço."""
    if v is None:
        return ""
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    if isinstance(v, (dt.datetime, dt.date)):
        v = v.isoformat()
    return re.sub(r"\s*[\r\n]+\s*", " ", str(v)).replace(",", ";")


def converter(xlsx, destino=None, saida=print):
    """Converte a aba "Checklist 60 dias" de `xlsx` em csv (UTF-8) e devolve o caminho do csv. Erro se a aba não existir."""
    xlsx = Path(xlsx)
    destino = Path(destino) if destino else xlsx.with_suffix(".csv")
    valores = openpyxl.load_workbook(xlsx, data_only=True)
    if ABA not in valores.sheetnames:
        raise ValueError(f'a aba "{ABA}" não existe em {xlsx.name} (abas: {", ".join(valores.sheetnames)})')
    ws = valores[ABA]
    linhas = [[_celula(c) for c in row] for row in ws.iter_rows(values_only=True)]
    while linhas and not any(linhas[-1]):
        linhas.pop()
    # fórmula sem valor guardado: o csv ficaria vazio onde o Excel mostra número
    formulas = openpyxl.load_workbook(xlsx, data_only=False)[ABA]
    sem_valor = [c.coordinate for row in formulas.iter_rows() for c in row
                 if isinstance(c.value, str) and c.value.startswith("=") and ws[c.coordinate].value is None]
    if sem_valor:
        saida(f"csv: aviso: {len(sem_valor)} fórmula(s) sem valor guardado ficaram vazias ({', '.join(sem_valor[:5])}...)")
    with destino.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f, delimiter=",", lineterminator="\n").writerows(linhas)
    saida(f"csv: {destino.name} ({len(linhas) - 1} linhas de dados)")
    return destino
