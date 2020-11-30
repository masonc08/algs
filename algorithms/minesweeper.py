"""
Leetcode 529
Runtime: 192 ms, faster than 23.29% of Python3 online submissions for Minesweeper.
Memory Usage: 16.7 MB, less than 38.52% of Python3 online submissions for Minesweeper.
"""


class Solution:
	dirs = [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]

	def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
		i, j = click
		if board[i][j] == 'M':
			board[i][j] = 'X'
		elif board[i][j] == 'E':
			nearby_bombs = self._numBombs(board, i, j)
			if nearby_bombs == 0:
				board[i][j] = 'B'
				for x, y in self.dirs:
					if 0 <= i+x < len(board) and 0 <= j+y < len(board[0]):
						self.updateBoard(board, [i+x, j+y])
			else:
				board[i][j] = str(nearby_bombs)
		return board

	def _numBombs(self, board, i, j):
		ttl = 0
		for x, y in self.dirs:
			if 0 <= i+x < len(board) and 0 <= j+y < len(board[0]) and board[i+x][j+y] == 'M':
				ttl += 1
		return ttl
