"""
Leetcode 55
Runtime: 88 ms, faster than 72.66% of Python3 online submissions for Jump Game.
Memory Usage: 17.8 MB, less than 99.99% of Python3 online submissions for Jump Game.
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastEscapable = len(nums) - 1
        for i, v in reversed(list(enumerate(nums))):
            if i+v >= lastEscapable:
                lastEscapable = i
        return lastEscapable == 0
