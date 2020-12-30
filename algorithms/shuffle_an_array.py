"""
Leetcode 384

"""


import random

"""
O(n) runtime and space by Fisher-Yates algorithm
Runtime: 332 ms, faster than 34.04% of Python3 online submissions for Shuffle an Array.
Memory Usage: 19.6 MB, less than 18.54% of Python3 online submissions for Shuffle an Array.
"""
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums.copy()
        self.cur = nums
        self.L = len(self.cur)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.cur
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(self.L):
            swp = random.randrange(i, self.L)
            self.cur[i], self.cur[swp] = self.cur[swp], self.cur[i]
        return self.cur
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

"""
Built-in
Runtime: 260 ms, faster than 92.02% of Python3 online submissions for Shuffle an Array.
Memory Usage: 19.5 MB, less than 44.37% of Python3 online submissions for Shuffle an Array.
"""
# class Solution:

#     def __init__(self, nums: List[int]):
#         self.li = nums
#         self.origi = nums.copy()

#     def reset(self) -> List[int]:
#         """
#         Resets the array to its original configuration and return it.
#         """
#         return self.origi
        

#     def shuffle(self) -> List[int]:
#         """
#         Returns a random shuffling of the array.
#         """
#         random.shuffle(self.li)
#         return self.li
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
