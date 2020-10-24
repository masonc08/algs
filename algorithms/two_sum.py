"""
Leetcode 1
Runtime: 48 ms, faster than 79.03% of Python3 online submissions for Two Sum.
Memory Usage: 15.3 MB, less than 16.39% of Python3 online submissions for Two Sum.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(nums):
            compl = target - num
            if compl in mp:
                return [i, mp[compl]]
            mp[num] = i
        raise Exception()