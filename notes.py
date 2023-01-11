####
"""
todo:
- Win/Draw pop-ups
- show player names and color
- show number of turns

- :( Bot :( :(


BOT CODE

"""
###
import random


class ConnectFour:
    def __init__(self):
        self.board = [['.' for _ in range(7)] for _ in range(6)]
        self.player = 'R'
        self.bot = 'Y'

    def drop_piece(self, col):
        for row in range(5, -1, -1):
            if self.board[row][col] == '.':
                self.board[row][col] = self.player
                return

    def switch_player(self):
        if self.player == 'R':
            self.player = self.bot
        else:
            self.player = 'R'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def check_winner(self):
        # check horizontal
        for row in range(6):
            for col in range(4):
                if self.board[row][col] != '.' and \
                        self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][
                    col + 3]:
                    return self.board[row][col]

        # check vertical
        for row in range(3):
            for col in range(7):
                if self.board[row][col] != '.' and \
                        self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == \
                        self.board[row + 3][col]:
                    return self.board[row][col]

        # check diagonal
        for row in range(3):
            for col in range(4):
                if self.board[row][col] != '.' and \
                        self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == \
                        self.board[row + 3][col + 3]:
                    return self.board[row][col]

        for row in range(3):
            for col in range(4):
                if self.board[row][col + 3] != '.' and \
                        self.board[row][col + 3] == self.board[row + 1][col + 2] == self.board[row + 2][col + 1] == \
                        self.board[row + 3][col]:
                    return self.board[row][col + 3]

    def bot_play(self):
        while True:
            if self.player == self.bot:
                bot_col = random.randint(0, 6)
                self.drop_piece(bot_col)
                print(f'Bot choose {bot_col} column')
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    print("Player " + winner + " wins!")
                    break
                self.switch_player()
            else:
                self.print_board()
                col = int(input("Player " + self.player + ", choose a column (0-6):"))
                self.drop_piece(col)
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    print("Player " + winner + " wins!")
                    break
                self.switch_player()


game = ConnectFour()
game.bot_play()

