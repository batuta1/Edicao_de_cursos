# Skills do Claude

> **Para o João:** esta pasta tem as versões **atualizadas** das skills, as que você vai usar daqui para a frente (vindas da `main`, commit `51a87a2`). Inclui a skill nova `organizar-pasta-de-cursos`, que as outras três citam. Elas substituem as cópias antigas desta pasta.

Cópias das skills pessoais que ficam em `%USERPROFILE%\.claude\skills\`.

| Skill | Para que serve |
|---|---|
| `criar-ementa-curso` | Cria do zero o pacote de um curso: ementa, roteiros Essentials e Hands-on, tabela MET e carga horária. |
| `revisar-curso-scorm` | Revisa os textos de cursos Articulate Rise 360 exportados em SCORM (.zip) sem quebrar a estrutura. |
| `inserir-blocos-scorm` | Insere blocos novos (nativos no padrão da equipe ou HTML próprio) em SCORM do Rise 360 sem a plataforma Articulate, e verifica se o pacote está consistente antes da LMS. |
| `organizar-pasta-de-cursos` | Diz onde guardar e como nomear tudo da pasta `Cursos/` (empresa, curso, versões do SCORM, cópias, apoio em `base/`, README). As três skills acima a citam para decidir onde entregar. Traz o script `versao_do_pacote.py`, que diz se um SCORM é versão nova ou cópia de uma existente. |

## Como instalar em outro Claude

**Claude Code (outro computador):** copie a pasta da skill para `%USERPROFILE%\.claude\skills\`
(no Mac/Linux, `~/.claude/skills/`). Se quiser que ela valha só para um projeto, copie para
`.claude\skills\` dentro da pasta desse projeto.

**Claude.ai / app Claude Desktop:** em *Settings → Capabilities → Skills*, clique em *Upload skill*
e envie o arquivo `.zip` correspondente.

> Se você editar uma skill em `%USERPROFILE%\.claude\skills\`, copie a nova versão para cá de novo
> e gere o `.zip` outra vez.
