import customtkinter as ctk
from tkcalendar import DateEntry

COR_ROXO = "#7c3aed" #Sidebar, botões principais, ícones
COR_AZUL = "#3b82f6" #Cards, destaques, status
COR_BRANCO ="#ffffff" #Fundo dos cards, superfícies
COR_CINZA = "#808080" #Fundo da página
COR_CINZA_ESCURO = "#111827" #Textos e títulos

class NovoPaciente(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_ROXO)
        self.grid_columnconfigure(0, weight=1)
        #frame titulo
        self.frame_titulo = ctk.CTkFrame(self,
                                         fg_color=COR_ROXO)
        self.frame_titulo.grid(row=0, column=0)
        #labels titulo
        self.emoji_titulo = ctk.CTkLabel(self.frame_titulo,
                                         text="💾",
                                         font=("Arial",50))
        self.emoji_titulo.pack()
        self.label_novo_paciente = ctk.CTkLabel(self.frame_titulo,
                                                   text="Novo Paciente",
                                                   text_color=COR_BRANCO,
                                                   font=("Arial", 24, "bold"))
        self.label_novo_paciente.pack()

        self.label_detalhes_paciente = ctk.CTkLabel(self.frame_titulo,
                                                    text="Registre os detalhes do Paciente",
                                                    text_color=COR_BRANCO,
                                                    font=('Arial', 12, 'bold'))
        self.label_detalhes_paciente.pack()
        #frame centro
        self.frame_centro = ctk.CTkFrame(self, fg_color=COR_ROXO)
        self.frame_centro.grid(row=1, column=0, sticky="nsew")
        self.frame_centro.grid_columnconfigure(0, weight=1)
        self.frame_centro.grid_rowconfigure(0, weight=1)
        #frame principal
        self.frame_principal = ctk.CTkFrame(self.frame_centro, fg_color=COR_BRANCO,
                                            corner_radius=20,
                                            width=400,
                                            height=500)
        self.frame_principal.pack(expand=True,padx=40, pady=20)
        self.frame_principal.pack_propagate(False)
        #card nome completo
        self.card_nome_completo = self.criar_card("Nome Completo",COR_ROXO)
        #entry nome completo
        self.entry_nome_completo = ctk.CTkEntry(self.card_nome_completo,
                                                placeholder_text="Maria da Silva",
                                                fg_color=COR_BRANCO,
                                                text_color=COR_CINZA)
        self.entry_nome_completo.pack(fill="x")
        #card data de nascimento
        self.card_data_nascimento = self.criar_card("📅 Data de Nascimento", COR_AZUL)
        #data entry data de nascimento
        self.dataentry_data_nascimento = DateEntry(self.card_data_nascimento,
                                                   date_pattern = "dd/mm/yyyy",
                                                font=("Arial", 12, "bold"),
                                                background=COR_CINZA,
                                                foreground="white")
        self.dataentry_data_nascimento.pack(fill="x")
        #card telefone
        self.card_telefone = self.criar_card("📞 Telefone","#f0c609")
        #entry telefone
        self.entry_telefone = ctk.CTkEntry(self.card_telefone,
                                                placeholder_text="(11) 99999-9999",
                                                fg_color=COR_BRANCO,
                                                text_color=COR_CINZA)
        self.entry_telefone.pack(fill="x")
        #card email
        self.card_email = self.criar_card("✉️E-mail","#2CCE6A")
        #entry email
        self.entry_email = ctk.CTkEntry(self.card_email,
                                                placeholder_text="maria@gmail.com",
                                                fg_color=COR_BRANCO,
                                                text_color=COR_CINZA)
        self.entry_email.pack(fill="x")
        #card numero de documento
        self.card_numero_documento = self.criar_card("📄 Número de Documento (CPF ou RG)","#ff0000")
        #entry numero de documento
        self.entry_numero_documento = ctk.CTkEntry(self.card_numero_documento,
                                                   placeholder_text="000.000.000-00",
                                                   fg_color=COR_BRANCO,
                                                   text_color=COR_CINZA)
        self.entry_numero_documento.pack(fill="x")
        #card para botao de salvar paciente
        self.card_salvar = ctk.CTkFrame(self.frame_principal,
                                        fg_color=COR_BRANCO)
        self.card_salvar.pack(fill='x', expand=True,pady=5, padx=20)
        #botao salvar atendimento
        self.botao_salvar_paciente = ctk.CTkButton(self.card_salvar,text="💾Salvar Paciente",
                                          text_color=COR_BRANCO,
                                          fg_color=COR_ROXO)
        self.botao_salvar_paciente.pack(fill='x', pady=10, padx=20)
    def criar_card(self, texto, cor):
        card = ctk.CTkFrame(self.frame_principal, fg_color=COR_BRANCO)
        card.pack(fill="x", pady=10, padx=20)

        label = ctk.CTkLabel(card,text=texto,
                                  text_color=cor,
                                  font=("Arial",12,"bold"))
        label.pack(anchor="w")
        return card