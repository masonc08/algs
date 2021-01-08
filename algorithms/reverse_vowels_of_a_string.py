"""
Leetcode 345
Runtime: 76 ms, faster than 18.68% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 14.9 MB, less than 80.84% of Python3 online submissions for Reverse Vowels of a String.
"""


class Solution:
    VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    def reverseVowels(self, s: str) -> str:
        sol = list(s)
        i, j = 0, len(s)-1
        while i < j:
            while i < j and s[i] not in self.VOWELS:
                i += 1
            while i < j and s[j] not in self.VOWELS:
                j -= 1
            if i < j:
                sol[i], sol[j] = sol[j], sol[i]
            i, j = i+1, j-1
        return ''.join(sol)
