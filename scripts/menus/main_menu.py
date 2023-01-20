import PySimpleGUI as sg

from layouts import create_main_menu_layout
from menus import mode_menu, scoreboard_menu
"""
This is the main menu file.
"""

sg.SetOptions(font=('Helvetica', 15))   # set the font size


def main():
    """
    This is the main function of the main menu.
    It shows the Main Menu, where the user can chose one of three games to play or to see the scoreboard.
    It loads the main-menu-layout and window and determines the button events for this menu.

    :return:  NO return parameter.
    """
    layout = create_main_menu_layout()                                          # create the layout

    window = sg.Window('Main Menu', layout, size=(1200, 800), resizable=True)   # create the window

    # Main Loop
    while True:
        event, values = window.read()                           # get the button click event
        if event in (sg.WIN_CLOSED, 'Quit'):                    # when Quit button is pressed, go back to the main menu
            break
        elif event == 'Connect Four':                           # for each of the buttons,
            window.close()
            mode_menu.main(event)                               # open the mode menu and give it the name of the game
            break
        elif event == 'Tic-Tac-Toe':
            window.close()
            mode_menu.main(event)
            break
        elif event == 'Rock-Paper-Scissors':
            window.close()
            mode_menu.main(event)
        elif event == 'Statistics':                             # if the statistic button is pressed,
            window.close()
            scoreboard_menu.main()                              # open the scoreboard menu

    window.close()                                              # close the window

