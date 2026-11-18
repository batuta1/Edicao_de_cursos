@echo off
rem Abre a janela de extracao de SCORM. Duplo clique. Precisa do uv instalado (https://docs.astral.sh/uv/).
rem Vai para a raiz do repositorio (duas pastas acima deste arquivo) e roda o comando.
cd /d "%~dp0..\.."
uv run python -m extrator_scorm
if errorlevel 1 (
  echo.
  echo A janela fechou com erro. Leia a mensagem acima.
  pause
)
