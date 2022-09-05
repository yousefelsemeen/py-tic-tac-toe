"""Simple CLI Python Tic Tac Toe Game"""

class Board:
    """Main Board class
        Attributes:
            board
        Methods:
            print_board, update_board, check_winner, check_draw
    """
    def __init__(self):
        self.board = ['1', '2', '3',
                      '4', '5', '6',
                      '7', '8', '9']

    def print_board(self):
        print('\n ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('-' * 11)
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('-' * 11)
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    def update_board(self, position, symbol):
        if position < 1 or position > 9:
            print('Invalid position! Select another position.')
            return False

        # if a player selects position n, n-1 index should be updated
        # if the position is not already filled, update the board
        if self.board[position - 1]  not in 'XO':
            self.board[position - 1] = symbol
            return True

        # if the position is already filled, ask user to select another position
        print('Position already selected. Select another position.')
        return False

    # If three symbols appears in a row, returning True
    def check_winner(self, symbol):
        if (self.board[0:3] == [symbol, symbol, symbol]) or \
           (self.board[3:6] == [symbol, symbol, symbol]) or \
           (self.board[6:9] == [symbol, symbol, symbol]) or \
           (self.board[0:7:3] == [symbol, symbol, symbol]) or \
           (self.board[1:8:3] == [symbol, symbol, symbol]) or \
           (self.board[2:9:3] == [symbol, symbol, symbol]) or \
           (self.board[0:9:4] == [symbol, symbol, symbol]) or \
           (self.board[2:7:2] == [symbol, symbol, symbol]):
            return True
        return False

    # If all fields are selected and there is no winner, it's a draw
    def check_draw(self):
        for i in self.board:
            if i not in 'XO':
                return False
        return True


class Player:
    """Player class to manage players
        Attributes:
            symbol, name
    """
    def __init__(self, symbol):
        self.symbol = symbol
        self.name = input(f'Player selecting {self.symbol}, enter your name: ')


class Game:
    """Game class to manage game states
        Attributes:
            board, player1, player2, current_player
        Methods:
            play
    """
    def __init__(self):
        self.board = Board()

        self.player1 = Player('X')
        self.player2 = Player('O')

        self.current_player = self.player1

    # updating the play method
    def play(self):
        try:
            print("\033c", end="")
            self.board.print_board()
            # using an infinite loop to run the game
            while True:
                message = f'{self.current_player.name}, enter the position (1 - 9): '
                position = int(input(message))

                # the update_board() method return True if
                # the user selected position is not already filled
                if self.board.update_board(position, self.current_player.symbol):
                    print("\033c", end="")
                    self.board.print_board()

                    # checking winner each time after updating the board
                    if self.board.check_winner(self.current_player.symbol):
                        print(self.current_player.name, 'wins!')
                        break

                    # checking draw each time after updating the board
                    if self.board.check_draw():
                        print('Game is a draw!')
                        break

                    # changing current player when board is updated
                    self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        except:
            print('Invalid input! Enter a number between 1 and 9.')
            self.play()


if __name__=="__main__":
    game = Game()
    game.play()
