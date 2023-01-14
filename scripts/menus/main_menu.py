import PySimpleGUI as sg

from scripts.layouts import create_main_menu_layout
from scripts.menus import mode_menu, scoreboard_menu
"""
This is the main menu file.
"""

# Set the font size
sg.SetOptions(font=('Helvetica', 15))


def main():
    """
    This is the main function of the main menu.
    It shows the Main Menu, where the user can chose one of three games to play or to see the scoreboard.
    It loads the main-menu-layout and window and determines the button events for this menu.

    :return:  NO return parameter.
    """
    # Create the layout
    layout = create_main_menu_layout()

    # Create the window
    window = sg.Window('Main Menu', layout, size=(1200, 800), resizable=True)

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

