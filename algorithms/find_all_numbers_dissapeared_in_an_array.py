"""
Leetcode 448
"""


class Solution:

    """
    Marking negative as occupied
    Runtime: 364 ms, faster than 42.64% of Python3 online submissions for Find All Numbers Disappeared in an Array.
    Memory Usage: 22 MB, less than 65.36% of Python3 online submissions for Find All Numbers Disappeared in an Array.
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            num = abs(num)
            nums[num-1] = -abs(nums[num-1])
        return [ i+1 for i, v in enumerate(nums) if v > 0 ]

    """
    By swapping
    Runtime: 424 ms, faster than 5.60% of Python3 online submissions for Find All Numbers Disappeared in an Array.
    Memory Usage: 21.9 MB, less than 81.77% of Python3 online submissions for Find All Numbers Disappeared in an Array.
    """
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     for i in range(len(nums)):
    #         while nums[i] != i+1:
    #             v = nums[i]
    #             other = nums[v-1]
    #             if v == other:
    #                 break
    #             nums[i], nums[v-1] = other, v
    #     sol = []
    #     for i, v in enumerate(nums):
    #         if i != v-1:
    #             sol.append(i+1)
    #     return sol
