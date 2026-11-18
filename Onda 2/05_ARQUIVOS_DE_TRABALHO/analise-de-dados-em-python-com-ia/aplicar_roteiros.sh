#!/bin/sh
# Aplica em cadeia os roteiros de <curso>/<slug>-blocos/trabalho/roteiros (ordem alfabetica),
# grava trabalho/curso_v1.json e valida. Uso: sh aplicar_roteiros.sh <pasta-curso> <slug>
set -e
S="/c/Users/João V/.claude/skills/inserir-blocos-scorm"
T="$1/$2-blocos/trabalho"
rm -rf "$T/etapas"; mkdir -p "$T/etapas"
ant="$T/curso_original.json"; n=0
for r in "$T"/roteiros/*.json; do
  n=$((n+1)); saida="$T/etapas/$(printf %02d $n).json"
  python "$S/scripts/inserir_sequencia.py" "$ant" --roteiro "$r" --modelos "$S/modelos/" --saida "$saida" | tail -1
  ant="$saida"
done
rm -f "$T/curso_v1.json"; cp "$ant" "$T/curso_v1.json"
python "$S/scripts/validar.py" "$T/curso_v1.json" --original "$T/curso_original.json" --modelos "$S/modelos/" | tail -6
