"""
Leetcode 937
O(nlogn) runtime, O(n) space
Runtime: 52 ms, faster than 7.19% of Python3 online submissions for Reorder Data in Log Files.
Memory Usage: 14.6 MB, less than 10.75% of Python3 online submissions for Reorder Data in Log Files.
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        A, B = [], []
        for log in logs:
            if log.split()[1].isnumeric():
                B.append(log)
            else:
                A.append(log)
        A.sort(key=lambda x: (x[x.find(' ')+1:], x[:x.find(' ')]))
        return A + B
