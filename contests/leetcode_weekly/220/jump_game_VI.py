"""
Leetcode 1696
Leetcode weekly contest 220
June Leetcoding challenge
Runtime: 1136 ms, faster than 50.00% of Python3 online submissions for Jump Game VI.
Memory Usage: 28.2 MB, less than 100.00% of Python3 online submissions for Jump Game VI.
"""


import collections


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q = collections.deque()
        for i, v in enumerate(nums):
            cur = v + q[0][0] if len(q) != 0 else v
            if len(q) != 0 and i-q[0][1]+1 > k:
                q.popleft()
            while len(q) != 0 and q[-1][0] < cur:
                q.pop()
            q.append((cur, i))
        return q[-1][0]



# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         i = j = len(nums)-1
#         ll = collections.deque()
#         while i >= 0:
#             if ll:
#                 nums[i] += ll[0]
#             while ll and ll[-1] < nums[i]:
#                 ll.pop()
#             ll.append(nums[i])
#             if j-i == k:
#                 if ll and ll[0] == nums[j]:
#                     ll.popleft()
#                 j -= 1
#             i -= 1
#         return nums[0]
