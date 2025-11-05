import json
import os

ARQUIVO = "Bd_agenda.json"

class Db:

    def __init__(self, agenda=None):
        self.agenda = agenda if agenda is not None else []


    def carregar_agenda(self):
        if not os.path.exists(ARQUIVO):
            print("Arquivo não encontrado. Criando nova agenda.")
            return []

        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                dados = json.load(f) 
                print("Arquivo carregado!!")
                return dados
            
        except (FileNotFoundError, json.JSONDecodeError):
            print("Erro ao ler o arquivo. Iniciando agenda vazia.")    
            return []


    def atuali_json(self):
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(self.agenda, f, indent=4, ensure_ascii=False)
        print("Arquivo atualizado!")


        


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
    