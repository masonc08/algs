class RabinKarp:
    salt = 101

    def search(self, s, pattern):
        if len(pattern) > len(s):
            return False
        target, cur, initial_match = 0, 0, True
        for i, c in enumerate(pattern):
            if initial_match and s[i] != c:
                initial_match = False
            target += ord(c)*self.salt**i
            cur += ord(s[i])*self.salt**i
        if initial_match:
            return True
        i = 1
        j = i+len(pattern)-1
        while j < len(s):
            cur -= ord(s[i-1])
            cur //= self.salt
            cur += ord(s[j])*self.salt**(j-i)
            if cur == target and self._compare(s, pattern, i, j):
                return True
            i += 1
            j += 1
        return False

    def _compare(self, s, pattern, i, j):
        a = 0
        while i <= j:
            if pattern[a] != s[i]:
                return False
            a += 1
            i += 1
        return True

f = RabinKarp().search

assert f("aaab", "aab")
assert f("abbdasbdabb", "dasbd")
assert f('ababcabcabababd', 'ababd')
assert not f('ababcabcabababd', 'ababf')
assert f('', '')
assert f('abcdef', '')