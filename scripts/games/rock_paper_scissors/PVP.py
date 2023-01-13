import PySimpleGUI as sg

from scripts.layouts import create_RPS_pvp_layout


def main(p_names: list):
    sg.theme('DarkAmber')

    layout = create_RPS_pvp_layout(p_names)
    window = sg.Window('Rock-Paper-Scissors', layout, size=(1100, 650), resizable=True, element_justification='center')

    p1 = ''
    p2 = ''

    while True:
        event, values = window.Read()
        if event in (None, 'Exit'):
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
        elif event == 'Play':
            if p1 == p2:
                sg.Popup('Draw')
            elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (
                    p1 == 'paper' and p2 == 'rock'):
                sg.Popup('Player 1 wins!')
            else:
                sg.Popup('Player 2 wins!')

    window.Close()


if __name__ == '__main__':
    p_names = ['john', 'bot']
    main(p_names)
