"""v2: corrige a alternativa "Base Brasileira" da questao 17 do Quiz do Essentials (associacao).

O texto dizia que a base brasileira "aceita expressoes com AND, OR e NOT"; o roteiro manda evitar NOT.
O campo e' `matchTitle`, que o validar_estrutura.py trata como nao textual — por isso a troca e' feita
DEPOIS da validacao da fase A, aqui, conferindo que so' esse campo muda.
Uso: python v2_quiz_associacao.py essentials/licoes_extraidas_RevBibEssentials/licao_08_Quiz.json
"""
import json
import pathlib
import sys

VELHO = 'Complementa a cobertura da literatura nacional, aceita expressões com AND, OR e NOT e permite aplicar filtros por idioma, país, ano e tipo de documento.'
NOVO = 'Complementa a cobertura da literatura nacional, aceita expressões booleanas com AND e OR (evitando NOT) e permite aplicar filtros por idioma, país, ano e tipo de documento.'

arq = pathlib.Path(sys.argv[1])
dados = json.loads(arq.read_text(encoding='utf-8'))
q = dados['lesson']['items'][16]
assert q['type'] == 'MATCHING', q['type']
alvo = q['answers'][2]
assert alvo['title'] == 'Base Brasileira' and alvo['matchTitle'] == VELHO, alvo
alvo['matchTitle'] = NOVO
arq.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding='utf-8')
print('matchTitle da questao 17 corrigido')
