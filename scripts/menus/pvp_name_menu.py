import PySimpleGUI as sg

from scripts.games.connect_four import connect_four
from scripts.games.tic_tac_toe import tic_tac_toe_1vs1
from scripts.games.rock_paper_scissors import PVP
from scripts.menus import main_menu
from scripts.layouts import create_pvp_name_menu_layout


def main(game):

    # Create the layout
    layout = create_pvp_name_menu_layout(game)

    # Create the window
    window = sg.Window('Name Menu', layout, size=(1100, 700), resizable=True)

    # Loop to handle events
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Back'):
            window.close()
            main_menu.main()
            break
        elif event == 'Continue':
            if values['input_p1_name'] == '' or values['input_p2_name'] == '':
                sg.popup('Player name(s) can\'t be empty!')
                continue
            window.close()
            if game == 'Connect Four':
                connect_four.main([values['input_p1_name'], values['input_p2_name']])
            elif game == 'Rock-Paper-Scissors':
                PVP.main([values['input_p1_name'], values['input_p2_name']])
            elif game == 'Tic-Tac-Toe':
                tic_tac_toe_1vs1.main([values['input_p1_name'], values['input_p2_name']])
            break

    window.close()
