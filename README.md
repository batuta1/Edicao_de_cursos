# Edição de cursos · branch `structuring`

🧪 Esta branch é o **laboratório** dos scripts. Aqui se corrige e se testa; quando estiver decidido, só a pasta `scripts/` vai para a `main`.

## 📁 O que tem aqui

| Pasta / arquivo | O que é |
|---|---|
| `scripts/automacao/` | Planilha de produção → autores → Notion (janela: `abrir-interface.bat`) |
| `scripts/extrator_scorm/` | Mapeamento dos SCORM de `Cursos/` (janela: `abrir-interface.bat`) |
| `scripts/comum/` | O que as duas partes usam (fontes e base de janelas, caminhos, `autor.json`) |
| `scripts/documentacao/` | Os guias (comece por `README.md` lá) |
| `.gitattributes` | Atalhos `.bat` com fim de linha do Windows |
| `pyproject.toml`, `uv.lock` | Dependências (uv). Ficam na raiz |
| `_plan/` | Planejamento (dúvidas e fases) |

## 🚀 Deploy da pasta `scripts/` na `main`

⛔ **Nunca** use `git merge structuring` na `main`: esta branch não tem `Cursos/`, `Skills/` nem `bagunca/`, e o merge pode **apagá-los** na `main`. O deploy copia só os caminhos do código.

Rode em PowerShell, na raiz do repositório:

1. ✅ **Tudo commitado aqui**

   ```powershell
   git switch structuring
   git status
   ```

2. 🌿 **Cópia limpa da `main`** (sem trocar de branch)

   ```powershell
   git fetch origin
   git worktree add -b promove-scripts ..\Edicao_main origin/main
   cd ..\Edicao_main
   ```

3. 📦 **Trazer só o código**

   ```powershell
   git rm -r -q --ignore-unmatch scripts
   git checkout structuring -- scripts pyproject.toml uv.lock .gitattributes
   ```

   Na 1ª vez o `git rm` não encontra nada e segue; nas próximas ele remove o que foi apagado aqui.

4. ✍️ **`.gitignore`**: copie à mão, da `structuring` para a cópia, só as linhas novas.

5. 🔍 **Conferir**

   ```powershell
   git status
   git diff origin/main --stat -- Cursos Skills bagunca
   ```

   O segundo comando tem que ficar **vazio**. Se aparecer algo, pare.

6. 💾 **Commit e envio**

   ```powershell
   git add -A scripts pyproject.toml uv.lock .gitattributes .gitignore
   git commit -m "scripts: atualiza automacao e extrator"
   git push -u origin promove-scripts
   ```

   Depois abra o Pull Request `promove-scripts` → `main` no GitHub.

7. 🧹 **Limpar** (depois do PR aceito)

   ```powershell
   cd ..\Edicao_de_cursos
   git worktree remove ..\Edicao_main
   git branch -D promove-scripts
   ```

🔑 O token do Notion (`scripts/automacao/.env`) **nunca** vai junto: o `.gitignore` o protege. O que vai é o `.env.example`.
