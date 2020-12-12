"""
Leetcode 1664
Leetcode weekly contest 216
Runtime: 1248 ms, faster than 100.00% of Python3 online submissions for Ways to Make a Fair Array.
Memory Usage: 21.3 MB, less than 33.33% of Python3 online submissions for Ways to Make a Fair Array.
"""


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        losum, lesum, rosum, resum = 0, 0, 0, 0
        for i in range(1, len(nums)):
            v = nums[i]
            if i%2 == 0:
                # if even with nothing removed
                rosum += v
            else:
                # if odd with nothing removed
                resum += v
        sol = 0
        if (losum + rosum) == (lesum + resum):
            sol += 1
        for i in range(1, len(nums)):
            v = nums[i]
            if i%2 == 0:
                # if even with nothing removed
                losum += nums[i-1]
                rosum -= v
            else:
                # if odd with nothing removed
                lesum += nums[i-1]
                resum -= v
            if (losum + rosum) == (lesum + resum):
                sol += 1
        return sol
