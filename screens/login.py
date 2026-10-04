import customtkinter as ctk
from tkinter import messagebox

# ==========================================
# Tela de Login
# ==========================================

# verifica as credenciais
def criar_tela_login(app, tela_cadastro):

    def verificar_login():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()

        if usuario == "admin" and senha == "4321":
            frame_login.pack_forget()
            tela_cadastro()
        else:
            messagebox.showerror(
                "Erro",
                "Usuário ou senha incorretos."
            )
    # container do login
    frame_login = ctk.CTkFrame(app)

    frame_login.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=30
    )

    titulo_login = ctk.CTkLabel(
        frame_login,
        text="Sistema de Cadastro",
        font=("Arial", 30, "bold")
    )

    titulo_login.pack(pady=(30, 40))

    label_usuario = ctk.CTkLabel(
        frame_login,
        text="Usuário",
        font=("Arial", 18, "bold")
    )

    label_usuario.pack()

    entrada_usuario = ctk.CTkEntry(
        frame_login,
        width=300,
        height=40,
        placeholder_text="Usuário"
    )

    entrada_usuario.pack(pady=10)

    label_senha = ctk.CTkLabel(
        frame_login,
        text="Senha",
        font=("Arial", 18, "bold")
    )

    label_senha.pack(pady=(20, 0))

    entrada_senha = ctk.CTkEntry(
        frame_login,
        width=300,
        height=40,
        show="*",
        placeholder_text="Senha"
    )

    entrada_senha.pack(pady=10)

    botao_login = ctk.CTkButton(
        frame_login,
        text="Acessar",
        width=120,
        height=45,
        font=("Arial", 16, "bold"),
        command=verificar_login
    )

    botao_login.pack(pady=40)

    app.bind("<Return>", lambda event: verificar_login())

    return frame_login