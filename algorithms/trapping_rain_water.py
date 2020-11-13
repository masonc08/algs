"""
Leetcode 42
Runtime: 56 ms, faster than 45.38% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 14.7 MB, less than 30.20% of Python3 online submissions for Trapping Rain Water.
"""



from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        cache = [0]*len(height)
        cache[0], cache[-1] = height[0], height[-1]
        for i in range(1, len(height)-1):
            if height[i] > cache[i-1]:
                cache[i] = height[i]
            else:
                cache[i] = cache[i-1]
        sol = 0
        for i in reversed(range(1, len(height)-1)):
            if cache[i+1] > height[i]:
                tmp = cache[i+1]
            else:
                tmp = height[i]
            sol += (min(tmp, cache[i])-height[i])
            cache[i] = tmp
        return sol
