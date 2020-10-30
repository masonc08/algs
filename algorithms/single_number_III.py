"""
Leetcode 260
Runtime: 60 ms, faster than 63.63% of Python3 online submissions for Single Number III.
Memory Usage: 15.7 MB, less than 72.58% of Python3 online submissions for Single Number III.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        last_bit = xor_sum&(-xor_sum)
        sol = [0, 0]
        for num in nums:
            if num & last_bit == 0:
                sol[0] ^= num
            else:
                sol[1] ^= num
        return sol