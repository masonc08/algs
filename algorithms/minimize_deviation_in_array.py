"""
Leetcode 1675
O(NlogMlogN) runtime, O(N) space, M=max(N)
January Leetcoding challenge
Runtime: 900 ms, faster than 88.38% of Python3 online submissions for Minimize Deviation in Array.
Memory Usage: 30.7 MB, less than 29.29% of Python3 online submissions for Minimize Deviation in Array.
"""


import heapq


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        hp = [(n/(n&-n), n) for n in nums]
        heapq.heapify(hp)
        sol, mx = float('inf'), max(hp, key=lambda x: x[0])[0]
        while len(hp) == len(nums):
            n0, n1 = heapq.heappop(hp)
            sol = min(sol, mx-n0)
            if n0 % 2 == 1 or n0 < n1:
                mx = max(mx, n0*2)
                heapq.heappush(hp, (n0*2, n1))
        return int(sol)
