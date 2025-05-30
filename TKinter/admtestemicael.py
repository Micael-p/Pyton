import tkinter as tk
from tkinter import messagebox
from bd import BancoDeDados
from cadastro import Cadastro_adm
from datetime import datetime



# Iniciar banco de dados
bd = BancoDeDados()
bd.conectar()
bd.criar_tabelas()

# Janela principal


def excluir_usuario_adm(cpf, frame):
    confirm = messagebox.askyesno("Confirmar Exclusão", f"Deseja realmente excluir o usuário com CPF {cpf}?")
    if confirm:
        try:
            cursor = bd.conn.cursor()
            cursor.execute("DELETE FROM Pessoa WHERE cpf = ?", (cpf,))
            bd.conn.commit()
            messagebox.showinfo("Sucesso", "Usuário excluído com sucesso.")
            frame.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir usuário: {e}")

def mostrar_usuarios(nome_adm=None, cpf_adm=None):
    if bd.conn:
        try:
            cursor = bd.conn.cursor()
            cursor.execute("SELECT nome, cpf, bloco, numeroAp, email, data_cadastro FROM Pessoa")
            usuarios = cursor.fetchall()

            janela_usuarios = tk.Toplevel()
            janela_usuarios.title("Usuários Cadastrados")
            janela_usuarios.geometry("650x550")

            tk.Label(janela_usuarios, text="Lista de Usuários", font=("Helvetica", 14, "bold")).pack(pady=10)

            for usuario in usuarios:
                nome, cpf, bloco, numeroAp, email, data_cadastro = usuario
                frame = tk.Frame(janela_usuarios, borderwidth=1, relief="solid")
                frame.pack(padx=10, pady=5, fill="x")

                info = f"Nome: {nome} | CPF: {cpf} | Bloco: {bloco} | Ap: {numeroAp} | Email: {email} | Cadastro: {data_cadastro}"
                tk.Label(frame, text=info, anchor="w", justify="left").pack(side="left", padx=5)

                def excluir_usuario(cpf_local=cpf, frame_local=frame):
                    if messagebox.askyesno("Confirmar", f"Deseja excluir o usuário de CPF {cpf_local}?"):
                        cursor.execute("DELETE FROM Pessoa WHERE cpf = ?", (cpf_local,))
                        bd.conn.commit()
                        frame_local.destroy()
                        messagebox.showinfo("Sucesso", "Usuário excluído.")

                tk.Button(frame, text="Excluir", fg="red", command=excluir_usuario).pack(side="right", padx=5)

                def editar_usuario(
                        cpf_local=cpf, nome_local=nome, bloco_local=bloco,
                        ap_local=numeroAp, email_local=email, login_local=""
                ):
                    cursor.execute("SELECT login FROM Pessoa WHERE cpf = ?", (cpf_local,))
                    login_result = cursor.fetchone()
                    login_local = login_result[0] if login_result else ""

                    janela_editar = tk.Toplevel(janela_usuarios)
                    janela_editar.title(f"Editar: {nome_local}")
                    janela_editar.geometry("350x450")

                    tk.Label(janela_editar, text="Nome").pack()
                    entry_nome = tk.Entry(janela_editar)
                    entry_nome.insert(0, nome_local)
                    entry_nome.pack()

                    tk.Label(janela_editar, text="Login").pack()
                    entry_login = tk.Entry(janela_editar)
                    entry_login.insert(0, login_local)
                    entry_login.pack()

                    tk.Label(janela_editar, text="Senha").pack()
                    entry_senha = tk.Entry(janela_editar, show="*")
                    entry_senha.pack()

                    tk.Label(janela_editar, text="Bloco").pack()
                    entry_bloco = tk.Entry(janela_editar)
                    entry_bloco.insert(0, bloco_local)
                    entry_bloco.pack()

                    tk.Label(janela_editar, text="Número do AP").pack()
                    entry_ap = tk.Entry(janela_editar)
                    entry_ap.insert(0, ap_local)
                    entry_ap.pack()

                    tk.Label(janela_editar, text="Email").pack()
                    entry_email = tk.Entry(janela_editar)
                    entry_email.insert(0, email_local)
                    entry_email.pack()

                    def salvar_edicao():
                        novo_nome = entry_nome.get()
                        novo_login = entry_login.get()
                        nova_senha = entry_senha.get()
                        novo_bloco = entry_bloco.get()
                        novo_ap = entry_ap.get()
                        novo_email = entry_email.get()

                        try:
                            # Atualiza os dados no banco
                            cursor.execute("""
                                UPDATE Pessoa
                                SET nome = ?, login = ?, senha = ?, bloco = ?, numeroAp = ?, email = ?
                                WHERE cpf = ?
                            """, (
                                novo_nome, novo_login, nova_senha,
                                int(novo_bloco), int(novo_ap), novo_email, cpf_local
                            ))
                            bd.conn.commit()
                            messagebox.showinfo("Sucesso", "Dados do usuário atualizados.")
                            janela_editar.destroy()
                        except Exception as e:
                            messagebox.showerror("Erro", f"Erro ao atualizar: {e}")

                    tk.Button(janela_editar, text="Salvar Alterações", command=salvar_edicao).pack(pady=10)

                tk.Button(frame, text="Editar", fg="blue", command=editar_usuario).pack(side="right", padx=5)

            # ADM - editar os próprios dados
            def editar_adm():
                janela_editar = tk.Toplevel(janela_usuarios)
                janela_editar.title("Editar Dados do Administrador")
                janela_editar.geometry("350x300")

                tk.Label(janela_editar, text="Editar Nome").pack()
                entry_nome = tk.Entry(janela_editar)
                entry_nome.insert(0, nome_adm)
                entry_nome.pack()

                tk.Label(janela_editar, text="Editar Senha").pack()
                entry_senha = tk.Entry(janela_editar, show="*")
                entry_senha.pack()

                def salvar_edicao():
                    novo_nome = entry_nome.get()
                    nova_senha = entry_senha.get()

                    cursor.execute("UPDATE Adm SET nome = ?, senha = ? WHERE cpf = ?", (novo_nome, nova_senha, cpf_adm))
                    bd.conn.commit()
                    messagebox.showinfo("Sucesso", "Dados atualizados.")

                tk.Button(janela_editar, text="Salvar", command=salvar_edicao).pack(pady=10)

            tk.Button(janela_usuarios, text="Editar Meus Dados", command=editar_adm).pack(pady=10)

            # Cadastro de novo ADM
            def abrir_cadastro_adm():
                cadastro_window = tk.Toplevel(janela_usuarios)
                cadastro_window.title("Cadastro de ADM")
                cadastro_window.geometry("350x300")

                def cadastrar():
                    try:
                        pessoa = Cadastro_adm(
                            cpf=entry_cpf.get(),
                            login=entry_login_cad.get(),
                            nome=entry_nome.get(),
                            senha=entry_senha_cad.get(),
                            data_cadastro=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        )
                        bd.inserir_adm(pessoa)
                        messagebox.showinfo("Sucesso", "Administrador cadastrado com sucesso!")
                        cadastro_window.destroy()
                    except Exception as e:
                        messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

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

                tk.Button(cadastro_window, text="Cadastrar", command=cadastrar).pack(pady=10)

            tk.Button(janela_usuarios, text="Cadastrar novo ADM", command=abrir_cadastro_adm).pack(pady=10)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar usuários: {e}")


