
from admin import class_arquivo


def play_adm():
    agenda = class_arquivo.carregar_agenda()
    while True:
        print("1 - Exibir Agenda")
        print("2 - Editar Agenda")
        print("3 - Sair")
        opc = input("Opção: ")
        
        if opc == "1":
            while True:
                class_arquivo.exibir_agenda(agenda)
                opc = class_arquivo.menu_sair()
                if opc == "v":
                    break
                elif opc == "s":
                    exit()
                else:
                    print("Opção invalida!")
        elif opc == "2":
            while True:
                class_arquivo.menu_de_edição()
                opc = input("Escolha uma opção: ")

                #Adicionar Horário
                if opc == "1": 
                    dia = input("Semana: ")
                    horario = input("Horário:")
                    agenda_atualizada = class_arquivo.criar_horario(agenda, dia, horario)
                    class_arquivo.atuali_json(agenda_atualizada)
                    opc = class_arquivo.menu_sair()
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
                    agenda_atualizada = class_arquivo.editar_agenda(agenda, semana, hora, valor, status)
                    class_arquivo.atuali_json(agenda_atualizada)
                    opc = class_arquivo.menu_sair()
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
        


