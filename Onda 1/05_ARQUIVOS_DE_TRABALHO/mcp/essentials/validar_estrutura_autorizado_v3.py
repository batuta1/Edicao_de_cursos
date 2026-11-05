"""Invólucro do validar_estrutura.py da skill (v3). Autorizações do usuário em 18/10/2026:
- campos de texto do quiz: matchTitle, feedbackCorrect, feedbackIncorrect;
- gabarito da questão da agenda (Lição 7): SÓ answers[0] e answers[3] em lesson.items[13].items[0]."""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path.home() / '.claude/skills/revisar-curso-scorm/scripts'))
import validar_estrutura as v
v.CAMPOS_TEXTO |= {'matchTitle', 'feedbackCorrect', 'feedbackIncorrect'}
PERMITIDO = re.compile(r'lesson\.items\[13\]\.items\[0\]\.answers\[[03]\]\.correct$')
original = v.comparar
def comparar(a, b, caminho, estruturais, textuais):
    if PERMITIDO.search(caminho) and isinstance(a, bool) and isinstance(b, bool):
        if a != b: textuais.append(('correct(autorizado)', caminho))
        return
    original(a, b, caminho, estruturais, textuais)
v.comparar = comparar
v.main()
