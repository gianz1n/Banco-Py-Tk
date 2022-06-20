class Historico:

    def __init__(self):
        self.Historico = []

    def historico_transacao(self):
        print('Seu historico de transações: ')
        for i in self.Historico:
            print('-', i)