import customtkinter as ctk
from utils.json_manager import carregar_json
from tkinter import messagebox as mg


class Login(ctk.CTkFrame):

    def __init__(self,master, abrir_sistema):
        super().__init__(master)
        self.abrir_sistema = abrir_sistema

        self.entry_usuario = ctk.CTkEntry(self, placeholder_text="Usuário")
        self.entry_usuario.pack(pady=10)

        self.entry_senha = ctk.CTkEntry(self, placeholder_text="Senha", show="*")
        self.entry_senha.pack(pady=10)

        self.botao = ctk.CTkButton(self, text="Entrar", command=self.verificar_login)
        self.botao.pack(pady=20)

    def verificar_login(self):

        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        usuarios = carregar_json("dados/usuarios.json")
        if not usuario or not senha:
            mg.showerror("Erro", "Preencha usuário e senha")
            return

        for u in usuarios:
            if u["usuario"] == usuario and u["senha"] == senha:
                mg.showinfo("Login Invalido", f"Bem-Vindo(a) de Volta: {u['usuario']}")
                self.destroy()
                self.abrir_sistema(u)
                return
        mg.showerror("Erro", "Usuário ou senha inválidos!")
        