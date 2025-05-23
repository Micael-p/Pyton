import tkinter as tk

class ExemploSMenu:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Menu")
        self.janela.geometry("300x200")
        self.janela.config(bg="white")
        menubar = tk.Menu(self.janela)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Novo")
        filemenu.add_command(label="Abrir")
        filemenu.add_command(label="Fechar")
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=self.sair)

        menubar.add_cascade(label="Arquivo", menu=filemenu)
        self.janela.config(menu=menubar)
        menu_ajuda= tk.Menu(menubar, tearoff=0)
        menu_ajuda.add_command(label="Bem vindo")
        menu_ajuda.add_command(label="Sobre")
        menubar.add_cascade(label="Ajuda", menu=menu_ajuda)


        sorvetemenu = tk.Menu(menubar, tearoff=0)
        sorvetemenu.add_command(label="Flocos")
        sorvetemenu.add_command(label="Morango")
        sorvetemenu.add_command(label="Chocolate")
        menubar.add_cascade(label="Sorvete", menu=sorvetemenu)


        self.janela.mainloop()
    def sair(self):
        self.janela.destroy()

if __name__ == "__main__":
    ExemploSMenu()
