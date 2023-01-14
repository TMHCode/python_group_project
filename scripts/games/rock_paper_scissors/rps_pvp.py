import PySimpleGUI as sg

from scripts.layouts import create_RPS_pvp_layout
from scripts.menus import main_menu
from scripts.statistics.stats import save_score


def main(p_names: list):
    sg.theme('DarkAmber')
    game_name = 'rps'

    layout = create_RPS_pvp_layout(p_names)
    window = sg.Window('Rock-Paper-Scissors', layout, size=(1200, 800), resizable=True, element_justification='center')

    p1 = 'p1'
    p2 = 'p2'

    while True:
        event, values = window.Read()
        if event in (None, 'Back'):
            window.close()
            main_menu.main()
            break

        elif event == 'p1-rock':
            p1 = 'rock'

        elif event == 'p1-paper':
            p1 = 'paper'

        elif event == 'p1-scissors':
            p1 = 'scissors'

        elif event == 'p2-rock':
            p2 = 'rock'

        elif event == 'p2-paper':
            p2 = 'paper'

        elif event == 'p2-scissors':
            p2 = 'scissors'

        elif event == 'Show':
            if p1 == p2:
                save_score(p_names, "Draw", 0, game_name)
                save_score(p_names, "Draw", 1, game_name)
                sg.Popup('Draw')
                p1 = 'p1'
                p2 = 'p2'

            elif (p1 == 'rock' and p2 == 'scissors') or \
                    (p1 == 'scissors' and p2 == 'paper') or (
                    p1 == 'paper' and p2 == 'rock'):
                save_score(p_names, "Win", 0, game_name)
                save_score(p_names, "Lose", 1, game_name)
                sg.Popup(f'{p_names[0]} wins!', text_color='#6F3AFC')
                p1 = 'p1'
                p2 = 'p2'

            elif p1 == 'p1':
                sg.Popup(f'Please choose a weapon {p_names[0]}!')

            elif p2 == 'p2':
                sg.Popup(f'Please choose a weapon {p_names[1]}!')

            else:
                save_score(p_names, "Win", 1, game_name)
                save_score(p_names, "Lose", 0, game_name)
                sg.Popup(f'{p_names[1]} wins!', text_color='#B8F1FF')
                p1 = 'p1'
                p2 = 'p2'

    window.Close()

