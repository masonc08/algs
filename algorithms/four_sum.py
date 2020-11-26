"""
Leetcode 18
"""


class Solution:
    """
    O(n^3) runtime, O(n) space solution, using expanded 3Sum solution
    Runtime: 992 ms, faster than 38.58% of Python3 online submissions for 4Sum.
    Memory Usage: 14.5 MB, less than 13.79% of Python3 online submissions for 4Sum.
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        sol = []
        for i in range(len(nums)-3):
            v = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                s, e = j+1, len(nums)-1
                while s < e:
                    ttl = v + nums[j] + nums[s] + nums[e]
                    if ttl > target:
                        e -= 1
                    elif ttl < target:
                        s += 1
                    else:
                        sol.append([v, nums[j], nums[s], nums[e]])
                        while s<e and nums[s]==nums[s+1]:
                            s += 1
                        while s<e and nums[e]==nums[e-1]:
                            e -= 1
                        s += 1
                        e -= 1
        return sol
