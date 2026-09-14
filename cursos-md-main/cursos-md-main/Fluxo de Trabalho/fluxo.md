<link rel="stylesheet" href="css/style.css">

1. passar o `plano_de_aula_xxx.md` essentials/hands-on (selecionado) passa por um primeiro prompt [objetivo: traduzir plano de aula para o articulate]; Resultado: `ROTEIRO_xxx.md`.

2. carregar no articulate `promptArticulate.md` e o `ROTEIRO_xxx.md`;

3. Gera o curso;

4. Verificação visual mínima;

5. Gerar SCORM;

6. Deserializar, separar em lições e enviar `.json` _claude code_;

7. Avaliar alterações na estrutura de blocos do Articulate;

8. Jump to 5; 

9. `prompt.md` (Arquivo Pendente) para alterar o conteúdo, sem estragar a estrutura do `.json`;

10. Reserializar - Novo SCORM;

11. FIM!