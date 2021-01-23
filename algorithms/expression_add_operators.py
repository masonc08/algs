"""
Leetcode 282
O(n4^n) runtime, O(4^n) space
Runtime: 668 ms, faster than 85.65% of Python3 online submissions for Expression Add Operators.
Memory Usage: 15 MB, less than 15.86% of Python3 online submissions for Expression Add Operators.
"""


class Solution:
    def addOperators(self, num: str, target: int):
        if not num:
            return []
        cur, sol = [], []
        def helper(ttl, i, bundle):
            if i == len(num):
                ttl == target and sol.append(''.join(cur))
                return
            n = 0
            for j in range(i, len(num)):
                if n == 0 and i != j:
                    break
                n = n*10+int(num[j])
                cur.append(f"+{n}")
                helper(ttl+n, j+1, n)
                cur[-1] = f"-{n}"
                helper(ttl-n, j+1, -n)
                cur[-1] = f"*{n}"
                helper(ttl-bundle+bundle*n, j+1, bundle*n)
                cur.pop()
        n = 0
        for i in range(len(num)):
            if n == 0 and i != 0:
                break
            n = n*10+int(num[i])
            cur.append(str(n))
            helper(n, i+1, n)
            cur.pop()
        return sol
