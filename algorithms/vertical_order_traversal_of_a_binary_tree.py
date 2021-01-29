"""
Leetcode 987
O(n) runtime and space
January Leetcoding challenge
Runtime: 32 ms, faster than 80.48% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
Memory Usage: 14.6 MB, less than 65.43% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
"""


import collections


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        mp = collections.defaultdict(list)
        q = collections.deque(((0, root),))
        while q:
            newq, newmp = collections.deque(), collections.defaultdict(list)
            while q:
                col, node = q.popleft()
                if node:
                    newmp[col].append(node.val)
                    newq.append((col-1, node.left)), newq.append((col+1, node.right))
            q = newq
            for k in newmp:
                mp[k] += sorted(newmp[k])
        sol = [None]*len(mp)
        mn = min(mp, default=0)
        mx = mn+len(mp)-1
        for i in range(mn, mx+1):
            sol[i-mn] = mp[i]
        return sol
