"""
Leetcode 1345
December Leetcoding challenge
Runtime: 564 ms, faster than 61.42% of Python3 online submissions for Jump Game IV.
Memory Usage: 35.8 MB, less than 9.48% of Python3 online submissions for Jump Game IV.
"""


import collections


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        L = len(arr)
        locs = collections.defaultdict(set)
        for i, n in enumerate(arr):
            locs[n].add(i)
        stk = [0]
        seen = set(stk)
        steps = 0
        while stk:
            new = []
            while stk:
                node = stk.pop()
                v = arr[node]
                if node == L-1:
                    return steps
                for i in locs[v]:
                    if i not in seen:
                        new += i,
                        seen.add(i)
                locs[v].clear()
                if node != 0 and node-1 not in seen:
                    new += node-1,
                    seen.add(node-1)
                if node != L-1 and node+1 not in seen:
                    new += node+1,
                    seen.add(node+1)
            steps += 1
            stk = new
        return -1 
