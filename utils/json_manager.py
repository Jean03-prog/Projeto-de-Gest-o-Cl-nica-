import json
import locale
from datetime import datetime as dt
def carregar_json(data):
    try:
        with open(data, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        return []
def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
#funcao salvar paciente
def adicionar_paciente(paciente):
    pacientes = carregar_json("dados/pacientes.json")
    paciente.id = gerar_id(pacientes)
    pacientes.append(paciente.to_dict())
    salvar_json("dados/pacientes.json", pacientes)
#funcao salvar atendimento
def adicionar_atendimento(atendimento):
    atendimentos = carregar_json("dados/atendimentos.json")
    atendimento.id = gerar_id(atendimentos)
    atendimentos.append(atendimento.to_dict())
    salvar_json("dados/atendimentos.json", atendimentos)
#cricao de id
def gerar_id(lista):
    if not lista:
        return 1
    ids = [item.get("id", 0) for item in lista]
    return max(ids) + 1
#listagem de pacientes
def listar_pacientes():
    return carregar_json("dados/pacientes.json")
#listagem de atendimentos
def listar_atendimentos():
    return carregar_json("dados/atendimentos.json")
#buscar paciente por nome
def buscar_paciente_por_nome(nome):
    pacientes = carregar_json("dados/pacientes.json")
    for paciente in pacientes:
        if paciente["nome"].lower() == nome.lower():
            return paciente
    return None
def convert_date_for_label() -> str:
    'Retornar data no formato dia da semana, dia, mês por extenso e ano. Ex.: Terça, 21 de Março de 2026'
    locale.setlocale(locale.LC_TIME, 'pt_BR')
    #capturar por extenso
    mes = dt.today().strftime("%B").capitalize()
    dia_semana_nome = dt.today().strftime("%A").capitalize()
    #capturar por numero
    ano = dt.today().strftime("%Y")
    dia_mes_valor = dt.today().strftime("%d")

    return f"{dia_semana_nome}, {dia_mes_valor} de {mes} de {ano}"