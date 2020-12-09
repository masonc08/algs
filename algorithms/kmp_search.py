def generate_table(needle):
    table = [0]*len(needle)
    i, j = 0, 1
    while j < len(needle):
        if needle[j] == needle[i]:
            i += 1
            table[j] = i
            j += 1
        elif i == 0:
            j += 1
        else:
            i = table[i-1]
    return table
            

def kmp_search(haystack, needle):
    if len(haystack) < len(needle):
        return False
    if len(needle) == 0:
        return True
    table = generate_table(needle)
    i, j = 0, 0
    while j < len(haystack):
        c = haystack[j]
        if c == needle[i]:
            i += 1
            j += 1
        elif i != 0:
            i = table[i-1]
        else:
            j += 1
        if i >= len(needle):
            return j-len(needle)
    return -1
