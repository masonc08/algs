"""
Leetcode 739
Runtime: 520 ms, faster than 45.24% of Python3 online submissions for Daily Temperatures.
Memory Usage: 18.7 MB, less than 58.31% of Python3 online submissions for Daily Temperatures.
"""


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        L = len(T)
        stk = [L-1]
        sol = [0]*L
        for i in range(L-1, -1, -1):
            v = T[i]
            while stk and T[stk[-1]] <= v:
                stk.pop()
            if stk:
                sol[i] = stk[-1]-i
            stk += i,
        return sol
