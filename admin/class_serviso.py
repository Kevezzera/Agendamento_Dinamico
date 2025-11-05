class Serviços:

    def __init__(self, data, hora, agenda, serviço=None, status="livre", promocao=None, cliente=None):
        self.data = data
        self.hora = hora
        self.serviço = serviço
        self.status = status
        self.promocao = promocao
        self.agenda = agenda
        self.cliente = cliente

    def novo_horario(self):
        for item in self.agenda:
            if item["data"] == self.data and item["hora"] == self.hora:
                print("Horário ja ocupado")
                return
        self.agenda.append({
            "data": self.data, 
            "hora": self.hora, 
            "status": self.status, 
            "serviço": self.serviço,
            "cliente": self.cliente,
            })
        
        return self.agenda
    
    def editar_horario(self):
        encontrado = False
        for item in self.agenda:
            if item["data"] == self.data and item["hora"] == self.hora:
                new_dat = input("Nova data: ")
                new_hora = input("Nova Hora: ")

                # Verifica se o novo horário já está ocupado
                for outro in self.agenda:
                    if outro["data"] == new_dat and outro["hora"] == new_hora and outro != item:
                        print("Novo horário já está ocupado.")
                        return


                item["data"] = new_dat
                item["hora"] = new_hora
                item["status"] = self.status
                item["serviço"] = self.serviço
                item["cliente"] = self.cliente
        
        if not encontrado:
            ("Horario não encontrado!!")

        return self.agenda
    
    def excluir_horario(self):
        for i, item in self.agenda:
            if item["data"] == self.data and item["hora"] == self.hora:
                del self.agenda[i]
                print("Horário excluido!")
                return self.agenda

        print("Horário não encontrado!!")
        return self.agenda
    
