
from admin import funções


def play_adm():
    agenda = funções.carregar_agenda()
    while True:
        print("1 - Exibir Agenda")
        print("2 - Editar Agenda")
        print("3 - Sair")
        opc = input("Opção: ")
        
        if opc == "1":
            while True:
                funções.exibir_agenda(agenda)
                opc = funções.menu_sair()
                if opc == "v":
                    break
                elif opc == "s":
                    exit()
                else:
                    print("Opção invalida!")
        elif opc == "2":
            while True:
                funções.menu_de_edição()
                opc = input("Escolha uma opção: ")

                #Adicionar Horário
                if opc == "1": 
                    dia = input("Semana: ")
                    horario = input("Horário:")
                    agenda_atualizada = funções.criar_horario(agenda, dia, horario)
                    funções.atuali_json(agenda_atualizada)
                    opc = funções.menu_sair()
                    if opc == "v":
                        break
                    elif opc == "s":
                        exit()
                    else:
                        print("Opção invalida!")
                
                #Editar Horário
                elif opc == "2": 
                    semana = input("Dia: ")
                    hora = input("hora: ")
                    valor = input("Valor: ")
                    status = input("Status: ")
                    agenda_atualizada = funções.editar_agenda(agenda, semana, hora, valor, status)
                    funções.atuali_json(agenda_atualizada)
                    opc = funções.menu_sair()
                    if opc == "v":
                        break
                    elif opc == "s":
                        exit()
                    else:
                        print("Opção invalida!")
                
                #Excluir Horário
                elif opc == "3":
                        break
                
                else:
                    print("Opção invalida!!!")
            
        elif opc == "3":
            break
        else: 
            print("Opção Invalida!!")
        


