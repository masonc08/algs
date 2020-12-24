"""
Leetcode 93
Runtime: 32 ms, faster than 81.09% of Python3 online submissions for Restore IP Addresses.
Memory Usage: 14.5 MB, less than 5.68% of Python3 online submissions for Restore IP Addresses.
"""


from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        L = len(s)
        sol, cur = [], []
        def helper(start, d):
            if d == 0 and start == L:
                sol.append('.'.join(cur))
                return
            if L-start > d*3 or L-start < d:
                return
            for i in range(start+1, min(start+4, L+1)):
                segment = s[start:i]
                if i != start+1 and int(s[start]) == 0:
                    return
                if i-start != 3 or int(segment) <= 255:
                    cur.append(segment)
                    helper(i, d-1)
                    cur.pop()
        helper(0, 4)
        return sol
