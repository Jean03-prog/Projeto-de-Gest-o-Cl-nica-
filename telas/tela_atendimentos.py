import customtkinter as ctk
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox as mg
from utils.json_manager import salvar_json
from utils.json_manager import listar_atendimentos, listar_pacientes
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
                                          font=("Arial", 12,"bold"), command=self.limpar_filtros)
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
        self.entry_buscar.bind("<KeyRelease>", self.filtrar_atendimentos)
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
        self.combo_status.bind("<<ComboboxSelected>>", self.filtrar_atendimentos)
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
        self.combo_tipo.bind("<<ComboboxSelected>>", self.filtrar_atendimentos)
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
        self.data_inicio.bind("<<DateEntrySelected>>", self.filtrar_atendimentos)
        self.data_fim.bind("<<DateEntrySelected>>", self.filtrar_atendimentos)
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
                                            columns=("ID", "PACIENTE", "ULTIMO", "TOTAL", "AÇÕES"),
                                            show="headings")
        self.treeview_filtro.pack(fill='both', expand=True, pady=20, padx=20)
        #heading treeview
        self.treeview_filtro.heading("ID", text="ID", anchor="w")
        self.treeview_filtro.heading("PACIENTE", text="Paciente", anchor="w")
        self.treeview_filtro.heading("ULTIMO", text="Último Atendimento", anchor="w")
        self.treeview_filtro.heading("TOTAL", text="Total", anchor="w")
        self.treeview_filtro.heading("AÇÕES", text="Ações", anchor="w")
        #column treeview
        self.treeview_filtro.column("ID", width=60)
        self.treeview_filtro.column("PACIENTE", width=250)
        self.treeview_filtro.column("ULTIMO", width=150)
        self.treeview_filtro.column("TOTAL", width=80)
        self.treeview_filtro.column("AÇÕES", width=120)
        self.treeview_filtro.bind("<ButtonRelease-1>", self.abrir_historico)
        self.carregar_atendimentos()
    def carregar_atendimentos(self):

        # limpar tabela
        for item in self.treeview_filtro.get_children():
            self.treeview_filtro.delete(item)
        self.atendimentos = listar_atendimentos()
        self.pacientes = listar_pacientes()

        # dicionário para agrupar pacientes
        self.pacientes_dict = {}
        for atendimento in self.atendimentos:
            self.paciente_id = atendimento["paciente_id"]
            if self.paciente_id not in self.pacientes_dict:

                self.pacientes_dict[self.paciente_id] = {
                    "total": 0,
                    "ultimo": atendimento["data"]}
            self.pacientes_dict[self.paciente_id]["total"] += 1
            self.pacientes_dict[self.paciente_id]["ultimo"] = atendimento["data"]

        for paciente in self.pacientes:
            self.pid = paciente["id"]

            if self.pid in self.pacientes_dict:
                self.total = self.pacientes_dict[self.pid]["total"]
                self.ultimo = self.pacientes_dict[self.pid]["ultimo"]

                self.treeview_filtro.insert(
                    "",
                    "end",
                    values=(
                        self.pid,
                        paciente["nome"],
                        self.ultimo,
                        self.total,
                        "Ver Histórico"))
    def filtrar_atendimentos(self, event=None):
        texto = self.entry_buscar.get().lower()
        status = self.combo_status.get()
        tipo = self.combo_tipo.get()
        data_inicio = self.data_inicio.get_date()
        data_fim = self.data_fim.get_date()
        for item in self.treeview_filtro.get_children():
            self.treeview_filtro.delete(item)
        atendimentos = listar_atendimentos()
        pacientes = listar_pacientes()
        pacientes_dict = {p["id"]: p["nome"] for p in pacientes}
        for atendimento in atendimentos:
            nome_paciente = pacientes_dict.get(atendimento["paciente_id"], "")
            # converter data do atendimento
            from datetime import datetime
            data_atendimento = datetime.strptime(atendimento["data"], "%d/%m/%Y").date()
            if (texto in nome_paciente.lower()
                and (status == "" or atendimento["status"] == status)
                and (tipo == "" or atendimento["tipo"] == tipo)
                and data_inicio <= data_atendimento <= data_fim):

                self.treeview_filtro.insert(
                    "",
                    "end",
                    values=(
                        atendimento["id"],
                        nome_paciente,
                        atendimento["tipo"],
                        atendimento["data"],
                        atendimento["status"],
                        "Ver"
                    )
                )
    def abrir_historico(self, event):
        item = self.treeview_filtro.selection()
        if not item:
            return

        valores = self.treeview_filtro.item(item)["values"]
        nome_paciente = valores[1]

        pacientes = listar_pacientes()
        paciente = None

        for p in pacientes:
            if p["nome"] == nome_paciente:
                paciente = p
                break
        if paciente:
            self.master.master.abrir_historico_paciente(paciente)
    def limpar_filtros(self):
        self.entry_buscar.delete(0, "end")
        self.combo_status.set("")
        self.combo_tipo.set("")
        self.carregar_atendimentos()
