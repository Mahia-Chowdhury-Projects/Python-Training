import pygame as pg

# constants defining our colours
PURPLE = (80, 0, 130)
LILAC = (215, 175, 237)

class Square:
    """
    Class for a tic tac toe square
    """

    def __init__(self, screen):
        """
        Constructor for square class
        """
        self._state = '-'
        self._screen = screen

    def set_state(self, new_state):
        """
        Set state of the square
        """
        self._state = new_state

    def get_state(self):
        """
        Get the state of the square
        """
        return self._state

    def draw(self, x, y, width=200, height=200):
        """
        Draw the square
        """
        pg.draw.rect(self._screen, PURPLE, (x, y, width, height), 2)
        font = pg.font.SysFont('American Typewriter', 60)
        self._screen.blit(font.render(self._state, True, PURPLE), (x + width//2 - 30, y + height//2 - 30))

    def __str__(self):
        return self._state

class Board:
    """
    Class that represents the tic tac toe board
    """

    def __init__(self, screen):
        """
        Constructor for Board class
        """
        self._board = []
        self._screen = screen

        # create 9 squares on a 3x3 grid
        for i in range(3):
            row = []
            for j in range(3):
                row = row + [Square(self._screen)]

            self._board = self._board + [row]

    def set_square_at(self, row, col, mark):
        """
        Set the state of a specific square
        """

        self._board[row][col].set_state(mark)

    def get_square_at(self, row, col):
        """
        Get the state of a specific square
        """

        return self._board[row][col].get_state()

    def check_diagonal_win(self, mark):
        """
        Check if we have a winner along the diagonal
        """

        for i in range(3):
            if self._board[i][i].get_state() != mark:
                return False
        
        return True


    def draw(self):
        """
        Draw the board
        """
        
        for row in range(3):
            for col in range(3):
                self._board[row][col].draw(row*200, col*200)

    def find_square(self, xcoord, ycoord):
        """
        Figure out the row, col of a specific x-coordinate y-coordinate from a mouse click
        """

        for row in range(3):
            for col in range(3):
                if row*200 < xcoord < (row+1)*200 and col*200 < ycoord < (col+1)*200:
                    return row, col

    def __str__(self):

        result = ""

        for row in range(3):

            for col in range(3):

                result = result + str(self._board[row][col]) + ' '

            result = result + '\n'

        return result



def play_game():
    """
    Function that implements the full gameplay of tic tac toe
    """

    player = "X"
    i = 0
    pg.init()
    screen = pg.display.set_mode((600, 600))
    board = Board(screen)
    running = True

    # keep running the game until the user asks us to quit
    while running:

        events = pg.event.get()

        # check all events and see if it was a quit event or mouse click event
        for event in events:

            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                position = pg.mouse.get_pos()
                row, col = board.find_square(position[0], position[1])

                if board.get_square_at(row, col) != "-":
                    print("Invalid move!!! Why are you doing this to me")
                else:
                    board.set_square_at(row, col, player)
                    i = i + 1
                    if i % 2 == 0:
                        player = "X"
                    else:
                        player = "O"

                if board.check_diagonal_win(player):
                    print(player, "wins")

        screen.fill(LILAC)
        board.draw()
        
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":

    play_game()