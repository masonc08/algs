"""
Leetcode 421
Runtime: 364 ms, faster than 66.78% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
Memory Usage: 16.1 MB, less than 84.54% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
"""


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        sol = mask = 0
        for i in range(31, -1, -1):
            mask |= (1<<i)
            prefixes = set()
            for num in nums:
                prefixes.add(num&mask)
            cur = sol|(1<<i)
            for prefix in prefixes:
                if cur^prefix in prefixes:
                    sol = cur
                    break
        return sol
