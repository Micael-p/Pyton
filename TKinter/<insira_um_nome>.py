import tkinter as tk
from tkinter import ttk
class TreeviewExampleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo de Treview")

        #criar o treeview
        self.tree = ttk.Treeview(
            root, columns=("Nome", "Idade", "Profissão"), show="headings"
        )
        #definir os cabeçalhos das colunas
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Idade", text="Idade")
        self.tree.heading("Profissão", text="Profissão")

        #definir a largura das colunas
        self.tree.column("Nome", width=150)
        self.tree.column("Idade", width=80)
        self.tree.column("Profissão", width=150)

        #adicionar alguns dados
        self.tree.insert("", "end", values= ("Ana", 10, "Aluna"))
        self.tree.insert("", "end", values= ("Lucy", 20, "Psicologa"))
        self.tree.insert("", "end", values= ("Linda", 40, "Assistente"))

        #mostrar o Treeview na tela
        self.tree.pack(pady=20)

        #botao pra adicionar mais uma linha de exemplo
        self.bnt_add_row = tk.Button(
            root, text="Adicionar linha", command=self.adicionar_linha
        )

        self.bnt_add_row.pack(pady=10)

    def adicionar_linha(self):
        # exemplo de como adicionar uma nova linha ao Treeview
        self.tree.insert("", "end", values=("Gilson", 90, "Contador"))


if __name__ == "__main__":
    root = tk.Tk()
    app = TreeviewExampleApp(root)
    root.mainloop()
