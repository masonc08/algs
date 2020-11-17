"""
Leetcode 238
"""


class Solution:
    """
    2 pass solution, O(n) runtime, O(n) space not including given and solution arrays
    Runtime: 212 ms, faster than 68.19% of Python3 online submissions for Product of Array Except Self.
    Memory Usage: 21.1 MB, less than 35.46% of Python3 online submissions for Product of Array Except Self.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr = [0]*len(nums)
        ltr[0] = 1
        for i in range(1, len(nums)):
            ltr[i] = ltr[i-1]*nums[i-1]
        prod = nums[-1]
        for i in reversed(range(len(nums)-1)):
            ltr[i] *= prod
            prod *= nums[i]
        return ltr

    """
    3 pass solution, O(n) runtime and space
    Runtime: 244 ms, faster than 22.21% of Python3 online submissions for Product of Array Except Self.
    Memory Usage: 21.1 MB, less than 32.21% of Python3 online submissions for Product of Array Except Self.
    """
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     ltr, rtl = [0]*len(nums), [0]*len(nums)
    #     ltr[0], rtl[-1] = 1, 1
    #     for i in range(1, len(nums)):
    #         ltr[i] = ltr[i-1]*nums[i-1]
    #     for i in reversed(range(len(nums)-1)):
    #         rtl[i] = rtl[i+1]*nums[i+1]
    #     for i in range(len(nums)):
    #         nums[i] = ltr[i]*rtl[i]
    #     return nums
