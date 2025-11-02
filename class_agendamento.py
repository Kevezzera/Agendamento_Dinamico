class Agendamento:

    def __init__(self, nome, telefone, email, servico):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.servico = servico

    def agendar(self):
        print("Serviço agendado!")
        pass
    
    def remarcar(self):
        print("Serviço remarcado!")
        pass

    def cancelar(self):
        print("Serviço cncelado!")
        pass

agendar = Agendamento(nome="nome", telefone="telefone", email="email", servico="servico")