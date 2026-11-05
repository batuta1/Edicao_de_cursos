"""Invólucro do validar_estrutura.py da skill revisar-curso-scorm.
Acrescenta SÓ os campos de texto do quiz autorizados pelo usuário em 18/10/2026:
matchTitle, feedbackCorrect, feedbackIncorrect. Todo o resto da validação é o da skill."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path.home() / '.claude/skills/revisar-curso-scorm/scripts'))
import validar_estrutura as v
v.CAMPOS_TEXTO |= {'matchTitle', 'feedbackCorrect', 'feedbackIncorrect'}
v.main()
