"""
Leetcode 216
Runtime: 32 ms, faster than 66.71% of Python3 online submissions for Combination Sum III.
Memory Usage: 14.1 MB, less than 21.83% of Python3 online submissions for Combination Sum III.
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.sol, self.cur = [], []
        self.k = k
        self.n = n
        for i in range(1, 10):
            if i > n:
                break
            self.cur.append(i)
            self._combinationSum3(i, i, 1)
            self.cur.pop()
        return self.sol

    def _combinationSum3(self, start, ttl, cnt):
        if cnt == self.k:
            if ttl == self.n:
                self.sol.append(self.cur.copy())
            return
        for i in range(start+1, 10):
            if ttl+i > self.n:
                break
            self.cur.append(i)
            self._combinationSum3(i, ttl+i, cnt+1)
            self.cur.pop()
