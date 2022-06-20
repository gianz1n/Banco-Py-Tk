from cliente import *
from conta import *

while input('Quer continuar a operação? \n') == 'S':

    operador1 = input('1-Realizar cadastro\n2-Entrar\n')
    if operador1 == '1':
        C1 = Cliente(nome=input('Nome:\n'), cpf=input('Cpf:\n'), dataNasc=input('Data de nascimento:\n'))
        CT = Conta(C1, num=input('Número da conta:\n'))

    elif operador1 == '2':
        operador2 = input('1-Depositar\n2-Sacar\n3-Extrato\n4-Sair\n')

        while operador2 != 4:
            if operador2 == '1':
                x1 = float(input('Valor a ser depositado: R$\n'))
                CT.depositar(x1)
                operador2 = input('1-Depositar\n2-Sacar\n3-Extrato\n4-Sair\n')

            elif operador2 == '2':
                x1 = float(input('Valor a ser sacado: R$\n'))
                CT.sacar(x1)
                operador2 = input('1-Depositar\n2-Sacar\n3-Extrato\n4-Sair\n')

            elif operador2 == '3':
                CT.extrato()
                cont2 = input('1-Depositar\n2-Sacar\n3-Extrato\n4-Sair\n')

            else:
                print('Obrigado, volte sempre!')
                break




