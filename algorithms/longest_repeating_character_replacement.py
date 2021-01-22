"""
Leetcode 424
"""


import collections


"""
O(n) runtime, O(1) space
Runtime: 152 ms, faster than 40.44% of Python3 online submissions for Longest Repeating Character Replacement.
Memory Usage: 14.3 MB, less than 58.27% of Python3 online submissions for Longest Repeating Character Replacement.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ct, i, sol = [0]*26, 0, 0
        for j, c in enumerate(s):
            ct[ord(c)-ord('A')] += 1
            most, size = max(ct), j-i+1
            if size-most > k:
                ct[ord(s[i])-ord('A')] -= 1
                i += 1
            sol = max(sol, j-i+1)
        return sol

"""
Runtime: 160 ms, faster than 35.90% of Python3 online submissions for Longest Repeating Character Replacement.
Memory Usage: 14.4 MB, less than 9.79% of Python3 online submissions for Longest Repeating Character Replacement.
"""
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         i = j = sol = 0
#         ct = collections.Counter()
#         while j < len(s):
#             v = s[j]
#             ct[v] += 1
#             most = max(ct.values())
#             if j-i+1-most > k:
#                 ct[s[i]] -= 1
#                 i += 1
#             sol = max(j-i+1, sol)
#             j += 1
#         return sol
