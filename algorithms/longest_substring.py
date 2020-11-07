# Given two strings, find the length of the longest substring that exists in both strings

class Solution:
    def longest_substring(self, s1: str, s2: str) -> int:
        pattern = min(s1, s2, key=len)
        s = s1 if pattern is s2 else s2
        table = self._gen_table(pattern)
        i, j = 0, 0
        sol = 0
        while i < len(s) and j < len(pattern):
            if s[i] == pattern[j]:
                j += 1
                i += 1
            else:
                sol = max(sol, j)
                if j == 0:
                    i += 1
                else:
                    j = table[j-1]
        return max(sol, j)
        

    def _gen_table(self, s: str) -> list:
        if len(s) == 0:
            return []
        sol = [0]*len(s)
        i, j = 0, 1
        while j < len(s):
            if s[i] != s[j]:
                sol[j] = 0
                i = 0
            else:
                sol[j] = i+1
                i += 1
            j += 1
        return sol

f = Solution().longest_substring

assert f("mississipi", "issip") == 5
assert f("aple", "pineapple") == 2
assert f("grep", "") == 0
