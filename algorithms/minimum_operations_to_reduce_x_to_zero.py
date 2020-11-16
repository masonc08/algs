"""
Leetcode 1658
Leetcode weekly contest 215
"""


import math
from typing import List


class Solution:
    """
    Runtime: 1144 ms, faster than 50.00% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
    Memory Usage: 35.8 MB, less than 50.00% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
    """
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums)-x
        if target == 0:
            return len(nums)
        sol = -math.inf
        cur = 0
        mp = { 0: -1 }
        for i, num in enumerate(nums):
            cur += num
            if cur-target in mp:
                sol = max(sol, i-mp[cur-target])
            mp[cur] = i
        return -1 if sol == -math.inf else len(nums)-sol

    """
    DFS attempt
    """
    # def minOperations(self, nums: List[int], x: int) -> int:
    #     cache = {}
    #     su = sum(nums)
    #     if su < x:
    #         return -1
    #     if su == x:
    #         return len(nums)
    #     def _minOperations(i, j, count, cur):
    #         if cur == x:
    #             return count
    #         if i == j or cur > x:
    #             return -1
    #         if cur+nums[i] > x and cur+nums[j] > x:
    #             return -1
    #         decisions = sorted([('i', nums[i]), ('j', nums[j])], key=lambda x: x[1])
    #         # If i has the higher one
    #         if decisions[1][0] == 'i':
    #             if (i+1, j, count+1, cur+decisions[1][1]) in cache:
    #                 sol = cache[(i+1, j, count+1, cur+decisions[1][1])]
    #             else:
    #                 sol = _minOperations(i+1, j, count+1, cur+decisions[1][1])
    #                 cache[(i+1, j, count+1, cur+decisions[1][1])] = sol
    #             if sol != -1:
    #                 return sol
    #             if (i, j-1, count+1, cur+decisions[0][1]) in cache:
    #                 sol = cache[(i, j-1, count+1, cur+decisions[0][1])]
    #             else:
    #                 sol = _minOperations(i, j-1, count+1, cur+decisions[0][1])
    #                 cache[(i, j-1, count+1, cur+decisions[0][1])] = sol
    #             if sol != -1:
    #                 return sol
    #         else:
    #             if (i, j-1, count+1, cur+decisions[1][1]) in cache:
    #                 sol = cache[(i, j-1, count+1, cur+decisions[1][1])]
    #             else:
    #                 sol = _minOperations(i, j-1, count+1, cur+decisions[1][1])
    #                 cache[(i, j-1, count+1, cur+decisions[1][1])] = sol
    #             if sol != -1:
    #                 return sol
    #             if (i+1, j, count+1, cur+decisions[0][1]) in cache:
    #                 sol = cache[(i+1, j, count+1, cur+decisions[0][1])]
    #             else:
    #                 sol = _minOperations(i+1, j, count+1, cur+decisions[0][1])
    #                 cache[(i+1, j, count+1, cur+decisions[0][1])] = sol
    #             if sol != -1:
    #                 return sol
    #         return -1
    #     return _minOperations(0, len(nums)-1, 0, 0)

print(Solution().minOperations([5207,5594,477,6938,8010,7606,2356,6349,3970,751,5997,6114,9903,3859,6900,7722,2378,1996,8902,228,4461,90,7321,7893,4879,9987,1146,8177,1073,7254,5088,402,4266,6443,3084,1403,5357,2565,3470,3639,9468,8932,3119,5839,8008,2712,2735,825,4236,3703,2711,530,9630,1521,2174,5027,4833,3483,445,8300,3194,8784,279,3097,1491,9864,4992,6164,2043,5364,9192,9649,9944,7230,7224,585,3722,5628,4833,8379,3967,5649,2554,5828,4331,3547,7847,5433,3394,4968,9983,3540,9224,6216,9665,8070,31,3555,4198,2626,9553,9724,4503,1951,9980,3975,6025,8928,2952,911,3674,6620,3745,6548,4985,5206,5777,1908,6029,2322,2626,2188,5639], 
565610))