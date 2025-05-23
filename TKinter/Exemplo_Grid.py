import tkinter as tk

class Exemplo_grid:
    def __init__(self):
        self.janela = tk.Tk()
        for i in range(3):
            self.janela.columnconfigure(i, weidth=1, minsize=75)
            self.janela.rowconfigure(i, weidth=1, minsize=50)
            for j in range(3):
                frame = tk.frame(master=self.janela, refief=tk.RAISED, borderwidth=1)
                frame.grid(row=i, column=j, padx=5, pady=5, sticky ="ne, sw")
                label = tk.label(master=frame, text=f"Linha {i}\nColuna {j}")
                label.pack()
        self.janela.mainloop()

if __name__ == "__main__":
    Exemplo_grid()
