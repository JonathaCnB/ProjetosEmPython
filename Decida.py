import random
import PySimpleGUI as sg
import time

class decida_por_mim:
    def __init__(self):
        self.respostas = ['Com certeza, você deve fazer isso!', 'Não sei, você que sabe!', 'Não faça isso!', 'Acho que está na hora certa...']
        self.resp_continue = ' '

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Faça sua pergunta: ')],
            [sg.Input()],
            [sg.Output(size=(20, 10))],
            [sg.Button('Decida')], [sg.CloseButton('Sair')]
        ]
        # Criar Janela
        self.janela = sg.Window('Decida!',layout=layout)
        while True:
            # Ler o valores
            self.eventos, self.valores = self.janela.Read()
            if self.eventos == 'Decida':
                print(random.choice(self.respostas))


decida = decida_por_mim()
decida.Iniciar()