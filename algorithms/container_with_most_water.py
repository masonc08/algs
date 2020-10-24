"""
Leetcode 11
Runtime: 160 ms, faster than 42.38% of Python3 online submissions for Container With Most Water.
Memory Usage: 16.2 MB, less than 55.17% of Python3 online submissions for Container With Most Water.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        marea = (j-i)*min(height[i], height[j])
        while i != j:
            lowest = min(height[i], height[j])
            new = (j-i)*lowest
            marea = new if new > marea else marea
            if lowest == height[i]:
                i += 1
            else:
                j -= 1
        return marea
