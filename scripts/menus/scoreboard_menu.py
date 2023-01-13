import PySimpleGUI as sg

from scripts.layouts import create_scoreboard_menu_layout
from scripts.menus import main_menu


def main():

    # Create the layout
    layout = create_scoreboard_menu_layout()

    # Create the window
    window = sg.Window('Scoreboard', layout, size=(1100, 700), resizable=True)

    # Loop to handle events
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == 'C4':
            window['TTT_key'].update(visible=False)
            window['RPS_key'].update(visible=False)
            window['C4_key'].update(visible=True)
        elif event == 'RPS':
            window['TTT_key'].update(visible=False)
            window['C4_key'].update(visible=False)
            window['RPS_key'].update(visible=True)
        elif event == 'TTT':
            window['C4_key'].update(visible=False)
            window['RPS_key'].update(visible=False)
            window['TTT_key'].update(visible=True)

        if event in (sg.WIN_CLOSED, 'Back'):
            window.close()
            main_menu.main()
            break


    window.close()
