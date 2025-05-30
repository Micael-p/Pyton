import tkinter as tk
from tkinter import messagebox
from bd import BancoDeDados
from cadastro import Cadastro
from datetime import datetime
from admteste import mostrar_usuarios

# Iniciar banco de dados
bd = BancoDeDados()
bd.conectar()
bd.criar_tabelas()

# Janela principal
root = tk.Tk()
root.title("Sistema de Login")
root.configure(bg="gray")
root.geometry("300x300")
# Criar barra de menu
menu_bar = tk.Menu(root)

# Menu "Arquivo"
menu_arquivo = tk.Menu(menu_bar, tearoff=0)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=root.quit)
menu_bar.add_cascade(label="1", menu=menu_arquivo)

# Menu "Ajuda"
menu_ajuda = tk.Menu(menu_bar, tearoff=0)
menu_ajuda.add_command(label="Sobre", command=lambda: messagebox.showinfo("Sobre", "Sistema de Login v1.0"))
menu_bar.add_cascade(label="2", menu=menu_ajuda)

# Associar a barra de menu à janela
root.config(menu=menu_bar)


def mostrar_dados_usuario(dados):
    nome, cpf, bloco, numero_ap, email = dados

    janela_dados = tk.Toplevel(root)
    janela_dados.title("Dados do Usuário")
    janela_dados.geometry("400x350")
    janela_dados.configure(bg="#f0f8ff")

    tk.Label(janela_dados, text="Informações do Usuário", font=("Helvetica", 14, "bold"), bg="#f0f8ff").pack(pady=10)

    for info in [
        f"Nome: {nome}",
        f"CPF: {cpf}",
        f"Bloco: {bloco}",
        f"Apartamento: {numero_ap}",
        f"Email: {email}"
    ]:
        tk.Label(janela_dados, text=info, anchor="w", justify="left", bg="#f0f8ff").pack(fill="x", padx=15, pady=4)

    tk.Button(janela_dados, text="Editar Dados", command=lambda: abrir_edicao_usuario((nome, cpf, bloco, numero_ap, email))).pack(pady=10)
    tk.Button(janela_dados, text="Excluir Conta", fg="red", command=lambda: excluir_usuario(cpf, janela_dados)).pack(pady=5)


def abrir_edicao_usuario(dados):
    nome_atual, cpf, bloco_atual, ap_atual, email_atual = dados

    janela_edicao = tk.Toplevel(root)
    janela_edicao.title("Editar Dados")
    janela_edicao.geometry("350x400")

    tk.Label(janela_edicao, text="Editar Informações", font=("Helvetica", 14, "bold")).pack(pady=10)

    # Campos para edição
    tk.Label(janela_edicao, text="Nome").pack()
    entry_nome = tk.Entry(janela_edicao)
    entry_nome.insert(0, nome_atual)
    entry_nome.pack()

    tk.Label(janela_edicao, text="Bloco").pack()
    entry_bloco = tk.Entry(janela_edicao)
    entry_bloco.insert(0, str(bloco_atual))
    entry_bloco.pack()

    tk.Label(janela_edicao, text="Número do AP").pack()
    entry_ap = tk.Entry(janela_edicao)
    entry_ap.insert(0, str(ap_atual))
    entry_ap.pack()

    tk.Label(janela_edicao, text="Email").pack()
    entry_email = tk.Entry(janela_edicao)
    entry_email.insert(0, email_atual)
    entry_email.pack()

    def salvar_alteracoes():
        novo_nome = entry_nome.get()
        novo_bloco = entry_bloco.get()
        novo_ap = entry_ap.get()
        novo_email = entry_email.get()

        try:
            cursor = bd.conn.cursor()
            cursor.execute("""
                UPDATE Pessoa SET nome = ?, bloco = ?, numeroAp = ?, email = ?
                WHERE cpf = ?
            """, (novo_nome, int(novo_bloco), int(novo_ap), novo_email, cpf))
            bd.conn.commit()
            messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
            janela_edicao.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar dados: {e}")

    tk.Button(janela_edicao, text="Salvar Alterações", command=salvar_alteracoes).pack(pady=10)

def excluir_usuario(cpf, janela):
    resposta = messagebox.askyesno("Confirmar Exclusão", "Tem certeza de que deseja excluir sua conta? Essa ação não poderá ser desfeita.")
    if resposta:
        try:
            cursor = bd.conn.cursor()
            cursor.execute("DELETE FROM Pessoa WHERE cpf = ?", (cpf,))
            bd.conn.commit()
            messagebox.showinfo("Conta Excluída", "Sua conta foi excluída com sucesso.")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir conta: {e}")

def fazer_login():
    login = entry_login.get()
    senha = entry_senha.get()
    if bd.conn:
        cursor = bd.conn.cursor()

        # Verifica login como ADM
        cursor.execute("SELECT nome, cpf FROM Adm WHERE login = ? AND senha = ?", (login, senha))
        dados = cursor.fetchone()
        if dados:
            nome_adm, cpf_adm = dados
            messagebox.showinfo("Sucesso", "Login de administrador bem-sucedido!")
            mostrar_usuarios(nome_adm=nome_adm, cpf_adm=cpf_adm)
            return

        # Verifica login como usuário
        cursor.execute("SELECT nome, cpf, bloco, numeroAp, email FROM Pessoa WHERE login = ? AND senha = ?", (login, senha))
        dados = cursor.fetchone()
        if dados:
            messagebox.showinfo("Sucesso", "Login de usuário bem-sucedido!")
            mostrar_dados_usuario(dados)
            return

        messagebox.showerror("Erro", "Login ou senha inválidos.")

def abrir_cadastro():
    cadastro_window = tk.Toplevel(root)
    cadastro_window.title("Cadastro")
    cadastro_window.geometry("350x400")

    def cadastrar():
        try:
            pessoa = Cadastro(
                cpf=entry_cpf.get(),
                login=entry_login_cad.get(),
                nome=entry_nome.get(),
                senha=entry_senha_cad.get(),
                bloco=int(entry_bloco.get()),
                numeroAp=int(entry_ap.get()),
                email=entry_email.get(),
                data_cadastro=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            bd.inserir_pessoa(pessoa)
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            cadastro_window.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

    # Campos de cadastro
    tk.Label(cadastro_window, text="CPF").pack()
    entry_cpf = tk.Entry(cadastro_window)
    entry_cpf.pack()

    tk.Label(cadastro_window, text="Login").pack()
    entry_login_cad = tk.Entry(cadastro_window)
    entry_login_cad.pack()

    tk.Label(cadastro_window, text="Nome").pack()
    entry_nome = tk.Entry(cadastro_window)
    entry_nome.pack()

    tk.Label(cadastro_window, text="Senha").pack()
    entry_senha_cad = tk.Entry(cadastro_window, show="*")
    entry_senha_cad.pack()

    tk.Label(cadastro_window, text="Bloco").pack()
    entry_bloco = tk.Entry(cadastro_window)
    entry_bloco.pack()

    tk.Label(cadastro_window, text="Número do AP").pack()
    entry_ap = tk.Entry(cadastro_window)
    entry_ap.pack()

    tk.Label(cadastro_window, text="Email").pack()
    entry_email = tk.Entry(cadastro_window)
    entry_email.pack()

    tk.Button(cadastro_window, text="Cadastrar", command=cadastrar).pack(pady=10)

# Tela de login
tk.Label(root, text="Login", bg="gray").pack()
entry_login = tk.Entry(root)
entry_login.pack()

tk.Label(root, text="Senha", bg="gray").pack()
entry_senha = tk.Entry(root, show="*")
entry_senha.pack()

tk.Button(root, text="Entrar", command=fazer_login).pack(pady=10)
tk.Button(root, text="Fazer Cadastro", command=abrir_cadastro).pack()

root.mainloop()
