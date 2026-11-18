"""Wrapper do validar_estrutura.py da skill revisar-curso-scorm que tambem aceita como texto
matchTitle, feedbackCorrect e feedbackIncorrect (enunciados/feedbacks de quiz em ingles).
Uso: python validar_texto.py curso.json licoes_extraidas_X/ [--detalhar]"""
import sys
sys.path.insert(0, r"C:\Users\João V\.claude\skills\revisar-curso-scorm\scripts")
import validar_estrutura as v
v.CAMPOS_TEXTO |= {'matchTitle', 'feedbackCorrect', 'feedbackIncorrect'}
sys.exit(v.main())
