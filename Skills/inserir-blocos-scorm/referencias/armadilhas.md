# Armadilhas conhecidas — e o que fazer

Problemas reais encontrados no laboratório. Se algo parecer estranho, procure aqui antes de concluir
que o curso quebrou.

| Sintoma | Causa | O que fazer |
|---|---|---|
| Regerei o pacote, mas o navegador mostra a versão antiga | **Cache do navegador**: mesmo endereço, cópia antiga reaproveitada (`transferSize: 0`) | Extraia cada versão em pasta **nova** (`teste/v2`, `teste/v3`…). Sirva com `teste/servidor_sem_cache.py`. |
| Roteiro/JSON recusado com "Unexpected UTF-8 BOM" | Arquivo salvo com BOM (Bloco de Notas, `Set-Content` do PowerShell 5.1) | Os scripts da skill já aceitam BOM. Se aparecer, o script é de fora da skill. |
| Parágrafos colados dentro de accordion/abas | Faltou o `<p></p>` vazio entre os parágrafos | Padrão dos cursos; o validador reprova. |
| `validar.py` mostra aviso "correct/corrects … não é id de alternativa" | O Rise grava texto de pergunta nesses campos em questões de **múltipla resposta** | Já existe no pacote original; não é causado pela inserção. Avise o usuário para revisar a questão. |
| Questão de verificação ou atividade HTML volta em branco ao reabrir o curso | O Rise só guarda a **conclusão**, não a resposta/estado | Comportamento do Rise (as questões nativas fazem igual). O Continue continua liberado. |
| Abrir itens de accordion não muda o `suspend_data` | O Rise não registra abertura de item de accordion | Normal; acontece também nos accordions originais. |
| "Content launched outside of a supported LMS environment." | Abriu via `http://` sem LMS | Abra por duplo clique (`file://`) ou pelo `lms_mock.html`. |
| Painel do navegador do Claude mostra página em branco ao abrir `file://` | O navegador embutido não executa scripts de `file://` | Use o servidor local + `lms_mock.html`. |
| Clique cai no lugar errado / bloco aparece em branco no print | O painel muda de tamanho; blocos têm animação de entrada; iframes carregam só quando visíveis (`loading="lazy"`) | Tire print antes de clicar por coordenada; role com o mouse (não só por script) e espere 1–3 s. |
| Erro antigo no console | O console da aba acumula mensagens de páginas anteriores | Abra uma aba nova para cada teste. |
| Script recusa gravar: "já existe" | Proteção contra sobrescrita | Use nome de versão novo. Só apague arquivos que você mesmo gerou nesta sessão. |
| PowerShell bloqueia `Remove-Item` com caminho montado por variável | Proteção do ambiente contra apagar pastas do sistema | Use `Remove-Item -LiteralPath "caminho\relativo\arquivo"`, um por vez. |
| Working directory mudou sozinho | `Set-Location` dentro de um comando persiste para os próximos | Volte com `Set-Location` à pasta do projeto ao terminar. |
| Acentos/emoji quebram ao imprimir no terminal | Codificação do console do Windows | `$env:PYTHONIOENCODING='utf-8'`; em `python -I` use `python -I -X utf8`. |
| Bloco HTML com barra de progresso "parada" no print | Print tirado no meio da animação | Meça pelo DOM ou tire outro print. |
| `listar_blocos.py \| Select-Object -First N` termina com código 255 | O PowerShell interrompe o pipeline | Inofensivo; não é erro do script. |
