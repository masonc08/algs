"""
Leetcode 1718
Leetcode biweekly contest 43
O(n^n) runtime, O(n) space
Brute force DFS
Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Construct the Lexicographically Largest Valid Sequence.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Construct the Lexicographically Largest Valid Sequence.
"""


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        sol, used = [0]*(2*n-1), [False]*(n+1)
        L = len(sol)
        def dfs(i):
            if i == L:
                return True
            for j in range(n, 0, -1):
                if used[j] or j != 1 and (i+j >= L or sol[i+j] != 0):
                    continue
                sol[i], used[j], next_avail = j, True, i+1
                if j != 1:
                    sol[i+j] = j
                while next_avail != L and sol[next_avail] != 0:
                    next_avail += 1
                if dfs(next_avail):
                    return True
                else:
                    used[j] = False
                    if j != L:
                        sol[i+j] = 0 if j != 1 else sol[i+j]
            sol[i] = 0
            return False
        dfs(0)
        return sol
