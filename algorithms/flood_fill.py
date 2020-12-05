"""
Leetcode 733
Runtime: 80 ms, faster than 15.13% of Python3 online submissions for Flood Fill.
Memory Usage: 14.4 MB, less than 19.37% of Python3 online submissions for Flood Fill.
"""


class Solution:
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        colour = image[sr][sc]
        stk = [(sr, sc)]
        while stk:
            y, x = stk.pop()
            if x < 0 or x >= len(image[0]) or y < 0 or y >= len(image) or image[y][x] != colour or image[y][x] == newColor:
                continue
            image[y][x] = newColor
            for y1, x1 in self.dirs:
                stk.append((y+y1, x+x1))
        return image
