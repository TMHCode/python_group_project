import PySimpleGUI as sg

from scripts.menus import pvp_name_menu, pvb_name_menu
from scripts.layouts import create_mode_menu_layout
from scripts.menus import main_menu


def main(game):
    # Create the layout
    layout = create_mode_menu_layout(game)

    # Create the window
    window = sg.Window('Menu', layout, size=(1100, 700), resizable=True)

    # Loop to handle events
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Back'):

            window.close()
            main_menu.main()
            break
        elif event == 'Player vs. Player':
            window.close()
            pvp_name_menu.main(game)
            break
        elif event == 'Player vs. Bot':
            window.close()
            pvb_name_menu.main(game)
            break

    window.close()
