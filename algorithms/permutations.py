"""
Leetcode 46
Runtime: 44 ms, faster than 34.05% of Python3 online submissions for Permutations.
Memory Usage: 14.2 MB, less than 91.91% of Python3 online submissions for Permutations.
"""


class Solution:
    @staticmethod
    def permute(nums):
        sol = []
        Solution.helper(sol, nums, [None]*len(nums))
        return sol

    @staticmethod
    def helper(sol, nums, frag=[None]*3, depth=0):
        if depth == len(nums):
            return sol.append(frag.copy())
        for i, v in enumerate(nums):
            if v is None:
                continue
            nums[i] = None
            frag[depth] = v
            Solution.helper(sol, nums, frag, depth + 1)
            frag[depth] = None
            nums[i] = v
