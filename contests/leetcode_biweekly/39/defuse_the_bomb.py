"""
Leetcode 1652
Leetcode biweekly contest 39
Runtime: 40 ms, faster than 50.00% of Python3 online submissions for Defuse the Bomb.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Defuse the Bomb.
"""


class Solution:
    def _wrap(self, i, A):
        if i == -1:
            return len(A)-1
        if i == len(A):
            return 0
        return i

    def decrypt(self, code: List[int], k: int) -> List[int]:
        sol = [0]*len(code)
        if k == 0:
            return sol
        i = 0
        j = 1 if k>0 else len(code)-1
        for _ in range(0, abs(k)):
            sol[i] += code[self._wrap(j, code)]
            j = self._wrap(j+1 if k>0 else j-1, code)
        if k<0:
            j = self._wrap(j+1, code)
        for i in range(1, len(sol)):
            sol[i] = sol[i-1]-code[i]+code[j] if k>0 else sol[i-1]+code[i-1]-code[j]
            j = self._wrap(j+1, code)
        return sol
