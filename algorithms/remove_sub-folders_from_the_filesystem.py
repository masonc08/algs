"""
Leetcode 1233
Runtime: 228 ms, faster than 71.26% of Python3 online submissions for Remove Sub-Folders from the Filesystem.
Memory Usage: 30.1 MB, less than 63.29% of Python3 online submissions for Remove Sub-Folders from the Filesystem.
"""


class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort()
        sol = []
        for folder in folders:
            if not sol:
                sol += folder,
            else:
                a, b = folder.split('/'), sol[-1].split('/')
                L = len(b)
                if a[:L] != b:
                    sol += folder,
        return sol
