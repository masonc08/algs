"""
Leetcode 137
"""

"""
Constant space, one pass
Runtime: 60 ms, faster than 50.68% of Python3 online submissions for Single Number II.
Memory Usage: 15.6 MB, less than 67.73% of Python3 online submissions for Single Number II.
"""
class Solution:
    def singleNumber(self, nums) -> int:
        first, second = 0, 0
        for n in nums:
            remove = first & second & n
            first &= ~remove
            second &= ~remove
            n &= ~remove
            second |= first & n
            first |= n
        return first


"""
Linear space, two pass
Runtime: 56 ms, faster than 73.29% of Python3 online submissions for Single Number II.
Memory Usage: 15.7 MB, less than 67.73% of Python3 online submissions for Single Number II.
"""
# import collections


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         occ = collections.defaultdict(int)
#         for num in nums:
#             occ[num] += 1
#         return min(list(occ.items()), key=lambda x: x[1])[0]
