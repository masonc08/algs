"""
Leetcode 128
Runtime: 52 ms, faster than 79.04% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 15.4 MB, less than 26.99% of Python3 online submissions for Longest Consecutive Sequence.
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        sol = 0
        for num in nums:
            if num in s:
                s.remove(num)
                cur = 1
                i = num
                while i-1 in s:
                    i -= 1
                    s.remove(i)
                    cur += 1
                i = num
                while i+1 in s:
                    i += 1
                    s.remove(i)
                    cur += 1
                sol = max(sol, cur)
        return sol  
