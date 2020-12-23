"""
Leetcode 456
Runtime: 96 ms, faster than 31.61% of Python3 online submissions for 132 Pattern.
Memory Usage: 15.2 MB, less than 49.82% of Python3 online submissions for 132 Pattern.
"""


import collections


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mins = [0]*len(nums)
        mins[0] = nums[0]
        for i, n in enumerate(nums):
            if i == 0:
                continue
            mins[i] = min(mins[i-1], n)
        stk = []
        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            while stk and stk[-1] < n:
                if stk[-1] > mins[i]:
                    return True
                stk.pop()
            stk += n,
        return False



    # def find132pattern(self, nums: List[int]) -> bool:
    #     dp = [0]*len(nums)
    #     dp[0] = float('inf')
    #     ll = collections.deque()
    #     def find(i, n):
    #         for i in range(i+1):
    #             if dp[i] < n < A[i]:
    #                 return True
    #         return False

    #     for i in range(1, len(nums)):
    #         dp[i] = min(dp[i-1], n)
    #     for i in range(len(nums)-1, -1, -1):
    #         n = nums[i]
        
    #     while ll and ll[-1] < dp[i]:
    #         ll.pop()
    #     if ll and n > ll[0]:
    #         return True
    #     ll.append(n)
    #     return False
                     
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         mins =[nums[0]]
#         for i in range(1, len(nums)):
#             mins.append(min(mins[-1], nums[i]))
#         stack = []
#         for i in range(len(nums)-1, 0,-1):
#             if nums[i] > mins[i]:
#                 while stack and stack[-1] <= mins[i - 1]:
#                     stack.pop()
#                 if nums[i] > mins[i - 1]:
#                     if stack and stack[-1] < nums[i]: return True
#                 stack.append(nums[i])       
#         return False
      