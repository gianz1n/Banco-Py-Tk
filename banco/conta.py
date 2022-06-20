from historico import Historico
class Conta:

    def __init__(self, titular, num: str, saldo=0.0):
        self.titular = titular.cpf
        self.num = num
        self.saldo = saldo
        self.Historico = Historico()

    def extrato(self):
        print(f'Cpf do titular: {self.titular}\nSaldo: {self.saldo}')
        self.Historico.historico_transacao()

    def depositar(self, valor):
        self.saldo += valor
        self.Historico.Historico.append(f'Depositou R${valor}')
        return self.saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.Historico.Historico.append(f'Sacou R${valor}')
            return self.saldo
        else: print('Saldo insuficiente!')

    def transferir(self, valor, destino):
        if valor <= self.saldo:
            self.saldo -= valor
            destino.saldo += valor
            self.Historico.Historico.append(f'Transferiu R${valor} para {destino.cpf}')
            return self.saldo
        else: print('Saldo insuficiente para transferir!')

    def recebe_transferencia(self, valor, origem):
        self.saldo += valor
        self.Historico.Historico.append(f'Recebeu R${valor} da conta {origem.cpf}')








