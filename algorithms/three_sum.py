"""
Leetcode 15
Runtime: 792 ms, faster than 73.13% of Python3 online submissions for 3Sum.
Memory Usage: 17.4 MB, less than 35.05% of Python3 online submissions for 3Sum.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        for i in range(len(nums)-2):
            v = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            s, e = i+1, len(nums)-1
            while s < e:
                ttl = v + nums[s] + nums[e]
                if ttl > 0:
                    e -= 1
                elif ttl < 0:
                    s += 1
                else:
                    sol.append([v, nums[s], nums[e]])
                    while s<e and nums[s]==nums[s+1]:
                        s += 1
                    while s<e and nums[e]==nums[e-1]:
                        e -= 1
                    s += 1
                    e -= 1
        return sol