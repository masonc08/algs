"""
Leetcode 605
Runtime: 164 ms, faster than 71.12% of Python3 online submissions for Can Place Flowers.
Memory Usage: 14.5 MB, less than 47.95% of Python3 online submissions for Can Place Flowers.
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while n > 0 and i < len(flowerbed):
            plot = flowerbed[i]
            if plot == 0 and (i-1 == -1 or flowerbed[i-1] == 0) and (i+1 == len(flowerbed) or flowerbed[i+1] == 0):
                n -= 1
                i += 2
            else:
                i += 1
        return n == 0
