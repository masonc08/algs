"""
Leetcode 1723
Leetcode weekly contest 223
"""


import functools


"""
O(k^n) runtime, O(n) space
Runtime: 264 ms, faster than 100.00% of Python3 online submissions for Find Minimum Time to Finish All Jobs.
Memory Usage: 27.1 MB, less than 20.00% of Python3 online submissions for Find Minimum Time to Finish All Jobs.
"""
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        times = [0]*k
        self.sol = float('inf')
        @functools.lru_cache(None)
        def assign(i, t):
            maxt = max(t)
            if i == len(jobs):
                self.sol = min(self.sol, maxt)
                return
            if maxt >= self.sol:
                return
            times = list(t)
            for j in range(k):
                times[j] += jobs[i]
                assign(i+1, tuple(sorted(times)))
                times[j] -= jobs[i]
        assign(0, tuple(times))
        return self.sol
