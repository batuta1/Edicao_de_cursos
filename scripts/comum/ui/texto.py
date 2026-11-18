"""Área de texto somente leitura (regra da skill `interface-tkinter`: áreas de visualização não aceitam digitação)."""


def criar_area_leitura(tk, pai, **opcoes):
    """Cria um `tk.Text` monoespaçado somente leitura. O usuário ainda consegue selecionar e copiar (clicar dá o foco).

    `tk` é o módulo `tkinter` (passado por quem chama, para este arquivo não importar a biblioteca antes da hora).
    """
    area = tk.Text(pai, font="TkFixedFont", state="disabled", **opcoes)
    area.bind("<Button-1>", lambda _e: area.focus_set())
    return area


def escrever(area, texto):
    """Troca o conteúdo de uma área somente leitura e a deixa bloqueada de novo."""
    area.configure(state="normal")
    area.delete("1.0", "end")
    area.insert("end", texto)
    area.configure(state="disabled")
