"""
Wayfair OA

We are given the maximum occurances of 'a', 'b' and 'c' in a string.
We need to make the largest length string containing only 'a', 'b' and 'c'
such that no three consecutive characters are same.

Ex:
Input: a=3 b=3 c=3
Output: "abcabcabc" (There can be a lot of different outputs)
Input: a=5 b=5 c=3
Output: "aabbcaabbcabc"
"""

class Solution:
    def longest_string_no_three_consecutive(self, a: int, b: int, c: int) -> int:
        li = [['a', a], ['b', b], ['c', c]]
        li.sort(key= lambda x: -x[1])
        sol = []
        while 1:
            last = sol[-1] if len(sol) != 0 else ''
            use = li[0] if li[0][0] != last else li[1]
            other = li[1] if use == li[0] else li[0]
            if use[1] == 0:
                break
            if use[1]-other[1] >= 2:
                sol.append(use[0])
                sol.append(use[0])
                use[1] -= 2
            else:
                sol.append(use[0])
                use[1] -= 1
            li.sort(key= lambda x: -x[1])
        return ''.join(sol)

f = Solution().longest_string_no_three_consecutive

assert f(7, 3, 3) == "aabaacacababc"
assert f(300000, 3, 3) == "aabaacaacaabaabaacaa"
assert f(1, 1, 1) == "abc"
assert f(0, 0, 0) == ""
assert f(10, 10, 10) == "abcbcacababcbcacababcbcacababc"
