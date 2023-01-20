import PySimpleGUI as sg

from games.connect_four import connect_four
from games.tic_tac_toe import tic_tac_toe_1vs1
from games.rock_paper_scissors import rps_pvp
from menus import main_menu
from layouts import create_pvp_name_menu_layout
"""
This is the PVP name menu file.
"""


def main(game: str):
    """
    This is the main function of the PVP (Player vs. Player) name menu.
    It shows the PVP Name Menu, where the users must enter their names in order to play the game.
    It loads the pvp-name-menu-layout and window and determines the button events for this menu.

    :param game: (str)  name of the game. Can be 'ttt', 'c4' or 'rps'
    :return:  NO return parameter.
    """
    layout = create_pvp_name_menu_layout(game)                                  # create the layout

    window = sg.Window('Name Menu', layout, size=(1200, 800), resizable=True)   # create the window

    # Main Loop
    while True:
        event, values = window.read()                           # get the button click event
        if event in (sg.WIN_CLOSED, 'Back'):                    # when Back button is pressed, go back to the main menu
            window.close()
            main_menu.main()
            break
        elif event == 'Continue':                                               # when Continue button is pressed
            if values['input_p1_name'] == '' or values['input_p2_name'] == '':  # check if names are not empty
                sg.popup('Player name(s) can\'t be empty!')
                continue
            elif values['input_p1_name'] == values['input_p2_name']:            # check if names are not the same
                sg.popup('Player names can\'t be identical!')
                continue
            elif len(values['input_p1_name']) > 10 or len(values['input_p2_name']) > 10:    # check that the names are
                sg.popup('Player names can\'t be longer then 10 characters!')               # not too long
                continue
            window.close()
            if game == 'Connect Four':                          # depending on the game that was selected earlier
                connect_four.main([values['input_p1_name'], values['input_p2_name']])   # go to that game
            elif game == 'Rock-Paper-Scissors':
                rps_pvp.main([values['input_p1_name'], values['input_p2_name']])
            elif game == 'Tic-Tac-Toe':
                tic_tac_toe_1vs1.main([values['input_p1_name'], values['input_p2_name']])
            break

    window.close()                                                                      # close the window
