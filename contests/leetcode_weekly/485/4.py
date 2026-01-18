import collections

class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        L = len(s)
        ct = collections.Counter(s)
        res = []
        i = 0
        while i < L:
            j = i
            c = s[i]
            while j < L and s[j] == c:
                j += 1
            different_c = s[j] if j != L else None
            amt_of_c = j-i
            i = j
            if different_c is None or ord(c) > ord(different_c):
                if ct[c] > 1:
                    amt_to_remove = min(ct[c] - 1, amt_of_c)
                    ct[c] -= amt_of_c
                    remaining_c = amt_of_c - amt_to_remove
                    res.extend(list(c*remaining_c))
                else:
                    res.extend(list(c*amt_of_c))
            else:
                res.extend(list(c*amt_of_c))
        for i in range(len(res)-1, -1, -1):
            c = res[i]
            if ct[c] > 1:
                ct[c] -= 1
                res.pop()
        return "".join(res)

        # for i in range(L):
        #     c = s[i]
        #     if i == L-1 and ct[c] >= 2:
        #         continue
        #     if ct[c] < 2:
        #         res.append(c)
        #         continue
        #     if ord(c) > ord(s[i+1]):
        #         del ct[c]
        #         continue
        #     res.append(c)
        # return "".join(res)
    
