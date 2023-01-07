import PySimpleGUI as sg

# Set color scheme of the window
sg.ChangeLookAndFeel('DarkAmber')  # Add a touch of color


# --- Create all the different Layouts for the window here ---

# ----- LAYOUT for menu.py -----
def create_menu_layout():
    return [
                [sg.VPush()],
                [sg.Push(), sg.Text('Main Menu', size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2', justification='center'), sg.Push()],
                [sg.Push(), sg.Button('Tic-Tac-Toe', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
                [sg.Push(), sg.Button('Connect Four', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
                [sg.Push(), sg.Button('Rock-Paper-Scissors', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
                [sg.Push(), sg.Button('Statistics', size=(16, 2), border_width=10, font=('Helvetica', 18), button_color=('black', '#FC9E47'), pad=(10, 20)), sg.Push()],
                [sg.VPush()],
                [sg.Button('Quit',  size=(7, 2), font=('Helvetica', 16), border_width=10, button_color=('black', '#B8F1FF'), pad=(0, 0))]
    ]
# ----------


# ----- LAYOUT for connect_four.py -----
def create_connect_four_layout(col_count, row_count):
    return [
                [sg.VPush()],
                [sg.Push(), sg.Text('Connect Four', size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2', justification='center'), sg.Push()],
                *[[sg.Button(' ', button_color=('white', 'black'), size=(5, 2), pad=(0, 0), key=(r, c)) for c in range(col_count)] for r in range(row_count)],
                [sg.Push(), sg.Button('Back', size=(8, 2), button_color=('black', '#B8F1FF'), pad=(50, 15), border_width=8),
                    sg.Button('New Game', size=(14, 2), pad=(50, 15), border_width=10), sg.Push()],
                [sg.VPush()]
    ]
# ----------
