class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = sum(1 for c in s if c in ('a', 'e', 'i', 'o', 'u'))
        letters = sum(1 for c in s if c.isalpha())
        consts = letters - vowels
        return vowels/consts if consts>0 else 0