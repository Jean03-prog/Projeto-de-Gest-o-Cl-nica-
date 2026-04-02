import customtkinter as ctk
from tkcalendar import DateEntry

COR_ROXO = "#7c3aed" #Sidebar, botões principais, ícones
COR_AZUL = "#3b82f6" #Cards, destaques, status
COR_BRANCO ="#ffffff" #Fundo dos cards, superfícies
COR_CINZA = "#808080" #Fundo da página
COR_CINZA_ESCURO = "#111827" #Textos e títulos

class NovoAtendimento(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_ROXO)
        self.grid_columnconfigure(0, weight=1)
        #frame titulo
        self.frame_titulo = ctk.CTkFrame(self,
                                         fg_color=COR_ROXO)
        self.frame_titulo.grid(row=0, column=0, pady=(20,10))
        #labels titulo
        self.emoji_titulo = ctk.CTkLabel(self.frame_titulo,
                                         text="💾",
                                         font=("Arial",50))
        self.emoji_titulo.pack()
        self.label_novo_atendimento = ctk.CTkLabel(self.frame_titulo,
                                                   text="Novo Atendimento",
                                                   text_color=COR_BRANCO,
                                                   font=("Arial", 24, "bold"))
        self.label_novo_atendimento.pack()

        self.label_registre_detalhes = ctk.CTkLabel(self.frame_titulo,
                                                    text="Registre os detalhes do Atendimento",
                                                    text_color=COR_BRANCO,
                                                    font=('Arial', 12, 'bold'))
        self.label_registre_detalhes.pack()
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
        self.frame_principal.pack(expand=True, padx=40, pady=20)
        self.frame_principal.pack_propagate(False)
        #card paciente
        self.card_paciente = self.criar_card("Paciente", COR_ROXO)
        #entry paciente
        self.entry_paciente = ctk.CTkEntry(self.card_paciente,
                                           placeholder_text="Nome do Paciente",
                                           fg_color=COR_BRANCO,
                                           text_color=COR_CINZA)
        self.entry_paciente.pack(fill="x")
        #card data de atendimento
        self.card_data = self.criar_card('📅Data de Atendimento', COR_AZUL)
        #data entry data de atendimento
        self.data_entry_atendimento = DateEntry(self.card_data,
                                                date_pattern = "dd/mm/yyyy",
                                                font=("Arial", 12, "bold"),
                                                background=COR_CINZA,
                                                foreground="white")
        self.data_entry_atendimento.pack(fill="x")
        #card tipo de atendimento
        self.card_tipo_atendimento = self.criar_card("📋 Tipo de Atendimento","#f0c609")
        #combobox tipo de atendimento
        self.combobox_tipo = ctk.CTkComboBox(self.card_tipo_atendimento,fg_color=COR_BRANCO,text_color='black',
                                             values=["Consulta",
                                                     "Retorno",
                                                     "Avaliação",
                                                     "Exame",
                                                     "Procedimento"],
                                                     state='readonly',
                                                     font=("Arial", 12, "bold"))
        self.combobox_tipo.pack(fill="x")

        #card obsrvacoes do profissional
        self.card_observacoes = self.criar_card("📓 Observações do Profissional","#2CCE6A")
        #text observacoes do profissional
        self.text_observacoes = ctk.CTkTextbox(self.card_observacoes,
                                               border_width=2,
                                               border_color=COR_CINZA,
                                               fg_color=COR_BRANCO,
                                               height=70)
        self.text_observacoes.pack(fill='x')
        #card status de atendimento
        self.card_status = self.criar_card("✅ Status de Atendimento","#ff0000")
        #combo box status de atendimento
        self.combo_status = ctk.CTkComboBox(self.card_status,fg_color=COR_BRANCO,text_color='black',
                                             values=["Realizado",
                                                     "Em Acompanhamento"],
                                                     state='readonly',
                                                     font=("Arial", 12, "bold"))
        self.combo_status.pack(fill="x")
        #card para botao de salvar atendimento
        self.card_salvar = ctk.CTkFrame(self.frame_principal,
                                        fg_color=COR_BRANCO)
        self.card_salvar.pack(fill='x',pady=10, padx=20)
        #botao salvar atendimento
        self.botao_salvar = ctk.CTkButton(self.card_salvar,text="💾Salvar Atendimento",
                                          text_color=COR_BRANCO,
                                          fg_color=COR_ROXO,
                                          height=40,
                                          corner_radius=10)
        self.botao_salvar.pack(fill='x')
    def criar_card(self, texto, cor):
        card = ctk.CTkFrame(self.frame_principal, fg_color=COR_BRANCO)
        card.pack(fill="x", pady=10, padx=20)

        label = ctk.CTkLabel(card,text=texto,
                                  text_color=cor,
                                  font=("Arial",12,"bold"))
        label.pack(anchor="w")
        return card