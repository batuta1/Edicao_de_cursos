"""A janela da automação (tkinter + ttk), no padrão da skill `interface-tkinter`. Duas abas:

* **Executar:** etapas (checklist, extrator, autores, notion) → botões Ensaio / Aplicar / Parar → estado → tabela por curso e relatório.
* **Notion:** estado do token (nunca digitado aqui) e botão para testar a conexão e listar as colunas.

Toda regra mora em `controlador.Controlador`; aqui só há widgets, thread + fila e textos.
Abrir: `uv run python -m automacao.interface` (ou o atalho `abrir-interface.bat` da pasta da automação).
"""
import queue
import threading

from comum.ui import fontes, texto

from ..atualizar import ETAPAS, ErroDeEtapa
from ..git_seguro import ErroGit
from ..notion.api import ErroNotion
from .controlador import ROTULOS, Controlador

MENSAGEM_SEM_TK = ("A tela precisa do tkinter, que não está instalado.\n"
                   "No Linux (Ubuntu/Debian): sudo apt install python3-tk\n"
                   "Enquanto isso, use a linha de comando: uv run python -m automacao --help")

COLUNAS_CURSOS = ("Curso", "Status", "Progresso", "Responsável", "Resultado")
COLUNAS_NOTION = ("Coluna", "Tipo", "Usada para")
PAPEIS = {"nome": "nome do curso", "status": "status", "responsavel": "responsável", "progresso": "progresso"}


def _erro_em_texto(e):
    """Mensagem curta e legível para qualquer erro previsto; os imprevistos mostram o tipo do erro."""
    if isinstance(e, (ErroDeEtapa, ErroGit, ErroNotion, ValueError)):
        return str(e)
    return f"erro inesperado ({type(e).__name__}): {e}"


def montar(janela, tk, ttk, messagebox, controlador=None):
    """Cria todos os widgets dentro de `janela` e devolve `janela`. Separada de `abrir()` para o teste usar uma janela escondida."""
    ctl = controlador or Controlador()
    janela.title("Automação · checklist → Notion")
    janela.geometry("1150x760")
    abas = ttk.Notebook(janela)
    abas.pack(fill="both", expand=True)
    aba_exec, aba_notion = ttk.Frame(abas), ttk.Frame(abas)
    abas.add(aba_exec, text="Executar")
    abas.add(aba_notion, text="Notion")

    fila = queue.Queue()                                     # a thread de trabalho só fala com a janela por aqui
    estado = {"rodando": False, "parar": threading.Event(), "log": []}

    # ------------------------------------------------------------------ aba Executar: entradas (etapas)
    quadro_etapas = ttk.LabelFrame(aba_exec, text="Etapas")
    quadro_etapas.pack(fill="x", padx=8, pady=8)
    marcas, caixas, avisos = {}, {}, {}
    for etapa in ETAPAS:
        marcas[etapa] = tk.BooleanVar(value=True)
        linha = ttk.Frame(quadro_etapas)
        linha.pack(fill="x", padx=8, pady=2)
        caixas[etapa] = ttk.Checkbutton(linha, text=ROTULOS[etapa], variable=marcas[etapa], command=lambda: ao_mudar_selecao())
        caixas[etapa].pack(side="left")
        avisos[etapa] = ttk.Label(linha, text="")
        avisos[etapa].pack(side="left", padx=12)
    commit_var = tk.BooleanVar(value=True)
    ttk.Checkbutton(quadro_etapas, text="Fazer commit (só local; nunca faz push)", variable=commit_var).pack(anchor="w", padx=8, pady=(4, 6))

    # ------------------------------------------------------------------ ações, estado e resultados
    quadro_botoes = ttk.Frame(aba_exec)
    quadro_botoes.pack(fill="x", padx=8)
    b_ensaio = ttk.Button(quadro_botoes, text="Ensaio", command=lambda: iniciar(True))
    b_aplicar = ttk.Button(quadro_botoes, text="Aplicar", command=lambda: iniciar(False), state="disabled")
    b_parar = ttk.Button(quadro_botoes, text="Parar", command=lambda: parar(), state="disabled")
    for b in (b_ensaio, b_aplicar, b_parar):
        b.pack(side="left", padx=(0, 6), pady=4)
    mensagem = tk.StringVar(value="Escolha as etapas e faça um Ensaio. O Aplicar só libera depois dele.")
    ttk.Label(aba_exec, textvariable=mensagem, wraplength=1100).pack(fill="x", padx=8, pady=4)

    quadro_tabela = ttk.Frame(aba_exec)
    quadro_tabela.pack(fill="both", expand=True, padx=8)
    tabela = ttk.Treeview(quadro_tabela, columns=COLUNAS_CURSOS, show="headings", height=12)
    for c, largura in zip(COLUNAS_CURSOS, (420, 110, 90, 110, 190)):
        tabela.heading(c, text=c)
        tabela.column(c, width=largura, anchor="w")
    rolagem = ttk.Scrollbar(quadro_tabela, orient="vertical", command=tabela.yview)
    tabela.configure(yscrollcommand=rolagem.set)
    rolagem.pack(side="right", fill="y")
    tabela.pack(side="left", fill="both", expand=True)

    quadro_relatorio = ttk.Frame(aba_exec)
    quadro_relatorio.pack(fill="x", padx=8, pady=8)
    relatorio = texto.criar_area_leitura(tk, quadro_relatorio, height=10, wrap="word")
    barra_relatorio = ttk.Scrollbar(quadro_relatorio, orient="vertical", command=relatorio.yview)
    relatorio.configure(yscrollcommand=barra_relatorio.set)
    barra_relatorio.pack(side="right", fill="y")
    relatorio.pack(side="left", fill="x", expand=True)

    # ------------------------------------------------------------------ aba Notion
    token_var = tk.StringVar()
    ttk.Label(aba_notion, textvariable=token_var, wraplength=1100).pack(fill="x", padx=8, pady=(8, 4))
    ttk.Label(aba_notion, wraplength=1100,
              text="O token fica em scripts/automacao/.env (linha NOTION_TOKEN=...). Ele nunca é digitado nesta janela.").pack(fill="x", padx=8)
    quadro_teste = ttk.Frame(aba_notion)
    quadro_teste.pack(fill="x", padx=8, pady=6)
    b_testar = ttk.Button(quadro_teste, text="Testar conexão", command=lambda: testar())
    b_testar.pack(side="left")
    msg_notion = tk.StringVar(value="Clique em Testar conexão para listar as colunas do banco.")
    ttk.Label(aba_notion, textvariable=msg_notion, wraplength=1100).pack(fill="x", padx=8, pady=4)
    quadro_cols = ttk.Frame(aba_notion)
    quadro_cols.pack(fill="both", expand=True, padx=8, pady=(0, 8))
    tabela_notion = ttk.Treeview(quadro_cols, columns=COLUNAS_NOTION, show="headings")
    for c, largura in zip(COLUNAS_NOTION, (380, 160, 220)):
        tabela_notion.heading(c, text=c)
        tabela_notion.column(c, width=largura, anchor="w")
    rolagem_notion = ttk.Scrollbar(quadro_cols, orient="vertical", command=tabela_notion.yview)
    tabela_notion.configure(yscrollcommand=rolagem_notion.set)
    rolagem_notion.pack(side="right", fill="y")
    tabela_notion.pack(side="left", fill="both", expand=True)

    # ------------------------------------------------------------------ lógica de tela
    def selecionadas():
        return [e for e in ETAPAS if marcas[e].get()]

    def atualizar_estado():
        """Recalcula o que está disponível (com o motivo escrito), o botão Aplicar e o aviso do token."""
        for _ in range(len(ETAPAS)):                         # desmarcar uma etapa pode tornar outra indisponível: repete até estabilizar
            motivos = ctl.motivos(selecionadas())
            mudou = False
            for e in ETAPAS:
                if motivos[e] and marcas[e].get():
                    marcas[e].set(False)
                    mudou = True
            if not mudou:
                break
        motivos = ctl.motivos(selecionadas())
        for e in ETAPAS:
            livre = motivos[e] is None and not estado["rodando"]
            caixas[e].configure(state="normal" if livre else "disabled")
            avisos[e].configure(text=f"indisponível: {motivos[e]}" if motivos[e] else "")
        pode = bool(selecionadas()) and not estado["rodando"]
        b_ensaio.configure(state="normal" if pode else "disabled")
        b_aplicar.configure(state="normal" if pode and ctl.pode_aplicar(selecionadas()) else "disabled")
        b_parar.configure(state="normal" if estado["rodando"] else "disabled")
        b_testar.configure(state="disabled" if estado["rodando"] else "normal")
        token_var.set("Token do Notion: encontrado ✔" if ctl.token_definido() else "Token do Notion: ausente ✘ (defina NOTION_TOKEN no .env)")

    def ao_mudar_selecao():
        """Marcar ou desmarcar uma etapa invalida o ensaio feito antes e recalcula o que está disponível."""
        ctl.esquecer_ensaio()                                # o ensaio anterior era de outra seleção
        atualizar_estado()

    def mostrar_log():
        """Mostra o log acumulado na área de relatório e rola até o fim."""
        texto.escrever(relatorio, "\n".join(estado["log"]))
        relatorio.see("end")

    def mostrar_tabela():
        """Preenche a tabela de cursos com o resultado da última execução do Notion."""
        tabela.delete(*tabela.get_children())
        for linha in ctl.linhas_da_tabela():
            tabela.insert("", "end", values=linha)

    def sondar():
        """Chamada a cada 100 ms enquanto algo roda: passa as mensagens da thread para a janela."""
        mudou_log = False
        while True:
            try:
                tipo, *dados = fila.get_nowait()
            except queue.Empty:
                break
            if tipo == "log":
                estado["log"].append(dados[0])
                mudou_log = True
            elif tipo == "progresso":
                mensagem.set(dados[0])
            elif tipo == "fim":
                estado["rodando"] = False
                codigo, erro, ensaio = dados
                if erro:
                    estado["log"].append(f"ERRO: {erro}")
                    mensagem.set(f"Erro: {erro}")
                elif codigo == 0:
                    mensagem.set("Ensaio concluído: confira a tabela e o relatório. Agora o Aplicar está liberado." if ensaio
                                 else "Aplicado. Faça um novo Ensaio antes de aplicar de novo.")
                else:
                    mensagem.set("Interrompido. O que já foi gravado fica; faça um novo Ensaio.")
                mudou_log = True
                mostrar_tabela()
                atualizar_estado()
            elif tipo == "fim_teste":
                estado["rodando"] = False
                resultado, erro = dados
                tabela_notion.delete(*tabela_notion.get_children())
                if erro:
                    msg_notion.set(f"Erro: {erro}")
                else:
                    titulo, colunas = resultado
                    msg_notion.set(f"Conexão ok. Fonte de dados: {titulo}. As 4 colunas necessárias foram encontradas.")
                    for nome, tipo_col, papel in colunas:
                        tabela_notion.insert("", "end", values=(nome, tipo_col, PAPEIS.get(papel, "")))
                atualizar_estado()
        if mudou_log:
            mostrar_log()
        if estado["rodando"]:
            janela.after(100, sondar)

    def iniciar(ensaio):
        """Botões Ensaio e Aplicar: confirma (só no Aplicar), prepara a janela e roda `ctl.rodar` numa thread."""
        etapas = selecionadas()
        if not ensaio:
            quantos = ctl.quantos_mudariam() if "notion" in etapas else 0
            linhas = ["Aplicar de verdade estas etapas: " + ", ".join(etapas) + "."]
            if "notion" in etapas:
                linhas.append(f"O Notion não tem desfazer. Cursos a atualizar no Notion (segundo o ensaio): {quantos}.")
            if commit_var.get():
                linhas.append("Serão feitos commits locais (sem push).")
            if not messagebox.askokcancel("Confirmar", "\n".join(linhas)):
                return
        estado.update(rodando=True, parar=threading.Event(), log=[])
        mensagem.set("Ensaio em andamento..." if ensaio else "Aplicando...")
        mostrar_log()
        tabela.delete(*tabela.get_children())
        atualizar_estado()
        commit = bool(commit_var.get())
        parar_evento = estado["parar"]

        def trabalho():
            """Roda fora da thread da janela; fala com ela só pela fila."""
            try:
                codigo = ctl.rodar(etapas, ensaio, commit, saida=lambda t: fila.put(("log", t)), cancelar=parar_evento.is_set,
                                   progresso=lambda i, n, nome: fila.put(("progresso", f"Notion: curso {i} de {n}: {nome}")))
                fila.put(("fim", codigo, None, ensaio))
            except Exception as e:                           # um erro não derruba a janela
                fila.put(("fim", None, _erro_em_texto(e), ensaio))
        threading.Thread(target=trabalho, daemon=True).start()
        janela.after(100, sondar)

    def parar():
        """Botão Parar: avisa a thread, que para entre uma etapa ou um curso e o seguinte."""
        estado["parar"].set()
        mensagem.set("Parando: vale quando terminar a etapa ou o curso atual do Notion.")
        b_parar.configure(state="disabled")

    def testar():
        """Botão Testar conexão: consulta o Notion numa thread e mostra as colunas na aba."""
        estado.update(rodando=True)
        msg_notion.set("Testando a conexão...")
        atualizar_estado()

        def trabalho():
            """Roda a consulta ao Notion fora da thread da janela."""
            try:
                fila.put(("fim_teste", ctl.testar_conexao(), None))
            except Exception as e:
                fila.put(("fim_teste", None, _erro_em_texto(e)))
        threading.Thread(target=trabalho, daemon=True).start()
        janela.after(100, sondar)

    atualizar_estado()
    # ganchos para o teste da janela
    janela.ctl, janela.abas, janela.aba_exec, janela.aba_notion = ctl, abas, aba_exec, aba_notion
    janela.marcas, janela.caixas, janela.avisos, janela.commit_var = marcas, caixas, avisos, commit_var
    janela.botoes = {"Ensaio": b_ensaio, "Aplicar": b_aplicar, "Parar": b_parar, "Testar": b_testar}
    janela.tabela, janela.relatorio_texto, janela.tabela_notion, janela.mensagem = tabela, relatorio, tabela_notion, mensagem
    janela.atualizar_estado = atualizar_estado
    return janela


def abrir():
    """Abre a janela e fica nela até fechar. Devolve o código de saída (1 se o tkinter não existir)."""
    try:
        import tkinter as tk
        from tkinter import messagebox, ttk
    except ImportError:
        print(MENSAGEM_SEM_TK)
        return 1
    fontes.preparar()                                        # antes de criar a janela: registra as fontes do projeto
    janela = tk.Tk()
    janela.fontes = fontes.aplicar(janela, ttk.Style(janela))
    montar(janela, tk, ttk, messagebox)
    janela.mainloop()
    return 0
