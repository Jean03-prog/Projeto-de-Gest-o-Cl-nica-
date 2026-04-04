import customtkinter as ctk
from tkcalendar import DateEntry
from tkinter import ttk
COR_ROXO = "#7c3aed" #Sidebar, botões principais, ícones
COR_AZUL = "#3b82f6" #Cards, destaques, status
COR_BRANCO ="#ffffff" #Fundo dos cards, superfícies
COR_CINZA = "#808080" #Fundo da página
COR_CINZA_ESCURO = "#111827" #Textos e títulos

class Atendimento(ctk.CTkFrame):
    def __init__(self, master, abrir_novo_atendimento):
        super().__init__(master, fg_color=COR_BRANCO)
        self.abrir_novo_atendimento = abrir_novo_atendimento
        #frame header
        self.frame_header = ctk.CTkFrame(self,fg_color=COR_BRANCO,border_width=1)
        self.frame_header.pack(fill='x', pady=20, padx=20)
        #label titulo
        self.label_titulo = ctk.CTkLabel(self.frame_header,
            text="Atendimentos",
            text_color=COR_ROXO,
            font=("Arial", 24, "bold"))
        self.label_titulo.pack(side='left',pady=5,padx=20)
        #botao novo atendimento
        self.botao_atendimento = ctk.CTkButton(self.frame_header,
                                               text="Novo Atendimento➕",
                                               text_color=COR_BRANCO,
                                               corner_radius=10,
                                               fg_color=COR_ROXO, command=self.abrir_novo_atendimento)
        self.botao_atendimento.pack(side='right',pady=5,padx=20)
        #frame para header filtros
        self.frame_header_filtros = ctk.CTkFrame(self,fg_color=COR_BRANCO)
        self.frame_header_filtros.pack(fill="x", pady=5, padx=20)
        #label subtitulo header filtros
        self.label_subtitulo = ctk.CTkLabel(self.frame_header_filtros,
                                            text="Filtros e Busca",
                                            text_color=COR_CINZA,
                                            font=("Arial", 12,"bold"))
        self.label_subtitulo.pack(side="left")
        #botao limpar filtros
        self.botao_limpar = ctk.CTkButton(self.frame_header_filtros,
                                          text="Limpar Filtros",
                                          text_color=COR_CINZA,
                                          fg_color="transparent",
                                          font=("Arial", 12,"bold"))
        self.botao_limpar.pack(side="right")
        #frame filtros
        self.frame_filtros = ctk.CTkFrame(self,fg_color=COR_BRANCO)
        self.frame_filtros.pack(fill="x", pady=20, padx=20)
        self.frame_filtros.grid_columnconfigure(0, weight=2)
        for i in range(1,5):
            self.frame_filtros.grid_columnconfigure(i, weight=1)
        #label buscar paciente
        self.label_buscar = ctk.CTkLabel(self.frame_filtros,
                             text="Buscar Paciente",
                             text_color=COR_CINZA,
                             font=("Arial", 12))
        self.label_buscar.grid(row=0, column=0,sticky='w',pady=5,padx=20)
        #entry buscar pacientes
        self.entry_buscar = ctk.CTkEntry(self.frame_filtros,
                                         placeholder_text="Maria",
                                         text_color=COR_CINZA_ESCURO,
                                         fg_color=COR_BRANCO,
                                         corner_radius=10,
                                         font=("Arial", 12,"bold"))
        self.entry_buscar.grid(row=1, column=0,sticky='ew',pady=5,padx=10)
        #label status
        self.label_status = ctk.CTkLabel(self.frame_filtros,
                                         text="Status",
                                         text_color=COR_CINZA,
                                         font=("Arial", 12))
        self.label_status.grid(row=0, column=1, sticky='w',pady=5,padx=20)
        #combobox status
        self.combo_status = ctk.CTkComboBox(self.frame_filtros,fg_color=COR_BRANCO,text_color=COR_CINZA_ESCURO,values=["Realizado",
                                                                                                              "Em Andamento"],
                                                    state="readonly",
                                                    font=("Arial", 12, "bold"))
        self.combo_status.grid(row=1, column=1,sticky='ew',pady=5,padx=10)
        #label tipo
        self.label_tipo = ctk.CTkLabel(self.frame_filtros,
                                         text="Tipo",
                                         text_color=COR_CINZA,
                                         font=("Arial", 12))
        self.label_tipo.grid(row=0, column=2,sticky='w',pady=5,padx=20)
        #combobox tipo
        self.combo_tipo = ctk.CTkComboBox(self.frame_filtros, fg_color=COR_BRANCO, text_color=COR_CINZA_ESCURO,
                                          values=["Consulta",
                                                     "Retorno",
                                                     "Avaliação",
                                                     "Exame",
                                                     "Procedimento"],
                                                     state='readonly',
                                                     font=("Arial", 12, "bold"))
        self.combo_tipo.grid(row=1, column=2,sticky='ew',pady=5,padx=10)
        #label data inicio
        self.label_data_inicio = ctk.CTkLabel(self.frame_filtros,
                                         text="Data Inicio",
                                         text_color=COR_CINZA,
                                         font=("Arial", 12))
        self.label_data_inicio.grid(row=0, column=3, sticky='w', pady=5,padx=20)
        #data entry data inicio
        self.data_inicio = DateEntry(self.frame_filtros,
                                    date_pattern="dd/mm/yyyy",
                                    font=("Arial", 12, "bold"),
                                    background=COR_CINZA,
                                    foreground="white")
        self.data_inicio.grid(row=1, column=3,sticky='ew',pady=5,padx=10)
        #label data fim
        self.label_data_fim = ctk.CTkLabel(self.frame_filtros,
                                         text="Data Fim",
                                         text_color=COR_CINZA,
                                         font=("Arial", 12))
        self.label_data_fim.grid(row=0, column=4, sticky='w', pady=5,padx=20)
        #data entry data fim
        self.data_fim = DateEntry(self.frame_filtros,
                                    date_pattern="dd/mm/yyyy",
                                    font=("Arial", 12, "bold"),
                                    background=COR_CINZA,
                                    foreground="white")
        self.data_fim.grid(row=1, column=4,sticky='ew',pady=5,padx=10)
        style = ttk.Style()

        style.configure(
            "Treeview",
            rowheight=32,
            font=("Arial", 12)
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 12, "bold")
)
        #frame tabela
        self.frame_tabela = ctk.CTkFrame(self, fg_color=COR_BRANCO)
        self.frame_tabela.pack(fill='both', expand=True, pady=20,padx=20)
        #treeview
        self.treeview_filtro = ttk.Treeview(self.frame_tabela,
                                            columns=("ID", "PACIENTE", "TIPO","DATA/HORA","STATUS", "AÇÕES"),
                                            show="headings")
        self.treeview_filtro.pack(fill='both', expand=True, pady=20, padx=20)
        self.treeview_filtro.heading("ID", text="ID", anchor="w")
        self.treeview_filtro.heading("PACIENTE", text="PACIENTE")
        self.treeview_filtro.heading("TIPO", text="TIPO")
        self.treeview_filtro.heading("DATA/HORA", text="DATA/HORA")
        self.treeview_filtro.heading("STATUS", text="STATUS")
        self.treeview_filtro.heading("AÇÕES", text="AÇÕES")