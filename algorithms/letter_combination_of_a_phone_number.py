"""
Leetcode 17
Runtime: 32 ms, faster than 51.40% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Letter Combinations of a Phone Number.
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mp = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        sol = []
        self._dfs(digits, 0, mp, [], sol)
        return sol


    def _dfs(self, digits, depth, mp, li, sol):
        if depth == len(digits):
            sol.append(''.join(li))
            return
        num = int(digits[depth])
        for c in mp[num]:
            li.append(c)
            self._dfs(digits, depth+1, mp, li, sol)
            li.pop()
