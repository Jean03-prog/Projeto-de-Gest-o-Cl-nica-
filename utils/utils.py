from datetime import datetime as dt
import locale



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