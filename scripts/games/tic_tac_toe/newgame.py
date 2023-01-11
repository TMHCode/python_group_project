board = [[" " for _ in range(3)] for _ in range(3)]


def draw_board():
    print("  0 1 2")
    for i, row in enumerate(board):
        print(i, *row)


def get_move(player):
    while True:
        try:
            row = int(input(f"{player}, enter row: "))
            col = int(input(f"{player}, enter col: "))
            if row in [0, 1, 2] and col in [0, 1, 2]:
                if board[row][col] == " ":
                    board[row][col] = player
                    return
                else:
                    print("That space is already occupied. Please try again.")
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")


def has_won(player):
    for row in board:
        if row == [player, player, player]:
            return True
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def is_draw():
    for row in board:
        if " " in row:
            return False
    return True


def main():
    while True:
        player1 = input("Player 1, choose your marker (X or O): ").upper()
        if player1 == "X":
            player2 = "O"
            break
        elif player1 == "O":
            player2 = "X"
            break
        else:
            print("Invalid marker. Please choose X or O.")

    while True:
        draw_board()
        get_move(player1)
        if has_won(player1):
            print(f"{player1} has won!")
            break
        elif is_draw():
            print("The game is a draw.")
            break
        draw_board()
        get_move(player2)
        if has_won(player2):
            print(f"{player2} has won!")
            break
        elif is_draw():
            print("The game is a draw.")
            break

    play_again = input("Would you like to play again (Y/N)? ")
    if play_again.upper() == "Y":
        for row in board:
            for i in range(3):
                row[i] = " "
        main()
    else:
        print("Thank you for playing!")


main()

