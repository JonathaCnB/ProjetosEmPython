# Simulador de Dado
import random

class SimuladorDeDados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de jogar novamente? [S/N] '

    def Iniciar(self):
        resposta = input(self.mensagem)
        while True:
            try:
                if resposta in 's' or resposta in 'sim':
                    self.GerarValorDoDado()
                elif resposta == 'não' or resposta == 'n':
                    print('Agradecemos a sua participação!')
                    # break
                else:
                    print('Favor digitar S ou N')
            except:
                print('Ocorreu um erro ao receber sua resposta!')
            respuser = input(self.mensagem)
            if respuser in 'nN':
                break
            while respuser not in 'SsNn':
                print('Favor digitar S! ou N')
                respuser = input(self.mensagem)

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDados()
simulador.Iniciar()
