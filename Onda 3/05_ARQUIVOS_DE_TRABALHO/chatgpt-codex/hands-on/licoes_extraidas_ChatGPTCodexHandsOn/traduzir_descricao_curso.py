"""Traduz a descricao do curso (texto da capa), que fica fora das licoes.

Grava um JSON-base novo, sem tocar no original. Esse JSON-base e' o que vai para o
scorm_reempacotar.py; o validar_estrutura.py continua comparando contra o original.

Uso (a partir da pasta hands-on):
    python licoes_extraidas_ChatGPTCodexHandsOn/traduzir_descricao_curso.py
"""
import json
import pathlib

ORIGINAL = pathlib.Path("cursoChatGPTCodexHandsOn.json")
SAIDA = pathlib.Path("cursoChatGPTCodexHandsOn_base_capa_pt.json")

WRAP_INI = '<div data-editor-id="10c2c046-e6e8-4dca-b123-edb8c03c2ca9"><p>'
WRAP_FIM = "</p></div>"
INGLES_INICIO = "Ready to see AI in action?"

NOVO_TEXTO = (
    "Em menos de 90 minutos, você sai deste curso com uma tarefa real entregue por um agente de "
    "IA, e não apenas com uma explicação sobre como isso funciona. Em quatro oficinas e um Projeto "
    "Final, você abre o Codex dentro do ChatGPT, conecta um repositório de teste no GitHub, aprende "
    "a pedir uma tarefa do jeito certo e confere o trabalho do agente antes de aceitar. Não é "
    "preciso saber programar como profissional: basta topar clicar, testar e errar um pouco pelo "
    "caminho."
)

curso = json.loads(ORIGINAL.read_text(encoding="utf-8"))
atual = curso["course"]["description"]
if not (atual.startswith(WRAP_INI + INGLES_INICIO) and atual.endswith(WRAP_FIM)):
    raise SystemExit("Descricao atual nao e' a original esperada. Nada foi gravado.")

curso["course"]["description"] = WRAP_INI + NOVO_TEXTO + WRAP_FIM
SAIDA.write_text(json.dumps(curso, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Gravado: {SAIDA}")
