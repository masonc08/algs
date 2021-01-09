"""
https://cdn.discordapp.com/attachments/321084536308105217/797288391984545802/unknown.png
https://cdn.discordapp.com/attachments/321084536308105217/797288437723037736/unknown.png
"""


class Solution:
    def unal_wheel(self, wheel_size, num, k):
        k %= wheel_size
        kp = wheel_size-k
        mask = (1<<kp)-1
        cp = num&mask
        num >>= kp
        cp <<= k
        num |= cp
        return num

f = Solution().unal_wheel

assert f(8, 1, 1) == 2
assert f(8, 13, 5) == 161
assert f(8, 17, 12) == 17
