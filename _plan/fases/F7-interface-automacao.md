# F7 · Interface da automação (tkinter)

Decisões: [02-interface-automacao.md](../_duvidas/02-interface-automacao.md) (D1 e D2 fechadas: atalho executável por pasta, comando `uv run python -m automacao.interface`; `.exe` de verdade em stand-by, D2.1). Padrão: skill [`interface-tkinter`](../../.claude/skill/interface-tkinter/SKILL.md).
Depende de: F6. Interferência do usuário: **nenhuma**.

## Objetivo

Janela com 2 abas (`Executar` e `Notion`) que chama a mesma lógica do CLI, com ensaio antes de aplicar.

## Checklist

### Base comum (em `scripts/comum/ui/`)
- [ ] Carregar Ubuntu e SUSE Mono **no Windows** (`AddFontResourceExW` com `FR_PRIVATE`, antes de criar a janela), mantendo o caminho do Linux (fontconfig)
- [ ] `aplicar()` com a mesma assinatura de hoje; se a fonte não existir, cai na fonte do sistema
- [ ] Helper de área de texto **somente leitura** (`tk.Text` com `state="disabled"`, escrevendo por função própria)
- [ ] Teste: abre janela oculta e confere `Ubuntu` e `SUSE Mono` instaladas (🧪 no Windows)
- [ ] A tela do extrator passa a usar `comum/ui` e as áreas de texto somente leitura

### Controlador sem widgets (`scripts/automacao/interface/controlador.py`)
- [ ] `estado_do_ambiente()`: existe `Cursos/`? existe `csv`? existe `NOTION_TOKEN`? (devolve motivos em texto)
- [ ] `executar(etapas, ensaio, commit, progresso, cancelar)` chama as funções de `automacao.atualizar` (sem duplicar regra)
- [ ] `ensaio_notion()` devolve as linhas (curso, status, progresso, responsável, resultado) e guarda a impressão do `csv` usada
- [ ] `aplicar_notion()` só roda se houve ensaio do **mesmo** `csv`; senão erro claro
- [ ] `testar_conexao()` chama o `inspecionar` e devolve colunas e tipos
- [ ] Testes do controlador sem janela

### Janela (`scripts/automacao/interface/tela.py`)
- [ ] 1150 × 760, redimensionável, `ttk.Notebook` com `Executar` e `Notion`
- [ ] Aba Executar, na ordem da skill: etapas (caixas) → ações (`Ensaio`, `Aplicar`, `Parar`; caixas "Ensaio" e "Fazer commit") → mensagem de estado → tabela por curso + relatório em texto
- [ ] Etapas indisponíveis desativadas, com o motivo escrito ao lado (P6)
- [ ] Operação em thread; progresso por fila + `after()`; ações em conflito desativadas; `Parar` com aviso de quando surte efeito (P7)
- [ ] `Aplicar` pede confirmação (quantos cursos serão alterados) antes de escrever no Notion
- [ ] Aba Notion: estado do token (sem digitar), `Testar conexão`, colunas e tipos, fonte de dados
- [ ] Cor de estado sempre acompanhada do estado por escrito
- [ ] Ganchos para teste (`janela.ctl`, `janela.abas`), como na tela do extrator

### Ponto de entrada e atalhos (D2)
- [ ] `scripts/automacao/interface/__main__.py` → `uv run python -m automacao.interface`
- [ ] `--help` e mensagem amigável se o `tkinter` não existir (igual ao extrator)
- [ ] `scripts/automacao/abrir-interface.bat`: vai para a raiz do repositório (`cd /d "%~dp0\..\.."`), roda `uv run python -m automacao.interface` e, se der erro, `pause` para a mensagem não sumir
- [ ] `scripts/extrator_scorm/abrir-interface.bat`: o mesmo, com `uv run python -m extrator_scorm`
- [ ] Testar o duplo clique nos dois atalhos (🧪 no Windows)
- [ ] Sem compilar nada agora; `.exe` com PyInstaller fica em stand-by (D2.1)

### Revisão (checklist da skill) 🧪
- [ ] Janela menor: nada some; textos e caminhos longos cortam sem quebrar a tela
- [ ] Cada ação principal fácil de achar
- [ ] `Ensaio` → `Aplicar` → 2ª execução reporta "sem mudança"
- [ ] Teste real no Notion com 1 curso antes do lote (o mesmo da F4)

### Documentação
- [ ] `scripts/automacao/README.md` **curto** (≤ 15 linhas): o que é, o atalho/comando que abre a interface, link para `scripts/documentacao/`
- [ ] Seção "Tela" no início de `automacao-notion.md` (atalho, comando e 3 observações)
- [ ] `lista de UIs.md`: marcar a interface como ✅
- [ ] Skill `interface-tkinter` corrigida (ver abaixo)

## Correções da skill `interface-tkinter` (após a F6)

- [ ] Trocar as referências de outro projeto (`1_src/generic/ui/`, `deployer`, `pairing`, `overviwer_render`, `_duvidas/1.4_...`) pelos caminhos reais: `scripts/comum/ui/`, `scripts/extrator_scorm/interface/`, `scripts/automacao/interface/`
- [ ] Regra nova: **ação que escreve fora da máquina** (Notion, push) tem ensaio antes e confirmação
- [ ] Receita de fontes por sistema (Windows e Linux)
- [ ] Reforçar "áreas de visualização somente leitura" apontando o helper de `comum/ui`
- [ ] Escopo: cada interface em `scripts/<parte>/interface/`, base compartilhada em `scripts/comum/ui/`; uma interface não importa de outra

## Pronto quando

A janela abre no Windows com as fontes certas, o ensaio mostra a tabela, o `Aplicar` só habilita depois do ensaio e os testes passam.
