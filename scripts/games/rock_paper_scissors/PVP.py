import PySimpleGUI as sg

sg.ChangeLookAndFeel('DarkAmber')


def rps_pvp():
    p1_score = 0
    p2_score = 0

    layout = [
        [sg.Text('Player 1:')],
        [sg.Button('', image_filename='stone.png', button_color=('white', 'black'), size=(3, 1)),
         sg.Button('', image_filename='paper.png', button_color=('white', 'black'), size=(3, 1)),
         sg.Button('', image_filename='scissors.png', button_color=('white', 'black'), size=(3, 1))],
        [sg.Text('Player 2:')],
        [sg.Button('', image_filename='stone.png', button_color=('white', 'black'), size=(3, 1)),
         sg.Button('', image_filename='paper.png', button_color=('white', 'black'), size=(3, 1)),
         sg.Button('', image_filename='scissors.png', button_color=('white', 'black'), size=(3, 1))],
        [sg.Text('Player 1 Score: '), sg.Text(p1_score, key='p1_score')],
        [sg.Text('Player 2 Score: '), sg.Text(p2_score, key='p2_score')],
        [sg.Button('Reset'), sg.Button('Quit')]
    ]

    window = sg.Window('Rock-Paper-Scissors').Layout(layout)

    while True:
        event, values = window.Read()

        if event in (None, 'Quit'):
            break

        elif event == 'Reset':
            p1_score = 0
            p2_score = 0
            window.FindElement('p1_score').Update(p1_score)
            window.FindElement('p2_score').Update(p2_score)

        elif event in ('rock.png', 'paper.png', 'scissors.png'):
            # Get the choice of the second player
            event2, values2 = window.Read()

            # Compare player 1 choice with player 2 choice
            # and determine the winner
            if event == event2:
                sg.Popup('Tie!')
            elif (event == 'rock.png' and event2 == 'scissors.png') or (
                    event == 'paper.png' and event2 == 'rock.png') or (
                    event == 'scissors.png' and event2 == 'paper.png'):
                p1_score += 1
                sg.Popup('Player 1 wins!')
                window.FindElement('p1_score').Update(p1_score)
            else:
                p2_score += 1
                sg.Popup('Player 2 wins!')
                window.FindElement('p2_score').Update(p2_score)

    window.Close()


rps_pvp()
