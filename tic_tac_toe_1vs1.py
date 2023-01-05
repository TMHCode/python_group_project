import PySimpleGUI as sg


sg.ChangeLookAndFeel("DarkAmber")
# Create the layout of the game
layout = [[sg.Text("Tic-Tac-Toe", font=("Helvetica", 20))],
         [[sg.Button(" ", size=(5, 2), font=("Helvetica", 20), key=(i, j)) for i in range(3)]
             for j in range(3)],
             [sg.Text("", size=(5, 1)), sg.Button("New Game", size=(10, 2), font=("Helvetica", 20))]]

# Create the window
window = sg.Window('Tic-Tac-Toe', layout, size=(1100, 700), resizable=True, element_justification="center")

# Create a list to store the state of the game
board = [[0 for _ in range(3)] for _ in range(3)]

# Create a variable to store the current player (1 = O, -1 = X)
player = 1

# Main game loop
while True:
    # Read the window
    event, values = window.read()

    # If the window was closed, break out of the loop
    if event is None:
        break

    # If the event is a button press, update the board and switch players
    if isinstance(event, tuple):
        row, col = event
        if board[row][col] == 0:
            board[row][col] = player
            player = -player
            window[event].update("O" if player == 1 else "X", button_color=("black", "#FC9E47" if player == 1 else "#B8F1FF"))

    # If the event is the "New Game" button, reset the board and switch players
    if event == "New Game":
        player = -player
        for row in range(3):
            for col in range(3):
                board[row][col] = 0
                window[(row, col)].update(" ", button_color=("#FCCB53", "#FCCB53"))

    # Check if someone has won the game
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0:
            sg.popup(f"Player {'X' if board[row][0] == 1 else 'O'} has won!")
            player = -player
            for row in range(3):
                for col in range(3):
                    board[row][col] = 0
                    window[(row, col)].update(" ", button_color=("#FCCB53", "#FCCB53"))
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            sg.popup(f"Player {'X' if board[0][col] == 1 else 'O'} has won!")
            player = -player
            for row in range(3):
                for col in range(3):
                    board[row][col] = 0
                    window[(row, col)].update(" ", button_color=("#FCCB53", "#FCCB53"))
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        sg.popup(f"Player {'X' if board[0][0] == 1 else 'O'} has won!")
        player = -player
        for row in range(3):
            for col in range(3):
                board[row][col] = 0
                window[(row, col)].update(" ", button_color=("#FCCB53", "#FCCB53"))
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        sg.popup(f"Player {'X' if board[0][2] == 1 else 'O'} has won!")
        player = -player
        for row in range(3):
            for col in range(3):
                board[row][col] = 0
                window[(row, col)].update(" ", button_color=("#FCCB53", "#FCCB53"))


# Close the window
window.close()
