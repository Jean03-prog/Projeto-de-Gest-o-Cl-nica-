import customtkinter as ctk

COR_ROXO = "#7c3aed"
COR_BRANCO ="#ffffff"
COR_CINZA = "#6b7280"
COR_CINZA_ESCURO = "#111827"

class TelaDetalhes(ctk.CTkFrame):

    def __init__(self, master, paciente, voltar_pacientes, novo_atendimento):
        super().__init__(master, fg_color=COR_BRANCO)
        self.paciente = paciente
        self.voltar_pacientes = voltar_pacientes
        self.novo_atendimento = novo_atendimento

        # frame principal
        self.frame_principal = ctk.CTkFrame(self, fg_color=COR_BRANCO)
        self.frame_principal.pack(fill="both", expand=True, padx=20, pady=20)
        # frame de ações
        self.frame_acoes = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_acoes.pack(fill="x", pady=(0,10))

        self.btn_voltar = ctk.CTkButton(
            self.frame_acoes,
            text="← Voltar",
            fg_color=COR_CINZA,
            command=self.voltar_pacientes)
        self.btn_voltar.pack(side="left")

        self.btn_novo_atendimento = ctk.CTkButton(
            self.frame_acoes,
            text="➕ Novo Atendimento",
            fg_color=COR_ROXO,
            command=self.novo_atendimento)
        self.btn_novo_atendimento.pack(side="right")
        # titulo
        self.titulo = ctk.CTkLabel(
            self.frame_principal,
            text=f"Detalhes - {paciente['nome']}",
            font=("Arial",24,"bold"),
            text_color=COR_CINZA_ESCURO
        )
        self.titulo.pack(anchor="w", pady=(0,20))

        # lista scrollável
        self.lista = ctk.CTkScrollableFrame(
            self.frame_principal,
            fg_color=COR_BRANCO
        )
        self.lista.pack(fill="both", expand=True)
        self.criar_item("Nome", paciente["nome"])
        self.criar_item("Telefone", paciente["telefone"])
        self.criar_item("Email", paciente["email"])

    def criar_item(self, nome, texto):

        item = ctk.CTkFrame(self.lista, fg_color="#f9fafb", corner_radius=10)
        item.pack(fill="x", pady=5)

        # avatar
        avatar = ctk.CTkLabel(
            item,
            text=nome[0],
            width=40,
            height=40,
            fg_color=COR_ROXO,
            corner_radius=20,
            text_color="white",
            font=("Arial",16,"bold")
        )
        avatar.pack(side="left", padx=10, pady=10)

        # texto
        frame_texto = ctk.CTkFrame(item, fg_color="transparent")
        frame_texto.pack(side="left", fill="x", expand=True)

        nome_label = ctk.CTkLabel(
            frame_texto,
            text=nome,
            font=("Arial",14,"bold"),
            text_color=COR_CINZA_ESCURO
        )
        nome_label.pack(anchor="w")

        desc = ctk.CTkLabel(
            frame_texto,
            text=texto,
            text_color=COR_CINZA
        )
        desc.pack(anchor="w")

        # seta direita
        seta = ctk.CTkLabel(
            item,
            text="›",
            font=("Arial",20),
            text_color=COR_CINZA
        )
        seta.pack(side="right", padx=10)