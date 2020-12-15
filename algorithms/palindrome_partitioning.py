"""
Leetcode 131
December Leetcoding challenge
Runtime: 720 ms, faster than 5.54% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 30.5 MB, less than 5.29% of Python3 online submissions for Palindrome Partitioning.
"""


import collections


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol = []
        cur = []
        def helper(l=0, r=len(s)-1):
            if l == len(s):
                sol.append(cur.copy())
                return
            for i in range(l, r+1):
                a = b = i
                while a >= l and b < r+1 and s[a] == s[b]:
                    a -= 1
                    b += 1
                if a == l-1:
                    cur.append(s[l:b])
                    helper(b, len(s)-1)
                    cur.pop()
                a, b = i, i+1
                while a >= l and b < r+1 and s[a] == s[b]:
                    a -= 1
                    b += 1
                if a == l-1:
                    cur.append(s[l:b])
                    helper(b, len(s)-1)
                    cur.pop()
        
        helper()
        return sol
