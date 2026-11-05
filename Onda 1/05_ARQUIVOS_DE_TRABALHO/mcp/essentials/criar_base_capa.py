"""Gera cursoMCPEssentials_base_v2.json: o curso original com SÓ course.description traduzida (autorizado em 18/10/2026)."""
import json, pathlib
AQUI = pathlib.Path(__file__).resolve().parent
d = json.loads((AQUI / 'cursoMCPEssentials.json').read_text(encoding='utf-8'))
d['course']['description'] = ("Conectar assistentes de IA a ferramentas e dados, com segurança. Entenda o que o Model Context Protocol (MCP) "
    "padroniza e o que ele não garante, ligue um conector remoto público, autorize a leitura de uma pasta de arquivos fictícios, "
    "consulte e altere a própria agenda de forma reversível e monte um plano de conexão segura para um caso do seu trabalho.")
saida = AQUI / 'cursoMCPEssentials_base_v2.json'
assert not saida.exists(), 'ja existe'
saida.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8')
o = json.loads((AQUI / 'cursoMCPEssentials.json').read_text(encoding='utf-8'))
o['course']['description'] = d['course']['description']
assert o == d, 'difere em algo alem da descricao'
print('base_v2 gravada; unica diferenca: course.description')
