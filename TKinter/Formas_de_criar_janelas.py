import tkinter as tk


class ExemploJanelas:
    def sobre (self):
        segunda_janela = tk.Toplevel(self.janela)
        segunda_janela.title("Sobre")
        segunda_janela.geometry("200x100")

    def janela_extra(self):
        import pathlib
        import os
        path = pathlib.Path(__file__).parent.absolute()
        os.system(fr"{path}\\Exemplo_ttk.py")

    def janela_extra_2(self):
        import batalha_naval
        batalha_naval.BatalhaNavalSimulator()
