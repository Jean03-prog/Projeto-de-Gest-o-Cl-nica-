import customtkinter as ctk
from utils.json_manager import listar_pacientes
COR_ROXO = "#7c3aed" #Sidebar, botões principais, ícones
COR_AZUL = "#3b82f6" #Cards, destaques, status
COR_BRANCO ="#ffffff" #Fundo dos cards, superfícies
COR_CINZA = "#808080" #Fundo da página
COR_CINZA_ESCURO = "#111827" #Textos e títulos

class Paciente(ctk.CTkFrame):
    def __init__(self,master,abrir_novo_paciente, abrir_detalhes):
        super().__init__(master, fg_color=COR_BRANCO)
        self.abrir_novo_paciente = abrir_novo_paciente
        self.abrir_detalhes = abrir_detalhes
        self.pacientes = listar_pacientes()
        #frame principal
        self.frame_principal = ctk.CTkFrame(self, fg_color=COR_BRANCO)
        self.frame_principal.pack(fill="both", expand=True)
        #card titulo
        self.card_titulo = ctk.CTkFrame(self.frame_principal, fg_color=COR_BRANCO)
        self.card_titulo.pack(pady=40, padx=20, anchor="w", fill="x")
        #button novo paciente
        self.novo_paciente = ctk.CTkButton(self.card_titulo,text="Novo Paciente➕",
                                               text_color=COR_BRANCO,
                                               corner_radius=10,
                                               fg_color=COR_ROXO,command=self.abrir_novo_paciente)
        self.novo_paciente.pack(side="right",padx=5,pady=5)
        #label titulo
        self.label_titulo = ctk.CTkLabel(self.card_titulo,text="Pacientes",
                                         text_color=COR_CINZA_ESCURO,
                                         font=("Arial", 24, "bold"))
        self.label_titulo.pack(anchor="w", padx=5, pady=5)
        #label subtitulo
        self.label_subtitulo = ctk.CTkLabel(self.card_titulo,
                                            text="Gerencie e visualize as informações dos pacientes",
                                            text_color=COR_CINZA,
                                            font=("Arial", 12, "bold"))
        self.label_subtitulo.pack(anchor="w",padx=5, pady=5)
        #entry buscar
        self.entry_buscar = ctk.CTkEntry(self.card_titulo,placeholder_text="🔍Buscar por nome ou telefone...",fg_color=COR_BRANCO,
                                         text_color=COR_CINZA_ESCURO,corner_radius=10,
                                         font=("Arial", 16, "bold"))
        self.entry_buscar.pack(padx=5, pady=5, anchor="w", fill="x")
        self.entry_buscar.bind("<KeyRelease>", self.buscar_paciente)
        # frame vazio (nenhum paciente)
        self.frame_vazio = ctk.CTkFrame(self.frame_principal, fg_color=COR_BRANCO)
        self.frame_vazio.pack(expand=True)
        self.frame_lista = ctk.CTkScrollableFrame(self.frame_principal, fg_color=COR_BRANCO)
        #label emoji
        self.label_emoji = ctk.CTkLabel(
            self.frame_vazio,
            text="🧑‍⚕️",
            font=("Arial", 50))
        self.label_emoji.pack(pady=(40,10))
        #label texto principal
        self.label_vazio = ctk.CTkLabel(
            self.frame_vazio,
            text="Nenhum paciente encontrado",
            font=("Arial", 18, "bold"),
            text_color=COR_CINZA_ESCURO)
        self.label_vazio.pack(pady=5)
        #label texto secundário
        self.label_vazio2 = ctk.CTkLabel(
            self.frame_vazio,
            text="Clique em 'Novo Paciente' para começar",
            font=("Arial", 14),
            text_color=COR_CINZA)
        self.label_vazio2.pack(pady=(0,40))
        self.mostrar_pacientes(self.pacientes)
    def mostrar_pacientes(self, lista):
        for widget in self.frame_lista.winfo_children():
            widget.destroy()

        if not lista:
            self.frame_lista.pack_forget()
            self.frame_vazio.pack(expand=True)
            return
        
        self.frame_vazio.pack_forget()
        self.frame_lista.pack(fill="both", expand=True)

        header = ctk.CTkFrame(self.frame_lista, fg_color="#f3f4f6")
        header.pack(fill="x", padx=20, pady=(10,5))

        ctk.CTkLabel(header, text="Nome", font=("Arial",14,"bold"),
                    text_color=COR_CINZA_ESCURO, width=250, anchor="w").grid(row=0,column=0,padx=10)
        ctk.CTkLabel(header, text="Telefone", font=("Arial",14,"bold"),
                    text_color=COR_CINZA_ESCURO, width=180, anchor="w").grid(row=0,column=1,padx=10)
        ctk.CTkLabel(header, text="Email", font=("Arial",14,"bold"),
                    text_color=COR_CINZA_ESCURO, width=250, anchor="w").grid(row=0,column=2,padx=10)
        ctk.CTkLabel(header, text="Ações", font=("Arial",14,"bold"),
                    text_color=COR_CINZA_ESCURO, width=150).grid(row=0,column=3,padx=10, sticky="e")


        for paciente in lista:

            linha = ctk.CTkFrame(self.frame_lista, fg_color="#ffffff")
            linha.pack(fill="x", padx=20, pady=2)
            linha.bind("<Button-1>", lambda e, p=paciente: self.abrir_detalhes(p))
            linha.configure(cursor="hand2")
            for widget in linha.winfo_children():
                widget.bind("<Button-1>", lambda e, p=paciente: self.abrir_detalhes(p))

            ctk.CTkLabel(
                linha,
                text=paciente["nome"],
                font=("Arial",14),
                text_color=COR_CINZA_ESCURO,
                width=250,
                anchor="w"
            ).grid(row=0,column=0,padx=10,pady=10)

            ctk.CTkLabel(
                linha,
                text=str(paciente["telefone"]),
                text_color=COR_CINZA_ESCURO,
                width=180,
                anchor="w"
            ).grid(row=0,column=1,padx=10)

            ctk.CTkLabel(
                linha,
                text=str(paciente["email"]),
                text_color=COR_CINZA_ESCURO,
                width=250,
                anchor="w"
            ).grid(row=0,column=2,padx=10)

            btn_editar = ctk.CTkButton(linha,text="Editar",width=60,fg_color=COR_AZUL)
            btn_editar.grid(row=0,column=3,padx=5, sticky="e")

            btn_excluir = ctk.CTkButton(linha,text="Excluir",width=60,fg_color="#ef4444")
            btn_excluir.grid(row=0,column=4,padx=5, sticky="e")

    def buscar_paciente(self, event=None):
        texto = self.entry_buscar.get().lower()
        resultado = []
        for paciente in self.pacientes:
            nome = paciente["nome"].lower()
            telefone = paciente["telefone"]
            if texto in nome or texto in telefone:
                resultado.append(paciente)
        self.mostrar_pacientes(resultado)