"""
Leetcode 303
Runtime: 76 ms, faster than 75.20% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 17.7 MB, less than 14.43% of Python3 online submissions for Range Sum Query - Immutable.
"""


class NumArray:

    def __init__(self, nums: List[int]):
        self.cache = [None]*len(nums)
        self.nums = nums
        for i in range(len(nums)):
            x = self.cache[i-1] if i != 0 else 0
            self.cache[i] = self.nums[i]+x

    def sumRange(self, i: int, j: int) -> int:
        x = self.cache[i-1] if i != 0 else 0
        return self.cache[j]-x


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)