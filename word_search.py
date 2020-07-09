# Leetcode 79


class Solution:
    def exist(self, board, word):
        for i in range(len(word)):
            for j in range(len(word[0])):
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
        down = Solution._dfs(board, i + 1, j, word, depth+1)
        up = Solution._dfs(board, i - 1, j, word, depth+1)
        right = Solution._dfs(board, i, j + 1, word, depth+1)
        left = Solution._dfs(board, i, j - 1, word, depth+1)
        board[i][j] = c
        return any[down, up, right, left]
