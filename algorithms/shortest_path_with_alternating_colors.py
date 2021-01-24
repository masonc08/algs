"""
Leetcode 1129
O(M+N) runtime and space
Runtime: 88 ms, faster than 63.67% of Python3 online submissions for Shortest Path with Alternating Colors.
Memory Usage: 14.6 MB, less than 59.80% of Python3 online submissions for Shortest Path with Alternating Colors.
"""


class Solution:
    def shortestAlternatingPaths(self, n: int, R: List[List[int]], B: List[List[int]]) -> List[int]:
        rli, bli, sol = [[] for _ in range(n)], [[] for _ in range(n)], [float('inf')]*n
        for u, v in R:
            rli[u].append(v)
        for u, v in B:
            bli[u].append(v)
        sol[0] = 0
        for i in {-1, 1}: # 1 is entering node from a blue node
            rseen, bseen, old = [i<0]+[False]*(n-1), [i>0]+[False]*(n-1), [0]
            while old:
                new = []
                while old:
                    node = old.pop()
                    nbrs = rli[node] if i > 0 else bli[node]
                    seen = rseen if i > 0 else bseen
                    for nbr in nbrs:
                        if seen[nbr]:
                            continue
                        seen[nbr] = True
                        sol[nbr] = min(sol[nbr], abs(i))
                        new.append(nbr)
                old = new
                i = -i+1 if i < 0 else -i-1
        return list(map(lambda x: x if x != float('inf') else -1, sol))
