"""
Leetcode 84
December Leetcoding challenge
Runtime: 112 ms, faster than 27.98% of Python3 online submissions for Largest Rectangle in Histogram.
Memory Usage: 17 MB, less than 21.79% of Python3 online submissions for Largest Rectangle in Histogram.
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        L = len(heights)
        if L == 0:
            return 0
        cache = [1]*L
        stkf, stkb = [], []
        for i in range(L+1):
            j = L-1-i
            a = heights[i] if i < L else float('-inf')
            b = heights[j] if j >= 0 else float('-inf')
            while stkf and heights[stkf[-1]] > a:
                prev = stkf.pop()
                cache[prev] += i-prev-1
            while stkb and heights[stkb[-1]] > b:
                prev = stkb.pop()
                cache[prev] += prev-j-1
            if i < L:
                stkf += i,
                stkb += j,
        return max(amt*v for amt, v in zip(cache, heights))
