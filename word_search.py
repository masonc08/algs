# Leetcode 79


class Solution:
    def exist(self, board, word):
        word_map = {}
        for c in word:
            word_map[c] = word_map.get(c, 0) + 1
        for i in range(len(word)):
            for j in range(len(word[0])):
                _word_map = word_map.copy()
                Solution._dfs(board, i, j, set(), _word_map)
                if len(_word_map == 0):
                    return True
        return False

    @staticmethod
    def _dfs(board, i, j, visited, word_map):
        if i == len(board) or \
                j == len(board[0]) or \
                (i, j) in visited or \
                board[i][j] not in word_map:
            return
        visited.add((i, j))
        c = board[i][j]
        word_map[c] -= 1
        if word_map[c] == 0:
            del word_map[c]
        Solution._dfs(board, i + 1, j, visited, word_map)
        Solution._dfs(board, i - 1, j, visited, word_map)
        Solution._dfs(board, i, j + 1, visited, word_map)
        Solution._dfs(board, i, j - 1, visited, word_map)

