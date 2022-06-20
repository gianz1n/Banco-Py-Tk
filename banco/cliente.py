class Cliente:

    def __init__(self, nome:str, cpf:str, dataNasc:str):
        self.nome = nome
        self.cpf = cpf
        self.dataNasc = dataNasc

    def dados_cliente(self):
        print(f'Nome: {self.nome}, CPF: {self.cpf}, Data de nascimento: {self.dataNasc}')