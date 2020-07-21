# Simulador de Dado
import random
import PySimpleGUI as sg

class SimuladorDeDados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        #self.mensagem = 'Você gostaria de jogar novamente? [S/N] '
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def Iniciar(self):
        # Cria uma janela
        self.janela = sg.Window('Simular de Dado', layout=self.layout)
        # Ler os valores
        while True:
            self.eventos, self.valores = self.janela.Read()
            # Fazer alguma coisa com esses valores
            try:
                if self.eventos == 'Sim' or self.eventos == 's':
                    self.GerarValorDoDado()
                elif self.eventos == 'Não' or self.eventos == 'n':
                    print('Agradecemos a sua participação!')
                    break
                else:
                    print('Por favor digitar Sim ou Não')
            except:
                print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDados()
simulador.Iniciar()
