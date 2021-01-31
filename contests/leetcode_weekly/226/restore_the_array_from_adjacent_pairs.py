"""
Leetcode 1743
Leetcode weekly contest 226
O(n) runtime and space
Runtime: 1108 ms, faster than 66.67% of Python3 online submissions for Restore the Array From Adjacent Pairs.
Memory Usage: 73.2 MB, less than 66.67% of Python3 online submissions for Restore the Array From Adjacent Pairs.
"""


import collections


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj_li = collections.defaultdict(set)
        for u, v in adjacentPairs:
            adj_li[u].add(v)
            adj_li[v].add(u)
        sol = []
        leaf = None
        for k in adj_li:
            if len(adj_li[k]) == 1:
                leaf = k
                break
        while 1:
            sol.append(leaf)
            if not adj_li[leaf]:
                return sol
            parent = adj_li[leaf].pop()
            adj_li[parent].remove(leaf)
            leaf = parent