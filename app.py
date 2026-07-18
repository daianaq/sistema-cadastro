import customtkinter as ctk
from tkinter import messagebox

# ==========================================
# Configurações
# ==========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

LARGURA = 650
ALTURA = 675

# ==========================================
# Janela
# ==========================================

app = ctk.CTk()
app.title("Sistema de Cadastro")
app.geometry(f"{LARGURA}x{ALTURA}")
app.resizable(False, False)

app.iconbitmap("assets/icon_form.ico")

# ==========================================
# Funções
# ==========================================

def verificar_login():

    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == "admin" and senha == "4321":

        frame_login.pack_forget()
        frame_cadastro.pack(fill="both", expand=True)

        entrada_nome.focus()

    else:

        messagebox.showerror(
            "Erro",
            "Usuário ou senha incorretos."
        )


def enviar_cadastro():

    messagebox.showinfo(
        "Cadastro",
        "Cadastro realizado com sucesso!"
    )

# ==========================================
# Frame Login
# ==========================================

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

# Enter faz login

app.bind("<Return>", lambda event: verificar_login())

# ==========================================
# Frame Cadastro
# ==========================================

frame_cadastro = ctk.CTkFrame(app)

titulo_cadastro = ctk.CTkLabel(
    frame_cadastro,
    text="Cadastro de Colaborador",
    font=("Arial", 28, "bold")
)
titulo_cadastro.pack(pady=(25, 15))

subtitulo_cadastro = ctk.CTkLabel(
    frame_cadastro,
    text="Preencha as informações abaixo para realizar o cadastro.",
    font=("Arial", 14),
    text_color="gray70"
)
subtitulo_cadastro.pack(pady=(0, 25))

# ==========================================
# Nome
# ==========================================

label_nome = ctk.CTkLabel(
    frame_cadastro,
    text="Nome Completo"
)
label_nome.pack(anchor="w", padx=70)

entrada_nome = ctk.CTkEntry(
    frame_cadastro,
    width=500,
    placeholder_text="Digite seu nome completo"
)
entrada_nome.pack(pady=(0, 15))

# ==========================================
# E-mail
# ==========================================

label_email = ctk.CTkLabel(
    frame_cadastro,
    text="E-mail"
)
label_email.pack(anchor="w", padx=70)

entrada_email = ctk.CTkEntry(
    frame_cadastro,
    width=500,
    placeholder_text="exemplo@email.com"
)
entrada_email.pack(pady=(0, 15))

# ==========================================
# Telefone
# ==========================================

label_telefone = ctk.CTkLabel(
    frame_cadastro,
    text="Telefone"
)
label_telefone.pack(anchor="w", padx=70)

entrada_telefone = ctk.CTkEntry(
    frame_cadastro,
    width=500,
    placeholder_text="(71) 99999-9999"
)
entrada_telefone.pack(pady=(0, 15))

# ==========================================
# Cidade
# ==========================================

label_cidade = ctk.CTkLabel(
    frame_cadastro,
    text="Cidade"
)
label_cidade.pack(anchor="w", padx=70)

entrada_cidade = ctk.CTkEntry(
    frame_cadastro,
    width=500,
    placeholder_text="Salvador"
)
entrada_cidade.pack(pady=(0, 15))

# ==========================================
# Estado
# ==========================================

label_estado = ctk.CTkLabel(
    frame_cadastro,
    text="Estado"
)
label_estado.pack(anchor="w", padx=70)

combo_estado = ctk.CTkComboBox(
    frame_cadastro,
    width=500,
    values=[
        "AC", "AL", "AP", "AM", "BA", "CE", "DF",
        "ES", "GO", "MA", "MT", "MS", "MG",
        "PA", "PB", "PR", "PE", "PI", "RJ",
        "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"
    ]
)

combo_estado.set("BA")
combo_estado.pack(pady=(0, 15))

# ==========================================
# Cargo
# ==========================================

label_cargo = ctk.CTkLabel(
    frame_cadastro,
    text="Cargo"
)
label_cargo.pack(anchor="w", padx=70)

entrada_cargo = ctk.CTkEntry(
    frame_cadastro,
    width=500,
    placeholder_text="Desenvolvedor de Software"
)
entrada_cargo.pack(pady=(0, 15))

# ==========================================
# Empresa
# ==========================================

label_empresa = ctk.CTkLabel(
    frame_cadastro,
    text="Empresa"
)
label_empresa.pack(anchor="w", padx=70)

entrada_empresa = ctk.CTkEntry(
    frame_cadastro,
    width=500,
    placeholder_text="Nome da empresa (opcional)"
)
entrada_empresa.pack(pady=(0, 25))

# ==========================================
# Botão
# ==========================================

botao_enviar = ctk.CTkButton(
    frame_cadastro,
    text="Enviar Cadastro",
    width=220,
    height=55,
    font=("Arial", 16, "bold"),
    command=enviar_cadastro
)

botao_enviar.pack(pady=(0, 10))

# ==========================================
# Rodapé
# ==========================================

rodape = ctk.CTkLabel(
    frame_cadastro,
    text="Versão 1.0 • Projeto de estudos",
    font=("Arial", 11),
    text_color="gray60"
)
rodape.pack(pady=(0, 15))

# ==========================================
# Inicialização
# ==========================================

entrada_usuario.focus()

app.mainloop()