"""
Databricks OA

Problem:
Given two integer strings a and b, compute their sums at each slot starting from the right and return it as a string
Eg:
a="30918", b="58331" -> "881249"
a="11111", b="9" -> "111110"
a="12", b="5850" -> "5862"
a="1", b="1" -> "2"
"""

class Solution:
    def sum_number_strings(self, a: str, b: str) -> str:
        lstr = max(a, b, key=len)
        sstr = a if lstr is b else b
        sol = list(lstr[:len(lstr)-len(sstr)])
        i = len(lstr)-len(sstr)
        j = 0
        while i < len(lstr) and j < len(sstr):
            a, b = int(lstr[i]), int(sstr[j])
            sol.append(str(a+b))
            i += 1
            j += 1
        return ''.join(sol)

f = Solution().sum_number_strings

assert f("30918", "58331") == "881249"
assert f("11111", "9") == "111110"
assert f("12", "5850") == "5862"
assert f("1", "1") == "2"
assert f("0", "0") == "0"
