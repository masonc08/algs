"""
Leetcode 16
Runtime: 264 ms, faster than 27.84% of Python3 online submissions for 3Sum Closest.
Memory Usage: 14.1 MB, less than 65.78% of Python3 online submissions for 3Sum Closest.
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sol = -0x7fffffff-1
        nums.sort()
        for i in range(len(nums)-2):
            a = nums[i]
            s, e = i+1, len(nums)-1
            while s < e:
                b, c = nums[s], nums[e]
                ttl = a + b + c
                sol = min(sol, ttl, key=lambda x: abs(x-target))
                if ttl > target:
                    e -= 1
                elif ttl < target:
                    s += 1
                else:
                    return ttl
        return sol
