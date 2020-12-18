"""
Leetcode 287
Runtime: 64 ms, faster than 68.08% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 16.6 MB, less than 46.63% of Python3 online submissions for Find the Duplicate Number.
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow1, slow2 = 0, slow
        while slow1 != slow2:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
        return slow1

    # def findDuplicate(self, nums: List[int]) -> int:
    #     l = len(nums)
    #     xor = 0
    #     for num in nums:
    #         xor ^= num
    #     for num in range(1, l+1):
    #         xor ^= num
    #     csum = l*(l+1)//2
    #     for num in nums:
    #         csum -= num
    #     offset = csum
    #     for num in nums:
    #         if num+offset > 0 and num^(num+offset) == xor:
    #             return num
    #     raise Exception()