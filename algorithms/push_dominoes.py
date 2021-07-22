"""
Leetcode 838
July Leetcoding challenge
O(n) runtime and space, O(1) space if using cpp or any other language supporting mutable strings
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        sol, last, L = list(dominoes), -1, len(dominoes)
        for i, v in enumerate(dominoes):
            if v == '.':
                if i == L-1 and last != -1 and dominoes[last] == 'R':
                    sol[last+1:i+1] = ['R']*(i-last)
            elif v == 'L':
                if last == -1 or dominoes[last] == 'L':
                    sol[last+1:i] = ['L']*(i-last-1)
                elif dominoes[last] == 'R':
                    diff = i-last-1
                    sol[last+1:i] = ['R']*(diff//2) + ['.']*(diff%2) + ['L']*(diff//2)
                last = i
            elif v == 'R':
                if last != -1 and dominoes[last] == 'R':
                    sol[last+1:i] = ['R']*(i-last-1)
                last = i
        return ''.join(sol)
