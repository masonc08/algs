# WIP

def longest_substring(s1, s2):
  sstr = if (len(s1) <= len(s2)) s1 else s2
  lstr = if (len(s2) > len(s1)) s2 else s1
  j = 0
  longest = 0
  while i < len(lstr):
    k = 0
    tmp = 0
    for j in enumerate(len(sstr)):
      if sstr[j] != lstr[i+j]:
        longest = max(longest, tmp)
        break
      if i+j == len(sstr) - 1:
        tmp += 1
        longest = max(longest, tmp)
        break
      if j != 0 and sstr[k] == lstr[i+j]:
        k += 1
      tmp += 1
    i += 1