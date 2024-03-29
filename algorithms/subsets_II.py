"""
Leetcode 90
"""


class Solution:
    def subsetswithdup(self, nums: list[int]) -> list[list[int]]:
        cur, sol = [], []
        nums.sort()
        L = len(nums)
        def explore(i=0, chose_prev=False):
            if i == L:
                sol.append(cur.copy())
                return
            explore(i+1, False)
            if i > 0 and nums[i] == nums[i-1] and not chose_prev:
                return
            cur.append(nums[i])
            explore(i+1, True)
            cur.pop()
        explore()
        return sol
 

    """
    Recursive solution
    Runtime: 28 ms, faster than 97.52% of Python3 online submissions for Subsets II.
    Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Subsets II.
    """
    # def subsetswithdup(self, nums: list[int]) -> list[list[int]]:
    #     nums.sort()
    #     sol, cur = [], []
    #     def _subsetsWithDup(i=0):
    #         sol.append(cur.copy())
    #         for j in range(i, len(nums)):
    #             v = nums[j]
    #             if j > i and nums[j-1] == v:
    #                 continue
    #             cur.append(v)
    #             _subsetsWithDup(j+1)
    #             cur.pop()
    #     _subsetsWithDup()
    #     return sol

    """
    Iterative solution
    Runtime: 36 ms, faster than 73.75% of Python3 online submissions for Subsets II.
    Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Subsets II.
    """
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     sol = [[]]
    #     prev = 0
    #     for i in range(len(nums)):
    #         num = nums[i]
    #         new = []
    #         start = prev if i != 0 and num == nums[i-1] else 0
    #         prev = len(sol)
    #         for j in range(start, len(sol)):
    #             subset = sol[j]
    #             tmp = subset.copy()
    #             tmp.append(num)
    #             new.append(tmp)
    #         sol += new
    #     return sol
