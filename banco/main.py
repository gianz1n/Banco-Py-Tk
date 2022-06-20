from cliente import Cliente
from conta import Conta

C1 = Cliente(nome='Exemplo', Cpf='00000000000', dataNasc='00/00/0000')
CT = Conta(C1, num='000-0')

C2 = Cliente(nome='Exemplo2', Cpf='00000000001', dataNasc='00/00/0001')
CT2 = Conta(C2, num='000-1')

CT.depositar(500)
CT.transferir(50, CT2)

CT.extrato()
CT2.extrato()