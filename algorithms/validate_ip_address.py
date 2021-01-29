"""
Leetcode 468
Runtime: 24 ms, faster than 94.22% of Python3 online submissions for Validate IP Address.
Memory Usage: 14.5 MB, less than 15.15% of Python3 online submissions for Validate IP Address.
"""


class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.validate_ipv4(IP):
            return 'IPv4'
        if self.validate_ipv6(IP):
            return 'IPv6'
        return 'Neither'

    def validate_ipv4(self, s):
        try:
            segs = s.split('.')
            assert len(segs) == 4
            for seg in segs:
                assert seg.isnumeric()
                n = int(seg)
                assert str(n) == seg
                assert 0 <= n <= 255
        except AssertionError:
            return False
        return True

    def validate_ipv6(self, s):
        try:
            segs = s.split(':')
            assert len(segs) == 8
            for seg in segs:
                assert 1 <= len(seg) <= 4
                assert all(c.isnumeric() or 'a' <= c.lower() <= 'f' for c in seg)
        except AssertionError:
            return False
        return True
