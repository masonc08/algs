"""
Leetcode 1701
Leetcode biweekly contest 42
Runtime: 928 ms, faster than 66.67% of Python3 online submissions for Average Waiting Time.
Memory Usage: 55.1 MB, less than 33.33% of Python3 online submissions for Average Waiting Time.
"""


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        sol = cur = 0
        N = len(customers)
        for s, t in customers:
            cur = max(cur, s)
            ttl = t
            if cur > s:
                ttl += cur-s
            sol += ttl/N
            cur += t
        return sol
