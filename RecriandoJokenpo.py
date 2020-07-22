from random import randint as ra
from random import choice as ch
import PySimpleGUI as sg
sg.ChangeLookAndFeel('BlueMono')

layout = [[sg.Text('Vamos Jogar?', font=('Helvetica', '30'), background_color='white', justification='center', size=(25, 1))],
          [sg.Button('Pedra', button_color=('white', 'black'), key='Pedra', size=(10, 5), pad=(10, 20)),
           sg.Button('Papel', button_color=('white', 'gray'), key='Papel', size=(10, 5), pad=(10, 20)),
           sg.Button('Tesoura', button_color=('yellow', 'black'), key='Tesoura', size=(10, 5), pad=(10, 20))],
          [sg.T(key='Resultado', size=(7, 1), font=('Helvetica', '25'), justification='left'), sg.T('X', size=(1, 1), font=('Helvetica', '35', 'bold'), justification='center'),
           sg.T(key='RespComputador', size=(7, 1), font=('Helvetica', '25'), justification='r')],
          [sg.Text('Score', font=('Helvetica', '30'), background_color='white', justification='center', size=(25, 1))],
          [sg.T(key='Resultado1', size=(17, 1), font=('Helvetica', '25'), justification='left')]

]

window = sg.Window("Jokenpo", layout, default_element_size=(40,1), text_justification='r', auto_size_text=False, auto_size_buttons=False,
                   default_button_element_size=(40, 1), finalize=True, size=(360, 400))

regra = ["Pedra", "Papel", "Tesoura"]
npc = ch(regra)
print(npc)
playerWin = empate = computador = 0

while True:
    event, values = window.read()
    print(event)
    window['Resultado'].Update(event)
    window['RespComputador'].Update(npc)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event in 'Pedra' and npc in 'Tesoura':
        window['Resultado1'].Update('Player Win')
        playerWin += 1
    elif event in 'Papel' and npc in 'Pedra':
        window['Resultado1'].Update('Player Win!')
        playerWin += 1
    elif event in 'Tesoura' and npc in 'Papel':
        window['Resultado1'].Update('Player Win!')
        playerWin += 1
    elif event == npc:
        window['Resultado1'].Update('Empate')
        empate += 1
    else:
        window['Resultado1'].Update('Computador Win')
        computador += 1


window.close()


