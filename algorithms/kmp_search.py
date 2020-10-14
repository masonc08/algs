def generate_table(s):
    if len(s) == 0:
        return []
    sol = [(s[0], 0)]
    i = 0
    j = 1
    while j < len(s):
        if s[i] == s[j]:
            sol.append((s[j], i+1))
            i += 1
            j += 1
        else:
            sol.append((s[j], 0))
            i = 0
            j += 1
    return sol
            

def kmp_search(s, pattern):
    if len(s) < len(pattern):
        return False
    if len(pattern) == 0:
        return True
    table = generate_table(pattern)
    i = 0
    j = -1
    while i < len(s):
        if j == len(pattern) - 1:
            return True
        elif s[i] == table[j+1][0]:
            i += 1
            j += 1
        elif j != -1:
            j = table[j][1] - 1
        else:
            i += 1
    return j == len(pattern) - 1

assert kmp_search('ababcabcabababd', 'ababd')
assert not kmp_search('ababcabcabababd', 'ababf')
assert kmp_search('', '')
assert kmp_search('abcdef', '')
