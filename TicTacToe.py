import pprint


class TicTacToe:
    def __init__(self):
        self._empty = 0
        self._X = 1
        self._O = 2
        self._w, self._h = 3, 3
        self._board = [[self._empty for y in range(self._h)] for x in range(self._w)]

    @property
    def playerX(self):
        return self._X

    @property
    def playerO(self):
        return self._O

    @property
    def empty(self):
        return self._empty

    def board_for_learning(self, player):
        data = [self._empty for i in range(self._w * self._h * 2)]

        offset = 0 # Handles if the board should be represented in the eyes of X or O.

        if player == self._O:
            offset = self._w * self._h
        else:
            offset = 0

        for x in range(self._w):
            for y in range(self._h):
                data[offset + x * self._w + y] = 1 if self._board[y][x] == self._X else 0

        if player == self._X:
            offset = self._w * self._h
        else:
            offset = 0
        for x in range(self._w):
            for y in range(self._h):
                data[offset + y * self._h + x] = 1 if self._board[y][x] == self._O else 0

        return data

    def playX(self, x, y):
        self.setField(x, y, self._X)

    def playO(self, x, y):
        self.setField(x, y, self._O)

    def isFieldAvailable(self, x, y):
        return self._board[y][x] == self._empty

    def setField(self, x, y, player):
        value = self._board[y][x]
        if value == 0:
            self._board[y][x] = player

    def isWinner(self, player):
        horizontally = [player for x in range(self._w)]
        vertically = [player for y in range(self._h)]

        for x in range(self._w):
            row = self._board[x]
            if row == horizontally:
                return player

        # Rearrange board to get a column in an array
        row = [self._empty for y in range(self._w)]
        for x in range(self._w):
            for y in range(self._h):
                row[y] = self._board[y][x]
            if row == vertically:
                return player

        if self._board[0][0] == player and self._board[1][1] == player and self._board[2][2] == player:
            return player

        if self._board[0][2] == player and self._board[1][1] == player and self._board[2][0] == player:
            return player

    def isWinnerX(self):
        return self.isWinner(self._X)

    def isWinnerO(self):
        return self.isWinner(self._O)

    def isFinished(self):
        if self.isWinnerX():
            return True
        if self.isWinnerO():
            return True
        for row in range(self._h):
            for col in range(self._w):
                if self._board[row][col] == self._empty:
                    return False
        return True # Tie

    @property
    def get_pretty_board(self):
        b = ' '.join('-' for x in range(self._w))
        for y in range(self._w):
            b += '\n'
            for x in range(self._w):
                b += str(self._board[y][x])
            b = b.replace(str(self._X), 'X')
            b = b.replace(str(self._O), 'O')
            b = b.replace(str(self._empty), ' ')
        return b
