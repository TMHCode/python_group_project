import PySimpleGUI as sg

from scripts.layouts import create_main_menu_layout
from scripts.menus import mode_menu, scoreboard_menu

# Set the size of the window
sg.SetOptions(font=('Helvetica', 20))


def main():
    # Create the layout
    layout = create_main_menu_layout()

    # Create the window
    window = sg.Window('Main Menu', layout, size=(1100, 700), resizable=True)

    # Loop to handle events
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Quit'):
            break
        elif event == 'Connect Four':
            window.close()
            mode_menu.main(event)
            break
        elif event == 'Tic-Tac-Toe':
            window.close()
            mode_menu.main(event)
            break
        elif event == 'Rock-Paper-Scissors':
            window.close()
            mode_menu.main(event)
        elif event == 'Statistics':
            window.close()
            scoreboard_menu.main()

    window.close()

