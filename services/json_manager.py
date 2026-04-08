import json
import locale
from datetime import datetime as dt
def carregar_json(data):
    try:
        with open(data, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            for item in dados:
                if "id" in item:
                    item["id"] = int(item["id"])
                if "paciente_id" in item:
                    item["paciente_id"] = int(item["paciente_id"])
            return dados
    except FileNotFoundError:
        return []
def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
#cricao de id
def gerar_id(lista):
    if not lista:
        return 1
    ids = [int(item.get("id", 0)) for item in lista]
    return max(ids) + 1
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
