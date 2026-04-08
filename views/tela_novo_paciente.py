import customtkinter as ctk
from tkcalendar import DateEntry
from tkinter import messagebox as mg
from models.pacientes import Paciente
from controllers.paciente_controller import adicionar_paciente

COR_ROXO = "#7c3aed" #Sidebar, botões principais, ícones
COR_AZUL = "#3b82f6" #Cards, destaques, status
COR_BRANCO ="#ffffff" #Fundo dos cards, superfícies
COR_CINZA = "#808080" #Fundo da página
COR_CINZA_ESCURO = "#111827" #Textos e títulos

class NovoPaciente(ctk.CTkFrame):
    def __init__(self, master, paciente=None):
        super().__init__(master, fg_color=COR_ROXO)
        self.paciente = paciente
        self.grid_columnconfigure(0, weight=1)
        #frame titulo
        self.frame_titulo = ctk.CTkFrame(self,
                                         fg_color=COR_ROXO)
        self.frame_titulo.grid(row=0, column=0, pady=20)
        #labels titulo
        self.emoji_titulo = ctk.CTkLabel(self.frame_titulo,
                                         text="💾",
                                         font=("Arial",50))
        self.emoji_titulo.pack()
        self.label_novo_paciente = ctk.CTkLabel(self.frame_titulo,
                                                   text="Novo Paciente",
                                                   text_color=COR_BRANCO,
                                                   font=("Arial", 28, "bold"))
        self.label_novo_paciente.pack()
        if paciente:
            self.label_novo_paciente.configure(text="Editar Paciente")

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
                                            width=750,
                                            height=620)
        self.frame_principal.pack(expand=True,padx=80, pady=10)
        self.frame_principal.pack_propagate(False)
        #card nome completo
        self.card_nome_completo = self.criar_card("Nome Completo",COR_ROXO)
        #entry nome completo
        self.entry_nome_completo = ctk.CTkEntry(self.card_nome_completo,
                                                placeholder_text="Maria da Silva",
                                                fg_color=COR_BRANCO,
                                                text_color=COR_CINZA,
                                                height=36)
        self.entry_nome_completo.pack(fill="x")
        #card data de nascimento
        self.card_data_nascimento = self.criar_card("📅 Data de Nascimento", COR_AZUL)
        #data entry data de nascimento
        self.dataentry_data_nascimento = DateEntry(self.card_data_nascimento,
                                                   date_pattern = "dd/mm/yyyy",
                                                font=("Arial", 12, "bold"),
                                                background=COR_CINZA,
                                                foreground="white",
                                                height=36)
        self.dataentry_data_nascimento.pack(fill="x")
        #card telefone
        self.card_telefone = self.criar_card("📞 Telefone","#f0c609")
        #entry telefone
        self.entry_telefone = ctk.CTkEntry(self.card_telefone,
                                                placeholder_text="(11) 99999-9999",
                                                fg_color=COR_BRANCO,
                                                text_color=COR_CINZA,
                                                height=36)
        self.entry_telefone.pack(fill="x")
        self.entry_telefone.bind("<KeyRelease>", self.mascara_telefone)
        #card email
        self.card_email = self.criar_card("✉️E-mail","#2CCE6A")
        #entry email
        self.entry_email = ctk.CTkEntry(self.card_email,
                                                placeholder_text="maria@gmail.com",
                                                fg_color=COR_BRANCO,
                                                text_color=COR_CINZA,
                                                height=36)
        self.entry_email.pack(fill="x")
        if paciente:
            self.entry_nome_completo.insert(0, paciente["nome"])
            self.entry_telefone.insert(0, paciente["telefone"])
            self.entry_email.insert(0, paciente["email"])
        #card numero de documento
        self.card_numero_documento = self.criar_card("📄 Número de Documento (CPF ou RG)","#ff0000")
        #entry numero de documento
        self.entry_numero_documento = ctk.CTkEntry(self.card_numero_documento,
                                                   placeholder_text="000.000.000-00",
                                                   fg_color=COR_BRANCO,
                                                   text_color=COR_CINZA,
                                                height=36)
        self.entry_numero_documento.pack(fill="x")
        self.entry_numero_documento.bind("<KeyRelease>", self.mascara_cpf)
        if paciente:
            self.entry_numero_documento.insert(0, paciente["doc"])
        #card para botao de salvar paciente
        self.card_salvar = ctk.CTkFrame(self.frame_principal,
                                        fg_color=COR_BRANCO)
        self.card_salvar.pack(fill='x', expand=True,pady=5, padx=20)
        #botao salvar atendimento
        self.botao_salvar_paciente = ctk.CTkButton(self.card_salvar,text="💾Salvar Paciente",
                                        font=("Arial", 16, "bold"),
                                        text_color=COR_BRANCO,
                                        fg_color=COR_ROXO,
                                        height=40, width=500,
                                        command=self.salvar_paciente) 
        self.botao_salvar_paciente.pack(fill='x')
    def criar_card(self, texto, cor):
        card = ctk.CTkFrame(self.frame_principal, fg_color=COR_BRANCO)
        card.pack(fill="x", pady=10, padx=20)

        label = ctk.CTkLabel(card,text=texto,
                                  text_color=cor,
                                  font=("Arial",12,"bold"))
        label.pack(anchor="w")
        return card
    def email_valido(self, email):
        import re
        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(padrao, email)
    def salvar_paciente(self):

        nome = self.entry_nome_completo.get()
        data_nascimento = self.dataentry_data_nascimento.get()
        telefone = self.entry_telefone.get()
        email = self.entry_email.get()
        doc = self.entry_numero_documento.get()
        if not nome:
            mg.showerror("Erro", "Digite o nome do paciente")
            return
        if not telefone:
            mg.showerror("Erro", "Digite o telefone")
            return
        if not email:
            mg.showerror("Erro", "Digite o E-mail")
        if email and not self.email_valido(email):
            mg.showerror("Erro", "Email inválido")
        if not doc:
            mg.showerror("Erro", "Digite o documento")
            return
        paciente = Paciente(
            id=0,
            nome=nome,
            data_nascimento=data_nascimento,
            telefone=telefone,
            email=email,
            doc=doc
            )
        adicionar_paciente(paciente)
        self.limpar_campos()
        mg.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
    def limpar_campos(self):
        self.entry_nome_completo.delete(0, "end")
        self.entry_telefone.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_numero_documento.delete(0, "end")
    def mascara_telefone(self, event):
        texto = self.entry_telefone.get()
        numeros = "".join(filter(str.isdigit, texto))
        if len(numeros) > 11:
            numeros = numeros[:11]
        if len(numeros) <= 2:
            texto_formatado = f"({numeros}"
        elif len(numeros) <= 7:
            texto_formatado = f"({numeros[:2]}) {numeros[2:]}"
        else:
            texto_formatado = f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"
        self.entry_telefone.delete(0, "end")
        self.entry_telefone.insert(0, texto_formatado)
    def mascara_cpf(self,event):
        text = self.entry_numero_documento.get()
        numeros = "".join(filter(str.isdigit, text))
        if len(numeros)>11:
            numeros = numeros[:11]
        if len(numeros)<=3:
            texto_formatado = f"{numeros}"
        elif len(numeros)<=6:
            texto_formatado = f"{numeros[:3]}.{numeros[3:]}"
        elif len(numeros)<=9:
            texto_formatado = f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:]}"
        else:
            texto_formatado = f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"
        self.entry_numero_documento.delete(0, "end")
        self.entry_numero_documento.insert(0, texto_formatado)