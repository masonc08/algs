"""
Leetcode 609
O(n) runtime and space
Runtime: 88 ms, faster than 66.49% of Python3 online submissions for Find Duplicate File in System.
Memory Usage: 24.2 MB, less than 37.27% of Python3 online submissions for Find Duplicate File in System.
"""


import collections


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for s in paths:
            files = s.split()
            path, files = files[0], files[1:]
            for f in files:
                name, content = f.split('(')
                mp[content].append(f'{path}/{name}')
        return [v for v in mp.values() if len(v) >= 2]
