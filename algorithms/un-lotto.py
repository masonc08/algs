"""
https://cdn.discordapp.com/attachments/321084536308105217/797229048757354538/unknown.png
https://cdn.discordapp.com/attachments/321084536308105217/797229122866511873/unknown.png
https://cdn.discordapp.com/attachments/321084536308105217/797230318029373470/unknown.png
"""


from typing import List


class Solution:
    def unLotto(self, m: int, n: int, s: str, P: List[float]) -> int:
        dp = [1]*(m+1)
        for i in range(n-1, -1, -1):
            size = n-i
            c = s[i]
            new = [0]*(m-size+1)
            p = P[ord(c)-ord('a')]
            for j in range(m-size, -1, -1):
                if j != m-size:
                    a, b = p*dp[j+1], new[j+1]
                    new[j] = a+b-a*b
                else:
                    new[j] = p*dp[j+1]
            dp, new = new, [0]*m
        return dp[0]

P = [0.5, 0.5] + [0]*24
print(Solution().unLotto(5, 3, "aaa", P))
