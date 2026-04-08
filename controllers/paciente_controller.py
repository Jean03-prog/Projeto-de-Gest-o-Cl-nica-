from services.json_manager import carregar_json, salvar_json, gerar_id
def adicionar_paciente(paciente):
    pacientes = carregar_json("dados/pacientes.json")
    paciente.id = gerar_id(pacientes)
    pacientes.append(paciente.to_dict())
    salvar_json("dados/pacientes.json", pacientes)
#listagem de pacientes
def listar_pacientes():
    return carregar_json("dados/pacientes.json")
#buscar paciente por nome
def buscar_paciente_por_nome(nome):
    pacientes = carregar_json("dados/pacientes.json")
    for paciente in pacientes:
        if paciente["nome"].lower() == nome.lower():
            return paciente
    return None