"""
Leetcode 152
Runtime: 52 ms, faster than 80.43% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 14.3 MB, less than 79.47% of Python3 online submissions for Maximum Product Subarray.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sol = float('-inf')
        min_neg, cur = float('inf'), 1
        for num in nums:
            if num == 0:
                min_neg, cur = float('inf'), 1
                sol = max(sol, 0)
            else:
                cur *= num
                if cur < 0:
                    sol = max(sol, -cur//min_neg if min_neg != float('inf') else cur)
                    min_neg = min(min_neg, -cur)
                else:
                    sol = max(sol, cur)
        return sol
