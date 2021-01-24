"""
Leetcode 616
O(WNN) runtime, O(N) space, where W=words.length, N=s.length
Runtime: 48 ms, faster than 94.30% of Python3 online submissions for Add Bold Tag in String.
Memory Usage: 14.7 MB, less than 63.25% of Python3 online submissions for Add Bold Tag in String.
"""


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bolded = [False]*len(s)
        for w in words:
            Lw = len(w)
            i = s.find(w)
            while i != -1:
                bolded[i:i+Lw] = [True]*Lw
                i = s.find(w, i+1)
        sol = []
        for i in range(len(s)+1):
            if i == len(s):
                if bolded[-1]:
                    sol.append('</b>')
            elif i == 0:
                if bolded[0]:
                    sol.append('<b>')
                sol.append(s[i])
            elif bolded[i] and not bolded[i-1]:
                sol.append('<b>')
                sol.append(s[i])
            elif not bolded[i] and bolded[i-1]:
                sol.append('</b>')
                sol.append(s[i])
            else:
                sol.append(s[i])
        return ''.join(sol)
