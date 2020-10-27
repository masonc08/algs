"""
Leetcode 414
"""

"""
1 pass
Runtime: 52 ms, faster than 70.50% of Python3 online submissions for Third Maximum Number.
Memory Usage: 14.7 MB, less than 91.31% of Python3 online submissions for Third Maximum Number.
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxes = []
        for num in nums:
            for i in range(3):
                if num not in maxes and (len(maxes) == i or num > maxes[i]):
                    if len(maxes) == 3:
                        maxes.pop()
                    maxes.insert(i, num)
                    break
        return maxes[-1] if len(maxes) == 3 else maxes[0]

"""
3 pass
Runtime: 52 ms, faster than 70.50% of Python3 online submissions for Third Maximum Number.
Memory Usage: 14.8 MB, less than 91.31% of Python3 online submissions for Third Maximum Number.
"""
# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         largest = [max(nums)]
#         if len(nums) < 3:
#             return largest[0]
#         for _ in range(2):
#             l = float('-inf')
#             for n in nums:
#                 if n in largest:
#                     continue
#                 if n > l:
#                     l = n
#             if l == float('-inf'):
#                 return largest[0]
#             largest.append(l)
#         return largest[-1]
