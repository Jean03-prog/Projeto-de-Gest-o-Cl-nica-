import customtkinter as ctk
from telas.dashbord import Dashboard
from telas.tela_atendimentos import Atendimento
from telas.tela_novo_atendimento import NovoAtendimento
from telas.tela_novo_paciente import NovoPaciente

COR_ROXO = "#7c3aed" #Sidebar, botões principais, ícones
COR_AZUL = "#3b82f6" #Cards, destaques, status
COR_BRANCO ="#ffffff" #Fundo dos cards, superfícies
COR_CINZA_CLARO = "#f9fafb" #Fundo da página
COR_CINZA_ESCURO = "#111827" #Textos e títulos

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Clínica Saúde")
        self.geometry("1820x800")
        self.configure(fg_color = COR_CINZA_CLARO)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menu_frame = ctk.CTkFrame(self, width=300, fg_color=COR_ROXO)
        self.menu_frame.grid(row=0, column=0, sticky='ns')

        self.label_clinica = ctk.CTkLabel(self.menu_frame, text="🧬 Clinica Saude+", font=("Arial", 24, "bold"), text_color=COR_BRANCO)
        self.label_clinica.pack(pady=20, padx=10)

        self.criar_botao("Dashboard", self.mostrar_dashboard)
        self.criar_botao("Pacientes", None)
        self.criar_botao("Atendimentos", self.mostrar_atendimento)
        self.criar_botao("Novo Paciente", self.mostrar_novo_paciente)
        self.criar_botao("Novo Atendimento", self.mostrar_novo_atendimento)
        #frame para as telas
        self.conteudo_frame = ctk.CTkFrame(self, fg_color=COR_CINZA_CLARO)
        self.conteudo_frame.grid(row=0, column=1, sticky="nsew")
        self.mostrar_dashboard()
    def criar_botao(self, texto, comando):
        botao = ctk.CTkButton(self.menu_frame, text=texto, anchor="w",font=("Arial", 16, "bold"), command=comando)
        botao.pack(pady=15, padx=10, fill="x")
        return botao
    def limpar_tela(self):
        for widget in self.conteudo_frame.winfo_children():
            widget.destroy()
    def mostrar_dashboard(self):
        self.limpar_tela()
        self.dashboard = Dashboard(self.conteudo_frame)
        self.dashboard.pack(fill="both",expand=True)
    def mostrar_atendimento(self):
        self.limpar_tela()
        self.atendimento = Atendimento(self.conteudo_frame)
        self.atendimento.pack(fill="both", expand=True)
    def mostrar_novo_atendimento(self):
        self.limpar_tela()
        self.novo_atendimento = NovoAtendimento(self.conteudo_frame)
        self.novo_atendimento.pack(fill="both", expand=True)
    def mostrar_novo_paciente(self):
        self.limpar_tela()
        self.novo_paciente = NovoPaciente(self.conteudo_frame)
        self.novo_paciente.pack(fill="both",expand=True)

app = App()
app.mainloop()