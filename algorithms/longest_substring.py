# TODO: WIP
# Given two strings, find the length of the longest substring that exists in both strings

def longest_substring(s1, s2):
    ss = s1 if len(s1) < len(s2) else s2
    ls = s1 if len(s1) >= len(s2) else s2
    table = [0]*len(ss)
    # Make table
    i = 0
    j = 1
    while j < len(s):
        if ss[j] != ss[i]:
            i = 0
        else:
            i += 1
            table[j] = i
        j += 1
    largest = float('-inf')
    cur = 0
    i = 0
    j = -1
    while i < len(ls):
        if ls[i] == table[j+1]:
            i += 1
            j += 1
            cur += 1
        else:
            j = table[j] - 1
            cur = j