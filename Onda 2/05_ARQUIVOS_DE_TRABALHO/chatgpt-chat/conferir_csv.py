"""Confere o gabarito da Oficina 4 (Hands On) a partir do CSV do roteiro."""
from collections import Counter
d = """2026-05,Atraso na entrega,42,38,6
2026-05,Produto com defeito,25,20,12
2026-05,Troca ou devolucao,12,11,4
2026-05,Cobranca indevida,9,9,3
2026-06,Atraso na entrega,38,35,5
2026-06,Produto com defeito,27,22,11
2026-06,Troca ou devolucao,14,13,4
2026-06,Cobranca indevida,8,8,3
2026-07,Atraso na entrega,45,41,6
2026-07,Produto com defeito,24,19,13
2026-07,Troca ou devolucao,13,12,5
2026-07,Cobranca indevida,10,9,4
2026-08,Atraso na entrega,40,37,5
2026-08,Produto com defeito,26,21,12
2026-08,Troca ou devolucao,15,14,4
2026-08,Cobranca indevida,7,7,3
2026-09,Atraso na entrega,39,36,6
2026-09,Produto com defeito,28,22,12
2026-09,Troca ou devolucao,46,25,15
2026-09,Cobranca indevida,9,9,3
2026-10,Atraso na entrega,41,38,5
2026-10,Produto com defeito,25,20,13
2026-10,Troca ou devolucao,58,27,18
2026-10,Cobranca indevida,8,8,3"""
R = [l.split(',') for l in d.splitlines()]
t = sum(int(r[2]) for r in R); s = sum(int(r[3]) for r in R)
print('total', t, 'resolvidas', s, round(100 * s / t, 1))
tr = [r for r in R if r[1].startswith('Troca')]
a = sum(int(r[2]) for r in tr); b = sum(int(r[3]) for r in tr)
print('troca', a, b, round(100 * b / a, 1), 'mai-ago', sum(int(r[2]) for r in tr[:4]), 'set-out', sum(int(r[2]) for r in tr[4:]))
c = Counter()
for r in R:
    c[r[0]] += int(r[2])
print(c)
for cat in sorted(set(r[1] for r in R)):
    x = [r for r in R if r[1] == cat]
    A = sum(int(r[2]) for r in x); B = sum(int(r[3]) for r in x)
    print(cat, A, B, round(100 * B / A, 1))
