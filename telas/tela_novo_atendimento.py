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
        super().__init__(master, fg_color="transparent")
        self.frame_central = ctk.CTkFrame(self, fg_color=COR_ROXO)
        self.frame_central.pack(expand=True, fill="both")