"""
Leetcode 66
Runtime: 32 ms, faster than 61.40% of Python3 online submissions for Plus One.
Memory Usage: 14.2 MB, less than 48.62% of Python3 online submissions for Plus One.
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            carry = (digits[i]//10)
            if carry == 0:
                return digits
            digits[i] %= 10
        return [1]+digits
