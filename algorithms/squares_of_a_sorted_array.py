"""
Leetcode 977
December Leetcoding challenge
Runtime: 248 ms, faster than 23.51% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.3 MB, less than 6.91% of Python3 online submissions for Squares of a Sorted Array.
"""


from bisect import bisect_left


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = bisect_left(nums, 0)
        i, j = i-1, i
        sol = [0]*len(nums)
        ptr = 0
        while i >= 0 or j < len(nums):
            if i != -1 and (j == len(nums) or abs(nums[i]) < abs(nums[j])):
                sol[ptr] = nums[i]*nums[i]
                i -= 1
            else:
                sol[ptr] = nums[j]*nums[j]
                j += 1
            ptr += 1
        return sol