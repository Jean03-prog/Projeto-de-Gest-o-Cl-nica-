import customtkinter as ctk
from telas.dashbord import Dashboard
from telas.tela_novo_atendimento import NovoAtendimento

"""| Cor | Código | Uso |"""

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

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Clínica Saúde")
        self.geometry("1200x800")
        self.configure(fg_color = COR_CINZA_CLARO)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menu_frame = ctk.CTkFrame(self, width=300, fg_color=COR_ROXO)
        self.menu_frame.grid(row=0, column=0, sticky='ns')

        self.label_clinica = ctk.CTkLabel(self.menu_frame, text="🧬 Clinica Saude+", font=("Arial", 24, "bold"), text_color=COR_BRANCO)
        self.label_clinica.pack(pady=20, padx=10)

        btn_dashboard = ctk.CTkButton(self.menu_frame, text= "Dashboard", anchor='w', font=("Arial", 16, "bold"))
        btn_dashboard.pack(pady=15, padx=10, fill='x')

        btn_paciente = ctk.CTkButton(self.menu_frame, text="Pacientes", anchor='w', font=("Arial", 16, "bold"))
        btn_paciente.pack(pady=15,padx=10, fill='x')

        btn_atendimentos = ctk.CTkButton(self.menu_frame, text="Atendimentos", anchor='w', font=("Arial", 16, "bold"))
        btn_atendimentos.pack(pady=15, padx=10, fill='x')

        btn_novo_paciente = ctk.CTkButton(self.menu_frame, text="Novo Paciente", anchor='w', font=("Arial", 16, "bold"))
        btn_novo_paciente.pack(pady=15, padx=10, fill='x')

        btn_novo_atendimento = ctk.CTkButton(self.menu_frame, text="Novo Atendimento", anchor='w', font=("Arial", 16, "bold"))
        btn_novo_atendimento.pack(pady=15, padx=10, fill='x')

        #frame para as telas
        self.conteudo_frame = ctk.CTkFrame(self, fg_color=COR_CINZA_CLARO)
        self.conteudo_frame.grid(row=0, column=1, sticky="nsew")

        #carregar dashboard
        # self.dashboard = Dashboard(self.conteudo_frame)
        # self.dashboard.pack(fill="both", expand=True)
        #carregar novo atendimento
        self.novo_atendimento = NovoAtendimento(self.conteudo_frame)
        self.novo_atendimento.pack(fill="both", expand=True)


app = App()
app.mainloop()