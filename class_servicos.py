class Servicos:

    def __init__(self, servico, valor):
        self.nome = servico
        self.telefone = valor
        
    def exibir_servico(self):
        print("Valores e Promoções da Semana!!!")
        print(f"{self.servico} | {self.valor}")

    def salvar_info(self):
        #salvar as informações no banco de dados
        pass
    
    def editar_info(self):
        pass

    def excluir_info(self):
        pass
