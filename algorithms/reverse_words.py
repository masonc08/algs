"""
Leetcode 151
Runtime: 32 ms, faster than 63.02% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 14.2 MB, less than 22.69% of Python3 online submissions for Reverse Words in a String.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        i = len(s) - 1
        sol = []
        collected = []
        while i >= 0:
            if s[i] == ' ':
                if collected:
                    collected.reverse()
                    sol.append(''.join(collected))
                    collected = []
            else:
                collected.append(s[i])
            i -= 1
        if collected:
            collected.reverse()
            sol.append(''.join(collected))
        return ' '.join(sol)


"""
kekw
Runtime: 24 ms, faster than 95.13% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 14.2 MB, less than 22.69% of Python3 online submissions for Reverse Words in a String.
"""
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return ' '.join(list(reversed(s.split())))