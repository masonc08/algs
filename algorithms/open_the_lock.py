"""
Leetcode 752
Runtime: 648 ms, faster than 45.65% of Python3 online submissions for Open the Lock.
Memory Usage: 15.5 MB, less than 56.63% of Python3 online submissions for Open the Lock.
"""


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        waves = 0
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        visited = set(['0000'])
        stk = ['0000']
        while stk:
            new = []
            while stk:
                cur = stk.pop()
                for nbr in self.get_nbrs(cur):
                    if nbr in visited or nbr in deadends:
                        continue
                    if nbr == target:
                        return waves+1
                    visited.add(nbr)
                    new += nbr,
            stk = new
            waves += 1
        return -1

    def get_nbrs(self, num):
        num = list(num)
        for i in range(4):
            for offset in {-1, 1}:
                num[i] = str((int(num[i])+offset)%10)
                yield ''.join(num)
                num[i] = str((int(num[i])-offset)%10)
