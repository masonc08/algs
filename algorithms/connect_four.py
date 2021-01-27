import copy


class ConnectFour:
    def __init__(self, m=6, n=7):
        self.board = [[-1]*n for _ in range(m)]
        self.empty = [m-1]*n
        self.m, self.n = m, n

    def yellow_plays(self, j):
        return self._play(j, 0)

    def red_plays(self, j):
        return self._play(j, 1)

    def get_board(self):
        return copy.deepcopy(self.board)

    def _play(self, j, player):
        if self.empty[j] == -1:
            raise Exception("You can't place your tile here")
        i = self.empty[j]
        self.board[i][j] = player
        self.empty[j] -= 1
        return self._check_win(i, j)

    def _check_win(self, i, j):
        return any((
            self._check_row(i, j),
            self._check_column(i, j),
            self._check_diags_bltr(i, j)
        ))

    def _check_row(self, i, j):
        count = 1
        l = r = j
        row = self.board[i]
        while count < 4 and l >= 1 and row[l] == row[l-1]:
            count += 1
            l -= 1
        while count < 4 and r < self.n-1 and row[r] == row[r+1]:
            count += 1
            r += 1
        return count == 4

    def _check_column(self, i, j):
        count = 1
        u = d = i
        col = lambda i: self.board[i][j]
        while count < 4 and u >= 1 and col(u) == col(u-1):
            count += 1
            u -= 1
        while count < 4 and d < self.m-1 and col(d) == col(d+1):
            count += 1
            d += 1
        return count == 4

    def _check_diags_bltr(self, i, j):
        count = 1
        i1, j1 = i, j
        while count < 4 and i1 < self.m-1 and j >= 1 and \
            self.board[i][j] == self.board[i+1][j-1]:
            count += 1
            i1, j1 = i1+1, j1-1
        i1, j1 = i, j
        while count < 4 and i1 >= 1 and j < self.n-1 and \
            self.board[i][j] == self.board[i-1][j+1]:
            count += 1
            i1, j1 = i1-1, j1+1
        if count == 4:
            return True
        count = 1
        i1, j1 = i, j
        while count < 4 and i1 < self.m-1 and j < self.n-1 and \
            self.board[i][j] == self.board[i+1][j+1]:
            count += 1
            i1, j1 = i1+1, j1+1
        i1, j1 = i, j
        while count < 4 and i1 >= 1 and j >= 1 and \
            self.board[i][j] == self.board[i-1][j-1]:
            count += 1
            i1, j1 = i1-1, j1-1
        return count == 4

game = ConnectFour()
print(game.red_plays(3))
print(game.get_board())
print(game.red_plays(3))
print(game.get_board())
print(game.red_plays(3))
print(game.get_board())
print(game.red_plays(3))
print(game.get_board())
