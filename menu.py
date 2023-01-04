import PySimpleGUI as sg

# Set the size of the window
sg.ChangeLookAndFeel('DarkAmber')  # Add a touch of color
sg.SetOptions(font=('Helvetica', 20))

# Create the layout
layout = [[sg.VPush()],
          [sg.Push(), sg.Text('Main Menu', size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2', justification='center'), sg.Push()],
          [sg.Push(), sg.Button('Tic-Tac-Toe', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
          [sg.Push(), sg.Button('Connect Four', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
          [sg.Push(), sg.Button('Rock-Paper-Scissors', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
          [sg.Push(), sg.Button('Statistics', size=(16, 2), border_width=10, font=('Helvetica', 18), button_color=('black', '#FC9E47'), pad=(10, 20)), sg.Push()],
          [sg.VPush()],
          [sg.Button('Exit',  size=(7, 2), font=('Helvetica', 16), border_width=10, button_color=('black', '#B8F1FF'), pad=(0, 0))]]


# Create the window
window = sg.Window('Menu', layout, size=(1100, 700), resizable=True)

# Loop to handle events
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    print(event, values)

window.close()