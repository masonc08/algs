import copy


class Solution:
    """
    O(mn) runtime, O(1) space through caching in another bit
    Runtime: 28 ms, faster than 90.58% of Python3 online submissions for Game of Life.
    Memory Usage: 14.1 MB, less than 68.58% of Python3 online submissions for Game of Life.
    """
    def gameOfLife(self, board: List[List[int]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                n = board[i-1][j]&1 if i != 0 else 0
                s = board[i+1][j]&1 if i+1 != len(board) else 0
                w = board[i][j-1]&1 if j != 0 else 0
                e = board[i][j+1]&1 if j+1 != len(board[0]) else 0
                nw = board[i-1][j-1]&1 if i != 0 and j != 0 else 0
                ne = board[i-1][j+1]&1 if i != 0 and j+1 != len(board[0]) else 0
                sw = board[i+1][j-1]&1 if i+1 != len(board) and j != 0 else 0
                se = board[i+1][j+1]&1 if i+1 != len(board) and j+1 != len(board[0]) else 0
                ttl = sum([n, s, w, e, nw, ne, sw, se])
                v = board[i][j]&1
                if v == 0:
                    if ttl == 3:
                        board[i][j] |= 0b10
                    else:
                        board[i][j] |= 0b00
                else:
                    if ttl < 2 or ttl > 3:
                        board[i][j] |= 0b00
                    else:
                        board[i][j] |= 0b10
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1


    """
    O(mn) runtime and space
    Runtime: 32 ms, faster than 71.11% of Python3 online submissions for Game of Life.
    Memory Usage: 14.1 MB, less than 68.58% of Python3 online submissions for Game of Life.
    """
    # def gameOfLife(self, board: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     ref = copy.deepcopy(board)
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             n = ref[i-1][j] if i != 0 else 0
    #             s = ref[i+1][j] if i+1 != len(ref) else 0
    #             w = ref[i][j-1] if j != 0 else 0
    #             e = ref[i][j+1] if j+1 != len(ref[0]) else 0
    #             nw = ref[i-1][j-1] if i != 0 and j != 0 else 0
    #             ne = ref[i-1][j+1] if i != 0 and j+1 != len(ref[0]) else 0
    #             sw = ref[i+1][j-1] if i+1 != len(ref) and j != 0 else 0
    #             se = ref[i+1][j+1] if i+1 != len(ref) and j+1 != len(ref[0]) else 0
    #             ttl = sum([n, s, w, e, nw, ne, sw, se])
    #             v = ref[i][j]
    #             if v == 0:
    #                 if ttl == 3:
    #                     board[i][j] = 1
    #             else:
    #                 if ttl < 2 or ttl > 3:
    #                     board[i][j] = 0
