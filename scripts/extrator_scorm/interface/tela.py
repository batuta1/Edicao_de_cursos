"""A tela. Duas abas: **Pasta de cursos** (a inicial: varre e extrai tudo) e **Individual** (um pacote por vez, como no MVP1).

Individual: escolher o pacote pelo explorador ou arrastando; mostra o JSON; grava em extrator_scorm/fichas/_individuais/ sem perguntar.
Pasta: o caminho de `Edicao_de_cursos/Cursos` já vem preenchido; Varrer lista o que há; Extrair tudo roda o lote.
"""
import queue
import threading
from pathlib import Path

from .. import servico
from ..erros import ErroExtracao
from ..leitura import inventario
from ..lote import lote, varredura
from comum.ui import fontes, texto

from ..path import caminhos

MENSAGEM_SEM_TK = ("A tela precisa do tkinter, que não está instalado.\n"
                   "No Linux (Ubuntu/Debian): sudo apt install python3-tk\n"
                   "Enquanto isso, use a linha de comando: python -m extrator_scorm CAMINHO.zip  (ou python -m extrator_scorm PASTA)")

PASTA_PADRAO = caminhos.PASTA_CURSOS

SITUACAO = {"copiado": "cópia idêntica", "pulado": "sem mudança", "fora": "fora da seleção", "erro": "erro"}


def limpar_caminho(texto):
    """O caminho que vem do arrastar pode vir entre chaves."""
    return Path(str(texto).strip().strip("{}"))


def situacao_do_pacote(p):
    """Texto da coluna Situação da tabela para um pacote do relatório do lote."""
    if p["resultado"] == "extraido":
        return {"novo": "novo", "alterado": "alterado"}.get(p["status"], "extraído de novo")
    return SITUACAO[p["resultado"]]


class Controlador:
    """Modo individual, sem nenhum widget (testável sem janela)."""

    def __init__(self):
        self.caminho = None
        self.resultado = None

    def carregar(self, caminho):
        """Extrai o pacote (zip ou pasta SCORM) e devolve o JSON como texto, para mostrar. Erros viram ErroExtracao."""
        caminho = limpar_caminho(caminho)
        self.resultado = servico.extrair(caminho)
        self.caminho = caminho
        return servico.para_texto(self.resultado)

    def gravar(self):
        """Grava em fichas/_individuais/, sem perguntar onde: o mesmo arquivo que a linha de comando gravaria."""
        if self.resultado is None:
            raise ErroExtracao("Escolha um pacote antes de gravar.")
        return servico.gravar(self.resultado, self.caminho)


class ControladorPasta:
    """Modo pasta, sem nenhum widget: o que a tela chama e a linha de comando também usa (varredura e lote)."""

    def __init__(self, pasta=None, pasta_padrao=None):
        padrao = Path(pasta_padrao) if pasta_padrao else PASTA_PADRAO
        self.aviso = None
        if pasta:
            self.pasta = str(limpar_caminho(pasta))
        elif padrao.is_dir():
            self.pasta = str(padrao)
        else:
            self.pasta = ""
            self.aviso = f"A pasta padrão não existe: {padrao}. Escolha a pasta de cursos."
        self.varredura = None
        self.relatorio = None

    def definir_pasta(self, texto):
        """Troca a pasta de cursos e descarta a varredura e o relatório anteriores."""
        self.pasta = str(limpar_caminho(texto)) if str(texto).strip() else ""
        self.varredura = self.relatorio = None

    def _exigir_pasta(self):
        """A pasta de cursos como `Path`; erro se nenhuma foi escolhida."""
        if not self.pasta:
            raise ErroExtracao("Escolha a pasta de cursos.")
        return Path(self.pasta)

    def varrer(self):
        """Só lista (não grava nada). Devolve as linhas (empresa, curso, versão, tipo, situação, caminho)."""
        self.varredura = varredura.varrer(self._exigir_pasta())
        self.relatorio = None
        return [(p["empresa"] or "", p["curso"] or "", p["versao"] or "", p["tipo"], "cópia" if p["copia"] else "", p["caminho"])
                for p in self.varredura["pacotes"]]

    def texto_da_varredura(self):
        """Texto da última varredura, para a área de relatório."""
        return varredura.texto_da_varredura(self.varredura)

    def extrair_tudo(self, progresso=None, cancelar=None, forcar=False, so_ultimas=False):
        """Roda o lote (o mesmo da linha de comando) e devolve o relatório."""
        self.relatorio = lote.executar(self._exigir_pasta(), forcar=forcar, progresso=progresso, cancelar=cancelar, so_ultimas=so_ultimas)
        return self.relatorio

    def linhas_do_relatorio(self):
        """Linhas da tabela (empresa, curso, versão, tipo, situação, caminho) do último lote."""
        return [(p["empresa"] or "", p["curso"] or "", p["versao"] or "", p["tipo"], situacao_do_pacote(p), p["caminho"])
                for p in self.relatorio["pacotes"]]

    def texto_do_relatorio(self):
        """Texto do relatório do último lote, para a área de relatório."""
        return lote.texto_do_relatorio(self.relatorio)


def eh_pasta_de_cursos(caminho):
    """Uma pasta que não é, ela mesma, um pacote SCORM."""
    caminho = Path(caminho)
    return caminho.is_dir() and not any(f.name.lower() == inventario.MANIFESTO for f in caminho.iterdir())


def abrir(pasta=None):
    """Abre a janela do extrator e fica nela até fechar. Devolve 0, ou 1 se o tkinter não existir."""
    try:
        import tkinter as tk
        from tkinter import filedialog, messagebox, ttk
    except ImportError:
        print(MENSAGEM_SEM_TK)
        return 1
    fontes.preparar()                                       # antes de abrir a janela: registra as fontes do projeto no fontconfig
    try:                                                    # arrastar: dependência autorizada (D01-9)
        from tkinterdnd2 import DND_FILES, TkinterDnD
        janela = TkinterDnD.Tk()
        arrastar = True
    except Exception:                                       # sem a biblioteca ou sem suporte no ambiente
        janela = tk.Tk()
        DND_FILES, arrastar = None, False

    janela.fontes = fontes.aplicar(janela, ttk.Style(janela))     # gancho para o teste da janela
    janela.title("Extrator de informações de SCORM")
    janela.geometry("1150x760")
    abas = ttk.Notebook(janela)
    abas.pack(fill="both", expand=True)
    aba_pasta, aba_individual = ttk.Frame(abas), ttk.Frame(abas)
    abas.add(aba_pasta, text="Pasta de cursos")
    abas.add(aba_individual, text="Individual")
    janela.aba_pasta, janela.aba_individual, janela.abas = aba_pasta, aba_individual, abas      # ganchos para o teste da janela

    # ------------------------------------------------------------------ modo pasta
    ctl_pasta = ControladorPasta(pasta)
    janela.ctl_pasta = ctl_pasta
    pasta_var, status_pasta = tk.StringVar(value=ctl_pasta.pasta), tk.StringVar()
    forcar_var, ultimas_var = tk.BooleanVar(value=False), tk.BooleanVar(value=False)
    status_pasta.set(ctl_pasta.aviso or "Confira a pasta e clique em Varrer (só lista) ou em Extrair tudo.")
    estado = {"rodando": False, "parar": threading.Event()}

    topo = ttk.Frame(aba_pasta, padding=8)
    topo.pack(fill="x")
    ttk.Label(topo, text="Pasta de cursos:").pack(side="left")
    ttk.Entry(topo, textvariable=pasta_var, width=60).pack(side="left", padx=4, fill="x", expand=True)
    botoes = ttk.Frame(aba_pasta, padding=(8, 0))
    botoes.pack(fill="x")

    colunas = ("empresa", "curso", "versao", "tipo", "situacao", "caminho")
    cabecalhos = ("Empresa", "Curso", "Versão", "Tipo", "Situação", "Caminho")
    larguras = (100, 270, 60, 60, 150, 420)
    quadro = ttk.Frame(aba_pasta)
    tabela = ttk.Treeview(quadro, columns=colunas, show="headings", height=14)
    for c, t, w in zip(colunas, cabecalhos, larguras):
        tabela.heading(c, text=t)
        tabela.column(c, width=w, anchor="w")
    for situacao, cor in (("novo", "#1a7f37"), ("alterado", "#b35900"), ("cópia idêntica", "#6e7781"), ("fora da seleção", "#6e7781"), ("erro", "#cf222e")):
        tabela.tag_configure(situacao, foreground=cor)
    rolagem = ttk.Scrollbar(quadro, orient="vertical", command=tabela.yview)
    tabela.configure(yscrollcommand=rolagem.set)
    andamento = ttk.Progressbar(aba_pasta, mode="determinate")
    quadro_relatorio = ttk.Frame(aba_pasta)
    relatorio = texto.criar_area_leitura(tk, quadro_relatorio, height=10, wrap="word")
    barra_relatorio = ttk.Scrollbar(quadro_relatorio, orient="vertical", command=relatorio.yview)
    relatorio.configure(yscrollcommand=barra_relatorio.set)

    def mostrar_linhas(linhas):
        """Preenche a tabela de pacotes; a coluna Situação vira a etiqueta da linha."""
        tabela.delete(*tabela.get_children())
        for linha in linhas:
            tabela.insert("", "end", values=linha, tags=(linha[4],))

    def mostrar_texto(linhas):
        """Mostra um texto (lista de linhas) na área de relatório somente leitura."""
        texto.escrever(relatorio, "\n".join(linhas))

    def ler_pasta():
        """Passa o caminho digitado na janela para o controlador."""
        ctl_pasta.pasta = str(limpar_caminho(pasta_var.get())) if pasta_var.get().strip() else ""

    def escolher_pasta():
        """Botão Escolher pasta: abre o seletor de pastas."""
        c = filedialog.askdirectory(title="Escolher a pasta de cursos", initialdir=ctl_pasta.pasta or None)
        if c:
            pasta_var.set(c)

    def varrer():
        """Botão Varrer: lista os pacotes da pasta, sem gravar nada."""
        if estado["rodando"]:
            return
        ler_pasta()
        try:
            mostrar_linhas(ctl_pasta.varrer())
            mostrar_texto(ctl_pasta.texto_da_varredura())
            status_pasta.set(f"Varredura pronta: {len(ctl_pasta.varredura['pacotes'])} pacotes. Nada foi gravado. Clique em Extrair tudo para ler.")
        except ErroExtracao as e:
            messagebox.showerror("Erro", str(e))
            status_pasta.set(f"Erro: {e}")

    def definir_rodando(rodando):
        """Liga ou desliga os botões conforme haja ou não um lote em andamento."""
        estado["rodando"] = rodando
        for b in (b_varrer, b_extrair, b_escolher):
            b.configure(state="disabled" if rodando else "normal")
        b_parar.configure(state="normal" if rodando else "disabled")

    def terminou(rel):
        """Mostra o resultado do lote (tabela, relatório e mensagem de estado) quando ele acaba."""
        definir_rodando(False)
        andamento.configure(value=0)
        if rel.get("sem_pacotes"):
            status_pasta.set("Nenhum pacote SCORM nessa pasta. Nada foi gravado.")
        elif rel["interrompido"]:
            status_pasta.set("Interrompido. O controle e o resumo não foram gravados.")
        else:
            mostrar_linhas(ctl_pasta.linhas_do_relatorio())
            status_pasta.set(f"Pronto. Fichas das últimas versões (um JSON só): {rel['arquivos']['ultimas']}")
        mostrar_texto(ctl_pasta.texto_do_relatorio())

    def sondar(fila):
        """Chamada a cada 100 ms durante o lote: passa as mensagens da thread para a janela."""
        try:
            while True:
                tipo, dado = fila.get_nowait()
                if tipo == "andamento":
                    etapa, atual, total, caminho = dado
                    andamento.configure(maximum=max(total, 1), value=atual)
                    status_pasta.set(f"{etapa}: pacote {atual} de {total} ({caminho})")
                elif tipo == "fim":
                    return terminou(dado)
                else:
                    definir_rodando(False)
                    messagebox.showerror("Erro", dado)
                    status_pasta.set(f"Erro: {dado}")
                    return
        except queue.Empty:
            janela.after(100, sondar, fila)

    def extrair_tudo():
        """Botão Extrair tudo: roda o lote numa thread, com progresso por fila."""
        if estado["rodando"]:
            return
        ler_pasta()
        fila, estado["parar"] = queue.Queue(), threading.Event()
        parar, forcar, so_ultimas = estado["parar"], bool(forcar_var.get()), bool(ultimas_var.get())
        if not ctl_pasta.pasta:
            messagebox.showerror("Erro", "Escolha a pasta de cursos.")
            return

        def trabalho():
            """Roda o lote fora da thread da janela e devolve o relatório pela fila."""
            try:
                fila.put(("fim", ctl_pasta.extrair_tudo(lambda *a: fila.put(("andamento", a)), parar.is_set, forcar, so_ultimas)))
            except ErroExtracao as e:
                fila.put(("erro", str(e)))
            except Exception as e:                           # nada pode deixar a janela esperando para sempre
                fila.put(("erro", f"erro inesperado ({type(e).__name__}): {e}"))

        definir_rodando(True)
        threading.Thread(target=trabalho, daemon=True).start()
        janela.after(100, sondar, fila)

    def parar():
        """Botão Parar: o lote termina depois do pacote atual."""
        estado["parar"].set()
        status_pasta.set("Parando depois do pacote atual...")

    b_escolher = ttk.Button(topo, text="Escolher pasta...", command=escolher_pasta)
    b_escolher.pack(side="left", padx=2)
    b_varrer = ttk.Button(botoes, text="Varrer", command=varrer)
    b_varrer.pack(side="left", padx=2)
    b_extrair = ttk.Button(botoes, text="Extrair tudo", command=extrair_tudo)
    b_extrair.pack(side="left", padx=2)
    b_parar = ttk.Button(botoes, text="Parar", command=parar, state="disabled")
    b_parar.pack(side="left", padx=2)
    c_ultimas = ttk.Checkbutton(botoes, text="Só as últimas versões", variable=ultimas_var)
    c_ultimas.pack(side="left", padx=12)
    ttk.Checkbutton(botoes, text="Forçar (extrair tudo de novo)", variable=forcar_var).pack(side="left", padx=4)
    ttk.Label(aba_pasta, textvariable=status_pasta, padding=(8, 4)).pack(fill="x")
    andamento.pack(fill="x", padx=8)
    quadro.pack(fill="both", expand=True, padx=8, pady=6)
    rolagem.pack(side="right", fill="y")
    tabela.pack(side="left", fill="both", expand=True)
    quadro_relatorio.pack(fill="x", padx=8, pady=(0, 8))
    barra_relatorio.pack(side="right", fill="y")
    relatorio.pack(side="left", fill="x", expand=True)
    janela.tabela, janela.relatorio_texto, janela.botoes_pasta = tabela, relatorio, {
        "Varrer": b_varrer, "Extrair tudo": b_extrair, "Parar": b_parar}
    janela.so_ultimas_var, janela.forcar_var = ultimas_var, forcar_var

    # ------------------------------------------------------------------ modo individual
    ctl = Controlador()
    caminho = tk.StringVar()
    status = tk.StringVar(value="Escolha um .zip" + (" ou arraste-o para esta janela." if arrastar else ".")
                          + ("" if arrastar else " (Arrastar não está disponível neste ambiente.)"))

    topo_i = ttk.Frame(aba_individual, padding=8)
    topo_i.pack(fill="x")
    ttk.Label(topo_i, text="Pacote (.zip ou pasta):").pack(side="left")
    ttk.Entry(topo_i, textvariable=caminho, width=60).pack(side="left", padx=4, fill="x", expand=True)

    area = texto.criar_area_leitura(tk, aba_individual, wrap="none")
    barra_y = ttk.Scrollbar(aba_individual, orient="vertical", command=area.yview)
    area.configure(yscrollcommand=barra_y.set)
    janela.area_individual = area

    def mostrar(conteudo):
        """Mostra o JSON do pacote escolhido na área somente leitura."""
        texto.escrever(area, conteudo)

    def extrair(origem=None):
        """Extrai um pacote só (aba Individual) e mostra o JSON."""
        if origem is not None:
            caminho.set(str(origem))
        try:
            mostrar(ctl.carregar(caminho.get()))
            status.set(f"Extraído: {ctl.caminho.name}. Use \"Gravar JSON\" para salvar em fichas/_individuais/.")
        except ErroExtracao as e:
            ctl.resultado = None
            messagebox.showerror("Erro", str(e))
            status.set(f"Erro: {e}")

    def escolher():
        """Botão Escolher: seletor de arquivo `.zip` do SCORM."""
        c = filedialog.askopenfilename(title="Escolher o zip do SCORM", filetypes=[("Zip", "*.zip"), ("Todos", "*")])
        if c:
            extrair(c)

    def gravar():
        """Botão Gravar JSON: grava a ficha em `fichas/_individuais/`."""
        try:
            destino = ctl.gravar()
            status.set(f"Gravado em {destino}")
        except ErroExtracao as e:
            messagebox.showerror("Erro", str(e))

    ttk.Button(topo_i, text="Escolher...", command=escolher).pack(side="left", padx=2)
    ttk.Button(topo_i, text="Extrair", command=lambda: extrair()).pack(side="left", padx=2)
    ttk.Button(topo_i, text="Gravar JSON", command=gravar).pack(side="left", padx=2)
    ttk.Label(aba_individual, textvariable=status, padding=(8, 2)).pack(fill="x")
    barra_y.pack(side="right", fill="y")
    area.pack(fill="both", expand=True, padx=(8, 0), pady=8)

    if arrastar:
        def soltou(evento):
            """Arrastar e soltar: pasta de cursos vai para a aba da pasta; um pacote, para a aba Individual."""
            itens = janela.tk.splitlist(evento.data)
            if not itens:
                return
            if eh_pasta_de_cursos(limpar_caminho(itens[0])):  # uma pasta de cursos vai para a aba da pasta; um pacote, para a individual
                abas.select(aba_pasta)
                pasta_var.set(str(limpar_caminho(itens[0])))
                varrer()
            else:
                abas.select(aba_individual)
                extrair(itens[0])
        for alvo in (janela, area):
            alvo.drop_target_register(DND_FILES)
            alvo.dnd_bind("<<Drop>>", soltou)
        janela.ao_soltar = soltou                           # gancho para o teste da janela (não dá para simular o arrastar real)
    janela.mainloop()
    return 0
