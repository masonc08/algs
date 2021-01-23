"""
Leetcode 1733
Leetcode biweekly contst 44
O(M*N) runtime and space
Runtime: 1340 ms, faster than 100.00% of Python3 online submissions for Minimum Number of People to Teach.
Memory Usage: 27.4 MB, less than 100.00% of Python3 online submissions for Minimum Number of People to Teach.
"""


from collections import Counter


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = list(map(set, languages))
        cant_speak = set()
        for a, b in friendships:
            if languages[a-1] & languages[b-1]:
                continue
            cant_speak.add(a), cant_speak.add(b)
        ct = Counter()
        for p in cant_speak:
            for l in languages[p]:
                ct[l] += 1
        return len(cant_speak)-max(ct.values()) if cant_speak else 0