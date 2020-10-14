# Leetcode 79


class Solution:
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if Solution._dfs(board, i, j, word):
                    return True
        return False

    @staticmethod
    def _dfs(board, i, j, word, depth=0):
        if i == len(board) or \
                j == len(board[0]) or \
                i == -1 or j == -1 or \
                board[i][j] != word[depth]:
            return False
        # has to be part of the word chain at this point
        if depth == len(word) - 1:
            return True
        c = board[i][j]
        board[i][j] = ''
        sol = Solution._dfs(board, i + 1, j, word, depth + 1) or \
            Solution._dfs(board, i - 1, j, word, depth + 1) or \
            Solution._dfs(board, i, j + 1, word, depth + 1) or \
            Solution._dfs(board, i, j - 1, word, depth + 1)
        board[i][j] = c
        return sol



