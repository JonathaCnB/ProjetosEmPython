import PySimpleGUI as sg

'''theme_name_list = sg.theme_list()
print(theme_name_list)
sg.theme('Reddit')
layout = [
    [sg.Text('My Window')],
    [sg.Input(key='-IN-')],
    [sg.Text(size=(20,1), key='-OUT-')],
    [sg.Button('GO'), sg.Button('Exit')] ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        sg.popup_ok_cancel('Você tem certeza que quer sair?\nGame Over!')
        break
    if event == 'Go':
        window['-OUT-'].update(values['-IN-'])
window.close()

# Escolha do tema

sg.theme('Dark Brown')


layout = [[sg.Text('Theme Browser')],
          [sg.Text('Click a Theme color to see demo window')],
          [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
          [sg.Button('Exit')]]

window = sg.Window('Theme Browser', layout)

while True:  # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    sg.theme(values['-LIST-'][0])
    sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

window.close()

# Cronometro

sg.theme('DarkBrown1')

layout = [  [sg.Text('Stopwatch', size=(20, 2), justification='center')],
            [sg.Text(size=(10, 2), font=('Helvetica', 20), justification='center', key='-OUTPUT-')],
            [sg.T(' ' * 5), sg.Button('Start/Stop', focus=True), sg.Quit()]]

window = sg.Window('Stopwatch Timer', layout)

timer_running, counter = True, 0

while True:                                  # Event Loop
    event, values = window.read(timeout=10)  # Please try and use as high of a timeout value as you can
    if event in (sg.WIN_CLOSED, 'Quit'):     # if user closed the window using X or clicked Quit button
        break
    elif event == 'Start/Stop':
        timer_running = not timer_running
    if timer_running:
        window['-OUTPUT-'].update('{:02d}:{:02d}.{:02d}'.format((counter // 100) // 60, (counter // 100) % 60, counter % 100))
        counter += 1
window.close()

'''
sg.ChangeLookAndFeel('Dark')
sg.SetOptions(element_padding=(0, 0))

layout = [
    [sg.T('User:', pad=((3, 0), 0)), sg.OptionMenu(values=('User 1', 'User 2'), size=(20, 1)), sg.T('0', size=(8, 1))],
    [sg.T('Customer:', pad=((3, 0), 0)), sg.OptionMenu(values=('Customer 1', 'Customer 2'), size=(20, 1)),
     sg.T('1', size=(8, 1))],
    [sg.T('Notes:', pad=((3, 0), 0)), sg.In(size=(44, 1), background_color='white', text_color='black')],
    [sg.Button('Start', button_color=('white', 'black'), key='Start'),
     sg.Button('Stop', button_color=('white', 'black'), key='Stop'),
     sg.Button('Reset', button_color=('white', 'firebrick3'), key='Reset'),
     sg.Button('Submit', button_color=('white', 'springgreen4'), key='Submit')]
    ]

window = sg.Window("Time Tracker", layout, default_element_size=(12, 1), text_justification='r', auto_size_text=False,
                   auto_size_buttons=False,
                   default_button_element_size=(12, 1))
window.Finalize()
window['Stop'].update(disabled=True)
window['Reset'].update(disabled=True)
window['Submit'].update(disabled=True)
recording = have_data = False
while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        exit(69)
    if event is 'Start':
        window['Start'].update(disabled=True)
        window['Stop'].update(disabled=False)
        window['Reset'].update(disabled=False)
        window['Submit'].update(disabled=True)
        recording = True
    elif event is 'Stop' and recording:
        window['Stop'].update(disabled=True)
        window['Start'].update(disabled=False)
        window['Submit'].update(disabled=False)
        recording = False
        have_data = True
    elif event is 'Reset':
        window['Stop'].update(disabled=True)
        window['Start'].update(disabled=False)
        window['Submit'].update(disabled=True)
        window['Reset'].update(disabled=False)
        recording = False
        have_data = False
    elif event is 'Submit' and have_data:
        window['Stop'].update(disabled=True)
        window['Start'].update(disabled=False)
        window['Submit'].update(disabled=True)
        window['Reset'].update(disabled=False)
        recording = False




layout = [[sg.Text('My To Do List', font='Helvetica 15')]]
layout += [[sg.Text(f'{i}. '), sg.CBox(''), sg.Input()] for i in range(1, 6)]
layout += [[sg.Button('Save'), sg.Button('Load'), sg.Button('Exit')]]

window = sg.Window('To Do List Example', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event == "Save":
        window.save_to_disk('mywindow.out')
    elif event == "Load":
        window.load_from_disk('mywindow.out')
window.close()