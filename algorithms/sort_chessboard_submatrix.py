"""
Databricks OA

Given...
- A matrix A of integers representing a chess board, 
- A list of queries Q, in format of [i, j, w] representing a submatrix starting at (i, j), spanning w tiles right and w tiles down.
process through each query by sorting the black and white tiles in each submatrix in ascending order, and return the newly semi-sorted matrix.
Eg: 
A = [             Q = [                 [
  [1, 4, 3, 2],     [0, 1, 3],    ->      [1, 1, 1, 2],
  [8, 4, 7, 1],     [1, 0, 2]     ->      [5, 8, 4, 3],
  [1, 5, 2, 1]    ]               ->      [1, 2, 4, 7]
]                                       ]
Explanation:
The query [0, 1, 3] is first processed, on a subarray starting at index [0, 1], spanning 3 tiles right and 3 tiles down.
This leaves us with the following matrix:
[
  [1, 1, 1, 2],
  [8, 2, 4, 3],
  [1, 5, 4, 7]
]
Next, the query [1, 0, 2] is processed, on a subarray starting at index [1, 0], spanning 2 tiles right and 2 tiles down.
This leaves us with the following matrix:
[
  [1, 1, 1, 2],
  [5, 1, 4, 3],
  [2, 8, 4, 7]
]
Since we have processed our last query, we return the pointer to the original matrix, which we have now finished sorting in-place.
Picture: https://i.imgur.com/TQzbcCh.png
"""

from typing import List
from heapq import heappush, heappop


class Solution:
    def sort_chessboard_submatrix(self, chessboard: List[List[int]], queries: List[List[int]]) -> List[List[int]]:
        for query in queries:
            start = (query[0], query[1])
            w = query[2]
            i = start[0]
            black_start = True
            blacks, whites = [], []
            while i < start[0]+w:
                j = start[1]
                black_tile = black_start
                while j < start[1]+w:
                    if black_tile:
                        heappush(blacks, chessboard[i][j])
                    else:
                        heappush(whites, chessboard[i][j])
                    black_tile = not black_tile
                    j += 1
                black_start = not black_start
                i += 1
            black_start = True
            i = start[0]
            while i < start[0]+w:
                j = start[1]
                black_tile = black_start
                while j < start[1]+w:
                    if black_tile:
                        chessboard[i][j] = heappop(blacks)
                    else:
                        chessboard[i][j] = heappop(whites)
                    black_tile = not black_tile
                    j += 1
                black_start = not black_start
                i += 1
        return chessboard

f = Solution().sort_chessboard_submatrix

assert f([
    [1, 4, 3, 2],
    [8, 4, 7, 1],
    [1, 5, 2, 1]
], [[0, 1, 3], [1, 0, 2]]) == \
    [
        [1, 1, 1, 2],
        [5, 1, 4, 3],
        [2, 8, 4, 7]
    ]
assert f([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
], [[0, 0, 3]]) == \
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
