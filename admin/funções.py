import json


ARQUIVO = "Bd_agenda.json"

def carregar_agenda():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            print("OK")
            return json.load(f) 
        
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def editar_agenda(agenda, semana, servico, valor, status):
    dia = None
    if semana == 'segunda': dia = 0
    if semana == 'terça': dia = 1
    if semana == 'quarta': dia = 2
    if semana == 'quinta': dia = 3
    if semana == 'sexta': dia = 4
    if semana == 'sabado': dia = 5
    if semana == 'domingo': dia = 6

    if dia is None:
        print("Semana invalida!")
        return
     
    for item in agenda[dia]: 
        if item["servico"] == servico:
            item["valor"] = valor
            item["status"] = status
    print("Serviço atualizado!")
    return agenda

def criar_horario(agenda, dia, hora):
    for dias in agenda:
        if dias["horario"] == hora:
            print("Horário já ocupado!!")
            return
    agenda.append({"dia": dia, "horário": hora, "status": "livre", "serviço": None ,"cliente": None})
    return agenda


def atuali_json(agenda_atualizada):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(agenda_atualizada, f, indent=4, ensure_ascii=False)




    #MENUS    
def exibir_agenda(agenda):
    for horaros in agenda:
        print(horaros)

def menu_sair():
    print("Digite 'v' para voltar ou 's' para sair!")
    opc = input("Opção [v/s]: ")
    return opc

def menu_de_edição():
    print("1 - A dicionar Horário")
    print("2 - Editar Horário")
    print("3 - Excluir Horário")
    print("2 - Sair")
    