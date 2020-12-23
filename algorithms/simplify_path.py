"""
Leetcode 71
Runtime: 24 ms, faster than 97.29% of Python3 online submissions for Simplify Path.
Memory Usage: 14.2 MB, less than 83.59% of Python3 online submissions for Simplify Path.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        sol = ['']
        for token in path:
            if token == '' or token == '.':
                continue
            elif token == '..':
                if sol[-1] != '':
                    sol.pop()
            else:
                sol.append(token)
        return '/'.join(sol) if len(sol) != 1 else '/'
