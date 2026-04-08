from services.json_manager import carregar_json, salvar_json, gerar_id
#funcao salvar atendimento
def adicionar_atendimento(atendimento):
    atendimentos = carregar_json("dados/atendimentos.json")
    atendimento.id = gerar_id(atendimentos)
    atendimentos.append(atendimento.to_dict())
    salvar_json("dados/atendimentos.json", atendimentos)
#listagem de atendimentos
def listar_atendimentos():
    return carregar_json("dados/atendimentos.json")