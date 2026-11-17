#!/bin/sh
# Aplica em cadeia os roteiros de trabalho/roteiros (ordem alfabetica) e grava trabalho/curso_v1.json.
# Uso: sh aplicar_roteiros.sh essentials|hands-on
set -e
S="/c/Users/João V/.claude/skills/inserir-blocos-scorm"
T="$1/chatgpt-$1-blocos/trabalho"
mkdir -p "$T/etapas"
ant="$T/curso_original.json"; n=0
for r in "$T"/roteiros/*.json; do
  n=$((n+1)); saida="$T/etapas/$(printf %02d $n).json"
  python "$S/scripts/inserir_sequencia.py" "$ant" --roteiro "$r" --modelos "$S/modelos/" --saida "$saida" | tail -1
  ant="$saida"
done
cp "$ant" "$T/curso_v1.json"
python "$S/scripts/validar.py" "$T/curso_v1.json" --original "$T/curso_original.json" --modelos "$S/modelos/" | tail -12
