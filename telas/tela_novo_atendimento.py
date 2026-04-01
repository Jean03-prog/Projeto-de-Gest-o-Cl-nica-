import customtkinter as ctk


COR_ROXO = "#7c3aed" #Sidebar, botões principais, ícones
COR_AZUL = "#3b82f6" #Cards, destaques, status
COR_BRANCO ="#ffffff" #Fundo dos cards, superfícies
COR_CINZA_CLARO = "#f9fafb" #Fundo da página
COR_CINZA_ESCURO = "#111827" #Textos e títulos

"""Cores dos Status na Tabela:
Status | Cor de Fundo | Cor do Texto |"""

FUNDO_REALIZADO = "#dcfce7" #verde claro fundo
TEXTO_REALIZADO = "#166534" #verde escuro texto

FUNDO_ACOMPANHAMENTO = "#dbeafe" #azul claro fundo
TEXTO_ACOMPANHAMENTO = "#1e40af" #azul escuro texto

class NovoAtendimento(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_ROXO)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame_principal = ctk.CTkFrame(self, fg_color=COR_BRANCO,
                                            corner_radius=20,
                                            width=400)
        self.frame_principal.grid(row=0, column=0, pady=20, padx=20)

        #card paciente
        self.card_paciente = ctk.CTkFrame(self.frame_principal,
                                          fg_color=COR_BRANCO)
        self.card_paciente.pack(fill="x", expand=True)

        #label paciente
        self.label_paciente = ctk.CTkLabel(self.card_paciente,
                                           text="Paciente",
                                           text_color=COR_ROXO,
                                           font=("Arial", 12, "bold"))
        self.label_paciente.grid(row=0, column=0, sticky='w')

        #entry paciente
        self.entry_paciente = ctk.CTkEntry(self.card_paciente,
                                           placeholder_text="Nome do Paciente",
                                           text_color=COR_CINZA_CLARO)
        self.entry_paciente.grid(row=1, column=0, sticky='w')
