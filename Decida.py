import random

class decida_por_mim:
    def __init__(self):
        self.respostas = ['Com certeza, você deve fazer isso!', 'Não sei, você que sabe!', 'Não faça isso!', 'Acho que está na hora certa...']
        self.resp_continue = ' '

    def Iniciar(self):
        while True:
            input('Faça sua pergunta: ')
            print(random.choice(self.respostas))
            resp_continue = input('Deseja fazer outra pergunta? [S/N]')
            if resp_continue in 'nN':
                break
            while resp_continue not in 'sSnN':
                resp_continue = input('Responda apenas S ou N: ')
                if resp_continue in 'SsNn':
                    break


decida = decida_por_mim()
decida.Iniciar()