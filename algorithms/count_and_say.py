"""
Leetcode 38
Runtime: 36 ms, faster than 82.59% of Python3 online submissions for Count and Say.
Memory Usage: 14.5 MB, less than 10.93% of Python3 online submissions for Count and Say.
"""


class Solution:
    cache = { 1: "1" }

    def countAndSay(self, n: int) -> str:
        if n in self.cache:
            return self.cache[n]
        s = self.countAndSay(n-1)
        sol = []
        i = 0
        c = 0
        while i < len(s):
            c += 1
            if i == len(s)-1 or s[i] != s[i+1]:
                sol.append(str(c))
                sol.append(s[i])
                c = 0
            i += 1
        sol = ''.join(sol)
        self.cache[n] = sol
        return sol
