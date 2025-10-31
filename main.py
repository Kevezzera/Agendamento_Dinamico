from Bd import agenda

def exibir_agenda(agenda):
    for dia, horarios in agenda.items():
        print(f"{dia.upper()}:")
        for bloco in horarios:
            print(f"  At.{bloco['id'].upper()} | {bloco['horário'].upper()} | STATUS: {bloco['status'].upper()}")

def exibir_horarios(agenda):
    for dias, horarios in agenda.items():
        print(f"        {dias.upper()}  ")
        print("Horários disponiveis:")
        for info in horarios:
            if info['status'] == "livre":
                print(f"id-{info['id']} | {info['horário']}")

while True:
    print("1 - Cliente")
    print("2 - Adm")
    opc = input("Escolha uma opção: ")

    if opc == "1":
        print("Digite seu nome")
        nome = str(input())
        print("Horários")
        exibir_horarios(agenda)
        #marcar horário
    elif opc == "2":
        print("Agenda da Semana")
        exibir_agenda(agenda)
        # Adicionarar horário
        # Remover horário
        