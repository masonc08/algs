"""
Leetcode 17
Runtime: 32 ms, faster than 51.40% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Letter Combinations of a Phone Number.
"""


class Solution:
    MP = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        sol, cur = [], [None]*len(digits)
        def dfs(depth):
            if depth == len(digits):
                sol.append(''.join(cur))
                return
            num = int(digits[depth])
            for c in self.MP[num]:
                cur[depth] = c
                dfs(depth+1)

        dfs(0)
        return sol
