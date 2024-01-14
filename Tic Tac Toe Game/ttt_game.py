class Square:

    def __init__(self):
        self._state = '-'

    def set_state(self, new_state):
        self._state = new_state

    def get_state(self):
        return self._state

    def __str__(self):
        return self._state

class Board:

    def __init__(self):
        
        self._board = []

        for i in range(3):
            row = []
            for j in range(3):
                row = row + [Square()]

            self._board = self._board + [row]

    def set_square_at(self, row, col, mark):

        self._board[row][col].set_state(mark)

    def get_square_at(self, row, col):

        return self._board[row][col].get_state()

    def check_diagonal_win(self, mark):

        for i in range(3):
            if self._board[i][i].get_state() != mark:
                return False
        
        return True

    def __str__(self):

        result = ""

        for row in range(3):

            for col in range(3):

                result = result + str(self._board[row][col]) + ' '

            result = result + '\n'

        return result



def play_game():

    player = "X"
    board = Board()

    winner = None
    i = 0

    while i < 9 and winner == None:

        if i % 2 == 0:
            player = "X"
        else:
            player = "O"

        print("It's", player, "turn!")
        print(board)

        row = int(input("Input row: "))
        col = int(input("Input col: "))

        #print("You placed", player, "at", row, col)
        if board.get_square_at(row, col) != "-":
            print("Invalid move!!! Why are you doing this to me")
            i = i - 1
        else:
            board.set_square_at(row, col, player)

        print(board.check_diagonal_win(player))
        if board.check_diagonal_win(player):
            winner = player
            print(player, "wins")

        print()

        i = i + 1

if __name__ == "__main__":

    play_game()